# Datasheet — DEL-041-05 Vendor Document Turnover Package (PKG-041)

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-041-05_vendor-document-turnover-package` |
| Name | Vendor Document Turnover Package |
| ParentPackageID | `PKG-041` |
| Package Name | 13.8kV, 3.0MW STANDBY GENERATOR BUILDING (490-1) |
| Workbook Tag | `26020-01-30-032` (PACKAGE_REGISTER row 43) |
| Discipline | Electrical |
| WBS | 01 |
| Type | Vendor Document Turnover |
| ResponsibleParty | Package Vendor (vendor documentation) with EPC Integrator interface/integration review |
| Covers Scope Items | `SOW-0042` |
| Supports Objectives | `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` |

## Attributes

The deliverable is a document set rather than a physical artifact. Attribute values describe the document register that the Package Vendor must deliver and the EPC Integrator must accept for the 490-1 standby generator building package.

| Attribute | Value | Source |
|---|---|---|
| Document register basis | Per-package "Vendor Engineering Deliverables" list defined in source `26020-Package_Requirements.docx` | `_Sources/26020-Package_Requirements.docx`, section "Vendor Engineering Deliverables" |
| Document control procedure | Vendor Document Control Procedure (`DOC-008`) required as core vendor document | `_Sources/26020-Package_Requirements.docx`, "Core vendor documents" |
| Index | Vendor Document Index (`PRQ-009`) required as core vendor document | same as above |
| Final book | Vendor Data Book / Final Supplier Documentation (`PRQ-016`); discipline final books as applicable (`MEC-023`, `ELE-030`) | same as above |
| Quality records | Supplier Quality Plan `QLT-006`; ITP `QLT-003`; MTRs/Certificates `QLT-013`; Inspection Release Certificate `QLT-020`; Manufacturing Record Book / VDB `QLT-021` | same as above |
| Logistics records | Logistics / Shipping Plan `PRQ-013`; SPIR `PRQ-015` | same as above |
| Discipline applicability | Electrical-led packaged generator building (genset, switchgear/MCC interface, transfer-switch interface, enclosure, controls) with significant Mechanical (engine, enclosure, fuel, cooling), I&C, Structural, and limited Civil/Piping content as the building is delivered as a packaged module | `PACKAGE_REGISTER.csv` row 43; `_Sources/26020-Package_Requirements.docx`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2076–2083, 2787 |
| Coverage | Single SOW item `SOW-0042` | `DELIVERABLE_REGISTER.csv` row 232 |
| Delivery form | Vendor-supplied weather-protective enclosure suitable for outdoor installation (per facility design basis for emergency-power generator package) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2076 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Lifecycle stage at acceptance | Post-FAT through site turnover, including as-built records | `_Sources/26020-Package_Requirements.docx` (PIP-028 As-Built; MEC-022 FAT Report; ELE-030 Energization Package) |
| Site basis affecting documentation | Cold-climate site (4-25 Deepcut); vendor data must reflect ambient, electrical-area, and access conditions per facility design basis; 1 m access walkway shall be maintained around the enclosure | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2076–2083 |
| Acceptance gate | EPC Integrator interface/integration review and acceptance via `DEL-041-06` | `DELIVERABLE_REGISTER.csv` rows 232, 233 |
| Submittal cadence | TBD — not stated in accessible source slices |
| Native file format requirements | TBD — not stated in accessible source slices |
| Voltage/rating reconciliation status | Package title states "13.8kV, 3.0MW"; current DBM basis (line 2943) states the standby-power basis has shifted to TOU low-voltage standby generators with transfer switches at the 600 V MCC level, superseding the prior centralized 13.8 kV emergency-generator concept for this facility scope. See Conflict Table HRR-041-05-001. | `PACKAGE_REGISTER.csv` row 43; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2076, 2083, 2943, 3086 |

## Construction

The "construction" of this deliverable is the assembly and turnover of a vendor document set for the 490-1 standby generator building package. The composing document classes are taken directly from `_Sources/26020-Package_Requirements.docx` "Vendor Engineering Deliverables" template.

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

**Discipline-applicable document classes (applied because PKG-041 is an Electrical-led packaged standby generator building delivered as a vendor-engineered module; refer to Specification for the per-discipline applicability call):**

- Electrical (`ELE-002`, `ELE-003`, `ELE-014`, `ELE-015`, `ELE-016`, `ELE-019`, `ELE-020`, `ELE-027`, `ELE-028`, `ELE-029`, `ELE-030`, `ELE-011`, `ELE-012`) for generator electrical scope, switchgear/MCC interface, transfer-switch interface, grounding, and energization
- Instrumentation and Controls (`INS-002`, `INS-003`, `INS-005`, `INS-006`, `INS-008`, `INS-009`, and subsequent INS entries — ASSUMPTION: applicable because the genset package includes engine controls, monitoring, alarms, and trip interfaces to the facility control system; confirm during EPC integration review)
- Mechanical Equipment (`MEC-001`, `MEC-002`, `MEC-003`, `MEC-006`, `MEC-016`, `MEC-017`, `MEC-018`, `MEC-021`, `MEC-022`, `MEC-023`, `MEC-024`, `MEC-025`) for the engine, enclosure, cooling, exhaust, and fuel-system mechanical content
- Structural / Building (applicable subset of the source's structural/foundation document classes — ASSUMPTION: applicable because the deliverable is a building/enclosure; the EPC Integrator confirms specific line items)
- Civil / Foundations / Drainage (limited applicability — ASSUMPTION: civil pad and drainage tie-ins are owned by the EPC Integrator rather than the Package Vendor; confirm in `DEL-041-06`)
- HVAC / Building services (enclosure ventilation, heating, fire/gas, lighting as integral to the module) — ASSUMPTION

Refer to `Specification.md` for the binding discipline applicability table for this package.

## References

- Gate 7 PROJECT_DECOMP snapshot deliverable row: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv`, row 232 (`DEL-041-05_vendor-document-turnover-package`)
- Gate 7 PROJECT_DECOMP snapshot package row: `.../PACKAGE_REGISTER.csv`, row 43 (`PKG-041`, tag `26020-01-30-032`)
- `_Sources/26020-Package_Requirements.docx` — "Vendor Engineering Deliverables" section (core vendor documents and per-discipline deliverable IDs)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — facility design basis (lines 2076–2083 emergency-power generator enclosure/access basis; line 2787 "490-1 Emergency Generator Module — Shop — Part of vendor package"; lines 2943, 3086 standby-generator basis change and open items)
- Deliverable-local: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`
