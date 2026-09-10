import { codexLoginConfigOverridesV2 } from "./codex-containment.js";
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
import { codexEffectiveConfigDigestV2 } from "./codex-authenticated-transport.js";
import { bindTrustedRuntimeReadRoot, bindTrustedRuntimeReadRootV2, prepareCodexContainmentV2, prepareCodexNativePolicy, prepareCodexNativePolicyV2, prepareCodexTrustedSupplierContainmentV2, type TrustedRuntimeReadRootBinding, type TrustedRuntimeReadRootBindingV2 } from "./codex-containment.js";
import { CodexLogin, validateCodexLoginStartup, type CodexLoginStartupAdmission } from "./codex-login.js";
import { CodexTurnSession } from "./codex-session.js";
import { CodexSupervisor, type HostedCodexSupervisorAdmission, type HostedCodexSupervisorOptions } from "./codex-supervisor.js";
import { HostedIdentityBindingStore } from "./hosted-identity-binding.js";
import type { HostedBootstrapPrivateBindings, TrustedHostedLoginCeremony, TrustedHostedPrivateAdmission } from "./hosted-bootstrap.js";
import {
  hostAuthoritySubjectBindingDigestV2,
  issueRuntimeInstanceAdmissionV2,
  revalidateRuntimeInstanceAdmissionV2,
  revalidateHostedAccountAuthorityV2,
  verifyRuntimePurposeReleaseV2,
  type CodexPolicyInstanceV2,
  type HostedAccountAuthorityAdmission,
  type RuntimeInstanceAdmissionInputV2, type RuntimeInstanceAdmissionV2, type RuntimePurposeReleaseAdmissionV2,
  type RuntimePackagedPolicyBasisV2,
} from "./runtime-conformance-v2-admission.js";
import { revalidateIssuedPackagedReleaseBasisV2, type HostedPackagedReleaseBasisV2 } from "./hosted-packaged-release-state.js";

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
  model?: string;
  managedAuth?: HostedManagedAuth;
  compatibility: RuntimeCompatibilityIdentity;
  conformance?: RuntimeConformanceConfiguration;
  loginPurposeRelease?: RuntimeConformanceConfiguration;
  configDigest?: string;
  consentVersion?: string;
  commandNetworkPosture: "off" | "ask-per-destination" | "on";
  commandNetworkConsent?: { approvedBy: string; approvedAt: string; explicitUserAct: true };
  protectedPaths: readonly string[];
  immutableReadRoots: readonly string[];
  nativePlanQualification?: NativePlanAdapterQualification;
  requestTimeoutMs?: number;
  turnTimeoutMs?: number;
  maxWorkers?: number;
  /** Loader-issued private v2 release projection. No account, consent, project or host authority is accepted here. */
  releaseV2?: {
    basis: Readonly<HostedPackagedReleaseBasisV2>;
  };
}

interface PolicyResult {
  policyDigest: string;
  cleanup(): Promise<void>;
}

export interface ControlledHostedPrivateCompositionAdapters {
  revalidateReleaseBasis?(basis: Readonly<HostedPackagedReleaseBasisV2>): Promise<void>;
  acquireLease(runtimeDirectory: string, nativeAddonPath: string): Promise<RuntimeAdmissionLease>;
  stageSupplier(sourcePath: string, privateDirectory: string): Promise<string>;
  prepareNativeRoles(instructionRoot: string, privateDirectory: string): Promise<{ digest: string; configOverrides: readonly string[] }>;
  bindRuntimeReadRoot(path: string, inventory: RuntimeConformanceConfiguration["artifactInventory"]): Promise<TrustedRuntimeReadRootBinding>;
  validateLoginStartup(options: Omit<ConstructorParameters<typeof CodexLogin>[0], "timeoutMs" | "startupAdmission">): Promise<CodexLoginStartupAdmission>;
  createLogin(options: ConstructorParameters<typeof CodexLogin>[0]): TrustedHostedLoginCeremony;
  preparePolicy(options: Parameters<typeof prepareCodexNativePolicy>[0]): Promise<PolicyResult>;
  createLauncherFactory(options: Parameters<typeof createCodexCandidateLauncherFactory>[0]): CodexCandidateLauncherFactory;
  admitHosted(options: HostedCodexSupervisorOptions): Promise<HostedCodexSupervisorAdmission>;
  logout(factory: CodexCandidateLauncherFactory, expectedSnapshotDigest: string, runtimeV2?: NonNullable<HostedCodexSupervisorOptions["runtimeV2"]>): Promise<void>;
  openBindingStore(options: Parameters<typeof HostedIdentityBindingStore.open>[0]): Promise<HostedIdentityBindingStore>;
  /** Returns only an already-issued P2 admission. It is not an issuer or structural callback. */
  hostAuthority?(input: { purpose: "login" | "worker"; projectId: string; manifestHash: string; canonicalRoot: string; consentDigest: string; account?: RuntimeInstanceAdmissionInputV2["account"] }): Promise<{ authority: HostedAccountAuthorityAdmission; account: RuntimeInstanceAdmissionInputV2["account"] }>;
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

export async function productionLogout(factory: CodexCandidateLauncherFactory, expectedAccountDigest: string, runtimeV2?: NonNullable<HostedCodexSupervisorOptions["runtimeV2"]>): Promise<void> {
  const launcher = factory.create();
  let session: CodexTurnSession | undefined;
  let authority: Awaited<ReturnType<CodexTurnSession["establishAuthority"]>> | undefined;
  let failure: unknown;
  try {
    const candidate = await launcher.launchCandidate();
    session = new CodexTurnSession({ transport: candidate.transport, commandNetworkPosture: "off",
      permissionProfile: candidate.expectedPolicy.permissionProfile, policyDigest: candidate.expectedPolicy.policyDigest });
    if (runtimeV2) await revalidateRuntimeInstanceAdmissionV2(runtimeV2.instanceInput, runtimeV2.instanceAdmission);
    authority = await session.establishAuthority(candidate.authorityInitialize, candidate.kernelLease, candidate.cleanup);
    if (runtimeV2 && (candidate.expectedOuterPolicyDigest !== runtimeV2.instanceInput.outerPolicyDigest
      || candidate.expectedPolicy.policyDigest !== runtimeV2.instanceInput.nativePolicyDigest
      || candidate.expectedEffectiveConfigDigestV2 !== runtimeV2.instanceInput.effectiveConfigDigest
      || recordKey(candidate.expectedPolicy.policyInstanceV2) !== recordKey(runtimeV2.instanceInput.policy))) throw unavailable("LOGOUT_INSTANCE_BINDING_MISMATCH");
    if (runtimeV2) await session.verifyNativePolicy(candidate.expectedPolicy.expectedPermissions, candidate.expectedPolicy.nativeRoleConfiguration);
    const accountDigest = await session.hostedAccountDigest(authority, candidate.supplierGeneration);
    if (accountDigest !== expectedAccountDigest) throw unavailable("LOGOUT_ACCOUNT_BINDING_MISMATCH");
    const account = await session.accountRead();
    if (!account.hasAccount) throw unavailable("SUPPLIER_ACCOUNT_ABSENT");
    if (runtimeV2) {
      await revalidateRuntimeInstanceAdmissionV2(runtimeV2.instanceInput, runtimeV2.instanceAdmission);
      if (await session.hostedAccountDigest(authority, candidate.supplierGeneration) !== runtimeV2.instanceInput.account?.accountDigest) throw unavailable("LOGOUT_ACCOUNT_BINDING_MISMATCH");
      await revalidateHostedAccountAuthorityV2(runtimeV2.instanceInput.hostAuthority, { purpose: "worker", projectId: runtimeV2.instanceInput.projectId, manifestHash: runtimeV2.instanceInput.manifestHash, canonicalRoot: runtimeV2.instanceInput.canonicalRoot, account: runtimeV2.instanceInput.account, consentDigest: runtimeV2.instanceInput.consent.digest });
    }
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
  revalidateReleaseBasis: revalidateIssuedPackagedReleaseBasisV2,
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
      resolveDefaultModel: () => login.resolveDefaultModel(),
      cancel: () => login.cancel(),
      close: () => login.close()
    });
  },
  preparePolicy: prepareCodexNativePolicy,
  createLauncherFactory: createCodexCandidateLauncherFactory,
  admitHosted: (options: HostedCodexSupervisorOptions) => CodexSupervisor.admitHosted(options),
  logout: productionLogout,
  openBindingStore: HostedIdentityBindingStore.open
  // HOST-P2 intentionally has no production adapter yet.
});

