import { constants } from "node:fs";
import { lstat, open, readdir, realpath } from "node:fs/promises";
import { createHash } from "node:crypto";
import { isAbsolute, resolve } from "node:path";
import { RuntimeError } from "@chirality/runtime-contracts";

export const ACCEPTED_SUPPLY = Object.freeze({
  version: "0.149.0",
  sha256: "b1d1a8c3146b16a01c057e9ecc2213b969a775ba76c424d812714a2911708de2",
  size: 179721344,
  platform: "darwin-arm64",
  signatureStatus: "OPEN_G5_FINDING_INVALID_VENDOR_SIGNATURE"
} as const);
interface FileIdentity {
  readonly dev: string;
  readonly ino: string;
  readonly size: string;
  readonly mtimeNs: string;
  readonly ctimeNs: string;
  readonly mode: string;
}
interface SupplyDescriptor {
  readonly executablePath: string;
  readonly canonicalPath: string;
  readonly sha256: string;
  readonly version: string;
  readonly identity: FileIdentity;
  readonly versionEvidence: "accepted-payload-mapping-not-executed" | "custom-build-exact-profile" | "controlled-fixture-not-vendor-evidence";
  readonly signatureStatus: string;
}
export interface VerifiedSupply extends SupplyDescriptor { readonly evidenceClass: "accepted-supply" }
export interface VerifiedCustomSupply extends SupplyDescriptor {
  readonly evidenceClass: "custom-supply-profile-verified";
  readonly custody: "packaged" | "private-staged";
  readonly closure: readonly Readonly<(ExactSupplyClosureEntry & { identity: FileIdentity })>[];
}
export type ExactVerifiedSupply = VerifiedSupply | VerifiedCustomSupply;
export type ExactSupplyClosureEntry =
  | { relativePath: string; type: "directory" }
  | { relativePath: string; type: "file"; sha256: string; size: number; mode: "executable" | "data" };
export interface CustomSupplyExactProfileV1 {
  schema: "chirality-custom-supplier-exact-profile/v1";
  executable: { relativePath: "supplier/codex"; version: string; sha256: string; size: number };
}
export interface ExactSupplyVerifier {
  verify(options: { executablePath: string; custody?: "packaged" | "private-staged" }): Promise<ExactVerifiedSupply>;
  revalidate(descriptor: ExactVerifiedSupply): Promise<ExactVerifiedSupply>;
  readonly closureEntries: readonly Readonly<ExactSupplyClosureEntry>[];
}
export interface ControlledFixtureSupply extends SupplyDescriptor { readonly evidenceClass: "controlled-fixture" }
interface SupplyOptions { executablePath: string; expectedSha256?: string; expectedVersion?: string }
interface Profile { sha256: string; version: string; size: number }
const denied = (message: string) => new RuntimeError("ENGINE_UNAVAILABLE", message, 503);
const issued = new WeakSet<VerifiedSupply>();
/**
 * Per-process digest cache keyed by canonical path. A path is hashed once; later verifications of the same
 * path answer from the recorded filesystem identity (dev, ino, size, mode, mtimeNs, ctimeNs) and re-hash only
 * when that identity changed. Every custody, symlink, closure-listing and size check still runs on each call.
 */
const digestCache = new Map<string, Readonly<{ identity: FileIdentity; sha256: string }>>();
const DIGEST_CACHE_BOUND = 4096;
let hashPasses = 0;
function cachedDigest(path: string, current: FileIdentity): string | undefined {
  const entry = digestCache.get(path);
  return entry && sameIdentity(entry.identity, current) ? entry.sha256 : undefined;
}
function rememberDigest(path: string, identity: FileIdentity, sha256: string): void {
  if (digestCache.size >= DIGEST_CACHE_BOUND && !digestCache.has(path)) digestCache.delete(digestCache.keys().next().value!);
  digestCache.set(path, Object.freeze({ identity, sha256 }));
}
/** Number of full byte-hashing passes this process has performed; a diagnostics counter for tests and timing. */
export function exactSupplyHashPassCountForTests(): number { return hashPasses; }

