import { randomBytes, randomUUID } from "node:crypto";
import {
  DescendantTracker,
  revalidateExactSupply,
  verifyExactSupply,
  type RuntimeAdmissionLease
} from "@chirality/runtime-core";
import { RuntimeError } from "@chirality/runtime-contracts";
import { loadNativeAdmissionBinding, type NativeGroupedSupplierChild, type NativeSupplierExit } from "@chirality/native-admission";
import {
  assertCodexKeyringHomeHasNoPlaintextCredentials,
  prepareCodexNativePolicy,
  prepareCodexTrustedSupplierContainment,
  type TrustedRuntimeReadRootBinding
} from "./codex-containment.js";
import type { CodexAuthorityInitialize, CodexSessionTransport } from "./codex-session.js";
import { HostedIdentityBindingStore } from "./hosted-identity-binding.js";
import { AUTHORITY_CONTRACT } from "./supplier-authority-controller.js";

export interface AuthenticatedCodexCandidateInput {
  canonicalRoot: string;
  privateDirectory: string;
  codexHome: string;
  executablePath: string;
  nativeAddonPath: string;
  providerNetworkConsent: { approvedBy: string; approvalReference: string };
  commandNetworkPosture: "off" | "ask-per-destination" | "on";
  protectedPaths: readonly string[];
  readOnlyProjectPaths?: readonly string[];
  immutableReadRoots: readonly string[];
  trustedRuntimeReadRoots?: readonly TrustedRuntimeReadRootBinding[];
  nativeRoleConfiguration?: { digest: string; configOverrides: readonly string[] };
  policyDigest: string;
  toolRuntime: { codexSelfExecutablePath: string };
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
  };
  expectedToolRuntime: {
    codexSelfExecutablePath: string;
    requiresSandboxedFileSystem: true;
    requiresSandboxedFileStreaming: true;
  };
  descendantTracker: DescendantTracker;
}

export interface ControlledAuthenticatedCodexCandidateAdapters {
  verifySupply(input: { executablePath: string }): Promise<Awaited<ReturnType<typeof verifyExactSupply>>>;
  revalidateSupply(supply: Awaited<ReturnType<typeof verifyExactSupply>>): Promise<unknown>;
  prepareOuter: typeof prepareCodexTrustedSupplierContainment;
  prepareToolPolicy: typeof prepareCodexNativePolicy;
  assertNoPlaintext(codexHome: string): Promise<void>;
  openBindingStore: typeof HostedIdentityBindingStore.open;
  loadNative: typeof loadNativeAdmissionBinding;
  randomBytes(size: number): Buffer;
  randomUUID(): string;
  retire(child: NativeGroupedSupplierChild): Promise<unknown>;
  createTracker(pid: number): DescendantTracker;
}

const productionAdapters: ControlledAuthenticatedCodexCandidateAdapters = Object.freeze({
  verifySupply: verifyExactSupply,
  revalidateSupply: revalidateExactSupply,
  prepareOuter: prepareCodexTrustedSupplierContainment,
  prepareToolPolicy: prepareCodexNativePolicy,
  assertNoPlaintext: assertCodexKeyringHomeHasNoPlaintextCredentials,
  openBindingStore: HostedIdentityBindingStore.open,
  loadNative: loadNativeAdmissionBinding,
  randomBytes,
  randomUUID,
  retire: retireAuthenticatedSupplierGroup,
  createTracker: (pid: number) => new DescendantTracker({ leaderPid: pid, maxDurationMs: 3_600_000 })
});

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
  const cleanup = () => closing ??= (async () => {
    let failure: unknown;
    for (const close of cleanups.splice(0).reverse()) {
      try { await close(); } catch (error) { failure ??= error; }
    }
    if (failure) throw failure;
  })();
  try {
    const supply = await adapters.verifySupply({ executablePath: input.executablePath });
    if (supply.version === "0.0.0") throw unavailable("DEVELOPMENT_SUPPLIER_BUILD");
    await adapters.assertNoPlaintext(input.codexHome);
    const outer = await adapters.prepareOuter({
      canonicalRoot: input.canonicalRoot,
      privateDirectory: input.privateDirectory,
      codexHome: input.codexHome,
      providerNetworkConsent: input.providerNetworkConsent,
      trustedRuntimeReadRoots: input.trustedRuntimeReadRoots === undefined ? undefined : structuredClone(input.trustedRuntimeReadRoots)
    });
    cleanups.push(outer.cleanup);
    const toolPolicy = await adapters.prepareToolPolicy({
      purpose: "worker",
      canonicalRoot: input.canonicalRoot,
      privateDirectory: input.privateDirectory,
      codexHome: input.codexHome,
      providerNetworkConsent: input.providerNetworkConsent,
      commandNetworkPosture: input.commandNetworkPosture,
      protectedPaths: [...input.protectedPaths],
      readOnlyProjectPaths: input.readOnlyProjectPaths === undefined ? undefined : [...input.readOnlyProjectPaths],
      immutableReadRoots: [...input.immutableReadRoots],
      trustedRuntimeReadRoots: input.trustedRuntimeReadRoots === undefined ? undefined : structuredClone(input.trustedRuntimeReadRoots),
      nativeRoleConfiguration: input.nativeRoleConfiguration === undefined ? undefined : {
        digest: input.nativeRoleConfiguration.digest,
        configOverrides: [...input.nativeRoleConfiguration.configOverrides]
      }
    });
    cleanups.push(toolPolicy.cleanup);
    if (toolPolicy.policyDigest !== input.policyDigest) throw unavailable("TOOL_POLICY_BINDING_MISMATCH");
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
    await adapters.revalidateSupply(supply);
    await adapters.assertNoPlaintext(input.codexHome);
    const environment = outer.environment;
    if (typeof environment.HOME !== "string" || typeof environment.CODEX_HOME !== "string" || typeof environment.TMPDIR !== "string" || typeof environment.PATH !== "string" || typeof environment.LANG !== "string") throw unavailable("SUPPLIER_ENVIRONMENT_INVALID");
    const spawned = native.value.spawnGroupedSupplier(
      "/usr/bin/sandbox-exec",
      [...launchArguments, "app-server", ...toolPolicy.args],
      authoritySecret,
      { cwd: input.canonicalRoot, environment: { HOME: environment.HOME, CODEX_HOME: environment.CODEX_HOME, TMPDIR: environment.TMPDIR, PATH: environment.PATH, LANG: environment.LANG }, processGroup: true }
    );
    if (spawned.state !== "available" || spawned.value.pid === undefined) throw unavailable("SUPPLIER_SPAWN_UNAVAILABLE");
    const child = spawned.value;
    const pid = child.pid;
    if (pid === undefined) throw unavailable("SUPPLIER_SPAWN_UNAVAILABLE");
    cleanups.push(async () => { const outcome=await adapters.retire(child);if(exposedCandidate&&isRetirementOutcome(outcome))retainedRetirementOutcomes.set(exposedCandidate,outcome); });
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
      expectedPolicy: Object.freeze({ permissionProfile: toolPolicy.permissionProfile, policyDigest: toolPolicy.policyDigest, expectedPermissions: toolPolicy.expectedPermissions, nativeRoleConfiguration: toolPolicy.nativeRoleConfiguration }),
      expectedToolRuntime: Object.freeze({ codexSelfExecutablePath: supply.executablePath, requiresSandboxedFileSystem: true, requiresSandboxedFileStreaming: true }),
      descendantTracker: adapters.createTracker(pid)
    });
    return exposedCandidate;
  } catch (error) {
    await cleanup().catch(() => {});
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
