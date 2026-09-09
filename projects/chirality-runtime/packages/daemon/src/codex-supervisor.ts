import { randomUUID } from "node:crypto";
import { RuntimeError, validateHostedManagedAuth, type HostedManagedAuth, type DelegatedHarnessProcessSupervisorPort, type WorkerContinuity, type WorkerHandle, type WorkerResult, type NetworkApprovalPrompt, type NetworkApprovalChoice, type HostedConsent } from "@chirality/runtime-contracts";
import { assertContinuity, recordKey, type RuntimeConformanceConfiguration, DescendantTracker, HostedConsentStore } from "@chirality/runtime-core";
import { prepareCodexNativePolicy } from "./codex-containment.js";
import { CodexTurnSession, type CodexSessionTransport, type CodexDynamicTool } from "./codex-session.js";
import { SupplierAuthorityController } from "./supplier-authority-controller.js";

import { ManagerMailbox, type ManagerMessage } from "./codex-manager.js";

export interface CodexSupervisorOptions {
  conformance?: RuntimeConformanceConfiguration;
  executablePath: string;
  model: string;
  identity: WorkerContinuity;
  codexHome: string;
  privateDirectory: string;
  managedAuth: HostedManagedAuth;
  providerNetworkConsent: { approvedBy: string; approvalReference: string };
  requestTimeoutMs?: number;
  turnTimeoutMs?: number;
  maxWorkers?: number;
  protectedPaths?: readonly string[];
  commandNetworkPosture?: "off" | "ask-per-destination" | "on";
  /** Private daemon-owned authority. Absence is the default-off state. */
  supplierAuthority?: SupplierAuthorityController;
}
type NativePermissions = Awaited<ReturnType<typeof prepareCodexNativePolicy>>["expectedPermissions"];
/** Same semantic digest used at admission; acceptance locations are intentionally excluded. */
export function codexRuntimeConformanceConfigDigest(options: CodexSupervisorOptions, policy: { configToml: string; expectedPermissions: NativePermissions }): string {
  return recordKey({ model: options.model, executablePath: options.executablePath, identity: options.identity,
            codexHome: options.codexHome, privateDirectory: options.privateDirectory, protectedPaths: options.protectedPaths,
            managedAuth: validateHostedManagedAuth(options.managedAuth), providerNetworkConsent: options.providerNetworkConsent,
            commandNetworkPosture: options.commandNetworkPosture ?? "off", requestTimeoutMs: options.requestTimeoutMs ?? 10000,
            turnTimeoutMs: options.turnTimeoutMs ?? 120000, maxWorkers: options.maxWorkers ?? 16,
            nativeConfig: policy.configToml, expectedPermissions: policy.expectedPermissions });
}
export interface ControlledCodexLauncher { (): Promise<{ pid: number; transport: CodexSessionTransport; permissionProfile?: string; policyDigest?: string; expectedPermissions?: NativePermissions; descendantTracker?: DescendantTracker }> }
interface Entry { handle: WorkerHandle; session: CodexTurnSession; result: Promise<WorkerResult>; cleanup: () => Promise<void> }
const unavailable = (message: string) => new RuntimeError("ENGINE_UNAVAILABLE", message, 503);
function id(value: string): void { if (typeof value !== "string" || !/^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$/.test(value)) throw new RuntimeError("INVALID_REQUEST", "Invalid worker identity"); }

