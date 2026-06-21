import { query, type Query } from '@anthropic-ai/claude-agent-sdk';
import { createHash, randomUUID } from 'node:crypto';
import { AgentEnginePort, AgentEngineRunInput } from './agent-engine-port';
import { getUiApiKey } from './api-key-store';
import { HarnessError } from './errors';
import { redactConfiguredApiKeys } from './run-logger';
import { buildSdkOptions, buildSdkPrompt } from './sdk-options-builder';
import {
  createSdkToolEvidenceState,
  mapSdkMessageToHarnessWithArtifacts
} from './sdk-message-mapper';
import { appendHarnessEvent } from './session-events';
import { ContentBlock, IAgentSdkManager, ResolvedOpts, SessionRecord, UIEvent } from './types';
import { createHarnessEvent, type HarnessEvent } from './event-schema';
import { harnessEventToUiEvent } from './harness-ui-bridge';
import {
  getPermissionEventChannel,
  type SessionPermissionChannel
} from './permission-event-channel';
import { getPermissionBroker } from './permission-broker';
import { CLAUDE_AGENT_SDK_PACKAGE_VERSION } from './sdk-version';

type SdkQuery = typeof query;

type ActiveTurnState = {
  abortController: AbortController;
  query?: Query;
  interrupted: boolean;
  permissionChannel?: SessionPermissionChannel;
};

const ANTHROPIC_API_KEY_ENV = 'ANTHROPIC_API_KEY';

function asNonEmptyString(value: string | undefined): string | undefined {
  if (typeof value !== 'string') {
    return undefined;
  }
  const trimmed = value.trim();
  return trimmed.length > 0 ? trimmed : undefined;
}

function hashPrompt(systemPrompt: string): string {
  return createHash('sha256').update(systemPrompt).digest('hex');
}

function readSdkApiKeyForTurn(): string | undefined {
  return (
    getUiApiKey() ??
    asNonEmptyString(process.env.ANTHROPIC_API_KEY) ??
    asNonEmptyString(process.env.CHIRALITY_ANTHROPIC_API_KEY)
  );
}

function installAnthropicApiKeyForSdkTurn(): (() => void) | undefined {
  const apiKey = readSdkApiKeyForTurn();
  if (!apiKey) {
    return undefined;
  }

  const hadPriorValue = Object.prototype.hasOwnProperty.call(process.env, ANTHROPIC_API_KEY_ENV);
  const priorValue = process.env.ANTHROPIC_API_KEY;
  process.env.ANTHROPIC_API_KEY = apiKey;

  return () => {
    if (hadPriorValue) {
      process.env.ANTHROPIC_API_KEY = priorValue;
      return;
    }
    delete process.env.ANTHROPIC_API_KEY;
  };
}

export class ClaudeAgentSdkManager implements IAgentSdkManager, AgentEnginePort {
  readonly subject = 'claude-agent-sdk' as const;
  private readonly activeTurns = new Map<string, ActiveTurnState>();

