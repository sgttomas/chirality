import { lstat, realpath } from "node:fs/promises";
import { isAbsolute, join, relative, resolve, sep } from "node:path";
import {
  CHIRALITY_INSTRUCTION_ROOT_ENV,
  RuntimeError,
  type AgentEnginePort,
  type EngineSelection,
  type HostedBootstrapStatus,
  type NativePlanAdapterQualification,
  type NativePlanCapabilityResponse,
  type NativePlanClarificationsResponse,
  type NativePlanRevisionsResponse,
  type ReplyNativePlanClarificationRequest,
  type RuntimeCompatibilityIdentity,
  type RuntimeSessionRecord,
  type SupervisorNativePlanPort,
  type NativePlanTransportEvent,
  type NativePlanClarificationPrompt,
  type WorkerContinuity
} from "@chirality/runtime-contracts";
import {
  assertContinuity,
  AuthRegistry,
  EngineRegistry,
  createDelegatedEngineAdapter,
  DelegatedRuntime,
  type DelegatedNativePlanSink,
  type DelegatedNativePlanWorkerBinding,
  privateDirectory,
  ProjectRegistry,
  ResidencyCoordinator,
  RuntimeAttachmentResolver,
  RuntimeService,
  SessionStore,
  TrustedNativePlanRegistry,
  TurnCoordinator,
  configureRuntimeConformanceArtifactInventory,
  type RuntimeConformanceArtifactInventorySelection,
  type TrustedNativePlanAdapterRegistry
} from "@chirality/runtime-core";
import { RuntimeDaemon } from "./runtime-daemon.js";
import { HOSTED_BOOTSTRAP_CLIENT_ID } from "./hosted-paths.js";

const invalid = (message: string) => new RuntimeError("INVALID_REQUEST", message);
const unavailable = (message: string) => new RuntimeError("ENGINE_UNAVAILABLE", message, 503);

export type HostedBootstrapRuntimeBootInput =
  | { enabled?: false }
  | { enabled: true; runtimeDirectory: string; daemonSocket: string; instructionRoot: string; nativeAddonPath?: string; artifactInventory?: RuntimeConformanceArtifactInventorySelection };

export interface HostedBootstrapRuntimeHost {
  socketPath: string;
  runtimeDirectory: string;
  /** Host-process custody only. Never expose this path or its contents to a renderer. */
  bootstrapTokenFile: string;
  stop(): Promise<void>;
}

export interface TrustedHostedLoginCeremony {
  start(): Promise<{ loginId: string; authUrl: string }>;
  status(): Promise<{ state: "pending" | "completed" | "failed"; hasAccount?: boolean }>;
  resolveDefaultModel?(): Promise<Readonly<{ model: string; defaultReasoningEffort: string }>>;
  cancel(): Promise<void>;
  close(): Promise<void>;
}

export interface TrustedHostedPrivateAdmission {
  continuity: WorkerContinuity;
  authority: { supplierGeneration: string; identityGeneration: string; snapshotDigest: string };
  nativePlanQualification?: NativePlanAdapterQualification;
  retire(): Promise<void>;
}

export interface HostedBootstrapPrivateBindings {
  createCeremony(input: { projectId: string; manifestHash?: string; canonicalRoot: string; privateDirectory: string; codexHome: string; providerNetworkConsent: { approvedBy: string; approvalReference: string; approvedAt: string } }): Promise<TrustedHostedLoginCeremony>;
  establishAdmission?(input: { projectId: string; canonicalRoot: string; ceremony: TrustedHostedLoginCeremony; nativeAddonPath?: string }): Promise<TrustedHostedPrivateAdmission>;
  /** Host-owned config/worker publication; receives private values and must not project them publicly. */
  materializeAdmission?(input: { projectId: string; canonicalRoot: string; admission: TrustedHostedPrivateAdmission; runtime: { projects: ProjectRegistry; sessions: SessionStore; nativePlanSink: DelegatedNativePlanSink; attachmentStagingRoot: string } }): Promise<
    | { engine: AgentEnginePort; selection: EngineSelection; evidenceClass?: "controlled-worker" }
    | { delegated: DelegatedRuntime; selection: EngineSelection; compatibility: RuntimeCompatibilityIdentity; evidenceClass: "provider-observed" | "controlled-worker" }
  >;
  /** Supplier-owned project-local logout after local admission retirement. */
  signOut?(input: { projectId: string; canonicalRoot: string; privateDirectory: string; codexHome: string }): Promise<void>;
  /** Retires host-owned private resources after every project admission is retired. */
  close?(): Promise<void>;
}

