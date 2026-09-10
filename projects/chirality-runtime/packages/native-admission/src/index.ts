import { createRequire } from "node:module";
import { isAbsolute, normalize } from "node:path";
import { Readable, Writable } from "node:stream";
import type { RuntimeAdmissionLease } from "@chirality/runtime-core";

export type NativeUnavailableReason = "platform-unsupported" | "api-unavailable" | "filesystem-unqualified" | "path-unsafe" | "lock-contended" | "inode-mismatch" | "descriptor-closure-unqualified" | "spawn-failed" | "wait-unavailable" | "native-package-unqualified";
export type NativeAuthorityResult<T> = { state: "available"; value: T } | { state: "unavailable"; reason: NativeUnavailableReason };
export interface NativeSupplierExit { exitCode: number | null; signal: number | null }
interface RawLease { device: bigint; inode: bigint; held: boolean; created: boolean; close(): void }
interface RawChild {
  pid?: number; read(): Promise<Buffer>; write(bytes: Buffer): Promise<void>; closeInput(): void;
  terminate(): void; kill(): void; wait(): Promise<NativeSupplierExit>;
  observeLeader?(): Promise<NativeSupplierExit>; reapLeader?(): Promise<NativeSupplierExit>; groupRetired?(): boolean;
}
interface Binding { acquire(directory: string, name: string): RawLease; spawnSupplier(executable: string, args: readonly string[], secret: Buffer, cwd?: string, environment?: readonly string[], processGroup?: boolean): RawChild }
export interface NativeSupplierSpawnOptions { cwd: string; environment: Readonly<Record<"HOME" | "CODEX_HOME" | "TMPDIR" | "PATH" | "LANG", string>>; processGroup: true }
interface NativeSupplierPipes { readonly stdin: Writable; readonly stdout: Readable; terminate(): void; kill(): void; closeInput(): void }
export interface NativeSupplierChild extends NativeSupplierPipes { readonly pid?: number; wait(): Promise<NativeSupplierExit> }
export interface NativeGroupedSupplierChild extends NativeSupplierPipes { readonly pid: number; observeLeader(): Promise<NativeSupplierExit>; reapLeader(): Promise<NativeSupplierExit>; groupRetired(): boolean }
export interface NativeAdmissionBinding {
  acquire(directory: string): NativeAuthorityResult<RuntimeAdmissionLease>;
  /** Historical non-grouped transport retained for controlled probes. */
  spawnSupplier(executable: string, args: readonly string[], secret: Buffer): NativeAuthorityResult<NativeSupplierChild>;
  /** Production candidate transport with explicit cwd, closed env and owned group. */
  spawnGroupedSupplier(executable: string, args: readonly string[], secret: Buffer, options: NativeSupplierSpawnOptions): NativeAuthorityResult<NativeGroupedSupplierChild>;
}

function unavailable<T>(reason: NativeUnavailableReason): NativeAuthorityResult<T> { return { state: "unavailable", reason }; }
const reasons: readonly string[] = ["platform-unsupported", "api-unavailable", "filesystem-unqualified", "path-unsafe", "lock-contended", "inode-mismatch", "descriptor-closure-unqualified", "spawn-failed", "wait-unavailable", "native-package-unqualified"];
function translate<T>(fn: () => T): NativeAuthorityResult<T> { try { return { state: "available", value: fn() }; } catch (error) { const reason = error && typeof error === "object" && "code" in error ? error.code : undefined; return unavailable(typeof reason === "string" && reasons.includes(reason) ? reason as NativeUnavailableReason : "native-package-unqualified"); } }
function path(value: unknown): asserts value is string { if (typeof value !== "string" || !isAbsolute(value) || normalize(value) !== value || Buffer.byteLength(value) > 4095 || /[\x00-\x1f]/.test(value)) throw Object.assign(new Error("invalid-native-path"), { code: "path-unsafe" }); }
function spawnOptions(value: NativeSupplierSpawnOptions): { cwd: string; environment: string[] } {
  if (!value || typeof value !== "object" || Array.isArray(value) || Object.keys(value).sort().join(",") !== "cwd,environment,processGroup" || value.processGroup !== true) throw new Error("invalid-native-bootstrap");
  path(value.cwd);
  const environment = value.environment;
  const keys = ["CODEX_HOME", "HOME", "LANG", "PATH", "TMPDIR"] as const;
  if (!environment || typeof environment !== "object" || Array.isArray(environment) || Object.keys(environment).sort().join(",") !== keys.join(",")) throw new Error("invalid-native-bootstrap");
  for (const key of ["CODEX_HOME", "HOME", "TMPDIR"] as const) path(environment[key]);
  if (environment.PATH !== "/usr/bin:/bin:/usr/sbin:/sbin" || environment.LANG !== "en_US.UTF-8") throw new Error("invalid-native-bootstrap");
  return { cwd: value.cwd, environment: keys.map(key => `${key}=${environment[key]}`) };
}
function validateExit(result: NativeSupplierExit): NativeSupplierExit {
  if (!result || Object.keys(result).sort().join(",") !== "exitCode,signal" || !(result.exitCode === null || Number.isInteger(result.exitCode)) || !(result.signal === null || Number.isInteger(result.signal)) || (result.exitCode === null) === (result.signal === null)) throw new Error("wait-unavailable");
  return result;
}
function pipes(child: RawChild): NativeSupplierPipes {
  let reading = false;
  const stdout = new Readable({ read() { if (reading) return; reading = true; void child.read().then(bytes => { reading = false; if (!Buffer.isBuffer(bytes)) throw new Error("invalid-native-read"); this.push(bytes.length ? bytes : null); }, () => { reading = false; this.destroy(new Error("native-read-unavailable")); }); } });
  const stdin = new Writable({ write(chunk: Buffer, _encoding, callback) { void child.write(Buffer.from(chunk)).then(() => callback(), () => callback(new Error("native-write-unavailable"))); }, final(callback) { try { child.closeInput(); callback(); } catch { callback(new Error("native-input-unavailable")); } } });
  return { stdin, stdout, closeInput: () => { stdin.end(); }, terminate: () => child.terminate(), kill: () => child.kill() };
}

