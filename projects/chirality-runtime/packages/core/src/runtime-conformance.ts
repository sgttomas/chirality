import { constants } from "node:fs";
import { lstat, open, realpath, readdir } from "node:fs/promises";
import { createHash, randomUUID } from "node:crypto";
import { dirname, isAbsolute, resolve, join, relative, sep } from "node:path";
import { RuntimeError } from "@chirality/runtime-contracts";
import { inventoryRuntimeDependencies } from "./runtime-dependencies.js";
import { ACCEPTED_SUPPLY, verifyExactSupply } from "./exact-supply.js";

const deny = () => new RuntimeError("ENGINE_UNAVAILABLE", "Runtime conformance is missing, stale, incomplete or not externally accepted", 503);
const hash = (value: string | Buffer) => createHash("sha256").update(value).digest("hex");
const digest = (value: unknown): value is string => typeof value === "string" && /^[a-f0-9]{64}$/.test(value);
const text = (value: unknown): value is string => typeof value === "string" && value.trim() === value && value.length > 0 && value.length <= 512 && !/[\x00-\x1f]/.test(value);
function keys(value: unknown, names: readonly string[]): asserts value is Record<string, unknown> {
  if (!value || typeof value !== "object" || Array.isArray(value) || Object.keys(value).length !== names.length || names.some(name => !Object.hasOwn(value, name))) throw deny();
}
function canonical(path: string): void { if (!text(path) || !isAbsolute(path) || resolve(path) !== path) throw deny(); }
export interface RuntimeConformanceIdentity {
  canonicalRoot: string; cwd: string; policyDigest: string; configDigest: string;
  activationId: string; gateIdentity: string; accountId: string; accountEpoch: number; accountDigest: string; consentVersion: string;
}
export interface RuntimeConformanceBasis extends RuntimeConformanceIdentity {
  executablePath: string;
  /** Ordered host-configured real artifacts, never paths supplied by a public request. */
  sourceFiles: readonly string[];
  packageFiles: readonly string[];
  dependencyResolutionDigest?: string;
}
export interface RuntimeConformanceBindings extends RuntimeConformanceIdentity {
  executablePath: string; sourceDigest: string; packageDigest: string;
}
export const REQUIRED_RUNTIME_CONFORMANCE_LIMBS = Object.freeze([
  "effective-policy", "primary.read", "primary.file-change", "primary.shell-write", "primary.network", "primary.process", "primary.environment", "primary.approval", "primary.role",
  "descendant.read", "descendant.file-change", "descendant.shell-write", "descendant.network", "descendant.process", "descendant.environment", "descendant.approval", "descendant.role", "owner-live-native-delegation"
] as const);
export type RuntimeConformanceLimb = typeof REQUIRED_RUNTIME_CONFORMANCE_LIMBS[number];
export interface RuntimeConformanceRecord {
  schema: "chirality-runtime-conformance/v1";
  evidenceClass: "exact-turn-path-observed";
  bindings: RuntimeConformanceBindings;
  supply: { sha256: string; size: number; version: string };
  issuedAt: string; expiresAt: string;
  limbs: Record<RuntimeConformanceLimb, { attempted: true; passed: true; evidenceSha256: string }>;
}
export interface RuntimeConformanceAcceptancePort {
  /** Trusted host-owned lookup against actual owner records; not a request field or self-assertion. */
  lookup(input: { recordSha256: string; sourceDigest: string; activationId: string; gateIdentity: string }): Promise<{ status: "accepted" | "revoked" | "unknown"; ownerReference?: string }>;
}
export interface RuntimeConformanceAdmission {
  readonly recordSha256: string; readonly ownerReference: string;
  readonly evidence: "mechanically-verified-with-external-acceptance";
  readonly checkedAt: string;
}
const issued = new WeakSet<object>();
const bindingKeys = ["canonicalRoot", "cwd", "policyDigest", "configDigest", "activationId", "gateIdentity", "accountId", "accountEpoch", "accountDigest", "consentVersion", "executablePath", "sourceDigest", "packageDigest"];
function validateBindings(value: RuntimeConformanceBindings): void {
  keys(value, bindingKeys);
  for (const path of [value.canonicalRoot, value.cwd, value.executablePath]) canonical(path);
  if (value.cwd !== value.canonicalRoot) throw deny();
  for (const item of [value.policyDigest, value.configDigest, value.accountDigest, value.consentVersion, value.sourceDigest, value.packageDigest]) if (!digest(item)) throw deny();
  for (const item of [value.activationId, value.gateIdentity, value.accountId]) if (!text(item)) throw deny();
  for (const item of [value.accountEpoch]) if (!Number.isSafeInteger(item) || item < 0) throw deny();
}
/** Mechanical inspection only. This cannot create or substitute for owner acceptance/admission. */
export function inspectRuntimeConformanceRecord(value: unknown, expected: RuntimeConformanceBindings, now = Date.now()): Readonly<RuntimeConformanceRecord> {
  validateBindings(expected);
  keys(value, ["schema", "evidenceClass", "bindings", "supply", "issuedAt", "expiresAt", "limbs"]);
  if (value.schema !== "chirality-runtime-conformance/v1" || value.evidenceClass !== "exact-turn-path-observed") throw deny();
  const record = value as unknown as RuntimeConformanceRecord;
  validateBindings(record.bindings);
  for (const key of bindingKeys as (keyof RuntimeConformanceBindings)[]) if (record.bindings[key] !== expected[key]) throw deny();
  keys(record.supply, ["sha256", "size", "version"]);
  if (record.supply.sha256 !== ACCEPTED_SUPPLY.sha256 || record.supply.size !== ACCEPTED_SUPPLY.size || record.supply.version !== ACCEPTED_SUPPLY.version) throw deny();
  const issuedAt = Date.parse(record.issuedAt), expiresAt = Date.parse(record.expiresAt);
  if (!Number.isFinite(now) || typeof record.issuedAt !== "string" || typeof record.expiresAt !== "string" || !Number.isFinite(issuedAt) || !Number.isFinite(expiresAt) || issuedAt > now || expiresAt <= now || expiresAt <= issuedAt) throw deny();
  keys(record.limbs, REQUIRED_RUNTIME_CONFORMANCE_LIMBS);
  for (const name of REQUIRED_RUNTIME_CONFORMANCE_LIMBS) {
    const limb = record.limbs[name]; keys(limb, ["attempted", "passed", "evidenceSha256"]);
    if (limb.attempted !== true || limb.passed !== true || !digest(limb.evidenceSha256)) throw deny();
  }
  const frozen = structuredClone(record);
  Object.freeze(frozen.bindings); Object.freeze(frozen.supply);
  for (const limb of Object.values(frozen.limbs)) Object.freeze(limb);
  Object.freeze(frozen.limbs); return Object.freeze(frozen);
}
const artifactCache = new Map<string, { sha256: string; size: number; statDigest: string }>();
async function readArtifact(path: string, privateRecord = false, signal?: AbortSignal, captureBytes = privateRecord): Promise<{ sha256: string; size: number; statDigest: string; bytes?: Buffer }> {
  signal?.throwIfAborted();
  canonical(path);
  if (await realpath(path) !== path) throw deny();
  if (privateRecord) { const parent = await lstat(dirname(path)); if (!parent.isDirectory() || parent.uid !== process.getuid?.() || (parent.mode & 0o077) !== 0) throw deny(); }
  const file = await open(path, constants.O_RDONLY | constants.O_NOFOLLOW | constants.O_NONBLOCK);
  try {
    signal?.throwIfAborted();
    const before = await file.stat({ bigint: true });
    if (!before.isFile() || before.size > BigInt(privateRecord ? 1_048_576 : 536_870_912) || (privateRecord && (before.uid !== BigInt(process.getuid?.() ?? -1) || (before.mode & 0o777n) !== 0o600n))) throw deny();
    const statDigest = hash(JSON.stringify([before.dev, before.ino, before.size, before.mtimeNs, before.ctimeNs, before.mode, before.uid].map(String)));
    const cached = privateRecord || captureBytes ? undefined : artifactCache.get(path);
    if (cached?.statDigest === statDigest) {
      const current = await lstat(path, { bigint: true });
      for (const key of ["dev", "ino", "size", "mtimeNs", "ctimeNs", "mode", "uid"] as const) if (before[key] !== current[key]) throw deny();
      if (await realpath(path) !== path) throw deny();
      return cached;
    }
    const sha = createHash("sha256"), parts: Buffer[] = []; let total = 0;
    const buffer = Buffer.alloc(65536);
    for (;;) { signal?.throwIfAborted(); const { bytesRead } = await file.read(buffer, 0, buffer.length, null); if (!bytesRead) break; total += bytesRead; if (total > Number(before.size)) throw deny(); sha.update(buffer.subarray(0, bytesRead)); if (captureBytes) parts.push(Buffer.from(buffer.subarray(0, bytesRead))); }
    const after = await file.stat({ bigint: true }), current = await lstat(path, { bigint: true });
    for (const key of ["dev", "ino", "size", "mtimeNs", "ctimeNs", "mode", "uid"] as const) if (before[key] !== after[key] || before[key] !== current[key]) throw deny();
    if (total !== Number(before.size) || await realpath(path) !== path) throw deny();
    const result = { sha256: sha.digest("hex"), size: total, statDigest, ...(captureBytes ? { bytes: Buffer.concat(parts) } : {}) };
    if (!privateRecord && !captureBytes && artifactCache.size < 50_000) artifactCache.set(path, result);
    return result;
  } finally { await file.close(); }
}
async function mapArtifacts<T>(paths: readonly string[], fn: (path: string) => Promise<T>, signal?: AbortSignal): Promise<T[]> {
  const output: T[] = [];
  for (let offset = 0; offset < paths.length; offset += 64) {
    signal?.throwIfAborted();
    // A failed/cancelled member must not leave sibling file handles running behind a rejected batch.
    const batch = await Promise.allSettled(paths.slice(offset, offset + 64).map(fn));
    const failed = batch.find(result => result.status === "rejected");
    if (failed?.status === "rejected") throw failed.reason;
    signal?.throwIfAborted();
    output.push(...batch.map(result => (result as PromiseFulfilledResult<T>).value));
  }
  return output;
}
/** Digest bytes plus canonical path/size, reusing hashes only with unchanged full file identity. */
export async function computeRuntimeArtifactDigest(paths: readonly string[], dependencyResolutionDigest?: string): Promise<string> {
  if (!Array.isArray(paths) || paths.length < 1 || paths.length > 50_000 || new Set(paths).size !== paths.length) throw deny();
  const inventory = await mapArtifacts(paths, async path => { const item = await readArtifact(path); return { path, size: item.size, sha256: item.sha256 }; });
  if (dependencyResolutionDigest !== undefined && !digest(dependencyResolutionDigest)) throw deny();
  return hash(JSON.stringify(dependencyResolutionDigest === undefined ? inventory : { artifacts: inventory, dependencyResolutionDigest }));
}
export class RuntimeConformanceVerifier {
  constructor(private readonly options: { acceptance: RuntimeConformanceAcceptancePort }) {}
  /** Reconsult acceptance and revalidate byte-cache identities on EVERY admission; returned objects are never portable launch tokens. */
  async verify(input: { recordPath: string; basis: RuntimeConformanceBasis }): Promise<RuntimeConformanceAdmission> {
    try {
      const generationController = configuredArtifactGeneration(), generation = await generationController.check();
      const basis = structuredClone(input.basis);
      keys(basis, [...bindingKeys.filter(key => key !== "sourceDigest" && key !== "packageDigest"), "sourceFiles", "packageFiles", ...(basis.dependencyResolutionDigest === undefined ? [] : ["dependencyResolutionDigest"])]);
      const { sourceFiles, packageFiles, dependencyResolutionDigest, ...identity } = basis;
      const bindings = { ...identity, sourceDigest: await computeRuntimeArtifactDigest(sourceFiles), packageDigest: await computeRuntimeArtifactDigest(packageFiles, dependencyResolutionDigest) };
      if (await realpath(bindings.canonicalRoot) !== bindings.canonicalRoot || !(await lstat(bindings.canonicalRoot)).isDirectory()) throw deny();
      const source = await readArtifact(input.recordPath, true);
      inspectRuntimeConformanceRecord(JSON.parse(source.bytes!.toString("utf8")), bindings);
      const acceptance = await this.options.acceptance.lookup({ recordSha256: source.sha256, sourceDigest: bindings.sourceDigest, activationId: bindings.activationId, gateIdentity: bindings.gateIdentity });
      if (acceptance?.status !== "accepted" || !text(acceptance.ownerReference)) throw deny();
      // Generic embedded callers cannot substitute a harmless file subset for this process's deployed closure.
      if (bindings.sourceDigest !== generation.sourceDigest || bindings.packageDigest !== generation.packageDigest) throw deny();
      await verifyExactSupply({ executablePath: bindings.executablePath });
      // Recheck inputs across asynchronous owner/supply verification, preventing stale results from intervening changes.
      if ((await readArtifact(input.recordPath, true)).sha256 !== source.sha256 || await computeRuntimeArtifactDigest(sourceFiles) !== bindings.sourceDigest || await computeRuntimeArtifactDigest(packageFiles, dependencyResolutionDigest) !== bindings.packageDigest) throw deny();
      inspectRuntimeConformanceRecord(JSON.parse(source.bytes!.toString("utf8")), bindings);
      const currentAcceptance = await this.options.acceptance.lookup({ recordSha256: source.sha256, sourceDigest: bindings.sourceDigest, activationId: bindings.activationId, gateIdentity: bindings.gateIdentity });
      if (currentAcceptance?.status !== "accepted" || currentAcceptance.ownerReference !== acceptance.ownerReference) throw deny();
      await generationController.check();
      const result = Object.freeze({ recordSha256: source.sha256, ownerReference: acceptance.ownerReference, evidence: "mechanically-verified-with-external-acceptance" as const, checkedAt: new Date().toISOString() });
      generationController.assertActive();
      issued.add(result); return result;
    } catch { throw deny(); }
  }
}
/** Provenance check only, NOT a replacement for verifier.verify at the next admission. */
export function isRuntimeConformanceAdmission(value: unknown): value is RuntimeConformanceAdmission { return typeof value === "object" && value !== null && issued.has(value); }

