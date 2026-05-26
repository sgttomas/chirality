# Procedure — DEL-050-06 EPC Vendor Package Review and Acceptance

## Purpose

Operational procedure for the EPC Integrator to (a) review the SOC vendor package against the EPC anchor deliverables and accessible source basis, (b) compile acceptance, test/inspection, and turnover evidence, and (c) advance the deliverable to a defensible handoff state.

## Prerequisites

Declared dependencies (per `_DEPENDENCIES.md`): none declared during PREPARATION. Functional prerequisites required to perform this procedure:

- **Inputs available** (or explicitly noted as missing):
  - EPC Scope of Work — `DEL-050-01_scope-of-work` (status: TBD; check `_STATUS.md`)
  - EPC Package Datasheet — `DEL-050-02_package-datasheet` (status: TBD)
  - Construction Work Package — `DEL-050-03_construction-work-package` (status: TBD)
  - Vendor Engineered Equipment Package — `DEL-050-04_vendor-engineered-equipment-package` (status: TBD)
  - Vendor Document Turnover Package — `DEL-050-05_vendor-document-turnover-package` (status: TBD)
- **Source slices accessible**:
  - `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §SEC-04 (SOC Basis, Controls/Protection, Interfaces, Assumptions/TBDs)
  - GATE-07 PROJECT_DECOMP snapshot registers
- **Source slices not locally accessible** (record as missing; acceptance items that depend solely on these become TBD):
  - `26020-01-PT-RFQ-12-005_Stabilizer_OH_Comp.docx`
  - `26020-Package_Requirements.docx` heading 5

## Steps

1. **Initialize.** Confirm `_STATUS.md` is in an overwrite-permitted state (`OPEN` or `INITIALIZED`). Read `_CONTEXT.md`, `_REFERENCES.md`, and `_DEPENDENCIES.md`.
2. **Assemble inputs.** Collect the upstream EPC anchors (DEL-050-01/02/03) and vendor deliverables (DEL-050-04/05). Where any upstream is not yet at the required maturity, record the gap and proceed only with the portions of the acceptance log that do not depend on it.
3. **Build the package acceptance checklist.** For each requirement R-01..R-16 in `Specification.md`, create a checklist row with: requirement ID, SourceRef, vendor evidence pointer, EPC reviewer disposition (Pass / Conditional / Fail / Open), reviewer initials, date, and notes. Carry `TBD`/`TBC` items as Open with an explicit ruling pointer.
4. **Vendor document review.**
   1. Pull the vendor document register from DEL-050-05.
   2. For each document, record: doc number, revision, scope, reviewer, comments raised, comment-disposition (vendor reply), and close-out reference. Mark documents whose authoritative source is not locally accessible as "scope-confirmed only" and route deeper review to detailed engineering.
5. **Cross-check vendor data against source.** Validate the SOC quantity/sparing, compressor model (Ariel KBC/6, 4 stages), driver basis (4000 V, 2,700 hp, 8-pole ~891 rpm, 3:1 inverter turndown, NEMA MG 1, "No Toshiba"), stage pressures, stage capacities, MAWPs, cooler discharge temperatures, scrubber configuration, and auxiliary scope against the source slice in DBM-Deepcut §SEC-04. Record each match/mismatch on the acceptance checklist.
6. **Verify interfaces.** For each of the 13 declared interface types (PACKAGE_REGISTER row 81), confirm vendor design addresses the interface and that EPC scope (DEL-050-01/03) lands the facility-side counterpart. For SOC process interfaces (per DBM-Deepcut §Interfaces), record the corresponding vendor P&ID and tie-in reference.
7. **Compile test and inspection evidence.** Index FAT/SAT records, hydrotest reports, NDE certificates, motor test reports, vibration/balance reports, and control function tests from the vendor turnover set. For each, record disposition and any open punch-list items.
8. **Compile turnover evidence.** Index mechanical completion certificates, OEM data books, calibration records, lube-oil sample results, spares lists, training records, and any conditional-acceptance riders. Map to the construction work package handoff requirements.
9. **Surface open items for human ruling.** Items left Open or Conditional after Steps 3-8 are written to a "NEEDS_HUMAN_RULING" section of the acceptance checklist with: item, source basis, EPC reviewer recommendation, and proposed close-out path. No item is silently closed.
10. **Status advance.** When all four artifacts in `_CONTEXT.md` Anticipated Artifacts are populated and either Pass or routed to ruling, propose advance of `_STATUS.md` to the next state per repository convention (proposal only; the human ruling drives the actual status edit).

## Verification

- All four anticipated artifacts (review log, acceptance checklist, test/inspection evidence index, turnover evidence index) are present in the deliverable folder.
- Every R-01..R-16 requirement appears as at least one row in the acceptance checklist with an explicit disposition.
- All 13 PKG-050 interface types are explicitly addressed in the checklist.
- No `TBC`/`TBD` source item has been silently converted to Pass.
- Cross-references to source slices (`SourcePath` + `SectionRef`) are present on every substantive verification row, or the row is marked `location TBD` with the relevant source name retained.

## Records

The deliverable folder shall retain:

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` (this four-document set).
- Package acceptance checklist (verification matrix) — TBD artifact, populated during execution.
- Vendor document review log — TBD artifact.
- Test and inspection evidence index — TBD artifact.
- Turnover evidence index — TBD artifact.
- `_STATUS.md` history entries for state advances.
- Run records under `_run_records/` (one per TASK invocation).
- Any human ruling memos generated during Step 9.
