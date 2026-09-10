import { readFile } from "node:fs/promises";
import {
  RuntimeClient,
  RuntimeTransportError,
  type RuntimeStream
} from "@chirality/runtime-client";
import {
  RuntimeError,
  type Agent1RunRequest,
  type CreateSessionRequest,
  type RuntimeCompatibilityIdentity,
  type DelegatedApprovalDecisionRequest,
  type SessionTurnRequest
} from "@chirality/runtime-contracts";
import { observeRuntimeSupportProfileFromPayloadV2, type RuntimePayloadSupportObservationInputV2, type RuntimeSupportProfileV2 } from "@chirality/runtime-core/runtime-conformance-v2";
import {
  resolveCliRuntimePaths,
  runtimeClientOptions,
  type CliRuntimePaths
} from "./config.js";
import {
  LaunchAgentManager,
  resolveRuntimeLaunchAgentOptions
} from "./launch-agent.js";

export interface CliIo {
  stdout(text: string): void;
  stderr(text: string): void;
  readStdin(): Promise<string>;
}

export interface RuntimeCliClient {
  startHostedLogin?(projectId: string, compatibility: RuntimeCompatibilityIdentity): Promise<unknown>;
  hostedLoginStatus?(projectId: string): Promise<unknown>;
  cancelHostedLogin?(projectId: string, compatibility: RuntimeCompatibilityIdentity): Promise<unknown>;
  delegatedCapabilities?(projectId: string): Promise<unknown>;
  pendingRuntimeApprovals?(projectId: string, scopeId?: string): Promise<unknown>;
  decideRuntimeApproval?(projectId: string, requestId: string, compatibility: RuntimeCompatibilityIdentity, request: Omit<DelegatedApprovalDecisionRequest, "compatibility" | "preflight">): Promise<unknown>;
  pendingDelegatedApprovals?(projectId: string, turnId: string): Promise<unknown>;
  decideDelegatedApproval?(projectId: string, requestId: string, compatibility: RuntimeCompatibilityIdentity, request: Omit<DelegatedApprovalDecisionRequest, "compatibility" | "preflight">): Promise<unknown>;
  runDelegatedTurn?(projectId: string, compatibility: RuntimeCompatibilityIdentity, request: {turnId: string; prompt: string; previousTurnId?: string; requestedRole?: "untyped"|"agent0"|"agent1"|"agent2"|"task"}): Promise<unknown>;
  interruptDelegatedTurn?(projectId: string, turnId: string, compatibility: RuntimeCompatibilityIdentity): Promise<unknown>;
  grantDelegatedConsent?(projectId: string, compatibility: RuntimeCompatibilityIdentity, request: {posture: "off"|"ask-per-destination"|"on"; approvedBy: string; explicitUserAct: boolean}): Promise<unknown>;

  daemonStatus(): Promise<unknown>;
  registerProject(request: {
    manifestPath: string;
    approvedBy: string;
    approvalReference: string;
  }): Promise<unknown>;
  listProjects(): Promise<unknown>;
  projectStatus(projectId: string): Promise<unknown>;
  listModels(): Promise<unknown>;
  activateModel(modelId: string, approvalReference: string): Promise<unknown>;
  createSession(
    projectId: string,
    request: CreateSessionRequest
  ): Promise<unknown>;
  listSessions(projectId: string): Promise<unknown>;
  replaySession(projectId: string, sessionId: string): Promise<unknown>;
  turnSession(
    projectId: string,
    sessionId: string,
    request: SessionTurnRequest
  ): Promise<RuntimeStream>;
  interruptSession(projectId: string, sessionId: string): Promise<unknown>;
  runAgent1(projectId: string, request: Agent1RunRequest): Promise<RuntimeStream>;
}

export interface RuntimeLaunchAgent {
  install(executablePath: string): Promise<void>;
  start(): Promise<void>;
  stop(): Promise<void>;
  status(): Promise<unknown>;
  uninstall(): Promise<void>;
}

export interface CliDependencies {
  client: RuntimeCliClient;
  launchAgent: RuntimeLaunchAgent;
  paths: CliRuntimePaths;
  executablePath: string;
  readTextFile(path: string): Promise<string>;
  measureRuntimeSupportProfile(input: RuntimePayloadSupportObservationInputV2): Promise<Readonly<RuntimeSupportProfileV2>>;
}

