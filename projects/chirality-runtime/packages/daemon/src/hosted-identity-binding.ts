import { constants } from "node:fs";
import { lstat, open, readdir, realpath, rename, unlink } from "node:fs/promises";
import { createHash, randomBytes, randomUUID } from "node:crypto";
import { isAbsolute, join, resolve } from "node:path";
import type { WorkerContinuity } from "@chirality/runtime-contracts";

const SCHEMA = "chirality.runtime.hosted-identity-binding/v1" as const;
const FILE_NAME = "hosted-identity-binding.json";
const LOCK_NAME = "hosted-identity-binding.lock";
const HEX = /^[a-f0-9]{64}$/;
const OPAQUE = /^[\x21-\x7e]{1,128}$/;
const HANDLE = /^rhb_[A-Za-z0-9_-]{43}$/;
const RECORD_KEYS = ["schema", "accountId", "accountEpoch", "accountUserId", "providerWorkspaceId", "supplierGeneration", "identityGeneration", "snapshotDigest", "runtimeAuthorityId", "canonicalRoot", "policyDigest", "state", "fenceReason", "digest"] as const;

export interface HostedIdentitySnapshot {
  accountUserId: string;
  providerWorkspaceId: string;
  supplierGeneration: string;
  identityGeneration: string;
  snapshotDigest: string;
}

export interface LiveHostedAuthority {
  /** Must fail unless the freshly validated snapshot still has live controller and kernel-lease authority. */
  assertLive(): void;
}

export type HostedIdentityFenceReason = "sign-out" | "switch" | "revoke" | "identity-change";

export type HostedIdentityBindingObservation =
  | { state: "absent" }
  | { state: "active" | "fenced"; accountId: string; accountEpoch: number; fenceReason: HostedIdentityFenceReason | null };

interface BindingRecord {
  schema: typeof SCHEMA;
  accountId: string;
  accountEpoch: number;
  accountUserId: string;
  providerWorkspaceId: string;
  supplierGeneration: string;
  identityGeneration: string;
  snapshotDigest: string;
  runtimeAuthorityId: string;
  canonicalRoot: string;
  policyDigest: string;
  state: "active" | "fenced";
  fenceReason: HostedIdentityFenceReason | null;
  digest: string;
}

type RecordBody = Omit<BindingRecord, "digest">;

export interface HostedIdentityBindingOptions {
  privateDirectory: string;
  canonicalRoot: string;
  policyDigest: string;
  runtimeAuthorityId: string;
  /** Test seam; production uses 32 cryptographically random bytes. */
  randomHandle?: () => Buffer;
}

