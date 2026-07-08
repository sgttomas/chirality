# D-PEC-24 - PROPOSAL: design-system & a11y foundation source tranche (UI/UX redesign tranche 1)

**Status:** AWAITING_RULING.
**Date prepared:** 2026-07-08
**Decision ID:** D-PEC-24 (first packet of the adopted redesign roadmap, standing plan P0 row)
**Prepared by:** PEC work loop agent. This packet is a PROPOSAL and confers no
authority; the ruling is the owner's act (K-AUTH-1; D-GOV-04).

Basis: the adopted standing plan
`_DomainEngines/pec/WORKPLAN_2026-07-08_pec_uiux_redesign.md` **as amended
2026-07-08 (reporting-first amendment, Receipt 60)** — its D-PEC-24 roadmap
row, design principles 1–10, and the redesign-phase fences corollary all bind
here — and the T0 design spec
`projects/pec/execution/_Coordination/DESIGN_SPEC_2026-07-08_uiux_redesign.md`
(**§2.1–§2.5** is this tranche's design authority; this packet cites its
section IDs instead of re-deriving design). Structure precedent: D-PEC-08 /
D-PEC-17 (source-tranche authorizations with exact fences); most recent form
D-PEC-23.

## Decision to rule

Whether to authorize the bounded source tranche implementing spec §2.1–§2.5
(global/shell design-system and accessibility foundation) at the exact file
fence below. First tranche of the ruled sequence: D-PEC-25/27/29/30 all touch
`shared.tsx` and queue behind this one (standing plan `shared.tsx` constraint —
sequential, never parallel).

## Scope (exactly the plan's D-PEC-24 row; spec section cited per item)