interface CeremonyContext {
  projectId: string; manifestHash: string; consentVersion: string; canonicalRoot: string; privateDirectory: string; codexHome: string;
  providerNetworkConsent: { approvedBy: string; approvalReference: string; approvedAt: string };
  stagedExecutable: string; configDigest: string; model?: string; defaultReasoningEffort?: string; ceremony: TrustedHostedLoginCeremony; nativeRoles: { digest: string; configOverrides: readonly string[] }; runtimeReadRoot: TrustedRuntimeReadRootBinding;
  v2?: { loginRelease: RuntimePurposeReleaseAdmissionV2; loginInput: RuntimeInstanceAdmissionInputV2; loginAdmission: RuntimeInstanceAdmissionV2; runtimeReadRoot: TrustedRuntimeReadRootBindingV2 };
}
interface AdmissionContext extends CeremonyContext {
  admission: HostedCodexSupervisorAdmission; launcherFactory: CodexCandidateLauncherFactory;
  store: HostedIdentityBindingStore; retirement?: Promise<void>; retired: boolean; signedOut: boolean; materialized?: DelegatedRuntime;
  runtimeV2?: HostedCodexSupervisorOptions["runtimeV2"];
}

export function validateHostedPrivateCompositionOptions(value: unknown): Readonly<HostedPrivateCompositionOptions> {
  const options = value as HostedPrivateCompositionOptions;
  const required = ["runtimeDirectory", "supplierExecutablePath", "nativeAddonPath", "instructionRoot", "compatibility", "commandNetworkPosture", "protectedPaths", "immutableReadRoots"];
  const optional = ["model", "conformance", "loginPurposeRelease", "configDigest", "consentVersion", "commandNetworkConsent", "nativePlanQualification", "requestTimeoutMs", "turnTimeoutMs", "maxWorkers"].filter(key => Object.prototype.hasOwnProperty.call(options ?? {}, key));
  if (Object.prototype.hasOwnProperty.call(options ?? {}, "managedAuth")) optional.push("managedAuth");
  if (Object.prototype.hasOwnProperty.call(options ?? {}, "releaseV2")) optional.push("releaseV2");
  if (!exactKeys(options, [...required, ...optional])) throw unavailable("HOST_CONFIGURATION_INVALID");
  if (!options || !canonical(options.runtimeDirectory) || !canonical(options.supplierExecutablePath) || !canonical(options.nativeAddonPath) || !canonical(options.instructionRoot)
    || (options.model !== undefined && (!options.model.trim() || options.model.length > 128))
    || (options.consentVersion !== undefined && !options.consentVersion.trim()) || !["off", "ask-per-destination", "on"].includes(options.commandNetworkPosture)
    || !Array.isArray(options.protectedPaths) || options.protectedPaths.some(path => !canonical(path))
    || !Array.isArray(options.immutableReadRoots) || options.immutableReadRoots.length === 0 || options.immutableReadRoots.some(path => !canonical(path))
    || !/^root-runtime-[1-9][0-9]*$/.test(options.compatibility?.compatibilityIdentity ?? "") || !HEX.test(options.compatibility?.contractBasisSha256 ?? "")) throw unavailable("HOST_CONFIGURATION_INVALID");
  if (options.releaseV2 !== undefined && (options.model !== undefined || options.managedAuth !== undefined || options.conformance !== undefined || options.loginPurposeRelease !== undefined || options.configDigest !== undefined || options.consentVersion !== undefined || options.commandNetworkConsent !== undefined || options.commandNetworkPosture !== "off"
    || !exactKeys(options.releaseV2, ["basis"]) || options.releaseV2.basis.schema !== "chirality-hosted-packaged-release-basis/v2"
    || ![options.runtimeDirectory, join(options.runtimeDirectory, "release-authority"), join(options.runtimeDirectory, "release-basis")].every(path => options.protectedPaths.includes(path)))) throw unavailable("HOST_CONFIGURATION_INVALID");
  if (options.releaseV2 === undefined && (!options.model || !options.managedAuth || !options.consentVersion || !options.conformance?.artifactInventory || !options.loginPurposeRelease?.artifactInventory || !HEX.test(options.configDigest ?? "")
    || !exactKeys(options.commandNetworkConsent, ["approvedBy", "approvedAt", "explicitUserAct"]) || !options.commandNetworkConsent!.approvedBy.trim()
    || !Number.isFinite(Date.parse(options.commandNetworkConsent!.approvedAt)) || options.commandNetworkConsent!.explicitUserAct !== true)) throw unavailable("HOST_CONFIGURATION_INVALID");
  if (options.managedAuth) validateHostedManagedAuth(options.managedAuth);
  const { releaseV2, ...plain } = options;
  const clone = structuredClone(plain) as HostedPrivateCompositionOptions;
  if (options.releaseV2) clone.releaseV2 = Object.freeze({ basis: options.releaseV2.basis });
  return Object.freeze(clone);
}

