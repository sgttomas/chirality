import { createHash, randomUUID } from "node:crypto";
import { chmod, mkdir, open, readFile, realpath, rename, rm, stat } from "node:fs/promises";
import { dirname, isAbsolute, relative, resolve, sep } from "node:path";
export async function ensurePrivateDirectory(path) {
    await mkdir(path, { recursive: true, mode: 0o700 });
    await chmod(path, 0o700);
}
export async function atomicWriteJson(path, value) {
    await ensurePrivateDirectory(dirname(path));
    const temporary = `${path}.${process.pid}.${randomUUID()}.tmp`;
    const handle = await open(temporary, "wx", 0o600);
    try {
        await handle.writeFile(`${JSON.stringify(value, null, 2)}\n`, "utf8");
        await handle.sync();
    }
    finally {
        await handle.close();
    }
    await rename(temporary, path);
    await chmod(path, 0o600);
}
export async function appendJsonLine(path, value) {
    await ensurePrivateDirectory(dirname(path));
    const handle = await open(path, "a", 0o600);
    try {
        await handle.appendFile(`${JSON.stringify(value)}\n`, "utf8");
        await handle.sync();
    }
    finally {
        await handle.close();
    }
    await chmod(path, 0o600);
}
export async function readJson(path) {
    return JSON.parse(await readFile(path, "utf8"));
}
export async function readJsonIfExists(path, fallback) {
    try {
        return await readJson(path);
    }
    catch (error) {
        if (error.code === "ENOENT")
            return fallback;
        throw error;
    }
}
export async function exists(path) {
    try {
        await stat(path);
        return true;
    }
    catch (error) {
        if (error.code === "ENOENT")
            return false;
        throw error;
    }
}
export function sha256(value) {
    return createHash("sha256").update(value).digest("hex");
}
export function assertSafeIdentifier(value, label) {
    if (!/^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$/.test(value)) {
        throw new Error(`${label} is not a safe identifier`);
    }
}
export function assertRelativeManifestPath(value, label) {
    if (value.length === 0 || isAbsolute(value)) {
        throw new Error(`${label} must be a non-empty relative path`);
    }
}
export function isContained(root, candidate) {
    const rel = relative(root, candidate);
    return rel === "" || (!(rel === ".." || rel.startsWith(`..${sep}`)) && !isAbsolute(rel));
}
export async function resolveContained(root, child) {
    const canonicalRoot = await realpath(root);
    const candidate = resolve(canonicalRoot, child);
    const canonical = await realpath(candidate);
    const rel = relative(canonicalRoot, canonical);
    if (rel === ".." || rel.startsWith(`..${sep}`) || isAbsolute(rel)) {
        throw new Error(`Path escapes project root: ${child}`);
    }
    return canonical;
}
export async function removeIfExists(path) {
    await rm(path, { force: true });
}
