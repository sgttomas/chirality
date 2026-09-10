import { constants } from "node:fs";
import { open, lstat, readdir, realpath, unlink } from "node:fs/promises";
import { dirname, isAbsolute, join, relative, resolve, sep } from "node:path";
import { CHIRALITY_INSTRUCTION_ROOT_ENV, RuntimeError, validateHostedManagedAuth, type HostedManagedAuth, type EngineSelection, type NativePlanAdapterQualification, type ProviderCredentialPort, type RuntimeCompatibilityIdentity, type WorkerContinuity } from "@chirality/runtime-contracts";
import {
  assertContinuity, configureRuntimeConformanceArtifactInventory, type RuntimeConformanceArtifactInventorySelection, type RuntimeConformanceConfiguration, GovernedAgent1RunCoordinator, type Agent1ManagerRuntimePort, ApprovalStore, AuthRegistry, createDelegatedEngineAdapter, DelegatedRuntime, EngineRegistry, HostedConsentStore, privateDirectory,
  privateRead, ProcessSupervisor, ProjectRegistry, publishPrivate, recordKey, ResidencyCoordinator,
  RuntimeAttachmentResolver, RuntimeService, SessionStore, TrustedNativePlanRegistry, TurnCoordinator, WorkerRetirementCoordinator
} from "@chirality/runtime-core";
import { CodexAgent1ManagerPort } from "./codex-manager.js";
import { CodexLogin } from "./codex-login.js";
import { CodexSupervisor } from "./codex-supervisor.js";
import { RuntimeDaemon } from "./runtime-daemon.js";
import { startSupervisorServer, SupervisorClient, type SupervisorCredential } from "./supervisor-server.js";

