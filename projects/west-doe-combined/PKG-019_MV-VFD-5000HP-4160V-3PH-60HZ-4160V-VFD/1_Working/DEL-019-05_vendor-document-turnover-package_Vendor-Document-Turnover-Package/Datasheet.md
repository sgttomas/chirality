# Datasheet — DEL-019-05 Vendor Document Turnover Package (PKG-019)

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-019-05_vendor-document-turnover-package` |
| Name | Vendor Document Turnover Package |
| ParentPackageID | `PKG-019` |
| Package Name | MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD |
| Workbook Tag | `26020-02-30-009` (PACKAGE_REGISTER row 21) |
| Discipline | Electrical |
| WBS | 02 |
| Type | Vendor Document Turnover |
| ResponsibleParty | Package Vendor (documentation) with EPC Integrator review |
| Covers Scope Items | `SOW-0020` |
| Supports Objectives | `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-008`, `OBJ-009`, `OBJ-010` |

## Attributes

The deliverable is a document set rather than a physical artifact. Attribute values describe the document register that the Package Vendor must deliver and the EPC Integrator must accept.

| Attribute | Value | Source |
|---|---|---|
| Document register basis | Per-package `Vendor Engineering Deliverables` list defined in source `26020-Package_Requirements.docx` | `_Sources/26020-Package_Requirements.docx`, section "Vendor Engineering Deliverables" |
| Document control procedure | Vendor Document Control Procedure (`DOC-008`) required as core vendor document | `_Sources/26020-Package_Requirements.docx`, "Core vendor documents" row |
| Index | Vendor Document Index (`PRQ-009`) required as core vendor document | same as above |
| Final book | Vendor Data Book / Final Supplier Documentation (`PRQ-016`); mechanical final book `MEC-023` | same as above |
| Quality records | Supplier Quality Plan `QLT-006`; ITP `QLT-003`; MTRs/Certificates `QLT-013`; Inspection Release Certificate `QLT-020`; Manufacturing Record Book / VDB `QLT-021` | same as above |
| Logistics records | Logistics / Shipping Plan `PRQ-013`; SPIR `PRQ-015` | same as above |
| Discipline applicability | Electrical-led (motor-driven VFD package); see Discipline Applicability table in Specification | `PACKAGE_REGISTER.csv` row 21; `_Sources/26020-Package_Requirements.docx` |
| Coverage | Single SOW item `SOW-0020` | `DELIVERABLE_REGISTER.csv` row 100 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Lifecycle stage at acceptance | Post-FAT through turnover, including as-built records | `_Sources/26020-Package_Requirements.docx` (PIP-028 As-Built; MEC-022 FAT Report; ELE-030 Energization Package) |
| Site basis affecting documentation | Cold-climate site; vendor data must reflect ambient and electrical-area conditions per facility design basis | `_Sources/26020-Package_Requirements.docx` (site basis statements); `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |
| Acceptance gate | EPC Integrator interface/integration review and acceptance via `DEL-019-06` | `DELIVERABLE_REGISTER.csv` rows 100, 101 |
| Submittal cadence | TBD — not stated in accessible source slices |
| Native file format requirements | TBD — not stated in accessible source slices |

## Construction

The "construction" of this deliverable is the assembly and turnover of a vendor document set. The composing document classes are taken directly from `_Sources/26020-Package_Requirements.docx` "Vendor Engineering Deliverables" template.

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

**Discipline-applicable document classes (applied because PKG-019 is a Medium-Voltage VFD electrical package; refer to Specification for the per-discipline applicability call):**

- Electrical (ELE-002, ELE-003, ELE-014, ELE-015, ELE-016, ELE-020, ELE-027, ELE-028, ELE-029, ELE-030, ELE-012, ELE-019, ELE-011)
- Instrumentation and Controls (INS-002, INS-003, INS-005, INS-006, INS-008, INS-009, and subsequent INS entries — ASSUMPTION: applicable because VFDs include control, monitoring, and trip interfaces; confirm during EPC integration review)
- Mechanical Equipment (MEC-001, MEC-002, MEC-003, MEC-006, MEC-016, MEC-017, MEC-018, MEC-021, MEC-022, MEC-023, MEC-024, MEC-025) for the VFD enclosure/skid as ASSUMPTION

Refer to `Specification.md` for the binding discipline applicability table for this package.

## References

- Gate 7 PROJECT_DECOMP snapshot deliverable row: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv`, row 100 (`DEL-019-05_vendor-document-turnover-package`)
- Gate 7 PROJECT_DECOMP snapshot package row: `.../PACKAGE_REGISTER.csv`, row 21 (`PKG-019`, tag `26020-02-30-009`)
- `_Sources/26020-Package_Requirements.docx` — "Vendor Engineering Deliverables" section (core vendor documents and per-discipline deliverable IDs)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — facility design basis (line 617 explicitly enumerates vendor document registers among required package deliverables; lines 324, 326, 533, 756 give VFD basis context)
- Deliverable-local: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`
