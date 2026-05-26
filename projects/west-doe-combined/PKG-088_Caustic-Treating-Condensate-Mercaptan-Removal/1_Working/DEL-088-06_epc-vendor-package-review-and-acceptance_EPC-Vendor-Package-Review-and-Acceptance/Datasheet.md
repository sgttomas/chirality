# Datasheet — DEL-088-06 EPC Vendor Package Review and Acceptance

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-088-06_epc-vendor-package-review-and-acceptance |
| Name | EPC Vendor Package Review and Acceptance |
| ParentPackageID | PKG-088 |
| PackageName | Caustic Treating (Condensate Mercaptan Removal) |
| Discipline | Mechanical |
| Type | EPC Vendor Package Acceptance |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input |
| Covers Scope Items | SOW-0055, SOW-0056, SOW-0057, SOW-0058 |
| Supports Objectives | OBJ-002 through OBJ-010 (ASSUMPTION: package-heuristic mapping) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Review subject | Vendor-engineered caustic mercaptan treating package (DEL-088-04) and vendor document turnover (DEL-088-05) | DELIVERABLE_REGISTER.csv row PKG-088 |
| Treating technology | Non-regenerative caustic mercaptan treating (Merichem or equivalent) | 3-25_Comp_and_Liquids_DBM.md §Condensate Mercaptan Treating |
| Treating capacity | 20,000 bbl/d C5+ condensate | 3-25_Comp_and_Liquids_DBM.md §Condensate Mercaptan Treating |
| Caustic regeneration | Not included in current basis | 3-25_Comp_and_Liquids_DBM.md §Condensate Mercaptan Treating |
| DSO entrainment (expected) | 30 ppmw S | 3-25_Comp_and_Liquids_DBM.md §Condensate Mercaptan Treating |
| DSO entrainment (design) | 50 ppmw S (TBC vendor) | 3-25_Comp_and_Liquids_DBM.md §Condensate Mercaptan Treating |
| Caustic solution basis | 50 wt% NaOH/H2O, SG 1.75 (TBC) | 3-25_Comp_and_Liquids_DBM.md §Condensate Mercaptan Treating |
| Acceptance authority | EPC Integrator | _CONTEXT.md; DELIVERABLE_REGISTER.csv |
| Acceptance basis documents | EPC Scope of Work (DEL-088-01), Package Datasheet (DEL-088-02), Construction Work Package (DEL-088-03) | _CONTEXT.md Scope |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service streams | Stabilized C5+ condensate from 04-25 returning to 03-25 Liquids Hub | 3-25_Comp_and_Liquids_DBM.md §Overview |
| Extractable compounds | H2S, CO2, methyl/ethyl/propyl/butyl mercaptans | 3-25_Comp_and_Liquids_DBM.md §Condensate Mercaptan Treating |
| Volatile mercaptans (basis) | methyl mercaptan, ethyl mercaptan, dimethyl sulphide, 2-propanethiol, n-propyl mercaptan, methyl ethyl sulphide | 3-25_Comp_and_Liquids_DBM.md §Products and Downstream Routing |
| Tank service (caustic) | Atmospheric 32 oz tanks; LP fuel-gas blanket; heating; insulation | 3-25_Comp_and_Liquids_DBM.md §Condensate Mercaptan Treating |
| Caustic drain max temperature | 121 deg C / 250 deg F (TBC) | 3-25_Comp_and_Liquids_DBM.md §Drains |
| Caustic drain rating | Min 300# ANSI; flange termination at spent-caustic tank | 3-25_Comp_and_Liquids_DBM.md §Drains |
| Material restriction | Aluminum shall not be used in the caustic building | 3-25_Comp_and_Liquids_DBM.md §Condensate Mercaptan Treating |

## Construction

| Item | Value | Source |
|---|---|---|
| Major package components | Caustic C5+ contactor, pre-heater, caustic outlet filter, water wash, DSO/spent/fresh-caustic/fresh-water tanks, incinerator overhead/dilution/enrichment-gas interfaces | 3-25_Comp_and_Liquids_DBM.md §Condensate Mercaptan Treating |
| Tank material/coating | TBC | 3-25_Comp_and_Liquids_DBM.md §Condensate Mercaptan Treating |
| Heat-tracing basis | 37.8 deg C / 100 deg F redundant circuits under consideration (caustic drain) | 3-25_Comp_and_Liquids_DBM.md §Drains |
| Spent caustic venting | Flame arrestor to incinerator header; truck-out supported | 3-25_Comp_and_Liquids_DBM.md §Condensate Mercaptan Treating |
| Fresh caustic VRU | Not connected to VRU | 3-25_Comp_and_Liquids_DBM.md §Condensate Mercaptan Treating |

## Anticipated Acceptance Artifacts

- Vendor document review log
- Package acceptance checklist
- Test and inspection evidence (vendor FAT, EPC integration witness)
- Turnover evidence (TBD: detailed turnover record format — location TBD)

## References

- _CONTEXT.md (deliverable identity, scope, anticipated artifacts)
- _REFERENCES.md
- _Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (sections: Overview; Scope Inclusions; Condensate Mercaptan Treating; Products and Downstream Routing; Drains)
- _Sources/26020-Package_Requirements.docx package heading 41 (location TBD — binary source not extracted)
- _Sources/26020-Packages_Interfaces_4_export.xlsx (location TBD — binary source not extracted)
- DELIVERABLE_REGISTER.csv (Gate 7 snapshot)
