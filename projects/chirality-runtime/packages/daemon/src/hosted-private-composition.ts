import { constants } from "node:fs";
import { lstat, open, realpath, unlink } from "node:fs/promises";
import { isAbsolute, join, relative, resolve, sep } from "node:path";
import {
  CHIRALITY_ROLE_NAMES,
  RuntimeError,
  validateHostedManagedAuth,
  type HostedManagedAuth,
  type NativePlanAdapterQualification,
  type RuntimeCompatibilityIdentity
} from "@chirality/runtime-contracts";
import {
  ApprovalStore,
  DelegatedRuntime,
  HostedConsentStore,
  WorkerRetirementCoordinator,
  codexNativeRoleConfigOverrides,
  loadTrustedNativeRoleConfiguration,
  privateDirectory,
  recordKey,
  revalidateExactSupply,
  syncDirectory,
  verifyExactSupply,
  type RuntimeAdmissionLease,
  type RuntimeConformanceConfiguration
} from "@chirality/runtime-core";
import { loadNativeAdmissionBinding } from "@chirality/native-admission";
import { createCodexCandidateLauncherFactory, type CodexCandidateLauncherFactory } from "./codex-admitted-launcher.js";
import { bindTrustedRuntimeReadRoot, prepareCodexNativePolicy, type TrustedRuntimeReadRootBinding } from "./codex-containment.js";
import { CodexLogin, validateCodexLoginStartup, type CodexLoginStartupAdmission } from "./codex-login.js";
import { CodexTurnSession } from "./codex-session.js";
import { CodexSupervisor, type HostedCodexSupervisorAdmission, type HostedCodexSupervisorOptions } from "./codex-supervisor.js";
import { HostedIdentityBindingStore } from "./hosted-identity-binding.js";
import type { HostedBootstrapPrivateBindings, TrustedHostedLoginCeremony, TrustedHostedPrivateAdmission } from "./hosted-bootstrap.js";

const HEX = /^[a-f0-9]{64}$/;
const ID = /^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$/;
const VALID_VENDOR_SIGNATURE = "accepted-valid-vendor-signature";

function unavailable(reason: string, cause?: unknown): RuntimeError {
  const error = new RuntimeError("ENGINE_UNAVAILABLE", "Hosted private Codex composition is unavailable", 503, { reason });
  if (cause !== undefined) error.cause = cause;
  return error;
}
function canonical(value: unknown): value is string {
  return typeof value === "string" && isAbsolute(value) && resolve(value) === value && !/[\x00-\x1f]/.test(value);
}
function contained(parent: string, child: string): boolean {
  const value = relative(parent, child);
  return value.length > 0 && value !== ".." && !value.startsWith(`..${sep}`) && !isAbsolute(value);
}
function exactKeys(value: unknown, keys: readonly string[]): boolean {
  return Boolean(value) && typeof value === "object" && !Array.isArray(value)
    && Object.keys(value as Record<string, unknown>).sort().join("\0") === [...keys].sort().join("\0");
}
function ownerId(): number {
  const uid = process.getuid?.();
  if (uid === undefined) throw unavailable("OWNER_ID_UNAVAILABLE");
  return uid;
}

export interface HostedPrivateCompositionOptions {
  runtimeDirectory: string;
  supplierExecutablePath: string;
  nativeAddonPath: string;
  instructionRoot: string;
  model: string;
  managedAuth: HostedManagedAuth;
  compatibility: RuntimeCompatibilityIdentity;
  conformance: RuntimeConformanceConfiguration;
  loginPurposeRelease: RuntimeConformanceConfiguration;
  configDigest: string;
  consentVersion: string;
  commandNetworkPosture: "off" | "ask-per-destination" | "on";
  commandNetworkConsent: { approvedBy: string; approvedAt: string; explicitUserAct: true };
  protectedPaths: readonly string[];
  immutableReadRoots: readonly string[];
  nativePlanQualification?: NativePlanAdapterQualification;
  requestTimeoutMs?: number;
  turnTimeoutMs?: number;
  maxWorkers?: number;
}

interface PolicyResult {
  policyDigest: string;
  cleanup(): Promise<void>;
}

