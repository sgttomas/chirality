import { createElement } from 'react';
import { renderToStaticMarkup } from 'react-dom/server';
import { describe, expect, it } from 'vitest';
import { PermissionDecisionCards } from '../../components/shell/permission-requests';
import type { PermissionRequestRow } from '../../lib/shell/harness-event-views';

function row(overrides: Partial<PermissionRequestRow> = {}): PermissionRequestRow {
  return {
    key: 'tp1',
    toolName: 'Write',
    reason: 'requires interactive approval and write hooks before execution.',
    status: 'pending',
    mode: 'ask',
    pathFields: { file_path: '/proj/x.ts' },
    timestamp: '2026-06-18T00:00:00.000Z',
    ...overrides
  };
}

describe('PermissionDecisionCards rendering', () => {
  it('renders nothing when there are no pending requests', () => {
    const html = renderToStaticMarkup(
      createElement(PermissionDecisionCards, { sessionId: 's1', requests: [] })
    );
    expect(html).toBe('');
  });

  it('renders an approval card with grouped a11y semantics, tool, reason, and actions', () => {
    const html = renderToStaticMarkup(
      createElement(PermissionDecisionCards, { sessionId: 's1', requests: [row()] })
    );

    // a11y: a labelled region of grouped cards (not multiple alertdialogs).
    expect(html).toContain('role="region"');
    expect(html).toContain('role="group"');
    expect(html).not.toContain('role="alertdialog"');
    expect(html).toContain('Write');
    expect(html).toContain('/proj/x.ts');
    expect(html).toContain('Approve');
    expect(html).toContain('Deny');
  });
});
