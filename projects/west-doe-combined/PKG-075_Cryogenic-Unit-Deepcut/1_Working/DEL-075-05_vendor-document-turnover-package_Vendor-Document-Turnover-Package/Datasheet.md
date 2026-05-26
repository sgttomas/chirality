# Datasheet — DEL-075-05 Vendor Document Turnover Package (PKG-075)

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-075-05_vendor-document-turnover-package` |
| Name | Vendor Document Turnover Package |
| ParentPackageID | `PKG-075` |
| Package Name | Cryogenic Unit ("Deepcut") |
| Workbook Tag | `26020-01-27-003` (PACKAGE_REGISTER row 52) |
| Tag Number | `26020-01-PT-28-001` — Cryogenic Deep Cut Package |
| Discipline | Mechanical |
| WBS | 01 |
| Type | Vendor Document Turnover |
| ResponsibleParty | Package Vendor (vendor documentation) with EPC Integrator interface/integration review |
| Covers Scope Items | `SOW-0063`, `SOW-0064`, `SOW-0065`, `SOW-0066` |
| Supports Objectives | `OBJ-001`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (ASSUMPTION — package-grouping heuristic per `_CONTEXT.md`) |

## Attributes

The deliverable is a document set rather than a physical artifact. Attribute values describe the document register that the Package Vendor must deliver and the EPC Integrator must accept for the cryogenic deep-cut propane-plus recovery package.

| Attribute | Value | Source |
|---|---|---|
| Document register basis | Per-package `Vendor Engineering Deliverables` list defined in source `26020-Package_Requirements.docx` | `_Sources/26020-Package_Requirements.docx`, section "Vendor Engineering Deliverables" (heading 29 — Cryogenic Unit) |
| Document control procedure | Vendor Document Control Procedure (`DOC-008`) required as core vendor document | `_Sources/26020-Package_Requirements.docx`, "Core vendor documents" row |
| Index | Vendor Document Index (`PRQ-009`) required as core vendor document | same as above |
| Final book | Vendor Data Book / Final Supplier Documentation (`PRQ-016`); mechanical final book `MEC-023` | same as above |
| Quality records | Supplier Quality Plan `QLT-006`; ITP `QLT-003`; MTRs/Certificates `QLT-013`; Inspection Release Certificate `QLT-020`; Manufacturing Record Book / VDB `QLT-021` | same as above |
| Logistics records | Logistics / Shipping Plan `PRQ-013`; SPIR `PRQ-015` | same as above |
| Discipline applicability | Mechanical-led process package with extensive piping/process/relief/utilities and electrical/I&C; see Discipline Applicability narrative in Specification | `PACKAGE_REGISTER.csv` row 52 (interface types list); `_Sources/26020-Package_Requirements.docx` |
| Coverage | Four SOW items `SOW-0063`, `SOW-0064`, `SOW-0065`, `SOW-0066` | `DELIVERABLE_REGISTER.csv` row 280 |
| Package technology | UltraTEF cryogenic turbo-expansion process; expected 99+ percent propane recovery (overview-level basis only) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-01 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Lifecycle stage at acceptance | Post-FAT through turnover, including as-built records | `_Sources/26020-Package_Requirements.docx` (PIP-028 As-Built; MEC-022 FAT Report; ELE-030 Energization Package) |
| Site basis affecting documentation | West Doe Deepcut expansion, facility identifier 04-25, LSD 04-25-80-15W6 (approx. 22.2 km north of Dawson Creek, BC). Vendor data must reflect cold-climate sour-service ambient and electrical-area conditions per facility design basis. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-01 |
| Process service | Sour gas, cryogenic temperatures, NGL/C3+ recovery service | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-01 |
| Acceptance gate | EPC Integrator interface/integration review and acceptance via `DEL-075-06` | `DELIVERABLE_REGISTER.csv` row 280; package-internal consistency with sibling DEL-XX-05 deliverables |
| Submittal cadence | TBD — not stated in accessible source slices |
| Native file format requirements | TBD — not stated in accessible source slices |

## Construction

The "construction" of this deliverable is the assembly and turnover of a vendor document set. The composing document classes are taken directly from `_Sources/26020-Package_Requirements.docx` "Vendor Engineering Deliverables" template (uniform across packages; per-package applicability is filtered in `DEL-075-06` review).

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

**Discipline-applicable document classes (applied because PKG-075 is a mechanical process package containing pressure equipment, piping, relief, drain, utilities, electrical power, grounding, I&C, fire & gas, structural foundations, and maintenance access interfaces per PACKAGE_REGISTER row 52):**

- Process / Mechanical Equipment (MEC-001, MEC-002, MEC-003, MEC-006, MEC-016, MEC-017, MEC-018, MEC-021, MEC-022, MEC-023, MEC-024, MEC-025) for the cryogenic process equipment, BAHX, columns, expanders, exchangers, vessels, etc.
- Piping / Pressure Equipment (PIP-xxx, PV-xxx — applicable because of extensive process and utility piping and pressure vessels in a cryogenic process package; specific IDs as enumerated in the source template — ASSUMPTION: full PIP/PV set applies; EPC Integrator confirms per-line in `DEL-075-06`)
- Relief / Flare / Vent (applicable because of cryogenic relief and HP flare interfaces; see DBM-Deepcut SEC on flare and incinerator)
- Electrical (ELE-002, ELE-003, ELE-014, ELE-015, ELE-016, ELE-020, ELE-027, ELE-028, ELE-029, ELE-030) for package electrical power, grounding, area lighting tie-in, energization
- Instrumentation and Controls (INS-002, INS-003, INS-005, INS-006, INS-008, INS-009, and subsequent INS entries — ASSUMPTION: applicable because the cryogenic package includes control, monitoring, ESD, and F&G interfaces; confirm during EPC integration review)
- Civil / Structural (foundations, supports, structural steel) per PACKAGE_REGISTER row 52 "Structural / Foundations / Supports"
- HVAC / Building Services where applicable to vendor-supplied enclosures

Refer to `Specification.md` for the binding discipline applicability narrative for this package.

## References

- Gate 7 PROJECT_DECOMP snapshot deliverable row: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv`, row 280 (`DEL-075-05_vendor-document-turnover-package`)
- Gate 7 PROJECT_DECOMP snapshot package row: `.../PACKAGE_REGISTER.csv`, row 52 (`PKG-075`, tag `26020-01-27-003`, tag number `26020-01-PT-28-001`)
- `_Sources/26020-Package_Requirements.docx` — "Vendor Engineering Deliverables" section (core vendor documents and per-discipline deliverable IDs); package heading 29 (Cryogenic Unit). Specific clause locations within the .docx: location TBD.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — facility design basis for the Deepcut cryogenic expansion (SEC-01 facility identity, project objectives, process and commercial basis)
- Deliverable-local: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`
