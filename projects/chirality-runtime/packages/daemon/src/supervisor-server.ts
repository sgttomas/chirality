import { createConnection, createServer, type Socket } from "node:net";
import { chmod, lstat, mkdir, unlink } from "node:fs/promises";
import { dirname, isAbsolute, parse, join } from "node:path";
import { randomBytes, randomUUID, timingSafeEqual, createHmac } from "node:crypto";
import type { SupervisorManagerPort, ManagerMessage } from "./codex-manager.js";
import type { CodexLoginStatus } from "./codex-login.js";
import { RuntimeError, validateHostedLoginStatus, type DelegatedHarnessProcessSupervisorPort, type WorkerHandle, type WorkerResult, type WorkerContinuity, type SupervisorNetworkApprovalPort, type NetworkApprovalPrompt, type NetworkApprovalChoice, type SupervisorApprovalDescription, type RuntimeCompatibilityIdentity, type SupervisorNativePlanPort, type NativePlanTransportEvent, type NativePlanClarificationPrompt, type NativePlanClarificationAnswers, type SupervisorRuntimeToolPort, type RuntimeToolCallbackDeclaration, type RuntimeToolCallbackMessage, type RuntimeToolCallbackResult, type SupervisorTurnProgressPort, type DelegatedTurnProgressEvent } from "@chirality/runtime-contracts";

function reconciliationDetails(value: unknown): Record<string, unknown> | undefined {
  if (!value || typeof value !== "object" || (value as Record<string, unknown>).reason !== "DESCENDANT_RECONCILIATION_REQUIRED") return undefined;
  const source = value as Record<string, unknown>, result: Record<string, unknown> = { reason: "DESCENDANT_RECONCILIATION_REQUIRED" };
  for (const key of ["observed", "observedCount", "scans", "detachedCount", "ownedGroupCount", "survivingGroupCount", "identityChangedCount"]) if (Number.isSafeInteger(source[key]) && (source[key] as number) >= 0) result[key] = source[key];
  for (const key of ["leaderObserved", "censusFailed"]) if (typeof source[key] === "boolean") result[key] = source[key];
  if (Array.isArray(source.detachedPids)) result.detachedPids = source.detachedPids.filter(value => Number.isSafeInteger(value) && value > 0).slice(0, 32);
  if (Array.isArray(source.limitations)) result.limitations = source.limitations.filter(value => typeof value === "string" && /^[A-Z_]{1,64}$/.test(value)).slice(0, 8);
  if (typeof source.censusFailure === "string" && source.censusFailure.length > 0) result.censusFailure = source.censusFailure.slice(0, 257);
  result.signalAuthority = "NONE";
  return result;
}