function identity(stat: { dev: bigint; ino: bigint; size: bigint; mtimeNs: bigint; ctimeNs: bigint; mode: bigint }): FileIdentity {
  return Object.freeze({ dev: `${stat.dev}`, ino: `${stat.ino}`, size: `${stat.size}`, mtimeNs: `${stat.mtimeNs}`, ctimeNs: `${stat.ctimeNs}`, mode: `${stat.mode}` });
}
function sameIdentity(a: FileIdentity, b: FileIdentity): boolean {
  return a.dev === b.dev && a.ino === b.ino && a.size === b.size && a.mtimeNs === b.mtimeNs && a.ctimeNs === b.ctimeNs && a.mode === b.mode;
}
async function inspect(executablePath: string, profile: Profile): Promise<{ canonicalPath: string; identity: FileIdentity; sha256: string }> {
  let handle;
  try {
    if (typeof executablePath !== "string" || !isAbsolute(executablePath) || resolve(executablePath) !== executablePath) throw denied("Supply executable requires an absolute canonical path");
    const pathStat = await lstat(executablePath, { bigint: true });
    if (!pathStat.isFile() || pathStat.isSymbolicLink()) throw denied("Supply executable must be a regular file, never a symlink");
    const canonicalPath = await realpath(executablePath);
    if (canonicalPath !== executablePath) throw denied("Supply path cannot traverse aliases or symlinks");
    handle = await open(executablePath, constants.O_RDONLY | constants.O_NOFOLLOW);
    const before = await handle.stat({ bigint: true });
    if (!before.isFile() || !sameIdentity(identity(pathStat), identity(before))) throw denied("Supply path changed before verification");
    if (before.size !== BigInt(profile.size)) throw denied("Supply payload size does not match the pinned identity");
    const cached = cachedDigest(canonicalPath, identity(before));
    let sha256 = cached, bytes = profile.size;
    if (sha256 === undefined) {
      const digest = createHash("sha256");
      const buffer = Buffer.alloc(64 * 1024);
      bytes = 0; hashPasses++;
      for (;;) {
        const { bytesRead } = await handle.read(buffer, 0, buffer.length, null);
        if (bytesRead === 0) break;
        bytes += bytesRead;
        if (bytes > profile.size) throw denied("Supply payload grew during verification");
        digest.update(buffer.subarray(0, bytesRead));
      }
      sha256 = digest.digest("hex");
    }
    const after = identity(await handle.stat({ bigint: true }));
    const currentPath = await lstat(executablePath, { bigint: true });
    if (!sameIdentity(identity(before), after) || !sameIdentity(after, identity(currentPath)) || await realpath(executablePath) !== canonicalPath) throw denied("Supply identity changed during verification");
    if (bytes !== profile.size || sha256 !== profile.sha256) throw denied("Supply payload digest does not match the pinned identity");
    if (cached === undefined) rememberDigest(canonicalPath, after, sha256);
    return { canonicalPath, identity: after, sha256 };
  } catch (error) {
    if (error instanceof RuntimeError) throw error;
    throw denied("Supply executable is missing, inaccessible or unsafe");
  } finally { await handle?.close(); }
}

/** Exact accepted payload verification only; no invocation, signature acceptance or launch grant. */
export async function verifyExactSupply(options: SupplyOptions): Promise<VerifiedSupply> {
  if (!options || (options.expectedSha256 !== undefined && options.expectedSha256 !== ACCEPTED_SUPPLY.sha256)
    || (options.expectedVersion !== undefined && options.expectedVersion !== ACCEPTED_SUPPLY.version)) throw denied("Supply overrides cannot replace the accepted exact payload");
  const result = await inspect(options.executablePath, ACCEPTED_SUPPLY);
  const descriptor: VerifiedSupply = Object.freeze({ executablePath: options.executablePath, ...result, version: ACCEPTED_SUPPLY.version,
    evidenceClass: "accepted-supply", versionEvidence: "accepted-payload-mapping-not-executed", signatureStatus: ACCEPTED_SUPPLY.signatureStatus });
  issued.add(descriptor);
  return descriptor;
}
/** Revalidate immediately before launch: identity-checked, re-hashed only when the identity changed. A path-based OS launch still has a residual race after this check. */
export async function revalidateExactSupply(descriptor: VerifiedSupply): Promise<VerifiedSupply> {
  if (!descriptor || !issued.has(descriptor)) throw denied("Supply descriptor was not issued by this exact verifier; verify again in this process");
  const current = await verifyExactSupply({ executablePath: descriptor.executablePath });
  if (!sameIdentity(descriptor.identity, current.identity)) throw denied("Supply executable identity drifted after verification");
  return current;
}

