import React from 'react';
import { renderToStaticMarkup } from 'react-dom/server';
import { expect, it } from 'vitest';
import type { HarnessEvent } from '@chirality/runtime-contracts/event-schema';
import { CoordinationPanel } from '../../components/woven-dialogue/coordination-panel';
it('shows native assignment evidence in Agents without inventing completion from the call', () => {
  const events = [{ schemaVersion: 1, timestamp: '2026-09-12T00:00:00Z', eventId: 'spawn', sessionId: 's', turnId: 'r', type: 'codex.notification', data: { method: 'item/completed', params: { threadId: 'p', turnId: 'n', item: { type: 'collabAgentToolCall', status: 'completed', receiverThreadIds: ['child'], prompt: 'Review the plan', agentsStates: { child: { status: 'running', message: 'Checking the constraints' } } } } } }] as HarnessEvent[];
  const html = renderToStaticMarkup(<CoordinationPanel activeView="agents" nativeEvents={events} hierarchy={{ roots: [], detached: [], childrenByParentSessionId: {}, unresolvedParentSessionIds: [], diagnostics: [] }} sessionsLoading={false} sessionsError={null} selectionDisabled={false} onSelectView={() => {}} onRefreshSessions={() => {}} onSelectSession={() => {}} />);
  expect(html).toContain('Review the plan'); expect(html).toContain('Checking the constraints'); expect(html).toContain('running'); expect(html).not.toContain('completed');
});
