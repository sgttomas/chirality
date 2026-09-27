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
import { cp, mkdir, mkdtemp, readFile, readdir, realpath, rename, rm, symlink, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { afterAll, describe, expect, it } from 'vitest';
import {
  buildProjectBlockerQueue,
  checkCurrency,
  DagPointerError,
  executionRootForDeliverable,
  heldArcs,
  MAX_REGISTER_FILE_BYTES,
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
  'declared-governs-arc':
    'a cross-deliverable arc whose declared maturity (satisfied) and row maturity (not satisfied) give different verdicts',
  'dag-current': 'an accepted DAG that is current: blockers from the version, candidates held',
  'dag-candidate-removed': 'a DAG candidate arc (CandidateEdges.csv) with no local row: its endpoints are DAG pending',
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

// The fixture case folders are execution roots that are not named `execution`,
// so reads of them in place name the root explicitly, as the Root tools take
// `--execution-root`. App reads resolve it instead; the copies under a
// `<project>/execution/` folder further below exercise that resolution.
describe('recorded register reads for one deliverable', () => {
  const scratch: string[] = [];

  afterAll(async () => {
    await Promise.all(scratch.map((dir) => rm(dir, { recursive: true, force: true })));
  });

  it('gives the supplier-judged verdict, the arcs and the disagreements of the deliverable', async () => {
    const root = path.join(CASES, 'union-with-csv');
    const deliverablePath = path.join(root, 'PKG-02_Data', '1_Working', 'DEL-02-01_Consumer');
    const read = await readDeliverableRecordedRegister({ deliverablePath, containmentRoot: root, executionRoot: root });

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
      containmentRoot: root,
      executionRoot: root
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
      containmentRoot: root,
      executionRoot: root
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
      containmentRoot: path.join(root, 'PKG-01_Core'),
      executionRoot: root
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
      containmentRoot: root,
      executionRoot: root
    });
    expect(read.blockers.blockerState).toBe('NOT_ASSESSED');
    expect(read.blockers.notAssessedReason).toMatch(/^DAG_POINTER_ERROR:/);
  });

  it('gives the execution root the SPEC §2 folder shape implies', () => {
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

describe('recorded register reads stay inside the read root', () => {
  const scratch: string[] = [];

  afterAll(async () => {
    await Promise.all(scratch.map((dir) => rm(dir, { recursive: true, force: true })));
  });

  /**
   * A copy of a fixture case as the execution root `<base>/project/execution`
   * of the project `<base>/project`, and an empty `<base>/outside`. Reads use
   * the project as their containment root and resolve the execution root.
   */
  async function copyCase(name: string): Promise<{ project: string; root: string; outside: string }> {
    const base = await realpath(await mkdtemp(path.join(os.tmpdir(), 'recorded-register-scope-')));
    scratch.push(base);
    const project = path.join(base, 'project');
    const root = path.join(project, 'execution');
    const outside = path.join(base, 'outside');
    await cp(path.join(CASES, name), root, { recursive: true });
    await mkdir(outside, { recursive: true });
    return { project, root, outside };
  }

  const status = (state: string): string => `# Status\n\n**Current State:** ${state}\n`;

  it('does not inventory units through a lifecycle folder linked outside the root', async () => {
    const { project, root, outside } = await copyCase('union-no-csv');
    const secret = path.join(outside, 'DEL-01-09_Secret');
    await mkdir(secret);
    const header = (await readFile(path.join(CASES, 'dag-current', '_DAG', 'DAG-001', 'DependencyEdges.csv'), 'utf8'))
      .split('\n')[0];
    await writeFile(
      path.join(secret, 'Dependencies.csv'),
      `${header}\nv3.1,DEP-01-09-001,PKG-01,DEL-01-09,,EXECUTION,NOT_APPLICABLE,DOWNSTREAM,ENABLES,DELIVERABLE,PKG-01,DEL-01-01,,,,x,_CONTEXT.md,_CONTEXT.md,x,EXPLICIT,ISSUED,,TBD,HIGH,EXTRACTED,2026-09-26,2026-09-26,ACTIVE,\n`,
      'utf8'
    );
    await writeFile(path.join(secret, '_STATUS.md'), status('OPEN'), 'utf8');
    await symlink(outside, path.join(root, 'PKG-01_Core', '3_Issued'), 'dir');

    expect([...(await readProjectRegisters(root)).keys()]).not.toContain('DEL-01-09');
    const read = await readDeliverableRecordedRegister({
      deliverablePath: path.join(root, 'PKG-01_Core', '1_Working', 'DEL-01-01_Alpha'),
      containmentRoot: project
    });
    expect(read.warnings).toEqual([
      `READ_OUTSIDE_ROOT: ${path.join('execution', 'PKG-01_Core', '3_Issued')} resolves outside the read root; it was not read.`
    ]);
    expect(read.blockers.blockerState).toBe('NOT_ASSESSED');
    expect(read.blockers.notAssessedReason).toMatch(/^READ_REFUSED:/);
    expect(JSON.stringify(read)).not.toContain('DEL-01-09');
  });

  it('does not read the default threshold through a _Coordination folder linked outside the root', async () => {
    const { project, root, outside } = await copyCase('union-no-csv');
    await rm(path.join(root, '_Coordination'), { recursive: true });
    await writeFile(
      path.join(outside, '_COORDINATION.md'),
      '# Coordination Record\n\n**Default maturity threshold (if computing blockers):** `ISSUED`\n',
      'utf8'
    );
    await symlink(outside, path.join(root, '_Coordination'), 'dir');

    expect(await readDefaultMaturity(root)).toEqual({ value: 'INITIALIZED', source: 'FALLBACK' });
    const read = await readDeliverableRecordedRegister({
      deliverablePath: path.join(root, 'PKG-01_Core', '1_Working', 'DEL-01-01_Alpha'),
      containmentRoot: project
    });
    expect(read.blockers.defaultMaturity).toEqual({ value: 'INITIALIZED', source: 'FALLBACK' });
    expect(read.warnings).toEqual([
      `READ_OUTSIDE_ROOT: ${path.join('execution', '_Coordination', '_COORDINATION.md')} resolves outside the read root; it was not read.`
    ]);
    expect(read.blockers.blockerState).toBe('NOT_ASSESSED');
  });

  it('does not read an accepted DAG version folder linked outside the root', async () => {
    const { project, root, outside } = await copyCase('dag-current');
    await rename(path.join(root, '_DAG', 'DAG-001'), path.join(outside, 'DAG-001'));
    await symlink(path.join(outside, 'DAG-001'), path.join(root, '_DAG', 'DAG-001'), 'dir');

    await expect(resolveAcceptedDag(root)).rejects.toBeInstanceOf(DagPointerError);
    const read = await readDeliverableRecordedRegister({
      deliverablePath: path.join(root, 'PKG-07_Graph', '1_Working', 'DEL-07-01_Planner'),
      containmentRoot: project
    });
    expect(read.warnings).toContain(
      `READ_OUTSIDE_ROOT: ${path.join('execution', '_DAG', 'DAG-001', 'DeliverableNodes.csv')} resolves outside the read root; it was not read.`
    );
    expect(read.blockers.blockerState).toBe('NOT_ASSESSED');
    expect(read.blockers.acceptedDagVersion).toBeNull();
  });

  it('does not read a _DAG folder linked outside the root, and does not fall back silently', async () => {
    const { project, root, outside } = await copyCase('dag-current');
    await rename(path.join(root, '_DAG'), path.join(outside, '_DAG'));
    await symlink(path.join(outside, '_DAG'), path.join(root, '_DAG'), 'dir');

    const queue = await buildProjectBlockerQueue(root);
    expect(queue.acceptedDag).toBeNull();
    expect(queue.warnings).toEqual([
      `READ_OUTSIDE_ROOT: ${path.join('_DAG', '_LATEST.md')} resolves outside the read root; it was not read.`
    ]);
    const read = await readDeliverableRecordedRegister({
      deliverablePath: path.join(root, 'PKG-07_Graph', '1_Working', 'DEL-07-01_Planner'),
      containmentRoot: project
    });
    expect(read.blockers.blockerState).toBe('NOT_ASSESSED');
    expect(read.blockers.blockerSource).not.toMatch(/^ACCEPTED_DAG|^RECORDED_REGISTER/);
    expect(read.blockers.notAssessedReason).toMatch(/^READ_REFUSED:/);
  });

  it('reads a _LATEST.md and a Dependencies.csv linked inside the root as their targets, as the Root tools do', async () => {
    const { project, root } = await copyCase('dag-current');
    const links = path.join(root, '_Coordination', 'linked');
    await mkdir(links);
    await rename(path.join(root, '_DAG', '_LATEST.md'), path.join(links, 'LATEST.md'));
    await symlink(path.join('..', '_Coordination', 'linked', 'LATEST.md'), path.join(root, '_DAG', '_LATEST.md'));
    const planner = path.join(root, 'PKG-07_Graph', '1_Working', 'DEL-07-01_Planner');
    await rename(path.join(planner, 'Dependencies.csv'), path.join(links, 'planner.csv'));
    await symlink(path.join(links, 'planner.csv'), path.join(planner, 'Dependencies.csv'));

    const expected = JSON.parse(await readFile(path.join(FIXTURES, 'expected', 'dag-current.json'), 'utf8'));
    expect(JSON.parse(JSON.stringify(await actual(root)))).toEqual(expected);
    const read = await readDeliverableRecordedRegister({ deliverablePath: planner, containmentRoot: project });
    expect(read.warnings).toEqual([]);
    expect(read.blockers.blockerSource).toBe('ACCEPTED_DAG:DAG-001');
  });

  it('refuses a _LATEST.md linked outside the root with a warning and no verdict', async () => {
    const { project, root, outside } = await copyCase('dag-current');
    await rename(path.join(root, '_DAG', '_LATEST.md'), path.join(outside, 'LATEST.md'));
    await symlink(path.join(outside, 'LATEST.md'), path.join(root, '_DAG', '_LATEST.md'));

    const read = await readDeliverableRecordedRegister({
      deliverablePath: path.join(root, 'PKG-07_Graph', '1_Working', 'DEL-07-01_Planner'),
      containmentRoot: project
    });
    expect(read.warnings).toEqual([
      `READ_OUTSIDE_ROOT: ${path.join('execution', '_DAG', '_LATEST.md')} resolves outside the read root; it was not read.`
    ]);
    expect(read.blockers.blockerState).toBe('NOT_ASSESSED');
  });

  it('gives no verdict for a deliverable reached through a package folder linked inside the root', async () => {
    const { project, root } = await copyCase('dag-current');
    await mkdir(path.join(root, 'store'));
    await rename(path.join(root, 'PKG-07_Graph'), path.join(root, 'store', 'PKG-07_Graph'));
    await symlink(path.join(root, 'store', 'PKG-07_Graph'), path.join(root, 'PKG-07_Graph'), 'dir');
    const requestedPath = path.join(root, 'PKG-07_Graph', '1_Working', 'DEL-07-01_Planner');
    const deliverablePath = await realpath(requestedPath);

    // The canonical folder sits under execution/store, which has no _DAG: a verdict there would be silently wrong.
    const read = await readDeliverableRecordedRegister({ deliverablePath, requestedPath, containmentRoot: project });
    expect(read.executionRoot).toBeNull();
    expect(read.blockers.blockerState).toBe('NOT_ASSESSED');
    expect(read.blockers.notAssessedReason).toMatch(/^SYMLINKED_UNIT_PATH: /);
    expect(read.warnings).toEqual([read.blockers.notAssessedReason]);

    const direct = await readDeliverableRecordedRegister({ deliverablePath: requestedPath, containmentRoot: project });
    expect(direct.blockers.notAssessedReason).toMatch(/^SYMLINKED_UNIT_PATH: /);
  });

  it('refuses a symbolic-link loop instead of reading it as an absent file', async () => {
    const { project, root } = await copyCase('union-with-csv');
    const consumer = path.join(root, 'PKG-02_Data', '1_Working', 'DEL-02-01_Consumer');
    await rm(path.join(consumer, 'Dependencies.csv'));
    await symlink('Dependencies.csv', path.join(consumer, 'Dependencies.csv'));

    const read = await readDeliverableRecordedRegister({ deliverablePath: consumer, containmentRoot: project });
    expect(read.warnings).toEqual([
      `LINK_LOOP: ${path.join('execution', 'PKG-02_Data', '1_Working', 'DEL-02-01_Consumer', 'Dependencies.csv')} is a symbolic-link loop; it was not read.`
    ]);
    expect(read.blockers.blockerState).toBe('NOT_ASSESSED');
    expect(read.blockers.notAssessedReason).toMatch(/^READ_REFUSED:/);
  });

  it('reports a file over the size cap as a warning instead of reading it', async () => {
    const { project, root } = await copyCase('union-with-csv');
    const consumer = path.join(root, 'PKG-02_Data', '1_Working', 'DEL-02-01_Consumer');
    const csvPath = path.join(consumer, 'Dependencies.csv');
    const original = await readFile(csvPath, 'utf8');
    await writeFile(csvPath, original + ' '.repeat(MAX_REGISTER_FILE_BYTES + 1 - Buffer.byteLength(original)), 'utf8');

    const read = await readDeliverableRecordedRegister({ deliverablePath: consumer, containmentRoot: project });
    expect(read.warnings).toEqual([
      `FILE_TOO_LARGE: ${path.join('execution', 'PKG-02_Data', '1_Working', 'DEL-02-01_Consumer', 'Dependencies.csv')} is larger than ${MAX_REGISTER_FILE_BYTES} bytes; it was not read.`
    ]);
    expect(read.csvPresent).toBe(false);
    expect(read.blockers.blockerState).toBe('NOT_ASSESSED');

    await writeFile(csvPath, original + ' '.repeat(MAX_REGISTER_FILE_BYTES - Buffer.byteLength(original)), 'utf8');
    const atLimit = await readDeliverableRecordedRegister({ deliverablePath: consumer, containmentRoot: project });
    expect(atLimit.warnings).toEqual([]);
    expect(atLimit.csvPresent).toBe(true);
  });
});

describe('recorded register reads resolve the execution root', () => {
  const scratch: string[] = [];

  afterAll(async () => {
    await Promise.all(scratch.map((dir) => rm(dir, { recursive: true, force: true })));
  });

  /** A project at `<base>/project` holding a copy of a fixture case at `<project>/<relativeRoot>`. */
  async function project(name: string, relativeRoot: string): Promise<{ project: string; root: string }> {
    const base = await realpath(await mkdtemp(path.join(os.tmpdir(), 'recorded-register-root-')));
    scratch.push(base);
    const projectRoot = path.join(base, 'project');
    const root = path.join(projectRoot, relativeRoot);
    await cp(path.join(CASES, name), root, { recursive: true });
    return { project: projectRoot, root };
  }

  async function writeAdapter(folder: string): Promise<void> {
    await mkdir(path.join(folder, '_harness'), { recursive: true });
    await writeFile(path.join(folder, '_harness', 'adapter.yaml'), 'adapter_version: 1\n', 'utf8');
  }

  const planner = (root: string): string => path.join(root, 'PKG-07_Graph', '1_Working', 'DEL-07-01_Planner');

  it('gives a deliverable under <project>/execution the same judgment as the fixture read with its root named', async () => {
    const { project: projectRoot, root } = await project('union-with-csv', 'execution');
    await writeAdapter(projectRoot);
    const fixtureRoot = path.join(CASES, 'union-with-csv');
    const named = await readDeliverableRecordedRegister({
      deliverablePath: path.join(fixtureRoot, 'PKG-02_Data', '1_Working', 'DEL-02-01_Consumer'),
      containmentRoot: fixtureRoot,
      executionRoot: fixtureRoot
    });

    const read = await readDeliverableRecordedRegister({
      deliverablePath: path.join(root, 'PKG-02_Data', '1_Working', 'DEL-02-01_Consumer'),
      containmentRoot: projectRoot
    });
    expect(read.executionRoot).toBe(root);
    expect(read.warnings).toEqual([]);
    expect(read.blockers).toEqual(named.blockers);
    expect(read.blockers).toMatchObject({ blockerState: 'BLOCKED', blockingUpstreamDeliverables: ['DEL-02-02', 'DEL-02-05'] });
    expect(read.unionRows).toEqual(named.unionRows);
    expect(read.disagreements).toEqual(named.disagreements);
  });

  it('accepts an adapter manifest inside the execution root that names it', async () => {
    const { project: projectRoot, root } = await project('dag-current', 'execution');
    await writeAdapter(root);
    const read = await readDeliverableRecordedRegister({ deliverablePath: planner(root), containmentRoot: projectRoot });
    expect(read.executionRoot).toBe(root);
    expect(read.warnings).toEqual([]);
    expect(read.blockers.blockerSource).toBe('ACCEPTED_DAG:DAG-001');
  });

  it('gives no verdict for a linked package requested at its target outside execution/ (FU5 review case)', async () => {
    const { project: projectRoot, root } = await project('dag-current', 'execution');
    await mkdir(path.join(projectRoot, 'store'));
    await rename(path.join(root, 'PKG-07_Graph'), path.join(projectRoot, 'store', 'PKG-07_Graph'));
    await symlink(path.join('..', 'store', 'PKG-07_Graph'), path.join(root, 'PKG-07_Graph'), 'dir');
    const target = path.join(projectRoot, 'store', 'PKG-07_Graph', '1_Working', 'DEL-07-01_Planner');

    // Inferred from the path shape, store/ would be taken for an execution root with no _DAG.
    expect(executionRootForDeliverable(target)).toBe(path.join(projectRoot, 'store'));
    const read = await readDeliverableRecordedRegister({ deliverablePath: target, requestedPath: target, containmentRoot: projectRoot });
    expect(read.executionRoot).toBeNull();
    expect(read.blockers.blockerState).toBe('NOT_ASSESSED');
    expect(read.blockers.blockerSource).toBe('NOT_ASSESSED');
    expect(read.blockers.notAssessedReason).toBe(
      `EXECUTION_ROOT_NOT_RESOLVED: ${path.join('store', 'PKG-07_Graph', '1_Working', 'DEL-07-01_Planner')} is not inside an execution/ folder; no verdict is given`
    );
    expect(read.warnings).toEqual([read.blockers.notAssessedReason]);

    // Requested through the link, it stays a linked unit path.
    const linked = await readDeliverableRecordedRegister({
      deliverablePath: target,
      requestedPath: planner(root),
      containmentRoot: projectRoot
    });
    expect(linked.blockers.notAssessedReason).toMatch(/^SYMLINKED_UNIT_PATH: /);
  });

  it('gives no verdict for a linked package requested at its target inside execution/ but off the unit shape', async () => {
    const { project: projectRoot, root } = await project('dag-current', 'execution');
    await mkdir(path.join(root, '_store'));
    await rename(path.join(root, 'PKG-07_Graph'), path.join(root, '_store', 'PKG-07_Graph'));
    await symlink(path.join('_store', 'PKG-07_Graph'), path.join(root, 'PKG-07_Graph'), 'dir');
    const target = path.join(root, '_store', 'PKG-07_Graph', '1_Working', 'DEL-07-01_Planner');

    const read = await readDeliverableRecordedRegister({ deliverablePath: target, requestedPath: target, containmentRoot: projectRoot });
    expect(read.executionRoot).toBeNull();
    expect(read.blockers.blockerState).toBe('NOT_ASSESSED');
    expect(read.blockers.notAssessedReason).toBe(
      `DELIVERABLE_OUTSIDE_EXECUTION_ROOT: ${path.join('execution', '_store', 'PKG-07_Graph', '1_Working', 'DEL-07-01_Planner')} is not at {EXECUTION_ROOT}/PKG-*/<lifecycle folder>/DEL-* for the execution root execution; no verdict is given`
    );
    expect(read.warnings).toEqual([read.blockers.notAssessedReason]);
  });

  it('gives no verdict for a deliverable outside any execution/ folder', async () => {
    const { project: projectRoot, root } = await project('union-with-csv', 'work');
    const read = await readDeliverableRecordedRegister({
      deliverablePath: path.join(root, 'PKG-02_Data', '1_Working', 'DEL-02-01_Consumer'),
      containmentRoot: projectRoot
    });
    expect(read.executionRoot).toBeNull();
    expect(read.blockers.blockerState).toBe('NOT_ASSESSED');
    expect(read.blockers.notAssessedReason).toMatch(/^EXECUTION_ROOT_NOT_RESOLVED: work\/PKG-02_Data\/.* is not inside an execution\/ folder/);
    expect(read.warnings).toEqual([read.blockers.notAssessedReason]);
    // The deliverable's own register is still read.
    expect(read.unionRows.map((row) => row.DependencyID)).toContain('DEP-02-01-001');
  });

  it('uses the outermost execution/ folder', async () => {
    const { project: projectRoot, root } = await project('union-with-csv', path.join('execution', 'nested', 'execution'));
    const read = await readDeliverableRecordedRegister({
      deliverablePath: path.join(root, 'PKG-02_Data', '1_Working', 'DEL-02-01_Consumer'),
      containmentRoot: projectRoot
    });
    expect(read.blockers.blockerState).toBe('NOT_ASSESSED');
    expect(read.blockers.notAssessedReason).toMatch(
      /^DELIVERABLE_OUTSIDE_EXECUTION_ROOT: .* for the execution root execution; no verdict is given$/
    );
  });

  it('keeps the verdict when the project is reached through an aliased path', async () => {
    const { project: projectRoot, root } = await project('union-with-csv', 'execution');
    const unit = path.join(root, 'PKG-02_Data', '1_Working', 'DEL-02-01_Consumer');
    const direct = await readDeliverableRecordedRegister({ deliverablePath: unit, containmentRoot: projectRoot });
    const alias = path.join(path.dirname(projectRoot), 'alias');
    await symlink(projectRoot, alias, 'dir');
    const aliased = await readDeliverableRecordedRegister({
      deliverablePath: path.join(alias, 'execution', 'PKG-02_Data', '1_Working', 'DEL-02-01_Consumer'),
      containmentRoot: projectRoot
    });
    expect(direct.blockers.blockerState).not.toBe('NOT_ASSESSED');
    expect(aliased.blockers).toEqual(direct.blockers);

    // So does an execution root named through the alias.
    const named = await readDeliverableRecordedRegister({
      deliverablePath: path.join(alias, 'execution', 'PKG-02_Data', '1_Working', 'DEL-02-01_Consumer'),
      containmentRoot: alias,
      executionRoot: path.join(alias, 'execution')
    });
    expect(named.blockers).toEqual(direct.blockers);
    expect(named.executionRoot).toBe(root);
  });

  it('gives no verdict when an adapter manifest implies another execution root', async () => {
    const { project: projectRoot, root } = await project('union-with-csv', path.join('app', 'execution'));
    await writeAdapter(projectRoot);
    const read = await readDeliverableRecordedRegister({
      deliverablePath: path.join(root, 'PKG-02_Data', '1_Working', 'DEL-02-01_Consumer'),
      containmentRoot: projectRoot
    });
    expect(read.executionRoot).toBeNull();
    expect(read.blockers.blockerState).toBe('NOT_ASSESSED');
    expect(read.blockers.notAssessedReason).toBe(
      "EXECUTION_ROOT_NOT_RESOLVED: adapter manifest _harness/adapter.yaml implies execution root execution, but the deliverable's execution root is app/execution; no verdict is given"
    );
    expect(read.warnings).toEqual([read.blockers.notAssessedReason]);

    // The same layout with the manifest beside its execution root is judged.
    await rm(path.join(projectRoot, '_harness'), { recursive: true });
    await writeAdapter(path.join(projectRoot, 'app'));
    const agreed = await readDeliverableRecordedRegister({
      deliverablePath: path.join(root, 'PKG-02_Data', '1_Working', 'DEL-02-01_Consumer'),
      containmentRoot: projectRoot
    });
    expect(agreed.executionRoot).toBe(root);
    expect(agreed.blockers.blockerState).toBe('BLOCKED');
  });
});

describe('held arcs', () => {
  const id = (index: number): string => `DEL-${String(index).padStart(6, '0')}`;

  it('finds cycles without recursion on a 12,000-arc chain', () => {
    const chain: Array<[string, string]> = [];
    for (let index = 0; index < 12000; index += 1) {
      chain.push([id(index), id(index + 1)]);
    }
    expect(heldArcs(chain).size).toBe(0);

    const cycle: Array<[string, string]> = [...chain, [id(12000), id(0)]];
    expect(heldArcs(cycle).size).toBe(12001);
  });

  it('holds only the arcs inside a cycle, and self-loops', () => {
    const held = heldArcs([
      ['A', 'B'],
      ['B', 'C'],
      ['C', 'B'],
      ['C', 'D'],
      ['E', 'E']
    ]);
    expect([...held].map((key) => key.split('\u0000').join('->')).sort()).toEqual(['B->C', 'C->B', 'E->E']);
  });
});
