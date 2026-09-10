import { randomUUID } from "node:crypto";
import { realpath } from "node:fs/promises";
import {
  RuntimeError, validateHarnessEventV2,
  type NetworkApprovalPrompt, type SupervisorNetworkApprovalPort,
  type DelegatedCapabilities, type DelegatedApprovalDecisionRequest, type EventAttributionV2,
  type DelegatedHarnessProcessSupervisorPort,
  type DelegatedPreflight,
  type DelegatedTurnRequest,
  type DelegatedTurnResponse,
  type HostedEngineConsentPort,
  type RuntimeCompatibilityIdentity,
  type WorkerContinuity,
  type WorkerRetirementCoordinatorPort,
  type SupervisorNativePlanPort,
  type NativePlanTransportEvent,
  type NativePlanClarificationPrompt,
  type SupervisorRuntimeToolPort,
  type RuntimeToolDefinition,
  type RuntimeToolCallbackDeclaration,
  type SupervisorTurnProgressPort,
  type DelegatedTurnProgressEvent
} from "@chirality/runtime-contracts";

import { ApprovalStore, type ApprovalBinding, type NetworkApprovalContext } from "./approval-store.js";
import { createRolePolicyEvidence, RUNTIME_ROLES, type RolePolicySettings } from "./role-policy.js";

export interface DelegatedProjectBinding {
  actual?: EventAttributionV2;
  rolePolicy?: RolePolicySettings;
  commandNetworkPosture?: "off" | "ask-per-destination" | "on";
  approvals?: ApprovalStore;
  approvalForwardingEnabled?: boolean;
  identity: WorkerContinuity;
  compatibility: RuntimeCompatibilityIdentity;
  supervisor: DelegatedHarnessProcessSupervisorPort;
  consent: HostedEngineConsentPort;
  retirement?: WorkerRetirementCoordinatorPort;
  nativePlanSink?: DelegatedNativePlanSink;
  /** Controlled fixture evidence must never be upgraded by a client request. */
  evidenceClass: "controlled-worker" | "provider-observed";
}
export interface DelegatedNativePlanWorkerBinding {
  projectId: string;
  sessionId: string;
  clientTurnId: string;
  workerId: string;
  generation: string;
}
export interface DelegatedNativePlanSink {
  open(binding: DelegatedNativePlanWorkerBinding, bridge: SupervisorNativePlanPort): Promise<void>;
  capture(binding: DelegatedNativePlanWorkerBinding, events: readonly NativePlanTransportEvent[], clarifications: readonly NativePlanClarificationPrompt[]): Promise<void>;
  close(binding: DelegatedNativePlanWorkerBinding): Promise<void>;
}
export interface DelegatedTurnObserver {
  onProgress(event: DelegatedTurnProgressEvent): void | Promise<void>;
}
export interface DelegatedRuntimeOptions {
  daemonId: string;
  projects: ReadonlyMap<string, DelegatedProjectBinding>;
  preflightTtlMs?: number;
  approvalOnly?: boolean;
}

const nonempty = (value: unknown): value is string => typeof value === "string" && value.length > 0 && value.length <= 256;
const compatibilityValid = (value: RuntimeCompatibilityIdentity | undefined): boolean =>
  value !== undefined && value !== null && typeof value === "object" && typeof value.compatibilityIdentity === "string" && typeof value.contractBasisSha256 === "string" && /^root-runtime-[1-9][0-9]*$/u.test(value.compatibilityIdentity) && /^[0-9a-f]{64}$/u.test(value.contractBasisSha256);

/** Runtime-owned broker composition. It does not implement a guessed provider wire. */
export class DelegatedRuntime {
  private readonly preflights = new Map<string, { value: DelegatedPreflight; expires: number }>();
  private readonly active = new Set<string>();
  private readonly turnRetirements = new Map<string, Promise<void>>();
  private readonly interruptedTurns = new Set<string>();
  private readonly liveTurns = new Map<string, ApprovalBinding>();
  private readonly approvalCallbacks = new Map<string, { requestId: string; prompt: NetworkApprovalPrompt; sent: boolean }>();
  private readonly approvalSyncs = new Map<string, Promise<void>>();
  private readonly approvalSends = new Map<string, Promise<{ record: unknown; applied: boolean; reason: string }>>();
  private closing = false;
  private readonly options: DelegatedRuntimeOptions;
  private readonly inFlight = new Set<Promise<unknown>>();
  constructor(options: DelegatedRuntimeOptions) {
    this.options = { ...options, projects: new Map([...options.projects].map(([key, value]) => [key, Object.freeze({ ...value, ...(value.actual ? { actual: Object.freeze({ ...value.actual }) } : {}), ...(value.rolePolicy ? { rolePolicy: structuredClone(value.rolePolicy) } : {}), identity: Object.freeze({ ...value.identity }), compatibility: Object.freeze({ ...value.compatibility }) })])) };
  }

