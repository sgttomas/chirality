# D-PEC-24 - PROPOSAL: design-system and accessibility foundation

**Status:** AWAITING_RULING.
**Date prepared:** 2026-07-08
**Decision ID:** D-PEC-24
**Prepared by:** PEC work loop agent. The ruling act is the owner's
(K-AUTH-1; D-GOV-04). Packet form follows the D-PEC-20 source-tranche
packet precedent: verified current state, decision to rule, exact fence,
options, verification plan, rollback, and open human ruling.

> **Epistemic status: agent-prepared source-tranche packet, not authority.**
> It proposes a bounded source tranche under the adopted PEC UI/UX redesign
> standing plan. Source execution remains prohibited unless and until the owner
> rules this packet. Sources govern on any disagreement.

## Why this row exists

The adopted standing plan names D-PEC-24 as the first redesign implementation
tranche and the prerequisite for the drill spine and later page work:
`_DomainEngines/pec/WORKPLAN_2026-07-08_pec_uiux_redesign.md` roadmap row
"D-PEC-24 - Design-system & a11y foundation." The T0 design specification
then pins the live details in
`projects/pec/execution/_Coordination/DESIGN_SPEC_2026-07-08_uiux_redesign.md`
sections 2.1-2.5, 11A/E20, and 14.

This row exists to ask whether the owner authorizes that bounded source
tranche: design tokens, shell accessibility, keyboard-operable shared
affordances, and navigation shell improvements. It does not authorize D-PEC-25
RecordRef/drill-spine work or any page-specific redesign.

## Verified current state

| Fact | Source |
|---|---|
| Sidebar is eight flat links: Overview, Packages, Deliverables, Plan, Action & Hold Log, My Week, Registers, Admin. | `projects/pec/web/src/main.tsx:96-107` |
| Project switcher always navigates to `/overview`, discarding the current lens. | `projects/pec/web/src/main.tsx:112-115` |
| Sign-out is an anchor with inline hex color, not a button. | `projects/pec/web/src/main.tsx:120` |
| `KpiCard` is a clickable `div`, not a keyboard-operable button. | `projects/pec/web/src/shared.tsx:163-170` |
| `Drawer` lacks dialog semantics, focus trap, and focus restore. | `projects/pec/web/src/shared.tsx:175-190` |
| T0 confirms the token migration scope as 64 hex literals in `styles.css` plus 2 inline TSX hex literals. | `DESIGN_SPEC_2026-07-08_uiux_redesign.md` §1.3 D5 and §11A/E20 |
| T0 states no global focus styles exist and requires `:focus-visible`. | `DESIGN_SPEC_2026-07-08_uiux_redesign.md` §2.5 |
| Dark mode is explicitly conditional on open redesign slate item 6; the token layer lands regardless. | `DESIGN_SPEC_2026-07-08_uiux_redesign.md` §2.4 and §14 item 6 |

## Decision to rule

Whether to authorize one source tranche implementing the D-PEC-24 foundation:

1. **Token layer:** migrate all existing color use in the fence to primitive
   palette tokens plus semantic tokens (`--surface`, `--text`,
   `--text-muted`, `--border`, `--accent`, status/severity/badge roles).
   No new runtime or web dependency.
2. **Focus and contrast:** add global `:focus-visible`; raise amber/green
   badge contrast to AA target; preserve the existing dense operational
   aesthetic, not a marketing restyle.
3. **Drawer accessibility:** convert `Drawer` to a real modal dialog with
   `role="dialog"`, `aria-modal`, Esc close, focus trap, and focus restore.
4. **Keyboard affordances:** make `KpiCard` keyboard-operable as a button;
   make shared row/reflink affordance styling support real buttons/links
   without layout shift.
5. **Shell navigation:** group sidebar links into the six working lenses and
   the Registers/Admin control surfaces; preserve the current lens when
   switching projects; make Sign out a real button.
6. **Breadcrumb primitive:** add a shared breadcrumb component as specified in
   T0 §2.2. Consumers may land in later packets; this tranche only supplies
   the primitive.
7. **Dark mode:** only if the owner selects the dark-mode option below, add
   `prefers-color-scheme`, `:root[data-theme]`, and persisted theme selection
   over the same semantic tokens. No component-level theme forks.

**Not in scope:** D-PEC-25 `RecordRef`; page-level Admin/Log/Plan/Package/
Deliverable redesign; server routes; core model changes; import behavior;
role-assignment routes; any new dependency; any lifecycle/status mutation; any
database mutation.

## Fence (exact; STOP outside it)

- `projects/pec/web/src/styles.css`
- `projects/pec/web/src/shared.tsx`
- `projects/pec/web/src/main.tsx`

No `server/**`, no `core/**`, no `agent-sidecar/**`, no root manifests, no
database files, no profile, no decision/register file edits during execution
except the post-run receipt.

## Options

- **O-A (recommended):** authorize items 1-6, defer the dark-mode toggle.
  This ships the prerequisite foundation with the smallest reporting-first
  scope and leaves slate item 6 available for a later explicit ruling.
- **O-B:** authorize items 1-7, including dark mode in this tranche.
- **O-C:** defer D-PEC-24.

## Verification plan (workplan step-4 bar)

- PEC belt-and-braces: `npm run typecheck && npm test && npm run build &&
  npm run drill`.
- Browser visual pass on changed surfaces at about 1280 px desktop and one
  narrow/mobile viewport: no blank pages, overflow, overlap, or unreadable
  contrast; sidebar grouping and project switching verified.
- Keyboard pass: Tab reaches shell actions and KPI cards; Enter/Space operate
  `KpiCard`; Drawer traps focus, closes with Esc, and restores focus.
- Scope containment: `git diff --name-only` is a subset of the fence above.
- Repo checks: `PYTHONDONTWRITEBYTECODE=1 python3
  tools/practitioner_harness/harness.py self-check`, coord-check on the branch
  diff, `git diff --check`.
- Adversarial review of citations, fence containment, no new dependencies, and
  no silent activation of dark mode unless O-B is ruled.

## Rollback

Single revert of the source tranche commit(s). Because the tranche adds no
runtime dependency and no schema/data migration, rollback restores the prior
shell and shared component behavior.

## Human ruling

AWAITING_RULING. No source implementation is authorized by this packet until
the owner records a ruling.
