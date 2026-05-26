# Specification: DEL-072-02 Package Datasheet

## Scope

This specification governs the EPC Integrator package datasheet for `PKG-072` Truck Product Loading Unit 4-25. The datasheet is the mandatory technical handoff deliverable for `DEL-072-02_package-datasheet` and must carry source-supported package data for third-party vendor or discipline package engineering and design.

Included scope:

- Package identity and handoff basis for `PKG-072` Truck Product Loading Unit 4-25, WBS 01, CoA tracking number `26020-01-23-001`, discipline Mechanical.
- The scope items `SOW-0245`, `SOW-0246`, `SOW-0247`, and `SOW-0248` as recorded in the Gate 7 scope ledger.
- The eleven interface facts recorded for `PKG-072` in the Gate 7 `INTERFACE_REGISTER.csv`.
- Objective context for `OBJ-001`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, and `OBJ-010`.

Excluded scope:

- Detailed mechanical/process design, construction sequencing, and inspection turnover instructions that belong in `DEL-072-03_construction-work-package`.
- Vendor package engineering, design, fabrication, and physical equipment supply that belong in `DEL-072-04_vendor-engineered-equipment-package`.
- Vendor document register and turnover content that belongs in `DEL-072-05_vendor-document-turnover-package`.
- EPC vendor package review and acceptance evidence that belongs in `DEL-072-06_epc-vendor-package-review-and-acceptance`.
- Requirements not supported by the Gate 7 accepted snapshot, deliverable-local context, or locally accessible source materials.

Sources: `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row `PKG-072`; `DELIVERABLE_REGISTER.csv` row `DEL-072-02_package-datasheet`; `SCOPE_LEDGER.csv` rows `SOW-0245`..`SOW-0248`; `ARTIFACT_REGISTER.csv` artifacts under `DEL-072-02_package-datasheet`.

## Requirements

| Requirement ID | Requirement | Source | Verification |
|---|---|---|---|
| REQ-072-02-001 | The datasheet must identify `PKG-072` as Truck Product Loading Unit 4-25, workbook ID 72, workbook row 99, WBS 01, discipline Mechanical, and CoA tracking number `26020-01-23-001`. | `PACKAGE_REGISTER.csv` row `PKG-072` | Datasheet identity table check |
| REQ-072-02-002 | The datasheet must identify the responsible party as EPC Integrator and the deliverable type as EPC Package Datasheet. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-072-02_package-datasheet` | Datasheet identity table check |
| REQ-072-02-003 | The datasheet must carry `SOW-0245`, `SOW-0246`, `SOW-0247`, and `SOW-0248` as covered scope items. | `_CONTEXT.md`; `SCOPE_LEDGER.csv` rows `SOW-0245`..`SOW-0248` | Scope traceability check |
| REQ-072-02-004 | The datasheet must include the technical handoff datasheet, vendor engineering handoff basis, and package interface requirements matrix artifacts anticipated for this deliverable. | `ARTIFACT_REGISTER.csv` artifacts `ART-1E30749941`, `ART-6F113CE055`, `ART-170CD144CD` | Artifact coverage check |
| REQ-072-02-005 | The datasheet must preserve all eleven `PKG-072` interface facts exactly as named in `INTERFACE_REGISTER.csv`: Process Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports; Product Loading. | `INTERFACE_REGISTER.csv` rows scoped to `PKG-072`; `ARTIFACT_REGISTER.csv` interface-fact artifacts for `DEL-072-02_package-datasheet` | Interface matrix check |
| REQ-072-02-006 | The datasheet must expose the mapped objective context for `OBJ-001`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, and `OBJ-010` without treating objective statements as clause-level mechanical design criteria. | `OBJECTIVE_DELIVERABLE_MAP.csv` rows for `DEL-072-02_package-datasheet`; `OBJECTIVE_REGISTER.csv` rows | Objective traceability check |
| REQ-072-02-007 | The datasheet must carry the source-quoted equipment and design values from `SOW-0247` and `SOW-0248` and explicitly mark the discrepancy between the package name (Truck Product Loading Unit 4-25) and the source row text (fuel-gas heater/scrubber) as an open conflict (HRR-072-02-001) rather than silently choosing one interpretation. | `SCOPE_LEDGER.csv` rows `SOW-0247`, `SOW-0248`; 26020-Package_Requirements.docx package heading 26; `PACKAGE_REGISTER.csv` row `PKG-072` | Conflict table review |
| REQ-072-02-008 | Any unsupported design values, codes, dimensions, capacities, materials, or execution criteria must remain `TBD` rather than inferred. | `PACKAGE_REGISTER.csv` row `PKG-072`; `SCOPE_LEDGER.csv` row `SOW-0248` (multiple `TBD` markers) | Source gap review |

