import { constants } from "node:fs";
import { open, lstat, readdir, realpath, unlink } from "node:fs/promises";
import { dirname, isAbsolute, join, relative, resolve, sep } from "node:path";
import { RuntimeError, validateHostedManagedAuth, type HostedManagedAuth, type EngineSelection, type ProviderCredentialPort, type RuntimeCompatibilityIdentity, type WorkerContinuity } from "@chirality/runtime-contracts";
import {
  assertContinuity, type RuntimeConformanceConfiguration, GovernedAgent1RunCoordinator, type Agent1ManagerRuntimePort, ApprovalStore, AuthRegistry, DelegatedRuntime, EngineRegistry, HostedConsentStore, privateDirectory,
  privateRead, ProcessSupervisor, ProjectRegistry, publishPrivate, recordKey, ResidencyCoordinator,
  RuntimeService, SessionStore, TurnCoordinator, WorkerRetirementCoordinator
} from "@chirality/runtime-core";
import { createPiTurnRuntime, createPiOmlxEngineAdapter, normalizeOmlxBaseUrl, OmlxClient } from "@chirality/engine-pi-omlx";
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
export interface StandaloneJob { role: "daemon" | "supervisor"; mode: StandaloneConfig["mode"]; socketPath: string; close(): Promise<void> }
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
export async function readStandaloneConfig(path: string): Promise<StandaloneConfig> {
  if (process.platform === "win32") throw unavailable("Standalone runtime requires Unix domain sockets");
  await privateFile(path);
  const config = await privateRead<StandaloneConfig>(path);
  if (config?.mode === "local-engine-only") return validateLocalConfig(config, path);
  keys(config, ["schema", "mode", "runtimeDirectory", "daemonSocket", "supervisorSocket", "supervisorCredential", "project", "worker", ...(config?.mode==="hosted-validation"?["supplierAuthority"]:[])]);
  if (!["controlled-worker", "hosted-validation"].includes(config.mode)) throw unavailable("Only controlled-worker or explicitly configured hosted-validation modes are supported");
  if (config.schema !== (config.mode === "hosted-validation" ? "chirality-standalone-hosted/v2" : "chirality-standalone/v1")) throw invalid("Unsupported standalone schema for mode");
  absolute(config.runtimeDirectory);
  if(config.mode==="hosted-validation")validateStandaloneSupplierAuthority(config.supplierAuthority,config.runtimeDirectory);
  if (!within(config.runtimeDirectory, path)) throw invalid("Configuration must reside in its private runtime directory");
  await privateTree(config.runtimeDirectory);
  keys(config.project, ["projectId", "identity", "compatibility", "codexHome", "retirementDirectory"]);
  keys(config.worker, config.mode === "controlled-worker" ? ["executablePath", "args", "maxRunMs"] : ["executablePath", "privateDirectory", "model", "commandNetworkPosture", "managedAuth", "providerNetworkConsent", "maxRunMs", "conformance"]);
  if (config.mode === "hosted-validation") validateHostedManagedAuth(config.worker.managedAuth);
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
  if (config.mode === "controlled-worker") {
    if (!Array.isArray(config.worker.args) || config.worker.args.length > 128 || config.worker.args.some(arg => typeof arg !== "string" || arg.length > 4096 || /[\x00-\x1f]/.test(arg))) throw invalid("Invalid trusted worker argument vector");
  } else {
    keys(config.worker.providerNetworkConsent, ["approvedBy", "approvalReference"]);
    if (config.worker.conformance !== undefined) {
      const c = config.worker.conformance;
      keys(c, ["recordPath", "acceptancePath", "ownerActPath", "ownerActSha256", "activationId", "gateIdentity"]);
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
  return structuredClone(config);
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
export async function startStandaloneJob(role: "daemon" | "supervisor", configPath: string): Promise<StandaloneJob> {
  if (role !== "daemon" && role !== "supervisor") throw invalid("Expected daemon or supervisor job");
  const config = await readStandaloneConfig(configPath);
  if(config.mode==="hosted-validation"&&config.supplierAuthority?.enabled)throw unavailable("Supplier authority native package remains unqualified");
  if (config.mode === "local-engine-only") {
    if (role !== "daemon") throw invalid("Local engine mode has no supervisor job");
    return startLocalDaemon(config);
  }
  const socketPath = child(config.runtimeDirectory, role === "daemon" ? config.daemonSocket : config.supervisorSocket);
  if (role === "supervisor") {
    const codexHome = child(config.runtimeDirectory, config.project.codexHome);
    await privateDirectory(codexHome);
    const workers = config.mode === "controlled-worker"
      ? new ProcessSupervisor({ command: config.worker.executablePath, args: config.worker.args, cwd: config.project.identity.canonicalRoot,
        env: { CODEX_HOME: codexHome }, maxRunMs: config.worker.maxRunMs ?? 30_000 })
      // Supplier authority is deliberately absent here: packaging remains default-off until a later qualified composition.
      : new CodexSupervisor({ executablePath: config.worker.executablePath, model: config.worker.model, identity: config.project.identity,
        codexHome, privateDirectory: child(config.runtimeDirectory, config.worker.privateDirectory), protectedPaths: [config.runtimeDirectory], commandNetworkPosture: config.worker.commandNetworkPosture ?? "off", managedAuth: config.worker.managedAuth,
        providerNetworkConsent: config.worker.providerNetworkConsent, turnTimeoutMs: config.worker.maxRunMs ?? 120_000,
        ...(config.worker.conformance === undefined ? {} : { conformance: { ...config.worker.conformance,
          recordPath: child(config.runtimeDirectory, config.worker.conformance.recordPath), acceptancePath: child(config.runtimeDirectory, config.worker.conformance.acceptancePath) } }) });
    const login = config.mode === "hosted-validation" ? new CodexLogin({ executablePath: config.worker.executablePath, canonicalRoot: config.project.identity.canonicalRoot,
      codexHome, privateDirectory: child(config.runtimeDirectory, config.worker.privateDirectory), providerNetworkConsent: config.worker.providerNetworkConsent }) : undefined;
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
  const projects = new ProjectRegistry(config.runtimeDirectory, {});
  const registered = await projects.requireAuthorized(config.project.projectId);
  if (registered.canonicalRoot !== config.project.identity.canonicalRoot) throw invalid("Configured root differs from explicit project registration");
  const sessions = new SessionStore(config.runtimeDirectory, projects), engines = new EngineRegistry();
  const offline = async (): Promise<never> => { throw unavailable("No hosted or local model engine is configured in controlled standalone mode"); };
  const residency = new ResidencyCoordinator({ async listStatus() { return []; }, load: offline, unload: offline }, config.runtimeDirectory);
  const service = new RuntimeService(projects, sessions, engines, residency, new TurnCoordinator(projects, sessions, engines, residency), new AuthRegistry(config.runtimeDirectory), {
    async get() { return undefined; }, async status() { return { configured: false }; }, set: offline, remove: offline
  });
  const retirement = new WorkerRetirementCoordinator({ directory: child(config.runtimeDirectory, config.project.retirementDirectory) });
  await retirement.reconcile();
  const consent = new HostedConsentStore({ canonicalRoot: config.project.identity.canonicalRoot, codexHome: child(config.runtimeDirectory, config.project.codexHome) });
  let delegated!: DelegatedRuntime;
  const approvals = new ApprovalStore({ canonicalRoot: config.project.identity.canonicalRoot, storageRoot: join(config.runtimeDirectory, "approvals"), consent, isLive: binding => delegated.isApprovalLive(binding) });
  delegated = new DelegatedRuntime({ daemonId: "standalone-starting", projects: new Map([[config.project.projectId, {
    identity: config.project.identity, compatibility: config.project.compatibility, supervisor,
    consent, retirement, approvals, approvalForwardingEnabled: config.mode === "hosted-validation",
    actual: config.mode === "hosted-validation" ? { adapterId: "codex-app-server", providerId: "openai", model: config.worker.model } : { adapterId: "controlled-worker", providerId: "not-applicable", model: "not-applicable" },
    commandNetworkPosture: config.mode === "controlled-worker" ? "off" : config.worker.commandNetworkPosture ?? "off",
    evidenceClass: config.mode === "controlled-worker" ? "controlled-worker" : "provider-observed"
  }]]) });
  const daemon = new RuntimeDaemon({ socketPath, runtimeDirectory: config.runtimeDirectory, service, delegated,
    ...(config.mode === "hosted-validation" ? { loginProjectId: config.project.projectId, login: {
      startLogin: () => supervisor.startLogin(), status: () => supervisor.loginStatus(), cancel: () => supervisor.cancelLogin()
    } } : {}) });
  await daemon.start();
  return { role, mode: config.mode, socketPath, close: () => daemon.stop() };
}

async function validateLocalConfig(config: LocalStandaloneConfig, path: string, checkCredential = true): Promise<LocalStandaloneConfig> {
  keys(config, ["schema", "mode", "runtimeDirectory", "daemonSocket", "project", "engine", "manager"]);
  if (config.schema !== "chirality-standalone/v1") throw invalid("Unknown local configuration schema");
  absolute(config.runtimeDirectory);
  if (!within(config.runtimeDirectory, path)) throw invalid("Configuration must reside in private runtime storage");
  await privateTree(config.runtimeDirectory);
  keys(config.project, ["projectId", "canonicalRoot"]);
  keys(config.engine, ["baseUrl", "model", "credentialFile", "approvalReference", "turnTimeoutMs", "maxOutputBytes"]);
  keys(config.engine.model, ["id", "contextWindow", "maxTokens"]);
  if (typeof config.project.projectId !== "string" || !/^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$/.test(config.project.projectId)) throw invalid("Invalid project ID");
  absolute(config.project.canonicalRoot);
  if (await realpath(config.project.canonicalRoot) !== config.project.canonicalRoot || !(await lstat(config.project.canonicalRoot)).isDirectory()) throw invalid("Project root must be a canonical directory");
  if (config.runtimeDirectory === config.project.canonicalRoot || within(config.runtimeDirectory, config.project.canonicalRoot) || within(config.project.canonicalRoot, config.runtimeDirectory)) throw invalid("Broker storage must be disjoint from project root");
  if (typeof config.engine.approvalReference !== "string" || !config.engine.approvalReference.trim() || config.engine.approvalReference.length > 512) throw invalid("An explicit private model selection approval reference is required");
  normalizeOmlxBaseUrl(config.engine.baseUrl);
  const model = config.engine.model;
  if (typeof model.id !== "string" || !model.id || model.id.trim() !== model.id || model.id.length > 256 || /[\x00-\x1f]/.test(model.id)) throw invalid("An exact model ID is required");
  for (const value of [model.contextWindow, model.maxTokens]) if (!Number.isSafeInteger(value) || value < 1 || value > 10_000_000) throw invalid("Invalid model limits");
  if (model.maxTokens > model.contextWindow) throw invalid("Output token limit exceeds context window");
  for (const [value, max] of [[config.engine.turnTimeoutMs, 300_000], [config.engine.maxOutputBytes, 8_388_608]]) if (value !== undefined && (!Number.isSafeInteger(value) || value < 1 || value > max!)) throw invalid("Invalid local turn limits");
  const socket = child(config.runtimeDirectory, config.daemonSocket), credential = child(config.runtimeDirectory, config.engine.credentialFile);
  if (Buffer.byteLength(socket) > 100 || socket === path || socket === credential || credential === path) throw invalid("Local resources require distinct bounded paths");
  for (const name of ["auth", "projects", "sessions", "approvals", "model-residency.json", "model-residency.jsonl"])
    for (const resource of [socket, credential]) if (resource === join(config.runtimeDirectory, name) || within(join(config.runtimeDirectory, name), resource)) throw invalid("Local resources overlap broker control storage");
  if (config.manager !== undefined) {
    keys(config.manager, ["kind", "supervisorSocket", "supervisorCredential", "bindingDigest", "model"]);
    const m = config.manager;
    if (m.kind !== "codex-supervisor" || typeof m.bindingDigest !== "string" || !/^[a-f0-9]{64}$/.test(m.bindingDigest) || typeof m.model !== "string" || !m.model.trim() || m.model.length > 128 || /[\x00-\x1f]/.test(m.model)) throw invalid("Invalid pinned hosted manager configuration");
    const resources = [child(config.runtimeDirectory, m.supervisorSocket), child(config.runtimeDirectory, m.supervisorCredential)];
    if (Buffer.byteLength(resources[0]!) > 100 || new Set([...resources, socket, credential, path]).size !== 5) throw invalid("Manager requires distinct private resources");
    for (const resource of resources) for (const name of ["auth", "projects", "sessions", "approvals", "pi-transcripts", "model-residency.json", "model-residency.jsonl"]) if (resource === join(config.runtimeDirectory, name) || within(join(config.runtimeDirectory, name), resource)) throw invalid("Manager resources overlap broker controls");
  }
  if (checkCredential) await localCredential(credential);
  return structuredClone(config);
}
async function localCredential(path: string): Promise<string> {
  await privateFile(path);
  const value = await privateRead<{ providerId: string; credential: string }>(path);
  keys(value, ["providerId", "credential"]);
  if (value.providerId !== "omlx" || typeof value.credential !== "string" || !value.credential.trim() || value.credential.length > 16_384 || /[\x00-\x1f]/.test(value.credential)) throw invalid("Invalid private oMLX credential record");
  return value.credential;
}
export async function startLocalDaemon(config: LocalStandaloneConfig, injectedCredentials?: ProviderCredentialPort, injectedManager?: { port: Agent1ManagerRuntimePort; selection: EngineSelection }): Promise<StandaloneJob> {
  config = await validateLocalConfig(config, join(config.runtimeDirectory, "memory-configuration"), injectedCredentials === undefined);
  const projects = new ProjectRegistry(config.runtimeDirectory, {});
  const registered = await projects.requireAuthorized(config.project.projectId);
  if (registered.canonicalRoot !== config.project.canonicalRoot) throw invalid("Configured local root differs from explicit project registration");
  const denied = async (): Promise<never> => { throw unavailable("Local pilot configuration is read-only and resident-only"); };
  const credentials = {
    async get(providerId: string) { return providerId === "omlx" ? injectedCredentials === undefined ? localCredential(child(config.runtimeDirectory, config.engine.credentialFile)) : injectedCredentials.get(providerId) : undefined; },
    async status(providerId: string) { return { configured: providerId === "omlx" && Boolean(await this.get(providerId)) }; }, set: denied, remove: denied
  };
  const client = new OmlxClient({ baseUrl: config.engine.baseUrl, credentials });
  const exactlyResident = async (id: string): Promise<boolean> => {
    const models = await client.listStatus();
    const active = models.filter(model => model.kind === "llm" && (model.loaded || model.loading));
    return id === config.engine.model.id && active.length === 1 && active[0]?.id === id && active[0].loaded && !active[0].loading;
  };
  if (!(await exactlyResident(config.engine.model.id))) throw unavailable("Configured exact model must be the sole resident local LLM");
  const residency = new ResidencyCoordinator({ listStatus: signal => client.listStatus(signal), load: denied, unload: denied }, config.runtimeDirectory);
  // Explicit private configuration selects an already resident model; never loads or falls back.
  await residency.activate(config.engine.model.id, config.engine.approvalReference);
  const sessions = new SessionStore(config.runtimeDirectory, projects), engines = new EngineRegistry();
  const transcriptRoot = join(config.runtimeDirectory, "pi-transcripts"); await privateDirectory(transcriptRoot);
  const pi = createPiTurnRuntime({ baseUrl: config.engine.baseUrl, model: config.engine.model, canonicalRoot: config.project.canonicalRoot,
    protectedPaths: [config.runtimeDirectory], turnTimeoutMs: config.engine.turnTimeoutMs, maxOutputBytes: config.engine.maxOutputBytes });
  engines.register(createPiOmlxEngineAdapter({ credentials, isExactlyResident: exactlyResident, transcriptRootFor: () => transcriptRoot, runtime: pi }));
  const turns = new TurnCoordinator(projects, sessions, engines, residency);
  if (injectedManager !== undefined && config.manager !== undefined) throw invalid("Manager binding must have one source");
  let manager = injectedManager;
  let managerApprovals: DelegatedRuntime | undefined;
  if (config.manager !== undefined) {
    const credential = await loadCredential({ ...config, supervisorSocket: config.manager.supervisorSocket, supervisorCredential: config.manager.supervisorCredential } as unknown as DelegatedStandaloneConfig, config.manager.bindingDigest);
    const channel = new SupervisorClient({ socketPath: child(config.runtimeDirectory, config.manager.supervisorSocket), credential });
    await channel.inventory();
    const description = await channel.describeApprovalScope();
    if (!description || description.identity?.canonicalRoot !== config.project.canonicalRoot || description.identity.cwd !== config.project.canonicalRoot || description.model !== config.manager.model || !/^root-runtime-[1-9][0-9]*$/.test(description.compatibility?.compatibilityIdentity ?? "") || !/^[a-f0-9]{64}$/.test(description.compatibility?.contractBasisSha256 ?? "")) throw invalid("Manager approval scope or exact compatibility differs from trusted composition");
    const identity = Object.freeze({ ...description.identity });
    const readonlyConsent = {
      async read(requestedIdentity: WorkerContinuity) {
        const current = await channel.describeApprovalScope();
        if (JSON.stringify(requestedIdentity) !== JSON.stringify(identity) && !["canonicalRoot", "cwd", "accountId", "accountEpoch", "policyDigest"].every(key => requestedIdentity[key as keyof WorkerContinuity] === identity[key as keyof WorkerContinuity])) throw invalid("Manager consent identity mismatch");
        if (!["canonicalRoot", "cwd", "accountId", "accountEpoch", "policyDigest"].every(key => current.identity[key as keyof WorkerContinuity] === identity[key as keyof WorkerContinuity]) || current.model !== description.model || JSON.stringify(current.compatibility) !== JSON.stringify(description.compatibility) || current.commandNetworkPosture !== description.commandNetworkPosture) throw invalid("Manager approval identity or compatibility drifted");
        return current.consent;
      },
      async grant() { throw invalid("Approval facade cannot modify standing hosted consent"); },
      async authorizeDestination() { throw invalid("Approval facade requires a durable attributed request decision"); }
    };
    let controller!: DelegatedRuntime;
    const store = new ApprovalStore({ canonicalRoot: identity.canonicalRoot, storageRoot: join(config.runtimeDirectory, "approvals"), consent: readonlyConsent, isLive: binding => controller.isApprovalLive(binding) });
    controller = new DelegatedRuntime({ daemonId: "manager-starting", approvalOnly: true, projects: new Map([[config.project.projectId, { identity, compatibility: description.compatibility, supervisor: channel, consent: readonlyConsent, approvals: store, approvalForwardingEnabled: true, commandNetworkPosture: description.commandNetworkPosture, actual: { adapterId: "codex-app-server", providerId: "openai", model: description.model }, evidenceClass: "provider-observed" }]]) });
    managerApprovals = controller;
    manager = { selection: { adapterId: "codex-app-server", providerId: "openai", model: config.manager.model }, port: new CodexAgent1ManagerPort({ channel, approvals: { async register(session, handle, scopeDigest) {
      if (session.projectId !== config.project.projectId || session.projectRoot !== identity.canonicalRoot || session.sessionId !== handle.workerId || session.role !== "agent1" || session.engineSelection.model !== description.model) throw invalid("Manager approval scope does not match the admitted manager session");
      await channel.describeApprovalScope(handle.workerId, handle.generation);
      return controller.registerExternalApprovalWorker(session.projectId, handle, scopeDigest);
    } }, loadInstructions: async session => {
      const roots = await projects.roots(session.projectId);
      if (!/^[A-Z][A-Z0-9_]{0,127}$/.test(session.persona)) throw invalid("Invalid manager instruction identity");
      const root = await realpath(roots.instructionRoot), path = join(root, "agents", `AGENT_${session.persona}.md`);
      if (await realpath(path) !== path) throw invalid("Manager instructions must not traverse aliases");
      const file = await open(path, constants.O_RDONLY | constants.O_NOFOLLOW);
      try {
        const before = await file.stat();
        if (!before.isFile() || before.size > 1_048_576) throw invalid("Manager instructions exceed bounded regular file scope");
        const contents = await file.readFile("utf8"), after = await file.stat(), current = await lstat(path);
        if (before.dev !== current.dev || before.ino !== current.ino || before.mtimeMs !== after.mtimeMs || before.size !== after.size) throw invalid("Manager instructions changed while loading");
        return contents;
      } finally { await file.close(); }
    } }) };
  }
  if (manager !== undefined && (manager.selection.providerId === "omlx" || manager.selection.adapterId === "pi")) throw invalid("Local Agent 1 is not authorized");
  const agent1Runs = manager === undefined ? undefined : new GovernedAgent1RunCoordinator({ projects, sessions, turns, residency, manager: manager.port,
    tools: pi.toolBindings, protectedPaths: [config.runtimeDirectory], resolveManagerSelection: async () => ({ ...manager!.selection }) });
  const service = new RuntimeService(projects, sessions, engines, residency, turns, new AuthRegistry(config.runtimeDirectory), credentials, undefined, agent1Runs);
  const socketPath = child(config.runtimeDirectory, config.daemonSocket);
  const daemon = new RuntimeDaemon({ socketPath, runtimeDirectory: config.runtimeDirectory, service, approvals: managerApprovals });
  await daemon.start();
  return { role: "daemon", mode: config.mode, socketPath, async close() { await daemon.stop(); await pi.close(); } };
}
