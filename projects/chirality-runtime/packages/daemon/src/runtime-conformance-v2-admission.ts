import { createHash } from "node:crypto";
import { constants } from "node:fs";
import { lstat, open, realpath } from "node:fs/promises";
import { isAbsolute, relative, resolve, sep } from "node:path";
import { RuntimeError } from "@chirality/runtime-contracts";
import {
  REQUIRED_RUNTIME_CONFORMANCE_LIMBS,
  compareRuntimeUtf8V2,
  matchRuntimeSupportProfileV2,
  type RuntimeSupportProfileV2
} from "@chirality/runtime-core";
import { revalidateIssuedPackagedReleaseBasisV2, type HostedPackagedReleaseBasisV2 } from "./hosted-packaged-release-state.js";
import { HostAccountAuthority, type HostAccountAdmissionLeaseSnapshot } from "./host-account-authority.js";

export type RuntimePurposeV2 = "login" | "worker";
export type RuntimeWorkerReleaseDispositionV2 = "qualified" | "local-human-trial";
export type RuntimeSha256AdmissionV2 = string;

export interface RuntimePurposeReleaseSourceV2 {
  purpose: RuntimePurposeV2;
  recordPath: string;
  recordSha256: RuntimeSha256AdmissionV2;
  acceptancePath: string;
  acceptanceSha256: RuntimeSha256AdmissionV2;
  ownerActPath: string;
  ownerActSha256: RuntimeSha256AdmissionV2;
  activationId: string;
  gateIdentity: string;
  payloadDigest: RuntimeSha256AdmissionV2;
  supportProfile: RuntimeSupportProfileV2;
}

export interface RuntimePurposeReleaseAdmissionV2 {
  readonly purpose: RuntimePurposeV2;
  readonly recordSha256: RuntimeSha256AdmissionV2;
  readonly ownerReference: string;
  readonly profileDigest: RuntimeSha256AdmissionV2;
  readonly evidence: "externally-accepted-release-purpose-v2";
  readonly disposition: RuntimeWorkerReleaseDispositionV2;
}

declare const hostedAuthorityBrand: unique symbol;
export interface HostedAccountAuthorityAdmission {
  readonly evidence: "accepted-host-account-authority";
  readonly mechanismId: string;
  readonly daemonGeneration: string;
  readonly authorityGeneration: string;
  readonly subjectBindingDigest: RuntimeSha256AdmissionV2;
  readonly liveLeaseDigest: RuntimeSha256AdmissionV2;
  readonly [hostedAuthorityBrand]: true;
}

export interface RuntimePackagedPolicyBasisV2 {
  schema: "chirality-runtime-packaged-basis/v2";
  resourcesRoot: string;
  inventoryPath: string;
  payloadManifestPath: string;
  outerInventorySha256: RuntimeSha256AdmissionV2;
  payloadDigest: RuntimeSha256AdmissionV2;
}

export interface CodexPolicyInstanceV2 {
  schema: "chirality-codex-policy-instance/v2";
  outerPurpose: "trusted-login" | "trusted-supplier";
  nativePurpose: null | "worker";
  canonicalRoot: string;
  privateDirectory: string;
  codexHome: string;
  executablePath: string;
  nativeAddonPath: string;
  providerNetworkConsent: { approvedBy: string; approvalReference: string };
  commandNetworkPosture: "off" | "ask-per-destination" | "on";
  immutableReadRoots: readonly string[];
  protectedPaths: readonly string[];
  readOnlyProjectPaths: readonly string[];
  trustedRuntimeReadRoots: readonly {
    path: string;
    readPaths: readonly string[];
    contentDigest: RuntimeSha256AdmissionV2;
    artifactInventory: RuntimePackagedPolicyBasisV2;
  }[];
  toolRuntime: {
    codexSelfExecutablePath: string;
    requiresSandboxedFileSystem: true;
    requiresSandboxedFileStreaming: true;
  };
  nativeRoleConfiguration: null | { digest: RuntimeSha256AdmissionV2; configOverrides: readonly string[] };
}

export interface RuntimeInstanceAdmissionInputV2 {
  purposeRelease: RuntimePurposeReleaseAdmissionV2;
  hostAuthority: HostedAccountAuthorityAdmission;
  projectId: string;
  manifestHash: RuntimeSha256AdmissionV2;
  canonicalRoot: string;
  cwd: string;
  privateDirectory: string;
  codexHome: string;
  brokerRoot: string;
  instructionRoot: string;
  nativeAddonPath: string;
  supplierExecutablePath: string;
  attachmentRoot: string;
  account: null | { accountId: string; accountEpoch: number; accountDigest: RuntimeSha256AdmissionV2 };
  consent: { version: RuntimeSha256AdmissionV2; digest: RuntimeSha256AdmissionV2; authenticatedExplicitUserAct: true };
  policy: CodexPolicyInstanceV2;
  outerPolicyDigest: RuntimeSha256AdmissionV2;
  nativePolicyDigest: null | RuntimeSha256AdmissionV2;
  effectiveConfigDigest: RuntimeSha256AdmissionV2;
}

export interface RuntimeInstanceAdmissionV2 {
  readonly purpose: RuntimePurposeV2;
  readonly evidence: "release-and-live-instance-v2";
}

