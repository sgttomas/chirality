import { describe, expect, it } from "vitest";
import type { DelegatedTurnProgressEvent } from "@chirality/runtime-contracts";
import type { CodexTurnEnvelope } from "@chirality/runtime-core";
import { CodexSupervisor, type CodexSupervisorHost } from "../packages/daemon/src/codex-supervisor.js";
import type { CodexAppServerExit, CodexNotification, CodexServerRequest, CodexServerRequestHandler, CodexServerRequestOutcome } from "../packages/daemon/src/codex-app-server-client.js";

/** Scripted host: records requests, answers from a table, and lets the test raise notifications and server requests. */
function fakeHost() {
  const calls: { method: string; params: any }[] = [];
  let generation = 1;
  let nextThread = 1, nextTurn = 1;
  const listeners = new Set<(notification: CodexNotification) => void>();
  const exits = new Set<(exit: CodexAppServerExit, generation: number) => void>();
  let handler: CodexServerRequestHandler = async () => ({ error: { code: -32601, message: "none" } });
  const answers: Record<string, (params: any) => unknown> = {
    "thread/start": params => ({ thread: { id: `thread-${nextThread++}` }, model: params.model ?? "gpt-5-codex" }),
    "thread/resume": params => ({ thread: { id: params.threadId }, model: params.model ?? "gpt-5-codex" }),
    "thread/settings/update": () => ({}),
    "turn/start": () => ({ turn: { id: `turn-${nextTurn++}`, status: "inProgress" } }),
    "turn/interrupt": () => ({})
  };
  const host: CodexSupervisorHost & { calls: typeof calls; notify(method: string, params: unknown): void; exit(exit: CodexAppServerExit): void; ask(request: CodexServerRequest): Promise<CodexServerRequestOutcome>; restart(): void; fail(method: string, error: Error): void } = {
    get generation() { return generation; },
    calls,
    async request<T>(method: string, params: unknown): Promise<T> {
      calls.push({ method, params });
      const failure = failures.get(method);
      if (failure) { failures.delete(method); throw failure; }
      const answer = answers[method];
      if (!answer) throw new Error(`unscripted ${method}`);
      return answer(params) as T;
    },
    onNotification(listener) { listeners.add(listener); return () => { listeners.delete(listener); }; },
    onExit(listener) { exits.add(listener); return () => { exits.delete(listener); }; },
    onStart() { return () => {}; },
    setServerRequestHandler(next) { handler = next; },
    notify(method, params) { for (const listener of listeners) listener({ method, params }); },
    exit(exit) { const current = generation; for (const listener of exits) listener(exit, current); },
    ask(request) { return handler(request); },
    restart() { generation += 1; },
    fail(method, error) { failures.set(method, error); }
  };
  const failures = new Map<string, Error>();
  return host;
}
function envelope(overrides: Partial<CodexTurnEnvelope> = {}): string {
  return JSON.stringify({ schema: "chirality-codex-turn/v1", prompt: "hello", cwd: "/tmp/project", policy: { approvalPolicy: "on-request", sandbox: "workspace-write" }, interactionMode: "chat", requestedRole: "untyped", projectId: "project", sessionId: "session", clientTurnId: "turn-a", ...overrides } satisfies CodexTurnEnvelope);
}
const drain = async (supervisor: CodexSupervisor, workerId: string, generation: string): Promise<DelegatedTurnProgressEvent[]> => [...await supervisor.drainTurnProgress(workerId, generation)];