export interface ControlledHostedPrivateCompositionAdapters {
  acquireLease(runtimeDirectory: string, nativeAddonPath: string): Promise<RuntimeAdmissionLease>;
  stageSupplier(sourcePath: string, privateDirectory: string): Promise<string>;
  prepareNativeRoles(instructionRoot: string, privateDirectory: string): Promise<{ digest: string; configOverrides: readonly string[] }>;
  bindRuntimeReadRoot(path: string, inventory: RuntimeConformanceConfiguration["artifactInventory"]): Promise<TrustedRuntimeReadRootBinding>;
  validateLoginStartup(options: Omit<ConstructorParameters<typeof CodexLogin>[0], "timeoutMs" | "startupAdmission">): Promise<CodexLoginStartupAdmission>;
  createLogin(options: ConstructorParameters<typeof CodexLogin>[0]): TrustedHostedLoginCeremony;
  preparePolicy(options: Parameters<typeof prepareCodexNativePolicy>[0]): Promise<PolicyResult>;
  createLauncherFactory(options: Parameters<typeof createCodexCandidateLauncherFactory>[0]): CodexCandidateLauncherFactory;
  admitHosted(options: HostedCodexSupervisorOptions): Promise<HostedCodexSupervisorAdmission>;
  logout(factory: CodexCandidateLauncherFactory, expectedSnapshotDigest: string): Promise<void>;
  openBindingStore(options: Parameters<typeof HostedIdentityBindingStore.open>[0]): Promise<HostedIdentityBindingStore>;
}

async function productionAcquireLease(runtimeDirectory: string, nativeAddonPath: string): Promise<RuntimeAdmissionLease> {
  await privateDirectory(runtimeDirectory);
  const binding = loadNativeAdmissionBinding(true, nativeAddonPath);
  if (binding.state !== "available") throw unavailable("NATIVE_ADMISSION_UNAVAILABLE");
  const acquired = binding.value.acquire(runtimeDirectory);
  if (acquired.state !== "available" || !acquired.value.held) throw unavailable("RUNTIME_ADMISSION_LEASE_UNAVAILABLE");
  return acquired.value;
}

async function assertStagedFile(path: string): Promise<void> {
  const info = await lstat(path);
  if (!info.isFile() || info.isSymbolicLink() || info.uid !== ownerId() || (info.mode & 0o777) !== 0o700 || info.nlink !== 1
    || await realpath(path) !== path) throw unavailable("STAGED_SUPPLIER_CUSTODY_UNSAFE");
}
async function assertPackagedSourceFile(path: string): Promise<void> {
  const info = await lstat(path);
  if (!info.isFile() || info.isSymbolicLink() || info.uid !== ownerId() || info.nlink !== 1 || (info.mode & 0o022) !== 0 || (info.mode & 0o100) === 0
    || await realpath(path) !== path) throw unavailable("PACKAGED_SUPPLIER_CUSTODY_UNSAFE");
}

