import { mkdir, mkdtemp, realpath, rm, writeFile, symlink, rename, stat, utimes } from "node:fs/promises";
import { dirname, join, relative } from "node:path";
import { afterEach, expect, it } from "vitest";
import { inventoryRuntimeDependencies } from "../packages/core/src/runtime-dependencies.js";
import { computeRuntimeArtifactDigest, createControlledArtifactGenerationForTests } from "../packages/core/src/runtime-conformance.js";
const roots: string[] = [];
afterEach(async () => { await Promise.all(roots.splice(0).map(root => rm(root, { recursive: true, force: true }))); });
async function fixture() {
  const root = await realpath(await mkdtemp("/tmp/runtime-deps-")); roots.push(root);
  const app = join(root, "packages/app");
  const pkg = async (path: string, name: string, extra = {}) => {
    await mkdir(path, { recursive: true }); await writeFile(join(path, "package.json"), JSON.stringify({ name, version: "1.0.0", ...extra }));
    await writeFile(join(path, "index.js"), "fixture package bytes");
    return path;
  };
  await pkg(app, "app", { dependencies: { dep: "1.0.0" }, optionalDependencies: { maybe: "*" }, devDependencies: { devonly: "*" } });
  const dep = await pkg(join(root, "node_modules/dep"), "dep", { dependencies: { transitive: "*" }, peerDependencies: { peer: "*" } });
  await pkg(join(root, "node_modules/transitive"), "transitive");
  const inventory = () => inventoryRuntimeDependencies(root, [app]);
  const generation = () => createControlledArtifactGenerationForTests(async () => {
    const result = await inventory();
    return { sourceFiles: [join(app, "index.js")], packageFiles: [join(app, "package.json"), ...result.files], dependencyResolutionDigest: result.resolutionDigest };
  });
  return { root, app, dep, pkg, inventory, generation };
}
it("follows declared production transitives and present peers while excluding dev-only packages", async () => {
  const f = await fixture(); await f.pkg(join(f.root, "node_modules/devonly"), "devonly"); await f.pkg(join(f.root, "node_modules/peer"), "peer");
  const result = await f.inventory(); expect(result.packageCount).toBe(4); expect(result.fileCount).toBe(6);
  expect(result.files.some(path => path.includes("/devonly/"))).toBe(false);
  expect(result.files.some(path => path.includes("/peer/"))).toBe(true);
});
it("records optional absence and actual nested Node lookup precedence", async () => {
  const f = await fixture(), original = await f.inventory();
  await f.pkg(join(f.dep, "node_modules/transitive"), "transitive");
  // Node may retain its old require-resolution cache. A mismatch with fresh lookup is a fail-closed drift.
  await expect(f.inventory()).rejects.toThrow();
  const fresh = await fixture(); await fresh.pkg(join(fresh.dep, "node_modules/transitive"), "transitive");
  const nested = await fresh.inventory();
  expect(nested.files).toContain(join(fresh.dep, "node_modules/transitive/index.js"));
  await fresh.pkg(join(fresh.root, "node_modules/maybe"), "maybe");
  expect((await fresh.inventory()).resolutionDigest).not.toBe(nested.resolutionDigest);
  expect(original.resolutionDigest).toMatch(/^[a-f0-9]{64}$/);
});
it("permits only the exact known workspace link and rejects retargeting or external links", async () => {
  const f = await fixture(), lib = await f.pkg(join(f.root, "packages/lib"), "lib");
  await writeFile(join(f.app, "package.json"), JSON.stringify({ name: "app", version: "1.0.0", dependencies: { lib: "*" } }));
  const link = join(f.root, "node_modules/lib"); await symlink(relative(dirname(link), lib), link);
  expect((await inventoryRuntimeDependencies(f.root, [f.app, lib])).packageCount).toBe(2);
  await rm(link); await symlink(f.dep, link);
  await expect(inventoryRuntimeDependencies(f.root, [f.app, lib])).rejects.toThrow();
  await rm(link); await symlink("/tmp", link);
  await expect(inventoryRuntimeDependencies(f.root, [f.app, lib])).rejects.toThrow();
});
it("rejects package-file symlinks and absent required dependencies", async () => {
  const f = await fixture(); await symlink(join(f.app, "index.js"), join(f.dep, "alias.js"));
  await expect(f.inventory()).rejects.toThrow(); await rm(join(f.dep, "alias.js"));
  await rm(join(f.root, "node_modules/transitive"), { recursive: true });
  await expect(f.inventory()).rejects.toThrow();
});
it.each(["contents-restored-mtime", "replacement", "new-file", "new-optional", "resolution-parent"] as const)("permanently poisons a process generation on %s", async change => {
  const f = await fixture(), processGeneration = f.generation(), first = processGeneration.createVerifier();
  await first.verify();
  const path = join(f.dep, "index.js"), before = await stat(path), original = "fixture package bytes";
  if (change === "contents-restored-mtime") { await writeFile(path, "changed package bytes"); await utimes(path, before.atime, before.mtime); }
  if (change === "replacement") { await writeFile(path + ".new", original); await rename(path + ".new", path); }
  if (change === "new-file") await writeFile(join(f.dep, "added.js"), "new file");
  if (change === "new-optional") await f.pkg(join(f.root, "node_modules/maybe"), "maybe");
  if (change === "resolution-parent") {
    await rename(join(f.root, "node_modules"), join(f.root, "old-modules")); await mkdir(join(f.root, "node_modules"));
    for (const name of ["dep", "transitive"]) await rename(join(f.root, "old-modules", name), join(f.root, "node_modules", name));
  }
  await expect(first.verify()).rejects.toThrow();
  await writeFile(path, original);
  await expect(processGeneration.createVerifier().verify()).rejects.toThrow();
});
it("hash cache observes content mutation even when size and mtime are restored", async () => {
  const f = await fixture(), path = join(f.dep, "index.js"), before = await stat(path);
  const original = await computeRuntimeArtifactDigest([path]);
  await writeFile(path, "changed package bytes"); await utimes(path, before.atime, before.mtime);
  expect(await computeRuntimeArtifactDigest([path])).not.toBe(original);
});

