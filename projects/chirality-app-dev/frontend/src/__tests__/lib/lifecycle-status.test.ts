import { mkdir, mkdtemp, readFile, rm, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';
import type { AmendmentReopenDecision } from '../../lib/lifecycle/amendment-reopen';
import {
  StatusParseError,
  parseStatusDocument
} from '../../lib/lifecycle/status-parser';
import {
  StatusWriteError,
  updateStatusDocument,
  writeStatusDocument
} from '../../lib/lifecycle/status-writer';
import {
  LifecycleTransitionError,
  applyLifecycleTransition,
  transitionStatusFile
} from '../../lib/lifecycle/transition';
import { writeAmendmentRecords } from './amendment-records-fixture';

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
    ['HUMAN with neither SHA nor ruling (missing SHA reported first)', {}, 'APPROVAL_SHA_REQUIRED'],
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
      'a ruling that would split the history note',
      { approvalSha: 'abc1234', ruling: 'D-001.md; approval SHA: fff0000' },
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

  it('denies a ruling reference on a transition that is not a human gate', () => {
    expect(() =>
      applyLifecycleTransition(statusAt('INITIALIZED'), 'IN_PROGRESS', 'WORKING_ITEMS', {
        date: '2026-02-26',
        ruling: RULING
      })
    ).toThrowError(
      expect.objectContaining({ code: 'RULING_NOT_APPLICABLE' }) satisfies Partial<LifecycleTransitionError>
    );
  });

  it.each([
    ['IN_PROGRESS', 'CHECKING', 'Checking Approval SHA'],
    ['CHECKING', 'ISSUED', 'Approval SHA']
  ] as const)('accepts an optional ruling on %s -> %s and records it in history', (from, to, field) => {
    const result = applyLifecycleTransition(statusAt(from), to, 'HUMAN', {
      date: '2026-02-26',
      approvalSha: 'abc1234',
      ruling: RULING
    });

    const note = `ruling: ${RULING}; approval SHA: abc1234`;
    expect(result.content).toContain(`- 2026-02-26 - State set to ${to} (HUMAN) [${note}]`);
    expect(result.content).toContain(`**${field}:** abc1234`);
    expect(parseStatusDocument(result.content).history.at(-1)).toMatchObject({ state: to, notes: note });
  });

  it('keeps the forward gates without a history note when no ruling is supplied', () => {
    const result = applyLifecycleTransition(statusAt('IN_PROGRESS'), 'CHECKING', 'HUMAN', {
      date: '2026-02-26',
      approvalSha: 'abc1234'
    });
    expect(result.content).toContain('- 2026-02-26 - State set to CHECKING (HUMAN)\n');
  });

  it('denies a malformed ruling on a forward gate', () => {
    expect(() =>
      applyLifecycleTransition(statusAt('CHECKING'), 'ISSUED', 'HUMAN', {
        date: '2026-02-26',
        approvalSha: 'abc1234',
        ruling: 'D-001.md] [forged'
      })
    ).toThrowError(
      expect.objectContaining({ code: 'INVALID_RULING_REFERENCE' }) satisfies Partial<LifecycleTransitionError>
    );
  });

  it('removes the Checking Approval SHA field on the reversal and keeps it in history', () => {
    const checking = applyLifecycleTransition(statusAt('IN_PROGRESS'), 'CHECKING', 'HUMAN', {
      date: '2026-02-26',
      approvalSha: 'abc1234'
    });
    expect(checking.content).toContain('**Checking Approval SHA:** abc1234');

    const reversed = applyLifecycleTransition(checking.content, 'IN_PROGRESS', 'HUMAN', {
      date: '2026-02-27',
      approvalSha: 'def5678',
      ruling: RULING
    });

    expect(reversed.content).not.toContain('Checking Approval SHA');
    expect(parseStatusDocument(reversed.content).extraFields).toEqual([]);
    expect(reversed.content).toContain(
      `[reversal from CHECKING; ruling: ${RULING}; approval SHA: def5678]`
    );

    const reentered = applyLifecycleTransition(reversed.content, 'CHECKING', 'HUMAN', {
      date: '2026-02-28',
      approvalSha: 'fedcba9'
    });
    expect(reentered.content).toContain('**Checking Approval SHA:** fedcba9');
  });
});

