import { RuntimeError } from "@chirality/runtime-contracts";
import { isAbsolute, relative, resolve, sep } from "node:path";
import {
  launchAuthenticatedCodexCandidate,
  type AuthenticatedCodexCandidate,
  type AuthenticatedCodexCandidateInput
} from "./codex-authenticated-transport.js";
import { inspectCodexPolicyInstanceV2, prepareRuntimeWorkerInstanceV2FromP2, completeRuntimeWorkerInstanceV2FromP2, revalidateRuntimeInstanceAdmissionV2, type RuntimeInstanceAdmissionInputV2, type RuntimeInstanceAdmissionV2, type RuntimeWorkerInstancePreparationV2 } from "./runtime-conformance-v2-admission.js";
import { assertIssuedPackagedSupplyVerifierV2 } from "./hosted-packaged-release-state.js";

export type CodexAdmittedLauncherBindings = Omit<AuthenticatedCodexCandidateInput, "kernelLease"> & {
  model: string;
  configDigest: string;
  consentVersion: string;
};

export interface CodexCandidateLauncher {
  /** Starts one nonexecuting supplier candidate. The Supervisor owns private
   * authority, identity, conformance and operation admission on this transport. */
  launchCandidate(): Promise<AuthenticatedCodexCandidate>;
  close?(): Promise<void>;
}

export interface CodexCandidateLauncherFactory {
  refreshHostAdmission?(account: NonNullable<RuntimeInstanceAdmissionInputV2["account"]>): Promise<{ instanceInput: RuntimeInstanceAdmissionInputV2; instanceAdmission: RuntimeInstanceAdmissionV2 }>;
  create(): CodexCandidateLauncher;
  close?(): Promise<void>;
}

export interface CodexCandidateLauncherOptions {
  bindings: CodexAdmittedLauncherBindings;
  /** Borrowed from the Runtime authority owner and never closed here. */
  kernelLease: AuthenticatedCodexCandidateInput["kernelLease"];
}

export interface ControlledCodexCandidateLauncherAdapters {
  launchCandidate(input: AuthenticatedCodexCandidateInput): Promise<AuthenticatedCodexCandidate>;
}

const productionAdapters: ControlledCodexCandidateLauncherAdapters = Object.freeze({ launchCandidate: launchAuthenticatedCodexCandidate });
const HEX = /^[a-f0-9]{64}$/;

function unavailable(reason: string): RuntimeError {
  return new RuntimeError("ENGINE_UNAVAILABLE", "Codex supplier candidate launch is unavailable", 503, { reason });
}

function exactKeys(value: unknown, keys: readonly string[]): boolean {
  return Boolean(value) && typeof value === "object" && !Array.isArray(value)
    && Object.keys(value as Record<string, unknown>).sort().join("\0") === [...keys].sort().join("\0");
}

function frozenClone<T>(value: T): T {
  const clone = structuredClone(value);
  const freeze = (item: unknown): void => {
    if (!item || typeof item !== "object" || Object.isFrozen(item)) return;
    for (const nested of Object.values(item as Record<string, unknown>)) freeze(nested);
    Object.freeze(item);
  };
  freeze(clone);
  return clone;
}

function canonicalPath(value: unknown): value is string {
  return typeof value === "string" && isAbsolute(value) && resolve(value) === value && !/[\x00-\x1f]/.test(value);
}

function contained(parent: string, child: string): boolean {
  const path = relative(parent, child);
  return path.length > 0 && path !== ".." && !path.startsWith(`..${sep}`) && !isAbsolute(path);
}