interface ProjectBootstrap {
  projectId: string;
  canonicalRoot: string;
  manifestHash: string;
  consent?: { approvedBy: string; approvalReference: string; approvedAt: string };
  ceremonyState: HostedBootstrapStatus["ceremony"];
  ceremony?: TrustedHostedLoginCeremony;
  admissionState: HostedBootstrapStatus["admission"];
  admission?: TrustedHostedPrivateAdmission;
  engine?: AgentEnginePort;
  selection?: EngineSelection;
  establishing?: Promise<void>;
  generation: number;
}

class BootstrapNativePlanRegistry implements TrustedNativePlanAdapterRegistry, DelegatedNativePlanSink {
  private readonly registries = new Map<string, TrustedNativePlanRegistry>();
  private readonly activeQualifications = new Set<string>();
  constructor(private readonly sessions: SessionStore) {}
  ensure(projectId: string): TrustedNativePlanRegistry {
    let registry = this.registries.get(projectId);
    if (!registry) { registry = new TrustedNativePlanRegistry({ projectId, sessions: this.sessions, unavailableReason: "No admitted native Plan adapter qualification is available for this project" }); this.registries.set(projectId, registry); }
    return registry;
  }
  qualify(projectId: string, qualification: NativePlanAdapterQualification): void {
    // A qualified replacement reads durable revisions from the shared SessionStore.
    this.registries.set(projectId, new TrustedNativePlanRegistry({ projectId, sessions: this.sessions, qualification }));
    this.activeQualifications.add(projectId);
  }
  deactivate(projectId: string): void { this.activeQualifications.delete(projectId); }
  private unavailableRegistry(projectId: string): TrustedNativePlanRegistry {
    return new TrustedNativePlanRegistry({ projectId, sessions: this.sessions, unavailableReason: "No active admitted native Plan adapter qualification is available for this project" });
  }
  private live(projectId: string): TrustedNativePlanRegistry {
    return this.activeQualifications.has(projectId) ? this.ensure(projectId) : this.unavailableRegistry(projectId);
  }
  capability(session: RuntimeSessionRecord): Promise<NativePlanCapabilityResponse> { return this.live(session.projectId).capability(session); }
  revisions(projectId: string, sessionId: string): Promise<NativePlanRevisionsResponse> { return this.ensure(projectId).revisions(projectId, sessionId); }
  clarifications(projectId: string, sessionId: string): Promise<NativePlanClarificationsResponse> { return this.live(projectId).clarifications(projectId, sessionId); }
  replyClarification(projectId: string, sessionId: string, request: ReplyNativePlanClarificationRequest): Promise<{ sent: true }> { return this.live(projectId).replyClarification(projectId, sessionId, request); }
  open(binding: DelegatedNativePlanWorkerBinding, bridge: SupervisorNativePlanPort): Promise<void> { return this.live(binding.projectId).open(binding, bridge); }
  // An already-open binding may drain its final provider events during admission
  // retirement. The underlying registry still validates its exact generation.
  capture(binding: DelegatedNativePlanWorkerBinding, events: readonly NativePlanTransportEvent[], clarifications: readonly NativePlanClarificationPrompt[]): Promise<void> { return this.ensure(binding.projectId).capture(binding, events, clarifications); }
  // Cleanup must remain reachable after admission invalidation so a retiring turn can
  // settle its live clarification bridge. Historical revisions remain in SessionStore.
  close(binding: DelegatedNativePlanWorkerBinding): Promise<void> { return this.ensure(binding.projectId).close(binding); }
}