async function inspectClosure(executablePath: string, entries: ExactSupplyVerifier["closureEntries"], custody: "packaged" | "private-staged"): Promise<VerifiedCustomSupply["closure"]> {
  const root = resolve(executablePath, "..");
  const observed: string[] = [];
  async function walk(path: string, relativePath: string): Promise<void> {
    if (observed.length >= 50_000) throw denied("Custom supply closure exceeds its bound");
    const info = await lstat(path);
    if (info.isSymbolicLink() || await realpath(path) !== path) throw denied("Custom supply closure path is unsafe");
    observed.push(relativePath);
    if (info.isDirectory()) for (const name of (await readdir(path)).sort((a, b) => Buffer.compare(Buffer.from(a), Buffer.from(b)))) await walk(resolve(path, name), `${relativePath}/${name}`);
  }
  await walk(root, "supplier");
  if (observed.length !== entries.length || observed.some((value, index) => value !== entries[index]!.relativePath)) throw denied("Custom supply closure contains an unlisted or missing path");
  const values = [];
  for (const expected of entries) {
    const relativePath = expected.relativePath === "supplier" ? "" : expected.relativePath.slice("supplier/".length), path = relativePath ? resolve(root, relativePath) : root;
    if ((relativePath && !path.startsWith(`${root}/`)) || await realpath(path) !== path) throw denied("Custom supply closure path is unsafe");
    const info = await lstat(path, { bigint: true });
    const permissions = info.mode & 0o777n;
    const modeInvalid = custody === "private-staged"
      ? permissions !== BigInt(expected.type === "directory" || expected.mode === "executable" ? 0o700 : 0o600)
      : (permissions & 0o022n) !== 0n || (expected.type === "file" && ((permissions & 0o111n) !== 0n) !== (expected.mode === "executable"));
    if (info.isSymbolicLink() || info.uid !== BigInt(process.getuid?.() ?? -1) || modeInvalid
      || (expected.type === "directory" ? !info.isDirectory() : (!info.isFile() || info.nlink !== 1n || info.size !== BigInt(expected.size)))) throw denied("Custom supply closure custody is unsafe");
    if (expected.type === "directory") { values.push(Object.freeze({ ...expected, identity: identity(info) })); continue; }
    const handle = await open(path, constants.O_RDONLY | constants.O_NOFOLLOW);
    try {
      const before = identity(await handle.stat({ bigint: true })), cached = cachedDigest(path, before);
      let sha256 = cached, total = expected.size;
      if (sha256 === undefined) {
        const digest = createHash("sha256"), buffer = Buffer.alloc(64 * 1024); total = 0; hashPasses++;
        for (;;) { const { bytesRead } = await handle.read(buffer, 0, buffer.length, null); if (!bytesRead) break; total += bytesRead; if (total > expected.size) throw denied("Custom supply closure grew during verification"); digest.update(buffer.subarray(0, bytesRead)); }
        sha256 = digest.digest("hex");
      }
      const after = identity(await handle.stat({ bigint: true })), current = identity(await lstat(path, { bigint: true }));
      if (total !== expected.size || sha256 !== expected.sha256 || !sameIdentity(before, after) || !sameIdentity(after, current)) throw denied("Custom supply closure changed or differs from its accepted profile");
      if (cached === undefined) rememberDigest(path, after, sha256);
      values.push(Object.freeze({ ...expected, identity: after }));
    } finally { await handle.close(); }
  }
  return Object.freeze(values);
}

