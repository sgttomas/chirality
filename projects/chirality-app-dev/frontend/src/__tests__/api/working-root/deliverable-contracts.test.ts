import { lstat, mkdtemp, mkdir, readFile, rm, symlink, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { serializeDependencyRegister } from '../../../lib/dependencies/register-writer';
import { DependencyRegisterRow } from '../../../lib/dependencies/schema';

type RouteModules = {
  statusRoute: typeof import('../../../app/api/working-root/deliverable/status/route');
  transitionRoute: typeof import('../../../app/api/working-root/deliverable/status/transition/route');
  dependenciesRoute: typeof import('../../../app/api/working-root/deliverable/dependencies/route');
  contentRoute: typeof import('../../../app/api/working-root/deliverable/content/route');
};

type FixtureContext = {
  tmpRoot: string;
  projectRoot: string;
  deliverablePath: string;
  statusFilePath: string;
  dependenciesFilePath: string;
};

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

async function importRouteModules(): Promise<RouteModules> {
  vi.resetModules();
  const [statusRoute, transitionRoute, dependenciesRoute, contentRoute] = await Promise.all([
    import('../../../app/api/working-root/deliverable/status/route'),
    import('../../../app/api/working-root/deliverable/status/transition/route'),
    import('../../../app/api/working-root/deliverable/dependencies/route'),
    import('../../../app/api/working-root/deliverable/content/route')
  ]);
  return { statusRoute, transitionRoute, dependenciesRoute, contentRoute };
}

function contentRequest(
  projectRoot: string,
  deliverablePath: string,
  file?: string
): Request {
  const params = new URLSearchParams({ projectRoot, deliverablePath });
  if (file !== undefined) {
    params.set('file', file);
  }
  return new Request(`http://localhost/api/working-root/deliverable/content?${params.toString()}`);
}

beforeEach(async () => {
  const tmpRoot = await mkdtemp(path.join(os.tmpdir(), 'chirality-working-root-contracts-'));
  const projectRoot = path.join(tmpRoot, 'project-root');
  const deliverablePath = path.join(
    projectRoot,
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

describe('working-root deliverable contract routes', () => {
  it('reads parsed lifecycle state from _STATUS.md', async () => {
    const routes = await importRouteModules();
    const response = await routes.statusRoute.GET(
      new Request(
        `http://localhost/api/working-root/deliverable/status?projectRoot=${encodeURIComponent(fixture.projectRoot)}&deliverablePath=${encodeURIComponent(fixture.deliverablePath)}`
      )
    );

    expect(response.status).toBe(200);
    const body = (await response.json()) as {
      status: { currentState: string };
    };

    expect(body.status.currentState).toBe('INITIALIZED');
  });

  it('applies authorized lifecycle transitions and persists status changes', async () => {
    const routes = await importRouteModules();
    const response = await routes.transitionRoute.POST(
      new Request('http://localhost/api/working-root/deliverable/status/transition', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          projectRoot: fixture.projectRoot,
          deliverablePath: fixture.deliverablePath,
          targetState: 'IN_PROGRESS',
          actor: 'WORKING_ITEMS',
          date: '2026-02-24'
        })
      })
    );

    expect(response.status).toBe(200);
    const body = (await response.json()) as {
      transition: { to: string };
      status: { currentState: string };
    };
    expect(body.transition.to).toBe('IN_PROGRESS');
    expect(body.status.currentState).toBe('IN_PROGRESS');

    const statusFile = await readFile(fixture.statusFilePath, 'utf8');
    expect(statusFile).toContain('**Current State:** IN_PROGRESS');
    expect(statusFile).toContain('- 2026-02-24 - State set to IN_PROGRESS (WORKING_ITEMS)');
  });

  it('rejects unauthorized actor transitions with explicit error typing', async () => {
    const routes = await importRouteModules();
    await routes.transitionRoute.POST(
      new Request('http://localhost/api/working-root/deliverable/status/transition', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          projectRoot: fixture.projectRoot,
          deliverablePath: fixture.deliverablePath,
          targetState: 'IN_PROGRESS',
          actor: 'WORKING_ITEMS',
          date: '2026-02-24'
        })
      })
    );

    const unauthorized = await routes.transitionRoute.POST(
      new Request('http://localhost/api/working-root/deliverable/status/transition', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          projectRoot: fixture.projectRoot,
          deliverablePath: fixture.deliverablePath,
          targetState: 'CHECKING',
          actor: 'WORKING_ITEMS',
          date: '2026-02-25'
        })
      })
    );

    expect(unauthorized.status).toBe(400);
    expect(await unauthorized.json()).toMatchObject({
      error: {
        type: 'UNAUTHORIZED_ACTOR'
      }
    });
  });

  it('requires approvalSha evidence for CHECKING and ISSUED transitions', async () => {
    const routes = await importRouteModules();

    await routes.transitionRoute.POST(
      new Request('http://localhost/api/working-root/deliverable/status/transition', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          projectRoot: fixture.projectRoot,
          deliverablePath: fixture.deliverablePath,
          targetState: 'IN_PROGRESS',
          actor: 'WORKING_ITEMS',
          date: '2026-02-24'
        })
      })
    );

    const missingForChecking = await routes.transitionRoute.POST(
      new Request('http://localhost/api/working-root/deliverable/status/transition', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          projectRoot: fixture.projectRoot,
          deliverablePath: fixture.deliverablePath,
          targetState: 'CHECKING',
          actor: 'HUMAN',
          date: '2026-02-25'
        })
      })
    );

    expect(missingForChecking.status).toBe(400);
    expect(await missingForChecking.json()).toMatchObject({
      error: {
        type: 'APPROVAL_SHA_REQUIRED'
      }
    });

    const toChecking = await routes.transitionRoute.POST(
      new Request('http://localhost/api/working-root/deliverable/status/transition', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          projectRoot: fixture.projectRoot,
          deliverablePath: fixture.deliverablePath,
          targetState: 'CHECKING',
          actor: 'HUMAN',
          date: '2026-02-25',
          approvalSha: 'abc1234'
        })
      })
    );

    expect(toChecking.status).toBe(200);

    const missingForIssued = await routes.transitionRoute.POST(
      new Request('http://localhost/api/working-root/deliverable/status/transition', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          projectRoot: fixture.projectRoot,
          deliverablePath: fixture.deliverablePath,
          targetState: 'ISSUED',
          actor: 'HUMAN',
          date: '2026-02-26'
        })
      })
    );

    expect(missingForIssued.status).toBe(400);
    expect(await missingForIssued.json()).toMatchObject({
      error: {
        type: 'APPROVAL_SHA_REQUIRED'
      }
    });
  });

  it('rejects malformed approvalSha values for human-gated transitions', async () => {
    const routes = await importRouteModules();

    await routes.transitionRoute.POST(
      new Request('http://localhost/api/working-root/deliverable/status/transition', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          projectRoot: fixture.projectRoot,
          deliverablePath: fixture.deliverablePath,
          targetState: 'IN_PROGRESS',
          actor: 'WORKING_ITEMS',
          date: '2026-02-24'
        })
      })
    );

    const malformed = await routes.transitionRoute.POST(
      new Request('http://localhost/api/working-root/deliverable/status/transition', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          projectRoot: fixture.projectRoot,
          deliverablePath: fixture.deliverablePath,
          targetState: 'CHECKING',
          actor: 'HUMAN',
          date: '2026-02-25',
          approvalSha: 'not-a-sha'
        })
      })
    );

    expect(malformed.status).toBe(400);
    expect(await malformed.json()).toMatchObject({
      error: {
        type: 'INVALID_APPROVAL_SHA'
      }
    });
  });

  describe('human-ruled CHECKING reversal', () => {
    const RULING_RELATIVE = 'execution/_Coordination/_DECISIONS/D-001_check_withdrawn.md';

    function statusAt(state: 'IN_PROGRESS' | 'CHECKING' | 'ISSUED'): string {
      return `${INITIAL_STATUS.replace('**Current State:** INITIALIZED', `**Current State:** ${state}`)}- 2026-02-25 - State set to ${state} (HUMAN)\n`;
    }

    async function postTransition(body: Record<string, unknown>): Promise<Response> {
      const routes = await importRouteModules();
      return routes.transitionRoute.POST(
        new Request('http://localhost/api/working-root/deliverable/status/transition', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            projectRoot: fixture.projectRoot,
            deliverablePath: fixture.deliverablePath,
            targetState: 'IN_PROGRESS',
            actor: 'HUMAN',
            date: '2026-02-27',
            approvalSha: 'abc1234',
            ...body
          })
        })
      );
    }

    beforeEach(async () => {
      await mkdir(path.join(fixture.projectRoot, path.dirname(RULING_RELATIVE)), { recursive: true });
      await writeFile(path.join(fixture.projectRoot, RULING_RELATIVE), '# Ruling\n', 'utf8');
    });

    it('applies CHECKING -> IN_PROGRESS with a ruling inside projectRoot and records it', async () => {
      await writeFile(fixture.statusFilePath, statusAt('CHECKING'), 'utf8');

      const response = await postTransition({ ruling: RULING_RELATIVE });

      expect(response.status).toBe(200);
      expect(await response.json()).toMatchObject({
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

      const response = await postTransition({
        ruling: path.join(fixture.projectRoot, RULING_RELATIVE)
      });

      expect(response.status).toBe(200);
      await expect(readFile(fixture.statusFilePath, 'utf8')).resolves.toContain(
        `[reversal from CHECKING; ruling: ${RULING_RELATIVE}; approval SHA: abc1234]`
      );
    });

    it.each([
      ['CHECKING', 'HUMAN with neither SHA nor ruling', { approvalSha: undefined }, 'APPROVAL_SHA_REQUIRED'],
      ['CHECKING', 'HUMAN with a SHA but no ruling', {}, 'RULING_REQUIRED'],
      ['CHECKING', 'no SHA', { approvalSha: undefined, ruling: RULING_RELATIVE }, 'APPROVAL_SHA_REQUIRED'],
      ['CHECKING', 'an agent actor', { actor: 'WORKING_ITEMS', ruling: RULING_RELATIVE }, 'UNAUTHORIZED_ACTOR'],
      ['CHECKING', 'a missing ruling', { ruling: 'execution/_Coordination/_DECISIONS/D-404.md' }, 'RULING_NOT_FOUND'],
      ['CHECKING', 'a directory ruling', { ruling: 'execution/_Coordination/_DECISIONS' }, 'RULING_NOT_FOUND'],
      ['CHECKING', 'the project root as ruling', { ruling: '.' }, 'RULING_OUTSIDE_PROJECT_ROOT'],
      ['CHECKING', 'a ruling outside projectRoot', { ruling: '../outside-ruling.md' }, 'RULING_OUTSIDE_PROJECT_ROOT'],
      ['CHECKING', 'a non-string ruling', { ruling: 42 }, 'INVALID_REQUEST'],
      ['ISSUED', 'a ruling on ISSUED -> IN_PROGRESS', { ruling: RULING_RELATIVE }, 'BACKWARD_TRANSITION'],
      ['ISSUED', 'ISSUED -> CHECKING', { targetState: 'CHECKING', ruling: RULING_RELATIVE }, 'BACKWARD_TRANSITION']
    ] as const)('denies %s reversal request with %s as %s without writing', async (state, _label, body, type) => {
      await writeFile(path.join(fixture.tmpRoot, 'outside-ruling.md'), '# Outside\n', 'utf8');
      const before = statusAt(state);
      await writeFile(fixture.statusFilePath, before, 'utf8');

      const response = await postTransition(body);

      expect(response.status).toBe(400);
      expect(await response.json()).toMatchObject({ error: { type } });
      await expect(readFile(fixture.statusFilePath, 'utf8')).resolves.toBe(before);
    });

    async function expectDeniedWithoutWrite(
      body: Record<string, unknown>,
      type: string,
      state: 'IN_PROGRESS' | 'CHECKING' = 'CHECKING'
    ): Promise<void> {
      const before = statusAt(state);
      await writeFile(fixture.statusFilePath, before, 'utf8');

      const response = await postTransition(body);

      expect(response.status).toBe(400);
      expect(await response.json()).toMatchObject({ error: { type } });
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

      const response = await postTransition({ ruling: '..ruling-notes.md' });

      expect(response.status).toBe(200);
      await expect(readFile(fixture.statusFilePath, 'utf8')).resolves.toContain(
        '[reversal from CHECKING; ruling: ..ruling-notes.md; approval SHA: abc1234]'
      );
    });

    it('accepts an optional ruling on IN_PROGRESS -> CHECKING and records it', async () => {
      await writeFile(fixture.statusFilePath, statusAt('IN_PROGRESS'), 'utf8');

      const response = await postTransition({ targetState: 'CHECKING', ruling: RULING_RELATIVE });

      expect(response.status).toBe(200);
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

      const response = await postTransition({
        ruling: 'execution/_Coordination/_DECISIONS/D-LINK.md'
      });

      expect(response.status).toBe(400);
      expect(await response.json()).toMatchObject({
        error: { type: 'RULING_OUTSIDE_PROJECT_ROOT' }
      });
    });
  });

  it('reads dependency register data from Dependencies.csv', async () => {
    const routes = await importRouteModules();
    const response = await routes.dependenciesRoute.GET(
      new Request(
        `http://localhost/api/working-root/deliverable/dependencies?projectRoot=${encodeURIComponent(fixture.projectRoot)}&deliverablePath=${encodeURIComponent(fixture.deliverablePath)}`
      )
    );

    expect(response.status).toBe(200);
    const body = (await response.json()) as {
      rows: DependencyRegisterRow[];
      headers: string[];
      registerPresent: boolean;
      secondarySummaryPresent: boolean;
    };

    expect(body.registerPresent).toBe(true);
    expect(body.secondarySummaryPresent).toBe(false);
    expect(body.rows).toHaveLength(1);
    expect(body.rows[0].DependencyID).toBe('DEP-05-03-001');
    expect(body.headers).toContain('RegisterSchemaVersion');
  });

  it('returns explicit dependency-register absence without inferring summary rows', async () => {
    await rm(fixture.dependenciesFilePath, { force: true });
    const summaryPath = path.join(fixture.deliverablePath, '_DEPENDENCIES.md');
    await writeFile(
      summaryPath,
      '# Dependencies\n\nThis prose summary names dependency context but is not a structured register.\n',
      'utf8'
    );

    const routes = await importRouteModules();
    const response = await routes.dependenciesRoute.GET(
      new Request(
        `http://localhost/api/working-root/deliverable/dependencies?projectRoot=${encodeURIComponent(fixture.projectRoot)}&deliverablePath=${encodeURIComponent(fixture.deliverablePath)}`
      )
    );

    expect(response.status).toBe(200);
    const body = (await response.json()) as {
      deliverablePath: string;
      rows: DependencyRegisterRow[];
      headers: string[];
      warnings: string[];
      dependenciesSummaryPath?: string;
      registerPresent: boolean;
      secondarySummaryPresent: boolean;
    };

    expect(body.registerPresent).toBe(false);
    expect(body.secondarySummaryPresent).toBe(true);
    expect(body.dependenciesSummaryPath).toBe(path.join(body.deliverablePath, '_DEPENDENCIES.md'));
    expect(body.rows).toEqual([]);
    expect(body.headers).toEqual([]);
    expect(body.warnings).toEqual([
      'DEPENDENCY_REGISTER_NOT_FOUND: Dependencies.csv is absent; _DEPENDENCIES.md is present as a secondary summary, but no structured rows were inferred.'
    ]);
  });

  it('rejects symlink deliverable paths that resolve outside projectRoot', async () => {
    const routes = await importRouteModules();
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

    const response = await routes.statusRoute.GET(
      new Request(
        `http://localhost/api/working-root/deliverable/status?projectRoot=${encodeURIComponent(fixture.projectRoot)}&deliverablePath=${encodeURIComponent(symlinkDeliverable)}`
      )
    );

    expect(response.status).toBe(400);
    expect(await response.json()).toMatchObject({
      error: {
        type: 'DELIVERABLE_PATH_OUTSIDE_PROJECT_ROOT'
      }
    });
  });

  it('rejects dependency writes when FromDeliverableID mismatches the host deliverable', async () => {
    const routes = await importRouteModules();
    const response = await routes.dependenciesRoute.PUT(
      new Request('http://localhost/api/working-root/deliverable/dependencies', {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          projectRoot: fixture.projectRoot,
          deliverablePath: fixture.deliverablePath,
          rows: [makeDependencyRow({ FromDeliverableID: 'DEL-99-99' })]
        })
      })
    );

    expect(response.status).toBe(400);
    expect(await response.json()).toMatchObject({
      error: {
        type: 'INVALID_IDENTITY'
      }
    });
  });

  it('rejects invalid SatisfactionStatus jumps against prior register rows', async () => {
    const routes = await importRouteModules();
    const response = await routes.dependenciesRoute.PUT(
      new Request('http://localhost/api/working-root/deliverable/dependencies', {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          projectRoot: fixture.projectRoot,
          deliverablePath: fixture.deliverablePath,
          rows: [makeDependencyRow({ SatisfactionStatus: 'SATISFIED' })]
        })
      })
    );

    expect(response.status).toBe(400);
    expect(await response.json()).toMatchObject({
      error: {
        type: 'INVALID_SATISFACTION_TRANSITION'
      }
    });
  });

  it('writes dependency register rows when transitions are valid', async () => {
    const routes = await importRouteModules();
    const response = await routes.dependenciesRoute.PUT(
      new Request('http://localhost/api/working-root/deliverable/dependencies', {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          projectRoot: fixture.projectRoot,
          deliverablePath: fixture.deliverablePath,
          rows: [makeDependencyRow({ SatisfactionStatus: 'IN_PROGRESS' })]
        })
      })
    );

    expect(response.status).toBe(200);
    const body = (await response.json()) as { rows: DependencyRegisterRow[] };
    expect(body.rows[0].SatisfactionStatus).toBe('IN_PROGRESS');

    const csv = await readFile(fixture.dependenciesFilePath, 'utf8');
    expect(csv).toContain('IN_PROGRESS');
  });

  it('rejects dependency writes to an external-target leaf symlink without replacing it', async () => {
    const externalDependenciesPath = path.join(fixture.tmpRoot, 'external-dependencies.csv');
    const externalBytes = 'external dependency bytes must remain unchanged\n';
    await writeFile(externalDependenciesPath, externalBytes, 'utf8');
    await rm(fixture.dependenciesFilePath);
    await symlink(externalDependenciesPath, fixture.dependenciesFilePath);

    const routes = await importRouteModules();
    const response = await routes.dependenciesRoute.PUT(
      new Request('http://localhost/api/working-root/deliverable/dependencies', {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          projectRoot: fixture.projectRoot,
          deliverablePath: fixture.deliverablePath,
          rows: [makeDependencyRow({ SatisfactionStatus: 'IN_PROGRESS' })]
        })
      })
    );

    expect(response.status).toBe(403);
    expect(await response.json()).toMatchObject({
      error: {
        type: 'SYMLINK_WRITE_DENIED',
        details: { file: 'Dependencies.csv' }
      }
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

    const routes = await importRouteModules();
    const response = await routes.dependenciesRoute.PUT(
      new Request('http://localhost/api/working-root/deliverable/dependencies', {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          projectRoot: fixture.projectRoot,
          deliverablePath: fixture.deliverablePath,
          rows: [makeDependencyRow({ SatisfactionStatus: 'IN_PROGRESS' })]
        })
      })
    );

    expect(response.status).toBe(403);
    expect(await response.json()).toMatchObject({
      error: {
        type: 'SYMLINK_WRITE_DENIED',
        details: { file: 'Dependencies.csv' }
      }
    });
    expect((await lstat(fixture.dependenciesFilePath)).isSymbolicLink()).toBe(true);
    await expect(readFile(danglingTargetPath, 'utf8')).rejects.toMatchObject({ code: 'ENOENT' });
    expect(await readFile(sentinelPath, 'utf8')).toBe(externalBytes);
  });

  it('serves _STATUS.md content by default when no file is requested', async () => {
    const routes = await importRouteModules();
    const response = await routes.contentRoute.GET(
      contentRequest(fixture.projectRoot, fixture.deliverablePath)
    );

    expect(response.status).toBe(200);
    const body = (await response.json()) as { content: string; file: string };
    expect(body.file).toBe('_STATUS.md');
    expect(body.content).toContain('**Current State:** INITIALIZED');
  });

  it('serves an explicit relative file within the deliverable', async () => {
    await writeFile(
      path.join(fixture.deliverablePath, 'Specification.md'),
      '# Spec\n\nThe body of the deliverable.\n',
      'utf8'
    );
    const routes = await importRouteModules();
    const response = await routes.contentRoute.GET(
      contentRequest(fixture.projectRoot, fixture.deliverablePath, 'Specification.md')
    );

    expect(response.status).toBe(200);
    const body = (await response.json()) as { content: string; file: string };
    expect(body.file).toBe('Specification.md');
    expect(body.content).toContain('The body of the deliverable.');
  });

  it('rejects a file that traverses out of the deliverable directory', async () => {
    const routes = await importRouteModules();
    const response = await routes.contentRoute.GET(
      contentRequest(fixture.projectRoot, fixture.deliverablePath, '../_STATUS.md')
    );

    expect(response.status).toBe(400);
    expect(await response.json()).toMatchObject({
      error: { type: 'DELIVERABLE_FILE_OUTSIDE_DELIVERABLE' }
    });
  });

  it('rejects an absolute file path', async () => {
    const routes = await importRouteModules();
    const response = await routes.contentRoute.GET(
      contentRequest(fixture.projectRoot, fixture.deliverablePath, '/etc/hosts')
    );

    expect(response.status).toBe(400);
    expect(await response.json()).toMatchObject({
      error: { type: 'DELIVERABLE_FILE_OUTSIDE_DELIVERABLE' }
    });
  });

  it('returns 404 for a missing file in the deliverable', async () => {
    const routes = await importRouteModules();
    const response = await routes.contentRoute.GET(
      contentRequest(fixture.projectRoot, fixture.deliverablePath, 'Datasheet.md')
    );

    expect(response.status).toBe(404);
    expect(await response.json()).toMatchObject({
      error: { type: 'DELIVERABLE_CONTENT_NOT_FOUND' }
    });
  });

  it('rejects a symlinked file that resolves outside the deliverable', async () => {
    const externalSecret = path.join(fixture.tmpRoot, 'outside-secret.md');
    await writeFile(externalSecret, '# Secret\n\nshould never be served.\n', 'utf8');
    const escapingLink = path.join(fixture.deliverablePath, 'escape.md');
    await symlink(externalSecret, escapingLink);

    const routes = await importRouteModules();
    const response = await routes.contentRoute.GET(
      contentRequest(fixture.projectRoot, fixture.deliverablePath, 'escape.md')
    );

    expect(response.status).toBe(400);
    expect(await response.json()).toMatchObject({
      error: { type: 'DELIVERABLE_FILE_OUTSIDE_DELIVERABLE' }
    });
  });

  it('rejects a file reached through a symlinked directory component that escapes', async () => {
    // The escape is via an intermediate directory symlink, not a leaf-file symlink:
    // the post-realpath containment re-check must catch mid-path symlink resolution.
    const externalDir = path.join(fixture.tmpRoot, 'outside-dir');
    await mkdir(externalDir, { recursive: true });
    await writeFile(path.join(externalDir, 'Spec.md'), '# External\n\nleaked.\n', 'utf8');
    await symlink(externalDir, path.join(fixture.deliverablePath, 'linkdir'));

    const routes = await importRouteModules();
    const response = await routes.contentRoute.GET(
      contentRequest(fixture.projectRoot, fixture.deliverablePath, 'linkdir/Spec.md')
    );

    expect(response.status).toBe(400);
    expect(await response.json()).toMatchObject({
      error: { type: 'DELIVERABLE_FILE_OUTSIDE_DELIVERABLE' }
    });
  });

  it('serves a valid file nested in a subdirectory and reports its relative path', async () => {
    await mkdir(path.join(fixture.deliverablePath, 'attachments'), { recursive: true });
    await writeFile(
      path.join(fixture.deliverablePath, 'attachments', 'diagram.md'),
      '# Diagram\n\nnested body.\n',
      'utf8'
    );

    const routes = await importRouteModules();
    const response = await routes.contentRoute.GET(
      contentRequest(fixture.projectRoot, fixture.deliverablePath, 'attachments/diagram.md')
    );

    expect(response.status).toBe(200);
    const body = (await response.json()) as { content: string; file: string };
    expect(body.file).toBe(path.join('attachments', 'diagram.md'));
    expect(body.content).toContain('nested body.');
  });

  it('returns 404 when the requested file is the deliverable directory itself', async () => {
    const routes = await importRouteModules();
    const response = await routes.contentRoute.GET(
      contentRequest(fixture.projectRoot, fixture.deliverablePath, '.')
    );

    expect(response.status).toBe(404);
    expect(await response.json()).toMatchObject({
      error: { type: 'DELIVERABLE_CONTENT_NOT_FOUND' }
    });
  });

  it('returns 404 when the requested file is a subdirectory, not a regular file', async () => {
    await mkdir(path.join(fixture.deliverablePath, 'subdir'), { recursive: true });

    const routes = await importRouteModules();
    const response = await routes.contentRoute.GET(
      contentRequest(fixture.projectRoot, fixture.deliverablePath, 'subdir')
    );

    expect(response.status).toBe(404);
    expect(await response.json()).toMatchObject({
      error: { type: 'DELIVERABLE_CONTENT_NOT_FOUND' }
    });
  });
});
