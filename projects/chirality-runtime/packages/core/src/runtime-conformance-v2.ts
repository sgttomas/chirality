import { createHash } from "node:crypto";
import { execFile } from "node:child_process";
import { constants } from "node:fs";
import { lstat, open, readdir, realpath } from "node:fs/promises";
import { isAbsolute, join, relative, resolve, sep } from "node:path";
import { RuntimeError } from "@chirality/runtime-contracts";

export type RuntimeSha256V2 = string;
export const RUNTIME_V2_MAX_PAYLOAD_ARTIFACT_BYTES = 1_073_741_824 as const;
const RUNTIME_V2_MAX_SYSTEM_OR_NATIVE_ARTIFACT_BYTES = 536_870_912;
export const RUNTIME_NATIVE_ADMISSION_NAPI_VERSION_V2 = "6" as const;
/** Stage C is an additive compiler identity. Historical native-10 profiles remain unchanged. */
export const RUNTIME_STAGE_C_NATIVE_POLICY_IDENTITY_VERSION = 11 as const;
export const RUNTIME_STAGE_C_NATIVE_SKILL_ARGUMENT = "--chirality-disable-native-skills" as const;
export const RUNTIME_STAGE_C_NATIVE_TOOLS_SCHEMA = "chirality-native-tools/v1" as const;
export const RUNTIME_STAGE_C_POLICY_PARAMETER_DECLARATION = Object.freeze({
  schema: "chirality-runtime-stage-c-policy-parameters/v1",
  nativePolicyIdentityVersion: RUNTIME_STAGE_C_NATIVE_POLICY_IDENTITY_VERSION,
  nativeSkills: "disabled",
  appServerArgument: RUNTIME_STAGE_C_NATIVE_SKILL_ARGUMENT,
  effectiveReadback: Object.freeze({ nativeSkills: "disabled" }),
  inheritedToolsSchema: RUNTIME_STAGE_C_NATIVE_TOOLS_SCHEMA,
  inheritedToolsDigestEncoding: "typed-utf8-length-prefix-v1"
} as const);
export function runtimeStageCPolicyParameterSchemaDigest(): RuntimeSha256V2 {
  return sha256(canonicalJsonBytes(RUNTIME_STAGE_C_POLICY_PARAMETER_DECLARATION));
}
/** The single compiler-owned native-11 app-server argv projection. */
export function runtimeStageCAppServerArguments(configOverrides: readonly string[]): readonly string[] {
  if (!Array.isArray(configOverrides) || configOverrides.some(value => typeof value !== "string" || !value.length || value.includes("\0"))) throw unavailable();
  return Object.freeze(["app-server", RUNTIME_STAGE_C_NATIVE_SKILL_ARGUMENT, ...configOverrides.flatMap(value => ["-c", value])]);
}
export interface RuntimeArtifactEntryV2<P extends string = string> { relativePath: P; size: number; sha256: RuntimeSha256V2 }
export type RuntimePayloadEntryV2 =
  | { relativePath: string; type: "directory" }
  | { relativePath: string; type: "file"; size: number; sha256: RuntimeSha256V2 };

export interface RuntimeSupportProfileV2 {
  schema: "chirality-runtime-support-profile/v2";
  macosProductVersion: string;
  macosBuildVersion: string;
  architecture: "arm64";
  electronVersion: string;
  nodeVersion: string;
  nodeModuleAbi: string;
  napiVersion: string;
  osMeasurement: { executablePath: "/usr/bin/sw_vers"; executableSha256: RuntimeSha256V2; executableSize: number };
  sandboxExec: { path: "/usr/bin/sandbox-exec"; sha256: RuntimeSha256V2; size: number };
  nativeAdmission: { contract: "chirality-native-admission/v1"; sha256: RuntimeSha256V2; size: number; napiVersion: string };
  supplier: { version: string; sha256: RuntimeSha256V2; size: number; appServerProtocolDigest: RuntimeSha256V2; authorityContract: "chirality.local-admission-authority/1.0"; identityContract: "chirality-supplier-account-identity/1" };
  compiler: { outerPolicySchema: "chirality-codex-outer-policy/v2"; nativePolicyIdentityVersion: 10 | 11; sourceDigest: RuntimeSha256V2; parameterSchemaDigest: RuntimeSha256V2 };
  immutableSystemRoots: readonly string[];
  kernelHelperContractDigest: RuntimeSha256V2;
  profileDigest: RuntimeSha256V2;
}

export interface RuntimePayloadManifestV2 {
  schema: "chirality-runtime-payload-manifest/v2";
  dependencyResolutionDigest: RuntimeSha256V2;
  roots: readonly string[];
  supportProfiles: readonly RuntimeSupportProfileV2[];
  entries: readonly RuntimePayloadEntryV2[];
}

export interface RuntimeArtifactInventoryV2 {
  schema: "chirality-runtime-artifact-inventory/v2";
  payloadManifest: RuntimeArtifactEntryV2<"runtime-payload-manifest.json">;
  governance: readonly [
    RuntimeArtifactEntryV2<"runtime-governance/v2/login-purpose-record.json">,
    RuntimeArtifactEntryV2<"runtime-governance/v2/login-purpose-acceptance.json">,
    RuntimeArtifactEntryV2<"runtime-governance/v2/login-owner-act">,
    RuntimeArtifactEntryV2<"runtime-governance/v2/worker-purpose-record.json">,
    RuntimeArtifactEntryV2<"runtime-governance/v2/worker-purpose-acceptance.json">,
    RuntimeArtifactEntryV2<"runtime-governance/v2/worker-owner-act">
  ];
}

