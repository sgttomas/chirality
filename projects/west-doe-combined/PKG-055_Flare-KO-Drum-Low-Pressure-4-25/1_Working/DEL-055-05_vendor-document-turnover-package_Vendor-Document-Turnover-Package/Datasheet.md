# Datasheet — DEL-055-05 Vendor Document Turnover Package (PKG-055)

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-055-05_vendor-document-turnover-package` |
| Name | Vendor Document Turnover Package |
| ParentPackageID | `PKG-055` |
| Package Name | Flare KO Drum (Low Pressure) 4-25 |
| Discipline | Mechanical |
| Type | Vendor Document Turnover |
| ResponsibleParty | Package Vendor (documentation) with EPC Integrator interface/integration review |
| Covers Scope Items | `SOW-0083`, `SOW-0084`, `SOW-0085`, `SOW-0086` |
| Supports Objectives | `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (ASSUMPTION: package-grouping heuristic per skill `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC`) |

## Attributes

The deliverable is a document set, not a physical artifact. Attribute values describe the document register that the Package Vendor must deliver and the EPC Integrator must accept for the LP Flare KO Drum package (one LP flare KO drum V-3900-1 and one dedicated transfer pump P-3900-1 per `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2581-2582 and 2535).

| Attribute | Value | Source |
|---|---|---|
| Document register basis | Per-package `Vendor Engineering Deliverables` list defined in source `26020-Package_Requirements.docx`, package heading 10 | `_Sources/26020-Package_Requirements.docx` (location TBD — binary not text-accessible at run time) |
| Document control procedure | Vendor Document Control Procedure (`DOC-008`) required as core vendor document (ASSUMPTION: same template used by other package deliverables in this decomposition, e.g., DEL-081-05) | `_Sources/26020-Package_Requirements.docx`, "Core vendor documents" row (location TBD) |
| Index | Vendor Document Index (`PRQ-009`) required as core vendor document | same as above |
| Final book | Vendor Data Book / Final Supplier Documentation (`PRQ-016`); mechanical final book `MEC-023` | same as above |
| Quality records | Supplier Quality Plan `QLT-006`; ITP `QLT-003`; MTRs/Certificates `QLT-013`; Inspection Release Certificate `QLT-020`; Manufacturing Record Book / VDB `QLT-021` | same as above |
| Logistics records | Logistics / Shipping Plan `PRQ-013`; SPIR `PRQ-015` | same as above |
| Discipline applicability | Mechanical-led (pressure vessel + rotating equipment package); see Discipline Applicability in Specification | `_CONTEXT.md` (Discipline = Mechanical) |
| Coverage | SOW items `SOW-0083`, `SOW-0084`, `SOW-0085`, `SOW-0086` | `DELIVERABLE_REGISTER.csv` row for DEL-055-05 |
| Equipment basis | One LP flare KO drum (V-3900-1) plus one LP KO drum transfer pump (P-3900-1) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2535, 2581-2582 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Lifecycle stage at acceptance | Post-FAT through turnover, including as-built records | `_Sources/26020-Package_Requirements.docx` (PIP-028 As-Built; MEC-022 FAT Report) — location TBD |
| Site basis affecting documentation | Cold-climate site (4-25 Deepcut plant); vendor data must reflect ambient and electrical-area conditions per facility design basis | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (4-25 Deepcut plant) |
| Process service | Low-pressure flare relief knock-out service for LP equipment including amine regeneration, TEG regeneration, VRU, and reciprocating compressor seal pot; LP relief header is 508 mm / 20 in; LP element piggy-backs on the common HP/cryo flare stack | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2029, 2031 |
| Acceptance gate | EPC Integrator interface/integration review and acceptance via `DEL-055-06` | `DELIVERABLE_REGISTER.csv` (DEL-055-06 row) |
| Submittal cadence | TBD — not stated in accessible source slices |
| Native file format requirements | TBD — not stated in accessible source slices |
| Modularization basis | "390-1 LP Flare KO Drum Module" is shop-built per the 4-25 module list, which affects shipping-plan and skid-level documentation expectations | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2783 |

## Construction

The "construction" of this deliverable is the assembly and turnover of a vendor document set for the LP Flare KO Drum package. The composing document classes are taken from the standard `26020-Package_Requirements.docx` "Vendor Engineering Deliverables" template (location TBD; mirrored from sibling deliverable DEL-081-05 which uses the same template), filtered for a Mechanical-led pressure-vessel + transfer-pump package.

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

**Discipline-applicable document classes (applied because PKG-055 is a Mechanical pressure-vessel + transfer-pump package; refer to Specification for the per-discipline applicability call):**

- Mechanical Equipment / Pressure Vessel (MEC-001, MEC-002, MEC-003, MEC-006, MEC-016, MEC-017, MEC-018, MEC-021, MEC-022, MEC-023, MEC-024, MEC-025) — for the LP KO drum and the transfer pump (ASSUMPTION: same MEC IDs used by sibling DEL-081-05 derived from the common template; per-line confirmation in `DEL-055-06`)
- Process Piping interface scope (vendor scope-of-supply termination points) — IDs TBD pending source access
- Relief / Flare / Vent interface scope — IDs TBD pending source access
- Drain / Containment interface scope — IDs TBD pending source access
- Electrical (motor data for the transfer pump): ELE class IDs as applicable to motor-driven pumps (ASSUMPTION; per-line confirmation in `DEL-055-06`)
- I&C / Control Cabling (level, pressure, temperature instrumentation and trip interfaces): INS class IDs as applicable (ASSUMPTION)
- Structural / Foundations / Supports (vessel saddles, pump skid, anchor loads): MEC/CIV class IDs as applicable (ASSUMPTION)
- Heat Tracing (EHT) and Area / Exterior Lighting interface IDs as applicable (ASSUMPTION; cold-climate site)
- Grounding / Bonding — ELE class IDs as applicable (ASSUMPTION)
- Maintenance Access — handling/maintenance documents under MEC class (ASSUMPTION)

Refer to `Specification.md` for the binding discipline applicability table for this package.

## References

- Gate 7 PROJECT_DECOMP snapshot deliverable row: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` (DEL-055-05 row)
- Gate 7 PROJECT_DECOMP snapshot package register: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` (PKG-055)
- `_Sources/26020-Package_Requirements.docx` — "Vendor Engineering Deliverables" section and package heading 10 (binary; specific clause locations TBD)
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — Workbook Packages row 57 (binary; specific cell locations TBD)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — facility design basis (lines 2029, 2031, 2535, 2581-2582, 2783 enumerate LP flare KO drum equipment, header sizing, stack configuration, and shop-built modularization for the 4-25 plant)
- Sibling-template reference (PROVENANCE for ASSUMPTION-labeled rows): `projects/west-doe-combined/PKG-081_*/.../DEL-081-05_vendor-document-turnover-package_*/Datasheet.md`, `.../Specification.md` — used to mirror the standard core/discipline ID set when source slices are not text-accessible
- Deliverable-local: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`