export type RuntimeWorkerInstancePreparationInputV2 = Omit<RuntimeInstanceAdmissionInputV2, "hostAuthority" | "account">;
export interface RuntimeWorkerInstancePreparationV2 {
  readonly evidence: "release-live-host-policy-preparation-v2";
  readonly releaseBasis: Readonly<HostedPackagedReleaseBasisV2>;
  readonly source: HostAccountAuthority;
  readonly lease: HostAccountAdmissionLeaseSnapshot;
  readonly input: Readonly<RuntimeWorkerInstancePreparationInputV2>;
  readonly inputDigest: RuntimeSha256AdmissionV2;
}

type ReleaseState = { basis: Readonly<HostedPackagedReleaseBasisV2>; source: Readonly<RuntimePurposeReleaseSourceV2>; ownerReference: string; disposition: RuntimeWorkerReleaseDispositionV2 };
type InstanceState = { digest: string; input: RuntimeInstanceAdmissionInputV2 };
const releaseAdmissions = new WeakMap<object, ReleaseState>();
const hostAuthorities = new WeakMap<object, () => Promise<boolean>>();
const instanceAdmissions = new WeakMap<object, InstanceState>();

const LOGIN_LIMBS = Object.freeze(["exact-supplier", "keyring-backend", "plaintext-fallback-absent", "process-containment", "storage-isolation", "provider-network", "bounded-protocol-purpose", "retirement"] as const);
const HEX = /^[a-f0-9]{64}$/;
const unavailable = (reason: string) => new RuntimeError("ENGINE_UNAVAILABLE", "Runtime v2 admission is missing, invalid, stale or no longer live", 503, { reason });
const hash = (value: string | Buffer) => createHash("sha256").update(value).digest("hex");
const digest = (value: unknown): value is string => typeof value === "string" && HEX.test(value);
const text = (value: unknown, maximum = 512): value is string => typeof value === "string" && value.trim() === value && value.length > 0 && Buffer.byteLength(value) <= maximum && !/[\x00-\x1f\x7f]/u.test(value);
function exactKeys(value: unknown, names: readonly string[]): value is Record<string, unknown> {
  return !!value && typeof value === "object" && !Array.isArray(value) && Object.keys(value).length === names.length && names.every(name => Object.hasOwn(value, name));
}
function canonical(value: unknown): value is string {
  return typeof value === "string" && value.length <= 4095 && isAbsolute(value) && resolve(value) === value && !/[\x00-\x1f\x7f]/u.test(value);
}
function properChild(parent: string, child: string): boolean {
  const value = relative(parent, child);
  return value !== "" && value !== ".." && !value.startsWith(`..${sep}`) && !isAbsolute(value);
}
function strictlySorted(values: readonly string[]): boolean {
  return values.every((value, index) => index === 0 || compareRuntimeUtf8V2(values[index - 1]!, value) < 0);
}
export function hostAuthoritySubjectBindingDigestV2(input: { purpose: RuntimePurposeV2; projectId: string; manifestHash: string; canonicalRoot: string; account: RuntimeInstanceAdmissionInputV2["account"]; consentDigest: string }): string {
  if (!["login", "worker"].includes(input.purpose) || !text(input.projectId, 128) || !digest(input.manifestHash) || !canonical(input.canonicalRoot) || !digest(input.consentDigest)) throw unavailable("HOST_AUTHORITY_SUBJECT_INVALID");
  if (input.purpose === "login" ? input.account !== null : !input.account || !text(input.account.accountId) || !Number.isSafeInteger(input.account.accountEpoch) || input.account.accountEpoch < 0 || !digest(input.account.accountDigest)) throw unavailable("HOST_AUTHORITY_SUBJECT_INVALID");
  return hash(`${JSON.stringify({ schema: "chirality-host-account-authority-subject/v2", purpose: input.purpose, projectId: input.projectId, manifestHash: input.manifestHash,
    canonicalRoot: input.canonicalRoot, account: input.account, consentDigest: input.consentDigest })}\n`);
}
export async function revalidateHostedAccountAuthorityV2(
  authority: HostedAccountAuthorityAdmission,
  expected: { purpose: RuntimePurposeV2; projectId: string; manifestHash: string; canonicalRoot: string; account: RuntimeInstanceAdmissionInputV2["account"]; consentDigest: string }
): Promise<void> {
  const current = hostAuthorities.get(authority as object);
  if (!current || authority.evidence !== "accepted-host-account-authority"
    || authority.subjectBindingDigest !== hostAuthoritySubjectBindingDigestV2(expected)) throw unavailable("HOST_AUTHORITY_INVALID");
  if (!(await current())) throw unavailable("HOST_AUTHORITY_NOT_LIVE");
}