describe("Codex supervisor over the shared app-server", () => {
  it("starts a thread, applies the collaboration mode once, starts the turn and assembles text from deltas plus the completed message", async () => {
    const host = fakeHost();
    const supervisor = new CodexSupervisor({ host });
    const worker = await supervisor.acquire("w1", envelope({ developerInstructions: "# Chirality role: agent1", model: "gpt-5-codex", reasoningEffort: "high" }));
    expect(host.calls.map(call => call.method)).toEqual(["thread/start", "thread/settings/update", "turn/start"]);
    expect(host.calls[0]!.params).toMatchObject({ cwd: "/tmp/project", developerInstructions: "# Chirality role: agent1", approvalPolicy: "on-request", sandbox: "workspace-write", model: "gpt-5-codex", ephemeral: false, serviceName: "chirality" });
    expect(host.calls[0]!.params).not.toHaveProperty("baseInstructions");
    expect(host.calls[1]!.params).toEqual({ threadId: "thread-1", collaborationMode: { mode: "default", settings: { model: "gpt-5-codex", reasoning_effort: "high", developer_instructions: null } } });
    expect(host.calls[2]!.params).toEqual({ threadId: "thread-1", input: [{ type: "text", text: "hello" }], model: "gpt-5-codex", effort: "high" });
    expect(await drain(supervisor, worker.workerId, worker.generation)).toEqual([{ type: "started", providerThreadId: "thread-1", providerTurnId: "turn-1" }]);
    host.notify("turn/started", { threadId: "thread-1", turn: { id: "turn-1", status: "inProgress" } });
    host.notify("item/agentMessage/delta", { threadId: "thread-1", turnId: "turn-1", itemId: "m1", delta: "Hel" });
    host.notify("item/reasoning/textDelta", { threadId: "thread-1", turnId: "turn-1", itemId: "r1", delta: "thinking" });
    host.notify("item/completed", { threadId: "thread-1", turnId: "turn-1", item: { type: "agentMessage", id: "m1", text: "Hello there" } });
    host.notify("turn/completed", { threadId: "thread-1", turn: { id: "turn-1", status: "completed", error: null } });
    const events = await drain(supervisor, worker.workerId, worker.generation);
    expect(events.map(event => event.type)).toEqual(["notification", "notification", "text", "notification", "notification", "text", "notification"]);
    expect(events.filter(event => event.type === "notification").map(event => (event as { method: string }).method)).toEqual(["turn/started", "item/agentMessage/delta", "item/reasoning/textDelta", "item/completed", "turn/completed"]);
    expect(events.filter(event => event.type === "text").map(event => (event as { text: string }).text)).toEqual(["Hel", "lo there"]);
    await expect(supervisor.wait(worker.workerId, worker.generation)).resolves.toMatchObject({ exitCode: 0, signal: null, threadId: "thread-1", stdout: "Hello there" });
    await supervisor.retire(worker.workerId, worker.generation);
    expect(await supervisor.inventory()).toEqual([]);

    // The same thread, same mode and same policy: no settings update and no policy resend.
    const second = await supervisor.acquire("w2", envelope({ resumeThreadId: "thread-1", clientTurnId: "turn-b", contextUpdate: "Chirality context update:\nnew method" }));
    expect(host.calls.slice(3).map(call => call.method)).toEqual(["turn/start"]);
    expect(host.calls[3]!.params).toEqual({ threadId: "thread-1", input: [{ type: "text", text: "Chirality context update:\nnew method" }, { type: "text", text: "hello" }] });
    host.notify("turn/completed", { threadId: "thread-1", turn: { id: "turn-2", status: "completed" } });
    await supervisor.wait(second.workerId, second.generation);
    await supervisor.retire(second.workerId, second.generation);

    // A policy change travels on turn/start; a mode change updates the thread settings.
    const third = await supervisor.acquire("w3", envelope({ resumeThreadId: "thread-1", clientTurnId: "turn-c", interactionMode: "native-plan", policy: { approvalPolicy: "never", sandbox: "read-only" } }));
    expect(host.calls.slice(4).map(call => call.method)).toEqual(["thread/settings/update", "turn/start"]);
    expect(host.calls[4]!.params).toMatchObject({ collaborationMode: { mode: "plan" } });
    expect(host.calls[5]!.params).toMatchObject({ approvalPolicy: "never", sandboxPolicy: { type: "readOnly", networkAccess: false } });
    host.notify("turn/completed", { threadId: "thread-1", turn: { id: "turn-3", status: "completed" } });
    await supervisor.wait(third.workerId, third.generation);
    await supervisor.close();
  });

  it("resumes an unknown thread after the app-server restarted and fails live turns when the child exits", async () => {
    const host = fakeHost();
    const supervisor = new CodexSupervisor({ host });
    const first = await supervisor.acquire("w1", envelope());
    host.exit({ code: 1, signal: null });
    const failed = await supervisor.wait(first.workerId, first.generation);
    expect(failed).toMatchObject({ exitCode: 1, stderr: expect.stringContaining("exited during the turn") });
    const progress = await drain(supervisor, first.workerId, first.generation);
    expect(progress.at(-1)).toMatchObject({ type: "notification", method: "chirality/appServer/exited" });
    await supervisor.retire(first.workerId, first.generation);
    host.restart();
    await supervisor.acquire("w2", envelope({ resumeThreadId: "thread-1", clientTurnId: "turn-b" }));
    expect(host.calls.slice(3).map(call => call.method)).toEqual(["thread/resume", "thread/settings/update", "turn/start"]);
    expect(host.calls[3]!.params).toMatchObject({ threadId: "thread-1", cwd: "/tmp/project", approvalPolicy: "on-request", sandbox: "workspace-write" });
    await supervisor.close();
  });

  it("answers every server request kind: pending approvals, user input, elicitation, immediate dynamic tool refusal and visible unsupported outcomes", async () => {
    const host = fakeHost();
    const supervisor = new CodexSupervisor({ host });
    const worker = await supervisor.acquire("w1", envelope());
    await drain(supervisor, worker.workerId, worker.generation);
    const approval = host.ask({ id: 7, method: "item/commandExecution/requestApproval", params: { threadId: "thread-1", turnId: "turn-1", itemId: "cmd-1", command: "ls" } });
    const patch = host.ask({ id: 8, method: "applyPatchApproval", params: { conversationId: "thread-1", callId: "call-1", fileChanges: {} } });
    const permissions = host.ask({ id: 9, method: "item/permissions/requestApproval", params: { threadId: "thread-1", turnId: "turn-1", itemId: "perm-1", cwd: "/tmp/project", reason: "x", permissions: { network: { enabled: true } } } });
    const input = host.ask({ id: 10, method: "item/tool/requestUserInput", params: { threadId: "thread-1", turnId: "turn-1", itemId: "ask-1", questions: [{ id: "q1", header: "H", question: "Q?", isOther: false, isSecret: false, options: null }], isBlocking: true, autoResolutionMs: null } });
    const elicitation = host.ask({ id: 11, method: "mcpServer/elicitation/request", params: { threadId: "thread-1", turnId: "turn-1", serverName: "srv", mode: "form" } });
    await expect(host.ask({ id: 12, method: "item/tool/call", params: { threadId: "thread-1", turnId: "turn-1", callId: "c1", tool: "x", arguments: {} } })).resolves.toEqual({ result: { success: false, contentItems: [{ type: "inputText", text: "Chirality registers no dynamic tools" }] } });
    await expect(host.ask({ id: 13, method: "account/chatgptAuthTokens/refresh", params: { threadId: "thread-1" } })).resolves.toEqual({ error: { code: -32601, message: "unsupported request" } });
    await expect(host.ask({ id: 14, method: "attestation/generate", params: {} })).resolves.toEqual({ error: { code: -32601, message: "unsupported request" } });
    await expect(host.ask({ id: 15, method: "future/unknown", params: { threadId: "thread-1" } })).resolves.toEqual({ error: { code: -32601, message: "unsupported request" } });
    const pending = await supervisor.pendingRequests(worker.workerId, worker.generation);
    expect(pending.map(request => [request.requestId, request.method, request.itemId])).toEqual([["7", "item/commandExecution/requestApproval", "cmd-1"], ["8", "applyPatchApproval", "call-1"], ["9", "item/permissions/requestApproval", "perm-1"], ["10", "item/tool/requestUserInput", "ask-1"], ["11", "mcpServer/elicitation/request", undefined]]);
    const events = await drain(supervisor, worker.workerId, worker.generation);
    expect(events.filter(event => event.type === "request").map(event => (event as { method: string }).method)).toEqual(["item/commandExecution/requestApproval", "applyPatchApproval", "item/permissions/requestApproval", "item/tool/requestUserInput", "mcpServer/elicitation/request", "item/tool/call", "account/chatgptAuthTokens/refresh", "future/unknown"]);
    expect(events.filter(event => event.type === "request-resolved").map(event => [(event as { requestId: string }).requestId, (event as { outcome: string }).outcome])).toEqual([["12", "answered"], ["13", "unsupported"], ["15", "unsupported"]]);

    await expect(supervisor.answerRequest(worker.workerId, worker.generation, "7", { kind: "userInput", answers: {} })).rejects.toMatchObject({ code: "INVALID_REQUEST" });
    await supervisor.answerRequest(worker.workerId, worker.generation, "7", { kind: "approval", verdict: "allowForSession" });
    await supervisor.answerRequest(worker.workerId, worker.generation, "8", { kind: "approval", verdict: "deny" });
    await supervisor.answerRequest(worker.workerId, worker.generation, "9", { kind: "approval", verdict: "allow" });
    await supervisor.answerRequest(worker.workerId, worker.generation, "10", { kind: "userInput", answers: { q1: { answers: ["yes"] } } });
    await supervisor.answerRequest(worker.workerId, worker.generation, "11", { kind: "elicitation", action: "decline" });
    await expect(approval).resolves.toEqual({ result: { decision: "acceptForSession" } });
    await expect(patch).resolves.toEqual({ result: { decision: { denied: { rejection: "Declined by the user in Chirality" } } } });
    await expect(permissions).resolves.toEqual({ result: { permissions: { network: { enabled: true } }, scope: "turn" } });
    await expect(input).resolves.toEqual({ result: { answers: { q1: { answers: ["yes"] } } } });
    await expect(elicitation).resolves.toEqual({ result: { action: "decline", content: null, _meta: null } });
    await expect(supervisor.answerRequest(worker.workerId, worker.generation, "7", { kind: "approval", verdict: "allow" })).rejects.toMatchObject({ code: "NOT_FOUND" });
    expect(await supervisor.pendingRequests(worker.workerId, worker.generation)).toEqual([]);
    const resolved = await drain(supervisor, worker.workerId, worker.generation);
    expect(resolved.map(event => [(event as { requestId: string }).requestId, (event as { outcome: string }).outcome, (event as { decidedBy: string }).decidedBy])).toEqual([["7", "answered", "user"], ["8", "answered", "user"], ["9", "answered", "user"], ["10", "answered", "user"], ["11", "answered", "user"]]);
    await supervisor.close();
  });

  it("cancels still-pending requests when the turn ends and when the supplier resolves them itself", async () => {
    const host = fakeHost();
    const supervisor = new CodexSupervisor({ host });
    const worker = await supervisor.acquire("w1", envelope());
    const approval = host.ask({ id: 1, method: "item/fileChange/requestApproval", params: { threadId: "thread-1", turnId: "turn-1", itemId: "f1" } });
    const legacy = host.ask({ id: 2, method: "execCommandApproval", params: { conversationId: "thread-1", callId: "c2", command: ["ls"], cwd: "/tmp/project" } });
    const supplierResolved = host.ask({ id: 3, method: "item/tool/requestUserInput", params: { threadId: "thread-1", turnId: "turn-1", itemId: "ask", questions: [], isBlocking: false, autoResolutionMs: 10 } });
    host.notify("serverRequest/resolved", { threadId: "thread-1", requestId: 3 });
    await expect(supplierResolved).resolves.toEqual({ result: { answers: {} } });
    host.notify("turn/completed", { threadId: "thread-1", turn: { id: "turn-1", status: "failed", error: { message: "boom" } } });
    await expect(approval).resolves.toEqual({ result: { decision: "cancel" } });
    await expect(legacy).resolves.toEqual({ result: { decision: "abort" } });
    await expect(supervisor.wait(worker.workerId, worker.generation)).resolves.toMatchObject({ exitCode: 1, stderr: "boom" });
    const events = await drain(supervisor, worker.workerId, worker.generation);
    expect(events.filter(event => event.type === "request-resolved").map(event => [(event as { requestId: string }).requestId, (event as { outcome: string }).outcome, (event as { decidedBy: string }).decidedBy])).toEqual([["3", "cancelled", "runtime"], ["1", "cancelled", "runtime"], ["2", "cancelled", "runtime"]]);
    await supervisor.close();
  });

  it("interrupts through turn/interrupt without retiring, memoizes retirement per generation and rejects stale generations", async () => {
    const host = fakeHost();
    const supervisor = new CodexSupervisor({ host });
    const worker = await supervisor.acquire("w1", envelope());
    const interrupting = supervisor.interrupt(worker.workerId, worker.generation);
    await new Promise(resolve => setTimeout(resolve, 1));
    expect(host.calls.at(-1)).toEqual({ method: "turn/interrupt", params: { threadId: "thread-1", turnId: "turn-1" } });
    expect((await supervisor.inventory()).map(handle => handle.workerId)).toEqual(["w1"]);
    host.notify("turn/completed", { threadId: "thread-1", turn: { id: "turn-1", status: "interrupted" } });
    await interrupting;
    await expect(supervisor.wait(worker.workerId, worker.generation)).resolves.toMatchObject({ exitCode: null, signal: "SIGTERM", threadId: "thread-1" });
    expect((await supervisor.inventory()).map(handle => handle.state)).toEqual(["exited"]);
    await supervisor.interrupt(worker.workerId, worker.generation);
    const first = supervisor.retire(worker.workerId, worker.generation);
    const second = supervisor.retire(worker.workerId, worker.generation);
    expect(second).toBe(first);
    await first;
    expect(await supervisor.inventory()).toEqual([]);
    await expect(supervisor.retire(worker.workerId, "stale")).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE", message: "unknown or stale worker generation" });
    await expect(supervisor.wait(worker.workerId, worker.generation)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
    await expect(supervisor.retire(worker.workerId, worker.generation)).resolves.toBeUndefined();
    await expect(supervisor.acquire("w1", "not json")).rejects.toMatchObject({ code: "INVALID_REQUEST" });
    await supervisor.close();
    await expect(supervisor.acquire("w9", envelope())).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
  });

  it("waits for the turn identity when Stop arrives during the turn/start round trip", async () => {
    const host = fakeHost();
    let releaseStart!: () => void;
    const started = new Promise<void>(resolve => { releaseStart = resolve; });
    const original = host.request.bind(host);
    host.request = (async (method: string, params: unknown) => { if (method === "turn/start") await started; return original(method, params); }) as typeof host.request;
    const supervisor = new CodexSupervisor({ host });
    const acquiring = supervisor.acquire("w1", envelope());
    await new Promise(resolve => setTimeout(resolve, 1));
    const handles = await supervisor.inventory();
    expect(handles.map(handle => handle.workerId)).toEqual(["w1"]);
    const interrupting = supervisor.interrupt("w1", handles[0]!.generation);
    await new Promise(resolve => setTimeout(resolve, 1));
    expect(host.calls.some(call => call.method === "turn/interrupt")).toBe(false);
    releaseStart();
    const worker = await acquiring;
    await new Promise(resolve => setTimeout(resolve, 1));
    expect(host.calls.at(-1)).toEqual({ method: "turn/interrupt", params: { threadId: "thread-1", turnId: "turn-1" } });
    host.notify("turn/completed", { threadId: "thread-1", turn: { id: "turn-1", status: "interrupted" } });
    await interrupting;
    await expect(supervisor.wait(worker.workerId, worker.generation)).resolves.toMatchObject({ signal: "SIGTERM" });
  });

  it("captures native plan items and clarifications for plan-mode turns and routes child-thread notifications to the parent turn", async () => {
    const host = fakeHost();
    const supervisor = new CodexSupervisor({ host });
    const worker = await supervisor.acquire("w1", envelope({ interactionMode: "native-plan" }));
    host.notify("thread/started", { thread: { id: "thread-child", parentThreadId: "thread-1" } });
    host.notify("item/completed", { threadId: "thread-child", turnId: "turn-x", item: { type: "agentMessage", id: "child-m", text: "child text" } });
    host.notify("item/completed", { threadId: "thread-1", turnId: "turn-1", item: { type: "plan", id: "plan-1", text: "1. do" } });
    const clarification = host.ask({ id: 5, method: "item/tool/requestUserInput", params: { threadId: "thread-1", turnId: "turn-1", itemId: "ask-1", questions: [{ id: "q1", header: "Scope", question: "Which?", isOther: true, isSecret: false, options: [{ label: "A", description: "a" }] }], isBlocking: true, autoResolutionMs: null } });
    const events = await drain(supervisor, worker.workerId, worker.generation);
    expect(events.filter(event => event.type === "notification").map(event => (event as { method: string; params: any }).method)).toEqual(["thread/started", "item/completed", "item/completed"]);
    expect(events.some(event => event.type === "text")).toBe(false);
    expect(await supervisor.drainNativePlanEvents(worker.workerId, worker.generation)).toEqual([expect.objectContaining({ projectId: "project", sessionId: "session", clientTurnId: "turn-a", providerThreadId: "thread-1", providerTurnId: "turn-1", eventId: "plan-1", plan: "1. do" })]);
    expect(await supervisor.drainNativePlanEvents(worker.workerId, worker.generation)).toEqual([]);
    expect(await supervisor.pendingNativePlanClarifications(worker.workerId, worker.generation)).toEqual([expect.objectContaining({ requestId: "5", itemId: "ask-1", isBlocking: true, autoResolutionMs: null, questions: [{ id: "q1", header: "Scope", question: "Which?", options: [{ label: "A", description: "a" }], isOther: true, isSecret: false }] })]);
    await supervisor.replyNativePlanClarification(worker.workerId, worker.generation, "5", { q1: { answers: ["A"] } });
    await expect(clarification).resolves.toEqual({ result: { answers: { q1: { answers: ["A"] } } } });
    expect(await supervisor.pendingNativePlanClarifications(worker.workerId, worker.generation)).toEqual([]);
    await supervisor.close();
  });
});
