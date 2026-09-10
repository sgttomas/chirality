import { createHash } from "node:crypto";
import { constants } from "node:fs";
import { open, realpath } from "node:fs/promises";
import { spawn } from "node:child_process";
import { RuntimeError, validateHostedLoginStatus, type HostedLoginStatus } from "@chirality/runtime-contracts";
import { computeRuntimeArtifactDigest, configureRuntimeConformanceArtifactInventory, isContained, privateDirectory, recordKey, revalidateExactSupply, runtimeConformanceArtifactInventory, RuntimeConformanceFileAcceptancePort, verifyExactSupply, type RuntimeConformanceConfiguration } from "@chirality/runtime-core";
import { assertCodexKeyringHomeHasNoPlaintextCredentials, prepareCodexContainment } from "./codex-containment.js";
import { CodexTurnSession, type CodexSessionTransport } from "./codex-session.js";

export interface CodexLoginOptions {
  executablePath: string; canonicalRoot: string; codexHome: string; privateDirectory: string;
  /** Trusted operator provenance, never populated from client request fields. */
  providerNetworkConsent: { approvedBy: string; approvalReference: string };
  purposeRelease?: RuntimeConformanceConfiguration;
  startupAdmission?: CodexLoginStartupAdmission;
  /** @deprecated Temporary private-composition source compatibility. */
  purposeAdmission?: CodexLoginStartupAdmission;
  timeoutMs?: number;
}
export interface CodexLoginStartupAdmission {
  readonly bindingDigest: string;
  readonly evidence: "externally-accepted-native-login-purpose";
  readonly recordSha256: string;
  readonly ownerReference: string;
}
const loginAdmissions = new WeakSet<object>();
function loginBinding(options: Omit<CodexLoginOptions, "timeoutMs" | "startupAdmission" | "purposeRelease">, supplySha256: string, outerPolicyDigest: string): string {
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
  const consent = options.providerNetworkConsent;
  if (!consent?.approvedBy?.trim() || !consent.approvalReference?.trim()) throw unavailable("Explicit trusted provider consent is required for sign-in");
  if (!isContained(options.privateDirectory, options.codexHome) || options.privateDirectory === options.codexHome || !isContained(options.privateDirectory, options.executablePath)) throw unavailable("Login home and exact executable must be inside the dedicated private directory");
  await privateDirectory(options.privateDirectory); await privateDirectory(options.codexHome);
  await assertCodexKeyringHomeHasNoPlaintextCredentials(options.codexHome);
  const { purposeRelease, ...startup } = options;
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
/** Operator-only, explicit-consent sign-in lifecycle; construction performs no login. */
export class CodexLogin {
  private actor: CodexTurnSession | undefined;
  private fixture: CodexSessionTransport | undefined;
  private started = false;
  private closed = false;
  private expired = false;
  private timer: ReturnType<typeof setTimeout> | undefined;
  private result: CodexLoginStatus | undefined;
  constructor(private readonly options: CodexLoginOptions) {
    const timeout = options.timeoutMs ?? 300000;
    if (!Number.isSafeInteger(timeout) || timeout < 1 || timeout > 900000) throw unavailable("Invalid bounded login timeout");
  }
  /** Explicit fixture seam, never emits exact-supply-login evidence. */
  static controlledForTests(input: { transport: CodexSessionTransport; codexHome: string; timeoutMs?: number }): CodexLogin {
    const instance = new CodexLogin({ executablePath: "", canonicalRoot: "", privateDirectory: "", codexHome: input.codexHome, providerNetworkConsent: { approvedBy: "", approvalReference: "" }, timeoutMs: input.timeoutMs });
    instance.fixture = input.transport; return instance;
  }
  private get evidenceClass(): CodexLoginStatus["evidenceClass"] { return this.fixture ? "controlled-fixture" : "exact-supply-login"; }
  private async launch(): Promise<CodexSessionTransport> {
    if (this.fixture) return this.fixture;
    if (process.platform !== "darwin" || process.arch !== "arm64") throw unavailable("Exact login requires darwin-arm64");
    const consent = this.options.providerNetworkConsent;
    if (!consent || typeof consent.approvedBy !== "string" || !consent.approvedBy.trim() || typeof consent.approvalReference !== "string" || !consent.approvalReference.trim()) throw unavailable("Explicit trusted provider consent is required for sign-in");
    if (!isContained(this.options.privateDirectory, this.options.codexHome) || this.options.privateDirectory === this.options.codexHome || !isContained(this.options.privateDirectory, this.options.executablePath)) throw unavailable("Login home and exact executable must be inside the dedicated private directory");
    await privateDirectory(this.options.privateDirectory); await privateDirectory(this.options.codexHome);
    await assertCodexKeyringHomeHasNoPlaintextCredentials(this.options.codexHome);
    const supply = await verifyExactSupply({ executablePath: this.options.executablePath });
    const containment = await prepareCodexContainment({ canonicalRoot: this.options.canonicalRoot, privateDirectory: this.options.privateDirectory, codexHome: this.options.codexHome, providerNetworkConsent: consent, purpose: "trusted-login" });
    try {
      this.requireQualifiedLoginPurpose(supply.sha256, containment.outerPolicyDigest);
      const args = await containment.launchArguments(supply.executablePath);
      await revalidateExactSupply(supply);
      const flags = ["-c", 'cli_auth_credentials_store="keyring"', "-c", "features.plugins=false", "-c", "allow_login_shell=false", "-c", 'approval_policy="never"', "-c", "check_for_update_on_startup=false", "-c", "analytics.enabled=false", "-c", "feedback.enabled=false"];
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
    } catch (error) { await containment.cleanup(); throw error; }
  }
  async startLogin(): Promise<{ loginId: string; authUrl: string }> {
    if (this.started || this.closed) throw unavailable("Login component is single-use"); this.started = true;
    try {
      const transport = await this.launch();
      if (this.closed) { await transport.close(); throw unavailable("Login was closed during startup"); }
      this.actor = new CodexTurnSession({ transport, purpose: "login" });
      this.timer = setTimeout(() => { this.expired = true; void this.close(); }, this.options.timeoutMs ?? 300000);
      await this.actor.initialize();
      return await this.actor.loginStart();
    } catch (error) { await this.close(); throw error; }
  }
  private requireQualifiedLoginPurpose(supplySha256: string, outerPolicyDigest: string): void {
    const admission = this.options.startupAdmission ?? this.options.purposeAdmission;
    const { timeoutMs: _timeoutMs, startupAdmission: _startupAdmission, purposeAdmission: _purposeAdmission, purposeRelease: _purposeRelease, ...binding } = this.options;
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
      const account = await this.actor!.accountRead();
      // Cancellation, timeout or close during account/read must not revive the ceremony.
      if (this.closed || this.expired) return this.projectStatus({ state: "failed", loginId: current.loginId });
      if (!account.hasAccount) throw unavailable("Provider completion has no account");
      if (!this.fixture) await assertCodexKeyringHomeHasNoPlaintextCredentials(this.options.codexHome);
      this.result = this.projectStatus({ state: "completed", loginId: current.loginId, hasAccount: true });
      clearTimeout(this.timer); await this.close(); return validateHostedLoginStatus(this.result);
    } catch {
      this.result ??= this.projectStatus({ state: "failed", loginId: current.loginId });
      await this.close(); return validateHostedLoginStatus(this.result);
    }
  }
  async cancel(): Promise<void> {
    this.closed = true;
    try { if (this.actor?.loginStatus().state === "pending") await this.actor.loginCancel(); }
    finally { await this.close(); }
  }
  async close(): Promise<void> {
    this.closed = true; clearTimeout(this.timer);
    if (this.actor) await this.actor.close(); else if (this.fixture) await this.fixture.close();
    // Persistent managed-auth storage remains supplier-owned; this component never reads credentials.
  }
}
export const createControlledCodexLoginForTests = CodexLogin.controlledForTests;
