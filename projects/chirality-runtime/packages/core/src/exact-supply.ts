import { constants } from "node:fs";
import { lstat, open, realpath } from "node:fs/promises";
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
}
interface SupplyDescriptor {
  readonly executablePath: string;
  readonly canonicalPath: string;
  readonly sha256: string;
  readonly version: string;
  readonly identity: FileIdentity;
  readonly versionEvidence: "accepted-payload-mapping-not-executed" | "controlled-fixture-not-vendor-evidence";
  readonly signatureStatus: string;
}
export interface VerifiedSupply extends SupplyDescriptor { readonly evidenceClass: "accepted-supply" }
export interface ControlledFixtureSupply extends SupplyDescriptor { readonly evidenceClass: "controlled-fixture" }
interface SupplyOptions { executablePath: string; expectedSha256?: string; expectedVersion?: string }
interface Profile { sha256: string; version: string; size: number }
const denied = (message: string) => new RuntimeError("ENGINE_UNAVAILABLE", message, 503);
const issued = new WeakSet<VerifiedSupply>();

function identity(stat: { dev: bigint; ino: bigint; size: bigint; mtimeNs: bigint; ctimeNs: bigint }): FileIdentity {
  return Object.freeze({ dev: `${stat.dev}`, ino: `${stat.ino}`, size: `${stat.size}`, mtimeNs: `${stat.mtimeNs}`, ctimeNs: `${stat.ctimeNs}` });
}
function sameIdentity(a: FileIdentity, b: FileIdentity): boolean {
  return a.dev === b.dev && a.ino === b.ino && a.size === b.size && a.mtimeNs === b.mtimeNs && a.ctimeNs === b.ctimeNs;
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
    const digest = createHash("sha256");
    const buffer = Buffer.alloc(64 * 1024);
    let bytes = 0;
    for (;;) {
      const { bytesRead } = await handle.read(buffer, 0, buffer.length, null);
      if (bytesRead === 0) break;
      bytes += bytesRead;
      if (bytes > profile.size) throw denied("Supply payload grew during verification");
      digest.update(buffer.subarray(0, bytesRead));
    }
    const after = identity(await handle.stat({ bigint: true }));
    const currentPath = await lstat(executablePath, { bigint: true });
    if (!sameIdentity(identity(before), after) || !sameIdentity(after, identity(currentPath)) || await realpath(executablePath) !== canonicalPath) throw denied("Supply identity changed during verification");
    const sha256 = digest.digest("hex");
    if (bytes !== profile.size || sha256 !== profile.sha256) throw denied("Supply payload digest does not match the pinned identity");
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
/** Rehash immediately before launch. A path-based OS launch still has a residual race after this check. */
export async function revalidateExactSupply(descriptor: VerifiedSupply): Promise<VerifiedSupply> {
  if (!descriptor || !issued.has(descriptor)) throw denied("Supply descriptor was not issued by this exact verifier; verify again in this process");
  const current = await verifyExactSupply({ executablePath: descriptor.executablePath });
  if (!sameIdentity(descriptor.identity, current.identity)) throw denied("Supply executable identity drifted after verification");
  return current;
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