export interface RuntimeConformanceConfiguration {
  recordPath: string; acceptancePath: string; ownerActPath: string; ownerActSha256: string;
  activationId: string; gateIdentity: string;
  artifactInventory: RuntimeConformanceArtifactInventorySelection;
}
/** Host-selected owner act pin is external asserted acceptance, not machine interpretation of human intent. */
export class RuntimeConformanceFileAcceptancePort implements RuntimeConformanceAcceptancePort {
  constructor(private readonly config: Pick<RuntimeConformanceConfiguration, "acceptancePath" | "ownerActPath" | "ownerActSha256">) {}
  async lookup(input: { recordSha256: string; sourceDigest: string; activationId: string; gateIdentity: string }): Promise<{ status: "accepted" | "revoked" | "unknown"; ownerReference?: string }> {
    try {
      if (!digest(this.config.ownerActSha256) || (await readArtifact(this.config.ownerActPath)).sha256 !== this.config.ownerActSha256) return { status: "unknown" };
      const source = await readArtifact(this.config.acceptancePath, true);
      const record = JSON.parse(source.bytes!.toString("utf8"));
      keys(record, ["schema", "status", "recordSha256", "sourceDigest", "activationId", "gateIdentity", "ownerActSha256", "ownerReference", "expiresAt"]);
      if (record.schema !== "chirality-runtime-conformance-acceptance/v1" || record.ownerActSha256 !== this.config.ownerActSha256 || !text(record.ownerReference)
        || typeof record.expiresAt !== "string" || !Number.isFinite(Date.parse(record.expiresAt)) || Date.parse(record.expiresAt) <= Date.now()) return { status: "unknown" };
      for (const key of ["recordSha256", "sourceDigest", "activationId", "gateIdentity"] as const) if (record[key] !== input[key]) return { status: "unknown" };
      if (record.status === "revoked") return { status: "revoked" };
      return record.status === "accepted" ? { status: "accepted", ownerReference: record.ownerReference } : { status: "unknown" };
    } catch { return { status: "unknown" }; }
  }
}
export type RuntimeConformanceArtifactInventorySelection =
  | { kind: "source-tree"; sourceRoot: string }
  | { kind: "packaged-resources"; resourcesRoot: string; manifestPath: string };
