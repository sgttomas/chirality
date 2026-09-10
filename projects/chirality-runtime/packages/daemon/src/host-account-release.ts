import { createHash } from "node:crypto";
import { execFile } from "node:child_process";
import { open, readFile, realpath } from "node:fs/promises";
import { dirname, isAbsolute, join, resolve } from "node:path";
import { promisify } from "node:util";
import { RuntimeError } from "@chirality/runtime-contracts";
import type { AuthRegistry } from "@chirality/runtime-core";
import { loadNativeAdmissionBinding } from "@chirality/native-admission";
import { assertIssuedPackagedReleaseBasisV2, revalidateIssuedPackagedReleaseBasisV2, type HostedPackagedReleaseBasisV2 } from "./hosted-packaged-release-state.js";
import { HostAccountAuthority } from "./host-account-authority.js";
import { createHostAccountClient, type HostAccountClient } from "./host-account-client.js";
import {
  HOST_ACCOUNT_SIGNING_PREDICATE_RESOURCE,
  loadHostAccountSigningPredicate
} from "./host-account-protocol.js";

const execute = promisify(execFile);
const FUSE_SENTINEL = Buffer.from("dL7pKGdnNz796PbbjQWNKmHXBZaB9tsX", "ascii");

function unavailable(reason: string): RuntimeError {
  return new RuntimeError("ENGINE_UNAVAILABLE", "Verified App account host is unavailable", 503, { reason });
}

async function run(executable: string, args: readonly string[]): Promise<{ stdout: string; stderr: string }> {
  try {
    return await execute(executable, [...args], {
      shell: false, timeout: 5_000, maxBuffer: 1024 * 1024, encoding: "utf8",
      env: { PATH: "/usr/bin:/bin", LANG: "C" }
    });
  } catch { throw unavailable("SIGNED_APP_VERIFICATION_FAILED"); }
}

function appPaths(executablePath: string, resourcesPath: string): { appRoot: string; framework: string; plist: string; asar: string } {
  if (!isAbsolute(executablePath) || resolve(executablePath) !== executablePath
    || !isAbsolute(resourcesPath) || resolve(resourcesPath) !== resourcesPath) throw unavailable("PACKAGED_APP_PATH_INVALID");
  const macos = dirname(executablePath);
  if (macos.split("/").at(-1) !== "MacOS") throw unavailable("PACKAGED_APP_PATH_INVALID");
  const contents = dirname(macos);
  if (join(contents, "Resources") !== resourcesPath || !contents.endsWith(".app/Contents")) throw unavailable("PACKAGED_APP_PATH_INVALID");
  return {
    appRoot: dirname(contents),
    framework: join(contents, "Frameworks", "Electron Framework.framework", "Electron Framework"),
    plist: join(contents, "Info.plist"),
    asar: join(resourcesPath, "app.asar")
  };
}

async function verifyFuses(frameworkPath: string): Promise<void> {
  const bytes = await readFile(frameworkPath).catch(() => { throw unavailable("ELECTRON_FUSE_VERIFICATION_FAILED"); });
  const positions: number[] = [];
  for (let offset = 0; ; ) {
    const found = bytes.indexOf(FUSE_SENTINEL, offset);
    if (found < 0) break;
    positions.push(found); offset = found + FUSE_SENTINEL.length;
  }
  if (positions.length < 1 || positions.length > 2) throw unavailable("ELECTRON_FUSE_VERIFICATION_FAILED");
  for (const position of positions) {
    const wire = position + FUSE_SENTINEL.length;
    if (bytes[wire] !== 1 || (bytes[wire + 1] ?? 0) < 6
      || bytes[wire + 2] !== 48
      || bytes[wire + 4] !== 48
      || bytes[wire + 5] !== 48
      || bytes[wire + 6] !== 49
      || bytes[wire + 7] !== 49) throw unavailable("ELECTRON_FUSE_VERIFICATION_FAILED");
  }
}

async function asarHeaderHash(path: string): Promise<string> {
  const handle = await open(path, "r").catch(() => { throw unavailable("ASAR_INTEGRITY_VERIFICATION_FAILED"); });
  try {
    const sizeBytes = Buffer.alloc(8);
    if ((await handle.read(sizeBytes, 0, 8, 0)).bytesRead !== 8) throw unavailable("ASAR_INTEGRITY_VERIFICATION_FAILED");
    const pickleSize = sizeBytes.readUInt32LE(4);
    if (pickleSize < 8 || pickleSize > 16_777_216) throw unavailable("ASAR_INTEGRITY_VERIFICATION_FAILED");
    const pickle = Buffer.alloc(pickleSize);
    if ((await handle.read(pickle, 0, pickle.length, 8)).bytesRead !== pickle.length) throw unavailable("ASAR_INTEGRITY_VERIFICATION_FAILED");
    const stringSize = pickle.readUInt32LE(4);
    if (stringSize < 2 || stringSize > pickle.length - 8) throw unavailable("ASAR_INTEGRITY_VERIFICATION_FAILED");
    return createHash("sha256").update(pickle.subarray(8, 8 + stringSize)).digest("hex");
  } finally { await handle.close(); }
}

