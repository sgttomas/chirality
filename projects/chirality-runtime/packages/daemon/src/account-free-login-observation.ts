import { createHash, randomBytes, randomUUID } from "node:crypto";
import { execFile } from "node:child_process";
import { constants } from "node:fs";
import { chmod, copyFile, mkdir, open, readdir, realpath, rm, stat } from "node:fs/promises";
import { dirname, isAbsolute, join, relative, resolve, sep } from "node:path";
import { PassThrough } from "node:stream";
import { promisify } from "node:util";
import {
  createCustomSupplyVerifier,
  RUNTIME_STAGE_C_NATIVE_SKILL_ARGUMENT,
  runtimeStageCAppServerArguments,
  type CustomSupplyExactProfileV1,
  type ExactSupplyClosureEntry
} from "@chirality/runtime-core";
import { RuntimeError } from "@chirality/runtime-contracts";
import { loadNativeAdmissionBinding, type NativeGroupedSupplierChild } from "@chirality/native-admission";
import {
  assertCodexKeyringHomeHasNoPlaintextCredentials,
  codexLoginConfigOverridesV2,
  prepareCodexContainmentV2,
  type TrustedRuntimeReadRootBindingV2
} from "./codex-containment.js";
import { retireAuthenticatedSupplierGroup } from "./codex-authenticated-transport.js";
import { CodexTurnSession, type CodexAuthorityInitialize } from "./codex-session.js";
import { AUTHORITY_CONTRACT } from "./supplier-authority-controller.js";

const LIMBS = ["exact-supplier", "keyring-backend", "plaintext-fallback-absent", "process-containment", "storage-isolation", "provider-network", "bounded-protocol-purpose", "retirement"] as const;
const DIAGNOSTIC_REQUEST_TIMEOUT_MS = 120_000;
type Limb = typeof LIMBS[number];
type Sha256 = string;

export interface AccountFreeLoginObservationRecipeV1 {
  schema: "chirality-account-free-login-observation-recipe/v1";
  runId: string;
  supplyProfile: Readonly<CustomSupplyExactProfileV1>;
  supplyClosure: readonly Readonly<ExactSupplyClosureEntry>[];
  nativeAddon: Readonly<{ sha256: Sha256; size: number; signatureEvidenceSha256: Sha256; sourceCorrespondenceEvidenceSha256: Sha256; xpcRecordSha256: Sha256; groupedRecordSha256: Sha256 }>;
  providerNetworkConsent: Readonly<{ approvedBy: string; approvalReference: string }>;
  supportProfileDigest: Sha256;
  nativePolicyIdentityVersion: 11;
}
export interface AccountFreeLoginObservationInputV2 {
  runtimeDirectory: string;
  resourcesPath: string;
  evidencePaths: Readonly<{ signatureEvidenceSha256: string; sourceCorrespondenceEvidenceSha256: string; xpcRecordSha256: string; groupedRecordSha256: string }>;
  recipe: Readonly<AccountFreeLoginObservationRecipeV1>;
}

export interface AccountFreeLoginObservationResultV1 {
  schema: "chirality-account-free-login-observation-result/v1";
  observationSha256: Sha256;
  outputDirectory: string;
  limbs: Readonly<Record<Limb, Readonly<{ attempted: true; passed: true; evidenceSha256: Sha256 }>>>;
}
export type AccountFreeLoginObservationPhaseV1 = "supply-verification" | "prelaunch-verification" | "containment" | "native-load" | "supplier-spawn" | "initialize" | "config-read" | "protocol-validation" | "retirement" | "final-verification" | "publication";
export interface AccountFreeLoginObservationFailureV1 {
  schema: "chirality-account-free-login-observation-failure/v1";
  status: "failed";
  phase: AccountFreeLoginObservationPhaseV1;
  issuedMethods: readonly ("initialize" | "initialized" | "config/read")[];
  elapsedMs: number;
  retirement: Readonly<{ status: "verified"; groupRetired: true; leader: Readonly<{ exitCode: number | null; signal: number | null }>; signalFailurePhases: readonly string[] } | { status: "unavailable" }>;
}
export interface AccountFreeLoginStartupDiagnosticV1 {
  schema: "chirality-account-free-login-startup-diagnostic/v1";
  status: "diagnostic-only";
  outcome: "initialize-resolved" | "initialize-failed";
  qualification: false;
  phase: AccountFreeLoginObservationPhaseV1;
  issuedMethods: readonly ("initialize" | "initialized")[];
  elapsedMs: number;
  initialize: Readonly<{ issuedAtMs: number | null; settledAtMs: number | null }>;
  leaderObservation: Readonly<{ status: "resolved"; elapsedMs: number; leader: Readonly<{ exitCode: number | null; signal: number | null }> } | { status: "unavailable"; elapsedMs: number | null }>;
  cleanupStartedAtMs: number | null;
  retirementSettledAtMs: number | null;
  retirement: AccountFreeLoginObservationFailureV1["retirement"];
  launchDeviation: Readonly<{ executable: "/bin/sh"; stderrCapture: "private-fifo"; sandboxExecutable: "/usr/bin/sandbox-exec"; compiledArgumentsUnchanged: true; requestTimeoutMs: 120000 }>;
  stderr: Readonly<{ status: "captured"; artifactPath: string; sha256: Sha256; retainedBytes: number; totalBytes: number; truncated: boolean } | { status: "unavailable" }>;
}