/** Create-only staging. Existing bytes are reusable only after full exact-supply verification. */
export async function stageExactSupplierExecutable(sourcePath: string, privateRoot: string): Promise<string> {
  if (!canonical(sourcePath) || !canonical(privateRoot)) throw unavailable("SUPPLIER_STAGING_PATH_INVALID");
  const supplierDirectory = join(privateRoot, "supplier"), destination = join(supplierDirectory, "codex");
  if (!contained(privateRoot, destination)) throw unavailable("SUPPLIER_STAGING_PATH_INVALID");
  await privateDirectory(supplierDirectory);
  await assertPackagedSourceFile(sourcePath);
  const source = await verifyExactSupply({ executablePath: sourcePath });
  if (source.signatureStatus !== VALID_VENDOR_SIGNATURE) throw unavailable("SUPPLIER_SIGNATURE_UNQUALIFIED");
  let input: Awaited<ReturnType<typeof open>> | undefined;
  let output: Awaited<ReturnType<typeof open>> | undefined;
  let created = false;
  try {
    try { output = await open(destination, constants.O_WRONLY | constants.O_CREAT | constants.O_EXCL | constants.O_NOFOLLOW, 0o700); created = true; }
    catch (error) {
      if ((error as NodeJS.ErrnoException).code !== "EEXIST") throw error;
      await assertStagedFile(destination);
      const existing = await verifyExactSupply({ executablePath: destination });
      if (existing.sha256 !== source.sha256 || existing.version !== source.version || existing.signatureStatus !== source.signatureStatus) throw unavailable("STAGED_SUPPLIER_CONFLICT");
      await assertPackagedSourceFile(sourcePath); await revalidateExactSupply(source); await revalidateExactSupply(existing);
      return destination;
    }
    const metadata = await output.stat();
    if (!metadata.isFile() || metadata.uid !== ownerId() || (metadata.mode & 0o777) !== 0o700 || metadata.nlink !== 1) throw unavailable("STAGED_SUPPLIER_CUSTODY_UNSAFE");
    input = await open(source.executablePath, constants.O_RDONLY | constants.O_NOFOLLOW);
    const buffer = Buffer.alloc(64 * 1024);
    for (;;) {
      const { bytesRead } = await input.read(buffer, 0, buffer.length, null); if (bytesRead === 0) break;
      let written = 0; while (written < bytesRead) written += (await output.write(buffer, written, bytesRead - written)).bytesWritten;
    }
    await output.sync(); await output.close(); output = undefined; await syncDirectory(supplierDirectory);
    await assertStagedFile(destination);
    const staged = await verifyExactSupply({ executablePath: destination });
    if (staged.sha256 !== source.sha256 || staged.version !== source.version || staged.signatureStatus !== source.signatureStatus) throw unavailable("STAGED_SUPPLIER_MISMATCH");
    await assertPackagedSourceFile(sourcePath); await revalidateExactSupply(source); await revalidateExactSupply(staged);
    return destination;
  } catch (error) {
    if (created) await unlink(destination).catch(() => {});
    throw error instanceof RuntimeError ? error : unavailable("SUPPLIER_STAGING_FAILED", error);
  } finally { await input?.close().catch(() => {}); await output?.close().catch(() => {}); }
}

async function productionLogout(factory: CodexCandidateLauncherFactory, expectedAccountDigest: string): Promise<void> {
  const launcher = factory.create();
  let session: CodexTurnSession | undefined;
  let authority: Awaited<ReturnType<CodexTurnSession["establishAuthority"]>> | undefined;
  let failure: unknown;
  try {
    const candidate = await launcher.launchCandidate();
    session = new CodexTurnSession({ transport: candidate.transport });
    authority = await session.establishAuthority(candidate.authorityInitialize, candidate.kernelLease, candidate.cleanup);
    const accountDigest = await session.hostedAccountDigest(authority, candidate.supplierGeneration);
    if (accountDigest !== expectedAccountDigest) throw unavailable("LOGOUT_ACCOUNT_BINDING_MISMATCH");
    const account = await session.accountRead();
    if (!account.hasAccount) throw unavailable("SUPPLIER_ACCOUNT_ABSENT");
    await session.accountLogout();
  } catch (error) { failure = error; }
  for (const close of [() => authority?.close(), () => session?.close(), () => launcher.close?.()]) {
    try { await close(); } catch (error) { failure = failure === undefined ? error : new AggregateError([failure, error], "Hosted logout and cleanup failed"); }
  }
  if (failure !== undefined) throw failure;
}

async function productionPrepareNativeRoles(instructionRoot: string, privateRoot: string): Promise<{ digest: string; configOverrides: readonly string[] }> {
  const configuration = await loadTrustedNativeRoleConfiguration(instructionRoot);
  const directory = join(privateRoot, "native-roles"); await privateDirectory(directory);
  const files = {} as Record<(typeof CHIRALITY_ROLE_NAMES)[number], string>;
  for (const role of configuration.nativeRoles) {
    const path = join(directory, role.configFileName); files[role.roleId] = path;
    let handle;
    try {
      try { handle = await open(path, constants.O_WRONLY | constants.O_CREAT | constants.O_EXCL | constants.O_NOFOLLOW, 0o600); await handle.writeFile(role.configToml); await handle.sync(); }
      catch (error) {
        if ((error as NodeJS.ErrnoException).code !== "EEXIST") throw error;
        handle = await open(path, constants.O_RDONLY | constants.O_NOFOLLOW);
        const info = await handle.stat();
        if (!info.isFile() || info.uid !== ownerId() || (info.mode & 0o777) !== 0o600 || info.nlink !== 1 || await handle.readFile("utf8") !== role.configToml) throw unavailable("NATIVE_ROLE_CONFIG_CONFLICT");
      }
    } finally { await handle?.close(); }
  }
  await syncDirectory(directory);
  return Object.freeze({ digest: configuration.digest, configOverrides: codexNativeRoleConfigOverrides(configuration, files) });
}

