import { describe, expect, it } from "vitest";
import { RuntimeError } from "@chirality/runtime-contracts";
import { mkdtemp, lstat, rm, symlink } from "node:fs/promises";
import { tmpdir } from "node:os";
import { realpathSync } from "node:fs";
import { join } from "node:path";
import { createConnection } from "node:net";
import { spawn } from "node:child_process";
import { once } from "node:events";
import { createHmac } from "node:crypto";
import { ProcessSupervisor } from "../packages/core/src/process-supervisor.js";
import { startSupervisorServer, SupervisorClient } from "../packages/daemon/src/supervisor-server.js";

async function fixture(code: string, maxRunMs = 2000) {
  const dir = await mkdtemp(join(realpathSync(tmpdir()), "sup-"));
  const supervisor = new ProcessSupervisor({ command: process.execPath, args: ["-e", code], env: {}, maxRunMs, shutdownTimeoutMs: 40 });
  const socketPath = join(dir, "control.sock");
  const server = await startSupervisorServer({ socketPath, supervisor });
  const client = new SupervisorClient({ socketPath, credential: server.credential });
  return { dir, supervisor, socketPath, server, client, async close() { await supervisor.close(); await server.close(); await rm(dir, { recursive: true, force: true }); } };
}
function signed(secret: string, r: Record<string, unknown>): string {
  return JSON.stringify({ ...r, token: createHmac("sha256", secret).update(JSON.stringify([r.owner, r.epoch, r.op, r.workerId ?? null, r.generation, r.input ?? null])).digest("hex") }) + "\n";
}
function raw(socketPath: string, value: string): Promise<string> {
  return new Promise((resolve, reject) => {
    const socket = createConnection(socketPath); let output = "";
    socket.on("error", reject); socket.on("connect", () => socket.write(value));
    socket.on("data", data => { output += data.toString(); }); socket.on("end", () => resolve(output));
  });
}
describe("private process supervisor", () => {
  it("runs trusted child through socket, caches terminal result, fences and retires", async () => {
    const f = await fixture('let s="";process.stdin.on("data",x=>s+=x);process.stdin.on("end",()=>process.stdout.write(s.toUpperCase()))');
    try {
      expect((await lstat(f.dir)).mode & 0o777).toBe(0o700);
      expect((await lstat(f.socketPath)).mode & 0o777).toBe(0o600);
      const h = await f.client.acquire("turn_1", "hello");
      expect(h.pid).toBeGreaterThan(0);
      await expect(f.client.acquire("turn_1", "different")).rejects.toThrow();
      await expect(f.client.wait(h.workerId, "stale")).rejects.toThrow();
      expect((await f.client.wait(h.workerId, h.generation)).stdout).toBe("HELLO");
      expect((await f.client.wait(h.workerId, h.generation)).exitCode).toBe(0);
      expect((await f.client.reconnect(h.workerId, h.generation)).state).toBe("exited");
      expect(await f.client.inventory()).toHaveLength(1);
      await f.client.retire(h.workerId, h.generation);
      expect(await f.client.inventory()).toHaveLength(0);
      await expect(f.client.reconnect(h.workerId, h.generation)).rejects.toThrow();
      expect(() => process.kill(h.pid, 0)).toThrow();
    } finally { await f.close(); }
  });
  it("checks token owner epoch generation and operation on every request", async () => {
    const f = await fixture('setInterval(()=>{},1000)');
    try {
      for (const field of ["token", "owner", "epoch"] as const) {
        const bad = new SupervisorClient({ socketPath: f.socketPath, credential: { ...f.server.credential, [field]: "invalid" } });
        await expect(bad.inventory()).rejects.toThrow();
      }
      const request = { ...f.server.credential, op: "inventory", generation: null };
      expect(JSON.parse(await raw(f.socketPath, signed(f.server.credential.token, { ...request, op: "exec", command: "anything" }))).ok).toBe(false);
      expect(JSON.parse(await raw(f.socketPath, signed(f.server.credential.token, { ...request, generation: "stale" }))).ok).toBe(false);
      expect(JSON.parse(await raw(f.socketPath, "x".repeat(300000) + "\n")).ok).toBe(false);
      await expect(f.client.acquire("../bad", "x")).rejects.toThrow();
      expect(await f.client.inventory()).toHaveLength(0);
    } finally { await f.close(); }
  });
  it("does not replace active owner; a new server epoch invalidates previous token", async () => {
    const f = await fixture('process.exit(0)');
    let second: Awaited<ReturnType<typeof startSupervisorServer>> | undefined;
    try {
      await expect(startSupervisorServer({ socketPath: f.socketPath, supervisor: f.supervisor, recoverStale: true })).rejects.toThrow("owned");
      await f.server.close();
      second = await startSupervisorServer({ socketPath: f.socketPath, supervisor: f.supervisor, recoverStale: true });
      expect(second.credential.epoch).not.toBe(f.server.credential.epoch);
      await expect(f.client.inventory()).rejects.toThrow();
      expect(await new SupervisorClient({ socketPath: f.socketPath, credential: second.credential }).inventory()).toHaveLength(0);
    } finally { await f.supervisor.close(); await second?.close(); await rm(f.dir, { recursive: true, force: true }); }
  });
  it("recovers a real crashed socket owner with new credentials", async () => {
    const f = await fixture('process.exit(0)');
    let replacement: Awaited<ReturnType<typeof startSupervisorServer>> | undefined;
    let child: ReturnType<typeof spawn> | undefined;
    try {
      await f.server.close();
      child = spawn(process.execPath, ["-e", 'require("node:net").createServer(()=>{}).listen(process.argv[1],()=>process.stdout.write("ready"))', f.socketPath], { stdio: ["ignore", "pipe", "pipe"], env: {} });
      await once(child.stdout!, "data");
      const closed = once(child, "close"); child.kill("SIGKILL"); await closed;
      expect((await lstat(f.socketPath)).isSocket()).toBe(true);
      replacement = await startSupervisorServer({ socketPath: f.socketPath, supervisor: f.supervisor, recoverStale: true });
      await expect(f.client.inventory()).rejects.toThrow();
      expect(await new SupervisorClient({ socketPath: f.socketPath, credential: replacement.credential }).inventory()).toEqual([]);
    } finally { child?.kill("SIGKILL"); await f.supervisor.close(); await replacement?.close(); await rm(f.dir, { recursive: true, force: true }); }
  });
  it("binds authentication to the operation and worker generation", async () => {
    const f = await fixture('process.exit(0)');
    try {
      const h = await f.client.acquire("auth", "");
      const frame = JSON.parse(signed(f.server.credential.token, { ...f.server.credential, op: "wait", workerId: h.workerId, generation: h.generation }));
      frame.generation = "different";
      expect(JSON.parse(await raw(f.socketPath, JSON.stringify(frame) + "\n")).ok).toBe(false);
      frame.generation = h.generation; frame.op = "retire";
      expect(JSON.parse(await raw(f.socketPath, JSON.stringify(frame) + "\n")).ok).toBe(false);
      expect((await f.client.wait(h.workerId, h.generation)).exitCode).toBe(0);
    } finally { await f.close(); }
  });
  it("bounds worker lifetime and kills stubborn children during retirement", async () => {
    const f = await fixture('process.on("SIGTERM",()=>{});setInterval(()=>{},1000)', 100);
    try {
      const h = await f.client.acquire("timeout", "");
      expect((await f.client.wait(h.workerId, h.generation)).signal).toBe("SIGKILL");
      expect(() => process.kill(h.pid, 0)).toThrow();
      const other = await f.client.acquire("retire", "");
      await f.client.retire(other.workerId, other.generation);
      expect(() => process.kill(other.pid, 0)).toThrow();
    } finally { await f.close(); }
  });
  it("caps output and terminates flooding child", async () => {
    const f = await fixture('setInterval(()=>process.stdout.write("x".repeat(65536)),1)');
    try { const h = await f.client.acquire("flood", ""); const r = await f.client.wait(h.workerId, h.generation); expect(Buffer.byteLength(r.stdout)).toBeLessThanOrEqual(65536); expect(r.signal).toBe("SIGKILL"); }
    finally { await f.close(); }
  });
  it("rejects spawn failure without returning a phantom worker and bounds retained inventory", async () => {
    const missing = new ProcessSupervisor({ command: "/nonexistent-chirality-fixture", env: {} });
    await expect(missing.acquire("missing", "")).rejects.toThrow("spawn failed");
    expect(await missing.inventory()).toEqual([]);
    await missing.close();
    const limited = new ProcessSupervisor({ command: process.execPath, args: ["-e", "process.exit(0)"], maxWorkers: 1, env: {} });
    try {
      const acquiring = limited.acquire("one.valid-id", "");
      await expect(limited.acquire("other", "")).rejects.toThrow("capacity");
      const h = await acquiring; await limited.wait(h.workerId, h.generation);
      await expect(limited.acquire("other", "")).rejects.toThrow("capacity");
      await limited.retire(h.workerId, h.generation);
      expect((await limited.acquire("other", "")).pid).toBeGreaterThan(0);
    } finally { await limited.close(); }
  });
  it("kills inherited-pipe descendants when the leader exits normally", async () => {
    const f = await fixture('const c=require("node:child_process").spawn(process.execPath,["-e","setInterval(()=>{},1000)"],{stdio:["ignore","inherit","inherit"]}); process.stdout.write(String(c.pid)); setTimeout(()=>process.exit(0),30)', 2000);
    try {
      const h = await f.client.acquire("descendant", "");
      const r = await f.client.wait(h.workerId, h.generation);
      expect(r.exitCode).toBe(0); const pid = Number(r.stdout); expect(pid).toBeGreaterThan(0);
      // Reaping is asynchronous on Unix; require eventual process disappearance.
      await expect.poll(() => { try { process.kill(pid, 0); return false; } catch { return true; } }).toBe(true);
    } finally { await f.close(); }
  });
  it("rejects symlink control directories", async () => {
    const f = await fixture('process.exit(0)');
    try { await symlink(f.dir, join(f.dir, "alias")); await expect(startSupervisorServer({ socketPath: join(f.dir, "alias", "other.sock"), supervisor: f.supervisor })).rejects.toThrow("symlink"); }
    finally { await f.close(); }
  });
});

