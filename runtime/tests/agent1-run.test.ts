import { mkdtemp, readFile, readdir, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { describe, expect, it } from "vitest";
import type {
  AgentEnginePort,
  OmlxControlPort,
  RuntimeToolDefinition,
  UIEvent
} from "@chirality/runtime-contracts";
import {
  EngineRegistry,
  GovernedAgent1RunCoordinator,
  ProjectRegistry,
  ResidencyCoordinator,
  SessionStore,
  TurnCoordinator
} from "@chirality/runtime-core";
import { createProjectFixture } from "./helpers.js";

async function setup(managerMode: "success" | "missing") {
  const root = await mkdtemp(join(tmpdir(), "chirality-agent1-"));
  const { manifestPath } = await createProjectFixture(root, "agent-pilot");
  await writeFile(join(root, "known.txt"), "known-value\n", "utf8");
  const runtime = join(root, "user-data", "runtime");
  const projects = new ProjectRegistry(runtime);
  await projects.register(manifestPath, {
    approvedBy: "test",
    approvalReference: "D-TEST"
  });
  const sessions = new SessionStore(runtime, projects);
  const control: OmlxControlPort = {
    async listStatus() {
      return [{ id: "qwen", kind: "llm", loaded: true, loading: false }];
    },
    async load() {},
    async unload() {}
  };
  const residency = new ResidencyCoordinator(control, runtime);
  await residency.activate("qwen", "D-TEST");
  const bindings = new Map<string, readonly RuntimeToolDefinition[]>();
  const engines = new EngineRegistry();
  const engine: AgentEnginePort = {
    descriptor: {
      adapterId: "pi",
      providerId: "omlx",
      capabilities: {
        credentials: true,
        tools: true,
        attachments: false,
        interruption: true,
        durableResume: false,
        compaction: true
      }
    },
    subject: "pi",
    async preflight() {},
    async *startTurn(input) {
      const tool = bindings.get(input.session.sessionId)?.[0];
      const result = tool === undefined ? "missing-tool" : await tool.execute({}, new AbortController().signal);
      yield {
        type: "session:init",
        data: {
          engineSessionId: `engine-${input.session.sessionId}`,
          adapterId: "pi",
          providerId: "omlx",
          model: input.opts.model
        }
      };
      yield { type: "chat:complete", data: { text: JSON.stringify(result) } };
      yield { type: "process:exit", data: { exitCode: 0 } };
    },
    async interrupt() {}
  };
  engines.register(engine);
  const turns = new TurnCoordinator(projects, sessions, engines, residency);
  const manager = {
    async *execute(
      _session: unknown,
      _request: unknown,
      hooks: {
        delegate(input: { sealedBrief: string }): Promise<{ childSessionId: string }>;
        review(input: {
          childSessionId: string;
          decision: "accepted";
          rationale: string;
        }): Promise<void>;
      }
    ): AsyncIterable<UIEvent> {
      if (managerMode === "success") {
        const child = await hooks.delegate({ sealedBrief: "Read the governed file." });
        await hooks.review({
          childSessionId: child.childSessionId,
          decision: "accepted",
          rationale: "The return contains the known value."
        });
      }
      yield { type: "chat:complete", data: { text: "manager-finished" } };
    }
  };
  const coordinator = new GovernedAgent1RunCoordinator({
    projects,
    sessions,
    turns,
    residency,
    manager,
    tools: {
      async bind(sessionId, tools) {
        bindings.set(sessionId, tools);
        return async () => {
          bindings.delete(sessionId);
        };
      }
    },
    async resolveManagerSelection() {
      return { adapterId: "stub", providerId: "stub", model: "manager" };
    }
  });
  return { coordinator, root };
}

describe("governed Agent 1 local-child pilot", () => {
  it("runs exactly one read-only Agent 2, records parentage/model epoch, and requires review", async () => {
    const { coordinator, root } = await setup("success");
    const events: UIEvent[] = [];
    for await (const event of coordinator.run("agent-pilot", {
      brief: "Delegate the file check and review it.",
      localModel: "qwen",
      agentId: "HELP_HUMAN",
      approvalReference: "D-TEST",
      readOnlyTool: { name: "read_file", relativePath: "known.txt" }
    })) {
      events.push(event);
    }
    expect(events.at(-1)).toMatchObject({ type: "process:exit", data: { exitCode: 0 } });
    const runRoots = await readdir(
      join(root, "execution", "_Coordination", "AgentRuns", "runtime")
    );
    const record = JSON.parse(
      await readFile(
        join(
          root,
          "execution",
          "_Coordination",
          "AgentRuns",
          "runtime",
          runRoots[0]!,
          "run.json"
        ),
        "utf8"
      )
    );
    expect(record).toMatchObject({
      status: "completed",
      child: {
        role: "agent2",
        selection: { adapterId: "pi", providerId: "omlx", model: "qwen" },
        permissions: ["read"],
        tool: "read_file"
      },
      review: { decision: "accepted" }
    });
  });

  it("fails with REQUIRED_DELEGATION_MISSING when the manager skips the child", async () => {
    const { coordinator } = await setup("missing");
    const events: UIEvent[] = [];
    for await (const event of coordinator.run("agent-pilot", {
      brief: "Must delegate.",
      localModel: "qwen",
      agentId: "HELP_HUMAN",
      approvalReference: "D-TEST",
      readOnlyTool: { name: "read_file", relativePath: "known.txt" }
    })) {
      events.push(event);
    }
    expect(events).toContainEqual(
      expect.objectContaining({
        type: "turn:error",
        data: expect.objectContaining({
          details: { runtimeCode: "REQUIRED_DELEGATION_MISSING" }
        })
      })
    );
    expect(events.at(-1)).toMatchObject({ type: "process:exit", data: { exitCode: 1 } });
  });
});