  private binding(projectId: string): DelegatedProjectBinding {
    if (this.closing) throw new RuntimeError("ENGINE_UNAVAILABLE", "Delegated runtime is shutting down", 503);
    const binding = this.options.projects.get(projectId);
    if (binding === undefined) throw new RuntimeError("ENGINE_UNAVAILABLE", "No delegated worker is configured for this project", 503);
    if (binding.evidenceClass !== "controlled-worker" && binding.supervisor.verifyHostedBoundary === undefined) throw new RuntimeError("ENGINE_UNAVAILABLE", "Production delegated workers require a verified hard containment/provider composition; unavailable in this tranche", 503);
    if (!compatibilityValid(binding.compatibility)) throw new RuntimeError("ENGINE_UNAVAILABLE", "Daemon compatibility basis is unavailable", 503);
    return binding;
  }

  private async verifyHosted(binding: DelegatedProjectBinding): Promise<void> {
    if (binding.evidenceClass === "controlled-worker") return;
    try { await binding.supervisor.verifyHostedBoundary!(binding.identity); }
    catch { throw new RuntimeError("ENGINE_UNAVAILABLE", "Verified hosted worker, account continuity or operator provider consent is unavailable", 503); }
  }

  async preflight(projectId: string, operationId: string): Promise<DelegatedPreflight> {
    const binding = this.binding(projectId);
    if (!nonempty(operationId)) throw new RuntimeError("INVALID_REQUEST", "A bounded operation identity is required");
    if (operationId.startsWith("interrupt:")) {
      const live = this.approvalTurn(projectId, operationId.slice("interrupt:".length));
      if (!await this.isApprovalLive(live)) throw new RuntimeError("FORBIDDEN", "Turn is no longer interruptible", 403);
    } else if (operationId !== "login:start" && operationId !== "login:cancel") await this.verifyHosted(binding);
    for (const [key, value] of this.preflights) if (value.expires <= Date.now()) this.preflights.delete(key);
    if (this.preflights.size >= 1024) throw new RuntimeError("ENGINE_UNAVAILABLE", "Too many pending admissions", 503);
    const value: DelegatedPreflight = { ...binding.compatibility, operationId, projectId, daemonId: this.options.daemonId, nonce: randomUUID() };
    this.preflights.set(value.nonce, { value, expires: Date.now() + (this.options.preflightTtlMs ?? 30_000) });
    return { ...value };
  }

  private admit(projectId: string, operationId: string, request: { compatibility?: RuntimeCompatibilityIdentity; preflight?: DelegatedPreflight }): DelegatedProjectBinding {
    const binding = this.binding(projectId);
    if (!request || typeof request !== "object") request = {};
    const supplied = request.preflight;
    const pending = supplied && this.preflights.get(supplied.nonce);
    // Consume even mismatches, so neither rejected nor accepted requests can replay a nonce.
    if (supplied) this.preflights.delete(supplied.nonce);
    const valid = compatibilityValid(request.compatibility) && pending !== undefined && pending.expires > Date.now()
      && supplied?.operationId === operationId && supplied.projectId === projectId
      && supplied.daemonId === this.options.daemonId
      && JSON.stringify(supplied) === JSON.stringify(pending.value)
      && request.compatibility?.compatibilityIdentity === binding.compatibility.compatibilityIdentity
      && request.compatibility.contractBasisSha256 === binding.compatibility.contractBasisSha256;
    if (!valid) throw new RuntimeError("RUNTIME_COMPATIBILITY_MISMATCH", "Runtime compatibility admission rejected", 409, {
      operation_id: operationId, project_id: projectId, daemon_identity: this.options.daemonId,
      client_compatibility_identity: nonempty(request.compatibility?.compatibilityIdentity) ? request.compatibility.compatibilityIdentity : null,
      daemon_compatibility_identity: binding.compatibility.compatibilityIdentity,
      client_contract_basis_sha256: nonempty(request.compatibility?.contractBasisSha256) ? request.compatibility.contractBasisSha256 : null,
      daemon_contract_basis_sha256: binding.compatibility.contractBasisSha256,
      retryable: false, consequential_work_started: false,
      diagnostic: "Absent, malformed, stale, replayed, unbound or unequal compatibility declaration"
    });
    return binding;
  }

  authorizeControl(projectId: string, operationId: "login:start" | "login:cancel", request: { compatibility: RuntimeCompatibilityIdentity; preflight: DelegatedPreflight }): void {
    if (operationId !== "login:start" && operationId !== "login:cancel") throw new RuntimeError("FORBIDDEN", "Unsupported control operation", 403);
    this.admit(projectId, operationId, request);
  }

  assertProjectRoot(projectId: string, canonicalRoot: string): void {
    if (this.binding(projectId).identity.canonicalRoot !== canonicalRoot) throw new RuntimeError("FORBIDDEN", "Delegated project root differs from authenticated project registration", 403);
  }

