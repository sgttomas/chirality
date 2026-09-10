import { createHash, randomUUID } from "node:crypto";
import { constants } from "node:fs";
import { link, lstat, mkdir, open, readdir, realpath, unlink } from "node:fs/promises";
import { dirname, isAbsolute, join, relative, resolve, sep } from "node:path";
import {
  verifyPackagedRuntimeBasisV2,
  type RuntimeArtifactEntryV2,
  type RuntimeSupportProfileV2,
  type VerifiedPackagedRuntimeBasisV2
} from "@chirality/runtime-core/runtime-conformance-v2";
import {
  inspectRuntimePurposeAcceptanceV2,
  inspectRuntimePurposeReleaseV2,
  type RuntimePurposeV2
} from "./runtime-conformance-v2-admission.js";

const HEX = /^[a-f0-9]{64}$/;
const MAX_FILE_BYTES = 1_048_576;
const GOVERNANCE_NAMES = Object.freeze([
  "login-purpose-record.json",
  "login-purpose-acceptance.json",
  "login-owner-act",
  "worker-purpose-record.json",
  "worker-purpose-acceptance.json",
  "worker-owner-act"
] as const);

export interface AcceptedHostedReleaseProvisioningV2 {
  runtimeDirectory: string;
  resourcesRoot: string;
  acceptedGovernanceRoot: string;
  expectedOuterInventorySha256: string;
  login: { activationId: string; gateIdentity: "D36" };
  worker: { activationId: string; gateIdentity: string };
}

export interface InstalledHostedReleaseAnchorV2 {
  anchorPath: string;
  anchorSha256: string;
  outerInventorySha256: string;
  governanceSha256: readonly [string, string, string, string, string, string];
  disposition: "created" | "already-identical";
}

type StableFile = Readonly<{ bytes: Buffer; sha256: string }>;
type PurposeAnchor = Readonly<{
  recordSha256: string;
  acceptanceSha256: string;
  ownerActSha256: string;
  activationId: string;
  gateIdentity: string;
}>;
type ReleaseAnchor = Readonly<{
  schema: "chirality-runtime-release-anchor/v2";
  outerInventorySha256: string;
  login: PurposeAnchor;
  worker: PurposeAnchor;
}>;
type Observation = Readonly<{
  verified: Readonly<VerifiedPackagedRuntimeBasisV2>;
  files: ReadonlyMap<(typeof GOVERNANCE_NAMES)[number], StableFile>;
  anchor: ReleaseAnchor;
  anchorBytes: Buffer;
  anchorSha256: string;
}>;

const hash = (value: string | Buffer): string => createHash("sha256").update(value).digest("hex");
const canonical = (value: unknown): value is string => typeof value === "string" && value.length <= 4095 && isAbsolute(value) && resolve(value) === value && !/[\x00-\x1f\x7f]/u.test(value);
const text = (value: unknown): value is string => typeof value === "string" && value.trim() === value && value.length > 0 && Buffer.byteLength(value, "utf8") <= 512 && !/[\x00-\x1f\x7f]/u.test(value);
const childOf = (parent: string, child: string): boolean => { const value = relative(parent, child); return value !== "" && value !== ".." && !value.startsWith(`..${sep}`) && !isAbsolute(value); };
const overlaps = (left: string, right: string): boolean => left === right || childOf(left, right) || childOf(right, left);
const invalid = (message: string): Error => new Error(`Hosted release provisioning refused: ${message}`);

async function inspectOwnerDirectory(path: string): Promise<void> {
  if (!canonical(path) || await realpath(path) !== path) throw invalid("owner directory is noncanonical");
  const info = await lstat(path);
  if (!info.isDirectory() || info.isSymbolicLink() || info.uid !== (process.getuid?.() ?? -1) || (info.mode & 0o777) !== 0o700) throw invalid("owner directory is not private");
}

/** File-custody primitive local to this owner tool; semantic parsing stays in the shared inspectors. */
async function stableOwnerFile(path: string): Promise<StableFile> {
  if (!canonical(path) || await realpath(path) !== path) throw invalid("owner file is noncanonical");
  const handle = await open(path, constants.O_RDONLY | constants.O_NOFOLLOW | constants.O_NONBLOCK);
  try {
    const before = await handle.stat({ bigint: true });
    if (!before.isFile() || before.nlink !== 1n || before.uid !== BigInt(process.getuid?.() ?? -1)
      || (before.mode & 0o777n) !== 0o600n || before.size > BigInt(MAX_FILE_BYTES)) throw invalid("owner file custody is invalid");
    const declared = Number(before.size), storage = Buffer.alloc(declared + 1);
    let offset = 0;
    while (offset < storage.length) {
      const { bytesRead } = await handle.read(storage, offset, storage.length - offset, offset);
      if (bytesRead === 0) break;
      offset += bytesRead;
    }
    const after = await handle.stat({ bigint: true }), current = await lstat(path, { bigint: true });
    for (const key of ["dev", "ino", "size", "mtimeNs", "ctimeNs", "mode", "uid", "nlink"] as const) {
      if (before[key] !== after[key] || before[key] !== current[key]) throw invalid("owner file changed while reading");
    }
    if (offset !== declared || await realpath(path) !== path) throw invalid("owner file changed while reading");
    const bytes = storage.subarray(0, declared);
    return Object.freeze({ bytes: Buffer.from(bytes), sha256: hash(bytes) });
  } finally { await handle.close(); }
}

