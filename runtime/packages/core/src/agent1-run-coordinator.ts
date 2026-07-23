import { randomUUID } from "node:crypto";
import { readFile, realpath, stat } from "node:fs/promises";
import { join, resolve } from "node:path";
import {
  RuntimeError,
  type Agent1RunRequest,
  type EngineSelection,
  type RuntimeSessionRecord,
  type RuntimeToolDefinition,
  type UIEvent
} from "@chirality/runtime-contracts";
import { atomicWriteJson, isContained, sha256 } from "./fs.js";
import type { ProjectRegistry } from "./project-registry.js";
import type { ResidencyCoordinator } from "./residency-coordinator.js";
import type { SessionStore } from "./session-store.js";
import type { TurnCoordinator } from "./turn-coordinator.js";

export interface Agent2Return {
  childSessionId: string;
  returnText: string;
  model: string;
  residencyEpoch: string;
}

export interface Agent1ManagerHooks {
  delegate(input: { sealedBrief: string }): Promise<Agent2Return>;
  review(input: {
    childSessionId: string;
    decision: "accepted" | "rejected";
    rationale: string;
  }): Promise<void>;
}

export interface Agent1ManagerRuntimePort {
  execute(
    session: RuntimeSessionRecord,
    request: Agent1RunRequest,
    hooks: Agent1ManagerHooks
  ): AsyncIterable<UIEvent>;
}

export interface RuntimeToolBindingPort {
  bind(sessionId: string, tools: readonly RuntimeToolDefinition[]): Promise<() => Promise<void>>;
}

export interface GovernedAgent1RunOptions {
  projects: ProjectRegistry;
  sessions: SessionStore;
  turns: TurnCoordinator;
  residency: ResidencyCoordinator;
  manager: Agent1ManagerRuntimePort;
  tools: RuntimeToolBindingPort;
  resolveManagerSelection(projectId: string): Promise<EngineSelection>;
}

interface AgentRunRecord {
  schemaVersion: "chirality.agent-run/v1";
  runId: string;
  projectId: string;
  managerSessionId: string;
  managerAgentId: string;
  managerSelection: EngineSelection;
  child?: {
    sessionId: string;
    role: "agent2";
    selection: EngineSelection;
    residencyEpoch: string;
    sealedBriefHash: string;
    permissions: ["read"];
    tool: "read_file";
  };
  review?: {
    decision: "accepted" | "rejected";
    rationaleHash: string;
  };
  status: "completed" | "failed";
  failureCode?: string;
  approvalReference: string;
  createdAt: string;
  completedAt: string;
}

export class GovernedAgent1RunCoordinator {
  constructor(private readonly options: GovernedAgent1RunOptions) {}

