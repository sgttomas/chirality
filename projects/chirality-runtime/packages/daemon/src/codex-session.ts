import { randomUUID } from "node:crypto";
import { isIP } from "node:net";
import type { NetworkApprovalPrompt, NetworkApprovalChoice } from "@chirality/runtime-contracts";
import type { Readable, Writable } from "node:stream";
import { isAbsolute, resolve } from "node:path";
import { RuntimeError } from "@chirality/runtime-contracts";

export interface CodexDynamicToolResult { success: boolean; contentItems: readonly { type: "inputText"; text: string }[] }
export interface CodexDynamicTool {
  name: "delegate_agent" | "review";
  description: string;
  inputSchema: Readonly<Record<string, unknown>>;
  handler(arguments_: Readonly<Record<string, unknown>>, context: { threadId: string; turnId: string; callId: string; signal: AbortSignal }): Promise<CodexDynamicToolResult>;
}
interface DynamicCall { signature: string; turnId: string; controller: AbortController; done: Promise<CodexDynamicToolResult>; completed: boolean }
export interface CodexNativePermissions { filesystem: Readonly<Record<string, "read" | "write" | "deny">>; network: { enabled: boolean; [key: string]: unknown } }
export interface CodexSessionTransport { stdin: Writable; stdout: Readable; close(): Promise<void> }
export interface CodexTurnTerminal { threadId: string; turnId: string; status: "completed" | "failed" | "interrupted"; output: string }
export type CodexSessionEvent = { type: "text"; threadId: string; turnId: string; text: string } | { type: "terminal"; terminal: CodexTurnTerminal };
interface Pending { resolve(value: Record<string, unknown>): void; reject(error: Error): void; timer: ReturnType<typeof setTimeout> }
interface Turn {
  threadId: string; id?: string; terminal?: CodexTurnTerminal; items: Map<string, { text: string; completed: boolean }>;
  done: Promise<CodexTurnTerminal>; resolve(value: CodexTurnTerminal): void; reject(error: Error): void;
  timer: ReturnType<typeof setTimeout>;
}
const invalid = (message: string) => new RuntimeError("INVALID_REQUEST", message, 400);
const protocol = (message: string) => new RuntimeError("ENGINE_UNAVAILABLE", message, 503, { reason: "CODEX_PROTOCOL_FAILURE" });
function object(value: unknown): Record<string, unknown> {
  if (!value || typeof value !== "object" || Array.isArray(value)) throw protocol("Unsupported Codex message shape");
  return value as Record<string, unknown>;
}
function identifier(value: unknown): string {
  if (typeof value !== "string" || !/^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$/.test(value)) throw protocol("Invalid Codex identifier");
  return value;
}
/**
 * Known-method actor, not a sandbox or launch/authentication authority. The trusted
 * host provides an already-contained transport and checks continuity before thread
 * selection. Current documented turn events are a candidate adapter dialect, not
 * evidence that the pinned 0.149 payload has completed an authenticated turn.
 */