async function compose(options: HostedPrivateCompositionOptions, adapters: ControlledHostedPrivateCompositionAdapters): Promise<HostedBootstrapPrivateBindings> {
  const trusted = validateHostedPrivateCompositionOptions(options);
  if (trusted.releaseV2) await (adapters.revalidateReleaseBasis ?? revalidateIssuedPackagedReleaseBasisV2)(trusted.releaseV2.basis);
  const adapterNames = ["acquireLease", "stageSupplier", "prepareNativeRoles", "bindRuntimeReadRoot", "validateLoginStartup", "createLogin", "preparePolicy", "createLauncherFactory", "admitHosted", "logout", "openBindingStore", ...(Object.prototype.hasOwnProperty.call(adapters, "hostAuthority") ? ["hostAuthority"] : []), ...(Object.prototype.hasOwnProperty.call(adapters, "revalidateReleaseBasis") ? ["revalidateReleaseBasis"] : [])];
  if (!exactKeys(adapters, adapterNames)
    || Object.values(adapters).some(value => typeof value !== "function")) throw unavailable("COMPOSITION_ADAPTER_INVALID");
  const lease = await adapters.acquireLease(trusted.runtimeDirectory, trusted.nativeAddonPath);
  if (!lease.held) throw unavailable("RUNTIME_ADMISSION_LEASE_UNAVAILABLE");
  const ceremonies = new Map<TrustedHostedLoginCeremony, CeremonyContext>();
  const admissions = new Map<TrustedHostedPrivateAdmission, AdmissionContext>();
  let closed = false, closing: Promise<void> | undefined;
  const retire = (context: AdmissionContext): Promise<void> => context.retirement ??= (async () => {
    context.retired = true;
    const failures: unknown[] = [];
    for (const close of [() => context.materialized?.close(), () => context.admission.retire(), () => context.launcherFactory.close?.()]) {
      try { await close(); } catch (error) { failures.push(error); }
    }
    if (failures.length) throw new AggregateError(failures, "Hosted admission retirement failed; ownership retained");
  })();
  const bindings: HostedBootstrapPrivateBindings = {
    async createCeremony(input) {
      if (closed || !lease.held || !ID.test(input.projectId) || (trusted.releaseV2 !== undefined && !HEX.test(input.manifestHash ?? "")) || !canonical(input.canonicalRoot) || !canonical(input.privateDirectory) || !canonical(input.codexHome)
        || !contained(input.privateDirectory, input.codexHome) || contained(input.canonicalRoot, input.privateDirectory) || contained(input.privateDirectory, input.canonicalRoot)
        || !exactKeys(input.providerNetworkConsent, ["approvedBy", "approvalReference", "approvedAt"]) || !input.providerNetworkConsent.approvedBy.trim()
        || !input.providerNetworkConsent.approvalReference.trim() || !Number.isFinite(Date.parse(input.providerNetworkConsent.approvedAt))) throw unavailable("CEREMONY_BINDING_INVALID");
      let loginHost: { authority: HostedAccountAuthorityAdmission; account: RuntimeInstanceAdmissionInputV2["account"] } | undefined;
      let v2ConsentDigest: string | undefined;
      let v2ConsentVersion: string | undefined;
      if (trusted.releaseV2) {
        if (!adapters.hostAuthority) throw unavailable("HOST_ACCOUNT_AUTHORITY_UNAVAILABLE");
        const manifestHash = input.manifestHash!;
        v2ConsentVersion = recordKey({ schema: "chirality-hosted-consent-version/v2", projectId: input.projectId, manifestHash, provenance: input.providerNetworkConsent });
        v2ConsentDigest = recordKey({ schema: "chirality-hosted-consent/v2", projectId: input.projectId, manifestHash, version: v2ConsentVersion, provenance: input.providerNetworkConsent, authenticatedExplicitUserAct: true });
        loginHost = await adapters.hostAuthority({ purpose: "login", projectId: input.projectId, manifestHash, canonicalRoot: input.canonicalRoot, consentDigest: v2ConsentDigest });
        if (loginHost.account !== null || loginHost.authority.subjectBindingDigest !== hostAuthoritySubjectBindingDigestV2({ purpose: "login", projectId: input.projectId, manifestHash, canonicalRoot: input.canonicalRoot, account: null, consentDigest: v2ConsentDigest })) throw unavailable("HOST_ACCOUNT_AUTHORITY_MISMATCH");
        await revalidateHostedAccountAuthorityV2(loginHost.authority, { purpose: "login", projectId: input.projectId, manifestHash, canonicalRoot: input.canonicalRoot, account: null, consentDigest: v2ConsentDigest });
      }
      const stagedExecutable = await adapters.stageSupplier(trusted.supplierExecutablePath, input.privateDirectory);
      if (!canonical(stagedExecutable) || !contained(input.privateDirectory, stagedExecutable)) throw unavailable("STAGED_SUPPLIER_PATH_INVALID");
      const nativeRoles = await adapters.prepareNativeRoles(trusted.instructionRoot, input.privateDirectory);
      const policyBasis: RuntimePackagedPolicyBasisV2 | undefined = trusted.releaseV2 ? { schema: "chirality-runtime-packaged-basis/v2", resourcesRoot: trusted.releaseV2.basis.verified.resourcesRoot,
        inventoryPath: trusted.releaseV2.basis.verified.inventoryPath, payloadManifestPath: trusted.releaseV2.basis.verified.payloadManifestPath,
        outerInventorySha256: trusted.releaseV2.basis.verified.inventorySha256, payloadDigest: trusted.releaseV2.basis.verified.payloadDigest } : undefined;
      const runtimeReadRoot = trusted.releaseV2
        ? await bindTrustedRuntimeReadRootV2(trusted.instructionRoot, policyBasis!)
        : await adapters.bindRuntimeReadRoot(trusted.instructionRoot, trusted.conformance!.artifactInventory);
      const expectedConfigDigest = trusted.releaseV2
        ? recordKey({ schema: "chirality.hosted-private-config/v2", projectId: input.projectId, manifestHash: input.manifestHash, model: trusted.model, accountStorage: { backend: "keyring" },
            compatibility: trusted.compatibility, providerNetworkConsent: input.providerNetworkConsent, commandNetworkPosture: trusted.commandNetworkPosture, protectedPaths: trusted.protectedPaths,
            immutableReadRoots: trusted.immutableReadRoots, instructionRoot: trusted.instructionRoot, nativeRoleConfigurationDigest: nativeRoles.digest,
            trustedRuntimeReadRoot: { contentDigest: runtimeReadRoot.contentDigest, readPaths: runtimeReadRoot.readPaths }, releaseV2: { basisDigest: trusted.releaseV2.basis.basisDigest }, consentVersion: v2ConsentVersion })
        : recordKey({ schema: "chirality.hosted-private-config/v1", model: trusted.model, managedAuth: trusted.managedAuth,
            compatibility: trusted.compatibility, commandNetworkPosture: trusted.commandNetworkPosture, commandNetworkConsent: trusted.commandNetworkConsent, protectedPaths: trusted.protectedPaths,
            immutableReadRoots: trusted.immutableReadRoots, instructionRoot: trusted.instructionRoot, nativeRoleConfigurationDigest: nativeRoles.digest,
            trustedRuntimeReadRoot: { contentDigest: runtimeReadRoot.contentDigest, readPaths: runtimeReadRoot.readPaths }, loginPurposeRelease: trusted.loginPurposeRelease, consentVersion: trusted.consentVersion });
      if (!trusted.releaseV2 && trusted.configDigest !== expectedConfigDigest) throw unavailable("HOST_CONFIG_DIGEST_MISMATCH");
      const loginOptions = { executablePath: stagedExecutable, canonicalRoot: input.canonicalRoot, codexHome: input.codexHome,
        privateDirectory: input.privateDirectory, providerNetworkConsent: { approvedBy: input.providerNetworkConsent.approvedBy, approvalReference: input.providerNetworkConsent.approvalReference }, ...(trusted.loginPurposeRelease ? { purposeRelease: trusted.loginPurposeRelease } : {}) };
      let v2: CeremonyContext["v2"];
      if (trusted.releaseV2) {
        const manifestHash = input.manifestHash!;
        const consentDigest = v2ConsentDigest!, observedHost = loginHost!;
        const purposeRelease = await verifyRuntimePurposeReleaseV2(trusted.releaseV2.basis, "login");
        const policy: CodexPolicyInstanceV2 = { schema: "chirality-codex-policy-instance/v2", outerPurpose: "trusted-login", nativePurpose: null,
          canonicalRoot: input.canonicalRoot, privateDirectory: input.privateDirectory, codexHome: input.codexHome, executablePath: stagedExecutable, nativeAddonPath: trusted.nativeAddonPath,
          providerNetworkConsent: { approvedBy: input.providerNetworkConsent.approvedBy, approvalReference: input.providerNetworkConsent.approvalReference }, commandNetworkPosture: "off",
          immutableReadRoots: [], protectedPaths: [], readOnlyProjectPaths: [], trustedRuntimeReadRoots: [], toolRuntime: { codexSelfExecutablePath: stagedExecutable, requiresSandboxedFileSystem: true, requiresSandboxedFileStreaming: true }, nativeRoleConfiguration: null };
        const outer = await prepareCodexContainmentV2({ ...loginOptions, purpose: "trusted-login" });
        try {
          const instanceInput: RuntimeInstanceAdmissionInputV2 = { purposeRelease, hostAuthority: observedHost.authority, projectId: input.projectId, manifestHash,
            canonicalRoot: input.canonicalRoot, cwd: input.canonicalRoot, privateDirectory: input.privateDirectory, codexHome: input.codexHome, brokerRoot: trusted.runtimeDirectory,
            instructionRoot: trusted.instructionRoot, nativeAddonPath: trusted.nativeAddonPath, supplierExecutablePath: stagedExecutable, attachmentRoot: join(input.canonicalRoot, ".chirality", "attachments"),
        account: null, consent: { version: v2ConsentVersion!, digest: consentDigest, authenticatedExplicitUserAct: true }, policy, outerPolicyDigest: outer.outerPolicyDigest,
            nativePolicyDigest: null, effectiveConfigDigest: codexEffectiveConfigDigestV2({ executablePath: stagedExecutable, cwd: input.canonicalRoot,
              environment: { HOME: outer.environment.HOME, CODEX_HOME: outer.environment.CODEX_HOME, PATH: outer.environment.PATH, LANG: outer.environment.LANG }, configOverrides: codexLoginConfigOverridesV2(outer.config) }) };
          const instanceAdmission = await issueRuntimeInstanceAdmissionV2(instanceInput);
          Object.assign(loginOptions, { releaseV2: trusted.releaseV2.basis, instanceV2: instanceInput, instanceAdmissionV2: instanceAdmission });
          v2 = { loginRelease: purposeRelease, loginInput: instanceInput, loginAdmission: instanceAdmission, runtimeReadRoot: runtimeReadRoot as TrustedRuntimeReadRootBindingV2 };
        } finally { await outer.cleanup(); }
      }
      const startupAdmission = await adapters.validateLoginStartup(loginOptions);
      const ceremony = adapters.createLogin({ ...loginOptions, startupAdmission });
      ceremonies.set(ceremony, { ...input, manifestHash: input.manifestHash ?? "", consentVersion: v2?.loginInput.consent.version ?? trusted.consentVersion!, stagedExecutable, configDigest: expectedConfigDigest, ceremony, nativeRoles, runtimeReadRoot: runtimeReadRoot as TrustedRuntimeReadRootBinding, ...(v2 ? { v2 } : {}) });
      return ceremony;
    },
    async establishAdmission(input) {
      if (closed || !lease.held || (input.nativeAddonPath !== undefined && input.nativeAddonPath !== trusted.nativeAddonPath)) throw unavailable("ADMISSION_BINDING_INVALID");
      const context = ceremonies.get(input.ceremony);
      if (!context || context.projectId !== input.projectId || context.canonicalRoot !== input.canonicalRoot) throw unavailable("CEREMONY_BINDING_MISMATCH");
      const status = await context.ceremony.status();
      if (status.state !== "completed" || status.hasAccount !== true) throw unavailable("CEREMONY_NOT_COMPLETED");
      const selected = context.v2
        ? await context.ceremony.resolveDefaultModel?.() ?? (() => { throw unavailable("MODEL_CATALOG_UNAVAILABLE"); })()
        : { model: trusted.model!, defaultReasoningEffort: "" };
      context.model = selected.model; context.defaultReasoningEffort = context.v2 ? selected.defaultReasoningEffort : undefined;
      if (context.v2 && trusted.releaseV2) context.configDigest = recordKey({ schema: "chirality.hosted-private-config/v2", projectId: context.projectId, manifestHash: context.manifestHash,
        model: selected.model, defaultReasoningEffort: selected.defaultReasoningEffort, accountStorage: { backend: "keyring" }, compatibility: trusted.compatibility,
        providerNetworkConsent: context.providerNetworkConsent, commandNetworkPosture: trusted.commandNetworkPosture, protectedPaths: trusted.protectedPaths,
        immutableReadRoots: trusted.immutableReadRoots, instructionRoot: trusted.instructionRoot, nativeRoleConfigurationDigest: context.nativeRoles.digest,
        trustedRuntimeReadRoot: { contentDigest: context.v2.runtimeReadRoot.contentDigest, readPaths: context.v2.runtimeReadRoot.readPaths }, releaseV2: { basisDigest: trusted.releaseV2.basis.basisDigest }, consentVersion: context.consentVersion });
      const attachmentRoot = join(context.canonicalRoot, ".chirality", "attachments"); await privateDirectory(attachmentRoot);
      const policy = context.v2
        ? await prepareCodexNativePolicyV2({ purpose: "worker", canonicalRoot: context.canonicalRoot, privateDirectory: context.privateDirectory,
            codexHome: context.codexHome, executablePath: context.stagedExecutable, nativeAddonPath: trusted.nativeAddonPath,
            providerNetworkConsent: { approvedBy: context.providerNetworkConsent.approvedBy, approvalReference: context.providerNetworkConsent.approvalReference },
            commandNetworkPosture: trusted.commandNetworkPosture, protectedPaths: [...trusted.protectedPaths], readOnlyProjectPaths: [attachmentRoot], immutableReadRoots: [...trusted.immutableReadRoots],
            trustedRuntimeReadRoots: [context.v2.runtimeReadRoot], nativeRoleConfiguration: context.nativeRoles,
            toolRuntime: { codexSelfExecutablePath: context.stagedExecutable, requiresSandboxedFileSystem: true, requiresSandboxedFileStreaming: true } })
        : await adapters.preparePolicy({ purpose: "worker", canonicalRoot: context.canonicalRoot, privateDirectory: context.privateDirectory,
            codexHome: context.codexHome, providerNetworkConsent: { approvedBy: context.providerNetworkConsent.approvedBy, approvalReference: context.providerNetworkConsent.approvalReference },
            commandNetworkPosture: trusted.commandNetworkPosture, protectedPaths: [...trusted.protectedPaths], readOnlyProjectPaths: [attachmentRoot], immutableReadRoots: [...trusted.immutableReadRoots],
            trustedRuntimeReadRoots: [context.runtimeReadRoot], nativeRoleConfiguration: context.nativeRoles });
      let launcherFactory: CodexCandidateLauncherFactory | undefined;
      let admitted: HostedCodexSupervisorAdmission | undefined;
      try {
        let runtimeV2: HostedCodexSupervisorOptions["runtimeV2"];
        if (context.v2 && trusted.releaseV2) {
          if (!adapters.hostAuthority) throw unavailable("HOST_ACCOUNT_AUTHORITY_UNAVAILABLE");
          const consentDigest = context.v2.loginInput.consent.digest;
          const observedHost = await adapters.hostAuthority({ purpose: "worker", projectId: context.projectId, manifestHash: context.manifestHash, canonicalRoot: context.canonicalRoot, consentDigest });
          if (!observedHost.account || observedHost.authority.subjectBindingDigest !== hostAuthoritySubjectBindingDigestV2({ purpose: "worker", projectId: context.projectId, manifestHash: context.manifestHash, canonicalRoot: context.canonicalRoot, account: observedHost.account, consentDigest })) throw unavailable("HOST_ACCOUNT_AUTHORITY_MISMATCH");
          const purposeRelease = await verifyRuntimePurposeReleaseV2(trusted.releaseV2.basis, "worker");
          const outer = await prepareCodexTrustedSupplierContainmentV2({ canonicalRoot: context.canonicalRoot, privateDirectory: context.privateDirectory, codexHome: context.codexHome,
            providerNetworkConsent: { approvedBy: context.providerNetworkConsent.approvedBy, approvalReference: context.providerNetworkConsent.approvalReference }, trustedRuntimeReadRoots: [context.v2.runtimeReadRoot] });
          try {
            const instanceInput: RuntimeInstanceAdmissionInputV2 = { purposeRelease, hostAuthority: observedHost.authority, projectId: context.projectId, manifestHash: context.manifestHash,
              canonicalRoot: context.canonicalRoot, cwd: context.canonicalRoot, privateDirectory: context.privateDirectory, codexHome: context.codexHome, brokerRoot: trusted.runtimeDirectory,
              instructionRoot: trusted.instructionRoot, nativeAddonPath: trusted.nativeAddonPath, supplierExecutablePath: context.stagedExecutable, attachmentRoot,
              account: observedHost.account, consent: context.v2.loginInput.consent, policy: (policy as Awaited<ReturnType<typeof prepareCodexNativePolicyV2>>).policyInstance,
              outerPolicyDigest: outer.outerPolicyDigest, nativePolicyDigest: policy.policyDigest, effectiveConfigDigest: codexEffectiveConfigDigestV2({ executablePath: context.stagedExecutable, cwd: context.canonicalRoot,
                environment: { HOME: outer.environment.HOME, CODEX_HOME: outer.environment.CODEX_HOME, PATH: outer.environment.PATH, LANG: outer.environment.LANG },
                configOverrides: (policy as Awaited<ReturnType<typeof prepareCodexNativePolicyV2>>).configOverrides }) };
            const instanceAdmission = await issueRuntimeInstanceAdmissionV2(instanceInput);
            runtimeV2 = { releaseBasis: trusted.releaseV2.basis, instanceInput, instanceAdmission };
          } finally { await outer.cleanup(); }
        }
        launcherFactory = adapters.createLauncherFactory({ bindings: { canonicalRoot: context.canonicalRoot, privateDirectory: context.privateDirectory,
          codexHome: context.codexHome, executablePath: context.stagedExecutable, nativeAddonPath: trusted.nativeAddonPath, model: selected.model,
          providerNetworkConsent: { approvedBy: context.providerNetworkConsent.approvedBy, approvalReference: context.providerNetworkConsent.approvalReference },
          commandNetworkPosture: trusted.commandNetworkPosture, protectedPaths: [...trusted.protectedPaths], readOnlyProjectPaths: [attachmentRoot],
          immutableReadRoots: [...trusted.immutableReadRoots], trustedRuntimeReadRoots: [context.runtimeReadRoot], policyDigest: policy.policyDigest, configDigest: context.configDigest,
          consentVersion: context.consentVersion, toolRuntime: { codexSelfExecutablePath: context.stagedExecutable }, nativeRoleConfiguration: context.nativeRoles,
          ...(context.v2 && runtimeV2 ? { policyInstanceV2: (policy as Awaited<ReturnType<typeof prepareCodexNativePolicyV2>>).policyInstance,
            expectedEffectiveConfigDigestV2: runtimeV2.instanceInput.effectiveConfigDigest, instanceInputV2: runtimeV2.instanceInput, instanceAdmissionV2: runtimeV2.instanceAdmission } : {}) }, kernelLease: lease });
        const admission = admitted = await adapters.admitHosted({ canonicalRoot: context.canonicalRoot, candidateLauncherFactory: launcherFactory,
          ...(trusted.conformance ? { conformance: trusted.conformance } : {}), executablePath: context.stagedExecutable, model: selected.model, ...(context.v2 ? { reasoningEffort: selected.defaultReasoningEffort } : {}), codexHome: context.codexHome,
          privateDirectory: context.privateDirectory, ...(context.v2 ? { accountStorageBackend: "keyring" as const } : { managedAuth: trusted.managedAuth! }), providerNetworkConsent: { approvedBy: context.providerNetworkConsent.approvedBy, approvalReference: context.providerNetworkConsent.approvalReference },
          protectedPaths: [...trusted.protectedPaths], readOnlyProjectPaths: [attachmentRoot], commandNetworkPosture: trusted.commandNetworkPosture,
          configDigest: context.configDigest, consentVersion: context.consentVersion, ...(runtimeV2 ? { runtimeV2 } : {}),
          requestTimeoutMs: trusted.requestTimeoutMs, turnTimeoutMs: trusted.turnTimeoutMs, maxWorkers: trusted.maxWorkers });
        if (admission.continuity.canonicalRoot !== context.canonicalRoot || admission.continuity.cwd !== context.canonicalRoot || admission.continuity.policyDigest !== policy.policyDigest) throw unavailable("ADMISSION_CONTINUITY_MISMATCH");
        const store = await adapters.openBindingStore({ privateDirectory: context.privateDirectory, canonicalRoot: context.canonicalRoot,
          policyDigest: policy.policyDigest, runtimeAuthorityId: `composition-${recordKey({ projectId: context.projectId, policyDigest: policy.policyDigest }).slice(0, 32)}` });
        const publicAdmission: TrustedHostedPrivateAdmission = Object.freeze({ continuity: { ...admission.continuity }, authority: { ...admission.authority },
          ...(trusted.nativePlanQualification ? { nativePlanQualification: structuredClone(trusted.nativePlanQualification) } : {}), retire: async () => retire(admissions.get(publicAdmission)!) });
        admissions.set(publicAdmission, { ...context, admission, launcherFactory, store, retired: false, signedOut: false, ...(runtimeV2 ? { runtimeV2 } : {}) }); ceremonies.delete(context.ceremony);
        launcherFactory = undefined; return publicAdmission;
      } catch (error) {
        const failures: unknown[] = [error];
        for (const close of [() => admitted?.retire(), () => launcherFactory?.close?.()]) try { await close(); } catch (cleanup) { failures.push(cleanup); }
        if (failures.length > 1) throw new AggregateError(failures, "Hosted establishment and cleanup failed"); throw error;
      }
      finally { await policy.cleanup(); }
    },
    async materializeAdmission(input) {
      const context = admissions.get(input.admission);
      if (closed || !context || context.retired || context.projectId !== input.projectId || context.canonicalRoot !== input.canonicalRoot
        || input.runtime.attachmentStagingRoot !== join(input.canonicalRoot, ".chirality", "attachments")) throw unavailable("MATERIALIZATION_BINDING_INVALID");
      const project = await input.runtime.projects.requireAuthorized(input.projectId), roots = await input.runtime.projects.roots(input.projectId);
      if (project.canonicalRoot !== input.canonicalRoot || (context.v2 && project.manifestHash !== context.manifestHash) || roots.workingRoot !== input.canonicalRoot || roots.instructionRoot !== trusted.instructionRoot) throw unavailable("PROJECT_REGISTRATION_MISMATCH");
      const consent = new HostedConsentStore({ canonicalRoot: input.canonicalRoot, codexHome: context.codexHome });
      if (!context.v2) await consent.grant({ identity: input.admission.continuity, posture: trusted.commandNetworkPosture,
        approvedBy: trusted.commandNetworkConsent!.approvedBy, approvedAt: trusted.commandNetworkConsent!.approvedAt });
      const retirement = new WorkerRetirementCoordinator({ directory: join(context.privateDirectory, "retirements") }); await retirement.reconcile();
      const approvals = new ApprovalStore({ canonicalRoot: input.canonicalRoot, storageRoot: join(context.privateDirectory, "approvals"), consent,
        isLive: async binding => (await context.admission.supervisor.inventory()).some(worker => worker.workerId === binding.turnId && worker.generation === binding.workerGeneration && worker.state === "running") });
      const delegated = new DelegatedRuntime({ daemonId: `hosted-${input.projectId}`, projects: new Map([[input.projectId, { identity: input.admission.continuity,
        compatibility: trusted.compatibility, supervisor: context.admission.supervisor, consent, retirement, approvals,
        approvalForwardingEnabled: trusted.commandNetworkPosture === "ask-per-destination", nativePlanSink: input.runtime.nativePlanSink,
        commandNetworkPosture: trusted.commandNetworkPosture, actual: { adapterId: "codex-app-server", providerId: "openai", model: context.model! }, evidenceClass: "provider-observed" as const }]]) });
      if (context.runtimeV2) {
        await revalidateRuntimeInstanceAdmissionV2(context.runtimeV2.instanceInput, context.runtimeV2.instanceAdmission);
        const finalProject = await input.runtime.projects.requireAuthorized(input.projectId), finalRoots = await input.runtime.projects.roots(input.projectId);
        if (finalProject.canonicalRoot !== context.canonicalRoot || finalProject.manifestHash !== context.manifestHash || finalRoots.workingRoot !== context.canonicalRoot || finalRoots.instructionRoot !== trusted.instructionRoot
          || closed || !lease.held || context.retired || context.signedOut || admissions.get(input.admission) !== context) throw unavailable("PROJECT_REGISTRATION_MISMATCH");
        await revalidateHostedAccountAuthorityV2(context.runtimeV2.instanceInput.hostAuthority, { purpose: "worker", projectId: context.projectId, manifestHash: context.manifestHash, canonicalRoot: context.canonicalRoot, account: context.runtimeV2.instanceInput.account, consentDigest: context.runtimeV2.instanceInput.consent.digest });
        if (closed || !lease.held || context.retired || context.signedOut || admissions.get(input.admission) !== context) throw unavailable("MATERIALIZATION_BINDING_INVALID");
      }
      context.materialized = delegated;
      return { delegated, selection: { adapterId: "codex-app-server", providerId: "openai", model: context.model! }, compatibility: { ...trusted.compatibility }, evidenceClass: "provider-observed" as const };
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
      let localFailure: unknown, fencedContinuity: Awaited<ReturnType<HostedIdentityBindingStore["fence"]>>;
      try { fencedContinuity = await context.store.fence("sign-out"); } catch (error) { localFailure = error; }
      try { await retire(context); } catch (error) { localFailure = localFailure === undefined ? error : new AggregateError([localFailure, error], "Hosted sign-out fence and retirement failed"); }
      if (localFailure !== undefined) throw localFailure;
      const stagedExecutable = context.stagedExecutable, attachmentRoot = join(input.canonicalRoot, ".chirality", "attachments");
      let logoutRuntimeV2: NonNullable<HostedCodexSupervisorOptions["runtimeV2"]> | undefined;
      let logoutOuter: Awaited<ReturnType<typeof prepareCodexTrustedSupplierContainmentV2>> | undefined;
      const policy = context.v2
        ? await prepareCodexNativePolicyV2({ purpose: "worker", canonicalRoot: input.canonicalRoot, privateDirectory: input.privateDirectory, codexHome: input.codexHome,
            executablePath: stagedExecutable, nativeAddonPath: trusted.nativeAddonPath, providerNetworkConsent: { approvedBy: context.providerNetworkConsent.approvedBy, approvalReference: context.providerNetworkConsent.approvalReference },
            commandNetworkPosture: "off", protectedPaths: [...trusted.protectedPaths], readOnlyProjectPaths: [attachmentRoot], immutableReadRoots: [...trusted.immutableReadRoots], trustedRuntimeReadRoots: [context.v2.runtimeReadRoot],
            nativeRoleConfiguration: context.nativeRoles, toolRuntime: { codexSelfExecutablePath: stagedExecutable, requiresSandboxedFileSystem: true, requiresSandboxedFileStreaming: true } })
        : await adapters.preparePolicy({ purpose: "worker", canonicalRoot: input.canonicalRoot, privateDirectory: input.privateDirectory, codexHome: input.codexHome,
            providerNetworkConsent: { approvedBy: context.providerNetworkConsent.approvedBy, approvalReference: context.providerNetworkConsent.approvalReference }, commandNetworkPosture: "off", protectedPaths: [...trusted.protectedPaths], immutableReadRoots: [...trusted.immutableReadRoots],
            trustedRuntimeReadRoots: [context.runtimeReadRoot], nativeRoleConfiguration: context.nativeRoles });
      let factory: CodexCandidateLauncherFactory | undefined, failure: unknown;
      try {
        if (context.v2 && trusted.releaseV2) {
          if (!fencedContinuity || !adapters.hostAuthority) throw unavailable("LOGOUT_FENCED_ACCOUNT_UNAVAILABLE");
          const account = { accountId: fencedContinuity.accountId, accountEpoch: fencedContinuity.accountEpoch, accountDigest: context.admission.accountDigest };
          const host = await adapters.hostAuthority({ purpose: "worker", projectId: context.projectId, manifestHash: context.manifestHash, canonicalRoot: context.canonicalRoot, account, consentDigest: context.v2.loginInput.consent.digest });
          if (!host.account || recordKey(host.account) !== recordKey(account)) throw unavailable("HOST_ACCOUNT_AUTHORITY_MISMATCH");
          await revalidateHostedAccountAuthorityV2(host.authority, { purpose: "worker", projectId: context.projectId, manifestHash: context.manifestHash, canonicalRoot: context.canonicalRoot, account, consentDigest: context.v2.loginInput.consent.digest });
          const purposeRelease = await verifyRuntimePurposeReleaseV2(trusted.releaseV2.basis, "worker");
          logoutOuter = await prepareCodexTrustedSupplierContainmentV2({ canonicalRoot: input.canonicalRoot, privateDirectory: input.privateDirectory, codexHome: input.codexHome,
            providerNetworkConsent: { approvedBy: context.providerNetworkConsent.approvedBy, approvalReference: context.providerNetworkConsent.approvalReference },
            trustedRuntimeReadRoots: [context.v2.runtimeReadRoot] });
          const effectiveConfigDigest = codexEffectiveConfigDigestV2({ executablePath: stagedExecutable, cwd: input.canonicalRoot,
            environment: { HOME: logoutOuter.environment.HOME, CODEX_HOME: logoutOuter.environment.CODEX_HOME, PATH: logoutOuter.environment.PATH, LANG: logoutOuter.environment.LANG }, configOverrides: (policy as Awaited<ReturnType<typeof prepareCodexNativePolicyV2>>).configOverrides });
          const instanceInput: RuntimeInstanceAdmissionInputV2 = { purposeRelease, hostAuthority: host.authority, projectId: context.projectId, manifestHash: context.manifestHash,
            canonicalRoot: context.canonicalRoot, cwd: context.canonicalRoot, privateDirectory: context.privateDirectory, codexHome: context.codexHome, brokerRoot: trusted.runtimeDirectory,
            instructionRoot: trusted.instructionRoot, nativeAddonPath: trusted.nativeAddonPath, supplierExecutablePath: stagedExecutable, attachmentRoot, account,
            consent: context.v2.loginInput.consent, policy: (policy as Awaited<ReturnType<typeof prepareCodexNativePolicyV2>>).policyInstance,
            outerPolicyDigest: logoutOuter.outerPolicyDigest, nativePolicyDigest: policy.policyDigest, effectiveConfigDigest };
          logoutRuntimeV2 = { releaseBasis: trusted.releaseV2.basis, instanceInput, instanceAdmission: await issueRuntimeInstanceAdmissionV2(instanceInput) };
        }
        factory = adapters.createLauncherFactory({ bindings: { canonicalRoot: input.canonicalRoot, privateDirectory: input.privateDirectory, codexHome: input.codexHome,
          executablePath: stagedExecutable, nativeAddonPath: trusted.nativeAddonPath, model: context.model!, providerNetworkConsent: { approvedBy: context.providerNetworkConsent.approvedBy, approvalReference: context.providerNetworkConsent.approvalReference },
          commandNetworkPosture: "off", protectedPaths: [...trusted.protectedPaths], readOnlyProjectPaths: [attachmentRoot], immutableReadRoots: [...trusted.immutableReadRoots], trustedRuntimeReadRoots: [context.v2?.runtimeReadRoot ?? context.runtimeReadRoot], policyDigest: policy.policyDigest,
          configDigest: context.configDigest, consentVersion: context.consentVersion, toolRuntime: { codexSelfExecutablePath: stagedExecutable }, nativeRoleConfiguration: context.nativeRoles,
          ...(context.v2 && logoutRuntimeV2 ? { policyInstanceV2: (policy as Awaited<ReturnType<typeof prepareCodexNativePolicyV2>>).policyInstance,
            expectedEffectiveConfigDigestV2: logoutRuntimeV2.instanceInput.effectiveConfigDigest, instanceInputV2: logoutRuntimeV2.instanceInput, instanceAdmissionV2: logoutRuntimeV2.instanceAdmission } : {}) }, kernelLease: lease });
        await adapters.logout(factory, context.admission.accountDigest, logoutRuntimeV2);
      } catch (error) { failure = error; }
      for (const cleanup of [() => factory?.close?.(), () => logoutOuter?.cleanup(), () => policy.cleanup()]) {
        try { await cleanup(); } catch (error) { failure = failure === undefined ? error : new AggregateError([failure, error], "Hosted sign-out and cleanup failed"); }
      }
      if (failure !== undefined) throw failure;
    },
    close() {
      return closing ??= (async () => { closed = true; let failure: unknown;
        for (const context of admissions.values()) try { await retire(context); } catch (error) { failure ??= error; }
        for (const context of ceremonies.values()) try { await context.ceremony.close(); } catch (error) { failure ??= error; }
        if (!failure) { ceremonies.clear(); admissions.clear(); try { if (lease.held) lease.close(); } catch (error) { failure = error; } }
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