/** Package-internal issuer. Only a concrete live P2 authority can populate the private WeakMap. */
export function issueHostedAccountAuthorityV2FromP2(
  source: HostAccountAuthority,
  subject: { purpose: RuntimePurposeV2; projectId: string; manifestHash: string; canonicalRoot: string; account: RuntimeInstanceAdmissionInputV2["account"]; consentDigest: string }
): HostedAccountAuthorityAdmission {
  if (!(source instanceof HostAccountAuthority)) throw unavailable("HOST_AUTHORITY_SOURCE_INVALID");
  const lease = source.snapshotAdmissionLease();
  const admission = Object.freeze({
    evidence: "accepted-host-account-authority" as const,
    mechanismId: lease.mechanismId,
    daemonGeneration: lease.daemonGeneration,
    authorityGeneration: lease.authorityGeneration,
    subjectBindingDigest: hostAuthoritySubjectBindingDigestV2(subject),
    liveLeaseDigest: lease.liveLeaseDigest
  }) as HostedAccountAuthorityAdmission;
  hostAuthorities.set(admission as object, async () => source.matchesAdmissionLease(lease));
  return admission;
}

export async function prepareRuntimeWorkerInstanceV2FromP2(
  source: HostAccountAuthority,
  releaseBasis: Readonly<HostedPackagedReleaseBasisV2>,
  input: RuntimeWorkerInstancePreparationInputV2
): Promise<RuntimeWorkerInstancePreparationV2> {
  if (!(source instanceof HostAccountAuthority)) throw unavailable("HOST_AUTHORITY_SOURCE_INVALID");
  const inputDigest = inspectWorkerPreparationInput(input);
  const release = releaseAdmissions.get(input.purposeRelease as object);
  if (!release || release.basis !== releaseBasis) throw unavailable("PURPOSE_ADMISSION_INVALID");
  const lease = source.snapshotAdmissionLease();
  await revalidateRuntimePurposeReleaseV2(releaseBasis, input.purposeRelease);
  if (inspectWorkerPreparationInput(input) !== inputDigest || !source.matchesAdmissionLease(lease)) throw unavailable("WORKER_PREPARATION_CHANGED");
  return Object.freeze({ evidence: "release-live-host-policy-preparation-v2", releaseBasis, source, lease, input: Object.freeze({ ...input }), inputDigest });
}

export async function revalidateRuntimeWorkerInstancePreparationV2(preparation: RuntimeWorkerInstancePreparationV2): Promise<void> {
  if (!exactKeys(preparation, ["evidence", "releaseBasis", "source", "lease", "input", "inputDigest"])
    || preparation.evidence !== "release-live-host-policy-preparation-v2"
    || !(preparation.source instanceof HostAccountAuthority)
    || inspectWorkerPreparationInput(preparation.input) !== preparation.inputDigest
    || !preparation.source.matchesAdmissionLease(preparation.lease)) throw unavailable("WORKER_PREPARATION_INVALID");
  const release = releaseAdmissions.get(preparation.input.purposeRelease as object);
  if (!release || release.basis !== preparation.releaseBasis) throw unavailable("PURPOSE_ADMISSION_INVALID");
  await revalidateRuntimePurposeReleaseV2(preparation.releaseBasis, preparation.input.purposeRelease);
  if (!preparation.source.matchesAdmissionLease(preparation.lease)) throw unavailable("HOST_AUTHORITY_NOT_LIVE");
}

export async function completeRuntimeWorkerInstanceV2FromP2(
  preparation: RuntimeWorkerInstancePreparationV2,
  account: NonNullable<RuntimeInstanceAdmissionInputV2["account"]>
): Promise<{ instanceInput: RuntimeInstanceAdmissionInputV2; instanceAdmission: RuntimeInstanceAdmissionV2 }> {
  await revalidateRuntimeWorkerInstancePreparationV2(preparation);
  const subject = { purpose: "worker" as const, projectId: preparation.input.projectId, manifestHash: preparation.input.manifestHash,
    canonicalRoot: preparation.input.canonicalRoot, account, consentDigest: preparation.input.consent.digest };
  const hostAuthority = issueHostedAccountAuthorityV2FromP2(preparation.source, subject);
  const instanceInput: RuntimeInstanceAdmissionInputV2 = { ...preparation.input, hostAuthority, account };
  const instanceAdmission = await issueRuntimeInstanceAdmissionV2(instanceInput);
  await revalidateRuntimeWorkerInstancePreparationV2(preparation);
  await revalidateRuntimeInstanceAdmissionV2(instanceInput, instanceAdmission);
  return Object.freeze({ instanceInput, instanceAdmission });
}
function utc(value: unknown): value is string {
  if (typeof value !== "string" || value.length !== 24 || !/^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d\.\d{3}Z$/.test(value)) return false;
  const time = Date.parse(value);
  return Number.isFinite(time) && new Date(time).toISOString() === value;
}