function custodyError(): Error { return new Error("hosted-identity-binding-custody-unsafe"); }
function invalidSnapshot(): Error { return new Error("hosted-identity-snapshot-invalid"); }
function aborted(): Error { const error = new Error("hosted-identity-binding-aborted"); error.name = "AbortError"; return error; }
function abortIfRequested(signal?: AbortSignal): void { if (signal?.aborted) throw aborted(); }
function digest(body: RecordBody): string { return createHash("sha256").update(JSON.stringify(body)).digest("hex"); }
function withDigest(body: RecordBody): BindingRecord { return { ...body, digest: digest(body) }; }
function exactKeys(value: Record<string, unknown>, keys: readonly string[]): boolean {
  return Object.keys(value).sort().join("\0") === [...keys].sort().join("\0");
}
function ownerId(): number {
  const uid = process.getuid?.();
  if (uid === undefined) throw custodyError();
  return uid;
}
function validateOpaque(value: unknown): value is string { return typeof value === "string" && OPAQUE.test(value); }
function validateSnapshot(value: HostedIdentitySnapshot): void {
  if (!value || !exactKeys(value as unknown as Record<string, unknown>, ["accountUserId", "providerWorkspaceId", "supplierGeneration", "identityGeneration", "snapshotDigest"])
    || !validateOpaque(value.accountUserId) || !validateOpaque(value.providerWorkspaceId)
    || !validateOpaque(value.supplierGeneration) || !validateOpaque(value.identityGeneration) || !HEX.test(value.snapshotDigest)) throw invalidSnapshot();
}
function parseRecord(text: string): BindingRecord {
  let value: unknown;
  try { value = JSON.parse(text); } catch { throw custodyError(); }
  if (!value || typeof value !== "object" || Array.isArray(value) || !exactKeys(value as Record<string, unknown>, RECORD_KEYS)) throw custodyError();
  const record = value as BindingRecord;
  if (record.schema !== SCHEMA || !HANDLE.test(record.accountId) || !Number.isSafeInteger(record.accountEpoch) || record.accountEpoch < 1
    || !validateOpaque(record.accountUserId) || !validateOpaque(record.providerWorkspaceId)
    || !validateOpaque(record.supplierGeneration) || !validateOpaque(record.identityGeneration) || !HEX.test(record.snapshotDigest)
    || !validateOpaque(record.runtimeAuthorityId) || typeof record.canonicalRoot !== "string" || !isAbsolute(record.canonicalRoot) || resolve(record.canonicalRoot) !== record.canonicalRoot
    || !HEX.test(record.policyDigest) || !["active", "fenced"].includes(record.state)
    || (record.fenceReason !== null && !["sign-out", "switch", "revoke", "identity-change"].includes(record.fenceReason))) throw custodyError();
  const { digest: observed, ...body } = record;
  if (!HEX.test(observed) || digest(body) !== observed || (record.state === "active") !== (record.fenceReason === null)) throw custodyError();
  return record;
}
function continuity(record: BindingRecord): WorkerContinuity {
  return Object.freeze({ canonicalRoot: record.canonicalRoot, cwd: record.canonicalRoot, accountId: record.accountId, accountEpoch: record.accountEpoch, policyDigest: record.policyDigest });
}

/** Owner-private durable mapping. Its record is correlation state and never proves live supplier identity. */
export class HostedIdentityBindingStore {
  private record: BindingRecord | undefined;
  private serial: Promise<void> = Promise.resolve();
  private poisoned = false;
  private readonly recordPath: string;
  private readonly lockPath: string;

  private constructor(private readonly options: HostedIdentityBindingOptions, private readonly rootIdentity: { device: bigint; inode: bigint }, record?: BindingRecord) {
    this.record = record;
    this.recordPath = join(options.privateDirectory, FILE_NAME);
    this.lockPath = join(options.privateDirectory, LOCK_NAME);
  }

  static async open(options: HostedIdentityBindingOptions): Promise<HostedIdentityBindingStore> {
    if (!options || typeof options.privateDirectory !== "string" || !isAbsolute(options.privateDirectory) || resolve(options.privateDirectory) !== options.privateDirectory
      || typeof options.canonicalRoot !== "string" || !isAbsolute(options.canonicalRoot) || resolve(options.canonicalRoot) !== options.canonicalRoot
      || !HEX.test(options.policyDigest) || !validateOpaque(options.runtimeAuthorityId)) throw custodyError();
    await HostedIdentityBindingStore.assertDirectory(options.privateDirectory);
    const root = await lstat(options.canonicalRoot).catch(() => undefined);
    if (!root?.isDirectory() || root.isSymbolicLink() || await realpath(options.canonicalRoot).catch(() => undefined) !== options.canonicalRoot) throw custodyError();
    const entries = await readdir(options.privateDirectory);
    if (entries.some(name => name === LOCK_NAME || (name.startsWith(`${FILE_NAME}.`) && name.endsWith(".tmp")))) throw custodyError();
    const record = await HostedIdentityBindingStore.readRecord(join(options.privateDirectory, FILE_NAME));
    return new HostedIdentityBindingStore({ ...options }, { device: BigInt(root.dev), inode: BigInt(root.ino) }, record);
  }

  private static async assertDirectory(path: string): Promise<void> {
    const [metadata, canonical] = await Promise.all([lstat(path).catch(() => undefined), realpath(path).catch(() => undefined)]);
    if (!metadata?.isDirectory() || metadata.isSymbolicLink() || canonical !== path || metadata.uid !== ownerId() || (metadata.mode & 0o777) !== 0o700) throw custodyError();
  }