const productionAdapters: ControlledHostedPrivateCompositionAdapters = Object.freeze({
  acquireLease: productionAcquireLease,
  stageSupplier: stageExactSupplierExecutable,
  prepareNativeRoles: productionPrepareNativeRoles,
  bindRuntimeReadRoot: bindTrustedRuntimeReadRoot,
  validateLoginStartup: validateCodexLoginStartup,
  createLogin: (options: ConstructorParameters<typeof CodexLogin>[0]) => {
    const login = new CodexLogin(options);
    return Object.freeze({
      start: () => login.startLogin(),
      async status() { const value = await login.status(); return { state: value.state, ...(value.hasAccount === undefined ? {} : { hasAccount: value.hasAccount }) }; },
      cancel: () => login.cancel(),
      close: () => login.close()
    });
  },
  preparePolicy: prepareCodexNativePolicy,
  createLauncherFactory: createCodexCandidateLauncherFactory,
  admitHosted: (options: HostedCodexSupervisorOptions) => CodexSupervisor.admitHosted(options),
  logout: productionLogout,
  openBindingStore: HostedIdentityBindingStore.open
});

interface CeremonyContext {
  projectId: string; canonicalRoot: string; privateDirectory: string; codexHome: string;
  providerNetworkConsent: { approvedBy: string; approvalReference: string; approvedAt: string };
  stagedExecutable: string; ceremony: TrustedHostedLoginCeremony; nativeRoles: { digest: string; configOverrides: readonly string[] }; runtimeReadRoot: TrustedRuntimeReadRootBinding;
}
interface AdmissionContext extends CeremonyContext {
  admission: HostedCodexSupervisorAdmission; launcherFactory: CodexCandidateLauncherFactory;
  store: HostedIdentityBindingStore; retired: boolean; signedOut: boolean; materialized?: DelegatedRuntime;
}

export function validateHostedPrivateCompositionOptions(value: unknown): Readonly<HostedPrivateCompositionOptions> {
  const options = value as HostedPrivateCompositionOptions;
  const required = ["runtimeDirectory", "supplierExecutablePath", "nativeAddonPath", "instructionRoot", "model", "managedAuth", "compatibility", "conformance", "loginPurposeRelease", "configDigest", "consentVersion", "commandNetworkPosture", "commandNetworkConsent", "protectedPaths", "immutableReadRoots"];
  const optional = ["nativePlanQualification", "requestTimeoutMs", "turnTimeoutMs", "maxWorkers"].filter(key => Object.prototype.hasOwnProperty.call(options ?? {}, key));
  if (!exactKeys(options, [...required, ...optional])) throw unavailable("HOST_CONFIGURATION_INVALID");
  if (!options || !canonical(options.runtimeDirectory) || !canonical(options.supplierExecutablePath) || !canonical(options.nativeAddonPath) || !canonical(options.instructionRoot)
    || !options.model?.trim() || options.model.length > 128 || !HEX.test(options.configDigest)
    || !options.consentVersion?.trim() || !["off", "ask-per-destination", "on"].includes(options.commandNetworkPosture)
    || !exactKeys(options.commandNetworkConsent, ["approvedBy", "approvedAt", "explicitUserAct"]) || !options.commandNetworkConsent.approvedBy.trim()
    || !Number.isFinite(Date.parse(options.commandNetworkConsent.approvedAt)) || options.commandNetworkConsent.explicitUserAct !== true
    || !Array.isArray(options.protectedPaths) || options.protectedPaths.some(path => !canonical(path))
    || !Array.isArray(options.immutableReadRoots) || options.immutableReadRoots.length === 0 || options.immutableReadRoots.some(path => !canonical(path))
    || !/^root-runtime-[1-9][0-9]*$/.test(options.compatibility?.compatibilityIdentity ?? "") || !HEX.test(options.compatibility?.contractBasisSha256 ?? "")
    || !options.conformance?.artifactInventory || !options.loginPurposeRelease?.artifactInventory) throw unavailable("HOST_CONFIGURATION_INVALID");
  validateHostedManagedAuth(options.managedAuth);
  return Object.freeze(structuredClone(options));
}