async function stablePrivateFile(path: string): Promise<{ bytes: Buffer; sha256: string }> {
  if (!canonical(path) || await realpath(path) !== path) throw unavailable("PRIVATE_RELEASE_FILE_UNAVAILABLE");
  const parent = await lstat(resolve(path, ".."));
  if (!parent.isDirectory() || parent.uid !== (process.getuid?.() ?? -1) || (parent.mode & 0o077) !== 0) throw unavailable("PRIVATE_RELEASE_CUSTODY_INVALID");
  const handle = await open(path, constants.O_RDONLY | constants.O_NOFOLLOW | constants.O_NONBLOCK);
  try {
    const before = await handle.stat({ bigint: true });
    if (!before.isFile() || before.nlink !== 1n || before.uid !== BigInt(process.getuid?.() ?? -1) || (before.mode & 0o777n) !== 0o600n || before.size > 1_048_576n) throw unavailable("PRIVATE_RELEASE_CUSTODY_INVALID");
    const declared = Number(before.size), bytes = Buffer.alloc(declared + 1);
    let offset = 0;
    while (offset < bytes.length) {
      const { bytesRead } = await handle.read(bytes, offset, bytes.length - offset, offset);
      if (bytesRead === 0) break;
      offset += bytesRead;
    }
    const after = await handle.stat({ bigint: true }), current = await lstat(path, { bigint: true });
    for (const key of ["dev", "ino", "size", "mtimeNs", "ctimeNs", "mode", "uid", "nlink"] as const) if (before[key] !== after[key] || before[key] !== current[key]) throw unavailable("PRIVATE_RELEASE_FILE_CHANGED");
    if (offset !== declared || await realpath(path) !== path) throw unavailable("PRIVATE_RELEASE_FILE_CHANGED");
    const exact = bytes.subarray(0, declared);
    return { bytes: exact, sha256: hash(exact) };
  } finally { await handle.close(); }
}

function inspectLimbs(value: unknown, names: readonly string[]): void {
  if (!exactKeys(value, names)) throw unavailable("PURPOSE_RELEASE_LIMBS_INVALID");
  for (const name of names) {
    const limb = value[name];
    if (!exactKeys(limb, ["attempted", "passed", "evidenceSha256"]) || limb.attempted !== true || limb.passed !== true || !digest(limb.evidenceSha256)) throw unavailable("PURPOSE_RELEASE_LIMBS_INVALID");
  }
}

const TRIAL_PREREQUISITES = Object.freeze(["signed-payload-and-supply", "trusted-app-and-account-host", "native-enforcement-and-retirement", "connected-source-contract"] as const);
function inspectPendingTrialLimbs(value: unknown): void {
  if (!exactKeys(value, REQUIRED_RUNTIME_CONFORMANCE_LIMBS)) throw unavailable("PURPOSE_RELEASE_LIMBS_INVALID");
  for (const name of REQUIRED_RUNTIME_CONFORMANCE_LIMBS) if (!exactKeys(value[name], ["status"]) || value[name].status !== "pending-human-trial") throw unavailable("PURPOSE_RELEASE_LIMBS_INVALID");
}
function inspectTrialPrerequisites(value: unknown): void {
  if (!exactKeys(value, TRIAL_PREREQUISITES)) throw unavailable("PURPOSE_RELEASE_PREREQUISITES_INVALID");
  for (const name of TRIAL_PREREQUISITES) {
    const check = value[name];
    if (!exactKeys(check, ["attempted", "passed", "evidenceSha256"]) || check.attempted !== true || check.passed !== true || !digest(check.evidenceSha256)) throw unavailable("PURPOSE_RELEASE_PREREQUISITES_INVALID");
  }
}

export function inspectRuntimePurposeReleaseV2(input: { purpose: RuntimePurposeV2; record: unknown; expected: { payloadDigest: string; supportProfile: RuntimeSupportProfileV2 }; now?: number }): Readonly<{ sourceDigest: string; disposition: RuntimeWorkerReleaseDispositionV2 }> {
  const { purpose, record: value, expected } = input;
  matchRuntimeSupportProfileV2(expected.supportProfile, [expected.supportProfile]);
  const common = ["schema", "evidenceClass", "sourceDigest", "payloadDigest", "supportProfileDigests", "policyContractDigest", "supplyProfileDigest", "issuedAt", "expiresAt", "limbs"];
  const trial = purpose === "worker" && !!value && typeof value === "object" && !Array.isArray(value) && (value as Record<string, unknown>).schema === "chirality-codex-worker-purpose-release/v3";
  const keys = purpose === "login" ? [...common, "backend", "methods", "modelExecution"] : trial ? [...common, "trialScope", "prerequisites"] : common;
  if (!exactKeys(value, keys) || !digest(value.sourceDigest) || value.payloadDigest !== expected.payloadDigest || value.policyContractDigest !== expected.supportProfile.compiler.parameterSchemaDigest) throw unavailable("PURPOSE_RELEASE_INVALID");
  const record = value as Record<string, any>;
  if (!Array.isArray(record.supportProfileDigests) || record.supportProfileDigests.length < 1 || record.supportProfileDigests.length > 8 || !record.supportProfileDigests.every(digest) || !strictlySorted(record.supportProfileDigests) || !record.supportProfileDigests.includes(expected.supportProfile.profileDigest)) throw unavailable("PURPOSE_SUPPORT_INVALID");
  const supplyProfileDigest = hash(`${JSON.stringify(expected.supportProfile.supplier)}\n`);
  if (record.supplyProfileDigest !== supplyProfileDigest || !utc(record.issuedAt) || !utc(record.expiresAt)) throw unavailable("PURPOSE_RELEASE_INVALID");
  const now = input.now ?? Date.now(), issuedAt = Date.parse(record.issuedAt), expiresAt = Date.parse(record.expiresAt);
  if (!Number.isFinite(now) || issuedAt > now || expiresAt <= now || expiresAt <= issuedAt) throw unavailable("PURPOSE_RELEASE_STALE");
  if (purpose === "login") {
    if (record.schema !== "chirality-codex-login-purpose-release/v2" || record.evidenceClass !== "exact-account-free-login-purpose-observed"
      || !exactKeys(record.backend, ["credentialStore", "plaintextFallback"]) || record.backend.credentialStore !== "keyring" || record.backend.plaintextFallback !== false
      || record.modelExecution !== false || JSON.stringify(record.methods) !== JSON.stringify(["account/login/start", "account/login/cancel", "account/read", "model/list"])) throw unavailable("PURPOSE_RELEASE_INVALID");
    inspectLimbs(record.limbs, LOGIN_LIMBS);
  } else {
    if (trial) {
      if (record.evidenceClass !== "exact-local-human-trial-authorized" || record.trialScope !== "local-human-functional-trial") throw unavailable("PURPOSE_RELEASE_INVALID");
      inspectPendingTrialLimbs(record.limbs);
      inspectTrialPrerequisites(record.prerequisites);
    } else {
      if (record.schema !== "chirality-codex-worker-purpose-release/v2" || record.evidenceClass !== "exact-worker-purpose-observed") throw unavailable("PURPOSE_RELEASE_INVALID");
      inspectLimbs(record.limbs, REQUIRED_RUNTIME_CONFORMANCE_LIMBS);
    }
  }
  return Object.freeze({ sourceDigest: record.sourceDigest, disposition: trial ? "local-human-trial" : "qualified" });
}

