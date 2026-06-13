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

function isRecord(value: unknown): value is Record<string, unknown> {
  return Boolean(value) && typeof value === 'object' && !Array.isArray(value);
}

function readString(value: unknown): string | undefined {
  return typeof value === 'string' && value.length > 0 ? value : undefined;
}

function readSessionId(message: SDKMessage): string | undefined {
  return isRecord(message) ? readString(message.session_id) : undefined;
}

function readMessageId(message: SDKMessage): string | undefined {
  return isRecord(message) ? readString(message.uuid) : undefined;
}

function readTextFromUnknownContent(content: unknown): string {
  if (typeof content === 'string') {
    return content;
  }
  if (!Array.isArray(content)) {
    return '';
  }

  return content.map(readTextFromContentBlock).filter(Boolean).join('');
}

function readTextFromMessageParam(message: unknown): string {
  if (!isRecord(message)) {
    return '';
  }

  return readTextFromUnknownContent(message.content);
}

function readBlockTypes(content: unknown): string[] {
  if (!Array.isArray(content)) {
    return [];
  }

  return content
    .map((block) => (isRecord(block) ? readString(block.type) : undefined))
    .filter((type): type is string => Boolean(type));
}

type ToolUseEvidence = {
  toolUseId?: string;
  toolName?: string;
  input?: unknown;
};

function readToolUsesFromContent(content: unknown): ToolUseEvidence[] {
  if (!Array.isArray(content)) {
    return [];
  }

  return content.flatMap((block) => {
    if (!isRecord(block)) {
      return [];
    }
    const type = readString(block.type);
    if (type !== 'tool_use' && type !== 'server_tool_use') {
      return [];
    }
    return [
      {
        toolUseId: readString(block.id),
        toolName: readString(block.name),
        input: block.input
      }
    ];
  });
}

function readToolUseFromStreamEvent(message: SDKPartialAssistantMessage): ToolUseEvidence | undefined {
  const event = message.event as unknown;
  if (!isRecord(event) || event.type !== 'content_block_start') {
    return undefined;
  }
  const contentBlock = event.content_block;
  if (!isRecord(contentBlock)) {
    return undefined;
  }
  const type = readString(contentBlock.type);
  if (type !== 'tool_use' && type !== 'server_tool_use') {
    return undefined;
  }

  return {
    toolUseId: readString(contentBlock.id),
    toolName: readString(contentBlock.name),
    input: contentBlock.input
  };
}

function sdkEvidence(message: SDKMessage, extra?: Record<string, unknown>): Record<string, unknown> {
  const sdkSessionId = readSessionId(message);
  return redactJsonLike({
    adapterName: 'claude-agent-sdk',
    adapterSessionId: sdkSessionId,
    adapterMessageId: readMessageId(message),
    sdkSessionId,
    ...extra
  });
}

function createSdkEvent(
  sessionId: string,
  message: SDKMessage,
  type: Parameters<typeof createHarnessEvent>[0]['type'],
  data?: Record<string, unknown>
): HarnessEvent {
  return createHarnessEvent({
    sessionId,
    type,
    data: sdkEvidence(message, data)
  });
}

function mapAssistantToolUses(sessionId: string, message: SDKAssistantMessage): HarnessEvent[] {
  const content = message.message.content;
  return readToolUsesFromContent(content).map((toolUse) =>
    createSdkEvent(sessionId, message, 'tool.queued', {
      source: 'model',
      adapterToolUseId: toolUse.toolUseId,
      adapterToolName: toolUse.toolName,
      toolUseId: toolUse.toolUseId,
      toolName: toolUse.toolName,
      input: toolUse.input
    })
  );
}

