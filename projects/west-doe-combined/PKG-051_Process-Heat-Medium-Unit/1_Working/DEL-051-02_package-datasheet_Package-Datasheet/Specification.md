# Specification — DEL-051-02 Package Datasheet (Process Heat Medium Unit)

## Scope

### In Scope

- Define the technical package data required for third-party vendor or discipline package engineering and design of the Process Heat Medium Unit (PKG-051; CoA tag 26020-01-15-001; docx tag 26020-01-PT-15-001). [`_CONTEXT.md` → Scope]
- Carry the equipment list, design parameters, and physical interface declarations for the package, drawn from `26020-Package_Requirements.docx` (heading 6) and `26020-Packages_Interfaces_4_export.xlsx` (row ID# 51). [`_REFERENCES.md`]
- Provide the EPC anchor point that downstream interface, datasheet, and discipline deliverables reference. [`_CONTEXT.md` → Notes]
- Covers scope items SOW-0165, SOW-0166, SOW-0167, SOW-0168. [`_CONTEXT.md`]

### Out of Scope

- Vendor-internal engineering, fabrication, and detailed design (responsibility of the package vendor).
- Detailed P&IDs, datasheets for individual mechanical items beyond the package boundary, and discipline-specific design documents (covered by other deliverables in PKG-051 and adjacent packages).
- Process simulation and heat-medium duty calculations (not in the available source slice — TBD).

## Requirements

Identifier convention: REQ-051-02-NN. Each requirement cites its source slice. `ASSUMPTION` labels mark inferred requirements; `TBD` marks unresolved values.

| ID | Requirement | Source / Note |
|---|---|---|
| REQ-051-02-01 | The package SHALL implement a closed-loop hot-oil / heat-medium heating system that supplies heat to process users via pumped thermal heating fluid. | docx → Basic Scope |
| REQ-051-02-02 | The system SHALL provide a hot loop and a cold loop, with hot/cold mixing used to deliver optimum supply temperature to users. | docx → Basic Scope |
| REQ-051-02-03 | The Supply Pump Module SHALL include one expansion tank and three heat-medium pumps. | docx → Basic Scope |
| REQ-051-02-04 | The Medium Heater Module SHALL include one medium heater, one heater blower, and one air intake pre-heater. | docx → Basic Scope |
| REQ-051-02-05 | The expansion tank SHALL be horizontal; size and capacity SHALL be advised by the vendor. | docx → Major Included Equipment |
| REQ-051-02-06 | At 274 °C the expansion volume SHALL not exceed 85% fill of the expansion tank. | docx → Major Included Equipment |
| REQ-051-02-07 | Expansion tank operating pressure SHALL be 125–240 kPag (18–23 psig), selected based on heat-medium NPSHR. | docx → Major Included Equipment |
| REQ-051-02-08 | Heat-medium pumps SHALL be single-stage vertical inline, configured 3 × 66%. | docx → Major Included Equipment |
| REQ-051-02-09 | Heat-medium pump design pressure SHALL be 2413 kPag (350 psig). | docx → Major Included Equipment |
| REQ-051-02-10 | Heat-medium pump operating pressure SHALL be 695 kPag (100 psig). | docx → Major Included Equipment |
| REQ-051-02-11 | Heat-medium pump operating temperature SHALL be TBD. | docx text truncated ("...and temp.") |
| REQ-051-02-12 | Assumed start-up temperature SHALL be 20 °C (68 °F). | docx → Major Included Equipment |
| REQ-051-02-13 | Maximum bulk fluid temperature SHALL not exceed 260 °C (500 °F). | docx → Major Included Equipment |
| REQ-051-02-14 | Heat transfer fluid SHALL be a Petro-Canada Petrotherm-family product. (ASSUMPTION on spelling; docx reads "Peterotherm".) | docx → Major Included Equipment |
| REQ-051-02-15 | The package SHALL provide and coordinate the physical interfaces marked applicable in `26020-Packages_Interfaces_4_export.xlsx` row ID# 51: Utility Piping; Drain/Containment; Electrical Power; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports. | xlsx → Packages row ID# 51 |
| REQ-051-02-16 | Vendor Engineering Deliverables SHALL be enumerated by the vendor in alignment with EPC Integrator handoff requirements. Specific list is TBD (source heading present but body empty). | docx → Vendor Engineering Deliverables |
| REQ-051-02-17 | Interface coordination notes specific to this package are TBD (docx body: "TBD."). | docx → Interface Coordination Notes |

## Standards

| Standard | Applicability | Source / Note |
|---|---|---|
| ASME/ANSI piping standards for hot-oil systems | ASSUMPTION: likely applicable for design pressures cited; specific clauses TBD. | Inferred from discipline = Mechanical; location TBD |
| Heat transfer fluid vendor data (Petro-Canada Petrotherm) | Applicable for fluid selection, max bulk temperature limits, fire-point and degradation criteria. | docx; vendor data not in source set — location TBD |
| Site-specific electrical area classification, F&G, structural codes | Applicable per project EPC basis. | TBD — not in available source slice |

## Verification

| Requirement | Verification Approach |
|---|---|
| REQ-051-02-01 to -04 | Design review of vendor package P&ID and equipment list against scope statements. |
| REQ-051-02-05 to -07 | Expansion-tank datasheet review; vendor calculation of fill volume at 274 °C; NPSHR-driven pressure setting review. |
| REQ-051-02-08 to -11 | Pump datasheet and hydraulic curve review; confirm 3 × 66% standby philosophy; operating-temperature confirmation closes TBD. |
| REQ-051-02-12, -13 | Operating-envelope check against design basis; confirm relief, expansion, and material ratings for 260 °C bulk. |
| REQ-051-02-14 | Confirm fluid grade with Petro-Canada datasheet; verify fluid is rated for 260 °C continuous service. |
| REQ-051-02-15 | Interface walk-down against the workbook interface row; cross-check with applicable discipline deliverables. |
| REQ-051-02-16, -17 | Close TBDs by vendor scope-of-supply submission and EPC interface coordination meetings. |

## Documentation

Anticipated artifacts (from `_CONTEXT.md` → Anticipated Artifacts):

- Package technical datasheet (this deliverable).
- Vendor engineering handoff basis (cross-references vendor deliverables list once populated).
- Package interface requirements matrix (constructed from the xlsx interface row).
- Source-supported equipment and design criteria summary.

Additional documents implied by source: vendor-supplied expansion-tank datasheet, pump datasheets, heater datasheet, fluid selection record. All TBD pending vendor submission.