export function accountFreeLoginObservationFailure(error: unknown): Readonly<AccountFreeLoginObservationFailureV1> | undefined {
  const value = error && typeof error === "object" ? (error as { accountFreeObservationFailure?: unknown }).accountFreeObservationFailure : undefined;
  const phases: readonly AccountFreeLoginObservationPhaseV1[] = ["supply-verification", "prelaunch-verification", "containment", "native-load", "supplier-spawn", "initialize", "config-read", "protocol-validation", "retirement", "final-verification", "publication"];
  if (!exactKeys(value, ["schema", "status", "phase", "issuedMethods", "elapsedMs", "retirement"]) || value.schema !== "chirality-account-free-login-observation-failure/v1" || value.status !== "failed"
    || !phases.includes(value.phase as AccountFreeLoginObservationPhaseV1) || !Array.isArray(value.issuedMethods) || value.issuedMethods.length > 16
    || !value.issuedMethods.every(method => typeof method === "string" && ["initialize", "initialized", "config/read"].includes(method)) || !Number.isSafeInteger(value.elapsedMs) || Number(value.elapsedMs) < 0 || Number(value.elapsedMs) > 86_400_000
    || !record(value.retirement)) return undefined;
  const retirement = value.retirement;
  if (retirement.status === "unavailable") {
    if (!exactKeys(retirement, ["status"])) return undefined;
    return Object.freeze({ schema: value.schema, status: value.status, phase: value.phase as AccountFreeLoginObservationPhaseV1,
      issuedMethods: Object.freeze([...value.issuedMethods]) as AccountFreeLoginObservationFailureV1["issuedMethods"], elapsedMs: Number(value.elapsedMs), retirement: Object.freeze({ status: "unavailable" }) });
  }
  if (!exactKeys(retirement, ["status", "groupRetired", "leader", "signalFailurePhases"]) || retirement.status !== "verified" || retirement.groupRetired !== true
    || !exactKeys(retirement.leader, ["exitCode", "signal"])
    || (retirement.leader.exitCode !== null && (!Number.isSafeInteger(retirement.leader.exitCode) || Number(retirement.leader.exitCode) < 0 || Number(retirement.leader.exitCode) > 255))
    || (retirement.leader.signal !== null && (!Number.isSafeInteger(retirement.leader.signal) || Number(retirement.leader.signal) < 1 || Number(retirement.leader.signal) > 127))
    || (retirement.leader.exitCode === null) === (retirement.leader.signal === null)
    || !Array.isArray(retirement.signalFailurePhases) || retirement.signalFailurePhases.length > 2 || !retirement.signalFailurePhases.every(item => item === "term" || item === "kill")) return undefined;
  return Object.freeze({ schema: value.schema, status: value.status, phase: value.phase as AccountFreeLoginObservationPhaseV1,
    issuedMethods: Object.freeze([...value.issuedMethods]) as AccountFreeLoginObservationFailureV1["issuedMethods"], elapsedMs: Number(value.elapsedMs), retirement: Object.freeze({ status: "verified", groupRetired: true,
      leader: Object.freeze({ exitCode: retirement.leader.exitCode as number | null, signal: retirement.leader.signal as number | null }), signalFailurePhases: Object.freeze([...retirement.signalFailurePhases]) }) });
}

const boundedMs = (value: unknown): value is number => Number.isSafeInteger(value) && Number(value) >= 0 && Number(value) <= 86_400_000;
const validLeader = (value: unknown): value is Readonly<{ exitCode: number | null; signal: number | null }> => exactKeys(value, ["exitCode", "signal"])
  && (value.exitCode === null || (Number.isSafeInteger(value.exitCode) && Number(value.exitCode) >= 0 && Number(value.exitCode) <= 255))
  && (value.signal === null || (Number.isSafeInteger(value.signal) && Number(value.signal) >= 1 && Number(value.signal) <= 127))
  && (value.exitCode === null) !== (value.signal === null);
const safePath = (value: unknown): value is string => typeof value === "string" && value.length <= 4096 && isAbsolute(value) && resolve(value) === value && !/[\x00-\x1f\x7f]/u.test(value);

/** Reconstructs only bounded diagnostic metadata; raw Supplier stderr is never returned. */
export function accountFreeLoginStartupDiagnostic(error: unknown): Readonly<AccountFreeLoginStartupDiagnosticV1> | undefined {
  const value = error && typeof error === "object" ? (error as { accountFreeStartupDiagnostic?: unknown }).accountFreeStartupDiagnostic : undefined;
  const phases: readonly AccountFreeLoginObservationPhaseV1[] = ["supply-verification", "prelaunch-verification", "containment", "native-load", "supplier-spawn", "initialize", "retirement", "final-verification"];
  if (!exactKeys(value, ["schema", "status", "outcome", "qualification", "phase", "issuedMethods", "elapsedMs", "initialize", "leaderObservation", "cleanupStartedAtMs", "retirementSettledAtMs", "retirement", "launchDeviation", "stderr"])
    || value.schema !== "chirality-account-free-login-startup-diagnostic/v1" || value.status !== "diagnostic-only" || (value.outcome !== "initialize-resolved" && value.outcome !== "initialize-failed") || value.qualification !== false
    || !phases.includes(value.phase as AccountFreeLoginObservationPhaseV1) || !Array.isArray(value.issuedMethods) || value.issuedMethods.length > 2
    || !value.issuedMethods.every(method => typeof method === "string" && (method === "initialize" || method === "initialized")) || !boundedMs(value.elapsedMs)
    || !exactKeys(value.initialize, ["issuedAtMs", "settledAtMs"]) || (value.initialize.issuedAtMs !== null && !boundedMs(value.initialize.issuedAtMs)) || (value.initialize.settledAtMs !== null && !boundedMs(value.initialize.settledAtMs))
    || (value.cleanupStartedAtMs !== null && !boundedMs(value.cleanupStartedAtMs)) || (value.retirementSettledAtMs !== null && !boundedMs(value.retirementSettledAtMs)) || !record(value.leaderObservation) || !record(value.retirement)
    || !exactKeys(value.launchDeviation, ["executable", "stderrCapture", "sandboxExecutable", "compiledArgumentsUnchanged", "requestTimeoutMs"]) || value.launchDeviation.executable !== "/bin/sh" || value.launchDeviation.stderrCapture !== "private-fifo"
    || value.launchDeviation.sandboxExecutable !== "/usr/bin/sandbox-exec" || value.launchDeviation.compiledArgumentsUnchanged !== true || value.launchDeviation.requestTimeoutMs !== DIAGNOSTIC_REQUEST_TIMEOUT_MS || !record(value.stderr)) return undefined;
  const leaderObservation = value.leaderObservation.status === "resolved" && exactKeys(value.leaderObservation, ["status", "elapsedMs", "leader"]) && boundedMs(value.leaderObservation.elapsedMs) && validLeader(value.leaderObservation.leader)
    ? Object.freeze({ status: "resolved" as const, elapsedMs: value.leaderObservation.elapsedMs, leader: Object.freeze({ ...value.leaderObservation.leader }) })
    : value.leaderObservation.status === "unavailable" && exactKeys(value.leaderObservation, ["status", "elapsedMs"]) && (value.leaderObservation.elapsedMs === null || boundedMs(value.leaderObservation.elapsedMs))
      ? Object.freeze({ status: "unavailable" as const, elapsedMs: value.leaderObservation.elapsedMs as number | null }) : undefined;
  const retirement = value.retirement.status === "unavailable" && exactKeys(value.retirement, ["status"])
    ? Object.freeze({ status: "unavailable" as const })
    : value.retirement.status === "verified" && exactKeys(value.retirement, ["status", "groupRetired", "leader", "signalFailurePhases"]) && value.retirement.groupRetired === true && validLeader(value.retirement.leader)
      && Array.isArray(value.retirement.signalFailurePhases) && value.retirement.signalFailurePhases.length <= 2 && value.retirement.signalFailurePhases.every(item => item === "term" || item === "kill")
      ? Object.freeze({ status: "verified" as const, groupRetired: true as const, leader: Object.freeze({ ...value.retirement.leader }), signalFailurePhases: Object.freeze([...value.retirement.signalFailurePhases]) }) : undefined;
  const stderr = value.stderr.status === "unavailable" && exactKeys(value.stderr, ["status"])
    ? Object.freeze({ status: "unavailable" as const })
    : value.stderr.status === "captured" && exactKeys(value.stderr, ["status", "artifactPath", "sha256", "retainedBytes", "totalBytes", "truncated"]) && safePath(value.stderr.artifactPath) && hex(value.stderr.sha256)
      && Number.isSafeInteger(value.stderr.retainedBytes) && Number(value.stderr.retainedBytes) >= 0 && Number(value.stderr.retainedBytes) <= 65_536
      && Number.isSafeInteger(value.stderr.totalBytes) && Number(value.stderr.totalBytes) >= Number(value.stderr.retainedBytes) && value.stderr.truncated === (Number(value.stderr.totalBytes) > Number(value.stderr.retainedBytes))
      ? Object.freeze({ status: "captured" as const, artifactPath: value.stderr.artifactPath, sha256: value.stderr.sha256, retainedBytes: Number(value.stderr.retainedBytes), totalBytes: Number(value.stderr.totalBytes), truncated: value.stderr.truncated }) : undefined;
  if (!leaderObservation || !retirement || !stderr) return undefined;
  return Object.freeze({ schema: value.schema, status: value.status, outcome: value.outcome as AccountFreeLoginStartupDiagnosticV1["outcome"], qualification: false, phase: value.phase as AccountFreeLoginObservationPhaseV1,
    issuedMethods: Object.freeze([...value.issuedMethods]) as AccountFreeLoginStartupDiagnosticV1["issuedMethods"], elapsedMs: value.elapsedMs as number,
    initialize: Object.freeze({ issuedAtMs: value.initialize.issuedAtMs as number | null, settledAtMs: value.initialize.settledAtMs as number | null }), leaderObservation,
    cleanupStartedAtMs: value.cleanupStartedAtMs as number | null, retirementSettledAtMs: value.retirementSettledAtMs as number | null, retirement, launchDeviation: Object.freeze({ executable: "/bin/sh", stderrCapture: "private-fifo", sandboxExecutable: "/usr/bin/sandbox-exec", compiledArgumentsUnchanged: true, requestTimeoutMs: DIAGNOSTIC_REQUEST_TIMEOUT_MS }), stderr });
}