export function inspectRuntimePurposeAcceptanceV2(input: { purpose: RuntimePurposeV2; acceptance: unknown; expected: { recordSha256: string; sourceDigest: string; ownerActSha256: string; activationId: string; gateIdentity: string }; now?: number }): Readonly<{ ownerReference: string }> {
  const { acceptance, expected } = input;
  if (!digest(expected.recordSha256) || !digest(expected.sourceDigest) || !digest(expected.ownerActSha256) || !text(expected.activationId) || !text(expected.gateIdentity)
    || (input.purpose === "login" && expected.gateIdentity !== "D36")
    || !exactKeys(acceptance, ["schema", "status", "recordSha256", "sourceDigest", "activationId", "gateIdentity", "ownerActSha256", "ownerReference", "expiresAt"])
    || acceptance.schema !== "chirality-runtime-conformance-acceptance/v1" || acceptance.status !== "accepted" || acceptance.recordSha256 !== expected.recordSha256
    || acceptance.sourceDigest !== expected.sourceDigest || acceptance.activationId !== expected.activationId || acceptance.gateIdentity !== expected.gateIdentity
    || acceptance.ownerActSha256 !== expected.ownerActSha256 || !text(acceptance.ownerReference) || !utc(acceptance.expiresAt)
    || Date.parse(acceptance.expiresAt) <= (input.now ?? Date.now())) throw unavailable("PURPOSE_RELEASE_NOT_ACCEPTED");
  return Object.freeze({ ownerReference: acceptance.ownerReference });
}

async function inspectAcceptedRelease(source: RuntimePurposeReleaseSourceV2): Promise<{ ownerReference: string; disposition: RuntimeWorkerReleaseDispositionV2 }> {
  if (!exactKeys(source, ["purpose", "recordPath", "recordSha256", "acceptancePath", "acceptanceSha256", "ownerActPath", "ownerActSha256", "activationId", "gateIdentity", "payloadDigest", "supportProfile"])
    || !["login", "worker"].includes(source.purpose) || !text(source.activationId) || !text(source.gateIdentity) || (source.purpose === "login" && source.gateIdentity !== "D36")
    || ![source.recordSha256, source.acceptanceSha256, source.ownerActSha256, source.payloadDigest, source.supportProfile?.profileDigest].every(digest)) throw unavailable("PURPOSE_SOURCE_INVALID");
  const [recordFile, acceptanceFile, ownerActFile] = await Promise.all([stablePrivateFile(source.recordPath), stablePrivateFile(source.acceptancePath), stablePrivateFile(source.ownerActPath)]);
  if (recordFile.sha256 !== source.recordSha256 || acceptanceFile.sha256 !== source.acceptanceSha256 || ownerActFile.sha256 !== source.ownerActSha256) throw unavailable("PURPOSE_SOURCE_CHANGED");
  let record: unknown, acceptance: unknown;
  try { record = JSON.parse(recordFile.bytes.toString("utf8")); acceptance = JSON.parse(acceptanceFile.bytes.toString("utf8")); } catch { throw unavailable("PURPOSE_RELEASE_INVALID"); }
  const inspected = inspectRuntimePurposeReleaseV2({ purpose: source.purpose, record, expected: { payloadDigest: source.payloadDigest, supportProfile: source.supportProfile } });
  if (!acceptance || typeof acceptance !== "object" || Array.isArray(acceptance)) throw unavailable("PURPOSE_RELEASE_NOT_ACCEPTED");
  const accepted = inspectRuntimePurposeAcceptanceV2({ purpose: source.purpose, acceptance, expected: { recordSha256: recordFile.sha256, sourceDigest: inspected.sourceDigest,
    ownerActSha256: ownerActFile.sha256, activationId: source.activationId, gateIdentity: source.gateIdentity } });
  return Object.freeze({ ...accepted, disposition: inspected.disposition });
}

