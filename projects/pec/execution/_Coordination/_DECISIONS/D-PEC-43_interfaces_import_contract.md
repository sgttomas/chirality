# D-PEC-43 - PROPOSAL: Interfaces import contract (TWD packages-interfaces workbook)

**Status:** RULED 2026-07-09 (O-A, limited)
**Date prepared:** 2026-07-09
**Decision ID:** D-PEC-43
**Prepared by:** PEC work loop agent. The ruling act is the owner's
(K-AUTH-1; D-GOV-04). Packet form follows the D-PEC-39/41 precedent.

> **Epistemic status: agent-prepared source-tranche packet, not authority.**
> It proposes the R2 "Interfaces import contract" row of the reporting-product
> standing plan, designed against the owner-provided TWD interfaces workbook.
> Source execution remains prohibited unless and until the owner rules this
> packet. The owner's 2026-07-09 merge pre-approval covers PR merges for
> already-ruled work; it is not a ruling on this packet.

## Why this row exists

The standing plan's R2 row "Interfaces import contract" was parked on a
Tier-P prerequisite: the interfaces document format. On 2026-07-09 the owner
provided it (ruling statement of record, Receipt 76: "I just added
`26020-Packages_Interfaces.3.xlsx` in the `inputs/` folder"). The product
interview records interfaces arriving "via a separately uploaded document"
(findings; workplan reconciliation 2). The owner's fidelity direction
(Receipt 75) applies: every provided column and sheet is captured losslessly;
display stays selective.

## Verified current state (live tree, 2026-07-09)

| Fact | Source |
|---|---|
| R2 row "Interfaces import contract": §16-style import contract + round-trip export for the owner's periodically uploaded interfaces document; fence `server/src/import/**`, `fixtures/**`, `server/test/**`, IMPORT_TEMPLATES docs; Tier-P prerequisite now satisfied. | `_DomainEngines/pec/WORKPLAN_2026-07-09_pec_reporting_product.md` (R2 row; Tier-P) |
| The interfaces file is present, owner-provided (gitignored). | `projects/pec/pilot-scratch/input/26020-Packages_Interfaces.3.xlsx`; Receipt 76 |
| RAIL v1 already accepts `type=interface` rows into `interface_item`; the MDL Data Dictionary records interface tags/notes enrichment sourced from this workbook. | `projects/pec/server/src/import/index.ts`; D-PEC-41 structure of record |

## Template structure of record (owner-provided TWD workbook)

Three sheets (structure and vocabulary only — no project row content):

1. **Packages** — a package × interface-category matrix. Columns: `Area #` ·
   `Package Number` · `Packages` (name) · `Discipline` · **18
   interface-category columns** (Process Piping · Utility Piping ·
   Relief / Flare / Vent · Drain / Containment · Electrical Power · EHT ·
   Grounding / Bonding · Area / Exterior Lighting · Cathodic Protection ·
   I&C / Control Cabling · Communications / Network · Building HVAC /
   Services · Fire & Gas / Safety Systems · Maintenance Access · Grading /
   Site Drainage / Spill Containment · Structural / Foundations / Supports ·
   Product Loading · Pipeline / Pigging; several header cells carry trailing
   spaces — normalized on read, captured verbatim) · `Interface Review
   Notes`. Matrix cells carry only the marker `X` (or blank); notes are
   free text on a minority of rows. 105 data rows observed.
2. **CoA Tracking Number** — tracking-number construction table: `Project
   Number_1` · `Project Number_2` · `Doc Type` · `CoA` · `Sequence` ·
   (unnamed composed column) · `CoA Tracking Number` · `Package Name` ·
   `Line Items` (multi-line cell) · `LSD (Area)`. 60 data rows observed.
   `CoA Tracking Number` values join to the RAIL v2 `CoA Tracking Number`
   column (D-PEC-41).
3. **CoA Master** — lookup: `CoA` (integer code) · `CoA Description`.
   33 data rows observed.

## Decision to rule

Whether to authorize one source tranche implementing the interfaces import
contract:

1. **Contract:** package-anchored interface facts from the Packages matrix —
   each `X` becomes an attested package-interface-category fact; `Interface
   Review Notes` captured verbatim; identity = `Package Number` +
   category; re-import updates idempotently under the existing
   import-ownership guard. Rows whose package is unknown land as caught
   review signals (unanchored-stays-visible, I-2), never dropped.
2. **CoA capture:** the CoA Tracking Number table and CoA Master lookup are
   captured losslessly (fidelity direction) and joined read-side to RAIL v2's
   `CoA Tracking Number` where values match; no fabricated joins.
3. **Full-fidelity:** unmapped columns and all three sheets retained verbatim
   against the source document, per the D-PEC-41 capture mechanism.
4. **Round-trip export parity** for the contract.
5. **Read-side surfacing:** interface facts feed existing package/discipline
   views' interface counts only where drill-backed (factual-or-absent); no
   new web surface under O-A.
6. **Tests:** header normalization (trailing spaces), matrix expansion,
   idempotent re-import, unknown-package signals, CoA join behavior,
   round-trip parity.

**Not in scope:** any mutation surface; interface workflow/status modeling
beyond attested facts; reopening ADR-011; `.docx`; XLSX parsing (D-PEC-42
delivers the workbook to this contract once both land).

## Fence (exact; STOP outside it)

O-A may touch only: `projects/pec/server/src/import/**`,
`projects/pec/core/src/**` (additive schema for interface facts/CoA capture),
`projects/pec/server/src/**` read-side projections, `projects/pec/server/test/**`,
`projects/pec/fixtures/**`, `projects/pec/agent-sidecar/**` (contract naming
on the mapping lane only), `projects/pec/execution/_Coordination/IMPORT_TEMPLATES/**`,
`projects/pec/execution/_Coordination/REPORT_BASIS.md`. No `web/**`, no
tracked DB files, no new dependencies, no direct-apply path.

## Options

- **O-A (recommended):** full contract as above.
- **O-B:** Packages matrix only (defers CoA tables). Conflicts with the
  fidelity direction unless the owner scopes it deliberately.
- **O-C:** spec-only documentation of the mapping.
- **O-D:** defer.

## Verification plan (workplan step-4 bar)

PEC belt-and-braces; the tests above; scope containment ⊆ fence; self-check /
coord-check / `git diff --check`; adversarial review (no dropped columns, no
invented interface facts, unknown packages caught not guessed); scratch-DB
verification only; TWD content stays out of the repo (D-PEC-01; F-PEC-3).

## Rollback

Single revert of the tranche commit(s); additive migration reverses by
ordinary rollback.

## Human ruling

**RULED: O-A, limited** (owner in-session, Ryan Tufts, 2026-07-09,
verbatim):

> D-PEC-43: O-A, limited to importing/displaying interface relationships as
> attested facts now; no invented interface status unless the source document
> explicitly carries it. Later packet reserved for interface status vocabulary:
> unknown / not started / in progress / spec created / incorporated in scope /
> complete.

Execution rider: O-A is affirmed for attested interface relationship import
and display/report use. Interface status vocabulary/modeling is explicitly
not authorized here unless the source document itself carries the status. A
future packet owns the interface status vocabulary named above.