function exactAbsolute(value: string, label: string): void {
  if (typeof value !== "string" || !isAbsolute(value) || resolve(value) !== value || /[\x00-\x1f]/.test(value)) throw invalid(`${label} must be a normalized absolute path`);
}
function safeId(value: string): void { if (!/^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$/.test(value)) throw invalid("Invalid project ID"); }
function child(root: string, value: string): string {
  if (!value || isAbsolute(value)) throw invalid("Bootstrap socket must be a relative path");
  const result = resolve(root, value), rel = relative(root, result);
  if (!rel || rel === ".." || rel.startsWith(`..${sep}`) || isAbsolute(rel) || rel !== value) throw invalid("Bootstrap socket must be normalized and contained");
  return result;
}

export class HostedBootstrapController {
  private readonly states = new Map<string, ProjectBootstrap>();
  private closed = false;
  private admissionGuard: Promise<void> = Promise.resolve();
  constructor(private readonly projects: ProjectRegistry, private readonly sessions: SessionStore, private readonly nativePlans: BootstrapNativePlanRegistry, private readonly runtimeDirectory: string, private readonly bindings?: HostedBootstrapPrivateBindings, private readonly nativeAddonPath?: string, private readonly controlledNativePlanQualification?: NativePlanAdapterQualification) {}

  private async invalidateState(state: ProjectBootstrap, cancelCeremony = true): Promise<void> {
    let failure: unknown;
    const ceremony = state.ceremony; state.ceremony = undefined;
    if (cancelCeremony) try { await ceremony?.cancel(); } catch (error) { failure ??= error; }
    try { await ceremony?.close(); } catch (error) { failure ??= error; }
    await state.establishing?.catch(error => { failure ??= error; }); state.establishing = undefined;
    try { await this.retireAdmission(state); } catch (error) { failure ??= error; }
    if (failure !== undefined) throw failure;
  }

  private async state(projectId: string): Promise<{ state: ProjectBootstrap; canonicalRoot: string }> {
    safeId(projectId);
    let state = this.states.get(projectId);
    let project;
    try { project = await this.projects.requireAuthorized(projectId); }
    catch (error) {
      if (state) {
        state.generation++;
        await this.invalidateState(state).catch(() => {}); this.states.delete(projectId);
      }
      throw error;
    }
    if (this.closed) throw unavailable("Hosted bootstrap controller is closed");
    if (state && (state.canonicalRoot !== project.canonicalRoot || state.manifestHash !== project.manifestHash)) {
      state.generation++;
      await this.invalidateState(state);
      this.states.delete(projectId); state = undefined;
    }
    if (!state) { state = { projectId, canonicalRoot: project.canonicalRoot, manifestHash: project.manifestHash, ceremonyState: "consent-required", admissionState: "unavailable", generation: 0 }; this.states.set(projectId, state); }
    return { state, canonicalRoot: project.canonicalRoot };
  }

  private projection(projectId: string, state: ProjectBootstrap): HostedBootstrapStatus {
    return { schema: "chirality-hosted-bootstrap-status/v1", projectId, ceremony: state.ceremonyState, admission: state.admissionState,
      canStartLogin: ["ready-to-start", "failed", "cancelled"].includes(state.ceremonyState) };
  }

  selection(projectId: string): EngineSelection {
    const state = this.states.get(projectId);
    if (!state || state.admissionState !== "ready" || !state.selection) throw unavailable("Hosted admission is not ready for this project");
    return { ...state.selection };
  }

