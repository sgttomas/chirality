import { randomUUID } from "node:crypto";
import { readFile, realpath } from "node:fs/promises";
import { dirname, join, resolve } from "node:path";
import { RuntimeError } from "@chirality/runtime-contracts";
import { assertRelativeManifestPath, assertSafeIdentifier, atomicWriteJson, isContained, readJsonIfExists, sha256 } from "./fs.js";
export class ProjectRegistry {
    runtimeDirectory;
    registryFile;
    constructor(runtimeDirectory) {
        this.runtimeDirectory = runtimeDirectory;
        this.registryFile = join(runtimeDirectory, "projects", "registry.json");
    }
    async register(manifestPath, approval, clientId = `project-${randomUUID()}`) {
        const canonicalManifest = await realpath(manifestPath);
        const source = await readFile(canonicalManifest, "utf8");
        const manifest = this.parseManifest(source);
        const manifestDirectory = await realpath(dirname(canonicalManifest));
        const { workingRoot: canonicalRoot } = await this.validateReferences(manifestDirectory, manifest);
        const registry = await this.readRegistry();
        const record = {
            projectId: manifest.projectId,
            displayName: manifest.displayName,
            canonicalRoot,
            manifestPath: canonicalManifest,
            manifestHash: sha256(source),
            registeredAt: new Date().toISOString(),
            approval,
            clientId,
            enabledAdapterIds: [...manifest.enabledAdapterIds],
            legacySessionRoots: [...(manifest.legacySessionRoots ?? [])]
        };
        await this.writeRegistry({
            ...registry,
            projects: [...registry.projects.filter((item) => item.projectId !== record.projectId), record]
        });
        return record;
    }
    async list() {
        const registry = await this.readRegistry();
        return Promise.all(registry.projects.map(async (project) => this.status(project.projectId)));
    }
    async status(projectId) {
        const project = await this.getRecord(projectId);
        const source = await readFile(project.manifestPath, "utf8").catch(() => "");
        const manifestDrift = sha256(source) !== project.manifestHash;
        return { project, manifestDrift, adaptersEnabled: !manifestDrift };
    }
    async requireAuthorized(projectId) {
        const status = await this.status(projectId);
        if (status.manifestDrift) {
            throw new RuntimeError("PROJECT_MANIFEST_DRIFT", "The project manifest changed after approval; re-registration is required", 409, { projectId });
        }
        return status.project;
    }
    async readManifest(projectId) {
        const project = await this.getRecord(projectId);
        return this.parseManifest(await readFile(project.manifestPath, "utf8"));
    }
    async roots(projectId) {
        const project = await this.requireAuthorized(projectId);
        const manifest = await this.readManifest(projectId);
        return {
            workingRoot: project.canonicalRoot,
            instructionRoot: await realpath(resolve(dirname(project.manifestPath), manifest.instructionRoot))
        };
    }
    async getRecord(projectId) {
        assertSafeIdentifier(projectId, "projectId");
        const registry = await this.readRegistry();
        const record = registry.projects.find((project) => project.projectId === projectId);
        if (record === undefined) {
            throw new RuntimeError("PROJECT_NOT_FOUND", `Unknown project: ${projectId}`, 404);
        }
        return record;
    }
    parseManifest(source) {
        let value;
        try {
            value = JSON.parse(source);
        }
        catch {
            throw new RuntimeError("PROJECT_MANIFEST_INVALID", "Project manifest is not valid JSON");
        }
        if (!this.isManifest(value)) {
            throw new RuntimeError("PROJECT_MANIFEST_INVALID", "Project manifest does not conform to chirality.project/v1");
        }
        return value;
    }
    isManifest(value) {
        if (typeof value !== "object" || value === null)
            return false;
        const item = value;
        const profiles = item["profiles"];
        const embeddedUi = item["embeddedUi"];
        return (item["schemaVersion"] === "chirality.project/v1" &&
            typeof item["projectId"] === "string" &&
            typeof item["displayName"] === "string" &&
            typeof item["workingRoot"] === "string" &&
            typeof item["instructionRoot"] === "string" &&
            typeof item["defaultExecutionRoot"] === "string" &&
            typeof profiles === "object" &&
            Array.isArray(profiles?.["domain"]) &&
            Array.isArray(profiles?.["capability"]) &&
            Array.isArray(profiles?.["dataBoundary"]) &&
            Array.isArray(item["enabledAdapterIds"]) &&
            typeof embeddedUi === "object" &&
            typeof embeddedUi?.["declared"] === "boolean");
    }
    async validateReferences(manifestDirectory, manifest) {
        assertSafeIdentifier(manifest.projectId, "projectId");
        assertRelativeManifestPath(manifest.workingRoot, "workingRoot");
        assertRelativeManifestPath(manifest.instructionRoot, "instructionRoot");
        const workingRoot = await this.canonicalizeReference(manifestDirectory, manifest.workingRoot, "workingRoot");
        const instructionRoot = await this.canonicalizeReference(manifestDirectory, manifest.instructionRoot, "instructionRoot");
        if (!isContained(instructionRoot, workingRoot) && !isContained(workingRoot, instructionRoot)) {
            throw new RuntimeError("PROJECT_MANIFEST_INVALID", "Working and instruction roots must belong to one canonical project tree");
        }
        const paths = [
            ["defaultExecutionRoot", manifest.defaultExecutionRoot],
            ...(manifest.agentsOverlay === undefined
                ? []
                : [["agentsOverlay", manifest.agentsOverlay]]),
            ...(manifest.embeddedUi.path === undefined
                ? []
                : [["embeddedUi.path", manifest.embeddedUi.path]]),
            ...manifest.profiles.domain.map((path) => ["profiles.domain", path]),
            ...manifest.profiles.capability.map((path) => ["profiles.capability", path]),
            ...manifest.profiles.dataBoundary.map((path) => ["profiles.dataBoundary", path]),
            ...(manifest.legacySessionRoots ?? []).map((path) => ["legacySessionRoots", path])
        ];
        for (const [label, path] of paths) {
            assertRelativeManifestPath(path, label);
            // legacySessionRoots is read-if-present downstream: SessionStore.list()
            // and SessionStore.get() (session-store.ts, listLegacyCandidates /
            // migrateLegacy) only enumerate or migrate legacy sessions from roots
            // that actually exist, and treat an absent root as "no legacy sessions".
            // Registration therefore tolerates a missing legacySessionRoots entry
            // (its containment check is skipped while absent) but still rejects any
            // entry that exists and escapes the declared roots. Every other
            // reference must exist at registration time.
            const tolerateAbsence = label === "legacySessionRoots";
            const canonical = await this.canonicalizeReference(manifestDirectory, path, label, tolerateAbsence);
            if (canonical === undefined)
                continue;
            if (!isContained(workingRoot, canonical) && !isContained(instructionRoot, canonical)) {
                throw new RuntimeError("PROJECT_MANIFEST_INVALID", `${label} escapes the declared working and instruction roots`);
            }
        }
        return { workingRoot, instructionRoot };
    }
    async canonicalizeReference(manifestDirectory, relativePath, label, tolerateAbsence = false) {
        try {
            return await realpath(resolve(manifestDirectory, relativePath));
        }
        catch (error) {
            const code = error.code;
            if (code !== "ENOENT" && code !== "ENOTDIR")
                throw error;
            if (tolerateAbsence)
                return undefined;
            throw new RuntimeError("PROJECT_MANIFEST_INVALID", `${label} references a path that does not exist: ${relativePath}`);
        }
    }
    readRegistry() {
        return readJsonIfExists(this.registryFile, {
            schemaVersion: "chirality.project-registry/v1",
            projects: []
        });
    }
    writeRegistry(registry) {
        return atomicWriteJson(this.registryFile, registry);
    }
}
