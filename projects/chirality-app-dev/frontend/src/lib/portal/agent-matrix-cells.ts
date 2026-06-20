/**
 * Pure data for the portal agent matrix, extracted from `agent-matrix.tsx` so it
 * is importable in the node-env test runner without pulling in the client
 * component. The matrix convention (rendered in the component header):
 *
 *   NORMATIVE / EVALUATIVE cells  → `/?agent=…`             (mounted loop persona swap)
 *   OPERATIVE cells (marked `*`)  → `/pipeline?category=…`  (Type-2 task work)
 *
 * A mechanical guard (`agent-matrix-cells.test.ts`) asserts every
 * loop-persona target resolves (through `resolvePersona`) to a roster
 * entry whose type is 0 or 1, so a Type-2 task agent can never again be wired to
 * boot as a top-level loop persona session.
 */

export type MatrixCell = {
  row: 'NORMATIVE' | 'OPERATIVE' | 'EVALUATIVE';
  column: 'GUIDING' | 'APPLYING' | 'JUDGING' | 'REVIEWING';
  label: string;
  target: string;
};

export type MatrixCellLaunchKind = 'loop-persona' | 'route';

function buildLoopPersonaTarget(
  agent: string,
  row: MatrixCell['row'],
  column: MatrixCell['column']
): string {
  const params = new URLSearchParams({ agent, row, column });
  return `/?${params.toString()}`;
}

export function matrixCellLaunchKind(cell: MatrixCell): MatrixCellLaunchKind {
  return cell.row === 'OPERATIVE' ? 'route' : 'loop-persona';
}

export function isMatrixLaunchBlockedByStreaming(streaming: boolean): boolean {
  return streaming;
}

export const MATRIX_ROWS: Array<{
  rowLabel: MatrixCell['row'];
  cells: MatrixCell[];
}> = [
  {
    rowLabel: 'NORMATIVE',
    cells: [
      {
        row: 'NORMATIVE',
        column: 'GUIDING',
        label: 'HELP',
        target: buildLoopPersonaTarget('HELP', 'NORMATIVE', 'GUIDING')
      },
      {
        row: 'NORMATIVE',
        column: 'APPLYING',
        label: 'ORCHESTRATE',
        target: buildLoopPersonaTarget('ORCHESTRATE', 'NORMATIVE', 'APPLYING')
      },
      {
        row: 'NORMATIVE',
        column: 'JUDGING',
        label: 'WORKING_ITEMS',
        target: buildLoopPersonaTarget('WORKING_ITEMS', 'NORMATIVE', 'JUDGING')
      },
      {
        // Re-pointed from the Type-2 TASK agent AGGREGATION to the Type-1
        // REVIEW persona: NORMATIVE cells boot top-level loop persona sessions,
        // and Type-2 task agents run only via the orchestrated path (D-APP-24).
        row: 'NORMATIVE',
        column: 'REVIEWING',
        label: 'REVIEW',
        target: buildLoopPersonaTarget('REVIEW', 'NORMATIVE', 'REVIEWING')
      }
    ]
  },
  {
    rowLabel: 'OPERATIVE',
    cells: [
      {
        row: 'OPERATIVE',
        column: 'GUIDING',
        label: 'DECOMP*',
        target: '/pipeline?category=DECOMP'
      },
      {
        row: 'OPERATIVE',
        column: 'APPLYING',
        label: 'PREP*',
        target: '/pipeline?category=PREP'
      },
      {
        row: 'OPERATIVE',
        column: 'JUDGING',
        label: 'TASK*',
        target: '/pipeline?category=TASK'
      },
      {
        row: 'OPERATIVE',
        column: 'REVIEWING',
        label: 'AUDIT*',
        target: '/pipeline?category=AUDIT'
      }
    ]
  },
  {
    rowLabel: 'EVALUATIVE',
    cells: [
      {
        row: 'EVALUATIVE',
        column: 'GUIDING',
        label: 'AGENTS',
        target: buildLoopPersonaTarget('AGENTS', 'EVALUATIVE', 'GUIDING')
      },
      {
        row: 'EVALUATIVE',
        column: 'APPLYING',
        label: 'DEPENDENCIES',
        target: buildLoopPersonaTarget('DEPENDENCIES', 'EVALUATIVE', 'APPLYING')
      },
      {
        row: 'EVALUATIVE',
        column: 'JUDGING',
        label: 'CHANGE',
        target: buildLoopPersonaTarget('CHANGE', 'EVALUATIVE', 'JUDGING')
      },
      {
        row: 'EVALUATIVE',
        column: 'REVIEWING',
        label: 'RESEARCH',
        target: buildLoopPersonaTarget('RESEARCH', 'EVALUATIVE', 'REVIEWING')
      }
    ]
  }
];
