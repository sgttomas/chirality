import { createHash, randomBytes, randomUUID } from "node:crypto";
import { constants } from "node:fs";
import { open, realpath } from "node:fs/promises";
import { spawn } from "node:child_process";
import { RuntimeError, hostedModelCatalog, validateHostedLoginStatus, type HostedLoginStatus, type HostedModelCatalog } from "@chirality/runtime-contracts";
import { computeRuntimeArtifactDigest, configureRuntimeConformanceArtifactInventory, isContained, privateDirectory, recordKey, revalidateExactSupply, runtimeConformanceArtifactInventory, runtimeStageCAppServerArguments, RuntimeConformanceFileAcceptancePort, verifyExactSupply, type ExactSupplyVerifier, type ExactVerifiedSupply, type RuntimeConformanceConfiguration } from "@chirality/runtime-core";
import { assertCodexKeyringHomeHasNoPlaintextCredentials, codexLoginConfigOverridesV2, prepareCodexContainment, prepareCodexContainmentV2 } from "./codex-containment.js";
import { CodexTurnSession, type CodexAuthorityInitialize, type CodexSessionTransport } from "./codex-session.js";
import { AUTHORITY_CONTRACT } from "./supplier-authority-controller.js";
import { revalidateHostedAccountAuthorityV2, revalidateRuntimeInstanceAdmissionV2, type RuntimeInstanceAdmissionInputV2, type RuntimeInstanceAdmissionV2 } from "./runtime-conformance-v2-admission.js";
import type { HostedPackagedReleaseBasisV2 } from "./hosted-packaged-release-state.js";
import { assertIssuedPackagedSupplyVerifierV2 } from "./hosted-packaged-release-state.js";
import { loadNativeAdmissionBinding } from "@chirality/native-admission";
import { assertOwnedCompiledPathV2, codexEffectiveConfigDigestV2, retireAuthenticatedSupplierGroup, type AuthenticatedSupplierRetirementOutcome } from "./codex-authenticated-transport.js";

const CODEX_LOGIN_V1_CONFIG_OVERRIDES = Object.freeze(['cli_auth_credentials_store="keyring"', "features.plugins=false", "allow_login_shell=false", 'approval_policy="never"', "check_for_update_on_startup=false", "analytics.enabled=false", "feedback.enabled=false"] as const);

