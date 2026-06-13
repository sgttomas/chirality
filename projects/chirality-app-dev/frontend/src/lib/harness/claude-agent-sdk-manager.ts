import { query, type Query } from '@anthropic-ai/claude-agent-sdk';
import { randomUUID } from 'node:crypto';
import { AgentEnginePort, AgentEngineRunInput } from './agent-engine-port';
import { HarnessError } from './errors';
import { buildSdkOptions, buildSdkPrompt } from './sdk-options-builder';
import { mapSdkMessageToHarness } from './sdk-message-mapper';
import { appendHarnessEvent } from './session-events';
import { ContentBlock, IAgentSdkManager, ResolvedOpts, SessionRecord, UIEvent } from './types';
import { createHarnessEvent } from './event-schema';

type SdkQuery = typeof query;

type ActiveTurnState = {
  abortController: AbortController;
  query?: Query;
  interrupted: boolean;
};

const SDK_PACKAGE_VERSION = '0.3.150';

export class ClaudeAgentSdkManager implements IAgentSdkManager, AgentEnginePort {
  readonly subject = 'claude-agent-sdk' as const;
  private readonly activeTurns = new Map<string, ActiveTurnState>();

  constructor(
    private readonly sdkQuery: SdkQuery = query,
    private readonly buildSystemPrompt: (
      projectRoot: string,
      persona: string,
      mode: string
    ) => Promise<string> = async () => ''
  ) {}

  async interrupt(sessionId: string): Promise<void> {
    const activeTurn = this.activeTurns.get(sessionId);
    if (!activeTurn) {
      throw new HarnessError('SESSION_NOT_FOUND', 404, `No active turn for session '${sessionId}'`, {
        sessionId
      });
    }

    await appendHarnessEvent(
      createHarnessEvent({
        sessionId,
        type: 'interruption.requested',
        data: {
          provider: 'claude-agent-sdk'
        }
      })
    );
    activeTurn.interrupted = true;
    activeTurn.abortController.abort();
    await activeTurn.query?.interrupt().catch(() => undefined);
    activeTurn.query?.close();
  }

  startTurn(input: AgentEngineRunInput): AsyncIterable<UIEvent>;
  startTurn(
    session: SessionRecord,
    message: string,
    opts: ResolvedOpts,
    contentBlocks?: ContentBlock[]
  ): AsyncIterable<UIEvent>;
  async *startTurn(
    inputOrSession: AgentEngineRunInput | SessionRecord,
    message?: string,
    opts?: ResolvedOpts,
    contentBlocks?: ContentBlock[]
  ): AsyncIterable<UIEvent> {
    const input =
      'session' in inputOrSession
        ? inputOrSession
        : {
            session: inputOrSession,
            message: message ?? '',
            opts: opts as ResolvedOpts,
            contentBlocks
          };
    const abortController = new AbortController();
    const activeTurn: ActiveTurnState = {
      abortController,
      interrupted: false
    };
    this.activeTurns.set(input.session.sessionId, activeTurn);

    const bootstrapSessionId = input.session.sdkSessionId ?? input.session.claudeSessionId ?? `sdk_${randomUUID()}`;

    try {
      if (input.message.trim() === 'bootstrap') {
        yield {
          type: 'session:init',
          data: {
            engineSessionId: bootstrapSessionId,
            claudeSessionId: bootstrapSessionId,
            model: input.opts.model
          }
        };
        yield {
          type: 'process:exit',
          data: {
            exitCode: 0
          }
        };
        return;
      }

      const systemPrompt = await this.buildSystemPrompt(
        input.session.projectRoot,
        input.opts.persona,
        input.opts.mode
      );
      const sdkOptions = buildSdkOptions({
        session: input.session,
        opts: input.opts,
        abortController,
        systemPrompt
      });
      const sdkPrompt = buildSdkPrompt(input.message, input.contentBlocks);
      await appendHarnessEvent(
        createHarnessEvent({
          sessionId: input.session.sessionId,
          type: 'turn.accepted',
          data: {
            provider: 'claude-agent-sdk',
            sdkPackageVersion: SDK_PACKAGE_VERSION,
            model: input.opts.model
          }
        })
      );
      const sdkStream = this.sdkQuery({
        prompt: sdkPrompt,
        options: sdkOptions
      });
      activeTurn.query = sdkStream;
      await appendHarnessEvent(
        createHarnessEvent({
          sessionId: input.session.sessionId,
          type: 'turn.started',
          data: {
            provider: 'claude-agent-sdk'
          }
        })
      );

      let sawTerminal = false;
      for await (const sdkMessage of sdkStream) {
        if (activeTurn.interrupted) {
          await appendHarnessEvent(
            createHarnessEvent({
              sessionId: input.session.sessionId,
              type: 'interruption.completed',
              data: {
                provider: 'claude-agent-sdk'
              }
            })
          );
          await appendHarnessEvent(
            createHarnessEvent({
              sessionId: input.session.sessionId,
              type: 'turn.cancelled',
              data: {
                provider: 'claude-agent-sdk'
              }
            })
          );
          yield {
            type: 'process:exit',
            data: {
              exitCode: 130,
              interrupted: true
            }
          };
          return;
        }

        const mapped = mapSdkMessageToHarness(input.session.sessionId, sdkMessage);
        for (const event of mapped.harnessEvents) {
          await appendHarnessEvent(event);
        }
        for (const event of mapped.uiEvents) {
          if (event.type === 'process:exit') {
            sawTerminal = true;
          }
          yield event;
        }
      }

      if (!sawTerminal) {
        yield {
          type: 'process:exit',
          data: {
            exitCode: 0
          }
        };
      }
    } catch (error) {
      if (activeTurn.interrupted || abortController.signal.aborted) {
        await appendHarnessEvent(
          createHarnessEvent({
            sessionId: input.session.sessionId,
            type: 'interruption.completed',
            data: {
              provider: 'claude-agent-sdk'
            }
          })
        );
        await appendHarnessEvent(
          createHarnessEvent({
            sessionId: input.session.sessionId,
            type: 'turn.cancelled',
            data: {
              provider: 'claude-agent-sdk'
            }
          })
        );
        yield {
          type: 'process:exit',
          data: {
            exitCode: 130,
            interrupted: true
          }
        };
        return;
      }

      const messageText = error instanceof Error ? error.message : 'Claude Agent SDK turn failed';
      await appendHarnessEvent(
        createHarnessEvent({
          sessionId: input.session.sessionId,
          type: 'turn.failed',
          data: {
            provider: 'claude-agent-sdk',
            sdkPackageVersion: SDK_PACKAGE_VERSION,
            error: messageText
          }
        })
      );
      throw new HarnessError('SDK_FAILURE', 500, messageText, {
        provider: 'claude-agent-sdk',
        sdkPackageVersion: SDK_PACKAGE_VERSION
      });
    } finally {
      this.activeTurns.delete(input.session.sessionId);
    }
  }
}
