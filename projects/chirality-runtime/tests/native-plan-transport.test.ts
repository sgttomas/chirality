import { describe, expect, it } from "vitest";
import { PassThrough } from "node:stream";
import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { realpathSync } from "node:fs";
import type { DelegatedHarnessProcessSupervisorPort, NativePlanClarificationAnswers, NativePlanClarificationPrompt, NativePlanTransportEvent, SupervisorNativePlanPort, SupervisorTurnProgressPort, WorkerHandle, WorkerResult } from "@chirality/runtime-contracts";
import { CodexTurnSession } from "../packages/daemon/src/codex-session.js";
import { startSupervisorServer, SupervisorClient } from "../packages/daemon/src/supervisor-server.js";
import { createControlledCodexSupervisorForTests } from "../packages/daemon/src/codex-supervisor.js";

function nativePlanFixture(requestId: string | number, late = false) {
  const stdin = new PassThrough(), stdout = new PassThrough();
  let buffer = "";
  const send = (value: unknown) => stdout.write(`${JSON.stringify(value)}\n`);
  stdin.on("data", chunk => {
    buffer += chunk.toString();
    for (let newline = buffer.indexOf("\n"); newline >= 0; newline = buffer.indexOf("\n")) {
      const line = buffer.slice(0, newline); buffer = buffer.slice(newline + 1);
      const request = JSON.parse(line);
      if (request.method === "initialize") send({ id: request.id, result: {} });
      else if (request.method === "thread/start") {
        send({ method: "thread/started", params: { thread: { id: "provider-thread" } } });
        send({ id: request.id, result: { thread: { id: "provider-thread" }, approvalPolicy: "never", approvalsReviewer: "auto_review" } });
      } else if (request.method === "turn/start") {
        expect(request.params.collaborationMode).toEqual({ mode: "plan", settings: { model: "fixture-model", reasoning_effort: null, developer_instructions: null } });
        expect(request.params.approvalPolicy).toBeUndefined();
        send({ id: request.id, result: { turn: { id: "provider-turn", status: "inProgress" } } });
        send({ method: "turn/started", params: { threadId: "provider-thread", turn: { id: "provider-turn", status: "inProgress" } } });
        send({ method: "turn/plan/updated", params: { threadId: "provider-thread", turnId: "provider-turn", plan: [{ step: "checklist only" }] } });
        send({ method: "item/plan/delta", params: { threadId: "provider-thread", turnId: "provider-turn", itemId: "plan-1", delta: "non-authoritative delta" } });
        send({ method: "item/completed", params: { threadId: "foreign-thread", turnId: "provider-turn", item: { id: "foreign-plan", type: "plan", text: "foreign" } } });
        send({ method: "item/completed", params: { threadId: "provider-thread", turnId: "provider-turn", item: { id: "plan-1", type: "plan", text: "authoritative completed plan" } } });
        send({ method: "item/completed", params: { threadId: "provider-thread", turnId: "provider-turn", item: { id: "plan-1", type: "plan", text: "authoritative completed plan" } } });
        send({ id: requestId, method: "item/tool/requestUserInput", params: { threadId: "provider-thread", turnId: "provider-turn", itemId: "question-1", questions: [
          { id: "scope", header: "Scope", question: "Which scope?", options: [{ label: "A", description: "First" }, { label: "B", description: "Second" }], isOther: true, isSecret: false },
          { id: "token", header: "Token", question: "Provide token", options: null, isSecret: true }
        ], isBlocking: true, autoResolutionMs: null } });
      } else if (request.id === requestId && request.result) {
        send({ method: "serverRequest/resolved", params: { threadId: "provider-thread", requestId } });
        send({ method: "turn/completed", params: { threadId: "provider-thread", turn: { id: "provider-turn", status: "completed" } } });
        if (late) send({ method: "item/completed", params: { threadId: "provider-thread", turnId: "provider-turn", item: { id: "late-plan", type: "plan", text: "late" } } });
      } else if (request.method === "turn/interrupt") {
        send({ id: request.id, result: {} });
        send({ method: "turn/completed", params: { threadId: "provider-thread", turn: { id: "provider-turn", status: "interrupted" } } });
      }
    }
  });
  const session = new CodexTurnSession({ transport: { stdin, stdout, async close() { stdin.destroy(); stdout.destroy(); } }, requestTimeoutMs: 500, turnTimeoutMs: 1000 });
  return { session };
}