async function verifyAsarIntegrity(plistPath: string, asarPath: string): Promise<void> {
  const { stdout } = await run("/usr/bin/plutil", ["-convert", "json", "-o", "-", plistPath]);
  let plist: unknown;
  try { plist = JSON.parse(stdout); } catch { throw unavailable("ASAR_INTEGRITY_VERIFICATION_FAILED"); }
  const integrity = (plist as { ElectronAsarIntegrity?: Record<string, { algorithm?: unknown; hash?: unknown }> }).ElectronAsarIntegrity;
  const entry = integrity?.["Resources/app.asar"];
  if (entry?.algorithm !== "SHA256" || typeof entry.hash !== "string" || !/^[a-f0-9]{64}$/u.test(entry.hash)
    || entry.hash !== await asarHeaderHash(asarPath)) throw unavailable("ASAR_INTEGRITY_VERIFICATION_FAILED");
}

export interface VerifiedHostAccountPackagedIdentity {
  schema: "chirality.host-account-signed-peer-identity-binding/v1";
  predicate: Awaited<ReturnType<typeof loadHostAccountSigningPredicate>>;
  effectivePeerRequirement: string;
  subject: Readonly<{ path: string; cdHash: string; designatedRequirement: string; identifier: string; teamIdentifier: string }>;
  outer: Readonly<{ path: string; cdHash: string; designatedRequirement: string; identifier: string; teamIdentifier: string }>;
  fuses: "electron-runtime-fuses-verified";
  asarIntegrity: "electron-asar-integrity-verified";
}

async function inspectSignedCode(path: string): Promise<VerifiedHostAccountPackagedIdentity["subject"]> {
  const detail = await run("/usr/bin/codesign", ["-d", "-r-", "--verbose=4", path]);
  const output = `${detail.stdout}\n${detail.stderr}`;
  const designatedRequirement = /^designated => (.+)$/mu.exec(output)?.[1]?.trim();
  const identifier = /^Identifier=(.+)$/mu.exec(output)?.[1]?.trim();
  const teamIdentifier = /^TeamIdentifier=(.+)$/mu.exec(output)?.[1]?.trim();
  const cdHash = /^CDHash=([a-fA-F0-9]{40})$/mu.exec(output)?.[1]?.toLowerCase();
  if (!designatedRequirement || !identifier || !teamIdentifier || !cdHash) throw unavailable("SIGNED_APP_IDENTITY_MISMATCH");
  return Object.freeze({ path, cdHash, designatedRequirement, identifier, teamIdentifier });
}

async function verifyExecutable(executablePath: string, paths: ReturnType<typeof appPaths>, predicate: Awaited<ReturnType<typeof loadHostAccountSigningPredicate>>): Promise<{
  subject: VerifiedHostAccountPackagedIdentity["subject"];
  outer: VerifiedHostAccountPackagedIdentity["outer"];
}> {
  await run("/usr/bin/codesign", ["--verify", "--strict", "--deep", paths.appRoot]);
  await run("/usr/bin/codesign", ["--verify", "--strict", `-R=${predicate.peerRequirement}`, executablePath]);
  const subject = await inspectSignedCode(executablePath);
  const outer = await inspectSignedCode(paths.appRoot);
  if (subject.identifier !== predicate.bundleId || subject.teamIdentifier !== predicate.teamId
    || outer.identifier !== predicate.bundleId || outer.teamIdentifier !== predicate.teamId) throw unavailable("SIGNED_APP_IDENTITY_MISMATCH");
  return { subject, outer };
}

/** Pure static final-product inspection. It neither consumes release admission nor loads native/XPC. */
export async function inspectHostAccountSignedPeerIdentity(input: {
  executablePath: string;
  resourcesPath: string;
}): Promise<VerifiedHostAccountPackagedIdentity> {
  if (process.platform !== "darwin") throw unavailable("PLATFORM_UNSUPPORTED");
  const paths = appPaths(input.executablePath, input.resourcesPath);
  if (await realpath(input.executablePath) !== input.executablePath || await realpath(paths.appRoot) !== paths.appRoot) throw unavailable("PACKAGED_APP_PATH_INVALID");
  const predicate = await loadHostAccountSigningPredicate(input.resourcesPath);
  const identity = await verifyExecutable(input.executablePath, paths, predicate);
  const effectivePeerRequirement = `(${predicate.peerRequirement}) and cdhash H"${identity.subject.cdHash}"`;
  await run("/usr/bin/codesign", ["--verify", "--strict", `-R=${effectivePeerRequirement}`, input.executablePath]);
  await verifyFuses(paths.framework);
  await verifyAsarIntegrity(paths.plist, paths.asar);
  return Object.freeze({ schema: "chirality.host-account-signed-peer-identity-binding/v1", predicate, effectivePeerRequirement,
    subject: identity.subject, outer: identity.outer, fuses: "electron-runtime-fuses-verified", asarIntegrity: "electron-asar-integrity-verified" });
}