export interface RuntimePolicyParameterDeclarationV2 {
  schema: "chirality-runtime-policy-parameters/v2";
  outerPolicySchema: "chirality-codex-outer-policy/v2";
  nativePolicyIdentityVersion: 10;
  bounds: {
    immutableReadRoots: 64; protectedPaths: 256; readOnlyProjectPaths: 32;
    trustedRuntimeReadRoots: 1; trustedRuntimeReadPaths: 32; pathUtf8Bytes: 4095;
    consentUtf8Bytes: 512; nativeRoleOverrides: 12;
  };
  ordering: "unsigned-utf8";
  collisionPolicy: "reject-except-readonly-or-deny-descendant-of-project-write";
  outerDefaults: {
    readableSystemPaths: readonly ["/System","/usr","/bin","/sbin","/Library/Apple","/private/var/db/dyld"];
    readableDevices: readonly ["/dev/null","/dev/urandom","/dev/random"];
    writableDevice: "/dev/null";
    sandboxMode: "workspace-write"; networkAccess: false; approvalPolicy: "never";
    excludeSlashTmp: true; excludeTmpdirEnvVar: true; plugins: false; shellSnapshot: false;
    useLoginShell: false; checkForUpdateOnStartup: false; webSearch: "disabled";
    analytics: false; feedback: false; credentialsStore: "keyring";
    path: "/usr/bin:/bin:/usr/sbin:/sbin"; lang: "en_US.UTF-8";
  };
  nativeDefaults: {
    shellSnapshot: false; approvalsReviewer: "user"; sandboxMode: "workspace-write";
    excludePlatformSandboxDefaults: true; useLoginShell: false; projectTrusted: true;
    permissionProfilePrefix: "chirality_"; permissionProfileDigestCharacters: 24;
    authoritySecretFd: 3; groupedProcess: true; cwd: "canonical-project-root";
  };
  commandNetworkPostures: readonly ["off","ask-per-destination","on"];
  nativeRoleNames: readonly ["HELP_HUMAN","HELPS_HUMANS","WORKING_ITEMS","TASK"];
  nativeRolePrefixOverrides: readonly ["agents.enabled=true","features.multi_agent=true","features.multi_agent_v2=false","agents.max_depth=2"];
  nativeArgumentOrder: readonly ["approval","sandbox","login-keyring-update-search","workspace-network-tmp","proxy-shell-plugins","analytics-feedback","trusted-project","permissions","roles"];
  launcher: readonly ["/usr/bin/sandbox-exec","-f","<ephemeral-outer-profile>","<staged-supplier/codex>","app-server","<ordered-native-args>"];
}

export const RUNTIME_POLICY_PARAMETER_DECLARATION_V2: Readonly<RuntimePolicyParameterDeclarationV2> = Object.freeze({
  schema: "chirality-runtime-policy-parameters/v2",
  outerPolicySchema: "chirality-codex-outer-policy/v2",
  nativePolicyIdentityVersion: 10,
  bounds: Object.freeze({ immutableReadRoots: 64, protectedPaths: 256, readOnlyProjectPaths: 32, trustedRuntimeReadRoots: 1, trustedRuntimeReadPaths: 32, pathUtf8Bytes: 4095, consentUtf8Bytes: 512, nativeRoleOverrides: 12 }),
  ordering: "unsigned-utf8",
  collisionPolicy: "reject-except-readonly-or-deny-descendant-of-project-write",
  outerDefaults: Object.freeze({ readableSystemPaths: Object.freeze(["/System","/usr","/bin","/sbin","/Library/Apple","/private/var/db/dyld"] as const), readableDevices: Object.freeze(["/dev/null","/dev/urandom","/dev/random"] as const), writableDevice: "/dev/null", sandboxMode: "workspace-write", networkAccess: false, approvalPolicy: "never", excludeSlashTmp: true, excludeTmpdirEnvVar: true, plugins: false, shellSnapshot: false, useLoginShell: false, checkForUpdateOnStartup: false, webSearch: "disabled", analytics: false, feedback: false, credentialsStore: "keyring", path: "/usr/bin:/bin:/usr/sbin:/sbin", lang: "en_US.UTF-8" }),
  nativeDefaults: Object.freeze({ shellSnapshot: false, approvalsReviewer: "user", sandboxMode: "workspace-write", excludePlatformSandboxDefaults: true, useLoginShell: false, projectTrusted: true, permissionProfilePrefix: "chirality_", permissionProfileDigestCharacters: 24, authoritySecretFd: 3, groupedProcess: true, cwd: "canonical-project-root" }),
  commandNetworkPostures: Object.freeze(["off","ask-per-destination","on"] as const),
  nativeRoleNames: Object.freeze(["HELP_HUMAN","HELPS_HUMANS","WORKING_ITEMS","TASK"] as const),
  nativeRolePrefixOverrides: Object.freeze(["agents.enabled=true","features.multi_agent=true","features.multi_agent_v2=false","agents.max_depth=2"] as const),
  nativeArgumentOrder: Object.freeze(["approval","sandbox","login-keyring-update-search","workspace-network-tmp","proxy-shell-plugins","analytics-feedback","trusted-project","permissions","roles"] as const),
  launcher: Object.freeze(["/usr/bin/sandbox-exec","-f","<ephemeral-outer-profile>","<staged-supplier/codex>","app-server","<ordered-native-args>"] as const)
});

const unavailable = () => new RuntimeError("ENGINE_UNAVAILABLE", "Packaged Runtime release basis is missing, invalid, stale or unsupported", 503);
const sha256 = (bytes: string | Buffer) => createHash("sha256").update(bytes).digest("hex");
const digest = (value: unknown): value is string => typeof value === "string" && /^[a-f0-9]{64}$/.test(value);
const exactKeys = (value: unknown, names: readonly string[]): value is Record<string, unknown> => !!value && typeof value === "object" && !Array.isArray(value) && Object.keys(value).length === names.length && names.every(name => Object.hasOwn(value, name));
export const compareRuntimeUtf8V2 = (left: string, right: string): number => Buffer.compare(Buffer.from(left, "utf8"), Buffer.from(right, "utf8"));

