# Datasheet: DEL-105-01 — Scope of Work (PKG-105 Platforms)

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-105-01_scope-of-work` | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv |
| Deliverable Name | Scope of Work | `_CONTEXT.md` |
| Parent Package ID | `PKG-105` | `_CONTEXT.md`; PACKAGE_REGISTER.csv |
| Parent Workbook ID | 105 (Workbook Packages row 106) | PACKAGE_REGISTER.csv |
| Package Name | Platforms | `_CONTEXT.md`; PACKAGE_REGISTER.csv |
| CoA Tracking Number | 26020-01-36-005 | PACKAGE_REGISTER.csv |
| WBS | 01 | PACKAGE_REGISTER.csv |
| Discipline | Structural | `_CONTEXT.md`; PACKAGE_REGISTER.csv |
| Type | EPC Scope of Work | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv |
| Responsible Party | EPC Integrator | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv |
| Covers Scope Items | `SOW-0261` | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv |
| Supports Objectives | `OBJ-001`, `OBJ-005`, `OBJ-008`, `OBJ-010` (ASSUMPTION — PACKAGE_HEURISTIC, best-effort mapping) | `_CONTEXT.md`; OBJECTIVE_DELIVERABLE_MAP.csv |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package function (declared) | Platforms (Structural package) | PACKAGE_REGISTER.csv row PKG-105 |
| Package description | "Workbook-defined Structural package for 'Platforms' under WBS 01 with recorded physical interfaces." | PACKAGE_REGISTER.csv row PKG-105 |
| Applicable interface types | Area / Exterior Lighting; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports | PACKAGE_REGISTER.csv row PKG-105; INTERFACE_REGISTER.csv (IFC-26E3DCAD56, IFC-07C472C58B, IFC-B7C0A01E38) |
| Package note (source) | "Platform-to-equipment tie-ins should be confirmed by layout/model." | PACKAGE_REGISTER.csv row PKG-105 |
| Gate 6 interface disposition | "Platform-to-equipment tie-ins are the EPC Integrator's responsibility through the overall 3D model and integrated P&ID set." | INTERFACE_REGISTER.csv rows for PKG-105 |
| Tagged equipment list | TBD — workbook row 106 detail not transcribed; resolve from `26020-Package_Requirements.docx` package heading for row 106 (location TBD) | `_REFERENCES.md`; ARTIFACT_REGISTER.csv ART-21C90A2BB4 |
| Boundaries/exclusions | TBD — "no package-specific exclusions stated in source materials" | PACKAGE_REGISTER.csv row PKG-105 |
| Battery limits | TBD — source location not yet transcribed | location TBD |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Governing structural code | CSA S16:19 (Design of steel structures) | DBM `4-25_Deepcut_DBM.md` §"Governing Civil and Structural Basis" / Standards table line 3412 |
| Governing structural material standard | CSA G40.20-13 / G40.21-13 (350W for W-flange and HSS; 300W for channels, plates, angles) | DBM `4-25_Deepcut_DBM.md` line 2676; line 3411 |
| Governing welding code | CSA W59-18 | DBM `4-25_Deepcut_DBM.md` line 3413 |
| Site geotechnical basis | Geotechnical assessment to be conducted; report to be reviewed for completeness of design parameters | DBM `4-25_Deepcut_DBM.md` line 2685 |
| Climate / load conditions | TBD — values not transcribed for this deliverable | DBM (location TBD) |

## Construction

| Item | Value | Source |
|---|---|---|
| Structural steel material basis | CSA G40.20/G40.21 350W (W-flange, HSS); 300W (channels, plates, angles) | DBM `4-25_Deepcut_DBM.md` line 2676 |
| Field construction scope reference | "Installation of miscellaneous structural supports" listed under Tourmaline field construction scope (ASSUMPTION: directionally relevant to platform installation scope) | DBM `4-25_Deepcut_DBM.md` line 116 |
| Walkway / access provisions (general site basis) | "A 1 m access walkway shall be maintained" (cited for emergency-generator context; ASSUMPTION: indicative of site walkway minimum where applicable) | DBM `4-25_Deepcut_DBM.md` line 2076 |
| Platform-specific construction details | TBD — not present in transcribed source slices | location TBD |

## References

- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/ARTIFACT_REGISTER.csv`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/INTERFACE_REGISTER.csv`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/OBJECTIVE_DELIVERABLE_MAP.csv`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Package_Requirements.docx` (binary; package heading for Workbook row 106 — location TBD, not transcribed)