async function syncDirectory(path: string): Promise<void> {
  const handle = await open(path, constants.O_RDONLY | constants.O_DIRECTORY | constants.O_NOFOLLOW);
  try { await handle.sync(); } finally { await handle.close(); }
}

async function ensurePrivateChild(parent: string, name: "release-authority" | "v2"): Promise<string> {
  const path = join(parent, name);
  try { await mkdir(path, { mode: 0o700 }); }
  catch (error) { if ((error as NodeJS.ErrnoException).code !== "EEXIST") throw error; }
  await inspectOwnerDirectory(path);
  // Sync even an existing entry: a prior failed publisher may have created it
  // without durably publishing the parent directory entry.
  await syncDirectory(parent);
  return path;
}

function parseJson(source: StableFile, label: string): unknown {
  try { return JSON.parse(source.bytes.toString("utf8")); }
  catch { throw invalid(`${label} is not JSON`); }
}

function governanceEntry(verified: Readonly<VerifiedPackagedRuntimeBasisV2>, name: string): RuntimeArtifactEntryV2 {
  const relativePath = `runtime-governance/v2/${name}`;
  const entry = verified.inventory.governance.find(value => value.relativePath === relativePath);
  if (!entry) throw invalid(`packaged governance is missing ${name}`);
  return entry;
}

function purposeAnchor(input: {
  purpose: RuntimePurposeV2;
  files: ReadonlyMap<string, StableFile>;
  verified: Readonly<VerifiedPackagedRuntimeBasisV2>;
  activationId: string;
  gateIdentity: string;
}): PurposeAnchor {
  const prefix = input.purpose === "login" ? "login" : "worker";
  const record = input.files.get(`${prefix}-purpose-record.json`)!;
  const acceptance = input.files.get(`${prefix}-purpose-acceptance.json`)!;
  const ownerAct = input.files.get(`${prefix}-owner-act`)!;
  if (!text(input.activationId) || !text(input.gateIdentity) || (input.purpose === "login" && input.gateIdentity !== "D36")) throw invalid("purpose activation or gate is invalid");
  const recordValue = parseJson(record, `${prefix} record`);
  const declared = recordValue && typeof recordValue === "object" && !Array.isArray(recordValue)
    ? (recordValue as Record<string, unknown>).supportProfileDigests : undefined;
  if (!Array.isArray(declared) || declared.length < 1 || declared.length > 8 || declared.some(value => typeof value !== "string")) throw invalid("purpose support profiles are invalid");
  const profiles = declared.map(profileDigest => input.verified.payload.supportProfiles.find(profile => profile.profileDigest === profileDigest));
  if (profiles.some(profile => profile === undefined) || new Set(declared).size !== declared.length) throw invalid("purpose support profile is not in the verified payload");
  for (const profile of profiles as RuntimeSupportProfileV2[]) {
    const release = inspectRuntimePurposeReleaseV2({ purpose: input.purpose, record: recordValue, expected: { payloadDigest: input.verified.payloadDigest, supportProfile: profile } });
    inspectRuntimePurposeAcceptanceV2({ purpose: input.purpose, acceptance: parseJson(acceptance, `${prefix} acceptance`), expected: {
      recordSha256: record.sha256, sourceDigest: release.sourceDigest, ownerActSha256: ownerAct.sha256,
      activationId: input.activationId, gateIdentity: input.gateIdentity
    } });
  }
  return Object.freeze({ recordSha256: record.sha256, acceptanceSha256: acceptance.sha256, ownerActSha256: ownerAct.sha256, activationId: input.activationId, gateIdentity: input.gateIdentity });
}

function encodeAnchor(value: ReleaseAnchor): Buffer {
  return Buffer.from(`${JSON.stringify({
    schema: value.schema,
    outerInventorySha256: value.outerInventorySha256,
    login: { recordSha256: value.login.recordSha256, acceptanceSha256: value.login.acceptanceSha256, ownerActSha256: value.login.ownerActSha256, activationId: value.login.activationId, gateIdentity: value.login.gateIdentity },
    worker: { recordSha256: value.worker.recordSha256, acceptanceSha256: value.worker.acceptanceSha256, ownerActSha256: value.worker.ownerActSha256, activationId: value.worker.activationId, gateIdentity: value.worker.gateIdentity }
  })}\n`, "utf8");
}

