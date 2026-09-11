import { randomUUID } from "node:crypto";
import { HOSTED_MODEL_ID_PATTERN, HOSTED_REASONING_EFFORT_PATTERN, RuntimeError, validateHostedManagedAuth, validateHostedModelCatalogEntries, type HostedManagedAuth, type HostedModelCatalogEntry, type DelegatedAttachmentInput, type DelegatedHarnessProcessSupervisorPort, type WorkerContinuity, type WorkerHandle, type WorkerResult, type NetworkApprovalPrompt, type NetworkApprovalChoice, type HostedConsent, type NativePlanTransportEvent, type NativePlanClarificationPrompt, type NativePlanClarificationAnswers, type RuntimeToolCallbackDeclaration, type RuntimeToolCallbackMessage, type RuntimeToolCallbackResult, type DelegatedTurnProgressEvent } from "@chirality/runtime-contracts";
import { assertContinuity, recordKey, verifyConfiguredRuntimeConformance, withRetirementFailure, type RuntimeConformanceConfiguration, DescendantTracker, HostedConsentStore } from "@chirality/runtime-core";
import { prepareCodexNativePolicy } from "./codex-containment.js";
import { CodexTurnSession, type CodexSessionTransport, type CodexDynamicTool, type CodexDynamicToolResult } from "./codex-session.js";
import { SupplierAuthorityController } from "./supplier-authority-controller.js";
import type { AuthenticatedCodexCandidate } from "./codex-authenticated-transport.js";
import type { CodexCandidateLauncherFactory } from "./codex-admitted-launcher.js";
import { completeRuntimeWorkerInstanceV2FromP2, revalidateHostedAccountAuthorityV2, revalidateRuntimeInstanceAdmissionV2, revalidateRuntimeWorkerInstancePreparationV2, type RuntimeInstanceAdmissionInputV2, type RuntimeInstanceAdmissionV2, type RuntimeWorkerInstancePreparationV2 } from "./runtime-conformance-v2-admission.js";
import type { HostedPackagedReleaseBasisV2 } from "./hosted-packaged-release-state.js";

import { ManagerMailbox, type ManagerMessage } from "./codex-manager.js";

export interface CodexSupervisorOptions {
  conformance?: RuntimeConformanceConfiguration;
  executablePath: string;
  model: string;
  reasoningEffort?: string;
  /** Authenticated non-hidden catalog. Envelope model/effort outside it fail before any provider request. */
  modelCatalog?: readonly HostedModelCatalogEntry[];
  identity: WorkerContinuity;
  codexHome: string;
  privateDirectory: string;
  managedAuth?: HostedManagedAuth;
  /** V2 storage backend policy. Account identity remains bound by the admitted same-actor authority. */
  accountStorageBackend?: "keyring";
  providerNetworkConsent: { approvedBy: string; approvalReference: string };
  requestTimeoutMs?: number;
  turnTimeoutMs?: number;
  maxWorkers?: number;
  protectedPaths?: readonly string[];
  readOnlyProjectPaths?: readonly string[];
  commandNetworkPosture?: "off" | "ask-per-destination" | "on";
  /** Exact native action-policy profile implemented by this supervisor. */
  supportedPermissionMode?: "workspaceWrite";
  /** Legacy controlled-test authority. Production authority is established per candidate. */
  supplierAuthority?: SupplierAuthorityController;
  /** Trusted nonexecuting candidate launcher. Absence preserves the production default-off launch gate. */
  candidateLauncherFactory?: CodexCandidateLauncherFactory;
}
export interface HostedCodexSupervisorOptions extends Omit<CodexSupervisorOptions, "identity" | "supplierAuthority" | "candidateLauncherFactory"> {
  canonicalRoot: string;
  candidateLauncherFactory: CodexCandidateLauncherFactory;
  conformance?: RuntimeConformanceConfiguration;
  configDigest: string;
  consentVersion: string;
  runtimeV2?: { releaseBasis: Readonly<HostedPackagedReleaseBasisV2>; instanceInput: RuntimeInstanceAdmissionInputV2; instanceAdmission: RuntimeInstanceAdmissionV2 };
  runtimeV2Preparation?: RuntimeWorkerInstancePreparationV2;
}
export interface HostedCodexSupervisorAdmission {
  supervisor: CodexSupervisor;
  continuity: WorkerContinuity;
  authority: { supplierGeneration: string; identityGeneration: string; snapshotDigest: string };
  /** Stable digest of the privately observed account/workspace pair; no raw identity leaves the session. */
  accountDigest: string;
  runtimeV2?: NonNullable<HostedCodexSupervisorOptions["runtimeV2"]>;
  retire(): Promise<void>;
}
export type ControlledHostedConformanceVerifier = (input: {
  configuration: RuntimeConformanceConfiguration;
  actual: Parameters<typeof verifyConfiguredRuntimeConformance>[1];
}) => Promise<void>;
type NativePermissions = Awaited<ReturnType<typeof prepareCodexNativePolicy>>["expectedPermissions"];
/** Same semantic digest used at admission; acceptance locations are intentionally excluded. */
export function codexRuntimeConformanceConfigDigest(options: CodexSupervisorOptions, policy: { configToml: string; expectedPermissions: NativePermissions }): string {
  return recordKey({ model: options.model, executablePath: options.executablePath, identity: options.identity,
            codexHome: options.codexHome, privateDirectory: options.privateDirectory, protectedPaths: options.protectedPaths, readOnlyProjectPaths: options.readOnlyProjectPaths,
            ...(options.accountStorageBackend ? { accountStorage: { backend: options.accountStorageBackend } } : { managedAuth: validateHostedManagedAuth(options.managedAuth!) }), providerNetworkConsent: options.providerNetworkConsent,
            commandNetworkPosture: options.commandNetworkPosture ?? "off", requestTimeoutMs: options.requestTimeoutMs ?? 10000,
            supportedPermissionMode: options.supportedPermissionMode ?? "workspaceWrite",
            turnTimeoutMs: options.turnTimeoutMs ?? 120000, maxWorkers: options.maxWorkers ?? 16,
            nativeConfig: policy.configToml, expectedPermissions: policy.expectedPermissions });
}
export interface ControlledCodexLauncher { (): Promise<{ pid: number; transport: CodexSessionTransport; permissionProfile?: string; policyDigest?: string; expectedPermissions?: NativePermissions; descendantTracker?: DescendantTracker }> }
interface NativePlanBinding { projectId: string; sessionId: string; clientTurnId: string }
interface Entry { handle: WorkerHandle; session: CodexTurnSession; result: Promise<WorkerResult>; cleanup: () => Promise<void>; nativePlanBinding?: NativePlanBinding; nativePlanEvents: NativePlanTransportEvent[]; turnProgress: DelegatedTurnProgressEvent[] }
interface AdmittedCandidate { candidate: AuthenticatedCodexCandidate; session: CodexTurnSession; authority: SupplierAuthorityController; continuity: WorkerContinuity; evidence: HostedCodexSupervisorAdmission["authority"]; accountDigest: string; runtimeV2?: NonNullable<HostedCodexSupervisorOptions["runtimeV2"]> }
const unavailable = (message: string) => new RuntimeError("ENGINE_UNAVAILABLE", message, 503);
/**
 * Per-field ceilings for the supervisor's operational budgets. A request
 * budget covers one app-server exchange; a turn budget covers a whole
 * agentic turn and may legitimately run for many minutes, but never beyond
 * the descendant tracker's one-hour lifetime.
 */