describe("native Plan Codex transport", () => {
  it.each([77, "request-77"])("keeps checklist state separate and bridges multipart answers for %s request IDs", async requestId => {
    const { session } = nativePlanFixture(requestId);
    try {
      await session.initialize();
      const threadId = await session.startThread({ cwd: "/private/tmp", model: "fixture-model", continuityChecked: true });
      const turnId = await session.startTurn({ threadId, text: "make a plan", model: "fixture-model", interactionMode: "native-plan" });
      await expect.poll(() => session.pendingNativePlanClarifications()).toHaveLength(1);
      const [prompt] = session.pendingNativePlanClarifications();
      expect(prompt).toMatchObject({ threadId, turnId, requestId, itemId: "question-1", isBlocking: true, autoResolutionMs: null });
      expect(prompt!.questions).toEqual([
        { id: "scope", header: "Scope", question: "Which scope?", options: [{ label: "A", description: "First" }, { label: "B", description: "Second" }], isOther: true, isSecret: false },
        { id: "token", header: "Token", question: "Provide token", options: [], isOther: false, isSecret: true }
      ]);
      await session.replyNativePlanClarification(requestId, { scope: { answers: ["A"] }, token: { answers: ["secret-value"] } });
      expect((await session.waitTurn(turnId)).status).toBe("completed");
      const events = [];
      for await (const event of session.events()) { events.push(event); if (event.type === "terminal") break; }
      expect(events.filter(event => event.type === "plan")).toHaveLength(1);
      expect(events.find(event => event.type === "plan")).toMatchObject({ plan: { id: "plan-1", type: "plan", text: "authoritative completed plan" } });
      expect(session.diagnostics().quarantinedNotifications).toBe(2); // checklist plus foreign plan
      await expect(session.replyNativePlanClarification(requestId, { scope: { answers: ["A"] }, token: { answers: ["again"] } })).rejects.toThrow("Unknown or resolved");
    } finally { await session.close(); }
  });

  it("makes an interrupted clarification stale", async () => {
    const { session } = nativePlanFixture("interrupt-question");
    try {
      await session.initialize(); const threadId = await session.startThread({ cwd: "/private/tmp", model: "fixture-model", continuityChecked: true });
      const turnId = await session.startTurn({ threadId, text: "make a plan", model: "fixture-model", interactionMode: "native-plan" });
      await expect.poll(() => session.pendingNativePlanClarifications()).toHaveLength(1);
      await session.interrupt(turnId); expect((await session.waitTurn(turnId)).status).toBe("interrupted");
      await expect(session.replyNativePlanClarification("interrupt-question", { scope: { answers: ["A"] }, token: { answers: ["x"] } })).rejects.toThrow("Unknown or resolved");
    } finally { await session.close(); }
  });

  it("fails the worker instead of publishing success after the plan projection bound is exceeded", async () => {
    const stdin = new PassThrough(), stdout = new PassThrough(); let buffer = "";
    const send = (value: unknown) => stdout.write(`${JSON.stringify(value)}\n`);
    stdin.on("data", chunk => {
      buffer += chunk.toString();
      for (let newline = buffer.indexOf("\n"); newline >= 0; newline = buffer.indexOf("\n")) {
        const request = JSON.parse(buffer.slice(0, newline)); buffer = buffer.slice(newline + 1);
        if (request.method === "initialize") send({ id: request.id, result: {} });
        else if (request.method === "account/read") send({ id: request.id, result: { requiresOpenaiAuth: false, account: null } });
        else if (request.method === "thread/start") { send({ method: "thread/started", params: { thread: { id: "thread" } } }); send({ id: request.id, result: { thread: { id: "thread" }, approvalsReviewer: "auto_review", approvalPolicy: "never" } }); }
        else if (request.method === "turn/start") {
          send({ id: request.id, result: { turn: { id: "turn", status: "inProgress" } } }); send({ method: "turn/started", params: { threadId: "thread", turn: { id: "turn", status: "inProgress" } } });
          for (let index = 0; index < 65; index++) send({ method: "item/completed", params: { threadId: "thread", turnId: "turn", item: { id: `plan-${index}`, type: "plan", text: `plan ${index}` } } });
          send({ method: "turn/completed", params: { threadId: "thread", turn: { id: "turn", status: "completed" } } });
        }
      }
    });
    const root = realpathSync(tmpdir());
    const supervisor = createControlledCodexSupervisorForTests({ identity: { canonicalRoot: root, cwd: root, accountId: "fixture", accountEpoch: 1, policyDigest: "fixture" }, model: "fixture-model", allowUnauthenticatedModel: true, launch: async () => ({ pid: 1, transport: { stdin, stdout, async close() { stdin.destroy(); stdout.destroy(); } } }) });
    try {
      const worker = await supervisor.acquire("overflow", JSON.stringify({ prompt: "plan", interactionMode: "native-plan", projectId: "project", sessionId: "session", clientTurnId: "client-turn" }));
      await expect(supervisor.wait(worker.workerId, worker.generation)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    } finally { await supervisor.close().catch(() => undefined); }
  });
});

it("carries native Plan events and questions over the authenticated supervisor boundary", async () => {
  const dir = await mkdtemp(join(realpathSync(tmpdir()), "native-plan-supervisor-"));
  const handle: WorkerHandle = { workerId: "worker", generation: "generation", pid: 1, state: "running" };
  const event: NativePlanTransportEvent = { projectId: "project", sessionId: "session", clientTurnId: "client-turn", providerThreadId: "provider-thread", providerTurnId: "provider-turn", eventId: "event", occurredAt: new Date(0).toISOString(), plan: { id: "plan", type: "plan", text: "done" } };
  const question: NativePlanClarificationPrompt = { projectId: "project", sessionId: "session", clientTurnId: "client-turn", providerThreadId: "provider-thread", providerTurnId: "provider-turn", requestId: 9, itemId: "question", questions: [{ id: "q", header: "Q", question: "Choose", options: [], isOther: true, isSecret: false }], isBlocking: true, autoResolutionMs: null };
  let delivered: NativePlanClarificationAnswers | undefined;
  const supervisor: DelegatedHarnessProcessSupervisorPort & SupervisorNativePlanPort & SupervisorTurnProgressPort = {
    async acquire() { return handle; }, async inventory() { return [handle]; }, async reconnect() { return handle; },
    async wait() { return { worker: handle, exitCode: 0, signal: null, stdout: "", stderr: "" } as WorkerResult; }, async retire() {},
    async drainNativePlanEvents() { return [event]; }, async pendingNativePlanClarifications() { return [question]; },
    async drainTurnProgress() { return [{ type: "started" as const, providerThreadId: "provider-thread", providerTurnId: "provider-turn" }, { type: "text" as const, providerThreadId: "provider-thread", providerTurnId: "provider-turn", text: "stream" }]; },
    async replyNativePlanClarification(_workerId, _generation, _requestId, answers) { delivered = answers; return { sent: true }; }
  };
  const socketPath = join(dir, "s.sock"), server = await startSupervisorServer({ socketPath, supervisor });
  try {
    const client = new SupervisorClient({ socketPath, credential: server.credential });
    expect(await client.drainNativePlanEvents("worker", "generation")).toEqual([event]);
    expect(await client.pendingNativePlanClarifications("worker", "generation")).toEqual([question]);
    expect(await client.drainTurnProgress("worker", "generation")).toEqual([{ type: "started", providerThreadId: "provider-thread", providerTurnId: "provider-turn" }, { type: "text", providerThreadId: "provider-thread", providerTurnId: "provider-turn", text: "stream" }]);
    const answers = { q: { answers: ["yes"] } };
    expect(await client.replyNativePlanClarification("worker", "generation", 9, answers)).toEqual({ sent: true });
    expect(delivered).toEqual(answers);
  } finally { await server.close(); await rm(dir, { recursive: true, force: true }); }
});