  engine(projectId: string, canonicalRoot: string): AgentEnginePort {
    const state = this.states.get(projectId);
    if (!state || state.canonicalRoot !== canonicalRoot || state.admissionState !== "ready" || !state.engine) throw unavailable("Hosted admission is not ready for this project");
    return state.engine;
  }

  async status(projectId: string): Promise<HostedBootstrapStatus> {
    const { state, canonicalRoot } = await this.state(projectId);
    if (state.ceremony && state.ceremonyState === "pending") {
      const ceremony = state.ceremony, generation = state.generation;
      const observed = await ceremony.status();
      if (this.closed || state.ceremony !== ceremony || state.generation !== generation) return this.projection(projectId, state);
      if (observed.state === "failed") { state.ceremonyState = "failed"; await this.retireAdmission(state); }
      else if (observed.state === "completed") {
        state.ceremonyState = "signed-in";
        if (observed.hasAccount && this.bindings?.establishAdmission && this.bindings.materializeAdmission && !state.establishing && !state.admission) {
          state.admissionState = "establishing";
          state.establishing = this.establish(projectId, canonicalRoot, state, generation, ceremony);
          try { await state.establishing; } catch { state.admissionState = "unavailable"; }
          finally { state.establishing = undefined; }
        }
      }
    }
    return this.projection(projectId, state);
  }

  async grantProviderNetworkConsent(projectId: string, provenance: { approvedBy: string; approvalReference: string; approvedAt: string }): Promise<HostedBootstrapStatus> {
    const { state } = await this.state(projectId);
    if (!provenance.approvedBy.trim() || !provenance.approvalReference.trim() || !Number.isFinite(Date.parse(provenance.approvedAt))) throw invalid("Invalid authenticated provider-network consent provenance");
    if (state.ceremonyState === "pending") throw invalid("Cannot replace provider-network consent during a login ceremony");
    state.generation++;
    await this.invalidateState(state, false);
    state.consent = { ...provenance };
    state.ceremonyState = "ready-to-start";
    return this.projection(projectId, state);
  }

  async startLogin(projectId: string): Promise<{ loginId: string; authUrl: string }> {
    const { state, canonicalRoot } = await this.state(projectId);
    if (!state.consent || !this.bindings) throw unavailable("Hosted login is unavailable until explicit consent and a trusted private ceremony adapter are configured");
    if (!["ready-to-start", "failed", "cancelled"].includes(state.ceremonyState)) throw invalid("Hosted login ceremony cannot start in its current state");
    const generation = ++state.generation;
    await this.invalidateState(state, false);
    const privateDirectory = join(this.runtimeDirectory, "hosted-bootstrap", projectId);
    const codexHome = join(privateDirectory, "codex-home");
    await privateDirectoryReady(privateDirectory); await privateDirectoryReady(codexHome);
    const ceremony = await this.bindings.createCeremony({ projectId, manifestHash: state.manifestHash, canonicalRoot, privateDirectory, codexHome, providerNetworkConsent: state.consent });
    if (this.closed || state.generation !== generation) { await ceremony.close(); throw unavailable("Hosted login start was superseded"); }
    state.ceremony = ceremony;
    try { const result = await ceremony.start(); if (this.closed || state.generation !== generation || state.ceremony !== ceremony) { await ceremony.close(); throw unavailable("Hosted login start was superseded"); } state.ceremonyState = "pending"; return result; }
    catch (error) { state.ceremonyState = "failed"; await ceremony.close(); state.ceremony = undefined; throw error; }
  }

  async cancelLogin(projectId: string): Promise<HostedBootstrapStatus> {
    const { state } = await this.state(projectId);
    state.generation++;
    try { await this.invalidateState(state); } finally { state.ceremonyState = state.consent ? "cancelled" : "consent-required"; }
    return this.projection(projectId, state);
  }

