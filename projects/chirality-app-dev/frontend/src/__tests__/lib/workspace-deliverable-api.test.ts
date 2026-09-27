import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import {
  WorkspaceApiClientError,
  fetchDeliverableDependencies,
  fetchDeliverableStatus,
  transitionDeliverableStatus
} from '../../lib/workspace/deliverable-api';
import type { DependencyRegisterRow } from '../../lib/dependencies/schema';

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

describe('deliverable API client', () => {
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
    expect(caught).toBeInstanceOf(WorkspaceApiClientError);
    expect(caught).toMatchObject({
      status: 400,
      code: 'AMENDMENT_NOT_ADMITTED',
      message: 'AMENDMENT_ALREADY_USED: already reopened under SCA-001',
      details: { refusalCode: 'AMENDMENT_ALREADY_USED' }
    });
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
  });
});