export interface CodexLoginOptions {
  executablePath: string; canonicalRoot: string; codexHome: string; privateDirectory: string;
  /** Trusted operator provenance, never populated from client request fields. */
  providerNetworkConsent: { approvedBy: string; approvalReference: string };
  purposeRelease?: RuntimeConformanceConfiguration;
  startupAdmission?: CodexLoginStartupAdmission;
  /** @deprecated Temporary private-composition source compatibility. */
  purposeAdmission?: CodexLoginStartupAdmission;
  releaseV2?: Readonly<HostedPackagedReleaseBasisV2>;
  supplyVerifier?: ExactSupplyVerifier;
  instanceV2?: RuntimeInstanceAdmissionInputV2;
  instanceAdmissionV2?: RuntimeInstanceAdmissionV2;
  timeoutMs?: number;
}
export interface CodexLoginStartupAdmission {
  readonly bindingDigest: string;
  readonly evidence: "externally-accepted-native-login-purpose";
  readonly recordSha256: string;
  readonly ownerReference: string;
  readonly instanceAdmissionV2?: RuntimeInstanceAdmissionV2;
}
const loginAdmissions = new WeakSet<object>();
function supplyOperations(options: Pick<CodexLoginOptions, "supplyVerifier">): { verify(input: { executablePath: string; custody?: "packaged" | "private-staged" }): Promise<ExactVerifiedSupply>; revalidate(value: ExactVerifiedSupply): Promise<unknown> } {
  if (!options.supplyVerifier) return { verify: verifyExactSupply, revalidate: value => revalidateExactSupply(value as Awaited<ReturnType<typeof verifyExactSupply>>) };
  assertIssuedPackagedSupplyVerifierV2(options.supplyVerifier); return options.supplyVerifier;
}
function loginBinding(options: Omit<CodexLoginOptions, "timeoutMs" | "startupAdmission" | "purposeRelease" | "releaseV2" | "supplyVerifier" | "instanceV2" | "instanceAdmissionV2">, supplySha256: string, outerPolicyDigest: string): string {
  return recordKey({ purpose: "trusted-login", ...options, supplySha256, outerPolicyDigest });
}
const LOGIN_LIMBS = Object.freeze(["exact-supplier", "keyring-backend", "plaintext-fallback-absent", "process-containment", "storage-isolation", "provider-network", "bounded-protocol-purpose", "retirement"] as const);
export const CODEX_LOGIN_PURPOSE_GATE_IDENTITY = "D36" as const;
export type CodexLoginPurposeReleaseLimb = typeof LOGIN_LIMBS[number];
export interface CodexLoginPurposeReleaseRecord {
  schema: "chirality-codex-login-purpose-release/v1";
  evidenceClass: "exact-login-purpose-observed";
  bindings: { bindingDigest:string; outerPolicyDigest:string; sourceDigest:string; packageDigest:string; activationId:string; gateIdentity:string; consentDigest:string };
  supply: { sha256:string; size:number; version:string };
  backend: { credentialStore:"keyring"; plaintextFallback:false };
  purpose: { modelExecution:false; methods: readonly ["account/login/start","account/login/cancel","account/read"] };
  issuedAt:string; expiresAt:string;
  limbs: Record<CodexLoginPurposeReleaseLimb,{attempted:true;passed:true;evidenceSha256:string}>;
}
function exactKeys(value: unknown, keys: readonly string[]): value is Record<string, unknown> {
  return Boolean(value) && typeof value === "object" && !Array.isArray(value) && Object.keys(value as Record<string, unknown>).sort().join("\0") === [...keys].sort().join("\0");
}
function digest(value: unknown): value is string { return typeof value === "string" && /^[a-f0-9]{64}$/.test(value); }
export function inspectCodexLoginPurposeReleaseRecord(record: unknown, expected: CodexLoginPurposeReleaseRecord["bindings"] & {supply:CodexLoginPurposeReleaseRecord["supply"]}, now=Date.now()): Readonly<CodexLoginPurposeReleaseRecord> {
  if (expected.gateIdentity !== CODEX_LOGIN_PURPOSE_GATE_IDENTITY) throw unavailable("Login purpose release gate is invalid");
  if (!exactKeys(record, ["schema","evidenceClass","bindings","supply","backend","purpose","issuedAt","expiresAt","limbs"]) || record.schema !== "chirality-codex-login-purpose-release/v1" || record.evidenceClass !== "exact-login-purpose-observed") throw unavailable("Login purpose release record is invalid");
  if (!exactKeys(record.bindings, Object.keys(expected).filter(key=>key!=="supply"))) throw unavailable("Login purpose release binding differs from startup");
  const bindings=record.bindings;
  if (Object.entries(expected).some(([key,value])=>key!=="supply"&&bindings[key]!==value)) throw unavailable("Login purpose release binding differs from startup");
  if (!exactKeys(record.supply,["sha256","size","version"])) throw unavailable("Login purpose release supply differs from startup");
  const observedSupply=record.supply;
  if (Object.entries(expected.supply).some(([key,value])=>observedSupply[key]!==value)) throw unavailable("Login purpose release supply differs from startup");
  if (!exactKeys(record.backend,["credentialStore","plaintextFallback"]) || record.backend.credentialStore!=="keyring" || record.backend.plaintextFallback!==false) throw unavailable("Login purpose backend is not accepted");
  if (!exactKeys(record.purpose,["modelExecution","methods"]) || record.purpose.modelExecution!==false || JSON.stringify(record.purpose.methods)!==JSON.stringify(["account/login/start","account/login/cancel","account/read"])) throw unavailable("Login purpose protocol is not bounded");
  const issuedAt=Date.parse(String(record.issuedAt)),expiresAt=Date.parse(String(record.expiresAt));
  if (!Number.isFinite(now)||!Number.isFinite(issuedAt)||!Number.isFinite(expiresAt)||issuedAt>now||expiresAt<=now||expiresAt<=issuedAt) throw unavailable("Login purpose release is stale");
  if (!exactKeys(record.limbs,LOGIN_LIMBS)) throw unavailable("Login purpose release evidence is incomplete");
  const limbs=record.limbs;
  if(LOGIN_LIMBS.some(name=>{const limb=limbs[name];return !exactKeys(limb,["attempted","passed","evidenceSha256"])||limb.attempted!==true||limb.passed!==true||!digest(limb.evidenceSha256);}))throw unavailable("Login purpose release evidence is incomplete");
  return Object.freeze(structuredClone(record)) as Readonly<CodexLoginPurposeReleaseRecord>;
}
async function readPrivateReleaseRecord(path: string): Promise<{bytes:Buffer;sha256:string}> {
  if (await realpath(path) !== path) throw unavailable("Login purpose release record is unavailable");
  const file = await open(path, constants.O_RDONLY | constants.O_NOFOLLOW | constants.O_NONBLOCK);
  try {
    const before = await file.stat({ bigint:true });
    if (!before.isFile() || before.size > 1_048_576n || before.uid !== BigInt(process.getuid?.() ?? -1) || (before.mode & 0o777n) !== 0o600n || before.nlink !== 1n) throw unavailable("Login purpose release record is unavailable");
    const parts:Buffer[]=[];let total=0,position=0;const buffer=Buffer.alloc(65_536);
    for(;;){const {bytesRead}=await file.read(buffer,0,Math.min(buffer.length,1_048_577-total),position);if(!bytesRead)break;total+=bytesRead;position+=bytesRead;if(total>1_048_576)throw unavailable("Login purpose release record is unavailable");parts.push(Buffer.from(buffer.subarray(0,bytesRead)));}
    const after=await file.stat({bigint:true}),current=await open(path,constants.O_RDONLY|constants.O_NOFOLLOW|constants.O_NONBLOCK);
    try { const pathInfo=await current.stat({bigint:true});for(const key of ["dev","ino","size","mtimeNs","ctimeNs","mode","uid","nlink"] as const)if(before[key]!==after[key]||before[key]!==pathInfo[key])throw unavailable("Login purpose release record changed"); }
    finally { await current.close(); }
    if(BigInt(total)!==before.size||await realpath(path)!==path)throw unavailable("Login purpose release record changed");
    const bytes=Buffer.concat(parts,total);return {bytes,sha256:createHash("sha256").update(bytes).digest("hex")};
  }
  finally { await file.close(); }
}
/** Validates startup inputs and consumes independently accepted, account-free native-purpose evidence. It executes no login or account request. */
export async function validateCodexLoginStartup(options: Omit<CodexLoginOptions, "timeoutMs" | "startupAdmission">): Promise<CodexLoginStartupAdmission> {
  if (process.platform !== "darwin" || process.arch !== "arm64") throw unavailable("Exact login requires darwin-arm64");
  if (options.supplyVerifier) assertIssuedPackagedSupplyVerifierV2(options.supplyVerifier);
  const consent = options.providerNetworkConsent;
  if (!consent?.approvedBy?.trim() || !consent.approvalReference?.trim()) throw unavailable("Explicit trusted provider consent is required for sign-in");
  if (!isContained(options.privateDirectory, options.codexHome) || options.privateDirectory === options.codexHome || !isContained(options.privateDirectory, options.executablePath)) throw unavailable("Login home and exact executable must be inside the dedicated private directory");
  await privateDirectory(options.privateDirectory); await privateDirectory(options.codexHome);
  await assertCodexKeyringHomeHasNoPlaintextCredentials(options.codexHome);
  const { purposeRelease, releaseV2, supplyVerifier: _supplyVerifier, instanceV2, instanceAdmissionV2, ...startup } = options;
  if ([releaseV2, instanceV2, instanceAdmissionV2].some(value => value !== undefined)) {
    if (!releaseV2 || !instanceV2 || !instanceAdmissionV2 || instanceV2.purposeRelease.purpose !== "login" || instanceV2.account !== null) throw unavailable("Complete v2 login admission is required");
    const supplyOps = supplyOperations(options), supply = await supplyOps.verify({ executablePath: options.executablePath, ...(options.supplyVerifier ? { custody: "private-staged" as const } : {}) });
    if (supply.sha256 !== releaseV2.supportProfile.supplier.sha256 || Number(supply.identity.size) !== releaseV2.supportProfile.supplier.size || supply.version !== releaseV2.supportProfile.supplier.version) throw unavailable("Login supply differs from v2 release profile");
    const containment = await prepareCodexContainmentV2({ ...startup, purpose: "trusted-login" });
    try {
      if (containment.launcher !== "outer-seatbelt" || containment.sandboxProfilePath === null) throw unavailable("Login requires the outer containment profile");
      await assertOwnedCompiledPathV2(options.privateDirectory, containment.environment.TMPDIR, "directory");
      await assertOwnedCompiledPathV2(containment.environment.TMPDIR, containment.sandboxProfilePath, "file");
      const effectiveConfigDigest = codexEffectiveConfigDigestV2({ executablePath: supply.executablePath, cwd: options.canonicalRoot,
        environment: { HOME: containment.environment.HOME, CODEX_HOME: containment.environment.CODEX_HOME, PATH: containment.environment.PATH, LANG: containment.environment.LANG }, configOverrides: codexLoginConfigOverridesV2(containment.config), nativePolicyIdentityVersion: releaseV2!.supportProfile.compiler.nativePolicyIdentityVersion });
      if (containment.outerPolicyDigest !== instanceV2.outerPolicyDigest || effectiveConfigDigest !== instanceV2.effectiveConfigDigest) throw unavailable("Login compiled policy differs from v2 admission");
      await revalidateRuntimeInstanceAdmissionV2(instanceV2, instanceAdmissionV2); await supplyOps.revalidate(supply);
      const result = Object.freeze({ bindingDigest: instanceV2.outerPolicyDigest, evidence: "externally-accepted-native-login-purpose" as const, recordSha256: releaseV2.login.recordSha256,
        ownerReference: instanceV2.purposeRelease.ownerReference, instanceAdmissionV2 });
      loginAdmissions.add(result); return result;
    } finally { await containment.cleanup(); }
  }
  if (!purposeRelease || purposeRelease.gateIdentity !== CODEX_LOGIN_PURPOSE_GATE_IDENTITY) throw unavailable("Externally accepted D36 login purpose release evidence is required");
  const supply = await verifyExactSupply({ executablePath: options.executablePath });
  if (supply.version === "0.0.0") throw unavailable("Development supplier cannot qualify trusted login");
    const containment = await prepareCodexContainment({ ...startup, purpose: "trusted-login" });
  try {
    await containment.launchArguments(supply.executablePath); await revalidateExactSupply(supply);
    configureRuntimeConformanceArtifactInventory(purposeRelease.artifactInventory);
    const inventory = await runtimeConformanceArtifactInventory(purposeRelease.artifactInventory);
    const sourceDigest = await computeRuntimeArtifactDigest(inventory.sourceFiles);
    const packageDigest = await computeRuntimeArtifactDigest(inventory.packageFiles, inventory.dependencyResolutionDigest);
    const bindingDigest = loginBinding(startup, supply.sha256, containment.outerPolicyDigest);
    const source = await readPrivateReleaseRecord(purposeRelease.recordPath), expectedBindings = { bindingDigest, outerPolicyDigest:containment.outerPolicyDigest, sourceDigest, packageDigest, activationId:purposeRelease.activationId, gateIdentity:purposeRelease.gateIdentity, consentDigest:recordKey(startup.providerNetworkConsent) };
    inspectCodexLoginPurposeReleaseRecord(JSON.parse(source.bytes.toString("utf8")),{...expectedBindings,supply:{sha256:supply.sha256,size:Number(supply.identity.size),version:supply.version}});
    const acceptance = new RuntimeConformanceFileAcceptancePort(purposeRelease);
    const accepted = await acceptance.lookup({recordSha256:source.sha256,sourceDigest,activationId:purposeRelease.activationId,gateIdentity:purposeRelease.gateIdentity});
    if (accepted.status !== "accepted" || typeof accepted.ownerReference !== "string" || !accepted.ownerReference.trim()) throw unavailable("Login purpose release is not externally accepted");
    await revalidateExactSupply(supply);
    const current = await readPrivateReleaseRecord(purposeRelease.recordPath), currentAcceptance = await acceptance.lookup({recordSha256:source.sha256,sourceDigest,activationId:purposeRelease.activationId,gateIdentity:purposeRelease.gateIdentity});
    if (current.sha256 !== source.sha256 || currentAcceptance.status !== "accepted" || currentAcceptance.ownerReference !== accepted.ownerReference) throw unavailable("Login purpose release changed during validation");
    const result = Object.freeze({ bindingDigest, evidence: "externally-accepted-native-login-purpose" as const, recordSha256:source.sha256, ownerReference:accepted.ownerReference });
    loginAdmissions.add(result); return result;
  }
  finally { await containment.cleanup(); }
}
/** @deprecated Use validateCodexLoginStartup; this alias carries no qualification by itself. */
export const qualifyCodexLoginPurpose = validateCodexLoginStartup;
/** @deprecated Use CodexLoginStartupAdmission. */
export type CodexLoginPurposeAdmission = CodexLoginStartupAdmission;
export type CodexLoginStatus = HostedLoginStatus;
const unavailable = (message: string) => new RuntimeError("ENGINE_UNAVAILABLE", message, 503);
/** Sanitized pre-reap signal diagnostic from a verified group retirement; never a failure by itself. */
export interface CodexLoginCloseDiagnostic { readonly phase: "term" | "kill"; readonly message: string }
/** Login transport whose close may expose retirement diagnostics after it settles. */
export type CodexLoginTransport = CodexSessionTransport & { diagnostics?(): readonly CodexLoginCloseDiagnostic[] };
const diagnosticText = (value: unknown) => (value instanceof Error ? value.message : String(value ?? "")).replace(/[\x00-\x1f\x7f]/g, " ").slice(0, 200);
/** Memoized grouped-login close. A verified retirement (leader exited, reaped, group retired) with failed pre-reap signals
 * resolves and keeps those signals as diagnostics; only unproven retirement or a failed containment cleanup rejects. */
