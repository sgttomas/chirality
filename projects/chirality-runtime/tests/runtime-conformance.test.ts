import { mkdir, mkdtemp, realpath, rm, writeFile, symlink, chmod } from "node:fs/promises";
import { join } from "node:path";
import { afterAll, afterEach, beforeAll, expect, it, vi } from "vitest";
import { ACCEPTED_SUPPLY } from "../packages/core/src/exact-supply.js";
import { computeRuntimeArtifactDigest, configureRuntimeConformanceArtifactInventory, inspectRuntimeConformanceRecord, isRuntimeConformanceAdmission, REQUIRED_RUNTIME_CONFORMANCE_LIMBS, RuntimeConformanceVerifier, type RuntimeConformanceBasis, type RuntimeConformanceBindings } from "../packages/core/src/runtime-conformance.js";
// Production generation verification inventories the installed dependency closure.
vi.setConfig({ testTimeout: 120_000 });
const roots: string[] = [];
let runtimeRoot: string;
beforeAll(async () => {
  runtimeRoot = await realpath(await mkdtemp(join(await realpath("/tmp"), "runtime-source-inventory-")));
  await mkdir(join(runtimeRoot, "packages/runtime/dist"), { recursive: true });
  await writeFile(join(runtimeRoot, "package.json"), JSON.stringify({ name: "runtime", version: "1.0.0" }));
  await writeFile(join(runtimeRoot, "package-lock.json"), JSON.stringify({ lockfileVersion: 3 }));
  await writeFile(join(runtimeRoot, "packages/runtime/package.json"), JSON.stringify({ name: "@test/runtime", version: "1.0.0" }));
  await writeFile(join(runtimeRoot, "packages/runtime/dist/runtime.js"), "export const runtime = true;");
  configureRuntimeConformanceArtifactInventory({ kind: "source-tree", sourceRoot: runtimeRoot });
});
afterAll(async () => { await rm(runtimeRoot, { recursive: true, force: true }); });
afterEach(async () => { await Promise.all(roots.splice(0).map(root => rm(root, { recursive: true, force: true }))); });
async function fixture() {
  const root = await realpath(await mkdtemp(join(await realpath("/tmp"), "rc-"))); roots.push(root);
  const project = join(root, "project"); await mkdir(project);
  const source = join(root, "source.ts"), packageFile = join(root, "package-lock.json"), executablePath = join(root, "not-vendor");
  await writeFile(source, "actual source fixture"); await writeFile(packageFile, "actual package fixture"); await writeFile(executablePath, "not the accepted artifact");
  const basis: RuntimeConformanceBasis = { canonicalRoot: project, cwd: project, executablePath, sourceFiles: [source], packageFiles: [packageFile], policyDigest: "a".repeat(64), configDigest: "b".repeat(64), activationId: "fixture-activation", gateIdentity: "fixture-G4", accountId: "fixture-account", accountEpoch: 1, accountDigest: "c".repeat(64), consentVersion: "f".repeat(64) };
  const { sourceFiles, packageFiles, ...identity } = basis;
  const bindings: RuntimeConformanceBindings = { ...identity, sourceDigest: await computeRuntimeArtifactDigest(sourceFiles), packageDigest: await computeRuntimeArtifactDigest(packageFiles) };
  const now = Date.now();
  const record = { schema: "chirality-runtime-conformance/v1", evidenceClass: "exact-turn-path-observed", bindings, supply: { sha256: ACCEPTED_SUPPLY.sha256, size: ACCEPTED_SUPPLY.size, version: ACCEPTED_SUPPLY.version }, issuedAt: new Date(now - 1000).toISOString(), expiresAt: new Date(now + 60000).toISOString(), limbs: Object.fromEntries(REQUIRED_RUNTIME_CONFORMANCE_LIMBS.map(name => [name, { attempted: true, passed: true, evidenceSha256: "d".repeat(64) }])) };
  const recordPath = join(root, "conformance.json"); const save = () => writeFile(recordPath, JSON.stringify(record), { mode: 0o600 }); await save();
  return { root, source, packageFile, basis, bindings, record, recordPath, save, now };
}
it("mechanically inspects a complete immutable record without creating admission or owner acceptance", async () => {
  const f = await fixture(); const record = inspectRuntimeConformanceRecord(f.record, f.bindings, f.now);
  expect(Object.isFrozen(record.bindings)).toBe(true); expect(Object.isFrozen(record.limbs["primary.read"])).toBe(true);
  expect(isRuntimeConformanceAdmission(record)).toBe(false); expect(isRuntimeConformanceAdmission({ evidence: "mechanically-verified-with-external-acceptance" })).toBe(false);
});
it.each(REQUIRED_RUNTIME_CONFORMANCE_LIMBS)("rejects missing/unattempted/failed required limb %s", async name => {
  const f = await fixture(); f.record.limbs[name]!.attempted = false; expect(() => inspectRuntimeConformanceRecord(f.record, f.bindings)).toThrow();
  f.record.limbs[name]!.attempted = true; f.record.limbs[name]!.passed = false; expect(() => inspectRuntimeConformanceRecord(f.record, f.bindings)).toThrow();
  delete f.record.limbs[name]; expect(() => inspectRuntimeConformanceRecord(f.record, f.bindings)).toThrow();
});
it.each(["policyDigest", "configDigest", "sourceDigest", "packageDigest", "activationId", "gateIdentity", "accountId", "accountEpoch", "accountDigest", "consentVersion", "canonicalRoot", "cwd", "executablePath"] as const)("invalidates changed binding %s", async key => {
  const f = await fixture(); const changed = structuredClone(f.bindings); (changed as any)[key] = typeof changed[key] === "number" ? 2 : key.endsWith("Digest") ? "e".repeat(64) : key.includes("Root") || key === "cwd" || key === "executablePath" ? f.root : "changed";
  expect(() => inspectRuntimeConformanceRecord(f.record, changed)).toThrow();
});
it("rejects expired/future evidence, unknown fields and controlled evidence labels", async () => {
  const f = await fixture(); expect(() => inspectRuntimeConformanceRecord(f.record, f.bindings, f.now + 120000)).toThrow(); expect(() => inspectRuntimeConformanceRecord(f.record, f.bindings, f.now - 120000)).toThrow();
  expect(() => inspectRuntimeConformanceRecord({ ...f.record, accepted: true }, f.bindings)).toThrow(); expect(() => inspectRuntimeConformanceRecord({ ...f.record, evidenceClass: "controlled-fixture" }, f.bindings)).toThrow();
});
it("binds source/package order, actual bytes and canonical paths, rejecting aliases and directories", async () => {
  const f = await fixture(); expect(await computeRuntimeArtifactDigest([f.source, f.packageFile])).not.toBe(await computeRuntimeArtifactDigest([f.packageFile, f.source]));
  await writeFile(f.source, "changed source"); expect(await computeRuntimeArtifactDigest([f.source])).not.toBe(f.bindings.sourceDigest);
  const alias = join(f.root, "alias"); await symlink(f.source, alias); await expect(computeRuntimeArtifactDigest([alias])).rejects.toThrow(); await expect(computeRuntimeArtifactDigest([f.root])).rejects.toThrow(); await expect(computeRuntimeArtifactDigest([f.source, f.source])).rejects.toThrow();
});
it.each(["unknown", "revoked"] as const)("never admits self-asserted passing records when external status is %s", async status => {
  const f = await fixture(); const lookup = vi.fn(async () => ({ status }));
  await expect(new RuntimeConformanceVerifier({ acceptance: { lookup } }).verify({ recordPath: f.recordPath, basis: f.basis })).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
  expect(lookup).toHaveBeenCalledWith(expect.objectContaining({ activationId: f.basis.activationId, sourceDigest: f.bindings.sourceDigest, recordSha256: expect.stringMatching(/^[a-f0-9]{64}$/) }));
});
it("even a controlled accepted lookup cannot substitute fixture bytes for the real accepted supply", async () => {
  const f = await fixture(); await expect(new RuntimeConformanceVerifier({ acceptance: { async lookup() { return { status: "accepted", ownerReference: "controlled-test-only" }; } } }).verify({ recordPath: f.recordPath, basis: f.basis })).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
});
it("rejects nonprivate/symlink records and stale actual source before acceptance lookup", async () => {
  const f = await fixture(); const lookup = vi.fn(async () => ({ status: "unknown" as const })); const verifier = new RuntimeConformanceVerifier({ acceptance: { lookup } });
  await chmod(f.recordPath, 0o644); await expect(verifier.verify({ recordPath: f.recordPath, basis: f.basis })).rejects.toThrow(); await chmod(f.recordPath, 0o600);
  const alias = join(f.root, "record-alias"); await symlink(f.recordPath, alias); await expect(verifier.verify({ recordPath: alias, basis: f.basis })).rejects.toThrow();
  await writeFile(f.source, "source drift"); await expect(verifier.verify({ recordPath: f.recordPath, basis: f.basis })).rejects.toThrow(); expect(lookup).not.toHaveBeenCalled();
});