export interface RuntimeArtifactInventoryManifest {
  schema: "chirality-runtime-artifact-inventory/v1";
  sourceIdentityDigest: string;
  dependencyResolutionDigest: string;
  closureRoots: readonly string[];
  entries: readonly { relativePath: string; sha256: string; size: number }[];
}
const requiredPackagedRoots = Object.freeze(["app.asar", "instruction-root", "native", "runtime-cli"] as const);
const requiredPackagedFiles = Object.freeze(["app.asar", "instruction-root/instruction-bundle-manifest.json", "native/chirality_native_admission.node", "runtime-cli/chirality-cli.mjs", "runtime-cli/chirality-cli.mjs.map"] as const);
function cleanRelativePath(value: unknown): value is string {
  return text(value) && !isAbsolute(value) && !value.includes("\\") && value !== "." && !value.startsWith("../") && !value.includes("/../") && resolve("/", value) === join("/", value);
}
function validateSelection(value: RuntimeConformanceArtifactInventorySelection): void {
  if (value?.kind === "source-tree") {
    keys(value, ["kind", "sourceRoot"]); canonical(value.sourceRoot);
    return;
  }
  if (value?.kind === "packaged-resources") {
    keys(value, ["kind", "resourcesRoot", "manifestPath"]); canonical(value.resourcesRoot); canonical(value.manifestPath);
    if (value.manifestPath !== join(value.resourcesRoot, "runtime-artifact-inventory.json")) throw deny();
    return;
  }
  throw deny();
}
async function walkRegularFiles(root: string, signal: AbortSignal | undefined, output: string[]): Promise<void> {
  signal?.throwIfAborted();
  if (await realpath(root) !== root) throw deny();
  const info = await lstat(root);
  if (info.isFile()) { output.push(root); return; }
  if (!info.isDirectory()) throw deny();
  for (const entry of (await readdir(root)).sort()) await walkRegularFiles(join(root, entry), signal, output);
}
/** Host-selected complete disk inventory; packaged mode verifies a Packaging-produced closure manifest. */
async function buildRuntimeConformanceArtifactInventory(selection: RuntimeConformanceArtifactInventorySelection, signal?: AbortSignal): Promise<ArtifactInventory> {
  signal?.throwIfAborted();
  validateSelection(selection);
  if (selection.kind === "packaged-resources") {
    if (await realpath(selection.resourcesRoot) !== selection.resourcesRoot || !(await lstat(selection.resourcesRoot)).isDirectory()) throw deny();
    const manifestArtifact = await readArtifact(selection.manifestPath, false, signal, true);
    if (manifestArtifact.size > 16_777_216) throw deny();
    const manifest = JSON.parse(manifestArtifact.bytes!.toString("utf8")) as unknown;
    keys(manifest, ["schema", "sourceIdentityDigest", "dependencyResolutionDigest", "closureRoots", "entries"]);
    const value = manifest as unknown as RuntimeArtifactInventoryManifest;
    if (value.schema !== "chirality-runtime-artifact-inventory/v1" || !digest(value.sourceIdentityDigest) || !digest(value.dependencyResolutionDigest)
      || !Array.isArray(value.closureRoots) || !Array.isArray(value.entries)) throw deny();
    const roots = [...value.closureRoots];
    if (roots.length < requiredPackagedRoots.length || roots.length > 32 || new Set(roots).size !== roots.length
      || roots.some(root => !cleanRelativePath(root) || root === "runtime-artifact-inventory.json") || !requiredPackagedRoots.every(root => roots.includes(root))) throw deny();
    for (let index = 1; index < roots.length; index++) if (roots[index - 1]! >= roots[index]!) throw deny();
    for (let left = 0; left < roots.length; left++) for (let right = left + 1; right < roots.length; right++) {
      if (roots[right]!.startsWith(`${roots[left]!}/`)) throw deny();
    }
    const actual: string[] = [];
    for (const root of roots) {
      const path = join(selection.resourcesRoot, root);
      if (relative(selection.resourcesRoot, path).startsWith(`..${sep}`)) throw deny();
      // Prove every mandatory semantic root exists and is canonical before the complete Resources walk.
      if (await realpath(path) !== path) throw deny();
    }
    await walkRegularFiles(selection.resourcesRoot, signal, actual);
    const deployedFiles = actual.filter(path => path !== selection.manifestPath);
    const entries = [...value.entries];
    if (entries.length < requiredPackagedFiles.length || entries.length > 50_000) throw deny();
    const paths: string[] = [], expectedArtifacts = new Map<string, { sha256: string; size: number }>([[selection.manifestPath, { sha256: manifestArtifact.sha256, size: manifestArtifact.size }]]);
    for (let index = 0; index < entries.length; index++) {
      const raw: unknown = entries[index]!;
      keys(raw, ["relativePath", "sha256", "size"]);
      const entry = raw as unknown as RuntimeArtifactInventoryManifest["entries"][number];
      if (!cleanRelativePath(entry.relativePath) || !digest(entry.sha256) || !Number.isSafeInteger(entry.size) || entry.size < 0
        || (index > 0 && entries[index - 1]!.relativePath >= entry.relativePath)
        || !roots.some(root => entry.relativePath === root || entry.relativePath.startsWith(`${root}/`))) throw deny();
      const path = join(selection.resourcesRoot, entry.relativePath), artifact = await readArtifact(path, false, signal);
      if (artifact.sha256 !== entry.sha256 || artifact.size !== entry.size) throw deny();
      paths.push(path); expectedArtifacts.set(path, { sha256: entry.sha256, size: entry.size });
    }
    if (!requiredPackagedFiles.every(path => entries.some(entry => entry.relativePath === path))) throw deny();
    const actualRelative = deployedFiles.map(path => relative(selection.resourcesRoot, path).split(sep).join("/")).sort();
    if (actualRelative.length !== entries.length || actualRelative.some((path, index) => path !== entries[index]!.relativePath)) throw deny();
    // The manifest is included in both digests: its asserted source identity cannot float free of verified deployed bytes.
    const files = Object.freeze([selection.manifestPath, ...paths]);
    return { sourceFiles: files, packageFiles: files, dependencyResolutionDigest: value.dependencyResolutionDigest, expectedArtifacts };
  }
  const runtimeRoot = selection.sourceRoot;
  if (await realpath(runtimeRoot) !== runtimeRoot || !(await lstat(runtimeRoot)).isDirectory()) throw deny();
  const packages = join(runtimeRoot, "packages"), sourceFiles: string[] = [], packageFiles = [join(runtimeRoot, "package-lock.json"), join(runtimeRoot, "package.json")], workspaceRoots: string[] = [];
  for (const name of (await readdir(packages)).sort()) {
    const path = join(packages, name);
    if (!(await lstat(path)).isDirectory() || await realpath(path) !== path) throw deny();
    workspaceRoots.push(path); packageFiles.push(join(path, "package.json")); await walkRegularFiles(join(path, "dist"), signal, sourceFiles);
  }
  if (sourceFiles.length === 0) throw deny();
  const dependencies = await inventoryRuntimeDependencies(runtimeRoot, [runtimeRoot, ...workspaceRoots], signal);
  return { sourceFiles: Object.freeze(sourceFiles), packageFiles: Object.freeze([...packageFiles, ...dependencies.files]), dependencyResolutionDigest: dependencies.resolutionDigest };
}
export async function runtimeConformanceArtifactInventory(selection: RuntimeConformanceArtifactInventorySelection, signal?: AbortSignal): Promise<ArtifactInventory> {
  try { return await buildRuntimeConformanceArtifactInventory(selection, signal); } catch { throw deny(); }
}
/** Exact reviewed instruction-bundle identity from the verified packaged closure. Source-tree mode has no native instruction-read basis. */
export async function runtimeConformanceInstructionBundleDigest(selection: RuntimeConformanceArtifactInventorySelection, signal?: AbortSignal): Promise<string> {
  try {
    if (selection.kind !== "packaged-resources") throw deny();
    const inventory = await buildRuntimeConformanceArtifactInventory(selection, signal), root = join(selection.resourcesRoot, "instruction-root");
    const records = inventory.sourceFiles.filter(path => path.startsWith(`${root}${sep}`)).map(path => {
      const expected = inventory.expectedArtifacts?.get(path);
      if (!expected) throw deny();
      return { path: relative(root, path).split(sep).join("/"), sha256: expected.sha256, size: expected.size };
    });
    if (records.length < 2 || records[0]?.path !== "instruction-bundle-manifest.json") throw deny();
    return hash(JSON.stringify(records));
  } catch { throw deny(); }
}
/** Supervisor-only integration: identities are actual bound configuration/account/consent, not public requests. */
export async function verifyConfiguredRuntimeConformance(config: RuntimeConformanceConfiguration | undefined, actual: Omit<RuntimeConformanceIdentity, "activationId" | "gateIdentity"> & { executablePath: string }): Promise<RuntimeConformanceAdmission> {
  try {
  if (config === undefined) throw deny();
  keys(config, ["recordPath", "acceptancePath", "ownerActPath", "ownerActSha256", "activationId", "gateIdentity", "artifactInventory"]);
  for (const path of [config.recordPath, config.acceptancePath, config.ownerActPath]) canonical(path);
  if (!digest(config.ownerActSha256) || !text(config.activationId) || !text(config.gateIdentity)) throw deny();
  const selection = structuredClone(config.artifactInventory);
  configureRuntimeConformanceArtifactInventory(selection);
  const inventory = await runtimeConformanceArtifactInventory(selection);
  return await new RuntimeConformanceVerifier({ acceptance: new RuntimeConformanceFileAcceptancePort(config) }).verify({ recordPath: config.recordPath,
    basis: { ...actual, ...inventory, activationId: config.activationId, gateIdentity: config.gateIdentity } });
  } catch { throw deny(); }
}

