import { lstat, readFile, realpath } from "node:fs/promises";
import { request as httpRequest } from "node:http";
import { resolve } from "node:path";
import { RUNTIME_ROUTES, RuntimeError } from "@chirality/runtime-contracts";
import { RuntimeTransportError, runtimeErrorFromResponse } from "./errors.js";
import { parseSse, parseUiEvent } from "./sse.js";
const MAX_JSON_BYTES = 16 * 1024 * 1024;
async function defaultLoadToken(tokenFile) {
    const metadata = await lstat(tokenFile);
    if (!metadata.isFile() || metadata.isSymbolicLink()) {
        throw new RuntimeTransportError("Runtime token path must be a regular file");
    }
    if ((metadata.mode & 0o077) !== 0) {
        throw new RuntimeTransportError("Runtime token file permissions must be 0600 or stricter");
    }
    if (process.getuid !== undefined && metadata.uid !== process.getuid()) {
        throw new RuntimeTransportError("Runtime token file must be owned by the current user");
    }
    const token = (await readFile(tokenFile, "utf8")).trim();
    if (!/^[A-Za-z0-9_-]+$/u.test(token)) {
        throw new RuntimeTransportError("Runtime token file is empty or malformed");
    }
    return token;
}
async function readResponseJson(response) {
    const chunks = [];
    let bytes = 0;
    for await (const chunk of response) {
        const buffer = Buffer.isBuffer(chunk) ? chunk : Buffer.from(chunk);
        bytes += buffer.byteLength;
        if (bytes > MAX_JSON_BYTES) {
            response.destroy();
            throw new RuntimeTransportError("Runtime JSON response exceeds the size limit");
        }
        chunks.push(buffer);
    }
    if (chunks.length === 0)
        return undefined;
    const source = Buffer.concat(chunks).toString("utf8");
    try {
        return JSON.parse(source);
    }
    catch (cause) {
        throw new RuntimeTransportError("Runtime returned malformed JSON", cause);
    }
}
export class RuntimeClient {
    options;
    timeoutMs;
    loadToken;
    constructor(options) {
        this.options = options;
        if (!options.socketPath) {
            throw new RuntimeTransportError("A Unix socket path is required");
        }
        if (!options.tokenFile) {
            throw new RuntimeTransportError("A runtime token file is required");
        }
        this.timeoutMs = options.timeoutMs ?? 30_000;
        this.loadToken = options.loadToken ?? defaultLoadToken;
    }
    async requestJson(path, options = {}) {
        const token = await this.loadToken(this.options.tokenFile);
        const body = options.body === undefined ? undefined : Buffer.from(JSON.stringify(options.body), "utf8");
        const response = await this.request(path, {
            method: options.method ?? "GET",
            token,
            body,
            signal: options.signal,
            accept: "application/json"
        });
        const value = await readResponseJson(response);
        const status = response.statusCode ?? 500;
        if (status < 200 || status >= 300) {
            throw runtimeErrorFromResponse(status, value);
        }
        return value;
    }
    async requestSse(path, options = {}) {
        const token = await this.loadToken(this.options.tokenFile);
        const body = options.body === undefined ? undefined : Buffer.from(JSON.stringify(options.body), "utf8");
        const controller = new AbortController();
        const abort = () => controller.abort(options.signal?.reason);
        if (options.signal?.aborted)
            abort();
        else
            options.signal?.addEventListener("abort", abort, { once: true });
        const response = await this.request(path, {
            method: options.method ?? "GET",
            token,
            body,
            signal: controller.signal,
            accept: "text/event-stream"
        });
        const status = response.statusCode ?? 500;
        if (status < 200 || status >= 300) {
            const value = await readResponseJson(response);
            options.signal?.removeEventListener("abort", abort);
            throw runtimeErrorFromResponse(status, value);
        }
        const contentType = response.headers["content-type"] ?? "";
        if (!contentType.toLowerCase().includes("text/event-stream")) {
            response.destroy();
            options.signal?.removeEventListener("abort", abort);
            throw new RuntimeTransportError("Runtime stream response is not text/event-stream");
        }
        const iterator = (async function* () {
            try {
                yield* parseSse(response);
            }
            finally {
                options.signal?.removeEventListener("abort", abort);
                response.destroy();
            }
        })();
        return {
            [Symbol.asyncIterator]() {
                return iterator;
            },
            cancel(reason) {
                controller.abort(reason);
                response.destroy();
            }
        };
    }
    async requestEvents(path, options = {}) {
        const source = await this.requestSse(path, options);
        const iterator = (async function* () {
            try {
                for await (const frame of source) {
                    yield parseUiEvent(frame);
                }
            }
            finally {
                source.cancel();
            }
        })();
        return {
            [Symbol.asyncIterator]() {
                return iterator;
            },
            cancel(reason) {
                source.cancel(reason);
            }
        };
    }
    health(signal) {
        return this.requestJson(RUNTIME_ROUTES.health, { signal });
    }
    daemonStatus(signal) {
        return this.requestJson(RUNTIME_ROUTES.daemonStatus, { signal });
    }
    async listProjects(signal) {
        const response = await this.requestJson(RUNTIME_ROUTES.projects, {
            signal
        });
        return response.projects;
    }
    registerProject(request, signal) {
        return this.requestJson(RUNTIME_ROUTES.projectRegister, {
            method: "POST",
            body: request,
            signal
        });
    }
    projectStatus(projectId, signal) {
        return this.requestJson(RUNTIME_ROUTES.projectStatus(projectId), { signal });
    }
    async resolveProjectByRoot(projectRoot, signal) {
        const requested = await realpath(resolve(projectRoot)).catch(() => resolve(projectRoot));
        const projects = await this.listProjects(signal);
        const match = projects.find(({ project }) => resolve(project.canonicalRoot) === requested);
        if (match === undefined) {
            throw new RuntimeError("PROJECT_NOT_FOUND", `No registered project owns ${requested}`, 404);
        }
        if (match.manifestDrift || !match.adaptersEnabled) {
            throw new RuntimeError("PROJECT_MANIFEST_DRIFT", "Project manifest changed after registration", 409, { projectId: match.project.projectId });
        }
        return match.project;
    }
    async listSessions(projectId, signal) {
        const response = await this.requestJson(RUNTIME_ROUTES.sessions(projectId), {
            signal
        });
        return response.sessions;
    }
    async createSession(projectId, request, signal) {
        if (request.projectId !== projectId) {
            throw new RuntimeError("INVALID_REQUEST", "Session request projectId does not match the route", 400);
        }
        const { projectId: _projectId, ...daemonRequest } = request;
        const response = await this.requestJson(RUNTIME_ROUTES.sessions(projectId), {
            method: "POST",
            body: daemonRequest,
            signal
        });
        return response.session;
    }
    getSession(projectId, sessionId, signal) {
        return this.requestJson(RUNTIME_ROUTES.session(projectId, sessionId), { signal }).then((response) => response.session);
    }
    deleteSession(projectId, sessionId, signal) {
        return this.requestJson(RUNTIME_ROUTES.session(projectId, sessionId), {
            method: "DELETE",
            signal
        });
    }
    async resolveSessionOwner(sessionId, signal) {
        const projects = await this.listProjects(signal);
        for (const status of projects) {
            try {
                const session = await this.getSession(status.project.projectId, sessionId, signal);
                return { project: status.project, session };
            }
            catch (error) {
                if (error instanceof RuntimeError &&
                    (error.code === "SESSION_NOT_FOUND" || error.code === "NOT_FOUND")) {
                    continue;
                }
                throw error;
            }
        }
        throw new RuntimeError("SESSION_NOT_FOUND", `Unknown session: ${sessionId}`, 404);
    }
    async bootSession(projectId, sessionId, request = {}, signal) {
        return this.requestJson(RUNTIME_ROUTES.sessionBoot(projectId, sessionId), {
            method: "POST",
            body: request,
            signal
        });
    }
    replaySession(projectId, sessionId, signal) {
        return this.requestJson(RUNTIME_ROUTES.sessionReplay(projectId, sessionId), {
            signal
        });
    }
    turnSession(projectId, sessionId, request, signal) {
        return this.requestEvents(RUNTIME_ROUTES.sessionTurn(projectId, sessionId), {
            method: "POST",
            body: request,
            signal
        });
    }
    interruptSession(projectId, sessionId, signal) {
        return this.requestJson(RUNTIME_ROUTES.sessionInterrupt(projectId, sessionId), {
            method: "POST",
            signal
        });
    }
    decidePermission(projectId, sessionId, request, signal) {
        return this.requestJson(RUNTIME_ROUTES.sessionPermission(projectId, sessionId), {
            method: "POST",
            body: request,
            signal
        });
    }
    async listAgents(projectId, signal) {
        const response = await this.requestJson(RUNTIME_ROUTES.agents(projectId), {
            signal
        });
        return response.agents;
    }
    scaffold(projectId, request, signal) {
        return this.requestJson(RUNTIME_ROUTES.scaffold(projectId), {
            method: "POST",
            body: request,
            signal
        }).then((response) => response.scaffold);
    }
    runAgent1(projectId, request, signal) {
        return this.requestEvents(RUNTIME_ROUTES.runs(projectId), {
            method: "POST",
            body: request,
            signal
        });
    }
    async listModels(signal) {
        const response = await this.requestJson(RUNTIME_ROUTES.models, {
            signal
        });
        return response.residency;
    }
    activateModel(modelId, approvalReference, signal) {
        return this.requestJson(RUNTIME_ROUTES.modelActivate(modelId), {
            method: "POST",
            body: { approvalReference },
            signal
        }).then((response) => response.residency);
    }
    credentialStatus(providerId, signal) {
        return this.requestJson(RUNTIME_ROUTES.credentials(providerId), { signal });
    }
    storeCredential(providerId, credential, signal) {
        return this.requestJson(RUNTIME_ROUTES.credentials(providerId), {
            method: "PUT",
            body: { credential },
            signal
        });
    }
    removeCredential(providerId, signal) {
        return this.requestJson(RUNTIME_ROUTES.credentials(providerId), {
            method: "DELETE",
            signal
        });
    }
    async request(path, input) {
        return new Promise((resolveResponse, reject) => {
            let settled = false;
            const fail = (error) => {
                if (settled)
                    return;
                settled = true;
                reject(error instanceof RuntimeTransportError
                    ? error
                    : new RuntimeTransportError(`Unable to reach the Chirality runtime at ${this.options.socketPath}`, error));
            };
            const request = httpRequest({
                socketPath: this.options.socketPath,
                path,
                method: input.method,
                signal: input.signal,
                headers: {
                    Accept: input.accept,
                    Authorization: `Bearer ${input.token}`,
                    ...(input.body === undefined
                        ? {}
                        : {
                            "Content-Type": "application/json",
                            "Content-Length": String(input.body.byteLength)
                        })
                }
            }, (response) => {
                if (settled) {
                    response.destroy();
                    return;
                }
                settled = true;
                resolveResponse(response);
            });
            request.setTimeout(this.timeoutMs, () => {
                request.destroy(new Error("Runtime request timed out"));
            });
            request.once("error", fail);
            if (input.body !== undefined)
                request.write(input.body);
            request.end();
        });
    }
}