  async capabilities(projectId: string): Promise<DelegatedCapabilities> {
    const binding = this.binding(projectId);
    const configuredPosture = (await binding.consent.read(binding.identity))?.posture ?? "off";
    return { offeredRoles: [...RUNTIME_ROLES], configuredPosture,
      commandNetwork: (["off", "ask-per-destination", "on"] as const).map(posture => ({ posture, configured: posture === configuredPosture, executionSupported: posture === (binding.commandNetworkPosture ?? "off") && (posture !== "ask-per-destination" || Boolean(binding.approvals && this.approvalPort(binding))), label: posture === "on" ? "Command network on (requires matching configured worker policy and explicit consent)" : posture === "off" ? "Command network off (default)" : "Ask per destination (explicit user decision; a grant may unblock queued requests to the same destination)" })),
      approvalRecordsAvailable: binding.approvals !== undefined, approvalForwardingSupported: this.approvalPort(binding) !== undefined };
  }

  async isApprovalLive(binding: ApprovalBinding): Promise<boolean> {
    if (this.closing) return false;
    for (const [key, live] of this.liveTurns) {
      if (this.interruptedTurns.has(key)) continue;
      if (!["canonicalRoot", "cwd", "accountId", "accountEpoch", "policyDigest", "sessionId", "turnId", "workerGeneration", "scopeDigest"].every(field => live[field as keyof ApprovalBinding] === binding[field as keyof ApprovalBinding])) continue;
      const project = this.options.projects.get(key.slice(0, key.indexOf("\0")));
      const workers = await project?.supervisor.inventory();
      return !this.closing && this.liveTurns.get(key) === live && Boolean(workers?.some(worker => worker.workerId === live.turnId && worker.generation === live.workerGeneration && worker.state === "running"));
    }
    return false;
  }

  /** Trusted manager composition only; never exposed as a public control route. */
  async registerExternalApprovalWorker(projectId: string, worker: { workerId: string; generation: string }, scopeDigest: string): Promise<() => Promise<void>> {
    if (this.options.approvalOnly !== true || !/^[a-f0-9]{64}$/.test(scopeDigest)) throw new RuntimeError("FORBIDDEN", "External approval registration requires the approval-only composition", 403);
    worker = Object.freeze({ workerId: worker.workerId, generation: worker.generation });
    const binding = this.binding(projectId), key = `${projectId}\0${worker.workerId}`;
    if (!binding.approvals || !this.approvalPort(binding) || this.liveTurns.has(key)) throw new RuntimeError("FORBIDDEN", "Manager approval scope is unavailable or already registered", 403);
    const actual = await binding.supervisor.reconnect(worker.workerId, worker.generation);
    if (actual.state !== "running" || actual.workerId !== worker.workerId || actual.generation !== worker.generation) throw new RuntimeError("FORBIDDEN", "Manager worker generation is not live", 403);
    if (this.closing) throw new RuntimeError("ENGINE_UNAVAILABLE", "Approval controller is stopping", 503);
    this.liveTurns.set(key, { ...binding.identity, sessionId: worker.workerId, turnId: worker.workerId, workerGeneration: worker.generation, scopeDigest });
    let released = false, failed: unknown;
    const polling = (async () => {
      while (!released && !this.closing) {
        try { await this.syncApprovals(projectId, worker.workerId); } catch (error) { if (this.closing || released) break; failed = error; await binding.supervisor.retire(worker.workerId, worker.generation).catch(() => {}); break; }
        if (!released && !this.closing) await new Promise(resolve => setTimeout(resolve, 25));
      }
    })();
    return async () => { if (released) return; released = true; this.interruptedTurns.add(key); await polling; this.liveTurns.delete(key); this.interruptedTurns.delete(key); for (const [id, callback] of this.approvalCallbacks) if (id.startsWith(`${key}\0`)) { this.approvalCallbacks.delete(id); this.approvalSends.delete(callback.requestId); } if (failed) throw failed; };
  }
  async pendingProjectApprovals(projectId: string, scopeId?: string) {
    this.binding(projectId);
    if (scopeId) return this.pendingApprovals(projectId, scopeId);
    const scopes = [...this.liveTurns.keys()].filter(key => key.startsWith(`${projectId}\0`)).map(key => key.slice(projectId.length + 1));
    const results = await Promise.all(scopes.map(scope => this.pendingApprovals(projectId, scope).catch(error => { if (!this.liveTurns.has(`${projectId}\0${scope}`)) return []; throw error; })));
    return results.flat();
  }
  private approvalTurn(projectId: string, turnId: string, generation?: string): ApprovalBinding {
    const live = this.liveTurns.get(`${projectId}\0${turnId}`);
    if (!live || (generation !== undefined && live.workerGeneration !== generation)) throw new RuntimeError("FORBIDDEN", "Approval requires this project's live worker generation", 403);
    return live;
  }

  /** Trusted broker hook only. No public route can mint an approval request. */
  async requestApproval(projectId: string, turnId: string, context: NetworkApprovalContext, requestedBy: string) {
    const store = this.binding(projectId).approvals;
    if (!store) throw new RuntimeError("ENGINE_UNAVAILABLE", "Approval record store unavailable", 503);
    return store.request(this.approvalTurn(projectId, turnId), context, requestedBy);
  }

