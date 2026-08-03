import { describe, expect, it } from 'vitest';
import type { SessionRecord } from '@chirality/runtime-contracts/types';
import {
  buildOperatorSessionProjection,
  projectOperatorSession
} from '../../lib/woven-dialogue/operator-projection';

function session(
  sessionId: string,
  overrides: Partial<SessionRecord> & Record<string, unknown> = {}
): SessionRecord {
  return {
    sessionId,
    projectRoot: '/repo/project',
    persona: 'WORKING_ITEMS',
    mode: 'governed',
    createdAt: '2026-07-23T00:00:00.000Z',
    updatedAt: '2026-07-23T00:00:00.000Z',
    ...overrides
  };
}

describe('operator session projection', () => {
  it('uses exact recorded parentage and provider-neutral attribution fields', () => {
    const parent = session('parent', {
      role: 'agent1',
      agentType: 1,
      status: 'running',
      engineSelection: {
        adapterId: 'pi',
        providerId: 'omlx',
        model: 'local-model'
      },
      residencyEpoch: 'epoch-7'
    });
    const child = session('child', {
      persona: 'TASK',
      role: 'agent2',
      parentSessionId: 'parent',
      status: 'completed',
      outputArtifact: 'runs/child/RETURN.md',
      approvalRef: 'OWNER-1'
    });

    const result = buildOperatorSessionProjection([parent, child], {
      observedAt: '2026-07-23T01:00:00.000Z',
      currencyBySessionId: { parent: 'CURRENT', child: 'CURRENT' }
    });

    expect(result.sessions[0]).toMatchObject({
      sessionId: 'parent',
      role: 'agent1',
      runtimeStatus: 'running',
      adapterId: 'pi',
      providerId: 'omlx',
      model: 'local-model',
      residencyEpoch: 'epoch-7',
      parentage: { state: 'NOT_RECORDED' }
    });
    expect(result.sessions[1]).toMatchObject({
      sessionId: 'child',
      role: 'agent2',
      runtimeStatus: 'completed',
      parentage: {
        state: 'RECORDED',
        parentSessionId: 'parent',
        parentAvailable: true
      },
      outputArtifactReference: 'runs/child/RETURN.md',
      approvalEvidenceReference: 'OWNER-1'
    });
  });

  it('does not infer role, parentage, status, model, or currency from persona and time', () => {
    const projected = projectOperatorSession(
      session('untyped', {
        persona: 'TASK',
        createdAt: '2020-01-01T00:00:00.000Z',
        model: undefined
      }),
      new Set(['untyped']),
      { observedAt: '2026-07-23T01:00:00.000Z' }
    );

    expect(projected).toMatchObject({
      sessionId: 'untyped',
      persona: 'TASK',
      currency: 'UNKNOWN',
      parentage: { state: 'NOT_RECORDED' }
    });
    expect(projected.role).toBeUndefined();
    expect(projected.runtimeStatus).toBeUndefined();
    expect(projected.model).toBeUndefined();
  });

  it('preserves an unresolved exact parent identifier without inventing an edge target', () => {
    const result = buildOperatorSessionProjection(
      [session('child', { parentSessionId: 'missing-parent' })],
      { observedAt: '2026-07-23T01:00:00.000Z' }
    );

    expect(result.sessions[0].parentage).toEqual({
      state: 'RECORDED',
      parentSessionId: 'missing-parent',
      parentAvailable: false
    });
  });

  it('fails closed on conflicting role fields and duplicate session records', () => {
    const first = session('conflict', {
      role: 'agent1',
      agentType: 2,
      status: 'running'
    });
    const second = session('conflict', {
      role: 'agent1',
      agentType: 1,
      status: 'completed'
    });

    const result = buildOperatorSessionProjection([first, second], {
      observedAt: '2026-07-23T01:00:00.000Z',
      currencyBySessionId: { conflict: 'CURRENT' }
    });

    expect(result.sessions).toHaveLength(1);
    expect(result.sessions[0].currency).toBe('CONFLICTING');
    expect(result.sessions[0].role).toBeUndefined();
    expect(result.sessions[0].diagnostics.map(({ code }) => code)).toEqual(
      expect.arrayContaining([
        'CONFLICTING_SESSION_RECORDS',
        'CONFLICTING_RECORDED_ROLE'
      ])
    );
    expect(result.diagnostics.map(({ code }) => code)).toContain(
      'CONFLICTING_SESSION_RECORDS'
    );
  });
});
