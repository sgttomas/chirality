import { randomBytes, randomUUID } from "node:crypto";
import { lstat, realpath } from "node:fs/promises";
import { isAbsolute, relative, resolve, sep } from "node:path";
import {
  DescendantTracker,
  recordKey,
  runtimeStageCAppServerArguments,
  revalidateExactSupply,
  verifyExactSupply,
  type ExactSupplyVerifier,
  type RuntimeAdmissionLease
} from "@chirality/runtime-core";
import { RuntimeError } from "@chirality/runtime-contracts";
import { loadNativeAdmissionBinding, type NativeGroupedSupplierChild, type NativeSupplierExit } from "@chirality/native-admission";
import {
  assertCodexKeyringHomeHasNoPlaintextCredentials,
  prepareCodexNativePolicy,
  prepareCodexNativePolicyV2,
  prepareCodexTrustedSupplierContainment,
  prepareCodexTrustedSupplierContainmentV2,
  type TrustedRuntimeReadRootBindingV2,
  type TrustedRuntimeReadRootBinding
} from "./codex-containment.js";
import { revalidateHostedAccountAuthorityV2, revalidateRuntimeInstanceAdmissionV2, revalidateRuntimeWorkerInstancePreparationV2, type RuntimeInstanceAdmissionInputV2, type RuntimeInstanceAdmissionV2, type RuntimeWorkerInstancePreparationV2, type CodexPolicyInstanceV2 } from "./runtime-conformance-v2-admission.js";
import type { CodexAuthorityInitialize, CodexSessionTransport } from "./codex-session.js";
import { HostedIdentityBindingStore } from "./hosted-identity-binding.js";
import { AUTHORITY_CONTRACT } from "./supplier-authority-controller.js";
import { assertIssuedPackagedSupplyVerifierV2 } from "./hosted-packaged-release-state.js";

export interface AuthenticatedCodexCandidateInput {
  canonicalRoot: string;
  privateDirectory: string;
  codexHome: string;
  executablePath: string;
  supplyVerifier?: ExactSupplyVerifier;
  nativeAddonPath: string;
  providerNetworkConsent: { approvedBy: string; approvalReference: string };
  commandNetworkPosture: "off" | "ask-per-destination" | "on";
  protectedPaths: readonly string[];
  readOnlyProjectPaths?: readonly string[];
  immutableReadRoots: readonly string[];
  trustedRuntimeReadRoots?: readonly (TrustedRuntimeReadRootBinding | TrustedRuntimeReadRootBindingV2)[];
  nativeRoleConfiguration?: { digest: string; configOverrides: readonly string[] };
  policyDigest: string;
  toolRuntime: { codexSelfExecutablePath: string };
  /** Additive private v2 policy binding. Absence preserves the v1 candidate path. */
  policyInstanceV2?: CodexPolicyInstanceV2;
  expectedEffectiveConfigDigestV2?: string;
  instanceInputV2?: RuntimeInstanceAdmissionInputV2;
  instanceAdmissionV2?: RuntimeInstanceAdmissionV2;
  instancePreparationV2?: RuntimeWorkerInstancePreparationV2;
  nativePolicyIdentityVersion?: 10 | 11;
  /** Borrowed from the Runtime authority owner; candidate cleanup never closes it. */
  kernelLease: RuntimeAdmissionLease;
}

export interface AuthenticatedCodexCandidate {
  pid: number;
  transport: CodexSessionTransport;
  cleanup(): Promise<void>;
  authorityInitialize: CodexAuthorityInitialize;
  kernelLease: RuntimeAdmissionLease;
  supplierGeneration: string;
  privateBindingStore: HostedIdentityBindingStore;
  expectedPolicy: {
    permissionProfile: string;
    policyDigest: string;
    expectedPermissions: Awaited<ReturnType<typeof prepareCodexNativePolicy>>["expectedPermissions"];
    nativeRoleConfiguration: Awaited<ReturnType<typeof prepareCodexNativePolicy>>["nativeRoleConfiguration"];
    policyInstanceV2?: CodexPolicyInstanceV2;
    nativeSkills?: "disabled";
  };
  expectedToolRuntime: {
    codexSelfExecutablePath: string;
    requiresSandboxedFileSystem: true;
    requiresSandboxedFileStreaming: true;
  };
  expectedOuterPolicyDigest?: string;
  expectedEffectiveConfigDigestV2?: string;
  descendantTracker: DescendantTracker;
}

