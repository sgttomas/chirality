import { existsSync, readFileSync } from 'node:fs';
import { mkdir, mkdtemp, readFile, realpath, rm, symlink, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { afterAll, describe, expect, it } from 'vitest';
import {
  AMENDMENT_REOPEN_REFUSAL_CODES,
  ROOT_ONLY_REFUSAL_CODES,
  AmendmentReopenUsageError,
  checkAmendmentReopen
} from '../../lib/lifecycle/amendment-reopen';

// Shared inputs and the Root checker's working-tree decisions, written by
// fixtures/amendment-reopen/generate_expected.py from
// tools/validation/check_amendment_reopen.py.
const FIXTURE_DIR = fileURLToPath(new URL('../fixtures/amendment-reopen/', import.meta.url));
// fixtures/amendment-reopen -> fixtures, __tests__, src, frontend, chirality-app-dev, projects, repository.
const REPO_ROOT = path.resolve(FIXTURE_DIR, '../../../../../../..');

type Query = {
  deliverable: string;
  deliverableIsPath: boolean;
  amendment: string;
  amendmentIsPath: boolean;
  scopeChangeRoot: string | null;
  projectRoot: string;
  cwd: string;
  /** The deliverable's `_STATUS.md`: the Root checker's `--status-file`, passed to the App as text. */
  statusFile: string | null;
};
type Tree = { files: Record<string, string>; symlinks: Record<string, string>; dirs: string[] };
type Cases = {
  fixtures: { name: string; tree: Tree; queries: Query[] }[];
  real: { name: string; requires: string[]; queries: Query[] }[];
};
type Expected = {
  fixtures: Record<string, Record<string, unknown>[]>;
  real: Record<string, Record<string, unknown>[] | null>;
};

const cases = JSON.parse(readFileSync(path.join(FIXTURE_DIR, 'cases.json'), 'utf8')) as Cases;
const expected = JSON.parse(readFileSync(path.join(FIXTURE_DIR, 'expected.json'), 'utf8')) as Expected;

const tmpRoots: string[] = [];

afterAll(async () => {
  await Promise.all(tmpRoots.map((root) => rm(root, { recursive: true, force: true })));
});

async function materialize(tree: Tree): Promise<string> {
  const root = await mkdtemp(path.join(os.tmpdir(), 'amendment-reopen-parity-'));
  tmpRoots.push(root);
  for (const dir of tree.dirs) {
    await mkdir(path.join(root, dir), { recursive: true });
  }
  for (const [rel, text] of Object.entries(tree.files)) {
    const target = path.join(root, rel);
    await mkdir(path.dirname(target), { recursive: true });
    await writeFile(target, text, 'utf8');
  }
  for (const [rel, target] of Object.entries(tree.symlinks)) {
    const link = path.join(root, rel);
    await mkdir(path.dirname(link), { recursive: true });
    await symlink(target, link);
  }
  return root;
}

async function readStatusText(file: string): Promise<string> {
  // Python read_text(encoding="utf-8-sig"): strict UTF-8, one leading BOM removed.
  return new TextDecoder('utf-8', { fatal: true }).decode(await readFile(file));
}

async function run(query: Query, root: string): Promise<Record<string, unknown>> {
  let statusText: string | undefined;
  if (query.statusFile !== null) {
    try {
      statusText = await readStatusText(path.join(root, query.statusFile));
    } catch {
      return { usageError: true };
    }
  }
  try {
    const decision = await checkAmendmentReopen(
      query.deliverableIsPath ? path.join(root, query.deliverable) : query.deliverable,
      query.amendmentIsPath ? path.join(root, query.amendment) : query.amendment,
      {
        projectRoot: path.join(root, query.projectRoot),
        cwd: path.join(root, query.cwd),
        ...(statusText !== undefined ? { statusText } : {}),
        ...(query.scopeChangeRoot !== null
          ? { scopeChangeRoot: path.join(root, query.scopeChangeRoot) }
          : {})
      }
    );
    let reason = decision.reason;
    const prefixes = [...new Set([root, await realpath(root)])].sort((a, b) => b.length - a.length);
    for (const prefix of prefixes) {
      reason = reason.split(prefix).join('<ROOT>');
    }
    return { ...decision, reason };
  } catch (error) {
    if (error instanceof AmendmentReopenUsageError) {
      return { usageError: true };
    }
    throw error;
  }
}

describe('amendment reopen checker parity with tools/validation/check_amendment_reopen.py', () => {
  it('covers every fixture and real case the generator recorded', () => {
    expect(Object.keys(expected.fixtures).sort()).toEqual(cases.fixtures.map((item) => item.name).sort());
    expect(Object.keys(expected.real).sort()).toEqual(cases.real.map((item) => item.name).sort());
  });

  it('exercises every refusal code and the admitted outcome', () => {
    const codes = new Set(
      Object.values(expected.fixtures)
        .flat()
        .map((result) => result.code)
        .filter(Boolean)
    );
    expect([...codes].sort()).toEqual(['ADMITTED', ...AMENDMENT_REOPEN_REFUSAL_CODES].sort());
  });

  it('mirrors the Root REFUSAL_CODES less the at-commit codes (skipped when the Root checker is absent)', () => {
    const checker = path.join(REPO_ROOT, 'tools', 'validation', 'check_amendment_reopen.py');
    if (!existsSync(checker)) {
      return;
    }
    const source = readFileSync(checker, 'utf8');
    const tuple = /^REFUSAL_CODES = \(([\s\S]*?)^\)/m.exec(source)?.[1] ?? '';
    const rootCodes = [...tuple.matchAll(/^\s+([A-Z0-9_]+),/gm)].map((match) => match[1]);
    expect(rootCodes.length).toBeGreaterThan(0);
    expect([...AMENDMENT_REOPEN_REFUSAL_CODES, ...ROOT_ONLY_REFUSAL_CODES].sort()).toEqual([...rootCodes].sort());
  });

  it.each(cases.fixtures.map((item) => [item.name, item] as const))(
    'fixture %s decides as the Root checker does',
    async (name, item) => {
      const root = await materialize(item.tree);
      const results = [];
      for (const query of item.queries) {
        results.push(await run(query, root));
      }
      expect(results).toEqual(expected.fixtures[name]);
    }
  );

  it.each(cases.real.map((item) => [item.name, item] as const))(
    'real records %s decide as the Root checker does (skipped when absent)',
    async (name, item) => {
      const recorded = expected.real[name];
      const present = item.requires.every((rel) => existsSync(path.join(REPO_ROOT, rel)));
      if (!present || recorded === null) {
        return;
      }
      const results = [];
      for (const query of item.queries) {
        results.push(await run(query, REPO_ROOT));
      }
      expect(results).toEqual(recorded);
    }
  );
});
