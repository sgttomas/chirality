/**
 * Parity of the App recorded-register module with the Root reference tools.
 *
 * Each folder in `src/__tests__/fixtures/recorded-register/cases/` is an
 * execution root. `expected/<case>.json` holds what the Root tools
 * (`tools/coordination/dependency_evidence.py` and the project mode of
 * `tools/coordination/build_dev001_blocker_queue.py`) produce on it. After a
 * change to either implementation or to a fixture, regenerate and re-check
 * from the repository root:
 *
 *   python3 projects/chirality-app-dev/frontend/src/__tests__/fixtures/recorded-register/generate_expected.py
 *   python3 projects/chirality-app-dev/frontend/src/__tests__/fixtures/recorded-register/generate_expected.py --check
 *
 * then run this test. A difference here means the TypeScript module and the
 * Root tools no longer agree on the same files.
 */
import { cp, mkdtemp, readFile, readdir, rm, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { afterAll, describe, expect, it } from 'vitest';
import {
  buildProjectBlockerQueue,
  checkCurrency,
  DagPointerError,
  executionRootForDeliverable,
  parseDeclarations,
  parseDefaultMaturity,
  readDefaultMaturity,
  readDeliverableRecordedRegister,
  readProjectRegisters,
  resolveAcceptedDag
} from '../../lib/dependencies/recorded-register';

const FIXTURES = path.resolve(__dirname, '../fixtures/recorded-register');
const CASES = path.join(FIXTURES, 'cases');

async function caseNames(): Promise<string[]> {
  const entries = await readdir(CASES, { withFileTypes: true });
  return entries.filter((entry) => entry.isDirectory()).map((entry) => entry.name).sort();
}

async function actual(root: string): Promise<unknown> {
  const defaultMaturity = await readDefaultMaturity(root);
  const registers = await readProjectRegisters(root);
  const dag = await resolveAcceptedDag(root);
  const queue = await buildProjectBlockerQueue(root, { defaultMaturity: defaultMaturity.value });
  return {
    defaultMaturity,
    registers: Object.fromEntries(
      [...registers].map(([id, register]) => [
        id,
        {
          deliverableId: register.deliverableId,
          mode: register.mode,
          csvPresent: register.csvPresent,
          declarationsPresent: register.declarationsPresent,
          entries: register.entries,
          rows: register.rows,
          declaredOnly: register.declaredOnly,
          disagreements: register.disagreements,
          unread: register.unread
        }
      ])
    ),
    currency: dag === null ? null : checkCurrency(dag, registers),
    queue: {
      blockerSource: queue.blockerSource,
      acceptedDagVersion: queue.acceptedDag?.version ?? null,
      gatingArcCount: queue.gatingArcCount,
      heldArcCount: queue.heldArcCount,
      declaredOnlyCount: queue.declaredOnlyCount,
      declaredDisagreements: queue.declaredDisagreements,
      unblockedCount: queue.unblockedCount,
      blockedCount: queue.blockedCount,
      dagPendingCount: queue.dagPendingCount,
      notTrackedCount: queue.notTrackedCount,
      queueRows: queue.queueRows
    }
  };
}

const COVERAGE: Record<string, string> = {
  'union-no-csv': 'declarations only, no Dependencies.csv',
  'union-with-csv': 'union with a CSV: a matching entry counted once, a CSV-only row, and a declaration that governs a disagreeing maturity',
  'retired-row': 'a declaration whose only CSV row is RETIRED, with no stated maturity',
  'legacy-headings': 'legacy headings, TRACKED read as FULL_GRAPH, the combined list, informational downstream and unread lines',
  'default-threshold': 'missing and TBD maturities take the _COORDINATION.md default threshold',
  'downstream-first': 'DOWNSTREAM-first rows judged by the supplier, a cross-deliverable disagreement, NOT_TRACKED and a held cycle',
  'dag-current': 'an accepted DAG that is current: blockers from the version, candidates held',
  'dag-departure': 'a DAG departure: DAG pending with no verdict, excluded arcs, inventory changes'
};

describe('recorded register parity with the Root reference tools', () => {
  it('has an expected result for every fixture case and covers the listed cases', async () => {
    const names = await caseNames();
    const expected = (await readdir(path.join(FIXTURES, 'expected'))).sort();
    expect(expected).toEqual(names.map((name) => `${name}.json`));
    expect(names).toEqual(Object.keys(COVERAGE).sort());
  });

  for (const [name, coverage] of Object.entries(COVERAGE)) {
    it(`${name}: ${coverage}`, async () => {
      const expected = JSON.parse(await readFile(path.join(FIXTURES, 'expected', `${name}.json`), 'utf8'));
      expect(JSON.parse(JSON.stringify(await actual(path.join(CASES, name))))).toEqual(expected);
    });
  }
});

describe('recorded register reads for one deliverable', () => {
  const scratch: string[] = [];

  afterAll(async () => {
    await Promise.all(scratch.map((dir) => rm(dir, { recursive: true, force: true })));
  });

  it('gives the supplier-judged verdict, the arcs and the disagreements of the deliverable', async () => {
    const root = path.join(CASES, 'union-with-csv');
    const deliverablePath = path.join(root, 'PKG-02_Data', '1_Working', 'DEL-02-01_Consumer');
    const read = await readDeliverableRecordedRegister({ deliverablePath, containmentRoot: root });

    expect(read.executionRoot).toBe(root);
    expect(read.trackingMode).toBe('FULL_GRAPH');
    expect(read.blockers.blockerState).toBe('BLOCKED');
    expect(read.blockers.blockerSource).toBe('RECORDED_REGISTER');
    expect(read.blockers.blockingUpstreamCount).toBe(2);
    expect(read.blockers.blockingUpstreamDeliverables).toEqual(['DEL-02-02', 'DEL-02-05']);
    expect(read.blockers.upstreamArcs.find((arc) => arc.supplier === 'DEL-02-02')).toMatchObject({
      requiredMaturity: 'ISSUED',
      supplierState: 'IN_PROGRESS',
      satisfied: false
    });
    expect(read.disagreements).toEqual([
      expect.objectContaining({ DependencyID: 'DEP-02-01-001', Declared: 'ISSUED', Csv: 'INITIALIZED' })
    ]);
    expect(read.unionRows.map((row) => row.DependencyID)).toEqual([
      'DEP-02-01-001',
      'DEP-02-01-002',
      'DEP-02-01-004',
      'DEP-02-01-005'
    ]);
  });

  it('marks a deliverable DAG pending with no verdict and keeps a current one judged by the version', async () => {
    const root = path.join(CASES, 'dag-departure');
    const pending = await readDeliverableRecordedRegister({
      deliverablePath: path.join(root, 'PKG-08_Flow', '1_Working', 'DEL-08-03_Worker'),
      containmentRoot: root
    });
    expect(pending.blockers).toMatchObject({
      blockerState: 'DAG_PENDING',
      dagPending: true,
      blockingUpstreamCount: null,
      acceptedDagVersion: 'DAG-002',
      dagPendingReasons: ['arc added: DEL-08-03 -> DEL-08-04']
    });

    const current = await readDeliverableRecordedRegister({
      deliverablePath: path.join(root, 'PKG-08_Flow', '1_Working', 'DEL-08-01_Intake'),
      containmentRoot: root
    });
    expect(current.blockers).toMatchObject({
      blockerState: 'BLOCKED',
      blockerSource: 'ACCEPTED_DAG:DAG-002',
      dagPending: false,
      blockingEdgeIds: ['E-101']
    });
  });

  it('gives no verdict when the execution root is outside the containment root', async () => {
    const root = path.join(CASES, 'union-no-csv');
    const deliverablePath = path.join(root, 'PKG-01_Core', '1_Working', 'DEL-01-01_Alpha');
    const read = await readDeliverableRecordedRegister({
      deliverablePath,
      containmentRoot: path.join(root, 'PKG-01_Core')
    });
    expect(read.executionRoot).toBeNull();
    expect(read.blockers.blockerState).toBe('NOT_ASSESSED');
    expect(read.blockers.notAssessedReason).toMatch(/^EXECUTION_ROOT_OUTSIDE_PROJECT_ROOT/);
    expect(read.declaredOnlyRows.map((row) => row.TargetDeliverableID)).toEqual(['DEL-01-02', 'DEL-01-03']);
  });

  it('reports an unresolvable DAG pointer instead of giving a verdict', async () => {
    const root = await mkdtemp(path.join(os.tmpdir(), 'recorded-register-'));
    scratch.push(root);
    await cp(path.join(CASES, 'dag-current'), root, { recursive: true });
    await writeFile(path.join(root, '_DAG', '_LATEST.md'), '# Pointer\n\nLatest: DAG-009\n', 'utf8');
    await expect(resolveAcceptedDag(root)).rejects.toBeInstanceOf(DagPointerError);
    const read = await readDeliverableRecordedRegister({
      deliverablePath: path.join(root, 'PKG-07_Graph', '1_Working', 'DEL-07-01_Planner'),
      containmentRoot: root
    });
    expect(read.blockers.blockerState).toBe('NOT_ASSESSED');
    expect(read.blockers.notAssessedReason).toMatch(/^DAG_POINTER_ERROR:/);
  });

  it('locates the execution root only from the SPEC §2 folder shape', () => {
    expect(executionRootForDeliverable('/p/execution/PKG-01_A/1_Working/DEL-01-01_X')).toBe('/p/execution');
    expect(executionRootForDeliverable('/p/execution/CAT-01_A/3_Issued/KTY-01-01_X')).toBe('/p/execution');
    expect(executionRootForDeliverable('/p/execution/PKG-01_A/0_References/DEL-01-01_X')).toBeNull();
    expect(executionRootForDeliverable('/p/execution/DEL-01-01_X')).toBeNull();
  });

  it('reads the default threshold only when the coordination record names one state', () => {
    expect(parseDefaultMaturity('**Default maturity threshold (if computing blockers):** `CHECKING`')).toEqual({
      value: 'CHECKING',
      source: 'COORDINATION_RECORD'
    });
    expect(
      parseDefaultMaturity(
        '**Default maturity threshold (if computing blockers):** [INITIALIZED|SEMANTIC_READY|IN_PROGRESS|CHECKING|ISSUED]'
      )
    ).toEqual({ value: 'INITIALIZED', source: 'FALLBACK' });
    expect(parseDefaultMaturity(null)).toEqual({ value: 'INITIALIZED', source: 'FALLBACK' });
  });

  it('skips placeholder and externally coordinated lines', () => {
    const parsed = parseDeclarations(
      '## Dependency Tracking Mode\n- **Mode:** NOT_TRACKED\n\n## Declared Upstream (I need these before I can proceed)\n- Dependencies coordinated externally by humans.\n- TBD\n'
    );
    expect(parsed).toEqual({ mode: 'NOT_TRACKED', entries: [], unread: [] });
  });
});
