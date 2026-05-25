# Procedure: DEL-029-01 Scope of Work

## Purpose

This procedure describes how to produce, verify, and close out the EPC Scope of Work artifact for PKG-029 (`Transformer TXP-8600-1`). It addresses both producing the artifact (drafting the Scope of Work document) and using the artifact downstream (handing it off to the Package Datasheet, Construction Work Package, Vendor Engineered Equipment Package, Vendor Document Turnover, and EPC Vendor Package Review and Acceptance deliverables).

## Prerequisites

- Read `_CONTEXT.md` (identity, scope, anticipated artifacts).
- Read `_STATUS.md` (current lifecycle state).
- Read `_REFERENCES.md` (decomposition basis and shared source root).
- Read `_DEPENDENCIES.md` (declared upstream/downstream; coordination mode).
- Read the Gate 7 snapshot registers identified in `_REFERENCES.md`:
  - `DELIVERABLE_REGISTER.csv` row `DEL-029-01_scope-of-work`;
  - `PACKAGE_REGISTER.csv` row `PKG-029`;
  - `INTERFACE_REGISTER.csv` rows for `PKG-029`;
  - `ARTIFACT_REGISTER.csv` rows for the deliverable;
  - `OBJECTIVE_DELIVERABLE_MAP.csv` rows for the package.
- Read the accessible source slices:
  - `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages sheet row 31;
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Power System, System Voltages, Standby Power, Transformers, 208/120 V Systems, Electrical Buildings, Grounding and Bonding paragraphs;
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Incoming Power and Transformers context (analog only).
- Confirm declared dependencies: none declared upstream; none declared downstream.

## Steps

1. **Confirm identity.** Verify the identity fields in `Datasheet.md` against workbook Packages row 31 and `PACKAGE_REGISTER.csv` row PKG-029. Confirm WBS 01, tracking number `26020-01-30-020`, discipline Electrical, type EPC Scope of Work, responsible party EPC Integrator.
2. **Confirm responsibility split.** Verify the Package Vendor / EPC Integrator responsibility model is reproduced from `PACKAGE_REGISTER.csv` row PKG-029 with no scope migration.
3. **Confirm interface set.** Verify that all seven interfaces (Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports) are carried with the correct `IFC-*` IDs from `INTERFACE_REGISTER.csv`.
4. **Confirm facility-level function statements.** Verify each statement of facility-level function (13.8 kV primary; 600/347 V secondary; HRG 5 A continuous secondary grounding rule; structural-steel transformer base on precast concrete bearing foundation; CEC spacing) cites the correct DBM source slice.
5. **Confirm scope items.** Verify `SOW-0030` is the covered scope item and that the Scope of Work narrative does not extend to scope items not assigned to PKG-029.
6. **Confirm objective association.** Record that the objective set (`OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-008`, `OBJ-009`, `OBJ-010`) is taken from package-grouped objective rows under `OBJECTIVE_ASSOCIATION_MODE = PACKAGE_HEURISTIC` as an ASSUMPTION pending human ruling.
7. **Confirm TBDs.** Verify that all package-specific technical values not supported by accessible source slices remain `TBD` rather than being asserted. Confirm `Guidance.md` Conflict Table contains the open human ruling items (HRR-029-01-001 through HRR-029-01-003).
8. **Cross-document consistency sweep.** Run the Step 5 cross-document consistency checks (Datasheet ↔ Specification ↔ Guidance ↔ Procedure). Confirm:
   - identity values are identical across all four documents;
   - the interface list is identical across documents;
   - the grounding rule (5 A continuous HRG on 600 V secondary) is stated consistently;
   - terminology uses `TXP-8600-1`, `2.5 MVA`, `13.8 kV`, `600/347 V`, and `EPC Integrator` / `Package Vendor` consistently.
9. **Status update.** Read `_STATUS.md`. If current state is `OPEN`, update `OPEN → INITIALIZED` with a History line crediting `TASK + four-documents (P1_P2)`. If current state is not `OPEN`, do not modify `_STATUS.md`.
10. **Run record.** Write the run record at `_run_records/TASK_RUN_2026-05-24_<HHMM>.md` per the AGENT_TASK and skill specifications.

## Verification

- All four documents (`Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`) exist in the deliverable folder.
- Default schema sections are present in each document:
  - Datasheet: Identification, Attributes, Conditions, Construction, References;
  - Specification: Scope, Requirements, Standards, Verification, Documentation;
  - Guidance: Purpose, Principles, Considerations, Trade-offs, Examples;
  - Procedure: Purpose, Prerequisites, Steps, Verification, Records.
- Identity, responsibility, interface, scope-item, and objective sets match `_CONTEXT.md` and Gate 7 registers.
- Each non-trivial technical statement cites a source (`SourcePath` + section/line reference) or is marked `TBD`.
- The Conflict Table in `Guidance.md` records open human ruling items.
- No writes occurred outside the deliverable folder.

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` — produced by this run.
- `_STATUS.md` — updated `OPEN → INITIALIZED` (safe state update).
- `_run_records/TASK_RUN_2026-05-24_<HHMM>.md` — run record.
- Open human ruling items: HRR-029-01-001 (rating/insulating medium), HRR-029-01-002 (downstream allocation), HRR-029-01-003 (Area/Exterior Lighting & Communications/Network tie-in basis) — recorded in `Guidance.md` Conflict Table for downstream resolution.
