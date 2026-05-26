# Datasheet — DEL-081-05 Vendor Document Turnover Package (PKG-081)

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-081-05_vendor-document-turnover-package` |
| Name | Vendor Document Turnover Package |
| ParentPackageID | `PKG-081` |
| Package Name | Flare KO Drum (High Pressure) 3-25 |
| Workbook Tag | `26020-02-17-001` (PACKAGE_REGISTER row 54) |
| Discipline | Mechanical |
| WBS | 02 |
| Type | Vendor Document Turnover |
| ResponsibleParty | Package Vendor (documentation) with EPC Integrator interface/integration review |
| Covers Scope Items | `SOW-0071`, `SOW-0072`, `SOW-0073`, `SOW-0074` |
| Supports Objectives | `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (ASSUMPTION: package-grouping heuristic per skill `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC`) |

## Attributes

The deliverable is a document set, not a physical artifact. Attribute values describe the document register that the Package Vendor must deliver and the EPC Integrator must accept for the HP Flare KO Drum package (two HP flare KO drums and two dedicated transfer pumps per `PACKAGE_REGISTER.csv` row 54).

| Attribute | Value | Source |
|---|---|---|
| Document register basis | Per-package `Vendor Engineering Deliverables` list defined in source `26020-Package_Requirements.docx`, package heading 34 | `_Sources/26020-Package_Requirements.docx` (location TBD — binary not text-accessible at run time) |
| Document control procedure | Vendor Document Control Procedure (`DOC-008`) required as core vendor document (ASSUMPTION: same template used by other package deliverables in this decomposition, e.g., DEL-019-05) | `_Sources/26020-Package_Requirements.docx`, "Core vendor documents" row (location TBD) |
| Index | Vendor Document Index (`PRQ-009`) required as core vendor document | same as above |
| Final book | Vendor Data Book / Final Supplier Documentation (`PRQ-016`); mechanical final book `MEC-023` | same as above |
| Quality records | Supplier Quality Plan `QLT-006`; ITP `QLT-003`; MTRs/Certificates `QLT-013`; Inspection Release Certificate `QLT-020`; Manufacturing Record Book / VDB `QLT-021` | same as above |
| Logistics records | Logistics / Shipping Plan `PRQ-013`; SPIR `PRQ-015` | same as above |
| Discipline applicability | Mechanical-led (pressure vessel + rotating equipment package); see Discipline Applicability in Specification | `PACKAGE_REGISTER.csv` row 54 (Discipline = Mechanical; WBS 02) |
| Coverage | SOW items `SOW-0071`, `SOW-0072`, `SOW-0073`, `SOW-0074` | `DELIVERABLE_REGISTER.csv` row for DEL-081-05 |
| Equipment basis | Two HP flare KO drums (V-4100-2 in compressor area; V-4150-2 in tank farm) plus two HP KO drum transfer pumps (P-4100-2, P-4150-2, 1 x 100% per KO drum) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 497, 583 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Lifecycle stage at acceptance | Post-FAT through turnover, including as-built records | `_Sources/26020-Package_Requirements.docx` (PIP-028 As-Built; MEC-022 FAT Report) — location TBD |
| Site basis affecting documentation | Cold-climate site; vendor data must reflect ambient and electrical-area conditions per facility design basis | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Comp & Liquids 3-25 plant) |
| Process service | High-pressure flare relief knock-out service; HP relief header is 508 mm / 20 in carried to a sonic HP/Cryo flare stack (660 mm OD by 60,957 mm tall) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 497, 499 |
| Acceptance gate | EPC Integrator interface/integration review and acceptance via `DEL-081-06` | `DELIVERABLE_REGISTER.csv` (DEL-081-06 row) |
| Submittal cadence | TBD — not stated in accessible source slices |
| Native file format requirements | TBD — not stated in accessible source slices |
| Budgetary go-by | A go-by reference exists at `Bid Docs/Budgetary/24292-02-PT-ENR-17-201_HP FKOD_R2.pdf` per `PACKAGE_REGISTER.csv` row 54, but the file was not located under `_Sources/` at run time; location TBD |

## Construction

The "construction" of this deliverable is the assembly and turnover of a vendor document set for the HP Flare KO Drum package. The composing document classes are taken from the standard `26020-Package_Requirements.docx` "Vendor Engineering Deliverables" template (location TBD; mirrored from sibling deliverable DEL-019-05 which uses the same template), filtered for a Mechanical-led pressure-vessel + transfer-pump package.

**Core vendor documents (always required):**

- `PRQ-009` Vendor Document Index
- `DOC-008` Vendor Document Control Procedure
- `QLT-006` Supplier Quality Plan
- `QLT-003` Inspection and Test Plan (ITP)
- `QLT-013` Material Test Reports / Certificates
- `QLT-020` Inspection Release Certificate
- `QLT-021` Manufacturing Record Book / Vendor Data Book
- `PRQ-013` Logistics / Shipping Plan
- `PRQ-015` Spare Parts Interchangeability Record (SPIR)
- `PRQ-016` Vendor Data Book / Final Supplier Documentation

**Discipline-applicable document classes (applied because PKG-081 is a Mechanical pressure-vessel + transfer-pump package; refer to Specification for the per-discipline applicability call):**

- Mechanical Equipment / Pressure Vessel (MEC-001, MEC-002, MEC-003, MEC-006, MEC-016, MEC-017, MEC-018, MEC-021, MEC-022, MEC-023, MEC-024, MEC-025) — for the HP KO drums and the transfer pumps (ASSUMPTION: same MEC IDs used by sibling DEL-019-05 derived from the common template; per-line confirmation in `DEL-081-06` review)
- Process Piping interface scope (vendor scope-of-supply termination points) — IDs TBD pending source access
- Relief / Flare / Vent interface scope — IDs TBD pending source access
- Drain / Containment interface scope — IDs TBD pending source access
- Electrical (motor data for transfer pumps): ELE class IDs as applicable to motor-driven pumps (ASSUMPTION; per-line confirmation in `DEL-081-06`)
- I&C / Control Cabling (level, pressure, temperature instrumentation and trip interfaces): INS class IDs as applicable (ASSUMPTION)
- Structural / Foundations / Supports (vessel saddles, pump skid, anchor loads): MEC/CIV class IDs as applicable (ASSUMPTION)
- Heat Tracing (EHT) and Area / Exterior Lighting interface IDs as applicable (ASSUMPTION; cold-climate site)
- Grounding / Bonding — ELE class IDs as applicable (ASSUMPTION)
- Maintenance Access — handling/maintenance documents under MEC class (ASSUMPTION)

Refer to `Specification.md` for the binding discipline applicability table for this package.

## References

- Gate 7 PROJECT_DECOMP snapshot deliverable row: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` (DEL-081-05 row)
- Gate 7 PROJECT_DECOMP snapshot package row: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` row 54 (PKG-081, tag `26020-02-17-001`)
- `_Sources/26020-Package_Requirements.docx` — "Vendor Engineering Deliverables" section and package heading 34 (binary; specific clause locations TBD)
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — Workbook Packages row 54 (binary; specific cell locations TBD)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — facility design basis (lines 497, 499, 583, 584 enumerate HP KO drum equipment count, sizing, and transfer pump configuration for the 3-25 plant)
- Sibling-template reference (PROVENANCE for ASSUMPTION-labeled rows): `projects/west-doe-combined/PKG-019_*/.../DEL-019-05_vendor-document-turnover-package_*/Datasheet.md`, `.../Specification.md` — used to mirror the standard core/discipline ID set when source slices are not text-accessible
- Deliverable-local: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`