  private static async readRecord(path: string): Promise<BindingRecord | undefined> {
    let handle;
    try { handle = await open(path, constants.O_RDONLY | constants.O_NOFOLLOW); }
    catch (error) { if ((error as NodeJS.ErrnoException).code === "ENOENT") return undefined; throw custodyError(); }
    try {
      const metadata = await handle.stat();
      if (!metadata.isFile() || metadata.uid !== ownerId() || (metadata.mode & 0o777) !== 0o600 || metadata.nlink !== 1 || metadata.size < 2 || metadata.size > 16_384) throw custodyError();
      return parseRecord(await handle.readFile("utf8"));
    } finally { await handle.close(); }
  }

  private nextCoordinate(record?: BindingRecord): { accountId: string; accountEpoch: number } {
    if (record && record.accountEpoch < Number.MAX_SAFE_INTEGER) return { accountId: record.accountId, accountEpoch: record.accountEpoch + 1 };
    const bytes = (this.options.randomHandle ?? (() => randomBytes(32)))();
    if (!Buffer.isBuffer(bytes) || bytes.length !== 32) throw custodyError();
    const accountId = `rhb_${bytes.toString("base64url")}`;
    if (!HANDLE.test(accountId) || accountId === record?.accountId) throw custodyError();
    return { accountId, accountEpoch: 1 };
  }

  private async assertCustody(): Promise<void> {
    if (this.poisoned) throw custodyError();
    await HostedIdentityBindingStore.assertDirectory(this.options.privateDirectory);
    const root = await lstat(this.options.canonicalRoot).catch(() => undefined);
    if (!root?.isDirectory() || root.isSymbolicLink() || await realpath(this.options.canonicalRoot).catch(() => undefined) !== this.options.canonicalRoot
      || BigInt(root.dev) !== this.rootIdentity.device || BigInt(root.ino) !== this.rootIdentity.inode) { this.poisoned = true; throw custodyError(); }
    const disk = await HostedIdentityBindingStore.readRecord(this.recordPath);
    if (JSON.stringify(disk) === JSON.stringify(this.record)) return;
    // Several store instances of one runtime process share this record (each
    // admitted candidate opens its own). A digest-valid record that continues
    // this instance's lineage is adopted; anything else is custody loss.
    if (!HostedIdentityBindingStore.lineageSuccessor(this.record, disk)) { this.poisoned = true; throw custodyError(); }
    this.record = disk;
  }

  private static lineageSuccessor(prior: BindingRecord | undefined, disk: BindingRecord | undefined): disk is BindingRecord {
    if (!disk || !prior) return false;
    return disk.canonicalRoot === prior.canonicalRoot && disk.policyDigest === prior.policyDigest && disk.accountId === prior.accountId && disk.accountEpoch >= prior.accountEpoch;
  }

  /**
   * Re-reads the durable record under custody checks. Reports whether the
   * binding is still active and at which coordinate, so an admission bound to
   * an earlier epoch can learn that it was fenced by another store instance.
   */
  observe(signal?: AbortSignal): Promise<HostedIdentityBindingObservation> {
    const run = this.serial.then(async () => {
      abortIfRequested(signal); await this.assertCustody();
      const record = this.record;
      return record ? { state: record.state, accountId: record.accountId, accountEpoch: record.accountEpoch, fenceReason: record.fenceReason } as const : { state: "absent" } as const;
    });
    this.serial = run.then(() => {}, () => {});
    return run;
  }

  private async acquireLock(): Promise<() => Promise<void>> {
    let lock;
    try { lock = await open(this.lockPath, constants.O_WRONLY | constants.O_CREAT | constants.O_EXCL | constants.O_NOFOLLOW, 0o600); }
    catch { this.poisoned = true; throw custodyError(); }
    try {
      const metadata = await lock.stat();
      if (!metadata.isFile() || metadata.uid !== ownerId() || (metadata.mode & 0o777) !== 0o600 || metadata.nlink !== 1) throw custodyError();
      await lock.writeFile(`${process.pid}\n`, "utf8"); await lock.sync();
    } catch (error) { await lock.close().catch(() => {}); await unlink(this.lockPath).catch(() => {}); throw error; }
    await lock.close();
    return async () => { await unlink(this.lockPath); };
  }

