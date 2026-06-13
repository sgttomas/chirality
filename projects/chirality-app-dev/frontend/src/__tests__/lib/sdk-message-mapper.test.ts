import { describe, expect, it } from 'vitest';
import { mapSdkMessageToHarness } from '../../lib/harness/sdk-message-mapper';

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
    expect(permission.harnessEvents[0].data).toMatchObject({
      behavior: 'deny',
      source: 'adapter',
      adapterToolName: 'Write'
    });
  });
});
