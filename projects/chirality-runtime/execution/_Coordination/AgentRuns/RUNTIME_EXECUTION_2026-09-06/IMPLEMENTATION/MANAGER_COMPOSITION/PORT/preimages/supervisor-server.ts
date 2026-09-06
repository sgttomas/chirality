import { createConnection, createServer, type Socket } from "node:net";
import { chmod, lstat, mkdir, unlink } from "node:fs/promises";
import { dirname, isAbsolute, parse, join } from "node:path";
import { randomBytes, randomUUID, timingSafeEqual, createHmac } from "node:crypto";
import type { CodexLoginStatus } from "./codex-login.js";
import { RuntimeError, type DelegatedHarnessProcessSupervisorPort, type WorkerHandle, type WorkerResult, type WorkerContinuity } from "@chirality/runtime-contracts";

function reconciliationDetails(value: unknown): Record<string, unknown> | undefined {
  if (!value || typeof value !== "object" || (value as Record<string, unknown>).reason !== "DESCENDANT_RECONCILIATION_REQUIRED") return undefined;
  const source = value as Record<string, unknown>, result: Record<string, unknown> = { reason: "DESCENDANT_RECONCILIATION_REQUIRED" };
  for (const key of ["observed", "observedCount", "scans", "detachedCount", "ownedGroupCount", "survivingGroupCount", "identityChangedCount"]) if (Number.isSafeInteger(source[key]) && (source[key] as number) >= 0) result[key] = source[key];
  for (const key of ["leaderObserved", "censusFailed"]) if (typeof source[key] === "boolean") result[key] = source[key];
  if (Array.isArray(source.detachedPids)) result.detachedPids = source.detachedPids.filter(value => Number.isSafeInteger(value) && value > 0).slice(0, 32);
  if (Array.isArray(source.limitations)) result.limitations = source.limitations.filter(value => typeof value === "string" && /^[A-Z_]{1,64}$/.test(value)).slice(0, 8);
  result.signalAuthority = "NONE";
  return result;
}

