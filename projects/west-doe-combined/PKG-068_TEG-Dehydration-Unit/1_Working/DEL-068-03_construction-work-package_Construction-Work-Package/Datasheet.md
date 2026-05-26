# Datasheet: DEL-068-03 — Construction Work Package (TEG Dehydration Unit)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-068-03_construction-work-package` | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row 548 |
| Name | Construction Work Package | DELIVERABLE_REGISTER.csv row 548 |
| Parent Package | `PKG-068` — TEG Dehydration Unit | PACKAGE_REGISTER.csv row 97 |
| Workbook Reference | row 97; WBS 01 (04-25 Deepcut) | PACKAGE_REGISTER.csv row 97 |
| Discipline | Mechanical | PACKAGE_REGISTER.csv row 97 |
| Deliverable Type | EPC Construction Work Package | DELIVERABLE_REGISTER.csv row 548 |
| Responsible Party | EPC Integrator | DELIVERABLE_REGISTER.csv row 548; OBJ-004 |
| Vendor (counterparty) | Package Vendor (owns engineering, design, vendor docs, equipment) | PACKAGE_REGISTER.csv row 97 |
| Covers Scope Items | SOW-0237, SOW-0238, SOW-0239, SOW-0240 | SCOPE_LEDGER.csv |
| Supports Objectives | OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | OBJECTIVE_DELIVERABLE_MAP.csv; ASSUMPTION (PACKAGE_HEURISTIC) |

## Attributes — Package Being Installed

| Attribute | Value | Source |
|---|---|---|
| Package title | TEG Dehydration Unit (26020-01-PT-22-001) | PACKAGE_REGISTER.csv row 97 |
| Service classification | Common equipment — single train serves the facility; must be removed from service for maintenance | 4-25_Deepcut_DBM.md line 2429 |
| Process role | Process-gas TEG dehydration downstream of amine treating; upstream of molecular-sieve dehydration | 4-25_Deepcut_DBM.md SEC-06; lines 1098, 1105, 1113 |
| Major included equipment | Inlet Air Cooler, Filter Coalescer, TEG Contactor, Glycol Flash Tank, Glycol Reboiler/Still Column, Glycol Circulation Pumps, Glycol Particulate Filters, Glycol Charcoal Filter, Gas/Glycol Exchanger, Air/Glycol Exchanger, Fuel Gas Scrubber, TEG Make-up Tank, Burner Control Panel | PACKAGE_REGISTER.csv row 97; SOW-0238; SOW-0239 |
| Module assignment (Deepcut layout) | Module 520 (HP gas filtration, sweetening, TEG dehy); Module 570 (TEG regeneration module/building) | 4-25_Deepcut_DBM.md lines 1131, 1133, 2795 |
| Vendor document basis | 26020-Package_Requirements.docx package heading 23 | DELIVERABLE_REGISTER.csv row 548; PACKAGE_REGISTER.csv row 97 |

## Conditions — Construction & Installation Envelope

| Condition | Value | Source |
|---|---|---|
| Design pressure (process side) | 1,480 psig | SOW-0240 |
| Design temperature (process side) | 150 °F | SOW-0240 |
| Design throughput basis | 360 MMSCFD design flow (Appendix A reference) | SOW-0240 |
| Piping classification (heat medium reference) | ASME Category D — heat-medium loop reference value; package-internal piping classification TBD | 4-25_Deepcut_DBM.md line 1933; TBD for package piping |
| TEG reboiler heat-medium supply | 425 °F heat medium via mixing valves | 4-25_Deepcut_DBM.md lines 1214, 1375 |
| Module fabrication location | TEG Dehydration Module identified as Shop (570-1) | 4-25_Deepcut_DBM.md line 2795 |
| Lease boundary tie-in start | First aboveground flange within 04-25 lease boundary (general front-end basis applies) | 4-25_Deepcut_DBM.md line 573 |
| By-others exclusions | Interconnecting piping, foundations, electrical supply to burner control panel | SOW-0240 |

## Construction — Scope Composition

| Construction Element | Notes | Source |
|---|---|---|
| Receive & set vendor-built skids/modules | Module 520 and Module 570 contents per DBM module table | 4-25_Deepcut_DBM.md lines 1131, 1133 |
| Foundations & supports installation | By EPC Integrator (excluded from vendor scope) | SOW-0240; OBJ-008 |
| Interconnecting process piping & tie-ins | By EPC Integrator (excluded from vendor scope) | SOW-0240; IFC-5242875251 (Process Piping); IFC-8AFEC4B531 (Utility Piping) |
| Relief/flare/vent and drain/containment tie-ins | EPC integration to LP/HP flare and drain headers | IFC-9432C19C68; IFC-0CC21E6251; 4-25_Deepcut_DBM.md line 2029 |
| Electrical power and EHT installation | Burner control panel power excluded from vendor scope; cathodic protection, grounding/bonding | SOW-0240; IFC-230C589A38; IFC-A75CF67B27; IFC-BBADD0BD10; OBJ-005 |
| I&C and control cabling integration | Package controls to plant DCS/SIS; F&G interfaces | IFC-ECD6D46F5A; IFC-AC3A79E94B; OBJ-006 |
| Area lighting; building HVAC / services | Where Module 570 includes a building | IFC-2A49A0639A; IFC-A4653976DF; 4-25_Deepcut_DBM.md line 1133 |
| Maintenance access provisions | Common-equipment maintenance access required | IFC-7286F463F5; 4-25_Deepcut_DBM.md line 2429 |
| Structural foundations / pipe-rack / platforms | Civil/structural support | IFC-0B65AE534B; OBJ-008 |
| Construction interface and turnover checklist | Anticipated artifact | DELIVERABLE_REGISTER.csv row 548 |
| Installation and tie-in workface plan | Anticipated artifact | DELIVERABLE_REGISTER.csv row 548 |

## References

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (deliverable-local)
- `DELIVERABLE_REGISTER.csv` row 548 (GATE-07 snapshot)
- `PACKAGE_REGISTER.csv` row 97 (GATE-07 snapshot)
- `SCOPE_LEDGER.csv` rows SOW-0237..SOW-0240
- `INTERFACE_REGISTER.csv` 13 interfaces flagged YES for PKG-068
- `OBJECTIVE_REGISTER.csv` OBJ-001, OBJ-003..OBJ-010
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-06 (TEG dehy), modules table, common-equipment basis, heat-medium basis, flare basis
- `_Sources/26020-Package_Requirements.docx` package heading 23 — TBD: not extracted to markdown; cited at location TBD inside source
