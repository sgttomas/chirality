# Datasheet — DEL-033-05 Vendor Document Turnover Package (PKG-033)

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-033-05_vendor-document-turnover-package` |
| Name | Vendor Document Turnover Package |
| ParentPackageID | `PKG-033` |
| Package Name | 4160V SWITCHGEAR ELECTRICAL BUILDING (830-2) |
| Workbook Tag | `26020-02-30-024` (PACKAGE_REGISTER row, workbook row 35) |
| Discipline | Electrical |
| WBS | 02 |
| Type | Vendor Document Turnover |
| ResponsibleParty | Package Vendor (vendor documentation) with EPC Integrator interface/integration review |
| Covers Scope Items | `SOW-0034` |
| Supports Objectives | `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` |

## Attributes

The deliverable is a document set rather than a physical artifact. Attribute values describe the document register that the Package Vendor must deliver and the EPC Integrator must accept for the 4160V Switchgear Electrical Building (830-2).

| Attribute | Value | Source |
|---|---|---|
| Document register basis | Per-package `Vendor Engineering Deliverables` list defined in source `26020-Package_Requirements.docx` | `_Sources/26020-Package_Requirements.docx`, section "Vendor Engineering Deliverables" |
| Document control procedure | Vendor Document Control Procedure (`DOC-008`) required as core vendor document | `_Sources/26020-Package_Requirements.docx`, "Core vendor documents" row |
| Index | Vendor Document Index (`PRQ-009`) required as core vendor document | same as above |
| Final book | Vendor Data Book / Final Supplier Documentation (`PRQ-016`); mechanical final book `MEC-023` where building/skid handling applies | same as above |
| Quality records | Supplier Quality Plan `QLT-006`; ITP `QLT-003`; MTRs/Certificates `QLT-013`; Inspection Release Certificate `QLT-020`; Manufacturing Record Book / VDB `QLT-021` | same as above |
| Logistics records | Logistics / Shipping Plan `PRQ-013`; SPIR `PRQ-015` | same as above |
| Discipline applicability | Electrical-led (medium-voltage switchgear lineup housed in a vendor-supplied electrical building); see Discipline Applicability table in Specification | `PACKAGE_REGISTER.csv` PKG-033 row; `_Sources/26020-Package_Requirements.docx` |
| Coverage | Single SOW item `SOW-0034` | `DELIVERABLE_REGISTER.csv` DEL-033-05 row |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Lifecycle stage at acceptance | Post-FAT through turnover, including as-built records and energization package | `_Sources/26020-Package_Requirements.docx` (PIP-028 As-Built; MEC-022 FAT Report; ELE-029/ELE-030 FAT / Energization Package) |
| Site basis affecting documentation | Cold-climate site with -40 deg C to +35 deg C design ambient (DBM SEC-02 referenced in SEC-11); Class I Zone 2, Gas Groups IIA/IIB area-classification basis with electrical buildings coordinated to area classification and ventilation | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 686, 720-727, 764-770 |
| Service voltage | 4,160 V, 3 phase, 3 wire, 60 Hz LRG (DBM SEC-12 system voltages) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 730-734 |
| Acceptance gate | EPC Integrator interface/integration review and acceptance via `DEL-033-06` | `DELIVERABLE_REGISTER.csv` DEL-033-05 and DEL-033-06 rows |
| Submittal cadence | TBD — not stated in accessible source slices |
| Native file format requirements | TBD — not stated in accessible source slices |

## Construction

The "construction" of this deliverable is the assembly and turnover of a vendor document set for a packaged 4160V switchgear lineup housed in a vendor-supplied electrical building. The composing document classes are taken directly from `_Sources/26020-Package_Requirements.docx` "Vendor Engineering Deliverables" template.

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

**Discipline-applicable document classes (applied because PKG-033 is a medium-voltage switchgear lineup delivered inside a vendor-supplied electrical building; refer to Specification for the per-discipline applicability call):**

- Electrical (ELE-002, ELE-003, ELE-011 protective relaying / coordination as applicable, ELE-012, ELE-014, ELE-015, ELE-016, ELE-017 integral lighting, ELE-019, ELE-020, ELE-027, ELE-028, ELE-029, ELE-030)
- Instrumentation and Controls (INS-002, INS-003, INS-005, INS-006, INS-008, INS-009 — ASSUMPTION: applicable because switchgear includes protection, metering, control, and PCN/data interfaces consistent with DBM SEC-12 4160V MCC EtherNet PLC interface; confirm during EPC integration review)
- Mechanical Equipment / Building (MEC-001, MEC-002, MEC-003, MEC-006, MEC-016, MEC-017, MEC-018, MEC-021, MEC-022, MEC-023, MEC-024, MEC-025) for the electrical building enclosure, HVAC equipment, lifting and handling, and packaged-equipment IOM — ASSUMPTION pending source confirmation
- Building services (HVAC, fire/gas detection, building heaters, lighting) where the vendor supplies them integral to the building — ASSUMPTION; see DBM SEC-11 buildings discussion

## References

- Gate 7 PROJECT_DECOMP snapshot deliverable row: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` (`DEL-033-05_vendor-document-turnover-package`)
- Gate 7 PROJECT_DECOMP snapshot package row: `.../PACKAGE_REGISTER.csv` (`PKG-033`, tag `26020-02-30-024`)
- `_Sources/26020-Package_Requirements.docx` — "Vendor Engineering Deliverables" section (core vendor documents and per-discipline deliverable IDs)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — facility design basis (line 617 enumerates vendor document registers among required package deliverables; lines 686, 720-727, 730-756, 764-770 establish site basis, area classification, system voltages, 4160V MCC/switchgear context, and electrical-building requirements)
- Deliverable-local: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`