/** Concrete hosted-validation adapter. Supply/account checks do not accept a vendor signature or authorize account use. */
export class CodexSupervisor implements DelegatedHarnessProcessSupervisorPort {
  private readonly options: CodexSupervisorOptions;
  private fixtureLauncher?: ControlledCodexLauncher;
  private fixtureAllowUnauthenticatedModel = false;
  private barrier?: (name:string)=>Promise<void>;
  private readonly cancellations = new Map<string,{cancelled:boolean;acquiring:boolean}>();
  private readonly entries = new Map<string, Entry>();
  private readonly acquiring = new Set<string>();
  private readonly pendingAcquisitions = new Map<string, Promise<void>>();
  private closed = false;
  private readonly managers = new Map<string, ManagerMailbox>();
  constructor(options: CodexSupervisorOptions) {
    if (!options || typeof options.model !== "string" || !options.model.trim() || options.model.length > 128 || /[\x00-\x1f]/.test(options.model)) throw new RuntimeError("INVALID_REQUEST", "Explicit Codex model required");
    for (const value of [options.requestTimeoutMs ?? 10_000, options.turnTimeoutMs ?? 120_000, options.maxWorkers ?? 16]) if (!Number.isSafeInteger(value) || value < 1 || value > 600_000) throw new RuntimeError("INVALID_REQUEST", "Invalid Codex supervisor bound");
    if (options.commandNetworkPosture !== undefined && !["off", "ask-per-destination", "on"].includes(options.commandNetworkPosture)) throw new RuntimeError("INVALID_REQUEST", "Unsupported executable command-network posture");
    validateHostedManagedAuth(options.managedAuth);
    this.options = { ...structuredClone({ ...options, supplierAuthority: undefined }), supplierAuthority: options.supplierAuthority };
  }
  /** Controlled adapter tests are structurally excluded from verifyHostedBoundary. */
  static controlledForTests(options: { supplierAuthority?:SupplierAuthorityController; barrier?:(name:string)=>Promise<void>; commandNetworkPosture?: "off" | "ask-per-destination" | "on"; allowUnauthenticatedModel?: boolean; identity: WorkerContinuity; model: string; launch: ControlledCodexLauncher; requestTimeoutMs?: number; turnTimeoutMs?: number }): CodexSupervisor {
    const result = new CodexSupervisor({ identity: options.identity, model: options.model, privateDirectory: options.identity.canonicalRoot, codexHome: options.identity.canonicalRoot,
      commandNetworkPosture: options.commandNetworkPosture, executablePath: "controlled-fixture-only", managedAuth: { backend: "keyring", binding: { schema: "chirality-hosted-account-binding/v1", state: "unavailable", reason: "canonical-identity-producer-unavailable" } }, providerNetworkConsent: { approvedBy: "", approvalReference: "" }, requestTimeoutMs: options.requestTimeoutMs, turnTimeoutMs: options.turnTimeoutMs });
    result.fixtureLauncher = options.launch;
    result.options.supplierAuthority=options.supplierAuthority;
    result.barrier=options.barrier;
    result.fixtureAllowUnauthenticatedModel = options.allowUnauthenticatedModel === true;
    return result;
  }
  private requireHostedIdentity(): void {
    if (this.options.supplierAuthority?.projection().state === "ready") return;
    // Neither caller continuity, ceremony presence nor fixture data supplies a principal.
    throw unavailable("Canonical hosted identity producer is unavailable");
  }
  async verifyHostedBoundary(_identity: WorkerContinuity): Promise<void> {
    if (this.fixtureLauncher) throw unavailable("Controlled Codex fixture cannot establish a hosted boundary");
    this.requireHostedIdentity();
  }
  private async observedTransport<T extends { pid: number; transport: CodexSessionTransport }>(launched: T, tracker: DescendantTracker): Promise<T> {
    const diagnostic = (state: Awaited<ReturnType<DescendantTracker["reconcile"]>>) => new RuntimeError("ENGINE_UNAVAILABLE", "Observed worker descendants require reconciliation", 503, {
      reason: "DESCENDANT_RECONCILIATION_REQUIRED", leaderObserved: Boolean(state.leader), observed: state.observed, scans: state.scans,
      detachedCount: state.detached.length, detachedPids: state.detached.slice(0, 32).map(value => value.pid),
      ownedGroupCount: state.ownedGroup.length, identityChangedCount: state.identityChanged.length,
      censusFailed: Boolean(state.failure), limitations: state.limitations, signalAuthority: "NONE"
    });
    try { await tracker.start(); }
    catch {
      await launched.transport.close().catch(() => {});
      const state = await tracker.reconcile(); await tracker.stop();
      throw diagnostic(state);
    }
    let closing: Promise<void> | undefined;
    const close = () => closing ??= (async () => {
      await tracker.reconcile(); // Fresh before caller-owned process-group cleanup.
      let cleanupError: unknown;
      try { await launched.transport.close(); } catch (error) { cleanupError = error; }
      const after = await tracker.reconcile();
      await tracker.stop();
      if (after.failure || after.detached.length || after.identityChanged.length || after.ownedGroup.length) throw diagnostic(after);
      if (cleanupError) throw cleanupError;
    })();
    return { ...launched, transport: { stdin: launched.transport.stdin, stdout: launched.transport.stdout, close } };
  }
  private async launch(): Promise<{ pid: number; transport: CodexSessionTransport; permissionProfile?: string; policyDigest?: string; expectedPermissions?: NativePermissions }> {
    if (this.fixtureLauncher) {
      const fixture = await this.fixtureLauncher();
      return fixture.descendantTracker ? this.observedTransport(fixture, fixture.descendantTracker) : fixture;
    }
    // No production transport can be created until a separately qualified identity
    // producer and its conformance admission contract are supplied.
    this.requireHostedIdentity();
    throw unavailable("Hosted production launch is unavailable");
  }
  async startManager(workerId: string, input: string): Promise<WorkerHandle> {
    if (!this.fixtureLauncher) this.requireHostedIdentity();
    id(workerId);
    if (typeof input !== "string" || Buffer.byteLength(input) > 65536) throw unavailable("Invalid manager envelope");
    const request = JSON.parse(input);
    if (!request || Object.keys(request).sort().join(",") !== "canonicalRoot,model,prompt" || request.canonicalRoot !== this.options.identity.canonicalRoot || request.model !== this.options.model || typeof request.prompt !== "string" || this.managers.has(workerId)) throw unavailable("Manager configuration differs from trusted supervisor");
    const mailbox = new ManagerMailbox();
    this.managers.set(workerId, mailbox);
    try {
      const handle = await this.acquireInternal(workerId, JSON.stringify({ prompt: request.prompt, requestedRole: "agent1", roleEvidence: { selectedRole: "agent1", enforcementLabel: "role not mechanically enforced", evidencePosture: "instruction-asserted" } }), mailbox.tools);
      void this.wait(workerId, handle.generation).then(result => result.exitCode === 0 ? mailbox.finish(result.stdout) : mailbox.finish(undefined, unavailable("Hosted manager did not complete")), error => mailbox.finish(undefined, error));
      return handle;
    } catch (error) { this.managers.delete(workerId); mailbox.finish(undefined, error as Error); throw error; }
  }
  async nextManager(workerId: string, generation: string): Promise<ManagerMessage> {
    this.entry(workerId, generation);
    const mailbox = this.managers.get(workerId); if (!mailbox) throw unavailable("Unknown manager worker"); return mailbox.next();
  }
  async replyManager(workerId: string, generation: string, input: string): Promise<void> {
    this.entry(workerId, generation);
    const mailbox = this.managers.get(workerId); if (!mailbox) throw unavailable("Unknown manager worker"); mailbox.reply(input);
  }
  async acquire(workerId: string, input: string): Promise<WorkerHandle> { return this.acquireInternal(workerId, input); }
  cancelAdmission(workerId:string):void {const pending=this.cancellations.get(workerId);if(!pending)return;pending.cancelled=true;if(pending.acquiring)void this.options.supplierAuthority?.revoke();}
  private async acquireInternal(workerId:string,input:string,dynamicTools?:readonly CodexDynamicTool[]):Promise<WorkerHandle>{const run=()=>this.acquireGuarded(workerId,input,dynamicTools);return this.options.supplierAuthority?this.options.supplierAuthority.runGuarded(run):run();}
  private async acquireGuarded(workerId: string, input: string, dynamicTools?: readonly CodexDynamicTool[]): Promise<WorkerHandle> {
    if (!this.fixtureLauncher) this.requireHostedIdentity();
    id(workerId);
    if (this.closed || this.entries.has(workerId) || this.acquiring.has(workerId) || this.entries.size + this.acquiring.size >= (this.options.maxWorkers ?? 16)) throw unavailable("Codex worker is unavailable or already acquired");
    if (typeof input !== "string" || Buffer.byteLength(input) > 65536) throw new RuntimeError("INVALID_REQUEST", "Invalid hosted turn envelope");
    let request: { prompt: string; resumeThreadId?: string; requestedRole?: string; roleEvidence?: { selectedRole?: string; enforcementLabel?: string; evidencePosture?: string } };
    try { request = JSON.parse(input); } catch { throw new RuntimeError("INVALID_REQUEST", "Hosted worker requires the private broker JSON envelope"); }
    if (!request || typeof request !== "object" || Array.isArray(request) || Object.keys(request).some(key => !["prompt", "resumeThreadId", "requestedRole", "roleEvidence"].includes(key)) || typeof request.prompt !== "string" || !request.prompt.trim()) throw new RuntimeError("INVALID_REQUEST", "Invalid hosted turn envelope");
    if (request.resumeThreadId !== undefined) id(request.resumeThreadId);
    const selectedRole = request.requestedRole === undefined ? "untyped" : request.requestedRole;
    if (!["untyped", "agent0", "agent1", "agent2", "task"].includes(selectedRole)) throw new RuntimeError("INVALID_REQUEST", "Unknown explicitly requested role");
    const evidence = request.roleEvidence;
    if ((selectedRole !== "untyped" && !evidence) || (evidence !== undefined && (!evidence || typeof evidence !== "object" || Array.isArray(evidence) || evidence.selectedRole !== selectedRole || evidence.enforcementLabel !== "role not mechanically enforced" || evidence.evidencePosture !== "instruction-asserted"))) throw new RuntimeError("INVALID_REQUEST", "Role evidence must preserve the selected role and calibrated labels");
    const prompt = selectedRole === "untyped" ? request.prompt : `Runtime role instruction (explicit user selection): ${selectedRole}.\nrole not mechanically enforced; evidence posture: instruction-asserted.\n\n${request.prompt}`;
    const authority = this.options.supplierAuthority;
    const operationId = dynamicTools ? `manager:${workerId}` : `regular:${workerId}`;
    let authorityAcquired = false, publicationCommitted = false, releaseAttempted=false;
    const cancellation={cancelled:false,acquiring:false};this.cancellations.set(workerId,cancellation);
    const cancelled=()=>{if(cancellation.cancelled||this.closed)throw unavailable("Admission cancelled");};
    const kind=dynamicTools?"manager":"regular";
    let localEntry:Entry|undefined;let begin:(()=>void)|undefined;
    this.acquiring.add(workerId);
    let finishAcquisition!: () => void;
    this.pendingAcquisitions.set(workerId, new Promise<void>(resolve => { finishAcquisition = resolve; }));
    try {
      await this.barrier?.(`${kind}/pre-acquire`);cancelled();
      if (authority) {cancellation.acquiring=true;try{await authority.acquire(operationId);authorityAcquired=true;}finally{cancellation.acquiring=false;}}cancelled();
      if (this.fixtureLauncher) await assertContinuity(this.options.identity);
      else this.requireHostedIdentity();
      if (this.closed) throw unavailable("Supervisor is closing");
      const launched = await this.launch();
      if (this.closed) { await launched.transport.close(); throw unavailable("Supervisor closed during acquisition"); }
      const handle: WorkerHandle = { workerId, generation: randomUUID(), pid: launched.pid, state: "running" };
      let session: CodexTurnSession;
      try {
        if (!this.fixtureLauncher && (!launched.permissionProfile || launched.policyDigest !== this.options.identity.policyDigest)) throw unavailable("Native action policy binding was lost during launch");
        session = new CodexTurnSession({ transport: launched.transport, requestTimeoutMs: this.options.requestTimeoutMs, turnTimeoutMs: this.options.turnTimeoutMs,
          commandNetworkPosture: this.options.commandNetworkPosture, permissionProfile: launched.permissionProfile, policyDigest: launched.policyDigest, dynamicTools, toolTimeoutMs: this.options.turnTimeoutMs });
      } catch (error) { await launched.transport.close(); throw error; }
      if(!this.fixtureLauncher){
        try{await session.initialize();if(!launched.expectedPermissions)throw unavailable("Native effective-policy verification basis is missing");await session.verifyNativePolicy(launched.expectedPermissions);}
        catch(error){await session.close();await launched.transport.close();throw error;}
      }
      // Drain bounded actor events; the authoritative result still comes only from waitTurn.
      void (async () => { for await (const _event of session.events()) { /* actor output accumulated in terminal */ } })().catch(() => {});
      const admitted=new Promise<void>(resolve=>{begin=resolve;});
      const result = (async (): Promise<WorkerResult> => {
        await admitted;
        try {
          if(!publicationCommitted)throw unavailable("Admission cancelled before publication");
          if(this.fixtureLauncher){await session.initialize();if(launched.expectedPermissions)await session.verifyNativePolicy(launched.expectedPermissions);}
          const account = await session.accountRead();
          if (!account.hasAccount && !(this.fixtureLauncher && this.fixtureAllowUnauthenticatedModel && account.authRequired === false)) throw unavailable("Codex has no root-private authenticated account");
          if (!this.fixtureLauncher) this.requireHostedIdentity();
          const threadId = request.resumeThreadId
            ? await session.resumeThread({ threadId: request.resumeThreadId, model: this.options.model, continuityChecked: true })
            : await session.startThread({ cwd: this.options.identity.canonicalRoot, model: this.options.model, continuityChecked: true });
          const turnId = await session.startTurn({ threadId, text: prompt, model: this.options.model });
          const terminal = await session.waitTurn(turnId);
          return { worker: { ...handle, state: "exited" }, exitCode: terminal.status === "completed" ? 0 : terminal.status === "failed" ? 1 : null,
            signal: terminal.status === "interrupted" ? "SIGTERM" : null, stdout: terminal.output, stderr: "", threadId };
        } finally { handle.state = "exited"; await session.close(); await launched.transport.close(); }
      })();
      void result.catch(() => {});
      localEntry={handle,session,result,cleanup:launched.transport.close};
      await this.barrier?.(`${kind}/post-acquire-pre-worker-publication`);cancelled();authority?.assertCommit(operationId);
      this.entries.set(workerId,localEntry);
      publicationCommitted = true;begin?.();
      await this.barrier?.(`${kind}/post-publication-pre-release`);
      if (authority) {releaseAttempted=true;await authority.release(operationId);}
      cancelled();return { ...handle };
    } catch (error) {
      // Removal is synchronous and precedes all cleanup awaits and caller return.
      if(localEntry&&this.entries.get(workerId)===localEntry)this.entries.delete(workerId);
      begin?.();
      if (authorityAcquired && authority) {
        if (publicationCommitted) {if(!releaseAttempted){releaseAttempted=true;await authority.release(operationId).catch(()=>authority.revoke());}}
        else await authority.abort(operationId).catch(()=>authority.revoke());
      }
      if(localEntry){await localEntry.session.close();await localEntry.result.catch(()=>{});await localEntry.cleanup();}
      throw error;
    } finally { this.cancellations.delete(workerId);this.acquiring.delete(workerId); this.pendingAcquisitions.delete(workerId); finishAcquisition(); }
  }