function validateBindings(value: CodexAdmittedLauncherBindings): Readonly<CodexAdmittedLauncherBindings> {
  const keys = ["canonicalRoot", "privateDirectory", "codexHome", "executablePath", "nativeAddonPath", "model", "providerNetworkConsent", "commandNetworkPosture", "protectedPaths", "immutableReadRoots", "policyDigest", "configDigest", "consentVersion", "toolRuntime"];
  const optionalKeys = [...(value.supplyVerifier === undefined ? [] : ["supplyVerifier"]), ...(value.readOnlyProjectPaths === undefined ? [] : ["readOnlyProjectPaths"]), ...(value.trustedRuntimeReadRoots === undefined ? [] : ["trustedRuntimeReadRoots"]), ...(value.nativeRoleConfiguration === undefined ? [] : ["nativeRoleConfiguration"]), ...(value.policyInstanceV2 === undefined ? [] : ["policyInstanceV2"]), ...(value.expectedEffectiveConfigDigestV2 === undefined ? [] : ["expectedEffectiveConfigDigestV2"]), ...(value.instanceInputV2 === undefined ? [] : ["instanceInputV2"]), ...(value.instanceAdmissionV2 === undefined ? [] : ["instanceAdmissionV2"]), ...(value.instancePreparationV2 === undefined ? [] : ["instancePreparationV2"]), ...(value.nativePolicyIdentityVersion === undefined ? [] : ["nativePolicyIdentityVersion"])];
  if (!exactKeys(value, [...keys, ...optionalKeys])) throw unavailable("BINDINGS_INVALID");
  for (const path of [value.canonicalRoot, value.privateDirectory, value.codexHome, value.executablePath, value.nativeAddonPath]) if (!canonicalPath(path)) throw unavailable("BINDINGS_INVALID");
  if (!contained(value.privateDirectory, value.codexHome) || !contained(value.privateDirectory, value.executablePath)
    || contained(value.canonicalRoot, value.privateDirectory) || contained(value.privateDirectory, value.canonicalRoot)) throw unavailable("PRIVATE_ROOT_BINDING_INVALID");
  if (typeof value.model !== "string" || !value.model.trim() || value.model.length > 128 || /[\x00-\x1f]/.test(value.model)
    || !HEX.test(value.policyDigest) || !HEX.test(value.configDigest)
    || typeof value.consentVersion !== "string" || !value.consentVersion.trim() || value.consentVersion.length > 128
    || !["off", "ask-per-destination", "on"].includes(value.commandNetworkPosture)
    || !Array.isArray(value.protectedPaths) || value.protectedPaths.length === 0 || value.protectedPaths.some(path => !canonicalPath(path))
    || !Array.isArray(value.immutableReadRoots) || value.immutableReadRoots.length === 0 || value.immutableReadRoots.some(path => !canonicalPath(path))
    || (value.readOnlyProjectPaths !== undefined && (!Array.isArray(value.readOnlyProjectPaths) || value.readOnlyProjectPaths.some(path => !canonicalPath(path) || !contained(value.canonicalRoot, path))))
    || (value.trustedRuntimeReadRoots !== undefined && (!Array.isArray(value.trustedRuntimeReadRoots) || value.trustedRuntimeReadRoots.some(entry => !exactKeys(entry, ["path", "readPaths", "contentDigest", "artifactInventory"]) || !canonicalPath(entry.path) || !HEX.test(entry.contentDigest) || !Array.isArray(entry.readPaths) || entry.readPaths.length<1 || entry.readPaths.some((path:string)=>!canonicalPath(path))
      || !entry.artifactInventory || (entry.artifactInventory.kind === "source-tree" ? !exactKeys(entry.artifactInventory,["kind","sourceRoot"]) || !canonicalPath(entry.artifactInventory.sourceRoot)
        : entry.artifactInventory.kind === "packaged-resources" ? !exactKeys(entry.artifactInventory,["kind","resourcesRoot","manifestPath"]) || !canonicalPath(entry.artifactInventory.resourcesRoot) || !canonicalPath(entry.artifactInventory.manifestPath)
        : entry.artifactInventory.schema === "chirality-runtime-packaged-basis/v2" ? false : true))))
    || (value.nativeRoleConfiguration !== undefined && (!exactKeys(value.nativeRoleConfiguration, ["digest", "configOverrides"]) || !HEX.test(value.nativeRoleConfiguration.digest) || !Array.isArray(value.nativeRoleConfiguration.configOverrides)))) throw unavailable("BINDINGS_INVALID");
  if (!exactKeys(value.providerNetworkConsent, ["approvedBy", "approvalReference"])
    || typeof value.providerNetworkConsent.approvedBy !== "string" || !value.providerNetworkConsent.approvedBy.trim()
    || typeof value.providerNetworkConsent.approvalReference !== "string" || !value.providerNetworkConsent.approvalReference.trim()) throw unavailable("PROVIDER_CONSENT_INVALID");
  if (!exactKeys(value.toolRuntime, ["codexSelfExecutablePath"]) || value.toolRuntime.codexSelfExecutablePath !== value.executablePath) throw unavailable("TOOL_RUNTIME_BINDING_MISMATCH");
  if (value.supplyVerifier) assertIssuedPackagedSupplyVerifierV2(value.supplyVerifier);
  if (value.nativePolicyIdentityVersion !== undefined && ![10,11].includes(value.nativePolicyIdentityVersion)) throw unavailable("COMPILER_IDENTITY_INVALID");
  if (value.policyInstanceV2 !== undefined) {
    const policy = inspectCodexPolicyInstanceV2(value.policyInstanceV2);
    const hasInstanceInput = value.instanceInputV2 !== undefined;
    const hasInstanceAdmission = value.instanceAdmissionV2 !== undefined;
    const hasAdmission = hasInstanceInput && hasInstanceAdmission;
    const preparation = value.instancePreparationV2 as RuntimeWorkerInstancePreparationV2 | undefined;
    if (hasInstanceInput !== hasInstanceAdmission || hasAdmission === (preparation !== undefined) || !HEX.test(value.expectedEffectiveConfigDigestV2 ?? "") || policy.executablePath !== value.executablePath || policy.nativeAddonPath !== value.nativeAddonPath || policy.canonicalRoot !== value.canonicalRoot || policy.privateDirectory !== value.privateDirectory || policy.codexHome !== value.codexHome
      || policy.providerNetworkConsent.approvedBy !== value.providerNetworkConsent.approvedBy || policy.providerNetworkConsent.approvalReference !== value.providerNetworkConsent.approvalReference
      || policy.commandNetworkPosture !== value.commandNetworkPosture || JSON.stringify(policy.immutableReadRoots) !== JSON.stringify(value.immutableReadRoots)
      || JSON.stringify(policy.protectedPaths) !== JSON.stringify(value.protectedPaths) || JSON.stringify(policy.readOnlyProjectPaths) !== JSON.stringify(value.readOnlyProjectPaths ?? [])
      || JSON.stringify(policy.nativeRoleConfiguration) !== JSON.stringify(value.nativeRoleConfiguration ?? null)) throw unavailable("V2_POLICY_BINDING_MISMATCH");
  }
  const { supplyVerifier, instanceInputV2, instanceAdmissionV2, instancePreparationV2, ...data } = value;
  return Object.freeze({ ...frozenClone(data), ...(supplyVerifier ? { supplyVerifier } : {}), ...(instanceInputV2 ? { instanceInputV2, instanceAdmissionV2 } : {}), ...(instancePreparationV2 ? { instancePreparationV2 } : {}) });
}

