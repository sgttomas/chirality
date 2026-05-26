# Specification: DEL-105-01 — Scope of Work (PKG-105 Platforms)

## Scope

**In scope.** This deliverable is the EPC Integrator-authored Scope of Work for PKG-105 "Platforms," a Structural package under WBS 01 with CoA tracking number 26020-01-36-005 (Workbook Packages row 106). It defines:

- the package's tagged-equipment basis,
- the package function and whole-facility integration narrative,
- the package source basis and boundaries,
- the responsibility assignment for executing the package.

Source: `_CONTEXT.md` Scope; DELIVERABLE_REGISTER.csv row `DEL-105-01_scope-of-work`; PACKAGE_REGISTER.csv row PKG-105; ARTIFACT_REGISTER.csv artifacts ART-B537AC5EA7, ART-21C90A2BB4, ART-1B624DB0B8, ART-77976FD844.

**Out of scope / excluded.** TBD — no package-specific exclusions are stated in the current source materials (PACKAGE_REGISTER.csv exclusions field for PKG-105: "TBD; no package-specific exclusions stated in source materials"). Boundaries and battery limits to be resolved against `26020-Package_Requirements.docx` package heading for row 106 (location TBD).

## Requirements

| Req ID | Requirement | Basis | Verification (cross-ref Procedure) |
|---|---|---|---|
| R-105-01-01 | The SoW shall identify the package by Workbook ID 105 / row 106, CoA `26020-01-36-005`, WBS 01, discipline Structural, name "Platforms." | PACKAGE_REGISTER.csv row PKG-105 (FACT) | Procedure §Steps 2; §Verification |
| R-105-01-02 | The SoW shall include a tagged-equipment and package identity list grounded in the workbook row 106 source. | ARTIFACT_REGISTER.csv ART-21C90A2BB4; DELIVERABLE_REGISTER.csv anticipated artifacts (FACT) | Procedure §Steps 3 |
| R-105-01-03 | The SoW shall include a package function and whole-facility integration narrative explaining what platforms do and how they integrate with adjacent equipment and structures. | ARTIFACT_REGISTER.csv ART-1B624DB0B8 (FACT) | Procedure §Steps 4 |
| R-105-01-04 | The SoW shall record responsibility for execution. Responsibility is the EPC Integrator at the SoW level. | DELIVERABLE_REGISTER.csv ResponsibleParty field; PACKAGE_REGISTER.csv responsibility note (FACT) | Procedure §Steps 5 |
| R-105-01-05 | The SoW shall enumerate the package's applicable physical interfaces: Area / Exterior Lighting; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. | INTERFACE_REGISTER.csv rows IFC-26E3DCAD56, IFC-07C472C58B, IFC-B7C0A01E38; PACKAGE_REGISTER.csv (FACT) | Procedure §Steps 6 |
| R-105-01-06 | The SoW shall record the Gate 6 disposition that platform-to-equipment tie-ins are the EPC Integrator's responsibility, executed through the overall 3D model and the integrated P&ID set. | INTERFACE_REGISTER.csv notes for PKG-105 (FACT) | Procedure §Steps 6 |
| R-105-01-07 | The structural basis cited in the SoW shall be consistent with the governing civil and structural basis (CSA S16, CSA G40.20/G40.21, CSA W59) defined in the project DBM. | DBM `4-25_Deepcut_DBM.md` §"Governing Civil and Structural Basis" (lines 2666-2685; 3411-3413) (FACT) | Procedure §Steps 7 |
| R-105-01-08 | Package boundaries, battery limits, and exclusions shall be stated. Where the current source set does not state them, they shall be marked `TBD` with a pointer to `26020-Package_Requirements.docx` row 106 heading for resolution. | PACKAGE_REGISTER.csv exclusions field; `_REFERENCES.md` (ASSUMPTION: drafting rule) | Procedure §Steps 8 |
| R-105-01-09 | The SoW shall cite its upstream decomposition snapshot (GATE-07 Final Published 2026-05-24) as the authoritative basis. | `_CONTEXT.md` Decomposition Reference; `_REFERENCES.md` (FACT) | Procedure §Records |

## Standards

| Standard | Applicability | Location |
|---|---|---|
| CSA S16:19 — Design of steel structures | Structural steel design basis | DBM `4-25_Deepcut_DBM.md` line 3412 |
| CSA G40.20-13 / G40.21-13 — Rolled or welded structural quality steel | Structural material basis (350W W-flange/HSS; 300W channels/plates/angles) | DBM `4-25_Deepcut_DBM.md` lines 2676, 3411 |
| CSA W59-18 — Welded steel construction | Structural welding basis | DBM `4-25_Deepcut_DBM.md` line 3413 |
| Platform / walking-working surface code (e.g., OH&S / occupancy code with guardrail, stair, and grating requirements) | ASSUMPTION: likely applicable to access platforms; specific code not transcribed in accessible sources | location TBD |
| Geotechnical report (project-specific) | Lateral pile design, LPILE curves, dynamic criteria — to be reviewed for completeness | DBM `4-25_Deepcut_DBM.md` line 2685 |

## Verification

| Requirement | Verification Approach |
|---|---|
| R-105-01-01 to R-105-01-04 | Document inspection of the SoW deliverable against the cited register rows. |
| R-105-01-05, R-105-01-06 | Cross-check against INTERFACE_REGISTER.csv rows for PKG-105 and the 3D model / integrated P&ID set when produced. |
| R-105-01-07 | Standards-citation review against the DBM "Governing Civil and Structural Basis" section. |
| R-105-01-08 | TBD-marker audit; confirm each open boundary/exclusion item carries a source pointer or explicit TBD. |
| R-105-01-09 | Provenance check that the SoW cites the GATE-07 snapshot path. |

## Documentation

Anticipated artifacts produced by this deliverable (DELIVERABLE_REGISTER.csv anticipated artifacts field; ARTIFACT_REGISTER.csv):

- Package scope of work (ART-B537AC5EA7)
- Tagged equipment and package identity list (ART-21C90A2BB4)
- Package function and whole-facility integration narrative (ART-1B624DB0B8)
- Package responsibility assignment record (ART-77976FD844)