it("keeps login commands on the private authenticated capability channel", async () => {
  const dir = await mkdtemp(join(realpathSync(tmpdir()), "sup-login-"));
  const workers = new ProcessSupervisor({ command: process.execPath, args: ["-e", "process.exit(0)"], env: {} });
  let starts = 0, cancels = 0;
  const server = await startSupervisorServer({ socketPath: join(dir, "s.sock"), supervisor: workers, login: {
    async startLogin() { starts++; return { loginId: "fixture-login", authUrl: "https://auth.openai.com/authorize" }; },
    async status() { return { state: "pending", evidenceClass: "controlled-fixture" }; },
    async cancel() { cancels++; }
  } });
  try {
    const client = new SupervisorClient({ socketPath: join(dir, "s.sock"), credential: server.credential });
    const bad = new SupervisorClient({ socketPath: join(dir, "s.sock"), credential: { ...server.credential, token: "0".repeat(64) } });
    await expect(bad.startLogin()).rejects.toThrow();
    expect(starts).toBe(0);
    expect(await client.startLogin()).toMatchObject({ loginId: "fixture-login" });
    expect(await client.loginStatus()).toMatchObject({ state: "pending" });
    await client.cancelLogin();
    expect([starts, cancels]).toEqual([1, 1]);
    expect(await workers.inventory()).toEqual([]);
  } finally { await workers.close(); await server.close(); await rm(dir, { recursive: true, force: true }); }
});

it("preserves bounded descendant reconciliation diagnostics through the private socket", async () => {
  const f = await fixture('process.stdin.resume(); setTimeout(()=>{},1000)');
  try {
    const handle = await f.client.acquire("diagnostic", "");
    const retire = f.supervisor.retire.bind(f.supervisor);
    f.supervisor.retire = async (workerId, generation) => {
      await retire(workerId, generation);
      throw new RuntimeError("ENGINE_UNAVAILABLE", "unsafe raw message", 503, { reason: "DESCENDANT_RECONCILIATION_REQUIRED", detachedPids: [123, -1, "secret"], observedCount: 2, limitations: ["UNOBSERVED_DETACH_BETWEEN_POLLS", "secret key data"], privateCredential: "NEVER_FORWARD" });
    };
    await expect(f.client.retire(handle.workerId, handle.generation)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE", message: "Observed descendants require reconciliation", details: { reason: "DESCENDANT_RECONCILIATION_REQUIRED", detachedPids: [123], observedCount: 2, limitations: ["UNOBSERVED_DETACH_BETWEEN_POLLS"], signalAuthority: "NONE" } });
  } finally { await f.close(); }
});