function mapSdkUserMessage(sessionId: string, message: SDKMessage): SdkMessageMapping {
  const record = message as Record<string, unknown>;
  const shouldQueue = record.shouldQuery === false || record.priority === 'next' || record.priority === 'later';
  const messageEvent = createSdkEvent(sessionId, message, 'message.completed', {
    role: 'user',
    source: record.isSynthetic ? 'synthetic' : 'operator',
    text: readTextFromMessageParam(record.message),
    blockTypes: isRecord(record.message) ? readBlockTypes(record.message.content) : [],
    priority: record.priority,
    shouldQuery: record.shouldQuery,
    synthetic: record.isSynthetic === true,
    origin: record.origin,
    parentToolUseId: record.parent_tool_use_id,
    toolUseResultPresent: record.tool_use_result !== undefined,
    timestamp: record.timestamp
  });

  return {
    sdkSessionId: readSessionId(message),
    uiEvents: [],
    harnessEvents: shouldQueue
      ? [
          messageEvent,
          createSdkEvent(sessionId, message, 'queue.enqueued', {
            queueKind: record.priority ?? 'deferred',
            shouldQuery: record.shouldQuery,
            origin: record.origin
          })
        ]
      : [messageEvent]
  };
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
  if (message.type === 'user') {
    return mapSdkUserMessage(sessionId, message);
  }

  if (isSystemInit(message)) {
    return {
      sdkSessionId: message.session_id,
      sdkClaudeCodeVersion: message.claude_code_version,
      uiEvents: [
        {
          type: 'session:init',
          data: {
            engineSessionId: message.session_id,
            claudeSessionId: message.session_id,
            model: message.model
          }
        }
      ],
      harnessEvents: [
        createHarnessEvent({
          sessionId,
          type: 'adapter.initialized',
          data: sdkEvidence(message, {
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
    const toolUse = readToolUseFromStreamEvent(message);
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
      harnessEvents: [
        ...(text
          ? [
              createSdkEvent(sessionId, message, 'model.delta', { text }),
              createSdkEvent(sessionId, message, 'message.delta', {
                role: 'assistant',
                source: 'model',
                text,
                parentToolUseId: message.parent_tool_use_id,
                timeToFirstTokenMs: message.ttft_ms
              })
            ]
          : []),
        ...(toolUse
          ? [
              createSdkEvent(sessionId, message, 'tool.queued', {
                source: 'model',
                adapterToolUseId: toolUse.toolUseId,
                adapterToolName: toolUse.toolName,
                toolUseId: toolUse.toolUseId,
                toolName: toolUse.toolName,
                input: toolUse.input,
                parentToolUseId: message.parent_tool_use_id
              })
            ]
          : [])
      ]
    };
  }

  if (message.type === 'assistant') {
    const text = readAssistantText(message);
    const content = message.message.content;
    const toolUseEvents = mapAssistantToolUses(sessionId, message);
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
      harnessEvents: [
        ...(text
          ? [
              createSdkEvent(sessionId, message, 'model.delta', { text }),
              createSdkEvent(sessionId, message, 'message.completed', {
                role: 'assistant',
                source: 'model',
                text,
                blockTypes: readBlockTypes(content),
                parentToolUseId: message.parent_tool_use_id,
                subagentType: message.subagent_type,
                taskDescription: message.task_description,
                requestId: message.request_id,
                error: message.error
              })
            ]
          : []),
        ...toolUseEvents
      ]
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
          ...(result.deferred_tool_use
            ? [
                createSdkEvent(sessionId, result, 'tool.queued', {
                  source: 'adapter',
                  queueReason: 'deferred_tool_use',
                  adapterToolUseId: result.deferred_tool_use.id,
                  adapterToolName: result.deferred_tool_use.name,
                  toolUseId: result.deferred_tool_use.id,
                  toolName: result.deferred_tool_use.name,
                  input: result.deferred_tool_use.input
                })
              ]
            : []),
          createSdkEvent(sessionId, result, 'model.completed', {
            stopReason: result.stop_reason,
            numTurns: result.num_turns,
            terminalReason: result.terminal_reason
          }),
          createSdkEvent(sessionId, result, 'turn.completed', {
            totalCostUsd: result.total_cost_usd
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
        createSdkEvent(sessionId, result, 'turn.failed', {
          subtype: result.subtype,
          errors: result.errors,
          terminalReason: result.terminal_reason
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
        createSdkEvent(sessionId, message, 'tool.permission', {
          behavior: 'deny',
          source: 'adapter',
          adapterToolUseId: message.tool_use_id,
          adapterToolName: message.tool_name,
          toolUseId: message.tool_use_id,
          toolName: message.tool_name,
          agentId: message.agent_id,
          reason: message.decision_reason,
          reasonType: message.decision_reason_type,
          message: message.message
        }),
        createSdkEvent(sessionId, message, 'tool.failed', {
          source: 'adapter',
          failureSource: 'permission',
          adapterToolUseId: message.tool_use_id,
          adapterToolName: message.tool_name,
          toolUseId: message.tool_use_id,
          toolName: message.tool_name,
          reason: message.decision_reason,
          message: message.message
        })
      ]
    };
  }

  if (isCompactBoundary(message)) {
    return {
      sdkSessionId: message.session_id,
      uiEvents: [],
      harnessEvents: [
        createSdkEvent(sessionId, message, 'context.compacted', {
          adapterCompactMetadata: message.compact_metadata,
          compactMetadata: message.compact_metadata,
          replayImplication: 'sdk_transcript_linkage_required'
        })
      ]
    };
  }

  if (isMirrorError(message)) {
    return {
      sdkSessionId: message.session_id,
      uiEvents: [],
      harnessEvents: [
        createSdkEvent(sessionId, message, 'runtime.mirror.error', {
          adapterMirrorKey: message.key,
          error: message.error,
          key: message.key
        })
      ]
    };
  }

  if (message.type === 'tool_progress') {
    return {
      sdkSessionId: message.session_id,
      uiEvents: [],
      harnessEvents: [
        createSdkEvent(sessionId, message, 'tool.progress', {
          adapterToolUseId: message.tool_use_id,
          adapterToolName: message.tool_name,
          toolUseId: message.tool_use_id,
          toolName: message.tool_name,
          parentToolUseId: message.parent_tool_use_id,
          elapsedTimeSeconds: message.elapsed_time_seconds,
          taskId: message.task_id
        })
      ]
    };
  }

  if (message.type === 'tool_use_summary') {
    return {
      sdkSessionId: message.session_id,
      uiEvents: [],
      harnessEvents: [
        createSdkEvent(sessionId, message, 'tool.completed', {
          source: 'adapter',
          summary: message.summary,
          precedingToolUseIds: message.preceding_tool_use_ids
        })
      ]
    };
  }

  if (message.type === 'system' && message.subtype === 'hook_started') {
    return {
      sdkSessionId: message.session_id,
      uiEvents: [],
      harnessEvents: [
        createSdkEvent(sessionId, message, 'hook.started', {
          hookId: message.hook_id,
          hookName: message.hook_name,
          hookEvent: message.hook_event
        })
      ]
    };
  }

  if (message.type === 'system' && message.subtype === 'hook_progress') {
    return {
      sdkSessionId: message.session_id,
      uiEvents: [],
      harnessEvents: [
        createSdkEvent(sessionId, message, 'hook.progress', {
          hookId: message.hook_id,
          hookName: message.hook_name,
          hookEvent: message.hook_event,
          stdout: message.stdout,
          stderr: message.stderr,
          output: message.output
        })
      ]
    };
  }

  if (message.type === 'system' && message.subtype === 'hook_response') {
    const eventType = message.outcome === 'success' ? 'hook.completed' : 'hook.failed';
    return {
      sdkSessionId: message.session_id,
      uiEvents: [],
      harnessEvents: [
        createSdkEvent(sessionId, message, eventType, {
          hookId: message.hook_id,
          hookName: message.hook_name,
          hookEvent: message.hook_event,
          outcome: message.outcome,
          exitCode: message.exit_code,
          stdout: message.stdout,
          stderr: message.stderr,
          output: message.output
        })
      ]
    };
  }

  if (message.type === 'system' && message.subtype === 'status') {
    const harnessEvents: HarnessEvent[] = [];
    if (message.status === 'requesting') {
      harnessEvents.push(
        createSdkEvent(sessionId, message, 'model.request.started', {
          permissionMode: message.permissionMode
        })
      );
    }
    if (message.status === 'compacting') {
      harnessEvents.push(
        createSdkEvent(sessionId, message, 'context.compaction.started', {
          permissionMode: message.permissionMode
        })
      );
    }
    if (message.compact_result === 'success') {
      harnessEvents.push(
        createSdkEvent(sessionId, message, 'context.compacted', {
          compactResult: message.compact_result,
          replayImplication: 'sdk_transcript_linkage_required'
        })
      );
    }
    if (message.compact_result === 'failed') {
      harnessEvents.push(
        createSdkEvent(sessionId, message, 'context.compaction.failed', {
          compactResult: message.compact_result,
          compactError: message.compact_error
        })
      );
    }
    return {
      sdkSessionId: message.session_id,
      uiEvents: [],
      harnessEvents
    };
  }

  if (message.type === 'system' && message.subtype === 'task_started') {
    return {
      sdkSessionId: message.session_id,
      uiEvents: [],
      harnessEvents: [
        createSdkEvent(sessionId, message, 'subagent.started', {
          taskId: message.task_id,
          toolUseId: message.tool_use_id,
          description: message.description,
          subagentType: message.subagent_type,
          taskType: message.task_type,
          workflowName: message.workflow_name,
          skipTranscript: message.skip_transcript
        })
      ]
    };
  }

  if (message.type === 'system' && message.subtype === 'task_progress') {
    return {
      sdkSessionId: message.session_id,
      uiEvents: [],
      harnessEvents: [
        createSdkEvent(sessionId, message, 'subagent.progress', {
          taskId: message.task_id,
          toolUseId: message.tool_use_id,
          description: message.description,
          subagentType: message.subagent_type,
          usage: message.usage,
          lastToolName: message.last_tool_name,
          summary: message.summary
        })
      ]
    };
  }

  if (message.type === 'system' && message.subtype === 'task_updated') {
    const status = message.patch.status;
    const eventType =
      status === 'completed'
        ? 'subagent.completed'
        : status === 'failed' || status === 'killed'
          ? 'subagent.failed'
          : 'subagent.progress';
    return {
      sdkSessionId: message.session_id,
      uiEvents: [],
      harnessEvents: [
        createSdkEvent(sessionId, message, eventType, {
          taskId: message.task_id,
          patch: message.patch
        })
      ]
    };
  }

  if (message.type === 'system' && message.subtype === 'task_notification') {
    const eventType = message.status === 'completed' ? 'subagent.completed' : 'subagent.failed';
    return {
      sdkSessionId: message.session_id,
      uiEvents: [],
      harnessEvents: [
        createSdkEvent(sessionId, message, eventType, {
          taskId: message.task_id,
          toolUseId: message.tool_use_id,
          status: message.status,
          outputFile: message.output_file,
          summary: message.summary,
          usage: message.usage,
          skipTranscript: message.skip_transcript
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
