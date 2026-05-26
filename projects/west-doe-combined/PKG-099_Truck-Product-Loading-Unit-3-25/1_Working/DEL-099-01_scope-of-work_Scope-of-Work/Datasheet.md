# Datasheet — DEL-099-01 Scope of Work (PKG-099 Truck Product Loading Unit 3-25)

> Descriptive view of identity, attributes, conditions, and construction basis for the EPC Scope of Work deliverable.
> Substantive values are source-grounded. `TBD` marks information not present in locally accessible sources; `ASSUMPTION` marks inferences.

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-099-01_scope-of-work` | `_CONTEXT.md` (Identity) |
| Deliverable Name | Scope of Work | `_CONTEXT.md` |
| Parent Package ID | `PKG-099` | `_CONTEXT.md` |
| Parent Workbook ID | 99 (Workbook Packages row 98) | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` PKG-099 row |
| Package Name | Truck Product Loading Unit 3-25 | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` PKG-099 row |
| Discipline | Mechanical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` PKG-099 row (Discipline = Mechanical) |
| WBS | 03 | `PACKAGE_REGISTER.csv` PKG-099 row (WBS = 03) |
| Tag (CoA) | `26020-03-23-001` (CoA Tracking and Tag Number) | `PACKAGE_REGISTER.csv` PKG-099 row |
| Deliverable Type | EPC Scope of Work | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` DEL-099-01 row |
| Responsible Party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` DEL-099-01 row |
| Source Basis | Workbook Packages row 98; 26020-Package_Requirements.docx package heading 51; RFQ `26020-03-PT-RFQ-23-001_Truck_Load_stn_R0.docx`; `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` | `PACKAGE_REGISTER.csv` PKG-099 row (Source Reference) |

## Attributes (package function and identity)

