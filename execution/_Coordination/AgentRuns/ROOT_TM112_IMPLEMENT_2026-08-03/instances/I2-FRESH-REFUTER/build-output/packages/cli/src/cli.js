import { readFile } from "node:fs/promises";
import { RuntimeClient, RuntimeTransportError } from "@chirality/runtime-client";
import { RuntimeError } from "@chirality/runtime-contracts";
import { resolveCliRuntimePaths, runtimeClientOptions } from "./config.js";
import { LaunchAgentManager, resolveRuntimeLaunchAgentOptions } from "./launch-agent.js";
export class CliUsageError extends Error {
    constructor(message) {
        super(message);
        this.name = "CliUsageError";
    }
}
function parseArguments(args) {
    const positionals = [];
    const options = new Map();
    for (let index = 0; index < args.length; index += 1) {
        const argument = args[index];
        if (argument === undefined)
            continue;
        if (!argument.startsWith("--")) {
            positionals.push(argument);
            continue;
        }
        const equals = argument.indexOf("=");
        if (equals > 2) {
            options.set(argument.slice(2, equals), argument.slice(equals + 1));
            continue;
        }
        const key = argument.slice(2);
        if (key === "json") {
            options.set(key, true);
            continue;
        }
        const value = args[index + 1];
        if (value === undefined || value.startsWith("--")) {
            throw new CliUsageError(`Option --${key} requires a value`);
        }
        options.set(key, value);
        index += 1;
    }
    return { positionals, options };
}
function option(args, name) {
    const value = args.options.get(name);
    return typeof value === "string" ? value : undefined;
}
function requiredOption(args, name) {
    const value = option(args, name);
    if (value === undefined || value.length === 0) {
        throw new CliUsageError(`Missing required --${name}`);
    }
    return value;
}
function flag(args, name) {
    return args.options.get(name) === true;
}
function printJson(io, value, json) {
    io.stdout(`${JSON.stringify(value, null, json ? 0 : 2)}\n`);
}
async function streamEvents(io, stream, json) {
    let processExitCode;
    for await (const event of stream) {
        if (processExitCode !== undefined) {
            throw new RuntimeError("INTERNAL_FAILURE", "Runtime stream emitted data after terminal process:exit", 502);
        }
        if (json) {
            io.stdout(`${JSON.stringify(event)}\n`);
        }
        else if (event.type === "chat:delta") {
            io.stdout(event.data.text);
        }
        else if (event.type === "turn:error") {
            io.stderr(`${event.data.errorType}: ${event.data.message}\n`);
        }
        else if (event.type === "process:exit" && event.data.exitCode !== 0) {
            io.stderr(`process exited ${event.data.exitCode}\n`);
        }
        else if (event.type !== "harness:event") {
            io.stdout(`[${event.type}]\n`);
        }
        if (event.type === "process:exit") {
            processExitCode = event.data.exitCode;
        }
    }
    if (processExitCode === undefined) {
        throw new RuntimeError("INTERNAL_FAILURE", "Runtime stream ended without terminal process:exit", 502);
    }
    return Number.isInteger(processExitCode) && processExitCode > 0
        ? processExitCode
        : processExitCode === 0
            ? 0
            : 1;
}
async function readRequestFile(path, deps) {
    let value;
    try {
        value = JSON.parse(await deps.readTextFile(path));
    }
    catch {
        throw new CliUsageError(`Request file is not valid JSON: ${path}`);
    }
    if (typeof value !== "object" || value === null || Array.isArray(value)) {
        throw new CliUsageError(`Request file must contain a JSON object: ${path}`);
    }
    return value;
}
async function readPrompt(args, io, deps) {
    const requestFile = option(args, "request-file");
    if (requestFile !== undefined) {
        return readRequestFile(requestFile, deps);
    }
    const prompt = option(args, "prompt") ?? (await io.readStdin()).trim();
    if (!prompt) {
        throw new CliUsageError("Session turn requires --prompt, --request-file, or standard input");
    }
    return { prompt };
}
async function readRunRequest(args, io, deps) {
    const requestFile = option(args, "request-file");
    if (requestFile !== undefined) {
        const input = await readRequestFile(requestFile, deps);
        const projectId = option(args, "project") ?? input.project;
        if (!projectId)
            throw new CliUsageError("Run request requires --project");
        const { project: _project, agent: legacyAgent, ...request } = input;
        return {
            projectId,
            request: {
                ...request,
                agentId: input.agentId ?? option(args, "agent") ?? legacyAgent
            }
        };
    }
    const projectId = requiredOption(args, "project");
    const agentId = requiredOption(args, "agent");
    const briefFile = option(args, "brief-file");
    const localModel = option(args, "local-model");
    const brief = briefFile === undefined
        ? (await io.readStdin()).trim()
        : (await deps.readTextFile(briefFile)).trim();
    if (!brief) {
        throw new CliUsageError("Run requires --brief-file, --request-file, or standard input");
    }
    return {
        projectId,
        request: {
            brief,
            agentId,
            approvalReference: option(args, "approval-reference") ?? `cli-agent1:${agentId}`,
            ...(localModel === undefined
                ? {}
                : {
                    localModel,
                    readOnlyTool: {
                        name: "read_file",
                        relativePath: option(args, "read-file") ?? "chirality.project.json"
                    }
                })
        }
    };
}
export async function runCli(argv, io, deps) {
    try {
        const group = argv[0];
        if (!group)
            throw new CliUsageError("A command is required");
        const action = group === "run" ? undefined : argv[1];
        const rest = group === "run" ? argv.slice(1) : argv.slice(2);
        const args = parseArguments(rest);
        const json = flag(args, "json");
        if (group === "daemon") {
            if (action === "install") {
                await deps.launchAgent.install(option(args, "executable") ?? deps.executablePath);
                printJson(io, { installed: true }, json);
            }
            else if (action === "start") {
                await deps.launchAgent.start();
                printJson(io, { started: true }, json);
            }
            else if (action === "stop") {
                await deps.launchAgent.stop();
                printJson(io, { stopped: true }, json);
            }
            else if (action === "status") {
                printJson(io, {
                    launchAgent: await deps.launchAgent.status(),
                    daemon: await deps.client.daemonStatus()
                }, json);
            }
            else if (action === "uninstall") {
                await deps.launchAgent.uninstall();
                printJson(io, { uninstalled: true }, json);
            }
            else {
                throw new CliUsageError("daemon requires install, start, stop, status, or uninstall");
            }
            return 0;
        }
        if (group === "project") {
            if (action === "register") {
                const manifestPath = option(args, "manifest") ?? args.positionals[0];
                if (!manifestPath) {
                    throw new CliUsageError("project register requires a manifest path or --manifest");
                }
                printJson(io, await deps.client.registerProject({
                    manifestPath,
                    approvedBy: option(args, "approved-by") ?? "local-operator",
                    approvalReference: option(args, "approval-reference") ?? "cli-explicit-registration"
                }), json);
            }
            else if (action === "list") {
                printJson(io, await deps.client.listProjects(), json);
            }
            else if (action === "status") {
                printJson(io, await deps.client.projectStatus(option(args, "project") ?? args.positionals[0] ??
                    requiredOption(args, "project")), json);
            }
            else {
                throw new CliUsageError("project requires register, list, or status");
            }
            return 0;
        }
        if (group === "models") {
            if (action === "list") {
                printJson(io, await deps.client.listModels(), json);
            }
            else if (action === "activate") {
                const modelId = option(args, "model") ?? args.positionals[0];
                if (!modelId)
                    throw new CliUsageError("models activate requires an exact model ID");
                printJson(io, await deps.client.activateModel(modelId, option(args, "approval-reference") ??
                    "cli-explicit-model-activation"), json);
            }
            else {
                throw new CliUsageError("models requires list or activate");
            }
            return 0;
        }
        if (group === "session") {
            const projectId = requiredOption(args, "project");
            if (action === "create") {
                const requestFile = option(args, "request-file");
                const request = requestFile === undefined
                    ? {
                        projectId,
                        role: requiredOption(args, "role"),
                        engineSelection: {
                            adapterId: requiredOption(args, "adapter"),
                            providerId: requiredOption(args, "provider"),
                            model: requiredOption(args, "model")
                        },
                        ...(option(args, "parent-session") === undefined
                            ? {}
                            : { parentSessionId: option(args, "parent-session") })
                    }
                    : await readRequestFile(requestFile, deps);
                printJson(io, await deps.client.createSession(projectId, request), json);
            }
            else if (action === "list") {
                printJson(io, await deps.client.listSessions(projectId), json);
            }
            else {
                const sessionId = option(args, "session") ?? args.positionals[0];
                if (!sessionId) {
                    throw new CliUsageError(`session ${action ?? ""} requires --session`);
                }
                if (action === "replay") {
                    printJson(io, await deps.client.replaySession(projectId, sessionId), json);
                }
                else if (action === "turn") {
                    return await streamEvents(io, await deps.client.turnSession(projectId, sessionId, await readPrompt(args, io, deps)), json);
                }
                else if (action === "interrupt") {
                    printJson(io, await deps.client.interruptSession(projectId, sessionId), json);
                }
                else {
                    throw new CliUsageError("session requires create, list, replay, turn, or interrupt");
                }
            }
            return 0;
        }
        if (group === "run") {
            const run = await readRunRequest(args, io, deps);
            return await streamEvents(io, await deps.client.runAgent1(run.projectId, run.request), json);
        }
        throw new CliUsageError(`Unknown command: ${argv.join(" ")}`);
    }
    catch (error) {
        if (error instanceof CliUsageError) {
            io.stderr(`chirality: ${error.message}\n`);
            return 2;
        }
        if (error instanceof RuntimeError) {
            io.stderr(`${error.code}: ${error.message}\n`);
            return error.code === "INTERRUPTED" ? 130 : 1;
        }
        if (error instanceof RuntimeTransportError) {
            io.stderr(`RUNTIME_UNAVAILABLE: ${error.message}\n`);
            return 1;
        }
        io.stderr(`INTERNAL_FAILURE: ${error instanceof Error ? error.message : String(error)}\n`);
        return 1;
    }
}
async function readStandardInput() {
    const chunks = [];
    for await (const chunk of process.stdin) {
        chunks.push(Buffer.isBuffer(chunk) ? chunk : Buffer.from(chunk));
    }
    return Buffer.concat(chunks).toString("utf8");
}
export function createDefaultCliDependencies() {
    const paths = resolveCliRuntimePaths();
    return {
        paths,
        client: new RuntimeClient(runtimeClientOptions(paths)),
        // The job posture comes from the environment, not from a hard-coded default.
        // Constructing this with no options meant two things: `daemon install` could
        // never render anything but the historical `crash-only` plist with no pinned
        // environment (so the CLI path silently reinstated the defect the in-app
        // install fixes), and every verb resolved to the default label — so an
        // otherwise fully isolated environment still addressed, and could have
        // booted out or deleted, an operator's real job.
        launchAgent: new LaunchAgentManager({
            launchAgentsDirectory: paths.launchAgentsDirectory,
            runtimeDirectory: paths.runtimeDirectory
        }, undefined, undefined, resolveRuntimeLaunchAgentOptions(process.env, paths.userData)),
        executablePath: process.execPath,
        readTextFile: (path) => readFile(path, "utf8")
    };
}
export const processCliIo = {
    stdout(text) {
        process.stdout.write(text);
    },
    stderr(text) {
        process.stderr.write(text);
    },
    readStdin: readStandardInput
};