  async *run(projectId: string, request: Agent1RunRequest): AsyncIterable<UIEvent> {
    const project = await this.options.projects.requireAuthorized(projectId);
    if (request.brief.trim() === "") {
      throw new RuntimeError("INVALID_REQUEST", "Agent 1 brief cannot be empty");
    }
    const managerAgentId = request.agentId ?? "HELP_HUMAN";
    const managerDefinition = (await this.listManagerDefinitions(projectId)).find(
      (agent) => agent.agentId === managerAgentId
    );
    if (managerDefinition === undefined || managerDefinition.agentType !== 1) {
      throw new RuntimeError(
        "DELEGATION_POLICY_VIOLATION",
        `Direct run target must be an Agent 1: ${managerAgentId}`,
        403
      );
    }
    const managerSelection = await this.options.resolveManagerSelection(projectId);
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
    let child:
      | {
          sessionId: string;
          selection: EngineSelection;
          epoch: string;
          sealedBriefHash: string;
        }
      | undefined;
    let review: { decision: "accepted" | "rejected"; rationaleHash: string } | undefined;
    const accepted = await this.options.sessions.appendEvent(projectId, {
      sessionId: managerSession.sessionId,
      turnId,
      type: "turn.accepted",
      data: { runId, agentId: managerAgentId, briefHash: sha256(request.brief) }
    });
    yield { type: "harness:event", data: accepted };
    const hooks: Agent1ManagerHooks = {
      delegate: async ({ sealedBrief }) => {
        if (request.localModel === undefined) {
          throw new RuntimeError(
            "DELEGATION_POLICY_VIOLATION",
            "This run did not authorize a local child",
            403
          );
        }
        if (child !== undefined) {
          throw new RuntimeError(
            "DELEGATION_POLICY_VIOLATION",
            "Agent 1 may launch at most one local child in this milestone",
            403
          );
        }
        if (request.readOnlyTool?.name !== "read_file") {
          throw new RuntimeError(
            "DELEGATION_POLICY_VIOLATION",
            "Local child requires one declared read_file tool",
            403
          );
        }
        const residency = await this.options.residency.status();
        if (
          residency.phase !== "READY" ||
          residency.managedModelId !== request.localModel ||
          residency.epoch === undefined
        ) {
          throw new RuntimeError(
            "MODEL_NOT_RESIDENT",
            `Exact local model is not resident: ${request.localModel}`,
            409
          );
        }
        const selection: EngineSelection = {
          adapterId: "pi",
          providerId: "omlx",
          model: request.localModel
        };
        const childSession = await this.options.sessions.create({
          projectId,
          role: "agent2",
          engineSelection: selection,
          parentSessionId: managerSession.sessionId
        });
        const tool = await this.readFileTool(
          project.canonicalRoot,
          request.readOnlyTool.relativePath
        );
        const release = await this.options.tools.bind(childSession.sessionId, [tool]);
        let text = "";
        let successful = false;
        try {
          for await (const event of this.options.turns.run(
            projectId,
            childSession.sessionId,
            { prompt: sealedBrief },
            ["read_file"]
          )) {
            if (event.type === "chat:delta" || event.type === "chat:complete") {
              text += event.data.text;
            }
            if (event.type === "process:exit") successful = event.data.exitCode === 0;
          }
        } finally {
          await release();
        }
        if (!successful) {
          throw new RuntimeError("ENGINE_UNAVAILABLE", "Local child did not complete", 502);
        }
        child = {
          sessionId: childSession.sessionId,
          selection,
          epoch: residency.epoch.epochId,
          sealedBriefHash: sha256(sealedBrief)
        };
        return {
          childSessionId: childSession.sessionId,
          returnText: text,
          model: request.localModel,
          residencyEpoch: residency.epoch.epochId
        };
      },
      review: async (input) => {
        if (child === undefined || input.childSessionId !== child.sessionId) {
          throw new RuntimeError(
            "DELEGATION_POLICY_VIOLATION",
            "Review must refer to this manager's governed child",
            403
          );
        }
        review = {
          decision: input.decision,
          rationaleHash: sha256(input.rationale)
        };
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
      }
    };
    let failure: RuntimeError | undefined;
    try {
      for await (const event of this.options.manager.execute(managerSession, request, hooks)) {
        if (event.type === "process:exit") {
          throw new RuntimeError(
            "INTERNAL_FAILURE",
            "Manager runtime must leave terminal ownership to the coordinator",
            500
          );
        }
        if (
          event.type === "harness:event" &&
          ["turn.completed", "turn.failed", "turn.cancelled", "turn.interrupted"].includes(
            event.data.type
          )
        ) {
          throw new RuntimeError(
            "INTERNAL_FAILURE",
            "Manager runtime emitted a terminal harness event",
            500
          );
        }
        if (event.type === "harness:event") {
          await this.options.sessions.persistEvent(projectId, event.data);
        }
        yield event;
      }
      if (request.localModel !== undefined && (child === undefined || review === undefined)) {
        failure = new RuntimeError(
          "REQUIRED_DELEGATION_MISSING",
          "Agent 1 did not complete and review the required local delegation",
          409
        );
      }
    } catch (error) {
      failure =
        error instanceof RuntimeError
          ? error
          : new RuntimeError("INTERNAL_FAILURE", "Agent 1 run failed", 500);
    }
    const completedAt = new Date().toISOString();
    const record: AgentRunRecord = {
      schemaVersion: "chirality.agent-run/v1",
      runId,
      projectId,
      managerSessionId: managerSession.sessionId,
      managerAgentId,
      managerSelection,
      status: failure === undefined ? "completed" : "failed",
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
              sealedBriefHash: child.sealedBriefHash,
              permissions: ["read"],
              tool: "read_file"
            }
          }),
      ...(review === undefined ? {} : { review }),
      ...(failure === undefined ? {} : { failureCode: failure.code })
    };
    await this.persistAgentRun(projectId, runId, record);
    const terminal = await this.options.sessions.appendEvent(projectId, {
      sessionId: managerSession.sessionId,
      turnId,
      type: failure === undefined ? "turn.completed" : "turn.failed",
      data:
        failure === undefined
          ? { runId }
          : { runId, code: failure.code, message: failure.message }
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

  private async readFileTool(
    projectRoot: string,
    relativePath: string
  ): Promise<RuntimeToolDefinition> {
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
    return {
      name: "read_file",
      description: "Read the one file declared by the governing Agent 1 run.",
      inputSchema: {
        type: "object",
        properties: {},
        additionalProperties: false
      },
      permission: { effect: "allow", operation: "read", roots: [canonicalPath] },
      async execute(_input, signal) {
        if (signal.aborted) throw new RuntimeError("INTERRUPTED", "Read interrupted", 499);
        return { path: relativePath, content: await readFile(canonicalPath, "utf8") };
      }
    };
  }

  private async listManagerDefinitions(
    projectId: string
  ): Promise<readonly { agentId: string; agentType: 0 | 1 | 2 }[]> {
    const roots = await this.options.projects.roots(projectId);
    const result: { agentId: string; agentType: 0 | 1 | 2 }[] = [];
    const { readdir } = await import("node:fs/promises");
    for (const directory of [join(roots.instructionRoot, "agents"), join(roots.workingRoot, "agents")]) {
      for (const entry of await readdir(directory, { withFileTypes: true }).catch(() => [])) {
        const nameMatch = /^AGENT_(.+)\.md$/u.exec(entry.name);
        if (!entry.isFile() || nameMatch?.[1] === undefined) continue;
        const source = await readFile(join(directory, entry.name), "utf8");
        const match = /AGENT_TYPE\s*:\s*([012])/iu.exec(source);
        if (match?.[1] !== undefined) {
          result.push({
            agentId: nameMatch[1],
            agentType: Number(match[1]) as 0 | 1 | 2
          });
        }
      }
    }
    return result;
  }

  private async persistAgentRun(
    projectId: string,
    runId: string,
    record: AgentRunRecord
  ): Promise<void> {
    const project = await this.options.projects.requireAuthorized(projectId);
    const manifest = await this.options.projects.readManifest(projectId);
    const executionRoot = await realpath(resolve(project.canonicalRoot, manifest.defaultExecutionRoot));
    if (!isContained(project.canonicalRoot, executionRoot)) {
      throw new RuntimeError("FORBIDDEN", "Execution root escapes the project", 403);
    }
    await atomicWriteJson(
      join(executionRoot, "_Coordination", "AgentRuns", "runtime", runId, "run.json"),
      record
    );
  }
}
