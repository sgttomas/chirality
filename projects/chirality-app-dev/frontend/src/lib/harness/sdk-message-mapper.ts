import type {
  SDKAssistantMessage,
  SDKCompactBoundaryMessage,
  SDKMessage,
  SDKMirrorErrorMessage,
  SDKPartialAssistantMessage,
  SDKPermissionDeniedMessage,
  SDKResultMessage,
  SDKSystemMessage
} from '@anthropic-ai/claude-agent-sdk';
import { createHarnessEvent, HarnessEvent } from './event-schema';
import { redactJsonLike } from './run-logger';
import { UIEvent } from './types';

export type SdkMessageMapping = {
  uiEvents: UIEvent[];
  harnessEvents: HarnessEvent[];
  sdkSessionId?: string;
  sdkClaudeCodeVersion?: string;
};

function readTextFromContentBlock(block: unknown): string | undefined {
  if (!block || typeof block !== 'object') {
    return undefined;
  }
  const candidate = block as { type?: unknown; text?: unknown };
  return candidate.type === 'text' && typeof candidate.text === 'string'
    ? candidate.text
    : undefined;
}

function readAssistantText(message: SDKAssistantMessage): string {
  const content = message.message.content;
  if (!Array.isArray(content)) {
    return '';
  }

  return content.map(readTextFromContentBlock).filter(Boolean).join('');
}

function readPartialText(message: SDKPartialAssistantMessage): string {
  const event = message.event as unknown;
  if (!event || typeof event !== 'object') {
    return '';
  }

  const candidate = event as {
    type?: unknown;
    delta?: { type?: unknown; text?: unknown };
  };
  if (candidate.type === 'content_block_delta' && typeof candidate.delta?.text === 'string') {
    return candidate.delta.text;
  }
  return '';
}

function isSystemInit(message: SDKMessage): message is SDKSystemMessage {
  return message.type === 'system' && 'subtype' in message && message.subtype === 'init';
}

function isCompactBoundary(message: SDKMessage): message is SDKCompactBoundaryMessage {
  return message.type === 'system' && 'subtype' in message && message.subtype === 'compact_boundary';
}

function isPermissionDenied(message: SDKMessage): message is SDKPermissionDeniedMessage {
  return message.type === 'system' && 'subtype' in message && message.subtype === 'permission_denied';
}

function isMirrorError(message: SDKMessage): message is SDKMirrorErrorMessage {
  return message.type === 'system' && 'subtype' in message && message.subtype === 'mirror_error';
}

export function mapSdkMessageToHarness(
  sessionId: string,
  message: SDKMessage
): SdkMessageMapping {
  if (isSystemInit(message)) {
    return {
      sdkSessionId: message.session_id,
      sdkClaudeCodeVersion: message.claude_code_version,
      uiEvents: [
        {
          type: 'session:init',
          data: {
            claudeSessionId: message.session_id,
            model: message.model
          }
        }
      ],
      harnessEvents: [
        createHarnessEvent({
          sessionId,
          type: 'sdk.system.init',
          data: redactJsonLike({
            sdkSessionId: message.session_id,
            sdkClaudeCodeVersion: message.claude_code_version,
            model: message.model,
            tools: message.tools,
            mcpServers: message.mcp_servers,
            permissionMode: message.permissionMode
          })
        })
      ]
    };
  }

  if (message.type === 'stream_event') {
    const text = readPartialText(message);
    return {
      sdkSessionId: message.session_id,
      uiEvents: text
        ? [
            {
              type: 'chat:delta',
              data: {
                text
              }
            }
          ]
        : [],
      harnessEvents: text
        ? [
            createHarnessEvent({
              sessionId,
              type: 'model.delta',
              data: redactJsonLike({ text })
            })
          ]
        : []
    };
  }

  if (message.type === 'assistant') {
    const text = readAssistantText(message);
    return {
      sdkSessionId: message.session_id,
      uiEvents: text
        ? [
            {
              type: 'chat:delta',
              data: {
                text
              }
            }
          ]
        : [],
      harnessEvents: text
        ? [
            createHarnessEvent({
              sessionId,
              type: 'model.delta',
              data: redactJsonLike({ text })
            })
          ]
        : []
    };
  }

  if (message.type === 'result') {
    const result = message as SDKResultMessage;
    if (result.subtype === 'success') {
      return {
        sdkSessionId: result.session_id,
        uiEvents: [
          {
            type: 'chat:complete',
            data: {
              text: result.result
            }
          },
          {
            type: 'session:complete',
            data: {}
          },
          {
            type: 'process:exit',
            data: {
              exitCode: 0
            }
          }
        ],
        harnessEvents: [
          createHarnessEvent({
            sessionId,
            type: 'model.completed',
            data: redactJsonLike({
              sdkSessionId: result.session_id,
              stopReason: result.stop_reason,
              numTurns: result.num_turns,
              terminalReason: result.terminal_reason
            })
          }),
          createHarnessEvent({
            sessionId,
            type: 'turn.completed',
            data: redactJsonLike({
              sdkSessionId: result.session_id,
              totalCostUsd: result.total_cost_usd
            })
          })
        ]
      };
    }

    return {
      sdkSessionId: result.session_id,
      uiEvents: [
        {
          type: 'process:exit',
          data: {
            exitCode: 1,
            error: result.errors.join('\n') || result.subtype,
            errorType: 'SDK_FAILURE',
            status: 500,
            severity: 'error',
            fatal: true,
            errorDetails: redactJsonLike({
              subtype: result.subtype,
              terminalReason: result.terminal_reason,
              permissionDenials: result.permission_denials
            })
          }
        }
      ],
      harnessEvents: [
        createHarnessEvent({
          sessionId,
          type: 'turn.failed',
          data: redactJsonLike({
            sdkSessionId: result.session_id,
            subtype: result.subtype,
            errors: result.errors,
            terminalReason: result.terminal_reason
          })
        })
      ]
    };
  }

  if (isPermissionDenied(message)) {
    return {
      sdkSessionId: message.session_id,
      uiEvents: [
        {
          type: 'tool:result',
          data: {
            name: message.tool_name,
            ok: false,
            output: message.message
          }
        }
      ],
      harnessEvents: [
        createHarnessEvent({
          sessionId,
          type: 'sdk.permission.denied',
          data: redactJsonLike({
            sdkSessionId: message.session_id,
            toolName: message.tool_name,
            reason: message.decision_reason,
            reasonType: message.decision_reason_type,
            message: message.message
          })
        })
      ]
    };
  }

  if (isCompactBoundary(message)) {
    return {
      sdkSessionId: message.session_id,
      uiEvents: [],
      harnessEvents: [
        createHarnessEvent({
          sessionId,
          type: 'sdk.compact.boundary',
          data: redactJsonLike({
            sdkSessionId: message.session_id,
            compactMetadata: message.compact_metadata
          })
        })
      ]
    };
  }

  if (isMirrorError(message)) {
    return {
      sdkSessionId: message.session_id,
      uiEvents: [],
      harnessEvents: [
        createHarnessEvent({
          sessionId,
          type: 'sdk.mirror.error',
          data: redactJsonLike({
            sdkSessionId: message.session_id,
            error: message.error,
            key: message.key
          })
        })
      ]
    };
  }

  return {
    sdkSessionId: 'session_id' in message ? message.session_id : undefined,
    uiEvents: [],
    harnessEvents: []
  };
}
