# Datasheet: DEL-027-06_epc-vendor-package-review-and-acceptance

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-027-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Type | EPC Vendor Package Acceptance | `DELIVERABLE_REGISTER.csv` |
| ParentPackageID | `PKG-027` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package Name | Transformer TXP-8301-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 20/26MVA 13.8kV/6.9kV/0.4kV | Workbook Packages row 29; `PACKAGE_REGISTER.csv` |
| Workbook Row | 29 | `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` |
| CoA Tracking Number | 26020-01-30-018 | `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | `PACKAGE_REGISTER.csv`; `_CONTEXT.md` |
| Responsible Party | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Covers Scope Items | `SOW-0028` | `DELIVERABLE_REGISTER.csv`; `_CONTEXT.md` |
| Supports Objectives | `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-008`, `OBJ-009`, `OBJ-010` | `DELIVERABLE_REGISTER.csv`; `_CONTEXT.md` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Deliverable role | EPC-integrator-side review, integration acceptance, and handoff-readiness evidence for the vendor-supplied `PKG-027` transformer package (TXP-8301-1). | `DELIVERABLE_REGISTER.csv`; `_CONTEXT.md` |
| Acceptance basis | EPC Scope of Work, Package Datasheet (`DEL-027-02`), and Construction Work Package (`DEL-027-03`). | `_CONTEXT.md` |
| Anticipated artifacts | Vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Coordination mode | DECLARED | `_DEPENDENCIES.md` |
| Declared upstream | None declared during PREPARATION. | `_DEPENDENCIES.md` |
| Declared downstream | None declared during PREPARATION. | `_DEPENDENCIES.md` |
| Applicable interfaces (package) | Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. | `INTERFACE_REGISTER.csv` rows for `PKG-027` |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Responsibility split | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility integration. | `PACKAGE_REGISTER.csv` row `PKG-027` |
| Source set for acceptance criteria | EPC Scope of Work for `PKG-027` (TBD — not in accessible source set); Package Datasheet `DEL-027-02` (in-project, not yet drafted); Construction Work Package `DEL-027-03` (in-project, not yet drafted); applicable Gate 7 registers; DBM-Deepcut electrical slices (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`). | `_REFERENCES.md`; `_CONTEXT.md` |
| Vendor deliverables to be reviewed | Vendor design documentation, certified drawings, FAT records (no-load loss, load loss/impedance, ratio, polarity, dielectric, induced voltage, temperature rise as applicable), installation/operation manuals, spare parts and warranty data (item set TBD pending vendor data list). | ASSUMPTION grounded in deliverable type `EPC Vendor Package Acceptance` and standard oil-filled distribution transformer FAT practice. |
| Transformer service basis (package-level) | Step-down distribution transformer rated 20/26 MVA, primary 13.8 kV, secondaries 6.9 kV / 0.4 kV; project medium-voltage system is low-resistance grounded with 100 A, 10 s neutral grounding resistor on each 6.9 kV transformer; 600 V transformers (not this unit) use 5 A continuous high-resistance grounding. The 0.4 kV winding voltage on this unit is non-standard relative to the DBM voltage hierarchy and is recorded from the package title as `ASSUMPTION` pending vendor data. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §Electrical (lines ~2917, 2933-2937, 2985); `PACKAGE_REGISTER.csv`; `_CONTEXT.md` |

## Construction

| Element | Value | Source |
|---|---|---|
| Production unit | Single deliverable folder under `PKG-027/1_Working`. | `_CONTEXT.md` |
| Document set | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, plus deliverable-local metadata. | Skill contract `four-documents`; this run. |
| Acceptance evidence container | Vendor document review log + acceptance checklist (seven interfaces) + test/inspection evidence + turnover evidence (file shapes TBD until EPC procedure is confirmed). | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Status gate (this run) | `OPEN` → `INITIALIZED` on successful Pass 1+2. | `_STATUS.md`; `four-documents/SKILL.md` Step 7 |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- Gate 7 PROJECT_DECOMP snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `PACKAGE_REGISTER.csv` row `PKG-027`
  - `DELIVERABLE_REGISTER.csv` row `DEL-027-06_epc-vendor-package-review-and-acceptance`
  - `INTERFACE_REGISTER.csv` rows for `PKG-027` (seven interface rows)
  - `OBJECTIVE_DELIVERABLE_MAP.csv`
- Workbook Packages row 29: `_Sources/26020-Packages_Interfaces_4_export.xlsx`
- Companion deliverables in `PKG-027/1_Working/`:
  - `DEL-027-01_scope-of-work` (Scope of Work) — provisional, status TBD
  - `DEL-027-02_package-datasheet` (Package Datasheet) — not yet drafted at this run
  - `DEL-027-03_construction-work-package` (Construction Work Package) — not yet drafted at this run
  - `DEL-027-04_vendor-engineered-equipment-package`
  - `DEL-027-05_vendor-document-turnover-package`
- DBM electrical context: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (medium-voltage distribution and grounding basis)
- EPC Scope of Work, vendor data package: not present in accessible source set — `location TBD`.