function pathText(value: unknown): value is string {
  if (typeof value !== "string" || value !== value.normalize("NFC") || Buffer.byteLength(value, "utf8") < 1 || Buffer.byteLength(value, "utf8") > 4095 || /[\\\x00-\x1f]/.test(value)) return false;
  if (isAbsolute(value) || value.startsWith("/") || value.endsWith("/") || value.split("/").length > 64) return false;
  const parts = value.split("/");
  return parts.every(part => part !== "" && part !== "." && part !== "..");
}
function boundedSize(value: unknown, maximum: number = RUNTIME_V2_MAX_PAYLOAD_ARTIFACT_BYTES): value is number { return Number.isSafeInteger(value) && (value as number) >= 0 && (value as number) <= maximum; }
function strictSorted(values: readonly string[]): boolean { return values.every((value, index) => index === 0 || compareRuntimeUtf8V2(values[index - 1]!, value) < 0); }
function canonicalJsonBytes(value: unknown): Buffer { return Buffer.from(`${JSON.stringify(value)}\n`, "utf8"); }

function orderedSupportProfile(profile: RuntimeSupportProfileV2): RuntimeSupportProfileV2 {
  return {
    schema: profile.schema, macosProductVersion: profile.macosProductVersion, macosBuildVersion: profile.macosBuildVersion,
    architecture: profile.architecture, electronVersion: profile.electronVersion, nodeVersion: profile.nodeVersion,
    nodeModuleAbi: profile.nodeModuleAbi, napiVersion: profile.napiVersion,
    osMeasurement: { executablePath: profile.osMeasurement.executablePath, executableSha256: profile.osMeasurement.executableSha256, executableSize: profile.osMeasurement.executableSize },
    sandboxExec: { path: profile.sandboxExec.path, sha256: profile.sandboxExec.sha256, size: profile.sandboxExec.size },
    nativeAdmission: { contract: profile.nativeAdmission.contract, sha256: profile.nativeAdmission.sha256, size: profile.nativeAdmission.size, napiVersion: profile.nativeAdmission.napiVersion },
    supplier: { version: profile.supplier.version, sha256: profile.supplier.sha256, size: profile.supplier.size, appServerProtocolDigest: profile.supplier.appServerProtocolDigest, authorityContract: profile.supplier.authorityContract, identityContract: profile.supplier.identityContract },
    compiler: { outerPolicySchema: profile.compiler.outerPolicySchema, nativePolicyIdentityVersion: profile.compiler.nativePolicyIdentityVersion, sourceDigest: profile.compiler.sourceDigest, parameterSchemaDigest: profile.compiler.parameterSchemaDigest },
    immutableSystemRoots: [...profile.immutableSystemRoots], kernelHelperContractDigest: profile.kernelHelperContractDigest,
    profileDigest: profile.profileDigest
  };
}

function inspectArtifact(value: unknown, expectedPath?: string, maximum: number = RUNTIME_V2_MAX_PAYLOAD_ARTIFACT_BYTES): RuntimeArtifactEntryV2 {
  if (!exactKeys(value, ["relativePath", "size", "sha256"]) || !pathText(value.relativePath) || (expectedPath !== undefined && value.relativePath !== expectedPath) || !boundedSize(value.size, maximum) || !digest(value.sha256)) throw unavailable();
  return value as unknown as RuntimeArtifactEntryV2;
}

function inspectSupportProfile(value: unknown): RuntimeSupportProfileV2 {
  const names = ["schema","macosProductVersion","macosBuildVersion","architecture","electronVersion","nodeVersion","nodeModuleAbi","napiVersion","osMeasurement","sandboxExec","nativeAdmission","supplier","compiler","immutableSystemRoots","kernelHelperContractDigest","profileDigest"];
  if (!exactKeys(value, names) || value.schema !== "chirality-runtime-support-profile/v2" || value.architecture !== "arm64") throw unavailable();
  const profile = value as unknown as RuntimeSupportProfileV2;
  if (!/^\d+(\.\d+){1,2}$/.test(profile.macosProductVersion) || !/^[0-9A-Za-z]+$/.test(profile.macosBuildVersion) || !/^\d+\.\d+\.\d+$/.test(profile.electronVersion) || !/^\d+\.\d+\.\d+$/.test(profile.nodeVersion) || !/^\d+$/.test(profile.nodeModuleAbi) || !/^\d+$/.test(profile.napiVersion)) throw unavailable();
  if (!exactKeys(profile.osMeasurement, ["executablePath","executableSha256","executableSize"]) || profile.osMeasurement.executablePath !== "/usr/bin/sw_vers" || !digest(profile.osMeasurement.executableSha256) || !boundedSize(profile.osMeasurement.executableSize, RUNTIME_V2_MAX_SYSTEM_OR_NATIVE_ARTIFACT_BYTES)) throw unavailable();
  if (!exactKeys(profile.sandboxExec, ["path","sha256","size"]) || profile.sandboxExec.path !== "/usr/bin/sandbox-exec" || !digest(profile.sandboxExec.sha256) || !boundedSize(profile.sandboxExec.size, RUNTIME_V2_MAX_SYSTEM_OR_NATIVE_ARTIFACT_BYTES)) throw unavailable();
  if (!exactKeys(profile.nativeAdmission, ["contract","sha256","size","napiVersion"]) || profile.nativeAdmission.contract !== "chirality-native-admission/v1" || !digest(profile.nativeAdmission.sha256) || !boundedSize(profile.nativeAdmission.size, RUNTIME_V2_MAX_SYSTEM_OR_NATIVE_ARTIFACT_BYTES) || profile.nativeAdmission.napiVersion !== RUNTIME_NATIVE_ADMISSION_NAPI_VERSION_V2 || Number(profile.napiVersion) < Number(RUNTIME_NATIVE_ADMISSION_NAPI_VERSION_V2)) throw unavailable();
  if (!exactKeys(profile.supplier, ["version","sha256","size","appServerProtocolDigest","authorityContract","identityContract"]) || typeof profile.supplier.version !== "string" || profile.supplier.version.length < 1 || profile.supplier.version.length > 128 || !digest(profile.supplier.sha256) || !boundedSize(profile.supplier.size) || !digest(profile.supplier.appServerProtocolDigest) || profile.supplier.authorityContract !== "chirality.local-admission-authority/1.0" || profile.supplier.identityContract !== "chirality-supplier-account-identity/1") throw unavailable();
  if (!exactKeys(profile.compiler, ["outerPolicySchema","nativePolicyIdentityVersion","sourceDigest","parameterSchemaDigest"]) || profile.compiler.outerPolicySchema !== "chirality-codex-outer-policy/v2" || ![10,11].includes(profile.compiler.nativePolicyIdentityVersion) || !digest(profile.compiler.sourceDigest) || !digest(profile.compiler.parameterSchemaDigest)) throw unavailable();
  if (profile.compiler.parameterSchemaDigest !== (profile.compiler.nativePolicyIdentityVersion === 11 ? runtimeStageCPolicyParameterSchemaDigest() : runtimePolicyParameterSchemaDigestV2())) throw unavailable();
  if (!Array.isArray(profile.immutableSystemRoots) || profile.immutableSystemRoots.length < 1 || profile.immutableSystemRoots.length > 64 || !profile.immutableSystemRoots.every(item => typeof item === "string" && isAbsolute(item) && resolve(item) === item) || !strictSorted(profile.immutableSystemRoots) || !digest(profile.kernelHelperContractDigest) || !digest(profile.profileDigest)) throw unavailable();
  const ordered = orderedSupportProfile(profile); const { profileDigest, ...preimage } = ordered;
  if (sha256(canonicalJsonBytes(preimage)) !== profileDigest) throw unavailable();
  return ordered;
}

