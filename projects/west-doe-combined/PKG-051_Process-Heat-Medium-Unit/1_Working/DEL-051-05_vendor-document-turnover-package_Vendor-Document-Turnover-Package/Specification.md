# Specification: DEL-051-05 — Vendor Document Turnover Package

## Scope

### In scope
- A consolidated **Vendor Document Register** indexing every vendor-produced document for package `26020-01-PT-15-001` (Process Heat Medium Unit) — including engineering, quality, fabrication, FAT, IOM, spares, and final data-book material. (Source: `26020-Package_Requirements.docx` §6 Vendor Engineering Deliverables.)
- Controlled **vendor document submittals** for review by the EPC Integrator (interface/integration review) per the EPC Scope of Work (DEL-051-01) and Package Datasheet (DEL-051-02). (Source: `DELIVERABLE_REGISTER.csv` row DEL-051-05.)
- Source-required vendor documentation listed under the package's Vendor Engineering Deliverables in `26020-Package_Requirements.docx` §6. Individual source-row documents are carried as artifacts/evidence within this package, not as separate deliverables. (Source: `_CONTEXT.md` Notes; `DELIVERABLE_REGISTER.csv`.)
- **Turnover records** culminating in the Vendor Data Book (PRQ-016) and Mechanical Final Documentation (MEC-023). (Source: `26020-Package_Requirements.docx` §6.)

### Out of scope
- Engineering, fabrication, FAT execution, and physical equipment supply — covered by DEL-051-04 (Vendor Engineered Equipment Package). (Source: `DELIVERABLE_REGISTER.csv`.)
- EPC integration review acceptance decisions — performed under the EPC Vendor Package Review and Acceptance deliverable for this package family (ASSUMPTION: typical pattern, e.g. DEL-051-06; not explicitly named in `_CONTEXT.md`).
- Construction work-package installation and tie-in — covered by DEL-051-03 (Construction Work Package). (Source: `DELIVERABLE_REGISTER.csv`.)

## Requirements

| Req ID | Requirement | Source / Basis |
|---|---|---|
| R-01 | A Vendor Document Index (PRQ-009) shall be issued and maintained for the package; it shall enumerate every document submittal listed under the package's Vendor Engineering Deliverables. | `26020-Package_Requirements.docx` §6 — PRQ-009 |
| R-02 | A Vendor Document Control Procedure (DOC-008) shall govern revision, transmittal, hold/code review status, and document-control numbering. | `26020-Package_Requirements.docx` §6 — DOC-008 |
| R-03 | Quality records shall include a Supplier Quality Plan (QLT-006), Inspection and Test Plan (QLT-003), Material Test Reports / Certificates (QLT-013), Inspection Release Certificate (QLT-020), and Manufacturing Record Book (QLT-021). | `26020-Package_Requirements.docx` §6 — QLT-003, QLT-006, QLT-013, QLT-020, QLT-021 |
| R-04 | Logistics / shipping records shall include a Logistics / Shipping Plan (PRQ-013) and Spare Parts Interchangeability Record (PRQ-015). | `26020-Package_Requirements.docx` §6 — PRQ-013, PRQ-015 |
| R-05 | Final supplier documentation shall be assembled as a Vendor Data Book — PRQ-016 (overall) and MEC-023 (mechanical final documentation), with IOM content per MEC-025. | `26020-Package_Requirements.docx` §6 — PRQ-016, MEC-023, MEC-025 |
| R-06 | Pressure equipment registration (REG-022) shall be assembled and submitted for the heat-transfer scope per applicable jurisdictional code. | `26020-Package_Requirements.docx` §6 — REG-022 (specific code citation TBD; not in accessible source slice) |
| R-07 | FAT/SAT records shall include Equipment FAT Procedure (MEC-021), FAT Report (MEC-022), and Electrical FAT/SAT Procedure (ELE-029) and Test Records / Energization Package (ELE-030). | `26020-Package_Requirements.docx` §6 — MEC-021, MEC-022, ELE-029, ELE-030 |
| R-08 | The discipline document categories listed in the Datasheet — Process, Piping, Drainage, Electrical, Instrumentation/Controls, Fire & Gas, Structural — shall each be represented in the turnover register with the document codes enumerated in the source. | `26020-Package_Requirements.docx` §6 (full deliverable list) |
| R-09 | As-built documentation shall be issued for instrumentation (INS-029) and process PFD/P&IDs (PRO-028) at turnover. | `26020-Package_Requirements.docx` §6 — INS-029, PRO-028 |
| R-10 | Submittals shall be made available to the EPC Integrator for interface/integration review consistent with the Package Datasheet's interface scope (Utility Piping, Drain/Containment, Electrical Power, Lighting, Grounding, I&C Cabling, Fire & Gas, Maintenance Access, Structural/Foundations) where "Yes" in the Physical Interface Summary. | `26020-Package_Requirements.docx` §6 — Physical Interface Summary; `_CONTEXT.md` |
| R-11 | Submittal cadence, hold codes, and turnover acceptance criteria are TBD until specified by the EPC document-control procedure or contractual MDR. | TBD — not in accessible source slice |

## Standards

| Standard / Reference | Applicability | Location |
|---|---|---|
| `26020-Package_Requirements.docx` §6 — Process Heat Medium Unit | Authoritative package scope and vendor deliverable list | Accessible (extracted) |
| `26020-Packages_Interfaces_4_export.xlsx` row 79 | Package interface matrix referenced in source | Accessible (binary; row 79 cited in source slice) |
| Jurisdictional pressure-equipment registration code | Governs REG-022 content | location TBD (not in accessible source slice) |
| EPC document-control procedure / MDR | Governs hold codes, submittal cadence, transmittal mechanics | location TBD |

## Verification

| Req | Verification Method | Verification Artifact |
|---|---|---|
| R-01 | Document index audit — every Vendor Engineering Deliverable code in source §6 present in PRQ-009 | PRQ-009 register cross-walk |
| R-02 | Procedure review against EPC document-control rules | DOC-008 + EPC review record |
| R-03 | Quality records audit at FAT close-out and at turnover | QLT-003/006/013/020/021 sign-offs |
| R-04 | Receipt of PRQ-013 and PRQ-015 prior to shipment | Shipment release record |
| R-05 | Completeness check of final data books | PRQ-016 + MEC-023 transmittal |
| R-06 | Jurisdictional registration approval | REG-022 stamped/registered package |
| R-07 | FAT / SAT records present and signed | MEC-021/022, ELE-029/030 |
| R-08 | Category-completeness check against source §6 | Index gap-analysis report |
| R-09 | As-built confirmation against final field state | INS-029, PRO-028 |
| R-10 | EPC interface/integration review sign-off | Review record (per DEL-051-06 ASSUMPTION) |
| R-11 | EPC procedure issuance | EPC document-control procedure (TBD) |

## Documentation

The deliverables produced by this package are the document register and submittal/turnover records themselves. The anticipated artifacts from `_CONTEXT.md` are:

- Vendor document register (PRQ-009 as the controlled instance)
- Vendor document submittals (each coded item in the Datasheet "Construction" register)
- Source vendor document table rows as artifacts where available (per `26020-Package_Requirements.docx` §6 list)
- Turnover records (PRQ-016, MEC-023, plus FAT/SAT close-out packets)
