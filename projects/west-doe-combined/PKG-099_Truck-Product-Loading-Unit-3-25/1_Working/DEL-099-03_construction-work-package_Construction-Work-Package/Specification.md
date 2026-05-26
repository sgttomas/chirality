# Specification — DEL-099-03 Construction Work Package (PKG-099)

> Normative requirements for the EPC Construction Work Package deliverable that governs how PKG-099 (truck product loading stations for sweet stabilized condensate at the 03-25 Liquids Hub) will be physically installed, inspected, turned over, and integrated into the 03-25 facility.

## Scope

In scope:
- Construction Work Package narrative covering site receipt, mechanical erection, hydrostatic/leak testing of loading piping, metering proving witness, inspection, mechanical completion, and turnover for the truck loading stations and their package-side equipment (PACKAGE_REGISTER.csv row PKG-099).
- Installation and tie-in workface plan covering the eleven declared package interface types for PKG-099: Process Piping; Drain/Containment; Electrical Power; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas/Safety Systems; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports; Product Loading (PACKAGE_REGISTER.csv row PKG-099).
- Construction interface and turnover checklist evidencing mechanical completion and EPC acceptance of vendor-supplied truck loading equipment.

Out of scope:
- Package engineering, package design, and vendor documentation for the physical equipment package — these are Package Vendor scope (PACKAGE_REGISTER.csv row PKG-099).
- Operating procedures for the truck loading stations once handed over to operations.
- Detailed design of the condensate storage tanks, condensate booster pumps, condensate loading pumps (separate equipment under liquids hub scope; see DBM SEC-06).
- LACT/custody-transfer scope (third-party NRM scope per DBM SEC-09).

## Requirements

| Req ID | Requirement | Basis / Source |
|---|---|---|
| R-099-03-01 | The Construction Work Package shall identify each truck loading station by tag and final station count per the resolved equipment list. The current source set carries a discrepancy: PACKAGE_REGISTER lists two stations (2x2 loading); DBM SEC-06/SEC-10 lists three stations. Final count shall be confirmed against the issued vendor equipment list and resolved per the Conflict Table in `Guidance.md`. | PACKAGE_REGISTER.csv row PKG-099; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Condensate Storage and Product Handling, Miscellaneous Facilities |
| R-099-03-02 | Loading piping, metering skids, pumps, and associated equipment shall be installed per the package vendor's installation instructions and 26020-Package_Requirements.docx package heading 51. (Clause-level acceptance criteria TBD — `location TBD`.) | PACKAGE_REGISTER.csv row PKG-099 (Word Source Basis); ASSUMPTION on clause set |
| R-099-03-03 | Foundations, truck-loading slabs, and structural supports shall be designed for the final geotechnical report, equipment loads, snow/wind/seismic criteria, frost protection, and -40 deg C minimum ambient. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Site Basis; SEC-11 Foundations and Structural Supports |
| R-099-03-04 | Truck-loading area civil works shall provide access, turning, queuing, and spill-control provisions for condensate traffic; access roads shall be sized for module delivery, operations, maintenance, and emergency response in winter operation. | DBM SEC-11 Roads and Access |
| R-099-03-05 | Loading piping and any closed-system pressure boundary shall be hydrostatically / leak-tested prior to commissioning per the package requirements and applicable piping code. (Test pressure, hold time, and acceptance criteria `location TBD` in vendor package and project piping spec.) | ASSUMPTION (standard piping commissioning); clause `location TBD` |
| R-099-03-06 | Construction shall provide tie-ins for all eleven declared interface types listed in PKG-099 (process piping; drain/containment; electrical power; grounding/bonding; area lighting; I&C cabling; building HVAC/services; F&G/safety systems; grading/drainage/spill containment; structural/foundations/supports; product loading). | PACKAGE_REGISTER.csv row PKG-099 |
| R-099-03-07 | A Construction Interface and Turnover Checklist shall be produced; each item closed with documented evidence prior to mechanical-completion turnover. | DELIVERABLE_REGISTER.csv row DEL-099-03 (artifact list); _CONTEXT.md Anticipated Artifacts |
| R-099-03-08 | Spill containment, drainage routing, and process-contaminated drainage segregation shall be installed and turned over consistent with the package's declared drain/containment and grading/spill-containment interfaces. Surface-water and process drainage shall not be commingled. | PACKAGE_REGISTER.csv row PKG-099; DBM SEC-11 Surface Water and Drainage |
| R-099-03-09 | Cathodic protection (where applicable) and grounding/bonding interfaces shall be installed, tested, and recorded prior to mechanical completion. Static grounding/bonding at each loading position shall be verified before first product load. | PACKAGE_REGISTER.csv row PKG-099 (grounding/bonding interface); ASSUMPTION on static-bonding test (standard truck loading practice) |
| R-099-03-10 | Fire & gas / safety system devices serving the truck loading area (LEL, H2S, methyl mercaptan, fire detection) shall be installed, commissioned, and integrated to the BPCS/ESD per the project F&G design (detection point list, set points, voting logic TBD). | DBM SEC-13 Fire & Gas references; ASSUMPTION on inclusion |
| R-099-03-11 | Custody-transfer / fiscal metering at each loading station shall be installed, proved (witnessed calibration), and documented per the applicable metering standard and project measurement specification (standard and clause `location TBD`). | PACKAGE_REGISTER.csv row PKG-099 (Product Loading interface); ASSUMPTION (standard custody metering); DBM SEC-09 metering context |
| R-099-03-12 | The Construction Work Package shall identify and resolve EPC/Vendor split-of-supply items at every tie-in (terminal connection point) and record them in the Construction Interface Register entries for PKG-099. | PACKAGE_REGISTER.csv row PKG-099 (boundary statement) |
| R-099-03-13 | All exposed package equipment, instrumentation, panels, field devices, electrical heat tracing, and ancillary heaters in scope of this construction work package shall be specified, installed, and protected for the -40 deg C minimum ambient unless a more severe process or vendor condition applies. | DBM Site Basis; SEC-12 Electrical (heat tracing) |
| R-099-03-14 | Electrical power tie-ins shall be coordinated with the shared cross-facility electrical system supplied from 04-25, and commissioned through the appropriate MCC/distribution path. | DBM SEC-12 Electrical Design Basis |

