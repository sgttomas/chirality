import { spawn, type ChildProcessWithoutNullStreams } from "node:child_process";
import { randomUUID } from "node:crypto";
import { RuntimeError, type DelegatedHarnessProcessSupervisorPort, type WorkerHandle, type WorkerResult } from "@chirality/runtime-contracts";

import { DescendantTracker } from "./descendant-tracker.js";

export interface ProcessSupervisorOptions {
  command: string;
  args?: readonly string[];
  cwd?: string;
  env?: NodeJS.ProcessEnv;
  shutdownTimeoutMs?: number;
  maxOutputBytes?: number;
  maxRunMs?: number;
  maxWorkers?: number;
}
interface Entry { child: ChildProcessWithoutNullStreams; handle: WorkerHandle; done: Promise<WorkerResult>; tracker?: DescendantTracker }
/** Commands are installed by trusted broker configuration, never selected by callers. */
export class ProcessSupervisor implements DelegatedHarnessProcessSupervisorPort {
  private readonly entries = new Map<string, Entry>();
  private closed = false;
  constructor(private readonly options: ProcessSupervisorOptions) {
    if (!options.command || [options.shutdownTimeoutMs ?? 500, options.maxRunMs ?? 30000, options.maxOutputBytes ?? 65536, options.maxWorkers ?? 64].some(n => !Number.isSafeInteger(n) || n < 1 || n > 2147483647)) throw new Error("invalid supervisor configuration");
  }
  async acquire(workerId: string, input: string): Promise<WorkerHandle> {
    if (this.closed) throw new Error("supervisor closed");
    if (!/^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$/.test(workerId) || typeof input !== "string" || Buffer.byteLength(input) > 65536) throw new Error("invalid worker request");
    if (this.entries.has(workerId)) throw new Error("worker already acquired");
    if (this.entries.size >= (this.options.maxWorkers ?? 64)) throw new Error("worker capacity exceeded; retire cached workers");
    const child = spawn(this.options.command, [...(this.options.args ?? [])], {
      cwd: this.options.cwd, env: this.options.env ?? {}, shell: false, stdio: "pipe",
      detached: process.platform !== "win32",
    });
    const handle: WorkerHandle = { workerId, generation: randomUUID(), pid: child.pid ?? 0, state: "running" };
    const kill = () => { if (child.pid) { try { process.kill(process.platform === "win32" ? child.pid : -child.pid, "SIGKILL"); } catch { /* exited */ } } };
    const lifetime = setTimeout(kill, this.options.maxRunMs ?? 30000);
    child.once("exit", kill); // A finished leader must not leave background descendants behind.
    let stdout: Buffer = Buffer.alloc(0), stderr: Buffer = Buffer.alloc(0);
    const limit = this.options.maxOutputBytes ?? 65536;
    const append = (old: Buffer, chunk: Buffer): Buffer => { if (old.length + chunk.length > limit) kill(); return Buffer.concat([old, chunk]).subarray(0, limit); };
    child.stdout.on("data", (chunk: Buffer) => { stdout = append(stdout, chunk); });
    child.stderr.on("data", (chunk: Buffer) => { stderr = append(stderr, chunk); });
    child.stdin.on("error", () => { /* worker may exit before consuming input */ });
    const done = new Promise<WorkerResult>((resolve) => {
      child.once("error", () => { stderr = append(stderr, Buffer.from("worker spawn failed")); });
      child.once("close", (exitCode, signal) => {
        clearTimeout(lifetime);
        handle.state = "exited";
        resolve({ worker: { ...handle }, exitCode, signal, stdout: stdout.toString(), stderr: stderr.toString() });
      });
    });
    const entry: Entry = { child, handle, done };
    this.entries.set(workerId, entry);
    try {
      await new Promise<void>((resolve, reject) => { child.once("spawn", resolve); child.once("error", reject); });
      entry.tracker = new DescendantTracker({ leaderPid: child.pid!, maxDurationMs: Math.min(3600000, Math.max(1000, (this.options.maxRunMs ?? 30000) + 5000)) });
      await entry.tracker.start();
    } catch {
      kill();
      await done;
      await entry.tracker?.stop();
      if (this.entries.get(workerId) === entry) this.entries.delete(workerId);
      throw new Error("worker spawn failed");
    }
    child.stdin.end(input);
    return { ...handle };
  }
  async inventory(): Promise<readonly WorkerHandle[]> { return [...this.entries.values()].map(e => ({ ...e.handle })); }
  private entry(workerId: string, generation: string): Entry {
    const entry = this.entries.get(workerId);
    if (!entry || entry.handle.generation !== generation) throw new Error("unknown or stale worker generation");
    return entry;
  }
  async reconnect(workerId: string, generation: string): Promise<WorkerHandle> { return { ...this.entry(workerId, generation).handle }; }
  async wait(workerId: string, generation: string): Promise<WorkerResult> { return this.entry(workerId, generation).done; }
  async retire(workerId: string, generation: string): Promise<void> {
    const entry = this.entry(workerId, generation);
    const signal = (value: NodeJS.Signals) => {
      if (!entry.child.pid) return;
      try { process.kill(process.platform === "win32" ? entry.child.pid : -entry.child.pid, value); }
      catch (error) { if ((error as NodeJS.ErrnoException).code !== "ESRCH") throw error; }
    };
    await entry.tracker?.sample().catch(() => {});
    // Signal the process group even when its leader exited, to retire descendants.
    signal("SIGTERM");
    let timer: ReturnType<typeof setTimeout> | undefined;
    await Promise.race([entry.done, new Promise<void>(resolve => { timer = setTimeout(resolve, this.options.shutdownTimeoutMs ?? 500); })]);
    clearTimeout(timer);
    signal("SIGKILL");
    await entry.done;
    const deadline = Date.now() + (this.options.shutdownTimeoutMs ?? 500);
    let reconciliation = await entry.tracker?.reconcile();
    while (reconciliation?.ownedGroup.length && Date.now() < deadline) {
      await new Promise(resolve => setTimeout(resolve, 20));
      reconciliation = await entry.tracker?.reconcile();
    }
    if (!reconciliation || reconciliation.failure || reconciliation.ownedGroup.length || reconciliation.detached.length || reconciliation.identityChanged.length) {
      throw new RuntimeError("ENGINE_UNAVAILABLE", "Observed descendants require reconciliation", 503, {
        reason: "DESCENDANT_RECONCILIATION_REQUIRED", observedCount: reconciliation?.observed ?? 0,
        survivingGroupCount: reconciliation?.ownedGroup.length ?? 0,
        detachedPids: reconciliation?.detached.slice(0, 32).map(row => row.pid) ?? [],
        identityChangedCount: reconciliation?.identityChanged.length ?? 0,
        censusFailed: !reconciliation || Boolean(reconciliation.failure),
        limitations: reconciliation?.limitations ?? ["NO_PROCESS_CENSUS"]
      });
    }
    await entry.tracker?.stop();
    if (this.entries.get(workerId) === entry) this.entries.delete(workerId);
  }
  async close(): Promise<void> {
    this.closed = true;
    await Promise.all([...this.entries.values()].map(e => this.retire(e.handle.workerId, e.handle.generation)));
  }
}