/** Test injection proves wrapper behavior only; it never establishes native qualification. */
export function wrapNativeAdmissionBinding(raw: unknown): NativeAdmissionBinding {
  const binding = raw as Binding;
  const spawn = (executable: string, args: readonly string[], secret: Buffer, options?: NativeSupplierSpawnOptions): NativeAuthorityResult<NativeSupplierChild | NativeGroupedSupplierChild> => translate(() => {
    path(executable);
    if (!Array.isArray(args) || args.length > 128 || args.some(value => typeof value !== "string" || Buffer.byteLength(value) > 4096 || /[\x00-\x1f]/.test(value)) || !Buffer.isBuffer(secret) || secret.length !== 32 || typeof binding?.spawnSupplier !== "function") throw new Error("invalid-native-bootstrap");
    const strict = options === undefined ? undefined : spawnOptions(options);
    const child = strict ? binding.spawnSupplier(executable, args, secret, strict.cwd, strict.environment, true) : binding.spawnSupplier(executable, args, secret);
    const required = ["read", "write", "closeInput", "terminate", "kill", ...(strict ? ["observeLeader", "reapLeader", "groupRetired"] : ["wait"])];
    if (!child || required.some(key => typeof (child as unknown as Record<string, unknown>)[key] !== "function") || (strict && (!Number.isSafeInteger(child.pid) || child.pid! <= 0))) throw new Error("invalid-native-child");
    const streams = pipes(child);
    if (strict) {
      let observed: Promise<NativeSupplierExit> | undefined, reaped: Promise<NativeSupplierExit> | undefined;
      return Object.freeze({ pid: child.pid!, ...streams, observeLeader: () => observed ??= child.observeLeader!().then(validateExit), reapLeader: () => reaped ??= child.reapLeader!().then(validateExit), groupRetired: () => child.groupRetired!() === true });
    }
    let waited: Promise<NativeSupplierExit> | undefined;
    return Object.freeze({ ...streams, ...(child.pid === undefined ? {} : { pid: child.pid }), wait: () => waited ??= child.wait().then(validateExit, () => { throw new Error("wait-unavailable"); }) });
  });
  return {
    acquire(directory) { return translate(() => { path(directory); if (!binding || typeof binding.acquire !== "function") throw new Error("invalid-native-binding"); const lease = binding.acquire(directory, "runtime-admission-authority.lock"); if (!lease || typeof lease.device !== "bigint" || lease.device < 0n || typeof lease.inode !== "bigint" || lease.inode < 0n || lease.held !== true || typeof lease.created !== "boolean" || typeof lease.close !== "function") throw new Error("invalid-native-lease"); let closed = false; return Object.freeze({ device: lease.device, inode: lease.inode, created: lease.created, get held() { return !closed && lease.held === true; }, close() { if (closed) throw new Error("native-lease-already-closed"); closed = true; lease.close(); } }); }); },
    spawnSupplier(executable, args, secret) { return spawn(executable, args, secret) as NativeAuthorityResult<NativeSupplierChild>; },
    spawnGroupedSupplier(executable, args, secret, options) { return spawn(executable, args, secret, options) as NativeAuthorityResult<NativeGroupedSupplierChild>; }
  };
}

/** Importing the package never loads the addon. A later qualified composition must inject its trusted absolute packaged path. */
export function loadNativeAdmissionBinding(enabled: boolean, addonPath?: string): NativeAuthorityResult<NativeAdmissionBinding> {
  if (!enabled) return unavailable("native-package-unqualified");
  if (addonPath === undefined) return unavailable("native-package-unqualified");
  try { path(addonPath); } catch { return unavailable("path-unsafe"); }
  if (process.platform !== "darwin" || !["arm64", "x64"].includes(process.arch)) return unavailable("platform-unsupported");
  return translate(() => wrapNativeAdmissionBinding(createRequire(addonPath)(addonPath)));
}
