import { revalidateHostedAccountAuthorityV2, revalidateRuntimeInstanceAdmissionV2, type RuntimeInstanceAdmissionInputV2, type RuntimeInstanceAdmissionV2 } from "./runtime-conformance-v2-admission.js";
import type { RuntimeAdmissionLease } from "@chirality/runtime-core";
import { randomUUID, createHash } from "node:crypto";
import { constants } from "node:fs";
import { lstat, open, realpath } from "node:fs/promises";
import { isIP } from "node:net";
import { CHIRALITY_ROLE_NAMES, type DelegatedAttachmentInput, type NetworkApprovalPrompt, type NetworkApprovalChoice, type NativePlanClarificationAnswers, type NativePlanClarificationQuestion, type WorkerContinuity } from "@chirality/runtime-contracts";
import type { Readable, Writable } from "node:stream";
import { isAbsolute, resolve } from "node:path";
import { RuntimeError } from "@chirality/runtime-contracts";
import { AUTHORITY_CONTRACT, SupplierAuthorityController, initializationProof, verifyProof, strictKeys, parseAuthorityJson, type AuthorityTransport, type AuthorityEnvelope, type AuthorityNotification, type AuthorityRequest } from "./supplier-authority-controller.js";
import type { HostedIdentityBindingStore, HostedIdentitySnapshot } from "./hosted-identity-binding.js";
import { CODEX_NATIVE_TOOLS_SCHEMA, digestCodexNativeToolDefinitionsV1 } from "./codex-native-tools.js";

export interface CodexAuthorityInitialize {
  runtimeProcessIncarnationId:string;supplierGeneration:string;runtimeChallenge:string;exactSupplyDigest:string;authoritySecret:Buffer;
  descriptor:{capability:string;contract:string;major:number;minor:number};v4Descriptor:{capability:string;contract:string;major:number;minor:number;method:string};
}
export function verifyAuthorityInitialization(input:CodexAuthorityInitialize,result:unknown):void {
  strictKeys(result,["contract","runtimeProcessIncarnationId","supplierGeneration","supplierChallenge","descriptor","v4Descriptor","proof"]);
  strictKeys(result.descriptor,["capability","contract","major","minor"]);strictKeys(result.v4Descriptor,["capability","contract","major","minor","method"]);
  const descriptor={capability:"chirality.local-admission-authority",contract:AUTHORITY_CONTRACT,major:1,minor:0};
  const v4Descriptor={capability:"account.identity-snapshot",contract:"chirality-supplier-account-identity/1",major:1,minor:0,method:"account/identitySnapshot"};
  for(const [key,value] of Object.entries(descriptor))if(result.descriptor[key]!==value||(input.descriptor as unknown as Record<string,unknown>)[key]!==value)throw new Error("authority-unavailable");
  for(const [key,value] of Object.entries(v4Descriptor))if(result.v4Descriptor[key]!==value||(input.v4Descriptor as unknown as Record<string,unknown>)[key]!==value)throw new Error("authority-unavailable");
  if(result.contract!==AUTHORITY_CONTRACT||result.runtimeProcessIncarnationId!==input.runtimeProcessIncarnationId||result.supplierGeneration!==input.supplierGeneration||typeof result.supplierChallenge!=="string"||!/^[A-Za-z0-9_-]{43}$/.test(result.supplierChallenge)||Buffer.from(result.supplierChallenge,"base64url").length!==32||Buffer.from(result.supplierChallenge,"base64url").toString("base64url")!==result.supplierChallenge||!/^[A-Za-z0-9_-]{43}$/.test(input.runtimeChallenge)||!/^[a-f0-9]{64}$/.test(input.exactSupplyDigest))throw new Error("authority-unavailable");
  verifyProof(initializationProof(input.authoritySecret,{contract:AUTHORITY_CONTRACT,runtimeProcessIncarnationId:input.runtimeProcessIncarnationId,supplierGeneration:input.supplierGeneration,runtimeChallenge:input.runtimeChallenge,supplierChallenge:result.supplierChallenge,exactSupplyDigest:input.exactSupplyDigest,descriptor,v4Descriptor}),result.proof);
}
export type CodexPrivateAuthorityFrame = AuthorityEnvelope<AuthorityRequest|AuthorityNotification>;

export interface CodexDynamicToolResult { success: boolean; contentItems: readonly { type: "inputText"; text: string }[] }
export interface CodexDynamicTool {
  name: string;
  description: string;
  inputSchema: Readonly<Record<string, unknown>>;
  handler(arguments_: Readonly<Record<string, unknown>>, context: { threadId: string; turnId: string; callId: string; signal: AbortSignal; nativeChild?: NativeChildCallbackContext }): Promise<CodexDynamicToolResult>;
}
export type CodexNativeChildRole = Readonly<{ kind: "configured"; name: string; basisDigest: string }> | Readonly<{ kind: "upstream" }>;
export interface NativeChildCallbackContext { associationId: string; supplierGeneration: string; rootThreadId: string; rootTurnId: string; parentThreadId: string; parentTurnId: string; selectedRole: CodexNativeChildRole; inheritedToolsDigest: string }
interface DynamicCall { signature: string; threadId: string; turnId: string; associationId?: string; controller: AbortController; done: Promise<CodexDynamicToolResult>; completed: boolean }
interface NativeChildAssociation extends NativeChildCallbackContext { childThreadId: string; childTurnId: string; rootThreadId: string; rootTurnId: string; live: boolean }
export interface CodexNativePermissions { filesystem: Readonly<Record<string, "read" | "write" | "deny">>; network: { enabled: boolean; [key: string]: unknown } }
export interface CodexSessionTransport { stdin: Writable; stdout: Readable; close(): Promise<void> }
export interface CodexTurnTerminal { threadId: string; turnId: string; status: "completed" | "failed" | "interrupted"; output: string }
export interface CodexPlanEvent { type: "plan"; threadId: string; turnId: string; eventId: string; occurredAt: string; plan: { id: string; type: "plan"; text: string } }
export interface CodexUserInputRequest {
  threadId: string; turnId: string; requestId: string | number; itemId: string;
  questions: readonly NativePlanClarificationQuestion[]; isBlocking: boolean; autoResolutionMs: number | null;
}
export type CodexSessionEvent = { type: "started"; threadId: string; turnId: string } | { type: "text"; threadId: string; turnId: string; text: string } | CodexPlanEvent | { type: "terminal"; terminal: CodexTurnTerminal };
interface Pending { resolve(value: Record<string, unknown>): void; reject(error: Error): void; timer: ReturnType<typeof setTimeout> }
interface Turn {
  threadId: string; id?: string; terminal?: CodexTurnTerminal; startedEmitted: boolean; items: Map<string, { text: string; completed: boolean }>;
  plans: Map<string, { deltaText: string; completed: boolean; completedText?: string }>;
  done: Promise<CodexTurnTerminal>; resolve(value: CodexTurnTerminal): void; reject(error: Error): void;
  timer: ReturnType<typeof setTimeout>;
  familyEnabled: boolean; familySettled: boolean; primaryTerminal?: CodexTurnTerminal;
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
function nativeIdentifier(value: unknown): string {
  if (typeof value !== "string" || Buffer.byteLength(value, "utf8") < 1 || Buffer.byteLength(value, "utf8") > 128 || value.includes("\0") || Buffer.from(value, "utf8").toString("utf8") !== value) throw protocol("Invalid native child identifier");
  return value;
}
function dynamicCallKey(threadId: string, turnId: string, callId: string, nativeChild?: NativeChildCallbackContext): string {
  return JSON.stringify(nativeChild
    ? ["child", nativeChild.associationId, threadId, turnId, callId]
    : ["primary", threadId, turnId, callId]);
}
async function stableNativeRoleInstruction(path: string): Promise<string> {
  const pathBefore = await lstat(path, { bigint: true });
  if (!pathBefore.isFile() || pathBefore.isSymbolicLink() || pathBefore.nlink !== 1n || pathBefore.size > BigInt(1024 * 1024) || await realpath(path) !== path) throw protocol("Native role instruction source is not a stable direct file");
  const handle = await open(path, constants.O_RDONLY | constants.O_NOFOLLOW);
  try {
    const before = await handle.stat({ bigint: true });
    const bytes = Buffer.alloc(Number(before.size) + 1); const read = await handle.read(bytes, 0, bytes.length, 0); const after = await handle.stat({ bigint: true }); const pathAfter = await lstat(path, { bigint: true });
    const same = (left: typeof before, right: typeof before) => left.dev === right.dev && left.ino === right.ino && left.size === right.size && left.mtimeNs === right.mtimeNs && left.ctimeNs === right.ctimeNs;
    if (!same(pathBefore, before) || !same(before, after) || !same(after, pathAfter) || read.bytesRead !== Number(before.size) || await realpath(path) !== path) throw protocol("Native role instruction source changed while it was read");
    const source = bytes.subarray(0, read.bytesRead).toString("utf8");
    if (Buffer.from(source, "utf8").length !== read.bytesRead || !source.startsWith("developer_instructions = ") || !source.endsWith("\n")) throw protocol("Native role instruction source is invalid");
    const instruction: unknown = JSON.parse(source.slice("developer_instructions = ".length, -1));
    if (typeof instruction !== "string") throw protocol("Native role instruction source is invalid");
    return instruction;
  } finally { await handle.close(); }
}
/** Network callback correlation IDs are opaque supplier tokens, not primary thread/turn identifiers. */
function networkApprovalItemId(value: unknown, environmentId: unknown, host: string, protocolName: string): string {
  if (typeof value !== "string" || !value.startsWith("network#")) return identifier(value);
  // Supplier: network#environment#protocol#lowercase-host#u16-port#v4-uuid.
  // Environment 128 is an adapter bound, not an upstream guarantee; host 253 is our existing context bound.
  // 444 = 7 + 128 + 10 + 253 + 5 + 36 + five separators. Keep the original token/signature intact.
  if (value.length > 444 || /[\x00-\x20\x7f]/.test(value)) throw protocol("Invalid network approval item ID");
  const parts = value.split("#");
  const protocolLabel = protocolName === "socks5Tcp" ? "socks5-tcp" : protocolName === "socks5Udp" ? "socks5-udp" : protocolName;
  if (parts.length !== 6 || parts[1] !== identifier(environmentId) || parts[2] !== protocolLabel || parts[3] !== host.toLowerCase()
    || !/^(?:0|[1-9][0-9]{0,4})$/.test(parts[4]!) || Number(parts[4]) > 65535
    || !/^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/.test(parts[5]!)) throw protocol("Invalid network approval item ID");
  return value;
}
function ignoredNetworkPolicyChoice(value: unknown, host: string): void {
  const choice = object(value), network = object(choice.applyNetworkPolicyAmendment), amendment = object(network.network_policy_amendment);
  if (Object.keys(choice).join(",") !== "applyNetworkPolicyAmendment" || Object.keys(network).join(",") !== "network_policy_amendment"
    || Object.keys(amendment).sort().join(",") !== "action,host" || amendment.host !== host || (amendment.action !== "allow" && amendment.action !== "deny")) throw protocol("Unknown approval decision");
  // Recognized persistent-rule choices are omitted, never executed or mapped to a one-time grant.
}
/**
 * Known-method actor, not a sandbox or launch/authentication authority. The trusted
 * host provides an already-contained transport and checks continuity before thread
 * selection. Current documented turn events are a candidate adapter dialect, not
 * evidence that the pinned 0.149 payload has completed an authenticated turn.
 */
export class CodexTurnSession {
  static privateAuthorityTransport(transport:CodexSessionTransport):AuthorityTransport {
    let subscribed=false,closed=false;let buffer=Buffer.alloc(0);let fail:(()=>void)|undefined;let detach:(()=>void)|undefined;
    return {subscribe(onFrame,onFailure){if(subscribed||closed)throw new Error("authority-unavailable");subscribed=true;fail=onFailure;
      const data=(chunk:Buffer)=>{try{buffer=Buffer.concat([buffer,chunk]);if(buffer.length>1048576)throw new Error("request-malformed");let end:number;while((end=buffer.indexOf(10))>=0){const line=buffer.subarray(0,end);buffer=buffer.subarray(end+1);parseAuthorityJson(line);onFrame(line);}}catch{onFailure();}};
      const failed=()=>onFailure();transport.stdout.on("data",data);transport.stdout.on("end",failed);transport.stdout.on("error",failed);transport.stdin.on("error",failed);
      detach=()=>{transport.stdout.off("data",data);transport.stdout.off("end",failed);transport.stdout.off("error",failed);transport.stdin.off("error",failed);};return detach;},
      async send(frame){if(closed||!subscribed)throw new Error("authority-unavailable");const wire=JSON.stringify(frame)+"\n";await new Promise<void>((resolve,reject)=>{transport.stdin.write(wire,error=>error?reject(new Error("authority-unavailable")):resolve());});},
      async close(){if(closed)return;closed=true;detach?.();await transport.close();}
    };
  }