export function inspectRuntimePayloadManifestV2(value: unknown): Readonly<RuntimePayloadManifestV2> {
  if (!exactKeys(value, ["schema","dependencyResolutionDigest","roots","supportProfiles","entries"]) || value.schema !== "chirality-runtime-payload-manifest/v2" || !digest(value.dependencyResolutionDigest)) throw unavailable();
  const manifest = value as unknown as RuntimePayloadManifestV2;
  if (!Array.isArray(manifest.roots) || manifest.roots.length < 1 || manifest.roots.length > 128 || !manifest.roots.every(pathText) || manifest.roots.some(root => root.includes("/")) || !strictSorted(manifest.roots)) throw unavailable();
  if (!Array.isArray(manifest.supportProfiles) || manifest.supportProfiles.length < 1 || manifest.supportProfiles.length > 8) throw unavailable();
  const profiles = manifest.supportProfiles.map(inspectSupportProfile);
  if (!strictSorted(profiles.map(profile => profile.profileDigest))) throw unavailable();
  if (!Array.isArray(manifest.entries) || manifest.entries.length < 1 || manifest.entries.length > 50_000) throw unavailable();
  const reservedPayloadPaths=["runtime-artifact-inventory.json","runtime-artifact-inventory-v2.json","runtime-payload-manifest.json","runtime-governance"];
  if(manifest.roots.some(root=>reservedPayloadPaths.includes(root)))throw unavailable();
  let aggregate = 0;
  const paths: string[] = [];
  for (const entry of manifest.entries) {
    if (!entry || typeof entry !== "object" || !pathText(entry.relativePath) || reservedPayloadPaths.some(path=>entry.relativePath===path||entry.relativePath.startsWith(`${path}/`))) throw unavailable();
    paths.push(entry.relativePath);
    if (entry.type === "directory") { if (!exactKeys(entry, ["relativePath","type"])) throw unavailable(); }
    else if (entry.type === "file") { if (!exactKeys(entry, ["relativePath","type","size","sha256"]) || !boundedSize(entry.size) || !digest(entry.sha256)) throw unavailable(); aggregate += entry.size; if (aggregate > 4_294_967_296) throw unavailable(); }
    else throw unavailable();
  }
  if (!strictSorted(paths)) throw unavailable();
  const entryTypes = new Map(manifest.entries.map(entry => [entry.relativePath, entry.type]));
  const topLevel = [...new Set(manifest.entries.map(entry => entry.relativePath.split("/")[0]!))].sort(compareRuntimeUtf8V2);
  if (manifest.roots.length !== topLevel.length || manifest.roots.some((root,index) => root !== topLevel[index]) || manifest.roots.some(root => !entryTypes.has(root))) throw unavailable();
  for (const entry of manifest.entries) {
    const parts = entry.relativePath.split("/");
    for (let index=1; index<parts.length; index++) if (entryTypes.get(parts.slice(0,index).join("/")) !== "directory") throw unavailable();
  }
  const requiredRoots = ["app.asar","instruction-root","native","runtime-cli","runtime-contracts","supplier"];
  if (requiredRoots.some(root => !manifest.roots.includes(root))) throw unavailable();
  const requiredFiles = ["app.asar","instruction-root/instruction-bundle-manifest.json","native/chirality_native_admission.node","runtime-cli/chirality-cli.mjs","runtime-cli/chirality-cli.mjs.map","runtime-contracts/runtime-policy-parameters-v2.json","supplier/codex"];
  for (const required of requiredFiles) if (!manifest.entries.some(entry => entry.relativePath === required && entry.type === "file")) throw unavailable();
  return Object.freeze({
    schema: manifest.schema,
    dependencyResolutionDigest: manifest.dependencyResolutionDigest,
    roots: Object.freeze([...manifest.roots]),
    supportProfiles: Object.freeze(profiles.map(profile => Object.freeze(orderedSupportProfile(profile)))),
    entries: Object.freeze(manifest.entries.map(entry => Object.freeze(entry.type === "directory" ? { relativePath: entry.relativePath, type: entry.type } : { relativePath: entry.relativePath, type: entry.type, size: entry.size, sha256: entry.sha256 })))
  });
}

export function encodeRuntimePayloadManifestV2(value: RuntimePayloadManifestV2): Buffer {
  const inspected = inspectRuntimePayloadManifestV2(value);
  const bytes = canonicalJsonBytes(inspected);
  if (bytes.length > 16_777_216) throw unavailable();
  return bytes;
}
export function decodeRuntimePayloadManifestV2(bytes: Uint8Array): Readonly<RuntimePayloadManifestV2> {
  const buffer = Buffer.from(bytes);
  if (buffer.length < 2 || buffer.length > 16_777_216 || buffer[buffer.length - 1] !== 0x0a || buffer.subarray(0, -1).includes(0x0a) || buffer[0] === 0xef) throw unavailable();
  const parsed = inspectRuntimePayloadManifestV2(JSON.parse(buffer.toString("utf8")));
  if (!encodeRuntimePayloadManifestV2(parsed).equals(buffer)) throw unavailable();
  return parsed;
}