const unavailable = (reason: string, cause?: unknown) => {
  const error = new RuntimeError("ENGINE_UNAVAILABLE", "Account-free Supplier observation is unavailable", 503, { reason });
  if (cause !== undefined) error.cause = cause;
  return error;
};
const hex = (value: unknown): value is string => typeof value === "string" && /^[a-f0-9]{64}$/.test(value);
const bytes = (value: unknown): Buffer => Buffer.from(`${JSON.stringify(value)}\n`);
const digest = (value: Buffer | string): string => createHash("sha256").update(value).digest("hex");
const record = (value: unknown): value is Record<string, unknown> => !!value && typeof value === "object" && !Array.isArray(value);
const exactKeys = (value: unknown, keys: readonly string[]): value is Record<string, unknown> => record(value)
  && Object.keys(value).length === keys.length && keys.every(key => Object.hasOwn(value, key));

interface StableFile { path: string; sha256: string; size: number; identity: Readonly<{ dev: string; ino: string; mode: string; uid: string; nlink: string; size: string; mtimeNs: string; ctimeNs: string }> }
async function stableFile(path: string, expected: { sha256: string; size: number }): Promise<StableFile> {
  if (!isAbsolute(path) || resolve(path) !== path || !hex(expected.sha256) || !Number.isSafeInteger(expected.size) || expected.size < 1 || await realpath(path) !== path) throw unavailable("OBSERVATION_FILE_INVALID");
  const handle = await open(path, constants.O_RDONLY | constants.O_NOFOLLOW);
  try {
    const before = await handle.stat({ bigint: true });
    if (!before.isFile() || before.isSymbolicLink() || before.nlink !== 1n || before.size !== BigInt(expected.size)) throw unavailable("OBSERVATION_FILE_INVALID");
    const hash = createHash("sha256"), buffer = Buffer.alloc(65_536); let total = 0;
    for (;;) { const read = await handle.read(buffer, 0, Math.min(buffer.length, expected.size + 1 - total), total); if (!read.bytesRead) break; total += read.bytesRead; if (total > expected.size) throw unavailable("OBSERVATION_FILE_CHANGED"); hash.update(buffer.subarray(0, read.bytesRead)); }
    const after = await handle.stat({ bigint: true }), current = await stat(path, { bigint: true });
    const identity = (value: typeof before) => ({ dev: `${value.dev}`, ino: `${value.ino}`, mode: `${value.mode}`, uid: `${value.uid}`, nlink: `${value.nlink}`, size: `${value.size}`, mtimeNs: `${value.mtimeNs}`, ctimeNs: `${value.ctimeNs}` });
    const first = identity(before), final = identity(after), present = identity(current);
    if (total !== expected.size || hash.digest("hex") !== expected.sha256 || JSON.stringify(first) !== JSON.stringify(final) || JSON.stringify(final) !== JSON.stringify(present) || await realpath(path) !== path) throw unavailable("OBSERVATION_FILE_CHANGED");
    return Object.freeze({ path, sha256: expected.sha256, size: expected.size, identity: Object.freeze(final) });
  } finally { await handle.close(); }
}
async function stableEvidence(path: string, expectedSha256: string): Promise<StableFile> {
  if (!isAbsolute(path) || resolve(path) !== path || await realpath(path) !== path) throw unavailable("OBSERVATION_EVIDENCE_INVALID");
  const info = await stat(path, { bigint: true });
  if (!info.isFile() || info.isSymbolicLink() || info.nlink !== 1n || info.uid !== BigInt(process.getuid?.() ?? -1) || (info.mode & 0o022n) !== 0n || info.size < 1n || info.size > 16_777_216n) throw unavailable("OBSERVATION_EVIDENCE_INVALID");
  return stableFile(path, { sha256: expectedSha256, size: Number(info.size) });
}

