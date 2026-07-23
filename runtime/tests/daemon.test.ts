import { request as httpRequest } from "node:http";
import { chmod, mkdir, mkdtemp, readFile, stat, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { afterEach, describe, expect, it } from "vitest";
import type { OmlxControlPort, UIEvent } from "@chirality/runtime-contracts";
import {
  AuthRegistry,
  EngineRegistry,
  ProjectRegistry,
  ResidencyCoordinator,
  RuntimeService,
  SessionStore,
  TurnCoordinator,
  atomicWriteJson
} from "@chirality/runtime-core";
import { RuntimeDaemon } from "@chirality/runtime-daemon";
import { createProjectFixture } from "./helpers.js";

const active: RuntimeDaemon[] = [];
afterEach(async () => {
  await Promise.all(active.splice(0).map(async (daemon) => daemon.stop().catch(() => undefined)));
});

function request(
  socketPath: string,
  path: string,
  token?: string,
  method = "GET",
  body?: unknown
): Promise<{ status: number; body: string }> {
  return new Promise((resolve, reject) => {
    const encoded = body === undefined ? undefined : JSON.stringify(body);
    const outgoing = httpRequest(
      {
        socketPath,
        path,
        method,
        headers: {
          ...(token === undefined ? {} : { authorization: `Bearer ${token}` }),
          ...(encoded === undefined
            ? {}
            : {
                "content-type": "application/json",
                "content-length": Buffer.byteLength(encoded)
              })
        }
      },
      (response) => {
        const chunks: Buffer[] = [];
        response.on("data", (chunk) => chunks.push(Buffer.from(chunk)));
        response.on("end", () =>
          resolve({
            status: response.statusCode ?? 0,
            body: Buffer.concat(chunks).toString("utf8")
          })
        );
      }
    );
    outgoing.once("error", reject);
    if (encoded !== undefined) outgoing.write(encoded);
    outgoing.end();
  });
}

async function fixture(root: string) {
  const runtime = join(root, "runtime");
  const projects = new ProjectRegistry(runtime);
  const sessions = new SessionStore(runtime, projects);
  const engines = new EngineRegistry();
  const control: OmlxControlPort = {
    async listStatus() {
      return [];
    },
    async load() {},
    async unload() {}
  };
  const residency = new ResidencyCoordinator(control, runtime);
  const auth = new AuthRegistry(runtime);
  const credentials = {
    async get() {
      return undefined;
    },
    async status() {
      return { configured: false };
    },
    async set() {},
    async remove() {}
  };
  const turns = new TurnCoordinator(projects, sessions, engines, residency);
  const runner = {
    async *run(): AsyncIterable<UIEvent> {
      yield { type: "chat:delta", data: { text: "hello" } };
      yield { type: "process:exit", data: { exitCode: 0 } };
    }
  };
  const service = new RuntimeService(
    projects,
    sessions,
    engines,
    residency,
    turns,
    auth,
    credentials,
    undefined,
    runner
  );
  return { runtime, service };
}

describe("Unix-domain runtime daemon", () => {
  it("uses private files, authenticates, and preserves UIEvent SSE wire format", async () => {
    const root = await mkdtemp(join(tmpdir(), "chirality-daemon-"));
    const { runtime, service } = await fixture(root);
    const socketPath = join(runtime, "control.sock");
    const daemon = new RuntimeDaemon({ runtimeDirectory: runtime, socketPath, service });
    active.push(daemon);
    const started = await daemon.start();
    expect((await stat(runtime)).mode & 0o777).toBe(0o700);
    expect((await stat(socketPath)).mode & 0o777).toBe(0o600);
    expect((await stat(`${socketPath}.owner.json`)).mode & 0o777).toBe(0o600);
    expect((await request(socketPath, "/v1/health")).status).toBe(401);
    const operator = (await readFile(started.operatorTokenFile, "utf8")).trim();
    const health = await request(socketPath, "/v1/health", operator);
    expect(health.status).toBe(200);
    expect(JSON.parse(health.body)).toMatchObject({ apiVersion: "v1", status: "ok" });

    const projectRoot = join(root, "project");
    const { manifestPath } = await createProjectFixture(projectRoot, "daemon-project");
    const registered = await service.registerProject(manifestPath, "test", "D-TEST");
    const projectToken = (await readFile(registered.tokenFile, "utf8")).trim();
    const stream = await request(
      socketPath,
      "/v1/projects/daemon-project/runs",
      projectToken,
      "POST",
      { brief: "test", approvalReference: "D-TEST" }
    );
    expect(stream.status).toBe(200);
    expect(stream.body).toContain("event: chat:delta\ndata: {\"text\":\"hello\"}\n\n");
    expect(stream.body).not.toContain("\"type\":\"chat:delta\"");
  });

  it("fails closed for a non-socket or ambiguous live owner record", async () => {
    const root = await mkdtemp(join(tmpdir(), "chirality-daemon-stale-"));
    const first = await fixture(root);
    const socketPath = join(first.runtime, "control.sock");
    await mkdir(first.runtime, { recursive: true });
    await writeFile(socketPath, "not a socket", "utf8");
    const daemon = new RuntimeDaemon({
      runtimeDirectory: first.runtime,
      socketPath,
      service: first.service
    });
    await expect(daemon.start()).rejects.toMatchObject({ code: "FORBIDDEN" });

    const root2 = await mkdtemp(join(tmpdir(), "chirality-daemon-owner-"));
    const second = await fixture(root2);
    const socket2 = join(second.runtime, "control.sock");
    await atomicWriteJson(`${socket2}.owner.json`, {
      schemaVersion: "chirality.daemon-owner/v1",
      daemonId: "live",
      pid: process.pid,
      uid: process.getuid?.() ?? -1,
      socketPath: socket2,
      startedAt: new Date().toISOString()
    });
    await chmod(`${socket2}.owner.json`, 0o600);
    const daemon2 = new RuntimeDaemon({
      runtimeDirectory: second.runtime,
      socketPath: socket2,
      service: second.service
    });
    await expect(daemon2.start()).rejects.toMatchObject({ code: "FORBIDDEN" });
  });
});
