# Procedure — DEL-106-02 Package Datasheet (Yard Lighting)

> Pass: P1_P2 (four-documents skill, 2026-05-25). Procedure here describes the steps to **produce** the Package Datasheet deliverable artifact set. Steps requiring human judgment are marked `TBD`. Inferences are labeled `ASSUMPTION`.

## Purpose

Produce the EPC-Integrator-authored Package Datasheet for `PKG-106 Yard Lighting`, with carried interface-fact evidence, in a form suitable for vendor handoff and downstream review/acceptance (`DEL-106-06_epc-vendor-package-review-and-acceptance`).

## Prerequisites

- Read access to deliverable folder `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/PKG-106_Yard-Lighting/1_Working/DEL-106-02_package-datasheet_Package-Datasheet/`.
- Read access to the GATE-07 snapshot at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- Read access to source set at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/` including:
  - `26020-Packages_Interfaces_4_export.xlsx` (row 12);
  - `26020-Package_Requirements.docx` (verify per-package row absence);
  - `DBM-Deepcut/4-25_Deepcut_DBM.md` (§Lighting and Receptacles; §Power System; §Cable, Wire, and Raceways; §Energy and Emissions; §Discipline Scope);
  - `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (§Electrical Design Basis; §System Voltages; §Electrical Buildings, Raceways, Lighting, and Heat Tracing).
- Declared upstream dependencies: none at PREPARATION (`_DEPENDENCIES.md`). Functional upstream context: `DEL-106-01_scope-of-work` (sibling) for package identity narrative — not a declared blocker per `_DEPENDENCIES.md`.

## Steps

1. **Confirm deliverable identity** against `_CONTEXT.md` and `PACKAGE_REGISTER.csv` row 12. Populate the Datasheet `Identification` table from these two sources only. WBS remains `TBD` until human assignment.
2. **Read workbook row 12** in `26020-Packages_Interfaces_4_export.xlsx` to enumerate the X-marked interfaces (`Electrical Power`, `Grounding / Bonding`, `Area / Exterior Lighting`). Cross-check against `INTERFACE_REGISTER.csv` rows 40-42.
3. **Scan `26020-Package_Requirements.docx` for a Yard Lighting per-package row.** If absent (as verified on 2026-05-25), record the gap explicitly in Guidance Considerations and in `_REFERENCES.md` (read-only context — do not modify `_REFERENCES.md`).
4. **Extract source slices** from the two DBMs:
   - `DBM-Deepcut/4-25_Deepcut_DBM.md` §Lighting and Receptacles (lines 3027-3035); §Power System (lines 2937-2967); §Cable, Wire, and Raceways (lines 2997-3025); §Energy and Emissions Design Considerations (line 2183); §Discipline Scope (line 2860).
   - `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §Electrical Design Basis (line 718); §System Voltages (lines 734-736); §Electrical Buildings, Raceways, Lighting, and Heat Tracing (lines 764-770); §Construction Scope Summary (line 75).
5. **Populate Datasheet `Attributes`, `Conditions`, and `Construction`** strictly from the extracted source slices. For any field not present, write `TBD` and cite `location TBD`. Do not infer photometric levels, pole heights, fixture quantities, or tagged-equipment lists.
6. **Carry interface-fact evidence** in the Datasheet by listing the three workbook X-marked interfaces with their `INTERFACE_REGISTER.csv` interface IDs (`IFC-6FCF1B30D6`, `IFC-DA0D60681B`, `IFC-ED86F51087`) and their `ARTIFACT_REGISTER.csv` artifact IDs (`ART-B670C2963F`, `ART-0686DF8D13`, `ART-9F2D1E8063`).
7. **Draft Specification requirements** as direct, citable statements of the source slices; label every requirement with a source. Label inferred requirements as ASSUMPTION (e.g., REQ-106-02-008 emergency-lighting extension).
8. **Map verification approaches** in Specification §Verification to each requirement; verification approach must be performable by the EPC Integrator against vendor submittals or facility documents — no human ruling embedded as verification.
9. **Write Guidance** with: Purpose (from `_CONTEXT.md` and decomposition); Principles (rationale from DBM and registers); Considerations (gaps and source-set realities); Trade-offs (alternative-set treatments warranted by source); Examples (only those grounded in source slices); Conflict Table for the four open issues identified in step 11.
10. **Cross-document consistency sweep** (Pass 2 — Step 5 of skill): confirm
    - Identification values are identical across Datasheet, Specification, and Procedure (PackageID, CoA tracking, Discipline, Responsible Party).
    - Lighting values (LED type, 120/208 V supply, conductor size #10 AWG, tray-cable / conduit method) are consistent across all four documents.
    - Interface IDs are quoted identically in Datasheet and Specification.
    - Terminology: "Yard Lighting", "yard / area exterior lighting", "Package Vendor", "EPC Integrator" used consistently.
11. **Open Conflict Table** entries to surface unresolved authority questions (per skill Step 5 §4): per-package source-row absence, building-centric emergency-lighting language vs. yard-package scope, WBS TBD, and unspecified light-pollution regulator. Record in `Guidance.md` Conflict Table only; do not modify metadata files.
12. **Status update** (per skill Step 7): if `_STATUS.md` `Current State` is `OPEN`, invoke `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`. If state is not in `ALLOW_OVERWRITE_STATES` (`OPEN,INITIALIZED`), skip status update and report.
13. **Write run record** in `_run_records/TASK_RUN_2026-05-25_<HHMM>.md` noting source rereads, pass set executed, status transition, conflicts opened, and RUN_STATUS.

## Verification

- All four documents (`Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`) exist after the run.
- Default schema sections present in each document.
- Every non-trivial value carries a citation (`SourcePath` + `SectionRef`) or is `TBD`/`ASSUMPTION` labelled.
- Identification values consistent across documents.
- Interface IDs match `INTERFACE_REGISTER.csv` rows 40-42 exactly.
- `_STATUS.md` transition is `OPEN → INITIALIZED` (Pass 1/2) or skipped with reason.
- No metadata files other than `_STATUS.md` modified.
- Run record written to `_run_records/TASK_RUN_2026-05-25_<HHMM>.md`.

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` in `{DELIVERABLE_PATH}`.
- Updated `_STATUS.md` (safe transition only).
- `_run_records/TASK_RUN_2026-05-25_<HHMM>.md` (this run record).
- Conflict Table entries in `Guidance.md` for downstream human ruling.
