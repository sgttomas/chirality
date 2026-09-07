import { spawn } from "node:child_process";
import { RuntimeError, validateHostedLoginStatus, type HostedLoginStatus } from "@chirality/runtime-contracts";
import { isContained, privateDirectory, revalidateExactSupply, verifyExactSupply } from "@chirality/runtime-core";
import { prepareCodexContainment } from "./codex-containment.js";
import { CodexTurnSession, type CodexSessionTransport } from "./codex-session.js";

export interface CodexLoginOptions {
  executablePath: string; canonicalRoot: string; codexHome: string; privateDirectory: string;
  /** Trusted operator provenance, never populated from client request fields. */
  providerNetworkConsent: { approvedBy: string; approvalReference: string };
  timeoutMs?: number;
}
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
    this.requireQualifiedLoginPurpose();
    if (process.platform !== "darwin" || process.arch !== "arm64") throw unavailable("Exact login requires darwin-arm64");
    const consent = this.options.providerNetworkConsent;
    if (!consent || typeof consent.approvedBy !== "string" || !consent.approvedBy.trim() || typeof consent.approvalReference !== "string" || !consent.approvalReference.trim()) throw unavailable("Explicit trusted provider consent is required for sign-in");
    if (!isContained(this.options.privateDirectory, this.options.codexHome) || this.options.privateDirectory === this.options.codexHome || !isContained(this.options.privateDirectory, this.options.executablePath)) throw unavailable("Login home and exact executable must be inside the dedicated private directory");
    await privateDirectory(this.options.privateDirectory); await privateDirectory(this.options.codexHome);
    const supply = await verifyExactSupply({ executablePath: this.options.executablePath });
    const containment = await prepareCodexContainment({ canonicalRoot: this.options.canonicalRoot, privateDirectory: this.options.privateDirectory, codexHome: this.options.codexHome, providerNetworkConsent: consent, purpose: "trusted-login" });
    try {
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
  private requireQualifiedLoginPurpose(): void {
    // Exact executable provenance alone cannot qualify this new keyring/process purpose.
    // No independent qualifying basis or operational unlock is supplied in this increment.
    throw unavailable("Trusted keyring login purpose is not independently qualified");
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
