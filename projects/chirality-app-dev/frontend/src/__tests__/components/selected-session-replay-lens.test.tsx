import React from 'react';
import { renderToStaticMarkup } from 'react-dom/server';
import renderer, { act } from 'react-test-renderer';
import { describe, expect, it, vi } from 'vitest';
import type { HarnessEvent } from '@chirality/harness-contract/event-schema';
import type { SessionRecord } from '@chirality/harness-contract/types';
import { SelectedSessionReplayLens } from '../../components/woven-dialogue/selected-session-replay-lens';
import { buildSelectedSessionReplayProjection } from '../../lib/woven-dialogue/selected-session-replay';

function replayProjection() {
  const session = {
    sessionId: 'recorded-session',
    projectRoot: '/repo/project',
    persona: 'WORKING_ITEMS',
    mode: 'governed',
    createdAt: '2026-07-23T00:00:00.000Z',
    updatedAt: '2026-07-23T00:00:00.000Z',
    engineSelection: {
      adapterId: 'pi',
      providerId: 'omlx',
      model: 'recorded-model'
    },
    status: 'completed'
  } as SessionRecord;
  const events: HarnessEvent[] = [
    {
      schemaVersion: 1,
      eventId: 'event-1',
      sessionId: session.sessionId,
      turnId: 'turn-1',
      timestamp: '2026-07-23T00:00:01.000Z',
      type: 'message.completed',
      data: { role: 'assistant', text: 'Recorded answer' }
    },
    {
      schemaVersion: 1,
      eventId: 'event-2',
      sessionId: session.sessionId,
      turnId: 'turn-1',
      timestamp: '2026-07-23T00:00:02.000Z',
      type: 'turn.completed',
      data: { stopReason: 'end_turn' }
    }
  ];

  return buildSelectedSessionReplayProjection(
    session.sessionId,
    {
      session,
      events,
      malformedLineCount: 0,
      summary: {
        eventCount: events.length,
        malformedLineCount: 0,
        eventTypeCounts: {
          'message.completed': 1,
          'turn.completed': 1
        },
        firstTimestamp: events[0].timestamp,
        lastTimestamp: events[1].timestamp
      }
    },
    {
      observedAt: '2026-07-23T01:00:00.000Z',
      currency: 'CURRENT'
    }
  );
}

describe('SelectedSessionReplayLens', () => {
  it('labels replay as read-only and renders exact provenance and attribution', () => {
    const html = renderToStaticMarkup(
      <SelectedSessionReplayLens
        state={{ status: 'READY', projection: replayProjection() }}
        primarySessionId="primary-live-session"
        onReturnToPrimary={() => {}}
      />
    );

    expect(html).toContain('Replay — read-only');
    expect(html).toContain('recorded-session');
    expect(html).toContain('primary-live-session');
    expect(html).toContain('session:recorded-session/events');
    expect(html).toContain('Recorded answer');
    expect(html).toContain('recorded-model');
    expect(html).toContain('Recorded runtime status');
    expect(html).toContain('Return to primary dialogue');
  });

  it('exposes no historical mutation controls', () => {
    const html = renderToStaticMarkup(
      <SelectedSessionReplayLens
        state={{ status: 'READY', projection: replayProjection() }}
        onReturnToPrimary={() => {}}
      />
    );

    for (const forbidden of [
      'Send',
      'Continue',
      'Interrupt',
      'Allow',
      'Deny',
      'Resume',
      'Boot',
      'Delete'
    ]) {
      expect(html).not.toContain(`>${forbidden}<`);
    }
    expect((html.match(/<button/g) ?? [])).toHaveLength(1);
  });

  it('offers only Return and optional Retry when replay is unavailable', () => {
    const onReturn = vi.fn();
    const onRetry = vi.fn();
    const tree = renderer.create(
      <SelectedSessionReplayLens
        state={{
          status: 'UNAVAILABLE',
          selectedSessionId: 'missing-session',
          message: 'canonical replay unavailable'
        }}
        primarySessionId="primary-live-session"
        onReturnToPrimary={onReturn}
        onRetry={onRetry}
      />
    );
    const buttons = tree.root.findAllByType('button');

    expect(buttons.map((button) => button.children.join(''))).toEqual([
      'Return to primary dialogue',
      'Retry'
    ]);

    act(() => {
      buttons[0].props.onClick();
      buttons[1].props.onClick();
    });
    expect(onReturn).toHaveBeenCalledOnce();
    expect(onRetry).toHaveBeenCalledOnce();
  });

  it('keeps Return available while canonical replay evidence is loading', () => {
    const html = renderToStaticMarkup(
      <SelectedSessionReplayLens
        state={{ status: 'LOADING', selectedSessionId: 'recorded-session' }}
        primarySessionId="primary-live-session"
        onReturnToPrimary={() => {}}
      />
    );

    expect(html).toContain('Loading canonical replay evidence');
    expect(html).toContain('Return to primary dialogue');
    expect((html.match(/<button/g) ?? [])).toHaveLength(1);
  });
});
