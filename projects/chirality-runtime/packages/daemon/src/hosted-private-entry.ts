import { RuntimeError } from "@chirality/runtime-contracts";
import { constants, type BigIntStats } from "node:fs";
import { lstat, open, realpath } from "node:fs/promises";
import { isAbsolute, resolve } from "node:path";
import type { RuntimeConformanceArtifactInventorySelection } from "@chirality/runtime-core";
import {
  startHostedBootstrapRuntimeHost,
  type HostedBootstrapRuntimeBootInput,
  type HostedBootstrapRuntimeHost,
  type HostedBootstrapPrivateBindings
} from "./hosted-bootstrap.js";
import type { RuntimeDaemonLogger } from "./runtime-daemon.js";
import { createHostedBootstrapPrivateBindings, validateHostedPrivateCompositionOptions, type HostedPrivateCompositionOptions } from "./hosted-private-composition.js";

type BootstrapEnabled = Extract<HostedBootstrapRuntimeBootInput, { enabled: true }>;

export type HostedPrivateBootstrapHostInput = {
  bootstrap: BootstrapEnabled;
  /** Absence deliberately starts the usable, unbound bootstrap surface. */
  privateComposition?: HostedPrivateCompositionOptions;
  /** Host diagnostic sink for hosted-account failures and ceremony retirement diagnostics; absent means discarded. */
  logger?: RuntimeDaemonLogger;
};

export interface HostedPrivateBootstrapConfigurationReadInput {
  configFile?: string;
  bootstrap: BootstrapEnabled;
  packaged: {
    supplierExecutablePath: string;
    nativeAddonPath: string;
    instructionRoot: string;
    artifactInventory: RuntimeConformanceArtifactInventorySelection;
  };
}

interface HostedPrivateEntryAdapters {
  createBindings(options: HostedPrivateCompositionOptions): Promise<HostedBootstrapPrivateBindings>;
  startHost(input: BootstrapEnabled, bindings?: HostedBootstrapPrivateBindings, logger?: RuntimeDaemonLogger): Promise<HostedBootstrapRuntimeHost>;
}

const productionAdapters: HostedPrivateEntryAdapters = Object.freeze({
  createBindings: createHostedBootstrapPrivateBindings,
  startHost: startHostedBootstrapRuntimeHost
});

function unavailable(reason: string): RuntimeError {
  return new RuntimeError("ENGINE_UNAVAILABLE", "Trusted hosted private Runtime configuration is unavailable", 503, { reason });
}

function sameFileIdentity(left: BigIntStats, right: BigIntStats): boolean {
  return left.dev === right.dev && left.ino === right.ino && left.size === right.size
    && left.mode === right.mode && left.uid === right.uid && left.nlink === right.nlink
    && left.mtimeNs === right.mtimeNs && left.ctimeNs === right.ctimeNs;
}

function safePrivateConfigStat(value: BigIntStats): boolean {
  const owner = process.getuid?.();
  return owner !== undefined && value.isFile() && !value.isSymbolicLink()
    && value.uid === BigInt(owner) && (value.mode & 0o777n) === 0o600n
    && value.nlink === 1n && value.size >= 2n && value.size <= 262_144n;
}

function sameInventory(left: RuntimeConformanceArtifactInventorySelection, right: RuntimeConformanceArtifactInventorySelection): boolean {
  if (left.kind !== right.kind) return false;
  if (left.kind === "source-tree" && right.kind === "source-tree") {
    const keys = "kind\0sourceRoot";
    return Object.keys(left).sort().join("\0") === keys && Object.keys(right).sort().join("\0") === keys
      && left.sourceRoot === right.sourceRoot;
  }
  if (left.kind === "packaged-resources" && right.kind === "packaged-resources") {
    const keys = "kind\0manifestPath\0resourcesRoot";
    return Object.keys(left).sort().join("\0") === keys && Object.keys(right).sort().join("\0") === keys
      && left.resourcesRoot === right.resourcesRoot && left.manifestPath === right.manifestPath;
  }
  return false;
}

