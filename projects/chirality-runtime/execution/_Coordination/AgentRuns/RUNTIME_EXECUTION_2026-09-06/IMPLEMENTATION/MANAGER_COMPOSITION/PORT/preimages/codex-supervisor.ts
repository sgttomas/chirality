import { spawn } from "node:child_process";
import { constants } from "node:fs";
import { lstat, open, realpath } from "node:fs/promises";
import { createHash, randomUUID } from "node:crypto";
import { join } from "node:path";
import { RuntimeError, type DelegatedHarnessProcessSupervisorPort, type WorkerContinuity, type WorkerHandle, type WorkerResult } from "@chirality/runtime-contracts";
import { assertContinuity, DescendantTracker, HostedConsentStore, isContained, privateDirectory, revalidateExactSupply, sameContinuity, verifyExactSupply } from "@chirality/runtime-core";
import { prepareCodexNativePolicy } from "./codex-containment.js";
import { CodexTurnSession, type CodexSessionTransport } from "./codex-session.js";

export interface CodexSupervisorOptions {
  executablePath: string;
  model: string;
  identity: WorkerContinuity;
  codexHome: string;
  privateDirectory: string;
  authBindingSha256: string;
  providerNetworkConsent: { approvedBy: string; approvalReference: string };
  requestTimeoutMs?: number;
  turnTimeoutMs?: number;
  maxWorkers?: number;
  protectedPaths?: readonly string[];
  commandNetworkPosture?: "off" | "on";
}
type NativePermissions = Awaited<ReturnType<typeof prepareCodexNativePolicy>>["expectedPermissions"];
export interface ControlledCodexLauncher { (): Promise<{ pid: number; transport: CodexSessionTransport; permissionProfile?: string; policyDigest?: string; expectedPermissions?: NativePermissions; descendantTracker?: DescendantTracker }> }
interface Entry { handle: WorkerHandle; session: CodexTurnSession; result: Promise<WorkerResult>; cleanup: () => Promise<void> }
const unavailable = (message: string) => new RuntimeError("ENGINE_UNAVAILABLE", message, 503);
function id(value: string): void { if (typeof value !== "string" || !/^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$/.test(value)) throw new RuntimeError("INVALID_REQUEST", "Invalid worker identity"); }

