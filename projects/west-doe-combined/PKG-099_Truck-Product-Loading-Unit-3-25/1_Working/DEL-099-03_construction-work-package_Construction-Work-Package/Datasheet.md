# Datasheet — DEL-099-03 Construction Work Package (PKG-099 Truck Product Loading Unit 3-25)

> Descriptive datasheet for the EPC Construction Work Package covering the truck product (condensate) loading stations in PKG-099 at the 03-25 West Doe Compressor Station and Liquids Hub.

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-099-03_construction-work-package` |
| Name | Construction Work Package |
| ParentPackageID | `PKG-099` |
| PackageName | Truck Product Loading Unit 3-25 |
| Discipline | Mechanical |
| Type | EPC Construction Work Package |
| ResponsibleParty | EPC Integrator |
| Facility | 03-25 West Doe Compressor Station and Liquids Hub, LSD 03-25-80-15 W6M, north of Dawson Creek, BC (`SourcePath: _Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, `SectionRef: Site Basis`) |
| Covers ScopeItems | SOW-0241; SOW-0242; SOW-0243; SOW-0244 |
| Supports Objectives | OBJ-002; OBJ-003; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 (ASSUMPTION: package-grouping heuristic) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package equipment (per PACKAGE_REGISTER) | Two (2) truck loading and unloading stations, each capable of loading two trucks simultaneously (2x2) | PACKAGE_REGISTER.csv row PKG-099 |
| Package equipment (per DBM SEC-06 / SEC-10) | Three (3) condensate truck-loading stations, each with a dedicated loading pump | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Condensate Storage and Product Handling; Miscellaneous Facilities |
| Equipment tag basis | 26020-03-PT-23-001 — Condensate Truck Loading Stations | PACKAGE_REGISTER.csv row PKG-099 (Word Source Basis: RFQ 26020-03-PT-RFQ-23-001) |
| Process service | Sweet Dehydrated Condensate (stabilized C5+) pumped from Condensate Storage Tanks via Truck Loading pumps to loading stations; metered into atmospheric condensate trucks | PACKAGE_REGISTER.csv row PKG-099 (deliverable narrative) |
| Truck loading station capacity | 103 m3/h per station, 345 kPad differential | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Condensate Storage and Product Handling |
| Loading pumps | One condensate loading pump per truck loading station; electric motor driven | DBM Condensate Storage and Product Handling; DBM SEC-08 Prime Movers |
| Construction artifact set | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist | DELIVERABLE_REGISTER.csv row DEL-099-03; _CONTEXT.md Anticipated Artifacts |
| Site ambient design temperature (governing) | -40 deg C minimum to +35 deg C maximum (governs exposed equipment, packages, instrumentation, road design) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Site Basis; SEC-11 Site and Civil Conditions |
| Site elevation | 673 m AMSL | DBM Site and Civil Conditions |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Product handled | Sweet, stabilized C5+ condensate (post-mercaptan-treating) loaded to atmospheric trucks | DBM SEC-06 Liquids Hub Process; PACKAGE_REGISTER.csv row PKG-099 |
| Loading hydraulics | 103 m3/h per station, 345 kPad differential head provided by dedicated loading pumps | DBM Condensate Storage and Product Handling |
| Truck movement design basis | Truck-loading areas shall provide access, turning, queuing, and spill-control provisions for condensate traffic; road design accounts for -40 deg C winter operation | DBM SEC-11 Roads and Access |
| Civil truck-loading slab basis | Truck-loading slabs and structures require equipment-specific foundation and anchorage checks per final geotechnical report and snow/wind/seismic criteria | DBM SEC-11 Civil Conditions; Foundations |
| Vapour handling | Truck-loading vapour handling and VRU integration governed by liquids hub VRU basis (two 200 hp electric-drive VRUs collect tank-system vapours; truck-loading vapour return TBD) | DBM Vapour Recovery; clause-level location TBD |
| Applicable package interface types | Process Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports; Product Loading | PACKAGE_REGISTER.csv row PKG-099 (eleven interface types) |
| Electrical basis | Loading pump motors and station electrical loads supplied from shared cross-facility electrical system supplied from 04-25 | DBM SEC-12 Electrical Design Basis |
| Fire & gas detection scope | LEL, H2S, methyl mercaptan, and fire detection devices placed per process hazards including truck loading; quantity, set points, voting logic TBD pending detailed design | DBM SEC-13 (Fire & Gas references); ASSUMPTION on inclusion |

## Construction

| Item | Value | Source |
|---|---|---|
| EPC Integrator scope (governing this deliverable) | Integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration | PACKAGE_REGISTER.csv row PKG-099 |
| Package Vendor scope (boundary) | Package engineering, package design, vendor documentation, and physical equipment package for the truck loading stations | PACKAGE_REGISTER.csv row PKG-099 |
| Anchor artifacts produced | Construction Work Package narrative; Installation and Tie-in Workface Plan; Construction Interface and Turnover Checklist | DELIVERABLE_REGISTER.csv row DEL-099-03 |
| Civil basis | Truck-loading slabs, foundations, drainage, spill containment, and access roads designed for site geotech, snow/wind/seismic, and -40 deg C operation | DBM SEC-11 |
| Spill containment basis | Truck-loading areas require spill-control provisions for condensate; process-contaminated drainage routed to appropriate drain/containment, not surface-water discharge | DBM SEC-11 Roads and Access; Surface Water and Drainage |
| Tie-in interfaces | Condensate header from condensate booster pumps / product condensate storage; loading-pump suction/discharge; metering; vapour return (TBD); drain/containment; power; grounding/bonding; control/safety cabling; area lighting; F&G | PACKAGE_REGISTER.csv row PKG-099 interface types; DBM Condensate Storage and Product Handling |
| Inspection / turnover scope | Hydrostatic / leak test of loading piping; metering calibration witness; pump performance test; vapour-handling tie-in verification; spill containment walkdown; CP/grounding test; F&G commissioning; cold-weather electrical and heat-tracing commissioning | ASSUMPTION (industry-standard truck loading commissioning set); clause-level location TBD in 26020-Package_Requirements.docx heading 51 and RFQ 26020-03-PT-RFQ-23-001 (binary; not text-accessible this run) |

## References

- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Site Basis; Condensate and Produced-Water Receipts; SEC-06 Liquids Hub — Condensate Storage and Product Handling; SEC-08 Prime Movers; SEC-10 Miscellaneous Facilities; SEC-11 Plant Layout/Civil; SEC-12 Electrical)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` (row PKG-099)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` (row DEL-099-03)
- 26020-Package_Requirements.docx package heading 51 (binary; clause-level slice not text-accessible this run — location TBD)
- 26020-03-PT-RFQ-23-001_Truck_Load_stn_R0.docx (binary RFQ; not text-accessible this run — location TBD)
