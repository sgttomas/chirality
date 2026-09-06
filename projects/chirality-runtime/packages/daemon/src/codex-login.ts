import { spawn } from "node:child_process";
import { constants } from "node:fs";
import { lstat, open, realpath } from "node:fs/promises";
import { createHash } from "node:crypto";
import { join } from "node:path";
import { RuntimeError } from "@chirality/runtime-contracts";
import { isContained, privateDirectory, revalidateExactSupply, verifyExactSupply } from "@chirality/runtime-core";
import { prepareCodexContainment } from "./codex-containment.js";
import { CodexTurnSession, type CodexSessionTransport } from "./codex-session.js";

export interface CodexLoginOptions {
  executablePath: string; canonicalRoot: string; codexHome: string; privateDirectory: string;
  /** Trusted operator provenance, never populated from client request fields. */
  providerNetworkConsent: { approvedBy: string; approvalReference: string };
  timeoutMs?: number;
}
export interface CodexLoginStatus {
  state: "pending" | "completed" | "failed";
  loginId?: string;
  hasAccount?: boolean;
  authBindingSha256?: string;
  evidenceClass: "exact-supply-login" | "controlled-fixture";
}
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
    const supply = await verifyExactSupply({ executablePath: this.options.executablePath });
    const containment = await prepareCodexContainment({ canonicalRoot: this.options.canonicalRoot, privateDirectory: this.options.privateDirectory, codexHome: this.options.codexHome, providerNetworkConsent: consent });
    try {
      const args = await containment.launchArguments(supply.executablePath);
      await revalidateExactSupply(supply);
      const flags = ["-c", 'cli_auth_credentials_store="file"', "-c", "features.plugins=false", "-c", "allow_login_shell=false", "-c", 'approval_policy="never"', "-c", "check_for_update_on_startup=false", "-c", "analytics.enabled=false", "-c", "feedback.enabled=false"];
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
  private async authBinding(): Promise<string> {
    await privateDirectory(this.options.codexHome);
    if (await realpath(this.options.codexHome) !== this.options.codexHome) throw unavailable("Login home alias rejected");
    const path = join(this.options.codexHome, "auth.json");
    let handle;
    try {
      const before = await lstat(path, { bigint: true });
      if (!before.isFile() || before.isSymbolicLink() || before.uid !== BigInt(process.getuid?.() ?? -1) || (before.mode & 0o077n) !== 0n || before.size < 1n || before.size > 1048576n) throw unavailable("Login credential record is not private bounded data");
      handle = await open(path, constants.O_RDONLY | constants.O_NOFOLLOW);
      const opened = await handle.stat({ bigint: true });
      if (opened.dev !== before.dev || opened.ino !== before.ino) throw unavailable("Credential record changed before binding");
      const buffer = Buffer.alloc(Number(before.size) + 1);
      let length = 0;
      while (length < buffer.length) { const { bytesRead } = await handle.read(buffer, length, buffer.length - length, null); if (!bytesRead) break; length += bytesRead; }
      const bytes = buffer.subarray(0, length);
      const after = await handle.stat({ bigint: true }), current = await lstat(path, { bigint: true });
      if (after.dev !== current.dev || after.ino !== current.ino || after.mtimeNs !== before.mtimeNs || after.ctimeNs !== before.ctimeNs || after.size !== before.size || bytes.length !== Number(before.size)) throw unavailable("Credential record changed during binding");
      const value: unknown = JSON.parse(bytes.toString()); if (!value || typeof value !== "object" || Array.isArray(value)) throw unavailable("Invalid credential record");
      return createHash("sha256").update(bytes).digest("hex");
    } catch { throw unavailable("Private login credential binding is unavailable"); }
    finally { await handle?.close(); }
  }
  async status(): Promise<CodexLoginStatus> {
    if (this.result) return { ...this.result };
    const current = this.actor?.loginStatus();
    if (!current || this.expired || (this.closed && current.state !== "completed")) return { state: "failed", evidenceClass: this.evidenceClass };
    if (current.state !== "completed") { if (current.state === "failed") await this.close(); return { ...current, evidenceClass: this.evidenceClass }; }
    try {
      const account = await this.actor!.accountRead();
      if (!account.hasAccount) throw unavailable("Provider completion has no persisted account");
      const authBindingSha256 = await this.authBinding();
      this.result = { state: "completed", loginId: current.loginId, hasAccount: true, authBindingSha256, evidenceClass: this.evidenceClass };
      clearTimeout(this.timer); await this.close(); return { ...this.result };
    } catch { this.result = { state: "failed", loginId: current.loginId, evidenceClass: this.evidenceClass }; await this.close(); return { ...this.result }; }
  }
  async cancel(): Promise<void> {
    try { if (this.actor?.loginStatus().state === "pending") await this.actor.loginCancel(); }
    finally { await this.close(); }
  }
  async close(): Promise<void> {
    this.closed = true; clearTimeout(this.timer);
    if (this.actor) await this.actor.close(); else if (this.fixture) await this.fixture.close();
    // Persistent CODEX_HOME and auth.json are deliberately preserved.
  }
}
export const createControlledCodexLoginForTests = CodexLogin.controlledForTests;