export function inspectRuntimeArtifactInventoryV2(value: unknown): Readonly<RuntimeArtifactInventoryV2> {
  if (!exactKeys(value, ["schema","payloadManifest","governance"]) || value.schema !== "chirality-runtime-artifact-inventory/v2" || !Array.isArray(value.governance) || value.governance.length !== 6) throw unavailable();
  inspectArtifact(value.payloadManifest, "runtime-payload-manifest.json", 16_777_216);
  const paths = ["runtime-governance/v2/login-purpose-record.json","runtime-governance/v2/login-purpose-acceptance.json","runtime-governance/v2/login-owner-act","runtime-governance/v2/worker-purpose-record.json","runtime-governance/v2/worker-purpose-acceptance.json","runtime-governance/v2/worker-owner-act"];
  value.governance.forEach((entry, index) => inspectArtifact(entry, paths[index], 1_048_576));
  const inventory = value as unknown as RuntimeArtifactInventoryV2;
  return Object.freeze({ schema: inventory.schema, payloadManifest: Object.freeze({ relativePath: inventory.payloadManifest.relativePath, size: inventory.payloadManifest.size, sha256: inventory.payloadManifest.sha256 }), governance: Object.freeze(inventory.governance.map(entry => Object.freeze({ relativePath: entry.relativePath, size: entry.size, sha256: entry.sha256 }))) as unknown as RuntimeArtifactInventoryV2["governance"] });
}
export function encodeRuntimeArtifactInventoryV2(value: RuntimeArtifactInventoryV2): Buffer {
  const bytes = canonicalJsonBytes(inspectRuntimeArtifactInventoryV2(value));
  if (bytes.length > 16_777_216) throw unavailable();
  return bytes;
}
export function decodeRuntimeArtifactInventoryV2(bytes: Uint8Array): Readonly<RuntimeArtifactInventoryV2> {
  const buffer = Buffer.from(bytes);
  if (buffer.length < 2 || buffer.length > 16_777_216 || buffer[buffer.length - 1] !== 0x0a || buffer.subarray(0, -1).includes(0x0a) || buffer[0] === 0xef) throw unavailable();
  const parsed = inspectRuntimeArtifactInventoryV2(JSON.parse(buffer.toString("utf8")));
  if (!encodeRuntimeArtifactInventoryV2(parsed).equals(buffer)) throw unavailable();
  return parsed;
}
export function encodeRuntimePolicyParameterDeclarationV2(): Buffer { return canonicalJsonBytes(RUNTIME_POLICY_PARAMETER_DECLARATION_V2); }
export function runtimePolicyParameterSchemaDigestV2(): RuntimeSha256V2 { return sha256(canonicalJsonBytes({ schema: "chirality-runtime-policy-parameters/v2", contractEntry: "runtime-contracts/runtime-policy-parameters-v2.json", contractEntrySha256: sha256(encodeRuntimePolicyParameterDeclarationV2()) })); }

export const RUNTIME_V2_REQUIRED_PAYLOAD_ROOTS = Object.freeze(["app.asar","instruction-root","native","runtime-cli","runtime-contracts","supplier"] as const);
export const RUNTIME_V2_REQUIRED_PAYLOAD_FILES = Object.freeze(["app.asar","instruction-root/instruction-bundle-manifest.json","native/chirality_native_admission.node","runtime-cli/chirality-cli.mjs","runtime-cli/chirality-cli.mjs.map","runtime-contracts/runtime-policy-parameters-v2.json","supplier/codex"] as const);

export interface VerifiedPackagedRuntimeBasisV2 {
  resourcesRoot: string;
  inventoryPath: string;
  payloadManifestPath: string;
  inventorySha256: RuntimeSha256V2;
  payloadDigest: RuntimeSha256V2;
  payload: Readonly<RuntimePayloadManifestV2>;
  inventory: Readonly<RuntimeArtifactInventoryV2>;
}

export interface EmbeddedRuntimeVersionsV2 { electron: string; node: string; modules: string; napi: string; architecture: string }
export interface RuntimeSupportObservationInputV2 {
  embeddedRuntime: EmbeddedRuntimeVersionsV2;
  basis: VerifiedPackagedRuntimeBasisV2;
  supplierVersion: string;
  appServerProtocolDigest: RuntimeSha256V2;
  immutableSystemRoots: readonly string[];
  /** Compiler-owned selection; omission preserves historical native-10 observation. */
  nativePolicyIdentityVersion?: 10 | 11;
}
export interface RuntimePayloadSupportObservationInputV2 extends Omit<RuntimeSupportObservationInputV2, "basis"> {
  resourcesRoot: string;
  payloadEntries: readonly RuntimePayloadEntryV2[];
}