describe('status field writes', () => {
  it('rejects metadata that would forge history through a newline in a value', () => {
    const before = statusAt('IN_PROGRESS');
    let caught: unknown;
    try {
      applyLifecycleTransition(before, 'CHECKING', 'HUMAN', {
        date: '2026-02-26',
        approvalSha: 'abc1234',
        metadata: {
          currentState: 'ISSUED',
          note: 'x\n\n## History\n- 2026-02-26 - State set to ISSUED (HUMAN)'
        }
      });
    } catch (error) {
      caught = error;
    }
    expect(caught).toBeInstanceOf(LifecycleTransitionError);
    expect(caught).toMatchObject({ code: 'INVALID_METADATA' });
  });

  it.each([
    ['a reserved key', { currentState: 'ISSUED' }],
    ['a reserved key in another form', { 'last-updated': '2026-02-26' }],
    ['a History key', { history: 'x' }],
    ['a newline in a value', { note: 'x\n## History' }],
    ['a carriage return in a value', { note: 'x\r- forged' }],
    ['a control character in a value', { note: 'x\u0007' }],
    ['an asterisk in a key', { 'note**': 'x' }],
    ['a heading mark in a key', { '# note': 'x' }],
    ['a colon in a key', { 'Note:': 'x' }],
    ['a newline in a key', { 'note\n## History': 'x' }]
  ])('updateStatusDocument rejects %s', (_label, metadata) => {
    expect(() =>
      updateStatusDocument(LIST_FORMAT_STATUS, {
        targetState: 'IN_PROGRESS',
        actor: 'WORKING_ITEMS',
        date: '2026-02-24',
        metadata
      })
    ).toThrowError(StatusWriteError);
  });

  it('writeStatusDocument rejects a reserved or multi-line extra field', () => {
    const base = {
      title: 'Status: DEL-05-03',
      currentState: 'IN_PROGRESS' as const,
      lastUpdated: '2026-02-24',
      history: []
    };
    expect(() =>
      writeStatusDocument({ ...base, extraFields: [{ key: 'Current State', value: 'ISSUED' }] })
    ).toThrowError(StatusWriteError);
    expect(() =>
      writeStatusDocument({ ...base, extraFields: [{ key: 'Note', value: 'a\n## History' }] })
    ).toThrowError(StatusWriteError);
  });

  it('keeps ordinary metadata keys working', () => {
    const updated = updateStatusDocument(LIST_FORMAT_STATUS, {
      targetState: 'IN_PROGRESS',
      actor: 'WORKING_ITEMS',
      date: '2026-02-24',
      metadata: {
        acceptedBasisSha: 'abc1234',
        'Authorization Basis': 'ruling: execution/_Coordination/_DECISIONS/D-001.md',
        current_state_basis: 'owner ruling'
      }
    });
    expect(updated.content).toContain('**Accepted Basis SHA:** abc1234');
    expect(updated.content).toContain(
      '**Authorization Basis:** ruling: execution/_Coordination/_DECISIONS/D-001.md'
    );
    expect(updated.content).toContain('**Current State Basis:** owner ruling');
  });
});