  private approvalPort(binding: DelegatedProjectBinding): SupervisorNetworkApprovalPort | undefined {
    if (binding.approvalForwardingEnabled !== true) return undefined;
    const port = binding.supervisor as DelegatedHarnessProcessSupervisorPort & Partial<SupervisorNetworkApprovalPort>;
    return typeof port.pendingNetworkApprovals === "function" && typeof port.replyNetworkApproval === "function" ? port as SupervisorNetworkApprovalPort : undefined;
  }
  private syncApprovals(projectId: string, turnId: string): Promise<void> {
    const key = `${projectId}\0${turnId}`, previous = this.approvalSyncs.get(key);
    if (previous) return previous;
    const pending = this.reconcileApprovals(projectId, turnId);
    this.approvalSyncs.set(key, pending);
    void pending.finally(() => { if (this.approvalSyncs.get(key) === pending) this.approvalSyncs.delete(key); }).catch(() => {});
    return pending;
  }
  private async reconcileApprovals(projectId: string, turnId: string): Promise<void> {
    const binding = this.binding(projectId), port = this.approvalPort(binding), store = binding.approvals;
    if (!port || !store) return;
    const live = this.approvalTurn(projectId, turnId);
    if (!await this.isApprovalLive(live)) return;
    const prompts = await port.pendingNetworkApprovals(turnId, live.workerGeneration);
    if (!Array.isArray(prompts) || prompts.length > 128) throw new RuntimeError("ENGINE_UNAVAILABLE", "Invalid private approval snapshot", 503);
    const prefix = `${projectId}\0${turnId}\0${live.workerGeneration}\0`, present = new Set<string>();
    for (const prompt of prompts) {
      if (!prompt || !nonempty(prompt.approvalId) || !nonempty(prompt.threadId) || !nonempty(prompt.turnId) || !Array.isArray(prompt.availableDecisions) || !prompt.availableDecisions.length || prompt.availableDecisions.some((choice: unknown) => !["allow", "deny", "acceptForSession"].includes(String(choice)))) throw new RuntimeError("ENGINE_UNAVAILABLE", "Invalid private approval prompt", 503);
      const key = prefix + prompt.approvalId; if (present.has(key)) throw new RuntimeError("ENGINE_UNAVAILABLE", "Duplicate private approval prompt", 503); present.add(key);
      const existing = this.approvalCallbacks.get(key);
      if (existing) { if (JSON.stringify(existing.prompt) !== JSON.stringify(prompt)) throw new RuntimeError("FORBIDDEN", "Approval callback identity changed", 403); continue; }
      const request = await store.request(live, prompt.networkApprovalContext, "trusted-codex-supervisor");
      this.approvalCallbacks.set(key, { requestId: request.requestId, prompt: structuredClone(prompt), sent: false });
    }
    for (const [key, entry] of this.approvalCallbacks) if (key.startsWith(prefix) && !present.has(key) && !entry.sent) await store.resolve(entry.requestId, live, "trusted-codex-supervisor");
  }
  async pendingApprovals(projectId: string, turnId: string) {
    const store = this.binding(projectId).approvals;
    if (!store) throw new RuntimeError("ENGINE_UNAVAILABLE", "Approval record store unavailable", 503);
    await this.syncApprovals(projectId, turnId);
    const requests = await store.listPending(this.approvalTurn(projectId, turnId));
    return requests.map(request => { const callback = [...this.approvalCallbacks.values()].find(value => value.requestId === request.requestId); return { ...request, ...(callback ? { availableDecisions: [...callback.prompt.availableDecisions] } : {}) }; });
  }

  interruptTurn(projectId: string, request: { turnId: string; compatibility: RuntimeCompatibilityIdentity; preflight: DelegatedPreflight }) {
    const pending = this.executeInterrupt(projectId, structuredClone(request));
    this.inFlight.add(pending);
    void pending.finally(() => this.inFlight.delete(pending)).catch(() => undefined);
    return pending;
  }

  private async executeInterrupt(projectId: string, request: { turnId: string; compatibility: RuntimeCompatibilityIdentity; preflight: DelegatedPreflight }) {
    if (!request || !nonempty(request.turnId)) throw new RuntimeError("INVALID_REQUEST", "A bounded turn identity is required");
    const binding = this.admit(projectId, `interrupt:${request.turnId}`, request);
    const live = this.approvalTurn(projectId, request.turnId);
    const key = `${projectId}\0${request.turnId}`;
    if (!await this.isApprovalLive(live) || this.interruptedTurns.has(key)) throw new RuntimeError("FORBIDDEN", "Turn is no longer interruptible", 403);
    this.interruptedTurns.add(key);
    await this.retireWorker(binding, key, live.turnId, live.workerGeneration);
    return { interrupted: true as const, turnId: live.turnId, workerGeneration: live.workerGeneration };
  }

  private retireWorker(binding: DelegatedProjectBinding, key: string, workerId: string, generation: string): Promise<void> {
    const previous = this.turnRetirements.get(key);
    if (previous) return previous;
    // Install the promise before invoking the supervisor. Interrupt, failure and
    // completion must join the same attempt, including its rejection.
    const retirement = Promise.resolve().then(() => binding.supervisor.retire(workerId, generation));
    this.turnRetirements.set(key, retirement);
    return retirement;
  }