function purposeSourceFromBasis(basis: Readonly<HostedPackagedReleaseBasisV2>, purpose: RuntimePurposeV2): Readonly<RuntimePurposeReleaseSourceV2> {
  const selected = basis[purpose];
  return Object.freeze({ purpose, ...selected, payloadDigest: basis.verified.payloadDigest, supportProfile: basis.supportProfile });
}

export async function verifyRuntimePurposeReleaseV2(basis: Readonly<HostedPackagedReleaseBasisV2>, purpose: RuntimePurposeV2): Promise<RuntimePurposeReleaseAdmissionV2> {
  await revalidateIssuedPackagedReleaseBasisV2(basis);
  const frozenSource = purposeSourceFromBasis(basis, purpose);
  const accepted = await inspectAcceptedRelease(frozenSource);
  await revalidateIssuedPackagedReleaseBasisV2(basis);
  const admission = Object.freeze({ purpose: frozenSource.purpose, recordSha256: frozenSource.recordSha256, ownerReference: accepted.ownerReference, profileDigest: frozenSource.supportProfile.profileDigest, evidence: "externally-accepted-release-purpose-v2" as const, disposition: accepted.disposition });
  releaseAdmissions.set(admission, { basis, source: frozenSource, ownerReference: accepted.ownerReference, disposition: accepted.disposition });
  return admission;
}

export async function revalidateRuntimePurposeReleaseV2(basis: Readonly<HostedPackagedReleaseBasisV2>, admission: RuntimePurposeReleaseAdmissionV2): Promise<void> {
  const state = releaseAdmissions.get(admission as object);
  if (!state || state.basis !== basis || admission.evidence !== "externally-accepted-release-purpose-v2") throw unavailable("PURPOSE_ADMISSION_INVALID");
  await revalidateIssuedPackagedReleaseBasisV2(basis);
  const current = await inspectAcceptedRelease(state.source);
  await revalidateIssuedPackagedReleaseBasisV2(basis);
  if (current.ownerReference !== state.ownerReference || current.disposition !== state.disposition || admission.disposition !== state.disposition) throw unavailable("PURPOSE_ACCEPTANCE_CHANGED");
}

export function inspectCodexPolicyInstanceV2(value: unknown): Readonly<CodexPolicyInstanceV2> {
  const names = ["schema", "outerPurpose", "nativePurpose", "canonicalRoot", "privateDirectory", "codexHome", "executablePath", "nativeAddonPath", "providerNetworkConsent", "commandNetworkPosture", "immutableReadRoots", "protectedPaths", "readOnlyProjectPaths", "trustedRuntimeReadRoots", "toolRuntime", "nativeRoleConfiguration"];
  if (!exactKeys(value, names) || value.schema !== "chirality-codex-policy-instance/v2" || !["trusted-login", "trusted-supplier"].includes(String(value.outerPurpose)) || ![null, "worker"].includes(value.nativePurpose as null | string)) throw unavailable("POLICY_INSTANCE_INVALID");
  const policy = value as unknown as CodexPolicyInstanceV2;
  for (const path of [policy.canonicalRoot, policy.privateDirectory, policy.codexHome, policy.executablePath, policy.nativeAddonPath]) if (!canonical(path)) throw unavailable("POLICY_PATH_INVALID");
  if (policy.canonicalRoot === "/" || !properChild(policy.privateDirectory, policy.codexHome) || !properChild(policy.privateDirectory, policy.executablePath)
    || properChild(policy.canonicalRoot, policy.privateDirectory) || properChild(policy.privateDirectory, policy.canonicalRoot)) throw unavailable("POLICY_PATH_INVALID");
  if (!exactKeys(policy.providerNetworkConsent, ["approvedBy", "approvalReference"]) || !text(policy.providerNetworkConsent.approvedBy) || !text(policy.providerNetworkConsent.approvalReference)
    || !["off", "ask-per-destination", "on"].includes(policy.commandNetworkPosture)) throw unavailable("POLICY_CONSENT_INVALID");
  for (const [values, minimum, maximum] of [[policy.immutableReadRoots, policy.nativePurpose === "worker" ? 1 : 0, 64], [policy.protectedPaths, policy.nativePurpose === "worker" ? 1 : 0, 256], [policy.readOnlyProjectPaths, 0, 32]] as const) {
    if (!Array.isArray(values) || values.length < minimum || values.length > maximum || !values.every(canonical) || !strictlySorted(values)) throw unavailable("POLICY_COLLECTION_INVALID");
  }
  if (!exactKeys(policy.toolRuntime, ["codexSelfExecutablePath", "requiresSandboxedFileSystem", "requiresSandboxedFileStreaming"]) || policy.toolRuntime.codexSelfExecutablePath !== policy.executablePath
    || policy.toolRuntime.requiresSandboxedFileSystem !== true || policy.toolRuntime.requiresSandboxedFileStreaming !== true) throw unavailable("POLICY_TOOL_RUNTIME_INVALID");
  if (policy.outerPurpose === "trusted-login") {
    if (policy.nativePurpose !== null || policy.commandNetworkPosture !== "off" || policy.immutableReadRoots.length || policy.protectedPaths.length || policy.readOnlyProjectPaths.length || policy.trustedRuntimeReadRoots.length || policy.nativeRoleConfiguration !== null) throw unavailable("LOGIN_POLICY_INVALID");
  } else {
    if (policy.nativePurpose !== "worker" || policy.trustedRuntimeReadRoots.length !== 1 || policy.nativeRoleConfiguration === null) throw unavailable("WORKER_POLICY_INVALID");
    const attachment = resolve(policy.canonicalRoot, ".chirality", "attachments");
    if (!policy.readOnlyProjectPaths.includes(attachment)) throw unavailable("WORKER_POLICY_INVALID");
  }
  for (const entry of policy.trustedRuntimeReadRoots) {
    if (!exactKeys(entry, ["path", "readPaths", "contentDigest", "artifactInventory"]) || !canonical(entry.path) || !digest(entry.contentDigest) || !Array.isArray(entry.readPaths) || entry.readPaths.length < 1 || entry.readPaths.length > 32 || !entry.readPaths.every(canonical) || !strictlySorted(entry.readPaths)) throw unavailable("TRUSTED_RUNTIME_READ_INVALID");
    const inventory = entry.artifactInventory;
    if (!exactKeys(inventory, ["schema", "resourcesRoot", "inventoryPath", "payloadManifestPath", "outerInventorySha256", "payloadDigest"]) || inventory.schema !== "chirality-runtime-packaged-basis/v2"
      || ![inventory.resourcesRoot, inventory.inventoryPath, inventory.payloadManifestPath].every(canonical) || ![inventory.outerInventorySha256, inventory.payloadDigest].every(digest)) throw unavailable("TRUSTED_RUNTIME_READ_INVALID");
  }
  const roles = policy.nativeRoleConfiguration;
  if (roles !== null) {
    const prefix = ["agents.enabled=true", "features.multi_agent=true", "features.multi_agent_v2=false", "agents.max_depth=2"];
    const roleNames = ["HELP_HUMAN", "HELPS_HUMANS", "WORKING_ITEMS", "TASK"];
    if (!exactKeys(roles, ["digest", "configOverrides"]) || !digest(roles.digest) || !Array.isArray(roles.configOverrides) || roles.configOverrides.length !== 12
      || prefix.some((value, index) => roles.configOverrides[index] !== value)) throw unavailable("NATIVE_ROLES_INVALID");
    for (let index = 0; index < roleNames.length; index++) {
      if (!roles.configOverrides[4 + index * 2]?.startsWith(`agents.${roleNames[index]}.description=`)
        || !roles.configOverrides[5 + index * 2]?.startsWith(`agents.${roleNames[index]}.config_file=`)) throw unavailable("NATIVE_ROLES_INVALID");
    }
  }
  return Object.freeze(structuredClone(policy));
}