interface StableRuntimeFileV2 { size: number; sha256: string; identity: string }
interface StableRuntimeDocumentV2 extends StableRuntimeFileV2 { bytes: Buffer }
async function stableFile(path: string, maximum: number, signal: AbortSignal | undefined, retainBytes: true): Promise<StableRuntimeDocumentV2>;
async function stableFile(path: string, maximum: number, signal?: AbortSignal, retainBytes?: false): Promise<StableRuntimeFileV2>;
async function stableFile(path: string, maximum: number, signal?: AbortSignal, retainBytes = false): Promise<StableRuntimeFileV2 | StableRuntimeDocumentV2> {
  signal?.throwIfAborted();
  if (!isAbsolute(path) || resolve(path) !== path || await realpath(path) !== path) throw unavailable();
  const handle = await open(path, constants.O_RDONLY | constants.O_NOFOLLOW | constants.O_NONBLOCK);
  try {
    const before = await handle.stat({ bigint: true });
    if (!before.isFile() || before.nlink !== 1n || before.size > BigInt(maximum)) throw unavailable();
    const parts:Buffer[]=[];const digest=createHash("sha256");let total=0,position=0;const buffer=Buffer.alloc(65_536);
    for(;;){signal?.throwIfAborted();const {bytesRead}=await handle.read(buffer,0,Math.min(buffer.length,Number(before.size)+1-total),position);if(bytesRead===0)break;total+=bytesRead;position+=bytesRead;if(total>Number(before.size)||total>maximum)throw unavailable();const chunk=buffer.subarray(0,bytesRead);digest.update(chunk);if(retainBytes)parts.push(Buffer.from(chunk));}
    const after = await handle.stat({ bigint: true }); const current = await lstat(path, { bigint: true });
    for (const key of ["dev","ino","size","mtimeNs","ctimeNs"] as const) if (before[key] !== after[key] || before[key] !== current[key]) throw unavailable();
    if (total !== Number(before.size) || await realpath(path) !== path) throw unavailable();
    const identity=JSON.stringify([before.dev,before.ino,before.size,before.mtimeNs,before.ctimeNs,before.mode,before.uid,before.nlink].map(String));
    const observed={size:total,sha256:digest.digest("hex"),identity};
    return retainBytes ? {...observed,bytes:Buffer.concat(parts,total)} : observed;
  } finally { await handle.close(); }
}

async function stableDirectory(path:string):Promise<string>{
  if(!isAbsolute(path)||resolve(path)!==path||await realpath(path)!==path)throw unavailable();const info=await lstat(path,{bigint:true});if(!info.isDirectory()||info.isSymbolicLink())throw unavailable();
  return JSON.stringify([info.dev,info.ino,info.size,info.mtimeNs,info.ctimeNs,info.mode,info.uid,info.nlink].map(String));
}

async function walk(root: string, base: string, output: string[], signal?: AbortSignal): Promise<void> {
  signal?.throwIfAborted();
  if (output.length > 50_010 || await realpath(root) !== root) throw unavailable();
  const info = await lstat(root);
  if (info.isSymbolicLink() || (info.isFile() && info.nlink !== 1) || (!info.isDirectory() && !info.isFile())) throw unavailable();
  const rel = relative(base, root).split(sep).join("/"); if (rel) output.push(rel);
  if (info.isDirectory()) for (const name of (await readdir(root)).sort(compareRuntimeUtf8V2)) await walk(join(root, name), base, output, signal);
}

export async function verifyPackagedRuntimeBasisV2(input: { resourcesRoot: string; signal?: AbortSignal }): Promise<Readonly<VerifiedPackagedRuntimeBasisV2>> {
  try {
    const resourcesRoot = await realpath(input.resourcesRoot);
    if (resourcesRoot !== input.resourcesRoot || !(await lstat(resourcesRoot)).isDirectory()) throw unavailable();
    const resourcesIdentity=await stableDirectory(resourcesRoot);
    const inventoryPath = join(resourcesRoot, "runtime-artifact-inventory-v2.json");
    const payloadManifestPath = join(resourcesRoot, "runtime-payload-manifest.json");
    const inventorySource = await stableFile(inventoryPath, 16_777_216, input.signal, true);
    const inventory = decodeRuntimeArtifactInventoryV2(inventorySource.bytes);
    const payloadSource = await stableFile(payloadManifestPath, 16_777_216, input.signal, true);
    if (payloadSource.sha256 !== inventory.payloadManifest.sha256 || payloadSource.size !== inventory.payloadManifest.size) throw unavailable();
    const payload = decodeRuntimePayloadManifestV2(payloadSource.bytes);
    const byPath = new Map(payload.entries.filter((entry): entry is Extract<RuntimePayloadEntryV2,{type:"file"}> => entry.type === "file").map(entry => [entry.relativePath, entry]));
    const governanceDirectoryObservations=new Map<string,string>();for(const path of ["runtime-governance","runtime-governance/v2"])governanceDirectoryObservations.set(path,await stableDirectory(join(resourcesRoot,path)));
    const governanceObservations=new Map<string,string>();
    for (const entry of inventory.governance) { const current = await stableFile(join(resourcesRoot, entry.relativePath), 1_048_576, input.signal); if (current.size !== entry.size || current.sha256 !== entry.sha256) throw unavailable();governanceObservations.set(entry.relativePath,current.identity); }
    const observations=new Map<string,string>();
    for (const entry of payload.entries) {
      const path = join(resourcesRoot, entry.relativePath);
      if (entry.type === "directory") observations.set(entry.relativePath,await stableDirectory(path));
      else { const current = await stableFile(path, RUNTIME_V2_MAX_PAYLOAD_ARTIFACT_BYTES, input.signal); if (current.size !== entry.size || current.sha256 !== entry.sha256) throw unavailable();observations.set(entry.relativePath,current.identity); }
    }
    const seen: string[] = []; await walk(resourcesRoot, resourcesRoot, seen, input.signal);
    const expected = [...payload.entries.map(entry => entry.relativePath), "runtime-payload-manifest.json", "runtime-governance", "runtime-governance/v2", ...inventory.governance.map(entry => entry.relativePath), "runtime-artifact-inventory-v2.json"].sort(compareRuntimeUtf8V2);
    if (seen.length !== expected.length || seen.some((path, index) => path !== expected[index])) throw unavailable();
    if (byPath.get("runtime-contracts/runtime-policy-parameters-v2.json")?.sha256 !== sha256(encodeRuntimePolicyParameterDeclarationV2())) throw unavailable();
    for(const entry of payload.entries){const path=join(resourcesRoot,entry.relativePath),identity=entry.type==="directory"?await stableDirectory(path):(await stableFile(path,RUNTIME_V2_MAX_PAYLOAD_ARTIFACT_BYTES,input.signal)).identity;if(identity!==observations.get(entry.relativePath))throw unavailable();}
    for(const entry of inventory.governance){const current=await stableFile(join(resourcesRoot,entry.relativePath),1_048_576,input.signal);if(current.size!==entry.size||current.sha256!==entry.sha256||current.identity!==governanceObservations.get(entry.relativePath))throw unavailable();}
    for(const [path,identity] of governanceDirectoryObservations)if(await stableDirectory(join(resourcesRoot,path))!==identity)throw unavailable();
    const finalInventory = await stableFile(inventoryPath, 16_777_216, input.signal); const finalPayload = await stableFile(payloadManifestPath, 16_777_216, input.signal);
    if (finalInventory.sha256 !== inventorySource.sha256 || finalPayload.sha256 !== payloadSource.sha256) throw unavailable();
    if(await stableDirectory(resourcesRoot)!==resourcesIdentity)throw unavailable();
    return Object.freeze({ resourcesRoot, inventoryPath, payloadManifestPath, inventorySha256: inventorySource.sha256, payloadDigest: payloadSource.sha256, payload, inventory });
  } catch { throw unavailable(); }
}

