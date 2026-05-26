# Procedure — DEL-057-03 Construction Work Package (PKG-057 Stabilizers)

This Procedure describes how to produce the Construction Work Package deliverable artifact (i.e., the CWP document set plus the workface plan and turnover checklist). Operational/field execution procedures (e.g., crane lift plans, weld procedures) are produced by the EPC construction organization under this CWP and are out of scope for this deliverable's authoring procedure.

## Purpose

To assemble and issue the EPC Integrator's Construction Work Package for PKG-057 (three Inlet Stabilizer Packages), including the installation and tie-in workface plan and the construction interface and turnover checklist, grounded in the GATE-07 decomposition and the underlying source set.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot present (`GATE-07_Final_Published_2026-05-24`).
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` initialized for this deliverable (PREPARATION complete).
- `DEL-057-01` Scope of Work draft available (sibling deliverable).
- `DEL-057-02` Package Datasheet draft available (sibling deliverable).
- Source slices for `26020-Package_Requirements.docx` package heading 12, and for DBM SEC-08/SEC-09/SEC-11/SEC-12/SEC-13/SEC-14/SEC-15 referenced by OBJ-005..OBJ-010 — TBD (not yet extracted locally).
- Vendor design basis (`DEL-057-04`) — TBD (downstream; CWP issued for Construction must reflect vendor inputs once available).

## Steps

1. **Confirm package identity and scope basis.**
   - Pull deliverable row from `DELIVERABLE_REGISTER.csv` and package row 82 from `PACKAGE_REGISTER.csv`.
   - Pull `SOW-0177`..`SOW-0180` from `SCOPE_LEDGER.csv`.
   - Confirm no conflict with `_CONTEXT.md` identity block.
2. **Establish the interface checklist.**
   - Enumerate every applicable interface family from `PACKAGE_REGISTER.csv` row 82 (13 families listed).
   - For each family, capture: tie-in points, EPC vs Vendor responsibility, installation prerequisites, inspection/test, and turnover evidence.
   - Mark families where vendor input is required as `TBD: pending DEL-057-04`.
3. **Carry the source-stated process boundaries into tie-in constraints.**
   - Bring forward the flash feed separator, exchanger, column, and product cooler operating and design conditions from `SOW-0180` into the CWP's tie-in design boundaries.
   - Do not reinterpret values; reproduce them verbatim and cite `SOW-0180`.
4. **Define the installation and tie-in workface plan structure.**
   - Sections: receipt and laydown; foundations and supports; skid set; skid-edge piping tie-in; electrical tie-in (MCC supply, EHT, grounding/bonding, lighting); I&C tie-in and DCS integration; utility tie-ins (instrument air, fuel gas, drains, flare/vent, heat medium, HVAC as applicable); fire & gas; maintenance access verification.
   - Plan content beyond the structure remains `TBD` until vendor input lands.
5. **Define the construction interface and turnover checklist structure.**
   - One row per interface family from Step 2; one column per record type (drawing/redline, test, sign-off, deficiency log).
   - Tie acceptance to OBJ-010 closure expectations (open-item evidence handed to `DEL-057-06`).
6. **Carry vendor/EPC responsibility split into every section.**
   - Reinforce OBJ-004: vendor owns engineering/design/equipment/documentation; EPC owns integration; CWP does not redirect work across that line.
7. **Identify and label assumptions and TBDs.**
   - Mark sour-service classification as ASSUMPTION (OBJ-009; DBM slice not extracted).
   - Mark code/standard references as `location TBD` rather than naming standards not yet sourced.
   - Mark constructability constraints, lift weights/plans, hydrotest, and PWHT as TBD pending vendor input.
8. **Cross-check the four documents.**
   - Verify terminology, equipment counts (three packages; 20 trays; one LIT; one TIT), and values (793 kPag, 1724 kPag, 71 °C, 60 °C, 30.6 °C, 1,272 m3/d, 16.7 °C approach) are consistent across Datasheet, Specification, Guidance, and Procedure.
   - Verify the interface family list is consistent across documents.
9. **Capture conflicts and proposed authority.**
   - Record any source-vs-decomposition or source-vs-source disagreement in the Conflict Table in `Guidance.md`.
10. **Update `_STATUS.md` safely.**
    - If current state is `OPEN`, advance to `INITIALIZED` via `tools/scaffolding/write_status.sh` with actor `TASK+four-documents`.
    - Do not regress state.
11. **Write the run record.**
    - Produce `_run_records/TASK_RUN_<timestamp>.md` per AGENT_TASK contract; include input echo, resolved state, tools used, outputs, missing items, and TBDs.

## Verification

- All four documents exist in `{DELIVERABLE_PATH}` and contain the default schema sections.
- Each non-trivial value cites its source (`SOW-0179`, `SOW-0180`, `PACKAGE_REGISTER.csv` row 82, or a register row in `GATE-07`) or is marked `TBD`/`ASSUMPTION`.
- The 13 applicable interface families appear identically in Datasheet (Construction) and Specification (REQ-CWP-04).
- The Conflict Table is present in `Guidance.md` and lists at least the responsibility-wording and sour-service conflicts.
- `_STATUS.md` reflects `INITIALIZED` if and only if the prior state was `OPEN`; otherwise unchanged.
- Run record exists, has YAML frontmatter, and lists outputs and TBDs.

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` in `{DELIVERABLE_PATH}`.
- Updated `_STATUS.md` (state `INITIALIZED`).
- `_run_records/TASK_RUN_<timestamp>.md` with `run-status: SUCCESS` (or `FAILED_INPUTS` if preconditions failed).
- Conflict Table entries (in `Guidance.md`) for any unresolved source/decomposition disagreements.
- TBD register (inline `TBD` markers across the four documents) listing every deferred item for downstream resolution (notably DBM SEC-* source slices and vendor input from `DEL-057-04`).
