# D-PEC-41 - PROPOSAL: MDL/RAIL import contract v2 (TWD revised templates)

**Status:** RULED 2026-07-09 (O-A).
**Date prepared:** 2026-07-09
**Decision ID:** D-PEC-41
**Prepared by:** PEC work loop agent. The ruling act is the owner's
(K-AUTH-1; D-GOV-04). Packet form follows the D-PEC-20/D-PEC-39 source-tranche
packet precedent: verified current state, decision to rule, exact fence,
options, verification plan, rollback, and open human ruling.

> **Epistemic status: agent-prepared source-tranche packet, not authority.**
> It proposes the R1 "MDL/RAIL contract v2" tranche of the reporting-product
> standing plan, designed against the owner-provided revised TWD templates.
> Source execution remains prohibited unless and until the owner rules this
> packet. Sources govern on any disagreement.

## Why this row exists

The R1 contract-v2 row was parked on a Tier-P hard prerequisite: the revised
MDL/RAIL templates (Receipt 74: owner "not ready to provide those needed
MDL/RAIL templates"). On 2026-07-09 the owner provided them as the TWD project
workbooks (steer of record, Receipt 75) and gave a fidelity direction of
record, verbatim:

> "you should be importing all the data I'm providing. Not missing out on any
> of it, but not needing to display all of it either."

Contract v2 therefore has a **full-fidelity capture** requirement: every
column and sheet the owner provides is imported losslessly; display remains
selective. This packet specifies the v2 contract against the actual TWD
template structure — no guessed columns (K-INVENT-1).

## Dependencies

- **Tier-P input present:** the revised templates exist as owner-provided
  files (gitignored `projects/pec/pilot-scratch/input/`, D-PEC-01 convention):
  `2026-07-07-Deliverables_Status(1).xlsx` (MDL) and
  `2026-07-07-RAIL_Packages(1).xlsx` (RAIL). Owner-attested TWD project data;
  the earlier AUR-era inputs are superseded as template basis (steer of
  record: AUR "is invented data created to get the project off the ground").
- D-PEC-35 upload lane (landed) is the delivery path for CSV/TSV; binary XLSX
  parsing is **not** this packet — it is D-PEC-42 (the reserved D-PEC-35
  rider). Until D-PEC-42 lands, v2 files reach the lane as exported CSV/TSV.
- D-PEC-39 coverage declarations (landed) attach per-document coverage; the
  RAIL workbook's own metadata block (below) can prefill a declaration but
  never replaces the PE's declared coverage.

## Verified current state (live tree, 2026-07-09)

| Fact | Source |
|---|---|
| The standing plan's R1 row "MDL/RAIL contract v2" was parked on Tier-P revised templates; the row's scope is §16 contract extensions: % complete (0–100 int, PE-attested), full status vocabulary, coverage columns, additive fields, export round-trip parity. | `_DomainEngines/pec/WORKPLAN_2026-07-09_pec_reporting_product.md` (R1 row; Tier-P) |
| v1 MDL contract requires `doc_no, title, package, discipline, owner, current_rev, state, due_date`; v1 RAIL requires `item_id, statement, type, log, owner, need_by, status, raised_by, raised_date` with person-resolved owners. | `projects/pec/server/src/import/index.ts` (importMdl/importRail) |
| % complete is a PE-attested source fact arriving via import — never an in-app derivation, never in-app editable (reconciliation 1; F-PEC-2 stands). | `_DomainEngines/pec/WORKPLAN_2026-07-09_pec_reporting_product.md` (reconciliations) |
| Import stays proposal-gated on the agent lane; imported records carry import-ownership guards (`force` only overrides in-app-edited records with a conflict report). | `projects/pec/server/src/import/index.ts`; `projects/pec/execution/_Coordination/IMPORT_TEMPLATES/FILE_DROP_RUNBOOK.md` |
| Owner fidelity direction and template provision are recorded verbatim in the loop receipt. | `_DomainEngines/pec/LOOP_RECEIPTS.md` (Receipt 75) |

## Template structure of record (from the owner-provided TWD workbooks)

Recorded here because the workbooks live outside the repo (gitignored
pilot-scratch, D-PEC-01). Structure and vocabulary only — no project row
content.

### MDL — `Deliverables_Status` workbook

Four sheets: **Master Deliverables List** (title row 1, header row 2, data
from row 3), **Rules of Credit** (two rule sets: `ENGINEERING & DESIGN` and
`ENGINEERING ONLY`, each stage → % value), **Data Dictionary**
(topic/detail assumptions + column definitions), **Lists** (validation
vocabularies).

MDL columns: `Area #` · `Project Phase` · `Discipline` · `Package ID` ·
`Package Type` · `Package Name` · `Deliverable ID` · `Deliverable Type` ·
`Target Completeness` · `Working Status` · `% Complete`.

Observed template facts that bind the contract design:

- **`Deliverable ID` is defined but unpopulated** (0 of 552 data rows; the
  Data Dictionary defines it as "built from the package ID and deliverable
  code/source ID"). There is **no `doc_no`, owner, revision, state, or due
  date** — the v1 MDL required set does not exist in this template.
- `% Complete` is an integer 0–100 where present, **absent on most rows**,
  and carries a non-numeric verbatim marker (`Next Phase`) on some rows.
- Vocabularies (Lists sheet): Working Status = Not Set / Not Started /
  In Progress / On Hold / Complete / Cancelled; Target Completeness = Draft /
  Preliminary / FEED / IFA / IFR / IFQ / IFD / IFH / IFB / IFC / IFU /
  As Built / Issue Internally / Squad Check / None; Project Phase = Prelim /
  FEED / 30% / 60% / 90% / IFC / As Built; Package Type = Equipment /
  Documentation / Internal (observed data also carries `FEED Deliverable` and
  `Internal Deliverable`); Deliverable Type = 16-item vocabulary (observed
  data adds compound values, e.g. "Technical Datasheet / Specs"); and two
  vocabularies exist in Lists with **no corresponding MDL column**, captured
  as vocabulary only: `Hold Type` (Decision / Information / Clarification /
  Resources / Risk of Change / Approval) and `Priority` (Now / Next / Later /
  After).

### RAIL — `RAIL_Packages` workbook

Two sheets: **RAIL** (row 1 sheet title `PACKAGES RAIL`; metadata-label
block rows 2–5: `DATE / VERSION:` · `PROJECT NAME:` · `PROJECT NO.:` ·
`DOC NO.:`; row 6 blank; header row 7; data from row 8) and **Lists**
(vocabularies).

RAIL columns: `Package ID` · `Issue #` · `Package Discipline` · `Area` ·
`Phase` · `CoA Tracking Number` · `Package Type` · `PACKAGE` (name) ·
`ISSUE TYPE` · `ISSUE DESCRIPTION` · `UPDATES` · `Responsible Party` ·
`STATUS` · `PRIORITY` · `ASSIGNED DATE` · `ORIGINAL TARGET COMPLETION DATE` ·
`CURRENT TARGET COMPLETION DATE` · `ACTUAL COMPLETION DATE`.

Observed template facts that bind the contract design:

- **Identity is `Package ID` + `Issue #`** — there is no v1 `item_id`.
- **`Responsible Party` is a discipline/function, not a person** (Lists:
  Civil / Controls / Electrical / Instrumentation / Mechanical / Piping /
  Process / Procurement / Project Management / Regulatory / Structural).
  v1's person-resolution requirement does not fit this template.
- ISSUE TYPE vocabulary: Decision / Information / Clarification / Approval /
  Action / Opportunity / Risk / Resources.
- STATUS vocabulary: Not Set / Not Started / In Progress / On Hold /
  Complete / Cancelled. PRIORITY: Now / Next / Later / After.
- **Package placeholder rows exist**: rows carrying only package identity
  (no issue content). These are package-universe facts, not issues.
- The `Phase` column carries lifecycle values (30% / 60%) **and** the value
  `Cancelled` on some rows; Lists also enumerates `Cancelled` under PHASE.
  Captured verbatim, surfaced as a review signal, never coerced.
- Three completion-date columns (original target / current target / actual)
  enable factual slippage reporting.

## Decision to rule

Whether to authorize one source tranche implementing MDL/RAIL contract v2:

1. **MDL v2 contract** matching the TWD template: required identity =
   `Package ID` + `Deliverable Type` (+ `Package Name` for package
   attributes); all other columns optional-but-captured. Deliverable
   identity: because `doc_no`/`Deliverable ID` is unpopulated, the importer
   derives a deterministic, idempotent `doc_no` from `Package ID` +
   `Deliverable Type` (recorded rule, stable across re-imports; a populated
   `Deliverable ID`, when the PE starts filling it, takes precedence). v1's
   `owner/current_rev/state/due_date` become optional; absent revision facts
   create no revision record (factual-or-absent — no seeded fake rev).
2. **Attested fields on the deliverable**: `% Complete` (0–100 integer,
   PE-attested, never in-app editable, never derived — reconciliation 1;
   non-numeric verbatim markers such as `Next Phase` are captured verbatim as
   an attested marker and excluded from numeric rollups, with an explain
   basis saying so); `Working Status` (full vocabulary incl. On Hold —
   captured as an attested import field, distinct from the gated in-app
   revision state machine, which this tranche must not touch or bypass);
   `Target Completeness`; `Project Phase`; `Area #`.
3. **RAIL v2 contract** matching the TWD template: identity =
   `Package ID` + `Issue #`; issue rows map to the existing RAIL record
   machinery by ISSUE TYPE (full vocabulary above; hold semantics unchanged);
   placeholder package rows refresh package attributes only and create no
   issue/work-item/intake record; `Responsible Party` is captured verbatim as
   a discipline-valued responsible field (optional person mapping only where
   an exact person match exists — no fabricated persons); `UPDATES`,
   `CoA Tracking Number`, `PRIORITY`, and all three completion dates are
   captured; `Phase = Cancelled` and any MDL-status/RAIL-issue disagreement
   land as caught review signals (feeding the R2 consistency-check row), not
   silent coercions or rejections.
4. **Full-fidelity capture (owner direction):** every provided column not
   mapped to a first-class field is retained losslessly on the imported
   record (verbatim source key/value payload), and every non-tabular sheet
   (Rules of Credit, Data Dictionary, Lists, RAIL metadata block) is captured
   verbatim against the source document/import event. Display remains
   selective; capture is total. Rules of Credit is reference/explanation
   material only — it never becomes an in-app % computation (reconciliation
   1).
5. **Round-trip export parity**: exports of v2-imported data reproduce the
   provided columns (workplan R1 row).
6. **Templates + runbook**: v2 CSV templates and IMPORT_TEMPLATES /
   FILE_DROP_RUNBOOK / IMPORT_MAPPING documentation updated to the v2
   contract; v1 contracts remain accepted (additive, no breaking change).
7. **Tests** for: header detection (MDL row 2; RAIL row 7 + metadata block),
   identity derivation stability/idempotency, attested-field capture and
   non-editability, verbatim unmapped-column retention, placeholder-row
   handling, vocabulary acceptance, review-signal emission, round-trip
   parity, and no destructive mutation.

**Not in scope:** binary XLSX parsing (D-PEC-42); `.docx` generation;
MDL↔RAIL consistency checker itself (R2 — this tranche only emits the
caught signals its contract makes visible); needs internal/client typing;
interfaces contract; discipline-view changes beyond what lands automatically
through existing views; any in-app editing of attested fields; any revision
state-machine change.

## Fence (exact; STOP outside it)

O-A may touch only:

- `projects/pec/server/src/import/**`
- `projects/pec/core/src/**` (schema/model additions, additive migration)
- `projects/pec/server/src/**` read-side only where v2 fields must surface in
  existing explain/report payloads
- `projects/pec/server/test/**`
- `projects/pec/fixtures/**` (v2 contract fixtures only)
- `projects/pec/agent-sidecar/**` only where the mapping lane must name v2
  contracts
- `projects/pec/execution/_Coordination/IMPORT_TEMPLATES/**`
- `projects/pec/execution/_Coordination/REPORT_BASIS.md` (basis rows for any
  v2-fed figure)

No `web/**`, no tracked DB files, no root manifests, no new dependencies, no
profile edits, no direct import/apply/force path changes.

## Options

- **O-A (recommended):** full v2 contract as specified above — full-fidelity
  capture per the owner direction, additive migration, v1 kept working,
  CSV/TSV delivery until D-PEC-42.
- **O-B:** v2 with mapped-fields-only capture (drops unmapped columns/sheets).
  Listed for completeness; **conflicts with the owner's fidelity direction**
  — not recommended.
- **O-C:** coordination/spec-only — record the v2 mapping in IMPORT_TEMPLATES
  docs, no source change.
- **O-D:** defer.

## Verification plan (workplan step-4 bar)

- PEC belt-and-braces: `npm run typecheck && npm test && npm run build &&
  npm run drill`.
- Import tests as itemized above, including idempotent re-import against the
  derived identity and force/ownership-guard behavior on v2 fields.
- Scope containment: `git diff --name-only` ⊆ the ruled fence.
- Repo checks: `PYTHONDONTWRITEBYTECODE=1 python3
  tools/practitioner_harness/harness.py self-check`; coord-check on the
  branch diff; `git diff --check`.
- Adversarial review: no captured column silently dropped (fidelity
  direction); % complete never editable/derived; no fabricated persons,
  revisions, or issues from placeholder/absent data; every v2-fed report
  figure carries a basis row.
- Scratch-DB verification only; TWD project content stays out of the repo
  (D-PEC-01 pilot-scratch convention; F-PEC-3 data residency).

## Rollback

Single revert of the source tranche commit(s); additive migration reverses by
ordinary migration rollback if one is added. Scratch verification data stays
scratch-only and uncommitted.

## Human ruling

**RULED: O-A** (owner in-session 2026-07-09, Ryan Tufts, verbatim): "I rule
O-A on both D-PEC-41 and D-PEC-42. Place report files in
`projects/pec/pilot-scratch/reports/` a new folder you need to create. and I
just added `26020-Packages_Interfaces.3.xlsx` in the `inputs/` folder. You
can merge PR #122 when you see fit and any follow-up PR related to this work
I'm approving, is also approved to merge once ready without my review."
(Quote note: the owner gave the reports path absolute; recorded here
repo-relative per coordination-file conventions. Live folder is
`pilot-scratch/input/`.) — Source execution authorized inside this packet's
O-A fence. Riders recorded: report-file placement = gitignored
`projects/pec/pilot-scratch/reports/` (Tier-P "report template file
placement" row resolved); the interfaces document format arrived
(`pilot-scratch/input/26020-Packages_Interfaces.3.xlsx`) — its import
contract remains its own decision packet; PR merges for this ruled work are
pre-approved once checks are green.