it("file acceptance requires exact externally pinned owner act and observes revocation on every lookup", async () => {
  const f = await fixture();
  const { createHash } = await import("node:crypto");
  const { RuntimeConformanceFileAcceptancePort } = await import("../packages/core/src/runtime-conformance.js");
  const ownerActPath = join(f.root, "external-owner-act.txt"), acceptancePath = join(f.root, "acceptance.json");
  const bytes = "controlled externally asserted owner act fixture, not an actual owner ruling"; await writeFile(ownerActPath, bytes);
  const ownerActSha256 = createHash("sha256").update(bytes).digest("hex");
  const query = { recordSha256: "1".repeat(64), sourceDigest: f.bindings.sourceDigest, activationId: f.basis.activationId, gateIdentity: f.basis.gateIdentity };
  const accepted = { schema: "chirality-runtime-conformance-acceptance/v1", status: "accepted", ...query, ownerActSha256, ownerReference: "controlled mechanical lookup only", expiresAt: new Date(Date.now() + 60000).toISOString() };
  await writeFile(acceptancePath, JSON.stringify(accepted), { mode: 0o600 });
  const port = new RuntimeConformanceFileAcceptancePort({ acceptancePath, ownerActPath, ownerActSha256 });
  expect((await port.lookup(query)).status).toBe("accepted");
  await writeFile(acceptancePath, JSON.stringify({ ...accepted, status: "revoked" })); expect((await port.lookup(query)).status).toBe("revoked");
  await writeFile(acceptancePath, JSON.stringify(accepted)); await writeFile(ownerActPath, "changed external act"); expect((await port.lookup(query)).status).toBe("unknown");
});
it("derives all first-party runtime package artifacts instead of accepting a caller-selected subset", async () => {
  const { runtimeConformanceArtifactInventory } = await import("../packages/core/src/runtime-conformance.js");
  const inventory = await runtimeConformanceArtifactInventory({ kind: "source-tree", sourceRoot: runtimeRoot });
  expect(inventory.packageFiles.some(path => path.endsWith("/package.json"))).toBe(true);
  expect(inventory.dependencyResolutionDigest).toMatch(/^[a-f0-9]{64}$/);
  expect(inventory.sourceFiles).toEqual([join(runtimeRoot, "packages/runtime/dist/runtime.js")]);
  expect(inventory.packageFiles.some(path => path.endsWith("/package-lock.json"))).toBe(true);
});