  async signOut(projectId: string): Promise<HostedBootstrapStatus> {
    const { state, canonicalRoot } = await this.state(projectId);
    const privateDirectory = join(this.runtimeDirectory, "hosted-bootstrap", projectId), codexHome = join(privateDirectory, "codex-home");
    state.generation++;
    state.consent = undefined;
    state.ceremonyState = "failed";
    state.admissionState = "unavailable";
    this.nativePlans.deactivate(projectId);
    let cleanupFailure: unknown;
    try { await state.ceremony?.cancel(); } catch (error) { cleanupFailure ??= error; }
    try { await state.ceremony?.close(); } catch (error) { cleanupFailure ??= error; } finally { state.ceremony = undefined; }
    await state.establishing?.catch(error => { cleanupFailure ??= error; }); state.establishing = undefined;
    const admission = state.admission;
    state.admission = undefined; state.engine = undefined; state.selection = undefined;
    let admissionRetired = false;
    const retire = async () => { if (!admissionRetired) { admissionRetired = true; await admission?.retire(); } };
    if (!this.bindings?.signOut) {
      await retire();
      throw unavailable("Trusted project-local hosted sign-out is unavailable");
    }
    try {
      // The private hook durably fences the identity store first, then retires its
      // candidates/controllers, and only then asks the supplier to log out.
      await this.bindings.signOut({ projectId, canonicalRoot, privateDirectory, codexHome });
      await retire();
      if (cleanupFailure !== undefined) throw cleanupFailure;
      state.ceremonyState = "consent-required";
      return this.projection(projectId, state);
    } catch {
      await retire().catch(() => {});
      state.ceremonyState = "failed";
      throw unavailable("Project-local hosted sign-out failed after admission retirement");
    }
  }

  private establish(projectId: string, canonicalRoot: string, state: ProjectBootstrap, generation: number, ceremony: TrustedHostedLoginCeremony): Promise<void> {
    const run = this.admissionGuard.then(() => this.establishExclusive(projectId, canonicalRoot, state, generation, ceremony));
    this.admissionGuard = run.catch(() => {});
    return run;
  }

  private async establishExclusive(projectId: string, canonicalRoot: string, state: ProjectBootstrap, generation: number, ceremony: TrustedHostedLoginCeremony): Promise<void> {
    const admission = await this.bindings!.establishAdmission!({ projectId, canonicalRoot, ceremony, ...(this.nativeAddonPath === undefined ? {} : { nativeAddonPath: this.nativeAddonPath }) });
    try {
      await assertContinuity(admission.continuity);
      if (admission.continuity.canonicalRoot !== canonicalRoot || admission.continuity.cwd !== canonicalRoot) throw invalid("Private admission continuity does not bind the registered project root");
      if (!admission.authority.supplierGeneration || !admission.authority.identityGeneration || !/^[a-f0-9]{64}$/.test(admission.authority.snapshotDigest)) throw invalid("Private admission authority evidence is invalid");
      if (this.closed || state.generation !== generation || state.ceremony !== ceremony) { await admission.retire(); return; }
      const attachmentStagingRoot = join(canonicalRoot, ".chirality", "attachments");
      // The nested read-only path must exist before a native policy is compiled;
      // an absent child cannot be treated as a proven write restriction on macOS.
      await privateDirectoryReady(attachmentStagingRoot);
      const materialized = await this.bindings!.materializeAdmission!({ projectId, canonicalRoot, admission, runtime: { projects: this.projects, sessions: this.sessions, nativePlanSink: this.nativePlans, attachmentStagingRoot } });
      if (this.closed || state.generation !== generation || state.ceremony !== ceremony) { await admission.retire(); return; }
      const selection = materialized.selection;
      const engine = "delegated" in materialized ? createDelegatedEngineAdapter({ projectId, delegated: materialized.delegated, selection, compatibility: materialized.compatibility }) : materialized.engine;
      if (!selection.model?.trim() || selection.adapterId !== "codex-app-server" || selection.providerId !== "openai"
        || selection.adapterId !== engine.descriptor.adapterId || selection.providerId !== engine.descriptor.providerId) throw invalid("Materialized hosted engine does not match the admitted Codex selection");
      if (admission.nativePlanQualification !== undefined) {
        if (materialized.evidenceClass !== "provider-observed" || admission.nativePlanQualification.adapterId !== selection.adapterId || admission.nativePlanQualification.providerId !== selection.providerId) throw invalid("Native Plan qualification does not match an admitted provider-observed adapter");
        this.nativePlans.qualify(projectId, admission.nativePlanQualification);
      } else if (this.controlledNativePlanQualification !== undefined) {
        if (materialized.evidenceClass !== "controlled-worker" || !("delegated" in materialized)) throw invalid("Controlled native Plan qualification requires the actual controlled delegated transport");
        this.nativePlans.qualify(projectId, this.controlledNativePlanQualification);
      } else this.nativePlans.ensure(projectId);
      state.admission = admission; state.engine = engine; state.selection = { ...selection }; state.admissionState = "ready";
    } catch (error) { if (state.admission === admission) await this.retireAdmission(state); else await admission.retire(); throw error; }
  }