  decideApproval(projectId: string, requestId: string, request: DelegatedApprovalDecisionRequest) {
    const pending = this.executeApprovalDecision(projectId, requestId, structuredClone(request));
    this.inFlight.add(pending);
    void pending.finally(() => this.inFlight.delete(pending)).catch(() => undefined);
    return pending;
  }

  private async executeApprovalDecision(projectId: string, requestId: string, request: DelegatedApprovalDecisionRequest) {
    if (!nonempty(requestId) || !request || typeof request !== "object") throw new RuntimeError("INVALID_REQUEST", "A bounded approval identity and request are required");
    const binding = this.admit(projectId, `approval:${requestId}`, request);
    if (!binding.approvals) throw new RuntimeError("ENGINE_UNAVAILABLE", "Approval record store unavailable", 503);
    if (!nonempty(request.turnId) || !nonempty(request.workerGeneration)) throw new RuntimeError("INVALID_REQUEST", "Approval turn and generation required");
    const live = this.approvalTurn(projectId, request.turnId, request.workerGeneration);
    await this.syncApprovals(projectId, request.turnId);
    const callback = [...this.approvalCallbacks.values()].find(value => value.requestId === requestId);
    if (callback && !callback.prompt.availableDecisions.includes(request.decision)) throw new RuntimeError("FORBIDDEN", "Decision is not offered by this provider request", 403);
    const record = await binding.approvals.decide(requestId, live, { decision: request.decision, approvedBy: request.approvedBy, explicitUserAct: request.explicitUserAct });
    const port = this.approvalPort(binding);
    if (!callback || !port) return { record, applied: false, reason: "No live provider callback is associated with this durable record" };
    if (callback.sent) return { record, applied: true, reason: "Previously written to provider transport; not an execution acknowledgement" };
    const previous = this.approvalSends.get(requestId); if (previous) return previous;
    const sending = (async () => {
      if (!await this.isApprovalLive(live)) return { record, applied: false, reason: "Worker is no longer live" };
      if (request.decision !== "deny" && !await binding.approvals!.authorize(requestId, live)) return { record, applied: false, reason: "Current consent no longer authorizes this approval" };
      try {
        const delivery = await port.replyNetworkApproval(live.turnId, live.workerGeneration, callback.prompt.approvalId, request.decision);
        if (delivery?.sent !== true) throw new Error("Unsent approval");
        callback.sent = true;
        return { record, applied: true, reason: "Written to provider transport; not an execution acknowledgement" };
      } catch { return { record, applied: false, reason: "Provider callback resolved, expired or delivery failed; no delivery acknowledged" }; }
    })();
    this.approvalSends.set(requestId, sending);
    return sending;
  }

  startGeneration(daemonId?: string): void {
    if (this.inFlight.size !== 0 || (this.options.approvalOnly && this.liveTurns.size !== 0)) throw new RuntimeError("ENGINE_UNAVAILABLE", "Previous delegated generation has not drained", 503);
    this.preflights.clear();
    if (daemonId !== undefined) this.options.daemonId = daemonId;
    this.closing = false;
  }

  async close(): Promise<void> {
    this.closing = true;
    this.preflights.clear();
    if (this.options.approvalOnly) {
      // Manager runtime owns worker interruption/retirement. This facade only
      // revokes approval admission and drains its own private reconciliations.
      await Promise.allSettled([...this.approvalSyncs.values(), ...this.inFlight]); return;
    }
    const supervisors = new Set([...this.options.projects.values()].map((binding) => binding.supervisor));
    await Promise.all([...supervisors].map(async (supervisor) => {
      const workers = await supervisor.inventory();
      await Promise.all(workers.map((worker) => supervisor.retire(worker.workerId, worker.generation)));
    }));
    await Promise.allSettled([...this.inFlight]);
  }

  grantConsent(projectId: string, request: { compatibility: RuntimeCompatibilityIdentity; preflight: DelegatedPreflight; posture: "off" | "ask-per-destination" | "on"; approvedBy: string; explicitUserAct: boolean }): Promise<{ posture: string }> {
    const pending = this.executeConsent(projectId, structuredClone(request));
    this.inFlight.add(pending);
    void pending.finally(() => this.inFlight.delete(pending)).catch(() => undefined);
    return pending;
  }

  private async executeConsent(projectId: string, request: { compatibility: RuntimeCompatibilityIdentity; preflight: DelegatedPreflight; posture: "off" | "ask-per-destination" | "on"; approvedBy: string; explicitUserAct: boolean }): Promise<{ posture: string }> {
    const binding = this.admit(projectId, "consent", request);
    if (request.explicitUserAct !== true || !nonempty(request.approvedBy) || !["off", "ask-per-destination", "on"].includes(request.posture)) {
      throw new RuntimeError("INVALID_REQUEST", "Consent requires an attributed explicit user act and known posture");
    }
    await binding.consent.grant({ identity: binding.identity, posture: request.posture, approvedBy: request.approvedBy, approvedAt: new Date().toISOString() });
    return { posture: request.posture };
  }