export const CODEX_SUPERVISOR_BOUNDS = Object.freeze({
  requestTimeoutMs: Object.freeze({ min: 1, max: 600_000 }),
  turnTimeoutMs: Object.freeze({ min: 1, max: 3_600_000 }),
  maxWorkers: Object.freeze({ min: 1, max: 1_024 })
});
export function assertCodexSupervisorBounds(options: { requestTimeoutMs?: number; turnTimeoutMs?: number; maxWorkers?: number }): void {
  const values = { requestTimeoutMs: options.requestTimeoutMs ?? 10_000, turnTimeoutMs: options.turnTimeoutMs ?? 120_000, maxWorkers: options.maxWorkers ?? 16 };
  for (const key of ["requestTimeoutMs", "turnTimeoutMs", "maxWorkers"] as const) {
    const value = values[key], bound = CODEX_SUPERVISOR_BOUNDS[key];
    if (!Number.isSafeInteger(value) || value < bound.min || value > bound.max) throw new RuntimeError("INVALID_REQUEST", "Invalid Codex supervisor bound");
  }
}
function id(value: string): void { if (typeof value !== "string" || !/^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$/.test(value)) throw new RuntimeError("INVALID_REQUEST", "Invalid worker identity"); }

class RuntimeToolMailbox {
  private readonly callbacks = new Map<string, { message: Extract<RuntimeToolCallbackMessage, {kind:"callback"}>; delivered: boolean; resolve(value: CodexDynamicToolResult): void; reject(error: Error): void }>();
  private terminal?: Error;
  private static callbackKey(message: Pick<Extract<RuntimeToolCallbackMessage, {kind:"callback"}>, "callId" | "threadId" | "turnId" | "nativeChild">): string {
    return JSON.stringify(message.nativeChild
      ? ["child", message.nativeChild.associationId, message.threadId, message.turnId, message.callId]
      : ["primary", message.threadId, message.turnId, message.callId]);
  }
  readonly tools: readonly CodexDynamicTool[];
  constructor(declarations: readonly RuntimeToolCallbackDeclaration[]) {
    if (!Array.isArray(declarations) || declarations.length < 1 || declarations.length > 32) throw new RuntimeError("INVALID_REQUEST", "Invalid admitted runtime tool declarations");
    this.tools = declarations.map(declaration => {
      if (!declaration || typeof declaration !== "object" || !/^[A-Za-z][A-Za-z0-9_-]{0,63}$/.test(declaration.name) || typeof declaration.description !== "string" || !declaration.description.trim() || typeof declaration.inputSchema !== "object") throw new RuntimeError("INVALID_REQUEST", "Invalid admitted runtime tool declaration");
      return { ...structuredClone(declaration), handler: async (args, context) => {
        const message = { kind: "callback" as const, callId: context.callId, threadId: context.threadId, turnId: context.turnId, name: declaration.name, args, ...(context.nativeChild ? { nativeChild: structuredClone(context.nativeChild) } : {}) };
        const key = RuntimeToolMailbox.callbackKey(message);
        if (this.terminal || this.callbacks.has(key) || this.callbacks.size >= 8) throw unavailable("Runtime tool callback unavailable");
        return await new Promise((resolve, reject) => this.callbacks.set(key, { message, delivered: false, resolve, reject }));
      } };
    });
    if (new Set(this.tools.map(tool => tool.name)).size !== this.tools.length) throw new RuntimeError("INVALID_REQUEST", "Duplicate admitted runtime tool declaration");
  }
  next(): RuntimeToolCallbackMessage {
    if (this.terminal) return { kind: "pending" };
    const callback = [...this.callbacks.values()].find(value => !value.delivered);
    if (!callback) return { kind: "pending" };
    callback.delivered = true; return structuredClone(callback.message);
  }
  reply(message: Extract<RuntimeToolCallbackMessage, {kind:"callback"}>, result: RuntimeToolCallbackResult): void {
    const key = RuntimeToolMailbox.callbackKey(message), callback = this.callbacks.get(key);
    if (!callback || !callback.delivered || JSON.stringify(callback.message) !== JSON.stringify(message)) throw new RuntimeError("INVALID_REQUEST", "Unknown or stale runtime tool callback");
    if (!result || typeof result.success !== "boolean" || !Array.isArray(result.contentItems) || result.contentItems.length !== 1 || result.contentItems[0]?.type !== "inputText" || typeof result.contentItems[0].text !== "string" || Buffer.byteLength(result.contentItems[0].text) > 65536) throw new RuntimeError("INVALID_REQUEST", "Invalid runtime tool callback result");
    this.callbacks.delete(key); callback.resolve(structuredClone(result));
  }
  finish(error: Error = unavailable("Runtime tool worker ended")): void { this.terminal = error; for (const callback of this.callbacks.values()) callback.reject(error); this.callbacks.clear(); }
}