export function digestCodexPolicyInstanceV2(value: CodexPolicyInstanceV2): RuntimeSha256AdmissionV2 {
  return hash(`${JSON.stringify(inspectCodexPolicyInstanceV2(value))}\n`);
}

function inspectWorkerPreparationInput(input: RuntimeWorkerInstancePreparationInputV2): string {
  if (!exactKeys(input, ["purposeRelease", "projectId", "manifestHash", "canonicalRoot", "cwd", "privateDirectory", "codexHome", "brokerRoot", "instructionRoot", "nativeAddonPath", "supplierExecutablePath", "attachmentRoot", "consent", "policy", "outerPolicyDigest", "nativePolicyDigest", "effectiveConfigDigest"])) throw unavailable("WORKER_PREPARATION_INPUT_INVALID");
  if (!releaseAdmissions.has(input.purposeRelease as object) || input.purposeRelease.purpose !== "worker" || !text(input.projectId, 128) || !digest(input.manifestHash)
    || ![input.canonicalRoot, input.cwd, input.privateDirectory, input.codexHome, input.brokerRoot, input.instructionRoot, input.nativeAddonPath, input.supplierExecutablePath, input.attachmentRoot].every(canonical)
    || input.cwd !== input.canonicalRoot || !properChild(input.brokerRoot, input.privateDirectory) || input.policy.canonicalRoot !== input.canonicalRoot || input.policy.privateDirectory !== input.privateDirectory
    || input.policy.codexHome !== input.codexHome || input.policy.nativeAddonPath !== input.nativeAddonPath || input.policy.executablePath !== input.supplierExecutablePath
    || !exactKeys(input.consent, ["version", "digest", "authenticatedExplicitUserAct"]) || !digest(input.consent.version) || !digest(input.consent.digest) || input.consent.authenticatedExplicitUserAct !== true
    || !digest(input.outerPolicyDigest) || !digest(input.nativePolicyDigest) || !digest(input.effectiveConfigDigest)) throw unavailable("WORKER_PREPARATION_INPUT_INVALID");
  const policy = inspectCodexPolicyInstanceV2(input.policy);
  if (policy.outerPurpose !== "trusted-supplier" || policy.nativePurpose !== "worker") throw unavailable("WORKER_PREPARATION_INPUT_INVALID");
  return hash(JSON.stringify(input));
}