  turn(projectId: string, request: DelegatedTurnRequest, runtimeTools: readonly RuntimeToolDefinition[] = [], observer?: DelegatedTurnObserver): Promise<DelegatedTurnResponse> {
    const pending = this.executeTurn(projectId, structuredClone(request), [...runtimeTools], observer);
    this.inFlight.add(pending);
    void pending.finally(() => this.inFlight.delete(pending)).catch(() => undefined);
    return pending;
  }

  private async executeTurn(projectId: string, request: DelegatedTurnRequest, runtimeTools: readonly RuntimeToolDefinition[], observer?: DelegatedTurnObserver): Promise<DelegatedTurnResponse> {
    if (!request || typeof request !== "object" || typeof request.turnId !== "string") throw new RuntimeError("INVALID_REQUEST", "A scalar turn identity is required");
    if (this.options.approvalOnly) throw new RuntimeError("FORBIDDEN", "Approval-only composition cannot start delegated work", 403);
    const binding = this.admit(projectId, `turn:${request.turnId}`, request);
    if (!nonempty(request.turnId) || !/^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$/u.test(request.turnId) || typeof request.prompt !== "string" || Buffer.byteLength(request.prompt) > 65_536) {
      throw new RuntimeError("INVALID_REQUEST", "Invalid bounded turn request");
    }
    const interactionMode = request.interactionMode ?? "chat";
    if (interactionMode !== "chat" && interactionMode !== "native-plan") throw new RuntimeError("INVALID_REQUEST", "Unknown interaction mode");
    if (request.sessionId !== undefined && (!nonempty(request.sessionId) || !/^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$/u.test(request.sessionId))) throw new RuntimeError("INVALID_REQUEST", "Invalid runtime session identity");
    if (request.permissionMode !== undefined && !["readOnly", "ask", "workspaceWrite", "bypass"].includes(request.permissionMode)) throw new RuntimeError("INVALID_REQUEST", "Unknown permission mode");
    const nativePlanPort = binding.supervisor as DelegatedHarnessProcessSupervisorPort & Partial<SupervisorNativePlanPort>;
    if (interactionMode === "native-plan" && (!request.sessionId || !binding.nativePlanSink || !nativePlanPort.drainNativePlanEvents || !nativePlanPort.pendingNativePlanClarifications || !nativePlanPort.replyNativePlanClarification)) throw new RuntimeError("ENGINE_UNAVAILABLE", "Trusted native Plan supervisor and registry composition is unavailable", 503);
    const runtimeToolPort = binding.supervisor as DelegatedHarnessProcessSupervisorPort & Partial<SupervisorRuntimeToolPort>;
    const runtimeToolMap = new Map<string, RuntimeToolDefinition>();
    for (const tool of runtimeTools) {
      if (!tool || typeof tool !== "object" || !/^[A-Za-z][A-Za-z0-9_-]{0,63}$/.test(tool.name) || typeof tool.description !== "string" || !tool.description.trim() || typeof tool.inputSchema !== "object" || typeof tool.execute !== "function" || runtimeToolMap.has(tool.name)) throw new RuntimeError("INVALID_REQUEST", "Invalid or duplicate admitted runtime tool definition");
      runtimeToolMap.set(tool.name, tool);
    }
    if (runtimeToolMap.size && (!runtimeToolPort.acquireWithRuntimeTools || !runtimeToolPort.nextRuntimeToolCallback || !runtimeToolPort.replyRuntimeToolCallback)) throw new RuntimeError("ENGINE_UNAVAILABLE", "Governed runtime tool callback bridge is unavailable", 503);
    const progressPort = binding.supervisor as DelegatedHarnessProcessSupervisorPort & Partial<SupervisorTurnProgressPort>;
    if (observer && !progressPort.drainTurnProgress) throw new RuntimeError("ENGINE_UNAVAILABLE", "Delegated turn progress bridge is unavailable", 503);
    await this.verifyHosted(binding);
    const requestedRole = request.requestedRole ?? "untyped";
    if (!RUNTIME_ROLES.includes(requestedRole)) throw new RuntimeError("INVALID_REQUEST", "Unknown requested role");
    const retirement = binding.retirement;
    if (!retirement) throw new RuntimeError("ENGINE_UNAVAILABLE", "Turn retirement authority unavailable", 503);
    const identity = binding.identity;
    if (await realpath(identity.canonicalRoot) !== identity.canonicalRoot || identity.cwd !== identity.canonicalRoot) throw new RuntimeError("FORBIDDEN", "Worker root continuity is invalid", 403);
    const consent = await binding.consent.read(identity);
    if (consent === undefined) throw new RuntimeError("FORBIDDEN", "Hosted account consent is unavailable for this root/account/policy", 403);
    // This is a controlled-fixture path, not proof of network or filesystem confinement.
    // Consent and configured native posture must agree; record existence is never a network grant.
    if (consent.posture !== (binding.commandNetworkPosture ?? "off")) throw new RuntimeError("ENGINE_UNAVAILABLE", "Consent posture must match the configured native worker policy; worker policy does not match", 503);
    if (consent.posture === "ask-per-destination" && (!binding.approvals || !this.approvalPort(binding))) throw new RuntimeError("ENGINE_UNAVAILABLE", "Ask posture requires the private live approval bridge", 503);
    const actual = binding.actual ?? (binding.evidenceClass === "controlled-worker" ? { adapterId: "controlled-worker", providerId: "not-applicable", model: "not-applicable" } : undefined);
    if (!actual) throw new RuntimeError("ENGINE_UNAVAILABLE", "Trusted provider/model attribution is unavailable", 503);
    const roleEvidence = createRolePolicyEvidence({ role: requestedRole, actual, policy: binding.rolePolicy ?? { allowedTools: [], readRoots: [identity.canonicalRoot], writeRoots: [identity.canonicalRoot], networkPosture: consent.posture, processPolicy: "broker-managed", delegationPolicy: "native descent does not assign a role" } });
    const key = `${projectId}\0${request.turnId}`;
    if (this.active.has(key)) throw new RuntimeError("SESSION_TURN_IN_PROGRESS", "Turn is already running", 409);
    this.active.add(key);
    try {
      if (await retirement.read(request.turnId) !== undefined) throw new RuntimeError("INVALID_REQUEST", "Turn identity already has a durable record; automatic replay is forbidden", 409);
      if (request.previousTurnId !== undefined && (typeof request.previousTurnId !== "string" || !/^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$/u.test(request.previousTurnId))) throw new RuntimeError("INVALID_REQUEST", "Invalid previous turn identity");
      const restart = request.previousTurnId === undefined ? { method: "thread/start" as const } : await retirement.restart(request.previousTurnId, identity, roleEvidence.policyDigest);
      await retirement.prepare({ turnId: request.turnId, identity, rolePolicyDigest: roleEvidence.policyDigest, state: "prepared", ...(restart.threadId ? { threadId: restart.threadId } : {}) });
      if (this.closing) throw new RuntimeError("ENGINE_UNAVAILABLE", "Delegated runtime is shutting down", 503);
      const hostedEnvelope = { prompt: request.prompt, requestedRole, roleEvidence, interactionMode, ...(request.permissionMode ? { permissionMode: request.permissionMode } : {}),
        ...(request.attachments?.length ? { attachments: structuredClone(request.attachments) } : {}),
        ...(interactionMode === "native-plan" ? { projectId, sessionId: request.sessionId, clientTurnId: request.turnId } : {}), ...(restart.threadId ? { resumeThreadId: restart.threadId } : {}) };
      const workerInput = binding.evidenceClass === "controlled-worker" && interactionMode === "chat" && runtimeToolMap.size === 0 && !request.attachments?.length ? request.prompt : JSON.stringify(hostedEnvelope);
      const declarations: RuntimeToolCallbackDeclaration[] = [...runtimeToolMap.values()].map(({ name, description, inputSchema }) => ({ name, description, inputSchema: structuredClone(inputSchema) }));
      const worker = runtimeToolMap.size ? await runtimeToolPort.acquireWithRuntimeTools!(request.turnId, workerInput, declarations) : await binding.supervisor.acquire(request.turnId, workerInput);
      this.liveTurns.set(key, { ...identity, sessionId: request.turnId, turnId: request.turnId, workerGeneration: worker.generation });
      const nativePlanBinding = interactionMode === "native-plan" ? { projectId, sessionId: request.sessionId!, clientTurnId: request.turnId, workerId: worker.workerId, generation: worker.generation } : undefined;
      let nativePlanOpened = false, nativePlanClosed = false;
      const captureNativePlan = async () => {
        if (!nativePlanBinding || !binding.nativePlanSink) return;
        const [events, clarifications] = await Promise.all([nativePlanPort.drainNativePlanEvents!(worker.workerId, worker.generation), nativePlanPort.pendingNativePlanClarifications!(worker.workerId, worker.generation)]);
        // Empty clarification snapshots clear requests resolved by the supplier.
        await binding.nativePlanSink.capture(nativePlanBinding, events, clarifications);
      };
      const closeNativePlan = async () => {
        if (!nativePlanBinding || !binding.nativePlanSink || !nativePlanOpened || nativePlanClosed) return;
        nativePlanClosed = true; await binding.nativePlanSink.close(nativePlanBinding);
      };
      const captureProgress = async () => {
        if (!observer) return;
        for (const event of await progressPort.drainTurnProgress!(worker.workerId, worker.generation)) await observer.onProgress(event);
      };
      const runtimeToolControllers = new Set<AbortController>();
      const syncRuntimeTool = async () => {
        if (!runtimeToolMap.size) return;
        const message = await runtimeToolPort.nextRuntimeToolCallback!(worker.workerId, worker.generation);
        if (message.kind === "pending") return;
        const tool = runtimeToolMap.get(message.name);
        if (!tool) throw new RuntimeError("ENGINE_UNAVAILABLE", "Supervisor requested an unadmitted runtime tool", 503);
        const controller = new AbortController(); runtimeToolControllers.add(controller);
        let result: { success: boolean; contentItems: readonly { type: "inputText"; text: string }[] };
        try {
          let abort!: () => void;
          const interrupted = new Promise<never>((_, reject) => { abort = () => reject(new RuntimeError("INTERRUPTED", "Runtime tool callback interrupted", 499)); controller.signal.addEventListener("abort", abort, { once: true }); });
          const value = await Promise.race([tool.execute(structuredClone(message.args), controller.signal), interrupted]);
          controller.signal.removeEventListener("abort", abort);
          const text = JSON.stringify(value ?? null);
          if (Buffer.byteLength(text) > 65536) throw new Error("runtime tool result exceeds bound");
          result = { success: true, contentItems: [{ type: "inputText", text }] };
        } catch { result = { success: false, contentItems: [{ type: "inputText", text: "Runtime tool failed or was cancelled." }] }; }
        finally { runtimeToolControllers.delete(controller); }
        await runtimeToolPort.replyRuntimeToolCallback!(worker.workerId, worker.generation, message, result);
      };
      // Polling callbacks can outlive registry cleanup; retain their exact
      // generation's settled attempt rather than recreating it afterward.
      let retirementAttempt: Promise<void> | undefined;
      const retire = () => retirementAttempt ??= (async () => { for (const controller of runtimeToolControllers) controller.abort(); await this.retireWorker(binding, key, worker.workerId, worker.generation); })();
      try {
        if (nativePlanBinding && binding.nativePlanSink) { await binding.nativePlanSink.open(nativePlanBinding, nativePlanPort as SupervisorNativePlanPort); nativePlanOpened = true; }
        let waiting = true;
        const resultPromise = binding.supervisor.wait(worker.workerId, worker.generation);
        void resultPromise.finally(() => { waiting = false; for (const controller of runtimeToolControllers) controller.abort(); }).catch(() => {});
        const polling = (async () => { while (waiting) {
          if (this.approvalPort(binding) && binding.approvals) await this.syncApprovals(projectId, request.turnId);
          await captureNativePlan();
          await captureProgress();
          await syncRuntimeTool();
          if (waiting) await new Promise(resolve => setTimeout(resolve, 25));
        } })();
        void polling.catch(() => { void retire().catch(() => {}); });
        const result = await resultPromise;
        waiting = false; await polling; await captureNativePlan(); await captureProgress();
        if (result.threadId !== undefined) {
          if (retirement.associateThread === undefined) throw new RuntimeError("ENGINE_UNAVAILABLE", "Durable thread association is unavailable", 503);
          await retirement.associateThread(request.turnId, result.threadId);
        }
        // Process reconciliation must succeed before publishing any terminal.
        await retire();
        const terminal = await retirement.terminalize({ turnId: request.turnId, workerId: worker.workerId, generation: worker.generation, outcome: this.interruptedTurns.has(key) ? "interrupted" : result.exitCode === 0 ? "completed" : "failed", recordedAt: new Date().toISOString() });
        const event = { schemaVersion: 2, eventId: randomUUID(), sequence: 0, timestamp: terminal.recordedAt, projectId, sessionId: request.sessionId ?? request.turnId, turnId: request.turnId, attribution: actual,
          type: terminal.outcome === "completed" ? "turn.completed" : terminal.outcome === "interrupted" ? "turn.interrupted" : "turn.failed",
          data: terminal.outcome === "completed" ? { outcome: "completed" } : terminal.outcome === "interrupted" ? { outcome: "interrupted" } : { code: "WORKER_FAILED", message: "Delegated worker did not complete successfully" } };
        if (!validateHarnessEventV2(event)) throw new RuntimeError("INTERNAL_FAILURE", "Invalid canonical v2 terminal projection", 500);
        return { terminal, output: result.stdout, ...(result.threadId ? { providerThreadId: result.threadId } : {}), evidenceClass: binding.evidenceClass, roleEvidence, event };
      } catch (error) {
        // A transport outcome or interruption intent is not retirement evidence.
        // Keep the prepared record unresolved when cleanup cannot be confirmed.
        await retire();
        await retirement.terminalize({ turnId: request.turnId, workerId: worker.workerId, generation: worker.generation, outcome: this.interruptedTurns.has(key) ? "interrupted" : "failed", recordedAt: new Date().toISOString() });
        throw error;
      } finally {
        try { await retire(); }
        finally { await closeNativePlan(); }
      }
    } finally {
      this.turnRetirements.delete(key);
      this.interruptedTurns.delete(key);
      for (const [callbackKey, callback] of this.approvalCallbacks) if (callbackKey.startsWith(`${key}\0`)) { this.approvalCallbacks.delete(callbackKey); this.approvalSends.delete(callback.requestId); }
      this.liveTurns.delete(key);
      this.active.delete(key);
    }
  }
}

/** Public approval control surface excludes worker acquisition and consent mutation. */
export type RuntimeApprovalControlPort = Pick<DelegatedRuntime, "assertProjectRoot" | "preflight" | "pendingProjectApprovals" | "decideApproval" | "capabilities" | "startGeneration" | "close">;
