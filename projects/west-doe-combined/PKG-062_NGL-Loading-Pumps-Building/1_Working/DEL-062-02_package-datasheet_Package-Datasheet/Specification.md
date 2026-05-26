# Specification — DEL-062-02 Package Datasheet (NGL Loading Pumps Building, PKG-062)

> Pass 1 + Pass 2 draft. Requirements grounded in `26020-Package_Requirements.docx` (`26020-01-PT-18-003 - LPG Loading Pumps`) and the Gate-07 PROJECT_DECOMP snapshot. Inferences are labeled `ASSUMPTION`; missing values are marked `TBD`.

## Scope

### In scope (for this deliverable)

This Package Datasheet shall provide the technical handoff data required by a third-party Package Vendor and by EPC discipline engineering to engineer, design, fabricate, and supply the `PKG-062` package, and to integrate it into the facility. The Datasheet documents:

- Package identification and tagging.
- Equipment scope, configuration, capacity, and driver data.
- Operating and design conditions (or TBC placeholders where the source defers).
- Physical interface applicability across all interface types relevant to the package.
- Vendor engineering deliverables expected from the Package Vendor (as evidence carried in the Datasheet per `_CONTEXT.md` Notes).
- By-others / EPC-scope items needed for the package to operate.

Source: `26020-Package_Requirements.docx` (`26020-01-PT-18-003`, "Basic Scope" and "Vendor Engineering Deliverables"); `_CONTEXT.md` (Scope, Anticipated Artifacts).

### Out of scope (for this deliverable)

- Scope-of-work narrative covered by `DEL-062-01_scope-of-work`.
- Construction work package details covered by `DEL-062-03_construction-work-package`.
- Vendor-engineered equipment package itself covered by `DEL-062-04_vendor-engineered-equipment-package`.
- Vendor document turnover covered by `DEL-062-05_vendor-document-turnover-package`.
- Review/acceptance evidence covered by `DEL-062-06_epc-vendor-package-review-and-acceptance`.

Source: `DELIVERABLE_REGISTER.csv` rows for `PKG-062`.

## Requirements

Requirement IDs are local to this Datasheet (prefix `R-DEL-062-02-`).

### R-DEL-062-02-001 — Package identification

The Datasheet shall identify the package as `PKG-062` "NGL Loading Pumps Building" with package equipment tag `26020-01-PT-18-003` and WBS `01`.

Source: `PACKAGE_REGISTER.csv` row `PKG-062`.

### R-DEL-062-02-002 — Equipment quantity, type, and model

The Datasheet shall record 4 (four) identical Blackmer Model `LGL4B` rotary vane pumps arranged in parallel, tagged `P9510-1`, `P9520-1`, `P9530-1`, `P9540-1`.

Source: `26020-Package_Requirements.docx` (`26020-01-PT-18-003`, "Basic Scope" and "Major Included Equipment").

### R-DEL-062-02-003 — Pump hydraulic capacity (per unit, TBC TDH)

The Datasheet shall record per-pump capacity of 68 m³/hr at 345 kPad (300 USGPM at 50 psid). Total Dynamic Head (TDH) is `TBC` (To Be Confirmed) in the source and shall be carried as such until confirmed by the Package Vendor.

Source: `26020-Package_Requirements.docx` (`26020-01-PT-18-003`, "Major Included Equipment" and "Scope Notes / Open Items").

### R-DEL-062-02-004 — Process function

The Datasheet shall record the process function as "Pumps to move LPG product from storage to LPG Truck Loading."

Source: `26020-Package_Requirements.docx` (`26020-01-PT-18-003`, "Basic Scope"). See CONFLICT-1 (`Guidance.md`) regarding LPG vs. NGL labeling.

### R-DEL-062-02-005 — Driver, electrical class, control

The Datasheet shall record the driver as Electric 575 V / 3 PH / 60 Hz motors, fed from a 600 V MCC (by others), with local H-O-A or On-Off control at the package.