Requirements R-099-03-02, R-099-03-05, R-099-03-09 (static-bonding portion), R-099-03-10 (point list), and R-099-03-11 are flagged ASSUMPTION pending text-accessible review of 26020-Package_Requirements.docx package heading 51 and/or the 26020-03-PT-RFQ-23-001 RFQ.

## Standards

| Standard | Applies To | Location |
|---|---|---|
| 26020-Package_Requirements.docx package heading 51 | Package-specific scope/requirements for PKG-099 | binary source; location TBD |
| 26020-03-PT-RFQ-23-001_Truck_Load_stn_R0.docx | Vendor RFQ basis for truck loading stations | binary source; location TBD |
| Project piping specification | Loading piping fabrication, testing | location TBD (project piping spec not in `_Sources` this run) |
| Project measurement / custody-transfer specification | Loading metering installation, calibration, and proving | location TBD |
| API RP 2003 (Protection Against Ignitions Arising Out of Static, Lightning, and Stray Currents) | Static bonding/grounding at truck loading positions | location TBD (referenced as industry-standard practice; ASSUMPTION on applicability) |
| Site basis (cold climate, -40 deg C) | Winterization, heat tracing, materials, civil/structural | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Site Basis; SEC-11; SEC-12 |
| NBCC 2020 (Dawson Creek IDF) | Civil drainage and surface-water management for truck-loading slab area | DBM SEC-11 |

## Verification

| Req | Verification approach |
|---|---|
| R-099-03-01 | Document review against PKG-099 register and final vendor equipment list; tag check on shop drawings and nameplates; conflict resolution recorded. |
| R-099-03-02 | Vendor installation-instruction compliance records; package-requirements checklist when heading-51 slice is text-accessible. |
| R-099-03-03 | Geotech and foundation design review records; cold-weather concrete plan; truck-loading slab structural review. |
| R-099-03-04 | Civil walkdown of access, turning, queuing, and spill control; road design review against winter access basis. |
| R-099-03-05 | Hydrostatic / leak test reports with pressure, hold time, and acceptance criteria. |
| R-099-03-06 | Tie-in punch list complete and signed in Construction Interface and Turnover Checklist (one item per declared interface type per station). |
| R-099-03-07 | Signed checklist on file prior to mechanical completion. |
| R-099-03-08 | Walkdown record of containment and drainage routing; segregation check of process vs surface-water drainage. |
| R-099-03-09 | CP commissioning record (if applicable); ground-resistance test results; static-bonding verification at each loading position. |
| R-099-03-10 | F&G device installation and commissioning records; loop checks and integration with BPCS/ESD. |
| R-099-03-11 | Witnessed metering proving record; calibration certificates; documentation per project measurement spec. |
| R-099-03-12 | Construction Interface Register entries closed with EPC/Vendor sign-off. |
| R-099-03-13 | Cold-weather equipment specification review; heat-tracing commissioning records; cold-temperature class certification check. |
| R-099-03-14 | Electrical tie-in commissioning records; MCC point-to-point check; coordination evidence with 04-25 cross-facility electrical system. |

## Documentation

The deliverable shall produce the following documented artifacts (per DELIVERABLE_REGISTER.csv row DEL-099-03 and `_CONTEXT.md`):

- Construction Work Package narrative
- Installation and Tie-in Workface Plan
- Construction Interface and Turnover Checklist

Supporting records expected during execution:

- Hydrostatic / leak test reports for loading piping
- Metering proving / calibration records (per station)
- Pump performance and motor commissioning records
- F&G device installation and integration records
- CP (if applicable) and grounding/bonding test records
- Static-bonding verification records (per loading position)
- Foundation pour and cold-weather concrete records
- Heat-tracing commissioning records
- Tie-in punch list and as-built mark-ups
- EPC/Vendor sign-off records per interface register entry
