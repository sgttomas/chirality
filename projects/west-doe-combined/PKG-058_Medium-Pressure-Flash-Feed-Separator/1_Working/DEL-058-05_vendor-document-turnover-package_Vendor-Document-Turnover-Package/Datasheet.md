# Datasheet — DEL-058-05 Vendor Document Turnover Package (PKG-058)

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-058-05_vendor-document-turnover-package` |
| Name | Vendor Document Turnover Package |
| ParentPackageID | `PKG-058` |
| Package Name | Medium Pressure Flash Feed Separator (MPFF) |
| Workbook reference | Workbook Packages row 71; `26020-Package_Requirements.docx` package heading 13 |
| Discipline | Mechanical |
| Type | Vendor Document Turnover |
| ResponsibleParty | Package Vendor (vendor documentation) with EPC Integrator interface/integration review |
| Covers Scope Items | `SOW-0139`, `SOW-0140`, `SOW-0141`, `SOW-0142` |
| Supports Objectives | `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (ASSUMPTION — package-grouping heuristic per `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC`) |

## Attributes

The deliverable is a document set rather than a physical artifact. Attribute values describe the document register that the Package Vendor must deliver and the EPC Integrator must accept for the MPFF package.

| Attribute | Value | Source |
|---|---|---|
| Document register basis | Per-package `Vendor Engineering Deliverables` list defined in source `26020-Package_Requirements.docx` (package heading 13, MPFF) | `_Sources/26020-Package_Requirements.docx`, "Vendor Engineering Deliverables" section |
| Document control procedure | Vendor Document Control Procedure (`DOC-008`) required as core vendor document | `_Sources/26020-Package_Requirements.docx`, "Core vendor documents" |
| Index | Vendor Document Index (`PRQ-009`) required as core vendor document | same as above |
| Final book | Vendor Data Book / Final Supplier Documentation (`PRQ-016`); mechanical final book `MEC-023` | same as above |
| Quality records | Supplier Quality Plan `QLT-006`; ITP `QLT-003`; MTRs/Certificates `QLT-013`; Inspection Release Certificate `QLT-020`; Manufacturing Record Book / VDB `QLT-021` | same as above |
| Logistics records | Logistics / Shipping Plan `PRQ-013`; SPIR `PRQ-015` | same as above |
| Discipline applicability | Mechanical-led (pressure-equipment / packaged separator with internals, mist eliminator, instrumentation, building enclosure); see Specification | `PACKAGE_REGISTER` row for PKG-058; `_Sources/26020-Package_Requirements.docx` |
| Coverage | Four SOW items `SOW-0139`–`SOW-0142` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Lifecycle stage at acceptance | Post-FAT through turnover, including as-built records | `_Sources/26020-Package_Requirements.docx` (FAT, As-Built, final book rows) |
| Process service | Hydrocarbon liquid + flashed vapour service; MPFF receives HP hydrocarbon liquid from inlet separators via common header, level-controlled into MPFF vessels; overheads pressure-regulated to SOC third-stage suction | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 668, 672 |
| Site basis affecting documentation | Cold-climate site; vendor data must reflect ambient and electrical-area conditions per facility design basis; methanol injection on MPFF feed retained as hydrate safeguard | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 630, 674 |
| Vessel internals basis | MPFF internals are Mistex; no internal coating is specified for the MPFF | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 672 |
| Building enclosure | MPFF package is configured similarly to inlet separator with a self-framing building enclosing instrumentation and one end of the vessel | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 672 |
| Automated blowdown | Automated blowdown valve required on MPFF | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 672 |
| Acceptance gate | EPC Integrator interface/integration review and acceptance via `DEL-058-06` | `DELIVERABLE_REGISTER.csv`; `_CONTEXT.md` |
| Submittal cadence | TBD — not stated in accessible source slices |
| Native file format requirements | TBD — not stated in accessible source slices |
| Specific MPFF design pressure / temperature / dimensions | TBD — drive from Package Datasheet (`DEL-058-02`) and engineered package (`DEL-058-04`) once issued |

## Construction

The "construction" of this deliverable is the assembly and turnover of a vendor document set. The composing document classes are taken directly from `_Sources/26020-Package_Requirements.docx` "Vendor Engineering Deliverables" template, filtered for an MPFF (mechanical pressure-equipment) package.

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

**Discipline-applicable document classes (applied because PKG-058 is a Mechanical packaged separator with associated piping, instrumentation, and electrical/lighting for the enclosure — refer to Specification for the binding per-line applicability):**

- Mechanical Equipment (`MEC-001`, `MEC-002`, `MEC-003`, `MEC-006`, `MEC-016`, `MEC-017`, `MEC-018`, `MEC-021`, `MEC-022`, `MEC-023`, `MEC-024`, `MEC-025`) — primary; the MPFF vessel and skid are the engineered article
- Pressure Equipment / Code Vessel data (vessel datasheet, U-1A or jurisdictional equivalent, design calculations, NDE reports, hydrotest records) — ASSUMPTION applicable because the MPFF is a pressure vessel in hydrocarbon service; exact source IDs `TBD` until detailed Vendor Engineering Deliverables list is re-read at production time
- Piping (skid-edge piping, hookups, isometrics) — applicable for the skid; per-line IDs `TBD`
- Instrumentation and Controls (`INS-002`, `INS-003`, `INS-005`, `INS-006`, `INS-008`, `INS-009`, and remaining INS entries) — applicable for level control, pressure control, overhead vapour PCV to SOC, automated blowdown valve, hydrate-suppression methanol injection instrumentation
- Electrical / Lighting / Grounding (`ELE-002`, `ELE-003`, `ELE-014`, `ELE-015`, `ELE-016`, `ELE-017` lighting if integral, `ELE-019`, `ELE-020`, `ELE-027`, `ELE-028`, `ELE-029`, `ELE-030`) — applicable for the self-framing building enclosure, instrumentation power, heat-trace if any
- Structural / Foundations / Supports — applicable for skid steel and anchorage; per-line IDs `TBD`
- Civil/foundation interface data — applicable for vendor-supplied loads to civil; per-line IDs `TBD`

Refer to `Specification.md` for the binding discipline applicability table for this package.

## References

- Gate 7 PROJECT_DECOMP snapshot deliverable register: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` (row for `DEL-058-05_vendor-document-turnover-package`)
- Gate 7 PROJECT_DECOMP snapshot package register: `.../PACKAGE_REGISTER.csv` (row for `PKG-058`)
- `_Sources/26020-Package_Requirements.docx` — "Vendor Engineering Deliverables" section and package heading 13 (MPFF)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — MPFF process basis, including lines 668 (MPFF feed source), 672 (overheads, internals, blowdown, enclosure), 674 (heater bundle / methanol injection), 658 (per-MPFF flow basis)
- Deliverable-local: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`
