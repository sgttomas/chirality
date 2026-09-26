import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import {
  WorkspaceApiClientError,
  canAgentTransitionLifecycle,
  currentIsoDate,
  fetchDeliverableDependencies,
  fetchDeliverableStatus,
  DECLARED_READINESS_CAVEAT,
  formatBlockingUpstreamMetric,
  formatBlockingUpstreamNote,
  isExecutionBlockerSubsetRow,
  lifecycleTransitionErrorMessage,
  lifecycleTransitionEvidence,
  lifecycleTransitionTargetLabel,
  lifecycleTransitionTargets,
  nextLifecycleTargets,
  requiresApprovalShaForTarget,
  summarizeDependencyRows,
  transitionDeliverableStatus
} from '../../lib/workspace/deliverable-api';
import type { DependencyRegisterRow } from '../../lib/dependencies/schema';
import type { DeliverableRecordedRegister } from '../../lib/dependencies/recorded-register';

function makeRecordedRegister(
  blockers: Partial<DeliverableRecordedRegister['blockers']> = {}
): DeliverableRecordedRegister {
  return {
    deliverableId: 'DEL-05-04',
    executionRoot: '/repo/execution',
    trackingMode: 'DECLARED',
    csvPresent: true,
    declarationsPresent: true,
    declaredEntries: [],
    unionRows: [],
    declaredOnlyRows: [{ DependencyID: 'DECLARED-DEL-05-04-001' }],
    disagreements: [
      {
        DeliverableID: 'DEL-05-04',
        Direction: 'UPSTREAM',
        TargetDeliverableID: 'DEL-05-02',
        DependencyID: 'DEP-05-04-001',
        Field: 'RequiredMaturity',
        Declared: 'CHECKING',
        Csv: 'IN_PROGRESS'
      }
    ],
    unreadDeclarations: [],
    blockers: {
      blockerState: 'BLOCKED',
      blockerSource: 'RECORDED_REGISTER',
      acceptedDagVersion: null,
      defaultMaturity: { value: 'INITIALIZED', source: 'FALLBACK' },
      activeUpstreamCount: 3,
      satisfiedUpstreamCount: 2,
      blockingUpstreamCount: 1,
      blockingUpstreamDeliverables: ['DEL-05-02'],
      blockingEdgeIds: ['DEP-05-04-001'],
      upstreamArcs: [],
      heldSuppliers: [],
      dagPending: false,
      dagPendingReasons: [],
      ...blockers
    },
    warnings: []
  };
}

function jsonResponse(payload: unknown, status = 200): Response {
  return new Response(JSON.stringify(payload), {
    status,
    headers: {
      'Content-Type': 'application/json'
    }
  });
}

