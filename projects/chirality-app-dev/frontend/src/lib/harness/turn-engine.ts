import { hasUiApiKey } from './api-key-store';
import { randomUUID } from 'node:crypto';
import { asHarnessError, HarnessError } from '@chirality/harness-contract/errors';
import { resolveRuntimeOptions } from './options';
import { CLAUDE_AGENT_SDK_PACKAGE_VERSION } from '@chirality/harness-contract/sdk-version';
import { evaluateSubagentGovernance } from './subagent-governance';
import { resolveHarnessToolPool } from './tool-pool';
import { appendHarnessEvent } from './session-events';
import { createHarnessEvent } from './event-factory';
import {
  AttachmentError,
  AttachmentFailureDetails,
  ContentBlock,
  HarnessOpts,
  IAgentSdkManager,
  IAttachmentResolver,
  IPersonaManager,
  ISessionManager,
  ResolvedOpts,
  SessionRecord,
  TurnErrorSeverity,
  TurnRequest,
  UIEvent
} from '@chirality/harness-contract/types';

const MAX_ATTACHMENT_WARNING_DETAILS = 3;
export type TurnEngineProviderMode = 'stub' | 'anthropic' | 'agentSdk';

export type RunningHarnessTurn = {
  sessionId: string;
  events: AsyncIterable<UIEvent>;
  cancel(): Promise<void>;
};

type TurnEngineRunInput = {
  sessionId: string;
  message: string;
  opts?: HarnessOpts;
  attachments: string[];
};

type SubagentGovernanceEvaluator = typeof evaluateSubagentGovernance;
type RuntimeOptionsResolver = typeof resolveRuntimeOptions;

export type TurnEngineDependencies = {
  sessionManager: ISessionManager;
  personaManager: IPersonaManager;
  attachmentResolver: IAttachmentResolver;
  agentSdkManager: IAgentSdkManager;
  resolveProviderMode?: () => TurnEngineProviderMode;
  hasUiApiKey?: () => boolean;
  env?: NodeJS.ProcessEnv;
  sdkPackageVersion?: string;
  resolveRuntimeOptions?: RuntimeOptionsResolver;
  evaluateSubagentGovernance?: SubagentGovernanceEvaluator;
};

type StreamTurnInput = {
  session: SessionRecord;
  providerMode: TurnEngineProviderMode;
  message: string;
  opts: ResolvedOpts;
  contentBlocks?: ContentBlock[];
  releaseTurnLock: () => void;
  turnId: string;
};

type TurnEngineAgentSdkManager = IAgentSdkManager & {
  cancel?(sessionId: string): Promise<void>;
  startTurn(
    session: SessionRecord,
    message: string,
    opts: ResolvedOpts,
    contentBlocks?: ContentBlock[],
    turnId?: string
  ): AsyncIterable<UIEvent>;
};

function asNonEmptyString(value: string | undefined): string | undefined {
  if (typeof value !== 'string') {
    return undefined;
  }
  const trimmed = value.trim();
  return trimmed.length > 0 ? trimmed : undefined;
}

function requireNonEmptyString(value: unknown, field: string): string {
  if (typeof value !== 'string' || value.trim().length === 0) {
    throw new HarnessError('INVALID_REQUEST', 400, `Missing or invalid '${field}'`);
  }

  return value.trim();
}

function requireStringArray(value: unknown, field: string): string[] {
  if (!Array.isArray(value) || value.some((item) => typeof item !== 'string')) {
    throw new HarnessError('INVALID_REQUEST', 400, `Field '${field}' must be an array of strings`);
  }

  return value;
}

function parseTurnRequest(value: unknown): TurnEngineRunInput {
  if (!value || typeof value !== 'object' || Array.isArray(value)) {
    throw new HarnessError('INVALID_REQUEST', 400, 'Request body must be a JSON object');
  }

  const record = value as Record<string, unknown>;
  const sessionId = requireNonEmptyString(record.sessionId, 'sessionId');
  if (typeof record.message !== 'string') {
    throw new HarnessError('INVALID_REQUEST', 400, "Missing or invalid 'message'");
  }

  return {
    sessionId,
    message: record.message,
    opts: record.opts as HarnessOpts | undefined,
    attachments:
      record.attachments === undefined ? [] : requireStringArray(record.attachments, 'attachments')
  };
}

function basenameLike(rawPath: string): string {
  const segments = rawPath.split(/[\\/]/).filter((segment) => segment.length > 0);
  if (segments.length === 0) {
    return rawPath;
  }
  return segments[segments.length - 1];
}

