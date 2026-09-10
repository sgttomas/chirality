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
import { REQUIRED_RUNTIME_CONFORMANCE_LIMBS } from "@chirality/runtime-core";
import {
  inspectRuntimePurposeAcceptanceV2,
  inspectRuntimePurposeReleaseV2,
  type RuntimePurposeV2
} from "./runtime-conformance-v2-admission.js";
import { inspectHostAccountSignedPeerIdentity, type VerifiedHostAccountPackagedIdentity } from "./host-account-release.js";

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
  trial?: {
    observationPath: string;
    expectedObservationSha256: string;
    executablePath: string;
  };
}

const LOGIN_LIMBS = Object.freeze(["exact-supplier", "keyring-backend", "plaintext-fallback-absent", "process-containment", "storage-isolation", "provider-network", "bounded-protocol-purpose", "retirement"] as const);
const TRIAL_PREREQUISITES = Object.freeze(["signed-payload-and-supply", "trusted-app-and-account-host", "native-enforcement-and-retirement", "connected-source-contract"] as const);
type DigestEvidence<N extends string> = Readonly<Record<N, string>>;
export interface HostedReleaseGovernancePreparationV2 {
  payloadDigest: string;
  supportProfile: RuntimeSupportProfileV2;
  issuedAt: string;
  expiresAt: string;
  ownerReference: string;
  login: { activationId: string; gateIdentity: "D36"; ownerAct: Buffer; evidence: DigestEvidence<(typeof LOGIN_LIMBS)[number]> };
  worker: { activationId: string; gateIdentity: string; ownerAct: Buffer; prerequisites: DigestEvidence<(typeof TRIAL_PREREQUISITES)[number]> };
}
export type HostedReleaseGovernanceFilesV2 = Readonly<Record<(typeof GOVERNANCE_NAMES)[number], Readonly<{ bytes: Buffer; sha256: string }>>>;

export interface InstalledHostedReleaseAnchorV2 {
  anchorPath: string;
  anchorSha256: string;
  outerInventorySha256: string;
  governanceSha256: readonly [string, string, string, string, string, string];
  disposition: "created" | "already-identical";
  trialObservationPath?: string;
  trialObservationSha256?: string;
}

type StableFile = Readonly<{ bytes: Buffer; sha256: string }>;
type PurposeAnchor = Readonly<{
  recordSha256: string;
  acceptanceSha256: string;
  ownerActSha256: string;
  activationId: string;
  gateIdentity: string;
  disposition: "qualified" | "local-human-trial";
}>;
type QualifiedReleaseAnchor = Readonly<{
  schema: "chirality-runtime-release-anchor/v2";
  outerInventorySha256: string;
  login: PurposeAnchor;
  worker: PurposeAnchor;
}>;
type TrialReleaseAnchor = Readonly<{
  schema: "chirality-runtime-release-anchor/v3";
  outerInventorySha256: string;
  login: PurposeAnchor;
  worker: PurposeAnchor;
  postSealObservationSha256: string;
}>;
type ReleaseAnchor = QualifiedReleaseAnchor | TrialReleaseAnchor;
export interface HostedReleaseTrialSealObservationV1 {
  schema: "chirality-runtime-trial-seal-observation/v1";
  outerInventorySha256: string;
  payloadDigest: string;
  mainCodeDirectoryHash: string;
  peerRequirementSha256: string;
  checks: Readonly<Record<"signed-app" | "fuses-and-asar" | "signed-peer-identity-binding", Readonly<{ attempted: true; passed: true; evidenceSha256: string }>>>;
}
type Observation = Readonly<{
  verified: Readonly<VerifiedPackagedRuntimeBasisV2>;
  files: ReadonlyMap<(typeof GOVERNANCE_NAMES)[number], StableFile>;
  anchor: ReleaseAnchor;
  anchorBytes: Buffer;
  anchorSha256: string;
  trialObservation?: StableFile;
}>;