export function createGroupedLoginRetirement(input: { retire(): Promise<AuthenticatedSupplierRetirementOutcome>; cleanup(): Promise<void>; retainedResources: readonly string[]; pid?: number }): { close(): Promise<void>; diagnostics(): readonly CodexLoginCloseDiagnostic[] } {
  let closing: Promise<void> | undefined, diagnostics: readonly CodexLoginCloseDiagnostic[] = Object.freeze([]);
  const retained = { retainedResources: [...input.retainedResources], ...(input.pid === undefined ? {} : { pid: input.pid }) };
  const close = () => closing ??= (async () => {
    let outcome: AuthenticatedSupplierRetirementOutcome;
    try { outcome = await input.retire(); }
    catch (cause) {
      const error = new RuntimeError("ENGINE_UNAVAILABLE", "Login group retirement is unproven; containment allocation retained", 503, { reason: "LOGIN_RETIREMENT_UNVERIFIED", ...retained });
      error.cause = new AggregateError([cause], "Login retirement failed; cleanup is unsafe"); throw error;
    }
    diagnostics = Object.freeze(outcome.signalFailures.map(failure => Object.freeze({ phase: failure.phase, message: diagnosticText(failure.cause) })));
    try { await input.cleanup(); }
    catch (cause) {
      const error = new RuntimeError("ENGINE_UNAVAILABLE", "Login containment cleanup failed; allocation retained", 503, { reason: "LOGIN_CLEANUP_FAILED", ...retained, signalFailures: diagnostics.map(value => value.phase) });
      error.cause = new AggregateError([cause, ...outcome.signalFailures.map(failure => failure.cause)], "Login retirement and cleanup diagnostics"); throw error;
    }
  })();
  return { close, diagnostics: () => diagnostics };
}
/** Operator-only, explicit-consent sign-in lifecycle; construction performs no login. */
export class CodexLogin {
  private actor: CodexTurnSession | undefined;
  private fixture: CodexLoginTransport | undefined;
  private transport: CodexLoginTransport | undefined;
  private started = false;
  private closed = false;
  private expired = false;
  private cancelled = false;
  private timer: ReturnType<typeof setTimeout> | undefined;
  private closeFailure: unknown;
  private result: CodexLoginStatus | undefined;
  private selectedModel: Readonly<{ model: string; defaultReasoningEffort: string }> | undefined;
  private modelCatalog: Readonly<HostedModelCatalog> | undefined;
  private retainAuthenticatedSessionForModelCatalog = false;
  private authorityInitialize: CodexAuthorityInitialize | undefined;
  private controlledNativeSkills: "disabled" | undefined;
  constructor(private readonly options: CodexLoginOptions) {
    const timeout = options.timeoutMs ?? 300000;
    if (!Number.isSafeInteger(timeout) || timeout < 1 || timeout > 900000) throw unavailable("Invalid bounded login timeout");
    if (options.supplyVerifier) assertIssuedPackagedSupplyVerifierV2(options.supplyVerifier);
  }
  /** Explicit fixture seam, never emits exact-supply-login evidence. */
  static controlledForTests(input: { transport: CodexLoginTransport; codexHome: string; canonicalRoot?: string; timeoutMs?: number; retainAuthenticatedSessionForModelCatalog?: boolean; nativeSkills?: "disabled"; authorityInitialize?: CodexAuthorityInitialize }): CodexLogin {
    const instance = new CodexLogin({ executablePath: "", canonicalRoot: input.canonicalRoot ?? "", privateDirectory: "", codexHome: input.codexHome, providerNetworkConsent: { approvedBy: "", approvalReference: "" }, timeoutMs: input.timeoutMs });
    instance.fixture = input.transport; instance.retainAuthenticatedSessionForModelCatalog = input.retainAuthenticatedSessionForModelCatalog === true;
    instance.controlledNativeSkills=input.nativeSkills;instance.authorityInitialize=input.authorityInitialize;return instance;
  }
  private get evidenceClass(): CodexLoginStatus["evidenceClass"] { return this.fixture ? "controlled-fixture" : "exact-supply-login"; }
  private async launch(): Promise<CodexLoginTransport> {
    if (this.fixture) return this.fixture;
    if (process.platform !== "darwin" || process.arch !== "arm64") throw unavailable("Exact login requires darwin-arm64");
    const consent = this.options.providerNetworkConsent;
    if (!consent || typeof consent.approvedBy !== "string" || !consent.approvedBy.trim() || typeof consent.approvalReference !== "string" || !consent.approvalReference.trim()) throw unavailable("Explicit trusted provider consent is required for sign-in");
    if (!isContained(this.options.privateDirectory, this.options.codexHome) || this.options.privateDirectory === this.options.codexHome || !isContained(this.options.privateDirectory, this.options.executablePath)) throw unavailable("Login home and exact executable must be inside the dedicated private directory");
    await privateDirectory(this.options.privateDirectory); await privateDirectory(this.options.codexHome);
    await assertCodexKeyringHomeHasNoPlaintextCredentials(this.options.codexHome);
    const supplyOps = supplyOperations(this.options), supply = await supplyOps.verify({ executablePath: this.options.executablePath, ...(this.options.supplyVerifier ? { custody: "private-staged" as const } : {}) });
    const containment = this.options.instanceV2
      ? await prepareCodexContainmentV2({ canonicalRoot: this.options.canonicalRoot, privateDirectory: this.options.privateDirectory, codexHome: this.options.codexHome, providerNetworkConsent: consent, purpose: "trusted-login" })
      : await prepareCodexContainment({ canonicalRoot: this.options.canonicalRoot, privateDirectory: this.options.privateDirectory, codexHome: this.options.codexHome, providerNetworkConsent: consent, purpose: "trusted-login" });
    try {
      await this.requireQualifiedLoginPurpose(supply.sha256, containment.outerPolicyDigest);
      const args = await containment.launchArguments(supply.executablePath);
      await supplyOps.revalidate(supply);
      const configOverrides = this.options.instanceV2 ? codexLoginConfigOverridesV2(containment.config) : CODEX_LOGIN_V1_CONFIG_OVERRIDES;
      const flags = configOverrides.flatMap(value => ["-c", value]);
      if (this.options.instanceV2) {
        if (containment.launcher !== "outer-seatbelt" || containment.sandboxProfilePath === null) throw unavailable("Login requires the outer containment profile");
        await assertOwnedCompiledPathV2(this.options.privateDirectory, containment.environment.TMPDIR, "directory");
        await assertOwnedCompiledPathV2(containment.environment.TMPDIR, containment.sandboxProfilePath, "file");
        if (JSON.stringify(args) !== JSON.stringify(["-f", containment.sandboxProfilePath, supply.executablePath])) throw unavailable("Login outer invocation changed");
        const effectiveConfigDigest = codexEffectiveConfigDigestV2({ executablePath: supply.executablePath, cwd: this.options.canonicalRoot,
          environment: { HOME: containment.environment.HOME, CODEX_HOME: containment.environment.CODEX_HOME, PATH: containment.environment.PATH, LANG: containment.environment.LANG }, configOverrides: codexLoginConfigOverridesV2(containment.config), nativePolicyIdentityVersion: this.options.releaseV2!.supportProfile.compiler.nativePolicyIdentityVersion });
        if (containment.outerPolicyDigest !== this.options.instanceV2.outerPolicyDigest || effectiveConfigDigest !== this.options.instanceV2.effectiveConfigDigest) throw unavailable("Login effective configuration changed");
        const native = loadNativeAdmissionBinding(true, this.options.instanceV2.nativeAddonPath);
        if (native.state !== "available") throw unavailable("Native grouped login lifecycle unavailable");
        await revalidateRuntimeInstanceAdmissionV2(this.options.instanceV2, this.options.instanceAdmissionV2!);
        if (JSON.stringify(await containment.launchArguments(supply.executablePath)) !== JSON.stringify(args)) throw unavailable("Login outer invocation changed");
        const current = this.options.instanceV2;
        await revalidateHostedAccountAuthorityV2(current.hostAuthority, { purpose: "login", projectId: current.projectId, manifestHash: current.manifestHash, canonicalRoot: current.canonicalRoot, account: null, consentDigest: current.consent.digest });
        if (this.closed || this.expired) throw unavailable("Login closed during preparation");
        const authoritySecret=randomBytes(32),supplierGeneration=randomUUID();
        this.authorityInitialize={runtimeProcessIncarnationId:randomUUID(),supplierGeneration,runtimeChallenge:randomBytes(32).toString("base64url"),exactSupplyDigest:supply.sha256,authoritySecret,
          descriptor:{capability:"chirality.local-admission-authority",contract:AUTHORITY_CONTRACT,major:1,minor:0},v4Descriptor:{capability:"account.identity-snapshot",contract:"chirality-supplier-account-identity/1",major:1,minor:0,method:"account/identitySnapshot"}};
        const appServerArguments=this.options.releaseV2?.supportProfile.compiler.nativePolicyIdentityVersion===11?runtimeStageCAppServerArguments(configOverrides):["app-server",...flags];
        const child = native.value.spawnGroupedSupplier("/usr/bin/sandbox-exec", [...args, ...appServerArguments], authoritySecret, { cwd: this.options.canonicalRoot, environment: containment.environment, processGroup: true });
        if (child.state !== "available") throw unavailable("Contained login process could not start");
        const retirement = createGroupedLoginRetirement({ retire: () => retireAuthenticatedSupplierGroup(child.value), cleanup: () => containment.cleanup(),
          retainedResources: [containment.environment.TMPDIR, containment.sandboxProfilePath], ...(child.value.pid === undefined ? {} : { pid: child.value.pid }) });
        return { stdin: child.value.stdin, stdout: child.value.stdout, close: retirement.close, diagnostics: retirement.diagnostics };
      }
      const child = spawn("/usr/bin/sandbox-exec", [...args, ...flags], { env: containment.environment, cwd: this.options.canonicalRoot, shell: false, detached: true, stdio: "pipe" });
      const closed = new Promise<void>(resolve => child.once("close", () => resolve()));
      const signal = (value: NodeJS.Signals) => { if (child.pid) { try { process.kill(-child.pid, value); } catch (error) { if ((error as NodeJS.ErrnoException).code !== "ESRCH") throw error; } } };
      child.once("exit", () => signal("SIGKILL")); child.on("error", () => {});
      let stderrBytes = 0;
      child.stderr.on("data", (bytes: Buffer) => { stderrBytes += bytes.length; if (stderrBytes > 65536) signal("SIGKILL"); });
      let closing: Promise<void> | undefined;
      const close = () => closing ??= (async () => {
        signal("SIGTERM"); let timer: ReturnType<typeof setTimeout> | undefined;
        try { await Promise.race([closed, new Promise<void>(resolve => { timer = setTimeout(resolve, 500); })]); }
        finally { clearTimeout(timer); }
        signal("SIGKILL"); await closed; await containment.cleanup();
      })();
      try { await new Promise<void>((resolve, reject) => { child.once("spawn", resolve); child.once("error", reject); }); }
      catch { await close(); throw unavailable("Contained login process could not start"); }
      return { stdin: child.stdin, stdout: child.stdout, close };
    } catch (error) { try { await containment.cleanup(); } catch (cleanup) { throw new AggregateError([error, cleanup], "Login preparation and cleanup failed"); } throw error; }
  }
  async startLogin(): Promise<{ loginId: string; authUrl: string }> {
    if (this.started || this.closed) throw unavailable("Login component is single-use"); this.started = true;
    try {
      const transport = await this.launch(); this.transport = transport;
      if (this.closed) { await transport.close(); throw unavailable("Login was closed during startup"); }
      const nativeSkills = this.controlledNativeSkills ?? (this.options.releaseV2?.supportProfile.compiler.nativePolicyIdentityVersion === 11 ? "disabled" as const : undefined);
      this.actor = new CodexTurnSession({ transport, purpose: "login", nativeSkills, runtimeV2: this.options.instanceV2 && this.options.instanceAdmissionV2 ? { instanceInput: this.options.instanceV2, instanceAdmission: this.options.instanceAdmissionV2 } : undefined });
      this.timer = setTimeout(() => { this.expired = true; void this.close().catch(error => { this.closeFailure = error; }); }, this.options.timeoutMs ?? 300000);
      if(nativeSkills){if(!this.authorityInitialize)throw unavailable("Private login initialization unavailable");await this.actor.initializeAuthority(this.authorityInitialize);this.authorityInitialize.authoritySecret.fill(0);}else await this.actor.initialize();
      await this.actor.verifyNativeSkillSelection(this.options.canonicalRoot);
      if (this.options.instanceV2 && this.options.instanceAdmissionV2) await revalidateRuntimeInstanceAdmissionV2(this.options.instanceV2, this.options.instanceAdmissionV2);
      if (this.closed || this.expired) throw unavailable("Login closed before account effect");
      return await this.actor.loginStart();
    } catch (error) { try { await this.close(); } catch (cleanup) { throw new AggregateError([error, cleanup], "Login startup and retirement failed"); } throw error; }
  }
  /** The admitted default is the unique non-hidden default of the same catalog read `resolveModelCatalog` retains. */
  async resolveDefaultModel(): Promise<Readonly<{ model: string; defaultReasoningEffort: string }>> {
    if (this.selectedModel) return this.selectedModel;
    const catalog = await this.resolveModelCatalog();
    return this.selectedModel ?? Object.freeze({ model: catalog.default.model, defaultReasoningEffort: catalog.default.defaultReasoningEffort });
  }
  /** Same `model/list` requests, pages and bound as before; non-hidden entries are retained in catalog order. */
  async resolveModelCatalog(): Promise<Readonly<HostedModelCatalog>> {
    if (this.modelCatalog) return this.modelCatalog;
    if (!this.actor || this.closed) throw unavailable("Authenticated model catalog is unavailable");
    try {
    const cursors = new Set<string>(), models = new Map<string, { hidden: boolean; isDefault: boolean; defaultReasoningEffort: string; supportedReasoningEfforts: readonly string[] }>();
    let cursor: string | undefined;
    for (let pageIndex = 0; pageIndex < 64; pageIndex++) {
      if (this.options.instanceV2 && this.options.instanceAdmissionV2) await revalidateRuntimeInstanceAdmissionV2(this.options.instanceV2, this.options.instanceAdmissionV2);
      if (this.closed || this.expired) throw unavailable("Model catalog closed before request");
      const page = await this.actor.listModelsPage(cursor);
      for (const item of page.data) {
        const previous = models.get(item.model);
        if (previous && (previous.hidden !== item.hidden || previous.isDefault !== item.isDefault || previous.defaultReasoningEffort !== item.defaultReasoningEffort
          || previous.supportedReasoningEfforts.join("\0") !== item.supportedReasoningEfforts.join("\0"))) throw unavailable("Conflicting model catalog record");
        if (previous) throw unavailable("Duplicate model catalog record");
        models.set(item.model, { hidden: item.hidden, isDefault: item.isDefault, defaultReasoningEffort: item.defaultReasoningEffort, supportedReasoningEfforts: item.supportedReasoningEfforts });
      }
      if (page.nextCursor === null) {
        const visible = [...models].filter(([, value]) => !value.hidden);
        const defaults = visible.filter(([, value]) => value.isDefault);
        if (defaults.length !== 1) throw unavailable("Model catalog has no unique usable default");
        if (visible.length > 64) throw unavailable("Model catalog exceeds the retained catalog bound");
        if (this.options.instanceV2 && this.options.instanceAdmissionV2) await revalidateRuntimeInstanceAdmissionV2(this.options.instanceV2, this.options.instanceAdmissionV2);
        if (this.closed || this.expired) throw unavailable("Model catalog closed before selection");
        let catalog: Readonly<HostedModelCatalog>;
        try { catalog = hostedModelCatalog(visible.map(([model, value]) => ({ model, isDefault: value.isDefault, defaultReasoningEffort: value.defaultReasoningEffort, supportedReasoningEfforts: value.supportedReasoningEfforts }))); }
        catch { throw unavailable("Model catalog is not usable"); }
        const selected = Object.freeze({ model: catalog.default.model, defaultReasoningEffort: catalog.default.defaultReasoningEffort });
        await this.close();
        if (this.expired || this.cancelled) throw unavailable("Model catalog cancelled or expired during retirement");
        this.selectedModel = selected; this.modelCatalog = catalog; return catalog;
      }
      if (page.nextCursor === cursor || cursors.has(page.nextCursor)) throw unavailable("Model catalog cursor did not make progress");
      cursors.add(page.nextCursor); cursor = page.nextCursor;
    }
    throw unavailable("Model catalog pagination exceeded its bound");
    } catch (error) {
      try { await this.close(); } catch (cleanup) { throw new AggregateError([error, cleanup], "Model catalog and retirement failed"); }
      throw error;
    }
  }
  private async requireQualifiedLoginPurpose(supplySha256: string, outerPolicyDigest: string): Promise<void> {
    const admission = this.options.startupAdmission ?? this.options.purposeAdmission;
    if (this.options.instanceV2) {
      if (!this.options.instanceAdmissionV2 || admission?.instanceAdmissionV2 !== this.options.instanceAdmissionV2 || this.options.instanceV2.outerPolicyDigest !== outerPolicyDigest
        || this.options.releaseV2?.supportProfile.supplier.sha256 !== supplySha256) throw unavailable("Trusted v2 login admission is unavailable");
      await revalidateRuntimeInstanceAdmissionV2(this.options.instanceV2, this.options.instanceAdmissionV2); return;
    }
    const { timeoutMs: _timeoutMs, startupAdmission: _startupAdmission, purposeAdmission: _purposeAdmission, purposeRelease: _purposeRelease, releaseV2: _releaseV2, instanceV2: _instanceV2, instanceAdmissionV2: _instanceAdmissionV2, ...binding } = this.options;
    if (!admission || !loginAdmissions.has(admission) || admission.evidence !== "externally-accepted-native-login-purpose"
      || admission.bindingDigest !== loginBinding(binding, supplySha256, outerPolicyDigest)
      || !digest(admission.recordSha256) || !admission.ownerReference.trim()) throw unavailable("Trusted keyring login purpose lacks accepted release evidence");
  }
  private projectStatus(current: { state: HostedLoginStatus["state"]; loginId?: string; hasAccount?: boolean }): CodexLoginStatus {
    return validateHostedLoginStatus({ schema: "chirality-hosted-login-status/v2", ...current,
      evidenceClass: this.evidenceClass, hostedReady: false,
      binding: { schema: "chirality-hosted-account-binding/v1", state: "unavailable", reason: "canonical-identity-producer-unavailable" } });
  }
  async status(): Promise<CodexLoginStatus> {
    if (this.result) return validateHostedLoginStatus(this.result);
    const current = this.actor?.loginStatus();
    if (!current || this.expired || this.closed) return this.projectStatus({ state: "failed" });
    if (current.state !== "completed") { if (current.state === "failed") await this.close(); return this.projectStatus(current); }
    try {
      if (this.options.instanceV2 && this.options.instanceAdmissionV2) await revalidateRuntimeInstanceAdmissionV2(this.options.instanceV2, this.options.instanceAdmissionV2);
      const account = await this.actor!.accountRead();
      // Cancellation, timeout or close during account/read must not revive the ceremony.
      if (this.closed || this.expired) return this.projectStatus({ state: "failed", loginId: current.loginId });
      if (!account.hasAccount) throw unavailable("Provider completion has no account");
      if (this.options.instanceV2 && this.options.instanceAdmissionV2) await revalidateRuntimeInstanceAdmissionV2(this.options.instanceV2, this.options.instanceAdmissionV2);
      if (!this.fixture) await assertCodexKeyringHomeHasNoPlaintextCredentials(this.options.codexHome);
      this.result = this.projectStatus({ state: "completed", loginId: current.loginId, hasAccount: true });
      if (!this.options.instanceV2 && !this.retainAuthenticatedSessionForModelCatalog) clearTimeout(this.timer);
      if (!this.options.instanceV2 && !this.retainAuthenticatedSessionForModelCatalog) await this.close();
      return validateHostedLoginStatus(this.result);
    } catch {
      this.result ??= this.projectStatus({ state: "failed", loginId: current.loginId });
      await this.close(); return validateHostedLoginStatus(this.result);
    }
  }
  async cancel(): Promise<void> {
    this.cancelled = true; this.closed = true;
    try { if (this.actor?.loginStatus().state === "pending") await this.actor.loginCancel(); }
    finally { await this.close(); }
  }
  async close(): Promise<void> {
    this.closed = true; clearTimeout(this.timer);
    this.authorityInitialize?.authoritySecret.fill(0);
    if (this.actor) await this.actor.close(); else if (this.fixture) await this.fixture.close();
    if (this.closeFailure) throw this.closeFailure;
    // Persistent managed-auth storage remains supplier-owned; this component never reads credentials.
  }
  /** Sanitized retirement diagnostics recorded by the last settled close; empty before close or when nothing failed. */
  closeDiagnostics(): readonly CodexLoginCloseDiagnostic[] { return (this.transport ?? this.fixture)?.diagnostics?.() ?? []; }
}
export const createControlledCodexLoginForTests = CodexLogin.controlledForTests;