| Attribute | Value | Source |
|---|---|---|
| Package function (workbook) | Sweet Dehydrated Condensate from the Condensate Storage Tanks is pumped by the Truck Loading pumps to the Truck Loading stations, metered, and fills the atmospheric condensate truck. | `PACKAGE_REGISTER.csv` PKG-099 row (Package Scope) |
| Package function (DBM) | Liquids hub supports product truck loading; condensate booster/transfer feeds truck-loading stations; pipeline export of sales condensate is via NRM LACT (separate scope). | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-01, SEC-06 |
| Major equipment (workbook RFQ row) | Truck Loading/Unloading Stations; basket strainer (Sureflow 0300BF300SS; 316SS; c/w Mesh Screen); Emergency Shut Down Valve (ESDV); Flow transmitters | `ARTIFACT_REGISTER.csv` ART-517D0E9F90 (Major included equipment evidence) |
| Station quantity (Workbook/RFQ basis) | Two truck loading and unloading stations, each capable of loading two trucks simultaneously (2x2) | `PACKAGE_REGISTER.csv` PKG-099 row (Package Scope) |
| Station quantity (DBM basis) | Three product truck-loading stations; one condensate loading pump per station | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-01 (line 40), SEC-06 (line 414, 526, 578, 654) |
| Per-station loading capacity | 103 m3/h per station, 345 kPad differential | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-06 (line 415) |
| Service fluid | Sweet Dehydrated Condensate (atmospheric truck) | `PACKAGE_REGISTER.csv` PKG-099 row (Package Scope) |
| Upstream source | Condensate Storage Tanks (Liquids Hub); via Truck Loading pumps | `PACKAGE_REGISTER.csv` PKG-099 row; `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-06 |
| LACT relationship | LACT equipment is third-party NRM scope; 03-25 provides facility-side tie-in up to and including the tie-in flange. Truck loading is a parallel product disposition. | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-01 (line 22), SEC-05 (line 207) |

> **HRR (Human Resolution Required):** Station quantity differs between sources (Workbook/RFQ: 2x2; DBM: 3 stations). See `Guidance.md` Conflict Table CT-01.

## Conditions

| Condition | Value | Source |
|---|---|---|
| Site | LSD 03-25-80-15 W6M, north of Dawson Creek, BC; elevation 673 m AMSL | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-02 (line 85) |
| Ambient design basis (cold) | -40 deg C winter operation reference | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-12 (line 696) |
| Service condensate basis | 20,000 bbl/d (3,180 m3/d) stabilized condensate hub throughput; truck loading is a parallel product disposition route from product condensate storage. | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-06 (line 376) |
| Hazard classification | TBD (not stated in accessible sources for the truck loading area at deliverable-grain) |
| Detection (LEL/H2S/mercaptan/fire) coverage of truck loading area | Required as part of facility F&G coverage; detector count, set points, voting logic TBD | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-15 (line 838) |
| Permitting status | Liquids hub permitted under BCER application 100120203; truck-rack scope requires further permit amendment. | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-17 (line 872) |

## Construction

| Attribute | Value | Source |
|---|---|---|
| Civil basis | Truck-loading slab and supporting civil works are included in 03-25 civil basis (grading, drainage, roads, foundations) | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-12 (line 688) |
| Road / access basis | Roads shall accommodate truck-loading traffic; truck-loading areas shall provide access, turning, queuing, and spill-control provisions; designed for winter operation and -40 deg C basis. | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-12 (line 696) |
| Spill containment | Provisions for condensate, produced water, caustic, H2O2, and maintenance traffic spill control at truck-loading areas | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-12 (line 696) |
| Foundations / structural | Truck-loading structures require equipment-specific foundation/anchorage checks per final geotechnical report | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-12 (line 700) |
| Electrical | Electrical design supports truck loading among other 03-25 systems | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-13 (line 718) |
| Construction scope inclusion | Construction management, grading, piling, foundations, roads, module offloading/setting, mechanical hookups, shipped-loose instruments/valves installation, supports, ISBL/OSBL interconnecting piping, home-run cabling, terminations, area lighting, fencing, controls, demolition where required. | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-01 (line 75) |

## Applicable Interfaces (workbook X-column)

| Interface Type | Interface ID | Source |
|---|---|---|
| Process Piping | `IFC-6729163B3D` | `INTERFACE_REGISTER.csv` |
| Drain / Containment | `IFC-465E3D1DAE` | `INTERFACE_REGISTER.csv` |
| Electrical Power | `IFC-9F3372E24B` | `INTERFACE_REGISTER.csv` |
| Grounding / Bonding | `IFC-825D998849` | `INTERFACE_REGISTER.csv` |
| Area / Exterior Lighting | `IFC-F7A4A71AE3` | `INTERFACE_REGISTER.csv` |
| I&C / Control Cabling | `IFC-DC5E4EA6DB` | `INTERFACE_REGISTER.csv` |
| Building HVAC / Services | `IFC-44F649E356` | `INTERFACE_REGISTER.csv` |
| Fire & Gas / Safety Systems | `IFC-4B83FB2372` | `INTERFACE_REGISTER.csv` |
| Grading / Site Drainage / Spill Containment | `IFC-6915CFDC8E` | `INTERFACE_REGISTER.csv` |
| Structural / Foundations / Supports | `IFC-09F9836F29` | `INTERFACE_REGISTER.csv` |
| Product Loading | `IFC-C1DDD52FA4` | `INTERFACE_REGISTER.csv` |

## References

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (this deliverable folder)
- Accepted decomposition snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `DELIVERABLE_REGISTER.csv` (DEL-099-01 row)
  - `PACKAGE_REGISTER.csv` (PKG-099 row)
  - `ARTIFACT_REGISTER.csv` (PKG-099 rows)
  - `INTERFACE_REGISTER.csv` (PKG-099 rows)
- Locally accessible source material:
  - `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`
- Locally inaccessible source material (cited at `location TBD` and not used for clause-level values):
  - `_Sources/26020-Package_Requirements.docx` (heading 51) — docx; no md extraction available
  - `_Sources/26020-Packages_Interfaces_4_export.xlsx` (row 98) — xlsx; not parsed locally
  - RFQ `26020-03-PT-RFQ-23-001_Truck_Load_stn_R0.docx` — not located in `_Sources/`
