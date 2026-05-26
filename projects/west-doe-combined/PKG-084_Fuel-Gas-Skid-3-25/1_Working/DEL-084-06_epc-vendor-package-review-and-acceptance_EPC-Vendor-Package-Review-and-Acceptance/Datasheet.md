# Datasheet — DEL-084-06 EPC Vendor Package Review and Acceptance

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-084-06_epc-vendor-package-review-and-acceptance |
| Name | EPC Vendor Package Review and Acceptance |
| ParentPackageID | PKG-084 |
| PackageName | Fuel Gas Skid 3-25 |
| Discipline | Mechanical |
| Type | EPC Vendor Package Acceptance |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input |
| Facility | 03-25 West Doe Compressor Station and Liquids Hub (LSD 03-25-80-15W6) (source: 3-25_Comp_and_Liquids_DBM.md sec. Site/Facility Description) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Acceptance Object | Vendor-supplied Fuel Gas Skid package for PKG-084 | DELIVERABLE_REGISTER.csv row 329 |
| Acceptance Basis Documents | EPC Scope of Work (DEL-084-01); Package Datasheet (DEL-084-02); Construction Work Package (DEL-084-03) | DELIVERABLE_REGISTER.csv rows 324-326 |
| Upstream Vendor Production Units | DEL-084-04 Vendor Engineered Equipment Package; DEL-084-05 Vendor Document Turnover Package | DELIVERABLE_REGISTER.csv rows 327-328 |
| Covered SOW Items | SOW-0095, SOW-0096, SOW-0097, SOW-0098 | _CONTEXT.md |
| Supported Objectives | OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | _CONTEXT.md (ASSUMPTION: package-grouping heuristic) |
| Package Service | LP fuel gas supply for stripping, blanketing, purge, dilution/enrichment, building heaters, utility users at 03-25 | 3-25_Comp_and_Liquids_DBM.md sec. Fuel Gas |
| Primary Source Supply | Enbridge sales-gas pipeline through 04-25 sales-gas splitter; Alliance secondary source | 3-25_Comp_and_Liquids_DBM.md sec. Fuel Gas |
| Normal Fuel-Gas Total Demand | 1.382 MMSCFD (39.13 e3m3/d) | 3-25_Comp_and_Liquids_DBM.md sec. Fuel Gas |
| Design Fuel-Gas Total Demand | > 1.5 MMSCFD (42.5 e3m3/d) | 3-25_Comp_and_Liquids_DBM.md sec. Fuel Gas |
| LP Fuel-Gas Design Flow | TBC (source: 3-25_Comp_and_Liquids_DBM.md sec. Fuel Gas) | source |
| LP Fuel-Gas Scrubber | V-3210-2, downstream of heater, K=0.35, liquids to slop TK-9130-2 | 3-25_Comp_and_Liquids_DBM.md sec. Fuel Gas |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Site Ambient Design Range | -40 deg C to +35 deg C | 3-25_Comp_and_Liquids_DBM.md sec. Site Conditions |
| Site Elevation | 673 m AMSL | 3-25_Comp_and_Liquids_DBM.md sec. Site Conditions |
| Emergency Buyback Fuel Gas | UNRESOLVED — W242510 indicates not required; Process_DBM_fixed includes it in 04-25 utility package | 3-25_Comp_and_Liquids_DBM.md sec. Fuel Gas (NEEDS_HUMAN_RULING) |
| Sweet-Gas Purge Hazard Basis | Methyl mercaptan toxicity/odour; formal hazard review required | 3-25_Comp_and_Liquids_DBM.md sec. Fuel-Gas Sulphur and Purge Hazard Basis |

## Construction (Acceptance Evidence Set)

| Item | Description | Source |
|---|---|---|
| Vendor document review log | Reviewer log of vendor submittals against the EPC SOW, Package Datasheet, and CWP | _CONTEXT.md (Anticipated Artifacts) |
| Package acceptance checklist | Itemized acceptance checklist covering scope completeness, interface compliance, documentation, and test/inspection | _CONTEXT.md (Anticipated Artifacts) |
| Test/inspection evidence | FAT, SAT, NDE, pressure-test, functional-test records as required by the package basis | _CONTEXT.md (Anticipated Artifacts) (location TBD for specific test/inspection requirements) |
| Turnover evidence | Record of mechanical-completion, punchlist closure, and handoff to commissioning | _CONTEXT.md (Anticipated Artifacts); 3-25_Comp_and_Liquids_DBM.md sec. Isolation/Maintenance |

## References

- 3-25_Comp_and_Liquids_DBM.md (source slices: Fuel Gas; Fuel-Gas Sulphur and Purge Hazard Basis; Site Conditions; Utilities)
- 26020-Package_Requirements.docx package heading 37 (location TBD — binary source not parsed in this run)
- 26020-Packages_Interfaces_4_export.xlsx Packages row 60 (location TBD — binary source not parsed in this run)
- GATE-07 DELIVERABLE_REGISTER.csv rows 324-329 (PKG-084 deliverable set)
- DEL-084-01 Scope of Work, DEL-084-02 Package Datasheet, DEL-084-03 Construction Work Package (acceptance basis documents — content TBD pending sibling-deliverable drafting)