async function directoryObservation(path: string): Promise<Readonly<{ sha256: string; entries: readonly Readonly<{ name: string; type: "file" | "directory" | "other" }>[] }>> {
  if (await realpath(path) !== path) throw unavailable("OBSERVATION_STORAGE_INVALID");
  const info = await stat(path);
  if (!info.isDirectory() || info.uid !== (process.getuid?.() ?? -1) || (info.mode & 0o077) !== 0) throw unavailable("OBSERVATION_STORAGE_INVALID");
  const entries = await readdir(path, { withFileTypes: true });
  const facts: Array<{ name: string; type: "file" | "directory" | "other" }> = entries.map(entry => ({ name: entry.name, type: entry.isFile() ? "file" as const : entry.isDirectory() ? "directory" as const : "other" as const }))
    .sort((a, b) => Buffer.compare(Buffer.from(a.name), Buffer.from(b.name)));
  return Object.freeze({ sha256: digest(bytes(facts)), entries: Object.freeze(facts.map(value => Object.freeze(value))) });
}

async function publish(outputDirectory: string, privateDirectory: string, observation: unknown, projections: Readonly<Record<Limb, unknown>>): Promise<void> {
  const parent = dirname(outputDirectory), rel = relative(privateDirectory, outputDirectory);
  if (!isAbsolute(outputDirectory) || resolve(outputDirectory) !== outputDirectory || rel === "" || rel === ".." || rel.startsWith(`..${sep}`) || isAbsolute(rel) || await realpath(parent) !== parent) throw unavailable("OBSERVATION_OUTPUT_INVALID");
  const parentInfo = await stat(parent); if (!parentInfo.isDirectory() || parentInfo.uid !== (process.getuid?.() ?? -1) || (parentInfo.mode & 0o077) !== 0) throw unavailable("OBSERVATION_OUTPUT_INVALID");
  let created = false;
  try {
    await mkdir(outputDirectory, { mode: 0o700 }); created = true;
    const files: Array<readonly [string, unknown]> = [["observation.json", observation], ...LIMBS.map(limb => [`${limb}.json`, projections[limb]] as const)];
    for (const [name, value] of files) {
      const file = await open(resolve(outputDirectory, name), constants.O_CREAT | constants.O_EXCL | constants.O_WRONLY, 0o600);
      try { await file.writeFile(bytes(value)); await file.sync(); } finally { await file.close(); }
    }
    const directory = await open(outputDirectory, constants.O_RDONLY); try { await directory.sync(); } finally { await directory.close(); }
    const parentHandle = await open(parent, constants.O_RDONLY); try { await parentHandle.sync(); } finally { await parentHandle.close(); }
  } catch (error) { if (created) await rm(outputDirectory, { recursive: true, force: true }); throw error; }
}

async function stageSupplierClosure(sourceExecutablePath: string, privateDirectory: string, entries: readonly Readonly<ExactSupplyClosureEntry>[]): Promise<{ executablePath: string; root: string }> {
  const sourceRoot = dirname(sourceExecutablePath), root = join(privateDirectory, "supplier"), executablePath = join(root, "codex");
  await mkdir(root, { mode: 0o700 });
  try {
    for (const entry of entries.slice(1)) {
      const suffix = entry.relativePath.slice("supplier/".length), source = resolve(sourceRoot, suffix), destination = resolve(root, suffix);
      if (!suffix || !source.startsWith(`${sourceRoot}${sep}`) || !destination.startsWith(`${root}${sep}`)) throw unavailable("OBSERVATION_SUPPLY_STAGE_INVALID");
      if (entry.type === "directory") await mkdir(destination, { mode: 0o700 });
      else { await copyFile(source, destination, constants.COPYFILE_EXCL); await chmod(destination, entry.mode === "executable" ? 0o700 : 0o600); }
    }
    return { executablePath, root };
  } catch (error) { await rm(root, { recursive: true, force: true }); throw error; }
}

const execFileAsync = promisify(execFile);
interface DiagnosticStderrCapture {
  readonly fifoPath: string;
  stop(): Promise<Readonly<{ bytes: Buffer; totalBytes: number }>>;
}
async function startDiagnosticStderrCapture(privateDirectory: string): Promise<DiagnosticStderrCapture> {
  const fifoPath = join(privateDirectory, "supplier-stderr.fifo");
  await execFileAsync("/usr/bin/mkfifo", ["-m", "600", fifoPath], { shell: false, timeout: 10_000, maxBuffer: 1024 });
  const handle = await open(fifoPath, constants.O_RDWR | constants.O_NONBLOCK | constants.O_NOFOLLOW);
  try {
    const info = await handle.stat();
    if (!info.isFIFO() || info.uid !== (process.getuid?.() ?? -1) || (info.mode & 0o777) !== 0o600 || info.nlink !== 1) throw unavailable("OBSERVATION_STDERR_FIFO_INVALID");
  } catch (error) { await handle.close(); throw error; }
  let stopping = false, totalBytes = 0;
  const retained: Buffer[] = [];
  let retainedBytes = 0;
  const pause = () => new Promise<void>(resolvePause => { setTimeout(resolvePause, 5); });
  const drain = (async () => {
    const buffer = Buffer.alloc(8192); let finalReads = 0;
    for (;;) {
      try {
        const read = await handle.read(buffer, 0, buffer.length, null);
        if (read.bytesRead) {
          totalBytes = Math.min(Number.MAX_SAFE_INTEGER, totalBytes + read.bytesRead);
          const keep = Math.min(read.bytesRead, 65_536 - retainedBytes);
          if (keep > 0) { retained.push(Buffer.from(buffer.subarray(0, keep))); retainedBytes += keep; }
          if (stopping && ++finalReads >= 16) break;
          continue;
        }
      } catch (error) { if ((error as NodeJS.ErrnoException).code !== "EAGAIN") throw error; }
      if (stopping) break;
      await pause();
    }
    return Object.freeze({ bytes: Buffer.concat(retained, retainedBytes), totalBytes });
  })();
  void drain.catch(() => {});
  return Object.freeze({ fifoPath, async stop() { stopping = true; try { return await drain; } finally { await handle.close(); } } });
}