it("permanently poisons a captured generation on changed bytes, even after restoration and new verifier construction", async () => {
  const f = await fixture();
  const { createControlledArtifactGenerationForTests } = await import("../packages/core/src/runtime-conformance.js");
  const generation = createControlledArtifactGenerationForTests(async () => ({ sourceFiles: f.basis.sourceFiles, packageFiles: f.basis.packageFiles }));
  const first = generation.createVerifier(); const baseline = await first.verify(); expect(baseline.sourceDigest).toBe(f.bindings.sourceDigest);
  await writeFile(f.source, "new bytes that a new record might accept"); await expect(first.verify()).rejects.toThrow();
  await writeFile(f.source, "actual source fixture"); await expect(generation.createVerifier().verify()).rejects.toThrow();
});
it("invalidates inventory additions and identity-only replacement, not just content digests", async () => {
  const f = await fixture(); const { createControlledArtifactGenerationForTests } = await import("../packages/core/src/runtime-conformance.js");
  const paths = [f.source]; const generation = createControlledArtifactGenerationForTests(async () => ({ sourceFiles: paths, packageFiles: f.basis.packageFiles }));
  await generation.createVerifier().verify(); paths.push(f.packageFile); await expect(generation.createVerifier().verify()).rejects.toThrow();
  const other = createControlledArtifactGenerationForTests(async () => ({ sourceFiles: [f.source], packageFiles: f.basis.packageFiles }));
  await other.createVerifier().verify(); await rm(f.source); await writeFile(f.source, "actual source fixture"); await expect(other.createVerifier().verify()).rejects.toThrow();
});
it("retains startup capture failure without unhandled rejection or reset by a later verifier", async () => {
  const f = await fixture(); const { createControlledArtifactGenerationForTests } = await import("../packages/core/src/runtime-conformance.js");
  const missing = join(f.root, "missing-startup-file");
  const generation = createControlledArtifactGenerationForTests(async () => ({ sourceFiles: [missing], packageFiles: f.basis.packageFiles }));
  await expect(generation.createVerifier().verify()).rejects.toThrow(); await writeFile(missing, "appeared later"); await expect(generation.createVerifier().verify()).rejects.toThrow();
});
it("exposes the same non-resettable production capture across calls without claiming loaded-module proof", async () => {
  const { captureRuntimeConformanceGeneration } = await import("../packages/core/src/runtime-conformance.js");
  const a = await captureRuntimeConformanceGeneration(), b = await captureRuntimeConformanceGeneration();
  expect(a).toEqual(b); expect(a.evidence).toBe("startup-disk-inventory-not-loaded-module-proof"); expect(isRuntimeConformanceAdmission(a)).toBe(false);
});