async function compose(options: HostedPrivateCompositionOptions, adapters: ControlledHostedPrivateCompositionAdapters): Promise<HostedBootstrapPrivateBindings> {
  const trusted = validateHostedPrivateCompositionOptions(options);
  if (!exactKeys(adapters, ["acquireLease", "stageSupplier", "prepareNativeRoles", "bindRuntimeReadRoot", "validateLoginStartup", "createLogin", "preparePolicy", "createLauncherFactory", "admitHosted", "logout", "openBindingStore"])
    || Object.values(adapters).some(value => typeof value !== "function")) throw unavailable("COMPOSITION_ADAPTER_INVALID");
  const lease = await adapters.acquireLease(trusted.runtimeDirectory, trusted.nativeAddonPath);
  if (!lease.held) throw unavailable("RUNTIME_ADMISSION_LEASE_UNAVAILABLE");
  const ceremonies = new Map<TrustedHostedLoginCeremony, CeremonyContext>();
  const admissions = new Map<TrustedHostedPrivateAdmission, AdmissionContext>();
  let closed = false, closing: Promise<void> | undefined;
  const retire = async (context: AdmissionContext): Promise<void> => {
    if (context.retired) return; context.retired = true;
    let failure: unknown;
    try { await context.materialized?.close(); } catch (error) { failure ??= error; }
    try { await context.admission.retire(); } catch (error) { failure ??= error; }
    try { await context.launcherFactory.close?.(); } catch (error) { failure ??= error; }
    if (failure) throw failure;
  };
  const bindings: HostedBootstrapPrivateBindings = {
    async createCeremony(input) {
      if (closed || !lease.held || !ID.test(input.projectId) || !canonical(input.canonicalRoot) || !canonical(input.privateDirectory) || !canonical(input.codexHome)
        || !contained(input.privateDirectory, input.codexHome) || contained(input.canonicalRoot, input.privateDirectory) || contained(input.privateDirectory, input.canonicalRoot)
        || !exactKeys(input.providerNetworkConsent, ["approvedBy", "approvalReference", "approvedAt"]) || !input.providerNetworkConsent.approvedBy.trim()
        || !input.providerNetworkConsent.approvalReference.trim() || !Number.isFinite(Date.parse(input.providerNetworkConsent.approvedAt))) throw unavailable("CEREMONY_BINDING_INVALID");
      const stagedExecutable = await adapters.stageSupplier(trusted.supplierExecutablePath, input.privateDirectory);
      if (!canonical(stagedExecutable) || !contained(input.privateDirectory, stagedExecutable)) throw unavailable("STAGED_SUPPLIER_PATH_INVALID");
      const nativeRoles = await adapters.prepareNativeRoles(trusted.instructionRoot, input.privateDirectory);
      const runtimeReadRoot = await adapters.bindRuntimeReadRoot(trusted.instructionRoot, trusted.conformance.artifactInventory);
      const expectedConfigDigest = recordKey({ schema: "chirality.hosted-private-config/v1", model: trusted.model, managedAuth: trusted.managedAuth,
        compatibility: trusted.compatibility, commandNetworkPosture: trusted.commandNetworkPosture, commandNetworkConsent: trusted.commandNetworkConsent, protectedPaths: trusted.protectedPaths,
        immutableReadRoots: trusted.immutableReadRoots, instructionRoot: trusted.instructionRoot, nativeRoleConfigurationDigest: nativeRoles.digest,
        trustedRuntimeReadRoot: { contentDigest: runtimeReadRoot.contentDigest, readPaths: runtimeReadRoot.readPaths }, loginPurposeRelease: trusted.loginPurposeRelease, consentVersion: trusted.consentVersion });
      if (trusted.configDigest !== expectedConfigDigest) throw unavailable("HOST_CONFIG_DIGEST_MISMATCH");
      const loginOptions = { executablePath: stagedExecutable, canonicalRoot: input.canonicalRoot, codexHome: input.codexHome,
        privateDirectory: input.privateDirectory, providerNetworkConsent: { approvedBy: input.providerNetworkConsent.approvedBy, approvalReference: input.providerNetworkConsent.approvalReference }, purposeRelease: trusted.loginPurposeRelease };
      const startupAdmission = await adapters.validateLoginStartup(loginOptions);
      const ceremony = adapters.createLogin({ ...loginOptions, startupAdmission });
      ceremonies.set(ceremony, { ...input, stagedExecutable, ceremony, nativeRoles, runtimeReadRoot });
      return ceremony;
    },
    async establishAdmission(input) {
      if (closed || !lease.held || (input.nativeAddonPath !== undefined && input.nativeAddonPath !== trusted.nativeAddonPath)) throw unavailable("ADMISSION_BINDING_INVALID");
      const context = ceremonies.get(input.ceremony);
      if (!context || context.projectId !== input.projectId || context.canonicalRoot !== input.canonicalRoot) throw unavailable("CEREMONY_BINDING_MISMATCH");
      const status = await context.ceremony.status();
      if (status.state !== "completed" || status.hasAccount !== true) throw unavailable("CEREMONY_NOT_COMPLETED");
      const attachmentRoot = join(context.canonicalRoot, ".chirality", "attachments"); await privateDirectory(attachmentRoot);
      const policy = await adapters.preparePolicy({ purpose: "worker", canonicalRoot: context.canonicalRoot, privateDirectory: context.privateDirectory,
        codexHome: context.codexHome, providerNetworkConsent: { approvedBy: context.providerNetworkConsent.approvedBy, approvalReference: context.providerNetworkConsent.approvalReference },
        commandNetworkPosture: trusted.commandNetworkPosture, protectedPaths: [...trusted.protectedPaths], readOnlyProjectPaths: [attachmentRoot], immutableReadRoots: [...trusted.immutableReadRoots],
        trustedRuntimeReadRoots: [context.runtimeReadRoot], nativeRoleConfiguration: context.nativeRoles });
      let launcherFactory: CodexCandidateLauncherFactory | undefined;
      let admitted: HostedCodexSupervisorAdmission | undefined;
      try {
        launcherFactory = adapters.createLauncherFactory({ bindings: { canonicalRoot: context.canonicalRoot, privateDirectory: context.privateDirectory,
          codexHome: context.codexHome, executablePath: context.stagedExecutable, nativeAddonPath: trusted.nativeAddonPath, model: trusted.model,
          providerNetworkConsent: { approvedBy: context.providerNetworkConsent.approvedBy, approvalReference: context.providerNetworkConsent.approvalReference },
          commandNetworkPosture: trusted.commandNetworkPosture, protectedPaths: [...trusted.protectedPaths], readOnlyProjectPaths: [attachmentRoot],
          immutableReadRoots: [...trusted.immutableReadRoots], trustedRuntimeReadRoots: [context.runtimeReadRoot], policyDigest: policy.policyDigest, configDigest: trusted.configDigest,
          consentVersion: trusted.consentVersion, toolRuntime: { codexSelfExecutablePath: context.stagedExecutable }, nativeRoleConfiguration: context.nativeRoles }, kernelLease: lease });
        const admission = admitted = await adapters.admitHosted({ canonicalRoot: context.canonicalRoot, candidateLauncherFactory: launcherFactory,
          conformance: trusted.conformance, executablePath: context.stagedExecutable, model: trusted.model, codexHome: context.codexHome,
          privateDirectory: context.privateDirectory, managedAuth: trusted.managedAuth, providerNetworkConsent: { approvedBy: context.providerNetworkConsent.approvedBy, approvalReference: context.providerNetworkConsent.approvalReference },
          protectedPaths: [...trusted.protectedPaths], readOnlyProjectPaths: [attachmentRoot], commandNetworkPosture: trusted.commandNetworkPosture,
          configDigest: trusted.configDigest, consentVersion: trusted.consentVersion,
          requestTimeoutMs: trusted.requestTimeoutMs, turnTimeoutMs: trusted.turnTimeoutMs, maxWorkers: trusted.maxWorkers });
        if (admission.continuity.canonicalRoot !== context.canonicalRoot || admission.continuity.cwd !== context.canonicalRoot || admission.continuity.policyDigest !== policy.policyDigest) throw unavailable("ADMISSION_CONTINUITY_MISMATCH");
        const store = await adapters.openBindingStore({ privateDirectory: context.privateDirectory, canonicalRoot: context.canonicalRoot,
          policyDigest: policy.policyDigest, runtimeAuthorityId: `composition-${recordKey({ projectId: context.projectId, policyDigest: policy.policyDigest }).slice(0, 32)}` });
        const publicAdmission: TrustedHostedPrivateAdmission = Object.freeze({ continuity: { ...admission.continuity }, authority: { ...admission.authority },
          ...(trusted.nativePlanQualification ? { nativePlanQualification: structuredClone(trusted.nativePlanQualification) } : {}), retire: async () => retire(admissions.get(publicAdmission)!) });
        admissions.set(publicAdmission, { ...context, admission, launcherFactory, store, retired: false, signedOut: false }); ceremonies.delete(context.ceremony);
        launcherFactory = undefined; return publicAdmission;
      } catch (error) { await admitted?.retire().catch(() => {}); await launcherFactory?.close?.().catch(() => {}); throw error; }
      finally { await policy.cleanup(); }
    },
    async materializeAdmission(input) {
      const context = admissions.get(input.admission);
      if (closed || !context || context.retired || context.projectId !== input.projectId || context.canonicalRoot !== input.canonicalRoot
        || input.runtime.attachmentStagingRoot !== join(input.canonicalRoot, ".chirality", "attachments")) throw unavailable("MATERIALIZATION_BINDING_INVALID");
      const project = await input.runtime.projects.requireAuthorized(input.projectId), roots = await input.runtime.projects.roots(input.projectId);
      if (project.canonicalRoot !== input.canonicalRoot || roots.workingRoot !== input.canonicalRoot || roots.instructionRoot !== trusted.instructionRoot) throw unavailable("PROJECT_REGISTRATION_MISMATCH");
      const consent = new HostedConsentStore({ canonicalRoot: input.canonicalRoot, codexHome: context.codexHome });
      await consent.grant({ identity: input.admission.continuity, posture: trusted.commandNetworkPosture,
        approvedBy: trusted.commandNetworkConsent.approvedBy, approvedAt: trusted.commandNetworkConsent.approvedAt });
      const retirement = new WorkerRetirementCoordinator({ directory: join(context.privateDirectory, "retirements") }); await retirement.reconcile();
      const approvals = new ApprovalStore({ canonicalRoot: input.canonicalRoot, storageRoot: join(context.privateDirectory, "approvals"), consent,
        isLive: async binding => (await context.admission.supervisor.inventory()).some(worker => worker.workerId === binding.turnId && worker.generation === binding.workerGeneration && worker.state === "running") });
      const delegated = new DelegatedRuntime({ daemonId: `hosted-${input.projectId}`, projects: new Map([[input.projectId, { identity: input.admission.continuity,
        compatibility: trusted.compatibility, supervisor: context.admission.supervisor, consent, retirement, approvals,
        approvalForwardingEnabled: trusted.commandNetworkPosture === "ask-per-destination", nativePlanSink: input.runtime.nativePlanSink,
        commandNetworkPosture: trusted.commandNetworkPosture, actual: { adapterId: "codex-app-server", providerId: "openai", model: trusted.model }, evidenceClass: "provider-observed" as const }]]) });
      context.materialized = delegated;
      return { delegated, selection: { adapterId: "codex-app-server", providerId: "openai", model: trusted.model }, compatibility: { ...trusted.compatibility }, evidenceClass: "provider-observed" as const };
    },
    async signOut(input) {
      if (closed || !ID.test(input.projectId) || !canonical(input.canonicalRoot) || !canonical(input.privateDirectory) || !canonical(input.codexHome)) throw unavailable("SIGNOUT_BINDING_INVALID");
      const matching = [...admissions.values()].filter(value => !value.signedOut && value.projectId === input.projectId && value.canonicalRoot === input.canonicalRoot
        && value.privateDirectory === input.privateDirectory && value.codexHome === input.codexHome);
      if (matching.length !== 1) throw unavailable("SIGNOUT_ADMISSION_CONTEXT_UNAVAILABLE");
      const context = matching[0]!;
      // The durable local fence is the first mutation. A supplier failure below
      // cannot revive this admission or its continuity epoch.
      context.signedOut = true;
      let localFailure: unknown;
      try { await context.store.fence("sign-out"); } catch (error) { localFailure = error; }
      try { await retire(context); } catch (error) { localFailure = localFailure === undefined ? error : new AggregateError([localFailure, error], "Hosted sign-out fence and retirement failed"); }
      if (localFailure !== undefined) throw localFailure;
      const stagedExecutable = context.stagedExecutable;
      const policy = await adapters.preparePolicy({ purpose: "worker", canonicalRoot: input.canonicalRoot, privateDirectory: input.privateDirectory, codexHome: input.codexHome,
        providerNetworkConsent: { approvedBy: context.providerNetworkConsent.approvedBy, approvalReference: context.providerNetworkConsent.approvalReference }, commandNetworkPosture: "off", protectedPaths: [...trusted.protectedPaths], immutableReadRoots: [...trusted.immutableReadRoots],
        trustedRuntimeReadRoots: [context.runtimeReadRoot], nativeRoleConfiguration: context.nativeRoles });
      let factory: CodexCandidateLauncherFactory | undefined, failure: unknown;
      try {
        factory = adapters.createLauncherFactory({ bindings: { canonicalRoot: input.canonicalRoot, privateDirectory: input.privateDirectory, codexHome: input.codexHome,
          executablePath: stagedExecutable, nativeAddonPath: trusted.nativeAddonPath, model: trusted.model, providerNetworkConsent: { approvedBy: context.providerNetworkConsent.approvedBy, approvalReference: context.providerNetworkConsent.approvalReference },
          commandNetworkPosture: "off", protectedPaths: [...trusted.protectedPaths], immutableReadRoots: [...trusted.immutableReadRoots], trustedRuntimeReadRoots: [context.runtimeReadRoot], policyDigest: policy.policyDigest,
          configDigest: trusted.configDigest, consentVersion: trusted.consentVersion, toolRuntime: { codexSelfExecutablePath: stagedExecutable }, nativeRoleConfiguration: context.nativeRoles }, kernelLease: lease });
        await adapters.logout(factory, context.admission.accountDigest);
      } catch (error) { failure = error; }
      for (const cleanup of [() => factory?.close?.(), () => policy.cleanup()]) {
        try { await cleanup(); } catch (error) { failure = failure === undefined ? error : new AggregateError([failure, error], "Hosted sign-out and cleanup failed"); }
      }
      if (failure !== undefined) throw failure;
    },
    close() {
      return closing ??= (async () => { closed = true; let failure: unknown;
        for (const context of admissions.values()) try { await retire(context); } catch (error) { failure ??= error; }
        for (const context of ceremonies.values()) try { await context.ceremony.close(); } catch (error) { failure ??= error; }
        ceremonies.clear(); admissions.clear(); try { if (lease.held) lease.close(); } catch (error) { failure ??= error; }
        if (failure) throw failure;
      })();
    }
  };
  return Object.freeze(bindings);
}

export function createHostedBootstrapPrivateBindings(options: HostedPrivateCompositionOptions): Promise<HostedBootstrapPrivateBindings> {
  return compose(options, productionAdapters);
}

/** Controlled composition seam. It supplies no exact-supply, native, account, or conformance acceptance. */
export function createControlledHostedBootstrapPrivateBindingsForTests(options: HostedPrivateCompositionOptions, adapters: ControlledHostedPrivateCompositionAdapters): Promise<HostedBootstrapPrivateBindings> {
  return compose(options, Object.freeze({ ...adapters }));
}