/** Runtime activation wrapper: binds the static observation to a live issued payload basis. */
export async function verifyHostAccountPackagedIdentity(input: {
  executablePath: string;
  resourcesPath: string;
  basis: Readonly<HostedPackagedReleaseBasisV2>;
}): Promise<VerifiedHostAccountPackagedIdentity> {
  assertIssuedPackagedReleaseBasisV2(input.basis);
  await revalidateIssuedPackagedReleaseBasisV2(input.basis);
  if (input.basis.verified.resourcesRoot !== input.resourcesPath
    || !input.basis.verified.payload.entries.some((entry) => entry.type === "file" && entry.relativePath === HOST_ACCOUNT_SIGNING_PREDICATE_RESOURCE)) {
    throw unavailable("HOST_ACCOUNT_CARRIER_NOT_ACCEPTED");
  }
  const identity = await inspectHostAccountSignedPeerIdentity(input);
  await revalidateIssuedPackagedReleaseBasisV2(input.basis);
  return identity;
}

async function verifiedInputs(input: {
  executablePath: string;
  resourcesPath: string;
  basis: Readonly<HostedPackagedReleaseBasisV2>;
}) {
  const identity = await verifyHostAccountPackagedIdentity(input);
  // Keep native loading adjacent to another live read of every accepted payload
  // identity, including the carrier and addon.
  await revalidateIssuedPackagedReleaseBasisV2(input.basis);
  const loaded = loadNativeAdmissionBinding(true, input.basis.nativeAddonPath);
  if (loaded.state !== "available") throw unavailable("VERIFIED_NATIVE_ADMISSION_UNAVAILABLE");
  return { signingPredicate: Object.freeze({ ...identity.predicate, peerRequirement: identity.effectivePeerRequirement }), binding: loaded.value, expectedEuid: process.geteuid?.() ?? process.getuid?.() ?? -1 };
}

export async function createVerifiedHostAccountClient(input: {
  socketPath: string;
  executablePath: string;
  resourcesPath: string;
  basis: Readonly<HostedPackagedReleaseBasisV2>;
}): Promise<HostAccountClient> {
  const verified = await verifiedInputs(input);
  return createHostAccountClient({
    socketPath: input.socketPath,
    signingPredicate: verified.signingPredicate,
    expectedEuid: verified.expectedEuid,
    nativeAdmission: {
      createHostXpcClient(config) {
        const result = verified.binding.createHostXpcClient({
          peerRequirement: config.peerRequirement,
          expectedEuid: config.expectedEuid,
          onInvalidated(reason) { config.onInvalidated({ reason: reason === "peer-requirement-rejected" ? "peer-rejected" : reason === "lease-closed" ? "closed" : "invalidated" }); },
          onPing: config.onPing
        });
        if (result.state !== "available") throw unavailable("VERIFIED_NATIVE_ADMISSION_UNAVAILABLE");
        return result.value;
      }
    }
  });
}

export async function createVerifiedHostAccountAuthority(input: {
  runtimeDirectory: string;
  auth: AuthRegistry;
  executablePath: string;
  resourcesPath: string;
  basis: Readonly<HostedPackagedReleaseBasisV2>;
}): Promise<HostAccountAuthority> {
  const verified = await verifiedInputs(input);
  return new HostAccountAuthority({
    runtimeDirectory: input.runtimeDirectory,
    auth: input.auth,
    signingPredicate: verified.signingPredicate,
    expectedEuid: verified.expectedEuid,
    nativeAdmission: {
      createHostXpcServer(config) {
        const result = verified.binding.createHostXpcServer({
          peerRequirement: config.peerRequirement,
          expectedEuid: config.expectedEuid,
          onAdmitted() {},
          onInvalidated(connectionId, reason) { config.onInvalidated({ connectionId, reason: reason === "peer-requirement-rejected" ? "peer-rejected" : reason === "lease-closed" ? "closed" : "invalidated" }); },
          onCeremonyOpen: config.onCeremonyOpen,
          onCeremonyFinish: config.onCeremonyFinish
        });
        if (result.state !== "available") throw unavailable("VERIFIED_NATIVE_ADMISSION_UNAVAILABLE");
        return {
          async ping(connectionId, value) {
            return result.value.ping(connectionId, value);
          },
          closeConnection(connectionId) { return result.value.closeConnection(connectionId, "lease-closed"); },
          close() { return result.value.close(); }
        };
      }
    }
  });
}