describe('gate evidence and line-break hardening', () => {
  it.each([
    ['checkingApprovalSha', 'IN_PROGRESS'],
    ['approvalSha', 'IN_PROGRESS'],
    ['Checking Approval SHA', 'IN_PROGRESS'],
    ['approval_sha', 'IN_PROGRESS']
  ])('rejects caller metadata %s, which only the transition sets', (key, to) => {
    const before = statusAt('INITIALIZED');
    expect(() =>
      applyLifecycleTransition(before, to, 'WORKING_ITEMS', {
        date: '2026-02-26',
        metadata: { [key]: 'abc1234' }
      })
    ).toThrowError(
      expect.objectContaining({ code: 'INVALID_METADATA' }) satisfies Partial<LifecycleTransitionError>
    );
  });

  it('rejects approval SHA metadata on the reversal too', () => {
    const checking = applyLifecycleTransition(statusAt('IN_PROGRESS'), 'CHECKING', 'HUMAN', {
      date: '2026-02-26',
      approvalSha: 'abc1234'
    });
    expect(() =>
      applyLifecycleTransition(checking.content, 'IN_PROGRESS', 'HUMAN', {
        date: '2026-02-27',
        approvalSha: 'def5678',
        ruling: 'execution/_Coordination/_DECISIONS/D-001_check_withdrawn.md',
        metadata: { checkingApprovalSha: 'abc1234' }
      })
    ).toThrowError(
      expect.objectContaining({ code: 'INVALID_METADATA' }) satisfies Partial<LifecycleTransitionError>
    );
  });

  it('records a multi-line actor on one parseable history line', () => {
    const result = applyLifecycleTransition(
      statusAt('INITIALIZED'),
      'IN_PROGRESS',
      'WORKING\n\n  ITEMS',
      { date: '2026-02-26' }
    );
    expect(result.content).toContain('- 2026-02-26 - State set to IN_PROGRESS (WORKING ITEMS)');
    expect(parseStatusDocument(result.content).history.map((entry) => entry.state)).toEqual([
      'OPEN',
      'INITIALIZED',
      'IN_PROGRESS'
    ]);
  });

  it.each([' ', ' ', '\u0085'])(
    'rejects a Unicode line break (%j) in a metadata value',
    (separator) => {
      expect(() =>
        applyLifecycleTransition(statusAt('INITIALIZED'), 'IN_PROGRESS', 'WORKING_ITEMS', {
          date: '2026-02-26',
          metadata: { note: `x${separator}## History` }
        })
      ).toThrowError(
        expect.objectContaining({ code: 'INVALID_METADATA' }) satisfies Partial<LifecycleTransitionError>
      );
    }
  );

  it('rejects a non-ASCII look-alike metadata key', () => {
    expect(() =>
      applyLifecycleTransition(statusAt('INITIALIZED'), 'IN_PROGRESS', 'WORKING_ITEMS', {
        date: '2026-02-26',
        metadata: { 'Сurrent State': 'ISSUED' }
      })
    ).toThrowError(
      expect.objectContaining({ code: 'INVALID_METADATA' }) satisfies Partial<LifecycleTransitionError>
    );
  });
});

