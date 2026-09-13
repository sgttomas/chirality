import { describe, expect, it } from "vitest";
import type { AgentEngineRunInput, HarnessEvent, UIEvent } from "@chirality/runtime-contracts";
import { createDelegatedEngineAdapter } from "@chirality/runtime-core";

describe("Native item notifications across the delegated adapter", () => {
  it("retains message/summary/checklist updates and actual child identity independently of completed collaboration calls", async () => {
    const scripted = [
      ["item/agentMessage/delta", { threadId: "parent", turnId: "native", itemId: "m", delta: "hello" }],
      ["item/reasoning/summaryPartAdded", { threadId: "parent", turnId: "native", itemId: "r", summaryIndex: 0 }],
      ["item/reasoning/summaryTextDelta", { threadId: "parent", turnId: "native", itemId: "r", summaryIndex: 0, delta: "Checking" }],
      ["turn/plan/updated", { threadId: "parent", turnId: "native", explanation: null, plan: [{ step: "Check", status: "inProgress" }] }],
      ["turn/plan/updated", { threadId: "parent", turnId: "native", explanation: null, plan: [{ step: "Check", status: "completed" }] }],
      ["item/completed", { threadId: "parent", turnId: "native", item: { type: "collabAgentToolCall", id: "spawn", tool: "spawnAgent", status: "completed", receiverThreadIds: ["child"], agentsStates: { child: { status: "running", message: null } } } }],
      ["turn/started", { threadId: "child", turn: { id: "child-turn", status: "inProgress" } }],
      ["item/completed", { threadId: "child", turnId: "child-turn", item: { type: "agentMessage", id: "cm", text: "Child result", phase: "final_answer" } }],
      ["turn/completed", { threadId: "child", turn: { id: "child-turn", status: "completed" } }]
    ] as const;
    const adapter = createDelegatedEngineAdapter({ selection: { adapterId: "codex", providerId: "openai", model: "test" }, delegated: {
      async turn(_project: string, request: { turnId: string }, _tools: unknown[], observer: { onProgress(event: unknown): void }) {
        observer.onProgress({ type: "started", providerThreadId: "parent", providerTurnId: "native" });
        for (const [method, params] of scripted) observer.onProgress({ type: "notification", providerThreadId: "parent", providerTurnId: "native", method, params, occurredAt: "now" });
        return { terminal: { outcome: "completed", turnId: request.turnId }, output: "", providerThreadId: "parent" };
      }
    } as never });
    const input: AgentEngineRunInput = { projectId: "p", session: { projectId: "p", projectRoot: "/tmp/project", sessionId: "s", role: "untyped", engineSelection: { adapterId: "codex", providerId: "openai", model: "test" } } as never,
      message: "hello", turnId: "runtime", opts: { model: "test", tools: [], maxTurns: 10, persona: "HELP_HUMAN", mode: "workspaceWrite" } };
    await adapter.preflight(input);
    const received: UIEvent[] = []; for await (const value of adapter.startTurn(input)) received.push(value);
    const events = received.filter((value): value is Extract<UIEvent,{type:"harness:event"}> => value.type === "harness:event").map(value => value.data);
    const native = events.filter(event => event.type === "codex.notification");
    expect(native.map(event => event.data.method)).toEqual(scripted.map(([method]) => method));
    expect(events.some(event => event.type === "subagent.completed")).toBe(false);
    expect(events).toContainEqual(expect.objectContaining({ type: "tool.completed", data: expect.objectContaining({ toolUseId: "spawn" }) }));
    expect(native.at(-1)?.data.codex).toMatchObject({ providerThreadId: "child", providerTurnId: "child-turn", isPrimaryThread: false });
    expect(native[0]?.data.codex).toMatchObject({ providerThreadId: "parent", providerTurnId: "native", isPrimaryThread: true });
    expect(native[5]?.data.params).toEqual(scripted[5][1]);
  });
});