export interface ControlledAuthenticatedCodexCandidateAdapters {
  /** Test-only authority discriminator. Production always uses the packaged-basis issuance registry. */
  assertSupplyVerifier?: (verifier: ExactSupplyVerifier) => void;
  verifySupply(input: { executablePath: string }): Promise<Awaited<ReturnType<typeof verifyExactSupply>>>;
  revalidateSupply(supply: Awaited<ReturnType<typeof verifyExactSupply>>): Promise<unknown>;
  prepareOuter: typeof prepareCodexTrustedSupplierContainment;
  prepareToolPolicy: typeof prepareCodexNativePolicy;
  prepareOuterV2?: typeof prepareCodexTrustedSupplierContainmentV2;
  prepareToolPolicyV2?: typeof prepareCodexNativePolicyV2;
  assertCompiledPathV2?: typeof assertOwnedCompiledPathV2;
  assertNoPlaintext(codexHome: string): Promise<void>;
  openBindingStore: typeof HostedIdentityBindingStore.open;
  loadNative: typeof loadNativeAdmissionBinding;
  randomBytes(size: number): Buffer;
  randomUUID(): string;
  retire(child: NativeGroupedSupplierChild): Promise<unknown>;
  createTracker(pid: number): DescendantTracker;
}

const productionAdapters: ControlledAuthenticatedCodexCandidateAdapters = Object.freeze({
  assertSupplyVerifier: assertIssuedPackagedSupplyVerifierV2,
  verifySupply: verifyExactSupply,
  revalidateSupply: revalidateExactSupply,
  prepareOuter: prepareCodexTrustedSupplierContainment,
  prepareToolPolicy: prepareCodexNativePolicy,
  prepareOuterV2: prepareCodexTrustedSupplierContainmentV2,
  prepareToolPolicyV2: prepareCodexNativePolicyV2,
  assertCompiledPathV2: assertOwnedCompiledPathV2,
  assertNoPlaintext: assertCodexKeyringHomeHasNoPlaintextCredentials,
  openBindingStore: HostedIdentityBindingStore.open,
  loadNative: loadNativeAdmissionBinding,
  randomBytes,
  randomUUID,
  retire: retireAuthenticatedSupplierGroup,
  createTracker: (pid: number) => new DescendantTracker({ leaderPid: pid, maxDurationMs: 3_600_000 })
});

export function codexEffectiveConfigDigestV2(input: { executablePath: string; cwd: string; environment: { HOME: string; CODEX_HOME: string; PATH: string; LANG: string }; configOverrides: readonly string[]; nativePolicyIdentityVersion?: 10 | 11 }): string {
  return recordKey({ schema: "chirality-codex-effective-config/v2", executablePath: input.executablePath, cwd: input.cwd, environment: input.environment,
    appServerArgv: input.nativePolicyIdentityVersion===11?runtimeStageCAppServerArguments(input.configOverrides):["app-server", ...input.configOverrides.flatMap(value => ["-c", value])] });
}
export async function assertOwnedCompiledPathV2(parent: string, path: string, kind: "directory" | "file"): Promise<void> {
  const rel = relative(parent, path), info = await lstat(path);
  if (!isAbsolute(path) || resolve(path) !== path || rel === "" || rel === ".." || rel.startsWith(`..${sep}`) || isAbsolute(rel) || await realpath(path) !== path
    || info.uid !== (process.getuid?.() ?? -1) || (info.mode & 0o077) !== 0 || (kind === "directory" ? !info.isDirectory() : !info.isFile())) throw unavailable("COMPILED_PATH_CUSTODY_INVALID");
}

