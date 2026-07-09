# D-PEC-30 - PROPOSAL: Registers consistency

**Status:** AWAITING_RULING.
**Date prepared:** 2026-07-09
**Decision ID:** D-PEC-30
**Prepared by:** PEC work loop agent. The ruling act is the owner's
(K-AUTH-1; D-GOV-04). Packet form follows the D-PEC-20 source-tranche
packet precedent: verified current state, decision to rule, exact fence,
options, verification plan, rollback, and open human ruling.

> **Epistemic status: agent-prepared source-tranche packet, not authority.**
> It proposes a bounded source tranche under the adopted reporting-first PEC
> UI/UX redesign plan. Source execution remains prohibited unless and until the
> owner rules this packet. Sources govern on any disagreement.

## Why this row exists

The standing plan places Registers consistency after the reporting foundation:
D-PEC-24/25/27/29/26 first, then D-PEC-30/31 polish, then upload/reporting
lanes. Registers are the authoritative typed record surfaces, but the page
still has uneven tab semantics, inconsistent read-only signaling, a wide-table
layout risk, a `window.prompt` hold-withdraw path, and Schedule/Tracker parity
gaps.

The T0 design specification pins the scope in
`projects/pec/execution/_Coordination/DESIGN_SPEC_2026-07-08_uiux_redesign.md`
§9 and §11A E10/E20. D-PEC-38 repaired the shared generic RegisterTable row
keyboard path on this branch; D-PEC-30 should build on that repair, not redo it.

## Dependencies

D-PEC-30 source execution depends on D-PEC-24 and D-PEC-25 being ruled and
executed. Because this packet was prepared while D-PEC-38 source execution was
still branch-local, execution should start only after the D-PEC-38 closeout PR
is merged or the branch is rebased onto its final source state.

## Verified current state (live tree, 2026-07-09)

| Fact | Source |
|---|---|
| Registers tabs are rendered from `TABS` with Schedule and Tracker present, but the tab bar has no `role="tablist"` or `aria-selected` semantics. | `web/src/pages/Registers.tsx:18-48` |
| RegisterTable now supports keyboard row activation on this D-PEC-38 branch; D-PEC-30 should preserve it. | `web/src/shared.tsx:409-421` |
| Schedule and Tracker tabs are read-only and use `RegisterTable`, but Schedule has no `highlightRef`/row ref parity. | `web/src/pages/Registers.tsx:937-1035` |
| Hold withdraw still uses `window.prompt`. | `web/src/pages/Registers.tsx:1065` |
| The design spec calls for sticky/wide-register treatment and optional per-tab summary strips over existing loaded rows. | `DESIGN_SPEC_2026-07-08_uiux_redesign.md` §9 M9.1-M9.8 |

## Decision to rule

Whether to authorize one source tranche implementing D-PEC-30:

1. Add accessible tab semantics to Registers: `role="tablist"`, tab buttons or
   links with `role="tab"`, `aria-selected`, and visible grouping/marking for
   read-only Schedule and Tracker tabs.
2. Unify row-actionability cues: rows that open a drawer or route should read
   as actionable by mouse and keyboard; read-only rows should not imply
   mutation or hidden actions.
3. Add wide-register containment for Schedule/Tracker/other wide tabs:
   horizontal overflow inside the register region, stable column sizing, and a
   sticky Ref/source column where supported without breaking narrow viewports.
4. Replace hold-withdraw `window.prompt` with the existing Drawer/form pattern,
   preserving the existing server mutation and audit semantics.
5. Bring Schedule tab closer to Tracker parity: import-owned/read-only
   statement, agent context where relevant, deep-link/highlight support where
   rows expose a stable ref, and package/deliverable cells using existing
   route/drill affordances where resolvable.
6. Refresh the file/page docstring and any stale "five registers" copy so the
   page describes the live seven-tab register set honestly.
7. Optional under O-B only: add per-tab summary strips using display
   aggregation over the loaded rows, with export-what-is-displayed preserved.

**Not in scope:** bulk edit; new register mutations; Schedule/Tracker edit
paths; schema/model changes; new dependencies; import behavior changes;
D-PEC-32 issue-model completeness; professional/go-live claims.

## Fence (exact; STOP outside it)

- `projects/pec/web/src/pages/Registers.tsx`
- `projects/pec/web/src/shared.tsx`

No `server/**`, no `core/**`, no database files, no root manifests, no
profile, no import templates, no other page source edits, and no
decision/register file edits during execution except the post-run receipt.

## Options

- **O-A (recommended):** items 1-6 above; no per-tab summary strips.
- **O-B:** O-A plus item 7, lightweight per-tab summary strips over already
  loaded rows.
- **O-C:** minimal accessibility repair only: tab semantics plus prompt
  removal.
- **O-D:** defer D-PEC-30.

## Verification plan (workplan step-4 bar)

- PEC belt-and-braces: `npm run typecheck && npm test && npm run build &&
  npm run drill`.
- Browser visual pass on Registers at about 1280 px desktop and one
  narrow/mobile viewport: all tabs, wide Schedule/Tracker rows, no body
  overflow, no overlap.
- Keyboard pass: tablist traversal, Enter/Space row activation where
  actionable, focus visibility, Drawer open/close/escape for hold withdraw.
- Export pass: CSV export still works per tab and, under O-B, reflects the
  displayed filtered/summary context without inventing server truth.
- Scope containment: `git diff --name-only` is a subset of the ruled fence.
- Repo checks: `PYTHONDONTWRITEBYTECODE=1 python3
  tools/practitioner_harness/harness.py self-check`, coord-check on the branch
  diff, `git diff --check`.
- Adversarial review: no import-owned Schedule/Tracker mutation slipped in; no
  row is presented as actionable when no action exists.

## Rollback

Single revert of the source tranche commit(s). No schema, data, dependency, or
runtime rollback is needed.

## Human ruling

AWAITING_RULING.