1. **Two-tier token layer (spec §2.4):** primitive-palette + semantic-role
   tokens; migrate the **64 hex literals in `web/src/styles.css` and 2 inline
   tsx hex** (spec §1.3 D5 live count — the full 64, not the operator's ~30)
   onto the layer. Pages keep emitting semantic classNames. Tokens land
   theme-ready unconditionally; the toggle is conditional (below).
2. **Global `:focus-visible` ring (spec §2.5):** none exists today.
3. **AA badge contrast (spec §2.5):** amber/green badge palette raised to AA
   (operator-verified ~3.1:1 / ~4.4:1 today).
4. **`Drawer` → real dialog (spec §2.5):** `role="dialog"`, `aria-modal`,
   focus trap, focus restore on close, Esc to close (shared.tsx:175-190).
5. **Keyboard operability (spec §2.5):** `KpiCard`, `RegisterTable` clickable
   rows (`onRowClick`), and the `.reflink` affordance become real
   `<button>`/`<a href>` — tab order, Enter/Space. (All three live in
   `shared.tsx`; verified by grep 2026-07-08.)
6. **Sidebar grouping (spec §2.1):** the 8 flat `NavLink`s (main.tsx:96-107)
   become two labeled groups — six lenses, then Registers · Admin. No route
   changes; no "Issues" rename.
7. **Breadcrumb primitive (spec §2.2):** new shared `<Breadcrumb>`
   (`<nav aria-label="breadcrumb">` of real links). **Primitive only** — its
   first consumers (Package/Deliverable detail) ride D-PEC-29's fence.
8. **Project switcher keeps lens; Sign-out a real button (spec §2.3):**
   switcher preserves the current lens path segment (today it discards it,
   main.tsx:112-118); Sign-out `<a href="#">` with inline hex (main.tsx:120)
   becomes a token-styled `<button>`.

**Out of scope (fence honesty):** drill re-wiring / `<RecordRef>` (spec §2.6 —
that is D-PEC-25); `role="tablist"` on the Registers/Admin tab bars (spec
§2.5's last bullet cross-references §9/§10 and rides the D-PEC-30/26 fences,
where those files open); breadcrumb consumers (D-PEC-29); any server, core,
schema, or behavior change. No computed value, rollup, threshold, or export
changes — this tranche is presentation and semantics only (fences-corollary
guarantees preserved; principle 10).

## Conditionals (open slate items — neither defaulted here)

- **Slate item 1 (zero-new-dependency posture) — OPEN.** This packet proceeds
  either way on the standing fences corollary ("zero new runtime/web
  dependencies" binds every tranche regardless): everything here is
  hand-written CSS + JSX; `package.json` unchanged is an acceptance check
  below. A later slate-1 ruling changes nothing in this tranche (spec §14
  row 1).
- **Slate item 6 (dark mode) — OPEN.** If the owner rules "now" (O-B below,
  or a separate ruling before execution), the token layer additionally ships
  the toggle: `prefers-color-scheme` default + `:root[data-theme]` semantic
  override + persisted preference, per spec §14 row 6 — same fence, no new
  file. If unruled or deferred, §2.4 tokens land theme-ready with **no
  toggle** and dark mode remains a later S-effort packet.

## Exact write fence (the only writable paths for this tranche)

| Path | Change |
|---|---|
| `projects/pec/web/src/styles.css` | Token layer (primitive + semantic tiers); 64-hex migration; global `:focus-visible`; AA badge palette; dialog/nav-group/breadcrumb/button styles. |
| `projects/pec/web/src/shared.tsx` | `Drawer` dialog semantics; `KpiCard`/row/`.reflink` keyboard operability; new `<Breadcrumb>` primitive. |
| `projects/pec/web/src/main.tsx` | Sidebar grouping; switcher lens preservation; Sign-out button; inline-hex migration (main.tsx:120). |
| `projects/pec/web/src/pages/LogHome.tsx` | ⚑ **One-line delta from the plan's indicative fence, flagged for the owner:** the second of spec D5's two inline tsx hex is `LogHome.tsx:398` (`background: '#fbfcfd'`), outside the three indicative files. Proposed: this single literal → token, nothing else in the file. Alternative if the owner strikes this row: defer that literal to D-PEC-27 (whose ruled fence includes `LogHome.tsx`) and this tranche completes 65 of 66 literals, stated in the receipt. |

Everything else stays closed — in particular `web/package.json` and all
manifests (zero new dependencies; F-PEC-3/ADR-002 posture), all other
`web/src/pages/**`, `server/**`, `core/**`, `tools/**`, and all DB files.
F-PEC-1 remains the outer fence; a ruling of this packet opens exactly the
rows above and nothing more (fences corollary). Coordination-surface writes
(this packet, the register row, the receipt) ride the standing carve-out, not
this fence.

## Dependencies

- **T0 design spec** — authored and merged; design authority for every scope
  item (cited by §-ID above). No other prerequisite.
- **Queued behind this tranche:** D-PEC-25, 27, 29, 30 (the `shared.tsx`
  sequence); D-PEC-24 is the ruled default first step
  (plan sequencing: 24 → 25 → 27 → 29 → 26 → 30/31 → PR lanes).

## Verification plan (standing plan step-4, pec-source checks verbatim, at the final PR SHA)

- pec belt-and-braces: `npm run typecheck && npm test && npm run build &&
  npm run drill` green.
- Visual pass on **every changed surface** at a ~1280px desktop viewport and
  one narrow/mobile viewport; keyboard operability of changed interactions;
  no blank pages/overflow/overlap.
- Always-checks: repo-wide `self-check` exit 0; `coord-check` on the branch
  diff; `git diff --check`; adversarial scope check — `git diff --name-only`
  ⊆ the fence table plus this packet, the register row, and the receipt.
- **Packet-specific acceptance:**
  - AA contrast spot-checks on the migrated badge/severity tokens (amber and
    green badges the named cases);
  - `Drawer` focus behavior demonstrated: trap while open, restore on close,
    Esc closes;
  - `KpiCard`/rows/reflinks reachable and operable by keyboard alone
    (Tab + Enter/Space) on at least one live surface each;
  - **zero new dependencies:** `package.json`/`package-lock.json` show no
    diff;
  - **no behavioral change beyond a11y/tokens:** no computed value, count,
    sort, route, or export output changes; rendered colors may shift only
    where the AA fix requires it, and the delta is named in the receipt.
- CI green; owner merges.

## Rollback

Single `git revert` of the tranche PR. Code-only, additive-or-in-place CSS/JSX
edits in four files; **no data, schema, migration, server, or API surface is
touched** — nothing to unwind anywhere else. If execution discovers a need
outside the fence, STOP: it returns as its own register row, never an in-run
widening (D-PEC-12 recorded interpretation).

## Options

| ID | Option | Consequence |
|---|---|---|
| O-A | **Authorize the tranche as fenced above** (dark mode NOT included; slate 6 stays open). | The foundation every later redesign tranche builds on lands as the smallest reviewable unit: tokens theme-ready, a11y floor in, shared primitives fixed once. The dark-mode toggle remains a cheap later packet over the same tokens (spec §14 row 6: "No other section depends on this"). |
| O-B | Same, **plus the dark-mode toggle** — this ruling also rules slate item 6 "now" in the same act. | Toggle + `data-theme` semantic swap + persisted preference ride the same fence and PR (spec §14 row 6). Slightly larger tranche and visual-pass matrix (every changed surface in both themes). |
| O-C | Decline / defer. | F-PEC-1 stays closed for these files; the redesign phase stalls at its first tranche — D-PEC-25/27/29/30 all queue behind this fence's `shared.tsx` work. |

## Recommendation (non-binding)

**O-A.** Dark mode is cleanly separable by the spec's own matrix, and the
smallest tranche keeps the first `shared.tsx` change maximally reviewable;
the tokens land theme-ready either way, so nothing is lost by ruling slate 6
later.

## The gate

**STOP.** No execution until the owner rules this packet (K-AUTH-1;
D-GOV-04). On a ruling: execute branch-first + PR at the ruled fence
(including the owner's disposition of the flagged `LogHome.tsx` row); never
self-merge; record the ruling verbatim here and in the register row; receipt
per the loop protocol.