function compose(options: CodexCandidateLauncherOptions, adapters: ControlledCodexCandidateLauncherAdapters, onSettled: () => void = () => {}): CodexCandidateLauncher {
  if (!options || !exactKeys(options, ["bindings", "kernelLease"]) || !options.kernelLease?.held || !adapters || typeof adapters.launchCandidate !== "function") throw unavailable("LAUNCHER_CONFIGURATION_INVALID");
  const bindings = validateBindings(options.bindings);
  const kernelLease = options.kernelLease;
  let candidate: AuthenticatedCodexCandidate | undefined;
  let launching: Promise<AuthenticatedCodexCandidate> | undefined;
  let attempted = false;
  let closed = false;
  let settled = false;
  const settle = (): void => {
    if (settled) return;
    settled = true;
    candidate = undefined;
    onSettled();
  };
  return Object.freeze({
    launchCandidate(): Promise<AuthenticatedCodexCandidate> {
      if (closed) return Promise.reject(unavailable("LAUNCHER_CLOSED"));
      if (attempted) return Promise.reject(unavailable("CANDIDATE_ALREADY_LAUNCHED"));
      attempted = true;
      launching = Promise.resolve().then(() => adapters.launchCandidate({ ...bindings, kernelLease })).then(value => {
        let closing: Promise<void> | undefined;
        const cleanup = (): Promise<void> => closing ??= (async () => {
          await value.cleanup();
          value.authorityInitialize.authoritySecret.fill(0);
          settle();
        })();
        candidate = Object.freeze({ ...value, transport: Object.freeze({ ...value.transport, close: cleanup }), cleanup });
        return candidate;
      }, error => { settle(); throw error; }).finally(() => { launching = undefined; });
      return launching;
    },
    async close(): Promise<void> {
      closed = true;
      const current = candidate ?? await launching?.catch(() => undefined);
      if (current) await current.cleanup();
      else settle();
    }
  });
}

