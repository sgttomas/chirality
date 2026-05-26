# Procedure: DEL-076-05 — Vendor Document Turnover Package

> Operational procedure to produce and turn over the vendor document set for PKG-076 Lube Oil Supply. Steps cover producing the deliverable artifact (the document set + register + turnover records); use of the artifact is the EPC Integrator's responsibility under DEL-076-06.

## Purpose

To prepare, control, submit, review, and formally turn over the Lube Oil Supply package vendor documents and turnover records from the Package Vendor to the EPC Integrator, in accordance with `Specification.md`.

## Prerequisites

| Prerequisite | Source | Status |
|---|---|---|
| EPC Scope of Work for PKG-076 (DEL-076-01) issued | DELIVERABLE_REGISTER.csv (GATE-07) row 384 | Not yet issued (TBD) |
| EPC Package Datasheet for PKG-076 (DEL-076-02) issued | DELIVERABLE_REGISTER.csv row 385 | Not yet issued (TBD) |
| Project document control procedure / EDMS configured | Standard project basis | TBD — not in accessible source |
| Project hazardous-material list available | DBM 3-25 line 507 | Not in workspace (TBD) |
| Vendor package contracted with documentation requirements | Standard package contract | ASSUMPTION — required prior to register opening |
| Access to source materials: 26020-Package_Requirements.docx heading 30 | `_REFERENCES.md` | DOCX present in `_Sources`; not converted (location TBD for clause text) |
| `_REFERENCES.md`, `_CONTEXT.md`, `_DEPENDENCIES.md` for DEL-076-05 | Deliverable folder | Present |

## Steps

### Step 1 — Open vendor document register
1.1 Create the register with at minimum the columns required by R-076-05-01 (number, title, type, revision, status, planned issue date, actual issue date, EPC review status).
1.2 Seed the register from: EPC Scope of Work (DEL-076-01), Package Datasheet (DEL-076-02), source-required document rows from `26020-Package_Requirements.docx` heading 30, and the mechanical-package document class list (DBM 3-25 line 617).
1.3 Mark any unresolved row source as `TBD`.

### Step 2 — Plan submittals against mechanical package document classes
2.1 For each class enumerated in DBM 3-25 line 617 — datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, vendor document registers — confirm at least one register row exists.
2.2 Record gaps as `TBD` register rows so the gap is visible to EPC review.

### Step 3 — Produce vendor document content
3.1 Populate vendor datasheets and supporting documents for lube-oil storage (400 bbl heated tank), cylinder lube-oil pump P-9240-1, and crank-case basis per DBM 4-25 lines 2059-2068.
3.2 Where vendor documents need hazardous-material classification, reference the project hazardous-material list; if not available, leave the field `TBD` and note the dependency.
3.3 Apply project document numbering / revision codes when the document control basis is issued; otherwise hold issue.

### Step 4 — Submit to EPC Integrator for interface/integration review
4.1 Transmit each register row at planned issue per the project document control procedure.
4.2 EPC Integrator performs interface/integration review (per `_CONTEXT.md` ResponsibleParty; specification R-076-05-07) and records review status against each register row.
4.3 Resolve review comments; reissue at the next revision.

### Step 5 — Iterate to acceptance
5.1 Repeat Steps 3-4 through IFR/IFA/IFC issue cycles (cycle naming `TBD` pending project document control basis).
5.2 Submittal is accepted only when the EPC review status for that row is recorded as accepted/approved.

### Step 6 — Prepare turnover record set
6.1 Compile acceptance log (one row per accepted document).
6.2 Prepare vendor certification of compliance with the EPC Scope of Work and Package Datasheet.
6.3 Prepare custody-transfer / handover acknowledgement.
6.4 Prepare as-built confirmation for vendor documents updated to reflect installed configuration.

### Step 7 — Execute turnover
7.1 Issue the final vendor document index with all rows at their accepted/as-built revision.
7.2 Transmit the document set, register, and turnover records to the EPC Integrator.
7.3 Record turnover in the deliverable register and the package turnover log.

## Verification

| Verification | Method | Maps |
|---|---|---|
| Register completeness | Cross-check register rows against mechanical-package document class list (DBM 3-25 line 617) | V-01, V-02 |
| Lube-oil basis consistency | Compare vendor lube-oil datasheets to DBM 4-25 lines 2059-2068 values | V-03 |
| Hazardous-material citation | Inspect lube-oil docs for project hazardous-material list reference | V-04 |
| Turnover record set | Confirm presence of acceptance log, certification, handover, as-built | V-05 |
| EPC review status | Confirm review status recorded against every register row before acceptance | V-06 |
| Document control conformance | Inspect numbering, revision codes, transmittal format | V-07 |
| Scope coverage | Confirm SOW-0135..0138 each map to at least one vendor document set | V-08 |

## Records

- Vendor document register (final issued revision)
- Submitted vendor documents at their accepted/as-built revisions
- EPC Integrator review log entries against each register row
- Turnover records: acceptance log, certification, handover acknowledgement, as-built confirmation
- Final issued vendor document index at turnover
- Transmittals supporting each submittal
