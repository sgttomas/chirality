import { randomUUID } from "node:crypto";
import {
  RuntimeError,
  type AgentEngineRunInput,
  type HarnessEvent,
  type IAttachmentResolver,
  type SessionTurnRequest,
  type UIEvent
} from "@chirality/runtime-contracts";
import type { EngineRegistry } from "./engine-registry.js";
import type { ProjectRegistry } from "./project-registry.js";
import type { ResidencyCoordinator } from "./residency-coordinator.js";
import type { SessionStore } from "./session-store.js";

interface ActiveTurn {
  controller: AbortController;
  engineInterrupt: () => Promise<void>;
}

const HARNESS_TERMINAL_TYPES = new Set([
  "turn.completed",
  "turn.failed",
  "turn.cancelled",
  "turn.interrupted"
]);

export class TurnCoordinator {
  private readonly active = new Map<string, ActiveTurn>();

  constructor(
    private readonly projects: ProjectRegistry,
    private readonly sessions: SessionStore,
    private readonly engines: EngineRegistry,
    private readonly residency: ResidencyCoordinator,
    private readonly attachments?: IAttachmentResolver
  ) {}

  async *run(
    projectId: string,
    sessionId: string,
    request: SessionTurnRequest,
    toolNames: readonly string[] = []
  ): AsyncIterable<UIEvent> {
    await this.projects.requireAuthorized(projectId);
    let session = await this.sessions.get(projectId, sessionId);
    const key = `${projectId}\0${sessionId}`;
    if (this.active.has(key)) {
      throw new RuntimeError("SESSION_TURN_IN_PROGRESS", "Session already has an active turn", 409);
    }
    const engine = this.engines.resolve(session.engineSelection);
    const controller = new AbortController();
    const turnId = request.turnId ?? randomUUID();
    const message = request.message ?? request.prompt;
    if (message === undefined || message.trim() === "") {
      throw new RuntimeError("INVALID_REQUEST", "Turn message cannot be empty");
    }
    const local = session.engineSelection.providerId === "omlx";
    const releaseResidency = local
      ? await this.residency.admitTurn(session.engineSelection.model)
      : () => undefined;
    this.active.set(key, {
      controller,
      engineInterrupt: () => engine.interrupt(sessionId)
    });
    const input: AgentEngineRunInput = {
      session,
      message,
      opts: {
        model: request.opts?.model ?? session.engineSelection.model,
        tools: request.opts?.tools ?? [...toolNames],
        maxTurns: request.opts?.maxTurns ?? 50,
        persona: request.opts?.persona ?? session.persona,
        mode: request.opts?.mode ?? session.mode,
        ...(request.opts?.subagentGovernance === undefined
          ? {}
          : { subagentGovernance: request.opts.subagentGovernance })
      },
      turnId,
      ...(request.attachments === undefined || request.attachments.length === 0
        ? {}
        : this.attachments === undefined
          ? (() => {
              throw new RuntimeError(
                "INVALID_REQUEST",
                "Attachment resolver is unavailable",
                503
              );
            })()
          : {
              contentBlocks: (
                await this.attachments.resolveAttachmentsToContentBlocks(
                  message,
                  request.attachments
                )
              ).contentBlocks
            })
    };
    let processExitSeen = false;
    let terminalHarnessEvent: HarnessEvent | undefined;
    try {
      const accepted = await this.sessions.appendEvent(projectId, {
        sessionId,
        turnId,
        type: "turn.accepted",
        data: { message }
      });
      yield { type: "harness:event", data: accepted };
      await engine.preflight(input);
      await this.sessions.update({ ...session, status: "running" });
      for await (const received of engine.startTurn(input)) {
        if (received.type === "process:exit") {
          if (processExitSeen) {
            throw new RuntimeError("INTERNAL_FAILURE", "Engine emitted multiple process exits", 500);
          }
          processExitSeen = true;
        }
        if (received.type === "harness:event") {
          if (HARNESS_TERMINAL_TYPES.has(received.data.type)) {
            if (terminalHarnessEvent !== undefined) {
              throw new RuntimeError(
                "INTERNAL_FAILURE",
                "Engine emitted multiple terminal harness events",
                500
              );
            }
            terminalHarnessEvent = received.data;
          }
          await this.sessions.persistEvent(projectId, received.data);
        }
        if (received.type === "session:init") {
          const residencyStatus = local ? await this.residency.status() : undefined;
          session = {
            ...session,
            engineSessionId: received.data.engineSessionId,
            engineSelection: {
              adapterId: received.data.adapterId,
              providerId: received.data.providerId,
              model: received.data.model
            },
            adapterSession: {
              ...(session.adapterSession ?? {}),
              engineSessionId: received.data.engineSessionId
            },
            ...(received.data.claudeSessionId === undefined
              ? {}
              : { claudeSessionId: received.data.claudeSessionId }),
            ...(residencyStatus?.epoch === undefined
              ? {}
              : { residencyEpoch: residencyStatus.epoch.epochId })
          };
          await this.sessions.update(session);
        }
        yield received;
      }
      if (terminalHarnessEvent === undefined) {
        const completed = await this.sessions.appendEvent(projectId, {
          sessionId,
          turnId,
          type: controller.signal.aborted ? "turn.interrupted" : "turn.completed",
          data: {}
        });
        terminalHarnessEvent = completed;
        yield { type: "harness:event", data: completed };
      }
      if (!processExitSeen) {
        processExitSeen = true;
        yield {
          type: "process:exit",
          data: { exitCode: controller.signal.aborted ? 130 : 0, interrupted: controller.signal.aborted }
        };
      }
      await this.sessions.update({
        ...session,
        status: controller.signal.aborted
          ? "interrupted"
          : terminalHarnessEvent.type === "turn.completed"
            ? "completed"
            : "failed"
      });
    } catch (error) {
      const runtimeError =
        error instanceof RuntimeError
          ? error
          : new RuntimeError("INTERNAL_FAILURE", "Engine turn failed", 500);
      if (terminalHarnessEvent === undefined) {
        const failed = await this.sessions.appendEvent(projectId, {
          sessionId,
          turnId,
          type: controller.signal.aborted ? "turn.interrupted" : "turn.failed",
          data: { code: runtimeError.code, message: runtimeError.message }
        });
        yield { type: "harness:event", data: failed };
      }
      if (!processExitSeen) {
        yield {
          type: "turn:error",
          data: {
            phase: "mid-stream",
            errorType: "SDK_FAILURE",
            message: runtimeError.message,
            status: runtimeError.status,
            severity: "error",
            fatal: true,
            details: { runtimeCode: runtimeError.code }
          }
        };
        yield {
          type: "process:exit",
          data: {
            exitCode: controller.signal.aborted ? 130 : 1,
            interrupted: controller.signal.aborted,
            error: runtimeError.message,
            errorType: runtimeError.code,
            status: runtimeError.status,
            severity: "error",
            fatal: true
          }
        };
      }
      await this.sessions.update({
        ...session,
        status: controller.signal.aborted ? "interrupted" : "failed"
      });
    } finally {
      this.active.delete(key);
      releaseResidency();
    }
  }

  async interrupt(projectId: string, sessionId: string): Promise<void> {
    const active = this.active.get(`${projectId}\0${sessionId}`);
    if (active === undefined) return;
    active.controller.abort();
    await active.engineInterrupt();
  }
}