function buildAttachmentWarningText(errors: AttachmentError[]): string | undefined {
  if (errors.length === 0) {
    return undefined;
  }

  const lines = errors
    .slice(0, MAX_ATTACHMENT_WARNING_DETAILS)
    .map((error) => `- ${basenameLike(error.path)}: ${error.reason}`);
  const remaining = errors.length - lines.length;
  if (remaining > 0) {
    lines.push(`- ... ${remaining} additional attachment error(s) omitted`);
  }

  return [
    `Attachment warning: ${errors.length} attachment(s) could not be processed. Continuing with available content.`,
    'Rejected attachments:',
    ...lines
  ].join('\n');
}

function classifyStreamErrorSeverity(status: number): TurnErrorSeverity {
  return status >= 500 ? 'error' : 'warning';
}

function buildAttachmentFailureDetails(errors: AttachmentError[]): AttachmentFailureDetails {
  return {
    category: 'ALL_ATTACHMENTS_FAILED_NO_TEXT',
    attachmentErrors: errors,
    rejectedAttachmentCount: errors.length
  };
}

function assertKnownAgentSdkTools(sessionId: string, opts: ResolvedOpts): void {
  const toolPool = resolveHarnessToolPool({
    sessionId,
    requestedTools: opts.tools,
    mode: opts.mode
  });

  if (toolPool.unknownTools.length === 0) {
    return;
  }

  const toolNames = toolPool.unknownTools.map((issue) => issue.toolName).join(', ');
  throw new HarnessError('INVALID_REQUEST', 400, `Unknown harness tool(s): ${toolNames}`, {
    category: 'UNKNOWN_TOOLS',
    unknownTools: toolPool.unknownTools
  });
}

export class TurnEngine {
  private readonly activeSessionTurns = new Set<string>();
  private readonly resolveProviderMode: () => TurnEngineProviderMode;
  private readonly hasUiApiKey: () => boolean;
  private readonly env: NodeJS.ProcessEnv;
  private readonly sdkPackageVersion: string;
  private readonly resolveRuntimeOptions: RuntimeOptionsResolver;
  private readonly evaluateSubagentGovernance: SubagentGovernanceEvaluator;

  constructor(private readonly dependencies: TurnEngineDependencies) {
    this.resolveProviderMode = dependencies.resolveProviderMode ?? (() => 'stub');
    this.hasUiApiKey = dependencies.hasUiApiKey ?? hasUiApiKey;
    this.env = dependencies.env ?? process.env;
    this.sdkPackageVersion = dependencies.sdkPackageVersion ?? CLAUDE_AGENT_SDK_PACKAGE_VERSION;
    this.resolveRuntimeOptions = dependencies.resolveRuntimeOptions ?? resolveRuntimeOptions;
    this.evaluateSubagentGovernance =
      dependencies.evaluateSubagentGovernance ?? evaluateSubagentGovernance;
  }

