import { fileURLToPath } from 'node:url';
import path from 'node:path';
import { describe, expect, it } from 'vitest';
import { MATRIX_ROWS, type MatrixCell } from '../../lib/portal/agent-matrix-cells';
import { resolvePersona } from '../../lib/shell/persona-resolution';
import { listAgentRoster } from '../../lib/harness/agent-roster';

// Resolve the real instruction root (repo root) deterministically from this
// test file's location — independent of cwd — so the guard checks the matrix
// targets against the actual on-disk agent roster.
const HERE = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(HERE, '..', '..', '..', '..', '..', '..');

const ALL_CELLS: MatrixCell[] = MATRIX_ROWS.flatMap((row) => row.cells);

function workbenchAgentParam(target: string): string | null {
  if (!target.startsWith('/workbench')) {
    return null;
  }
  const query = target.includes('?') ? target.slice(target.indexOf('?') + 1) : '';
  return new URLSearchParams(query).get('agent');
}

describe('agent matrix cell wiring', () => {
  it('routes NORMATIVE/EVALUATIVE cells to /workbench and OPERATIVE cells to /pipeline', () => {
    for (const cell of ALL_CELLS) {
      if (cell.row === 'OPERATIVE') {
        expect(cell.target.startsWith('/pipeline')).toBe(true);
      } else {
        expect(cell.target.startsWith('/workbench?agent=')).toBe(true);
      }
    }
  });

  it('GUARD: every /workbench matrix target resolves to a Type-0/Type-1 persona on disk', async () => {
    const roster = await listAgentRoster(REPO_ROOT);
    expect(roster.length).toBeGreaterThan(0);
    const typeByName = new Map(roster.map((entry) => [entry.name, entry.type]));

    const workbenchCells = ALL_CELLS.filter((cell) => cell.target.startsWith('/workbench'));
    // Sanity: there really are workbench cells to check (NORMATIVE + EVALUATIVE).
    expect(workbenchCells.length).toBeGreaterThanOrEqual(8);

    for (const cell of workbenchCells) {
      const rawAgent = workbenchAgentParam(cell.target);
      expect(rawAgent, `cell ${cell.row}/${cell.column} missing ?agent=`).toBeTruthy();

      const persona = resolvePersona(rawAgent);
      const type = typeByName.get(persona);

      // The persona must exist on disk...
      expect(
        typeByName.has(persona),
        `cell ${cell.row}/${cell.column} (label ${cell.label}, agent ${rawAgent}) resolves to ${persona}, which has no AGENT_${persona}.md`
      ).toBe(true);

      // ...and must be Type-0 or Type-1 (never a Type-2 task agent booted as a
      // /workbench persona session — D-APP-24 / the AGGREGATE regression class).
      expect(
        type === 0 || type === 1,
        `cell ${cell.row}/${cell.column} (label ${cell.label}) resolves to ${persona} of type ${String(type)}; /workbench cells must be Type-0/Type-1`
      ).toBe(true);
    }
  });

  it('re-points the NORMATIVE/REVIEWING cell at the REVIEW persona (was the Type-2 AGGREGATION)', () => {
    const cell = ALL_CELLS.find((c) => c.row === 'NORMATIVE' && c.column === 'REVIEWING');
    expect(cell?.label).toBe('REVIEW');
    expect(workbenchAgentParam(cell?.target ?? '')).toBe('REVIEW');
  });
});
