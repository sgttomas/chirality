import { mkdtemp, readFile, rm, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';
import {
  StatusParseError,
  parseStatusDocument
} from '../../lib/lifecycle/status-parser';
import {
  updateStatusDocument
} from '../../lib/lifecycle/status-writer';
import {
  LifecycleTransitionError,
  applyLifecycleTransition,
  transitionStatusFile
} from '../../lib/lifecycle/transition';

const LIST_FORMAT_STATUS = `# Status: DEL-05-03 Lifecycle State Handling

**Current State:** INITIALIZED
**Last Updated:** 2026-02-22

## History
- 2026-02-21 - State set to OPEN (PREPARATION)
- 2026-02-22 - State set to INITIALIZED (4_DOCUMENTS)
`;

const TABLE_FORMAT_STATUS = `# Status: DEL-05-03 Lifecycle State Handling

**Current State:** SEMANTIC_READY
**Last Updated:** 2026-02-23

## History
| Date | From | To | Actor | Notes |
|---|---|---|---|---|
| 2026-02-21 | - | OPEN | PREPARATION | scaffold |
| 2026-02-22 | OPEN | INITIALIZED | 4_DOCUMENTS | docs generated |
| 2026-02-23 | INITIALIZED | SEMANTIC_READY | CHIRALITY_FRAMEWORK | semantic lens |
`;

let tmpDir = '';

afterEach(async () => {
  if (tmpDir) {
    await rm(tmpDir, { recursive: true, force: true });
    tmpDir = '';
  }
});

describe('lifecycle status parser/writer', () => {
  it('parses canonical list-format history entries', () => {
    const parsed = parseStatusDocument(LIST_FORMAT_STATUS);
    expect(parsed.currentState).toBe('INITIALIZED');
    expect(parsed.lastUpdated).toBe('2026-02-22');
    expect(parsed.history).toHaveLength(2);
    expect(parsed.history[1]).toMatchObject({
      date: '2026-02-22',
      state: 'INITIALIZED',
      actor: '4_DOCUMENTS',
      source: 'list'
    });
  });

  it('parses table-format history entries for backward compatibility', () => {
    const parsed = parseStatusDocument(TABLE_FORMAT_STATUS);
    expect(parsed.currentState).toBe('SEMANTIC_READY');
    expect(parsed.history).toHaveLength(3);
    expect(parsed.history[2]).toMatchObject({
      date: '2026-02-23',
      state: 'SEMANTIC_READY',
      actor: 'CHIRALITY_FRAMEWORK',
      source: 'table'
    });
  });

  it('appends new transitions and preserves prior history', () => {
    const updated = updateStatusDocument(LIST_FORMAT_STATUS, {
      targetState: 'IN_PROGRESS',
      actor: 'WORKING_ITEMS',
      date: '2026-02-24',
      metadata: {
        approvalSha: 'abc123'
      }
    });

    expect(updated.parsed.currentState).toBe('IN_PROGRESS');
    expect(updated.parsed.history).toHaveLength(3);
    expect(updated.content).toContain('**Approval SHA:** abc123');
    expect(updated.content).toContain(
      '- 2026-02-24 - State set to IN_PROGRESS (WORKING_ITEMS)'
    );
  });

  it('throws parse errors for invalid state values', () => {
    expect(() =>
      parseStatusDocument(LIST_FORMAT_STATUS.replace('INITIALIZED', 'MAYBE'))
    ).toThrow(StatusParseError);
  });
});

describe('lifecycle transitions', () => {
  it('allows authorized forward transitions', () => {
    const result = applyLifecycleTransition(
      LIST_FORMAT_STATUS,
      'IN_PROGRESS',
      'WORKING_ITEMS',
      { date: '2026-02-24' }
    );

    expect(result.from).toBe('INITIALIZED');
    expect(result.to).toBe('IN_PROGRESS');
    expect(result.content).toContain('**Current State:** IN_PROGRESS');
  });

  it('rejects unauthorized actors with explicit error code', () => {
    expect(() =>
      applyLifecycleTransition(
        `# Status: DEL-05-03 Lifecycle State Handling

**Current State:** IN_PROGRESS
**Last Updated:** 2026-02-24

## History
- 2026-02-21 - State set to OPEN (PREPARATION)
- 2026-02-22 - State set to INITIALIZED (4_DOCUMENTS)
- 2026-02-24 - State set to IN_PROGRESS (WORKING_ITEMS)
`,
        'CHECKING',
        'WORKING_ITEMS',
        { date: '2026-02-25' }
      )
    ).toThrowError(
      expect.objectContaining({
        code: 'UNAUTHORIZED_ACTOR'
      }) satisfies Partial<LifecycleTransitionError>
    );
  });

  it.each(['HUMANOID', 'HUMAN_RESOURCES', 'HUMAN AGENT'])(
    'rejects arbitrary HUMAN-prefixed actor %s at a human gate',
    (actor) => {
      expect(() =>
        applyLifecycleTransition(
          `# Status: DEL-05-03 Lifecycle State Handling\n\n**Current State:** IN_PROGRESS\n**Last Updated:** 2026-02-24\n\n## History\n- 2026-02-24 - State set to IN_PROGRESS (WORKING_ITEMS)\n`,
          'CHECKING',
          actor,
          { date: '2026-02-25', approvalSha: 'abcdef1' }
        )
      ).toThrowError(
        expect.objectContaining({ code: 'UNAUTHORIZED_ACTOR' }) satisfies Partial<LifecycleTransitionError>
      );
    }
  );

  it.each(['HUMAN', 'USER', 'OPERATOR'])(
    'accepts exact human actor alias %s while retaining approval-SHA evidence',
    (actor) => {
      const result = applyLifecycleTransition(
        `# Status: DEL-05-03 Lifecycle State Handling\n\n**Current State:** IN_PROGRESS\n**Last Updated:** 2026-02-24\n\n## History\n- 2026-02-24 - State set to IN_PROGRESS (WORKING_ITEMS)\n`,
        'CHECKING',
        actor,
        { date: '2026-02-25', approvalSha: 'abcdef1' }
      );
      expect(result.actor).toBe(actor);
      expect(result.content).toContain('**Checking Approval SHA:** abcdef1');
    }
  );

  it('rejects backward transitions with explicit error code', () => {
    expect(() =>
      applyLifecycleTransition(
        `# Status: DEL-05-03 Lifecycle State Handling

**Current State:** IN_PROGRESS
**Last Updated:** 2026-02-24

## History
- 2026-02-21 - State set to OPEN (PREPARATION)
- 2026-02-22 - State set to INITIALIZED (4_DOCUMENTS)
- 2026-02-24 - State set to IN_PROGRESS (WORKING_ITEMS)
`,
        'INITIALIZED',
        'HUMAN',
        { date: '2026-02-25' }
      )
    ).toThrowError(
      expect.objectContaining({
        code: 'BACKWARD_TRANSITION'
      }) satisfies Partial<LifecycleTransitionError>
    );
  });

  it('rejects non-existent transitions with explicit error code', () => {
    expect(() =>
      applyLifecycleTransition(LIST_FORMAT_STATUS, 'CHECKING', 'HUMAN', {
        date: '2026-02-24'
      })
    ).toThrowError(
      expect.objectContaining({
        code: 'TRANSITION_NOT_ALLOWED'
      }) satisfies Partial<LifecycleTransitionError>
    );
  });

  it('requires approvalSha for human-gated transitions', () => {
    expect(() =>
      applyLifecycleTransition(
        `# Status: DEL-05-03 Lifecycle State Handling

**Current State:** IN_PROGRESS
**Last Updated:** 2026-02-24

## History
- 2026-02-21 - State set to OPEN (PREPARATION)
- 2026-02-22 - State set to INITIALIZED (4_DOCUMENTS)
- 2026-02-24 - State set to IN_PROGRESS (WORKING_ITEMS)
`,
        'CHECKING',
        'HUMAN',
        { date: '2026-02-25' }
      )
    ).toThrowError(
      expect.objectContaining({
        code: 'APPROVAL_SHA_REQUIRED'
      }) satisfies Partial<LifecycleTransitionError>
    );
  });

  it('rejects invalid approvalSha formats for human-gated transitions', () => {
    expect(() =>
      applyLifecycleTransition(
        `# Status: DEL-05-03 Lifecycle State Handling

**Current State:** CHECKING
**Last Updated:** 2026-02-25

## History
- 2026-02-21 - State set to OPEN (PREPARATION)
- 2026-02-22 - State set to INITIALIZED (4_DOCUMENTS)
- 2026-02-24 - State set to IN_PROGRESS (WORKING_ITEMS)
- 2026-02-25 - State set to CHECKING (HUMAN)
`,
        'ISSUED',
        'HUMAN',
        { date: '2026-02-26', approvalSha: 'not-a-sha' }
      )
    ).toThrowError(
      expect.objectContaining({
        code: 'INVALID_APPROVAL_SHA'
      }) satisfies Partial<LifecycleTransitionError>
    );
  });

  it('records approval evidence metadata for CHECKING and ISSUED transitions', () => {
    const checking = applyLifecycleTransition(
      `# Status: DEL-05-03 Lifecycle State Handling

**Current State:** IN_PROGRESS
**Last Updated:** 2026-02-24

## History
- 2026-02-21 - State set to OPEN (PREPARATION)
- 2026-02-22 - State set to INITIALIZED (4_DOCUMENTS)
- 2026-02-24 - State set to IN_PROGRESS (WORKING_ITEMS)
`,
      'CHECKING',
      'HUMAN',
      { date: '2026-02-25', approvalSha: 'abc1234' }
    );

    expect(checking.content).toContain('**Checking Approval SHA:** abc1234');

    const issued = applyLifecycleTransition(checking.content, 'ISSUED', 'HUMAN', {
      date: '2026-02-26',
      approvalSha: 'def5678'
    });
    expect(issued.content).toContain('**Approval SHA:** def5678');
  });

  it('writes transition output back to disk', async () => {
    tmpDir = await mkdtemp(path.join(os.tmpdir(), 'chirality-lifecycle-test-'));
    const statusPath = path.join(tmpDir, '_STATUS.md');
    await writeFile(statusPath, LIST_FORMAT_STATUS, 'utf8');

    await transitionStatusFile(statusPath, 'IN_PROGRESS', 'WORKING_ITEMS', {
      date: '2026-02-24'
    });

    const nextContent = await readFile(statusPath, 'utf8');
    expect(nextContent).toContain('**Current State:** IN_PROGRESS');
    expect(nextContent).toContain('- 2026-02-24 - State set to IN_PROGRESS (WORKING_ITEMS)');
  });
});

function statusAt(state: string): string {
  return `# Status: DEL-05-03 Lifecycle State Handling

**Current State:** ${state}
**Last Updated:** 2026-02-25

## History
- 2026-02-21 - State set to OPEN (PREPARATION)
- 2026-02-25 - State set to ${state} (HUMAN)
`;
}

describe('lifecycle transition table (SPEC §4.3; DEL-07-04 REQ-004/REQ-005/REQ-006/REQ-017)', () => {
  const STATES = ['OPEN', 'INITIALIZED', 'SEMANTIC_READY', 'IN_PROGRESS', 'CHECKING', 'ISSUED'] as const;
  type Evidence = { actor: string; approvalSha?: string; ruling?: string };
  const RULING = 'execution/_Coordination/_DECISIONS/D-001_check_withdrawn.md';
  const ADMITTED: Record<string, Evidence> = {
    'OPEN>INITIALIZED': { actor: '4_DOCUMENTS' },
    'INITIALIZED>SEMANTIC_READY': { actor: 'CHIRALITY_FRAMEWORK' },
    'INITIALIZED>IN_PROGRESS': { actor: 'WORKING_ITEMS' },
    'SEMANTIC_READY>IN_PROGRESS': { actor: 'WORKING_ITEMS' },
    'IN_PROGRESS>CHECKING': { actor: 'HUMAN', approvalSha: 'abc1234' },
    'CHECKING>ISSUED': { actor: 'HUMAN', approvalSha: 'abc1234' },
    'CHECKING>IN_PROGRESS': { actor: 'HUMAN', approvalSha: 'abc1234', ruling: RULING }
  };
  const pairs = STATES.flatMap((from) =>
    STATES.filter((to) => to !== from).map((to) => [from, to] as const)
  );

  it.each(pairs)('%s -> %s follows the authorized table', (from, to) => {
    const admitted = ADMITTED[`${from}>${to}`];
    if (admitted) {
      const result = applyLifecycleTransition(statusAt(from), to, admitted.actor, {
        date: '2026-02-26',
        approvalSha: admitted.approvalSha,
        ruling: admitted.ruling
      });
      expect(result).toMatchObject({ from, to });
      expect(parseStatusDocument(result.content).currentState).toBe(to);
      return;
    }

    // A pair outside the table stays rejected even when every piece of human
    // evidence is supplied.
    const expectedCode =
      STATES.indexOf(to) < STATES.indexOf(from) ? 'BACKWARD_TRANSITION' : 'TRANSITION_NOT_ALLOWED';
    expect(() =>
      applyLifecycleTransition(statusAt(from), to, 'HUMAN', {
        date: '2026-02-26',
        approvalSha: 'abc1234',
        ruling: RULING
      })
    ).toThrowError(
      expect.objectContaining({ code: expectedCode }) satisfies Partial<LifecycleTransitionError>
    );
  });

  it('records the human-ruled CHECKING -> IN_PROGRESS reversal with its ruling and approval SHA', () => {
    const result = applyLifecycleTransition(statusAt('CHECKING'), 'IN_PROGRESS', 'HUMAN', {
      date: '2026-02-26',
      approvalSha: 'abc1234',
      ruling: RULING
    });

    const note = `reversal from CHECKING; ruling: ${RULING}; approval SHA: abc1234`;
    expect(result.content).toContain('**Current State:** IN_PROGRESS');
    expect(result.content).toContain(`- 2026-02-26 - State set to IN_PROGRESS (HUMAN) [${note}]`);
    const parsed = parseStatusDocument(result.content);
    expect(parsed.history).toHaveLength(3);
    expect(parsed.history[2]).toMatchObject({ state: 'IN_PROGRESS', actor: 'HUMAN', notes: note });
  });

  it.each(['USER', 'OPERATOR'])('admits the CHECKING reversal for human alias %s', (actor) => {
    const result = applyLifecycleTransition(statusAt('CHECKING'), 'IN_PROGRESS', actor, {
      date: '2026-02-26',
      approvalSha: 'abc1234',
      ruling: RULING
    });
    expect(result).toMatchObject({ from: 'CHECKING', to: 'IN_PROGRESS', actor });
  });

  it('keeps ISSUED -> IN_PROGRESS rejected; it belongs to the governed scope-change process', () => {
    let caught: unknown;
    try {
      applyLifecycleTransition(statusAt('ISSUED'), 'IN_PROGRESS', 'HUMAN', {
        date: '2026-02-27',
        approvalSha: 'def5678',
        ruling: RULING
      });
    } catch (error) {
      caught = error;
    }
    expect(caught).toBeInstanceOf(LifecycleTransitionError);
    expect(caught).toMatchObject({ code: 'BACKWARD_TRANSITION' });
    expect((caught as Error).message).toContain('governed scope-change process');
  });

  it.each(['WORKING_ITEMS', 'PREPARATION', 'HUMANOID', 'HUMAN AGENT', 'CHIRALITY_FRAMEWORK', 'agent'])(
    'denies the CHECKING reversal to actor %s even with full evidence',
    (actor) => {
      expect(() =>
        applyLifecycleTransition(statusAt('CHECKING'), 'IN_PROGRESS', actor, {
          date: '2026-02-26',
          approvalSha: 'abc1234',
          ruling: RULING
        })
      ).toThrowError(
        expect.objectContaining({ code: 'UNAUTHORIZED_ACTOR' }) satisfies Partial<LifecycleTransitionError>
      );
    }
  );

  it.each([
    ['a caller-supplied HUMAN string alone', {}, 'APPROVAL_SHA_REQUIRED'],
    ['HUMAN with a ruling but no SHA', { ruling: RULING }, 'APPROVAL_SHA_REQUIRED'],
    ['HUMAN with a SHA but no ruling', { approvalSha: 'abc1234' }, 'RULING_REQUIRED'],
    ['HUMAN with a blank ruling', { approvalSha: 'abc1234', ruling: '   ' }, 'RULING_REQUIRED'],
    ['HUMAN with a malformed SHA', { approvalSha: 'not-a-sha', ruling: RULING }, 'INVALID_APPROVAL_SHA'],
    [
      'a ruling that would forge a history note',
      { approvalSha: 'abc1234', ruling: 'D-001.md] [forged' },
      'INVALID_RULING_REFERENCE'
    ],
    [
      'a multi-line ruling',
      { approvalSha: 'abc1234', ruling: 'D-001.md\n- 2026-02-26 - State set to ISSUED (HUMAN)' },
      'INVALID_RULING_REFERENCE'
    ]
  ] as const)('denies the CHECKING reversal for %s', (_label, evidence, code) => {
    const before = statusAt('CHECKING');
    expect(() =>
      applyLifecycleTransition(before, 'IN_PROGRESS', 'HUMAN', {
        date: '2026-02-26',
        ...evidence
      })
    ).toThrowError(expect.objectContaining({ code }) satisfies Partial<LifecycleTransitionError>);
  });

  it.each([
    ['CHECKING', 'SEMANTIC_READY'],
    ['CHECKING', 'INITIALIZED'],
    ['ISSUED', 'CHECKING'],
    ['ISSUED', 'IN_PROGRESS'],
    ['IN_PROGRESS', 'INITIALIZED']
  ])('keeps %s -> %s rejected even with a ruling', (from, to) => {
    expect(() =>
      applyLifecycleTransition(statusAt(from), to, 'HUMAN', {
        date: '2026-02-26',
        approvalSha: 'abc1234',
        ruling: RULING
      })
    ).toThrowError(
      expect.objectContaining({ code: 'BACKWARD_TRANSITION' }) satisfies Partial<LifecycleTransitionError>
    );
  });

  it('denies a ruling reference on a transition that does not use one', () => {
    expect(() =>
      applyLifecycleTransition(statusAt('IN_PROGRESS'), 'CHECKING', 'HUMAN', {
        date: '2026-02-26',
        approvalSha: 'abc1234',
        ruling: RULING
      })
    ).toThrowError(
      expect.objectContaining({ code: 'RULING_NOT_APPLICABLE' }) satisfies Partial<LifecycleTransitionError>
    );
  });
});
