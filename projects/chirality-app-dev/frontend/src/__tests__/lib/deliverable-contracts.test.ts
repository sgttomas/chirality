import { lstat, mkdtemp, mkdir, readFile, rename, rm, symlink, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { afterEach, beforeEach, describe, expect, it } from 'vitest';
import { serializeDependencyRegister } from '../../lib/dependencies/register-writer';
import { DependencyRegisterRow } from '../../lib/dependencies/schema';
import {
  DeliverableStatusTransitionInput,
  readDeliverableDependencies,
  readDeliverableStatus,
  transitionDeliverableStatus,
  writeDeliverableDependencies
} from '../../lib/workspace/deliverable-contracts';
import { WorkspaceOperationError, WorkspaceValidationError } from '../../lib/workspace/filesystem';
import { writeAmendmentRecords } from './amendment-records-fixture';

/*
 * Library-level contract tests for deliverable status reads, lifecycle
 * transitions and dependency-register reads and writes. SCA-APP-011 retired
 * the working-root status, transition and dependency routes; these cases were
 * ported from their route test and call `lib/workspace/deliverable-contracts.ts`
 * directly. Where the route test asserted an HTTP status and error body, the
 * port asserts the thrown workspace error's `code` and `status`, which are the
 * values the route mapped to that status and `error.type`. The two
 * request-body parsing rows (`INVALID_REQUEST` for a non-string `ruling` or
 * `amendment`) retired with the routes: the library types both as strings.
 */

type FixtureContext = {
  tmpRoot: string;
  projectRoot: string;
  deliverablePath: string;
  statusFilePath: string;
  dependenciesFilePath: string;
};

type WorkspaceError = WorkspaceValidationError | WorkspaceOperationError;

const INITIAL_STATUS = `# Status: DEL-05-03 Lifecycle State Handling

**Current State:** INITIALIZED
**Last Updated:** 2026-02-22

## History
- 2026-02-21 - State set to OPEN (PREPARATION)
- 2026-02-22 - State set to INITIALIZED (4_DOCUMENTS)
`;

let fixture: FixtureContext;

function makeDependencyRow(
  overrides: Partial<DependencyRegisterRow> = {}
): DependencyRegisterRow {
  return {
    RegisterSchemaVersion: 'v3.1',
    DependencyID: 'DEP-05-03-001',
    FromPackageID: 'PKG-05',
    FromDeliverableID: 'DEL-05-03',
    FromDeliverableName: 'Lifecycle State Handling',
    DependencyClass: 'EXECUTION',
    AnchorType: 'NOT_APPLICABLE',
    Direction: 'UPSTREAM',
    DependencyType: 'PREREQUISITE',
    TargetType: 'DELIVERABLE',
    TargetPackageID: 'PKG-05',
    TargetDeliverableID: 'DEL-05-02',
    TargetRefID: '',
    TargetName: 'Execution Root Scaffolding',
    TargetLocation: '',
    Statement: 'Requires scaffolding baseline before lifecycle transitions',
    EvidenceFile: 'Specification.md',
    SourceRef:
      'execution/PKG-05_Filesystem_Execution_Model/1_Working/DEL-05-03_Lifecycle_State_Handling/Specification.md#REQ-01',
    EvidenceQuote: 'Ensure lifecycle is represented by _STATUS.md.',
    Explicitness: 'EXPLICIT',
    RequiredMaturity: 'IN_PROGRESS',
    ProposedMaturity: 'IN_PROGRESS',
    SatisfactionStatus: 'PENDING',
    Confidence: 'HIGH',
    Origin: 'EXTRACTED',
    FirstSeen: '2026-02-22',
    LastSeen: '2026-02-22',
    Status: 'ACTIVE',
    Notes: '',
    ...overrides
  };
}

/** The workspace error a library call rejects with; fails if it resolves. */
async function rejection(call: Promise<unknown>): Promise<WorkspaceError> {
  let caught: unknown;
  try {
    await call;
  } catch (error) {
    caught = error;
  }
  expect(caught).toBeDefined();
  expect(
    caught instanceof WorkspaceValidationError || caught instanceof WorkspaceOperationError
  ).toBe(true);
  return caught as WorkspaceError;
}

/** The error's code, message and details, as the retired route serialized them. */
function refusalText(error: WorkspaceError): string {
  return JSON.stringify({
    type: error.code,
    message: error.message,
    details: error instanceof WorkspaceOperationError ? error.details : undefined
  });
}

beforeEach(async () => {
  const tmpRoot = await mkdtemp(path.join(os.tmpdir(), 'chirality-deliverable-contracts-'));
  const projectRoot = path.join(tmpRoot, 'project-root');
  // The recorded-register read resolves the execution root as the outermost execution/ folder.
  const deliverablePath = path.join(
    projectRoot,
    'execution',
    'PKG-05_Filesystem_Execution_Model',
    '1_Working',
    'DEL-05-03_Lifecycle_State_Handling'
  );
  const statusFilePath = path.join(deliverablePath, '_STATUS.md');
  const dependenciesFilePath = path.join(deliverablePath, 'Dependencies.csv');

  await mkdir(deliverablePath, { recursive: true });
  await writeFile(statusFilePath, INITIAL_STATUS, 'utf8');

  const initialRegister = serializeDependencyRegister([makeDependencyRow()], {
    hostDeliverableId: 'DEL-05-03'
  });
  await writeFile(dependenciesFilePath, initialRegister.csv, 'utf8');

  fixture = {
    tmpRoot,
    projectRoot,
    deliverablePath,
    statusFilePath,
    dependenciesFilePath
  };
});

afterEach(async () => {
  await rm(fixture.tmpRoot, { recursive: true, force: true });
});

describe('deliverable contract library (status, transition, dependencies)', () => {
  it('reads parsed lifecycle state from _STATUS.md', async () => {
    const snapshot = await readDeliverableStatus(fixture.projectRoot, fixture.deliverablePath);

    expect(snapshot.status.currentState).toBe('INITIALIZED');
  });

  it('applies authorized lifecycle transitions and persists status changes', async () => {
    const result = await transitionDeliverableStatus({
      projectRoot: fixture.projectRoot,
      deliverablePath: fixture.deliverablePath,
      targetState: 'IN_PROGRESS',
      actor: 'WORKING_ITEMS',
      date: '2026-02-24'
    });

    expect(result.transition.to).toBe('IN_PROGRESS');
    expect(result.status.currentState).toBe('IN_PROGRESS');

    const statusFile = await readFile(fixture.statusFilePath, 'utf8');
    expect(statusFile).toContain('**Current State:** IN_PROGRESS');
    expect(statusFile).toContain('- 2026-02-24 - State set to IN_PROGRESS (WORKING_ITEMS)');
  });

  it('rejects unauthorized actor transitions with explicit error typing', async () => {
    await transitionDeliverableStatus({
      projectRoot: fixture.projectRoot,
      deliverablePath: fixture.deliverablePath,
      targetState: 'IN_PROGRESS',
      actor: 'WORKING_ITEMS',
      date: '2026-02-24'
    });

    const unauthorized = await rejection(
      transitionDeliverableStatus({
        projectRoot: fixture.projectRoot,
        deliverablePath: fixture.deliverablePath,
        targetState: 'CHECKING',
        actor: 'WORKING_ITEMS',
        date: '2026-02-25'
      })
    );

    expect(unauthorized).toMatchObject({ status: 400, code: 'UNAUTHORIZED_ACTOR' });
  });

  it('requires approvalSha evidence for CHECKING and ISSUED transitions', async () => {
    await transitionDeliverableStatus({
      projectRoot: fixture.projectRoot,
      deliverablePath: fixture.deliverablePath,
      targetState: 'IN_PROGRESS',
      actor: 'WORKING_ITEMS',
      date: '2026-02-24'
    });

    const missingForChecking = await rejection(
      transitionDeliverableStatus({
        projectRoot: fixture.projectRoot,
        deliverablePath: fixture.deliverablePath,
        targetState: 'CHECKING',
        actor: 'HUMAN',
        date: '2026-02-25'
      })
    );

    expect(missingForChecking).toMatchObject({ status: 400, code: 'APPROVAL_SHA_REQUIRED' });

    const toChecking = await transitionDeliverableStatus({
      projectRoot: fixture.projectRoot,
      deliverablePath: fixture.deliverablePath,
      targetState: 'CHECKING',
      actor: 'HUMAN',
      date: '2026-02-25',
      approvalSha: 'abc1234'
    });

    expect(toChecking.transition.to).toBe('CHECKING');

    const missingForIssued = await rejection(
      transitionDeliverableStatus({
        projectRoot: fixture.projectRoot,
        deliverablePath: fixture.deliverablePath,
        targetState: 'ISSUED',
        actor: 'HUMAN',
        date: '2026-02-26'
      })
    );

    expect(missingForIssued).toMatchObject({ status: 400, code: 'APPROVAL_SHA_REQUIRED' });
  });

  it('rejects malformed approvalSha values for human-gated transitions', async () => {
    await transitionDeliverableStatus({
      projectRoot: fixture.projectRoot,
      deliverablePath: fixture.deliverablePath,
      targetState: 'IN_PROGRESS',
      actor: 'WORKING_ITEMS',
      date: '2026-02-24'
    });

    const malformed = await rejection(
      transitionDeliverableStatus({
        projectRoot: fixture.projectRoot,
        deliverablePath: fixture.deliverablePath,
        targetState: 'CHECKING',
        actor: 'HUMAN',
        date: '2026-02-25',
        approvalSha: 'not-a-sha'
      })
    );

    expect(malformed).toMatchObject({ status: 400, code: 'INVALID_APPROVAL_SHA' });
  });

  describe('human-ruled CHECKING reversal', () => {
    const RULING_RELATIVE = 'execution/_Coordination/_DECISIONS/D-001_check_withdrawn.md';

    function statusAt(state: 'IN_PROGRESS' | 'CHECKING' | 'ISSUED'): string {
      return `${INITIAL_STATUS.replace('**Current State:** INITIALIZED', `**Current State:** ${state}`)}- 2026-02-25 - State set to ${state} (HUMAN)\n`;
    }

    function transition(overrides: Partial<DeliverableStatusTransitionInput>) {
      return transitionDeliverableStatus({
        projectRoot: fixture.projectRoot,
        deliverablePath: fixture.deliverablePath,
        targetState: 'IN_PROGRESS',
        actor: 'HUMAN',
        date: '2026-02-27',
        approvalSha: 'abc1234',
        ...overrides
      });
    }

    beforeEach(async () => {
      await mkdir(path.join(fixture.projectRoot, path.dirname(RULING_RELATIVE)), { recursive: true });
      await writeFile(path.join(fixture.projectRoot, RULING_RELATIVE), '# Ruling\n', 'utf8');
    });

    it('applies CHECKING -> IN_PROGRESS with a ruling inside projectRoot and records it', async () => {
      await writeFile(fixture.statusFilePath, statusAt('CHECKING'), 'utf8');

      const result = await transition({ ruling: RULING_RELATIVE });

      expect(result).toMatchObject({
        transition: { from: 'CHECKING', to: 'IN_PROGRESS', actor: 'HUMAN' },
        status: { currentState: 'IN_PROGRESS' }
      });
      const statusFile = await readFile(fixture.statusFilePath, 'utf8');
      expect(statusFile).toContain(
        `- 2026-02-27 - State set to IN_PROGRESS (HUMAN) [reversal from CHECKING; ruling: ${RULING_RELATIVE}; approval SHA: abc1234]`
      );
    });

    it('records an absolute ruling path inside projectRoot as project-relative', async () => {
      await writeFile(fixture.statusFilePath, statusAt('CHECKING'), 'utf8');

      await transition({
        ruling: path.join(fixture.projectRoot, RULING_RELATIVE)
      });

      await expect(readFile(fixture.statusFilePath, 'utf8')).resolves.toContain(
        `[reversal from CHECKING; ruling: ${RULING_RELATIVE}; approval SHA: abc1234]`
      );
    });

    // The route-only row "a non-string ruling" ({ ruling: 42 } -> INVALID_REQUEST)
    // retired with the transition route (SCA-APP-011).
    it.each([
      ['CHECKING', 'HUMAN with neither SHA nor ruling', { approvalSha: undefined }, 'APPROVAL_SHA_REQUIRED'],
      ['CHECKING', 'HUMAN with a SHA but no ruling', {}, 'RULING_REQUIRED'],
      ['CHECKING', 'no SHA', { approvalSha: undefined, ruling: RULING_RELATIVE }, 'APPROVAL_SHA_REQUIRED'],
      ['CHECKING', 'an agent actor', { actor: 'WORKING_ITEMS', ruling: RULING_RELATIVE }, 'UNAUTHORIZED_ACTOR'],
      ['CHECKING', 'a missing ruling', { ruling: 'execution/_Coordination/_DECISIONS/D-404.md' }, 'RULING_NOT_FOUND'],
      ['CHECKING', 'a directory ruling', { ruling: 'execution/_Coordination/_DECISIONS' }, 'RULING_NOT_FOUND'],
      ['CHECKING', 'the project root as ruling', { ruling: '.' }, 'RULING_OUTSIDE_PROJECT_ROOT'],
      ['CHECKING', 'a ruling outside projectRoot', { ruling: '../outside-ruling.md' }, 'RULING_OUTSIDE_PROJECT_ROOT'],
      ['ISSUED', 'a ruling on ISSUED -> IN_PROGRESS', { ruling: RULING_RELATIVE }, 'BACKWARD_TRANSITION'],
      ['ISSUED', 'ISSUED -> CHECKING', { targetState: 'CHECKING', ruling: RULING_RELATIVE }, 'BACKWARD_TRANSITION']
    ] as const)('denies %s reversal request with %s as %s without writing', async (state, _label, overrides, code) => {
      await writeFile(path.join(fixture.tmpRoot, 'outside-ruling.md'), '# Outside\n', 'utf8');
      const before = statusAt(state);
      await writeFile(fixture.statusFilePath, before, 'utf8');

      const error = await rejection(transition(overrides));

      expect(error).toMatchObject({ status: 400, code });
      await expect(readFile(fixture.statusFilePath, 'utf8')).resolves.toBe(before);
    });

    async function expectDeniedWithoutWrite(
      overrides: Partial<DeliverableStatusTransitionInput>,
      code: string,
      state: 'IN_PROGRESS' | 'CHECKING' = 'CHECKING'
    ): Promise<void> {
      const before = statusAt(state);
      await writeFile(fixture.statusFilePath, before, 'utf8');

      const error = await rejection(transition(overrides));

      expect(error).toMatchObject({ status: 400, code });
      await expect(readFile(fixture.statusFilePath, 'utf8')).resolves.toBe(before);
    }

    it('denies an absolute ruling path outside projectRoot', async () => {
      const outside = path.join(fixture.tmpRoot, 'outside-ruling.md');
      await writeFile(outside, '# Outside\n', 'utf8');
      await expectDeniedWithoutWrite({ ruling: outside }, 'RULING_OUTSIDE_PROJECT_ROOT');
    });

    it.each([
      ['a zero-byte ruling file', ''],
      ['a whitespace-only ruling file', ' \n\t\r\n  ']
    ])('denies %s', async (_label, content) => {
      const empty = 'execution/_Coordination/_DECISIONS/D-002_empty.md';
      await writeFile(path.join(fixture.projectRoot, empty), content, 'utf8');
      await expectDeniedWithoutWrite({ ruling: empty }, 'RULING_EMPTY');
    });

    it("denies the deliverable's own _STATUS.md as the ruling", async () => {
      await expectDeniedWithoutWrite(
        { ruling: path.relative(fixture.projectRoot, fixture.statusFilePath) },
        'RULING_IS_STATUS_FILE'
      );
    });

    it('denies a ruling path containing a semicolon', async () => {
      const semicolon = 'execution/_Coordination/_DECISIONS/D-003;approval SHA fff0000.md';
      await writeFile(path.join(fixture.projectRoot, semicolon), '# Ruling\n', 'utf8');
      await expectDeniedWithoutWrite({ ruling: semicolon }, 'INVALID_RULING_REFERENCE');
    });

    it('accepts a ruling whose name begins with two dots', async () => {
      await writeFile(fixture.statusFilePath, statusAt('CHECKING'), 'utf8');
      await writeFile(path.join(fixture.projectRoot, '..ruling-notes.md'), '# Ruling\n', 'utf8');

      await transition({ ruling: '..ruling-notes.md' });

      await expect(readFile(fixture.statusFilePath, 'utf8')).resolves.toContain(
        '[reversal from CHECKING; ruling: ..ruling-notes.md; approval SHA: abc1234]'
      );
    });

    it('accepts an optional ruling on IN_PROGRESS -> CHECKING and records it', async () => {
      await writeFile(fixture.statusFilePath, statusAt('IN_PROGRESS'), 'utf8');

      await transition({ targetState: 'CHECKING', ruling: RULING_RELATIVE });

      const statusFile = await readFile(fixture.statusFilePath, 'utf8');
      expect(statusFile).toContain(
        `- 2026-02-27 - State set to CHECKING (HUMAN) [ruling: ${RULING_RELATIVE}; approval SHA: abc1234]`
      );
      expect(statusFile).toContain('**Checking Approval SHA:** abc1234');
    });

    it('applies the same ruling path checks on a forward gate', async () => {
      await expectDeniedWithoutWrite(
        { targetState: 'CHECKING', ruling: '../outside-ruling.md' },
        'RULING_OUTSIDE_PROJECT_ROOT',
        'IN_PROGRESS'
      );
    });

    it('rejects metadata that would forge _STATUS.md history', async () => {
      await expectDeniedWithoutWrite(
        {
          ruling: RULING_RELATIVE,
          metadata: {
            currentState: 'ISSUED',
            note: 'x\n\n## History\n- 2026-02-27 - State set to ISSUED (HUMAN)'
          }
        },
        'INVALID_METADATA'
      );
    });

    it('denies a ruling symlink that resolves outside projectRoot', async () => {
      await writeFile(fixture.statusFilePath, statusAt('CHECKING'), 'utf8');
      const outside = path.join(fixture.tmpRoot, 'outside-ruling.md');
      await writeFile(outside, '# Outside\n', 'utf8');
      const link = path.join(fixture.projectRoot, 'execution/_Coordination/_DECISIONS/D-LINK.md');
      await symlink(outside, link);

      const error = await rejection(
        transition({
          ruling: 'execution/_Coordination/_DECISIONS/D-LINK.md'
        })
      );

      expect(error).toMatchObject({ status: 400, code: 'RULING_OUTSIDE_PROJECT_ROOT' });
    });
  });

  describe('reopening ISSUED -> IN_PROGRESS under an accepted amendment', () => {
    const ISSUED = `${INITIAL_STATUS.replace('**Current State:** INITIALIZED', '**Current State:** ISSUED')}- 2026-02-25 - State set to ISSUED (HUMAN)\n`;
    const MODIFY_ROW = {
      AmendmentID: 'SCA-001',
      ActionSeq: '3',
      ActionType: 'MODIFY',
      EntityType: 'DELIVERABLE',
      EntityID: 'DEL-05-03',
      ScopeChanging: 'NO'
    };

    // The amendment check reads <execution root>/_ScopeChange, so the reopened
    // deliverable lives under an execution/ folder of the working root.
    let reopen: {
      projectRoot: string;
      deliverablePath: string;
      statusFilePath: string;
      scopeChangeRoot: string;
    };

    function transition(
      overrides: Partial<DeliverableStatusTransitionInput>,
      target: { projectRoot: string; deliverablePath: string } = reopen
    ) {
      return transitionDeliverableStatus({
        projectRoot: target.projectRoot,
        deliverablePath: target.deliverablePath,
        targetState: 'IN_PROGRESS',
        actor: 'HUMAN',
        date: '2026-02-27',
        approvalSha: 'abc1234',
        ...overrides
      });
    }

    async function expectDenied(
      overrides: Partial<DeliverableStatusTransitionInput>,
      code: string,
      statusFilePath = reopen.statusFilePath,
      target: { projectRoot: string; deliverablePath: string } = reopen
    ): Promise<WorkspaceError> {
      const before = await readFile(statusFilePath, 'utf8');
      const error = await rejection(transition(overrides, target));
      expect(error).toMatchObject({ status: 400, code });
      await expect(readFile(statusFilePath, 'utf8')).resolves.toBe(before);
      return error;
    }

    beforeEach(async () => {
      const execution = path.join(fixture.projectRoot, 'execution');
      const deliverablePath = path.join(execution, 'PKG-05_Lifecycle', '1_Working', 'DEL-05-03_Lifecycle');
      await mkdir(deliverablePath, { recursive: true });
      const statusFilePath = path.join(deliverablePath, '_STATUS.md');
      await writeFile(statusFilePath, ISSUED, 'utf8');
      reopen = {
        projectRoot: fixture.projectRoot,
        deliverablePath,
        statusFilePath,
        scopeChangeRoot: path.join(execution, '_ScopeChange')
      };
    });

    it('admits a HUMAN reopening by amendment ID and records the amendment, row and SHAs', async () => {
      const records = await writeAmendmentRecords({
        scopeChangeRoot: reopen.scopeChangeRoot,
        manifestBase: fixture.projectRoot,
        rows: [MODIFY_ROW]
      });

      const result = await transition({ amendment: 'SCA-001' });

      expect(result).toMatchObject({
        transition: { from: 'ISSUED', to: 'IN_PROGRESS', actor: 'HUMAN' },
        status: { currentState: 'IN_PROGRESS' }
      });
      await expect(readFile(reopen.statusFilePath, 'utf8')).resolves.toContain(
        '- 2026-02-27 - State set to IN_PROGRESS (HUMAN) [reopened from ISSUED; ' +
          'amendment: SCA-001 (execution/_ScopeChange/checkpoint_snapshots/SCA-001_GROUP-3_2026-09-26); ' +
          'action: execution/_ScopeChange/SCA-001_2026-09-26_1200/Amendment_Actions.csv ActionSeq 3 MODIFY; ' +
          `register SHA-256: ${records.registerSha256}; approval SHA: abc1234]`
      );
    });

    it('admits a reopening named by its group-3 DECISION.md path', async () => {
      const records = await writeAmendmentRecords({
        scopeChangeRoot: reopen.scopeChangeRoot,
        manifestBase: fixture.projectRoot,
        rows: [MODIFY_ROW]
      });

      const result = await transition({
        amendment: path.relative(reopen.projectRoot, path.join(records.group3Dir, 'DECISION.md'))
      });

      expect(result.transition).toMatchObject({ from: 'ISSUED', to: 'IN_PROGRESS' });
    });

    // The route-only row "a non-string amendment" ({ amendment: 7 } -> INVALID_REQUEST)
    // retired with the transition route (SCA-APP-011).
    it.each([
      ['no amendment', {}, 'BACKWARD_TRANSITION'],
      ['an agent actor', { amendment: 'SCA-001', actor: 'WORKING_ITEMS' }, 'UNAUTHORIZED_ACTOR'],
      ['no approval SHA', { amendment: 'SCA-001', approvalSha: undefined }, 'APPROVAL_SHA_REQUIRED'],
      ['an unknown amendment', { amendment: 'SCA-404' }, 'AMENDMENT_NOT_ADMITTED'],
      ['an unresolvable amendment path', { amendment: 'no/such/amendment' }, 'AMENDMENT_NOT_ADMITTED']
    ] as const)('denies a reopening with %s without writing', async (_label, overrides, code) => {
      await writeAmendmentRecords({
        scopeChangeRoot: reopen.scopeChangeRoot,
        manifestBase: fixture.projectRoot,
        rows: [MODIFY_ROW]
      });
      await expectDenied(overrides, code);
    });

    it.each([
      [
        'a legacy register naming the deliverable only by RECLASSIFY',
        { rows: [{ ...MODIFY_ROW, ActionType: 'RECLASSIFY', ScopeChanging: undefined }], scopeColumn: false },
        'RECLASSIFY_LEGACY_REGISTER'
      ],
      [
        'a RECLASSIFY that does not change scope',
        { rows: [{ ...MODIFY_ROW, ActionType: 'RECLASSIFY', ScopeChanging: 'NO' }] },
        'RECLASSIFY_NOT_SCOPE_CHANGING'
      ],
      ['an amendment accepted only at group 2', { rows: [MODIFY_ROW], groups: ['1', '2'] as const }, 'GROUP3_NOT_ACCEPTED'],
      ['an ADD row', { rows: [{ ...MODIFY_ROW, ActionType: 'ADD' }] }, 'ACTION_NOT_AUTHORIZING'],
      [
        'an amendment that also removes the deliverable',
        { rows: [MODIFY_ROW, { ...MODIFY_ROW, ActionSeq: '4', ActionType: 'REMOVE' }] },
        'DELIVERABLE_REMOVED'
      ],
      [
        'a register row with stray whitespace',
        { rows: [{ ...MODIFY_ROW, EntityID: 'DEL-05-03 ' }] },
        'REGISTER_SCHEMA'
      ]
    ] as const)('denies a reopening under %s with the checker code', async (_label, records, refusal) => {
      await writeAmendmentRecords({
        scopeChangeRoot: reopen.scopeChangeRoot,
        manifestBase: fixture.projectRoot,
        ...records
      });
      const error = await expectDenied({ amendment: 'SCA-001' }, 'AMENDMENT_NOT_ADMITTED');
      expect(refusalText(error)).toContain(refusal);
    });

    it('refuses a second reopening under the same amendment', async () => {
      await writeAmendmentRecords({
        scopeChangeRoot: reopen.scopeChangeRoot,
        manifestBase: reopen.projectRoot,
        rows: [MODIFY_ROW]
      });
      expect((await transition({ amendment: 'SCA-001' })).transition.to).toBe('IN_PROGRESS');
      const reopened = await readFile(reopen.statusFilePath, 'utf8');
      await writeFile(
        reopen.statusFilePath,
        `${reopened.replace('**Current State:** IN_PROGRESS', '**Current State:** ISSUED')}- 2026-02-28 - State set to ISSUED (HUMAN)\n`,
        'utf8'
      );

      const error = await expectDenied({ amendment: 'SCA-001' }, 'AMENDMENT_NOT_ADMITTED');
      expect(refusalText(error)).toContain('AMENDMENT_ALREADY_USED');
    });

    it('denies an amendment on the CHECKING reversal', async () => {
      await writeFile(
        reopen.statusFilePath,
        ISSUED.replace('**Current State:** ISSUED', '**Current State:** CHECKING'),
        'utf8'
      );
      await mkdir(path.join(fixture.projectRoot, '_DECISIONS'), { recursive: true });
      await writeFile(path.join(fixture.projectRoot, '_DECISIONS', 'D-001.md'), '# Ruling\n', 'utf8');
      await expectDenied({ amendment: 'SCA-001', ruling: '_DECISIONS/D-001.md' }, 'AMENDMENT_NOT_APPLICABLE');
    });

    describe('inside a Git work tree', () => {
      let repo: string;
      let working: { projectRoot: string; deliverablePath: string; statusFilePath: string };

      beforeEach(async () => {
        repo = path.join(fixture.tmpRoot, 'repo');
        const projectRoot = path.join(repo, 'projects', 'app');
        const deliverablePath = path.join(projectRoot, 'execution', 'PKG-05_Lifecycle', '1_Working', 'DEL-05-03_Lifecycle');
        await mkdir(path.join(repo, '.git'), { recursive: true });
        await mkdir(deliverablePath, { recursive: true });
        const statusFilePath = path.join(deliverablePath, '_STATUS.md');
        await writeFile(statusFilePath, ISSUED, 'utf8');
        working = { projectRoot, deliverablePath, statusFilePath };
      });

      it('resolves repository-relative manifest paths and records repository-relative evidence', async () => {
        await writeAmendmentRecords({
          scopeChangeRoot: path.join(working.projectRoot, 'execution', '_ScopeChange'),
          manifestBase: repo,
          rows: [MODIFY_ROW]
        });

        const result = await transition({ amendment: 'SCA-001' }, working);

        expect(result.transition.to).toBe('IN_PROGRESS');
        await expect(readFile(working.statusFilePath, 'utf8')).resolves.toContain(
          'amendment: SCA-001 (projects/app/execution/_ScopeChange/checkpoint_snapshots/SCA-001_GROUP-3_2026-09-26)'
        );
      });

      it('refuses a scope-change root outside the working root', async () => {
        // The outermost execution/ folder lies above this working root, so the
        // scope-change root the Root rule selects is outside it.
        const projectRoot = path.join(repo, 'execution', 'app');
        const deliverablePath = path.join(projectRoot, 'execution', 'PKG-05_Lifecycle', '1_Working', 'DEL-05-03_Lifecycle');
        await mkdir(deliverablePath, { recursive: true });
        const statusFilePath = path.join(deliverablePath, '_STATUS.md');
        await writeFile(statusFilePath, ISSUED, 'utf8');
        await writeAmendmentRecords({
          scopeChangeRoot: path.join(repo, 'execution', '_ScopeChange'),
          manifestBase: repo,
          rows: [MODIFY_ROW]
        });

        const error = await expectDenied({ amendment: 'SCA-001' }, 'AMENDMENT_NOT_ADMITTED', statusFilePath, {
          projectRoot,
          deliverablePath
        });
        expect(refusalText(error)).toContain('PATH_ESCAPE');
        expect(refusalText(error)).toContain('outside the App working root');
      });
    });
  });

  it('reads dependency register data from Dependencies.csv', async () => {
    const snapshot = await readDeliverableDependencies(fixture.projectRoot, fixture.deliverablePath);

    expect(snapshot.registerPresent).toBe(true);
    expect(snapshot.secondarySummaryPresent).toBe(false);
    expect(snapshot.rows).toHaveLength(1);
    expect(snapshot.rows[0].DependencyID).toBe('DEP-05-03-001');
    expect(snapshot.headers).toContain('RegisterSchemaVersion');
  });

  it('returns explicit dependency-register absence without inferring summary rows', async () => {
    await rm(fixture.dependenciesFilePath, { force: true });
    const summaryPath = path.join(fixture.deliverablePath, '_DEPENDENCIES.md');
    await writeFile(
      summaryPath,
      '# Dependencies\n\nThis prose summary names dependency context but is not a structured register.\n',
      'utf8'
    );

    const snapshot = await readDeliverableDependencies(fixture.projectRoot, fixture.deliverablePath);

    expect(snapshot.registerPresent).toBe(false);
    expect(snapshot.secondarySummaryPresent).toBe(true);
    expect(snapshot.dependenciesSummaryPath).toBe(path.join(snapshot.deliverablePath, '_DEPENDENCIES.md'));
    expect(snapshot.rows).toEqual([]);
    expect(snapshot.headers).toEqual([]);
    expect(snapshot.warnings).toEqual([
      'DEPENDENCY_REGISTER_NOT_FOUND: Dependencies.csv is absent; the recorded register is read from the declared sections of _DEPENDENCIES.md (recordedRegister), and no CSV rows are inferred from it.'
    ]);
  });

  it('computes the supplier-judged verdict from the recorded register alongside the CSV rows', async () => {
    const supplierPath = path.join(
      fixture.projectRoot,
      'execution',
      'PKG-05_Filesystem_Execution_Model',
      '1_Working',
      'DEL-05-02_Execution_Root_Scaffolding'
    );
    await mkdir(supplierPath, { recursive: true });
    await writeFile(
      path.join(supplierPath, '_STATUS.md'),
      '# Status: DEL-05-02\n\n**Current State:** INITIALIZED\n**Last Updated:** 2026-09-26\n\n## History\n',
      'utf8'
    );
    await writeFile(
      path.join(fixture.deliverablePath, '_DEPENDENCIES.md'),
      [
        '# Dependencies: DEL-05-03 Lifecycle State Handling',
        '',
        '## Dependency Tracking Mode',
        '- **Mode:** DECLARED',
        '',
        '## Declared Upstream (I need these before I can proceed)',
        '- DEL-05-02 Execution Root Scaffolding — Reason: scaffolding baseline',
        '  - Required maturity: CHECKING',
        '- DEL-05-01 Folder Model — Reason: declared only in the markdown',
        '  - Required maturity: INITIALIZED',
        '',
        '## Declared Downstream (These need me)',
        '- TBD',
        ''
      ].join('\n'),
      'utf8'
    );

    const snapshot = await readDeliverableDependencies(fixture.projectRoot, fixture.deliverablePath);

    // The CSV rows stay as they are on disk: register evidence.
    expect(snapshot.rows).toHaveLength(1);
    expect(snapshot.rows[0].RequiredMaturity).toBe('IN_PROGRESS');
    const recorded = snapshot.recordedRegister!;
    expect(recorded.trackingMode).toBe('DECLARED');
    expect(recorded.unionRows.map((row) => row.DependencyID)).toEqual([
      'DEP-05-03-001',
      'DECLARED-DEL-05-03-001'
    ]);
    expect(recorded.declaredOnlyRows.map((row) => row.TargetDeliverableID)).toEqual(['DEL-05-01']);
    expect(recorded.disagreements).toEqual([
      expect.objectContaining({ DependencyID: 'DEP-05-03-001', Declared: 'CHECKING', Csv: 'IN_PROGRESS' })
    ]);
    expect(recorded.blockers.blockerState).toBe('BLOCKED');
    expect(recorded.blockers.blockerSource).toBe('RECORDED_REGISTER');
    expect(recorded.blockers.blockingUpstreamCount).toBe(2);
    expect(recorded.blockers.upstreamArcs).toEqual([
      expect.objectContaining({ supplier: 'DEL-05-01', requiredMaturity: 'INITIALIZED', supplierState: 'UNKNOWN' }),
      expect.objectContaining({ supplier: 'DEL-05-02', requiredMaturity: 'CHECKING', supplierState: 'INITIALIZED' })
    ]);
  });

  it('does not read recorded-register evidence through a lifecycle folder linked outside projectRoot', async () => {
    const outsideIssued = path.join(fixture.tmpRoot, 'outside-issued');
    const secretPath = path.join(outsideIssued, 'DEL-05-09_Secret');
    await mkdir(secretPath, { recursive: true });
    await writeFile(
      path.join(secretPath, 'Dependencies.csv'),
      serializeDependencyRegister(
        [
          makeDependencyRow({
            DependencyID: 'DEP-05-09-001',
            FromDeliverableID: 'DEL-05-09',
            Direction: 'DOWNSTREAM',
            TargetDeliverableID: 'DEL-05-03',
            RequiredMaturity: 'ISSUED'
          })
        ],
        { hostDeliverableId: 'DEL-05-09' }
      ).csv,
      'utf8'
    );
    await symlink(
      outsideIssued,
      path.join(fixture.projectRoot, 'execution', 'PKG-05_Filesystem_Execution_Model', '3_Issued'),
      'dir'
    );

    const snapshot = await readDeliverableDependencies(fixture.projectRoot, fixture.deliverablePath);

    expect(snapshot.warnings).toContain(
      'RECORDED_REGISTER_READ_OUTSIDE_ROOT: execution/PKG-05_Filesystem_Execution_Model/3_Issued resolves outside the read root; it was not read.'
    );
    const recorded = snapshot.recordedRegister!;
    expect(recorded.blockers.blockerState).toBe('NOT_ASSESSED');
    expect(recorded.blockers.notAssessedReason).toMatch(/^READ_REFUSED:/);
    expect(JSON.stringify(recorded)).not.toContain('DEL-05-09');
  });

  it('gives no recorded-register verdict for a deliverable reached through a linked package folder', async () => {
    const packageName = 'PKG-05_Filesystem_Execution_Model';
    const execution = path.join(fixture.projectRoot, 'execution');
    await mkdir(path.join(fixture.projectRoot, 'store'));
    await rename(path.join(execution, packageName), path.join(fixture.projectRoot, 'store', packageName));
    await symlink(path.join(fixture.projectRoot, 'store', packageName), path.join(execution, packageName), 'dir');

    const read = async (deliverablePath: string) => {
      const snapshot = await readDeliverableDependencies(fixture.projectRoot, deliverablePath);
      return { warnings: snapshot.warnings, recordedRegister: snapshot.recordedRegister! };
    };

    const body = await read(fixture.deliverablePath);
    expect(body.recordedRegister.executionRoot).toBeNull();
    expect(body.recordedRegister.blockers.blockerState).toBe('NOT_ASSESSED');
    expect(body.recordedRegister.blockers.notAssessedReason).toMatch(/^SYMLINKED_UNIT_PATH: /);
    expect(body.warnings).toContain(`RECORDED_REGISTER_${body.recordedRegister.blockers.notAssessedReason}`);

    // Requested at the link's target, the deliverable is outside every execution/ folder.
    const target = await read(
      path.join(fixture.projectRoot, 'store', packageName, '1_Working', 'DEL-05-03_Lifecycle_State_Handling')
    );
    expect(target.recordedRegister.executionRoot).toBeNull();
    expect(target.recordedRegister.blockers.blockerState).toBe('NOT_ASSESSED');
    expect(target.recordedRegister.blockers.notAssessedReason).toMatch(
      /^EXECUTION_ROOT_NOT_RESOLVED: store\/PKG-05_Filesystem_Execution_Model\/1_Working\/DEL-05-03_Lifecycle_State_Handling is not inside an execution\/ folder/
    );
    expect(target.warnings).toContain(`RECORDED_REGISTER_${target.recordedRegister.blockers.notAssessedReason}`);
  });

  it('rejects symlink deliverable paths that resolve outside projectRoot', async () => {
    const externalDeliverable = path.join(
      fixture.tmpRoot,
      'outside-root',
      'PKG-99_External',
      '1_Working',
      'DEL-99-01_External_Deliverable'
    );
    const symlinkDeliverable = path.join(
      fixture.projectRoot,
      'PKG-09_Symlink_Escape',
      '1_Working',
      'DEL-09-01_Symlink_Escape'
    );

    await mkdir(externalDeliverable, { recursive: true });
    await writeFile(path.join(externalDeliverable, '_STATUS.md'), INITIAL_STATUS, 'utf8');
    await mkdir(path.dirname(symlinkDeliverable), { recursive: true });
    await symlink(externalDeliverable, symlinkDeliverable);

    const error = await rejection(readDeliverableStatus(fixture.projectRoot, symlinkDeliverable));

    expect(error).toMatchObject({ status: 400, code: 'DELIVERABLE_PATH_OUTSIDE_PROJECT_ROOT' });
  });

  it('rejects dependency writes when FromDeliverableID mismatches the host deliverable', async () => {
    const error = await rejection(
      writeDeliverableDependencies({
        projectRoot: fixture.projectRoot,
        deliverablePath: fixture.deliverablePath,
        rows: [makeDependencyRow({ FromDeliverableID: 'DEL-99-99' })]
      })
    );

    expect(error).toMatchObject({ status: 400, code: 'INVALID_IDENTITY' });
  });

  it('rejects invalid SatisfactionStatus jumps against prior register rows', async () => {
    const error = await rejection(
      writeDeliverableDependencies({
        projectRoot: fixture.projectRoot,
        deliverablePath: fixture.deliverablePath,
        rows: [makeDependencyRow({ SatisfactionStatus: 'SATISFIED' })]
      })
    );

    expect(error).toMatchObject({ status: 400, code: 'INVALID_SATISFACTION_TRANSITION' });
  });

  it('writes dependency register rows when transitions are valid', async () => {
    const snapshot = await writeDeliverableDependencies({
      projectRoot: fixture.projectRoot,
      deliverablePath: fixture.deliverablePath,
      rows: [makeDependencyRow({ SatisfactionStatus: 'IN_PROGRESS' })]
    });

    expect(snapshot.rows[0].SatisfactionStatus).toBe('IN_PROGRESS');

    const csv = await readFile(fixture.dependenciesFilePath, 'utf8');
    expect(csv).toContain('IN_PROGRESS');
  });

  it('rejects dependency writes to an external-target leaf symlink without replacing it', async () => {
    const externalDependenciesPath = path.join(fixture.tmpRoot, 'external-dependencies.csv');
    const externalBytes = 'external dependency bytes must remain unchanged\n';
    await writeFile(externalDependenciesPath, externalBytes, 'utf8');
    await rm(fixture.dependenciesFilePath);
    await symlink(externalDependenciesPath, fixture.dependenciesFilePath);

    const error = await rejection(
      writeDeliverableDependencies({
        projectRoot: fixture.projectRoot,
        deliverablePath: fixture.deliverablePath,
        rows: [makeDependencyRow({ SatisfactionStatus: 'IN_PROGRESS' })]
      })
    );

    expect(error).toMatchObject({
      status: 403,
      code: 'SYMLINK_WRITE_DENIED',
      details: { file: 'Dependencies.csv' }
    });
    expect((await lstat(fixture.dependenciesFilePath)).isSymbolicLink()).toBe(true);
    expect(await readFile(externalDependenciesPath, 'utf8')).toBe(externalBytes);
  });

  it('rejects dependency writes to a dangling leaf symlink without replacing it', async () => {
    const externalDirectory = path.join(fixture.tmpRoot, 'external-dangling-target');
    const danglingTargetPath = path.join(externalDirectory, 'missing-dependencies.csv');
    const sentinelPath = path.join(externalDirectory, 'sentinel.txt');
    const externalBytes = 'external sentinel bytes must remain unchanged\n';
    await mkdir(externalDirectory, { recursive: true });
    await writeFile(sentinelPath, externalBytes, 'utf8');
    await rm(fixture.dependenciesFilePath);
    await symlink(danglingTargetPath, fixture.dependenciesFilePath);

    const error = await rejection(
      writeDeliverableDependencies({
        projectRoot: fixture.projectRoot,
        deliverablePath: fixture.deliverablePath,
        rows: [makeDependencyRow({ SatisfactionStatus: 'IN_PROGRESS' })]
      })
    );

    expect(error).toMatchObject({
      status: 403,
      code: 'SYMLINK_WRITE_DENIED',
      details: { file: 'Dependencies.csv' }
    });
    expect((await lstat(fixture.dependenciesFilePath)).isSymbolicLink()).toBe(true);
    await expect(readFile(danglingTargetPath, 'utf8')).rejects.toMatchObject({ code: 'ENOENT' });
    expect(await readFile(sentinelPath, 'utf8')).toBe(externalBytes);
  });
});
