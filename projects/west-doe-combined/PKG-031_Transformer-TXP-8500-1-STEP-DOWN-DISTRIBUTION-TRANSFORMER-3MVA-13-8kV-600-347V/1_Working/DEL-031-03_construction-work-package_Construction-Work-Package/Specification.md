# Specification: DEL-031-03_construction-work-package — Construction Work Package

## Scope

This specification governs the EPC Integrator-authored Construction Work Package (CWP) for `PKG-031` — Transformer TXP-8500-1, a 3 MVA 13.8 kV / 600 V (347 V neutral) step-down distribution transformer — covering physical installation, construction, inspection, tie-in to adjacent facility systems, and construction turnover.

**Included:** off-loading, setting, mechanical and electrical hookup, home-run cabling and terminations, structural support installation, area-lighting and tie-in coordination, installation/tie-in workface plan, construction interface and turnover checklist, and EPC integration with civil, electrical, controls, and instrumentation work fronts.

**Excluded:** package engineering, package design, vendor documentation, and the physical equipment package itself (Package Vendor scope under `DEL-031-04` and `DEL-031-05`); vendor factory/shop tests (carried under `DEL-031-06`); detailed civil/foundation engineering (governed by site civil package); MCC internal scope (downstream package).

## Requirements

| ID | Requirement | Source | Status |
|---|---|---|---|
| REQ-031-03-01 | The CWP shall identify TXP-8500-1 as a 3 MVA, 13.8 kV / 600 V step-down distribution transformer feeding the 600 V MCC for LV loads. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 745 | FACT |
| REQ-031-03-02 | The CWP shall assign field-construction activities (off-loading, setting, mechanical hookup, installation of shipped-loose items, structural supports, home-run cabling, electrical terminations, area lighting, and demolition where required) to Tourmaline field construction. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, lines 101-125 | FACT |
| REQ-031-03-03 | The CWP shall require ground-grid connections of the transformer at two points, with separately sized copper ground conductors per CEC. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs | FACT |
| REQ-031-03-04 | Power circuits at 13.8 kV and 600 V shall be separated from control/instrument circuits by distance, shielding, or routing per project electrical specifications. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 768 | FACT |
| REQ-031-03-05 | Cable tray and conduit routing for tie-ins shall not interfere with maintenance access at the transformer or downstream MCC. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray paragraphs | FACT |
| REQ-031-03-06 | Joint construction planning shall be performed for tie-ins to existing or related facilities; tie-in timing shall be established as the project progresses. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 127 | FACT |
| REQ-031-03-07 | Foundation, pile, settlement, frost-protection, and structural support requirements shall be confirmed against the final geotechnical report before issue for construction. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, line 141 | FACT |
| REQ-031-03-08 | The final CWP and miscellaneous facilities list shall be aligned with the plot plan, equipment list, and construction work package register before issue for construction. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, line 661 | FACT |
| REQ-031-03-09 | The CWP shall coordinate package buildings, MCC interfaces, RIO interfaces, heat tracing, HVAC, fire/gas detection, and drain/vent tie-ins with civil, electrical, controls, and instrumentation work fronts. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, line 619 | FACT |
| REQ-031-03-10 | The CWP shall produce an installation and tie-in workface plan (`ART-F476EFD32E`) and a construction interface and turnover checklist (`ART-273816BADA`). | `ARTIFACT_REGISTER.csv` rows for `DEL-031-03` | FACT |
| REQ-031-03-11 | Construction interfaces shall cover the seven workbook interface types for PKG-031: Electrical Power, Grounding/Bonding, Area/Exterior Lighting, I&C/Control Cabling, Communications/Network, Maintenance Access, Structural/Foundations/Supports. | `INTERFACE_REGISTER.csv` rows for `PKG-031` | FACT |
| REQ-031-03-12 | Transformer installation location (outdoor pad, electrical building, or skid arrangement) shall be confirmed by detailed design. | Source gap | ASSUMPTION |

## Standards

| Standard | Applicability | Location |
|---|---|---|
| Canadian Electrical Code (CEC) | Grounding conductor sizing for distribution transformers and three-phase motors >100 hp. | Referenced by `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs. Clause text — location TBD. |
| Project electrical specifications | Cable tray, conduit, grounding, bonding, and power/control circuit separation. | Referenced by `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 768. Specification document — location TBD. |
| Final geotechnical report | Foundation, pile, settlement, frost-protection, and support criteria. | Per `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, line 141. Report — location TBD; treat values as placeholders until accepted. |

## Verification

| Requirement | Verification approach |
|---|---|
| REQ-031-03-01 | Cross-check CWP cover page and tagged-equipment list against workbook row 33 and DBM transformer slice. |
| REQ-031-03-02 | Responsibility matrix review against DBM Construction Responsibility table. |
| REQ-031-03-03 | Electrical inspection at termination; visual + grounding continuity test of two ground-grid connections. |
| REQ-031-03-04 | Field walkdown verifying physical separation/shielding/routing of power vs control/instrument circuits. |
| REQ-031-03-05 | Field walkdown verifying maintenance-access clearances at transformer enclosure and MCC face. |
| REQ-031-03-06 | Tie-in coordination meeting records; tie-in schedule entries. |
| REQ-031-03-07 | Geotechnical sign-off; foundation/pile inspection records. |
| REQ-031-03-08 | CWP register alignment audit prior to IFC issue. |
| REQ-031-03-09 | Discipline-interface checklist sign-off (civil, electrical, controls, instrumentation). |
| REQ-031-03-10 | Document existence check: workface plan + turnover checklist present and signed. |
| REQ-031-03-11 | Interface matrix completeness check against `INTERFACE_REGISTER.csv` row set for `PKG-031`. |
| REQ-031-03-12 | Confirm installation-location assignment in detailed design package; remove ASSUMPTION marker. |

## Documentation

Anticipated artifacts (carried by this deliverable):

- Construction work package (`ART-7627442199`)
- Installation and tie-in workface plan (`ART-F476EFD32E`)
- Construction interface and turnover checklist (`ART-273816BADA`)

Construction records produced by execution (proposed):

- Off-loading and setting records
- Mechanical hookup punch list
- Electrical termination records (13.8 kV primary, 600 V secondary)
- Grounding continuity test results
- Foundation/structural support inspection records
- Tie-in close-out records by interface type (per `INTERFACE_REGISTER.csv`)
- Construction turnover package signed by EPC Integrator