function factory(options: CodexCandidateLauncherOptions, adapters: ControlledCodexCandidateLauncherAdapters): CodexCandidateLauncherFactory {
  if (!options || !exactKeys(options, ["bindings", "kernelLease"]) || !options.kernelLease?.held) throw unavailable("LAUNCHER_CONFIGURATION_INVALID");
  let bindings = validateBindings(options.bindings);
  const kernelLease = options.kernelLease;
  const launchers = new Set<CodexCandidateLauncher>();
  let closed = false;
  let refreshing = false;
  return Object.freeze({
    create(): CodexCandidateLauncher {
      if (closed || refreshing || !kernelLease.held) throw unavailable("LAUNCHER_FACTORY_CLOSED");
      let launcher!: CodexCandidateLauncher;
      launcher = compose({ bindings, kernelLease }, adapters, () => { launchers.delete(launcher); });
      launchers.add(launcher);
      return launcher;
    },
    async refreshHostAdmission(account: NonNullable<RuntimeInstanceAdmissionInputV2["account"]>) {
      if (closed || refreshing || !kernelLease.held || launchers.size) throw unavailable("LAUNCHER_FACTORY_NOT_IDLE");
      const previous = bindings.instancePreparationV2;
      if (!previous) throw unavailable("HOST_ADMISSION_REFRESH_UNAVAILABLE");
      refreshing = true;
      try {
        const next = await prepareRuntimeWorkerInstanceV2FromP2(previous.source, previous.releaseBasis, previous.input);
        if (next.lease.daemonGeneration !== previous.lease.daemonGeneration) throw unavailable("HOST_ADMISSION_DAEMON_CHANGED");
        const admission = await completeRuntimeWorkerInstanceV2FromP2(next, account);
        if (closed || !kernelLease.held || launchers.size) throw unavailable("LAUNCHER_FACTORY_NOT_IDLE");
        await revalidateRuntimeInstanceAdmissionV2(admission.instanceInput, admission.instanceAdmission);
        bindings = validateBindings({ ...bindings, instancePreparationV2: next });
        return admission;
      } finally { refreshing = false; }
    },
    async close(): Promise<void> {
      closed = true;
      const results = await Promise.allSettled([...launchers].map(launcher => launcher.close?.()));
      const failed = results.find(result => result.status === "rejected");
      if (failed?.status === "rejected") throw failed.reason;
    }
  });
}

export function createCodexCandidateLauncher(options: CodexCandidateLauncherOptions): CodexCandidateLauncher {
  return compose(options, productionAdapters);
}

export function createCodexCandidateLauncherFactory(options: CodexCandidateLauncherOptions): CodexCandidateLauncherFactory {
  return factory(options, productionAdapters);
}

/** Controlled transport seam; it never establishes production admission. */
export function createControlledCodexCandidateLauncherForTests(options: CodexCandidateLauncherOptions, adapters: ControlledCodexCandidateLauncherAdapters): CodexCandidateLauncher {
  return compose(options, Object.freeze({ ...adapters }));
}

export function createControlledCodexCandidateLauncherFactoryForTests(options: CodexCandidateLauncherOptions, adapters: ControlledCodexCandidateLauncherAdapters): CodexCandidateLauncherFactory {
  return factory(options, Object.freeze({ ...adapters }));
}
