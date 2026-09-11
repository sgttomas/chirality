import { createHash } from "node:crypto";
import { mkdir, mkdtemp, readFile, realpath, rm, symlink, writeFile } from "node:fs/promises";
import { join, relative, sep } from "node:path";
import { afterEach, expect, it } from "vitest";
import {
  computeRuntimeArtifactDigest,
  configureRuntimeConformanceArtifactInventory,
  captureRuntimeConformanceGeneration,
  runtimeConformanceArtifactInventory,
  type RuntimeArtifactInventoryManifest
} from "../packages/core/src/runtime-conformance.js";

const sha256 = (bytes: string | Buffer) => createHash("sha256").update(bytes).digest("hex");
const roots: string[] = [];
afterEach(async () => { await Promise.all(roots.splice(0).map(root => rm(root, { recursive: true, force: true }))); });

async function packagedFixture() {
  const resourcesRoot = await realpath(await mkdtemp(join(await realpath("/tmp"), "runtime-artifacts-"))); roots.push(resourcesRoot);
  const files: Record<string, string> = {
    "app.asar": "opaque application and bundled dependency bytes",
    "instruction-root/instruction-bundle-manifest.json": "instruction manifest",
    "instruction-root/agents/AGENT_TASK.md": "trusted instructions",
    "native/chirality_native_admission.node": "native addon bytes",
    "runtime-cli/chirality-cli.mjs": "cli bytes",
    "runtime-cli/chirality-cli.mjs.map": "cli source identity"
  };
  for (const [name, bytes] of Object.entries(files)) { await mkdir(join(resourcesRoot, name, ".."), { recursive: true }); await writeFile(join(resourcesRoot, name), bytes); }
  const entries = await Promise.all(Object.keys(files).sort().map(async relativePath => {
    const bytes = await readFile(join(resourcesRoot, relativePath)); return { relativePath, sha256: sha256(bytes), size: bytes.length };
  }));
  const manifest: RuntimeArtifactInventoryManifest = {
    schema: "chirality-runtime-artifact-inventory/v1",
    sourceIdentityDigest: sha256("source maps plus declared build inputs"),
    dependencyResolutionDigest: sha256("installed production dependency identities"),
    closureRoots: ["app.asar", "instruction-root", "native", "runtime-cli"], entries
  };
  const manifestPath = join(resourcesRoot, "runtime-artifact-inventory.json");
  const save = () => writeFile(manifestPath, JSON.stringify(manifest)); await save();
  return { resourcesRoot, manifestPath, manifest, save, files };
}

it("verifies the exact packaged Resources closure and binds the manifest into both digests", async () => {
  const fixture = await packagedFixture();
  const inventory = await runtimeConformanceArtifactInventory({ kind: "packaged-resources", resourcesRoot: fixture.resourcesRoot, manifestPath: fixture.manifestPath });
  expect(inventory.sourceFiles[0]).toBe(fixture.manifestPath);
  expect(inventory.sourceFiles.slice(1).map(path => relative(fixture.resourcesRoot, path).split(sep).join("/"))).toEqual(fixture.manifest.entries.map(entry => entry.relativePath));
  expect(inventory.packageFiles).toEqual(inventory.sourceFiles);
  expect(inventory.dependencyResolutionDigest).toBe(fixture.manifest.dependencyResolutionDigest);
  const before = await computeRuntimeArtifactDigest(inventory.sourceFiles);
  fixture.manifest.sourceIdentityDigest = sha256("different source identity"); await fixture.save();
  expect(await computeRuntimeArtifactDigest(inventory.sourceFiles)).not.toBe(before);
});