export interface SupervisorLoginPort { startLogin(): Promise<{ loginId: string; authUrl: string }>; status(): Promise<CodexLoginStatus>; cancel(): Promise<void> }
export interface SupervisorCredential { owner: string; epoch: string; token: string }
interface Options { socketPath: string; credential: SupervisorCredential; timeoutMs?: number }
const MAX_FRAME = 256 * 1024;
function requestToken(secret: string, r: Record<string, unknown>): string {
  return createHmac("sha256", secret).update(JSON.stringify([r.owner, r.epoch, r.op, r.workerId ?? null, r.generation, r.input ?? null])).digest("hex");
}
function validString(value: unknown, max = 128): value is string { return typeof value === "string" && value.length > 0 && value.length <= max; }
async function privateDirectory(path: string): Promise<void> {
  if (!isAbsolute(path)) throw new Error("socket path must be absolute");
  // Reject symlink components before creating anything inside the directory.
  let current = parse(path).root;
  for (const part of dirname(path).slice(current.length).split("/").filter(Boolean)) {
    current = join(current, part);
    try { if ((await lstat(current)).isSymbolicLink()) throw new Error("symlink socket ancestor"); }
    catch (error) { if ((error as NodeJS.ErrnoException).code !== "ENOENT") throw error; }
  }
  await mkdir(dirname(path), { recursive: true, mode: 0o700 });
  const st = await lstat(dirname(path));
  if (!st.isDirectory() || st.uid !== process.getuid?.() || (st.mode & 0o777) !== 0o700) throw new Error("socket directory must be owner-private 0700");
}
async function activeSocket(path: string): Promise<boolean> {
  return new Promise((resolve, reject) => {
    const socket = createConnection(path);
    socket.setTimeout(300);
    socket.once("connect", () => { socket.destroy(); resolve(true); });
    socket.once("timeout", () => { socket.destroy(); reject(new Error("socket owner probe timed out")); });
    socket.once("error", (error: NodeJS.ErrnoException) => { socket.destroy(); if (error.code === "ECONNREFUSED" || error.code === "ENOENT") resolve(false); else reject(error); });
  });
}
/** This credential is exclusively a daemon-to-supervisor capability. Never serialize it to public clients. */
export async function startSupervisorServer(options: { socketPath: string; supervisor: DelegatedHarnessProcessSupervisorPort; login?: SupervisorLoginPort; recoverStale?: boolean }): Promise<{ credential: SupervisorCredential; close(): Promise<void> }> {
  await privateDirectory(options.socketPath);
  try {
    const old = await lstat(options.socketPath);
    if (!old.isSocket() || old.uid !== process.getuid?.()) throw new Error("invalid existing socket owner");
    if (!options.recoverStale || await activeSocket(options.socketPath)) throw new Error("socket already owned");
    const again = await lstat(options.socketPath);
    if (again.ino !== old.ino || again.dev !== old.dev) throw new Error("socket changed during recovery");
    await unlink(options.socketPath);
  } catch (error) { if ((error as NodeJS.ErrnoException).code !== "ENOENT") throw error; }
  const credential: SupervisorCredential = { owner: `${process.getuid?.()}:${process.pid}`, epoch: randomUUID(), token: randomBytes(32).toString("hex") };
  let closing = false;
  const sockets = new Set<Socket>();
  const server = createServer(socket => {
    sockets.add(socket); socket.once("close", () => sockets.delete(socket));
    socket.on("error", () => {});
    socket.setTimeout(60000, () => socket.destroy());
    let data = Buffer.alloc(0), consumed = false;
    const respond = (value: unknown) => { const frame = JSON.stringify(value) + "\n"; socket.end(Buffer.byteLength(frame) <= MAX_FRAME ? frame : '{"ok":false,"error":"response too large"}\n'); };
    socket.on("data", chunk => {
      if (consumed) { socket.destroy(); return; }
      data = Buffer.concat([data, chunk]);
      if (data.length > MAX_FRAME) { consumed = true; respond({ ok: false, error: "request too large" }); return; }
      const newline = data.indexOf(10);
      if (newline < 0) return;
      consumed = true;
      void (async () => {
        try {
          if (closing || newline !== data.length - 1) throw new Error("invalid frame");
          const r = JSON.parse(data.subarray(0, newline).toString()) as Record<string, unknown>;
          if (!r || typeof r !== "object" || !validString(r.token, 64) || !/^[a-f0-9]{64}$/.test(r.token) || !timingSafeEqual(Buffer.from(r.token), Buffer.from(requestToken(credential.token, r))) || r.owner !== credential.owner || r.epoch !== credential.epoch) throw new Error("unauthorized supervisor request");
          const op = r.op;
          if (!["acquire", "inventory", "reconnect", "wait", "retire", "verify-hosted", "login-start", "login-status", "login-cancel"].includes(String(op))) throw new Error("unknown operation");
          let result: unknown;
          if (op === "login-start" || op === "login-status" || op === "login-cancel") {
            if (r.generation !== null || r.input !== undefined || options.login === undefined) throw new Error("Login service unavailable");
            if (op === "login-start") result = await options.login.startLogin();
            else if (op === "login-status") result = await options.login.status();
            else result = await options.login.cancel();
          }
          else if (op === "verify-hosted") {
            if (r.generation !== null || typeof r.input !== "string" || options.supervisor.verifyHostedBoundary === undefined) throw new Error("hosted boundary unavailable");
            await options.supervisor.verifyHostedBoundary(JSON.parse(r.input)); result = true;
          }
          else if (op === "inventory") { if (r.generation !== null) throw new Error("invalid generation"); result = await options.supervisor.inventory(); }
          else {
            if (!validString(r.workerId) || !/^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$/.test(r.workerId)) throw new Error("invalid worker");
            if (op === "acquire") {
              if (r.generation !== null || typeof r.input !== "string" || Buffer.byteLength(r.input) > 65536) throw new Error("invalid acquisition");
              result = await options.supervisor.acquire(r.workerId, r.input);
            } else {
              if (!validString(r.generation)) throw new Error("invalid generation");
              if (op === "reconnect") result = await options.supervisor.reconnect(r.workerId, r.generation);
              else if (op === "wait") result = await options.supervisor.wait(r.workerId, r.generation);
              else result = await options.supervisor.retire(r.workerId, r.generation);
            }
          }
          respond({ ok: true, result });
        } catch (error) {
          const details = error instanceof RuntimeError ? reconciliationDetails(error.details) : undefined;
          respond({ ok: false, error: "supervisor request rejected", ...(details ? { reconciliation: details } : {}) });
        }
      })();
    });
  });
  await new Promise<void>((resolve, reject) => { server.once("error", reject); server.listen(options.socketPath, resolve); });
  await chmod(options.socketPath, 0o600);
  const owned = await lstat(options.socketPath);
  return { credential, async close() {
    closing = true;
    for (const socket of sockets) socket.destroy();
    await new Promise<void>((resolve, reject) => server.close(error => error ? reject(error) : resolve()));
    try { const current = await lstat(options.socketPath); if (current.ino === owned.ino && current.dev === owned.dev) await unlink(options.socketPath); }
    catch (error) { if ((error as NodeJS.ErrnoException).code !== "ENOENT") throw error; }
  } };
}
export class SupervisorClient implements DelegatedHarnessProcessSupervisorPort {
  constructor(private readonly options: Options) {}
  async startLogin(): Promise<{ loginId: string; authUrl: string }> { return this.request("login-start") as Promise<{ loginId: string; authUrl: string }>; }
  async loginStatus(): Promise<CodexLoginStatus> { return this.request("login-status") as Promise<CodexLoginStatus>; }
  async cancelLogin(): Promise<void> { await this.request("login-cancel"); }
  async verifyHostedBoundary(identity: WorkerContinuity): Promise<void> {
    await this.request("verify-hosted", { input: JSON.stringify(identity) });
  }
  private async request(op: string, fields: Record<string, unknown> = {}): Promise<unknown> {
    const request = { owner: this.options.credential.owner, epoch: this.options.credential.epoch, op, generation: null, ...fields };
    const frame = JSON.stringify({ ...request, token: requestToken(this.options.credential.token, request) }) + "\n";
    if (Buffer.byteLength(frame) > MAX_FRAME) throw new Error("request too large");
    return new Promise((resolve, reject) => {
      const socket = createConnection(this.options.socketPath);
      let data = Buffer.alloc(0), done = false;
      const fail = (error: Error) => { if (!done) { done = true; socket.destroy(); reject(error); } };
      socket.setTimeout(this.options.timeoutMs ?? 65000, () => fail(new Error("supervisor timeout")));
      socket.once("error", fail); socket.once("connect", () => socket.write(frame));
      socket.on("data", chunk => {
        data = Buffer.concat([data, chunk]);
        if (data.length > MAX_FRAME) { fail(new Error("oversize supervisor response")); return; }
        if (!data.includes(10)) return;
        try { const response = JSON.parse(data.toString()); if (!response.ok) { const details = reconciliationDetails(response.reconciliation); if (details) throw new RuntimeError("ENGINE_UNAVAILABLE", "Observed descendants require reconciliation", 503, details); throw new Error("supervisor request rejected"); } done = true; socket.destroy(); resolve(response.result); }
        catch (error) { fail(error as Error); }
      });
      socket.once("close", () => { if (!done) fail(new Error("supervisor disconnected")); });
    });
  }
  async acquire(workerId: string, input: string): Promise<WorkerHandle> { return await this.request("acquire", { workerId, input }) as WorkerHandle; }
  async inventory(): Promise<readonly WorkerHandle[]> { return await this.request("inventory") as WorkerHandle[]; }
  async reconnect(workerId: string, generation: string): Promise<WorkerHandle> { return await this.request("reconnect", { workerId, generation }) as WorkerHandle; }
  async wait(workerId: string, generation: string): Promise<WorkerResult> { return await this.request("wait", { workerId, generation }) as WorkerResult; }
  async retire(workerId: string, generation: string): Promise<void> { await this.request("retire", { workerId, generation }); }
}