Source: `26020-Package_Requirements.docx` (`26020-01-PT-18-003`, "Scope Notes / Open Items").

### R-DEL-062-02-006 — Motor sizing basis

The Datasheet shall record the motor sizing basis as the inlet stabilizer composition density at −40 °C start-up condition.

Source: `26020-Package_Requirements.docx` (`26020-01-PT-18-003`, "Scope Notes / Open Items").

### R-DEL-062-02-007 — Operating and design conditions placeholders

The Datasheet shall carry operating and design conditions as `TBC` per the source until the Package Vendor confirms via the deliverables in R-DEL-062-02-013 (Pump Data Sheets, Hydraulic / NPSH Calculations).

Source: `26020-Package_Requirements.docx` (`26020-01-PT-18-003`, "Scope Notes / Open Items").

### R-DEL-062-02-008 — Building

The Datasheet shall record provision of a self-framing building erected at site, housing the four parallel pumps.

Source: `26020-Package_Requirements.docx` (`26020-01-PT-18-003`, "Major Included Equipment").

### R-DEL-062-02-009 — By-others / EPC scope statement

The Datasheet shall explicitly state that DCS integration, foundations, and electrical supply to the MCC are by others (EPC Integrator scope), so the Package Vendor receives an unambiguous battery limit.

Source: `26020-Package_Requirements.docx` (`26020-01-PT-18-003`, "Scope Notes / Open Items").

### R-DEL-062-02-010 — Physical interface applicability matrix

The Datasheet shall publish an interface applicability matrix matching the source row exactly (Yes / No values per interface type). All "Yes" interfaces require coordinated tie-in scope.

Source: `26020-Package_Requirements.docx` (`26020-01-PT-18-003`, "Physical Interface Summary"); also `PACKAGE_REGISTER.csv` row `PKG-062` "Applicable interface types".

### R-DEL-062-02-011 — Interface evidence carriage

The Datasheet shall carry interface facts (e.g., applicability, tie-in expectations) as evidence rather than producing them as standalone deliverables.

Source: `_CONTEXT.md` Notes.

### R-DEL-062-02-012 — Vendor engineering deliverables list

The Datasheet shall include the full Vendor Engineering Deliverables list grouped by category (Core vendor documents; Core package engineering; Rotating equipment / pumps; Loading / metering package; Relief / flare / vent design; Process piping interfaces; Utility piping interfaces; Drainage / containment interfaces; Electrical, lighting, EHT, grounding; Instrumentation and controls interfaces; Building / HVAC / code interfaces; Fire and gas / technical safety interfaces; Structural / foundations / supports).

Source: `26020-Package_Requirements.docx` (`26020-01-PT-18-003`, "Vendor Engineering Deliverables").

NOTE: The structural / foundations / supports group is `TBD` (source slice not fully captured in current extraction); resolve at closeout.

### R-DEL-062-02-013 — Hydraulic and motor confirmation deliverables (pointer)

The Datasheet shall name Pump Data Sheets (`MEC-007`), Mechanical Seal / Lube Oil Specification (`MEC-019`), Pump Hydraulic / NPSH Calculations (`PRO-013`), and Motor Starting Study (`ELE-011`) as the vendor deliverables that confirm the TBC capacity/operating values.

Source: `26020-Package_Requirements.docx` (`26020-01-PT-18-003`, "Vendor Engineering Deliverables", "Rotating equipment / pumps" group).

### R-DEL-062-02-014 — Scope coverage traceability

The Datasheet shall trace to scope items `SOW-0153`, `SOW-0154`, `SOW-0155`, `SOW-0156`.

Source: `SCOPE_LEDGER.csv` rows referenced; `_CONTEXT.md`.

### R-DEL-062-02-015 — Source citation discipline

Every non-trivial value on the Datasheet shall cite its `SourcePath` and `SectionRef`. Where the location is not yet known, the citation shall record "location TBD." Where the value is inferred, the entry shall be labeled `ASSUMPTION`.