function unavailable(reason: string, cause?: unknown): RuntimeError {
  const error = new RuntimeError("ENGINE_UNAVAILABLE", "Authenticated Codex supplier candidate is unavailable", 503, { reason });
  if (cause !== undefined) error.cause = cause;
  return error;
}

/** Keeps the exited leader unreaped as the process-group identity anchor while
 * pre-reap signals are attempted, then requires exact reap and proven group
 * absence. Signal failures remain diagnostic; no signal is sent after reaping. */
export interface AuthenticatedSupplierRetirementOutcome {
  leader: Readonly<{ exitCode: number | null; signal: number | null }>;
  groupRetired: true;
  /** Failed pre-reap signal attempts remain available to the owning cleanup caller. */
  signalFailures: readonly Readonly<{ phase: "term" | "kill"; cause: unknown }>[];
}
const retainedRetirementOutcomes = new WeakMap<AuthenticatedCodexCandidate, AuthenticatedSupplierRetirementOutcome>();
function isRetirementOutcome(value: unknown): value is AuthenticatedSupplierRetirementOutcome {
  return Boolean(value) && typeof value === "object" && !Array.isArray(value)
    && (value as AuthenticatedSupplierRetirementOutcome).groupRetired === true
    && Array.isArray((value as AuthenticatedSupplierRetirementOutcome).signalFailures);
}
/** Package-internal lifecycle evidence; this module is absent from daemon export maps. */
export function authenticatedSupplierRetirementOutcome(candidate: AuthenticatedCodexCandidate): AuthenticatedSupplierRetirementOutcome | undefined {
  return retainedRetirementOutcomes.get(candidate);
}
export async function retireAuthenticatedSupplierGroup(
  child: NativeGroupedSupplierChild,
  deadline: (phase: "eof" | "term" | "kill" | "group") => Promise<void> = () => new Promise(resolve => setTimeout(resolve, 1000))
): Promise<AuthenticatedSupplierRetirementOutcome> {
  const observed = child.observeLeader();
  void observed.catch(() => {});
  child.closeInput();
  await deadline("eof");
  const signalFailures: Array<{ phase: "term" | "kill"; cause: unknown }> = [];
  try { child.terminate(); } catch (cause) { signalFailures.push({ phase: "term", cause }); }
  await deadline("term");
  try { child.kill(); } catch (cause) { signalFailures.push({ phase: "kill", cause }); }
  const retirementUnavailable = (reason: string, cause?: unknown) => {
    const error = new RuntimeError("ENGINE_UNAVAILABLE", "Authenticated Codex supplier candidate is unavailable", 503, { reason, signalFailures: signalFailures.map(failure => failure.phase) });
    const causes = [...signalFailures.map(failure => failure.cause), ...(cause === undefined ? [] : [cause])];
    if (causes.length) error.cause = new AggregateError(causes, "Authenticated supplier retirement operations failed");
    return error;
  };
  let leaderExited: boolean;
  try { leaderExited = await Promise.race([observed.then(() => true), deadline("kill").then(() => false)]); }
  catch (cause) { throw retirementUnavailable("SUPPLIER_LEADER_OBSERVATION_FAILED", cause); }
  if (!leaderExited) throw retirementUnavailable("SUPPLIER_LEADER_RETIREMENT_UNVERIFIED");
  const leader = await observed;
  let reaped: NativeSupplierExit;
  try { reaped = await child.reapLeader(); }
  catch (cause) { throw retirementUnavailable("SUPPLIER_LEADER_REAP_FAILED", cause); }
  if (reaped.exitCode !== leader.exitCode || reaped.signal !== leader.signal) throw retirementUnavailable("SUPPLIER_LEADER_REAP_MISMATCH");
  for (let attempt = 0; attempt < 5; attempt++) {
    let retired = false;
    try { retired = child.groupRetired(); }
    catch (cause) { throw retirementUnavailable("SUPPLIER_GROUP_RETIREMENT_UNVERIFIED", cause); }
    if (retired) return Object.freeze({ leader: Object.freeze({ ...leader }), groupRetired: true as const, signalFailures: Object.freeze(signalFailures.map(failure => Object.freeze({ ...failure }))) });
    await deadline("group");
  }
  throw retirementUnavailable("SUPPLIER_GROUP_RETIREMENT_UNVERIFIED");
}

