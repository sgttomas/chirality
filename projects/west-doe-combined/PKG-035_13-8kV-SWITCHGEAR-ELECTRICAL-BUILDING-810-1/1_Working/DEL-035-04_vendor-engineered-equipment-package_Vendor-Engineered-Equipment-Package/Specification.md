# Specification: DEL-035-04 — Vendor Engineered Equipment Package

## Scope

This Specification governs the Package Vendor's engineering, design, fabrication/supply, and physical equipment package for `PKG-035` — 13.8kV Switchgear Electrical Building (810-1), workbook row 37, package tag `26020-01-30-026`. The Vendor Engineered Equipment Package is developed from the EPC Scope of Work (`DEL-035-01`) and EPC Package Datasheet (`DEL-035-02`). EPC Integrator retains facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration responsibility (`PACKAGE_REGISTER.csv` PKG-035).

Excluded: facility-level integration, civil sitework outside the building envelope, and any work not assigned to "Package Vendor" in the PKG-035 register row.

## Requirements

| Req ID | Requirement | Source |
|---|---|---|
| R-035-04-001 | The vendor engineered package shall realize a prefabricated modular electrical building housing 13.8 kV main switchgear and the supporting low-voltage / UPS / control equipment defined for an electrical building in the Deepcut DBM. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Electrical Buildings) |
| R-035-04-002 | The 13.8 kV switchgear shall be 13.8 kV, 3-phase, 3-wire, 60 Hz, low-resistance grounded, sized for the full facility scope as the plant main power distribution center. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Medium-voltage services; Facility electrical system) |
| R-035-04-003 | The switchgear bus shall accept the utility-fed 25 kV/13.8 kV 50 MVA transformer source and provide radial feeders to 820-1, 830-1, 840-1, 850-1, and 860-1 electrical buildings via step-down transformers. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Facility electrical system; radial distribution list) |
| R-035-04-004 | The electrical building shall be shop-built (modular), located in a general purpose area, and elevated on piles to permit bottom cable entry. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Electrical Buildings; shop/field table for 810-1) |
| R-035-04-005 | HVAC shall be n+1 such that loss of one HVAC unit does not affect building heating and cooling. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| R-035-04-006 | All major electrical equipment shall be grounded to the ground grid at two points, with bolted test connections at ground wells. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| R-035-04-007 | Building wiring shall be TECK and ACIC cables; EMT conduit only between adjacent panels; an outdoor GFI receptacle shall be provided for exterior maintenance. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| R-035-04-008 | Equipment doors shall be sized for, or include removable transom sections to allow, removal of the largest equipment. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| R-035-04-009 | Separation between the electrical building and any fired heater shall be at least 25 m (82 ft) per OGAOM Sec. 9.6.15. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| R-035-04-010 | The vendor scope shall include package engineering, package design, vendor documentation, and the physical equipment package per PKG-035 ownership statement. | `PACKAGE_REGISTER.csv` PKG-035 |
| R-035-04-011 | The vendor design shall expose interfaces of the types declared for PKG-035 (Electrical Power; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Communications/Network; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Utility Piping; Drain/Containment; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports) for EPC Integrator integration. | `PACKAGE_REGISTER.csv` PKG-035 |
| R-035-04-012 | Short-circuit duty, BIL, continuous current, arc-flash classification, and enclosure ratings for the 13.8 kV switchgear lineup shall be established from the EPC Package Datasheet (`DEL-035-02`). | `DELIVERABLE_REGISTER.csv` DEL-035-02 (EPC handoff basis); values `TBD` until datasheet content is accepted |

## Standards

| Standard / Source | Applicability | Location |
|---|---|---|
| West Doe Deepcut DBM, Section "Electrical Design Basis" and "Electrical Buildings" | Governing design basis for facility electrical system, electrical buildings, and the 13.8 kV switchgear role | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| OGAOM Sec. 9.6.15 | Separation distance from fired heaters | Cited in `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`; OGAOM text not in local source set (location TBD) |
| `26020-Package_Requirements.docx` | Project-wide package requirements; not parsed in P1/P2 (binary docx) | `_Sources/26020-Package_Requirements.docx` (location TBD until parsed) |
| Applicable codes and standards for MV switchgear (e.g., IEEE C37, ANSI, CSA) | ASSUMPTION: standard industry codes apply; not asserted from local source | location TBD |

## Verification

| Req ID | Verification Approach |
|---|---|
| R-035-04-001 / R-035-04-004 | Vendor general arrangement and architectural drawings; physical inspection at shop; modularity / shop-build confirmation against electrical building shop/field table |
| R-035-04-002 / R-035-04-003 | Single-line diagram review against DBM; factory acceptance test of switchgear; integration test against utility transformer feed; radial feeder schedule reconciliation against electrical building list |
| R-035-04-005 | HVAC unit count and changeover test for n+1 operation |
| R-035-04-006 | Grounding inspection: two-point grid connections verified; ground well bolted-connection test |
| R-035-04-007 / R-035-04-008 | Wiring inspection (TECK/ACIC, EMT, GFI); door / transom sizing check against largest equipment piece |
| R-035-04-009 | Plot plan review confirming ≥25 m separation from fired heaters |
| R-035-04-010 / R-035-04-011 | Vendor documentation register and interface matrix reviewed by EPC Integrator (DEL-035-06) |
| R-035-04-012 | Comparison of vendor design data sheet vs. EPC Package Datasheet (DEL-035-02); FAT short-circuit and BIL evidence |

## Documentation

Vendor shall produce, as the engineered package set:

- Vendor package design basis and datasheet set (per anticipated artifacts in `_CONTEXT.md`).
- Single-line diagram, three-line diagram, and protection coordination basis for the 13.8 kV lineup.
- General arrangement, equipment layout, and cable entry drawings for the modular building.
- Grounding plan and HVAC arrangement.
- Interface schedule covering the PKG-035 declared interface types.
- Factory acceptance test plan and reports.
- Inputs to the Vendor Document Turnover Package (`DEL-035-05`) and EPC Vendor Package Review and Acceptance (`DEL-035-06`).