Source: skill `four-documents/SKILL.md` (Non-negotiable constraints — Source-anchored).

## Standards

The source row does not enumerate governing codes for `PKG-062`. The following are commonly applicable to LPG / NGL rotary-vane truck-loading pump packages and are listed here as `ASSUMPTION: likely applicable`. Clause-level requirements shall not be derived until the standard text is locally accessible.

| Standard | Topic | Status |
|---|---|---|
| API 676 | Positive Displacement Rotary Pumps | `ASSUMPTION: likely applicable`; location TBD |
| API 670 | Machinery Protection Systems | `ASSUMPTION: likely applicable`; location TBD |
| NFPA 58 / NFPA 30 | LPG / flammable-liquid handling code | `ASSUMPTION: likely applicable`; location TBD |
| CSA Z662 (or applicable jurisdictional pipeline/piping code) | Piping interface (jurisdictional) | `ASSUMPTION: likely applicable`; location TBD |
| CEC (Canadian Electrical Code) Class I area classification | Electrical design / area classification | `ASSUMPTION: likely applicable`; location TBD |
| ASME B31.3 | Process piping | `ASSUMPTION: likely applicable`; location TBD |

The Package Vendor's Code/Standard Compliance Plan and the EPC Integrator's `REG-021` Fire Code / Building Code Compliance Package (listed in the vendor engineering deliverables) shall be the binding source once produced.

## Verification

| Requirement | Verification Approach | Evidence Artifact (from Vendor Engineering Deliverables) |
|---|---|---|
| R-DEL-062-02-002, -003, -007 | Vendor confirms equipment, capacity, and operating/design conditions on data sheet | `MEC-003` Mechanical Equipment Data Sheets; `MEC-007` Pump Data Sheets; `PRO-013` Pump Hydraulic / NPSH Calculations |
| R-DEL-062-02-005, -006 | Motor sized for -40 °C start-up density; starting study confirms MCC compatibility | `ELE-011` Motor Starting Study; `ELE-020` Electrical Equipment Data Sheets |
| R-DEL-062-02-008 | Building drawings issued and reviewed | `STR-002` Structural General Arrangement Drawings; `STR-012` Module Structural Drawings |
| R-DEL-062-02-009 | EPC scope statement reviewed against tie-in scope sheets | `PIP-004` Tie-In List / Tie-In Scope Sheets |
| R-DEL-062-02-010 | Interface matrix reconciled to interface workbook | `26020-Packages_Interfaces_4_export.xlsx` (see CONFLICT-2); `CTL-026` Package Vendor Interface Specification |
| R-DEL-062-02-012 | Vendor Document Index issued and tracked | `PRQ-009` Vendor Document Index; `DOC-008` Vendor Document Control Procedure |
| R-DEL-062-02-013 | FAT performance evidence for pumps | `MEC-021` Equipment FAT / Performance Test Procedure; `MEC-022` Equipment FAT / Performance Test Report |
| R-DEL-062-02-014 | Cross-check Datasheet content to `SCOPE_LEDGER.csv` `SOW-0153..0156` | Gate-07 snapshot SCOPE_LEDGER |
| R-DEL-062-02-015 | QA review per `four-documents/QA_CHECKS.md` | Run record + QA report |

## Documentation (artifacts that this deliverable produces or carries)

Per `_CONTEXT.md` Anticipated Artifacts and the source vendor-deliverables list, this Datasheet shall produce / carry:

- Package technical datasheet (this document set: `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`).
- Vendor engineering handoff basis (Vendor Engineering Deliverables list — `Datasheet.md`).
- Package interface requirements matrix (Physical Interface Summary table — `Datasheet.md`).
- Source-supported equipment and design criteria (capacity, driver, motor sizing, by-others — `Datasheet.md`).

Anticipated artifacts source: `_CONTEXT.md` "Anticipated Artifacts" and `DELIVERABLE_REGISTER.csv` row `DEL-062-02_package-datasheet` ("Anticipated Artifacts" column).