describe('reopening ISSUED -> IN_PROGRESS under an accepted amendment (SPEC §4.3; D-GOV-50)', () => {
  const ADMITTED_DECISION: AmendmentReopenDecision = {
    admitted: true,
    code: 'ADMITTED',
    reason: 'SCA-001 accepted at group 3',
    deliverableId: 'DEL-05-03',
    amendmentId: 'SCA-001',
    scopeChangeRoot: 'execution/_ScopeChange',
    group3Snapshot: 'execution/_ScopeChange/checkpoint_snapshots/SCA-001_GROUP-3_2026-09-26',
    group3Decision: 'execution/_ScopeChange/checkpoint_snapshots/SCA-001_GROUP-3_2026-09-26/DECISION.md',
    group2Manifest:
      'execution/_ScopeChange/checkpoint_snapshots/SCA-001_GROUP-2_2026-09-26/ACCEPTED_MANIFEST.csv',
    registerPath: 'execution/_ScopeChange/SCA-001_2026-09-26_1200/Amendment_Actions.csv',
    registerSha256: 'a'.repeat(64),
    actionSeq: '2',
    actionType: 'MODIFY',
    scopeChanging: 'NO',
    notes: []
  };
  const REOPEN = { date: '2026-02-27', approvalSha: 'def5678', amendment: 'SCA-001' };
  const NOTE =
    'reopened from ISSUED; amendment: SCA-001 (execution/_ScopeChange/checkpoint_snapshots/SCA-001_GROUP-3_2026-09-26); ' +
    'action: execution/_ScopeChange/SCA-001_2026-09-26_1200/Amendment_Actions.csv ActionSeq 2 MODIFY; ' +
    `register SHA-256: ${'a'.repeat(64)}; approval SHA: def5678`;
  const MODIFY_ROW = {
    AmendmentID: 'SCA-001',
    ActionSeq: '4',
    ActionType: 'MODIFY',
    EntityType: 'DELIVERABLE',
    EntityID: 'DEL-05-03',
    ScopeChanging: 'NO'
  };

  function expectCode(run: () => unknown, code: string): void {
    expect(run).toThrowError(
      expect.objectContaining({ code }) satisfies Partial<LifecycleTransitionError>
    );
  }

  it('admits a HUMAN reopening with an approval SHA and an admitted amendment, and records it', () => {
    const result = applyLifecycleTransition(statusAt('ISSUED'), 'IN_PROGRESS', 'HUMAN', REOPEN, {
      amendmentDecision: ADMITTED_DECISION
    });
    expect(result).toMatchObject({ from: 'ISSUED', to: 'IN_PROGRESS', actor: 'HUMAN' });
    expect(result.content).toContain('**Current State:** IN_PROGRESS');
    expect(result.content).toContain(`- 2026-02-27 - State set to IN_PROGRESS (HUMAN) [${NOTE}]`);
    expect(parseStatusDocument(result.content).history.at(-1)).toMatchObject({
      state: 'IN_PROGRESS',
      notes: NOTE
    });
  });

  it('keeps the ISSUED approval field as history, as write_status.sh does', () => {
    const issued = statusAt('ISSUED').replace(
      '**Last Updated:** 2026-02-25',
      '**Last Updated:** 2026-02-25\n**Approval SHA:** abc1234'
    );
    const result = applyLifecycleTransition(issued, 'IN_PROGRESS', 'USER', REOPEN, {
      amendmentDecision: ADMITTED_DECISION
    });
    expect(result.content).toContain('**Approval SHA:** abc1234');
  });

  it('refuses the reopening without an amendment as a backward transition', () => {
    expectCode(
      () =>
        applyLifecycleTransition(
          statusAt('ISSUED'),
          'IN_PROGRESS',
          'HUMAN',
          { ...REOPEN, amendment: '  ' },
          { amendmentDecision: ADMITTED_DECISION }
        ),
      'BACKWARD_TRANSITION'
    );
  });

  it('refuses the reopening when the amendment check did not run', () => {
    expectCode(
      () => applyLifecycleTransition(statusAt('ISSUED'), 'IN_PROGRESS', 'HUMAN', REOPEN),
      'AMENDMENT_NOT_ADMITTED'
    );
  });

  it('refuses the reopening with the checker refusal code and reason', () => {
    let caught: unknown;
    try {
      applyLifecycleTransition(statusAt('ISSUED'), 'IN_PROGRESS', 'HUMAN', REOPEN, {
        amendmentDecision: {
          ...ADMITTED_DECISION,
          admitted: false,
          code: 'RECLASSIFY_LEGACY_REGISTER',
          reason: 'DEL-05-03 is named only by RECLASSIFY'
        }
      });
    } catch (error) {
      caught = error;
    }
    expect(caught).toMatchObject({
      code: 'AMENDMENT_NOT_ADMITTED',
      message: 'RECLASSIFY_LEGACY_REGISTER: DEL-05-03 is named only by RECLASSIFY',
      details: expect.objectContaining({ refusalCode: 'RECLASSIFY_LEGACY_REGISTER' })
    });
  });

  it.each([
    ['an agent actor', 'WORKING_ITEMS', REOPEN, 'UNAUTHORIZED_ACTOR'],
    ['a HUMAN look-alike', 'HUMAN AGENT', REOPEN, 'UNAUTHORIZED_ACTOR'],
    ['no approval SHA', 'HUMAN', { ...REOPEN, approvalSha: undefined }, 'APPROVAL_SHA_REQUIRED'],
    ['a malformed approval SHA', 'HUMAN', { ...REOPEN, approvalSha: 'not-a-sha' }, 'INVALID_APPROVAL_SHA'],
    ['a ruling instead of the amendment', 'HUMAN', { ...REOPEN, ruling: 'D-001.md' }, 'RULING_NOT_APPLICABLE'],
    ['an amendment with a semicolon', 'HUMAN', { ...REOPEN, amendment: 'SCA-001; x' }, 'INVALID_AMENDMENT_REFERENCE'],
    ['an amendment with a bracket', 'HUMAN', { ...REOPEN, amendment: 'SCA-001]' }, 'INVALID_AMENDMENT_REFERENCE'],
    ['approval SHA metadata', 'HUMAN', { ...REOPEN, metadata: { approvalSha: 'abc1234' } }, 'INVALID_METADATA']
  ] as const)('refuses a reopening with %s even when the amendment was admitted', (_label, actor, options, code) => {
    expectCode(
      () =>
        applyLifecycleTransition(statusAt('ISSUED'), 'IN_PROGRESS', actor, options, {
          amendmentDecision: ADMITTED_DECISION
        }),
      code
    );
  });

  it.each([
    ['INITIALIZED', 'IN_PROGRESS', 'WORKING_ITEMS', {}, 'AMENDMENT_NOT_APPLICABLE'],
    ['IN_PROGRESS', 'CHECKING', 'HUMAN', { approvalSha: 'abc1234' }, 'AMENDMENT_NOT_APPLICABLE'],
    ['CHECKING', 'IN_PROGRESS', 'HUMAN', { approvalSha: 'abc1234', ruling: 'D-001.md' }, 'AMENDMENT_NOT_APPLICABLE'],
    ['ISSUED', 'CHECKING', 'HUMAN', { approvalSha: 'abc1234' }, 'BACKWARD_TRANSITION']
  ] as const)('denies an amendment on %s -> %s', (from, to, actor, options, code) => {
    expectCode(
      () =>
        applyLifecycleTransition(
          statusAt(from),
          to,
          actor,
          { ...options, amendment: 'SCA-001' },
          { amendmentDecision: ADMITTED_DECISION }
        ),
      code
    );
  });

  describe('through transitionStatusFile', () => {
    async function writeFixture(rows: (typeof MODIFY_ROW)[]) {
      tmpDir = await mkdtemp(path.join(os.tmpdir(), 'chirality-reopen-'));
      const deliverable = path.join(tmpDir, 'execution', 'PKG-05_Lifecycle', '1_Working', 'DEL-05-03_Lifecycle');
      await mkdir(deliverable, { recursive: true });
      const statusPath = path.join(deliverable, '_STATUS.md');
      await writeFile(statusPath, statusAt('ISSUED'), 'utf8');
      const records = await writeAmendmentRecords({
        scopeChangeRoot: path.join(tmpDir, 'execution', '_ScopeChange'),
        manifestBase: tmpDir,
        rows
      });
      return { statusPath, records };
    }

    it('runs the amendment check and writes the reopening', async () => {
      const { statusPath, records } = await writeFixture([MODIFY_ROW]);
      const result = await transitionStatusFile(statusPath, 'IN_PROGRESS', 'HUMAN', REOPEN, {
        projectRoot: tmpDir
      });
      expect(result.to).toBe('IN_PROGRESS');
      await expect(readFile(statusPath, 'utf8')).resolves.toContain(
        '[reopened from ISSUED; amendment: SCA-001 (execution/_ScopeChange/checkpoint_snapshots/SCA-001_GROUP-3_2026-09-26); ' +
          'action: execution/_ScopeChange/SCA-001_2026-09-26_1200/Amendment_Actions.csv ActionSeq 4 MODIFY; ' +
          `register SHA-256: ${records.registerSha256}; approval SHA: def5678]`
      );
    });

    it('refuses without writing when the register changed after acceptance', async () => {
      const { statusPath, records } = await writeFixture([MODIFY_ROW]);
      const register = await readFile(records.registerPath, 'utf8');
      await writeFile(records.registerPath, `${register}SCA-001,5,MODIFY,DELIVERABLE,DEL-09-09,NO\n`);
      await expect(
        transitionStatusFile(statusPath, 'IN_PROGRESS', 'HUMAN', REOPEN, { projectRoot: tmpDir })
      ).rejects.toMatchObject({
        code: 'AMENDMENT_NOT_ADMITTED',
        details: expect.objectContaining({ refusalCode: 'REGISTER_HASH_MISMATCH' })
      });
      await expect(readFile(statusPath, 'utf8')).resolves.toBe(statusAt('ISSUED'));
    });

    it('refuses without writing when no project root is supplied for the check', async () => {
      const { statusPath } = await writeFixture([MODIFY_ROW]);
      await expect(transitionStatusFile(statusPath, 'IN_PROGRESS', 'HUMAN', REOPEN)).rejects.toMatchObject({
        code: 'AMENDMENT_CHECK_ERROR'
      });
      await expect(readFile(statusPath, 'utf8')).resolves.toBe(statusAt('ISSUED'));
    });

    it('checks the actor before running the amendment check', async () => {
      const { statusPath } = await writeFixture([]);
      await expect(
        transitionStatusFile(statusPath, 'IN_PROGRESS', 'WORKING_ITEMS', REOPEN, { projectRoot: tmpDir })
      ).rejects.toMatchObject({ code: 'UNAUTHORIZED_ACTOR' });
    });
  });
});