type ParsedArguments = {
  positionals: string[];
  options: Map<string, string | true>;
};

export class CliUsageError extends Error {
  constructor(message: string) {
    super(message);
    this.name = "CliUsageError";
  }
}

function parseArguments(args: readonly string[]): ParsedArguments {
  const positionals: string[] = [];
  const options = new Map<string, string | true>();
  for (let index = 0; index < args.length; index += 1) {
    const argument = args[index];
    if (argument === undefined) continue;
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
    if (key === "json" || key === "explicit-user-act") {
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

function option(args: ParsedArguments, name: string): string | undefined {
  const value = args.options.get(name);
  return typeof value === "string" ? value : undefined;
}

function requiredOption(args: ParsedArguments, name: string): string {
  const value = option(args, name);
  if (value === undefined || value.length === 0) {
    throw new CliUsageError(`Missing required --${name}`);
  }
  return value;
}

function flag(args: ParsedArguments, name: string): boolean {
  return args.options.get(name) === true;
}

function printJson(io: CliIo, value: unknown, json: boolean): void {
  io.stdout(`${JSON.stringify(value, null, json ? 0 : 2)}\n`);
}

async function streamEvents(
  io: CliIo,
  stream: RuntimeStream,
  json: boolean
): Promise<number> {
  let processExitCode: number | undefined;
  for await (const event of stream) {
    if (processExitCode !== undefined) {
      throw new RuntimeError(
        "INTERNAL_FAILURE",
        "Runtime stream emitted data after terminal process:exit",
        502
      );
    }
    if (json) {
      io.stdout(`${JSON.stringify(event)}\n`);
    } else if (event.type === "chat:delta") {
      io.stdout(event.data.text);
    } else if (event.type === "turn:error") {
      io.stderr(`${event.data.errorType}: ${event.data.message}\n`);
    } else if (event.type === "process:exit" && event.data.exitCode !== 0) {
      io.stderr(`process exited ${event.data.exitCode}\n`);
    } else if (event.type !== "harness:event") {
      io.stdout(`[${event.type}]\n`);
    }
    if (event.type === "process:exit") {
      processExitCode = event.data.exitCode;
    }
  }
  if (processExitCode === undefined) {
    throw new RuntimeError(
      "INTERNAL_FAILURE",
      "Runtime stream ended without terminal process:exit",
      502
    );
  }
  return Number.isInteger(processExitCode) && processExitCode > 0
    ? processExitCode
    : processExitCode === 0
      ? 0
      : 1;
}

async function readRequestFile<T>(
  path: string,
  deps: CliDependencies
): Promise<T> {
  let value: unknown;
  try {
    value = JSON.parse(await deps.readTextFile(path));
  } catch {
    throw new CliUsageError(`Request file is not valid JSON: ${path}`);
  }
  if (typeof value !== "object" || value === null || Array.isArray(value)) {
    throw new CliUsageError(`Request file must contain a JSON object: ${path}`);
  }
  return value as T;
}

async function readPrompt(
  args: ParsedArguments,
  io: CliIo,
  deps: CliDependencies
): Promise<SessionTurnRequest> {
  const requestFile = option(args, "request-file");
  if (requestFile !== undefined) {
    return readRequestFile<SessionTurnRequest>(requestFile, deps);
  }
  const prompt = option(args, "prompt") ?? (await io.readStdin()).trim();
  if (!prompt) {
    throw new CliUsageError(
      "Session turn requires --prompt, --request-file, or standard input"
    );
  }
  return { prompt };
}

async function readRunRequest(
  args: ParsedArguments,
  io: CliIo,
  deps: CliDependencies
): Promise<{ projectId: string; request: Agent1RunRequest }> {
  const requestFile = option(args, "request-file");
  if (requestFile !== undefined) {
    const input = await readRequestFile<
      Agent1RunRequest & { project?: string; agent?: string }
    >(requestFile, deps);
    const projectId = option(args, "project") ?? input.project;
    if (!projectId) throw new CliUsageError("Run request requires --project");
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
  const brief =
    briefFile === undefined
      ? (await io.readStdin()).trim()
      : (await deps.readTextFile(briefFile)).trim();
  if (!brief) {
    throw new CliUsageError(
      "Run requires --brief-file, --request-file, or standard input"
    );
  }
  return {
    projectId,
    request: {
      brief,
      agentId,
      approvalReference:
        option(args, "approval-reference") ?? `cli-agent1:${agentId}`,
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

export async function runCli(
  argv: readonly string[],
  io: CliIo,
  deps: CliDependencies
): Promise<number> {
  try {
    const group = argv[0];
    if (!group) throw new CliUsageError("A command is required");
    if (group === "--help" || group === "help") {
      io.stdout(`Runtime CLI: daemon, project, models, session, run

Runtime approvals (require --project ID; works for governed managers and delegated turns):
  approvals list [--scope-id ID]
  approvals decide --request-id ID --scope-id ID --generation ID --decision allow|deny|acceptForSession --approved-by ACTOR --explicit-user-act

Delegated runtime (all require --project ID):
  delegated capabilities
  delegated turn --turn-id ID --prompt TEXT [--role untyped|agent0|agent1|agent2|task] [--previous-turn ID]
  delegated interrupt --turn-id ID
  delegated consent --posture off|ask-per-destination|on --approved-by ACTOR --explicit-user-act
  delegated approvals --turn-id ID
  delegated decide-approval --request-id ID --turn-id ID --generation ID --decision allow|deny|acceptForSession --approved-by ACTOR --explicit-user-act
  hosted-login start|status|cancel
Mutations also require --compatibility ID --basis-sha256 SHA256.
Login uses operator credentials. Approval records do not imply provider forwarding.
`);
      return 0;
    }
    const action = group === "run" ? undefined : argv[1];
    const rest = group === "run" ? argv.slice(1) : argv.slice(2);
    const args = parseArguments(rest);
    const json = flag(args, "json");

    if (group === "release" && action === "measure-support") {
      const path = requiredOption(args, "recipe");
      let recipe: unknown;
      try { recipe = JSON.parse(await deps.readTextFile(path)); } catch { throw new CliUsageError("Release support recipe must be valid JSON"); }
      if (!recipe || typeof recipe !== "object" || Array.isArray(recipe)) throw new CliUsageError("Release support recipe must be an object");
      const value = recipe as Omit<RuntimePayloadSupportObservationInputV2, "embeddedRuntime">;
      const embeddedRuntime = { electron: process.versions.electron ?? "", node: process.versions.node, modules: process.versions.modules ?? "", napi: process.versions.napi ?? "", architecture: process.arch };
      printJson(io, await deps.measureRuntimeSupportProfile({ ...value, embeddedRuntime }), true); return 0;
    }
    if (group === "approvals") {
      const projectId = requiredOption(args, "project");
      let result: unknown;
      if (action === "list") {
        if (!deps.client.pendingRuntimeApprovals) throw new RuntimeError("ENGINE_UNAVAILABLE", "Runtime approval API unavailable", 503);
        result = await deps.client.pendingRuntimeApprovals(projectId, option(args, "scope-id"));
      } else if (action === "decide") {
        if (!deps.client.decideRuntimeApproval) throw new RuntimeError("ENGINE_UNAVAILABLE", "Runtime approval API unavailable", 503);
        const decision = requiredOption(args, "decision");
        if (!["allow", "deny", "acceptForSession"].includes(decision) || !flag(args, "explicit-user-act")) throw new CliUsageError("Approval decision requires a known decision and --explicit-user-act");
        result = await deps.client.decideRuntimeApproval(projectId, requiredOption(args, "request-id"), { compatibilityIdentity: requiredOption(args, "compatibility"), contractBasisSha256: requiredOption(args, "basis-sha256") }, { turnId: requiredOption(args, "scope-id"), workerGeneration: requiredOption(args, "generation"), decision: decision as "allow" | "deny" | "acceptForSession", approvedBy: requiredOption(args, "approved-by"), explicitUserAct: true });
      } else throw new CliUsageError("approvals requires list or decide");
      printJson(io, result, json); return 0;
    }

    if (group === "hosted-login" || group === "delegated") {
      const projectId = requiredOption(args, "project");
      const compatibility = (): RuntimeCompatibilityIdentity => ({ compatibilityIdentity: requiredOption(args, "compatibility"), contractBasisSha256: requiredOption(args, "basis-sha256") });
      const missing = (): never => { throw new RuntimeError("ENGINE_UNAVAILABLE", "Runtime client does not support this operation", 503); };
      let result: unknown;
      if (group === "hosted-login") {
        if (action === "start") result = await (deps.client.startHostedLogin?.(projectId, compatibility()) ?? missing());
        else if (action === "status") result = await (deps.client.hostedLoginStatus?.(projectId) ?? missing());
        else if (action === "cancel") result = await (deps.client.cancelHostedLogin?.(projectId, compatibility()) ?? missing());
        else throw new CliUsageError("hosted-login requires start, status, or cancel");
      } else if (action === "capabilities") result = await (deps.client.delegatedCapabilities?.(projectId) ?? missing());
      else if (action === "turn") {
        const prompt = option(args, "prompt") ?? await io.readStdin();
        const requestedRole = option(args, "role") ?? "untyped";
        if (!["untyped", "agent0", "agent1", "agent2", "task"].includes(requestedRole)) throw new CliUsageError("Unknown runtime role");
        result = await (deps.client.runDelegatedTurn?.(projectId, compatibility(), { turnId: requiredOption(args, "turn-id"), prompt, ...(option(args, "previous-turn") ? { previousTurnId: option(args, "previous-turn") } : {}), requestedRole: requestedRole as "untyped"|"agent0"|"agent1"|"agent2"|"task" }) ?? missing());
      } else if (action === "interrupt") result = await (deps.client.interruptDelegatedTurn?.(projectId, requiredOption(args, "turn-id"), compatibility()) ?? missing());
      else if (action === "approvals") result = await (deps.client.pendingDelegatedApprovals?.(projectId, requiredOption(args, "turn-id")) ?? missing());
      else if (action === "decide-approval") {
        const decision = requiredOption(args, "decision");
        if (!["allow", "deny", "acceptForSession"].includes(decision) || !flag(args, "explicit-user-act")) throw new CliUsageError("Approval decision requires a known decision and --explicit-user-act");
        result = await (deps.client.decideDelegatedApproval?.(projectId, requiredOption(args, "request-id"), compatibility(), { turnId: requiredOption(args, "turn-id"), workerGeneration: requiredOption(args, "generation"), decision: decision as "allow"|"deny"|"acceptForSession", approvedBy: requiredOption(args, "approved-by"), explicitUserAct: true }) ?? missing());
      } else if (action === "consent") {
        const posture = requiredOption(args, "posture");
        if (!["off", "ask-per-destination", "on"].includes(posture) || !flag(args, "explicit-user-act")) throw new CliUsageError("Consent requires a known posture and --explicit-user-act");
        result = await (deps.client.grantDelegatedConsent?.(projectId, compatibility(), { posture: posture as "off"|"ask-per-destination"|"on", approvedBy: requiredOption(args, "approved-by"), explicitUserAct: true }) ?? missing());
      } else throw new CliUsageError("delegated requires capabilities, turn, interrupt, consent, approvals, or decide-approval");
      printJson(io, result, json);
      return 0;
    }

    if (group === "daemon") {
      if (action === "install") {
        await deps.launchAgent.install(
          option(args, "executable") ?? deps.executablePath
        );
        printJson(io, { installed: true }, json);
      } else if (action === "start") {
        await deps.launchAgent.start();
        printJson(io, { started: true }, json);
      } else if (action === "stop") {
        await deps.launchAgent.stop();
        printJson(io, { stopped: true }, json);
      } else if (action === "status") {
        printJson(
          io,
          {
            launchAgent: await deps.launchAgent.status(),
            daemon: await deps.client.daemonStatus()
          },
          json
        );
      } else if (action === "uninstall") {
        await deps.launchAgent.uninstall();
        printJson(io, { uninstalled: true }, json);
      } else {
        throw new CliUsageError(
          "daemon requires install, start, stop, status, or uninstall"
        );
      }
      return 0;
    }

    if (group === "project") {
      if (action === "register") {
        const manifestPath =
          option(args, "manifest") ?? args.positionals[0];
        if (!manifestPath) {
          throw new CliUsageError(
            "project register requires a manifest path or --manifest"
          );
        }
        printJson(
          io,
          await deps.client.registerProject({
            manifestPath,
            approvedBy: option(args, "approved-by") ?? "local-operator",
            approvalReference:
              option(args, "approval-reference") ?? "cli-explicit-registration"
          }),
          json
        );
      } else if (action === "list") {
        printJson(io, await deps.client.listProjects(), json);
      } else if (action === "status") {
        printJson(
          io,
          await deps.client.projectStatus(
            option(args, "project") ?? args.positionals[0] ??
              requiredOption(args, "project")
          ),
          json
        );
      } else {
        throw new CliUsageError("project requires register, list, or status");
      }
      return 0;
    }

    if (group === "models") {
      if (action === "list") {
        printJson(io, await deps.client.listModels(), json);
      } else if (action === "activate") {
        const modelId =
          option(args, "model") ?? args.positionals[0];
        if (!modelId) throw new CliUsageError("models activate requires an exact model ID");
        printJson(
          io,
          await deps.client.activateModel(
            modelId,
            option(args, "approval-reference") ??
              "cli-explicit-model-activation"
          ),
          json
        );
      } else {
        throw new CliUsageError("models requires list or activate");
      }
      return 0;
    }

    if (group === "session") {
      const projectId = requiredOption(args, "project");
      if (action === "create") {
        const requestFile = option(args, "request-file");
        const request =
          requestFile === undefined
            ? {
                projectId,
                role: requiredOption(args, "role") as CreateSessionRequest["role"],
                engineSelection: {
                  adapterId: requiredOption(args, "adapter"),
                  providerId: requiredOption(args, "provider"),
                  model: requiredOption(args, "model")
                },
                ...(option(args, "parent-session") === undefined
                  ? {}
                  : { parentSessionId: option(args, "parent-session") })
              }
            : await readRequestFile<CreateSessionRequest>(requestFile, deps);
        printJson(io, await deps.client.createSession(projectId, request), json);
      } else if (action === "list") {
        printJson(io, await deps.client.listSessions(projectId), json);
      } else {
        const sessionId =
          option(args, "session") ?? args.positionals[0];
        if (!sessionId) {
          throw new CliUsageError(`session ${action ?? ""} requires --session`);
        }
        if (action === "replay") {
          printJson(io, await deps.client.replaySession(projectId, sessionId), json);
        } else if (action === "turn") {
          return await streamEvents(
            io,
            await deps.client.turnSession(
              projectId,
              sessionId,
              await readPrompt(args, io, deps)
            ),
            json
          );
        } else if (action === "interrupt") {
          printJson(
            io,
            await deps.client.interruptSession(projectId, sessionId),
            json
          );
        } else {
          throw new CliUsageError(
            "session requires create, list, replay, turn, or interrupt"
          );
        }
      }
      return 0;
    }

    if (group === "run") {
      const run = await readRunRequest(args, io, deps);
      return await streamEvents(
        io,
        await deps.client.runAgent1(run.projectId, run.request),
        json
      );
    }

    throw new CliUsageError(`Unknown command: ${argv.join(" ")}`);
  } catch (error) {
    if (error instanceof CliUsageError) {
      io.stderr(`chirality: ${error.message}\n`);
      return 2;
    }
    if (error instanceof RuntimeError) {
      if (error.code === "RUNTIME_COMPATIBILITY_MISMATCH" || argv.includes("--json")) {
        io.stderr(`${JSON.stringify({ error: { code: error.code, message: error.message, ...(error.details === undefined ? {} : { details: error.details }) } })}\n`);
      } else {
        io.stderr(`${error.code}: ${error.message}\n`);
      }
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

async function readStandardInput(): Promise<string> {
  const chunks: Buffer[] = [];
  for await (const chunk of process.stdin) {
    chunks.push(Buffer.isBuffer(chunk) ? chunk : Buffer.from(chunk));
  }
  return Buffer.concat(chunks).toString("utf8");
}

export function createDefaultCliDependencies(): CliDependencies {
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
    launchAgent: new LaunchAgentManager(
      {
        launchAgentsDirectory: paths.launchAgentsDirectory,
        runtimeDirectory: paths.runtimeDirectory
      },
      undefined,
      undefined,
      resolveRuntimeLaunchAgentOptions(process.env, paths.userData)
    ),
    executablePath: process.execPath,
    readTextFile: (path) => readFile(path, "utf8"),
    measureRuntimeSupportProfile: (input) => observeRuntimeSupportProfileFromPayloadV2(input)
  };
}

export const processCliIo: CliIo = {
  stdout(text) {
    process.stdout.write(text);
  },
  stderr(text) {
    process.stderr.write(text);
  },
  readStdin: readStandardInput
};