/** Reads the sole owner-private server configuration carrier. No path means an unbound bootstrap; an explicit invalid carrier never falls back. */
export async function readHostedPrivateBootstrapConfiguration(input: HostedPrivateBootstrapConfigurationReadInput): Promise<HostedPrivateBootstrapHostInput> {
  if (!input || input.bootstrap?.enabled !== true || !input.packaged) throw unavailable("PRIVATE_CONFIG_READ_INPUT_INVALID");
  if (input.configFile === undefined) return Object.freeze({ bootstrap: structuredClone(input.bootstrap) });
  const path = input.configFile;
  if (path.trim() === "" || !isAbsolute(path) || resolve(path) !== path || /[\x00-\x1f]/.test(path)) throw unavailable("PRIVATE_CONFIG_FILE_UNSAFE");
  let handle: Awaited<ReturnType<typeof open>> | undefined;
  try {
    const pathInfo = await lstat(path, { bigint: true });
    if (!safePrivateConfigStat(pathInfo) || await realpath(path) !== path) throw unavailable("PRIVATE_CONFIG_FILE_UNSAFE");
    handle = await open(path, constants.O_RDONLY | constants.O_NOFOLLOW);
    const before = await handle.stat({ bigint: true });
    if (!safePrivateConfigStat(before) || !sameFileIdentity(pathInfo, before)) throw unavailable("PRIVATE_CONFIG_FILE_CHANGED");
    const expectedSize = Number(before.size);
    const bytes = Buffer.allocUnsafe(expectedSize + 1);
    let bytesRead = 0;
    while (bytesRead < bytes.length) {
      const chunk = await handle.read(bytes, bytesRead, bytes.length - bytesRead, bytesRead);
      if (chunk.bytesRead === 0) break;
      bytesRead += chunk.bytesRead;
    }
    const after = await handle.stat({ bigint: true });
    const finalPathInfo = await lstat(path, { bigint: true });
    if (bytesRead !== expectedSize || !safePrivateConfigStat(after) || !sameFileIdentity(before, after)
      || !sameFileIdentity(after, finalPathInfo) || await realpath(path) !== path) throw unavailable("PRIVATE_CONFIG_FILE_CHANGED");
    const source = bytes.subarray(0, bytesRead).toString("utf8");
    let parsed: unknown; try { parsed = JSON.parse(source); } catch { throw unavailable("PRIVATE_CONFIG_FILE_INVALID"); }
    if (!parsed || typeof parsed !== "object" || Array.isArray(parsed) || Object.keys(parsed as Record<string, unknown>).sort().join("\0") !== "privateComposition\0schema") throw unavailable("PRIVATE_CONFIG_FILE_INVALID");
    const record = parsed as { schema?: unknown; privateComposition?: unknown };
    if (record.schema !== "chirality.hosted-private-runtime/v1") throw unavailable("PRIVATE_CONFIG_FILE_INVALID");
    const privateComposition = validateHostedPrivateCompositionOptions(record.privateComposition);
    if (privateComposition.releaseV2 !== undefined || !privateComposition.conformance || !privateComposition.loginPurposeRelease) throw unavailable("PRIVATE_CONFIG_FILE_INVALID");
    const packaged = input.packaged;
    if (privateComposition.supplierExecutablePath !== packaged.supplierExecutablePath || privateComposition.nativeAddonPath !== packaged.nativeAddonPath
      || privateComposition.instructionRoot !== packaged.instructionRoot || !sameInventory(privateComposition.conformance.artifactInventory, packaged.artifactInventory)
      || !sameInventory(privateComposition.loginPurposeRelease.artifactInventory, packaged.artifactInventory)) throw unavailable("PRIVATE_CONFIG_PACKAGED_BASIS_MISMATCH");
    return Object.freeze({ bootstrap: structuredClone(input.bootstrap), privateComposition });
  } catch (error) {
    if (error instanceof RuntimeError) throw error;
    throw unavailable("PRIVATE_CONFIG_FILE_UNREADABLE");
  } finally { await handle?.close(); }
}

async function compose(input: HostedPrivateBootstrapHostInput, adapters: HostedPrivateEntryAdapters): Promise<HostedBootstrapRuntimeHost> {
  if (!input || input.bootstrap?.enabled !== true) throw unavailable("BOOTSTRAP_CONFIGURATION_MISSING");
  const trusted = input.privateComposition;
  // The logger argument is only passed when supplied so adapters keep their historical call shape otherwise.
  const logger = input.logger;
  if (trusted === undefined) return logger === undefined ? adapters.startHost(input.bootstrap) : adapters.startHost(input.bootstrap, undefined, logger);
  if (input.bootstrap.runtimeDirectory !== trusted.runtimeDirectory || input.bootstrap.instructionRoot !== trusted.instructionRoot
    || input.bootstrap.nativeAddonPath !== trusted.nativeAddonPath) throw unavailable("BOOTSTRAP_PRIVATE_CONFIGURATION_MISMATCH");
  if (trusted.releaseV2 === undefined) {
    if (!trusted.conformance || !trusted.loginPurposeRelease || input.bootstrap.artifactInventory === undefined
      || !sameInventory(input.bootstrap.artifactInventory, trusted.conformance.artifactInventory)) throw unavailable("BOOTSTRAP_PRIVATE_CONFIGURATION_MISMATCH");
  } else if (trusted.conformance !== undefined || trusted.loginPurposeRelease !== undefined || input.bootstrap.artifactInventory !== undefined) {
    throw unavailable("BOOTSTRAP_PRIVATE_CONFIGURATION_MISMATCH");
  }
  const bindings = await adapters.createBindings(trusted);
  try { return logger === undefined ? await adapters.startHost(input.bootstrap, bindings) : await adapters.startHost(input.bootstrap, bindings, logger); }
  catch (error) {
    try { await bindings.close?.(); }
    catch (cleanupError) { throw new AggregateError([error, cleanupError], "Hosted private bootstrap startup and cleanup failed"); }
    throw error;
  }
}

/** Concrete production entry: callers provide trusted values, never supplier callbacks. */
export function startHostedPrivateBootstrapRuntimeHost(input: HostedPrivateBootstrapHostInput): Promise<HostedBootstrapRuntimeHost> {
  return compose(input, productionAdapters);
}

/** Controlled entry wiring seam; it conveys no native, supplier, or conformance qualification. */
export function startControlledHostedPrivateBootstrapRuntimeHostForTests(input: HostedPrivateBootstrapHostInput, adapters: HostedPrivateEntryAdapters): Promise<HostedBootstrapRuntimeHost> {
  return compose(input, Object.freeze({ ...adapters }));
}
