# D-PEC-52 — RULED: resizable table columns

**Status:** RULED 2026-07-09 — owner-directed execution
**Decision ID:** D-PEC-52

## Owner direction and verified UX gap

Owner direction of record (Ryan Tufts, in-session, 2026-07-09):

> “I do need to be able to grab and drag the column widths in all these tables though. Often the columns stretch beyond the limits of the screen.”

PEC currently provides sorting, filtering, CSV export, and selective horizontal
containment, but table columns have no direct width control. Several pages also
render table-shaped surfaces outside the shared register component, so a fix
limited to one page would leave inconsistent behavior.

## Ruled behavior

1. Every visible PEC `table.reg` surface uses the same resizable table wrapper.
2. A visible divider at each column boundary supports pointer drag with a
   practical minimum width; resizing must not trigger sorting or row actions.
3. Widths persist in browser session storage per table identity, with no server
   mutation and a double-click reset to automatic sizing.
4. Every table is horizontally contained inside its own region. Expanding a
   column may scroll that region but must never widen the application page.
5. Existing sorting, filters, row keyboard behavior, sticky first columns, CSV
   export, and narrow-screen layout remain intact.

## Exact fence

- `projects/pec/web/src/shared.tsx`
- `projects/pec/web/src/styles.css`
- `projects/pec/web/src/pages/Admin.tsx`
- `projects/pec/web/src/pages/Deliverables.tsx`
- `projects/pec/web/src/pages/LogHome.tsx`
- `projects/pec/web/src/pages/Plan.tsx`
- this packet, the PEC decision register, standing PEC workplan, and PEC loop
  receipt ledger

No database/API change, no new dependency, and no data or workflow mutation.
This follows the D-PEC-30 register-consistency precedent by implementing the
behavior once in the shared table primitive and migrating exceptions to it.

## Verification and rollback

- PEC typecheck/tests/build/drill.
- Browser drag, persistence, double-click reset, sort non-interference, local
  horizontal scroll, and page-level no-overflow checks on Packages,
  Deliverables, Disciplines, Registers, Plan, and Admin at desktop and 390px.
- Self-check, coord-check, and `git diff --check`.
- Rollback by reverting this isolated source tranche; no data rollback exists.

## Human ruling

**RULED:** direct owner instruction authorizes resizable, locally contained
columns across all PEC tables inside the fence above.