export class CodexTurnSession {
  private readonly commandNetworkPosture: "off" | "ask-per-destination" | "on";
  private readonly networkApprovals = new Map<string, { prompt: NetworkApprovalPrompt; requestId: string | number; signature: string; state: "pending" | "sending" | "sent" | "resolved" }>();
  private readonly requests = new Map<number, Pending>();
  private nextId = 1;
  private buffer: Buffer = Buffer.alloc(0);
  private received = 0;
  private ready = false;
  private initializing = false;
  private selecting = false;
  private threadId: string | undefined;
  private threadNotice: string | undefined;
  private active: Turn | undefined;
  private readonly terminals = new Map<string, CodexTurnTerminal>();
  private failure: RuntimeError | undefined;
  private closing: Promise<void> | undefined;
  private readonly queue: CodexSessionEvent[] = [];
  private wake: (() => void) | undefined;
  private iteratorClaimed = false;
  private quarantinedNotifications = 0;
  private readonly childAssociations = new Map<string, string>();
  private retryableErrors = 0;
  private readonly tools = new Map<string, CodexDynamicTool>();
  private readonly toolCalls = new Map<string, DynamicCall>();
  private readonly resolvedServerRequests = new Set<string>();
  private readonly toolRequestIds = new Map<string, string>();
  private expectedPermissions: CodexNativePermissions | undefined;
  private policyCwd: string | undefined;
  private readonly nativePolicy: Readonly<{ permissionProfile: string; policyDigest: string }> | undefined;
  private login: { state: "pending" | "completed" | "failed"; loginId?: string } | undefined;
  constructor(private readonly options: { transport: CodexSessionTransport; requestTimeoutMs?: number; turnTimeoutMs?: number; purpose?: "turn" | "login"; permissionProfile?: string; policyDigest?: string; dynamicTools?: readonly CodexDynamicTool[]; toolTimeoutMs?: number; commandNetworkPosture?: "off" | "ask-per-destination" | "on" }) {
    this.commandNetworkPosture = options.commandNetworkPosture ?? "off";
    if (options.commandNetworkPosture !== undefined && !["off", "ask-per-destination", "on"].includes(options.commandNetworkPosture)) throw invalid("Invalid trusted command network posture");
    if ((options.dynamicTools?.length ?? 0) > 2 || (options.purpose === "login" && options.dynamicTools?.length)) throw invalid("Unsupported dynamic tool registry");
    for (const tool of options.dynamicTools ?? []) {
      if (!["delegate_agent", "review"].includes(tool.name) || this.tools.has(tool.name) || typeof tool.description !== "string" || !tool.description.trim() || tool.description.length > 4096 || typeof tool.handler !== "function") throw invalid("Invalid immutable dynamic tool declaration");
      const schema = JSON.parse(JSON.stringify(tool.inputSchema)) as Record<string, unknown>;
      if (Buffer.byteLength(JSON.stringify(schema)) > 16384) throw invalid("Dynamic tool schema exceeds bound");
      checkToolSchema(schema);
      if (schema.type !== "object") throw invalid("Dynamic tool input must be a closed object");
      this.tools.set(tool.name, Object.freeze({ name: tool.name, description: tool.description, inputSchema: freezeTree(schema), handler: tool.handler }));
    }
    if (options.permissionProfile !== undefined || options.policyDigest !== undefined) {
      if (typeof options.permissionProfile !== "string" || !/^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$/.test(options.permissionProfile) || typeof options.policyDigest !== "string" || !/^[a-f0-9]{64}$/.test(options.policyDigest)) throw invalid("Named policy requires an explicit profile and SHA-256 digest");
      this.nativePolicy = Object.freeze({ permissionProfile: options.permissionProfile, policyDigest: options.policyDigest });
    }
    for (const value of [options.requestTimeoutMs ?? 10000, options.turnTimeoutMs ?? 120000, options.toolTimeoutMs ?? 30000]) if (!Number.isSafeInteger(value) || value < 1 || value > 2147483647) throw invalid("Invalid session timeout");
    options.transport.stdout.on("data", (chunk: Buffer | string) => this.consume(Buffer.isBuffer(chunk) ? chunk : Buffer.from(chunk)));
    options.transport.stdout.on("error", () => this.fail(protocol("Codex transport failed")));
    options.transport.stdout.on("end", () => this.fail(protocol("Codex transport ended")));
    options.transport.stdin.on("error", () => this.fail(protocol("Codex input failed")));
  }
  private fail(error: RuntimeError): void {
    if (this.failure) return;
    this.failure = error;
    this.resolveNetworkApprovals();
    for (const call of this.toolCalls.values()) if (!call.completed) call.controller.abort();
    if (this.login?.state === "pending") this.login.state = "failed";
    for (const pending of this.requests.values()) { clearTimeout(pending.timer); pending.reject(error); }
    this.requests.clear();
    if (this.active) { clearTimeout(this.active.timer); this.active.reject(error); this.active = undefined; }
    this.wake?.(); this.wake = undefined;
    this.closing ??= this.options.transport.close().catch(() => {});
  }
  private assertReady(): void { if (this.failure) throw this.failure; if (!this.ready) throw invalid("Initialize Codex session first"); }
  private write(message: Record<string, unknown>): void {
    const data = JSON.stringify(message) + "\n";
    if (Buffer.byteLength(data) > 262144) throw invalid("Codex request is too large");
    this.options.transport.stdin.write(data, error => { if (error) this.fail(protocol("Codex input failed")); });
  }
  private request(method: string, params: Record<string, unknown>): Promise<Record<string, unknown>> {
    if (this.failure) return Promise.reject(this.failure);
    if (this.requests.size >= 8) return Promise.reject(invalid("Too many outstanding Codex requests"));
    const id = this.nextId++;
    return new Promise((resolveRequest, reject) => {
      const timer = setTimeout(() => this.fail(protocol("Codex request timed out")), this.options.requestTimeoutMs ?? 10000);
      this.requests.set(id, { resolve: resolveRequest, reject, timer });
      try { this.write({ id, method, params }); }
      catch (error) { clearTimeout(timer); this.requests.delete(id); reject(error); }
    });
  }
  private consume(chunk: Buffer): void {
    if (this.failure) return;
    this.received += chunk.length;
    if (this.received > 16 * 1024 * 1024 || this.buffer.length + chunk.length > 1024 * 1024) { this.fail(protocol("Codex output bound exceeded")); return; }
    this.buffer = Buffer.concat([this.buffer, chunk]);
    for (let newline = this.buffer.indexOf(10); newline >= 0; newline = this.buffer.indexOf(10)) {
      const line = this.buffer.subarray(0, newline); this.buffer = this.buffer.subarray(newline + 1);
      try {
        const message = object(JSON.parse(line.toString()));
        if ("id" in message) {
          if ("method" in message) { this.serverRequest(message); continue; }
          const pending = this.requests.get(message.id as number);
          if (!pending || (("result" in message) === ("error" in message))) throw protocol("Unsolicited or duplicate Codex response");
          const result = "result" in message ? object(message.result) : undefined;
          this.requests.delete(message.id as number); clearTimeout(pending.timer);
          if ("error" in message) pending.reject(new RuntimeError("ENGINE_UNAVAILABLE", "Codex rejected the requested operation", 503, { reason: "CODEX_REQUEST_REJECTED" }));
          else pending.resolve(result!);
        } else this.notification(identifierMethod(message.method), message.params);
      } catch (error) { this.fail(error instanceof RuntimeError ? error : protocol("Malformed Codex protocol")); return; }
    }
  }
  private serverRequest(message: Record<string, unknown>): void {
    if (message.method === "item/commandExecution/requestApproval") { this.networkApprovalRequest(message); return; }
    if (message.method !== "item/tool/call") throw protocol("Unsupported Codex server request; no approval granted");
    const requestId = message.id;
    if ((typeof requestId !== "string" && typeof requestId !== "number") || (typeof requestId === "number" && !Number.isSafeInteger(requestId)) || String(requestId).length > 128) throw protocol("Invalid server request ID");
    const params = object(message.params), active = this.active;
    const threadId = identifier(params.threadId), turnId = identifier(params.turnId), callId = identifier(params.callId);
    if (!active?.id || active.id !== turnId || threadId !== this.threadId || threadId !== active.threadId) throw protocol("Dynamic callback is not bound to the active primary turn");
    const tool = this.tools.get(String(params.tool));
    if (!tool) throw protocol("Dynamic tool is not registered by the trusted host");
    const input = object(params.arguments);
    if (Buffer.byteLength(JSON.stringify(input)) > 65536 || !matchesToolSchema(input, tool.inputSchema)) throw protocol("Dynamic tool arguments violate the closed schema");
    const signature = JSON.stringify([threadId, turnId, callId, params.tool, input]);
    const requestKey = `${typeof requestId}:${requestId}`;
    if (this.networkApprovals.has(requestKey) || this.resolvedServerRequests.has(requestKey)) throw protocol("Reused or resolved server request ID");
    const previousRequest = this.toolRequestIds.get(requestKey);
    if (previousRequest !== undefined) { if (previousRequest !== signature) throw protocol("Conflicting duplicate dynamic request"); return; }
    if (this.toolRequestIds.size >= 128) throw protocol("Dynamic request inventory bound exceeded");
    this.toolRequestIds.set(requestKey, signature);
    let call = this.toolCalls.get(callId);
    if (call && call.signature !== signature) throw protocol("Conflicting duplicate dynamic call");
    if (!call) {
      if (this.toolCalls.size >= 64 || [...this.toolCalls.values()].filter(value => !value.completed).length >= 8) throw protocol("Dynamic callback concurrency bound exceeded");
      const controller = new AbortController();
      const entry: DynamicCall = { signature, turnId, controller, done: Promise.resolve({ success: false, contentItems: [] }), completed: false };
      this.toolCalls.set(callId, entry);
      entry.done = (async () => {
        let timer: ReturnType<typeof setTimeout> | undefined;
        let abort: (() => void) | undefined;
        try {
          const interrupted = new Promise<never>((_, reject) => { abort = () => reject(protocol("Dynamic call cancelled")); controller.signal.addEventListener("abort", abort, { once: true }); timer = setTimeout(() => controller.abort(), this.options.toolTimeoutMs ?? 30000); });
          const result = await Promise.race([Promise.resolve().then(() => { if (controller.signal.aborted) throw protocol("Dynamic call cancelled before dispatch"); return tool.handler(freezeTree(JSON.parse(JSON.stringify(input)) as Record<string, unknown>), { threadId, turnId, callId, signal: controller.signal }); }), interrupted]);
          if (!result || Object.keys(result).sort().join(",") !== "contentItems,success" || typeof result.success !== "boolean" || !Array.isArray(result.contentItems) || result.contentItems.length > 16 || result.contentItems.some(item => !item || Object.keys(item).sort().join(",") !== "text,type" || item.type !== "inputText" || typeof item.text !== "string" || Buffer.byteLength(item.text) > 65536) || Buffer.byteLength(JSON.stringify(result)) > 262144) throw protocol("Invalid bounded dynamic tool result");
          return { success: result.success, contentItems: result.contentItems.map(item => ({ type: "inputText" as const, text: item.text })) };
        } catch { return { success: false, contentItems: [{ type: "inputText" as const, text: "Host tool failed or was cancelled." }] }; }
        finally { clearTimeout(timer); if (abort) controller.signal.removeEventListener("abort", abort); entry.completed = true; }
      })();
      call = entry;
    }
    void call.done.then(result => {
      if (this.resolvedServerRequests.has(requestKey) || this.failure || this.active?.id !== turnId || this.threadId !== threadId) return;
      try { this.write({ id: requestId, result }); } catch (error) { this.fail(error instanceof RuntimeError ? error : protocol("Dynamic response failed")); }
    });
  }
  private resolveNetworkApprovals(turnId?: string): void {
    for (const entry of this.networkApprovals.values()) if (!turnId || entry.prompt.turnId === turnId) entry.state = "resolved";
  }
  private networkApprovalRequest(message: Record<string, unknown>): void {
    if (this.commandNetworkPosture !== "ask-per-destination") throw protocol("Network approval requires trusted ask posture");
    const requestId = message.id;
    if ((typeof requestId !== "string" && typeof requestId !== "number") || (typeof requestId === "number" && !Number.isSafeInteger(requestId)) || String(requestId).length > 128) throw protocol("Invalid network request ID");
    const params = object(message.params), active = this.active;
    const threadId = identifier(params.threadId), turnId = identifier(params.turnId); identifier(params.itemId);
    if (!active?.id || active.id !== turnId || active.threadId !== threadId || this.threadId !== threadId) throw protocol("Network request is outside the active primary turn");
    if (!Number.isSafeInteger(params.startedAtMs) || Number(params.startedAtMs) < 0) throw protocol("Invalid network approval timestamp");
    // Never turn a combined filesystem/exec-policy prompt into a network-only grant.
    if (["additionalPermissions", "proposedExecpolicyAmendment", "command", "cwd", "commandActions"].some(key => params[key] !== undefined && params[key] !== null)) throw protocol("Unsupported combined approval request");
    const context = object(params.networkApprovalContext), host = context.host, protocolName = context.protocol;
    if (Object.keys(context).sort().join(",") !== "host,protocol" || typeof host !== "string" || host.length > 253 || (!isIP(host.replace(/^\[|\]$/g, "")) && !host.split(".").every(label => /^[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?$/i.test(label))) || !["http", "https", "socks5Tcp", "socks5Udp"].includes(String(protocolName))) throw protocol("Invalid network destination context");
    if (!Array.isArray(params.availableDecisions) || params.availableDecisions.length > 16) throw protocol("Exact available approval decisions required");
    const availableDecisions: NetworkApprovalChoice[] = [];
    for (const choice of params.availableDecisions) {
      if (choice === "accept") availableDecisions.push("allow"); else if (choice === "decline") availableDecisions.push("deny"); else if (choice === "acceptForSession") availableDecisions.push("acceptForSession");
      else if (choice === "cancel" || (choice && typeof choice === "object")) continue;
      else throw protocol("Unknown approval decision");
    }
    if (!availableDecisions.length || new Set(availableDecisions).size !== availableDecisions.length) throw protocol("No valid exact network choices");
    const signature = JSON.stringify(params), key = `${typeof requestId}:${requestId}`;
    const prior = this.networkApprovals.get(key);
    if (prior) { if (prior.signature !== signature || prior.state !== "pending") throw protocol("Conflicting or stale network approval request"); return; }
    if (this.networkApprovals.size >= 128) throw protocol("Network approval inventory bound exceeded");
    if (this.toolRequestIds.has(key)) throw protocol("Server request ID reused across capability classes");
    this.networkApprovals.set(key, { requestId, signature, state: "pending", prompt: { approvalId: randomUUID(), threadId, turnId, networkApprovalContext: { host, protocol: String(protocolName) }, availableDecisions } });
  }
  pendingNetworkApprovals(): readonly NetworkApprovalPrompt[] {
    if (this.failure) throw this.failure;
    if (!this.ready) return [];
    return [...this.networkApprovals.values()].filter(entry => entry.state === "pending" && entry.prompt.turnId === this.active?.id && entry.prompt.threadId === this.threadId).map(entry => structuredClone(entry.prompt));
  }
  async replyNetworkApproval(approvalId: string, decision: NetworkApprovalChoice): Promise<{ sent: true }> {
    this.assertReady();
    const entry = [...this.networkApprovals.values()].find(value => value.prompt.approvalId === approvalId);
    if (!entry || entry.state !== "pending" || entry.prompt.turnId !== this.active?.id || entry.prompt.threadId !== this.threadId || !entry.prompt.availableDecisions.includes(decision)) throw invalid("Unknown, resolved or unsupported network approval decision");
    const wire = decision === "allow" ? "accept" : decision === "deny" ? "decline" : decision;
    const frame = JSON.stringify({ id: entry.requestId, result: { decision: wire } }) + "\n";
    entry.state = "sending"; // A pending write is never eligible for another grant or retry.
    await new Promise<void>((resolveWrite, rejectWrite) => {
      let settled = false;
      const finish = (error?: Error | null) => {
        if (settled) return; settled = true; clearTimeout(timer);
        if (error || this.failure) { const failure = this.failure ?? protocol("Approval transport write failed"); this.fail(failure); rejectWrite(failure); }
        else resolveWrite();
      };
      const timer = setTimeout(() => finish(protocol("Approval transport write timed out")), this.options.requestTimeoutMs ?? 10000);
      try { this.options.transport.stdin.write(frame, error => finish(error)); }
      catch { finish(protocol("Approval transport write failed")); }
    });
    if (entry.state === "sending") entry.state = "sent";
    return { sent: true }; // Written to the transport; not a provider execution acknowledgement.
  }
  private emit(event: CodexSessionEvent): void {
    if (this.queue.length >= 1024) throw protocol("Codex event consumer fell behind");
    this.queue.push(event); this.wake?.(); this.wake = undefined;
  }
  nativeChildren(): readonly { threadId: string; sourceTurnId: string }[] { return [...this.childAssociations].map(([threadId, sourceTurnId]) => ({ threadId, sourceTurnId })); }
  diagnostics(): Readonly<{ quarantinedNotifications: number; retryableErrors: number }> {
    return { quarantinedNotifications: this.quarantinedNotifications, retryableErrors: this.retryableErrors };
  }
  private quarantine(method: string, params: unknown): void {
    if (++this.quarantinedNotifications > 1024) throw protocol("Codex diagnostic quarantine bound exceeded");
    if (method === "error" && params && typeof params === "object" && (params as Record<string, unknown>).willRetry === true) this.retryableErrors++;
    // Retain counts only, never raw diagnostics, account material or authority.
  }
  private notification(method: string, value: unknown): void {
    if (method === "serverRequest/resolved") {
      const params = object(value), threadId = identifier(params.threadId), id = params.requestId;
      if ((typeof id !== "string" && typeof id !== "number") || (typeof id === "number" && !Number.isSafeInteger(id)) || String(id).length > 128) throw protocol("Invalid resolved request ID");
      const entry = this.networkApprovals.get(`${typeof id}:${id}`);
      if (entry) { if (entry.prompt.threadId !== threadId) throw protocol("Resolved approval thread mismatch"); entry.state = "resolved"; }
      else {
        const key = `${typeof id}:${id}`, signature = this.toolRequestIds.get(key);
        if (signature) {
          const [callThread, , callId] = JSON.parse(signature);
          if (callThread !== threadId) throw protocol("Resolved tool thread mismatch");
          this.resolvedServerRequests.add(key); this.toolCalls.get(callId)?.controller.abort();
        } else this.quarantine(method, undefined);
      }
      return;
    }
    if (!["account/login/completed", "thread/started", "turn/started", "turn/completed", "item/agentMessage/delta", "item/started", "item/completed"].includes(method)) { this.quarantine(method, value); return; }
    const params = object(value);
    if (method === "account/login/completed") {
      if (this.options.purpose !== "login" || !this.login) throw protocol("Unexpected login completion");
      const loginId = identifier(params.loginId);
      if (typeof params.success !== "boolean" || (this.login.loginId && this.login.loginId !== loginId)) throw protocol("Mismatched login completion");
      const state = params.success ? "completed" : "failed";
      if (this.login.state !== "pending" && this.login.state !== state) throw protocol("Conflicting login completion");
      this.login.loginId = loginId; this.login.state = state; return;
    }
    if (method === "thread/started") {
      const id = identifier(object(params.thread).id);
      if (!this.selecting && id !== this.threadId) { this.quarantine(method, undefined); return; }
      this.threadNotice = id; return;
    }
    const threadId = identifier(params.threadId);
    if (threadId !== this.threadId) { this.quarantine(method, undefined); return; }
    const turnId = method.startsWith("turn/") ? identifier(object(params.turn).id) : identifier(params.turnId);
    if (method === "turn/completed" && this.terminals.has(turnId)) {
      const prior = this.terminals.get(turnId)!;
      if (object(params.turn).status !== prior.status) throw protocol("Conflicting duplicate Codex terminal");
      return;
    }
    if (this.terminals.has(turnId)) throw protocol("Codex reused a terminal turn identifier");
    const active = this.active;
    if (!active || (active.id && active.id !== turnId)) throw protocol("Late or mismatched Codex turn event");
    active.id ??= turnId;
    if (method === "turn/started") { if (object(params.turn).status !== "inProgress") throw protocol("Unsupported started turn status"); return; }
    if (method === "turn/completed") {
      const status = object(params.turn).status;
      if (status !== "completed" && status !== "failed" && status !== "interrupted") throw protocol("Unsupported terminal status");
      if ([...this.toolCalls.values()].some(call => call.turnId === turnId && !call.completed && !call.controller.signal.aborted)) throw protocol("Codex terminal preceded host tool completion");
      this.resolveNetworkApprovals(turnId);
      const terminal: CodexTurnTerminal = { threadId, turnId, status, output: [...active.items.values()].map(item => item.text).join("") };
      this.emit({ type: "terminal", terminal: { ...terminal } });
      clearTimeout(active.timer); this.terminals.set(turnId, terminal); active.terminal = terminal; this.active = undefined;
      active.resolve(terminal); return;
    }
    if (method === "item/agentMessage/delta") {
      const itemId = identifier(params.itemId), text = params.delta;
      if (typeof text !== "string" || Buffer.byteLength(text) > 65536) throw protocol("Unsupported text delta");
      const item = active.items.get(itemId) ?? { text: "", completed: false };
      if (item.completed || Buffer.byteLength(item.text) + Buffer.byteLength(text) > 262144) throw protocol("Late or oversized text delta");
      item.text += text; active.items.set(itemId, item); this.emit({ type: "text", threadId, turnId, text }); return;
    }
    if (method === "item/started" || method === "item/completed") {
      const item = object(params.item), itemId = identifier(item.id);
      if (item.type === "collabAgentToolCall" && item.receiverThreadIds !== undefined) {
        if (!Array.isArray(item.receiverThreadIds) || item.receiverThreadIds.length > 64) throw protocol("Invalid native child association");
        for (const receiver of item.receiverThreadIds) {
          const childId = identifier(receiver);
          if (!this.childAssociations.has(childId) && this.childAssociations.size >= 64) throw protocol("Native child association bound exceeded");
          this.childAssociations.set(childId, turnId);
        }
      }
      if (typeof item.type !== "string" || item.type.length > 128) throw protocol("Unsupported Codex item shape");
      if (item.type !== "agentMessage" && item.type !== "userMessage") { this.quarantine(method, undefined); return; }
      if (item.type === "userMessage") return;
      if (method === "item/started") { if (!active.items.has(itemId)) active.items.set(itemId, { text: "", completed: false }); return; }
      if (typeof item.text !== "string" || Buffer.byteLength(item.text) > 262144) throw protocol("Unsupported completed message");
      const prior = active.items.get(itemId);
      if (prior?.completed || (prior && !item.text.startsWith(prior.text))) throw protocol("Conflicting completed message");
      const remainder = item.text.slice(prior?.text.length ?? 0);
      active.items.set(itemId, { text: item.text, completed: true });
      if (remainder) this.emit({ type: "text", threadId, turnId, text: remainder }); return;
    }
    throw protocol("Unsupported Codex notification");
  }
  async initialize(): Promise<void> {
    if (this.ready || this.initializing) throw invalid("Codex connection initializes once");
    this.initializing = true;
    try { await this.request("initialize", { clientInfo: { name: "chirality_runtime_offline_probe", version: "0.0.0" }, capabilities: { experimentalApi: true } }); this.write({ method: "initialized" }); this.ready = true; }
    finally { this.initializing = false; }
  }
  async accountRead(): Promise<{ authRequired: boolean; hasAccount: boolean }> {
    this.assertReady(); const result = await this.request("account/read", { refreshToken: false });
    if (typeof result.requiresOpenaiAuth !== "boolean" || !("account" in result) || (result.account !== null && (typeof result.account !== "object" || Array.isArray(result.account)))) { this.fail(protocol("Unsupported account response")); throw this.failure; }
    return { authRequired: result.requiresOpenaiAuth, hasAccount: result.account !== null };
  }
  async loginStart(): Promise<{ loginId: string; authUrl: string }> {
    this.assertReady();
    if (this.options.purpose !== "login" || this.login) throw invalid("Login requires a fresh dedicated login transport");
    this.login = { state: "pending" };
    try {
      const result = await this.request("account/login/start", { type: "chatgpt" });
      const loginId = identifier(result.loginId);
      if (result.type !== "chatgpt" || (this.login.loginId && this.login.loginId !== loginId)) throw protocol("Unsupported login response");
      if (typeof result.authUrl !== "string" || result.authUrl.length > 8192 || /[\x00-\x1f]/.test(result.authUrl)) throw protocol("Invalid login URL");
      const url = new URL(result.authUrl);
      if (url.protocol !== "https:" || !["auth.openai.com", "accounts.openai.com", "chatgpt.com"].includes(url.hostname) || url.username || url.password || url.port || url.hash) throw protocol("Login URL is outside official HTTPS origins");
      this.login.loginId = loginId;
      return { loginId, authUrl: url.toString() };
    } catch (error) { this.login.state = "failed"; this.fail(error instanceof RuntimeError ? error : protocol("Invalid login response")); throw this.failure; }
  }
  loginStatus(): { state: "pending" | "completed" | "failed"; loginId?: string } {
    if (this.options.purpose !== "login") throw invalid("Not a login transport");
    return this.login ? { ...this.login } : { state: "failed" };
  }
  async loginCancel(): Promise<void> {
    this.assertReady();
    if (this.options.purpose !== "login" || !this.login?.loginId || this.login.state !== "pending") throw invalid("No pending login to cancel");
    await this.request("account/login/cancel", { loginId: this.login.loginId });
  }
  async verifyNativePolicy(expected: CodexNativePermissions): Promise<void> {
    this.assertReady();
    if (!this.nativePolicy) throw invalid("No trusted named policy is bound");
    let copy: CodexNativePermissions;
    try { copy = JSON.parse(JSON.stringify(expected)) as CodexNativePermissions; } catch { throw invalid("Invalid expected native policy table"); }
    if (!copy || Object.keys(copy).sort().join(",") !== "filesystem,network" || !copy.filesystem || typeof copy.filesystem !== "object" || Array.isArray(copy.filesystem) || !copy.network || typeof copy.network.enabled !== "boolean") throw invalid("Invalid expected native policy table");
    if (Object.keys(copy.network).some(key => !["enabled", "proxy_url", "enable_socks5", "socks_url", "enable_socks5_udp", "allow_upstream_proxy", "dangerously_allow_non_loopback_proxy", "dangerously_allow_all_unix_sockets", "mode", "domains", "unix_sockets", "allow_local_binding", "mitm"].includes(key)) || Buffer.byteLength(JSON.stringify(copy.network)) > 8192) throw invalid("Invalid expected native network table");
    const entries = Object.entries(copy.filesystem);
    if (!entries.length || entries.length > 256 || entries.some(([path, access]) => !isAbsolute(path) || resolve(path) !== path || !["read", "write", "deny"].includes(access))) throw invalid("Expected native policy must contain exact absolute paths");
    const roots = entries.filter(([, access]) => access === "write").map(([path]) => path);
    if (roots.length !== 1 || roots[0] === "/") throw invalid("Native policy needs one bounded project write root");
    if (this.expectedPermissions && !sameTable(this.expectedPermissions, copy)) throw invalid("Expected native policy cannot be replaced in this session");
    this.expectedPermissions ??= Object.freeze({ filesystem: Object.freeze(copy.filesystem), network: Object.freeze(copy.network) });
    this.policyCwd = roots[0]!;
    await this.checkNativePolicy();
  }
  private async checkNativePolicy(): Promise<void> {
    if (!this.nativePolicy) return;
    if (!this.expectedPermissions || !this.policyCwd) throw invalid("Verify the trusted effective native policy before work");
    try {
      const reply = await this.request("config/read", { includeLayers: true, cwd: this.policyCwd });
      const config = object(reply.config), profiles = object(config.permissions);
      const selected = normalizeObservedProfile(object(profiles[this.nativePolicy.permissionProfile]), this.expectedPermissions.network);
      if (!sameTable(selected, this.expectedPermissions)) throw protocol("Effective named policy differs from the trusted exact table");
      if (config.approvals_reviewer !== "user" || config.approval_policy !== (this.commandNetworkPosture === "ask-per-destination" ? "on-request" : "never") || config.allow_login_shell !== false || object(config.features).plugins !== false || object(config.features).remote_plugin !== false || object(config.features).network_proxy !== (this.commandNetworkPosture !== "off")) throw protocol("Unsafe effective host execution settings");
      for (const field of ["hooks", "mcp_servers", "notify", "plugins", "profiles"]) if (!emptyConfiguration(config[field])) throw protocol("Unsafe host hooks, tools or profile overlays");
      if (config.profile !== null && config.profile !== undefined) throw protocol("Unexpected effective profile override");
      if (config.projects !== null && config.projects !== undefined) {
        const projects = object(config.projects);
        if (Object.keys(projects).some(path => path !== this.policyCwd)) throw protocol("Unexpected project override");
        if (Object.hasOwn(projects, this.policyCwd) && !sameTable(projects[this.policyCwd], { trust_level: "trusted" })) throw protocol("Unsafe project settings override");
      }
    } catch (error) {
      this.fail(error instanceof RuntimeError ? error : protocol("Effective native policy is unavailable")); throw this.failure;
    }
  }
  policyBinding(): Readonly<{ permissionProfile: string; policyDigest: string }> | undefined { return this.nativePolicy; }
  private rejectPolicyOverride(input: object): void {
    if (["permissionProfile", "policyDigest", "permissions", "sandbox", "sandboxPolicy", "approvalPolicy", "approval_policy", "approvalsReviewer", "approvals_reviewer"].some(field => Object.hasOwn(input, field))) throw invalid("Policy overrides are forbidden; use trusted constructor binding");
  }
  private policyParameters(): Record<string, unknown> { return this.nativePolicy ? { permissions: this.nativePolicy.permissionProfile, approvalPolicy: this.commandNetworkPosture === "ask-per-destination" ? "on-request" : "never", approvalsReviewer: "user" } : {}; }
  private model(model: string): void { if (typeof model !== "string" || !model.trim() || model.length > 128 || /[\x00-\x1f]/.test(model)) throw invalid("An explicit model is required"); }
  private async select(method: "thread/start" | "thread/resume", input: { model: string; continuityChecked: true }, params: Record<string, unknown>): Promise<string> {
    this.assertReady(); if (this.options.purpose === "login") throw invalid("Login transport cannot start model work"); this.model(input.model);
    if (input.continuityChecked !== true) throw invalid("Host continuity check is required");
    if (this.active || this.selecting) throw invalid("Thread selection conflicts with active operation");
    this.selecting = true; this.threadNotice = undefined;
    try {
      await this.checkNativePolicy();
      const result = await this.request(method, { ...params, model: input.model, ...this.policyParameters() });
      if (this.nativePolicy && (result.approvalsReviewer !== "user" || result.approvalPolicy !== (this.commandNetworkPosture === "ask-per-destination" ? "on-request" : "never"))) throw protocol("Effective thread approval settings differ from trusted policy");
      const id = identifier(object(result.thread).id);
      if (this.threadNotice && this.threadNotice !== id) throw protocol("Thread response disagrees with notification");
      this.threadId = id; return id;
    } catch (error) { if (error instanceof RuntimeError && error.details?.reason === "CODEX_PROTOCOL_FAILURE") this.fail(error); throw error; } finally { this.selecting = false; }
  }
  async startThread(input: { cwd: string; model: string; continuityChecked: true }): Promise<string> {
    this.rejectPolicyOverride(input);
    if (typeof input.cwd !== "string" || !isAbsolute(input.cwd) || resolve(input.cwd) !== input.cwd) throw invalid("Thread cwd must be canonical absolute");
    if (this.nativePolicy && input.cwd !== this.policyCwd) throw invalid("Thread cwd must match the verified native policy root");
    return this.select("thread/start", input, { cwd: input.cwd, ephemeral: false, ...(this.nativePolicy ? {} : { sandbox: "workspace-write" }), approvalPolicy: this.commandNetworkPosture === "ask-per-destination" ? "on-request" : "never", ...(this.tools.size ? { dynamicTools: [...this.tools.values()].map(({ name, description, inputSchema }) => ({ name, description, inputSchema })) } : {}) });
  }
  async resumeThread(input: { threadId: string; model: string; continuityChecked: true }): Promise<string> {
    this.rejectPolicyOverride(input);
    const id = await this.select("thread/resume", input, { threadId: identifier(input.threadId) });
    if (id !== input.threadId) { this.fail(protocol("Resumed thread identity changed")); throw this.failure; } return id;
  }
  async startTurn(input: { threadId: string; text: string; model: string }): Promise<string> {
    this.rejectPolicyOverride(input);
    this.assertReady(); if (this.options.purpose === "login") throw invalid("Login transport cannot start model work"); this.model(input.model);
    if (input.threadId !== this.threadId || !this.threadId || this.selecting) throw invalid("Select this thread before starting a turn");
    if (this.active) throw new RuntimeError("SESSION_TURN_IN_PROGRESS", "A Codex turn is already active", 409);
    if (typeof input.text !== "string" || !input.text.trim() || Buffer.byteLength(input.text) > 65536 || this.terminals.size >= 64) throw invalid("Invalid prompt or session turn capacity reached");
    let resolveTurn!: (value: CodexTurnTerminal) => void, rejectTurn!: (error: Error) => void;
    const done = new Promise<CodexTurnTerminal>((yes, no) => { resolveTurn = yes; rejectTurn = no; }); void done.catch(() => {});
    const turn: Turn = { threadId: input.threadId, items: new Map(), done, resolve: resolveTurn, reject: rejectTurn, timer: setTimeout(() => this.fail(protocol("Codex turn timed out")), this.options.turnTimeoutMs ?? 120000) };
    this.active = turn;
    try {
      await this.checkNativePolicy();
      const result = await this.request("turn/start", { threadId: input.threadId, input: [{ type: "text", text: input.text }], model: input.model, ...this.policyParameters() });
      const id = identifier(object(result.turn).id);
      if ((turn.id && turn.id !== id) || (this.terminals.has(id) && turn.terminal?.turnId !== id)) throw protocol("Turn response identity mismatch");
      turn.id = id; return id;
    } catch (error) { clearTimeout(turn.timer); if (this.active === turn) this.active = undefined; turn.reject(error as Error); if (error instanceof RuntimeError && error.details?.reason === "CODEX_PROTOCOL_FAILURE") this.fail(error); throw error; }
  }
  async waitTurn(turnId: string): Promise<CodexTurnTerminal> {
    const terminal = this.terminals.get(turnId); if (terminal) return { ...terminal };
    if (this.failure) throw this.failure;
    if (this.active?.id !== turnId) throw invalid("Unknown Codex turn");
    return { ...await this.active.done };
  }
  async interrupt(turnId: string): Promise<void> {
    this.assertReady(); if (this.active?.id !== turnId) throw invalid("No matching active Codex turn");
    for (const call of this.toolCalls.values()) if (call.turnId === turnId && !call.completed) call.controller.abort();
    this.resolveNetworkApprovals(turnId);
    await this.request("turn/interrupt", { threadId: this.active.threadId, turnId });
    // Only an actual terminal notification can resolve waitTurn; acknowledgement is not completion.
  }
  async *events(): AsyncIterable<CodexSessionEvent> {
    if (this.iteratorClaimed) throw invalid("Codex events has one consumer"); this.iteratorClaimed = true;
    for (;;) { if (this.queue.length) { yield this.queue.shift()!; continue; } if (this.failure) throw this.failure; await new Promise<void>(resolveWake => { this.wake = resolveWake; }); }
  }
  async close(): Promise<void> { this.fail(protocol("Codex session closed")); await this.closing; }
}
function identifierMethod(value: unknown): string { if (typeof value !== "string" || value.length > 128) throw protocol("Invalid notification method"); return value; }

function emptyConfiguration(value: unknown): boolean {
  return value === undefined || value === null || (typeof value === "object" && Object.keys(value).length === 0);
}
function sameTable(a: unknown, b: unknown): boolean {
  if (a === b) return true;
  if (!a || !b || typeof a !== "object" || typeof b !== "object" || Array.isArray(a) || Array.isArray(b)) return false;
  const aa = a as Record<string, unknown>, bb = b as Record<string, unknown>;
  const keys = Object.keys(aa);
  return keys.length === Object.keys(bb).length && keys.every(key => Object.hasOwn(bb, key) && sameTable(aa[key], bb[key]));
}

/** Only inert null defaults observed from the pinned 0.149.0 typed readback. */
function normalizeObservedProfile(value: Record<string, unknown>, expectedNetwork: Record<string, unknown> = { enabled: false }): Record<string, unknown> {
  const stripNulls = (input: Record<string, unknown>, fields: readonly string[]): Record<string, unknown> => {
    const output = { ...input };
    for (const field of fields) {
      if (!Object.hasOwn(output, field)) continue;
      if (output[field] !== null) throw protocol("Non-inert native profile metadata is unsupported");
      delete output[field];
    }
    return output;
  };
  const profile = stripNulls(value, ["description", "extends", "workspace_roots"]);
  profile.filesystem = stripNulls(object(profile.filesystem), ["glob_scan_max_depth"]);
  profile.network = stripNulls(object(profile.network), ["proxy_url", "enable_socks5", "socks_url", "enable_socks5_udp", "allow_upstream_proxy", "dangerously_allow_non_loopback_proxy", "dangerously_allow_all_unix_sockets", "mode", "domains", "unix_sockets", "allow_local_binding", "mitm"].filter(field => !Object.hasOwn(expectedNetwork, field)));
  return profile;
}

function freezeTree<T>(value: T): T {
  if (value && typeof value === "object") { for (const child of Object.values(value)) freezeTree(child); Object.freeze(value); }
  return value;
}
function checkToolSchema(schema: Record<string, unknown>, depth = 0): void {
  if (depth > 8 || !schema || typeof schema !== "object" || Array.isArray(schema) || Object.keys(schema).some(key => !["type", "properties", "required", "additionalProperties", "items", "maxItems", "minItems", "maxLength", "minLength", "minimum", "maximum", "enum", "description", "title"].includes(key))) throw invalid("Unsupported dynamic schema vocabulary");
  if (!["object", "array", "string", "number", "integer", "boolean", "null"].includes(String(schema.type))) throw invalid("Unsupported dynamic schema type");
  if (schema.enum !== undefined && (!Array.isArray(schema.enum) || schema.enum.length > 64 || schema.enum.some(value => value !== null && typeof value === "object"))) throw invalid("Unsupported dynamic enum");
  for (const key of ["maxItems", "minItems", "maxLength", "minLength", "minimum", "maximum"]) if (schema[key] !== undefined && (typeof schema[key] !== "number" || !Number.isFinite(schema[key]))) throw invalid("Invalid dynamic schema bound");
  if (schema.type === "object") {
    const properties = schema.properties;
    if (schema.additionalProperties !== false || !properties || typeof properties !== "object" || Array.isArray(properties) || Object.keys(properties).length > 64) throw invalid("Dynamic objects require closed properties");
    if (schema.required !== undefined && (!Array.isArray(schema.required) || schema.required.some(key => typeof key !== "string" || !Object.hasOwn(properties, key)))) throw invalid("Invalid required tool fields");
    for (const child of Object.values(properties)) checkToolSchema(object(child), depth + 1);
  }
  if (schema.type === "array") checkToolSchema(object(schema.items), depth + 1);
}
function matchesToolSchema(value: unknown, schema: Readonly<Record<string, unknown>>): boolean {
  if (Array.isArray(schema.enum) && !schema.enum.includes(value)) return false;
  switch (schema.type) {
    case "null": return value === null;
    case "boolean": return typeof value === "boolean";
    case "number": case "integer": return typeof value === "number" && Number.isFinite(value) && (schema.type !== "integer" || Number.isSafeInteger(value)) && (schema.minimum === undefined || value >= Number(schema.minimum)) && (schema.maximum === undefined || value <= Number(schema.maximum));
    case "string": return typeof value === "string" && value.length <= Math.min(Number(schema.maxLength ?? 65536), 65536) && value.length >= Number(schema.minLength ?? 0);
    case "array": return Array.isArray(value) && value.length <= Math.min(Number(schema.maxItems ?? 64), 64) && value.length >= Number(schema.minItems ?? 0) && value.every(item => matchesToolSchema(item, schema.items as Record<string, unknown>));
    case "object": {
      if (!value || typeof value !== "object" || Array.isArray(value)) return false;
      const properties = schema.properties as Record<string, Record<string, unknown>>, input = value as Record<string, unknown>;
      return Object.keys(input).every(key => Object.hasOwn(properties, key) && matchesToolSchema(input[key], properties[key]!)) && ((schema.required ?? []) as string[]).every(key => Object.hasOwn(input, key));
    }
    default: return false;
  }
}
