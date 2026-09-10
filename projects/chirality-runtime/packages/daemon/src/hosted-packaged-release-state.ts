import { createHash } from "node:crypto";
import { constants, type BigIntStats } from "node:fs";
import { dirname, isAbsolute, join, resolve } from "node:path";
import { RuntimeError } from "@chirality/runtime-contracts";
import {
  verifyPackagedRuntimeBasisV2,
  type RuntimeSupportProfileV2,
  type VerifiedPackagedRuntimeBasisV2
} from "@chirality/runtime-core/runtime-conformance-v2";
import { createCustomSupplyVerifier, type ExactSupplyVerifier } from "@chirality/runtime-core";
import { runtimePhysicalFilesystem } from "@chirality/runtime-core/physical-filesystem";

type Purpose = "login" | "worker";
type Issuance = "production" | "controlled-test";

export interface HostedReleaseAnchorPurposeV2 {
  recordSha256: string;
  acceptanceSha256: string;
  ownerActSha256: string;
  activationId: string;
  gateIdentity: string;
}

export interface HostedPackagedPurposeBasisV2 extends HostedReleaseAnchorPurposeV2 {
  recordPath: string;
  acceptancePath: string;
  ownerActPath: string;
}

export type HostedWorkerReleaseDispositionV2 = "qualified" | "local-human-trial";
export interface HostedPackagedTrialSealObservationV1 {
  path: string;
  sha256: string;
  mainCodeDirectoryHash: string;
  peerRequirementSha256: string;
}

export interface HostedPackagedReleaseBasisV2 {
  schema: "chirality-hosted-packaged-release-basis/v2";
  basisDigest: string;
  verified: Readonly<VerifiedPackagedRuntimeBasisV2>;
  supportProfile: Readonly<RuntimeSupportProfileV2>;
  instructionRoot: string;
  nativeAddonPath: string;
  supplierExecutablePath: string;
  preNativeFilesystemObservation: {
    runtimeDirectory: string;
    anchorRoot: string;
    evidence: "canonical-owner-mode-chain-observed";
  };
  login: Readonly<HostedPackagedPurposeBasisV2>;
  worker: Readonly<HostedPackagedPurposeBasisV2>;
  workerDisposition: HostedWorkerReleaseDispositionV2;
  trialSealObservation?: Readonly<HostedPackagedTrialSealObservationV1>;
}

export interface RetainedIssuedPackagedBasisV2 {
  issuance: Issuance;
  resourcesRoot: string;
  runtimeDirectory: string;
  anchorRoot: string;
  anchorPath: string;
  anchorSha256: string;
  inventorySha256: string;
  payloadDigest: string;
  profileDigest: string;
  basisDigest: string;
  login: Readonly<HostedPackagedPurposeBasisV2>;
  worker: Readonly<HostedPackagedPurposeBasisV2>;
  workerDisposition: HostedWorkerReleaseDispositionV2;
  trialSealObservation?: Readonly<HostedPackagedTrialSealObservationV1>;
  revalidateTrialSeal?: () => Promise<void>;
}

export type IssuedPackagedFilesystemIdentityV2 = Readonly<{ dev: bigint; ino: bigint; size: bigint; mode: bigint; uid: bigint; nlink: bigint; mtimeNs: bigint; ctimeNs: bigint }>;
type Identity = IssuedPackagedFilesystemIdentityV2;
type StoredIssuedPackagedBasisV2 = Readonly<RetainedIssuedPackagedBasisV2 & {
  directories: Readonly<Record<"resourcesRoot" | "runtimeDirectory" | "anchorRoot" | "snapshotRoot", Identity>>;
  files: readonly Readonly<{ path: string; sha256: string; identity: Identity }>[];
  origin: readonly Readonly<{ path: string; kind: "file" | "directory"; identity: Identity }>[];
  supplyVerifier: ExactSupplyVerifier;
}>;
const issuedPackagedBases = new WeakMap<object, StoredIssuedPackagedBasisV2>();
const issuedSupplyVerifiers = new WeakSet<object>();
const PURPOSE_FILES: Readonly<Record<Purpose, readonly [keyof HostedPackagedPurposeBasisV2, keyof HostedPackagedPurposeBasisV2, keyof HostedPackagedPurposeBasisV2]>> = Object.freeze({
  login: ["recordPath", "acceptancePath", "ownerActPath"],
  worker: ["recordPath", "acceptancePath", "ownerActPath"]
});
const PURPOSE_HASHES: Readonly<Record<Purpose, readonly [keyof HostedPackagedPurposeBasisV2, keyof HostedPackagedPurposeBasisV2, keyof HostedPackagedPurposeBasisV2]>> = Object.freeze({
  login: ["recordSha256", "acceptanceSha256", "ownerActSha256"],
  worker: ["recordSha256", "acceptanceSha256", "ownerActSha256"]
});

