import { lstat, readFile, readdir, readlink, realpath } from "node:fs/promises";
import { createRequire } from "node:module";
import { dirname, isAbsolute, join, relative, resolve } from "node:path";
import { createHash } from "node:crypto";
import { RuntimeError } from "@chirality/runtime-contracts";
const denied = () => new RuntimeError("ENGINE_UNAVAILABLE", "Deployed dependency inventory is unsafe, incomplete or exceeds bounds", 503);
const within = (root: string, path: string) => { const rel = relative(root, path); return rel === "" || (!rel.startsWith("../") && rel !== ".." && !isAbsolute(rel)); };
const packageName = (value: unknown): value is string => typeof value === "string" && value.length <= 214 && !value.split("/").some(part => part === "." || part === "..") && /^(?:@[a-z0-9._-]+\/)?[a-z0-9._-]+$/i.test(value);
interface Manifest { name: string; version: string; dependencies?: Record<string, string>; optionalDependencies?: Record<string, string>; peerDependencies?: Record<string, string>; peerDependenciesMeta?: Record<string, { optional?: boolean }> }
export interface RuntimeDependencyInventory {
  files: readonly string[];
  resolutionDigest: string;
  packageCount: number; fileCount: number; byteCount: number;
}
/** Declared deployed package closure only; does not execute package entrypoints or model arbitrary dynamic imports. */
export async function inventoryRuntimeDependencies(runtimeRoot: string, workspaceRoots: readonly string[], signal?: AbortSignal): Promise<RuntimeDependencyInventory> {
  signal?.throwIfAborted();
  if (!isAbsolute(runtimeRoot) || resolve(runtimeRoot) !== runtimeRoot || await realpath(runtimeRoot) !== runtimeRoot) throw denied();
  const manifests = new Map<string, Manifest>(), workspace = new Map<string, string>();
  const manifest = async (root: string): Promise<Manifest> => {
    signal?.throwIfAborted();
    const cached = manifests.get(root); if (cached) return cached;
    const path = join(root, "package.json"), info = await lstat(path);
    if (!info.isFile() || info.isSymbolicLink() || info.size > 1_048_576 || await realpath(path) !== path) throw denied();
    const parsed = JSON.parse(await readFile(path, "utf8")) as Manifest;
    if (!packageName(parsed.name) || typeof parsed.version !== "string" || parsed.version.length > 128) throw denied();
    manifests.set(root, parsed); return parsed;
  };
  for (const root of workspaceRoots) {
    signal?.throwIfAborted();
    if (!within(runtimeRoot, root) || await realpath(root) !== root) throw denied();
    const value = await manifest(root); if (workspace.has(value.name)) throw denied(); workspace.set(value.name, root);
  }
  const visited = new Set<string>(), queue = [...workspaceRoots].sort(), files = new Set<string>(), bindings: object[] = [];
  let bytes = 0, directories = 0;
  const walk = async (path: string, depth = 0): Promise<void> => {
    signal?.throwIfAborted();
    if (depth > 64) throw denied();
    const info = await lstat(path);
    if (info.isSymbolicLink() || await realpath(path) !== path) throw denied();
    if (info.isDirectory()) {
      if (++directories > 50_000) throw denied();
      for (const name of (await readdir(path)).sort()) if (name !== "node_modules") await walk(join(path, name), depth + 1);
    } else {
      if (!info.isFile() || info.size > 536_870_912) throw denied();
      if (!files.has(path)) { files.add(path); bytes += info.size; }
      if (files.size > 50_000 || bytes > 2_147_483_648) throw denied();
    }
  };
  while (queue.length) {
    signal?.throwIfAborted();
    const root = queue.shift()!; if (visited.has(root)) continue; visited.add(root);
    if (visited.size > 1024) throw denied();
    const value = await manifest(root);
    // Workspace package bytes are separately inventoried from dist; avoid pulling source/tests/dev trees.
    if (![...workspace.values()].includes(root)) await walk(root);
    const edges = new Map<string, { spec: string; kind: string; optional: boolean }>();
    for (const [field, kind] of [["dependencies", "production"], ["optionalDependencies", "optional"], ["peerDependencies", "peer"]] as const) {
      const group = value[field]; if (group === undefined) continue;
      if (!group || typeof group !== "object" || Array.isArray(group)) throw denied();
      for (const [name, spec] of Object.entries(group)) {
        if (!packageName(name) || typeof spec !== "string" || !spec || spec.length > 1024) throw denied();
        if (kind === "peer" && edges.has(name)) continue;
        edges.set(name, { spec, kind, optional: kind === "optional" || kind === "peer" });
      }
    }
    for (const [name, edge] of [...edges].sort(([a], [b]) => a.localeCompare(b))) {
      signal?.throwIfAborted();
      const search = createRequire(join(root, "package.json")).resolve.paths(name) ?? [];
      let selected: string | undefined, canonicalRoot: string | undefined, linkTarget: string | undefined, resolutionIdentity: string[] | undefined;
      for (const directory of search) {
        signal?.throwIfAborted();
        const candidate = join(directory, name);
        // Outside lookup locations are checked for existence only: never read manifests or execute contents.
        // Import-only packages must be rejected too; require.resolve alone cannot establish their absence.
        if (!within(runtimeRoot, candidate)) {
          for (const suffix of ["", ".js", ".json", ".node"]) {
            try { await lstat(candidate + suffix); }
            catch (error) { if ((error as NodeJS.ErrnoException).code === "ENOENT") continue; throw error; }
            throw denied();
          }
          continue;
        }
        // Check lookup parents before inspecting a candidate through them; never follow an external node_modules/scope alias.
        try { if (await realpath(dirname(candidate)) !== dirname(candidate)) throw denied(); }
        catch (error) { if ((error as NodeJS.ErrnoException).code === "ENOENT") continue; throw error; }
        let info; try { info = await lstat(candidate); } catch (error) {
          if ((error as NodeJS.ErrnoException).code !== "ENOENT") throw error;
          // Node can load dep.js/json/node without a package directory; never omit that declared executable edge.
          for (const suffix of [".js", ".json", ".node"]) {
            try { await lstat(candidate + suffix); }
            catch (missing) { if ((missing as NodeJS.ErrnoException).code === "ENOENT") continue; throw missing; }
            throw denied();
          }
          continue;
        }
        const actual = await realpath(candidate);
        if (!within(runtimeRoot, actual)) throw denied();
        if (info.isSymbolicLink()) {
          linkTarget = await readlink(candidate);
          if (workspace.get(name) !== actual || linkTarget !== relative(dirname(candidate), actual)) throw denied();
        } else if (!info.isDirectory() || (workspace.has(name) && workspace.get(name) !== actual)) throw denied();
        if (!workspace.has(name) && !within(join(runtimeRoot, "node_modules"), actual) && !actual.includes("/node_modules/")) throw denied();
        const selectedStat = await lstat(candidate, { bigint: true }), parentStat = await lstat(dirname(candidate), { bigint: true });
        resolutionIdentity = [selectedStat, parentStat].flatMap(info => [info.dev, info.ino, info.size, info.mtimeNs, info.ctimeNs, info.mode, info.uid].map(String));
        selected = candidate; canonicalRoot = actual; break;
      }
      if (!canonicalRoot) {
        if (!edge.optional) throw denied();
        bindings.push({ from: root, requested: name, ...edge, absent: true }); if (bindings.length > 16_384) throw denied(); continue;
      }
      const child = await manifest(canonicalRoot);
      const alias = /^npm:((?:@[^/]+\/)?[^@]+)@(.+)$/.exec(edge.spec);
      if (child.name !== (alias?.[1] ?? name)) throw denied();
      let requireEntry: string | null = null;
      try {
        requireEntry = createRequire(join(root, "package.json")).resolve(name);
        if (!within(canonicalRoot, requireEntry) || await realpath(requireEntry) !== requireEntry || !(await lstat(requireEntry)).isFile()) throw denied();
      } catch (error) {
        // Import-only exports and type-only manifests can legitimately have no require entry.
        if (!["ERR_PACKAGE_PATH_NOT_EXPORTED", "MODULE_NOT_FOUND"].includes((error as NodeJS.ErrnoException).code ?? "")) throw error;
        requireEntry = null;
      }
      const spec = alias?.[2] ?? edge.spec;
      if (/^\d+\.\d+\.\d+(?:[-+][a-z0-9.-]+)?$/i.test(spec) && child.version !== spec) throw denied();
      bindings.push({ from: root, requested: name, ...edge, selected, canonicalRoot, resolutionIdentity, requireEntry, ...(linkTarget === undefined ? {} : { linkTarget }), name: child.name, version: child.version });
      if (bindings.length > 16_384) throw denied(); queue.push(canonicalRoot);
    }
  }
  bindings.sort((a, b) => JSON.stringify(a).localeCompare(JSON.stringify(b)));
  return Object.freeze({ files: Object.freeze([...files].sort()), resolutionDigest: createHash("sha256").update(JSON.stringify(bindings)).digest("hex"), packageCount: visited.size, fileCount: files.size, byteCount: bytes });
}