  async inventory(): Promise<readonly WorkerHandle[]> { return [...this.entries.values()].map(entry => ({ ...entry.handle })); }
  private entry(workerId: string, generation: string): Entry { const entry = this.entries.get(workerId); if (!entry || entry.handle.generation !== generation) throw unavailable("Unknown or stale Codex generation"); return entry; }
  async describeApprovalScope(workerId?: string, generation?: string): Promise<{ identity: WorkerContinuity; model: string; commandNetworkPosture: "off" | "ask-per-destination" | "on"; consent?: HostedConsent }> {
    if (this.closed || (workerId === undefined) !== (generation === undefined)) throw unavailable("Approval scope description unavailable");
    if (workerId !== undefined && generation !== undefined) { const entry = this.entry(workerId, generation); if (entry.handle.state !== "running") throw unavailable("Approval worker is no longer running"); }
    const consent = await new HostedConsentStore({ canonicalRoot: this.options.identity.canonicalRoot, codexHome: this.options.codexHome }).read(this.options.identity);
    return { identity: { ...this.options.identity }, model: this.options.model, commandNetworkPosture: this.options.commandNetworkPosture ?? "off", ...(consent ? { consent } : {}) };
  }
  async pendingNetworkApprovals(workerId: string, generation: string): Promise<readonly NetworkApprovalPrompt[]> {
    const entry = this.entry(workerId, generation);
    return entry.handle.state === "running" ? entry.session.pendingNetworkApprovals() : [];
  }
  async replyNetworkApproval(workerId: string, generation: string, approvalId: string, decision: NetworkApprovalChoice): Promise<{ sent: true }> {
    const entry = this.entry(workerId, generation);
    if (entry.handle.state !== "running") throw unavailable("Approval worker is no longer running");
    if (!this.fixtureLauncher) {
      this.requireHostedIdentity();
      const consent = await new HostedConsentStore({ canonicalRoot: this.options.identity.canonicalRoot, codexHome: this.options.codexHome }).read(this.options.identity);
      if (consent?.posture !== "ask-per-destination" || this.options.commandNetworkPosture !== "ask-per-destination") throw unavailable("Approval consent or configured identity changed");
    }
    return entry.session.replyNetworkApproval(approvalId, decision);
  }
  async reconnect(workerId: string, generation: string): Promise<WorkerHandle> { return { ...this.entry(workerId, generation).handle }; }
  async wait(workerId: string, generation: string): Promise<WorkerResult> { return this.entry(workerId, generation).result; }
  async retire(workerId: string, generation: string): Promise<void> { const entry = this.entry(workerId, generation); this.managers.get(workerId)?.finish(undefined, unavailable("Manager retired")); this.managers.delete(workerId); await entry.session.close(); await entry.result.catch(() => {}); await entry.cleanup(); if (this.entries.get(workerId) === entry) this.entries.delete(workerId); }
  async close(): Promise<void> { this.closed = true; for(const id of this.cancellations.keys())this.cancelAdmission(id); await Promise.all([...this.pendingAcquisitions.values()]); await Promise.all([...this.entries.values()].map(entry => this.retire(entry.handle.workerId, entry.handle.generation))); await this.options.supplierAuthority?.close(); }
}
export function createControlledCodexSupervisorForTests(options: Parameters<typeof CodexSupervisor.controlledForTests>[0]): CodexSupervisor { return CodexSupervisor.controlledForTests(options); }
