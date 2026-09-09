import { retireNativeSupplier } from "./codex-transport-lifecycle.js";
import { spawn } from "node:child_process";
import { lstat, mkdtemp, mkdir, realpath, writeFile, rm } from "node:fs/promises";
import { createHash } from "node:crypto";
import { homedir } from "node:os";
import { isAbsolute, resolve, join, dirname } from "node:path";
import { verifyExactSupply, revalidateExactSupply } from "@chirality/runtime-core";

export interface CodexProbeInput { executablePath: string; privateDirectory: string }
/** Workers never receive supplier authority secrets, leases, generations, snapshots, or transcript frames. */
export const CODEX_WORKER_AUTHORITY_SURFACE = "none" as const;
export interface CodexProtocolCheck { method: string; status: "passed" | "rejected" }
export interface CodexProbeResult {
  evidenceClass: "accepted-supply-offline-probe" | "controlled-fixture";
  protocolChecks: readonly CodexProtocolCheck[];
  authRequired: boolean | undefined;
  hostedTurnAvailable: false;
  exitCode: number | null;
  signal: string | null;
  stderrSha256: string;
  supply?: { sha256: string; version: string; signatureStatus: string };
}
const CONFIG = `approval_policy = "never"
sandbox_mode = "workspace-write"
allow_login_shell = false
cli_auth_credentials_store = "file"
check_for_update_on_startup = false
web_search = "disabled"
[sandbox_workspace_write]
network_access = false
exclude_slash_tmp = true
exclude_tmpdir_env_var = true
[features]
plugins = false
[analytics]
enabled = false
[feedback]
enabled = false
`;
function wire(cwd: string): Record<string, unknown>[] {
  return [
    { method: "initialize", id: 1, params: { clientInfo: { name: "chirality_runtime_offline_probe", version: "0.0.0" }, capabilities: { experimentalApi: true } } },
    { method: "initialized" },
    { method: "config/read", id: 2, params: { includeLayers: true, cwd } },
    { method: "configRequirements/read", id: 3, params: {} },
    { method: "experimentalFeature/list", id: 4, params: { limit: 100 } },
    { method: "account/read", id: 5, params: { refreshToken: false } },
  ];
}
async function privateScratch(input: CodexProbeInput): Promise<string> {
  for (const path of [input.executablePath, input.privateDirectory]) {
    if (typeof path !== "string" || !isAbsolute(path) || resolve(path) !== path || await realpath(path) !== path || /[\x00-\x1f]/.test(path)) throw new Error("probe requires canonical absolute paths without aliases");
  }
  const st = await lstat(input.privateDirectory);
  if (!st.isDirectory() || st.uid !== process.getuid?.() || (st.mode & 0o777) !== 0o700 || dirname(input.privateDirectory) === input.privateDirectory) throw new Error("probe directory must be private owned 0700");
  const root = await mkdtemp(join(input.privateDirectory, "codex-offline-"));
  try {
    await Promise.all(["home", "work", "tmp"].map(name => mkdir(join(root, name), { mode: 0o700 })));
    await writeFile(join(root, "home", "config.toml"), CONFIG, { mode: 0o600, flag: "wx" });
    return root;
  } catch (error) { await rm(root, { recursive: true, force: true }); throw error; }
}
async function exchange(executable: string, args: readonly string[], root: string): Promise<Omit<CodexProbeResult, "evidenceClass">> {
  const child = spawn(executable, [...args], { cwd: join(root, "work"), env: { PATH: "/usr/bin:/bin:/usr/sbin:/sbin", HOME: join(root, "home"), CODEX_HOME: join(root, "home"), TMPDIR: join(root, "tmp") }, stdio: "pipe", detached: process.platform !== "win32" });
  let stdout = Buffer.alloc(0), stdoutBytes = 0, stderrBytes = 0, failure: Error | undefined;
  const stderr = createHash("sha256");
  let pending: { id: number; resolve(value: Record<string, unknown>): void; reject(error: Error): void } | undefined;
  const kill = () => { if (child.pid) { try { process.kill(process.platform === "win32" ? child.pid : -child.pid, "SIGKILL"); } catch { /* exited */ } } };
  const fail = (message: string) => { failure ??= new Error(message); pending?.reject(failure); kill(); };
  const closed = new Promise<{ exitCode: number | null; signal: string | null }>(resolveClose => child.once("close", (exitCode, signal) => resolveClose({ exitCode, signal })));
  child.once("error", () => fail("offline probe spawn failed"));
  child.once("exit", () => { kill(); if (pending) fail("offline probe exited before response"); });
  child.stdin.on("error", () => fail("offline probe input closed"));
  child.stderr.on("data", (data: Buffer) => { stderrBytes += data.length; if (stderrBytes > 65536) fail("offline probe stderr limit exceeded"); else stderr.update(data); });
  child.stdout.on("data", (data: Buffer) => {
    stdoutBytes += data.length;
    if (stdoutBytes > 262144) { fail("offline probe stdout limit exceeded"); return; }
    stdout = Buffer.concat([stdout, data]);
    for (let newline = stdout.indexOf(10); newline >= 0; newline = stdout.indexOf(10)) {
      const line = stdout.subarray(0, newline); stdout = stdout.subarray(newline + 1);
      try {
        const value: unknown = JSON.parse(line.toString());
        if (!value || typeof value !== "object" || Array.isArray(value)) throw new Error();
        const message = value as Record<string, unknown>;
        // No server requests are executed; unknown notifications cannot convey authority.
        if (!("id" in message)) continue;
        if (!pending || message.id !== pending.id || ("method" in message) || (("result" in message) === ("error" in message))) throw new Error();
        const current = pending; pending = undefined; current.resolve(message);
      } catch { fail("offline probe invalid or unsolicited protocol response"); return; }
    }
  });
  const lifetime = setTimeout(() => fail("offline probe timed out"), 20000);
  const protocolChecks: CodexProtocolCheck[] = [];
  let authRequired: boolean | undefined;
  try {
    for (const request of wire(join(root, "work"))) {
      if (failure) throw failure;
      if (!("id" in request)) { child.stdin.write(JSON.stringify(request) + "\n"); continue; }
      const response = await new Promise<Record<string, unknown>>((resolveResponse, reject) => {
        const timer = setTimeout(() => fail("offline probe response timed out"), 4000);
        pending = { id: request.id as number, resolve: value => { clearTimeout(timer); resolveResponse(value); }, reject: error => { clearTimeout(timer); reject(error); } };
        child.stdin.write(JSON.stringify(request) + "\n");
      });
      const passed = !("error" in response);
      protocolChecks.push({ method: request.method as string, status: passed ? "passed" : "rejected" });
      if (!passed) break;
      if (request.method === "account/read") {
        const result = response.result;
        if (!result || typeof result !== "object" || typeof (result as Record<string, unknown>).requiresOpenaiAuth !== "boolean") throw new Error("offline probe account response is unrecognized");
        authRequired = (result as { requiresOpenaiAuth: boolean }).requiresOpenaiAuth;
      }
    }
    if (failure) throw failure;
    child.stdin.end();
    const grace = setTimeout(kill, 1000);
    const outcome = await closed; clearTimeout(grace);
    return { protocolChecks, authRequired, hostedTurnAvailable: false, ...outcome, stderrSha256: stderr.digest("hex") };
  } finally { clearTimeout(lifetime); kill(); await closed; }
}
/** Exact observed 0.149.0 offline methods only. This never enables a hosted turn. */
export async function probeExactCodexWorker(input: CodexProbeInput): Promise<CodexProbeResult> {
  if (process.platform !== "darwin" || process.arch !== "arm64") throw new Error("exact offline supply supports darwin-arm64 only");
  const supply = await verifyExactSupply({ executablePath: input.executablePath });
  const root = await privateScratch(input);
  try {
    const profile = `(version 1)\n(allow default)\n(deny network*)\n(deny file-write*)\n(allow file-write* (subpath ${JSON.stringify(root)}))\n(deny file-read* (subpath "/Users"))\n(deny file-read* (subpath ${JSON.stringify(homedir())}))\n(allow file-read* (subpath ${JSON.stringify(root)}))\n(allow file-read* (literal ${JSON.stringify(supply.canonicalPath)}))\n(deny mach-lookup (global-name "com.apple.securityd"))\n`;
    const profilePath = join(root, "offline.sb");
    await writeFile(profilePath, profile, { mode: 0o600, flag: "wx" });
    await revalidateExactSupply(supply);
    const result = await exchange("/usr/bin/sandbox-exec", ["-f", profilePath, supply.canonicalPath, "-c", "features.plugins=false"], root);
    return { evidenceClass: "accepted-supply-offline-probe", ...result, supply: { sha256: supply.sha256, version: supply.version, signatureStatus: supply.signatureStatus } };
  } finally { await rm(root, { recursive: true, force: true }); }
}
/** Explicit untrusted fixture seam; no supply acceptance or offline sandbox claim. */
export async function runControlledCodexProbeForTests(input: CodexProbeInput & { args: readonly string[] }): Promise<CodexProbeResult> {
  const root = await privateScratch(input);
  try { return { evidenceClass: "controlled-fixture", ...await exchange(input.executablePath, input.args, root) }; }
  finally { await rm(root, { recursive: true, force: true }); }
}

/** Private supplier source composition. This is never used by the public worker route. */
export async function createNativeSupplierTransport(input:{executable:string;args:readonly string[];authoritySecret:Buffer}):Promise<import("./codex-session.js").CodexSessionTransport> {
  const {loadNativeAdmissionBinding}=await import("@chirality/native-admission");
  const native=loadNativeAdmissionBinding(true);if(native.state!=="available")throw new Error("Supplier authority native package unavailable");
  const spawned=native.value.spawnSupplier(input.executable,input.args,input.authoritySecret);if(spawned.state!=="available")throw new Error("Supplier authority spawn unavailable");
  const child=spawned.value;let closing:Promise<void>|undefined;
  return {stdin:child.stdin,stdout:child.stdout,close:()=>closing??=retireNativeSupplier(child)};
}