function makeRow(overrides: Partial<DependencyRegisterRow> = {}): DependencyRegisterRow {
  return {
    RegisterSchemaVersion: 'v3.1',
    DependencyID: 'DEP-05-04-001',
    FromPackageID: 'PKG-05',
    FromDeliverableID: 'DEL-05-04',
    FromDeliverableName: 'Dependency Tracking Contract',
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
    Statement: 'Needs execution root scaffolding',
    EvidenceFile: 'Specification.md',
    SourceRef: 'execution/PKG-05/.../Specification.md',
    EvidenceQuote: 'Dependencies must be represented by v3.1 rows.',
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

beforeEach(() => {
  vi.stubGlobal('fetch', vi.fn());
});

afterEach(() => {
  vi.unstubAllGlobals();
  vi.restoreAllMocks();
});

describe('deliverable API helpers', () => {
  it('summarizes blocker-subset rows with coordination filters', () => {
    const rows: DependencyRegisterRow[] = [
      makeRow({ SatisfactionStatus: 'PENDING' }),
      makeRow({
        DependencyID: 'DEP-05-04-002',
        DependencyType: 'INTERFACE',
        SatisfactionStatus: 'PENDING'
      }),
      makeRow({
        DependencyID: 'DEP-05-04-003',
        SatisfactionStatus: 'SATISFIED'
      }),
      makeRow({
        DependencyID: 'DEP-05-04-004',
        Direction: 'DOWNSTREAM',
        SatisfactionStatus: 'PENDING'
      }),
      makeRow({
        DependencyID: 'DEP-05-04-005',
        Status: 'RETIRED',
        SatisfactionStatus: 'PENDING'
      }),
      makeRow({
        DependencyID: 'DEP-05-04-006',
        DependencyClass: 'ANCHOR',
        SatisfactionStatus: 'PENDING'
      }),
      makeRow({
        DependencyID: 'DEP-05-04-007',
        TargetType: 'REQUIREMENT',
        SatisfactionStatus: 'PENDING'
      }),
      makeRow({
        DependencyID: 'DEP-05-04-008',
        Notes: 'ASSUMPTION: pending human ruling',
        SatisfactionStatus: 'PENDING'
      }),
      makeRow({
        DependencyID: 'DEP-05-04-009',
        Notes: 'ASSUMPTION resolved in CT-002',
        SatisfactionStatus: 'PENDING'
      })
    ];

    expect(isExecutionBlockerSubsetRow(rows[0])).toBe(true);
    expect(isExecutionBlockerSubsetRow(rows[5])).toBe(false);
    expect(isExecutionBlockerSubsetRow(rows[6])).toBe(false);
    expect(isExecutionBlockerSubsetRow(rows[7])).toBe(false);
    expect(isExecutionBlockerSubsetRow(rows[8])).toBe(true);

    const summary = summarizeDependencyRows(rows);
    expect(summary.totalRows).toBe(9);
    expect(summary.activeRows).toBe(8);
    expect(summary.activeUpstreamBlockerCandidates).toBe(2);
    expect(summary.bySatisfaction.PENDING).toBe(8);
    expect(summary.bySatisfaction.SATISFIED).toBe(1);
    expect(summary.blockerState).toBe('CSV_EVIDENCE');
    expect(formatBlockingUpstreamMetric(summary)).toBe('2 CSV rows (evidence only)');
    expect(formatBlockingUpstreamNote(summary)).toBeNull();
  });

  it('takes the blocking count from the recorded register verdict when one is read', () => {
    const rows = [makeRow({ SatisfactionStatus: 'PENDING' }), makeRow({ DependencyID: 'DEP-05-04-002' })];

    const blocked = summarizeDependencyRows(rows, makeRecordedRegister());
    expect(blocked.totalRows).toBe(2);
    expect(blocked.csvBlockerSubsetRows).toBe(2);
    expect(blocked.activeUpstreamBlockerCandidates).toBe(1);
    expect(blocked.blockingUpstreamDeliverables).toEqual(['DEL-05-02']);
    expect(blocked.disagreementCount).toBe(1);
    expect(blocked.declaredOnlyRows).toBe(1);
    expect(formatBlockingUpstreamMetric(blocked)).toBe('1 (BLOCKED)');
    expect(blocked.trackingMode).toBe('DECLARED');
    expect(formatBlockingUpstreamNote(blocked)).toBe(DECLARED_READINESS_CAVEAT);

    const pending = summarizeDependencyRows(
      rows,
      makeRecordedRegister({
        blockerState: 'DAG_PENDING',
        blockerSource: 'ACCEPTED_DAG:DAG-002',
        blockingUpstreamCount: null,
        blockingUpstreamDeliverables: [],
        dagPending: true,
        dagPendingReasons: ['arc added: DEL-05-04 -> DEL-05-09']
      })
    );
    expect(pending.activeUpstreamBlockerCandidates).toBe(0);
    expect(pending.dagPending).toBe(true);
    expect(pending.dagPendingReasons).toEqual(['arc added: DEL-05-04 -> DEL-05-09']);
    expect(formatBlockingUpstreamMetric(pending)).toBe('DAG pending (no verdict)');
    expect(formatBlockingUpstreamNote(pending)).toBeNull();

    expect(
      formatBlockingUpstreamMetric(
        summarizeDependencyRows(rows, makeRecordedRegister({ blockerState: 'NOT_TRACKED', blockingUpstreamCount: null }))
      )
    ).toBe('Not tracked (no verdict)');
    expect(formatBlockingUpstreamMetric(null)).toBe('—');
    expect(formatBlockingUpstreamNote(null)).toBeNull();
  });

  it('shows the SPEC §5.3 caveat under DECLARED, including when nothing blocks', () => {
    const unblocked = summarizeDependencyRows(
      [],
      makeRecordedRegister({
        blockerState: 'UNBLOCKED',
        blockingUpstreamCount: 0,
        blockingUpstreamDeliverables: [],
        blockingEdgeIds: []
      })
    );
    expect(formatBlockingUpstreamMetric(unblocked)).toBe('0 (UNBLOCKED)');
    expect(formatBlockingUpstreamNote(unblocked)).toBe(DECLARED_READINESS_CAVEAT);
    expect(DECLARED_READINESS_CAVEAT).toContain('no recorded blocker is not a complete readiness judgment');

    const fullGraph = summarizeDependencyRows([], {
      ...makeRecordedRegister({ blockerState: 'UNBLOCKED', blockingUpstreamCount: 0 }),
      trackingMode: 'FULL_GRAPH'
    });
    expect(formatBlockingUpstreamNote(fullGraph)).toBeNull();
  });

  it('shows why a judgment was not assessed', () => {
    const reason =
      'EXECUTION_ROOT_OUTSIDE_PROJECT_ROOT: the execution root holding this deliverable is outside projectRoot';
    const summary = summarizeDependencyRows(
      [],
      makeRecordedRegister({ blockerState: 'NOT_ASSESSED', notAssessedReason: reason, blockingUpstreamCount: null })
    );
    expect(summary.notAssessedReason).toBe(reason);
    expect(formatBlockingUpstreamMetric(summary)).toBe('Not assessed (EXECUTION_ROOT_OUTSIDE_PROJECT_ROOT)');
    expect(formatBlockingUpstreamNote(summary)).toBe(`Not assessed: ${reason}.`);

    const unexplained = summarizeDependencyRows(
      [],
      makeRecordedRegister({ blockerState: 'NOT_ASSESSED', blockingUpstreamCount: null })
    );
    expect(formatBlockingUpstreamMetric(unexplained)).toBe('Not assessed (no verdict)');
  });

  it('returns allowed forward lifecycle targets per state', () => {
    expect(nextLifecycleTargets('OPEN')).toEqual(['INITIALIZED']);
    expect(nextLifecycleTargets('INITIALIZED')).toEqual(['SEMANTIC_READY', 'IN_PROGRESS']);
    expect(nextLifecycleTargets('ISSUED')).toEqual([]);
  });

  it('flags approvalSha requirements for human-gated targets', () => {
    expect(requiresApprovalShaForTarget('CHECKING')).toBe(true);
    expect(requiresApprovalShaForTarget('issued')).toBe(true);
    expect(requiresApprovalShaForTarget('IN_PROGRESS')).toBe(false);
    expect(requiresApprovalShaForTarget(undefined)).toBe(false);
  });

  it('adds the human-authorized reversal and reopening targets after the forward targets', () => {
    expect(lifecycleTransitionTargets('IN_PROGRESS')).toEqual(['CHECKING']);
    expect(lifecycleTransitionTargets('CHECKING')).toEqual(['ISSUED', 'IN_PROGRESS']);
    expect(lifecycleTransitionTargets('ISSUED')).toEqual(['IN_PROGRESS']);
    expect(lifecycleTransitionTargets('INITIALIZED')).toEqual(['SEMANTIC_READY', 'IN_PROGRESS']);
  });

  it('describes the evidence each transition takes (App SPEC §4.3)', () => {
    expect(lifecycleTransitionEvidence('CHECKING', 'IN_PROGRESS')).toEqual({
      kind: 'ruled-reversal',
      humanGate: true,
      approvalSha: 'required',
      ruling: 'required',
      amendment: 'none'
    });
    expect(lifecycleTransitionEvidence('issued', 'in_progress')).toEqual({
      kind: 'amendment-reopen',
      humanGate: true,
      approvalSha: 'required',
      ruling: 'none',
      amendment: 'required'
    });
    for (const [from, to] of [
      ['IN_PROGRESS', 'CHECKING'],
      ['CHECKING', 'ISSUED']
    ]) {
      expect(lifecycleTransitionEvidence(from, to)).toMatchObject({
        kind: 'forward',
        humanGate: true,
        ruling: 'optional',
        amendment: 'none'
      });
    }
    expect(lifecycleTransitionEvidence('INITIALIZED', 'IN_PROGRESS')).toMatchObject({
      humanGate: false,
      approvalSha: 'optional',
      ruling: 'none',
      amendment: 'none'
    });
    expect(lifecycleTransitionEvidence(undefined, '')).toMatchObject({ humanGate: false });
    expect(lifecycleTransitionTargetLabel('CHECKING', 'IN_PROGRESS')).toBe(
      'IN_PROGRESS (ruled reversal)'
    );
    expect(lifecycleTransitionTargetLabel('ISSUED', 'IN_PROGRESS')).toBe(
      'IN_PROGRESS (amendment reopening)'
    );
    expect(lifecycleTransitionTargetLabel('CHECKING', 'ISSUED')).toBe('ISSUED');
  });

  it('formats transition refusals with the checker code and a hint', () => {
    expect(
      lifecycleTransitionErrorMessage(
        new WorkspaceApiClientError(400, 'AMENDMENT_NOT_ADMITTED', 'DELIVERABLE_REMOVED: REMOVE row', {
          refusalCode: 'DELIVERABLE_REMOVED'
        })
      )
    ).toBe(
      'AMENDMENT_NOT_ADMITTED (checker code DELIVERABLE_REMOVED): REMOVE row. ' +
        'The amendment record check refused the reopening. _STATUS.md was not changed.'
    );
    // A refusal without a checker code (the decision did not match the request).
    expect(
      lifecycleTransitionErrorMessage(
        new WorkspaceApiClientError(400, 'AMENDMENT_NOT_ADMITTED', 'The amendment decision does not match')
      )
    ).toBe(
      'AMENDMENT_NOT_ADMITTED: The amendment decision does not match. ' +
        'The amendment record check refused the reopening. _STATUS.md was not changed.'
    );
    expect(
      lifecycleTransitionErrorMessage(new WorkspaceApiClientError(400, 'RULING_REQUIRED', 'needs a ruling'))
    ).toContain("RULING_REQUIRED: needs a ruling. Name the human ruling record: a non-empty file inside the project");
    expect(
      lifecycleTransitionErrorMessage(new WorkspaceApiClientError(400, 'HISTORY_NOT_PRESERVED', 'would drop'))
    ).toContain('HISTORY_NOT_PRESERVED: would drop. The transition would have dropped a recorded reopening');
    expect(
      lifecycleTransitionErrorMessage(new WorkspaceApiClientError(400, 'INVALID_STATUS_FORMAT', 'would not read'))
    ).toContain('INVALID_STATUS_FORMAT: would not read. _STATUS.md has a line break');
    expect(
      lifecycleTransitionErrorMessage(new WorkspaceApiClientError(404, 'STATUS_FILE_NOT_FOUND', 'missing'))
    ).toBe('STATUS_FILE_NOT_FOUND: missing');
    expect(lifecycleTransitionErrorMessage(new Error('network down'))).toBe('network down');
  });

  it('posts the ruling and amendment and reports the checker code of a refused reopening', async () => {
    const fetchMock = vi.mocked(fetch);
    fetchMock.mockResolvedValueOnce(
      jsonResponse(
        {
          error: {
            type: 'AMENDMENT_NOT_ADMITTED',
            message: 'AMENDMENT_ALREADY_USED: already reopened under SCA-001',
            details: { refusalCode: 'AMENDMENT_ALREADY_USED' }
          }
        },
        400
      )
    );

    let caught: unknown;
    try {
      await transitionDeliverableStatus({
        projectRoot: '/tmp/project',
        deliverablePath: '/tmp/project/DEL-05-03_X',
        targetState: 'IN_PROGRESS',
        actor: 'HUMAN',
        approvalSha: 'abc1234',
        amendment: 'SCA-001'
      });
    } catch (error) {
      caught = error;
    }

    expect(JSON.parse(String(fetchMock.mock.calls[0]?.[1]?.body))).toMatchObject({
      targetState: 'IN_PROGRESS',
      approvalSha: 'abc1234',
      amendment: 'SCA-001'
    });
    expect(lifecycleTransitionErrorMessage(caught)).toContain(
      'AMENDMENT_NOT_ADMITTED (checker code AMENDMENT_ALREADY_USED): already reopened under SCA-001'
    );
  });

  it('limits lifecycle transition controls to approved agents', () => {
    expect(canAgentTransitionLifecycle('CHANGE')).toBe(true);
    expect(canAgentTransitionLifecycle('working_items')).toBe(true);
    expect(canAgentTransitionLifecycle('DEPENDENCIES')).toBe(false);
    expect(canAgentTransitionLifecycle(undefined)).toBe(false);
  });

  it('loads lifecycle status snapshots from working-root contracts route', async () => {
    const fetchMock = vi.mocked(fetch);
    fetchMock.mockResolvedValueOnce(
      jsonResponse({
        projectRoot: '/tmp/project',
        deliverablePath: '/tmp/project/PKG-05/1_Working/DEL-05-03_X',
        statusFilePath: '/tmp/project/PKG-05/1_Working/DEL-05-03_X/_STATUS.md',
        status: {
          title: '# Status',
          currentState: 'IN_PROGRESS',
          lastUpdated: '2026-02-22',
          history: [],
          extraFields: []
        }
      })
    );

    const snapshot = await fetchDeliverableStatus(
      '/tmp/project',
      '/tmp/project/PKG-05/1_Working/DEL-05-03_X'
    );

    expect(fetchMock).toHaveBeenCalledTimes(1);
    expect(fetchMock.mock.calls[0]?.[0]).toBe(
      '/api/working-root/deliverable/status?projectRoot=%2Ftmp%2Fproject&deliverablePath=%2Ftmp%2Fproject%2FPKG-05%2F1_Working%2FDEL-05-03_X'
    );
    expect(snapshot.status.currentState).toBe('IN_PROGRESS');
  });

  it('throws typed client errors for non-2xx API responses', async () => {
    const fetchMock = vi.mocked(fetch);
    fetchMock.mockResolvedValueOnce(
      jsonResponse(
        {
          error: {
            type: 'STATUS_FILE_NOT_FOUND',
            message: '_STATUS.md is not accessible in deliverablePath'
          }
        },
        404
      )
    );

    await expect(
      fetchDeliverableStatus('/tmp/project', '/tmp/project/PKG-05/1_Working/DEL-05-03_X')
    ).rejects.toEqual(
      expect.objectContaining({
        name: 'WorkspaceApiClientError',
        status: 404,
        code: 'STATUS_FILE_NOT_FOUND'
      }) satisfies Partial<WorkspaceApiClientError>
    );
  });

  it('sends transition payloads to status transition route', async () => {
    const fetchMock = vi.mocked(fetch);
    fetchMock.mockResolvedValueOnce(
      jsonResponse({
        projectRoot: '/tmp/project',
        deliverablePath: '/tmp/project/PKG-05/1_Working/DEL-05-03_X',
        statusFilePath: '/tmp/project/PKG-05/1_Working/DEL-05-03_X/_STATUS.md',
        transition: {
          from: 'INITIALIZED',
          to: 'IN_PROGRESS',
          actor: 'WORKING_ITEMS'
        },
        status: {
          title: '# Status',
          currentState: 'IN_PROGRESS',
          lastUpdated: '2026-02-22',
          history: [],
          extraFields: []
        }
      })
    );

    const payload = {
      projectRoot: '/tmp/project',
      deliverablePath: '/tmp/project/PKG-05/1_Working/DEL-05-03_X',
      targetState: 'IN_PROGRESS',
      actor: 'WORKING_ITEMS',
      date: '2026-02-22'
    };

    const result = await transitionDeliverableStatus(payload);
    expect(result.transition.to).toBe('IN_PROGRESS');

    expect(fetchMock).toHaveBeenCalledTimes(1);
    const requestInput = fetchMock.mock.calls[0]?.[0];
    const requestInit = fetchMock.mock.calls[0]?.[1] as RequestInit;

    expect(requestInput).toBe('/api/working-root/deliverable/status/transition');
    expect(requestInit.method).toBe('POST');
    expect(requestInit.headers).toEqual({ 'Content-Type': 'application/json' });
    expect(requestInit.body).toBe(JSON.stringify(payload));
  });

  it('loads dependency register snapshots from dependencies route', async () => {
    const fetchMock = vi.mocked(fetch);
    fetchMock.mockResolvedValueOnce(
      jsonResponse({
        projectRoot: '/tmp/project',
        deliverablePath: '/tmp/project/PKG-05/1_Working/DEL-05-04_X',
        dependenciesFilePath: '/tmp/project/PKG-05/1_Working/DEL-05-04_X/Dependencies.csv',
        registerPresent: true,
        secondarySummaryPresent: false,
        headers: ['RegisterSchemaVersion', 'DependencyID'],
        rows: [makeRow()],
        warnings: []
      })
    );

    const snapshot = await fetchDeliverableDependencies(
      '/tmp/project',
      '/tmp/project/PKG-05/1_Working/DEL-05-04_X'
    );

    expect(snapshot.rows).toHaveLength(1);
    expect(snapshot.registerPresent).toBe(true);
    expect(snapshot.secondarySummaryPresent).toBe(false);
    expect(snapshot.rows[0].DependencyID).toBe('DEP-05-04-001');
    expect(currentIsoDate(new Date('2026-02-22T12:34:56.000Z'))).toBe('2026-02-22');
  });
});
