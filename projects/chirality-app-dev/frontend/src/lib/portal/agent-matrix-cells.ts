/**
 * Pure data for the portal agent matrix, extracted from `agent-matrix.tsx` so it
 * is importable in the node-env test runner without pulling in the client
 * component. The matrix convention (rendered in the component header):
 *
 *   NORMATIVE / EVALUATIVE cells  → `/workbench?agent=…`  (Type-0/Type-1 personas)
 *   OPERATIVE cells (marked `*`)  → `/pipeline?category=…` (Type-2 task work)
 *
 * A mechanical guard (`agent-matrix-cells.test.ts`) asserts every
 * `/workbench?agent=` target resolves (through `resolvePersona`) to a roster
 * entry whose type is 0 or 1, so a Type-2 task agent can never again be wired to
 * boot as a direct `/workbench` persona session.
 */

export type MatrixCell = {
  row: 'NORMATIVE' | 'OPERATIVE' | 'EVALUATIVE';
  column: 'GUIDING' | 'APPLYING' | 'JUDGING' | 'REVIEWING';
  label: string;
  target: string;
};

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
        target: '/workbench?agent=HELP&row=NORMATIVE&column=GUIDING'
      },
      {
        row: 'NORMATIVE',
        column: 'APPLYING',
        label: 'ORCHESTRATE',
        target: '/workbench?agent=ORCHESTRATE&row=NORMATIVE&column=APPLYING'
      },
      {
        row: 'NORMATIVE',
        column: 'JUDGING',
        label: 'WORKING_ITEMS',
        target: '/workbench?agent=WORKING_ITEMS&row=NORMATIVE&column=JUDGING'
      },
      {
        // Re-pointed from the Type-2 TASK agent AGGREGATION to the Type-1 REVIEW
        // persona: NORMATIVE cells boot `/workbench` persona sessions, and
        // Type-2 task agents run only via the orchestrated path (D-APP-24).
        row: 'NORMATIVE',
        column: 'REVIEWING',
        label: 'REVIEW',
        target: '/workbench?agent=REVIEW&row=NORMATIVE&column=REVIEWING'
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
        target: '/workbench?agent=AGENTS&row=EVALUATIVE&column=GUIDING'
      },
      {
        row: 'EVALUATIVE',
        column: 'APPLYING',
        label: 'DEPENDENCIES',
        target: '/workbench?agent=DEPENDENCIES&row=EVALUATIVE&column=APPLYING'
      },
      {
        row: 'EVALUATIVE',
        column: 'JUDGING',
        label: 'CHANGE',
        target: '/workbench?agent=CHANGE&row=EVALUATIVE&column=JUDGING'
      },
      {
        row: 'EVALUATIVE',
        column: 'REVIEWING',
        label: 'RESEARCH',
        target: '/workbench?agent=RESEARCH&row=EVALUATIVE&column=REVIEWING'
      }
    ]
  }
];