function inspectInstanceInput(input: RuntimeInstanceAdmissionInputV2): string {
  if (!exactKeys(input, ["purposeRelease", "hostAuthority", "projectId", "manifestHash", "canonicalRoot", "cwd", "privateDirectory", "codexHome", "brokerRoot", "instructionRoot", "nativeAddonPath", "supplierExecutablePath", "attachmentRoot", "account", "consent", "policy", "outerPolicyDigest", "nativePolicyDigest", "effectiveConfigDigest"])) throw unavailable("INSTANCE_INPUT_INVALID");
  const purpose = input.purposeRelease?.purpose;
  if (!releaseAdmissions.has(input.purposeRelease as object) || !hostAuthorities.has(input.hostAuthority as object) || !text(input.projectId, 128) || !digest(input.manifestHash)
    || ![input.canonicalRoot, input.cwd, input.privateDirectory, input.codexHome, input.brokerRoot, input.instructionRoot, input.nativeAddonPath, input.supplierExecutablePath, input.attachmentRoot].every(canonical)
    || input.cwd !== input.canonicalRoot || !properChild(input.brokerRoot, input.privateDirectory) || input.policy.canonicalRoot !== input.canonicalRoot || input.policy.privateDirectory !== input.privateDirectory
    || input.policy.codexHome !== input.codexHome || input.policy.nativeAddonPath !== input.nativeAddonPath || input.policy.executablePath !== input.supplierExecutablePath
    || !exactKeys(input.consent, ["version", "digest", "authenticatedExplicitUserAct"]) || !digest(input.consent.version) || !digest(input.consent.digest) || input.consent.authenticatedExplicitUserAct !== true
    || !digest(input.outerPolicyDigest) || !digest(input.effectiveConfigDigest)) throw unavailable("INSTANCE_INPUT_INVALID");
  inspectCodexPolicyInstanceV2(input.policy);
  if (input.hostAuthority.subjectBindingDigest !== hostAuthoritySubjectBindingDigestV2({ purpose, projectId: input.projectId, manifestHash: input.manifestHash, canonicalRoot: input.canonicalRoot, account: input.account, consentDigest: input.consent.digest })) throw unavailable("HOST_AUTHORITY_SUBJECT_MISMATCH");
  if (purpose === "login") {
    if (input.account !== null || input.nativePolicyDigest !== null || input.policy.outerPurpose !== "trusted-login") throw unavailable("LOGIN_INSTANCE_INVALID");
  } else if (purpose === "worker") {
    if (!input.account || !exactKeys(input.account, ["accountId", "accountEpoch", "accountDigest"]) || !text(input.account.accountId) || !Number.isSafeInteger(input.account.accountEpoch) || input.account.accountEpoch < 0 || !digest(input.account.accountDigest)
      || !digest(input.nativePolicyDigest) || input.policy.outerPurpose !== "trusted-supplier") throw unavailable("WORKER_INSTANCE_INVALID");
  } else throw unavailable("INSTANCE_INPUT_INVALID");
  return hash(JSON.stringify(input));
}

export async function issueRuntimeInstanceAdmissionV2(input: RuntimeInstanceAdmissionInputV2): Promise<RuntimeInstanceAdmissionV2> {
  const identity = inspectInstanceInput(input);
  await revalidateHostedAccountAuthorityV2(input.hostAuthority, { purpose: input.purposeRelease.purpose, projectId: input.projectId, manifestHash: input.manifestHash, canonicalRoot: input.canonicalRoot, account: input.account, consentDigest: input.consent.digest });
  const release = releaseAdmissions.get(input.purposeRelease as object)!;
  await revalidateRuntimePurposeReleaseV2(release.basis, input.purposeRelease);
  await revalidateHostedAccountAuthorityV2(input.hostAuthority, { purpose: input.purposeRelease.purpose, projectId: input.projectId, manifestHash: input.manifestHash, canonicalRoot: input.canonicalRoot, account: input.account, consentDigest: input.consent.digest });
  if (inspectInstanceInput(input) !== identity) throw unavailable("INSTANCE_ADMISSION_INVALID");
  const admission = Object.freeze({ purpose: input.purposeRelease.purpose, evidence: "release-and-live-instance-v2" as const });
  instanceAdmissions.set(admission, { digest: identity, input: structuredClone(input) });
  return admission;
}

export async function revalidateRuntimeInstanceAdmissionV2(input: RuntimeInstanceAdmissionInputV2, admission: RuntimeInstanceAdmissionV2): Promise<void> {
  const state = instanceAdmissions.get(admission as object);
  if (!state || admission.evidence !== "release-and-live-instance-v2" || admission.purpose !== input.purposeRelease.purpose || inspectInstanceInput(input) !== state.digest) throw unavailable("INSTANCE_ADMISSION_INVALID");
  await revalidateHostedAccountAuthorityV2(input.hostAuthority, { purpose: input.purposeRelease.purpose, projectId: input.projectId, manifestHash: input.manifestHash, canonicalRoot: input.canonicalRoot, account: input.account, consentDigest: input.consent.digest });
  const release = releaseAdmissions.get(input.purposeRelease as object)!;
  await revalidateRuntimePurposeReleaseV2(release.basis, input.purposeRelease);
  await revalidateHostedAccountAuthorityV2(input.hostAuthority, { purpose: input.purposeRelease.purpose, projectId: input.projectId, manifestHash: input.manifestHash, canonicalRoot: input.canonicalRoot, account: input.account, consentDigest: input.consent.digest });
  if (inspectInstanceInput(input) !== state.digest) throw unavailable("INSTANCE_ADMISSION_INVALID");
}
