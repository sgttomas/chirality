# Datasheet — DEL-055-06 EPC Vendor Package Review and Acceptance

> Descriptive datasheet for the EPC Integrator's vendor package review and acceptance
> deliverable for the Low-Pressure Flare KO Drum package (PKG-055) at facility 04-25.

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-055-06_epc-vendor-package-review-and-acceptance | `_CONTEXT.md` |
| Deliverable Name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md` |
| Parent Package ID | PKG-055 | `_CONTEXT.md` |
| Parent Package Name | Flare KO Drum (Low Pressure) 4-25 | `_CONTEXT.md` |
| Workbook Row | 57 | `_CONTEXT.md`, DELIVERABLE_REGISTER.csv |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | EPC Vendor Package Acceptance | `_CONTEXT.md` |
| Responsible Party | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md` |
| Covered SoW Items | SOW-0083, SOW-0084, SOW-0085, SOW-0086 | `_CONTEXT.md` |
| Supported Objectives | OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | `_CONTEXT.md` (ASSUMPTION via package-heuristic association) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package subject | Low-Pressure Flare Knock-Out Drum, facility 04-25 | DELIVERABLE_REGISTER.csv (PKG-055 name) |
| Facility | West Doe Deepcut Expansion, 04-25 lease | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Sec. site basis |
| Vendor identity | TBD | location TBD (`26020-Package_Requirements.docx` heading 10 — binary source, not locally readable) |
| Vendor scope split (engineering / supply / fabrication) | TBD | location TBD (same source) |
| Acceptance basis documents | EPC Scope of Work (DEL-055-01), Package Datasheet (DEL-055-02), Construction Work Package (DEL-055-03) | `_CONTEXT.md` scope statement |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Operating service | Low-pressure flare relief gas knock-out, upstream of LP flare stack/incinerator | DBM-Deepcut Sec. "Flare and Incinerator Spacing" |
| Design code basis (vessel) | ASME Section VIII Division 1 (ASSUMPTION) | not locally cited; pending source confirmation |
| Design code basis (piping tie-ins) | ASME B31.3 (ASSUMPTION) | not locally cited; pending source confirmation |
| Layout / siting constraints | Flare-and-incinerator spacing per OGAOM Sec. 9.6.15; KO drum spacing to vegetation/fire hazards >= 10 m | DBM-Deepcut Sec. "Flare and Incinerator Spacing" |
| Thermal radiation limits | <= 9 kW/m^2 inside boundary; <= 5 kW/m^2 outside boundary (OGPFR Appx 1) | DBM-Deepcut Sec. "Flare and Incinerator Spacing" |
| Process / mechanical design values (P, T, Q) | TBD | location TBD (vendor datasheet / package requirements docx) |

## Construction

| Item | Description | Source |
|---|---|---|
| Acceptance artifact set | Vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence | `_CONTEXT.md` Anticipated Artifacts |
| Review interfaces | EPC Integrator review of vendor engineered equipment package (DEL-055-04) and vendor document turnover (DEL-055-05) | DELIVERABLE_REGISTER.csv (PKG-055 rows) |
| Construction interfaces | Tie-in to LP flare header, drains, instrument air, electrical, and grounding per CWP | `_CONTEXT.md` (decomposition narrative); DEL-055-03 (CWP) |
| Turnover artifacts | Mechanical completion certificate, pressure-test records, NDE records, vendor data book — TBD specifics | location TBD (package requirements docx) |

## References

- `_CONTEXT.md` (this deliverable folder)
- `_REFERENCES.md` (this deliverable folder)
- DELIVERABLE_REGISTER.csv (GATE-07 snapshot) — row `DEL-055-06_epc-vendor-package-review-and-acceptance`
- OBJECTIVE_SCOPE_MAP.csv (GATE-07 snapshot) — PKG-055 rows
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — facility design basis (flare/KO drum spacing slice)
- `_Sources/26020-Package_Requirements.docx` package heading 10 — primary source (binary; not locally readable; location TBD)
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 57 — primary source (binary; not locally readable; location TBD)