  constructor(
    private readonly sdkQuery: SdkQuery = query,
    private readonly buildSystemPrompt: (
      projectRoot: string,
      persona: string,
      mode: string,
      tools?: readonly string[]
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
    let restoreSdkApiKey: (() => void) | undefined;

    // D-APP-25 manager-lifecycle bridging. `turn.accepted` / `turn.started` are
    // emitted before the SDK reports session:init, so we hold their bridged
    // UIEvents and flush them immediately after session:init keeps the public
    // contract (session:init present, process:exit terminal) intact even if the
    // turn is interrupted before the adapter initializes. Terminal lifecycle
    // events (interruption.completed / turn.interrupted / turn.failed) bridge in
    // place via emitAndBridge.
    const pendingLifecycleUiEvents: UIEvent[] = [];
    let lifecycleBridgeFlushed = false;
    const bufferLifecycleBridge = (event: HarnessEvent): void => {
      const bridged = harnessEventToUiEvent(event);
      if (bridged) {
        pendingLifecycleUiEvents.push(bridged);
      }
    };
    const emitAndBridge = async function* (
      type: HarnessEvent['type'],
      data: Record<string, unknown>
    ): AsyncGenerator<UIEvent> {
      const event = createHarnessEvent({ sessionId: input.session.sessionId, type, data });
      await appendHarnessEvent(event);
      const bridged = harnessEventToUiEvent(event);
      if (bridged) {
        yield bridged;
      }
    };

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
        input.opts.mode,
        input.opts.tools
      );
      const personaPromptHash = hashPrompt(systemPrompt);
      const sdkOptions = buildSdkOptions({
        session: input.session,
        opts: input.opts,
        abortController,
        systemPrompt
      });
      const sdkPrompt = buildSdkPrompt(input.message, input.contentBlocks);
      restoreSdkApiKey = installAnthropicApiKeyForSdkTurn();
      const turnAcceptedEvent = createHarnessEvent({
        sessionId: input.session.sessionId,
        type: 'turn.accepted',
        data: {
          provider: 'claude-agent-sdk',
          sdkPackageVersion: CLAUDE_AGENT_SDK_PACKAGE_VERSION,
          persona: input.opts.persona,
          mode: input.opts.mode,
          personaPromptHash,
          bootFingerprint: input.session.bootFingerprint,
          model: input.opts.model
        }
      });
      await appendHarnessEvent(turnAcceptedEvent);
      bufferLifecycleBridge(turnAcceptedEvent);
      const sdkStream = this.sdkQuery({
        prompt: sdkPrompt,
        options: sdkOptions
      });
      activeTurn.query = sdkStream;
      const turnStartedEvent = createHarnessEvent({
        sessionId: input.session.sessionId,
        type: 'turn.started',
        data: {
          provider: 'claude-agent-sdk'
        }
      });
      await appendHarnessEvent(turnStartedEvent);
      bufferLifecycleBridge(turnStartedEvent);

      let sawTerminal = false;
      const mapperState = createSdkToolEvidenceState({
        parentPersona: input.opts.persona,
        projectRoot: input.session.projectRoot,
        mode: input.opts.mode
      });

      // Merge the SDK message stream with the out-of-band permission-event
      // channel. `canUseTool` publishes `tool.permission` events to the channel
      // while the SDK iterator is suspended awaiting a verdict, so racing the two
      // lets those events reach the browser live (as `harness:event`s) instead of
      // being stranded until the SDK produces its next message.
      const permissionChannel = getPermissionEventChannel().open(input.session.sessionId);
      // Capture this turn's channel instance so teardown only retires its own.
      activeTurn.permissionChannel = permissionChannel;
      const sdkIterator = sdkStream[Symbol.asyncIterator]();
      let sdkNext = sdkIterator.next();
      let permNext = permissionChannel.next();
      // A promise that never settles — parks the permission side of the race once
      // the channel is closed so the SDK side decides the rest of the stream.
      const never = new Promise<never>(() => {}) as ReturnType<typeof permissionChannel.next>;

      while (true) {
        const winner = await Promise.race([
          sdkNext.then((result) => ({ kind: 'sdk' as const, result })),
          permNext.then((result) => ({ kind: 'perm' as const, result }))
        ]);

        if (winner.kind === 'perm') {
          if (winner.result.done) {
            permNext = never;
            continue;
          }
          const bridged = harnessEventToUiEvent(winner.result.value);
          if (bridged) {
            yield bridged;
          }
          permNext = permissionChannel.next();
          continue;
        }

        const { value: sdkMessage, done } = winner.result;
        if (done) {
          break;
        }

        if (activeTurn.interrupted) {
          yield* emitAndBridge('interruption.completed', { provider: 'claude-agent-sdk' });
          yield* emitAndBridge('turn.interrupted', { provider: 'claude-agent-sdk' });
          yield {
            type: 'process:exit',
            data: {
              exitCode: 130,
              interrupted: true
            }
          };
          return;
        }

        const mapped = await mapSdkMessageToHarnessWithArtifacts(
          input.session.sessionId,
          sdkMessage,
          mapperState
        );
        for (const event of mapped.harnessEvents) {
          await appendHarnessEvent(event);
          const bridged = harnessEventToUiEvent(event);
          if (bridged) {
            // Forward rich evidence before the thin uiEvents of the same message so the
            // terminal process:exit (a uiEvent) remains the final public event.
            yield bridged;
          }
        }
        // Flush any buffered permission events before this message's uiEvents so a
        // terminal process:exit always stays last.
        for (const event of permissionChannel.drain()) {
          const bridged = harnessEventToUiEvent(event);
          if (bridged) {
            yield bridged;
          }
        }
        for (const event of mapped.uiEvents) {
          if (event.type === 'process:exit') {
            sawTerminal = true;
          }
          yield event;
          // Flush the buffered turn.accepted / turn.started bridges immediately
          // after session:init so the live timeline reads accepted -> started
          // while keeping session:init as the first public UIEvent.
          if (!lifecycleBridgeFlushed && event.type === 'session:init') {
            for (const lifecycleEvent of pendingLifecycleUiEvents) {
              yield lifecycleEvent;
            }
            pendingLifecycleUiEvents.length = 0;
            lifecycleBridgeFlushed = true;
          }
        }

        sdkNext = sdkIterator.next();
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
        yield* emitAndBridge('interruption.completed', { provider: 'claude-agent-sdk' });
        yield* emitAndBridge('turn.interrupted', { provider: 'claude-agent-sdk' });
        yield {
          type: 'process:exit',
          data: {
            exitCode: 130,
            interrupted: true
          }
        };
        return;
      }

      const messageText =
        redactConfiguredApiKeys(error instanceof Error ? error.message : 'Claude Agent SDK turn failed') ??
        'Claude Agent SDK turn failed';
      yield* emitAndBridge('turn.failed', {
        provider: 'claude-agent-sdk',
        sdkPackageVersion: CLAUDE_AGENT_SDK_PACKAGE_VERSION,
        error: messageText
      });
      throw new HarnessError('SDK_FAILURE', 500, messageText, {
        provider: 'claude-agent-sdk',
        sdkPackageVersion: CLAUDE_AGENT_SDK_PACKAGE_VERSION
      });
    } finally {
      // Release any approval the turn is still suspended on (e.g. the SSE stream
      // was cancelled without an interrupt call) so no broker entry outlives the
      // turn, then tear down the live channel. All three teardowns are scoped to
      // THIS turn's identity (its AbortController / channel instance / state), so
      // if the one-turn lock was released early (the cancel/disconnect path) and a
      // newer same-session turn already installed fresh state, this stale teardown
      // cannot clobber it (DESIGN §5.3 identity guard).
      getPermissionBroker().clearSession(input.session.sessionId, 'deny', abortController);
      getPermissionEventChannel().close(input.session.sessionId, activeTurn.permissionChannel);
      restoreSdkApiKey?.();
      if (this.activeTurns.get(input.session.sessionId) === activeTurn) {
        this.activeTurns.delete(input.session.sessionId);
      }
    }
  }
}