function censusFailureText(failure: unknown): string {
  const text = failure instanceof Error ? `${failure.name}: ${failure.message}` : String(failure);
  return text.length > 256 ? `${text.slice(0, 256)}…` : text;
}
async function failAfterCleanup(error: unknown, closes: Array<() => Promise<unknown> | undefined>): Promise<never> {
  const failures: unknown[] = [error];
  for (const close of closes) try { await close(); } catch (cleanup) { failures.push(cleanup); }
  if (failures.length > 1) throw new AggregateError(failures, "Codex admission and retirement failed");
  throw error;
}
/** Concrete hosted-validation adapter. Supply/account checks do not accept a vendor signature or authorize account use. */
export class CodexSupervisor implements DelegatedHarnessProcessSupervisorPort {
  private readonly options: CodexSupervisorOptions;
  private fixtureLauncher?: ControlledCodexLauncher;
  private fixtureAllowUnauthenticatedModel = false;
  private barrier?: (name:string)=>Promise<void>;
  private readonly cancellations = new Map<string,{cancelled:boolean;acquiring:boolean;authority?:SupplierAuthorityController}>();
  private readonly entries = new Map<string, Entry>();
  private readonly acquiring = new Set<string>();
  private readonly pendingAcquisitions = new Map<string, Promise<void>>();
  private closed = false;
  private readonly managers = new Map<string, ManagerMailbox>();
  private readonly runtimeToolMailboxes = new Map<string, RuntimeToolMailbox>();
  private candidateLauncherFactory?: CodexCandidateLauncherFactory;
  private controlledVerifyConformance?: ControlledHostedConformanceVerifier;
  private conformance?: Pick<HostedCodexSupervisorOptions, "conformance" | "configDigest" | "consentVersion" | "runtimeV2"> & { accountDigest: string };
  private preadmitted?: AdmittedCandidate;
  constructor(options: CodexSupervisorOptions) {
    if (!options || typeof options.model !== "string" || !options.model.trim() || options.model.length > 128 || /[\x00-\x1f]/.test(options.model)) throw new RuntimeError("INVALID_REQUEST", "Explicit Codex model required");
    if (options.reasoningEffort !== undefined && !HOSTED_REASONING_EFFORT_PATTERN.test(options.reasoningEffort)) throw new RuntimeError("INVALID_REQUEST", "Invalid Codex reasoning effort");
    if (options.modelCatalog !== undefined) {
      const catalog = validateHostedModelCatalogEntries(options.modelCatalog);
      const admitted = catalog.find(entry => entry.model === options.model);
      if (!admitted || (options.reasoningEffort !== undefined && !admitted.supportedReasoningEfforts.includes(options.reasoningEffort))) throw new RuntimeError("INVALID_REQUEST", "Admitted Codex model or reasoning effort is outside its catalog");
    }
    assertCodexSupervisorBounds(options);
    if (options.commandNetworkPosture !== undefined && !["off", "ask-per-destination", "on"].includes(options.commandNetworkPosture)) throw new RuntimeError("INVALID_REQUEST", "Unsupported executable command-network posture");
    if (options.supportedPermissionMode !== undefined && options.supportedPermissionMode !== "workspaceWrite") throw new RuntimeError("INVALID_REQUEST", "Unsupported native permission profile");
    if ((options.accountStorageBackend === "keyring") === (options.managedAuth !== undefined)) throw new RuntimeError("INVALID_REQUEST", "Codex account storage policy must use exactly one Runtime generation");
    if (options.managedAuth) validateHostedManagedAuth(options.managedAuth);
    this.options = { ...structuredClone({ ...options, supplierAuthority: undefined, candidateLauncherFactory: undefined }), supplierAuthority: options.supplierAuthority };
    this.candidateLauncherFactory = options.candidateLauncherFactory;
  }
  static async admitHosted(options: HostedCodexSupervisorOptions): Promise<HostedCodexSupervisorAdmission> {
    return CodexSupervisor.admitHostedWithVerifier(options);
  }
  private static async admitHostedWithVerifier(options: HostedCodexSupervisorOptions, verifyConformance?: ControlledHostedConformanceVerifier): Promise<HostedCodexSupervisorAdmission> {
    if (options.accountStorageBackend === "keyring") {
      if ((options.runtimeV2 !== undefined) === (options.runtimeV2Preparation !== undefined)) throw unavailable("Exactly one worker v2 admission state is required");
      if (options.runtimeV2) await revalidateRuntimeInstanceAdmissionV2(options.runtimeV2.instanceInput, options.runtimeV2.instanceAdmission);
      else await revalidateRuntimeWorkerInstancePreparationV2(options.runtimeV2Preparation!);
    } else if (options.runtimeV2 || options.runtimeV2Preparation) throw unavailable("Worker v2 admission requires keyring storage");
    const raw = await options.candidateLauncherFactory.create().launchCandidate();
    const observed = await CodexSupervisor.observeTransport(raw, raw.descendantTracker);
    const candidate: AuthenticatedCodexCandidate = { ...observed, cleanup: observed.transport.close };
    let admitted: AdmittedCandidate | undefined;
    try {
      admitted = await CodexSupervisor.admitCandidate(options, candidate, verifyConformance);
      const { runtimeV2: _runtimeV2, runtimeV2Preparation: _runtimeV2Preparation, canonicalRoot: _canonicalRoot, ...supervisorOptions } = options;
      const supervisor = new CodexSupervisor({ ...supervisorOptions, identity: admitted.continuity, candidateLauncherFactory: options.candidateLauncherFactory });
      supervisor.controlledVerifyConformance = verifyConformance;
      supervisor.conformance = { conformance: options.conformance, configDigest: options.configDigest, accountDigest: admitted.accountDigest, consentVersion: options.consentVersion, ...(admitted.runtimeV2 ? { runtimeV2: admitted.runtimeV2 } : {}) };
      supervisor.preadmitted = admitted;
      return Object.freeze({ supervisor, continuity: { ...admitted.continuity }, authority: { ...admitted.evidence }, accountDigest: admitted.accountDigest, ...(admitted.runtimeV2 ? { runtimeV2: admitted.runtimeV2 } : {}), retire: () => supervisor.close() });
    } catch (error) { return failAfterCleanup(error, [() => admitted?.authority.close(), () => candidate.cleanup()]); }
  }
  private static async admitCandidate(options: Omit<HostedCodexSupervisorOptions, "candidateLauncherFactory"> & { expectedAccountDigest?: string }, candidate: AuthenticatedCodexCandidate, controlledVerifyConformance?: ControlledHostedConformanceVerifier): Promise<AdmittedCandidate> {
    if (options.runtimeV2Preparation) await revalidateRuntimeWorkerInstancePreparationV2(options.runtimeV2Preparation);
    const session = new CodexTurnSession({ runtimeV2: options.runtimeV2, transport: candidate.transport, requestTimeoutMs: options.requestTimeoutMs, turnTimeoutMs: options.turnTimeoutMs,
      commandNetworkPosture: options.commandNetworkPosture, permissionProfile: candidate.expectedPolicy.permissionProfile, policyDigest: candidate.expectedPolicy.policyDigest,
      nativeSkills: candidate.expectedPolicy.nativeSkills });
    let authority: SupplierAuthorityController | undefined;
    try {
      if (options.runtimeV2) await revalidateRuntimeInstanceAdmissionV2(options.runtimeV2.instanceInput, options.runtimeV2.instanceAdmission);
      authority = await session.establishAuthority(candidate.authorityInitialize, candidate.kernelLease, async () => {
        try { await candidate.privateBindingStore.fence("revoke"); } finally { await candidate.cleanup(); }
      });
      const bound = await session.establishHostedIdentityBinding(candidate.privateBindingStore, authority, candidate.supplierGeneration);
      await assertContinuity(bound.continuity);
      if (bound.continuity.canonicalRoot !== options.canonicalRoot || bound.continuity.cwd !== options.canonicalRoot
        || bound.continuity.policyDigest !== candidate.expectedPolicy.policyDigest) throw unavailable("Candidate continuity does not match its project and native policy");
      let runtimeV2 = options.runtimeV2;
      if (options.runtimeV2Preparation) {
        const completed = await completeRuntimeWorkerInstanceV2FromP2(options.runtimeV2Preparation, {
          accountId: bound.continuity.accountId,
          accountEpoch: bound.continuity.accountEpoch,
          accountDigest: bound.accountDigest
        });
        runtimeV2 = { releaseBasis: options.runtimeV2Preparation.releaseBasis, ...completed };
      }
      await session.verifyNativePolicy(candidate.expectedPolicy.expectedPermissions, candidate.expectedPolicy.nativeRoleConfiguration);
      if (candidate.expectedToolRuntime.codexSelfExecutablePath !== options.executablePath) throw unavailable("Candidate executable differs from the trusted supervisor binding");
      const account = await session.accountRead();
      if (!account.hasAccount) throw unavailable("Codex has no root-private authenticated account");
      if (options.expectedAccountDigest !== undefined && bound.accountDigest !== options.expectedAccountDigest) throw unavailable("Fresh candidate account identity changed");
      if (runtimeV2) {
        const expectedAccount = runtimeV2.instanceInput.account;
        if (!expectedAccount || expectedAccount.accountId !== bound.continuity.accountId || expectedAccount.accountEpoch !== bound.continuity.accountEpoch || expectedAccount.accountDigest !== bound.accountDigest
          || candidate.expectedOuterPolicyDigest !== runtimeV2.instanceInput.outerPolicyDigest || candidate.expectedPolicy.policyDigest !== runtimeV2.instanceInput.nativePolicyDigest
          || candidate.expectedEffectiveConfigDigestV2 !== runtimeV2.instanceInput.effectiveConfigDigest
          || recordKey(candidate.expectedPolicy.policyInstanceV2) !== recordKey(runtimeV2.instanceInput.policy)) throw unavailable("Fresh candidate differs from its v2 instance admission");
      }
      const conformanceActual = { canonicalRoot: bound.continuity.canonicalRoot, cwd: bound.continuity.cwd,
        policyDigest: bound.continuity.policyDigest, configDigest: options.configDigest, accountId: bound.continuity.accountId,
        accountEpoch: bound.continuity.accountEpoch, accountDigest: bound.accountDigest, consentVersion: options.consentVersion,
        executablePath: candidate.expectedToolRuntime.codexSelfExecutablePath };
      if (options.conformance) {
        if (controlledVerifyConformance) await controlledVerifyConformance({ configuration: options.conformance, actual: conformanceActual });
        else await verifyConfiguredRuntimeConformance(options.conformance, conformanceActual);
      } else if (!runtimeV2) throw unavailable("Runtime conformance is unavailable");
      if (!candidate.expectedToolRuntime.requiresSandboxedFileSystem || !candidate.expectedToolRuntime.requiresSandboxedFileStreaming) throw unavailable("Required sandboxed file runtime is unavailable");
      if (runtimeV2) await revalidateRuntimeInstanceAdmissionV2(runtimeV2.instanceInput, runtimeV2.instanceAdmission);
      return { candidate, session, authority, continuity: bound.continuity, evidence: bound.authority, accountDigest: bound.accountDigest, ...(runtimeV2 ? { runtimeV2 } : {}) };
    } catch (error) { return failAfterCleanup(error, [() => authority?.close(), () => session.close(), () => candidate.cleanup()]); }
  }
  /** Controlled adapter tests are structurally excluded from verifyHostedBoundary. */
  static controlledForTests(options: { supplierAuthority?:SupplierAuthorityController; barrier?:(name:string)=>Promise<void>; commandNetworkPosture?: "off" | "ask-per-destination" | "on"; allowUnauthenticatedModel?: boolean; identity: WorkerContinuity; model: string; reasoningEffort?: string; modelCatalog?: readonly HostedModelCatalogEntry[]; launch: ControlledCodexLauncher; requestTimeoutMs?: number; turnTimeoutMs?: number }): CodexSupervisor {
    const result = new CodexSupervisor({ identity: options.identity, model: options.model, ...(options.reasoningEffort === undefined ? {} : { reasoningEffort: options.reasoningEffort }), ...(options.modelCatalog === undefined ? {} : { modelCatalog: options.modelCatalog }), privateDirectory: options.identity.canonicalRoot, codexHome: options.identity.canonicalRoot,
      commandNetworkPosture: options.commandNetworkPosture, executablePath: "controlled-fixture-only", managedAuth: { backend: "keyring", binding: { schema: "chirality-hosted-account-binding/v1", state: "unavailable", reason: "canonical-identity-producer-unavailable" } }, providerNetworkConsent: { approvedBy: "", approvalReference: "" }, requestTimeoutMs: options.requestTimeoutMs, turnTimeoutMs: options.turnTimeoutMs });
    result.fixtureLauncher = options.launch;
    result.options.supplierAuthority=options.supplierAuthority;
    result.barrier=options.barrier;
    result.fixtureAllowUnauthenticatedModel = options.allowUnauthenticatedModel === true;
    return result;
  }
  /** Last line before launch: an envelope choice must be the admitted default or a member of the admitted catalog. */
  private assertCatalogChoice(model: unknown, reasoningEffort: unknown): { model: string; reasoningEffort?: string } {
    const invalid = (message: string) => new RuntimeError("INVALID_REQUEST", message, 400, { reason: "MODEL_NOT_IN_CATALOG" });
    if (model !== undefined && (typeof model !== "string" || !HOSTED_MODEL_ID_PATTERN.test(model))) throw invalid("Invalid hosted turn envelope model");
    if (reasoningEffort !== undefined && (typeof reasoningEffort !== "string" || !HOSTED_REASONING_EFFORT_PATTERN.test(reasoningEffort))) throw invalid("Invalid hosted turn envelope reasoning effort");
    const selectedModel = model ?? this.options.model;
    const catalog = this.options.modelCatalog;
    if (catalog === undefined) {
      if (selectedModel !== this.options.model) throw invalid(`Model '${selectedModel}' is not the admitted Codex model`);
      if (reasoningEffort !== undefined && reasoningEffort !== this.options.reasoningEffort) throw new RuntimeError("INVALID_REQUEST", `Reasoning effort '${reasoningEffort}' is not the admitted Codex reasoning effort`, 400, { reason: "REASONING_EFFORT_UNSUPPORTED" });
      return { model: selectedModel, reasoningEffort: this.options.reasoningEffort };
    }
    const entry = catalog.find(candidate => candidate.model === selectedModel);
    if (!entry) throw invalid(`Model '${selectedModel}' is not in the authenticated Codex catalog`);
    const effort = reasoningEffort ?? (selectedModel === this.options.model ? this.options.reasoningEffort : entry.defaultReasoningEffort);
    if (effort !== undefined && !entry.supportedReasoningEfforts.includes(effort)) throw new RuntimeError("INVALID_REQUEST", `Reasoning effort '${effort}' is not supported by '${selectedModel}'`, 400, { reason: "REASONING_EFFORT_UNSUPPORTED" });
    return { model: selectedModel, reasoningEffort: effort };
  }
  private async revalidateCurrentHost(): Promise<void> {
    const input = this.conformance?.runtimeV2?.instanceInput;
    if (input) await revalidateHostedAccountAuthorityV2(input.hostAuthority, { purpose: input.purposeRelease.purpose, projectId: input.projectId, manifestHash: input.manifestHash, canonicalRoot: input.canonicalRoot, account: input.account, consentDigest: input.consent.digest });
  }
  private requireHostedIdentity(): void {
    if (this.options.supplierAuthority?.projection().state === "ready" || (this.candidateLauncherFactory && this.conformance)) return;
    // Neither caller continuity, ceremony presence nor fixture data supplies a principal.
    throw unavailable("Canonical hosted identity producer is unavailable");
  }
  async verifyHostedBoundary(_identity: WorkerContinuity): Promise<void> {
    if (this.fixtureLauncher) throw unavailable("Controlled Codex fixture cannot establish a hosted boundary");
    this.requireHostedIdentity();
  }
  private static async observeTransport<T extends { pid: number; transport: CodexSessionTransport }>(launched: T, tracker: DescendantTracker): Promise<T> {
    const diagnostic = (state: Awaited<ReturnType<DescendantTracker["reconcile"]>>) => new RuntimeError("ENGINE_UNAVAILABLE", "Observed worker descendants require reconciliation", 503, {
      reason: "DESCENDANT_RECONCILIATION_REQUIRED", leaderObserved: Boolean(state.leader), observed: state.observed, scans: state.scans,
      detachedCount: state.detached.length, detachedPids: state.detached.slice(0, 32).map(value => value.pid),
      ownedGroupCount: state.ownedGroup.length, identityChangedCount: state.identityChanged.length,
      censusFailed: Boolean(state.failure), ...(state.failure ? { censusFailure: censusFailureText(state.failure) } : {}), limitations: state.limitations, signalAuthority: "NONE"
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
      if (after.failure || after.detached.length || after.identityChanged.length || after.ownedGroup.length) { const failure = diagnostic(after); if (cleanupError) throw new AggregateError([cleanupError, failure], "Supplier retirement and descendant reconciliation failed"); throw failure; }
      if (cleanupError) throw cleanupError;
    })();
    return { ...launched, transport: { stdin: launched.transport.stdin, stdout: launched.transport.stdout, close } };
  }
  private observedTransport<T extends { pid: number; transport: CodexSessionTransport }>(launched: T, tracker: DescendantTracker): Promise<T> { return CodexSupervisor.observeTransport(launched, tracker); }
  private async launchFixture(): Promise<{ pid: number; transport: CodexSessionTransport; permissionProfile?: string; policyDigest?: string; expectedPermissions?: NativePermissions }> {
    if (this.fixtureLauncher) {
      const fixture = await this.fixtureLauncher();
      return fixture.descendantTracker ? this.observedTransport(fixture, fixture.descendantTracker) : fixture;
    }
    throw unavailable("Controlled launch is unavailable");
  }
  private async launchAdmittedCandidate(): Promise<AdmittedCandidate> {
    const queued = this.preadmitted;
    if (queued) { this.preadmitted = undefined; return queued; }
    if (!this.candidateLauncherFactory || !this.conformance) throw unavailable("Hosted production launch is unavailable");
    if (this.conformance.runtimeV2) await revalidateRuntimeInstanceAdmissionV2(this.conformance.runtimeV2.instanceInput, this.conformance.runtimeV2.instanceAdmission);
    const raw = await this.candidateLauncherFactory.create().launchCandidate();
    let candidate = raw;
    try {
      const observed = await this.observedTransport(raw, raw.descendantTracker);
      candidate = { ...observed, cleanup: observed.transport.close };
      const admitted = await CodexSupervisor.admitCandidate({ ...this.options, canonicalRoot: this.options.identity.canonicalRoot,
        conformance: this.conformance.conformance, configDigest: this.conformance.configDigest,
        expectedAccountDigest: this.conformance.accountDigest, consentVersion: this.conformance.consentVersion, ...(this.conformance.runtimeV2 ? { runtimeV2: this.conformance.runtimeV2 } : {}) }, candidate, this.controlledVerifyConformance);
      if (recordKey(admitted.continuity) !== recordKey(this.options.identity)) throw unavailable("Fresh candidate continuity changed");
      return admitted;
    } catch (error) { return failAfterCleanup(error, [() => candidate.cleanup()]); }
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
  async acquireWithRuntimeTools(workerId: string, input: string, tools: readonly RuntimeToolCallbackDeclaration[], inheritableTools: readonly RuntimeToolCallbackDeclaration[] = []): Promise<WorkerHandle> {
    if (this.runtimeToolMailboxes.has(workerId)) throw unavailable("Runtime tool worker already exists");
    const mailbox = new RuntimeToolMailbox(tools); this.runtimeToolMailboxes.set(workerId, mailbox);
    try {
      const handle = await this.acquireInternal(workerId, input, mailbox.tools, inheritableTools);
      void this.wait(workerId, handle.generation).then(() => mailbox.finish(), error => mailbox.finish(error));
      return handle;
    } catch (error) { this.runtimeToolMailboxes.delete(workerId); mailbox.finish(error as Error); throw error; }
  }
  async nextRuntimeToolCallback(workerId: string, generation: string): Promise<RuntimeToolCallbackMessage> {
    this.entry(workerId, generation); const mailbox = this.runtimeToolMailboxes.get(workerId); if (!mailbox) throw unavailable("Unknown runtime tool worker"); return mailbox.next();
  }
  async replyRuntimeToolCallback(workerId: string, generation: string, message: Extract<RuntimeToolCallbackMessage, {kind:"callback"}>, result: RuntimeToolCallbackResult): Promise<void> {
    this.entry(workerId, generation); const mailbox = this.runtimeToolMailboxes.get(workerId); if (!mailbox) throw unavailable("Unknown runtime tool worker"); mailbox.reply(message, result);
  }
  cancelAdmission(workerId:string):void {const pending=this.cancellations.get(workerId);if(!pending)return;pending.cancelled=true;if(pending.acquiring)void pending.authority?.revoke();}
  private async acquireInternal(workerId:string,input:string,dynamicTools?:readonly CodexDynamicTool[],inheritableTools?:readonly RuntimeToolCallbackDeclaration[]):Promise<WorkerHandle>{return this.acquireGuarded(workerId,input,dynamicTools,inheritableTools);}
  private async acquireGuarded(workerId: string, input: string, dynamicTools?: readonly CodexDynamicTool[], inheritableTools?: readonly RuntimeToolCallbackDeclaration[]): Promise<WorkerHandle> {
    if (!this.fixtureLauncher) this.requireHostedIdentity();
    id(workerId);
    if (this.closed || this.entries.has(workerId) || this.acquiring.has(workerId) || this.entries.size + this.acquiring.size >= (this.options.maxWorkers ?? 16)) throw unavailable("Codex worker is unavailable or already acquired");
    if (typeof input !== "string" || Buffer.byteLength(input) > 1048576) throw new RuntimeError("INVALID_REQUEST", "Invalid hosted turn envelope");
    let request: { prompt: string; attachments?: DelegatedAttachmentInput[]; resumeThreadId?: string; requestedRole?: string; roleEvidence?: { selectedRole?: string; enforcementLabel?: string; evidencePosture?: string }; interactionMode?: "chat" | "native-plan"; permissionMode?: "readOnly" | "ask" | "workspaceWrite" | "bypass"; projectId?: string; sessionId?: string; clientTurnId?: string; model?: string; reasoningEffort?: string };
    try { request = JSON.parse(input); } catch { throw new RuntimeError("INVALID_REQUEST", "Hosted worker requires the private broker JSON envelope"); }
    if (!request || typeof request !== "object" || Array.isArray(request) || Object.keys(request).some(key => !["prompt", "attachments", "resumeThreadId", "requestedRole", "roleEvidence", "interactionMode", "permissionMode", "projectId", "sessionId", "clientTurnId", "model", "reasoningEffort"].includes(key)) || typeof request.prompt !== "string" || !request.prompt.trim()) throw new RuntimeError("INVALID_REQUEST", "Invalid hosted turn envelope");
    const choice = this.assertCatalogChoice(request.model, request.reasoningEffort);
    const validAttachment = (attachment: DelegatedAttachmentInput): boolean => {
      if (!attachment || typeof attachment !== "object" || Array.isArray(attachment)) return false;
      if (attachment.type === "text") return !Object.keys(attachment).some(key => !["type", "text", "source"].includes(key)) && attachment.source === "untrusted-document" && typeof attachment.text === "string" && Buffer.byteLength(attachment.text) <= 262144;
      if (attachment.type === "localImage") return !Object.keys(attachment).some(key => !["type", "path", "mimeType", "source"].includes(key)) && attachment.source === "untrusted-attachment" && typeof attachment.path === "string" && ["image/png", "image/jpeg", "image/gif", "image/webp"].includes(attachment.mimeType);
      return false;
    };
    if (request.attachments !== undefined && (!Array.isArray(request.attachments) || request.attachments.length > 32 || !request.attachments.every(validAttachment))) throw new RuntimeError("INVALID_REQUEST", "Invalid hosted attachment envelope");
    const interactionMode = request.interactionMode ?? "chat";
    if (interactionMode !== "chat" && interactionMode !== "native-plan") throw new RuntimeError("INVALID_REQUEST", "Unknown interaction mode");
    if (request.permissionMode !== undefined && !["readOnly", "ask", "workspaceWrite", "bypass"].includes(request.permissionMode)) throw new RuntimeError("INVALID_REQUEST", "Unknown permission mode");
    let nativePlanBinding: NativePlanBinding | undefined;
    if (interactionMode === "native-plan") {
      for (const value of [request.projectId, request.sessionId, request.clientTurnId]) if (typeof value !== "string" || !/^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$/.test(value)) throw new RuntimeError("INVALID_REQUEST", "Native Plan requires bound project, session and client turn identities");
      nativePlanBinding = { projectId: request.projectId!, sessionId: request.sessionId!, clientTurnId: request.clientTurnId! };
    } else if (request.projectId !== undefined || request.sessionId !== undefined || request.clientTurnId !== undefined) throw new RuntimeError("INVALID_REQUEST", "Native Plan binding fields require native Plan interaction mode");
    if (request.resumeThreadId !== undefined) id(request.resumeThreadId);
    const selectedRole = request.requestedRole === undefined ? "untyped" : request.requestedRole;
    if (!["untyped", "agent0", "agent1", "agent2", "task"].includes(selectedRole)) throw new RuntimeError("INVALID_REQUEST", "Unknown explicitly requested role");
    const evidence = request.roleEvidence;
    if ((selectedRole !== "untyped" && !evidence) || (evidence !== undefined && (!evidence || typeof evidence !== "object" || Array.isArray(evidence) || evidence.selectedRole !== selectedRole || evidence.enforcementLabel !== "role not mechanically enforced" || evidence.evidencePosture !== "instruction-asserted"))) throw new RuntimeError("INVALID_REQUEST", "Role evidence must preserve the selected role and calibrated labels");
    const prompt = selectedRole === "untyped" ? request.prompt : `Runtime role instruction (explicit user selection): ${selectedRole}.\nrole not mechanically enforced; evidence posture: instruction-asserted.\n\n${request.prompt}`;
    let authority = this.options.supplierAuthority;
    const operationId = dynamicTools ? `manager:${workerId}` : `regular:${workerId}`;
    let authorityAcquired = false, publicationCommitted = false, releaseAttempted=false;
    const cancellation:{cancelled:boolean;acquiring:boolean;authority?:SupplierAuthorityController}={cancelled:false,acquiring:false};this.cancellations.set(workerId,cancellation);
    const cancelled=()=>{if(cancellation.cancelled||this.closed)throw unavailable("Admission cancelled");};
    const kind=dynamicTools?"manager":"regular";
    let localEntry:Entry|undefined;let begin:(()=>void)|undefined;let finishAdmissionLifecycle:((graceful:boolean)=>void)|undefined;
    this.acquiring.add(workerId);
    let finishAcquisition!: () => void;
    this.pendingAcquisitions.set(workerId, new Promise<void>(resolve => { finishAcquisition = resolve; }));
    let launched: { pid: number; transport: CodexSessionTransport; permissionProfile?: string; policyDigest?: string; expectedPermissions?: NativePermissions } | undefined;
    let session: CodexTurnSession | undefined;
    let supplierGeneration: string | undefined;
    try {
      await this.barrier?.(`${kind}/pre-acquire`);cancelled();
      if (this.fixtureLauncher) {
        if (authority) { cancellation.authority = authority; cancellation.acquiring = true; try { await authority.acquire(operationId); authorityAcquired = true; } finally { cancellation.acquiring = false; } }
        cancelled();
        launched = await this.launchFixture();
      } else {
        const candidate = await this.launchAdmittedCandidate();
        authority = candidate.authority; cancellation.authority = authority; session = candidate.session;
        supplierGeneration = candidate.candidate.supplierGeneration;
        launched = { pid: candidate.candidate.pid, transport: candidate.candidate.transport,
          permissionProfile: candidate.candidate.expectedPolicy.permissionProfile, policyDigest: candidate.candidate.expectedPolicy.policyDigest,
          expectedPermissions: candidate.candidate.expectedPolicy.expectedPermissions };
        cancellation.acquiring=true; try { await authority.acquire(operationId); authorityAcquired=true; } finally { cancellation.acquiring=false; }
        if (this.conformance?.runtimeV2) {
          await revalidateRuntimeInstanceAdmissionV2(this.conformance.runtimeV2.instanceInput, this.conformance.runtimeV2.instanceAdmission);
          const observedAccountDigest = await session.hostedAccountDigest(authority, supplierGeneration!);
          if (observedAccountDigest !== this.conformance.runtimeV2.instanceInput.account?.accountDigest) throw unavailable("Fresh candidate account identity changed after acquire");
          await this.revalidateCurrentHost();
        }
        cancelled();
      }
      if (this.fixtureLauncher) await assertContinuity(this.options.identity);
      else this.requireHostedIdentity();
      if (this.closed) throw unavailable("Supervisor is closing");
      if (this.closed) { await launched.transport.close(); throw unavailable("Supervisor closed during acquisition"); }
      const handle: WorkerHandle = { workerId, generation: randomUUID(), pid: launched.pid, state: "running" };
      if (!session) try {
        if (!this.fixtureLauncher && (!launched.permissionProfile || launched.policyDigest !== this.options.identity.policyDigest)) throw unavailable("Native action policy binding was lost during launch");
        if (request.permissionMode !== undefined && request.permissionMode !== (this.options.supportedPermissionMode ?? "workspaceWrite")) throw unavailable("Requested permission mode has no qualified native policy profile");
        session = new CodexTurnSession({ transport: launched.transport, requestTimeoutMs: this.options.requestTimeoutMs, turnTimeoutMs: this.options.turnTimeoutMs,
          commandNetworkPosture: this.options.commandNetworkPosture, permissionProfile: launched.permissionProfile, policyDigest: launched.policyDigest, dynamicTools, toolTimeoutMs: this.options.turnTimeoutMs });
      } catch (error) { await launched.transport.close(); throw error; }
      if (request.permissionMode !== undefined && request.permissionMode !== (this.options.supportedPermissionMode ?? "workspaceWrite")) throw unavailable("Requested permission mode has no qualified native policy profile");
      if (!session) throw unavailable("Codex candidate session is unavailable");
      const activeSession = session;
      if (!this.fixtureLauncher) activeSession.installDynamicTools(dynamicTools ?? []);
      if (inheritableTools !== undefined) await activeSession.installInheritableTools(inheritableTools);
      const nativePlanEvents: NativePlanTransportEvent[] = [], turnProgress: DelegatedTurnProgressEvent[] = [];
      // Completed plan items are authoritative; streamed deltas are never promoted.
      const eventDrain = (async () => { for await (const event of activeSession.events()) {
        if (event.type === "terminal") return;
        if (event.type === "started") {
          if (turnProgress.length >= 1024) throw unavailable("Turn progress inventory exceeded");
          turnProgress.push({ type: "started", providerThreadId: event.threadId, providerTurnId: event.turnId }); continue;
        }
        if (event.type === "text") {
          if (turnProgress.length >= 1024) throw unavailable("Turn progress inventory exceeded");
          turnProgress.push({ type: "text", providerThreadId: event.threadId, providerTurnId: event.turnId, text: event.text }); continue;
        }
        if (event.type === "plan") {
          if (!nativePlanBinding || nativePlanEvents.length >= 64) throw unavailable("Native Plan event inventory exceeded or lacked a trusted binding");
          nativePlanEvents.push({ ...nativePlanBinding, providerThreadId: event.threadId, providerTurnId: event.turnId, eventId: event.eventId, occurredAt: event.occurredAt, plan: structuredClone(event.plan) });
        }
      } })();
      // A projection failure is a worker failure, including when the provider has
      // already emitted a terminal. Never publish success after losing an event.
      void eventDrain.catch(() => activeSession.close().catch(() => {}));
      const admitted=new Promise<void>(resolve=>{begin=resolve;});
      let admissionLifecycleFinished=false;
      const admissionLifecycle=new Promise<boolean>(resolve=>{finishAdmissionLifecycle=value=>{if(!admissionLifecycleFinished){admissionLifecycleFinished=true;resolve(value);}};});
      const result = (async (): Promise<WorkerResult> => {
        await admitted;
        let primary: unknown, failed = false;
        try {
          if(!publicationCommitted)throw unavailable("Admission cancelled before publication");
          if(this.fixtureLauncher){await activeSession.initialize();if(launched.expectedPermissions)await activeSession.verifyNativePolicy(launched.expectedPermissions);}
          if (!this.fixtureLauncher && this.conformance?.runtimeV2) await revalidateRuntimeInstanceAdmissionV2(this.conformance.runtimeV2.instanceInput, this.conformance.runtimeV2.instanceAdmission);
          const account = await activeSession.accountRead();
          if (!account.hasAccount && !(this.fixtureLauncher && this.fixtureAllowUnauthenticatedModel && account.authRequired === false)) throw unavailable("Codex has no root-private authenticated account");
          if (!this.fixtureLauncher) this.requireHostedIdentity();
          const threadId = request.resumeThreadId
            ? await activeSession.resumeThread({ threadId: request.resumeThreadId, model: choice.model, continuityChecked: true })
            : await activeSession.startThread({ cwd: this.options.identity.canonicalRoot, model: choice.model, continuityChecked: true });
          const turnId = await activeSession.startTurn({ threadId, text: prompt, model: choice.model, reasoningEffort: choice.reasoningEffort, interactionMode, attachments: request.attachments });
          const terminal = await activeSession.waitTurn(turnId);
          await eventDrain;
          return { worker: { ...handle, state: "exited" }, exitCode: terminal.status === "completed" ? 0 : terminal.status === "failed" ? 1 : null,
            signal: terminal.status === "interrupted" ? "SIGTERM" : null, stdout: terminal.output, stderr: "", threadId };
        } catch (error) { primary = error; failed = true; throw error; }
        finally {
          handle.state = "exited";
          const graceful=await admissionLifecycle;
          // Every retirement step runs. A retirement diagnostic is attached to the
          // turn's own failure as its cause; it only becomes the error when the turn
          // itself completed.
          let retirementFailure: unknown, retirementFailed = false;
          const note = (error: unknown) => { retirementFailure = retirementFailed ? withRetirementFailure(retirementFailure, error) : error; retirementFailed = true; };
          // The supplier requires the admission lease for every private model request and native descendant.
          // Keep it through the terminal/event drain, then release before retiring the private authority.
          if (authority && graceful && !releaseAttempted) {
            releaseAttempted = true;
            try { await authority.release(operationId); } catch (error) { note(error); await authority.revoke().catch(note); }
          }
          if(authority&&!this.fixtureLauncher){try{if(graceful)await authority.retire();else await authority.revoke();}catch(error){note(error);}}
          try { await activeSession.close(); } catch (error) { note(error); }
          try { await launched.transport.close(); } catch (error) { note(error); }
          if (retirementFailed) { if (failed) { const combined = withRetirementFailure(primary, retirementFailure); if (combined !== primary) throw combined; } else throw retirementFailure; }
        }
      })();
      void result.catch(() => {});
      localEntry={handle,session:activeSession,result,cleanup:launched.transport.close,nativePlanBinding,nativePlanEvents,turnProgress};
      await this.barrier?.(`${kind}/post-acquire-pre-worker-publication`);cancelled();authority?.assertCommit(operationId);
      this.entries.set(workerId,localEntry);
      publicationCommitted = true;begin?.();
      await this.barrier?.(`${kind}/post-publication-pre-release`);
      // Publication is not the end of supplier work. Releasing here races thread/start and removes its live lease.
      cancelled();authority?.assertCommit(operationId);finishAdmissionLifecycle?.(true);return { ...handle };
    } catch (error) {
      // Removal is synchronous and precedes all cleanup awaits and caller return.
      if(localEntry&&this.entries.get(workerId)===localEntry)this.entries.delete(workerId);
      finishAdmissionLifecycle?.(false);begin?.();
      if (authorityAcquired && authority) {
        const activeAuthority = authority;
        if (publicationCommitted) {if(!releaseAttempted){releaseAttempted=true;await activeAuthority.release(operationId).catch(()=>activeAuthority.revoke());}}
        else await activeAuthority.abort(operationId).catch(()=>activeAuthority.revoke());
      }
      if(localEntry){
        let failure: unknown = error;
        await localEntry.session.close().catch(cleanup => { failure = withRetirementFailure(failure, cleanup); });
        await localEntry.result.catch(()=>{});
        await localEntry.cleanup().catch(cleanup => { failure = withRetirementFailure(failure, cleanup); });
        throw failure;
      }
      return failAfterCleanup(error, [() => session?.close(), () => launched?.transport.close()]);
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
  async drainNativePlanEvents(workerId: string, generation: string): Promise<readonly NativePlanTransportEvent[]> {
    const entry = this.entry(workerId, generation), events = entry.nativePlanEvents.splice(0);
    return structuredClone(events);
  }
  async drainTurnProgress(workerId: string, generation: string): Promise<readonly DelegatedTurnProgressEvent[]> {
    const entry = this.entry(workerId, generation), events = entry.turnProgress.splice(0);
    return structuredClone(events);
  }
  async pendingNativePlanClarifications(workerId: string, generation: string): Promise<readonly NativePlanClarificationPrompt[]> {
    const entry = this.entry(workerId, generation), binding = entry.nativePlanBinding;
    if (!binding || entry.handle.state !== "running") return [];
    return entry.session.pendingNativePlanClarifications().map(prompt => ({ ...structuredClone(binding), providerThreadId: prompt.threadId, providerTurnId: prompt.turnId,
      requestId: prompt.requestId, itemId: prompt.itemId, questions: structuredClone(prompt.questions), isBlocking: prompt.isBlocking, autoResolutionMs: prompt.autoResolutionMs }));
  }
  async replyNativePlanClarification(workerId: string, generation: string, requestId: string | number, answers: NativePlanClarificationAnswers): Promise<{ sent: true }> {
    const entry = this.entry(workerId, generation);
    if (!entry.nativePlanBinding || entry.handle.state !== "running") throw unavailable("Native Plan worker is no longer running");
    return entry.session.replyNativePlanClarification(requestId, answers);
  }
  async reconnect(workerId: string, generation: string): Promise<WorkerHandle> { return { ...this.entry(workerId, generation).handle }; }
  async wait(workerId: string, generation: string): Promise<WorkerResult> { return this.entry(workerId, generation).result; }
  async interrupt(workerId: string, generation: string): Promise<void> {
    const entry = this.entry(workerId, generation);
    if (entry.handle.state === "running") entry.session.requestInterrupt();
    await entry.result;
  }
  async retire(workerId: string, generation: string): Promise<void> { const entry = this.entry(workerId, generation); this.managers.get(workerId)?.finish(undefined, unavailable("Manager retired")); this.managers.delete(workerId); this.runtimeToolMailboxes.get(workerId)?.finish(unavailable("Runtime tool worker retired")); this.runtimeToolMailboxes.delete(workerId); await entry.session.close(); await entry.result.catch(() => {}); await entry.cleanup(); if (this.entries.get(workerId) === entry) this.entries.delete(workerId); }
  async close(): Promise<void> {
    this.closed = true;
    for (const id of this.cancellations.keys()) this.cancelAdmission(id);
    await Promise.all([...this.pendingAcquisitions.values()]);
    const failures: unknown[] = [];
    for (const close of [
      ...[...this.entries.values()].map(entry => () => this.retire(entry.handle.workerId, entry.handle.generation)),
      () => this.preadmitted?.authority.close(), () => this.candidateLauncherFactory?.close?.(), () => this.options.supplierAuthority?.close()
    ]) try { await close(); } catch (error) { failures.push(error); }
    if (failures.length === 1) throw failures[0];
    if (failures.length > 1) throw new AggregateError(failures, "Supervisor retirement failed; candidate ownership retained");
    this.preadmitted = undefined;
  }
}
export function createControlledCodexSupervisorForTests(options: Parameters<typeof CodexSupervisor.controlledForTests>[0]): CodexSupervisor { return CodexSupervisor.controlledForTests(options); }