  private async retireAdmission(state: ProjectBootstrap): Promise<void> {
    const admission = state.admission; state.admission = undefined; state.engine = undefined; state.selection = undefined; state.admissionState = "unavailable";
    this.nativePlans.deactivate(state.projectId);
    // Keep the sink live while the admitted runtime drains and closes its last
    // turn. Capability becomes unavailable after retirement, while completed
    // revisions remain durable in the shared SessionStore.
    await admission?.retire();
  }

  async close(): Promise<void> {
    this.closed = true;
    for (const state of this.states.values()) state.generation++;
    let failure: unknown;
    for (const state of this.states.values()) {
      try { await state.ceremony?.cancel(); } catch {}
      try { await state.ceremony?.close(); } catch (error) { failure ??= error; }
      await state.establishing?.catch(error => { failure ??= error; });
      try { await this.retireAdmission(state); } catch (error) { failure ??= error; }
    }
    this.states.clear();
    try { await this.bindings?.close?.(); } catch (error) { failure ??= error; }
    if (failure !== undefined) throw failure;
  }
}

function projectEngineDispatcher(controller: HostedBootstrapController): AgentEnginePort {
  const sessions = new Map<string, AgentEnginePort>();
  const resolveInput = (input: Parameters<AgentEnginePort["preflight"]>[0]) => {
    const projectId = (input as typeof input & { projectId?: string }).projectId;
    if (!projectId) throw invalid("Hosted engine invocation lacks exact project identity");
    return controller.engine(projectId, input.session.projectRoot);
  };
  return { descriptor: { adapterId: "codex-app-server", providerId: "openai", capabilities: { credentials: false, tools: true, attachments: true, interruption: true, durableResume: true, compaction: true, runtimeControlTools: true } }, subject: "codex-app-server",
    async preflight(input) { const engine = resolveInput(input); sessions.set(input.session.sessionId, engine); await engine.preflight(input); },
    async *startTurn(input) { const engine = resolveInput(input); sessions.set(input.session.sessionId, engine); try { yield* engine.startTurn(input); } finally { sessions.delete(input.session.sessionId); } },
    async interrupt(sessionId) { const engine = sessions.get(sessionId); if (engine) await engine.interrupt(sessionId); }
  };
}

async function privateDirectoryReady(path: string): Promise<void> { await privateDirectory(path); }

