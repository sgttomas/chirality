import React from 'react';
import { renderToStaticMarkup } from 'react-dom/server';
import { describe, expect, it, vi } from 'vitest';
import { AgentsProjection } from '../../components/woven-dialogue/agents-projection';
import { buildRecordedAgentHierarchy } from '../../lib/woven-dialogue/recorded-agent-hierarchy';

describe('Agents projection evidence presentation', () => {
  it('shows currency, provenance, diagnostics, and detached recorded sessions', () => {
    const hierarchy = buildRecordedAgentHierarchy([
      {
        sessionId: 'detached-child',
        parentSessionId: 'missing-parent',
        sourceReference: 'session:detached-child',
        observedAt: '2026-07-23T10:01:00Z',
        currency: 'UNKNOWN',
        engineSelection: {
          adapterId: 'pi',
          providerId: 'omlx',
          model: 'local-model'
        }
      },
      {
        sessionId: 'cycle-first',
        parentSessionId: 'cycle-second',
        sourceReference: 'session:cycle-first',
        observedAt: '2026-07-23T10:02:00Z'
      },
      {
        sessionId: 'cycle-second',
        parentSessionId: 'cycle-first',
        sourceReference: 'session:cycle-second',
        observedAt: '2026-07-23T10:03:00Z'
      }
    ]);

    const html = renderToStaticMarkup(
      <AgentsProjection
        hierarchy={hierarchy}
        loading={false}
        error={null}
        selectionDisabled={false}
        onRefresh={vi.fn()}
        onSelectSession={vi.fn()}
      />
    );

    expect(html).toContain('Relationships unavailable or conflicting');
    expect(html).toContain('detached-child');
    expect(html).toContain('Currency: UNKNOWN');
    expect(html).toContain('session:detached-child');
    expect(html).toContain('PARENT_SESSION_UNAVAILABLE');
    expect(html).toContain('selected model: local-model');
    expect(html).toContain('Recorded parent: <code>missing-parent</code>');
    expect(html).toContain('Recorded parent: <code>cycle-second</code>');
    expect(html).toContain('Recorded parent: <code>cycle-first</code>');
  });
});
