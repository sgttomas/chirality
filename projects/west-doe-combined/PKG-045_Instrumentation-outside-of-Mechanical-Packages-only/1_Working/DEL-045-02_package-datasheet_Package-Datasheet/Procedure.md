# Procedure — DEL-045-02 Package Datasheet (PKG-045 Instrumentation, WBS 03)

## Purpose

Operational procedure to produce and verify the PKG-045 Package Datasheet so it satisfies the requirements in `Specification.md` and is fit for third-party vendor / discipline package engineering handoff.

## Prerequisites

- Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`.
- Have local access to the GATE-07 snapshot: `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`.
- Have local access to `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (SEC-04, SEC-05, SEC-08, SEC-12, SEC-13, SEC-14, SEC-15).
- Workbook Packages row 47 source slice: not locally accessible — treat as TBD location and route via registers.
- Coordinate with SEC-07 (Electrical) and SEC-13 (Controls) authors; see Conflict Table CONF-03.

## Steps

- **P-01 — Confirm protected-state safety.** Read `_STATUS.md`. Proceed only if state is in `ALLOW_OVERWRITE_STATES` (OPEN, INITIALIZED). Otherwise stop and report `SKIPPED_PROTECT_HUMAN_WORK`.
- **P-02 — Populate Identification.** Fill Datasheet Identification from `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv` / `PACKAGE_REGISTER.csv` for PKG-045. Cite both sources per cell.
- **P-03 — Pull objective associations.** From `OBJECTIVE_DELIVERABLE_MAP.csv`, list OBJ-002, OBJ-003, OBJ-005, OBJ-006, OBJ-007, OBJ-010 as supports-objectives (PACKAGE_HEURISTIC mode); label as ASSUMPTION (best-effort mapping) until human confirms.
- **P-04 — Populate utility, ambient, and coordination attributes.** Re-read DBM SEC-04 (site basis), SEC-08 (coordination), SEC-13 (instrument air, cable separation) and write Datasheet Attributes / Conditions rows for: instrument air supply / demand, ambient design min, cable separation, coordination with civil/electrical/controls/instrumentation.
- **P-05 — Populate detection, BPCS/RIO, ESD attributes.** Re-read DBM SEC-14 and write Datasheet Attributes rows for detector manufacturer basis, BPCS/RIO platform, ESD pushbutton location and wiring, visual/audible alarm association.
- **P-06 — Mark TBD items explicitly.** Detector quantity, tag list, set points, voting logic, placement, calibration, enclosure/classification/SIL, building-by-building ESD placement, reset/bypass/permissive logic, vendor model/ratings/certifications — write as TBD with source pointer to DBM SEC-14.
- **P-07 — Carry interface facts.** Copy the five interface rows for PKG-045 from `INTERFACE_REGISTER.csv` into the Datasheet Physical Interfaces table; cite the row, link each to its `ARTIFACT_REGISTER.csv` ART-* row.
- **P-08 — Surface open interface items.** Flag the shared HP/Cryo and LP dual flare stack / incinerator allocation as open per DBM SEC-04 (line 56). Record in Datasheet Conditions and in Guidance Conflict Table CONF-02.
- **P-09 — Verify source-grounding.** For every non-trivial Datasheet value, verify a Source column cell points to a real file and section. Missing values: TBD. Inferences: ASSUMPTION.
- **P-10 — Cross-document consistency sweep (Pass 2).** Apply Step 5 cross-checks: Datasheet attributes vs Specification requirements; Specification requirements vs Guidance principles; Specification requirements vs Procedure verification hooks; consistent terminology and numeric values.
- **P-11 — Conflict capture.** Where consistency cannot be resolved from drafts plus available sources, add a row to the Guidance Conflict Table rather than guess.
- **P-12 — Safe `_STATUS.md` update.** If state is OPEN, run `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`. If state is not OPEN, do not modify `_STATUS.md`; report skipped.

## Verification

- **V-01.** All six rows of Datasheet Identification populated and cited.
- **V-02.** Each Specification requirement R-01..R-16 has a Source cell and at least one Verification Hook.
- **V-03.** Every TBD in Datasheet corresponds to a source-acknowledged unknown (DBM section cited).
- **V-04.** Physical Interfaces table contains exactly the five PKG-045 interface rows from `INTERFACE_REGISTER.csv`.
- **V-05.** Guidance Conflict Table records each unresolved consistency issue with both source pointers populated.
- **V-06.** `_STATUS.md` either transitioned OPEN -> INITIALIZED or was left untouched with a documented skip reason.
- **V-07.** No files outside `{DELIVERABLE_PATH}` were modified; only `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, `_STATUS.md`, and the run record in `_run_records/` were written.

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` — the four-document kit.
- `_STATUS.md` — state record after safe update.
- `_run_records/TASK_RUN_<timestamp>.md` — execution provenance for this run.
- Downstream artifact-register rows (ART-28707828BB, ART-63FDE29B88, ART-D4E1D6D31B, ART-8ED52AB0CB, ART-D44857B017, ART-76EDC4125D, ART-69F2289654, ART-0B43FA4ACD, ART-C6BB7910F9) are evidenced by sections of `Datasheet.md`.