async function startBootstrap(input: Extract<HostedBootstrapRuntimeBootInput, { enabled: true }>, bindings?: HostedBootstrapPrivateBindings, controlledNativePlanQualification?: NativePlanAdapterQualification, controlled = false): Promise<HostedBootstrapRuntimeHost> {
  exactAbsolute(input.runtimeDirectory, "Runtime directory"); exactAbsolute(input.instructionRoot, "Runtime instruction root");
  if (input.nativeAddonPath !== undefined) exactAbsolute(input.nativeAddonPath, "Native admission add-on path");
  if (bindings !== undefined && !controlled && input.artifactInventory === undefined) throw unavailable("Trusted production bootstrap requires an explicit Runtime conformance artifact inventory");
  if (input.artifactInventory !== undefined) configureRuntimeConformanceArtifactInventory(input.artifactInventory);
  await privateDirectory(input.runtimeDirectory);
  const instruction = await lstat(input.instructionRoot);
  if (!instruction.isDirectory() || instruction.isSymbolicLink() || await realpath(input.instructionRoot) !== input.instructionRoot) throw invalid("Runtime instruction root must be a canonical directory");
  const socketPath = child(input.runtimeDirectory, input.daemonSocket);
  const environment = { [CHIRALITY_INSTRUCTION_ROOT_ENV]: input.instructionRoot };
  const projects = new ProjectRegistry(input.runtimeDirectory, environment), sessions = new SessionStore(input.runtimeDirectory, projects), engines = new EngineRegistry();
  const nativePlans = new BootstrapNativePlanRegistry(sessions);
  const offline = async (): Promise<never> => { throw unavailable("No admitted hosted worker is available during bootstrap"); };
  const residency = new ResidencyCoordinator({ async listStatus() { return []; }, load: offline, unload: offline }, input.runtimeDirectory);
  const bootstrap = new HostedBootstrapController(projects, sessions, nativePlans, input.runtimeDirectory, bindings, input.nativeAddonPath, controlledNativePlanQualification);
  engines.register(projectEngineDispatcher(bootstrap));
  const service = new RuntimeService(projects, sessions, engines, residency, new TurnCoordinator(projects, sessions, engines, residency, new RuntimeAttachmentResolver()), new AuthRegistry(input.runtimeDirectory), { async get() { return undefined; }, async status() { return { configured: false }; }, set: offline, remove: offline }, undefined, undefined, undefined,
    { async resolve(request) { return { role: request.agentType === 0 ? "agent0" : "agent1", engineSelection: bootstrap.selection(request.projectId) }; } }, nativePlans);
  const issued = await service.auth.ensureClient(HOSTED_BOOTSTRAP_CLIENT_ID, ["runtime:read", "projects:write", "credentials:write"]);
  const daemon = new RuntimeDaemon({ socketPath, runtimeDirectory: input.runtimeDirectory, service, hostedBootstrap: bootstrap });
  try { await daemon.start(); } catch (error) { await bootstrap.close(); throw error; }
  let stopping: Promise<void> | undefined;
  return { socketPath, runtimeDirectory: input.runtimeDirectory, bootstrapTokenFile: issued.tokenFile, stop: () => stopping ??= (async () => { let failure: unknown; try { await daemon.stop(); } catch (error) { failure = error; } try { await bootstrap.close(); } catch (error) { failure ??= error; } if (failure !== undefined) throw failure; })() };
}

/** Default-off unbound host entry. It creates no account identity or worker binding. */
export function startHostedBootstrapRuntimeHost(input?: HostedBootstrapRuntimeBootInput, trustedBindings?: HostedBootstrapPrivateBindings): Promise<HostedBootstrapRuntimeHost> {
  if (input?.enabled !== true) return Promise.reject(unavailable("Hosted bootstrap is disabled until the host supplies trusted runtime paths"));
  return startBootstrap(input, trustedBindings);
}

/** Controlled private adapter seam for end-to-end tests; production boot never receives these callbacks. */
export function startControlledHostedBootstrapRuntimeHostForTests(input: Extract<HostedBootstrapRuntimeBootInput, { enabled: true }>, bindings: HostedBootstrapPrivateBindings, controlledNativePlanQualification?: NativePlanAdapterQualification): Promise<HostedBootstrapRuntimeHost> {
  return startBootstrap(input, bindings, controlledNativePlanQualification, true);
}