  private readonly commandNetworkPosture: "off" | "ask-per-destination" | "on";
  private readonly networkApprovals = new Map<string, { prompt: NetworkApprovalPrompt; requestId: string | number; signature: string; state: "pending" | "sending" | "sent" | "resolved" }>();
  private readonly userInputRequests = new Map<string, { prompt: CodexUserInputRequest; signature: string; state: "pending" | "sending" | "sent" | "resolved" }>();
  private readonly requests = new Map<number, Pending>();
  private nextId = 1;
  private buffer: Buffer = Buffer.alloc(0);
  private received = 0;
  private ready = false;
  private authorityInitialized=false;
  private supplierAuthority?: SupplierAuthorityController;
  private supplierGeneration?: string;
  private authorityFrame?: (raw:Uint8Array)=>void;
  private authorityFailed?:()=>void;
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
  private readonly nativeChildAssociations = new Map<string, NativeChildAssociation>();
  private retryableErrors = 0;
  private readonly tools = new Map<string, CodexDynamicTool>();
  private inheritableTools: readonly { name: string; description: string; inputSchema: Readonly<Record<string, unknown>> }[] | undefined;
  private inheritableToolsDigest: string | undefined;
  private readonly toolCalls = new Map<string, DynamicCall>();
  private readonly resolvedServerRequests = new Set<string>();
  private readonly toolRequestIds = new Map<string, string>();
  private expectedPermissions: CodexNativePermissions | undefined;
  private expectedNativeRoles: { digest: string; configOverrides: readonly string[]; roles: Readonly<Record<string, { description: string; config_file: string; basisDigest?: string }>> } | undefined;
  private policyCwd: string | undefined;
  private readonly nativePolicy: Readonly<{ permissionProfile: string; policyDigest: string }> | undefined;
  private login: { state: "pending" | "completed" | "failed"; loginId?: string } | undefined;
  constructor(private readonly options: { runtimeV2?: { instanceInput: RuntimeInstanceAdmissionInputV2; instanceAdmission: RuntimeInstanceAdmissionV2 }; transport: CodexSessionTransport; requestTimeoutMs?: number; turnTimeoutMs?: number; purpose?: "turn" | "login"; permissionProfile?: string; policyDigest?: string; nativeSkills?: "disabled"; dynamicTools?: readonly CodexDynamicTool[]; toolTimeoutMs?: number; commandNetworkPosture?: "off" | "ask-per-destination" | "on" }) {
    this.commandNetworkPosture = options.commandNetworkPosture ?? "off";
    if (options.commandNetworkPosture !== undefined && !["off", "ask-per-destination", "on"].includes(options.commandNetworkPosture)) throw invalid("Invalid trusted command network posture");
    if ((options.dynamicTools?.length ?? 0) > 32 || (options.purpose === "login" && options.dynamicTools?.length)) throw invalid("Unsupported dynamic tool registry");
    this.installDynamicTools(options.dynamicTools ?? []);
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
  /** Installs host callbacks once, after private admission and before thread selection. */
  installDynamicTools(tools: readonly CodexDynamicTool[]): void {
    if (this.threadId || this.active || this.selecting || this.tools.size || tools.length > 32 || this.options.purpose === "login") {
      if (tools.length) throw invalid("Dynamic tools must be installed once before thread selection");
      return;
    }
    for (const tool of tools) {
      if (!/^[A-Za-z][A-Za-z0-9_-]{0,63}$/.test(tool.name) || this.tools.has(tool.name) || typeof tool.description !== "string" || !tool.description.trim() || tool.description.length > 4096 || typeof tool.handler !== "function") throw invalid("Invalid immutable dynamic tool declaration");
      const schema = JSON.parse(JSON.stringify(tool.inputSchema)) as Record<string, unknown>;
      if (Buffer.byteLength(JSON.stringify(schema)) > 16384) throw invalid("Dynamic tool schema exceeds bound");
      checkToolSchema(schema);
      if (schema.type !== "object") throw invalid("Dynamic tool input must be a closed object");
      this.tools.set(tool.name, Object.freeze({ name: tool.name, description: tool.description, inputSchema: freezeTree(schema), handler: tool.handler }));
    }
  }
  /** Installs the exact Runtime-authorized inheritable subset before root selection. */
  async installInheritableTools(tools: readonly { name: string; description: string; inputSchema: Readonly<Record<string, unknown>> }[]): Promise<void> {
    if (this.options.nativeSkills !== "disabled") {
      return;
    }
    if (this.threadId || this.active || this.selecting || this.inheritableTools !== undefined) throw invalid("Inherited tools must be installed once before thread selection");
    const available = new Map([...this.tools.values()].map(tool => [tool.name, tool]));
    const copy = tools.map(tool => ({ name: tool.name, description: tool.description, inputSchema: structuredClone(tool.inputSchema) }));
    for (const tool of copy) {
      const installed = available.get(tool.name);
      if (!installed || JSON.stringify({ name: installed.name, description: installed.description, inputSchema: installed.inputSchema }) !== JSON.stringify(tool)) throw invalid("Inherited tool differs from the installed Runtime definition");
    }
    this.inheritableToolsDigest = digestCodexNativeToolDefinitionsV1(copy);
    if (!this.expectedNativeRoles) throw invalid("Inherited native tools require verified native role configuration");
    const roles: Record<string, { description: string; config_file: string; basisDigest: string }> = {};
    for (const [name, role] of Object.entries(this.expectedNativeRoles.roles)) {
      const instruction = await stableNativeRoleInstruction(role.config_file);
      roles[name] = { ...role, basisDigest: createHash("sha256").update(instruction).digest("hex") };
    }
    this.expectedNativeRoles = Object.freeze({ ...this.expectedNativeRoles, roles: Object.freeze(roles) });
    this.inheritableTools = Object.freeze(copy.map(tool => Object.freeze({ ...tool, inputSchema: freezeTree(tool.inputSchema) })));
  }
  private fail(error: RuntimeError): void {
    if (this.failure) return;
    this.failure = error;
    this.authorityFailed?.();
    this.resolveNetworkApprovals();
    for (const call of this.toolCalls.values()) if (!call.completed) call.controller.abort();
    if (this.login?.state === "pending") this.login.state = "failed";
    for (const pending of this.requests.values()) { clearTimeout(pending.timer); pending.reject(error); }
    this.requests.clear();
    if (this.active) { clearTimeout(this.active.timer); this.active.reject(error); this.active = undefined; }
    this.wake?.(); this.wake = undefined;
    this.closing ??= this.options.transport.close();
    void this.closing.catch(() => {});
  }
  private assertReady(): void { if (this.failure) throw this.failure; if (!this.ready) throw invalid("Initialize Codex session first"); }
  private write(message: Record<string, unknown>): void {
    const data = JSON.stringify(message) + "\n";
    if (Buffer.byteLength(data) > 262144) throw invalid("Codex request is too large");
    this.options.transport.stdin.write(data, error => { if (error) this.fail(protocol("Codex input failed")); });
  }
  private request(method: string, params?: Record<string, unknown>): Promise<Record<string, unknown>> {
    if (this.failure) return Promise.reject(this.failure);
    if (this.requests.size >= 8) return Promise.reject(invalid("Too many outstanding Codex requests"));
    const id = this.nextId++;
    return new Promise((resolveRequest, reject) => {
      const timer = setTimeout(() => this.fail(protocol("Codex request timed out")), this.options.requestTimeoutMs ?? 10000);
      this.requests.set(id, { resolve: resolveRequest, reject, timer });
      try { this.write(params === undefined ? { id, method } : { id, method, params }); }
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
        const message = object(parseAuthorityJson(line));
        if(message.contract===AUTHORITY_CONTRACT){if(!this.authorityFrame)throw protocol("Unsolicited private authority frame");this.authorityFrame(line);continue;}
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
    if (message.method === "item/tool/requestUserInput") { this.userInputRequest(message); return; }
    if (message.method !== "item/tool/call") throw protocol("Unsupported Codex server request; no approval granted");
    const requestId = message.id;
    if ((typeof requestId !== "string" && typeof requestId !== "number") || (typeof requestId === "number" && !Number.isSafeInteger(requestId)) || String(requestId).length > 128) throw protocol("Invalid server request ID");
    const params = object(message.params), active = this.active;
    const childCarrierPresent = params.chiralityRuntime !== undefined;
    const threadId = childCarrierPresent ? nativeIdentifier(params.threadId) : identifier(params.threadId);
    const turnId = childCarrierPresent ? nativeIdentifier(params.turnId) : identifier(params.turnId);
    const callId = identifier(params.callId);
    let nativeChild: NativeChildCallbackContext | undefined;
    if (params.chiralityRuntime !== undefined) {
      const carrier = object(params.chiralityRuntime);
      if (Object.keys(carrier).sort().join(",") !== "associationId,schema" || carrier.schema !== "chirality-native-child-call/v1" || typeof carrier.associationId !== "string") throw protocol("Invalid native child callback carrier");
      const association = this.nativeChildAssociations.get(carrier.associationId);
      if (!active?.id || !association || !association.live || association.childThreadId !== threadId || association.childTurnId !== turnId || association.rootTurnId !== active.id || association.rootThreadId !== active.threadId) throw protocol("Dynamic callback is not bound to a live native child association");
      nativeChild = { associationId: association.associationId, supplierGeneration: this.supplierGeneration!, rootThreadId: association.rootThreadId, rootTurnId: association.rootTurnId, parentThreadId: association.parentThreadId, parentTurnId: association.parentTurnId, selectedRole: association.selectedRole, inheritedToolsDigest: association.inheritedToolsDigest };
    } else if (!active?.id || active.id !== turnId || threadId !== this.threadId || threadId !== active.threadId) throw protocol("Dynamic callback is not bound to the active primary turn");
    const tool = this.tools.get(String(params.tool));
    if (!tool) throw protocol("Dynamic tool is not registered by the trusted host");
    if (nativeChild && !this.inheritableTools?.some(inherited => inherited.name === tool.name)) throw protocol("Native child requested a non-inherited dynamic tool");
    const input = object(params.arguments);
    if (Buffer.byteLength(JSON.stringify(input)) > 65536 || !matchesToolSchema(input, tool.inputSchema)) throw protocol("Dynamic tool arguments violate the closed schema");
    const signature = JSON.stringify([threadId, turnId, callId, params.tool, input, nativeChild?.associationId ?? null]);
    const requestKey = `${typeof requestId}:${requestId}`;
    if (this.networkApprovals.has(requestKey) || this.resolvedServerRequests.has(requestKey)) throw protocol("Reused or resolved server request ID");
    const previousRequest = this.toolRequestIds.get(requestKey);
    if (previousRequest !== undefined) { if (previousRequest !== signature) throw protocol("Conflicting duplicate dynamic request"); return; }
    if (this.toolRequestIds.size >= 128) throw protocol("Dynamic request inventory bound exceeded");
    this.toolRequestIds.set(requestKey, signature);
    const callKey = dynamicCallKey(threadId, turnId, callId, nativeChild);
    let call = this.toolCalls.get(callKey);
    if (call && call.signature !== signature) throw protocol("Conflicting duplicate dynamic call");
    if (!call) {
      if (this.toolCalls.size >= 64 || [...this.toolCalls.values()].filter(value => !value.completed).length >= 8) throw protocol("Dynamic callback concurrency bound exceeded");
      const controller = new AbortController();
      const entry: DynamicCall = { signature, threadId, turnId, ...(nativeChild ? { associationId: nativeChild.associationId } : {}), controller, done: Promise.resolve({ success: false, contentItems: [] }), completed: false };
      this.toolCalls.set(callKey, entry);
      entry.done = (async () => {
        let timer: ReturnType<typeof setTimeout> | undefined;
        let abort: (() => void) | undefined;
        try {
          const interrupted = new Promise<never>((_, reject) => { abort = () => reject(protocol("Dynamic call cancelled")); controller.signal.addEventListener("abort", abort, { once: true }); timer = setTimeout(() => controller.abort(), this.options.toolTimeoutMs ?? 30000); });
          const result = await Promise.race([Promise.resolve().then(() => { if (controller.signal.aborted) throw protocol("Dynamic call cancelled before dispatch"); return tool.handler(freezeTree(JSON.parse(JSON.stringify(input)) as Record<string, unknown>), { threadId, turnId, callId, signal: controller.signal, ...(nativeChild ? { nativeChild: structuredClone(nativeChild) } : {}) }); }), interrupted]);
          if (!result || Object.keys(result).sort().join(",") !== "contentItems,success" || typeof result.success !== "boolean" || !Array.isArray(result.contentItems) || result.contentItems.length > 16 || result.contentItems.some(item => !item || Object.keys(item).sort().join(",") !== "text,type" || item.type !== "inputText" || typeof item.text !== "string" || Buffer.byteLength(item.text) > 65536) || Buffer.byteLength(JSON.stringify(result)) > 262144) throw protocol("Invalid bounded dynamic tool result");
          return { success: result.success, contentItems: result.contentItems.map(item => ({ type: "inputText" as const, text: item.text })) };
        } catch { return { success: false, contentItems: [{ type: "inputText" as const, text: "Host tool failed or was cancelled." }] }; }
        finally { clearTimeout(timer); if (abort) controller.signal.removeEventListener("abort", abort); entry.completed = true; this.finishActiveIfSettled(); }
      })();
      call = entry;
    }
    void call.done.then(result => {
      const associationLive = nativeChild === undefined || this.nativeChildAssociations.get(nativeChild.associationId)?.live === true;
      const rootMembership = nativeChild === undefined ? this.active?.id === turnId : this.active?.id === nativeChild.rootTurnId && this.active.threadId === nativeChild.rootThreadId;
      if (this.resolvedServerRequests.has(requestKey) || this.failure || !rootMembership || !associationLive || (nativeChild === undefined && this.threadId !== threadId)) return;
      try { this.write({ id: requestId, result }); } catch (error) { this.fail(error instanceof RuntimeError ? error : protocol("Dynamic response failed")); }
    });
  }
  private userInputRequest(message: Record<string, unknown>): void {
    const requestId = message.id;
    if ((typeof requestId !== "string" && typeof requestId !== "number") || (typeof requestId === "number" && !Number.isSafeInteger(requestId)) || String(requestId).length > 128) throw protocol("Invalid user-input request ID");
    const params = object(message.params), active = this.active;
    const threadId = identifier(params.threadId), turnId = identifier(params.turnId), itemId = identifier(params.itemId);
    if (!active?.id || active.id !== turnId || active.threadId !== threadId || this.threadId !== threadId) throw protocol("User-input request is outside the active primary turn");
    if (!Array.isArray(params.questions) || params.questions.length < 1 || params.questions.length > 3) throw protocol("Invalid native Plan questions");
    const questions = params.questions.map(value => {
      const q = object(value), questionId = identifier(q.id);
      if (typeof q.header !== "string" || !q.header.trim() || q.header.length > 64 || typeof q.question !== "string" || !q.question.trim() || Buffer.byteLength(q.question) > 8192) throw protocol("Invalid native Plan question");
      const sourceOptions = q.options === undefined || q.options === null ? [] : q.options;
      if (!Array.isArray(sourceOptions) || sourceOptions.length > 16) throw protocol("Invalid native Plan question options");
      const options = sourceOptions.map(value => {
        const option = object(value);
        if (typeof option.label !== "string" || !option.label.trim() || option.label.length > 256 || typeof option.description !== "string" || Buffer.byteLength(option.description) > 4096) throw protocol("Invalid native Plan question option");
        return { label: option.label, description: option.description };
      });
      if (q.isOther !== undefined && typeof q.isOther !== "boolean") throw protocol("Invalid native Plan other-answer flag");
      if (q.isSecret !== undefined && typeof q.isSecret !== "boolean") throw protocol("Invalid native Plan secret-answer flag");
      return { id: questionId, header: q.header, question: q.question, options, isOther: q.isOther === true, isSecret: q.isSecret === true };
    });
    if (new Set(questions.map(question => question.id)).size !== questions.length) throw protocol("Duplicate native Plan question identity");
    if (params.isBlocking !== undefined && typeof params.isBlocking !== "boolean") throw protocol("Invalid native Plan blocking flag");
    if (params.autoResolutionMs !== undefined && params.autoResolutionMs !== null && (!Number.isSafeInteger(params.autoResolutionMs) || Number(params.autoResolutionMs) < 0)) throw protocol("Invalid native Plan auto-resolution interval");
    const prompt: CodexUserInputRequest = { threadId, turnId, requestId, itemId, questions, isBlocking: params.isBlocking !== false, autoResolutionMs: params.autoResolutionMs === undefined ? null : params.autoResolutionMs as number | null };
    const key = `${typeof requestId}:${requestId}`, signature = JSON.stringify(params), prior = this.userInputRequests.get(key);
    if (prior) { if (prior.signature !== signature || prior.state !== "pending") throw protocol("Conflicting or stale user-input request"); return; }
    if (this.userInputRequests.size >= 64 || this.networkApprovals.has(key) || this.toolRequestIds.has(key)) throw protocol("User-input request inventory bound exceeded or ID reused");
    this.userInputRequests.set(key, { prompt, signature, state: "pending" });
  }
  pendingNativePlanClarifications(): readonly CodexUserInputRequest[] {
    if (this.failure) throw this.failure;
    if (!this.ready) return [];
    return [...this.userInputRequests.values()].filter(entry => entry.state === "pending" && entry.prompt.turnId === this.active?.id && entry.prompt.threadId === this.threadId).map(entry => structuredClone(entry.prompt));
  }
  async replyNativePlanClarification(requestId: string | number, answers: NativePlanClarificationAnswers): Promise<{ sent: true }> {
    this.assertReady();
    const key = `${typeof requestId}:${requestId}`, entry = this.userInputRequests.get(key);
    if (!entry || entry.state !== "pending" || entry.prompt.turnId !== this.active?.id || entry.prompt.threadId !== this.threadId) throw invalid("Unknown or resolved native Plan clarification");
    if (!answers || typeof answers !== "object" || Array.isArray(answers) || Object.keys(answers).sort().join(",") !== entry.prompt.questions.map(question => question.id).sort().join(",")) throw invalid("Native Plan answers must match every question identity");
    const copy: Record<string, { answers: string[] }> = {};
    for (const question of entry.prompt.questions) {
      const answer = answers[question.id];
      if (!answer || typeof answer !== "object" || Array.isArray(answer) || Object.keys(answer).join(",") !== "answers" || !Array.isArray(answer.answers) || answer.answers.length < 1 || answer.answers.length > 16 || answer.answers.some(value => typeof value !== "string" || Buffer.byteLength(value) > 8192)) throw invalid("Invalid native Plan answer payload");
      copy[question.id] = { answers: [...answer.answers] };
    }
    const frame = JSON.stringify({ id: requestId, result: { answers: copy } }) + "\n";
    entry.state = "sending";
    await new Promise<void>((resolveWrite, rejectWrite) => {
      let settled = false;
      const finish = (error?: Error | null) => {
        if (settled) return; settled = true; clearTimeout(timer);
        if (error || this.failure) { const failure = this.failure ?? protocol("Native Plan answer transport write failed"); this.fail(failure); rejectWrite(failure); }
        else resolveWrite();
      };
      const timer = setTimeout(() => finish(protocol("Native Plan answer transport write timed out")), this.options.requestTimeoutMs ?? 10000);
      try { this.options.transport.stdin.write(frame, error => finish(error)); }
      catch { finish(protocol("Native Plan answer transport write failed")); }
    });
    if (entry.state === "sending") entry.state = "sent";
    return { sent: true };
  }
  private resolveNetworkApprovals(turnId?: string): void {
    for (const entry of this.networkApprovals.values()) if (!turnId || entry.prompt.turnId === turnId) entry.state = "resolved";
  }
  private networkApprovalRequest(message: Record<string, unknown>): void {
    if (this.commandNetworkPosture !== "ask-per-destination") throw protocol("Network approval requires trusted ask posture");
    const requestId = message.id;
    if ((typeof requestId !== "string" && typeof requestId !== "number") || (typeof requestId === "number" && !Number.isSafeInteger(requestId)) || String(requestId).length > 128) throw protocol("Invalid network request ID");
    const params = object(message.params), active = this.active;
    const threadId = identifier(params.threadId), turnId = identifier(params.turnId);
    if (!active?.id || active.id !== turnId || active.threadId !== threadId || this.threadId !== threadId) throw protocol("Network request is outside the active primary turn");
    if (!Number.isSafeInteger(params.startedAtMs) || Number(params.startedAtMs) < 0) throw protocol("Invalid network approval timestamp");
    // Never turn a combined filesystem/exec-policy prompt into a network-only grant.
    if (["additionalPermissions", "proposedExecpolicyAmendment", "command", "cwd", "commandActions"].some(key => params[key] !== undefined && params[key] !== null)) throw protocol("Unsupported combined approval request");
    const context = object(params.networkApprovalContext), host = context.host, protocolName = context.protocol;
    if (Object.keys(context).sort().join(",") !== "host,protocol" || typeof host !== "string" || host.length > 253 || (!isIP(host.replace(/^\[|\]$/g, "")) && !host.split(".").every(label => /^[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?$/i.test(label))) || !["http", "https", "socks5Tcp", "socks5Udp"].includes(String(protocolName))) throw protocol("Invalid network destination context");
    networkApprovalItemId(params.itemId, params.environmentId, host, String(protocolName));
    if (!Array.isArray(params.availableDecisions) || params.availableDecisions.length > 16) throw protocol("Exact available approval decisions required");
    const availableDecisions: NetworkApprovalChoice[] = [];
    for (const choice of params.availableDecisions) {
      if (choice === "accept") availableDecisions.push("allow"); else if (choice === "decline") availableDecisions.push("deny"); else if (choice === "acceptForSession") availableDecisions.push("acceptForSession");
      else if (choice === "cancel") continue;
      else if (choice && typeof choice === "object") ignoredNetworkPolicyChoice(choice, host);
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
  private finishActiveIfSettled(): void {
    const active = this.active;
    if (!active?.primaryTerminal || (active.familyEnabled && !active.familySettled)) return;
    if ([...this.toolCalls.values()].some(call => !call.completed && (call.turnId === active.id || call.associationId !== undefined))) return;
    const terminal = active.primaryTerminal;
    this.emit({ type: "terminal", terminal: { ...terminal } });
    clearTimeout(active.timer); this.terminals.set(terminal.turnId, terminal); active.terminal = terminal; this.active = undefined;
    active.resolve(terminal);
  }
  private nativeChildNotification(method: string, value: unknown): void {
    if (this.options.nativeSkills !== "disabled" || this.inheritableTools === undefined || !this.inheritableToolsDigest || !this.supplierGeneration) throw protocol("Native child lifecycle requires an admitted inherited-tool family");
    const params = object(value), active = this.active;
    if (!active?.id || !active.familyEnabled) throw protocol("Native child lifecycle is outside the active root family");
    if (method === "chirality/nativeChild/turnStarted") {
      if (active.familySettled || Object.keys(params).sort().join(",") !== "associationId,childThreadId,childTurnId,inheritedToolsDigest,parentThreadId,parentTurnId,schema,selectedRole,supplierGeneration" || params.schema !== "chirality-native-child-association/v1" || params.supplierGeneration !== this.supplierGeneration) throw protocol("Invalid native child association");
      const associationId = params.associationId;
      if (typeof associationId !== "string" || !/^[a-f0-9]{32}$/.test(associationId) || this.nativeChildAssociations.has(associationId)) throw protocol("Invalid or reused native child association identity");
      const parentThreadId = nativeIdentifier(params.parentThreadId), parentTurnId = nativeIdentifier(params.parentTurnId);
      const childThreadId = nativeIdentifier(params.childThreadId), childTurnId = nativeIdentifier(params.childTurnId);
      const directRootParent = parentThreadId === active.threadId && parentTurnId === active.id;
      const parentAssociation = directRootParent ? undefined
        : [...this.nativeChildAssociations.values()].find(value => value.rootThreadId === active.threadId && value.rootTurnId === active.id && value.childThreadId === parentThreadId && value.childTurnId === parentTurnId);
      if ((!directRootParent && !parentAssociation?.live) || params.inheritedToolsDigest !== this.inheritableToolsDigest) throw protocol("Native child association differs from its live root family or inherited definitions");
      const selected = object(params.selectedRole); let selectedRole: CodexNativeChildRole;
      if (selected.kind === "upstream" && Object.keys(selected).join(",") === "kind") selectedRole = Object.freeze({ kind: "upstream" });
      else if (selected.kind === "configured" && Object.keys(selected).sort().join(",") === "basisDigest,kind,name") {
        const name = nativeIdentifier(selected.name), basisDigest = selected.basisDigest;
        const expected = this.expectedNativeRoles?.roles[name];
        if (typeof basisDigest !== "string" || !/^[a-f0-9]{64}$/.test(basisDigest) || !expected || expected.basisDigest !== basisDigest) throw protocol("Native child configured role differs from the trusted applied instruction");
        selectedRole = Object.freeze({ kind: "configured", name, basisDigest });
      } else throw protocol("Invalid native child selected role");
      if ([...this.nativeChildAssociations.values()].some(value => value.live && (value.childThreadId === childThreadId && value.childTurnId === childTurnId))) throw protocol("Native child turn is already associated");
      this.nativeChildAssociations.set(associationId, Object.freeze({ associationId, supplierGeneration: this.supplierGeneration, parentThreadId, parentTurnId, childThreadId, childTurnId, rootThreadId: active.threadId, rootTurnId: active.id, selectedRole, inheritedToolsDigest: this.inheritableToolsDigest, live: true }));
      this.childAssociations.set(childThreadId, parentTurnId); return;
    }
    if (method === "chirality/nativeChild/turnFinished") {
      if (Object.keys(params).sort().join(",") !== "associationId,childThreadId,childTurnId,reason,schema,supplierGeneration" || params.schema !== "chirality-native-child-terminal/v1" || params.supplierGeneration !== this.supplierGeneration || !["completed", "cancelled", "failed"].includes(String(params.reason))) throw protocol("Invalid native child terminal");
      const association = typeof params.associationId === "string" ? this.nativeChildAssociations.get(params.associationId) : undefined;
      if (!association?.live || association.childThreadId !== nativeIdentifier(params.childThreadId) || association.childTurnId !== nativeIdentifier(params.childTurnId)) throw protocol("Unknown or retired native child terminal");
      if ([...this.toolCalls.values()].some(call => call.associationId === association.associationId && !call.completed)) throw protocol("Native child terminal preceded callback completion");
      this.nativeChildAssociations.set(association.associationId, Object.freeze({ ...association, live: false })); this.finishActiveIfSettled(); return;
    }
    if (Object.keys(params).sort().join(",") !== "rootThreadId,rootTurnId,schema,supplierGeneration" || params.schema !== "chirality-native-family-settled/v1" || params.supplierGeneration !== this.supplierGeneration || nativeIdentifier(params.rootThreadId) !== active.threadId || nativeIdentifier(params.rootTurnId) !== active.id || !active.primaryTerminal || active.familySettled || [...this.nativeChildAssociations.values()].some(value => value.rootTurnId === active.id && value.live)) throw protocol("Invalid or premature native child family settlement");
    active.familySettled = true; this.finishActiveIfSettled();
  }
  private notification(method: string, value: unknown): void {
    if (["chirality/nativeChild/turnStarted", "chirality/nativeChild/turnFinished", "chirality/nativeChild/familySettled"].includes(method)) { this.nativeChildNotification(method, value); return; }
    if (method === "serverRequest/resolved") {
      const params = object(value), threadId = identifier(params.threadId), id = params.requestId;
      if ((typeof id !== "string" && typeof id !== "number") || (typeof id === "number" && !Number.isSafeInteger(id)) || String(id).length > 128) throw protocol("Invalid resolved request ID");
      const entry = this.networkApprovals.get(`${typeof id}:${id}`);
      if (entry) { if (entry.prompt.threadId !== threadId) throw protocol("Resolved approval thread mismatch"); entry.state = "resolved"; }
      else {
        const key = `${typeof id}:${id}`, question = this.userInputRequests.get(key), signature = this.toolRequestIds.get(key);
        if (question) { if (question.prompt.threadId !== threadId) throw protocol("Resolved user-input thread mismatch"); question.state = "resolved"; return; }
        if (signature) {
          const [callThread, callTurn, callId, , , associationId] = JSON.parse(signature);
          if (callThread !== threadId) throw protocol("Resolved tool thread mismatch");
          const association = associationId === null ? undefined : this.nativeChildAssociations.get(associationId);
          const nativeChild = association === undefined ? undefined : { associationId: association.associationId, supplierGeneration: this.supplierGeneration!, rootThreadId: association.rootThreadId, rootTurnId: association.rootTurnId, parentThreadId: association.parentThreadId, parentTurnId: association.parentTurnId, selectedRole: association.selectedRole, inheritedToolsDigest: association.inheritedToolsDigest };
          this.resolvedServerRequests.add(key); this.toolCalls.get(dynamicCallKey(callThread, callTurn, callId, nativeChild))?.controller.abort();
        } else this.quarantine(method, undefined);
      }
      return;
    }
    if (!["account/login/completed", "thread/started", "turn/started", "turn/completed", "item/agentMessage/delta", "item/plan/delta", "item/started", "item/completed"].includes(method)) { this.quarantine(method, value); return; }
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
    if (method === "turn/started") {
      if (object(params.turn).status !== "inProgress") throw protocol("Unsupported started turn status");
      if (!active.startedEmitted) { active.startedEmitted = true; this.emit({ type: "started", threadId, turnId }); }
      return;
    }
    if (method === "turn/completed") {
      const status = object(params.turn).status;
      if (status !== "completed" && status !== "failed" && status !== "interrupted") throw protocol("Unsupported terminal status");
      if ([...this.toolCalls.values()].some(call => call.turnId === turnId && !call.completed && !call.controller.signal.aborted)) throw protocol("Codex terminal preceded host tool completion");
      this.resolveNetworkApprovals(turnId);
      for (const entry of this.userInputRequests.values()) if (entry.prompt.turnId === turnId) entry.state = "resolved";
      const terminal: CodexTurnTerminal = { threadId, turnId, status, output: [...active.items.values()].map(item => item.text).join("") };
      if (active.primaryTerminal && JSON.stringify(active.primaryTerminal) !== JSON.stringify(terminal)) throw protocol("Conflicting duplicate Codex terminal");
      active.primaryTerminal = terminal; this.finishActiveIfSettled(); return;
    }
    if (method === "item/agentMessage/delta") {
      const itemId = identifier(params.itemId), text = params.delta;
      if (typeof text !== "string" || Buffer.byteLength(text) > 65536) throw protocol("Unsupported text delta");
      const item = active.items.get(itemId) ?? { text: "", completed: false };
      if (item.completed || Buffer.byteLength(item.text) + Buffer.byteLength(text) > 262144) throw protocol("Late or oversized text delta");
      item.text += text; active.items.set(itemId, item); this.emit({ type: "text", threadId, turnId, text }); return;
    }
    if (method === "item/plan/delta") {
      const itemId = identifier(params.itemId), text = params.delta;
      if (typeof text !== "string" || Buffer.byteLength(text) > 65536) throw protocol("Unsupported plan delta");
      const item = active.plans.get(itemId) ?? { deltaText: "", completed: false };
      if (item.completed || Buffer.byteLength(item.deltaText) + Buffer.byteLength(text) > 262144) throw protocol("Late or oversized plan delta");
      item.deltaText += text; active.plans.set(itemId, item); return;
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
      if (item.type === "plan") {
        if (method === "item/started") { if (!active.plans.has(itemId)) active.plans.set(itemId, { deltaText: "", completed: false }); return; }
        if (typeof item.text !== "string" || Buffer.byteLength(item.text) > 262144) throw protocol("Unsupported completed plan");
        const prior = active.plans.get(itemId);
        if (prior?.completed) { if (prior.completedText !== item.text) throw protocol("Conflicting completed plan"); return; }
        active.plans.set(itemId, { deltaText: prior?.deltaText ?? "", completed: true, completedText: item.text });
        this.emit({ type: "plan", threadId, turnId, eventId: randomUUID(), occurredAt: new Date().toISOString(), plan: { id: itemId, type: "plan", text: item.text } }); return;
      }
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
  async initializeAuthority(input:CodexAuthorityInitialize):Promise<void> {
    if(this.ready||this.initializing)throw invalid("Codex connection initializes once");this.initializing=true;
    try {const result=await this.request("initialize",{clientInfo:{name:"chirality_runtime_private_authority",version:"0.0.0"},capabilities:{experimentalApi:true},chiralityAdmissionAuthority:{contract:AUTHORITY_CONTRACT,runtimeProcessIncarnationId:input.runtimeProcessIncarnationId,supplierGeneration:input.supplierGeneration,runtimeChallenge:input.runtimeChallenge}});
      verifyAuthorityInitialization(input,result.chiralityAdmissionAuthority);this.authorityInitialized=true;this.write({method:"initialized"});this.ready=true;
    }catch{this.fail(protocol("Private authority initialization unavailable"));throw this.failure;}finally{this.initializing=false;}
  }
  private async privateAuthoritySnapshot(supplierGeneration:string):Promise<HostedIdentitySnapshot> {
    this.assertReady();if(!this.authorityInitialized)throw invalid("Private authority initialization required");
    try{const response=await this.request("account/identitySnapshot",{schema:"chirality-supplier-account-identity-request/1",expectedSupplierGeneration:supplierGeneration});
      strictKeys(response,["schema","state","supplierGeneration","identityGeneration","accountUserId","providerWorkspaceId"]);
      if(response.schema!=="chirality-supplier-account-identity-response/1"||response.state!=="available"||response.supplierGeneration!==supplierGeneration)throw new Error("authority-unavailable");
      for(const key of ["supplierGeneration","identityGeneration","accountUserId","providerWorkspaceId"])if(typeof response[key]!=="string"||!/^[\x21-\x7e]{1,128}$/.test(response[key]))throw new Error("authority-unavailable");
      const canonical={schema:response.schema,state:response.state,supplierGeneration:response.supplierGeneration,identityGeneration:response.identityGeneration,accountUserId:response.accountUserId,providerWorkspaceId:response.providerWorkspaceId};
      return {supplierGeneration,identityGeneration:response.identityGeneration as string,accountUserId:response.accountUserId as string,providerWorkspaceId:response.providerWorkspaceId as string,snapshotDigest:createHash("sha256").update(JSON.stringify(canonical)).digest("hex")};
    }catch{this.fail(protocol("Private identity snapshot unavailable"));throw this.failure;}
  }
  async authoritySnapshot(supplierGeneration:string):Promise<{supplierGeneration:string;identityGeneration:string;snapshotDigest:string}> {
    const {identityGeneration,snapshotDigest}=await this.privateAuthoritySnapshot(supplierGeneration);return{supplierGeneration,identityGeneration,snapshotDigest};
  }
  /** Consumes raw identity only within the private session/store seam and returns no supplier principal. */
  async establishHostedIdentityBinding(store:HostedIdentityBindingStore,authority:SupplierAuthorityController,supplierGeneration:string,signal?:AbortSignal):Promise<{continuity:WorkerContinuity;authority:{supplierGeneration:string;identityGeneration:string;snapshotDigest:string};accountDigest:string}> {
    return authority.runGuarded(async()=>{const snapshot=await this.privateAuthoritySnapshot(supplierGeneration);
      const projected={supplierGeneration:snapshot.supplierGeneration,identityGeneration:snapshot.identityGeneration,snapshotDigest:snapshot.snapshotDigest};
      const accountDigest=createHash("sha256").update(JSON.stringify({schema:"chirality-hosted-account-conformance/v1",accountUserId:snapshot.accountUserId,providerWorkspaceId:snapshot.providerWorkspaceId})).digest("hex");
      const assertLive=()=>authority.assertSnapshotBinding(projected);assertLive();
      try{const continuity=await store.establishLive(snapshot,{assertLive},signal);assertLive();return{continuity,authority:projected,accountDigest};}
      catch(error){if(authority.projection().state!=="ready")await store.fence("revoke");throw error;}});
  }
  /** Returns only a stable digest of the private account/workspace pair for same-principal checks. */
  async hostedAccountDigest(authority:SupplierAuthorityController,supplierGeneration:string):Promise<string> {
    return authority.runGuarded(async()=>{const snapshot=await this.privateAuthoritySnapshot(supplierGeneration);
      authority.assertSnapshotBinding({supplierGeneration:snapshot.supplierGeneration,identityGeneration:snapshot.identityGeneration,snapshotDigest:snapshot.snapshotDigest});
      return createHash("sha256").update(JSON.stringify({schema:"chirality-hosted-account-conformance/v1",accountUserId:snapshot.accountUserId,providerWorkspaceId:snapshot.providerWorkspaceId})).digest("hex");});
  }
  async listModelsPage(cursor?: string): Promise<{ data: readonly { model: string; hidden: boolean; isDefault: boolean; defaultReasoningEffort: string; supportedReasoningEfforts: readonly string[] }[]; nextCursor: string | null }> {
    this.assertReady();
    if (cursor !== undefined && (typeof cursor !== "string" || !/^[\x21-\x7e]{1,512}$/.test(cursor))) throw invalid("Invalid model catalog cursor");
    const response = await this.request("model/list", cursor === undefined ? { limit: 100 } : { limit: 100, cursor });
    strictKeys(response, ["data", "nextCursor"]);
    if (!Array.isArray(response.data) || response.data.length > 100 || (response.nextCursor !== null && (typeof response.nextCursor !== "string" || !/^[\x21-\x7e]{1,512}$/.test(response.nextCursor)))) throw protocol("Invalid model catalog page");
    const data = response.data.map((entry: unknown) => {
      if (!entry || typeof entry !== "object" || Array.isArray(entry)) throw protocol("Invalid model catalog entry");
      const item = entry as Record<string, unknown>;
      if (typeof item.model !== "string" || !/^[\x21-\x7e]{1,128}$/.test(item.model) || typeof item.isDefault !== "boolean" || typeof item.hidden !== "boolean"
        || typeof item.defaultReasoningEffort !== "string" || !/^[\x21-\x7e]{1,64}$/.test(item.defaultReasoningEffort)) throw protocol("Invalid model catalog entry");
      if (!Array.isArray(item.supportedReasoningEfforts) || item.supportedReasoningEfforts.length < 1 || item.supportedReasoningEfforts.length > 32) throw protocol("Invalid model reasoning options");
      const efforts = item.supportedReasoningEfforts.map((option: unknown) => {
        if (!option || typeof option !== "object" || Array.isArray(option)) throw protocol("Invalid model reasoning option");
        const effort = (option as Record<string, unknown>).reasoningEffort;
        if (typeof effort !== "string" || !/^[\x21-\x7e]{1,64}$/.test(effort)) throw protocol("Invalid model reasoning option");
        return effort;
      });
      if (new Set(efforts).size !== efforts.length || !efforts.includes(item.defaultReasoningEffort)) throw protocol("Unusable default model reasoning");
      return Object.freeze({ model: item.model, hidden: item.hidden, isDefault: item.isDefault, defaultReasoningEffort: item.defaultReasoningEffort, supportedReasoningEfforts: Object.freeze(efforts) });
    });
    return Object.freeze({ data: Object.freeze(data), nextCursor: response.nextCursor as string | null });
  }
  private connectedAuthorityTransport():AuthorityTransport {
    if(!this.authorityInitialized)throw invalid("Private authority initialization required");
    return {subscribe:(frame,failed)=>{if(this.authorityFrame)throw invalid("Private authority already attached");this.authorityFrame=frame;this.authorityFailed=failed;return()=>{this.authorityFrame=undefined;this.authorityFailed=undefined;};},send:async frame=>{this.assertReady();this.write(frame as unknown as Record<string,unknown>);},close:()=>this.close()};
  }
  async establishAuthority(input:CodexAuthorityInitialize,lease:RuntimeAdmissionLease,durableRevoke:()=>Promise<void>):Promise<SupplierAuthorityController> {
    await this.initializeAuthority(input);const snapshot=await this.authoritySnapshot(input.supplierGeneration);
    const controller = new SupplierAuthorityController({enabled:true,kernelLease:lease,transport:this.connectedAuthorityTransport(),authoritySecret:input.authoritySecret,runtimeProcessIncarnationId:input.runtimeProcessIncarnationId,...snapshot,durableRevoke,refreshSnapshot:()=>this.authoritySnapshot(input.supplierGeneration)});
    this.supplierAuthority = controller; this.supplierGeneration = input.supplierGeneration; return controller;
  }
  async initialize(): Promise<void> {
    if (this.ready || this.initializing) throw invalid("Codex connection initializes once");
    this.initializing = true;
    try { await this.request("initialize", { clientInfo: { name: "chirality_runtime_offline_probe", version: "0.0.0" }, capabilities: { experimentalApi: true } }); this.write({ method: "initialized" }); this.ready = true; }
    finally { this.initializing = false; }
  }
  async accountRead(): Promise<{ authRequired: boolean; hasAccount: boolean }> {
    this.assertReady(); const result = await this.request("account/read", { refreshToken: false });
    const bounded = (value: unknown): value is string => typeof value === "string" && value.length <= 1024 && !/[\x00-\x1f\x7f]/.test(value);
    const account = result.account;
    const accountObject = account !== null && typeof account === "object" && !Array.isArray(account) ? account as Record<string, unknown> : undefined;
    const knownAccount = account === null || (accountObject && (
      (accountObject.type === "apiKey" && Object.keys(accountObject).length === 1)
      || (accountObject.type === "chatgpt" && Object.keys(accountObject).sort().join(",") === "email,planType,type"
        && (accountObject.email === null || bounded(accountObject.email)) && bounded(accountObject.planType))));
    if (Object.keys(result).sort().join(",") !== "account,requiresOpenaiAuth" || typeof result.requiresOpenaiAuth !== "boolean" || !knownAccount) {
      this.fail(protocol("Unsupported account response")); throw this.failure;
    }
    return { authRequired: result.requiresOpenaiAuth, hasAccount: result.account !== null };
  }
  /** Supplier-owned logout. Runtime observes only the empty acknowledgement. */
  async accountLogout(): Promise<void> {
    this.assertReady();
    const result = await this.request("account/logout");
    if (Object.keys(result).length !== 0) { this.fail(protocol("Unsupported logout response")); throw this.failure; }
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
  async verifyNativePolicy(expected: CodexNativePermissions, nativeRoles?: { digest: string; configOverrides: readonly string[] }): Promise<void> {
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
    if (nativeRoles !== undefined) {
      const prefix = ["agents.enabled=true", "features.multi_agent=true", "features.multi_agent_v2=false", "agents.max_depth=2"];
      if (!/^[a-f0-9]{64}$/.test(nativeRoles.digest) || !Array.isArray(nativeRoles.configOverrides) || nativeRoles.configOverrides.length !== 12
        || prefix.some((value, index) => nativeRoles.configOverrides[index] !== value)) throw invalid("Invalid expected native role configuration");
      const roles: Record<string, { description: string; config_file: string }> = {}; let index = prefix.length;
      for (const roleId of CHIRALITY_ROLE_NAMES) {
        const descriptionPrefix = `agents.${roleId}.description=`, filePrefix = `agents.${roleId}.config_file=`;
        const description = nativeRoles.configOverrides[index++]!, file = nativeRoles.configOverrides[index++]!;
        try {
          if (!description.startsWith(descriptionPrefix) || !file.startsWith(filePrefix)) throw new Error();
          const parsedDescription: unknown = JSON.parse(description.slice(descriptionPrefix.length)), parsedFile: unknown = JSON.parse(file.slice(filePrefix.length));
          if (typeof parsedDescription !== "string" || typeof parsedFile !== "string" || !isAbsolute(parsedFile) || resolve(parsedFile) !== parsedFile) throw new Error();
          roles[roleId] = { description: parsedDescription, config_file: parsedFile };
        } catch { throw invalid("Invalid expected native role configuration"); }
      }
      const projected = { digest: nativeRoles.digest, configOverrides: [...nativeRoles.configOverrides], roles };
      if (this.expectedNativeRoles && JSON.stringify(this.expectedNativeRoles) !== JSON.stringify(projected)) throw invalid("Expected native role configuration cannot be replaced in this session");
      this.expectedNativeRoles ??= Object.freeze({ digest: projected.digest, configOverrides: Object.freeze(projected.configOverrides), roles: Object.freeze(projected.roles) });
    } else if (this.expectedNativeRoles) throw invalid("Expected native role configuration cannot be removed from this session");
    this.policyCwd = roots[0]!;
    await this.checkNativePolicy();
  }
  private async checkNativePolicy(): Promise<void> {
    if (!this.nativePolicy) return;
    if (!this.expectedPermissions || !this.policyCwd) throw invalid("Verify the trusted effective native policy before work");
    try {
      const reply = await this.request("config/read", { includeLayers: true, cwd: this.policyCwd });
      const config = object(reply.config), profiles = object(config.permissions);
      if (this.options.nativeSkills === "disabled") {
        const runtime = object(config.chirality_runtime);
        if (Object.keys(runtime).length !== 1 || runtime.nativeSkills !== "disabled") throw protocol("Effective native skill startup selection differs from the trusted compiler");
      }
      const selected = normalizeObservedProfile(object(profiles[this.nativePolicy.permissionProfile]), this.expectedPermissions.network);
      if (!sameTable(selected, this.expectedPermissions)) throw protocol("Effective named policy differs from the trusted exact table");
      if (config.approvals_reviewer !== "user" || config.approval_policy !== (this.commandNetworkPosture === "ask-per-destination" ? "on-request" : "never") || config.allow_login_shell !== false || object(config.features).shell_snapshot !== false || object(config.features).plugins !== false || object(config.features).remote_plugin !== false || object(config.features).network_proxy !== (this.commandNetworkPosture !== "off")) throw protocol("Unsafe effective host execution settings");
      if (this.expectedNativeRoles) {
        const features = object(config.features), agents = object(config.agents);
        if (features.multi_agent !== true || features.multi_agent_v2 !== false || agents.enabled !== true || agents.max_depth !== 2) throw protocol("Effective native role pins differ from the trusted configuration");
        for (const roleId of CHIRALITY_ROLE_NAMES) {
          const expectedRole = this.expectedNativeRoles.roles[roleId]!;
          if (!sameTable(agents[roleId], { description: expectedRole.description, config_file: expectedRole.config_file })) throw protocol("Effective native role entry differs from the trusted configuration");
        }
        const safeDefaults = new Set(["enabled", "max_depth", "max_concurrent_threads_per_session", "default_subagent_model", "default_subagent_reasoning_effort", "interrupt_message", ...CHIRALITY_ROLE_NAMES]);
        if (Object.entries(agents).some(([key, value]) => !safeDefaults.has(key) && value !== null && value !== undefined)) throw protocol("Unexpected effective native role configuration");
      }
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
  /** Private initialized transport readback. It deliberately requires no operation lease. */
  async verifyNativeSkillSelection(cwd?: string): Promise<void> {
    if (this.options.nativeSkills !== "disabled") return;
    this.assertReady();
    const selectedCwd = cwd ?? this.options.runtimeV2?.instanceInput.canonicalRoot ?? this.policyCwd;
    if (!selectedCwd) throw protocol("Native skill readback has no bound project root");
    try {
      const reply = await this.request("config/read", { includeLayers: true, cwd: selectedCwd });
      const config = object(reply.config), runtime = object(config.chirality_runtime);
      if (Object.keys(runtime).length !== 1 || runtime.nativeSkills !== "disabled") throw protocol("Effective native skill startup selection differs from the trusted compiler");
    } catch (error) { this.fail(error instanceof RuntimeError ? error : protocol("Effective native skill startup selection is unavailable")); throw this.failure; }
  }
  /** Account-free login observation. Reads one compiler-owned projection after
   * private initialization and before any account, model or admission request. */
  async observeAccountFreeLoginConfiguration(cwd: string, expected: Readonly<Record<string, unknown>>): Promise<Readonly<{
    schema: "chirality-account-free-login-config-observation/v1"; nativeSkills: "disabled"; credentialStore: "keyring"; plaintextFallback: false;
    compilerConfigDigest: string; observedConfigProjectionDigest: string;
  }>> {
    if (this.options.purpose !== "login" || this.options.nativeSkills !== "disabled" || !this.authorityInitialized) throw invalid("Account-free login readback requires private login initialization");
    if (!isAbsolute(cwd) || resolve(cwd) !== cwd || !expected || typeof expected !== "object" || Array.isArray(expected)
      || expected.cli_auth_credentials_store !== "keyring") throw invalid("Account-free login compiler projection is invalid");
    try {
      const reply = await this.request("config/read", { includeLayers: true, cwd }), config = object(reply.config), runtime = object(config.chirality_runtime);
      if (Object.keys(runtime).length !== 1 || runtime.nativeSkills !== "disabled") throw protocol("Effective native skill startup selection differs from the trusted compiler");
      const project = (value: unknown, template: unknown): unknown => {
        if (!template || typeof template !== "object" || Array.isArray(template)) return value;
        const source = object(value), result: Record<string, unknown> = {};
        for (const [key, child] of Object.entries(template)) result[key] = project(source[key], child);
        return result;
      };
      const observed = project(config, expected);
      if (JSON.stringify(observed) !== JSON.stringify(expected)) throw protocol("Effective login configuration differs from the trusted compiler");
      for (const field of ["hooks", "mcp_servers", "notify", "plugins", "profiles", "projects"]) if (!emptyConfiguration(config[field])) throw protocol("Unsafe login configuration overlay");
      if (config.profile !== null && config.profile !== undefined) throw protocol("Unexpected effective login profile");
      const compilerConfigDigest = createHash("sha256").update(`${JSON.stringify(expected)}\n`).digest("hex");
      const observedConfigProjectionDigest = createHash("sha256").update(`${JSON.stringify(observed)}\n`).digest("hex");
      return Object.freeze({ schema: "chirality-account-free-login-config-observation/v1" as const, nativeSkills: "disabled" as const,
        credentialStore: "keyring" as const, plaintextFallback: false as const, compilerConfigDigest, observedConfigProjectionDigest });
    } catch (error) { this.fail(error instanceof RuntimeError ? error : protocol("Effective account-free login configuration is unavailable")); throw this.failure; }
  }
  policyBinding(): Readonly<{ permissionProfile: string; policyDigest: string }> | undefined { return this.nativePolicy; }
  private rejectPolicyOverride(input: object): void {
    if (["permissionProfile", "policyDigest", "permissions", "sandbox", "sandboxPolicy", "approvalPolicy", "approval_policy", "approvalsReviewer", "approvals_reviewer"].some(field => Object.hasOwn(input, field))) throw invalid("Policy overrides are forbidden; use trusted constructor binding");
  }
  private policyParameters(): Record<string, unknown> { return this.nativePolicy ? { permissions: this.nativePolicy.permissionProfile, approvalPolicy: this.commandNetworkPosture === "ask-per-destination" ? "on-request" : "never", approvalsReviewer: "user" } : {}; }
  private async revalidateModelEffectV2(): Promise<void> {
    const binding = this.options.runtimeV2;
    if (!binding) return;
    const input = binding.instanceInput;
    await revalidateRuntimeInstanceAdmissionV2(input, binding.instanceAdmission);
    if (!this.supplierAuthority || !this.supplierGeneration || await this.hostedAccountDigest(this.supplierAuthority, this.supplierGeneration) !== input.account?.accountDigest) throw invalid("Current account differs from model admission");
    await revalidateHostedAccountAuthorityV2(input.hostAuthority, { purpose: "worker", projectId: input.projectId, manifestHash: input.manifestHash, canonicalRoot: input.canonicalRoot, account: input.account, consentDigest: input.consent.digest });
    this.assertReady();
  }
  private model(model: string): void { if (typeof model !== "string" || !model.trim() || model.length > 128 || /[\x00-\x1f]/.test(model)) throw invalid("An explicit model is required"); }
  private async select(method: "thread/start" | "thread/resume", input: { model: string; continuityChecked: true }, params: Record<string, unknown>): Promise<string> {
    this.assertReady(); if (this.options.purpose === "login") throw invalid("Login transport cannot start model work"); this.model(input.model);
    if (input.continuityChecked !== true) throw invalid("Host continuity check is required");
    if (this.active || this.selecting) throw invalid("Thread selection conflicts with active operation");
    this.selecting = true; this.threadNotice = undefined;
    try {
      await this.checkNativePolicy();
      await this.revalidateModelEffectV2();
      const chiralityRuntime = this.inheritableTools === undefined ? undefined : { schema: CODEX_NATIVE_TOOLS_SCHEMA, inheritableTools: this.inheritableTools };
      const result = await this.request(method, { ...params, model: input.model, ...this.policyParameters(), ...(chiralityRuntime ? { chiralityRuntime } : {}) });
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
  async startTurn(input: { threadId: string; text: string; model: string; reasoningEffort?: string; interactionMode?: "chat" | "native-plan"; attachments?: readonly DelegatedAttachmentInput[] }): Promise<string> {
    this.rejectPolicyOverride(input);
    this.assertReady(); if (this.options.purpose === "login") throw invalid("Login transport cannot start model work"); this.model(input.model);
    if (input.threadId !== this.threadId || !this.threadId || this.selecting) throw invalid("Select this thread before starting a turn");
    if (this.active) throw new RuntimeError("SESSION_TURN_IN_PROGRESS", "A Codex turn is already active", 409);
    if (typeof input.text !== "string" || !input.text.trim() || Buffer.byteLength(input.text) > 65536 || this.terminals.size >= 64) throw invalid("Invalid prompt or session turn capacity reached");
    let resolveTurn!: (value: CodexTurnTerminal) => void, rejectTurn!: (error: Error) => void;
    const done = new Promise<CodexTurnTerminal>((yes, no) => { resolveTurn = yes; rejectTurn = no; }); void done.catch(() => {});
    if (input.interactionMode !== undefined && input.interactionMode !== "chat" && input.interactionMode !== "native-plan") throw invalid("Unknown interaction mode");
    const attachments = input.attachments ?? [];
    if (!Array.isArray(attachments) || attachments.length > 32) throw invalid("Invalid turn attachments");
    const userInput: Record<string, unknown>[] = [{ type: "text", text: input.text, text_elements: [] }];
    for (const attachment of attachments) {
      if (attachment.type === "text") {
        if (attachment.source !== "untrusted-document" || typeof attachment.text !== "string" || Buffer.byteLength(attachment.text) > 262144) throw invalid("Invalid untrusted document attachment");
        userInput.push({ type: "text", text: attachment.text, text_elements: [] });
      } else {
        if (attachment.source !== "untrusted-attachment" || !isAbsolute(attachment.path) || resolve(attachment.path) !== attachment.path || !["image/png", "image/jpeg", "image/gif", "image/webp"].includes(attachment.mimeType)) throw invalid("Invalid local image attachment");
        userInput.push({ type: "localImage", path: attachment.path });
      }
    }
    const turn: Turn = { threadId: input.threadId, startedEmitted: false, items: new Map(), plans: new Map(), done, resolve: resolveTurn, reject: rejectTurn,
      familyEnabled: this.inheritableTools !== undefined, familySettled: this.inheritableTools === undefined,
      timer: setTimeout(() => this.fail(protocol("Codex turn timed out")), this.options.turnTimeoutMs ?? 120000) };
    this.active = turn;
    try {
      await this.checkNativePolicy();
      const mode = input.interactionMode ?? "chat";
      if (input.reasoningEffort !== undefined && !/^[\x21-\x7e]{1,64}$/.test(input.reasoningEffort)) throw invalid("Invalid reasoning effort");
      await this.revalidateModelEffectV2();
      const result = await this.request("turn/start", { threadId: input.threadId, input: userInput, model: input.model,
        collaborationMode: { mode: mode === "native-plan" ? "plan" : "default", settings: { model: input.model, reasoning_effort: input.reasoningEffort ?? null, developer_instructions: null } }, ...this.policyParameters() });
      const id = identifier(object(result.turn).id);
      if ((turn.id && turn.id !== id) || (this.terminals.has(id) && turn.terminal?.turnId !== id)) throw protocol("Turn response identity mismatch");
      turn.id = id; if (!turn.startedEmitted) { turn.startedEmitted = true; this.emit({ type: "started", threadId: turn.threadId, turnId: id }); } return id;
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
    for (const call of this.toolCalls.values()) {
      const association = call.associationId ? this.nativeChildAssociations.get(call.associationId) : undefined;
      if ((call.turnId === turnId || (association?.rootThreadId === this.active.threadId && association.rootTurnId === turnId)) && !call.completed) call.controller.abort();
    }
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
    const properties = schema.properties ?? {};
    if (schema.additionalProperties !== false || typeof properties !== "object" || Array.isArray(properties) || Object.keys(properties).length > 64) throw invalid("Dynamic objects require closed properties");
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
      const properties = (schema.properties ?? {}) as Record<string, Record<string, unknown>>, input = value as Record<string, unknown>;
      return Object.keys(input).every(key => Object.hasOwn(properties, key) && matchesToolSchema(input[key], properties[key]!)) && ((schema.required ?? []) as string[]).every(key => Object.hasOwn(input, key));
    }
    default: return false;
  }
}