async function persistDiagnosticStderr(runtimeDirectory: string, runId: string, capture: Readonly<{ bytes: Buffer; totalBytes: number }>): Promise<AccountFreeLoginStartupDiagnosticV1["stderr"]> {
  const root = join(runtimeDirectory, "account-free-startup-diagnostics"), output = join(root, runId);
  try { await mkdir(root, { mode: 0o700 }); } catch (error) { if ((error as NodeJS.ErrnoException).code !== "EEXIST") throw error; }
  const rootInfo = await stat(root); if (await realpath(root) !== root || !rootInfo.isDirectory() || rootInfo.uid !== (process.getuid?.() ?? -1) || (rootInfo.mode & 0o077) !== 0) throw unavailable("OBSERVATION_DIAGNOSTIC_OUTPUT_INVALID");
  await mkdir(output, { mode: 0o700 });
  const artifactPath = join(output, "supplier-stderr.bin"), file = await open(artifactPath, constants.O_CREAT | constants.O_EXCL | constants.O_WRONLY, 0o600);
  try { await file.writeFile(capture.bytes); await file.sync(); } finally { await file.close(); }
  const directory = await open(output, constants.O_RDONLY); try { await directory.sync(); } finally { await directory.close(); }
  const parent = await open(root, constants.O_RDONLY); try { await parent.sync(); } finally { await parent.close(); }
  return Object.freeze({ status: "captured", artifactPath, sha256: digest(capture.bytes), retainedBytes: capture.bytes.length, totalBytes: capture.totalBytes, truncated: capture.totalBytes > capture.bytes.length });
}