interface ArtifactInventory { sourceFiles: readonly string[]; packageFiles: readonly string[]; dependencyResolutionDigest?: string; expectedArtifacts?: ReadonlyMap<string, { sha256: string; size: number }> }
interface ArtifactSnapshot { sourceDigest: string; packageDigest: string; fingerprint: string }
async function artifactSnapshot(inventory: ArtifactInventory, signal?: AbortSignal): Promise<ArtifactSnapshot> {
  const metadata: { path: string; sha256: string; statDigest: string }[] = [];
  const collect = async (paths: readonly string[], resolutionDigest?: string) => {
    if (paths.length === 0 || new Set(paths).size !== paths.length) throw deny();
    const records = await mapArtifacts(paths, async path => {
      const file = await readArtifact(path, false, signal);
      const expected = inventory.expectedArtifacts?.get(path);
      if (expected !== undefined && (file.sha256 !== expected.sha256 || file.size !== expected.size)) throw deny();
      return { artifact: { path, size: file.size, sha256: file.sha256 }, metadata: { path, sha256: file.sha256, statDigest: file.statDigest } };
    }, signal);
    const values = records.map(record => record.artifact); metadata.push(...records.map(record => record.metadata));
    if (resolutionDigest !== undefined && !digest(resolutionDigest)) throw deny();
    return hash(JSON.stringify(resolutionDigest === undefined ? values : { artifacts: values, dependencyResolutionDigest: resolutionDigest }));
  };
  const sourceDigest = await collect(inventory.sourceFiles), packageDigest = await collect(inventory.packageFiles, inventory.dependencyResolutionDigest);
  return Object.freeze({ sourceDigest, packageDigest, fingerprint: hash(JSON.stringify(metadata)) });
}
class ArtifactGeneration {
  private poisoned = false;
  private readonly abort = new AbortController();
  private readonly baseline: Promise<ArtifactSnapshot>;
  private readonly activeChecks = new Set<Promise<ArtifactSnapshot>>();
  private retirement?: Promise<void>;
  readonly id = randomUUID();
  constructor(private readonly inventory: (signal?: AbortSignal) => Promise<ArtifactInventory>) {
    // Capture begins immediately, not when the first record or verifier is supplied.
    this.baseline = this.inventory(this.abort.signal).then(value => artifactSnapshot(value, this.abort.signal));
    void this.baseline.catch(() => { this.poisoned = true; });
  }
  check(): Promise<ArtifactSnapshot> {
    const operation = this.checkCurrent();
    this.activeChecks.add(operation);
    void operation.then(() => this.activeChecks.delete(operation), () => this.activeChecks.delete(operation));
    return operation;
  }
  private async checkCurrent(): Promise<ArtifactSnapshot> {
    try {
      if (this.poisoned) throw deny();
      const baseline = await this.baseline, current = await artifactSnapshot(await this.inventory(this.abort.signal), this.abort.signal);
      if (this.poisoned || current.fingerprint !== baseline.fingerprint || current.sourceDigest !== baseline.sourceDigest || current.packageDigest !== baseline.packageDigest) throw deny();
      return baseline;
    } catch { this.poisoned = true; throw deny(); }
  }
  assertActive(): void { if (this.poisoned || this.abort.signal.aborted) throw deny(); }
  retire(): Promise<void> {
    if (this.retirement) return this.retirement;
    // Whole-process retirement is irreversible: no future admission or constructor can reset this generation.
    this.poisoned = true; this.abort.abort();
    this.retirement = Promise.allSettled([this.baseline, ...this.activeChecks]).then(() => {});
    return this.retirement;
  }
}
// Exactly one irreversible baseline per loaded core module/process generation.
// This is an on-disk startup observation, not proof of bytes already in Node's module cache.
let processArtifactGeneration: ArtifactGeneration | undefined;
let processArtifactSelection: string | undefined;
let processArtifactSelectionPoisoned = false;
/** Must be called by the trusted host before runtime startup work. A changed selection permanently poisons this module generation. */
export function configureRuntimeConformanceArtifactInventory(selection: RuntimeConformanceArtifactInventorySelection): void {
  try {
    validateSelection(selection);
    const frozen: RuntimeConformanceArtifactInventorySelection = selection.kind === "source-tree"
      ? { kind: "source-tree", sourceRoot: selection.sourceRoot }
      : { kind: "packaged-resources", resourcesRoot: selection.resourcesRoot, manifestPath: selection.manifestPath };
    const identity = JSON.stringify(frozen);
    if (processArtifactSelectionPoisoned || (processArtifactSelection !== undefined && processArtifactSelection !== identity)) {
      processArtifactSelectionPoisoned = true; void processArtifactGeneration?.retire(); throw deny();
    }
    if (processArtifactGeneration === undefined) {
      Object.freeze(frozen); processArtifactSelection = identity;
      processArtifactGeneration = new ArtifactGeneration(signal => runtimeConformanceArtifactInventory(frozen, signal));
    }
  } catch { processArtifactSelectionPoisoned = true; void processArtifactGeneration?.retire(); throw deny(); }
}
function configuredArtifactGeneration(): ArtifactGeneration {
  if (processArtifactSelectionPoisoned || processArtifactGeneration === undefined) throw deny();
  return processArtifactGeneration;
}
/** Full process shutdown only: poison admission and join managed inventory/hash work; never a daemon restart API. */
export async function retireRuntimeConformanceGeneration(): Promise<void> {
  processArtifactSelectionPoisoned = true;
  if (processArtifactGeneration !== undefined) await processArtifactGeneration.retire();
}
export async function captureRuntimeConformanceGeneration(): Promise<Readonly<{ generationId: string; sourceDigest: string; packageDigest: string; evidence: "startup-disk-inventory-not-loaded-module-proof" }>> {
  const generation = configuredArtifactGeneration(), baseline = await generation.check();
  return Object.freeze({ generationId: generation.id, sourceDigest: baseline.sourceDigest, packageDigest: baseline.packageDigest, evidence: "startup-disk-inventory-not-loaded-module-proof" });
}
/** Controlled temporary-artifact test seam; cannot reset, replace or authorize the production singleton. */
export function createControlledArtifactGenerationForTests(inventory: () => Promise<ArtifactInventory>): { createVerifier(): { verify(): Promise<Readonly<ArtifactSnapshot>> } } {
  const generation = new ArtifactGeneration(inventory);
  return Object.freeze({ createVerifier: () => Object.freeze({ verify: () => generation.check() }) });
}