export type StandaloneSupplierAuthorityConfig={enabled:false}|{schema:"chirality-standalone-supplier-authority/v1";enabled:true;authorityDirectory:string;supplierExecutable:string;supplierArgs:string[];nativeBindingSha256:string;exactSupplyDigest:string};
export function validateStandaloneSupplierAuthority(value:unknown,runtimeDirectory:string):StandaloneSupplierAuthorityConfig|undefined {
  if(value===undefined)return undefined;keys(value,["schema","enabled","authorityDirectory","supplierExecutable","supplierArgs","nativeBindingSha256","exactSupplyDigest"]);
  if(value.enabled===false){if(Object.keys(value).join(",")!=="enabled")throw invalid("Disabled authority permits no additional fields");return{enabled:false};}
  if(value.enabled!==true||value.schema!=="chirality-standalone-supplier-authority/v1"||Object.keys(value).length!==7)throw invalid("Invalid supplier authority configuration");
  child(runtimeDirectory,value.authorityDirectory as string);absolute(value.supplierExecutable as string);
  if(!Array.isArray(value.supplierArgs)||value.supplierArgs.length>128||value.supplierArgs.some(a=>typeof a!=="string"||Buffer.byteLength(a)>4096||/[\x00-\x1f]/.test(a))||typeof value.nativeBindingSha256!=="string"||!/^[a-f0-9]{64}$/.test(value.nativeBindingSha256)||typeof value.exactSupplyDigest!=="string"||!/^[a-f0-9]{64}$/.test(value.exactSupplyDigest))throw invalid("Invalid supplier authority binding");
  return structuredClone(value) as StandaloneSupplierAuthorityConfig;
}
interface StandaloneBase {
  runtimeDirectory: string;
  daemonSocket: string;
  supervisorSocket: string;
  supervisorCredential: string;
  project: {
    projectId: string;
    identity: WorkerContinuity;
    compatibility: RuntimeCompatibilityIdentity;
    codexHome: string;
    retirementDirectory: string;
  };
}
export type DelegatedStandaloneConfig = StandaloneBase & (
  { schema: "chirality-standalone/v1"; mode: "controlled-worker"; worker: { executablePath: string; args: string[]; maxRunMs?: number } } |
  { schema: "chirality-standalone-hosted/v2"; mode: "hosted-validation"; supplierAuthority?:StandaloneSupplierAuthorityConfig; worker: { conformance?: RuntimeConformanceConfiguration; executablePath: string; privateDirectory: string; model: string; commandNetworkPosture?: "off" | "ask-per-destination" | "on"; managedAuth: HostedManagedAuth; providerNetworkConsent: { approvedBy: string; approvalReference: string }; maxRunMs?: number } }
);
export interface LocalStandaloneConfig {
  schema: "chirality-standalone/v1";
  mode: "local-engine-only";
  runtimeDirectory: string;
  daemonSocket: string;
  project: { projectId: string; canonicalRoot: string };
  manager?: { kind: "codex-supervisor"; supervisorSocket: string; supervisorCredential: string; bindingDigest: string; model: string };
  engine: { baseUrl: string; model: { id: string; contextWindow: number; maxTokens: number }; credentialFile: string; approvalReference: string; turnTimeoutMs?: number; maxOutputBytes?: number };
}
export type StandaloneConfig = DelegatedStandaloneConfig | LocalStandaloneConfig;
export type HostedStandaloneConfig = Extract<DelegatedStandaloneConfig, { mode: "hosted-validation" }>;
export interface StandaloneJob { role: "daemon" | "supervisor"; mode: StandaloneConfig["mode"]; socketPath: string; close(): Promise<void> }
export interface StandaloneRuntimeBindings {
  /** Trusted in-process composition evidence; never read from public daemon input or the standalone config file. */
  nativePlanQualification?: NativePlanAdapterQualification;
  /** Exact packaged admission add-on path carried by the trusted host composition. It is never loaded while supplier authority is disabled. */
  nativeAddonPath?: string;
  /** Explicit trusted instruction root used to resolve v2 project manifests; never inherited from ambient process state. */
  instructionRoot?: string;
}
interface CredentialRecord {
  schema: "chirality-supervisor-credential/v1";
  socketPath: string;
  bindingDigest: string;
  credential: SupervisorCredential;
}
const invalid = (message: string) => new RuntimeError("INVALID_REQUEST", message);
const unavailable = (message: string) => new RuntimeError("ENGINE_UNAVAILABLE", message, 503);
function keys(value: unknown, allowed: string[]): asserts value is Record<string, unknown> {
  if (!value || typeof value !== "object" || Array.isArray(value) || Object.keys(value).some(key => !allowed.includes(key))) throw invalid("Unsupported standalone configuration fields");
}
function absolute(path: string): void {
  if (typeof path !== "string" || !isAbsolute(path) || resolve(path) !== path || /[\x00-\x1f]/.test(path)) throw invalid("Standalone paths must be canonical absolute paths");
}
function artifactInventory(value: RuntimeConformanceArtifactInventorySelection): void {
  if (!value || typeof value !== "object" || Array.isArray(value)) throw invalid("Conformance artifact inventory selection is required");
  if (value.kind === "source-tree") { keys(value,["kind","sourceRoot"]);absolute(value.sourceRoot);return; }
  if (value.kind === "packaged-resources") {
    keys(value, ["kind", "resourcesRoot", "manifestPath"]); absolute(value.resourcesRoot); absolute(value.manifestPath);
    if (value.manifestPath !== join(value.resourcesRoot, "runtime-artifact-inventory.json")) throw invalid("Packaged conformance inventory manifest must use the fixed resources path");
    return;
  }
  throw invalid("Unknown conformance artifact inventory selection");
}
function within(root: string, path: string): boolean {
  const value = relative(root, path);
  return value !== "" && value !== ".." && !value.startsWith(`..${sep}`) && !isAbsolute(value);
}
function child(root: string, path: string): string {
  if (typeof path !== "string" || !path || isAbsolute(path) || /[\x00-\x1f]/.test(path)) throw invalid("Storage paths must be relative to the runtime directory");
  const result = resolve(root, path);
  if (!within(root, result) || relative(root, result) !== path) throw invalid("Storage paths must be normalized and contained");
  return result;
}
async function privateFile(path: string): Promise<void> {
  absolute(path);
  const info = await lstat(path);
  if (!info.isFile() || info.isSymbolicLink() || info.uid !== process.getuid?.() || (info.mode & 0o777) !== 0o600 || await realpath(path) !== path) throw invalid("Configuration and credentials must be canonical owner-only 0600 regular files");
  await privateDirectory(dirname(path));
}
/** Validate existing storage before older registry components consume it. */
async function privateTree(path: string): Promise<void> {
  await privateDirectory(path);
  for (const name of await readdir(path)) {
    const entry = join(path, name), info = await lstat(entry);
    if (info.isSymbolicLink() || info.uid !== process.getuid?.()) throw invalid("Runtime storage contains an unsafe owner or alias");
    if (info.isDirectory()) await privateTree(entry);
    else if ((!info.isFile() && !info.isSocket()) || ![0o600, ...(info.isFile() ? [0o700] : [])].includes(info.mode & 0o777)) throw invalid("Runtime storage must contain only private files and Unix sockets");
  }
}
export async function readHostedStandaloneConfig(path: string): Promise<HostedStandaloneConfig> {
  if (process.platform === "win32") throw unavailable("Standalone runtime requires Unix domain sockets");
  await privateFile(path);
  const config = await privateRead<StandaloneConfig>(path);
  if (config?.mode !== "hosted-validation") throw unavailable("Hosted standalone entry requires hosted-validation mode");
  keys(config, ["schema", "mode", "runtimeDirectory", "daemonSocket", "supervisorSocket", "supervisorCredential", "project", "worker", "supplierAuthority"]);
  if (config.schema !== "chirality-standalone-hosted/v2") throw invalid("Unsupported standalone schema for hosted mode");
  absolute(config.runtimeDirectory);
  validateStandaloneSupplierAuthority(config.supplierAuthority,config.runtimeDirectory);
  if (!within(config.runtimeDirectory, path)) throw invalid("Configuration must reside in its private runtime directory");
  await privateTree(config.runtimeDirectory);
  keys(config.project, ["projectId", "identity", "compatibility", "codexHome", "retirementDirectory"]);
  keys(config.worker, ["executablePath", "privateDirectory", "model", "commandNetworkPosture", "managedAuth", "providerNetworkConsent", "maxRunMs", "conformance"]);
  validateHostedManagedAuth(config.worker.managedAuth);
  keys(config.project.identity, ["canonicalRoot", "accountId", "accountEpoch", "policyDigest", "cwd"]);
  keys(config.project.compatibility, ["compatibilityIdentity", "contractBasisSha256"]);
  if (typeof config.project.projectId !== "string" || !/^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$/.test(config.project.projectId)) throw invalid("A bounded project ID is required");
  await assertContinuity(config.project.identity);
  if (!/^root-runtime-[1-9][0-9]*$/.test(config.project.compatibility.compatibilityIdentity) || !/^[a-f0-9]{64}$/.test(config.project.compatibility.contractBasisSha256)) throw invalid("A precise compatibility basis is required");
  const paths = [config.daemonSocket, config.supervisorSocket, config.supervisorCredential, config.project.codexHome, config.project.retirementDirectory].map(path => child(config.runtimeDirectory, path));
  if (new Set(paths).size !== paths.length || paths.includes(path)) throw invalid("Standalone resources require distinct storage paths");
  for (const socket of paths.slice(0, 2)) if (Buffer.byteLength(socket!) > 100) throw invalid("Unix socket path is too long");
  absolute(config.worker.executablePath);
  const executable = await lstat(config.worker.executablePath);
  if (!executable.isFile() || executable.isSymbolicLink() || await realpath(config.worker.executablePath) !== config.worker.executablePath || (executable.mode & 0o111) === 0) throw invalid("Controlled worker requires a canonical executable regular file");
  {
    keys(config.worker.providerNetworkConsent, ["approvedBy", "approvalReference"]);
    if (config.worker.conformance !== undefined) {
      const c = config.worker.conformance;
      keys(c, ["recordPath", "acceptancePath", "ownerActPath", "ownerActSha256", "activationId", "gateIdentity", "artifactInventory"]);
      artifactInventory(c.artifactInventory);
      const record = child(config.runtimeDirectory, c.recordPath), acceptance = child(config.runtimeDirectory, c.acceptancePath);
      if (record === acceptance || [record, acceptance].includes(path)) throw invalid("Conformance resources must be distinct");
      absolute(c.ownerActPath);
      if (!/^[a-f0-9]{64}$/.test(c.ownerActSha256) || typeof c.activationId !== "string" || !c.activationId.trim() || typeof c.gateIdentity !== "string" || !c.gateIdentity.trim()) throw invalid("Conformance requires exact external acceptance binding");
    }
    if (config.worker.commandNetworkPosture !== undefined && !["off", "ask-per-destination", "on"].includes(config.worker.commandNetworkPosture)) throw invalid("Unsupported executable command network posture");
    if (typeof config.worker.model !== "string" || !config.worker.model.trim() || config.worker.model.length > 128 || /[\x00-\x1f]/.test(config.worker.model)
      || typeof config.worker.providerNetworkConsent.approvedBy !== "string" || !config.worker.providerNetworkConsent.approvedBy.trim()
      || typeof config.worker.providerNetworkConsent.approvalReference !== "string" || !config.worker.providerNetworkConsent.approvalReference.trim()) throw invalid("Hosted validation requires managed authentication, model and attributed provider consent");
    const workerPrivate = child(config.runtimeDirectory, config.worker.privateDirectory);
    const overlaps = (a: string, b: string) => a === b || within(a, b) || within(b, a);
    if (overlaps(config.runtimeDirectory, config.project.identity.canonicalRoot)) throw invalid("Hosted project root must be disjoint from broker runtime storage");
    if (!within(workerPrivate, child(config.runtimeDirectory, config.project.codexHome)) || !within(workerPrivate, config.worker.executablePath)) throw invalid("Hosted home and binary must be inside the dedicated worker-private subtree");
    const controls = [path, child(config.runtimeDirectory, config.daemonSocket), child(config.runtimeDirectory, config.supervisorSocket), child(config.runtimeDirectory, config.supervisorCredential), child(config.runtimeDirectory, config.project.retirementDirectory),
      ...["auth", "projects", "sessions", "approvals", "model-residency.json", "model-residency.jsonl"].map(name => join(config.runtimeDirectory, name))];
    if (config.worker.conformance !== undefined) controls.push(child(config.runtimeDirectory, config.worker.conformance.recordPath), child(config.runtimeDirectory, config.worker.conformance.acceptancePath));
    if (controls.some(control => overlaps(workerPrivate, control))) throw invalid("Hosted worker-private storage must be disjoint from broker credentials, journals, registries and configuration");
  }
  if (config.worker.maxRunMs !== undefined && (!Number.isSafeInteger(config.worker.maxRunMs) || config.worker.maxRunMs < 1 || config.worker.maxRunMs > 300_000)) throw invalid("Invalid worker deadline");
  return structuredClone(config) as HostedStandaloneConfig;
}
async function loadCredential(config: DelegatedStandaloneConfig, expectedDigest = recordKey(config)): Promise<SupervisorCredential> {
  const path = child(config.runtimeDirectory, config.supervisorCredential);
  await privateFile(path);
  const record = await privateRead<CredentialRecord>(path);
  const socketPath = child(config.runtimeDirectory, config.supervisorSocket);
  if (!record || record.schema !== "chirality-supervisor-credential/v1" || record.socketPath !== socketPath || record.bindingDigest !== expectedDigest) throw unavailable("Supervisor credential does not bind this standalone configuration");
  const credential = record.credential;
  if (!credential || typeof credential.owner !== "string" || !new RegExp(`^${process.getuid?.()}:[1-9][0-9]*$`).test(credential.owner) || typeof credential.epoch !== "string" || !/^[a-f0-9-]{36}$/.test(credential.epoch) || typeof credential.token !== "string" || !/^[a-f0-9]{64}$/.test(credential.token)) throw unavailable("Invalid supervisor generation credential");
  try { process.kill(Number(credential.owner.split(":")[1]), 0); } catch { throw unavailable("Supervisor credential belongs to a dead process"); }
  const socket = await lstat(socketPath);
  if (!socket.isSocket() || socket.uid !== process.getuid?.() || (socket.mode & 0o777) !== 0o600) throw unavailable("Supervisor Unix endpoint is not owner-private");
  return credential;
}
interface StandaloneTestBindings { hostedSupervisor?: CodexSupervisor }
async function startHostedStandaloneJobWithBindings(role: "daemon" | "supervisor", configPath: string, runtimeBindings: StandaloneRuntimeBindings = {}, testBindings: StandaloneTestBindings = {}): Promise<StandaloneJob> {
  if (role !== "daemon" && role !== "supervisor") throw invalid("Expected daemon or supervisor job");
  const config = await readHostedStandaloneConfig(configPath);
  if (config.worker.conformance !== undefined) configureRuntimeConformanceArtifactInventory(config.worker.conformance.artifactInventory);
  if (runtimeBindings.nativeAddonPath !== undefined) absolute(runtimeBindings.nativeAddonPath);
  if (runtimeBindings.instructionRoot !== undefined) absolute(runtimeBindings.instructionRoot);
  if(config.supplierAuthority?.enabled)throw unavailable("Supplier authority native package remains unqualified");
  const socketPath = child(config.runtimeDirectory, role === "daemon" ? config.daemonSocket : config.supervisorSocket);
  if (role === "supervisor") {
    const codexHome = child(config.runtimeDirectory, config.project.codexHome);
    await privateDirectory(codexHome);
    const attachmentStagingRoot = join(config.project.identity.canonicalRoot, ".chirality", "attachments");
    // Materialize the read-only subtree before native policy compilation. Exact
    // provider policy source supports a narrower read entry beneath root write,
    // while absent nested paths do not provide the same platform guarantee.
    await privateDirectory(attachmentStagingRoot);
    // Supplier authority is deliberately absent here: packaging remains default-off until a later qualified composition.
    const workers = testBindings.hostedSupervisor ?? new CodexSupervisor({ executablePath: config.worker.executablePath, model: config.worker.model, identity: config.project.identity,
        codexHome, privateDirectory: child(config.runtimeDirectory, config.worker.privateDirectory), protectedPaths: [config.runtimeDirectory], readOnlyProjectPaths: [attachmentStagingRoot], commandNetworkPosture: config.worker.commandNetworkPosture ?? "off", managedAuth: config.worker.managedAuth,
        providerNetworkConsent: config.worker.providerNetworkConsent, turnTimeoutMs: config.worker.maxRunMs ?? 120_000,
        ...(config.worker.conformance === undefined ? {} : { conformance: { ...config.worker.conformance,
          recordPath: child(config.runtimeDirectory, config.worker.conformance.recordPath), acceptancePath: child(config.runtimeDirectory, config.worker.conformance.acceptancePath) } }) });
    const login = new CodexLogin({ executablePath: config.worker.executablePath, canonicalRoot: config.project.identity.canonicalRoot,
      codexHome, privateDirectory: child(config.runtimeDirectory, config.worker.privateDirectory), providerNetworkConsent: config.worker.providerNetworkConsent });
    const server = await startSupervisorServer({ socketPath, supervisor: workers, login, approvalCompatibility: config.project.compatibility, recoverStale: true });
    const credentialPath = child(config.runtimeDirectory, config.supervisorCredential);
    const record: CredentialRecord = { schema: "chirality-supervisor-credential/v1", socketPath, bindingDigest: recordKey(config), credential: server.credential };
    try { await publishPrivate(credentialPath, record, false); }
    catch (error) { await server.close(); await workers.close(); throw error; }
    let closing: Promise<void> | undefined;
    return { role, mode: config.mode, socketPath, close() {
      closing ??= (async () => {
        const stopped = await Promise.allSettled([server.close(), workers.close(), login?.close()]);
        const current = await privateRead<CredentialRecord>(credentialPath);
        if (current?.credential.epoch === record.credential.epoch) await unlink(credentialPath);
        for (const result of stopped) if (result.status === "rejected") throw result.reason;
      })();
      return closing;
    } };
  }
  const credential = await loadCredential(config);
  const supervisor = new SupervisorClient({ socketPath: child(config.runtimeDirectory, config.supervisorSocket), credential });
  await supervisor.inventory(); // Prove the loaded credential belongs to the live endpoint.
  const projects = new ProjectRegistry(config.runtimeDirectory, runtimeBindings.instructionRoot === undefined ? {} : { [CHIRALITY_INSTRUCTION_ROOT_ENV]: runtimeBindings.instructionRoot });
  const registered = await projects.requireAuthorized(config.project.projectId);
  if (registered.canonicalRoot !== config.project.identity.canonicalRoot) throw invalid("Configured root differs from explicit project registration");
  const sessions = new SessionStore(config.runtimeDirectory, projects), engines = new EngineRegistry();
  const offline = async (): Promise<never> => { throw unavailable("No hosted or local model engine is configured in controlled standalone mode"); };
  const residency = new ResidencyCoordinator({ async listStatus() { return []; }, load: offline, unload: offline }, config.runtimeDirectory);
  const retirement = new WorkerRetirementCoordinator({ directory: child(config.runtimeDirectory, config.project.retirementDirectory) });
  await retirement.reconcile();
  const consent = new HostedConsentStore({ canonicalRoot: config.project.identity.canonicalRoot, codexHome: child(config.runtimeDirectory, config.project.codexHome) });
  const nativePlan = new TrustedNativePlanRegistry({ projectId: config.project.projectId, sessions, qualification: runtimeBindings.nativePlanQualification, unavailableReason: "No accepted native Plan adapter qualification is supplied to this standalone composition" });
  let delegated!: DelegatedRuntime;
  const approvals = new ApprovalStore({ canonicalRoot: config.project.identity.canonicalRoot, storageRoot: join(config.runtimeDirectory, "approvals"), consent, isLive: binding => delegated.isApprovalLive(binding) });
  delegated = new DelegatedRuntime({ daemonId: "standalone-starting", projects: new Map([[config.project.projectId, {
    identity: config.project.identity, compatibility: config.project.compatibility, supervisor,
    consent, retirement, approvals, approvalForwardingEnabled: config.mode === "hosted-validation", nativePlanSink: nativePlan,
    actual: { adapterId: "codex-app-server", providerId: "openai", model: config.worker.model },
    commandNetworkPosture: config.worker.commandNetworkPosture ?? "off",
    evidenceClass: testBindings.hostedSupervisor !== undefined ? "controlled-worker" : "provider-observed"
  }]]) });
  engines.register(createDelegatedEngineAdapter({ projectId: config.project.projectId, delegated, compatibility: config.project.compatibility, selection: { adapterId: "codex-app-server", providerId: "openai", model: config.worker.model } }));
  const service = new RuntimeService(projects, sessions, engines, residency, new TurnCoordinator(projects, sessions, engines, residency, new RuntimeAttachmentResolver()), new AuthRegistry(config.runtimeDirectory), {
    async get() { return undefined; }, async status() { return { configured: false }; }, set: offline, remove: offline
  }, undefined, undefined, undefined, { async resolve({ agentType }) { return { role: agentType === 0 ? "agent0" : "agent1", engineSelection: { adapterId: "codex-app-server", providerId: "openai", model: config.worker.model } }; } }, nativePlan);
  const daemon = new RuntimeDaemon({ socketPath, runtimeDirectory: config.runtimeDirectory, service, delegated,
    loginProjectId: config.project.projectId, login: {
      startLogin: () => supervisor.startLogin(), status: () => supervisor.loginStatus(), cancel: () => supervisor.cancelLogin()
    } });
  await daemon.start();
  return { role, mode: config.mode, socketPath, close: () => daemon.stop() };
}

export async function startHostedStandaloneJob(role: "daemon" | "supervisor", configPath: string, runtimeBindings: StandaloneRuntimeBindings = {}): Promise<StandaloneJob> {
  return startHostedStandaloneJobWithBindings(role, configPath, runtimeBindings);
}

/** Test-only composition seam: substitutes a controlled hosted supervisor without weakening serialized production configuration. */
export async function startHostedStandaloneJobWithControlledSupervisorForTests(role: "daemon" | "supervisor", configPath: string, supervisor: CodexSupervisor, runtimeBindings: StandaloneRuntimeBindings = {}): Promise<StandaloneJob> {
  return startHostedStandaloneJobWithBindings(role, configPath, runtimeBindings, { hostedSupervisor: supervisor });
}