  async runTurn(request: TurnRequest | unknown): Promise<RunningHarnessTurn> {
    const input = parseTurnRequest(request);
    const session = await this.dependencies.sessionManager.resume(input.sessionId);
    const providerMode = this.resolveProviderMode();

    if (
      (providerMode === 'anthropic' || providerMode === 'agentSdk') &&
      !this.hasAnthropicApiKeyConfigured()
    ) {
      throw new HarnessError(
        'MISSING_API_KEY',
        503,
        'Anthropic API key is not configured. Enter a key in Settings or set ANTHROPIC_API_KEY.',
        {
          provider: 'anthropic',
          category: 'MISSING_API_KEY'
        }
      );
    }

    if (this.activeSessionTurns.has(input.sessionId)) {
      throw new HarnessError(
        'TURN_IN_PROGRESS',
        409,
        'A turn is already in progress for this session',
        { sessionId: input.sessionId }
      );
    }

    this.activeSessionTurns.add(input.sessionId);
    let released = false;
    let cancellationPersisted = false;
    const releaseTurnLock = (): void => {
      if (released) {
        return;
      }
      released = true;
      this.activeSessionTurns.delete(input.sessionId);
    };

    try {
      const resolvedOpts = await this.resolveRuntimeOptions(session, input.opts);
      if (providerMode === 'agentSdk') {
        assertKnownAgentSdkTools(input.sessionId, resolvedOpts);
      }

      const attachmentResolution =
        await this.dependencies.attachmentResolver.resolveAttachmentsToContentBlocks(
          input.message,
          input.attachments
        );

      const warningText = buildAttachmentWarningText(attachmentResolution.errors);
      const contentBlocks: ContentBlock[] = warningText
        ? [{ type: 'text', text: warningText }, ...attachmentResolution.contentBlocks]
        : attachmentResolution.contentBlocks;
      const text = input.message.trim();
      const hasExecutableAttachment = attachmentResolution.contentBlocks.some(
        (block) => block.type === 'file'
      );

      if (!text && !hasExecutableAttachment) {
        throw new HarnessError(
          'ATTACHMENT_FAILURE',
          400,
          'Turn requires text content or at least one valid attachment',
          buildAttachmentFailureDetails(attachmentResolution.errors)
        );
      }

      await this.dependencies.personaManager.buildSystemPrompt(
        session.projectRoot,
        resolvedOpts.persona,
        resolvedOpts.mode,
        resolvedOpts.tools
      );

      const governanceDecision = await this.evaluateSubagentGovernance(
        resolvedOpts.persona,
        resolvedOpts.subagentGovernance
      );
      const effectiveOpts = governanceDecision.allowed
        ? {
            ...resolvedOpts,
            delegatedSubagents: governanceDecision.delegatedSubagents,
            delegatedAgentInstructions: governanceDecision.delegatedAgentInstructions
          }
        : {
            ...resolvedOpts,
            delegatedSubagents: [],
            delegatedAgentInstructions: {}
          };
      const turnMessage =
        !hasExecutableAttachment && warningText
          ? [warningText, input.message].filter((part) => part.trim().length > 0).join('\n\n')
          : input.message;
      const turnContentBlocks = hasExecutableAttachment ? contentBlocks : undefined;
      const turnId = `turn_${randomUUID()}`;

      // Acceptance belongs to the route-independent lifecycle boundary. Persist the
      // raw user-authored text before provider iteration starts so replay can recover
      // an accepted message even when the provider never yields. appendHarnessEvent
      // applies the configured secret redaction policy before writing JSONL.
      await appendHarnessEvent(
        createHarnessEvent({
          sessionId: input.sessionId,
          turnId,
          type: 'message.accepted',
          data: {
            turnId,
            role: 'user',
            text: input.message
          }
        })
      );

      const agentSdkManager = this.dependencies.agentSdkManager as TurnEngineAgentSdkManager;

      return {
        sessionId: input.sessionId,
        events: this.streamTurn({
          session,
          providerMode,
          message: turnMessage,
          opts: effectiveOpts,
          contentBlocks: turnContentBlocks,
          releaseTurnLock,
          turnId
        }),
        cancel: async (): Promise<void> => {
          if (cancellationPersisted) {
            releaseTurnLock();
            return;
          }
          cancellationPersisted = true;
          try {
            // A transport disconnect is not an explicit user interrupt (D-APP-40).
            // Persist its own terminal outcome before best-effort provider shutdown.
            await appendHarnessEvent(
              createHarnessEvent({
                sessionId: input.sessionId,
                turnId,
                type: 'turn.cancelled',
                data: {
                  turnId,
                  reason: 'client_disconnect'
                }
              })
            );
            await agentSdkManager.cancel?.(input.sessionId);
          } catch {
            // Stream cancellation is best-effort; the route still needs the lock released.
          } finally {
            releaseTurnLock();
          }
        }
      };
    } catch (error) {
      releaseTurnLock();
      throw error;
    }
  }

  async interrupt(sessionId: string): Promise<void> {
    await this.dependencies.agentSdkManager.interrupt(sessionId);
  }

  private hasAnthropicApiKeyConfigured(): boolean {
    return (
      this.hasUiApiKey() ||
      Boolean(
        asNonEmptyString(this.env.ANTHROPIC_API_KEY) ??
          asNonEmptyString(this.env.CHIRALITY_ANTHROPIC_API_KEY)
      )
    );
  }

  private async *streamTurn(input: StreamTurnInput): AsyncIterable<UIEvent> {
    try {
      for await (const event of (this.dependencies.agentSdkManager as TurnEngineAgentSdkManager).startTurn(
        input.session,
        input.message,
        input.opts,
        input.contentBlocks,
        input.turnId
      )) {
        if (event.type === 'session:init') {
          const engineSessionId = event.data.engineSessionId ?? event.data.claudeSessionId;
          await this.dependencies.sessionManager.save(input.session.sessionId, {
            engineSessionId,
            claudeSessionId: event.data.claudeSessionId,
            model: event.data.model,
            ...(input.providerMode === 'agentSdk'
              ? {
                  sdkSessionId: engineSessionId,
                  sdkPackageVersion: this.sdkPackageVersion
                }
              : {})
          });
        }

        yield event;
      }
    } catch (error) {
      const harnessError = asHarnessError(error);
      const severity = classifyStreamErrorSeverity(harnessError.status);
      yield {
        type: 'turn:error',
        data: {
          phase: 'mid-stream',
          errorType: harnessError.type,
          message: harnessError.message,
          status: harnessError.status,
          severity,
          fatal: true,
          details: harnessError.details
        }
      };
      yield {
        type: 'process:exit',
        data: {
          exitCode: 1,
          interrupted: false,
          error: harnessError.message,
          errorType: harnessError.type,
          status: harnessError.status,
          severity,
          fatal: true,
          errorDetails: harnessError.details
        }
      };
    } finally {
      input.releaseTurnLock();
    }
  }
}
