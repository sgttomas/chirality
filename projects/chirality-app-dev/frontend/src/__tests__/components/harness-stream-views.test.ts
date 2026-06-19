import { createElement } from 'react';
import { renderToStaticMarkup } from 'react-dom/server';
import { describe, expect, it } from 'vitest';
import type { HarnessEvent, HarnessEventType } from '../../lib/harness/event-schema';
import {
  deriveSubagentActivity,
  deriveToolActivity
} from '../../lib/shell/harness-event-views';
import { SubagentStreamList } from '../../components/shell/subagent-stream-view';
import { ToolStreamList } from '../../components/shell/tool-stream-view';

let counter = 0;

function event(type: HarnessEventType, data: Record<string, unknown>): HarnessEvent {
  counter += 1;
  return {
    schemaVersion: 1,
    eventId: `evt_${counter}`,
    sessionId: 'sess_test',
    timestamp: '2026-06-18T00:00:00.000Z',
    type,
    data
  };
}

describe('ToolStreamList rendering', () => {
  it('shows an empty hint when there is no tool activity', () => {
    const html = renderToStaticMarkup(createElement(ToolStreamList, { rows: [] }));
    expect(html).toContain('No tool activity yet');
  });

  it('renders a row with tool name, status badge, and path field', () => {
    const events = [
      event('tool.queued', {
        toolUseId: 't1',
        toolName: 'Read',
        source: 'model',
        inputMetadata: { pathFields: { file_path: '/a/b.ts' } }
      }),
      event('tool.completed', { toolUseId: 't1', toolName: 'Read' })
    ];

    const html = renderToStaticMarkup(
      createElement(ToolStreamList, { rows: deriveToolActivity(events) })
    );

    expect(html).toContain('Read');
    expect(html).toContain('harness-status-badge--completed');
    expect(html).toContain('/a/b.ts');
  });
});

describe('SubagentStreamList rendering', () => {
  it('shows an empty hint when there is no subagent activity', () => {
    const html = renderToStaticMarkup(createElement(SubagentStreamList, { rows: [] }));
    expect(html).toContain('No subagent activity yet');
  });

  it('renders a row with agent name, description, and status badge', () => {
    const events = [
      event('subagent.started', {
        taskId: 'task-1',
        childRunId: 'c1',
        agentName: 'TASK',
        description: 'Investigate the failing import'
      }),
      event('subagent.completed', { taskId: 'task-1', childRunId: 'c1', outputArtifactPath: '/runs/c1.md' })
    ];

    const html = renderToStaticMarkup(
      createElement(SubagentStreamList, { rows: deriveSubagentActivity(events) })
    );

    expect(html).toContain('TASK');
    expect(html).toContain('Investigate the failing import');
    expect(html).toContain('harness-status-badge--completed');
  });
});