const hash = (value: string | Buffer): string => createHash("sha256").update(value).digest("hex");
const canonical = (value: unknown): value is string => typeof value === "string" && value.length <= 4095 && isAbsolute(value) && resolve(value) === value && !/[\x00-\x1f\x7f]/u.test(value);
const text = (value: unknown): value is string => typeof value === "string" && value.trim() === value && value.length > 0 && Buffer.byteLength(value, "utf8") <= 512 && !/[\x00-\x1f\x7f]/u.test(value);
const childOf = (parent: string, child: string): boolean => { const value = relative(parent, child); return value !== "" && value !== ".." && !value.startsWith(`..${sep}`) && !isAbsolute(value); };
const overlaps = (left: string, right: string): boolean => left === right || childOf(left, right) || childOf(right, left);
const invalid = (message: string): Error => new Error(`Hosted release provisioning refused: ${message}`);
function exactKeys(value: unknown, names: readonly string[]): value is Record<string, unknown> {
  return !!value && typeof value === "object" && !Array.isArray(value) && Object.keys(value).length === names.length && names.every(name => Object.hasOwn(value, name));
}

function releaseCommon(input: HostedReleaseGovernancePreparationV2) {
  return { sourceDigest: input.supportProfile.compiler.sourceDigest, payloadDigest: input.payloadDigest, supportProfileDigests: [input.supportProfile.profileDigest],
    policyContractDigest: input.supportProfile.compiler.parameterSchemaDigest, supplyProfileDigest: hash(`${JSON.stringify(input.supportProfile.supplier)}\n`), issuedAt: input.issuedAt, expiresAt: input.expiresAt };
}
const encoded = (value: unknown): Buffer => Buffer.from(`${JSON.stringify(value)}\n`, "utf8");
/** Factual six-file assembly. All authority and evidence bytes are explicit inputs; this function performs no observation or owner act. */
export function prepareHostedReleaseGovernanceV2(input: HostedReleaseGovernancePreparationV2): HostedReleaseGovernanceFilesV2 {
  if (!digest64(input.payloadDigest) || !text(input.ownerReference) || !Buffer.isBuffer(input.login.ownerAct) || !input.login.ownerAct.length || !Buffer.isBuffer(input.worker.ownerAct) || !input.worker.ownerAct.length) throw invalid("governance recipe is invalid");
  const loginEvidence=Object.fromEntries(LOGIN_LIMBS.map(name=>{const value=input.login.evidence[name];if(!digest64(value))throw invalid("login evidence is invalid");return[name,{attempted:true,passed:true,evidenceSha256:value}];}));
  const prerequisites=Object.fromEntries(TRIAL_PREREQUISITES.map(name=>{const value=input.worker.prerequisites[name];if(!digest64(value))throw invalid("worker prerequisite evidence is invalid");return[name,{attempted:true,passed:true,evidenceSha256:value}];}));
  const common=releaseCommon(input);
  const loginRecord=encoded({schema:"chirality-codex-login-purpose-release/v2",evidenceClass:"exact-account-free-login-purpose-observed",...common,backend:{credentialStore:"keyring",plaintextFallback:false},methods:["account/login/start","account/login/cancel","account/read","model/list"],modelExecution:false,limbs:loginEvidence});
  const workerRecord=encoded({schema:"chirality-codex-worker-purpose-release/v3",evidenceClass:"exact-local-human-trial-authorized",...common,limbs:Object.fromEntries(REQUIRED_RUNTIME_CONFORMANCE_LIMBS.map(name=>[name,{status:"pending-human-trial"}])),trialScope:"local-human-functional-trial",prerequisites});
  const acceptance=(purpose:RuntimePurposeV2,record:Buffer,ownerAct:Buffer,activationId:string,gateIdentity:string)=>encoded({schema:"chirality-runtime-conformance-acceptance/v1",status:"accepted",recordSha256:hash(record),sourceDigest:input.supportProfile.compiler.sourceDigest,activationId,gateIdentity,ownerActSha256:hash(ownerAct),ownerReference:input.ownerReference,expiresAt:input.expiresAt});
  const loginAcceptance=acceptance("login",loginRecord,input.login.ownerAct,input.login.activationId,input.login.gateIdentity),workerAcceptance=acceptance("worker",workerRecord,input.worker.ownerAct,input.worker.activationId,input.worker.gateIdentity);
  inspectRuntimePurposeReleaseV2({purpose:"login",record:JSON.parse(loginRecord.toString("utf8")),expected:{payloadDigest:input.payloadDigest,supportProfile:input.supportProfile}});
  inspectRuntimePurposeReleaseV2({purpose:"worker",record:JSON.parse(workerRecord.toString("utf8")),expected:{payloadDigest:input.payloadDigest,supportProfile:input.supportProfile}});
  inspectRuntimePurposeAcceptanceV2({purpose:"login",acceptance:JSON.parse(loginAcceptance.toString("utf8")),expected:{recordSha256:hash(loginRecord),sourceDigest:input.supportProfile.compiler.sourceDigest,ownerActSha256:hash(input.login.ownerAct),activationId:input.login.activationId,gateIdentity:input.login.gateIdentity}});
  inspectRuntimePurposeAcceptanceV2({purpose:"worker",acceptance:JSON.parse(workerAcceptance.toString("utf8")),expected:{recordSha256:hash(workerRecord),sourceDigest:input.supportProfile.compiler.sourceDigest,ownerActSha256:hash(input.worker.ownerAct),activationId:input.worker.activationId,gateIdentity:input.worker.gateIdentity}});
  const values={"login-purpose-record.json":loginRecord,"login-purpose-acceptance.json":loginAcceptance,"login-owner-act":Buffer.from(input.login.ownerAct),"worker-purpose-record.json":workerRecord,"worker-purpose-acceptance.json":workerAcceptance,"worker-owner-act":Buffer.from(input.worker.ownerAct)};
  return Object.freeze(Object.fromEntries(GOVERNANCE_NAMES.map(name=>[name,Object.freeze({bytes:values[name],sha256:hash(values[name])})])) as unknown as HostedReleaseGovernanceFilesV2);
}