async function compose(input: AuthenticatedCodexCandidateInput, adapters: ControlledAuthenticatedCodexCandidateAdapters): Promise<AuthenticatedCodexCandidate> {
  const cleanups: Array<() => Promise<void>> = [];
  let authoritySecret: Buffer | undefined;
  let closing: Promise<void> | undefined;
  let exposedCandidate: AuthenticatedCodexCandidate | undefined;
  let retirement: (() => Promise<void>) | undefined;
  let retainedPaths: string[] = [];
  const cleanup = () => closing ??= (async () => {
    const failures: unknown[] = [];
    if (retirement) {
      try { await retirement(); }
      catch (cause) {
        if (input.policyInstanceV2) throw unavailable("SUPPLIER_RETIREMENT_UNVERIFIED_RESOURCES_RETAINED", new AggregateError([cause, { retainedResources: retainedPaths }], "Supplier retirement failed; containment cleanup is unsafe"));
        failures.push(cause);
      }
    }
    for (const close of cleanups.splice(0).reverse()) {
      try { await close(); } catch (error) { failures.push(error); }
    }
    if (failures.length) throw new AggregateError(failures, "Supplier cleanup failed");
  })();
  try {
    if (input.policyInstanceV2) {
      const hasPreparation = input.instancePreparationV2 !== undefined;
      const hasInstanceInput = input.instanceInputV2 !== undefined;
      const hasInstanceAdmission = input.instanceAdmissionV2 !== undefined;
      const hasCompleteInstance = hasInstanceInput && hasInstanceAdmission;
      if (hasInstanceInput !== hasInstanceAdmission || hasPreparation === hasCompleteInstance) throw unavailable("INSTANCE_ADMISSION_INVALID");
      if (input.instancePreparationV2) await revalidateRuntimeWorkerInstancePreparationV2(input.instancePreparationV2);
      else {
        await revalidateRuntimeInstanceAdmissionV2(input.instanceInputV2!, input.instanceAdmissionV2!);
      }
    }
    if (input.supplyVerifier) (adapters.assertSupplyVerifier ?? assertIssuedPackagedSupplyVerifierV2)(input.supplyVerifier);
    const supply = input.supplyVerifier
      ? await input.supplyVerifier.verify({ executablePath: input.executablePath, custody: "private-staged" })
      : await adapters.verifySupply({ executablePath: input.executablePath });
    if (supply.version === "0.0.0") throw unavailable("DEVELOPMENT_SUPPLIER_BUILD");
    await adapters.assertNoPlaintext(input.codexHome);
    const outerInput = {
      canonicalRoot: input.canonicalRoot,
      privateDirectory: input.privateDirectory,
      codexHome: input.codexHome,
      providerNetworkConsent: input.providerNetworkConsent,
      trustedRuntimeReadRoots: input.policyInstanceV2 ? structuredClone(input.policyInstanceV2.trustedRuntimeReadRoots) : input.trustedRuntimeReadRoots === undefined ? undefined : structuredClone(input.trustedRuntimeReadRoots as readonly TrustedRuntimeReadRootBinding[])
    };
    const outer = input.policyInstanceV2
      ? await (adapters.prepareOuterV2 ?? (() => Promise.reject(unavailable("V2_OUTER_COMPILER_UNAVAILABLE"))))(outerInput as Parameters<typeof prepareCodexTrustedSupplierContainmentV2>[0])
      : await adapters.prepareOuter(outerInput as Parameters<typeof prepareCodexTrustedSupplierContainment>[0]);
    cleanups.push(outer.cleanup);
    const commonPolicy = {
      purpose: "worker" as const,
      canonicalRoot: input.canonicalRoot,
      privateDirectory: input.privateDirectory,
      codexHome: input.codexHome,
      providerNetworkConsent: input.providerNetworkConsent,
      commandNetworkPosture: input.commandNetworkPosture,
      protectedPaths: [...input.protectedPaths],
      readOnlyProjectPaths: input.readOnlyProjectPaths === undefined ? undefined : [...input.readOnlyProjectPaths],
      immutableReadRoots: [...input.immutableReadRoots],
      trustedRuntimeReadRoots: input.policyInstanceV2 ? undefined : input.trustedRuntimeReadRoots === undefined ? undefined : structuredClone(input.trustedRuntimeReadRoots as readonly TrustedRuntimeReadRootBinding[]),
      nativeRoleConfiguration: input.nativeRoleConfiguration === undefined ? undefined : {
        digest: input.nativeRoleConfiguration.digest,
        configOverrides: [...input.nativeRoleConfiguration.configOverrides]
      }
    };
    const toolPolicy = input.policyInstanceV2
      ? await (adapters.prepareToolPolicyV2 ?? (() => Promise.reject(unavailable("V2_NATIVE_COMPILER_UNAVAILABLE"))))({
          ...commonPolicy, executablePath: input.executablePath, nativeAddonPath: input.nativeAddonPath,
          nativePolicyIdentityVersion: input.nativePolicyIdentityVersion,
          trustedRuntimeReadRoots: input.policyInstanceV2.trustedRuntimeReadRoots as readonly TrustedRuntimeReadRootBindingV2[],
          toolRuntime: input.policyInstanceV2.toolRuntime
        })
      : await adapters.prepareToolPolicy(commonPolicy);
    cleanups.push(toolPolicy.cleanup);
    retainedPaths = [outer.environment.TMPDIR, ...(outer.sandboxProfilePath === null ? [] : [outer.sandboxProfilePath]), toolPolicy.scratchDirectory];
    if (toolPolicy.policyDigest !== input.policyDigest) throw unavailable("TOOL_POLICY_BINDING_MISMATCH");
    const compiledPolicyV2 = input.policyInstanceV2 ? (toolPolicy as Awaited<ReturnType<typeof prepareCodexNativePolicyV2>>).policyInstance : undefined;
    if (input.policyInstanceV2 && (!compiledPolicyV2 || recordKey(compiledPolicyV2) !== recordKey(input.policyInstanceV2))) throw unavailable("TOOL_POLICY_INSTANCE_MISMATCH");
    if (input.toolRuntime.codexSelfExecutablePath !== supply.executablePath) throw unavailable("TOOL_RUNTIME_BINDING_MISMATCH");

    const runtimeAuthorityId = adapters.randomUUID();
    const privateBindingStore = await adapters.openBindingStore({
      privateDirectory: input.privateDirectory,
      canonicalRoot: input.canonicalRoot,
      policyDigest: input.policyDigest,
      runtimeAuthorityId
    });
    const native = adapters.loadNative(true, input.nativeAddonPath);
    if (native.state !== "available") throw unavailable("NATIVE_ADMISSION_UNAVAILABLE");
    if (!input.kernelLease?.held) throw unavailable("KERNEL_LEASE_UNAVAILABLE");

    const supplierGeneration = adapters.randomUUID();
    authoritySecret = adapters.randomBytes(32);
    const authorityInitialize: CodexAuthorityInitialize = {
      runtimeProcessIncarnationId: runtimeAuthorityId,
      supplierGeneration,
      runtimeChallenge: adapters.randomBytes(32).toString("base64url"),
      exactSupplyDigest: supply.sha256,
      authoritySecret,
      descriptor: { capability: "chirality.local-admission-authority", contract: AUTHORITY_CONTRACT, major: 1, minor: 0 },
      v4Descriptor: { capability: "account.identity-snapshot", contract: "chirality-supplier-account-identity/1", major: 1, minor: 0, method: "account/identitySnapshot" }
    };
    const launchArguments = await outer.launchArguments(supply.executablePath);
    if (input.supplyVerifier) await input.supplyVerifier.revalidate(supply); else await adapters.revalidateSupply(supply as Awaited<ReturnType<typeof verifyExactSupply>>);
    await adapters.assertNoPlaintext(input.codexHome);
    const environment = outer.environment;
    if (typeof environment.HOME !== "string" || typeof environment.CODEX_HOME !== "string" || typeof environment.TMPDIR !== "string" || typeof environment.PATH !== "string" || typeof environment.LANG !== "string") throw unavailable("SUPPLIER_ENVIRONMENT_INVALID");
    const effectiveConfigDigestV2 = input.policyInstanceV2 ? codexEffectiveConfigDigestV2({ executablePath: supply.executablePath, cwd: input.canonicalRoot,
      environment: { HOME: environment.HOME, CODEX_HOME: environment.CODEX_HOME, PATH: environment.PATH, LANG: environment.LANG }, configOverrides: toolPolicy.configOverrides, nativePolicyIdentityVersion: input.nativePolicyIdentityVersion }) : undefined;
    if (input.policyInstanceV2 && effectiveConfigDigestV2 !== input.expectedEffectiveConfigDigestV2) throw unavailable("EFFECTIVE_CONFIG_BINDING_MISMATCH");
    if (input.policyInstanceV2) {
      const assertPath = adapters.assertCompiledPathV2 ?? assertOwnedCompiledPathV2;
      await assertPath(input.privateDirectory, environment.TMPDIR, "directory");
      if (outer.sandboxProfilePath !== null) await assertPath(environment.TMPDIR, outer.sandboxProfilePath, "file");
      await assertPath(input.canonicalRoot, (toolPolicy as Awaited<ReturnType<typeof prepareCodexNativePolicyV2>>).scratchDirectory, "directory");
    }
    const compilerArgs = toolPolicy.configOverrides.flatMap(value => ["-c", value]);
    const stageCPolicy = toolPolicy as Awaited<ReturnType<typeof prepareCodexNativePolicyV2>> & { nativeSkills?: "disabled"; appServerArguments?: readonly string[] };
    const appServerArguments = input.nativePolicyIdentityVersion === 11
      ? stageCPolicy.appServerArguments
      : ["app-server", ...(input.policyInstanceV2 ? compilerArgs : toolPolicy.args)];
    if (input.nativePolicyIdentityVersion === 11 && (stageCPolicy.nativeSkills !== "disabled"
      || JSON.stringify(appServerArguments) !== JSON.stringify(runtimeStageCAppServerArguments(toolPolicy.configOverrides)))) throw unavailable("COMPILED_INVOCATION_MISMATCH");
    if (input.policyInstanceV2) {
      // The v2 worker launches the verified supplier directly: its native Seatbelt is the containment.
      if (outer.launcher !== "direct" || outer.sandboxProfilePath !== null || JSON.stringify(launchArguments) !== JSON.stringify([supply.executablePath])
        || JSON.stringify(toolPolicy.args) !== JSON.stringify(compilerArgs)) throw unavailable("COMPILED_INVOCATION_MISMATCH");
      const expected = input.instanceInputV2 ?? input.instancePreparationV2?.input;
      if (!expected) throw unavailable("INSTANCE_ADMISSION_INVALID");
      if (outer.outerPolicyDigest !== expected.outerPolicyDigest || toolPolicy.policyDigest !== expected.nativePolicyDigest
        || effectiveConfigDigestV2 !== expected.effectiveConfigDigest || recordKey(compiledPolicyV2) !== recordKey(expected.policy)) throw unavailable("COMPILED_INSTANCE_MISMATCH");
      if (input.instancePreparationV2) await revalidateRuntimeWorkerInstancePreparationV2(input.instancePreparationV2);
      else await revalidateRuntimeInstanceAdmissionV2(input.instanceInputV2!, input.instanceAdmissionV2!);
      if (JSON.stringify(await outer.launchArguments(supply.executablePath)) !== JSON.stringify(launchArguments)) throw unavailable("COMPILED_INVOCATION_MISMATCH");
      await (toolPolicy as Awaited<ReturnType<typeof prepareCodexNativePolicyV2>>).revalidateScratch();
      if (input.instancePreparationV2) await revalidateRuntimeWorkerInstancePreparationV2(input.instancePreparationV2);
      else await revalidateHostedAccountAuthorityV2(input.instanceInputV2!.hostAuthority, { purpose: input.instanceInputV2!.purposeRelease.purpose, projectId: input.instanceInputV2!.projectId, manifestHash: input.instanceInputV2!.manifestHash, canonicalRoot: input.instanceInputV2!.canonicalRoot, account: input.instanceInputV2!.account, consentDigest: input.instanceInputV2!.consent.digest });
    }
    if (!input.kernelLease.held) throw unavailable("KERNEL_LEASE_UNAVAILABLE");
    const [launcherExecutable, ...launcherArguments] = outer.launcher === "direct" ? launchArguments : ["/usr/bin/sandbox-exec", ...launchArguments];
    if (typeof launcherExecutable !== "string" || (outer.launcher === "direct" && launcherExecutable !== supply.executablePath)) throw unavailable("COMPILED_INVOCATION_MISMATCH");
    const spawned = native.value.spawnGroupedSupplier(
      launcherExecutable,
      [...launcherArguments, ...appServerArguments!],
      authoritySecret,
      { cwd: input.canonicalRoot, environment: { HOME: environment.HOME, CODEX_HOME: environment.CODEX_HOME, TMPDIR: environment.TMPDIR, PATH: environment.PATH, LANG: environment.LANG }, processGroup: true }
    );
    if (spawned.state !== "available" || spawned.value.pid === undefined) throw unavailable("SUPPLIER_SPAWN_UNAVAILABLE");
    const child = spawned.value;
    const pid = child.pid;
    if (pid === undefined) throw unavailable("SUPPLIER_SPAWN_UNAVAILABLE");
    retirement = async () => { const outcome=await adapters.retire(child);if(exposedCandidate&&isRetirementOutcome(outcome))retainedRetirementOutcomes.set(exposedCandidate,outcome); };
    await adapters.assertNoPlaintext(input.codexHome);
    const transport: CodexSessionTransport = { stdin: child.stdin, stdout: child.stdout, close: cleanup };
    exposedCandidate = Object.freeze({
      pid,
      transport,
      cleanup,
      authorityInitialize,
      kernelLease: input.kernelLease,
      supplierGeneration,
      privateBindingStore,
      expectedPolicy: Object.freeze({ permissionProfile: toolPolicy.permissionProfile, policyDigest: toolPolicy.policyDigest, expectedPermissions: toolPolicy.expectedPermissions, nativeRoleConfiguration: toolPolicy.nativeRoleConfiguration,
        ...(input.nativePolicyIdentityVersion===11?{nativeSkills:"disabled" as const}:{}),
        ...(compiledPolicyV2 ? { policyInstanceV2: structuredClone(compiledPolicyV2) } : {}) }),
      expectedToolRuntime: Object.freeze({ codexSelfExecutablePath: supply.executablePath, requiresSandboxedFileSystem: true, requiresSandboxedFileStreaming: true }),
      expectedOuterPolicyDigest: outer.outerPolicyDigest,
      ...(effectiveConfigDigestV2 ? { expectedEffectiveConfigDigestV2: effectiveConfigDigestV2 } : {}),
      descendantTracker: adapters.createTracker(pid)
    });
    return exposedCandidate;
  } catch (error) {
    try { await cleanup(); } catch (cleanupError) { throw new AggregateError([error, cleanupError], "Candidate preparation and cleanup failed"); }
    authoritySecret?.fill(0);
    throw error instanceof RuntimeError ? error : unavailable("CANDIDATE_PREPARATION_FAILED", error);
  }
}

export function launchAuthenticatedCodexCandidate(input: AuthenticatedCodexCandidateInput): Promise<AuthenticatedCodexCandidate> {
  return compose(input, productionAdapters);
}

/** Controlled I/O seam; its values are never recognized as production qualification. */
export function launchControlledAuthenticatedCodexCandidateForTests(input: AuthenticatedCodexCandidateInput, adapters: ControlledAuthenticatedCodexCandidateAdapters): Promise<AuthenticatedCodexCandidate> {
  return compose(input, Object.freeze({ ...adapters }));
}
