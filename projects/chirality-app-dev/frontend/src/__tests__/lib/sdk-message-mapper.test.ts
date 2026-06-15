import { describe, expect, it } from 'vitest';
import {
  createSdkToolEvidenceState,
  mapSdkMessageToHarness
} from '../../lib/harness/sdk-message-mapper';

describe('mapSdkMessageToHarness', () => {
  it('maps SDK init metadata to stable session:init UI event and HarnessEvent evidence', () => {
    const mapped = mapSdkMessageToHarness('sess_1', {
      type: 'system',
      subtype: 'init',
      session_id: 'sdk_1',
      uuid: '00000000-0000-0000-0000-000000000001',
      apiKeySource: 'temporary',
      claude_code_version: '1.2.3',
      cwd: '/tmp/project',
      tools: [],
      mcp_servers: [],
      model: 'claude-test',
      permissionMode: 'default',
      slash_commands: [],
      output_style: 'default',
      skills: [],
      plugins: []
    });

    expect(mapped.sdkSessionId).toBe('sdk_1');
    expect(mapped.sdkClaudeCodeVersion).toBe('1.2.3');
    expect(mapped.uiEvents).toEqual([
      {
        type: 'session:init',
        data: {
          engineSessionId: 'sdk_1',
          claudeSessionId: 'sdk_1',
          model: 'claude-test'
        }
      }
    ]);
    expect(mapped.harnessEvents[0]).toMatchObject({
      schemaVersion: 1,
      sessionId: 'sess_1',
      type: 'adapter.initialized'
    });
    expect(mapped.harnessEvents[0].data).toMatchObject({
      adapterName: 'claude-agent-sdk',
      adapterSessionId: 'sdk_1',
      sdkSessionId: 'sdk_1'
    });
  });

  it('maps stream text and terminal result without changing UI event names', () => {
    const delta = mapSdkMessageToHarness('sess_1', {
      type: 'stream_event',
      event: {
        type: 'content_block_delta',
        index: 0,
        delta: { type: 'text_delta', text: 'Hello' }
      },
      parent_tool_use_id: null,
      uuid: '00000000-0000-0000-0000-000000000002',
      session_id: 'sdk_1'
    });
    expect(delta.uiEvents).toEqual([{ type: 'chat:delta', data: { text: 'Hello' } }]);
    expect(delta.harnessEvents.map((event) => event.type)).toEqual([
      'model.delta',
      'message.delta'
    ]);

    const terminal = mapSdkMessageToHarness('sess_1', {
      type: 'result',
      subtype: 'success',
      duration_ms: 10,
      duration_api_ms: 9,
      is_error: false,
      num_turns: 1,
      result: 'Hello',
      stop_reason: 'end_turn',
      total_cost_usd: 0,
      usage: {} as never,
      modelUsage: {},
      permission_denials: [],
      uuid: '00000000-0000-0000-0000-000000000003',
      session_id: 'sdk_1'
    });

    expect(terminal.uiEvents.map((event) => event.type)).toEqual([
      'chat:complete',
      'session:complete',
      'process:exit'
    ]);
    expect(terminal.harnessEvents.map((event) => event.type)).toEqual([
      'model.completed',
      'turn.completed'
    ]);
  });

  it('maps SDK-only system messages into provider-neutral HarnessEvent types', () => {
    const permission = mapSdkMessageToHarness('sess_1', {
      type: 'system',
      subtype: 'permission_denied',
      uuid: '00000000-0000-0000-0000-000000000004',
      session_id: 'sdk_1',
      tool_name: 'Write',
      decision_reason: 'read-only mode',
      decision_reason_type: 'policy',
      message: 'permission denied'
    } as never);
    const compact = mapSdkMessageToHarness('sess_1', {
      type: 'system',
      subtype: 'compact_boundary',
      uuid: '00000000-0000-0000-0000-000000000005',
      session_id: 'sdk_1',
      compact_metadata: { preservedTurns: 3 }
    } as never);
    const mirror = mapSdkMessageToHarness('sess_1', {
      type: 'system',
      subtype: 'mirror_error',
      uuid: '00000000-0000-0000-0000-000000000006',
      session_id: 'sdk_1',
      error: 'mirror failed',
      key: 'transcript-key'
    } as never);

    expect([
      permission.harnessEvents[0].type,
      compact.harnessEvents[0].type,
      mirror.harnessEvents[0].type
    ]).toEqual(['tool.permission', 'context.compacted', 'runtime.mirror.error']);
    expect(permission.harnessEvents.map((event) => event.type)).toEqual([
      'tool.permission',
      'tool.failed'
    ]);
    expect(permission.harnessEvents[0].data).toMatchObject({
      behavior: 'deny',
      source: 'adapter',
      adapterToolName: 'Write'
    });
  });

  it('maps assistant tool use and queued user messages into Chirality lifecycle events', () => {
    const assistant = mapSdkMessageToHarness('sess_1', {
      type: 'assistant',
      message: {
        role: 'assistant',
        content: [
          { type: 'text', text: 'I will inspect the file.' },
          { type: 'tool_use', id: 'toolu_1', name: 'Read', input: { file_path: 'README.md' } }
        ]
      },
      parent_tool_use_id: null,
      uuid: '00000000-0000-0000-0000-000000000007',
      session_id: 'sdk_1'
    } as never);
    expect(assistant.uiEvents).toEqual([
      { type: 'chat:delta', data: { text: 'I will inspect the file.' } }
    ]);
    expect(assistant.harnessEvents.map((event) => event.type)).toEqual([
      'model.delta',
      'message.completed',
      'tool.queued'
    ]);
    expect(assistant.harnessEvents[2].data).toMatchObject({
      source: 'model',
      toolUseId: 'toolu_1',
      toolName: 'Read',
      descriptorName: 'read_file',
      inputMetadata: {
        inputKeys: ['file_path'],
        pathFields: {
          file_path: 'README.md'
        }
      }
    });
    expect(assistant.harnessEvents[2].data).not.toHaveProperty('input');

    const queuedUser = mapSdkMessageToHarness('sess_1', {
      type: 'user',
      message: {
        role: 'user',
        content: 'follow up later'
      },
      parent_tool_use_id: null,
      isSynthetic: false,
      priority: 'later',
      shouldQuery: false,
      uuid: '00000000-0000-0000-0000-000000000008',
      session_id: 'sdk_1'
    } as never);
    expect(queuedUser.harnessEvents.map((event) => event.type)).toEqual([
      'message.completed',
      'queue.enqueued'
    ]);
  });

  it('emits SDK read built-in lifecycle evidence from queued tool use results', () => {
    const state = createSdkToolEvidenceState();
    mapSdkMessageToHarness(
      'sess_1',
      {
        type: 'assistant',
        message: {
          role: 'assistant',
          content: [
            { type: 'tool_use', id: 'toolu_read', name: 'Read', input: { file_path: 'README.md' } }
          ]
        },
        parent_tool_use_id: null,
        uuid: '00000000-0000-0000-0000-000000000014',
        session_id: 'sdk_1'
      } as never,
      state
    );

    const userResult = mapSdkMessageToHarness(
      'sess_1',
      {
        type: 'user',
        message: {
          role: 'user',
          content: []
        },
        parent_tool_use_id: 'toolu_read',
        tool_use_result: {
          type: 'tool_result',
          tool_use_id: 'toolu_read',
          content: 'raw file contents'
        },
        uuid: '00000000-0000-0000-0000-000000000015',
        session_id: 'sdk_1'
      } as never,
      state
    );

    expect(userResult.harnessEvents.map((event) => event.type)).toEqual([
      'tool.started',
      'tool.completed',
      'message.completed'
    ]);
    expect(userResult.harnessEvents[1].data).toMatchObject({
      source: 'adapter',
      toolUseId: 'toolu_read',
      toolName: 'Read',
      descriptorName: 'read_file',
      resultMetadata: {
        resultByteLength: expect.any(Number),
        inlineByteLimit: 65536,
        artifactByteLimit: 2097152,
        overflowPolicy: 'artifact',
        budgetClass: 'within-inline-budget',
        rawOutputPersisted: false
      }
    });
    expect(JSON.stringify(userResult.harnessEvents[1].data)).not.toContain('raw file contents');
  });

  it('maps SDK read tool error results to failed evidence and skips duplicate MCP completions', () => {
    const state = createSdkToolEvidenceState();
    mapSdkMessageToHarness(
      'sess_1',
      {
        type: 'assistant',
        message: {
          role: 'assistant',
          content: [
            { type: 'tool_use', id: 'toolu_grep', name: 'Grep', input: { pattern: 'needle' } },
            {
              type: 'tool_use',
              id: 'toolu_mcp',
              name: 'mcp__chirality__status_read',
              input: { deliverablePath: 'PKG/DEL' }
            }
          ]
        },
        parent_tool_use_id: null,
        uuid: '00000000-0000-0000-0000-000000000016',
        session_id: 'sdk_1'
      } as never,
      state
    );

    const failedRead = mapSdkMessageToHarness(
      'sess_1',
      {
        type: 'user',
        message: {
          role: 'user',
          content: []
        },
        parent_tool_use_id: 'toolu_grep',
        tool_use_result: {
          type: 'tool_result',
          tool_use_id: 'toolu_grep',
          is_error: true,
          content: 'grep failed'
        },
        uuid: '00000000-0000-0000-0000-000000000017',
        session_id: 'sdk_1'
      } as never,
      state
    );
    const mcpResult = mapSdkMessageToHarness(
      'sess_1',
      {
        type: 'user',
        message: {
          role: 'user',
          content: []
        },
        parent_tool_use_id: 'toolu_mcp',
        tool_use_result: {
          type: 'tool_result',
          tool_use_id: 'toolu_mcp',
          content: 'mcp result body'
        },
        uuid: '00000000-0000-0000-0000-000000000018',
        session_id: 'sdk_1'
      } as never,
      state
    );

    expect(failedRead.harnessEvents.map((event) => event.type)).toEqual([
      'tool.started',
      'tool.failed',
      'message.completed'
    ]);
    expect(failedRead.harnessEvents[1].data).toMatchObject({
      failureSource: 'tool_use_result',
      resultMetadata: {
        rawOutputPersisted: false
      }
    });
    expect(JSON.stringify(failedRead.harnessEvents[1].data)).not.toContain('grep failed');
    expect(mcpResult.harnessEvents.map((event) => event.type)).toEqual(['message.completed']);
  });

  it('maps SDK tool, hook, status, and subagent messages into expanded HarnessEvent categories', () => {
    const toolProgress = mapSdkMessageToHarness('sess_1', {
      type: 'tool_progress',
      tool_use_id: 'toolu_1',
      tool_name: 'Read',
      parent_tool_use_id: null,
      elapsed_time_seconds: 1.5,
      uuid: '00000000-0000-0000-0000-000000000009',
      session_id: 'sdk_1'
    } as never);
    const hookStarted = mapSdkMessageToHarness('sess_1', {
      type: 'system',
      subtype: 'hook_started',
      hook_id: 'hook_1',
      hook_name: 'PreToolUse',
      hook_event: 'PreToolUse',
      uuid: '00000000-0000-0000-0000-000000000010',
      session_id: 'sdk_1'
    } as never);
    const hookFailed = mapSdkMessageToHarness('sess_1', {
      type: 'system',
      subtype: 'hook_response',
      hook_id: 'hook_1',
      hook_name: 'PreToolUse',
      hook_event: 'PreToolUse',
      output: 'denied',
      stdout: '',
      stderr: 'blocked',
      exit_code: 1,
      outcome: 'error',
      uuid: '00000000-0000-0000-0000-000000000011',
      session_id: 'sdk_1'
    } as never);
    const status = mapSdkMessageToHarness('sess_1', {
      type: 'system',
      subtype: 'status',
      status: 'compacting',
      permissionMode: 'default',
      uuid: '00000000-0000-0000-0000-000000000012',
      session_id: 'sdk_1'
    } as never);
    const task = mapSdkMessageToHarness('sess_1', {
      type: 'system',
      subtype: 'task_started',
      task_id: 'task_1',
      tool_use_id: 'toolu_2',
      description: 'Run bounded task',
      subagent_type: 'TASK',
      uuid: '00000000-0000-0000-0000-000000000013',
      session_id: 'sdk_1'
    } as never);

    expect([
      toolProgress.harnessEvents[0].type,
      hookStarted.harnessEvents[0].type,
      hookFailed.harnessEvents[0].type,
      status.harnessEvents[0].type,
      task.harnessEvents[0].type
    ]).toEqual([
      'tool.progress',
      'hook.started',
      'hook.failed',
      'context.compaction.started',
      'subagent.started'
    ]);
  });
});