export interface SupervisorLoginPort { startLogin(): Promise<{ loginId: string; authUrl: string }>; status(): Promise<CodexLoginStatus>; cancel(): Promise<void> }
export interface SupervisorCredential { owner: string; epoch: string; token: string }
interface Options { socketPath: string; credential: SupervisorCredential; timeoutMs?: number }
const MAX_FRAME = 256 * 1024;
import type { SupplierAuthorityProjection } from "./supplier-authority-controller.js";
export type { SupplierAuthorityProjection } from "./supplier-authority-controller.js";
const PRIVATE_NAMES=new Set(["authoritySecret","accountUserId","providerWorkspaceId","runtimeProcessIncarnationId","runtimeChallenge","supplierChallenge","supplierGeneration","identityGeneration","snapshotDigest","leaseId","leaseHandle","lockIdentity","transcriptMac","previousTranscriptMac","chiralityAdmissionAuthority","exactSupplyDigest","revokedThroughRuntimeSequence"]);
const PRIVATE_VALUES=new Set(["chirality.local-admission-authority","chirality-local-supplier-admission-authority/1","chirality-supplier-account-identity/1","chirality-supplier-account-identity-response/1","account/identitySnapshot",... ["Acquire","Release","Abort","Acquired","Released","Aborted","Revoked"].map(name=>`chirality/admission${name}`)]);
export function assertNoPrivateAuthoritySurface(value:unknown,depth=0):void {
  if(depth>32)throw new Error("private supplier authority surface rejected");
  if(typeof value==="string") {if(PRIVATE_NAMES.has(value)||PRIVATE_VALUES.has(value))throw new Error("private supplier authority surface rejected");
    if(/^[\s]*[\[{]/.test(value)){let decoded:unknown;try{decoded=JSON.parse(value);}catch{return;}assertNoPrivateAuthoritySurface(decoded,depth+1);}return;}
  if(value&&typeof value==="object"){for(const [key,item]of Object.entries(value)){if(PRIVATE_NAMES.has(key))throw new Error("private supplier authority surface rejected");assertNoPrivateAuthoritySurface(item,depth+1);}}
}
export function validateSupplierAuthorityProjection(value:unknown):SupplierAuthorityProjection {
  if(!value||typeof value!=="object"||Array.isArray(value))throw new Error("invalid authority projection");const r=value as Record<string,unknown>;
  if((r.state==="ready"||r.state==="disabled")&&Object.keys(r).join(",")==="state")return{state:r.state};
  if(r.state==="unavailable"&&Object.keys(r).sort().join(",")==="reason,state"&&["not-configured","starting","revoking","retiring","blocked"].includes(String(r.reason)))return{state:"unavailable",reason:r.reason as Extract<SupplierAuthorityProjection,{state:"unavailable"}>["reason"]};
  throw new Error("invalid authority projection");
}
function requestToken(secret: string, r: Record<string, unknown>): string {
  return createHmac("sha256", secret).update(JSON.stringify([r.owner, r.epoch, r.op, r.workerId ?? null, r.generation, r.input ?? null])).digest("hex");
}
function validString(value: unknown, max = 128): value is string { return typeof value === "string" && value.length > 0 && value.length <= max; }
async function privateDirectory(path: string): Promise<void> {
  if (!isAbsolute(path)) throw new Error("socket path must be absolute");
  // Reject symlink components before creating anything inside the directory.
  let current = parse(path).root;
  for (const part of dirname(path).slice(current.length).split("/").filter(Boolean)) {
    current = join(current, part);
    try { if ((await lstat(current)).isSymbolicLink()) throw new Error("symlink socket ancestor"); }
    catch (error) { if ((error as NodeJS.ErrnoException).code !== "ENOENT") throw error; }
  }
  await mkdir(dirname(path), { recursive: true, mode: 0o700 });
  const st = await lstat(dirname(path));
  if (!st.isDirectory() || st.uid !== process.getuid?.() || (st.mode & 0o777) !== 0o700) throw new Error("socket directory must be owner-private 0700");
}
async function activeSocket(path: string): Promise<boolean> {
  return new Promise((resolve, reject) => {
    const socket = createConnection(path);
    socket.setTimeout(300);
    socket.once("connect", () => { socket.destroy(); resolve(true); });
    socket.once("timeout", () => { socket.destroy(); reject(new Error("socket owner probe timed out")); });
    socket.once("error", (error: NodeJS.ErrnoException) => { socket.destroy(); if (error.code === "ECONNREFUSED" || error.code === "ENOENT") resolve(false); else reject(error); });
  });
}
/** This credential is exclusively a daemon-to-supervisor capability. Never serialize it to public clients. */
export async function startSupervisorServer(options: { socketPath: string; supervisor: DelegatedHarnessProcessSupervisorPort; login?: SupervisorLoginPort; recoverStale?: boolean; approvalCompatibility?: RuntimeCompatibilityIdentity }): Promise<{ credential: SupervisorCredential; close(): Promise<void> }> {
  await privateDirectory(options.socketPath);
  try {
    const old = await lstat(options.socketPath);
    if (!old.isSocket() || old.uid !== process.getuid?.()) throw new Error("invalid existing socket owner");
    if (!options.recoverStale || await activeSocket(options.socketPath)) throw new Error("socket already owned");
    const again = await lstat(options.socketPath);
    if (again.ino !== old.ino || again.dev !== old.dev) throw new Error("socket changed during recovery");
    await unlink(options.socketPath);
  } catch (error) { if ((error as NodeJS.ErrnoException).code !== "ENOENT") throw error; }
  const credential: SupervisorCredential = { owner: `${process.getuid?.()}:${process.pid}`, epoch: randomUUID(), token: randomBytes(32).toString("hex") };
  let closing = false;
  const sockets = new Set<Socket>();
  const server = createServer(socket => {
    sockets.add(socket); socket.once("close", () => sockets.delete(socket));
    socket.on("error", () => {});
    socket.setTimeout(60000, () => socket.destroy());
    let data = Buffer.alloc(0), consumed = false;
    const respond = (value: unknown) => { const frame = JSON.stringify(value) + "\n"; socket.end(Buffer.byteLength(frame) <= MAX_FRAME ? frame : '{"ok":false,"error":"response too large"}\n'); };
    socket.on("data", chunk => {
      if (consumed) { socket.destroy(); return; }
      data = Buffer.concat([data, chunk]);
      if (data.length > MAX_FRAME) { consumed = true; respond({ ok: false, error: "request too large" }); return; }
      const newline = data.indexOf(10);
      if (newline < 0) return;
      consumed = true;
      void (async () => {
        try {
          if (closing || newline !== data.length - 1) throw new Error("invalid frame");
          const r = JSON.parse(data.subarray(0, newline).toString()) as Record<string, unknown>;
          assertNoPrivateAuthoritySurface(r);
          if(Object.keys(r).some(key=>!["owner","epoch","op","generation","workerId","input","token"].includes(key)))throw new Error("invalid request fields");
          if (!r || typeof r !== "object" || !validString(r.token, 64) || !/^[a-f0-9]{64}$/.test(r.token) || !timingSafeEqual(Buffer.from(r.token), Buffer.from(requestToken(credential.token, r))) || r.owner !== credential.owner || r.epoch !== credential.epoch) throw new Error("unauthorized supervisor request");
          const op = r.op;
          if (!["acquire", "inventory", "reconnect", "wait", "retire", "verify-hosted", "login-start", "login-status", "login-cancel", "manager-start", "manager-next", "manager-reply", "approval-pending", "approval-reply", "approval-describe", "native-plan-events", "native-plan-questions", "native-plan-answer", "runtime-tool-start", "runtime-tool-next", "runtime-tool-reply", "turn-progress"].includes(String(op))) throw new Error("unknown operation");
          let result: unknown;
          if (op === "approval-describe") {
            const describe = options.supervisor as DelegatedHarnessProcessSupervisorPort & { describeApprovalScope?: (workerId?: string, generation?: string) => Promise<Omit<SupervisorApprovalDescription, "compatibility">> };
            if (!describe.describeApprovalScope || !options.approvalCompatibility || !/^root-runtime-[1-9][0-9]*$/.test(options.approvalCompatibility.compatibilityIdentity) || !/^[a-f0-9]{64}$/.test(options.approvalCompatibility.contractBasisSha256) || r.input !== undefined) throw new Error("Exact approval compatibility description unavailable");
            if (r.workerId !== undefined && (!validString(r.workerId) || !validString(r.generation))) throw new Error("Invalid worker scope");
            if (r.workerId === undefined && r.generation !== null) throw new Error("Invalid configuration description");
            result = { ...await describe.describeApprovalScope(r.workerId as string | undefined, r.generation === null ? undefined : r.generation as string), compatibility: { ...options.approvalCompatibility } };
          }
          else if (op === "login-start" || op === "login-status" || op === "login-cancel") {
            if (r.generation !== null || r.input !== undefined || options.login === undefined) throw new Error("Login service unavailable");
            if (op === "login-start") result = await options.login.startLogin();
            else if (op === "login-status") {
              const status = await options.login.status();
              try { result = validateHostedLoginStatus(status); }
              catch { throw new RuntimeError("INTERNAL_FAILURE", "Invalid safe login status", 500); }
            }
            else result = await options.login.cancel();
          }
          else if (op === "verify-hosted") {
            if (r.generation !== null || typeof r.input !== "string" || options.supervisor.verifyHostedBoundary === undefined) throw new Error("hosted boundary unavailable");
            await options.supervisor.verifyHostedBoundary(JSON.parse(r.input)); result = true;
          }
          else if (op === "inventory") { if (r.generation !== null) throw new Error("invalid generation"); result = await options.supervisor.inventory(); }
          else {
            if (!validString(r.workerId) || !/^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$/.test(r.workerId)) throw new Error("invalid worker");
            if (op === "turn-progress") {
              const progress = options.supervisor as DelegatedHarnessProcessSupervisorPort & Partial<SupervisorTurnProgressPort>;
              if (!validString(r.generation) || r.input !== undefined || !progress.drainTurnProgress) throw new Error("Turn progress service unavailable");
              result = await progress.drainTurnProgress(r.workerId, r.generation);
            } else if (op === "runtime-tool-start" || op === "runtime-tool-next" || op === "runtime-tool-reply") {
              const runtimeTools = options.supervisor as DelegatedHarnessProcessSupervisorPort & Partial<SupervisorRuntimeToolPort>;
              if (!runtimeTools.acquireWithRuntimeTools || !runtimeTools.nextRuntimeToolCallback || !runtimeTools.replyRuntimeToolCallback) throw new Error("Runtime tool supervisor service unavailable");
              if (op === "runtime-tool-start") {
                if (r.generation !== null || typeof r.input !== "string" || Buffer.byteLength(r.input) > 196608) throw new Error("Invalid runtime tool start");
                const start = JSON.parse(r.input);
                if (!start || Object.keys(start).sort().join(",") !== "input,tools" || typeof start.input !== "string" || !Array.isArray(start.tools)) throw new Error("Invalid runtime tool start");
                result = await runtimeTools.acquireWithRuntimeTools(r.workerId, start.input, start.tools);
              } else {
                if (!validString(r.generation)) throw new Error("Invalid runtime tool generation");
                if (op === "runtime-tool-next") { if (r.input !== undefined) throw new Error("Unexpected runtime tool poll input"); result = await runtimeTools.nextRuntimeToolCallback(r.workerId, r.generation); }
                else {
                  if (typeof r.input !== "string" || Buffer.byteLength(r.input) > 131072) throw new Error("Invalid runtime tool reply");
                  const reply = JSON.parse(r.input);
                  if (!reply || Object.keys(reply).sort().join(",") !== "message,result") throw new Error("Invalid runtime tool reply");
                  result = await runtimeTools.replyRuntimeToolCallback(r.workerId, r.generation, reply.message, reply.result);
                }
              }
            } else if (op === "native-plan-events" || op === "native-plan-questions" || op === "native-plan-answer") {
              const nativePlan = options.supervisor as DelegatedHarnessProcessSupervisorPort & Partial<SupervisorNativePlanPort>;
              if (!validString(r.generation) || !nativePlan.drainNativePlanEvents || !nativePlan.pendingNativePlanClarifications || !nativePlan.replyNativePlanClarification) throw new Error("Native Plan supervisor service unavailable");
              if (op === "native-plan-events") { if (r.input !== undefined) throw new Error("Unexpected native Plan event input"); result = await nativePlan.drainNativePlanEvents(r.workerId, r.generation); }
              else if (op === "native-plan-questions") { if (r.input !== undefined) throw new Error("Unexpected native Plan question input"); result = await nativePlan.pendingNativePlanClarifications(r.workerId, r.generation); }
              else {
                if (typeof r.input !== "string" || Buffer.byteLength(r.input) > 131072) throw new Error("Invalid native Plan answer");
                const reply = JSON.parse(r.input);
                if (!reply || typeof reply !== "object" || Array.isArray(reply) || Object.keys(reply).sort().join(",") !== "answers,requestId" || (typeof reply.requestId !== "string" && typeof reply.requestId !== "number") || typeof reply.answers !== "object" || reply.answers === null || Array.isArray(reply.answers)) throw new Error("Invalid native Plan answer");
                result = await nativePlan.replyNativePlanClarification(r.workerId, r.generation, reply.requestId, reply.answers);
              }
            } else if (op === "approval-pending" || op === "approval-reply") {
              const approvals = options.supervisor as DelegatedHarnessProcessSupervisorPort & Partial<SupervisorNetworkApprovalPort>;
              if (!validString(r.generation) || !approvals.pendingNetworkApprovals || !approvals.replyNetworkApproval) throw new Error("Approval service unavailable");
              if (op === "approval-pending") { if (r.input !== undefined) throw new Error("Unexpected approval input"); result = await approvals.pendingNetworkApprovals(r.workerId, r.generation); }
              else {
                if (typeof r.input !== "string" || Buffer.byteLength(r.input) > 1024) throw new Error("Invalid approval reply");
                const reply = JSON.parse(r.input);
                if (!reply || Object.keys(reply).sort().join(",") !== "approvalId,decision" || !validString(reply.approvalId) || !["allow", "deny", "acceptForSession"].includes(reply.decision)) throw new Error("Invalid approval reply");
                result = await approvals.replyNetworkApproval(r.workerId, r.generation, reply.approvalId, reply.decision);
              }
            } else if (op === "manager-start" || op === "manager-next" || op === "manager-reply") {
              const manager = options.supervisor as DelegatedHarnessProcessSupervisorPort & Partial<SupervisorManagerPort>;
              if (!manager.startManager || !manager.nextManager || !manager.replyManager) throw new Error("Manager service unavailable");
              if (op === "manager-start") {
                if (r.generation !== null || typeof r.input !== "string" || Buffer.byteLength(r.input) > 65536) throw new Error("Invalid manager start");
                result = await manager.startManager(r.workerId, r.input);
              } else {
                if (!validString(r.generation)) throw new Error("Invalid manager generation");
                if (op === "manager-next") { if (r.input !== undefined) throw new Error("Unexpected poll input"); result = await manager.nextManager(r.workerId, r.generation); }
                else { if (typeof r.input !== "string" || Buffer.byteLength(r.input) > 65536) throw new Error("Invalid callback reply"); result = await manager.replyManager(r.workerId, r.generation, r.input); }
              }
            } else if (op === "acquire") {
              if (r.generation !== null || typeof r.input !== "string" || Buffer.byteLength(r.input) > 65536) throw new Error("invalid acquisition");
              result = await options.supervisor.acquire(r.workerId, r.input);
            } else {
              if (!validString(r.generation)) throw new Error("invalid generation");
              if (op === "reconnect") result = await options.supervisor.reconnect(r.workerId, r.generation);
              else if (op === "wait") result = await options.supervisor.wait(r.workerId, r.generation);
              else result = await options.supervisor.retire(r.workerId, r.generation);
            }
          }
          assertNoPrivateAuthoritySurface(result); respond({ ok: true, result });
        } catch (error) {
          const details = error instanceof RuntimeError ? reconciliationDetails(error.details) : undefined;
          respond({ ok: false, error: "supervisor request rejected", ...(details ? { reconciliation: details } : {}) });
        }
      })();
    });
  });
  await new Promise<void>((resolve, reject) => { server.once("error", reject); server.listen(options.socketPath, resolve); });
  await chmod(options.socketPath, 0o600);
  const owned = await lstat(options.socketPath);
  return { credential, async close() {
    closing = true;
    for (const socket of sockets) socket.destroy();
    await new Promise<void>((resolve, reject) => server.close(error => error ? reject(error) : resolve()));
    try { const current = await lstat(options.socketPath); if (current.ino === owned.ino && current.dev === owned.dev) await unlink(options.socketPath); }
    catch (error) { if ((error as NodeJS.ErrnoException).code !== "ENOENT") throw error; }
  } };
}
export class SupervisorClient implements DelegatedHarnessProcessSupervisorPort {
  constructor(private readonly options: Options) {}
  async describeApprovalScope(workerId?: string, generation?: string): Promise<SupervisorApprovalDescription> {
    return await this.request("approval-describe", { ...(workerId ? { workerId, generation } : {}) }) as SupervisorApprovalDescription;
  }
  async startLogin(): Promise<{ loginId: string; authUrl: string }> { return this.request("login-start") as Promise<{ loginId: string; authUrl: string }>; }
  async loginStatus(): Promise<CodexLoginStatus> {
    const status = await this.request("login-status");
    try { return validateHostedLoginStatus(status); }
    catch { throw new RuntimeError("INTERNAL_FAILURE", "Invalid safe login status", 500); }
  }
  async cancelLogin(): Promise<void> { await this.request("login-cancel"); }
  async verifyHostedBoundary(identity: WorkerContinuity): Promise<void> {
    await this.request("verify-hosted", { input: JSON.stringify(identity) });
  }
  private async request(op: string, fields: Record<string, unknown> = {}): Promise<unknown> {
    assertNoPrivateAuthoritySurface(fields);
    const request = { owner: this.options.credential.owner, epoch: this.options.credential.epoch, op, generation: null, ...fields };
    const frame = JSON.stringify({ ...request, token: requestToken(this.options.credential.token, request) }) + "\n";
    if (Buffer.byteLength(frame) > MAX_FRAME) throw new Error("request too large");
    return new Promise((resolve, reject) => {
      const socket = createConnection(this.options.socketPath);
      let data = Buffer.alloc(0), done = false;
      const fail = (error: Error) => { if (!done) { done = true; socket.destroy(); reject(error); } };
      socket.setTimeout(this.options.timeoutMs ?? 65000, () => fail(new Error("supervisor timeout")));
      socket.once("error", fail); socket.once("connect", () => socket.write(frame));
      socket.on("data", chunk => {
        data = Buffer.concat([data, chunk]);
        if (data.length > MAX_FRAME) { fail(new Error("oversize supervisor response")); return; }
        if (!data.includes(10)) return;
        try { const response = JSON.parse(data.toString()); assertNoPrivateAuthoritySurface(response); if (!response.ok) { const details = reconciliationDetails(response.reconciliation); if (details) throw new RuntimeError("ENGINE_UNAVAILABLE", "Observed descendants require reconciliation", 503, details); throw new Error("supervisor request rejected"); } done = true; socket.destroy(); resolve(response.result); }
        catch (error) { fail(error as Error); }
      });
      socket.once("close", () => { if (!done) fail(new Error("supervisor disconnected")); });
    });
  }
  async startManager(workerId: string, input: string): Promise<WorkerHandle> { return await this.request("manager-start", { workerId, input }) as WorkerHandle; }
  async nextManager(workerId: string, generation: string): Promise<ManagerMessage> { return await this.request("manager-next", { workerId, generation }) as ManagerMessage; }
  async replyManager(workerId: string, generation: string, input: string): Promise<void> { await this.request("manager-reply", { workerId, generation, input }); }
  async pendingNetworkApprovals(workerId: string, generation: string): Promise<readonly NetworkApprovalPrompt[]> { return await this.request("approval-pending", { workerId, generation }) as NetworkApprovalPrompt[]; }
  async replyNetworkApproval(workerId: string, generation: string, approvalId: string, decision: NetworkApprovalChoice): Promise<{ sent: true }> {
    const reply = await this.request("approval-reply", { workerId, generation, input: JSON.stringify({ approvalId, decision }) });
    if (!reply || typeof reply !== "object" || Object.keys(reply).join(",") !== "sent" || (reply as { sent?: unknown }).sent !== true) throw new Error("Invalid approval delivery receipt");
    return { sent: true };
  }
  async drainNativePlanEvents(workerId: string, generation: string): Promise<readonly NativePlanTransportEvent[]> {
    return await this.request("native-plan-events", { workerId, generation }) as NativePlanTransportEvent[];
  }
  async pendingNativePlanClarifications(workerId: string, generation: string): Promise<readonly NativePlanClarificationPrompt[]> {
    return await this.request("native-plan-questions", { workerId, generation }) as NativePlanClarificationPrompt[];
  }
  async replyNativePlanClarification(workerId: string, generation: string, requestId: string | number, answers: NativePlanClarificationAnswers): Promise<{ sent: true }> {
    const reply = await this.request("native-plan-answer", { workerId, generation, input: JSON.stringify({ requestId, answers }) });
    if (!reply || typeof reply !== "object" || Object.keys(reply).join(",") !== "sent" || (reply as { sent?: unknown }).sent !== true) throw new Error("Invalid native Plan answer delivery receipt");
    return { sent: true };
  }
  async acquireWithRuntimeTools(workerId: string, input: string, tools: readonly RuntimeToolCallbackDeclaration[]): Promise<WorkerHandle> {
    return await this.request("runtime-tool-start", { workerId, input: JSON.stringify({ input, tools }) }) as WorkerHandle;
  }
  async nextRuntimeToolCallback(workerId: string, generation: string): Promise<RuntimeToolCallbackMessage> {
    return await this.request("runtime-tool-next", { workerId, generation }) as RuntimeToolCallbackMessage;
  }
  async replyRuntimeToolCallback(workerId: string, generation: string, message: Extract<RuntimeToolCallbackMessage, {kind:"callback"}>, result: RuntimeToolCallbackResult): Promise<void> {
    await this.request("runtime-tool-reply", { workerId, generation, input: JSON.stringify({ message, result }) });
  }
  async drainTurnProgress(workerId: string, generation: string): Promise<readonly DelegatedTurnProgressEvent[]> {
    return await this.request("turn-progress", { workerId, generation }) as DelegatedTurnProgressEvent[];
  }
  async acquire(workerId: string, input: string): Promise<WorkerHandle> { return await this.request("acquire", { workerId, input }) as WorkerHandle; }
  async inventory(): Promise<readonly WorkerHandle[]> { return await this.request("inventory") as WorkerHandle[]; }
  async reconnect(workerId: string, generation: string): Promise<WorkerHandle> { return await this.request("reconnect", { workerId, generation }) as WorkerHandle; }
  async wait(workerId: string, generation: string): Promise<WorkerResult> { return await this.request("wait", { workerId, generation }) as WorkerResult; }
  async retire(workerId: string, generation: string): Promise<void> { await this.request("retire", { workerId, generation }); }
}