  private async persist(record: BindingRecord): Promise<void> {
    const temporary = `${this.recordPath}.${process.pid}.${randomUUID()}.tmp`;
    let handle;
    try {
      handle = await open(temporary, constants.O_WRONLY | constants.O_CREAT | constants.O_EXCL | constants.O_NOFOLLOW, 0o600);
      const metadata = await handle.stat();
      if (!metadata.isFile() || metadata.uid !== ownerId() || (metadata.mode & 0o777) !== 0o600 || metadata.nlink !== 1) throw custodyError();
      await handle.writeFile(`${JSON.stringify(record)}\n`, "utf8"); await handle.sync(); await handle.close(); handle = undefined;
      const current = await HostedIdentityBindingStore.readRecord(this.recordPath);
      if (JSON.stringify(current) !== JSON.stringify(this.record)) throw custodyError();
      await rename(temporary, this.recordPath);
      const directory = await open(this.options.privateDirectory, constants.O_RDONLY | constants.O_DIRECTORY | constants.O_NOFOLLOW);
      try { await directory.sync(); } finally { await directory.close(); }
      this.record = record;
    } catch (error) {
      this.poisoned = true;
      await handle?.close().catch(() => {}); await unlink(temporary).catch(() => {});
      throw error;
    }
  }

  private exclusive<T>(signal: AbortSignal | undefined, operation: () => Promise<T>): Promise<T> {
    const run = this.serial.then(async () => {
      abortIfRequested(signal); await this.assertCustody(); abortIfRequested(signal);
      const release = await this.acquireLock();
      try { abortIfRequested(signal); return await operation(); }
      finally {
        try { await release(); }
        catch { this.poisoned = true; throw custodyError(); }
      }
    });
    this.serial = run.then(() => {}, () => {});
    return run;
  }

  establishLive(snapshot: HostedIdentitySnapshot, authority: LiveHostedAuthority, signal?: AbortSignal): Promise<WorkerContinuity> {
    validateSnapshot(snapshot);
    if (!authority || typeof authority.assertLive !== "function") return Promise.reject(invalidSnapshot());
    return this.exclusive(signal, async () => {
      authority.assertLive();
      const prior = this.record;
      const unchanged = prior?.state === "active" && prior.accountUserId === snapshot.accountUserId && prior.providerWorkspaceId === snapshot.providerWorkspaceId
        && prior.canonicalRoot === this.options.canonicalRoot && prior.policyDigest === this.options.policyDigest;
      const coordinate = unchanged ? { accountId: prior.accountId, accountEpoch: prior.accountEpoch }
        : prior?.state === "fenced" ? { accountId: prior.accountId, accountEpoch: prior.accountEpoch }
        : this.nextCoordinate(prior);
      const next = withDigest({ schema: SCHEMA, ...coordinate, ...snapshot, runtimeAuthorityId: this.options.runtimeAuthorityId,
        canonicalRoot: this.options.canonicalRoot, policyDigest: this.options.policyDigest, state: "active", fenceReason: null });
      await this.persist(next);
      return continuity(next);
    });
  }

  fence(reason: HostedIdentityFenceReason, signal?: AbortSignal): Promise<WorkerContinuity | undefined> {
    if (!["sign-out", "switch", "revoke", "identity-change"].includes(reason)) return Promise.reject(custodyError());
    return this.exclusive(signal, async () => {
      const prior = this.record;
      if (!prior) return undefined;
      if (prior.state === "fenced") return continuity(prior);
      const { digest: _digest, ...body } = prior;
      const next = withDigest({ ...body, ...this.nextCoordinate(prior), state: "fenced", fenceReason: reason });
      await this.persist(next);
      return continuity(next);
    });
  }
}