/** Pure byte/custody verifier. A caller-created value is not operational; the packaged-basis registry separately issues it. */
export function createCustomSupplyVerifier(profile: Readonly<CustomSupplyExactProfileV1>, closureEntries: readonly Readonly<ExactSupplyClosureEntry>[]): ExactSupplyVerifier {
  const hex = (value: unknown) => typeof value === "string" && /^[a-f0-9]{64}$/.test(value);
  if (!profile || profile.schema !== "chirality-custom-supplier-exact-profile/v1" || profile.executable?.relativePath !== "supplier/codex"
    || !profile.executable.version || !hex(profile.executable.sha256) || !Number.isSafeInteger(profile.executable.size) || profile.executable.size < 1
    || !Array.isArray(closureEntries) || closureEntries.length < 2 || closureEntries.length > 50_000) throw denied("Custom supply exact profile is invalid");
  const paths = closureEntries.map(value => value.relativePath);
  if (new Set(paths).size !== paths.length || paths.some((path, index) => !/^supplier(?:\/[A-Za-z0-9._/-]+)?$/.test(path) || (index > 0 && Buffer.compare(Buffer.from(paths[index - 1]!), Buffer.from(path)) >= 0))
    || paths[0] !== "supplier"
    || closureEntries.some(value => value.type === "file" ? (!hex(value.sha256) || !Number.isSafeInteger(value.size) || value.size < 0 || !["executable", "data"].includes(value.mode)) : value.type !== "directory")) throw denied("Custom supply exact closure is invalid");
  const types = new Map(closureEntries.map(value => [value.relativePath, value.type]));
  if (closureEntries.some(value => value.relativePath !== "supplier" && types.get(value.relativePath.slice(0, value.relativePath.lastIndexOf("/"))) !== "directory")) throw denied("Custom supply exact closure parent is invalid");
  const executable = closureEntries.find((value): value is Extract<ExactSupplyClosureEntry, {type:"file"}> => value.relativePath === "supplier/codex" && value.type === "file");
  if (!executable || executable.sha256 !== profile.executable.sha256 || executable.size !== profile.executable.size) throw denied("Custom supply profile differs from its accepted closure");
  if (executable.mode !== "executable") throw denied("Custom supply executable is not executable");
  const frozenProfile = structuredClone(profile), frozenEntries = Object.freeze(closureEntries.map(value => Object.freeze({ ...value })));
  const descriptors = new WeakSet<VerifiedCustomSupply>();
  const verifier: ExactSupplyVerifier = Object.freeze({ closureEntries: frozenEntries,
    async verify(options: { executablePath: string; custody?: "packaged" | "private-staged" }) {
      const custody = options.custody ?? "packaged";
      const result = await inspect(options.executablePath, { sha256: frozenProfile.executable.sha256, version: frozenProfile.executable.version, size: frozenProfile.executable.size });
      const descriptor: VerifiedCustomSupply = Object.freeze({ executablePath: options.executablePath, ...result, version: frozenProfile.executable.version, evidenceClass: "custom-supply-profile-verified",
        custody, versionEvidence: "custom-build-exact-profile", signatureStatus: "custom-build-signature-not-evaluated", closure: await inspectClosure(options.executablePath, frozenEntries, custody) });
      descriptors.add(descriptor); return descriptor;
    },
    async revalidate(descriptor: ExactVerifiedSupply) {
      if (!descriptor || descriptor.evidenceClass !== "custom-supply-profile-verified" || !descriptors.has(descriptor)) throw denied("Custom supply descriptor was not issued by this verifier");
      const current = await verifier.verify({ executablePath: descriptor.executablePath, custody: descriptor.custody }) as VerifiedCustomSupply;
      if (!sameIdentity(descriptor.identity, current.identity) || descriptor.closure.length !== current.closure.length || descriptor.closure.some((value, index) => !sameIdentity(value.identity, current.closure[index]!.identity))) throw denied("Custom supply closure identity drifted after verification");
      return current;
    }
  });
  return verifier;
}

/** Explicit fixture seam; descriptors cannot pass the production verifier's issuance seal. */
export function createControlledSupplyVerifierForTests(profile: Profile): {
  verify(executablePath: string): Promise<ControlledFixtureSupply>;
  revalidate(descriptor: ControlledFixtureSupply): Promise<ControlledFixtureSupply>;
} {
  if (!profile || !/^[a-f0-9]{64}$/.test(profile.sha256) || !Number.isSafeInteger(profile.size) || profile.size < 0 || typeof profile.version !== "string" || !profile.version) throw new RuntimeError("INVALID_REQUEST", "Invalid controlled fixture identity");
  const frozen = Object.freeze({ ...profile });
  const fixtures = new WeakSet<ControlledFixtureSupply>();
  async function verify(executablePath: string): Promise<ControlledFixtureSupply> {
    const result = await inspect(executablePath, frozen);
    const descriptor: ControlledFixtureSupply = Object.freeze({ executablePath, ...result, version: frozen.version, evidenceClass: "controlled-fixture",
      versionEvidence: "controlled-fixture-not-vendor-evidence", signatureStatus: "NOT_VENDOR_SIGNATURE_EVIDENCE" });
    fixtures.add(descriptor);
    return descriptor;
  }
  return Object.freeze({ verify, async revalidate(descriptor: ControlledFixtureSupply) {
    if (!descriptor || !fixtures.has(descriptor)) throw denied("Unissued controlled fixture descriptor");
    const current = await verify(descriptor.executablePath);
    if (!sameIdentity(descriptor.identity, current.identity)) throw denied("Controlled fixture identity drifted after verification");
    return current;
  } });
}