async function runCodexAccountFreeLoginPurposeV2(input: AccountFreeLoginObservationInputV2, mode: "observe" | "diagnostic"): Promise<Readonly<AccountFreeLoginObservationResultV1 | AccountFreeLoginStartupDiagnosticV1>> {
  const recipe = input?.recipe;
  if (!exactKeys(input, ["runtimeDirectory", "resourcesPath", "evidencePaths", "recipe"])
    || !exactKeys(input.evidencePaths, ["signatureEvidenceSha256", "sourceCorrespondenceEvidenceSha256", "xpcRecordSha256", "groupedRecordSha256"])
    || !exactKeys(recipe, ["schema", "runId", "supplyProfile", "supplyClosure", "nativeAddon", "providerNetworkConsent", "supportProfileDigest", "nativePolicyIdentityVersion"])
    || !exactKeys(recipe.nativeAddon, ["sha256", "size", "signatureEvidenceSha256", "sourceCorrespondenceEvidenceSha256", "xpcRecordSha256", "groupedRecordSha256"])
    || !exactKeys(recipe.providerNetworkConsent, ["approvedBy", "approvalReference"])
    || process.platform !== "darwin" || process.arch !== "arm64" || process.versions.electron !== undefined
    || recipe.schema !== "chirality-account-free-login-observation-recipe/v1" || recipe.nativePolicyIdentityVersion !== 11
    || !/^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/.test(recipe.runId)
    || !hex(recipe.supportProfileDigest) || typeof recipe.nativeAddon.size !== "number" || !Number.isSafeInteger(recipe.nativeAddon.size) || recipe.nativeAddon.size < 1
    || typeof recipe.providerNetworkConsent.approvedBy !== "string" || !recipe.providerNetworkConsent.approvedBy.trim() || recipe.providerNetworkConsent.approvedBy.length > 256
    || typeof recipe.providerNetworkConsent.approvalReference !== "string" || !recipe.providerNetworkConsent.approvalReference.trim() || recipe.providerNetworkConsent.approvalReference.length > 1024) throw unavailable("OBSERVATION_INPUT_INVALID");
  for (const value of [recipe.nativeAddon.sha256, recipe.nativeAddon.signatureEvidenceSha256, recipe.nativeAddon.sourceCorrespondenceEvidenceSha256, recipe.nativeAddon.xpcRecordSha256, recipe.nativeAddon.groupedRecordSha256]) if (!hex(value)) throw unavailable("OBSERVATION_INPUT_INVALID");
  if (new Set(Object.values(input.evidencePaths)).size !== 4 || new Set([recipe.nativeAddon.signatureEvidenceSha256, recipe.nativeAddon.sourceCorrespondenceEvidenceSha256, recipe.nativeAddon.xpcRecordSha256, recipe.nativeAddon.groupedRecordSha256]).size !== 4) throw unavailable("OBSERVATION_EVIDENCE_INVALID");
  const evidenceFiles = Object.freeze(Object.fromEntries(await Promise.all(Object.entries(input.evidencePaths).map(async ([field, path]) => {
    if (typeof path !== "string") throw unavailable("OBSERVATION_EVIDENCE_INVALID");
    const expected = recipe.nativeAddon[field as keyof typeof recipe.nativeAddon];
    if (typeof expected !== "string") throw unavailable("OBSERVATION_EVIDENCE_INVALID");
    const observed = await stableEvidence(path, expected);
    return [field, Object.freeze({ sha256: observed.sha256, size: observed.size, identity: observed.identity })] as const;
  }))));
  const contained = (parent: string, path: string) => { const rel = relative(parent, path); return rel !== "" && rel !== ".." && !rel.startsWith(`..${sep}`) && !isAbsolute(rel); };
  for (const path of [input.runtimeDirectory, input.resourcesPath]) if (!isAbsolute(path) || resolve(path) !== path || await realpath(path) !== path) throw unavailable("OBSERVATION_PATH_INVALID");
  if (contained(input.runtimeDirectory, input.resourcesPath) || contained(input.resourcesPath, input.runtimeDirectory) || input.runtimeDirectory === input.resourcesPath) throw unavailable("OBSERVATION_PATH_INVALID");
  const runtimeInfo = await stat(input.runtimeDirectory); if (!runtimeInfo.isDirectory() || runtimeInfo.uid !== (process.getuid?.() ?? -1) || (runtimeInfo.mode & 0o077) !== 0) throw unavailable("OBSERVATION_PATH_INVALID");
  const observationsRoot = join(input.runtimeDirectory, "account-free-observations");
  try { await mkdir(observationsRoot, { mode: 0o700 }); } catch (error) { if ((error as NodeJS.ErrnoException).code !== "EEXIST") throw error; }
  if (await realpath(observationsRoot) !== observationsRoot || (await stat(observationsRoot)).uid !== (process.getuid?.() ?? -1) || ((await stat(observationsRoot)).mode & 0o077) !== 0) throw unavailable("OBSERVATION_PATH_INVALID");
  const runRoot = join(observationsRoot, recipe.runId), canonicalRoot = join(runRoot, "project"), privateDirectory = join(runRoot, "private"), codexHome = join(privateDirectory, "home"), outputDirectory = join(privateDirectory, "evidence");
  await mkdir(runRoot, { mode: 0o700 });
  try { await mkdir(canonicalRoot, { mode: 0o700 }); await mkdir(privateDirectory, { mode: 0o700 }); await mkdir(codexHome, { mode: 0o700 }); }
  catch (error) { await rm(runRoot, { recursive: true, force: true }); throw error; }
  const sourceExecutablePath = join(input.resourcesPath, "supplier", "codex"), nativeAddonPath = join(input.resourcesPath, "native", "chirality_native_admission.node");
  const supplyVerifier = createCustomSupplyVerifier(recipe.supplyProfile, recipe.supplyClosure);
  let staged: Awaited<ReturnType<typeof stageSupplierClosure>> | undefined;
  let sourceSupply: Awaited<ReturnType<typeof supplyVerifier.verify>> | undefined;
  let supply: Awaited<ReturnType<typeof supplyVerifier.verify>> | undefined;
  let containment: Awaited<ReturnType<typeof prepareCodexContainmentV2>> | undefined;
  let child: NativeGroupedSupplierChild | undefined;
  let actor: CodexTurnSession | undefined, retired: Awaited<ReturnType<typeof retireAuthenticatedSupplierGroup>> | undefined;
  let stderrCapture: DiagnosticStderrCapture | undefined, stderrStopped = false;
  let leaderObservation: Promise<Readonly<{ status: "resolved"; elapsedMs: number; leader: Readonly<{ exitCode: number | null; signal: number | null }> } | { status: "unavailable"; elapsedMs: number | null }>> | undefined;
  let initializeIssuedAtMs: number | null = null, initializeSettledAtMs: number | null = null, initializeResolved = false, cleanupStartedAtMs: number | null = null, retirementSettledAtMs: number | null = null;
  let published = false, failureFinalized = false;
  let phase: AccountFreeLoginObservationPhaseV1 = "supply-verification";
  const startedAt = Date.now();
  const allowedMethods = new Set(["initialize", "initialized", "config/read"] as const);
  const secret = randomBytes(32), methods: string[] = [], capture = new PassThrough(); let pending = "";
  try {
    sourceSupply = await supplyVerifier.verify({ executablePath: sourceExecutablePath, custody: "packaged" });
    staged = await stageSupplierClosure(sourceExecutablePath, privateDirectory, recipe.supplyClosure);
    supply = await supplyVerifier.verify({ executablePath: staged.executablePath, custody: "private-staged" });
    await supplyVerifier.revalidate(sourceSupply);
    phase = "prelaunch-verification";
    const addon = await stableFile(nativeAddonPath, recipe.nativeAddon), storageBefore = await directoryObservation(codexHome);
    await assertCodexKeyringHomeHasNoPlaintextCredentials(codexHome);
    phase = "containment";
    containment = await prepareCodexContainmentV2({ purpose: "trusted-login", canonicalRoot, privateDirectory, codexHome,
      providerNetworkConsent: recipe.providerNetworkConsent, trustedRuntimeReadRoots: [] as readonly TrustedRuntimeReadRootBindingV2[] });
    const configOverrides = codexLoginConfigOverridesV2(containment.config), appServerArguments = runtimeStageCAppServerArguments(configOverrides), launch = await containment.launchArguments(supply.executablePath);
    if (JSON.stringify(appServerArguments) !== JSON.stringify(["app-server", RUNTIME_STAGE_C_NATIVE_SKILL_ARGUMENT, ...configOverrides.flatMap(value => ["-c", value])])) throw unavailable("OBSERVATION_COMPILER_INVALID");
    await supplyVerifier.revalidate(sourceSupply); await supplyVerifier.revalidate(supply); await stableFile(nativeAddonPath, recipe.nativeAddon);
    phase = "native-load";
    const native = loadNativeAdmissionBinding(true, nativeAddonPath); if (native.state !== "available") throw unavailable("OBSERVATION_NATIVE_UNAVAILABLE");
    phase = "supplier-spawn";
    if (mode === "diagnostic") stderrCapture = await startDiagnosticStderrCapture(privateDirectory);
    const sandboxArguments = [...launch, ...appServerArguments];
    const spawned = mode === "diagnostic"
      ? native.value.spawnGroupedSupplier("/bin/sh", ["-c", "stderr=$1; shift; exec \"$@\" 2>\"$stderr\"", "chirality-account-free-startup", stderrCapture!.fifoPath, "/usr/bin/sandbox-exec", ...sandboxArguments], secret, { cwd: canonicalRoot, environment: containment.environment, processGroup: true })
      : native.value.spawnGroupedSupplier("/usr/bin/sandbox-exec", sandboxArguments, secret, { cwd: canonicalRoot, environment: containment.environment, processGroup: true });
    if (spawned.state !== "available") throw unavailable("OBSERVATION_SPAWN_UNAVAILABLE"); child = spawned.value;
    if (mode === "diagnostic") leaderObservation = child.observeLeader().then(leader => Object.freeze({ status: "resolved" as const, elapsedMs: Math.max(0, Math.min(86_400_000, Date.now() - startedAt)), leader: Object.freeze({ ...leader }) }), () => Object.freeze({ status: "unavailable" as const, elapsedMs: Math.max(0, Math.min(86_400_000, Date.now() - startedAt)) }));
    capture.on("data", chunk => { pending += String(chunk); for (;;) { const newline = pending.indexOf("\n"); if (newline < 0) break; const line = pending.slice(0, newline); pending = pending.slice(newline + 1); const message = JSON.parse(line) as { method?: unknown }; if (typeof message.method === "string") methods.push(message.method); } });
    capture.pipe(child.stdin);
    const close = async () => {
      if (mode === "diagnostic") cleanupStartedAtMs ??= Math.max(0, Math.min(86_400_000, Date.now() - startedAt));
      try { if (!retired) retired = await retireAuthenticatedSupplierGroup(child!); }
      finally { if (mode === "diagnostic") retirementSettledAtMs ??= Math.max(0, Math.min(86_400_000, Date.now() - startedAt)); }
    };
    actor = new CodexTurnSession({ purpose: "login", nativeSkills: "disabled", transport: { stdin: capture, stdout: child.stdout, close }, ...(mode === "diagnostic" ? { requestTimeoutMs: DIAGNOSTIC_REQUEST_TIMEOUT_MS } : {}) });
    const authority: CodexAuthorityInitialize = { runtimeProcessIncarnationId: randomUUID(), supplierGeneration: randomUUID(), runtimeChallenge: randomBytes(32).toString("base64url"), exactSupplyDigest: supply.sha256, authoritySecret: secret,
      descriptor: { capability: "chirality.local-admission-authority", contract: AUTHORITY_CONTRACT, major: 1, minor: 0 }, v4Descriptor: { capability: "account.identity-snapshot", contract: "chirality-supplier-account-identity/1", major: 1, minor: 0, method: "account/identitySnapshot" } };
    phase = "initialize";
    if (mode === "diagnostic") initializeIssuedAtMs = Math.max(0, Math.min(86_400_000, Date.now() - startedAt));
    try { await actor.initializeAuthority(authority); initializeResolved = true; initializeSettledAtMs = Math.max(0, Math.min(86_400_000, Date.now() - startedAt)); }
    catch (error) { initializeSettledAtMs = Math.max(0, Math.min(86_400_000, Date.now() - startedAt)); throw error; }
    secret.fill(0);
    if (mode === "diagnostic") {
      phase = "retirement"; cleanupStartedAtMs = Math.max(0, Math.min(86_400_000, Date.now() - startedAt));
      await actor.close(); actor = undefined;
      retirementSettledAtMs ??= Math.max(0, Math.min(86_400_000, Date.now() - startedAt));
      if (!retired?.groupRetired) throw unavailable("OBSERVATION_RETIREMENT_INVALID");
      phase = "final-verification";
      await supplyVerifier.revalidate(sourceSupply); await supplyVerifier.revalidate(supply); await stableFile(nativeAddonPath, recipe.nativeAddon);
      const captured = await stderrCapture!.stop(); stderrStopped = true;
      const stderr = await persistDiagnosticStderr(input.runtimeDirectory, recipe.runId, captured);
      const leader = await leaderObservation!;
      return Object.freeze({ schema: "chirality-account-free-login-startup-diagnostic/v1", status: "diagnostic-only", outcome: "initialize-resolved", qualification: false, phase,
        issuedMethods: Object.freeze(methods.filter((value): value is "initialize" | "initialized" => value === "initialize" || value === "initialized")), elapsedMs: Math.max(0, Math.min(86_400_000, Date.now() - startedAt)),
        initialize: Object.freeze({ issuedAtMs: initializeIssuedAtMs, settledAtMs: initializeSettledAtMs }), leaderObservation: leader, cleanupStartedAtMs, retirementSettledAtMs,
        retirement: Object.freeze({ status: "verified", groupRetired: true, leader: Object.freeze({ ...retired.leader }), signalFailurePhases: Object.freeze(retired.signalFailures.map(value => value.phase)) }),
        launchDeviation: Object.freeze({ executable: "/bin/sh", stderrCapture: "private-fifo", sandboxExecutable: "/usr/bin/sandbox-exec", compiledArgumentsUnchanged: true, requestTimeoutMs: DIAGNOSTIC_REQUEST_TIMEOUT_MS }), stderr });
    }
    phase = "config-read";
    const readback = await actor.observeAccountFreeLoginConfiguration(canonicalRoot, containment.config);
    phase = "protocol-validation";
    if (JSON.stringify(methods) !== JSON.stringify(["initialize", "initialized", "config/read"])) throw unavailable("OBSERVATION_PROTOCOL_INVALID");
    phase = "retirement";
    await actor.close(); actor = undefined;
    if (!retired?.groupRetired) throw unavailable("OBSERVATION_RETIREMENT_INVALID");
    phase = "final-verification";
    await supplyVerifier.revalidate(sourceSupply); await supplyVerifier.revalidate(supply); const addonAfter = await stableFile(nativeAddonPath, recipe.nativeAddon);
    await assertCodexKeyringHomeHasNoPlaintextCredentials(codexHome); const storageAfter = await directoryObservation(codexHome);
    if (JSON.stringify(addon.identity) !== JSON.stringify(addonAfter.identity)) throw unavailable("OBSERVATION_FINAL_STATE_CHANGED");
    const common = Object.freeze({ schema: "chirality-account-free-login-observation/v1", observedAt: new Date().toISOString(), accountUsed: false, modelUsed: false, admissionUsed: false, networkTriggeringRpcUsed: false,
      supportProfileDigest: recipe.supportProfileDigest, observationHost: { runtime: "external-node", node: process.versions.node, modules: process.versions.modules ?? "", napi: process.versions.napi ?? "", architecture: process.arch, platform: process.platform },
      supply: { sourcePath: sourceExecutablePath, stagedPath: supply.executablePath, sha256: supply.sha256, size: Number(supply.identity.size), version: supply.version, closure: recipe.supplyClosure,
        sourceIdentity: sourceSupply.identity, stagedIdentity: supply.identity },
      nativeAddon: { path: nativeAddonPath, sha256: addon.sha256, size: addon.size, signatureEvidenceSha256: recipe.nativeAddon.signatureEvidenceSha256, sourceCorrespondenceEvidenceSha256: recipe.nativeAddon.sourceCorrespondenceEvidenceSha256,
        xpcRecordSha256: recipe.nativeAddon.xpcRecordSha256, groupedRecordSha256: recipe.nativeAddon.groupedRecordSha256, evidenceFiles },
      compiler: { nativePolicyIdentityVersion: 11, outerPolicyDigest: containment.outerPolicyDigest, appServerArgumentsSha256: digest(bytes(appServerArguments)), providerNetworkEnabled: containment.providerNetworkEnabled, commandNetworkBoundary: containment.commandNetworkBoundary },
      readback, protocolMethods: methods, storage: { before: storageBefore, after: storageAfter }, retirement: { groupRetired: true, leader: retired.leader, signalFailurePhases: retired.signalFailures.map(value => value.phase) } });
    const observationSha256 = digest(bytes(common)), facts: Record<Limb, unknown> = {
      "exact-supplier": common.supply, "keyring-backend": { credentialStore: readback.credentialStore, compilerConfigDigest: readback.compilerConfigDigest, observedConfigProjectionDigest: readback.observedConfigProjectionDigest },
      "plaintext-fallback-absent": { plaintextFallback: false, storageBefore, storageAfter }, "process-containment": { nativeAddon: common.nativeAddon, compiler: common.compiler },
      "storage-isolation": { storageBefore, storageAfter, home: { source: "os-user-record", privateDirectory: containment.environment.HOME === privateDirectory },
        keyringNamespace: { codexHomePrivate: containment.environment.CODEX_HOME === codexHome }, tmpPrivate: contained(privateDirectory, containment.environment.TMPDIR) },
      "provider-network": { consentDigest: digest(bytes(recipe.providerNetworkConsent)), providerNetworkEnabled: containment.providerNetworkEnabled, commandNetworkBoundary: containment.commandNetworkBoundary, networkTriggeringRpcUsed: false },
      "bounded-protocol-purpose": { privateInitialization: true, methods, laterPurposeMethods: ["account/login/start", "account/login/cancel", "account/read", "model/list"], modelExecution: false },
      "retirement": common.retirement
    };
    const projections = Object.fromEntries(LIMBS.map(limb => [limb, Object.freeze({ schema: "chirality-account-free-login-limb-evidence/v1", limb, observationSha256, facts: facts[limb] })])) as Record<Limb, unknown>;
    const limbs = Object.fromEntries(LIMBS.map(limb => [limb, Object.freeze({ attempted: true as const, passed: true as const, evidenceSha256: digest(bytes(projections[limb])) })])) as Record<Limb, { attempted: true; passed: true; evidenceSha256: string }>;
    phase = "publication";
    await publish(outputDirectory, privateDirectory, common, projections);
    published = true;
    return Object.freeze({ schema: "chirality-account-free-login-observation-result/v1", observationSha256, outputDirectory, limbs: Object.freeze(limbs) });
  } catch (error) {
    const cleanupFailures: unknown[] = [];
    if (mode === "diagnostic" && child) cleanupStartedAtMs ??= Math.max(0, Math.min(86_400_000, Date.now() - startedAt));
    try { if (actor) await actor.close(); else if (child && !retired) retired = await retireAuthenticatedSupplierGroup(child); } catch (cleanup) { cleanupFailures.push(cleanup); }
    finally { if (child) retirementSettledAtMs ??= Math.max(0, Math.min(86_400_000, Date.now() - startedAt)); }
    let diagnosticStderr: AccountFreeLoginStartupDiagnosticV1["stderr"] = Object.freeze({ status: "unavailable" });
    if (mode === "diagnostic" && stderrCapture && !stderrStopped) {
      try {
        const captured = await stderrCapture.stop(); stderrStopped = true;
        if (retired?.groupRetired) diagnosticStderr = await persistDiagnosticStderr(input.runtimeDirectory, recipe.runId, captured);
      } catch (cleanup) { cleanupFailures.push(cleanup); }
    }
    if (!child || retired) {
      try { await containment?.cleanup(); containment = undefined; } catch (cleanup) { cleanupFailures.push(cleanup); }
      try { if (staged) await rm(staged.root, { recursive: true, force: true }); staged = undefined; } catch (cleanup) { cleanupFailures.push(cleanup); }
      try { if (!published) await rm(runRoot, { recursive: true, force: true }); } catch (cleanup) { cleanupFailures.push(cleanup); }
    }
    const retirement = retired?.groupRetired ? Object.freeze({ status: "verified" as const, groupRetired: true as const, leader: Object.freeze({ ...retired.leader }), signalFailurePhases: Object.freeze(retired.signalFailures.map(value => value.phase)) }) : Object.freeze({ status: "unavailable" as const });
    const projection = Object.freeze({ schema: "chirality-account-free-login-observation-failure/v1" as const, status: "failed" as const, phase,
      issuedMethods: Object.freeze(methods.filter((value): value is "initialize" | "initialized" | "config/read" => allowedMethods.has(value as "initialize" | "initialized" | "config/read"))),
      elapsedMs: Math.max(0, Math.min(86_400_000, Date.now() - startedAt)), retirement });
    const failure = cleanupFailures.length ? new AggregateError([error, ...cleanupFailures], "Account-free observation and cleanup failed")
      : error && typeof error === "object" ? error : new Error("Account-free observation failed", { cause: error });
    Object.defineProperty(failure, "accountFreeObservationFailure", { value: projection, enumerable: false });
    if (mode === "diagnostic") {
      const leader = retired?.groupRetired && leaderObservation ? await leaderObservation : Object.freeze({ status: "unavailable" as const, elapsedMs: null });
      const diagnostic = Object.freeze({ schema: "chirality-account-free-login-startup-diagnostic/v1" as const, status: "diagnostic-only" as const, outcome: initializeResolved ? "initialize-resolved" as const : "initialize-failed" as const, qualification: false as const, phase,
        issuedMethods: Object.freeze(methods.filter((value): value is "initialize" | "initialized" => value === "initialize" || value === "initialized")), elapsedMs: Math.max(0, Math.min(86_400_000, Date.now() - startedAt)),
        initialize: Object.freeze({ issuedAtMs: initializeIssuedAtMs, settledAtMs: initializeSettledAtMs }), leaderObservation: leader, cleanupStartedAtMs, retirementSettledAtMs, retirement,
        launchDeviation: Object.freeze({ executable: "/bin/sh" as const, stderrCapture: "private-fifo" as const, sandboxExecutable: "/usr/bin/sandbox-exec" as const, compiledArgumentsUnchanged: true as const, requestTimeoutMs: DIAGNOSTIC_REQUEST_TIMEOUT_MS }), stderr: diagnosticStderr });
      Object.defineProperty(failure, "accountFreeStartupDiagnostic", { value: diagnostic, enumerable: false });
    }
    failureFinalized = true;
    throw failure;
  } finally {
    secret.fill(0);
    if (!stderrStopped && stderrCapture && (!child || retired)) { await stderrCapture.stop(); stderrStopped = true; }
    if (!failureFinalized && (!child || retired)) { await containment?.cleanup(); if (staged) await rm(staged.root, { recursive: true, force: true }); if (!published) await rm(runRoot, { recursive: true, force: true }); }
  }
}

export async function observeCodexAccountFreeLoginPurposeV2(input: AccountFreeLoginObservationInputV2): Promise<Readonly<AccountFreeLoginObservationResultV1>> {
  return await runCodexAccountFreeLoginPurposeV2(input, "observe") as Readonly<AccountFreeLoginObservationResultV1>;
}

export async function diagnoseCodexAccountFreeLoginStartupV1(input: AccountFreeLoginObservationInputV2): Promise<Readonly<AccountFreeLoginStartupDiagnosticV1>> {
  return await runCodexAccountFreeLoginPurposeV2(input, "diagnostic") as Readonly<AccountFreeLoginStartupDiagnosticV1>;
}
