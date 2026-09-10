"use strict";

const crypto = require("node:crypto");
const fs = require("node:fs");
const path = require("node:path");

function parseExactArgs(argv, names) {
  if (argv.length !== names.length * 2) throw new Error("invalid-arguments");
  const result = Object.create(null);
  for (let index = 0; index < argv.length; index += 2) {
    const name = argv[index];
    if (!names.includes(name) || Object.hasOwn(result, name)) throw new Error("invalid-arguments");
    result[name] = argv[index + 1];
  }
  if (names.some((name) => typeof result[name] !== "string" || result[name].length === 0)) throw new Error("invalid-arguments");
  return result;
}

function validateSha256(value) {
  if (!/^[a-f0-9]{64}$/.test(value)) throw new Error("invalid-sha256");
  return value;
}

function verifyRegularFileIdentity(filePath, expectedSha256) {
  if (!path.isAbsolute(filePath) || path.normalize(filePath) !== filePath) throw new Error("unsafe-addon-path");
  const link = fs.lstatSync(filePath);
  if (!link.isFile() || link.isSymbolicLink()) throw new Error("unsafe-addon-file");
  const canonicalPath = fs.realpathSync.native(filePath);
  if (canonicalPath !== filePath) throw new Error("noncanonical-addon-path");
  const stat = fs.statSync(filePath);
  if (!stat.isFile()) throw new Error("unsafe-addon-file");
  const actualSha256 = crypto.createHash("sha256").update(fs.readFileSync(filePath)).digest("hex");
  if (actualSha256 !== validateSha256(expectedSha256)) throw new Error("addon-hash-mismatch");
  const after = fs.statSync(filePath);
  if (stat.dev !== after.dev || stat.ino !== after.ino || stat.size !== after.size || stat.mtimeMs !== after.mtimeMs || stat.ctimeMs !== after.ctimeMs) throw new Error("addon-identity-changed");
  return { path: canonicalPath, sha256: actualSha256, device: stat.dev.toString(), inode: stat.ino.toString(), size: stat.size, mtimeMs: stat.mtimeMs, ctimeMs: stat.ctimeMs };
}

function sameIdentity(left, right) {
  return left.path === right.path && left.sha256 === right.sha256 && left.device === right.device && left.inode === right.inode && left.size === right.size && left.mtimeMs === right.mtimeMs && left.ctimeMs === right.ctimeMs;
}

function runtimeEvidence() {
  return {
    platform: process.platform,
    arch: process.arch,
    electron: process.versions.electron || null,
    node: process.versions.node,
    modules: process.versions.modules,
    napi: process.versions.napi || null,
  };
}

function assertElectronRuntime(evidence) {
  if (evidence.platform !== "darwin" || evidence.arch !== "arm64") throw new Error("unsupported-host");
  if (typeof evidence.electron !== "string" || evidence.electron.length === 0) throw new Error("electron-required");
  if (!Number.isInteger(Number(evidence.napi)) || Number(evidence.napi) < 6) throw new Error("napi-version-unsupported");
}

function emit(value) {
  process.stdout.write(`${JSON.stringify(value)}\n`);
}

function main(argv = process.argv.slice(2)) {
  const evidence = { schemaVersion: "chirality.native-load-probe/v1", runtime: runtimeEvidence(), addon: null, result: "FAIL", reason: null };
  try {
    const args = parseExactArgs(argv, ["--addon", "--sha256"]);
    const addonIdentity = verifyRegularFileIdentity(args["--addon"], args["--sha256"]);
    evidence.addon = { path: addonIdentity.path, sha256: addonIdentity.sha256 };
    assertElectronRuntime(evidence.runtime);
    const binding = require(addonIdentity.path);
    const afterLoad = verifyRegularFileIdentity(addonIdentity.path, addonIdentity.sha256);
    if (!sameIdentity(addonIdentity, afterLoad)) throw new Error("addon-identity-changed-during-load");
    if (!binding || typeof binding.acquire !== "function" || typeof binding.spawnSupplier !== "function") throw new Error("addon-api-mismatch");
    evidence.result = "PASS";
    emit(evidence);
    return 0;
  } catch (error) {
    evidence.reason = error instanceof Error ? error.message : "unknown-failure";
    emit(evidence);
    return 1;
  }
}

module.exports = { assertElectronRuntime, parseExactArgs, runtimeEvidence, sameIdentity, validateSha256, verifyRegularFileIdentity };

if (require.main === module) process.exitCode = main();
