# Datasheet — DEL-072-06 EPC Vendor Package Review and Acceptance

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-072-06_epc-vendor-package-review-and-acceptance |
| Name | EPC Vendor Package Review and Acceptance |
| ParentPackageID | PKG-072 |
| PackageName | Truck Product Loading Unit 4-25 |
| Workbook Tracking Number | 26020-01-23-001 (workbook Packages row 99) |
| Discipline | Mechanical |
| Type | EPC Vendor Package Acceptance |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input |
| Facility | 04-25 West Doe Deepcut Gas Plant; Unit 03/04-25-80-15 W6M (source: 4-25_Deepcut_DBM.md sec. 2.2 Site Data Basis) |

ASSUMPTION: Although the workbook package name carries the label "Truck Product Loading Unit 4-25," sibling deliverable DEL-072-01 (Specification.md) identifies the tagged equipment in this package as a low-pressure fuel-gas skid (skid, LP fuel-gas heater, LP fuel-gas scrubber) serving the West Doe Deep Cut Facility. This package taxonomy is treated here consistently with DEL-072-01; if the workbook label is intended to govern instead, raise as a human ruling (see Guidance Conflict Table CONFLICT-0).

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Acceptance Object | Vendor-supplied package for PKG-072 (LP fuel-gas scrubbing, heating, and distribution skid per DEL-072-01 tagged equipment list) | DELIVERABLE_REGISTER.csv row 563; DEL-072-01 Specification.md |
| Acceptance Basis Documents | EPC Scope of Work (DEL-072-01); Package Datasheet (DEL-072-02); Construction Work Package (DEL-072-03) | DELIVERABLE_REGISTER.csv rows 558-560 |
| Upstream Vendor Production Units | DEL-072-04 Vendor Engineered Equipment Package; DEL-072-05 Vendor Document Turnover Package | DELIVERABLE_REGISTER.csv rows 561-562 |
| Covered SOW Items | SOW-0245, SOW-0246, SOW-0247, SOW-0248 | _CONTEXT.md; DELIVERABLE_REGISTER.csv row 563 |
| Supported Objectives | OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | _CONTEXT.md (ASSUMPTION: package-grouping heuristic per OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC) |
| Package Service | LP fuel gas supply for stripping, blanketing, purge, dilution/enrichment, building heating, and other utility users at 04-25 (shared with 03-25 per DBM) | 4-25_Deepcut_DBM.md sec. Fuel Gas Basis; DEL-072-01 Specification.md |
| Shared-Utility Scope | Fuel gas building/infrastructure shared with instrument air; 03-25/04-25 demand split and facility-boundary isolation philosophy not finalized in current basis | 4-25_Deepcut_DBM.md sec. Fuel Gas Basis |
| Normal Source | Plant fuel gas drawn upstream of the expander-compressor; no normal bulk filtration | 4-25_Deepcut_DBM.md sec. Fuel Gas Design Values |
| Emergency Buyback Source | Sales pipeline via independent regulators; MAOP estimate 9928 kPag pending DE verification | 4-25_Deepcut_DBM.md sec. Emergency Buyback and Purge |
| LP Fuel-Gas Scrubber | Tag location TBD for PKG-072; design K factor max 0.35 Imperial with operating-pressure derating; liquids route to TK-9130-1 (DBM basis) | 4-25_Deepcut_DBM.md sec. Fuel Gas Equipment and Controls |
| LP Fuel-Gas Heater | Electric resistance, SCR-controlled; skin-temperature thermocouple override; duty TBD pending DE | 4-25_Deepcut_DBM.md sec. Fuel Gas Equipment and Controls |
| Regulator Sparing Philosophy | Minimum 2 x 100% spare regulators; individually isolatable; outlet test connections; pilot-type with individual pilot isolation | 4-25_Deepcut_DBM.md sec. Fuel Gas Equipment and Controls |
| Emergency Generator Fuel Gas | < 66 psig at supply; design flow 0.468 MMSCFD; start-gas 3.6 MMSCFD for 30 s (TBC) | 4-25_Deepcut_DBM.md sec. Fuel Gas Equipment and Controls |
| Design Flow (per SOW-0248) | > 8.4 MMSCFD | DEL-072-01 Specification.md R-072-01-05 (echoes SCOPE_LEDGER.csv SOW-0248) |
| Operating Pressure (per SOW-0248) | 150 psig | DEL-072-01 Specification.md R-072-01-05 |
| Design Pressure (per SOW-0248) | 150 psig | DEL-072-01 Specification.md R-072-01-05 |
| Design Temperature (per SOW-0248) | -40 C to 35 C | DEL-072-01 Specification.md R-072-01-05 |
| Final Flow | TBD | SCOPE_LEDGER.csv SOW-0248 (carried as TBD) |
| MAWP | TBD | SCOPE_LEDGER.csv SOW-0248 (carried as TBD) |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Site Location | North of Dawson Creek, BC; Plant elevation 673 m AMSL | 4-25_Deepcut_DBM.md sec. 2.2 Site Data Basis |
| Design Ambient Temperature | -40 deg C minimum to +35 deg C maximum | 4-25_Deepcut_DBM.md sec. 2.2 Site Data Basis |
| Extreme Ambient Temperature | -49.2 deg C minimum; 38.9 deg C maximum | 4-25_Deepcut_DBM.md sec. 2.2 Site Data Basis |
| Snow Load Ss / Sr | 2.5 kPa / 0.2 kPa | 4-25_Deepcut_DBM.md sec. 2.2 Site Data Basis |
| Hourly Wind Pressure (1/50) | 0.40 kPa | 4-25_Deepcut_DBM.md sec. 2.2 Site Data Basis |
| Climate Code Basis | NBC Canada 2020 IDF, Dawson Creek station (worst case) | 4-25_Deepcut_DBM.md sec. 2.2 Site Data Basis |
| Fuel Gas H2S, expander-compressor inlet | < 6 mg/m3 (low/start-up, design, high) | 4-25_Deepcut_DBM.md sec. Fuel Gas Design Values |
| Fuel Gas Water Content (J-T / expander) | < 0.1 ppmv H2O (normal); upset <= 4 lb H2O/MMSCF | 4-25_Deepcut_DBM.md sec. Fuel Gas Design Values |
| Fuel Gas Supply Pressure (J-T mode) | High 2895 kPag; expected < 2561 kPag (TBC) | 4-25_Deepcut_DBM.md sec. Fuel Gas Design Values |
| Fuel Gas Heating Value (J-T design) | 1040 LHV BTU/SCF | 4-25_Deepcut_DBM.md sec. Fuel Gas Design Values |
| Sweet-Gas Purge Hazard Basis | Methyl mercaptan IDLH 150 ppmv; acute LC50 675 ppmv; fuel gas not assumed safe across all modes; hazard review required | 4-25_Deepcut_DBM.md sec. Emergency Buyback and Purge |
| Total Buyback Fuel Gas Demand | TBC; individual loads tabulated (start gas 3.6 MMSCFD; heat-medium heater 3.90 MMSCFD; TEG stripping 0.30 MMSCFD; compressor packing 0.15 MMSCFD; others TBC) | 4-25_Deepcut_DBM.md sec. Emergency Buyback and Purge |
| Acid-Gas Compressor Worst-Case Dilution Demand | Up to 23.8 MMSCFD instantaneous; inclusion in buyback sizing TBD | 4-25_Deepcut_DBM.md sec. Emergency Buyback and Purge |