## Standards

| Standard / basis | Status | Source |
|---|---|---|
| Gate 7 final published PROJECT_DECOMP snapshot | Governing accepted decomposition truth for this Phase 2.2 run | `_REFERENCES.md`; Gate 7 `PROJECT_DECOMP.md` |
| Workbook Packages row 99 | Accepted source reference for package identity, workbook row, interface facts, and source basis | `PACKAGE_REGISTER.csv` row `PKG-072`; `SCOPE_LEDGER.csv` rows `SOW-0245`..`SOW-0248`; `INTERFACE_REGISTER.csv` rows for `PKG-072` |
| 26020-Package_Requirements.docx package heading 26 | Source row for basic scope, major included equipment, scope notes, and vendor deliverable tables for `26020-01-PT-23-001 - Condensate Truck Loading Stations`; basic-scope text describes a fuel-gas skid, which conflicts with the package title (see HRR-072-02-001) | `_REFERENCES.md`; `PACKAGE_REGISTER.csv` row `PKG-072` |
| DBM-Deepcut/4-25_Deepcut_DBM.md | Directional facility design basis: references API 2510 minimum distance between pressurized bullets and truck loading station, and grounding-stud requirements for truck loading | `_REFERENCES.md`; DBM-Deepcut/4-25_Deepcut_DBM.md |
| API 2510 (LPG / pressurized storage spacing) | ASSUMPTION: applicable as a spacing reference per DBM citation; clause-level requirements not extracted | DBM-Deepcut/4-25_Deepcut_DBM.md (truck loading spacing reference) |
| Mechanical / loading-system codes (e.g., API metering, NFPA static electricity, NFPA 30, CSA grounding) | TBD - not named at clause level in the Gate 7 accepted snapshot for `PKG-072` | `OBJECTIVE_REGISTER.csv` row `OBJ-009` |

## Verification

| Check | Method | Acceptance |
|---|---|---|
| Identity completeness | Compare Datasheet Identification against `PACKAGE_REGISTER.csv` and `DELIVERABLE_REGISTER.csv`. | All listed identity fields match accepted Gate 7 rows. |
| Artifact coverage | Compare Datasheet Attributes against `ARTIFACT_REGISTER.csv` artifacts for `DEL-072-02_package-datasheet`. | Datasheet includes technical datasheet, vendor handoff basis, interface matrix, and all eleven interface-fact evidences. |
| Interface consistency | Compare Datasheet, Specification, Guidance, and Procedure interface wording against `INTERFACE_REGISTER.csv`. | Interface names appear exactly as recorded in the Gate 7 register. |
| Objective traceability | Compare mapped objectives against `_CONTEXT.md` and `OBJECTIVE_DELIVERABLE_MAP.csv`. | The nine mapped objectives appear as context only. |
| Conflict surfacing | Inspect the Guidance Conflict Table for HRR-072-02-001. | The package-name vs source-row-text conflict is recorded and not silently resolved. |
| Source gap control | Review all numeric values and standards citations. | Unsupported values remain `TBD` or are labeled `ASSUMPTION`. |

## Documentation

Required deliverable artifacts:

- Package technical datasheet.
- Vendor engineering handoff basis.
- Package interface requirements matrix.
- Source-supported equipment and design criteria.

Supporting records:

- Gate 7 final published snapshot references used for traceability.
- List of unresolved `TBD` technical values, MAWP, capacities, codes, and clause-level standards.
- Open human-ruling record HRR-072-02-001 capturing the package-name vs source-row-text conflict.
