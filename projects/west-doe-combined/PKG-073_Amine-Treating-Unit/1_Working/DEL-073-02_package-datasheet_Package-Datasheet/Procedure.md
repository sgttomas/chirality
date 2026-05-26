# Procedure — DEL-073-02 Package Datasheet (PKG-073 Amine Treating Unit)

> Interpretation: this procedure covers how the EPC Integrator **produces** the
> Package Datasheet artifact (`Datasheet.md`) for PKG-073 and how the artifact
> is **used** for vendor handoff.

## Purpose

To produce a complete, source-grounded EPC Package Datasheet sufficient for handoff to the PKG-073 Package Vendor, and to verify that the datasheet satisfies the requirements set out in `Specification.md`.

## Prerequisites

### Declared upstream dependencies
- None declared during PREPARATION (`_DEPENDENCIES.md`). Effective upstream dependency is the accepted PROJECT_DECOMP GATE-07 snapshot (`_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`).

### Required references
- `_CONTEXT.md`
- `_REFERENCES.md`
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` row DEL-073-02
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` row 49
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §"Amine Treating Basis" and adjacent sections
- `_Sources/26020-Package_Requirements.docx` heading 27 (binary; not parsed in this run — `TBD`)
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` (binary; not parsed in this run — `TBD`)

### Tools / actor assumptions
- Actor: EPC Integrator process/mechanical lead with project-decomposition access.
- No deterministic tools required for this skill; `tools/scaffolding/write_status.sh` is used only for the `_STATUS.md` lifecycle update.

## Steps

### S1 — Initialize datasheet identity
1. Open `_CONTEXT.md`. Copy DeliverableID, ParentPackageID, PackageName, Discipline, Type, ResponsibleParty into `Datasheet.md` §Identification.
2. From `PACKAGE_REGISTER.csv` row 49, record EquipmentTag and confirm Workbook row number.

### S2 — Capture package function and modules
1. From `PACKAGE_REGISTER.csv` row 49 "Description" and `4-25_Deepcut_DBM.md` §"Amine Treating Basis", populate `Datasheet.md` §"Package Function (Attributes)" for Module 1 (sweetening) and Module 2 (regeneration).
2. From the module tables in `4-25_Deepcut_DBM.md` (Module 520, Module 530), populate the configuration rows.

### S3 — Capture process conditions
1. Read `4-25_Deepcut_DBM.md` §"Amine Design Values" and copy temperature, hydrate margin, HC dewpoint margin, H₂S spec, CO₂ basis, mercaptan basis, and inlet H₂S into `Datasheet.md` §"Process Conditions".
2. From §"Amine Open Items and Assumptions", record amine pressure basis (7722 kPag).
3. Mark unresolved low-pressure CO₂/H₂S ratios, process-water user rates, surge tank design SG/pressure/vent, charge-pump model, reflux accumulator enrichment/dilution gas, and low-H₂S/CO₂ material selection as `TBD`.

### S4 — Capture equipment, sparing, and construction
1. From §"Amine Equipment and Design Requirements", build the equipment/sparing rows.
2. Cross-check against Module 520/530 equipment lists; reconcile discrepancies in `Guidance.md` §"Conflict Table" rather than silently choosing.

### S5 — Capture interfaces
1. From `PACKAGE_REGISTER.csv` row 49 "Applicable interface types", populate the interface bullet list in `Datasheet.md`.
2. Mark detailed interface schedule values as `TBD` until `26020-Packages_Interfaces_4_export.xlsx` is parsed.

### S6 — Specify normative requirements
1. Open `Specification.md` and confirm each R-PKG-073-02-### requirement has a single sentence statement and a cited source.
2. Confirm Verification table maps each requirement to a check method.

### S7 — Capture guidance and trade-offs
1. In `Guidance.md` document the design intent (priority of H₂S removal, MDEA trade-offs, sparing implications).
2. Surface every unresolved source-to-source disagreement in the Conflict Table; do not silently reconcile.

### S8 — Cross-document consistency sweep (Pass 2)
1. For each numeric value in `Datasheet.md`, confirm the same value appears unchanged in `Specification.md` and `Procedure.md` (where present).
2. Confirm terminology (Module 520 / 530; "amine absorber"; "lean/rich amine exchanger"; "reflux accumulator"; "amine charge pumps") is identical across documents.
3. Confirm every requirement in `Specification.md` is traceable to either `Datasheet.md` (value carrier) or `Guidance.md` (rationale carrier).
4. Confirm every interface in `Datasheet.md` is named in either R-PKG-073-02-013 or in `Guidance.md` §Considerations.

### S9 — Lifecycle update
1. Read `_STATUS.md`.
2. If `Current State == OPEN`, set state to `INITIALIZED` using `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`.
3. Otherwise, do not modify `_STATUS.md`; record the skip in the run record.

### S10 — Persist run record
1. Write `_run_records/TASK_RUN_<timestamp>.md` per AGENT_TASK contract.

## Verification

| Check | Method | Pass criterion |
|---|---|---|
| All four documents present | `ls` of deliverable folder | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` all exist |
| Default schema sections present | Visual scan of each document | Datasheet has Identification/Attributes/Conditions/Construction/References; Specification has Scope/Requirements/Standards/Verification/Documentation; Guidance has Purpose/Principles/Considerations/Trade-offs/Examples; Procedure has Purpose/Prerequisites/Steps/Verification/Records |
| Source grounding | Spot-check requirements | Each non-trivial value carries `SourcePath` + section reference or `location TBD` |
| Cross-document consistency | S8 sweep | No numeric or terminology drift between documents |
| Conflicts captured, not hidden | Open `Guidance.md` Conflict Table | All known disagreements logged with proposed authority and `TBD` ruling column |
| `_STATUS.md` lifecycle | Read `_STATUS.md` | State is `INITIALIZED` (if prior was `OPEN`) with `TASK+four-documents` author note |

## Records

The following records result from execution of this procedure:

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` (this fileset).
- `_STATUS.md` history entry (lifecycle transition).
- `_run_records/TASK_RUN_<timestamp>.md` (auditable run record).
- Conflict Table entries in `Guidance.md` (open items awaiting human ruling).
