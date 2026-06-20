import { fileURLToPath } from 'node:url';
import path from 'node:path';
import { describe, expect, it } from 'vitest';
import {
  MATRIX_ROWS,
  isMatrixLaunchBlockedByStreaming,
  matrixCellLaunchKind,
  type MatrixCell
} from '../../lib/portal/agent-matrix-cells';
import { resolvePersona } from '../../lib/shell/persona-resolution';
import { listAgentRoster } from '../../lib/harness/agent-roster';

// Resolve the real instruction root (repo root) deterministically from this
// test file's location — independent of cwd — so the guard checks the matrix
// targets against the actual on-disk agent roster.
const HERE = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(HERE, '..', '..', '..', '..', '..', '..');

const ALL_CELLS: MatrixCell[] = MATRIX_ROWS.flatMap((row) => row.cells);

function loopAgentParam(target: string): string | null {
  if (!target.startsWith('/?')) {
    return null;
  }
  const query = target.includes('?') ? target.slice(target.indexOf('?') + 1) : '';
  return new URLSearchParams(query).get('agent');
}

describe('agent matrix cell wiring', () => {
  it('encodes NORMATIVE/EVALUATIVE persona intent and OPERATIVE Pipeline intent', () => {
    for (const cell of ALL_CELLS) {
      if (cell.row === 'OPERATIVE') {
        expect(cell.target.startsWith('/pipeline')).toBe(true);
        expect(matrixCellLaunchKind(cell)).toBe('route');
      } else {
        expect(cell.target.startsWith('/?agent=')).toBe(true);
        expect(matrixCellLaunchKind(cell)).toBe('loop-persona');
      }
    }
  });

  it('GUARD: every loop-persona matrix target resolves to a Type-0/Type-1 persona on disk', async () => {
    const roster = await listAgentRoster(REPO_ROOT);
    expect(roster.length).toBeGreaterThan(0);
    const typeByName = new Map(roster.map((entry) => [entry.name, entry.type]));

    const loopPersonaCells = ALL_CELLS.filter((cell) => matrixCellLaunchKind(cell) === 'loop-persona');
    // Sanity: there really are loop-persona cells to check (NORMATIVE + EVALUATIVE).
    expect(loopPersonaCells.length).toBeGreaterThanOrEqual(8);

    for (const cell of loopPersonaCells) {
      const rawAgent = loopAgentParam(cell.target);
      expect(rawAgent, `cell ${cell.row}/${cell.column} missing ?agent=`).toBeTruthy();

      const persona = resolvePersona(rawAgent);
      const type = typeByName.get(persona);

      // The persona must exist on disk...
      expect(
        typeByName.has(persona),
        `cell ${cell.row}/${cell.column} (label ${cell.label}, agent ${rawAgent}) resolves to ${persona}, which has no AGENT_${persona}.md`
      ).toBe(true);

      // ...and must be Type-0 or Type-1 (never a Type-2 task agent booted as a
      // top-level loop persona session — D-APP-24 / the AGGREGATE regression class).
      expect(
        type === 0 || type === 1,
        `cell ${cell.row}/${cell.column} (label ${cell.label}) resolves to ${persona} of type ${String(type)}; loop persona cells must be Type-0/Type-1`
      ).toBe(true);
    }
  });

  it('re-points the NORMATIVE/REVIEWING cell at the REVIEW persona (was the Type-2 AGGREGATION)', () => {
    const cell = ALL_CELLS.find((c) => c.row === 'NORMATIVE' && c.column === 'REVIEWING');
    expect(cell?.label).toBe('REVIEW');
    expect(loopAgentParam(cell?.target ?? '')).toBe('REVIEW');
  });

  it('blocks all matrix launches while the mounted loop is streaming', () => {
    expect(isMatrixLaunchBlockedByStreaming(false)).toBe(false);
    expect(isMatrixLaunchBlockedByStreaming(true)).toBe(true);
  });
});