const evidenceDigest = (schema: string, evidence: unknown): string => hash(`${JSON.stringify({ schema, evidence })}\n`);
type InspectSignedPeerIdentity = (input: { executablePath: string; resourcesPath: string }) => Promise<VerifiedHostAccountPackagedIdentity>;
async function observeTrialSeal(input: { resourcesRoot: string; executablePath: string }, inspectIdentity: InspectSignedPeerIdentity) {
  if (!canonical(input.resourcesRoot) || !canonical(input.executablePath)) throw invalid("trial observation input is invalid");
  const verified = await verifyPackagedRuntimeBasisV2({ resourcesRoot: input.resourcesRoot });
  const identity = await inspectIdentity({ executablePath: input.executablePath, resourcesPath: input.resourcesRoot });
  const observation: HostedReleaseTrialSealObservationV1 = Object.freeze({
    schema: "chirality-runtime-trial-seal-observation/v1",
    outerInventorySha256: verified.inventorySha256,
    payloadDigest: verified.payloadDigest,
    mainCodeDirectoryHash: identity.subject.cdHash,
    peerRequirementSha256: hash(identity.effectivePeerRequirement),
    checks: Object.freeze({
      "signed-app": Object.freeze({ attempted: true, passed: true, evidenceSha256: evidenceDigest("chirality-runtime-trial-signed-app-evidence/v1", { subject: identity.subject, outer: identity.outer }) }),
      "fuses-and-asar": Object.freeze({ attempted: true, passed: true, evidenceSha256: evidenceDigest("chirality-runtime-trial-fuses-and-asar-evidence/v1", { fuses: identity.fuses, asarIntegrity: identity.asarIntegrity, outerInventorySha256: verified.inventorySha256, payloadDigest: verified.payloadDigest }) }),
      "signed-peer-identity-binding": Object.freeze({ attempted: true, passed: true, evidenceSha256: evidenceDigest("chirality-runtime-trial-signed-peer-identity-binding-evidence/v1", { predicate: identity.predicate, effectivePeerRequirement: identity.effectivePeerRequirement, subject: identity.subject }) })
    })
  });
  const bytes = Buffer.from(`${JSON.stringify(observation)}\n`, "utf8");
  return Object.freeze({ observation, bytes, sha256: hash(bytes) });
}

export function observeHostedReleaseTrialSealV1(input: { resourcesRoot: string; executablePath: string }) {
  return observeTrialSeal(input, inspectHostAccountSignedPeerIdentity);
}