/** Concrete hosted-validation adapter. Supply/account checks do not accept a vendor signature or authorize account use. */
export class CodexSupervisor implements DelegatedHarnessProcessSupervisorPort {
  private readonly options: CodexSupervisorOptions;
  private fixtureLauncher?: ControlledCodexLauncher;
  private readonly entries = new Map<string, Entry>();
  private readonly acquiring = new Set<string>();
  private readonly pendingAcquisitions = new Map<string, Promise<void>>();
  private closed = false;
  constructor(options: CodexSupervisorOptions) {
    if (!options || typeof options.model !== "string" || !options.model.trim() || options.model.length > 128 || /[\x00-\x1f]/.test(options.model)) throw new RuntimeError("INVALID_REQUEST", "Explicit Codex model required");
    for (const value of [options.requestTimeoutMs ?? 10_000, options.turnTimeoutMs ?? 120_000, options.maxWorkers ?? 16]) if (!Number.isSafeInteger(value) || value < 1 || value > 600_000) throw new RuntimeError("INVALID_REQUEST", "Invalid Codex supervisor bound");
    if (options.commandNetworkPosture !== undefined && !["off", "on"].includes(options.commandNetworkPosture)) throw new RuntimeError("INVALID_REQUEST", "Unsupported executable command-network posture");
    this.options = structuredClone(options);
  }
  /** Controlled adapter tests are structurally excluded from verifyHostedBoundary. */
  static controlledForTests(options: { identity: WorkerContinuity; model: string; launch: ControlledCodexLauncher; requestTimeoutMs?: number; turnTimeoutMs?: number }): CodexSupervisor {
    const result = new CodexSupervisor({ identity: options.identity, model: options.model, privateDirectory: options.identity.canonicalRoot, codexHome: options.identity.canonicalRoot,
      executablePath: "controlled-fixture-only", authBindingSha256: "", providerNetworkConsent: { approvedBy: "", approvalReference: "" }, requestTimeoutMs: options.requestTimeoutMs, turnTimeoutMs: options.turnTimeoutMs });
    result.fixtureLauncher = options.launch;
    return result;
  }
  private async accountBinding(): Promise<void> {
    if (typeof this.options.authBindingSha256 !== "string" || !/^[a-f0-9]{64}$/.test(this.options.authBindingSha256)) throw unavailable("Exact operator-approved account-file binding is required");
    const path = join(this.options.codexHome, "auth.json");
    let handle;
    try {
      const initial = await lstat(path, { bigint: true });
      if (!initial.isFile() || initial.isSymbolicLink() || initial.uid !== BigInt(process.getuid!()) || (initial.mode & 0o777n) !== 0o600n || initial.size > 1024n * 1024n || await realpath(path) !== path) throw unavailable("Account file must be canonical owner-private 0600");
      handle = await open(path, constants.O_RDONLY | constants.O_NOFOLLOW);
      const before = await handle.stat({ bigint: true });
      if (before.ino !== initial.ino || before.dev !== initial.dev) throw unavailable("Account file changed before binding check");
      const bytes = await handle.readFile();
      const after = await handle.stat({ bigint: true }), current = await lstat(path, { bigint: true });
      if (after.ino !== current.ino || after.dev !== current.dev || after.mtimeNs !== before.mtimeNs || after.ctimeNs !== before.ctimeNs || after.size !== before.size || createHash("sha256").update(bytes).digest("hex") !== this.options.authBindingSha256) throw unavailable("Account binding drifted; operator rebind with a new epoch is required");
    } catch (error) { if (error instanceof RuntimeError) throw error; throw unavailable("Root-private account binding is unavailable"); }
    finally { await handle?.close(); }
  }
  private async nativePolicy() {
    const protectedPaths = this.options.protectedPaths;
    if (!Array.isArray(protectedPaths) || protectedPaths.length === 0 || protectedPaths.some(path => typeof path !== "string") || !protectedPaths.some(path => path !== this.options.privateDirectory && isContained(path, this.options.privateDirectory))) throw unavailable("Native action policy requires an explicit broker control root covering worker-private storage");
    let policy: Awaited<ReturnType<typeof prepareCodexNativePolicy>>;
    try {
      policy = await prepareCodexNativePolicy({ canonicalRoot: this.options.identity.canonicalRoot, codexHome: this.options.codexHome,
        privateDirectory: this.options.privateDirectory, immutableReadRoots: ["/bin", "/usr/lib", "/System/Volumes/Preboot/Cryptexes/OS/System/Library/dyld"],
        protectedPaths: [...protectedPaths], commandNetworkPosture: this.options.commandNetworkPosture ?? "off", providerNetworkConsent: this.options.providerNetworkConsent });
    } catch { throw unavailable("Native action policy could not be compiled safely"); }
    if (policy.policyDigest !== this.options.identity.policyDigest) {
      await policy.cleanup();
      throw unavailable("Configured continuity policy digest differs from the compiled native action policy");
    }
    return policy;
  }
  async verifyHostedBoundary(identity: WorkerContinuity): Promise<void> {
    if (this.fixtureLauncher) throw unavailable("Controlled Codex fixture cannot establish a hosted boundary");
    if (process.platform !== "darwin") throw unavailable("Hosted validation requires macOS containment");
    await assertContinuity(identity);
    if (!sameContinuity(identity, this.options.identity)) throw unavailable("Hosted worker continuity differs from trusted configuration");
    await privateDirectory(this.options.privateDirectory); await privateDirectory(this.options.codexHome);
    if (!isContained(this.options.privateDirectory, this.options.codexHome) || !isContained(this.options.privateDirectory, this.options.executablePath)) throw unavailable("Hosted home and exact binary must lie inside the dedicated worker-private root");
    const consent = this.options.providerNetworkConsent;
    if (!consent || typeof consent.approvedBy !== "string" || !consent.approvedBy.trim() || typeof consent.approvalReference !== "string" || !consent.approvalReference.trim()) throw unavailable("Explicit trusted provider network consent is required");
    const policy = await this.nativePolicy();
    await policy.cleanup();
    await this.accountBinding();
    await verifyExactSupply({ executablePath: this.options.executablePath });
    // Preflight also serves consent management, including revocation from on/ask.
    // Inspect the bound home here; enforce executable command posture only at acquire.
    await new HostedConsentStore({ canonicalRoot: identity.canonicalRoot, codexHome: this.options.codexHome }).read(identity);
  }
  private async observedTransport<T extends { pid: number; transport: CodexSessionTransport }>(launched: T, tracker: DescendantTracker): Promise<T> {
    const diagnostic = (state: Awaited<ReturnType<DescendantTracker["reconcile"]>>) => new RuntimeError("ENGINE_UNAVAILABLE", "Observed worker descendants require reconciliation", 503, {
      reason: "DESCENDANT_RECONCILIATION_REQUIRED", leaderObserved: Boolean(state.leader), observed: state.observed, scans: state.scans,
      detachedCount: state.detached.length, detachedPids: state.detached.slice(0, 32).map(value => value.pid),
      ownedGroupCount: state.ownedGroup.length, identityChangedCount: state.identityChanged.length,
      censusFailed: Boolean(state.failure), limitations: state.limitations, signalAuthority: "NONE"
    });
    try { await tracker.start(); }
    catch {
      await launched.transport.close().catch(() => {});
      const state = await tracker.reconcile(); await tracker.stop();
      throw diagnostic(state);
    }
    let closing: Promise<void> | undefined;
    const close = () => closing ??= (async () => {
      await tracker.reconcile(); // Fresh before caller-owned process-group cleanup.
      let cleanupError: unknown;
      try { await launched.transport.close(); } catch (error) { cleanupError = error; }
      const after = await tracker.reconcile();
      await tracker.stop();
      if (after.failure || after.detached.length || after.identityChanged.length || after.ownedGroup.length) throw diagnostic(after);
      if (cleanupError) throw cleanupError;
    })();
    return { ...launched, transport: { stdin: launched.transport.stdin, stdout: launched.transport.stdout, close } };
  }
  private async launch(): Promise<{ pid: number; transport: CodexSessionTransport; permissionProfile?: string; policyDigest?: string; expectedPermissions?: NativePermissions }> {
    if (this.fixtureLauncher) {
      const fixture = await this.fixtureLauncher();
      return fixture.descendantTracker ? this.observedTransport(fixture, fixture.descendantTracker) : fixture;
    }
    const supply = await verifyExactSupply({ executablePath: this.options.executablePath });
    const policy = await this.nativePolicy();
    try {
      await this.accountBinding(); await revalidateExactSupply(supply);
      // Exact trusted provider host; primary/descendant actions receive the native named policy.
      // This topology still needs empirical G-SBX evidence; no whole-provider wrapper is claimed.
      const [executable, ...args] = await policy.launchArguments(supply.executablePath);
      const child = spawn(executable!, args, { cwd: this.options.identity.canonicalRoot, env: policy.environment, shell: false, detached: true, stdio: "pipe" });
      const closed = new Promise<void>(resolve => child.once("close", () => resolve()));
      child.on("error", () => {});
      const signal = (value: NodeJS.Signals) => { if (child.pid) { try { process.kill(-child.pid, value); } catch (error) { if ((error as NodeJS.ErrnoException).code !== "ESRCH") throw error; } } };
      child.once("exit", () => { signal("SIGKILL"); });
      let stderrBytes = 0;
      child.stderr.on("data", (bytes: Buffer) => { stderrBytes += bytes.length; if (stderrBytes > 65536) signal("SIGKILL"); });
      let closing: Promise<void> | undefined;
      const close = () => closing ??= (async () => {
        signal("SIGTERM");
        let timer: ReturnType<typeof setTimeout> | undefined;
        try { await Promise.race([closed, new Promise<void>(resolve => { timer = setTimeout(resolve, 500); })]); }
        finally { clearTimeout(timer); }
        signal("SIGKILL"); await closed; await policy.cleanup();
      })();
      try { await new Promise<void>((resolve, reject) => { child.once("spawn", resolve); child.once("error", reject); }); }
      catch { await close(); throw unavailable("Contained Codex process could not start"); }
      const tracker = new DescendantTracker({ leaderPid: child.pid!, intervalMs: 100,
        maxDurationMs: Math.min(3_600_000, (this.options.turnTimeoutMs ?? 120_000) + (this.options.requestTimeoutMs ?? 10_000) * 12 + 5000) });
      return await this.observedTransport({ pid: child.pid!, transport: { stdin: child.stdin, stdout: child.stdout, close }, permissionProfile: policy.permissionProfile, policyDigest: policy.policyDigest, expectedPermissions: policy.expectedPermissions }, tracker);
    } catch (error) { await policy.cleanup(); throw error; }
  }
  async acquire(workerId: string, input: string): Promise<WorkerHandle> {
    id(workerId);
    if (this.closed || this.entries.has(workerId) || this.acquiring.has(workerId) || this.entries.size + this.acquiring.size >= (this.options.maxWorkers ?? 16)) throw unavailable("Codex worker is unavailable or already acquired");
    if (typeof input !== "string" || Buffer.byteLength(input) > 65536) throw new RuntimeError("INVALID_REQUEST", "Invalid hosted turn envelope");
    let request: { prompt: string; resumeThreadId?: string; requestedRole?: string; roleEvidence?: { selectedRole?: string; enforcementLabel?: string; evidencePosture?: string } };
    try { request = JSON.parse(input); } catch { throw new RuntimeError("INVALID_REQUEST", "Hosted worker requires the private broker JSON envelope"); }
    if (!request || typeof request !== "object" || Array.isArray(request) || Object.keys(request).some(key => !["prompt", "resumeThreadId", "requestedRole", "roleEvidence"].includes(key)) || typeof request.prompt !== "string" || !request.prompt.trim()) throw new RuntimeError("INVALID_REQUEST", "Invalid hosted turn envelope");
    if (request.resumeThreadId !== undefined) id(request.resumeThreadId);
    const selectedRole = request.requestedRole === undefined ? "untyped" : request.requestedRole;
    if (!["untyped", "agent0", "agent1", "agent2", "task"].includes(selectedRole)) throw new RuntimeError("INVALID_REQUEST", "Unknown explicitly requested role");
    const evidence = request.roleEvidence;
    if ((selectedRole !== "untyped" && !evidence) || (evidence !== undefined && (!evidence || typeof evidence !== "object" || Array.isArray(evidence) || evidence.selectedRole !== selectedRole || evidence.enforcementLabel !== "role not mechanically enforced" || evidence.evidencePosture !== "instruction-asserted"))) throw new RuntimeError("INVALID_REQUEST", "Role evidence must preserve the selected role and calibrated labels");
    const prompt = selectedRole === "untyped" ? request.prompt : `Runtime role instruction (explicit user selection): ${selectedRole}.\nrole not mechanically enforced; evidence posture: instruction-asserted.\n\n${request.prompt}`;
    this.acquiring.add(workerId);
    let finishAcquisition!: () => void;
    this.pendingAcquisitions.set(workerId, new Promise<void>(resolve => { finishAcquisition = resolve; }));
    try {
      if (this.fixtureLauncher) await assertContinuity(this.options.identity);
      else {
        await this.verifyHostedBoundary(this.options.identity);
        const consent = await new HostedConsentStore({ canonicalRoot: this.options.identity.canonicalRoot, codexHome: this.options.codexHome }).read(this.options.identity);
        if (consent?.posture !== (this.options.commandNetworkPosture ?? "off")) throw unavailable("Recorded command-network consent must match the configured executable posture");
      }
      if (this.closed) throw unavailable("Supervisor is closing");
      const launched = await this.launch();
      if (this.closed) { await launched.transport.close(); throw unavailable("Supervisor closed during acquisition"); }
      const handle: WorkerHandle = { workerId, generation: randomUUID(), pid: launched.pid, state: "running" };
      let session: CodexTurnSession;
      try {
        if (!this.fixtureLauncher && (!launched.permissionProfile || launched.policyDigest !== this.options.identity.policyDigest)) throw unavailable("Native action policy binding was lost during launch");
        session = new CodexTurnSession({ transport: launched.transport, requestTimeoutMs: this.options.requestTimeoutMs, turnTimeoutMs: this.options.turnTimeoutMs,
          permissionProfile: launched.permissionProfile, policyDigest: launched.policyDigest });
      } catch (error) { await launched.transport.close(); throw error; }
      // Drain bounded actor events; the authoritative result still comes only from waitTurn.
      void (async () => { for await (const _event of session.events()) { /* actor output accumulated in terminal */ } })().catch(() => {});
      const result = (async (): Promise<WorkerResult> => {
        try {
          await session.initialize();
          if (!this.fixtureLauncher && !launched.expectedPermissions) throw unavailable("Native effective-policy verification basis is missing");
          if (launched.expectedPermissions) await session.verifyNativePolicy(launched.expectedPermissions);
          const account = await session.accountRead();
          if (!account.hasAccount) throw unavailable("Codex has no root-private authenticated account");
          if (!this.fixtureLauncher) await this.accountBinding();
          const threadId = request.resumeThreadId
            ? await session.resumeThread({ threadId: request.resumeThreadId, model: this.options.model, continuityChecked: true })
            : await session.startThread({ cwd: this.options.identity.canonicalRoot, model: this.options.model, continuityChecked: true });
          const turnId = await session.startTurn({ threadId, text: prompt, model: this.options.model });
          const terminal = await session.waitTurn(turnId);
          return { worker: { ...handle, state: "exited" }, exitCode: terminal.status === "completed" ? 0 : terminal.status === "failed" ? 1 : null,
            signal: terminal.status === "interrupted" ? "SIGTERM" : null, stdout: terminal.output, stderr: "", threadId };
        } finally { handle.state = "exited"; await session.close(); await launched.transport.close(); }
      })();
      void result.catch(() => {});
      this.entries.set(workerId, { handle, session, result, cleanup: launched.transport.close });
      return { ...handle };
    } finally { this.acquiring.delete(workerId); this.pendingAcquisitions.delete(workerId); finishAcquisition(); }
  }
  async inventory(): Promise<readonly WorkerHandle[]> { return [...this.entries.values()].map(entry => ({ ...entry.handle })); }
  private entry(workerId: string, generation: string): Entry { const entry = this.entries.get(workerId); if (!entry || entry.handle.generation !== generation) throw unavailable("Unknown or stale Codex generation"); return entry; }
  async reconnect(workerId: string, generation: string): Promise<WorkerHandle> { return { ...this.entry(workerId, generation).handle }; }
  async wait(workerId: string, generation: string): Promise<WorkerResult> { return this.entry(workerId, generation).result; }
  async retire(workerId: string, generation: string): Promise<void> { const entry = this.entry(workerId, generation); await entry.session.close(); await entry.result.catch(() => {}); await entry.cleanup(); if (this.entries.get(workerId) === entry) this.entries.delete(workerId); }
  async close(): Promise<void> { this.closed = true; await Promise.all([...this.pendingAcquisitions.values()]); await Promise.all([...this.entries.values()].map(entry => this.retire(entry.handle.workerId, entry.handle.generation))); }
}
export function createControlledCodexSupervisorForTests(options: Parameters<typeof CodexSupervisor.controlledForTests>[0]): CodexSupervisor { return CodexSupervisor.controlledForTests(options); }
