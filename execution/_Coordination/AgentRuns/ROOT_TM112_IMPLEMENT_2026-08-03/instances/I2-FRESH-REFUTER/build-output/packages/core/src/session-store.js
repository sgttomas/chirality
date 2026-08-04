import { randomUUID } from "node:crypto";
import { readdir, readFile, realpath, rename, rm } from "node:fs/promises";
import { basename, join, resolve } from "node:path";
import { RuntimeError } from "@chirality/runtime-contracts";
import { appendJsonLine, assertSafeIdentifier, atomicWriteJson, ensurePrivateDirectory, exists, isContained, readJson, readJsonIfExists } from "./fs.js";
export class SessionStore {
    runtimeDirectory;
    projects;
    constructor(runtimeDirectory, projects) {
        this.runtimeDirectory = runtimeDirectory;
        this.projects = projects;
    }
    async create(request) {
        if (request.role === undefined || request.engineSelection === undefined) {
            throw new RuntimeError("INVALID_REQUEST", "SessionStore requires a daemon-resolved role and engine selection", 500);
        }
        const project = await this.projects.requireAuthorized(request.projectId);
        const sessionId = randomUUID();
        const now = new Date().toISOString();
        const record = {
            schemaVersion: "chirality.session/v2",
            projectId: request.projectId,
            projectRoot: project.canonicalRoot,
            sessionId,
            createdAt: now,
            updatedAt: now,
            persona: request.persona ?? request.role,
            mode: request.mode ?? "governed",
            agentType: request.role === "agent0" ? 0 : request.role === "agent1" ? 1 : 2,
            role: request.role,
            engineSelection: request.engineSelection,
            status: "idle",
            ...(request.parentSessionId === undefined ? {} : { parentSessionId: request.parentSessionId }),
            ...(request.approvalRef === undefined ? {} : { approvalRef: request.approvalRef }),
            ...(request.allowedWriteTargets === undefined
                ? {}
                : { allowedWriteTargets: [...request.allowedWriteTargets] })
        };
        await atomicWriteJson(this.sessionFile(request.projectId, sessionId), record);
        return record;
    }
    async list(projectId) {
        const project = await this.projects.requireAuthorized(projectId);
        const records = new Map();
        const central = this.sessionsDirectory(projectId);
        for (const entry of await readdir(central, { withFileTypes: true }).catch(() => [])) {
            if (!entry.isDirectory())
                continue;
            const record = await this.readCentral(projectId, entry.name).catch(() => undefined);
            if (record !== undefined)
                records.set(record.sessionId, record);
        }
        for (const legacyRoot of project.legacySessionRoots) {
            for (const candidate of await this.listLegacyCandidates(project.canonicalRoot, legacyRoot)) {
                if (records.has(candidate.sessionId))
                    continue;
                if (await exists(this.deletedMarker(projectId, candidate.sessionId)))
                    continue;
                const record = this.normalizeLegacy(projectId, project.canonicalRoot, candidate.sessionId, candidate.raw);
                if (record !== undefined)
                    records.set(record.sessionId, record);
            }
        }
        return [...records.values()].sort((left, right) => left.createdAt.localeCompare(right.createdAt));
    }
    async get(projectId, sessionId) {
        assertSafeIdentifier(sessionId, "sessionId");
        const project = await this.projects.requireAuthorized(projectId);
        if (await exists(this.deletedMarker(projectId, sessionId))) {
            throw new RuntimeError("SESSION_NOT_FOUND", `Unknown session: ${sessionId}`, 404);
        }
        const central = await this.readCentral(projectId, sessionId).catch((error) => {
            if (error.code === "ENOENT")
                return undefined;
            throw error;
        });
        if (central !== undefined)
            return central;
        for (const legacyRoot of project.legacySessionRoots) {
            const migrated = await this.migrateLegacy(projectId, project.canonicalRoot, legacyRoot, sessionId);
            if (migrated !== undefined)
                return migrated;
        }
        throw new RuntimeError("SESSION_NOT_FOUND", `Unknown session: ${sessionId}`, 404);
    }
    async update(record) {
        await this.projects.requireAuthorized(record.projectId);
        const current = await this.get(record.projectId, record.sessionId);
        if (current.projectRoot !== record.projectRoot) {
            throw new RuntimeError("FORBIDDEN", "Session project root cannot be changed", 403);
        }
        await atomicWriteJson(this.sessionFile(record.projectId, record.sessionId), {
            ...record,
            updatedAt: new Date().toISOString()
        });
    }
    async delete(projectId, sessionId) {
        await this.get(projectId, sessionId);
        await rm(this.sessionDirectory(projectId, sessionId), { recursive: true, force: false });
        await atomicWriteJson(this.deletedMarker(projectId, sessionId), {
            schemaVersion: "chirality.session-deletion/v1",
            sessionId,
            deletedAt: new Date().toISOString()
        });
    }
    async appendEvent(projectId, input) {
        const event = {
            ...input,
            schemaVersion: 1,
            eventId: randomUUID(),
            timestamp: new Date().toISOString()
        };
        await this.get(projectId, input.sessionId);
        await appendJsonLine(this.eventsFile(projectId, input.sessionId), event);
        return event;
    }
    async persistEvent(projectId, event) {
        if (event.schemaVersion !== 1) {
            throw new RuntimeError("INVALID_REQUEST", "Unsupported harness event schema", 400);
        }
        await this.get(projectId, event.sessionId);
        const existing = await this.replay(projectId, event.sessionId);
        if (existing.some((candidate) => candidate.eventId === event.eventId))
            return;
        await appendJsonLine(this.eventsFile(projectId, event.sessionId), event);
    }
    async replay(projectId, sessionId) {
        return (await this.replayDetailed(projectId, sessionId)).events;
    }
    async replayDetailed(projectId, sessionId) {
        await this.get(projectId, sessionId);
        const source = await readFile(this.eventsFile(projectId, sessionId), "utf8").catch((error) => {
            if (error.code === "ENOENT")
                return "";
            throw error;
        });
        const events = [];
        let malformedLineCount = 0;
        for (const line of source.split("\n")) {
            if (line.trim() === "")
                continue;
            try {
                const value = JSON.parse(line);
                if (value.schemaVersion !== 1 || value.sessionId !== sessionId) {
                    malformedLineCount += 1;
                    continue;
                }
                events.push(value);
            }
            catch {
                malformedLineCount += 1;
            }
        }
        const eventTypeCounts = {};
        for (const event of events) {
            eventTypeCounts[event.type] = (eventTypeCounts[event.type] ?? 0) + 1;
        }
        return {
            events,
            malformedLineCount,
            summary: {
                eventCount: events.length,
                malformedLineCount,
                eventTypeCounts,
                ...(events[0]?.timestamp === undefined ? {} : { firstTimestamp: events[0].timestamp }),
                ...(events.at(-1)?.timestamp === undefined
                    ? {}
                    : { lastTimestamp: events.at(-1).timestamp })
            }
        };
    }
    async readCentral(projectId, sessionId) {
        const record = await readJson(this.sessionFile(projectId, sessionId));
        if (record.schemaVersion !== "chirality.session/v2" ||
            record.projectId !== projectId ||
            record.sessionId !== sessionId) {
            throw new RuntimeError("INTERNAL_FAILURE", "Invalid central session record", 500);
        }
        return record;
    }
    async migrateLegacy(projectId, projectRoot, relativeLegacyRoot, sessionId) {
        const root = await this.resolveLegacyRoot(projectRoot, relativeLegacyRoot);
        if (root === undefined)
            return undefined;
        const directoryCandidate = join(root, sessionId, "session.json");
        const flatCandidate = join(root, `${sessionId}.json`);
        const sourceFile = (await exists(directoryCandidate))
            ? directoryCandidate
            : (await exists(flatCandidate))
                ? flatCandidate
                : undefined;
        if (sourceFile === undefined)
            return undefined;
        const raw = await readJson(sourceFile);
        if (typeof raw["projectRoot"] === "string") {
            const legacyProjectRoot = await realpath(raw["projectRoot"]).catch(() => undefined);
            if (legacyProjectRoot !== projectRoot)
                return undefined;
        }
        const record = this.normalizeLegacy(projectId, projectRoot, sessionId, {
            ...raw,
            projectRoot
        });
        if (record === undefined)
            return undefined;
        const temporary = join(this.sessionsDirectory(projectId), `.${sessionId}.${randomUUID()}.tmp`);
        await ensurePrivateDirectory(temporary);
        await atomicWriteJson(join(temporary, "session.json"), {
            ...record,
            legacy: { sourcePath: sourceFile, migratedAt: new Date().toISOString() }
        });
        const legacyEvents = join(root, sessionId, "events.jsonl");
        if (await exists(legacyEvents)) {
            const lines = await readFile(legacyEvents, "utf8");
            const { writeFile, chmod } = await import("node:fs/promises");
            await writeFile(join(temporary, "events.jsonl"), lines, { encoding: "utf8", mode: 0o600 });
            await chmod(join(temporary, "events.jsonl"), 0o600);
        }
        await ensurePrivateDirectory(this.sessionsDirectory(projectId));
        const destination = this.sessionDirectory(projectId, sessionId);
        try {
            await rename(temporary, destination);
        }
        catch (error) {
            await rm(temporary, { recursive: true, force: true });
            if (error.code !== "EEXIST")
                throw error;
        }
        return this.readCentral(projectId, sessionId);
    }
    normalizeLegacy(projectId, projectRoot, sessionId, raw) {
        const rawRoot = typeof raw["projectRoot"] === "string" ? resolve(raw["projectRoot"]) : projectRoot;
        if (rawRoot !== projectRoot)
            return undefined;
        const selection = raw["engineSelection"];
        const inferredAdapter = typeof selection?.["adapterId"] === "string"
            ? selection["adapterId"]
            : raw["sdkSessionId"] !== undefined
                ? "claude-agent-sdk"
                : "stub";
        const inferredProvider = typeof selection?.["providerId"] === "string"
            ? selection["providerId"]
            : inferredAdapter === "stub"
                ? "stub"
                : "anthropic";
        const now = new Date().toISOString();
        return {
            ...raw,
            schemaVersion: "chirality.session/v2",
            projectId,
            projectRoot,
            sessionId,
            createdAt: typeof raw["createdAt"] === "string" ? raw["createdAt"] : now,
            updatedAt: typeof raw["updatedAt"] === "string" ? raw["updatedAt"] : now,
            persona: typeof raw["persona"] === "string" ? raw["persona"] : "agent1",
            mode: typeof raw["mode"] === "string" ? raw["mode"] : "governed",
            agentType: raw["agentType"] === 0 || raw["agentType"] === 2 || raw["agentType"] === 1
                ? raw["agentType"]
                : 1,
            role: raw["role"] === "agent0" || raw["role"] === "agent2" || raw["role"] === "agent1"
                ? raw["role"]
                : "agent1",
            engineSelection: {
                adapterId: inferredAdapter,
                providerId: inferredProvider,
                model: typeof selection?.["model"] === "string"
                    ? selection["model"]
                    : typeof raw["model"] === "string"
                        ? raw["model"]
                        : ""
            },
            status: raw["status"] === "running" ||
                raw["status"] === "completed" ||
                raw["status"] === "failed" ||
                raw["status"] === "interrupted" ||
                raw["status"] === "idle"
                ? raw["status"]
                : "idle",
            ...(typeof raw["engineSessionId"] === "string"
                ? { engineSessionId: raw["engineSessionId"] }
                : typeof raw["sdkSessionId"] === "string"
                    ? { engineSessionId: raw["sdkSessionId"] }
                    : {}),
            ...(typeof raw["claudeSessionId"] === "string"
                ? { claudeSessionId: raw["claudeSessionId"] }
                : {}),
            ...(typeof raw["parentSessionId"] === "string"
                ? { parentSessionId: raw["parentSessionId"] }
                : {})
        };
    }
    async listLegacyCandidates(projectRoot, relativeLegacyRoot) {
        const root = await this.resolveLegacyRoot(projectRoot, relativeLegacyRoot);
        if (root === undefined)
            return [];
        const candidates = [];
        for (const entry of await readdir(root, { withFileTypes: true }).catch(() => [])) {
            const source = entry.isDirectory()
                ? join(root, entry.name, "session.json")
                : entry.isFile() && entry.name.endsWith(".json")
                    ? join(root, entry.name)
                    : undefined;
            if (source === undefined || !(await exists(source)))
                continue;
            const sessionId = entry.isDirectory() ? entry.name : basename(entry.name, ".json");
            const raw = await readJsonIfExists(source, undefined);
            if (raw !== undefined)
                candidates.push({ sessionId, raw });
        }
        return candidates;
    }
    async resolveLegacyRoot(projectRoot, relativePath) {
        const candidate = resolve(projectRoot, relativePath);
        if (!isContained(projectRoot, candidate)) {
            throw new RuntimeError("FORBIDDEN", "Legacy session root escapes the project", 403);
        }
        const canonicalRoot = await realpath(projectRoot);
        // Legacy session roots are read-if-present: an absent root simply holds no
        // legacy sessions, so callers skip it instead of failing the request.
        // Escape checks above and below still apply whenever the root exists.
        let canonical;
        try {
            canonical = await realpath(candidate);
        }
        catch (error) {
            const code = error.code;
            if (code === "ENOENT" || code === "ENOTDIR")
                return undefined;
            throw error;
        }
        if (!isContained(canonicalRoot, canonical)) {
            throw new RuntimeError("FORBIDDEN", "Legacy session root escapes through a symlink", 403);
        }
        return canonical;
    }
    sessionsDirectory(projectId) {
        assertSafeIdentifier(projectId, "projectId");
        return join(this.runtimeDirectory, "projects", projectId, "sessions");
    }
    sessionDirectory(projectId, sessionId) {
        assertSafeIdentifier(sessionId, "sessionId");
        return join(this.sessionsDirectory(projectId), sessionId);
    }
    sessionFile(projectId, sessionId) {
        return join(this.sessionDirectory(projectId, sessionId), "session.json");
    }
    eventsFile(projectId, sessionId) {
        return join(this.sessionDirectory(projectId, sessionId), "events.jsonl");
    }
    deletedMarker(projectId, sessionId) {
        assertSafeIdentifier(sessionId, "sessionId");
        return join(this.sessionsDirectory(projectId), ".deleted", `${sessionId}.json`);
    }
}