it("accepts an additional Resources artifact only when it is both rooted and entered", async () => {
  const fixture = await packagedFixture(), bytes = "packaged notice";
  await writeFile(join(fixture.resourcesRoot, "NOTICE.txt"), bytes);
  fixture.manifest.closureRoots = ["NOTICE.txt", ...fixture.manifest.closureRoots].sort();
  fixture.manifest.entries.push({ relativePath: "NOTICE.txt", sha256: sha256(bytes), size: Buffer.byteLength(bytes) });
  fixture.manifest.entries.sort((a, b) => a.relativePath < b.relativePath ? -1 : a.relativePath > b.relativePath ? 1 : 0); await fixture.save();
  const inventory = await runtimeConformanceArtifactInventory({ kind: "packaged-resources", resourcesRoot: fixture.resourcesRoot, manifestPath: fixture.manifestPath });
  expect(inventory.sourceFiles).toContain(join(fixture.resourcesRoot, "NOTICE.txt"));
});

it.each(["hash", "missing", "undeclared", "root-sibling", "unrooted-entry", "symlink", "manifest-field"] as const)("fails closed for packaged closure defect %s", async defect => {
  const fixture = await packagedFixture();
  if (defect === "hash") fixture.manifest.entries[0]!.sha256 = "0".repeat(64);
  if (defect === "missing") await rm(join(fixture.resourcesRoot, "runtime-cli/chirality-cli.mjs.map"));
  if (defect === "undeclared") await writeFile(join(fixture.resourcesRoot, "native/undeclared.node"), "not declared");
  if (defect === "root-sibling") await writeFile(join(fixture.resourcesRoot, "NOTICE.txt"), "undeclared resource sibling");
  if (defect === "unrooted-entry") {
    const bytes = "entered but not rooted"; await writeFile(join(fixture.resourcesRoot, "NOTICE.txt"), bytes);
    fixture.manifest.entries.push({ relativePath: "NOTICE.txt", sha256: sha256(bytes), size: Buffer.byteLength(bytes) });
    fixture.manifest.entries.sort((a, b) => a.relativePath < b.relativePath ? -1 : a.relativePath > b.relativePath ? 1 : 0);
  }
  if (defect === "symlink") { await rm(join(fixture.resourcesRoot, "runtime-cli/chirality-cli.mjs.map")); await symlink("chirality-cli.mjs", join(fixture.resourcesRoot, "runtime-cli/chirality-cli.mjs.map")); }
  if (defect === "manifest-field") (fixture.manifest as unknown as Record<string, unknown>).unexpected = true;
  await fixture.save();
  await expect(runtimeConformanceArtifactInventory({ kind: "packaged-resources", resourcesRoot: fixture.resourcesRoot, manifestPath: fixture.manifestPath })).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
});

it("requires an explicit canonical host selection and permanently rejects a changed process selection", async () => {
  await expect(runtimeConformanceArtifactInventory(undefined as never)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
  const sourceRoot = await realpath(await mkdtemp(join(await realpath("/tmp"), "runtime-source-selection-"))); roots.push(sourceRoot);
  await mkdir(join(sourceRoot, "packages/runtime/dist"), { recursive: true });
  await writeFile(join(sourceRoot, "package.json"), JSON.stringify({ name: "runtime", version: "1.0.0" }));
  await writeFile(join(sourceRoot, "package-lock.json"), JSON.stringify({ lockfileVersion: 3 }));
  await writeFile(join(sourceRoot, "packages/runtime/package.json"), JSON.stringify({ name: "@test/runtime", version: "1.0.0" }));
  await writeFile(join(sourceRoot, "packages/runtime/dist/runtime.js"), "export const runtime = true;");
  configureRuntimeConformanceArtifactInventory({ kind: "source-tree", sourceRoot });
  configureRuntimeConformanceArtifactInventory({ kind: "source-tree", sourceRoot });
  expect((await captureRuntimeConformanceGeneration()).sourceDigest).toMatch(/^[a-f0-9]{64}$/);
  const other = await packagedFixture();
  expect(() => configureRuntimeConformanceArtifactInventory({ kind: "packaged-resources", resourcesRoot: other.resourcesRoot, manifestPath: other.manifestPath })).toThrow();
  expect(() => configureRuntimeConformanceArtifactInventory({ kind: "source-tree", sourceRoot })).toThrow();
});