/** Controlled source test seam. It cannot issue an acceptance, anchor, basis or host authority. */
export function observeHostedReleaseTrialSealV1ControlledForTests(input: { resourcesRoot: string; executablePath: string }, inspectIdentity: InspectSignedPeerIdentity) {
  return observeTrialSeal(input, inspectIdentity);
}

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
  let disposition: "qualified" | "local-human-trial" | undefined;
  for (const profile of profiles as RuntimeSupportProfileV2[]) {
    const release = inspectRuntimePurposeReleaseV2({ purpose: input.purpose, record: recordValue, expected: { payloadDigest: input.verified.payloadDigest, supportProfile: profile } });
    if (disposition !== undefined && release.disposition !== disposition) throw invalid("purpose release disposition changed across support profiles");
    disposition = release.disposition;
    inspectRuntimePurposeAcceptanceV2({ purpose: input.purpose, acceptance: parseJson(acceptance, `${prefix} acceptance`), expected: {
      recordSha256: record.sha256, sourceDigest: release.sourceDigest, ownerActSha256: ownerAct.sha256,
      activationId: input.activationId, gateIdentity: input.gateIdentity
    } });
  }
  return Object.freeze({ recordSha256: record.sha256, acceptanceSha256: acceptance.sha256, ownerActSha256: ownerAct.sha256, activationId: input.activationId, gateIdentity: input.gateIdentity, disposition: disposition! });
}

function encodeAnchor(value: ReleaseAnchor): Buffer {
  const encoded: Record<string, unknown> = {
    schema: value.schema,
    outerInventorySha256: value.outerInventorySha256,
    login: { recordSha256: value.login.recordSha256, acceptanceSha256: value.login.acceptanceSha256, ownerActSha256: value.login.ownerActSha256, activationId: value.login.activationId, gateIdentity: value.login.gateIdentity },
    worker: { recordSha256: value.worker.recordSha256, acceptanceSha256: value.worker.acceptanceSha256, ownerActSha256: value.worker.ownerActSha256, activationId: value.worker.activationId, gateIdentity: value.worker.gateIdentity }
  };
  if (value.schema === "chirality-runtime-release-anchor/v3") encoded.postSealObservationSha256 = value.postSealObservationSha256;
  return Buffer.from(`${JSON.stringify(encoded)}\n`, "utf8");
}

async function inspectTrialObservation(input: AcceptedHostedReleaseProvisioningV2, verified: Readonly<VerifiedPackagedRuntimeBasisV2>, inspectIdentity: InspectSignedPeerIdentity): Promise<StableFile> {
  const trial = input.trial;
  if (!trial || !canonical(trial.observationPath) || !canonical(trial.executablePath) || !HEX.test(trial.expectedObservationSha256)) throw invalid("trial observation input is invalid");
  await inspectOwnerDirectory(dirname(trial.observationPath));
  const source = await stableOwnerFile(trial.observationPath);
  if (source.sha256 !== trial.expectedObservationSha256) throw invalid("trial observation does not match owner pin");
  const value = parseJson(source, "trial observation");
  const checkNames = ["signed-app", "fuses-and-asar", "signed-peer-identity-binding"] as const;
  if (!exactKeys(value, ["schema", "outerInventorySha256", "payloadDigest", "mainCodeDirectoryHash", "peerRequirementSha256", "checks"])
    || value.schema !== "chirality-runtime-trial-seal-observation/v1" || value.outerInventorySha256 !== input.expectedOuterInventorySha256
    || value.payloadDigest !== verified.payloadDigest || typeof value.mainCodeDirectoryHash !== "string" || !/^[a-f0-9]{40}$/u.test(value.mainCodeDirectoryHash)
    || !digest64(value.peerRequirementSha256) || !exactKeys(value.checks, checkNames)) throw invalid("trial observation is invalid");
  for (const name of checkNames) {
    const check = value.checks[name];
    if (!exactKeys(check, ["attempted", "passed", "evidenceSha256"]) || check.attempted !== true || check.passed !== true || !digest64(check.evidenceSha256)) throw invalid("trial observation is invalid");
  }
  const identity = await inspectIdentity({ executablePath: trial.executablePath, resourcesPath: input.resourcesRoot });
  if (value.mainCodeDirectoryHash !== identity.subject.cdHash || value.peerRequirementSha256 !== hash(identity.effectivePeerRequirement)) throw invalid("trial observation does not match signed subject");
  return source;
}

const digest64 = (value: unknown): value is string => typeof value === "string" && HEX.test(value);