function runSwVers(argument: "-productVersion" | "-buildVersion", signal?: AbortSignal): Promise<string> {
  return new Promise((resolveValue, rejectValue) => {
    const child = execFile("/usr/bin/sw_vers", [argument], { shell: false, timeout: 2_000, maxBuffer: 128, encoding: "utf8", env: { PATH: "/usr/bin:/bin", LANG: "C" }, signal }, (error, stdout, stderr) => {
      if (error || stderr !== "" || Buffer.byteLength(stdout, "ascii") > 128 || !stdout.endsWith("\n") || stdout.slice(0, -1).includes("\n")) rejectValue(unavailable());
      else resolveValue(stdout.slice(0, -1));
    });
    child.stdin?.end();
  });
}

/** Pre-governance Electron-main observation over Packaging's frozen payload snapshot. This creates no qualification or acceptance. */
export async function observeRuntimeSupportProfileFromPayloadV2(input: RuntimePayloadSupportObservationInputV2, signal?: AbortSignal): Promise<Readonly<RuntimeSupportProfileV2>> {
  try {
    const live={electron:process.versions.electron,node:process.versions.node,modules:process.versions.modules,napi:process.versions.napi,architecture:process.arch};
    if (process.platform !== "darwin" || live.architecture !== "arm64" || !live.electron || !live.node || !live.modules || !live.napi || Object.entries(live).some(([key,value])=>input.embeddedRuntime[key as keyof EmbeddedRuntimeVersionsV2]!==value)) throw unavailable();
    if (!isAbsolute(input.resourcesRoot) || resolve(input.resourcesRoot) !== input.resourcesRoot || await realpath(input.resourcesRoot) !== input.resourcesRoot
      || !Array.isArray(input.payloadEntries) || input.payloadEntries.length < 1 || input.payloadEntries.length > 50_000) throw unavailable();
    const resourcesIdentity=await stableDirectory(input.resourcesRoot);
    const paths=input.payloadEntries.map(entry=>entry.relativePath);
    if(!strictSorted(paths)||new Set(paths).size!==paths.length)throw unavailable();
    for(const entry of input.payloadEntries){if(!entry||typeof entry!=="object"||!pathText(entry.relativePath)||(entry.type==="directory"?!exactKeys(entry,["relativePath","type"]):entry.type!=="file"||!exactKeys(entry,["relativePath","type","size","sha256"])||!boundedSize(entry.size)||!digest(entry.sha256)))throw unavailable();}
    const payload = new Map(input.payloadEntries.filter((entry): entry is Extract<RuntimePayloadEntryV2,{type:"file"}> => entry.type === "file").map(entry => [entry.relativePath, entry]));
    const nativeEntry = payload.get("native/chirality_native_admission.node"), supplierEntry = payload.get("supplier/codex");
    const appEntry = payload.get("app.asar"), cliEntry = payload.get("runtime-cli/chirality-cli.mjs"), cliMapEntry = payload.get("runtime-cli/chirality-cli.mjs.map");
    if (!nativeEntry || !supplierEntry || !appEntry || !cliEntry || !cliMapEntry || !digest(input.appServerProtocolDigest) || !/^\d+\.\d+\.\d+$/.test(input.supplierVersion)) throw unavailable();
    const [sw, sandbox, nativeFile, supplierFile, appFile, cliFile, cliMapFile, productVersion, buildVersion] = await Promise.all([
      stableFile("/usr/bin/sw_vers", RUNTIME_V2_MAX_SYSTEM_OR_NATIVE_ARTIFACT_BYTES, signal), stableFile("/usr/bin/sandbox-exec", RUNTIME_V2_MAX_SYSTEM_OR_NATIVE_ARTIFACT_BYTES, signal),
      stableFile(join(input.resourcesRoot, nativeEntry.relativePath), RUNTIME_V2_MAX_SYSTEM_OR_NATIVE_ARTIFACT_BYTES, signal), stableFile(join(input.resourcesRoot, supplierEntry.relativePath), RUNTIME_V2_MAX_PAYLOAD_ARTIFACT_BYTES, signal),
      stableFile(join(input.resourcesRoot, appEntry.relativePath), RUNTIME_V2_MAX_PAYLOAD_ARTIFACT_BYTES, signal), stableFile(join(input.resourcesRoot, cliEntry.relativePath), RUNTIME_V2_MAX_PAYLOAD_ARTIFACT_BYTES, signal), stableFile(join(input.resourcesRoot, cliMapEntry.relativePath), RUNTIME_V2_MAX_PAYLOAD_ARTIFACT_BYTES, signal),
      runSwVers("-productVersion", signal), runSwVers("-buildVersion", signal)
    ]);
    for(const [observed,entry] of [[nativeFile,nativeEntry],[supplierFile,supplierEntry],[appFile,appEntry],[cliFile,cliEntry],[cliMapFile,cliMapEntry]] as const)if(observed.sha256!==entry.sha256||observed.size!==entry.size)throw unavailable();
    if (!/^\d+(\.\d+){1,2}$/.test(productVersion) || !/^[0-9A-Za-z]+$/.test(buildVersion)) throw unavailable();
    if (!Array.isArray(input.immutableSystemRoots) || input.immutableSystemRoots.length < 1 || input.immutableSystemRoots.length > 64 || !strictSorted(input.immutableSystemRoots)) throw unavailable();
    const nativePolicyIdentityVersion = input.nativePolicyIdentityVersion ?? 10;
    const compilerSource = sha256(canonicalJsonBytes({ schema: "chirality-runtime-compiler-source/v2", compilerArtifacts: [appEntry, cliEntry, cliMapEntry], outerPolicySchema: "chirality-codex-outer-policy/v2", nativePolicyIdentityVersion }));
    const kernelHelper = sha256(canonicalJsonBytes({ schema: "chirality-runtime-kernel-helper-contract/v2", sandboxExecSha256: sandbox.sha256, nativeAdmissionSha256: nativeFile.sha256, nativeAdmissionContract: "chirality-native-admission/v1", groupedSpawn: true, processGroup: true, authoritySecretFd: 3, closeOnExecExceptAuthorityFd: true, leaderObservation: "waitid-pid-wnowait", exactLeaderReap: true, postReapGroupAbsence: true }));
    const finalFiles=await Promise.all([stableFile("/usr/bin/sw_vers",RUNTIME_V2_MAX_SYSTEM_OR_NATIVE_ARTIFACT_BYTES,signal),stableFile("/usr/bin/sandbox-exec",RUNTIME_V2_MAX_SYSTEM_OR_NATIVE_ARTIFACT_BYTES,signal),stableFile(join(input.resourcesRoot,nativeEntry.relativePath),RUNTIME_V2_MAX_SYSTEM_OR_NATIVE_ARTIFACT_BYTES,signal),stableFile(join(input.resourcesRoot,supplierEntry.relativePath),RUNTIME_V2_MAX_PAYLOAD_ARTIFACT_BYTES,signal),stableFile(join(input.resourcesRoot,appEntry.relativePath),RUNTIME_V2_MAX_PAYLOAD_ARTIFACT_BYTES,signal),stableFile(join(input.resourcesRoot,cliEntry.relativePath),RUNTIME_V2_MAX_PAYLOAD_ARTIFACT_BYTES,signal),stableFile(join(input.resourcesRoot,cliMapEntry.relativePath),RUNTIME_V2_MAX_PAYLOAD_ARTIFACT_BYTES,signal)]);
    for(const [before,after] of [[sw,finalFiles[0]!],[sandbox,finalFiles[1]!],[nativeFile,finalFiles[2]!],[supplierFile,finalFiles[3]!],[appFile,finalFiles[4]!],[cliFile,finalFiles[5]!],[cliMapFile,finalFiles[6]!]] as const)if(before.identity!==after.identity||before.sha256!==after.sha256||before.size!==after.size)throw unavailable();
    if(await stableDirectory(input.resourcesRoot)!==resourcesIdentity)throw unavailable();
    const withoutDigest = {
      schema: "chirality-runtime-support-profile/v2" as const, macosProductVersion: productVersion, macosBuildVersion: buildVersion, architecture: "arm64" as const,
      electronVersion: input.embeddedRuntime.electron, nodeVersion: input.embeddedRuntime.node, nodeModuleAbi: input.embeddedRuntime.modules, napiVersion: input.embeddedRuntime.napi,
      osMeasurement: { executablePath: "/usr/bin/sw_vers" as const, executableSha256: sw.sha256, executableSize: sw.size }, sandboxExec: { path: "/usr/bin/sandbox-exec" as const, sha256: sandbox.sha256, size: sandbox.size },
      nativeAdmission: { contract: "chirality-native-admission/v1" as const, sha256: nativeFile.sha256, size: nativeFile.size, napiVersion: RUNTIME_NATIVE_ADMISSION_NAPI_VERSION_V2 },
      supplier: { version: input.supplierVersion, sha256: supplierFile.sha256, size: supplierFile.size, appServerProtocolDigest: input.appServerProtocolDigest, authorityContract: "chirality.local-admission-authority/1.0" as const, identityContract: "chirality-supplier-account-identity/1" as const },
      compiler: { outerPolicySchema: "chirality-codex-outer-policy/v2" as const, nativePolicyIdentityVersion, sourceDigest: compilerSource, parameterSchemaDigest: nativePolicyIdentityVersion === 11 ? runtimeStageCPolicyParameterSchemaDigest() : runtimePolicyParameterSchemaDigestV2() },
      immutableSystemRoots: [...input.immutableSystemRoots], kernelHelperContractDigest: kernelHelper
    };
    const profile = { ...withoutDigest, profileDigest: sha256(canonicalJsonBytes(withoutDigest)) };
    return Object.freeze(inspectSupportProfile(profile));
  } catch { throw unavailable(); }
}