describe('gate-evidence metadata is HUMAN-only (owner decision D2, 2026-09-26)', () => {
  const GATE_KEYS = [
    'Authorization Basis',
    'authorizationBasis',
    'authorization_basis',
    'Accepted Basis SHA',
    'acceptedBasisSha',
    'Accepted ScopeOfWork SHA-256',
    'acceptedScopeOfWorkSha256',
    'accepted-scope-of-work-sha-256'
  ];

  it.each(GATE_KEYS)('refuses %s from an agent actor', (key) => {
    expect(() =>
      applyLifecycleTransition(statusAt('INITIALIZED'), 'IN_PROGRESS', 'WORKING_ITEMS', {
        date: '2026-02-26',
        metadata: { [key]: 'value' }
      })
    ).toThrowError(
      expect.objectContaining({ code: 'INVALID_METADATA' }) satisfies Partial<LifecycleTransitionError>
    );
  });

  it.each(GATE_KEYS)('lets a HUMAN actor record %s', (key) => {
    const result = applyLifecycleTransition(statusAt('IN_PROGRESS'), 'CHECKING', 'HUMAN', {
      date: '2026-02-26',
      approvalSha: 'abc1234',
      metadata: { [key]: 'owner ruling D-001' }
    });
    expect(result.content).toMatch(/\*\*[^*]+:\*\* owner ruling D-001/);
  });

  it('lets a HUMAN alias record gate evidence on an ordinary transition', () => {
    const result = applyLifecycleTransition(statusAt('INITIALIZED'), 'IN_PROGRESS', 'operator', {
      date: '2026-02-26',
      metadata: { authorizationBasis: 'owner ruling D-001', acceptedBasisSha: 'abc1234' }
    });
    expect(result.content).toContain('**Authorization Basis:** owner ruling D-001');
    expect(result.content).toContain('**Accepted Basis SHA:** abc1234');
  });

  it('keeps other metadata keys settable by any authorized actor', () => {
    const result = applyLifecycleTransition(statusAt('INITIALIZED'), 'IN_PROGRESS', 'WORKING_ITEMS', {
      date: '2026-02-26',
      metadata: { directive: 'owner directive 2026-09-26', authorizationNote: 'not gate evidence' }
    });
    expect(result.content).toContain('**Directive:** owner directive 2026-09-26');
    expect(result.content).toContain('**Authorization Note:** not gate evidence');
  });
});