const hash = (value: Buffer) => createHash("sha256").update(value).digest("hex");
const unavailable = (reason: string) => new RuntimeError("ENGINE_UNAVAILABLE", "Packaged hosted Runtime release basis is unavailable", 503, { reason });
const canonical = (path: string): boolean => isAbsolute(path) && resolve(path) === path && !/[\x00-\x1f]/.test(path);
function sameIdentity(left: BigIntStats, right: BigIntStats): boolean {
  return left.dev === right.dev && left.ino === right.ino && left.size === right.size && left.mode === right.mode
    && left.uid === right.uid && left.nlink === right.nlink && left.mtimeNs === right.mtimeNs && left.ctimeNs === right.ctimeNs;
}
function identity(value: BigIntStats): Identity {
  return Object.freeze({ dev: value.dev, ino: value.ino, size: value.size, mode: value.mode, uid: value.uid, nlink: value.nlink, mtimeNs: value.mtimeNs, ctimeNs: value.ctimeNs });
}
function exactIdentity(left: Identity, right: Identity, includeTimes: boolean): boolean {
  return left.dev === right.dev && left.ino === right.ino && left.mode === right.mode && left.uid === right.uid && left.nlink === right.nlink
    && (!includeTimes || (left.size === right.size && left.mtimeNs === right.mtimeNs && left.ctimeNs === right.ctimeNs));
}
function sameMutableAncestor(left: Identity, right: Identity): boolean {
  return left.dev === right.dev && left.ino === right.ino && left.mode === right.mode && left.uid === right.uid;
}
async function directoryIdentity(path: string): Promise<Identity> {
  if (!canonical(path) || await runtimePhysicalFilesystem().realpath(path) !== path) throw unavailable("PACKAGED_RELEASE_BASIS_CHANGED");
  const info = await runtimePhysicalFilesystem().lstat(path, { bigint: true });
  if (!info.isDirectory() || info.isSymbolicLink()) throw unavailable("PACKAGED_RELEASE_BASIS_CHANGED");
  return identity(info);
}

export async function assertIssuedPrivateDirectoryChainV2(runtimeDirectory: string, descendant: string): Promise<void> {
  if (!canonical(runtimeDirectory) || !canonical(descendant) || !(descendant === runtimeDirectory || descendant.startsWith(`${runtimeDirectory}/`))) throw unavailable("PRIVATE_RELEASE_DIRECTORY_UNSAFE");
  const suffix = descendant.slice(runtimeDirectory.length).split("/").filter(Boolean);
  let current = runtimeDirectory;
  for (const part of ["", ...suffix]) {
    if (part) current = join(current, part);
    const info = await runtimePhysicalFilesystem().lstat(current);
    if (!info.isDirectory() || info.isSymbolicLink() || info.uid !== (process.getuid?.() ?? -1) || (info.mode & 0o777) !== 0o700 || await runtimePhysicalFilesystem().realpath(current) !== current) throw unavailable("PRIVATE_RELEASE_DIRECTORY_UNSAFE");
  }
}

export async function readIssuedPrivateFileV2(path: string, maximum = 1_048_576): Promise<{ bytes: Buffer; sha256: string; identity: Identity }> {
  if (!canonical(path) || await runtimePhysicalFilesystem().realpath(path) !== path) throw unavailable("INVALID_PRIVATE_RELEASE_BASIS");
  const file = await runtimePhysicalFilesystem().open(path, constants.O_RDONLY | constants.O_NOFOLLOW | constants.O_NONBLOCK);
  try {
    const before = await file.stat({ bigint: true });
    const uid = BigInt(process.getuid?.() ?? -1);
    if (!before.isFile() || before.nlink !== 1n || before.uid !== uid || (before.mode & 0o777n) !== 0o600n || before.size > BigInt(maximum)) throw unavailable("INVALID_PRIVATE_RELEASE_BASIS");
    const expected = Number(before.size);
    const bytes = Buffer.allocUnsafe(expected + 1);
    let total = 0;
    while (total < bytes.length) {
      const result = await file.read(bytes, total, bytes.length - total, total);
      if (result.bytesRead === 0) break;
      total += result.bytesRead;
    }
    const after = await file.stat({ bigint: true });
    const pathInfo = await runtimePhysicalFilesystem().lstat(path, { bigint: true });
    if (total !== expected || !sameIdentity(before, after) || !sameIdentity(after, pathInfo) || await runtimePhysicalFilesystem().realpath(path) !== path) throw unavailable("CHANGED_PRIVATE_RELEASE_BASIS");
    const result = bytes.subarray(0, total);
    return { bytes: result, sha256: hash(result), identity: identity(after) };
  } finally {
    await file.close();
  }
}

