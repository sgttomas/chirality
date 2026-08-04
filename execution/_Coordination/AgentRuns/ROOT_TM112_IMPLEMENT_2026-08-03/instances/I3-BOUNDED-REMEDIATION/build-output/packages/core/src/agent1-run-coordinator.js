import { randomUUID } from "node:crypto";
import { readFile, realpath, stat } from "node:fs/promises";
import { join, resolve } from "node:path";
import { RuntimeError } from "@chirality/runtime-contracts";
import { atomicWriteJson, isContained, sha256 } from "./fs.js";
export class GovernedAgent1RunCoordinator {
    options;
    active = new Map();
    constructor(options) {
        this.options = options;
    }
    isActive(projectId, sessionId) {
        return this.active.get(sessionId)?.projectId === projectId;
    }
    async interrupt(projectId, sessionId) {
        const active = this.active.get(sessionId);
        if (active === undefined || active.projectId !== projectId)
            return;
        active.controller.abort();
        await Promise.all([
            this.options.manager.interrupt?.(sessionId) ?? Promise.resolve(),
            active.childSessionId === undefined
                ? Promise.resolve()
                : this.options.turns.interrupt(projectId, active.childSessionId)
        ]);
    }
    async *run(projectId, request) {
        const project = await this.options.projects.requireAuthorized(projectId);
        if (request.brief.trim() === "") {
            throw new RuntimeError("INVALID_REQUEST", "Agent 1 brief cannot be empty");
        }
        if (request.approvalReference.trim() === "") {
            throw new RuntimeError("INVALID_REQUEST", "Agent 1 approvalReference cannot be empty");
        }
        const managerAgentId = request.agentId ?? "WORKING_ITEMS";
        const managerDefinition = (await this.listManagerDefinitions(projectId)).find((agent) => agent.agentId === managerAgentId);
        if (managerDefinition === undefined || managerDefinition.agentType !== 1) {
            throw new RuntimeError("DELEGATION_POLICY_VIOLATION", `Direct run target must be an Agent 1: ${managerAgentId}`, 403);
        }
        const managerSelection = await this.options.resolveManagerSelection(projectId);
        if (!project.enabledAdapterIds.includes(managerSelection.adapterId)) {
            throw new RuntimeError("DELEGATION_POLICY_VIOLATION", `Agent 1 adapter is not enabled for project ${projectId}: ${managerSelection.adapterId}`, 403);
        }
        const managerSession = await this.options.sessions.create({
            projectId,
            role: "agent1",
            engineSelection: managerSelection,
            persona: managerAgentId,
            mode: "direct"
        });
        const turnId = randomUUID();
        const runId = randomUUID();
        const createdAt = new Date().toISOString();
        const controller = new AbortController();
        this.active.set(managerSession.sessionId, { projectId, controller });
        let managerActualSelection = managerSelection;
        let child;
        let review;
        await this.persistAgentRun(projectId, runId, {
            schemaVersion: "chirality.agent-run/v1",
            runId,
            projectId,
            managerSessionId: managerSession.sessionId,
            managerAgentId,
            managerSelection,
            sealedBrief: request.brief,
            briefHash: sha256(request.brief),
            status: "running",
            approvalReference: request.approvalReference,
            createdAt
        });
        const accepted = await this.options.sessions.appendEvent(projectId, {
            sessionId: managerSession.sessionId,
            turnId,
            type: "turn.accepted",
            data: { runId, agentId: managerAgentId, briefHash: sha256(request.brief) }
        });
        try {
            yield { type: "harness:event", data: accepted };
            const hooks = {
                delegate: async ({ sealedBrief }) => {
                    if (controller.signal.aborted) {
                        throw new RuntimeError("INTERRUPTED", "Agent 1 run was interrupted", 499);
                    }
                    if (request.localModel === undefined) {
                        throw new RuntimeError("DELEGATION_POLICY_VIOLATION", "This run did not authorize a local child", 403);
                    }
                    if (child !== undefined) {
                        throw new RuntimeError("DELEGATION_POLICY_VIOLATION", "Agent 1 may launch at most one local child in this milestone", 403);
                    }
                    if (request.readOnlyTool?.name !== "read_file") {
                        throw new RuntimeError("DELEGATION_POLICY_VIOLATION", "Local child requires one declared read_file tool", 403);
                    }
                    const residency = await this.options.residency.status();
                    if (residency.phase !== "READY" ||
                        residency.managedModelId !== request.localModel ||
                        residency.epoch === undefined) {
                        throw new RuntimeError("MODEL_NOT_RESIDENT", `Exact local model is not resident: ${request.localModel}`, 409);
                    }
                    const selection = {
                        adapterId: "pi",
                        providerId: "omlx",
                        model: request.localModel
                    };
                    if (!project.enabledAdapterIds.includes(selection.adapterId)) {
                        throw new RuntimeError("DELEGATION_POLICY_VIOLATION", "Pi is not enabled by the registered project manifest", 403);
                    }
                    const childSession = await this.options.sessions.create({
                        projectId,
                        role: "agent2",
                        engineSelection: selection,
                        persona: "TASK",
                        mode: "readOnly",
                        parentSessionId: managerSession.sessionId,
                        approvalRef: request.approvalReference,
                        allowedWriteTargets: []
                    });
                    child = {
                        sessionId: childSession.sessionId,
                        selection,
                        epoch: residency.epoch.epochId,
                        sealedBrief,
                        sealedBriefHash: sha256(sealedBrief),
                        status: "launched"
                    };
                    const active = this.active.get(managerSession.sessionId);
                    if (active !== undefined)
                        active.childSessionId = child.sessionId;
                    await this.persistAgentRun(projectId, runId, {
                        schemaVersion: "chirality.agent-run/v1",
                        runId,
                        projectId,
                        managerSessionId: managerSession.sessionId,
                        managerAgentId,
                        managerSelection: managerActualSelection,
                        sealedBrief: request.brief,
                        briefHash: sha256(request.brief),
                        child: {
                            sessionId: child.sessionId,
                            role: "agent2",
                            selection: child.selection,
                            residencyEpoch: child.epoch,
                            sealedBrief: child.sealedBrief,
                            sealedBriefHash: child.sealedBriefHash,
                            permissions: ["read"],
                            tool: "read_file",
                            status: child.status
                        },
                        status: "running",
                        approvalReference: request.approvalReference,
                        createdAt
                    });
                    const childTurnId = randomUUID();
                    const { tool, receipt } = await this.readFileTool({
                        projectId,
                        projectRoot: project.canonicalRoot,
                        sessionId: childSession.sessionId,
                        turnId: childTurnId,
                        relativePath: request.readOnlyTool.relativePath
                    });
                    const release = await this.options.tools.bind(childSession.sessionId, [tool]);
                    const interruptChild = () => {
                        void this.options.turns
                            .interrupt(projectId, childSession.sessionId)
                            .catch(() => undefined);
                    };
                    controller.signal.addEventListener("abort", interruptChild);
                    let text = "";
                    let successful = false;
                    let interrupted = false;
                    let requiredToolFailure = false;
                    try {
                        if (controller.signal.aborted) {
                            throw new RuntimeError("INTERRUPTED", "Agent 1 run was interrupted", 499);
                        }
                        for await (const event of this.options.turns.run(projectId, childSession.sessionId, { prompt: sealedBrief, turnId: childTurnId }, ["read_file"], [receipt])) {
                            if (event.type === "chat:delta") {
                                text += event.data.text;
                            }
                            else if (event.type === "chat:complete") {
                                text = event.data.text;
                            }
                            if (event.type === "harness:event" &&
                                (event.data.type === "turn.interrupted" ||
                                    event.data.type === "turn.cancelled")) {
                                interrupted = true;
                            }
                            if (event.type === "turn:error" &&
                                event.data.details
                                    ?.runtimeCode === "REQUIRED_DELEGATION_MISSING") {
                                requiredToolFailure = true;
                            }
                            if (event.type === "process:exit")
                                successful = event.data.exitCode === 0;
                        }
                    }
                    catch (error) {
                        child.status = controller.signal.aborted ? "interrupted" : "failed";
                        throw error;
                    }
                    finally {
                        controller.signal.removeEventListener("abort", interruptChild);
                        await release();
                    }
                    if (!successful || interrupted || controller.signal.aborted) {
                        child.status =
                            interrupted || controller.signal.aborted ? "interrupted" : "failed";
                        throw interrupted || controller.signal.aborted
                            ? new RuntimeError("INTERRUPTED", "Agent 1 run was interrupted", 499)
                            : requiredToolFailure
                                ? new RuntimeError("REQUIRED_DELEGATION_MISSING", "Local child did not complete the required read_file tool", 422)
                                : new RuntimeError("ENGINE_UNAVAILABLE", "Local child did not complete", 502);
                    }
                    if (!receipt.completed()) {
                        child.status = "failed";
                        await this.options.sessions.update({
                            ...(await this.options.sessions.get(projectId, childSession.sessionId)),
                            status: "failed"
                        });
                        throw new RuntimeError("REQUIRED_DELEGATION_MISSING", "Local child did not complete the required read_file tool", 422);
                    }
                    const completedChild = await this.options.sessions.get(projectId, childSession.sessionId);
                    child.selection = completedChild.engineSelection;
                    child.returnHash = sha256(text);
                    child.evidenceReference = {
                        projectId,
                        sessionId: childSession.sessionId,
                        source: "canonical-session-events"
                    };
                    child.status = "completed";
                    await this.persistAgentRun(projectId, runId, {
                        schemaVersion: "chirality.agent-run/v1",
                        runId,
                        projectId,
                        managerSessionId: managerSession.sessionId,
                        managerAgentId,
                        managerSelection: managerActualSelection,
                        sealedBrief: request.brief,
                        briefHash: sha256(request.brief),
                        child: {
                            sessionId: child.sessionId,
                            role: "agent2",
                            selection: child.selection,
                            residencyEpoch: child.epoch,
                            sealedBrief: child.sealedBrief,
                            sealedBriefHash: child.sealedBriefHash,
                            returnHash: child.returnHash,
                            evidenceReference: child.evidenceReference,
                            permissions: ["read"],
                            tool: "read_file",
                            status: child.status
                        },
                        status: "running",
                        approvalReference: request.approvalReference,
                        createdAt
                    });
                    return {
                        childSessionId: childSession.sessionId,
                        returnText: text,
                        model: request.localModel,
                        residencyEpoch: residency.epoch.epochId
                    };
                },
                review: async (input) => {
                    if (child === undefined || input.childSessionId !== child.sessionId) {
                        throw new RuntimeError("DELEGATION_POLICY_VIOLATION", "Review must refer to this manager's governed child", 403);
                    }
                    review = {
                        decision: input.decision,
                        rationaleHash: sha256(input.rationale)
                    };
                    child.acceptance = review;
                    const event = await this.options.sessions.appendEvent(projectId, {
                        sessionId: managerSession.sessionId,
                        turnId,
                        type: "coordination.acknowledged",
                        data: {
                            childSessionId: child.sessionId,
                            decision: input.decision,
                            rationaleHash: review.rationaleHash
                        }
                    });
                    await this.options.sessions.persistEvent(projectId, event);
                    await this.persistAgentRun(projectId, runId, {
                        schemaVersion: "chirality.agent-run/v1",
                        runId,
                        projectId,
                        managerSessionId: managerSession.sessionId,
                        managerAgentId,
                        managerSelection: managerActualSelection,
                        sealedBrief: request.brief,
                        briefHash: sha256(request.brief),
                        child: {
                            sessionId: child.sessionId,
                            role: "agent2",
                            selection: child.selection,
                            residencyEpoch: child.epoch,
                            sealedBrief: child.sealedBrief,
                            sealedBriefHash: child.sealedBriefHash,
                            ...(child.returnHash === undefined ? {} : { returnHash: child.returnHash }),
                            ...(child.evidenceReference === undefined
                                ? {}
                                : { evidenceReference: child.evidenceReference }),
                            acceptance: child.acceptance,
                            permissions: ["read"],
                            tool: "read_file",
                            status: child.status
                        },
                        review,
                        status: "running",
                        approvalReference: request.approvalReference,
                        createdAt
                    });
                }
            };
            let failure;
            try {
                for await (const event of this.options.manager.execute(managerSession, request, hooks, controller.signal)) {
                    if (controller.signal.aborted) {
                        throw new RuntimeError("INTERRUPTED", "Agent 1 run was interrupted", 499);
                    }
                    if (event.type === "process:exit") {
                        throw new RuntimeError("INTERNAL_FAILURE", "Manager runtime must leave terminal ownership to the coordinator", 500);
                    }
                    if (event.type === "harness:event" &&
                        ["turn.completed", "turn.failed", "turn.cancelled", "turn.interrupted"].includes(event.data.type)) {
                        throw new RuntimeError("INTERNAL_FAILURE", "Manager runtime emitted a terminal harness event", 500);
                    }
                    if (event.type === "harness:event") {
                        await this.options.sessions.persistEvent(projectId, event.data);
                    }
                    if (event.type === "session:init") {
                        managerActualSelection = {
                            adapterId: event.data.adapterId,
                            providerId: event.data.providerId,
                            model: event.data.model
                        };
                    }
                    yield event;
                }
                if (controller.signal.aborted) {
                    failure = new RuntimeError("INTERRUPTED", "Agent 1 run was interrupted", 499);
                }
                else if (request.localModel !== undefined &&
                    (child === undefined || review === undefined)) {
                    failure = new RuntimeError("REQUIRED_DELEGATION_MISSING", "Agent 1 did not complete and review the required local delegation", 409);
                }
            }
            catch (error) {
                failure = controller.signal.aborted
                    ? new RuntimeError("INTERRUPTED", "Agent 1 run was interrupted", 499)
                    : error instanceof RuntimeError
                        ? error
                        : new RuntimeError("INTERNAL_FAILURE", "Agent 1 run failed", 500);
            }
            if (failure !== undefined && child?.status === "launched") {
                child.status = failure.code === "INTERRUPTED" ? "interrupted" : "failed";
                const childSession = await this.options.sessions
                    .get(projectId, child.sessionId)
                    .catch(() => undefined);
                if (childSession !== undefined) {
                    await this.options.sessions.update({
                        ...childSession,
                        status: child.status
                    });
                }
            }
            const completedAt = new Date().toISOString();
            const record = {
                schemaVersion: "chirality.agent-run/v1",
                runId,
                projectId,
                managerSessionId: managerSession.sessionId,
                managerAgentId,
                managerSelection: managerActualSelection,
                sealedBrief: request.brief,
                briefHash: sha256(request.brief),
                status: failure === undefined
                    ? "completed"
                    : failure.code === "INTERRUPTED"
                        ? "interrupted"
                        : "failed",
                approvalReference: request.approvalReference,
                createdAt,
                completedAt,
                ...(child === undefined
                    ? {}
                    : {
                        child: {
                            sessionId: child.sessionId,
                            role: "agent2",
                            selection: child.selection,
                            residencyEpoch: child.epoch,
                            sealedBrief: child.sealedBrief,
                            sealedBriefHash: child.sealedBriefHash,
                            ...(child.returnHash === undefined ? {} : { returnHash: child.returnHash }),
                            ...(child.evidenceReference === undefined
                                ? {}
                                : { evidenceReference: child.evidenceReference }),
                            ...(child.acceptance === undefined ? {} : { acceptance: child.acceptance }),
                            permissions: ["read"],
                            tool: "read_file",
                            status: child.status
                        }
                    }),
                ...(review === undefined ? {} : { review }),
                ...(failure === undefined ? {} : { failureCode: failure.code })
            };
            await this.persistAgentRun(projectId, runId, record);
            const terminal = await this.options.sessions.appendEvent(projectId, {
                sessionId: managerSession.sessionId,
                turnId,
                type: failure === undefined
                    ? "turn.completed"
                    : failure.code === "INTERRUPTED"
                        ? "turn.interrupted"
                        : "turn.failed",
                data: failure === undefined
                    ? { runId }
                    : { runId, code: failure.code, message: failure.message }
            });
            await this.options.sessions.update({
                ...(await this.options.sessions.get(projectId, managerSession.sessionId)),
                status: failure === undefined
                    ? "completed"
                    : failure.code === "INTERRUPTED"
                        ? "interrupted"
                        : "failed"
            });
            yield { type: "harness:event", data: terminal };
            if (failure !== undefined) {
                yield {
                    type: "turn:error",
                    data: {
                        phase: "mid-stream",
                        errorType: "SDK_FAILURE",
                        message: failure.message,
                        status: failure.status,
                        severity: "error",
                        fatal: true,
                        details: { runtimeCode: failure.code }
                    }
                };
            }
            yield {
                type: "process:exit",
                data: {
                    exitCode: failure === undefined ? 0 : 1,
                    ...(failure === undefined
                        ? {}
                        : {
                            error: failure.message,
                            errorType: failure.code,
                            status: failure.status,
                            severity: "error",
                            fatal: true
                        })
                }
            };
        }
        finally {
            this.active.delete(managerSession.sessionId);
        }
    }
    async readFileTool(input) {
        const { projectId, projectRoot, sessionId, turnId, relativePath } = input;
        if (relativePath.length === 0 || resolve(relativePath) === relativePath) {
            throw new RuntimeError("INVALID_REQUEST", "read_file path must be relative");
        }
        const canonicalRoot = await realpath(projectRoot);
        const canonicalPath = await realpath(resolve(canonicalRoot, relativePath));
        if (!isContained(canonicalRoot, canonicalPath)) {
            throw new RuntimeError("FORBIDDEN", "read_file path escapes the project", 403);
        }
        const metadata = await stat(canonicalPath);
        if (!metadata.isFile() || metadata.size > 1024 * 1024) {
            throw new RuntimeError("FORBIDDEN", "read_file target must be a file no larger than 1 MiB", 403);
        }
        let completed = false;
        const tool = {
            name: "read_file",
            description: "Read the one file declared by the governing Agent 1 run.",
            inputSchema: {
                type: "object",
                properties: {},
                additionalProperties: false
            },
            permission: { effect: "allow", operation: "read", roots: [canonicalPath] },
            execute: async (_input, signal) => {
                const toolUseId = randomUUID();
                const evidence = {
                    toolName: "read_file",
                    adapterToolName: "read_file",
                    toolUseId,
                    source: "chirality-runtime-tool-bridge",
                    pathMetadata: { relativePath }
                };
                await this.options.sessions.appendEvent(projectId, {
                    sessionId,
                    turnId,
                    type: "tool.permission",
                    data: {
                        ...evidence,
                        decision: "allow",
                        operation: "read",
                        reason: "Bounded Agent 1 authorization"
                    }
                });
                await this.options.sessions.appendEvent(projectId, {
                    sessionId,
                    turnId,
                    type: "tool.started",
                    data: evidence
                });
                const startedAt = Date.now();
                try {
                    if (signal.aborted) {
                        throw new RuntimeError("INTERRUPTED", "Read interrupted", 499);
                    }
                    const content = await readFile(canonicalPath, "utf8");
                    await this.options.sessions.appendEvent(projectId, {
                        sessionId,
                        turnId,
                        type: "tool.completed",
                        data: {
                            ...evidence,
                            durationMs: Date.now() - startedAt,
                            resultMetadata: {
                                byteLength: Buffer.byteLength(content),
                                rawOutputPersisted: false
                            }
                        }
                    });
                    completed = true;
                    return { path: relativePath, content };
                }
                catch (error) {
                    await this.options.sessions.appendEvent(projectId, {
                        sessionId,
                        turnId,
                        type: "tool.failed",
                        data: {
                            ...evidence,
                            durationMs: Date.now() - startedAt,
                            error: error instanceof RuntimeError ? error.code : "READ_FAILED"
                        }
                    });
                    throw error;
                }
            }
        };
        return {
            tool,
            receipt: {
                toolName: "read_file",
                completed: () => completed
            }
        };
    }
    async listManagerDefinitions(projectId) {
        const roots = await this.options.projects.roots(projectId);
        const result = [];
        const { readdir } = await import("node:fs/promises");
        for (const directory of [join(roots.instructionRoot, "agents"), join(roots.workingRoot, "agents")]) {
            for (const entry of await readdir(directory, { withFileTypes: true }).catch(() => [])) {
                const nameMatch = /^AGENT_(.+)\.md$/u.exec(entry.name);
                if (!entry.isFile() || nameMatch?.[1] === undefined)
                    continue;
                const source = await readFile(join(directory, entry.name), "utf8");
                const match = /AGENT_TYPE\s*:\s*([012])/iu.exec(source);
                if (match?.[1] !== undefined) {
                    result.push({
                        agentId: nameMatch[1],
                        agentType: Number(match[1])
                    });
                }
            }
        }
        return result;
    }
    async persistAgentRun(projectId, runId, record) {
        const project = await this.options.projects.requireAuthorized(projectId);
        const manifest = await this.options.projects.readManifest(projectId);
        const executionRoot = await realpath(resolve(project.canonicalRoot, manifest.defaultExecutionRoot));
        if (!isContained(project.canonicalRoot, executionRoot)) {
            throw new RuntimeError("FORBIDDEN", "Execution root escapes the project", 403);
        }
        await atomicWriteJson(join(executionRoot, "_Coordination", "AgentRuns", "runtime", runId, "run.json"), record);
    }
}