it("rejects a package main that resolves outside its deployed package boundary", async () => {
  const f = await fixture();
  await writeFile(join(f.dep, "package.json"), JSON.stringify({ name: "dep", version: "1.0.0", main: "../../packages/app/index.js" }));
  await expect(f.inventory()).rejects.toThrow();
});
it("poisons when a workspace symlink is replaced even with the same target", async () => {
  const f = await fixture(), lib = await f.pkg(join(f.root, "packages/lib"), "lib");
  await writeFile(join(f.app, "package.json"), JSON.stringify({ name: "app", version: "1.0.0", dependencies: { lib: "*" } }));
  const link = join(f.root, "node_modules/lib"), target = relative(dirname(link), lib); await symlink(target, link);
  const generation = createControlledArtifactGenerationForTests(async () => {
    const result = await inventoryRuntimeDependencies(f.root, [f.app, lib]);
    return { sourceFiles: [join(f.app, "index.js")], packageFiles: [join(f.app, "package.json"), join(lib, "package.json")], dependencyResolutionDigest: result.resolutionDigest };
  });
  await generation.createVerifier().verify();
  await rm(link); await symlink(target, link);
  await expect(generation.createVerifier().verify()).rejects.toThrow();
});


it.each(["optionalDependencies", "peerDependencies"] as const)("rejects an outside ancestor package for %s instead of recording absence", async field => {
  const parent = await realpath(await mkdtemp("/tmp/runtime-ancestor-")); roots.push(parent);
  const runtime = join(parent, "runtime"), app = join(runtime, "packages/app"), escaped = join(parent, "node_modules/escaped-dep");
  await mkdir(app, { recursive: true }); await mkdir(escaped, { recursive: true });
  await writeFile(join(app, "package.json"), JSON.stringify({ name: "app", version: "1.0.0", [field]: { "escaped-dep": "*" } }));
  await writeFile(join(escaped, "package.json"), JSON.stringify({ name: "escaped-dep", version: "1.0.0", main: "index.js" }));
  await writeFile(join(escaped, "index.js"), 'throw new Error("fixture must never execute");');
  const { createRequire } = await import("node:module");
  expect(createRequire(join(app, "package.json")).resolve("escaped-dep")).toBe(join(escaped, "index.js"));
  await expect(inventoryRuntimeDependencies(runtime, [app])).rejects.toThrow();
});
it("rejects an import-only outside ancestor package without interpreting require-resolution failure as absence", async () => {
  const parent = await realpath(await mkdtemp("/tmp/runtime-ancestor-esm-")); roots.push(parent);
  const runtime = join(parent, "runtime"), app = join(runtime, "packages/app"), escaped = join(parent, "node_modules/escaped-esm");
  await mkdir(app, { recursive: true }); await mkdir(escaped, { recursive: true });
  await writeFile(join(app, "package.json"), JSON.stringify({ name: "app", version: "1.0.0", optionalDependencies: { "escaped-esm": "*" } }));
  await writeFile(join(escaped, "package.json"), JSON.stringify({ name: "escaped-esm", version: "1.0.0", type: "module", exports: { ".": { import: "./index.js" } } }));
  await writeFile(join(escaped, "index.js"), 'throw new Error("fixture must never execute");');
  const { createRequire } = await import("node:module");
  expect(() => createRequire(join(app, "package.json")).resolve("escaped-esm")).toThrow();
  await expect(inventoryRuntimeDependencies(runtime, [app])).rejects.toThrow();
});
it("poisons a generation when a previously absent optional edge appears outside Runtime", async () => {
  const parent = await realpath(await mkdtemp("/tmp/runtime-ancestor-drift-")); roots.push(parent);
  const runtime = join(parent, "runtime"), app = join(runtime, "packages/app"), escaped = join(parent, "node_modules/escaped-dep");
  await mkdir(app, { recursive: true });
  await writeFile(join(app, "package.json"), JSON.stringify({ name: "app", version: "1.0.0", optionalDependencies: { "escaped-dep": "*" } }));
  await writeFile(join(app, "index.js"), "controlled source");
  const generation = createControlledArtifactGenerationForTests(async () => {
    const inventory = await inventoryRuntimeDependencies(runtime, [app]);
    return { sourceFiles: [join(app, "index.js")], packageFiles: [join(app, "package.json")], dependencyResolutionDigest: inventory.resolutionDigest };
  });
  await generation.createVerifier().verify();
  await mkdir(escaped, { recursive: true });
  await expect(generation.createVerifier().verify()).rejects.toThrow();
  await rm(escaped, { recursive: true });
  await expect(generation.createVerifier().verify()).rejects.toThrow();
});
it("rejects an outside Node file-extension fallback without opening its contents", async () => {
  const parent = await realpath(await mkdtemp("/tmp/runtime-ancestor-file-")); roots.push(parent);
  const runtime = join(parent, "runtime"), app = join(runtime, "packages/app"), modules = join(parent, "node_modules");
  await mkdir(app, { recursive: true }); await mkdir(modules);
  await writeFile(join(app, "package.json"), JSON.stringify({ name: "app", version: "1.0.0", optionalDependencies: { "escaped-file": "*" } }));
  await writeFile(join(modules, "escaped-file.js"), 'throw new Error("fixture must never execute");');
  await expect(inventoryRuntimeDependencies(runtime, [app])).rejects.toThrow();
});


it.each(["optionalDependencies", "peerDependencies"] as const)("rejects unregistered in-root file-extension fallback for %s", async field => {
  const f = await fixture();
  await writeFile(join(f.app, "package.json"), JSON.stringify({ name: "app", version: "1.0.0", [field]: { "flat-dep": "*" } }));
  await writeFile(join(f.root, "node_modules/flat-dep.js"), 'throw new Error("fixture must never execute");');
  const { createRequire } = await import("node:module");
  expect(createRequire(join(f.app, "package.json")).resolve("flat-dep")).toBe(join(f.root, "node_modules/flat-dep.js"));
  await expect(f.inventory()).rejects.toThrow();
});