async function observedFile(path: string): Promise<{ path: string; sha256: string; identity: Identity }> {
  const value = await readIssuedPrivateFileV2(path);
  return Object.freeze({ path, sha256: value.sha256, identity: value.identity });
}
async function originIdentity(path: string, kind: "file" | "directory"): Promise<Identity> {
  if (!canonical(path) || await runtimePhysicalFilesystem().realpath(path) !== path) throw unavailable("PACKAGED_RELEASE_BASIS_CHANGED");
  const info = await runtimePhysicalFilesystem().lstat(path, { bigint: true });
  if (info.isSymbolicLink() || (kind === "file" ? (!info.isFile() || info.nlink !== 1n) : !info.isDirectory())) throw unavailable("PACKAGED_RELEASE_BASIS_CHANGED");
  return identity(info);
}

/** Loader-only registration. This module is deliberately absent from package export maps and barrels. */
export async function registerIssuedPackagedReleaseBasisV2(basis: Readonly<HostedPackagedReleaseBasisV2>, state: RetainedIssuedPackagedBasisV2): Promise<void> {
  if (issuedPackagedBases.has(basis as object)) throw unavailable("PACKAGED_RELEASE_BASIS_ALREADY_ISSUED");
  const snapshotRoot = dirname(state.login.recordPath);
  const fileInputs = [{ path: state.anchorPath, sha256: state.anchorSha256 }];
  for (const purpose of ["login", "worker"] as const) {
    const value = state[purpose];
    for (let index = 0; index < 3; index++) fileInputs.push({ path: String(value[PURPOSE_FILES[purpose][index]!]), sha256: String(value[PURPOSE_HASHES[purpose][index]!]) });
  }
  if (state.trialSealObservation) fileInputs.push({ path: state.trialSealObservation.path, sha256: state.trialSealObservation.sha256 });
  const files = await Promise.all(fileInputs.map(async expected => {
    const observed = await observedFile(expected.path);
    if (observed.sha256 !== expected.sha256) throw unavailable("PACKAGED_RELEASE_BASIS_CHANGED");
    return observed;
  }));
  const directories = Object.freeze({ resourcesRoot: await directoryIdentity(state.resourcesRoot), runtimeDirectory: await directoryIdentity(state.runtimeDirectory),
    anchorRoot: await directoryIdentity(state.anchorRoot), snapshotRoot: await directoryIdentity(snapshotRoot) });
  const originInputs = [{ path: state.resourcesRoot, kind: "directory" as const },
    { path: basis.verified.inventoryPath, kind: "file" as const }, { path: basis.verified.payloadManifestPath, kind: "file" as const },
    { path: join(state.resourcesRoot, "runtime-governance"), kind: "directory" as const }, { path: join(state.resourcesRoot, "runtime-governance/v2"), kind: "directory" as const },
    ...basis.verified.inventory.governance.map(entry => ({ path: join(state.resourcesRoot, entry.relativePath), kind: "file" as const })),
    ...basis.verified.payload.entries.map(entry => ({ path: join(state.resourcesRoot, entry.relativePath), kind: entry.type }))];
  const origin = Object.freeze(await Promise.all(originInputs.map(async entry => Object.freeze({ ...entry, identity: await originIdentity(entry.path, entry.kind) }))));
  const closureEntries = await Promise.all(basis.verified.payload.entries.filter(entry => entry.relativePath === "supplier" || entry.relativePath.startsWith("supplier/"))
    .map(async entry => entry.type === "directory" ? Object.freeze({ relativePath: entry.relativePath, type: "directory" as const }) : Object.freeze({
      relativePath: entry.relativePath, type: "file" as const, sha256: entry.sha256, size: entry.size,
      mode: ((await runtimePhysicalFilesystem().lstat(join(state.resourcesRoot, entry.relativePath))).mode & 0o111) !== 0 ? "executable" as const : "data" as const
    })));
  const supplier = basis.supportProfile.supplier;
  const supplyVerifier = createCustomSupplyVerifier({ schema: "chirality-custom-supplier-exact-profile/v1",
    executable: { relativePath: "supplier/codex", version: supplier.version, sha256: supplier.sha256, size: supplier.size }
  }, closureEntries);
  issuedSupplyVerifiers.add(supplyVerifier as object);
  issuedPackagedBases.set(basis as object, Object.freeze({ ...state, directories, files: Object.freeze(files), origin, supplyVerifier }));
}

/** Internal production projection; arbitrary verifier objects cannot cross this issued-basis gate. */
export async function issuedPackagedSupplyVerifierV2(basis: Readonly<HostedPackagedReleaseBasisV2>): Promise<ExactSupplyVerifier> {
  await revalidateIssuedPackagedReleaseBasisV2(basis);
  const state = requireIssued(basis, "production");
  if (!issuedSupplyVerifiers.has(state.supplyVerifier as object)) throw unavailable("PACKAGED_SUPPLY_VERIFIER_UNISSUED");
  return state.supplyVerifier;
}
export function assertIssuedPackagedSupplyVerifierV2(verifier: ExactSupplyVerifier): void {
  if (!verifier || !issuedSupplyVerifiers.has(verifier as object)) throw unavailable("PACKAGED_SUPPLY_VERIFIER_UNISSUED");
}

