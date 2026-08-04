import { request as httpRequest } from "node:http";
import { mkdir, mkdtemp, readFile, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { expect, it } from "vitest";
import type { RuntimeService } from "@chirality/runtime-core";
import type { UIEvent } from "@chirality/runtime-contracts";
import { RuntimeDaemon } from "@chirality/runtime-daemon";

it("preserves a refused non-socket control path on start failure", async () => {
  const root = await mkdtemp(join(tmpdir(), "tm112-refute-owner-"));
  const runtime = join(root, "runtime");
  const socketPath = join(runtime, "control.sock");
  await mkdir(runtime, { recursive: true });
  await writeFile(socketPath, "foreign-control-path", "utf8");
  const daemon = new RuntimeDaemon({
    runtimeDirectory: runtime,
    socketPath,
    service: {} as RuntimeService
  });

  await expect(daemon.start()).rejects.toMatchObject({ code: "FORBIDDEN" });
  await expect(readFile(socketPath, "utf8")).resolves.toBe("foreign-control-path");
});

it("interrupts when Agent-1 identity appears in a later event before force", async () => {
  const root = await mkdtemp(join(tmpdir(), "tm112-refute-preid-"));
  const runtime = join(root, "runtime");
  const socketPath = join(runtime, "control.sock");
  const tokenFile = join(runtime, "operator.token");
  let releaseIdentity!: () => void;
  const identityReady = new Promise<void>((resolve) => {
    releaseIdentity = resolve;
  });
  const never = new Promise<void>(() => undefined);
  let interrupts = 0;
  const service = {
    auth: {
      async ensureClient() {
        await writeFile(tokenFile, "token\n", "utf8");
        return { tokenFile };
      },
      async authenticate() {
        return { clientId: "refuter" };
      }
    },
    runAgent1(): AsyncIterable<UIEvent> {
      return {
        async *[Symbol.asyncIterator]() {
          yield { type: "chat:delta", data: { text: "pre-identity" } };
          await identityReady;
          yield {
            type: "harness:event",
            data: {
              schemaVersion: 1,
              eventId: "identity-event",
              sessionId: "manager-session",
              timestamp: new Date().toISOString(),
              type: "session.created",
              data: {}
            }
          };
          await never;
        }
      };
    },
    async interruptSession() {
      interrupts += 1;
    }
  } as unknown as RuntimeService;
  const daemon = new RuntimeDaemon({ runtimeDirectory: runtime, socketPath, service });
  await daemon.start();

  const body = JSON.stringify({ brief: "refute", approvalReference: "REFUTE" });
  let firstChunkResolve!: () => void;
  const firstChunk = new Promise<void>((resolve) => {
    firstChunkResolve = resolve;
  });
  const outgoing = httpRequest(
    {
      socketPath,
      path: "/v1/projects/refute/runs",
      method: "POST",
      headers: {
        authorization: "Bearer token",
        "content-type": "application/json",
        "content-length": Buffer.byteLength(body)
      }
    },
    (response) => {
      response.once("data", firstChunkResolve);
      response.on("error", () => undefined);
    }
  );
  outgoing.on("error", () => undefined);
  outgoing.end(body);
  await firstChunk;

  const stopping = daemon.stop().then(
    () => ({ fulfilled: true, code: undefined }),
    (error: unknown) => ({
      fulfilled: false,
      code: (error as { code?: string }).code
    })
  );
  releaseIdentity();
  const result = await stopping;
  outgoing.destroy();

  expect(interrupts).toBe(1);
  expect(result).toEqual({ fulfilled: true, code: undefined });
});