async function observe(input: AcceptedHostedReleaseProvisioningV2): Promise<Observation> {
  if (!canonical(input.resourcesRoot) || !canonical(input.runtimeDirectory) || !canonical(input.acceptedGovernanceRoot)
    || !HEX.test(input.expectedOuterInventorySha256) || overlaps(input.resourcesRoot,input.runtimeDirectory)
    || overlaps(input.resourcesRoot,input.acceptedGovernanceRoot) || overlaps(input.runtimeDirectory,input.acceptedGovernanceRoot)
    || !childOf(input.runtimeDirectory, join(input.runtimeDirectory, "release-authority"))) throw invalid("input is invalid");
  await inspectOwnerDirectory(input.runtimeDirectory);
  await inspectOwnerDirectory(input.acceptedGovernanceRoot);
  const names = (await readdir(input.acceptedGovernanceRoot)).sort();
  if (names.length !== GOVERNANCE_NAMES.length || names.some((name, index) => name !== [...GOVERNANCE_NAMES].sort()[index])) throw invalid("accepted governance root must contain exactly six files");
  const files = new Map<(typeof GOVERNANCE_NAMES)[number], StableFile>();
  for (const name of GOVERNANCE_NAMES) files.set(name, await stableOwnerFile(join(input.acceptedGovernanceRoot, name)));
  const verified = await verifyPackagedRuntimeBasisV2({ resourcesRoot: input.resourcesRoot });
  if (verified.inventorySha256 !== input.expectedOuterInventorySha256) throw invalid("outer inventory does not match owner pin");
  for (const name of GOVERNANCE_NAMES) {
    const accepted = files.get(name)!;
    const packaged = governanceEntry(verified, name);
    if (packaged.sha256 !== accepted.sha256 || packaged.size !== accepted.bytes.length) throw invalid("packaged governance differs from accepted source");
  }
  const login = purposeAnchor({ purpose: "login", files, verified, ...input.login });
  const worker = purposeAnchor({ purpose: "worker", files, verified, ...input.worker });
  const anchor = Object.freeze({ schema: "chirality-runtime-release-anchor/v2" as const, outerInventorySha256: input.expectedOuterInventorySha256, login, worker });
  const anchorBytes = encodeAnchor(anchor);
  return Object.freeze({ verified, files, anchor, anchorBytes, anchorSha256: hash(anchorBytes) });
}

async function publishAnchor(anchorPath: string, bytes: Buffer): Promise<"created" | "already-identical"> {
  const directory = dirname(anchorPath), temporary = join(directory, `.release-anchor.${process.pid}.${randomUUID()}.tmp`);
  let disposition: "created" | "already-identical" = "created";
  const output = await open(temporary, constants.O_WRONLY | constants.O_CREAT | constants.O_EXCL | constants.O_NOFOLLOW, 0o600);
  try {
    try { await output.writeFile(bytes); await output.sync(); } finally { await output.close(); }
    try { await link(temporary, anchorPath); }
    catch (error) {
      if ((error as NodeJS.ErrnoException).code !== "EEXIST") throw error;
      disposition = "already-identical";
    }
    await syncDirectory(directory);
  } finally {
    let cleanupFailure: unknown;
    try { await unlink(temporary); } catch (error) { cleanupFailure = error; }
    try { await syncDirectory(directory); } catch (error) { cleanupFailure ??= error; }
    if (cleanupFailure) throw cleanupFailure;
  }
  const installed = await stableOwnerFile(anchorPath);
  if (installed.sha256 !== hash(bytes) || !installed.bytes.equals(bytes)) throw invalid("installed anchor conflicts with accepted anchor");
  return disposition;
}

export async function installHostedReleaseAnchorV2(input: AcceptedHostedReleaseProvisioningV2): Promise<Readonly<InstalledHostedReleaseAnchorV2>> {
  const frozen = structuredClone(input);
  const first = await observe(frozen);
  const authorityRoot = await ensurePrivateChild(frozen.runtimeDirectory, "release-authority");
  const anchorRoot = await ensurePrivateChild(authorityRoot, "v2");
  const anchorPath = join(anchorRoot, "release-anchor.json");
  const disposition = await publishAnchor(anchorPath, first.anchorBytes);
  await inspectOwnerDirectory(frozen.runtimeDirectory); await inspectOwnerDirectory(authorityRoot); await inspectOwnerDirectory(anchorRoot);
  const final = await observe(frozen), installed = await stableOwnerFile(anchorPath);
  if (final.anchorSha256 !== first.anchorSha256 || !final.anchorBytes.equals(first.anchorBytes)
    || final.verified.inventorySha256 !== first.verified.inventorySha256 || installed.sha256 !== first.anchorSha256 || !installed.bytes.equals(first.anchorBytes)) throw invalid("release inputs changed during installation");
  const governanceSha256 = GOVERNANCE_NAMES.map(name => first.files.get(name)!.sha256) as [string, string, string, string, string, string];
  return Object.freeze({ anchorPath, anchorSha256: first.anchorSha256, outerInventorySha256: first.anchor.outerInventorySha256, governanceSha256: Object.freeze(governanceSha256), disposition });
}