## Construction (Acceptance Evidence Set)

| Item | Description | Source |
|---|---|---|
| Vendor document review log | Reviewer log of vendor submittals against EPC SOW (DEL-072-01), Package Datasheet (DEL-072-02), and CWP (DEL-072-03) | _CONTEXT.md (Anticipated Artifacts) |
| Package acceptance checklist | Itemized checklist covering scope completeness, interface compliance, documentation, and test/inspection results | _CONTEXT.md (Anticipated Artifacts) |
| Test/inspection evidence | FAT, SAT (where applicable), NDE, pressure-test, functional-test, regulator sparing/isolation verification records | _CONTEXT.md (Anticipated Artifacts); 4-25_Deepcut_DBM.md sec. Fuel Gas Equipment and Controls (specific ITP location TBD) |
| Turnover evidence | Mechanical-completion certificate, punchlist (open/cleared), system handover sign-off | _CONTEXT.md (Anticipated Artifacts) |

## References

- 4-25_Deepcut_DBM.md (source slices: 2.2 Site Data Basis; Fuel Gas Basis; Fuel Gas Design Values; Fuel Gas Equipment and Controls; Emergency Buyback and Purge)
- 26020-Package_Requirements.docx package heading 26 (location TBD — binary source not parsed in this run)
- 26020-Packages_Interfaces_4_export.xlsx Packages row 99 (location TBD — binary source not parsed in this run)
- GATE-07 DELIVERABLE_REGISTER.csv rows 558-563 (PKG-072 deliverable set)
- DEL-072-01 Scope of Work (Specification drafted), DEL-072-02 Package Datasheet, DEL-072-03 Construction Work Package (acceptance basis documents; sibling-deliverable maturity TBD beyond DEL-072-01)