/** Full accepted-basis observation retained unchanged; it delegates to the same pre-governance derivation. */
export function observeRuntimeSupportProfileV2(input: RuntimeSupportObservationInputV2, signal?: AbortSignal): Promise<Readonly<RuntimeSupportProfileV2>> {
  return observeRuntimeSupportProfileFromPayloadV2({ embeddedRuntime: input.embeddedRuntime, resourcesRoot: input.basis.resourcesRoot,
    payloadEntries: input.basis.payload.entries, supplierVersion: input.supplierVersion, appServerProtocolDigest: input.appServerProtocolDigest,
    immutableSystemRoots: input.immutableSystemRoots, ...(input.nativePolicyIdentityVersion === undefined ? {} : { nativePolicyIdentityVersion: input.nativePolicyIdentityVersion }) }, signal);
}

export function matchRuntimeSupportProfileV2(observed: RuntimeSupportProfileV2, accepted: readonly RuntimeSupportProfileV2[]): Readonly<RuntimeSupportProfileV2> {
  const checked = inspectSupportProfile(observed);
  if (!Array.isArray(accepted) || accepted.length < 1 || accepted.length > 8) throw unavailable();
  const profiles = accepted.map(inspectSupportProfile);
  if (!strictSorted(profiles.map(profile => profile.profileDigest))) throw unavailable();
  const match = profiles.find(profile => profile.profileDigest === checked.profileDigest);
  if (!match || !canonicalJsonBytes(match).equals(canonicalJsonBytes(checked))) throw unavailable();
  return Object.freeze(match);
}