async function observePrivateState(state: StoredIssuedPackagedBasisV2): Promise<void> {
  await assertIssuedPrivateDirectoryChainV2(state.runtimeDirectory, state.anchorRoot);
  await assertIssuedPrivateDirectoryChainV2(state.runtimeDirectory, dirname(state.login.recordPath));
  const directoryPaths = { resourcesRoot: state.resourcesRoot, runtimeDirectory: state.runtimeDirectory, anchorRoot: state.anchorRoot, snapshotRoot: dirname(state.login.recordPath) } as const;
  for (const name of Object.keys(directoryPaths) as (keyof typeof directoryPaths)[]) {
    const current = await directoryIdentity(directoryPaths[name]);
    const matches = name === "runtimeDirectory" ? sameMutableAncestor(state.directories[name], current) : exactIdentity(state.directories[name], current, true);
    if (!matches) throw unavailable("PACKAGED_RELEASE_BASIS_CHANGED");
  }
  for (const expected of state.files) {
    const current = await observedFile(expected.path);
    if (current.sha256 !== expected.sha256 || !exactIdentity(expected.identity, current.identity, true)) throw unavailable("PACKAGED_RELEASE_BASIS_CHANGED");
  }
}
async function observeOriginState(state: StoredIssuedPackagedBasisV2): Promise<void> {
  for (const expected of state.origin) {
    const current = await originIdentity(expected.path, expected.kind);
    if (!exactIdentity(expected.identity, current, true)) throw unavailable("PACKAGED_RELEASE_BASIS_CHANGED");
  }
}

function requireIssued(basis: Readonly<HostedPackagedReleaseBasisV2>, expectedIssuance: Issuance): StoredIssuedPackagedBasisV2 {
  const state = issuedPackagedBases.get(basis as object);
  if (!state || state.issuance !== expectedIssuance || basis.basisDigest !== state.basisDigest || basis.verified.resourcesRoot !== state.resourcesRoot
    || basis.verified.inventorySha256 !== state.inventorySha256 || basis.verified.payloadDigest !== state.payloadDigest
    || basis.supportProfile.profileDigest !== state.profileDigest || basis.preNativeFilesystemObservation.runtimeDirectory !== state.runtimeDirectory
    || basis.preNativeFilesystemObservation.anchorRoot !== state.anchorRoot || basis.login !== state.login || basis.worker !== state.worker
    || basis.workerDisposition !== state.workerDisposition
    || JSON.stringify(basis.trialSealObservation ?? null) !== JSON.stringify(state.trialSealObservation ?? null)
    || (basis.workerDisposition === "local-human-trial") !== (state.revalidateTrialSeal !== undefined)) throw unavailable("PACKAGED_RELEASE_BASIS_NOT_ISSUED");
  return state;
}
async function revalidate(basis: Readonly<HostedPackagedReleaseBasisV2>, expectedIssuance: Issuance): Promise<void> {
  const state = requireIssued(basis, expectedIssuance);
  await observePrivateState(state);
  await observeOriginState(state);
  await state.revalidateTrialSeal?.();
  const verified = await verifyPackagedRuntimeBasisV2({ resourcesRoot: state.resourcesRoot });
  if (verified.inventorySha256 !== state.inventorySha256 || verified.payloadDigest !== state.payloadDigest
    || !verified.payload.supportProfiles.some(profile => profile.profileDigest === state.profileDigest)) throw unavailable("PACKAGED_RELEASE_BASIS_CHANGED");
  await observeOriginState(state);
  await observePrivateState(state);
  await state.revalidateTrialSeal?.();
}

/** Cheap nominal entry check. Composition owns the immediately following live read. */
export function assertIssuedPackagedReleaseBasisV2(basis: Readonly<HostedPackagedReleaseBasisV2>): void { requireIssued(basis, "production"); }

export function revalidateIssuedPackagedReleaseBasisV2(basis: Readonly<HostedPackagedReleaseBasisV2>): Promise<void> {
  return revalidate(basis, "production");
}

/** Source-test seam. It cannot validate or convert a controlled basis for production use. */
export function revalidateControlledPackagedReleaseBasisForTests(basis: Readonly<HostedPackagedReleaseBasisV2>): Promise<void> {
  return revalidate(basis, "controlled-test");
}

export function isControlledPackagedReleaseBasisForTests(value: unknown): boolean {
  return typeof value === "object" && value !== null && issuedPackagedBases.get(value as object)?.issuance === "controlled-test";
}
