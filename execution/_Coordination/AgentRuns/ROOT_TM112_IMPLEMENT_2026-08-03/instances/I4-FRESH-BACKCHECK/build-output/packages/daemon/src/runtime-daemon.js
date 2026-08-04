import { randomUUID } from "node:crypto";
import { chmod, lstat, readFile, unlink } from "node:fs/promises";
import { createServer } from "node:http";
import { dirname } from "node:path";
import { performance } from "node:perf_hooks";
import { HarnessError, RUNTIME_API_VERSION, RuntimeError, deriveTranscriptView } from "@chirality/runtime-contracts";
import { ensurePrivateDirectory, atomicWriteJson } from "@chirality/runtime-core";
const JSON_LIMIT_BYTES = 1024 * 1024;
const STOP_GRACE_MS = 2_000;
const STOP_FORCE_SETTLE_MS = 500;
export class RuntimeDaemon {
    options;
    daemonId = randomUUID();
    startedAt = new Date().toISOString();
    server;
    lifecycle = "INITIAL";
    generationNumber = 0;
    generation;
    stopPromise;
    terminalStopError;
    ownerFile;
    constructor(options) {
        this.options = options;
        this.ownerFile = `${options.socketPath}.owner.json`;
    }
    async start() {
        if (this.lifecycle !== "INITIAL" && this.lifecycle !== "STOPPED") {
            throw new Error(`Runtime daemon cannot start while ${this.lifecycle.toLowerCase()}`);
        }
        this.lifecycle = "STARTING";
        this.terminalStopError = undefined;
        const generationNumber = ++this.generationNumber;
        const ownerGenerationId = randomUUID();
        let context;
        let controlSocketBound = false;
        try {
            await ensurePrivateDirectory(this.options.runtimeDirectory);
            await ensurePrivateDirectory(dirname(this.options.socketPath));
            await this.recoverStaleSocket();
            await atomicWriteJson(this.ownerFile, {
                schemaVersion: "chirality.daemon-owner/v1",
                daemonId: this.daemonId,
                generationId: ownerGenerationId,
                pid: process.pid,
                uid: process.getuid?.() ?? -1,
                socketPath: this.options.socketPath,
                startedAt: this.startedAt
            });
            const operator = await this.options.service.auth.ensureClient("operator", [
                "runtime:read",
                "projects:write",
                "sessions:read",
                "sessions:write",
                "models:read",
                "models:write",
                "credentials:read",
                "credentials:write"
            ]);
            let generation;
            const server = createServer((request, response) => {
                void this.route(request, response, generation).catch((error) => this.error(response, error));
            });
            generation = {
                number: generationNumber,
                ownerGenerationId,
                server,
                sockets: new Set(),
                streams: new Set(),
                stateWaiters: new Set(),
                closeStarted: false,
                closeComplete: false,
                forced: false,
                socketUnlinked: false,
                ownerRemoved: false,
                interruptionProblems: false
            };
            context = generation;
            server.on("connection", (socket) => {
                generation.sockets.add(socket);
                socket.once("close", () => {
                    generation.sockets.delete(socket);
                    this.notifyGeneration(generation);
                });
            });
            this.generation = generation;
            this.server = server;
            await new Promise((resolve, reject) => {
                const onError = (error) => reject(error);
                server.once("error", onError);
                server.listen(this.options.socketPath, () => {
                    server.off("error", onError);
                    controlSocketBound = true;
                    resolve();
                });
            });
            await chmod(this.options.socketPath, 0o600);
            if (this.generation !== generation || this.lifecycle !== "STARTING") {
                throw new Error("Runtime daemon generation changed during start");
            }
            this.lifecycle = "RUNNING";
            return { socketPath: this.options.socketPath, operatorTokenFile: operator.tokenFile };
        }
        catch (error) {
            if (context !== undefined) {
                for (const socket of context.sockets)
                    socket.destroy();
                try {
                    context.server.close();
                }
                catch {
                    // The listener may not have reached the listening state.
                }
            }
            if (controlSocketBound) {
                await this.unlinkControlSocket().catch(() => undefined);
            }
            await this.removeOwnedRecord(ownerGenerationId).catch(() => undefined);
            if (this.generation === context)
                this.generation = undefined;
            if (this.server === context?.server)
                this.server = undefined;
            this.lifecycle = generationNumber === 1 ? "INITIAL" : "STOPPED";
            throw error;
        }
    }
    stop() {
        if (this.stopPromise !== undefined)
            return this.stopPromise;
        if (this.lifecycle === "INITIAL" || this.lifecycle === "STOPPED") {
            return Promise.resolve();
        }
        if (this.lifecycle === "STARTING") {
            return Promise.reject(new Error("Runtime daemon cannot stop while starting"));
        }
        if (this.lifecycle === "STOPPED_DEGRADED") {
            return Promise.reject(this.terminalStopError ?? new Error("Runtime daemon stopped with interruption failure"));
        }
        const generation = this.generation;
        if (generation === undefined) {
            return Promise.reject(new Error("Runtime daemon lifecycle has no active generation"));
        }
        const retry = this.lifecycle === "STOP_FAILED_CLEANUP";
        this.lifecycle = "STOPPING";
        const deadline = retry ? undefined : performance.now() + STOP_GRACE_MS;
        const promise = this.performStop(generation, retry, deadline);
        this.stopPromise = promise;
        const clear = () => {
            if (this.stopPromise === promise)
                this.stopPromise = undefined;
        };
        void promise.then(clear, clear);
        return promise;
    }
    async route(request, response, generation) {
        try {
            const url = new URL(request.url ?? "/", "http://chirality.invalid");
            const method = request.method ?? "GET";
            const segments = url.pathname.split("/").filter(Boolean).map(decodeURIComponent);
            if (segments[0] !== "v1")
                throw new RuntimeError("NOT_FOUND", "Route not found", 404);
            if (method === "GET" && url.pathname === "/v1/health") {
                await this.authorize(request, "runtime:read");
                return this.json(response, 200, this.health());
            }
            if (method === "GET" && url.pathname === "/v1/daemon/status") {
                await this.authorize(request, "runtime:read");
                const body = {
                    ...this.health(),
                    startedAt: this.startedAt,
                    socketPath: this.options.socketPath,
                    engines: this.options.service.engines.descriptors()
                };
                return this.json(response, 200, body);
            }
            if (method === "GET" && url.pathname === "/v1/projects") {
                const principal = await this.authorize(request, "runtime:read");
                const projects = principal.projectId === undefined
                    ? await this.options.service.projects.list()
                    : [await this.options.service.projects.status(principal.projectId)];
                return this.json(response, 200, { projects });
            }
            if (method === "POST" && url.pathname === "/v1/projects/register") {
                await this.authorize(request, "projects:write");
                const body = await this.body(request);
                return this.json(response, 201, await this.options.service.registerProject(body.manifestPath, body.approvedBy, body.approvalReference));
            }
            if (segments[1] === "credentials" && typeof segments[2] === "string") {
                const providerId = segments[2];
                if (method === "GET") {
                    await this.authorize(request, "credentials:read");
                    return this.json(response, 200, {
                        providerId,
                        ...(await this.options.service.credentials.status(providerId))
                    });
                }
                if (method === "PUT") {
                    await this.authorize(request, "credentials:write");
                    const body = await this.body(request);
                    if (body.credential.trim() === "") {
                        throw new RuntimeError("INVALID_REQUEST", "Credential cannot be empty");
                    }
                    await this.options.service.credentials.set(providerId, body.credential);
                    return this.json(response, 200, { providerId, configured: true });
                }
                if (method === "DELETE") {
                    await this.authorize(request, "credentials:write");
                    await this.options.service.credentials.remove(providerId);
                    return this.json(response, 200, { providerId, configured: false });
                }
            }
            if (segments[1] === "models") {
                if (segments.length === 2 && method === "GET") {
                    await this.authorize(request, "models:read");
                    return this.json(response, 200, {
                        residency: await this.options.service.residency.status()
                    });
                }
                if (segments.length === 4 && segments[3] === "activate" && method === "POST") {
                    await this.authorize(request, "models:write");
                    const body = await this.body(request);
                    return this.json(response, 200, {
                        residency: await this.options.service.residency.activate(segments[2] ?? "", body.approvalReference)
                    });
                }
            }
            if (segments[1] === "projects" && typeof segments[2] === "string") {
                const projectId = segments[2];
                if (segments.length === 4 && segments[3] === "status" && method === "GET") {
                    await this.authorize(request, "runtime:read", projectId);
                    return this.json(response, 200, await this.options.service.projects.status(projectId));
                }
                if (segments.length === 4 && segments[3] === "agents" && method === "GET") {
                    await this.authorize(request, "sessions:read", projectId);
                    return this.json(response, 200, {
                        agents: await this.options.service.listAgents(projectId, url.searchParams.get("directChat") === "1")
                    });
                }
                if (segments.length === 4 && segments[3] === "scaffold" && method === "POST") {
                    await this.authorize(request, "sessions:write", projectId);
                    const body = await this.body(request);
                    return this.json(response, 200, {
                        scaffold: await this.options.service.scaffold(projectId, body)
                    });
                }
                if (segments.length === 4 && segments[3] === "runs" && method === "POST") {
                    await this.authorize(request, "sessions:write", projectId);
                    const body = await this.body(request);
                    let managerSessionId;
                    const source = this.options.service.runAgent1(projectId, body);
                    const tracked = (async function* () {
                        for await (const event of source) {
                            if (managerSessionId === undefined && event.type === "harness:event") {
                                managerSessionId = event.data.sessionId;
                            }
                            yield event;
                        }
                    })();
                    return await this.sse(response, tracked, () => {
                        if (managerSessionId !== undefined) {
                            return this.options.service.interruptSession(projectId, managerSessionId);
                        }
                        return undefined;
                    }, generation);
                }
                if (segments[3] === "sessions") {
                    return await this.sessionRoute(request, response, method, projectId, segments, generation);
                }
            }
            throw new RuntimeError("NOT_FOUND", "Route not found", 404);
        }
        catch (error) {
            this.error(response, error);
        }
    }
    async sessionRoute(request, response, method, projectId, segments, generation) {
        if (segments.length === 4) {
            if (method === "GET") {
                await this.authorize(request, "sessions:read", projectId);
                return this.json(response, 200, {
                    sessions: await this.options.service.sessions.list(projectId)
                });
            }
            if (method === "POST") {
                await this.authorize(request, "sessions:write", projectId);
                const body = await this.body(request);
                return this.json(response, 201, {
                    session: await this.options.service.createSession({ ...body, projectId })
                });
            }
        }
        const sessionId = segments[4];
        if (sessionId === undefined)
            throw new RuntimeError("NOT_FOUND", "Route not found", 404);
        if (segments.length === 5) {
            if (method === "GET") {
                await this.authorize(request, "sessions:read", projectId);
                return this.json(response, 200, {
                    session: await this.options.service.sessions.get(projectId, sessionId)
                });
            }
            if (method === "DELETE") {
                await this.authorize(request, "sessions:write", projectId);
                await this.options.service.sessions.delete(projectId, sessionId);
                return this.json(response, 200, { deleted: true, sessionId });
            }
        }
        if (segments.length !== 6)
            throw new RuntimeError("NOT_FOUND", "Route not found", 404);
        const action = segments[5];
        if (action === "boot" && method === "POST") {
            await this.authorize(request, "sessions:write", projectId);
            const body = await this.body(request);
            return this.json(response, 200, await this.options.service.bootSession(projectId, sessionId, body.opts, body.expectedSelection));
        }
        if (action === "replay" && method === "GET") {
            await this.authorize(request, "sessions:read", projectId);
            const session = await this.options.service.sessions.get(projectId, sessionId);
            const replay = await this.options.service.sessions.replayDetailed(projectId, sessionId);
            return this.json(response, 200, {
                session,
                ...replay,
                transcript: deriveTranscriptView(replay.events, session)
            });
        }
        if (action === "turn" && method === "POST") {
            await this.authorize(request, "sessions:write", projectId);
            const body = await this.body(request);
            return await this.sse(response, this.options.service.runSessionTurn(projectId, sessionId, body), () => this.options.service.interruptSession(projectId, sessionId), generation);
        }
        if (action === "interrupt" && method === "POST") {
            await this.authorize(request, "sessions:write", projectId);
            await this.options.service.interruptSession(projectId, sessionId);
            return this.json(response, 200, { interrupted: true, sessionId });
        }
        if (action === "permission" && method === "POST") {
            await this.authorize(request, "sessions:write", projectId);
            await this.options.service.sessions.get(projectId, sessionId);
            const body = await this.body(request);
            await this.options.service.decidePermission(projectId, sessionId, body);
            return this.json(response, 200, {
                accepted: true,
                requestId: body.requestId,
                decision: body.decision
            });
        }
        throw new RuntimeError("NOT_FOUND", "Route not found", 404);
    }
    health() {
        return {
            apiVersion: RUNTIME_API_VERSION,
            status: "ok",
            daemonId: this.daemonId,
            pid: process.pid
        };
    }
    authorize(request, scope, projectId) {
        const value = Array.isArray(request.headers.authorization)
            ? request.headers.authorization[0]
            : request.headers.authorization;
        return this.options.service.auth.authenticate(value, scope, projectId);
    }
    async body(request) {
        const chunks = [];
        let total = 0;
        for await (const chunk of request) {
            const buffer = Buffer.isBuffer(chunk) ? chunk : Buffer.from(chunk);
            total += buffer.length;
            if (total > JSON_LIMIT_BYTES) {
                throw new RuntimeError("INVALID_REQUEST", "Request body is too large", 413);
            }
            chunks.push(buffer);
        }
        try {
            return JSON.parse(Buffer.concat(chunks).toString("utf8"));
        }
        catch {
            throw new RuntimeError("INVALID_REQUEST", "Request body must be valid JSON");
        }
    }
    async discardOptionalBody(request) {
        for await (const _chunk of request) {
            // Drain the stream without interpreting unused compatibility input.
        }
    }
    json(response, status, value) {
        if (response.headersSent)
            return;
        const body = JSON.stringify(value);
        response.writeHead(status, {
            "content-type": "application/json; charset=utf-8",
            "content-length": Buffer.byteLength(body)
        });
        response.end(body);
    }
    async sse(response, events, onDisconnect, generation) {
        const iterator = events[Symbol.asyncIterator]();
        const control = {
            generation,
            interrupt: onDisconnect ?? (() => undefined),
            iterator,
            cancellationRequested: false,
            interruptionStarted: false,
            interruptionSettled: false,
            interruptionTimedOut: false,
            identityUnavailable: false,
            forceExpired: false,
            iteratorReturnRequested: false
        };
        generation.streams.add(control);
        let finished = false;
        let streamStarted = false;
        let disconnected = response.destroyed;
        const close = () => {
            if (finished)
                return;
            disconnected = true;
            this.cancelSse(control);
        };
        response.once("close", close);
        try {
            const first = await iterator.next();
            streamStarted = true;
            // The first Agent 1 event may reveal the session identity while a
            // shutdown cancellation is already latched.
            this.trySseInterrupt(control);
            if (response.destroyed && !disconnected)
                disconnected = true;
            if (disconnected) {
                // A run stream may not know its manager session until the first event.
                // Retry the single cancellation latch after identity has been captured.
                this.trySseInterrupt(control);
            }
            else {
                response.writeHead(200, {
                    "content-type": "text/event-stream",
                    "cache-control": "no-cache, no-transform",
                    connection: "keep-alive",
                    "x-accel-buffering": "no"
                });
            }
            if (!first.done && !disconnected) {
                response.write(`event: ${first.value.type}\ndata: ${JSON.stringify(first.value.data)}\n\n`);
            }
            while (true) {
                const next = await iterator.next();
                // A later Agent 1 event may be the first to reveal the manager
                // session while shutdown cancellation is already latched.
                this.trySseInterrupt(control);
                if (next.done)
                    break;
                if (!disconnected) {
                    response.write(`event: ${next.value.type}\ndata: ${JSON.stringify(next.value.data)}\n\n`);
                }
            }
        }
        finally {
            finished = true;
            response.off("close", close);
            if (control.cancellationRequested)
                this.requestSseIteratorReturn(control);
            generation.streams.delete(control);
            this.notifyGeneration(generation);
            if (streamStarted && !response.destroyed)
                response.end();
        }
    }
    cancelSse(control) {
        if (!control.cancellationRequested)
            control.cancellationRequested = true;
        this.trySseInterrupt(control);
    }
    requestSseIteratorReturn(control) {
        if (!control.iteratorReturnRequested && control.iterator?.return !== undefined) {
            control.iteratorReturnRequested = true;
            let returned;
            try {
                returned = Promise.resolve(control.iterator.return());
            }
            catch (error) {
                control.iteratorReturnFailure = error;
                this.notifyGeneration(control.generation);
                return;
            }
            void returned.then(() => this.notifyGeneration(control.generation), (error) => {
                control.iteratorReturnFailure = error;
                this.notifyGeneration(control.generation);
            });
        }
    }
    trySseInterrupt(control) {
        if (!control.cancellationRequested ||
            control.interruptionStarted ||
            control.forceExpired) {
            return;
        }
        let interruption;
        try {
            interruption = control.interrupt();
        }
        catch (error) {
            control.interruptionStarted = true;
            control.interruptionSettled = true;
            control.interruptionFailure = error;
            this.notifyGeneration(control.generation);
            return;
        }
        if (interruption === undefined)
            return;
        control.interruptionStarted = true;
        void interruption.then(() => {
            control.interruptionSettled = true;
            this.notifyGeneration(control.generation);
        }, (error) => {
            control.interruptionSettled = true;
            control.interruptionFailure = error;
            this.notifyGeneration(control.generation);
        });
    }
    async performStop(generation, retry, deadline) {
        const cleanupFailures = [];
        if (!retry) {
            generation.stopStreams = [...generation.streams];
            this.beginServerClose(generation);
            // Admission is closed before any semantic interruption is requested.
            for (const stream of generation.stopStreams)
                this.cancelSse(stream);
            await this.waitUntilGeneration(generation, () => generation.closeComplete &&
                generation.sockets.size === 0 &&
                (generation.stopStreams ?? []).every((stream) => stream.interruptionStarted &&
                    stream.interruptionSettled &&
                    !generation.streams.has(stream)), Math.max(0, (deadline ?? performance.now()) - performance.now()));
            for (const stream of generation.stopStreams) {
                if (!stream.interruptionStarted) {
                    stream.forceExpired = true;
                    stream.identityUnavailable = true;
                }
                else if (!stream.interruptionSettled) {
                    stream.forceExpired = true;
                    stream.interruptionTimedOut = true;
                }
                if (generation.streams.has(stream))
                    this.requestSseIteratorReturn(stream);
            }
            generation.interruptionProblems = generation.stopStreams.some((stream) => stream.identityUnavailable ||
                stream.interruptionTimedOut ||
                stream.interruptionFailure !== undefined ||
                stream.iteratorReturnFailure !== undefined);
            if (!generation.closeComplete || generation.sockets.size > 0) {
                this.forceGenerationTransport(generation, cleanupFailures);
            }
        }
        else if (!generation.closeComplete || generation.sockets.size > 0) {
            this.beginServerClose(generation);
            this.forceGenerationTransport(generation, cleanupFailures);
        }
        if (generation.forced) {
            const settled = await this.waitUntilGeneration(generation, () => generation.closeComplete && generation.sockets.size === 0, STOP_FORCE_SETTLE_MS);
            if (!settled)
                cleanupFailures.push(new Error("SERVER_CLOSE_SETTLEMENT_TIMEOUT"));
        }
        if (generation.closeError !== undefined)
            cleanupFailures.push(generation.closeError);
        if (generation.sockets.size > 0)
            cleanupFailures.push(new Error("RESIDUAL_SERVER_SOCKETS"));
        generation.interruptionProblems ||= (generation.stopStreams ?? []).some((stream) => stream.identityUnavailable ||
            stream.interruptionTimedOut ||
            stream.interruptionFailure !== undefined ||
            stream.iteratorReturnFailure !== undefined);
        if (!generation.socketUnlinked) {
            try {
                await this.unlinkControlSocket();
                generation.socketUnlinked = true;
            }
            catch (error) {
                cleanupFailures.push(error);
            }
        }
        if (!generation.ownerRemoved) {
            try {
                await this.removeOwnedRecord(generation.ownerGenerationId);
                generation.ownerRemoved = true;
            }
            catch (error) {
                cleanupFailures.push(error);
            }
        }
        if (cleanupFailures.length > 0 || !generation.closeComplete) {
            const error = this.stopError("STOP_FAILED_CLEANUP", cleanupFailures);
            if (this.generation === generation) {
                this.lifecycle = "STOP_FAILED_CLEANUP";
                this.terminalStopError = error;
            }
            throw error;
        }
        this.server = this.server === generation.server ? undefined : this.server;
        if (this.generation === generation)
            this.generation = undefined;
        if (generation.interruptionProblems) {
            const causes = (generation.stopStreams ?? []).flatMap((stream) => [
                ...(stream.identityUnavailable
                    ? [new Error("INTERRUPTION_IDENTITY_UNAVAILABLE")]
                    : []),
                ...(stream.interruptionTimedOut ? [new Error("INTERRUPTION_TIMEOUT")] : []),
                ...(stream.interruptionFailure === undefined ? [] : [stream.interruptionFailure]),
                ...(stream.iteratorReturnFailure === undefined ? [] : [stream.iteratorReturnFailure])
            ]);
            const error = this.stopError("STOPPED_DEGRADED", causes);
            this.lifecycle = "STOPPED_DEGRADED";
            this.terminalStopError = error;
            throw error;
        }
        this.lifecycle = "STOPPED";
        this.terminalStopError = undefined;
    }
    beginServerClose(generation) {
        if (generation.closeStarted && generation.closeError === undefined)
            return;
        generation.closeStarted = true;
        generation.closeError = undefined;
        try {
            generation.server.close((error) => {
                if (error === undefined) {
                    generation.closeComplete = true;
                }
                else {
                    generation.closeError = error;
                }
                this.notifyGeneration(generation);
            });
        }
        catch (error) {
            generation.closeError = error;
            this.notifyGeneration(generation);
        }
    }
    forceGenerationTransport(generation, failures) {
        generation.forced = true;
        try {
            generation.server.closeAllConnections();
        }
        catch (error) {
            failures.push(error);
        }
        for (const socket of generation.sockets) {
            try {
                socket.destroy();
            }
            catch (error) {
                failures.push(error);
            }
        }
    }
    waitUntilGeneration(generation, predicate, timeoutMs) {
        if (predicate())
            return Promise.resolve(true);
        return new Promise((resolve) => {
            let settled = false;
            const finish = (value) => {
                if (settled)
                    return;
                settled = true;
                clearTimeout(timer);
                generation.stateWaiters.delete(check);
                resolve(value);
            };
            const check = () => {
                if (predicate())
                    finish(true);
            };
            const timer = setTimeout(() => finish(predicate()), timeoutMs);
            generation.stateWaiters.add(check);
            check();
        });
    }
    notifyGeneration(generation) {
        for (const waiter of [...generation.stateWaiters])
            waiter();
    }
    stopError(code, causes) {
        const details = causes.map((cause) => cause instanceof Error ? cause.message : String(cause));
        const error = new Error(`${code}${details.length === 0 ? "" : `: ${details.join("; ")}`}`);
        error.name = code;
        Object.assign(error, { code, causes });
        return error;
    }
    async unlinkControlSocket() {
        await unlink(this.options.socketPath).catch((error) => {
            if (error.code !== "ENOENT")
                throw error;
        });
    }
    error(response, error) {
        if (response.headersSent) {
            response.end();
            return;
        }
        const normalized = error instanceof RuntimeError
            ? error
            : error instanceof HarnessError
                ? new RuntimeError(error.type === "SESSION_NOT_FOUND" ? "SESSION_NOT_FOUND" : "INTERNAL_FAILURE", error.message, error.status)
                : new RuntimeError("INTERNAL_FAILURE", "Unexpected runtime failure", 500);
        const body = {
            error: {
                code: normalized.code,
                message: normalized.message,
                ...(normalized.details === undefined ? {} : { details: normalized.details })
            }
        };
        this.json(response, normalized.status, body);
    }
    async recoverStaleSocket() {
        const owner = await this.readOwner();
        let metadata;
        try {
            metadata = await lstat(this.options.socketPath);
        }
        catch (error) {
            if (error.code === "ENOENT") {
                if (owner === undefined)
                    return;
                if (this.pidIsDemonstrablyAbsent(owner.pid)) {
                    await unlink(this.ownerFile);
                    return;
                }
                throw new RuntimeError("FORBIDDEN", "Daemon owner is live or ambiguous while the socket is absent", 409);
            }
            throw error;
        }
        if (!metadata.isSocket()) {
            throw new RuntimeError("FORBIDDEN", "Refusing to replace a non-socket control path", 409);
        }
        if (process.getuid !== undefined && metadata.uid !== process.getuid()) {
            throw new RuntimeError("FORBIDDEN", "Refusing to replace another user's socket", 403);
        }
        if (owner === undefined) {
            throw new RuntimeError("FORBIDDEN", "Refusing stale-socket recovery without an authenticated owner record", 409);
        }
        if (owner.socketPath !== this.options.socketPath ||
            owner.uid !== (process.getuid?.() ?? -1)) {
            throw new RuntimeError("FORBIDDEN", "Daemon owner record does not match this user/socket", 403);
        }
        if (!this.pidIsDemonstrablyAbsent(owner.pid)) {
            throw new RuntimeError("RESIDENCY_TRANSITION_IN_PROGRESS", "Runtime daemon owner is live or ambiguous", 409);
        }
        await unlink(this.options.socketPath);
        await unlink(this.ownerFile);
    }
    async readOwner() {
        let metadata;
        try {
            metadata = await lstat(this.ownerFile);
        }
        catch (error) {
            if (error.code === "ENOENT")
                return undefined;
            throw error;
        }
        if (!metadata.isFile() ||
            (process.getuid !== undefined && metadata.uid !== process.getuid()) ||
            (metadata.mode & 0o077) !== 0) {
            throw new RuntimeError("FORBIDDEN", "Unsafe daemon owner record", 403);
        }
        let value;
        try {
            value = JSON.parse(await readFile(this.ownerFile, "utf8"));
        }
        catch {
            throw new RuntimeError("FORBIDDEN", "Malformed daemon owner record", 409);
        }
        const owner = value;
        if (owner["schemaVersion"] !== "chirality.daemon-owner/v1" ||
            typeof owner["daemonId"] !== "string" ||
            (owner["generationId"] !== undefined && typeof owner["generationId"] !== "string") ||
            typeof owner["pid"] !== "number" ||
            !Number.isSafeInteger(owner["pid"]) ||
            typeof owner["uid"] !== "number" ||
            typeof owner["socketPath"] !== "string" ||
            typeof owner["startedAt"] !== "string") {
            throw new RuntimeError("FORBIDDEN", "Malformed daemon owner record", 409);
        }
        return owner;
    }
    pidIsDemonstrablyAbsent(pid) {
        if (pid <= 0)
            return false;
        try {
            process.kill(pid, 0);
            return false;
        }
        catch (error) {
            return error.code === "ESRCH";
        }
    }
    async removeOwnedRecord(ownerGenerationId) {
        const owner = await this.readOwner();
        if (owner === undefined ||
            owner.daemonId !== this.daemonId ||
            owner.pid !== process.pid ||
            owner.generationId !== ownerGenerationId) {
            return;
        }
        await unlink(this.ownerFile).catch((error) => {
            if (error.code !== "ENOENT")
                throw error;
        });
    }
}
