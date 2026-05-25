# Datasheet: DEL-035-05 — Vendor Document Turnover Package

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-035-05_vendor-document-turnover-package` | `_CONTEXT.md` |
| Name | Vendor Document Turnover Package | `_CONTEXT.md`; GATE-07 `DELIVERABLE_REGISTER.csv` row for `DEL-035-05` |
| Parent Package | `PKG-035` — 13.8kV SWITCHGEAR ELECTRICAL BUILDING (810-1) | `_CONTEXT.md` |
| Workbook Row | Packages row 37 (`ID #` 35) | `_Sources/26020-Packages_Interfaces_4_export.xlsx` (Packages, row 37) |
| CoA Tracking Number | 26020-01-30-026 | `_Sources/26020-Packages_Interfaces_4_export.xlsx` (Packages, row 37) |
| WBS | 01 | `_Sources/26020-Packages_Interfaces_4_export.xlsx` (Packages, row 37) |
| Discipline | Electrical | `_CONTEXT.md`; workbook row 37 |
| Type | Vendor Document Turnover | `_CONTEXT.md` |
| Responsible Party | Package Vendor (vendor documentation) with EPC Integrator interface/integration review | `_CONTEXT.md` |
| Covers Scope Items | `SOW-0036` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Supports Objectives | `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (ASSUMPTION: package-grouping heuristic per `four-documents` skill default) | `_CONTEXT.md`; `OBJECTIVE_DELIVERABLE_MAP.csv` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Deliverable form | Composite turnover package consisting of (a) vendor document register, (b) vendor document submittals, (c) source-required vendor documentation as artifact rows, (d) turnover records | `_CONTEXT.md` (Scope; Anticipated Artifacts) |
| Vendor document scope baseline | Generic core vendor document set defined by Package Requirements Table 4 ("Core vendor documents") | `_Sources/26020-Package_Requirements.docx` — Table 4, rows 1–11 |
| Discipline-specific document baseline | Electrical, lighting, EHT, grounding document family (Table 4 rows 64–80) — applicable subset for a 13.8kV switchgear electrical building package | `_Sources/26020-Package_Requirements.docx` — Table 4, rows 64–80 |
| Cross-discipline document baselines applicable to PKG-035 | I&C / Control cabling (`X`), Communications / Network (`X`), Building HVAC / Services (`X`), Fire & Gas / Safety Systems (`X`), Grounding / Bonding (`X`), Area / Exterior Lighting (`X`), Maintenance Access (`X`), Grading / Site Drainage / Spill Containment (`X`), Structural / Foundations / Supports (`X`), Utility Piping (`X`), Drain / Containment (`X`), Electrical Power (`X`) | `_Sources/26020-Packages_Interfaces_4_export.xlsx` (Packages, row 37) |
| Cross-discipline document baselines not applicable to PKG-035 | Process Piping (None), Relief / Flare / Vent (None), EHT (None), Cathodic Protection (None), Product Loading (None), Pipeline / Pigging (None) | `_Sources/26020-Packages_Interfaces_4_export.xlsx` (Packages, row 37) |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Authoritative decomposition basis | GATE-07 Final Published PROJECT_DECOMP snapshot (2026-05-24) | `_REFERENCES.md` |
| Coordination / dependency mode | DECLARED; no upstream or downstream dependencies declared during PREPARATION | `_DEPENDENCIES.md` |
| Package-specific Requirements section | No package-specific Heading 1 section for `PKG-035` / 13.8kV Switchgear Electrical Building exists in `_Sources/26020-Package_Requirements.docx` (only generic Table 4 applies) | `_Sources/26020-Package_Requirements.docx` (verified by heading scan) |
| Process DBM coverage | DBM source slices (`DBM-Comp_and_Liquids`, `DBM-Deepcut`) are process-unit DBMs; they do not contain vendor-document or turnover requirements for the switchgear/electrical-building package | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |

## Construction

### Core vendor document set (mandatory for every package; PKG-035 inherits in full)

Source: `_Sources/26020-Package_Requirements.docx` Table 4, rows 1–11 (header "Core vendor documents").

| Doc ID | Document Name |
|---|---|
| PRQ-009 | Vendor Document Index |
| DOC-008 | Vendor Document Control Procedure |
| QLT-006 | Supplier Quality Plan |
| QLT-003 | Inspection and Test Plan (ITP) |
| QLT-013 | Material Test Reports / Certificates |
| QLT-020 | Inspection Release Certificate |
| QLT-021 | Manufacturing Record Book / Vendor Data Book |
| PRQ-013 | Logistics / Shipping Plan |
| PRQ-015 | Spare Parts Interchangeability Record (SPIR) |
| PRQ-016 | Vendor Data Book / Final Supplier Documentation |

### Discipline-specific vendor document set — Electrical (Table 4 rows 64–80)

Applicable to a 13.8kV switchgear electrical building package; subset to be confirmed by the EPC Scope of Work (`DEL-035-01`) and Package Datasheet (`DEL-035-02`).

| Doc ID | Document Name |
|---|---|
| ELE-002 | Electrical Load List / Consumer List |
| ELE-003 | Single-Line Diagrams (SLDs) |
| ELE-014 | Cable Schedule |
| ELE-015 | Cable Tray / Routing Drawings |
| ELE-016 | Electrical Layout Drawings |
| ELE-020 | Electrical Equipment Data Sheets |
| ELE-027 | Electrical Installation Details |
| ELE-028 | Electrical Interconnection / Connection Diagrams |
| ELE-029 | Electrical FAT / SAT Procedure |
| ELE-030 | Electrical Test Records / Energization Package |
| ELE-017 | Lighting Layout Drawings |
| ELE-012 | Grounding / Earthing Study |
| ELE-019 | Earthing / Bonding Layout Drawings |

### Cross-discipline vendor document families applicable per workbook row 37

| Family | Representative documents (from Table 4) | Source |
|---|---|---|
| I&C / Control cabling | INS-002, INS-003, INS-005, INS-006, INS-008, INS-009, INS-010, INS-011, INS-018, INS-029; CTL-026 (Package Vendor Interface Specification) | `_Sources/26020-Package_Requirements.docx` Table 4 rows 82–98 |
| Fire & Gas / Safety Systems | TSF-002, TSF-003, TSF-004, TSF-009, TSF-011, TSF-013, TSF-028 | Table 4 rows 100–106 |
| Structural / Foundations / Supports | STR-001, STR-002, STR-004, STR-005, STR-006, STR-011, STR-013, STR-014 | Table 4 rows 108–117 |
| Building HVAC / Services, Communications / Network, Maintenance Access, Grading / Site Drainage / Spill Containment, Utility Piping, Drain / Containment | Specific document IDs `TBD` — not enumerated in Table 4 under a dedicated family for PKG-035 in the accessible source | `_Sources/26020-Package_Requirements.docx` Table 4 (no matching family heading) |

## References

- `_CONTEXT.md` (this deliverable folder)
- `_REFERENCES.md` (this deliverable folder)
- `_DEPENDENCIES.md` (this deliverable folder)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv`
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv`
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/OBJECTIVE_DELIVERABLE_MAP.csv`
- `_Sources/26020-Package_Requirements.docx` — Table 4 "Core vendor documents" and discipline-specific families
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — Packages sheet, row 37 (`PKG-035`)