async function observe(input: AcceptedHostedReleaseProvisioningV2, inspectIdentity: InspectSignedPeerIdentity): Promise<Observation> {
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
  if (login.disposition !== "qualified") throw invalid("login purpose cannot use trial disposition");
  if ((worker.disposition === "local-human-trial") !== (input.trial !== undefined)) throw invalid("trial observation must exactly match worker disposition");
  const trialObservation = worker.disposition === "local-human-trial" ? await inspectTrialObservation(input, verified, inspectIdentity) : undefined;
  const anchor: ReleaseAnchor = trialObservation
    ? Object.freeze({ schema: "chirality-runtime-release-anchor/v3" as const, outerInventorySha256: input.expectedOuterInventorySha256, login, worker, postSealObservationSha256: trialObservation.sha256 })
    : Object.freeze({ schema: "chirality-runtime-release-anchor/v2" as const, outerInventorySha256: input.expectedOuterInventorySha256, login, worker });
  const anchorBytes = encodeAnchor(anchor);
  return Object.freeze({ verified, files, anchor, anchorBytes, anchorSha256: hash(anchorBytes), ...(trialObservation ? { trialObservation } : {}) });
}

async function publishFile(path: string, bytes: Buffer): Promise<"created" | "already-identical"> {
  const directory = dirname(path), temporary = join(directory, `.${path.split("/").at(-1)}.${process.pid}.${randomUUID()}.tmp`);
  let disposition: "created" | "already-identical" = "created";
  const output = await open(temporary, constants.O_WRONLY | constants.O_CREAT | constants.O_EXCL | constants.O_NOFOLLOW, 0o600);
  try {
    try { await output.writeFile(bytes); await output.sync(); } finally { await output.close(); }
    try { await link(temporary, path); }
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
  const installed = await stableOwnerFile(path);
  if (installed.sha256 !== hash(bytes) || !installed.bytes.equals(bytes)) throw invalid("installed anchor conflicts with accepted anchor");
  return disposition;
}

async function install(input: AcceptedHostedReleaseProvisioningV2, inspectIdentity: InspectSignedPeerIdentity): Promise<Readonly<InstalledHostedReleaseAnchorV2>> {
  const frozen = structuredClone(input);
  const first = await observe(frozen, inspectIdentity);
  const authorityRoot = await ensurePrivateChild(frozen.runtimeDirectory, "release-authority");
  const anchorRoot = await ensurePrivateChild(authorityRoot, "v2");
  const anchorPath = join(anchorRoot, "release-anchor.json");
  if (first.trialObservation) await publishFile(join(anchorRoot, "trial-seal-observation.json"), first.trialObservation.bytes);
  const disposition = await publishFile(anchorPath, first.anchorBytes);
  await inspectOwnerDirectory(frozen.runtimeDirectory); await inspectOwnerDirectory(authorityRoot); await inspectOwnerDirectory(anchorRoot);
  const final = await observe(frozen, inspectIdentity), installed = await stableOwnerFile(anchorPath);
  if (final.anchorSha256 !== first.anchorSha256 || !final.anchorBytes.equals(first.anchorBytes)
    || final.verified.inventorySha256 !== first.verified.inventorySha256 || installed.sha256 !== first.anchorSha256 || !installed.bytes.equals(first.anchorBytes)) throw invalid("release inputs changed during installation");
  if (first.trialObservation) {
    const installedObservation = await stableOwnerFile(join(anchorRoot, "trial-seal-observation.json"));
    if (!final.trialObservation || installedObservation.sha256 !== first.trialObservation.sha256 || !installedObservation.bytes.equals(first.trialObservation.bytes)) throw invalid("release inputs changed during installation");
  }
  const governanceSha256 = GOVERNANCE_NAMES.map(name => first.files.get(name)!.sha256) as [string, string, string, string, string, string];
  return Object.freeze({ anchorPath, anchorSha256: first.anchorSha256, outerInventorySha256: first.anchor.outerInventorySha256, governanceSha256: Object.freeze(governanceSha256), disposition,
    ...(first.trialObservation ? { trialObservationPath: join(anchorRoot, "trial-seal-observation.json"), trialObservationSha256: first.trialObservation.sha256 } : {}) });
}

export async function installHostedReleaseAnchorV2(input: AcceptedHostedReleaseProvisioningV2): Promise<Readonly<InstalledHostedReleaseAnchorV2>> {
  return install(input, inspectHostAccountSignedPeerIdentity);
}

/** Controlled source test seam. It cannot issue a packaged basis or host authority. */
export async function installHostedReleaseAnchorV2ControlledForTests(input: AcceptedHostedReleaseProvisioningV2, inspectIdentity: InspectSignedPeerIdentity): Promise<Readonly<InstalledHostedReleaseAnchorV2>> {
  return install(input, inspectIdentity);
}
