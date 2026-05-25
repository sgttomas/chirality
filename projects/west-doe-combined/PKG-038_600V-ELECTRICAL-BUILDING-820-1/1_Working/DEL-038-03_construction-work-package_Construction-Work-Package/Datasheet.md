# Datasheet: DEL-038-03_construction-work-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-038-03_construction-work-package` | `_CONTEXT.md` |
| Deliverable name | Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-038` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 600V ELECTRICAL BUILDING (820-1) | Workbook Packages row 40; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 38 / row 40 | Workbook Packages row 40; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 40; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-029 | Workbook Packages row 40; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 40; `_CONTEXT.md` |
| Deliverable type | EPC Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-038` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Construction scope role | EPC Integrator construction-facing deliverable for physically installing, building, inspecting, turning over, and tying the `PKG-038` 600V Electrical Building (820-1) into the larger facility systems. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-038-03_construction-work-package` |
| Artifact set | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist. | `ARTIFACT_REGISTER.csv` rows `ART-9F12F8D18F`, `ART-A7B67360EB`, `ART-C554CB9646` |
| Package class | Vendor-owned Electrical package installed by EPC construction scope. | `PACKAGE_REGISTER.csv` row `PKG-038` |
| Package function | Prefabricated, modular Electrical Building housing 600 V MCCs, distribution, UPS, contactor panels, PLC control panels, and network racks as required by detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section |
| Building basis (workbook identity) | Package name "600V ELECTRICAL BUILDING (820-1)" per workbook row 40. | Workbook Packages row 40 |
| Building basis (DBM cross-reference) | DBM electrical-buildings list (row "820-1") identifies tag 820-1 as the "6.9 kV Inlet / Sales Compressor Electrical Building"; the workbook identifies the same tag at a 600 V designation. See Guidance Conflict Table HRR-038-03-001. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-buildings table; Workbook Packages row 40 |
| Construction type | Prefabricated, modular building, climate controlled, elevated on piles with bottom cable entry. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section |
| Installation location | Plot location TBD. DBM requires electrical buildings to be located in general-purpose (non-hazardous) areas; the specific plot coordinates for tag 820-1 are not stated in accessible source material. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Area Classification and Electrical Buildings sections |
| Modularization basis | Shop-fabricated, modular building per DBM. Shipping splits, lift weights, and specific transport configuration for `PKG-038` are TBD pending vendor data. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section; source gap for package-specific values |

## Conditions

| Interface / condition | Construction-facing basis | Source |
|---|---|---|
| Utility Piping | Applicable interface for `PKG-038`; installation must respect facility utility piping tie-ins to/around the building. Package-specific piping content is TBD. | Workbook Packages row 40; `INTERFACE_REGISTER.csv` `IFC-592E5CCFE2` |
| Drain / Containment | Applicable interface; building drainage and containment connections to facility drain/containment systems shall be field-routed during construction. | Workbook Packages row 40; `INTERFACE_REGISTER.csv` `IFC-EA9C0A8BD1` |
| Electrical Power | Applicable interface; building incoming feeders and outgoing distribution shall use bottom entry to/from the elevated electrical building. | Workbook Packages row 40; `INTERFACE_REGISTER.csv` `IFC-C7243E4F80`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section |
| Grounding / Bonding | Applicable interface; major electrical equipment shall be directly connected to the ground grid at two points; ground wells at the electrical building shall be provided for maintenance and operational testing; the 600 V transformer feeding the building shall be high-resistance grounded (5 A continuous). | Workbook Packages row 40; `INTERFACE_REGISTER.csv` `IFC-065DD9678E`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Grounding and Bonding section |
| Area / Exterior Lighting | Applicable interface; exterior lighting at the building shall be coordinated with the facility lighting design. | Workbook Packages row 40; `INTERFACE_REGISTER.csv` `IFC-8D5F57505E` |
| I&C / Control Cabling | Applicable interface; control signal cabling between the electrical building and field/process skids shall use tray/conduit routing per DBM and shall preserve segregation from power cables. | Workbook Packages row 40; `INTERFACE_REGISTER.csv` `IFC-33A55B6DBB`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Cable, Wire, and Raceways section |
| Communications / Network | Applicable interface; field-run communications cabling (Ethernet, ControlNet, DeviceNet, fiber, twisted pair) into the building shall be armored and rated for tray installation. | Workbook Packages row 40; `INTERFACE_REGISTER.csv` `IFC-6F5BF129A3`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Cable, Wire, and Raceways section |
| Building HVAC / Services | Applicable interface; the electrical building HVAC shall be n + 1 redundant; building heaters are electric by default. Facility services to the building shall be field-connected during construction. | Workbook Packages row 40; `INTERFACE_REGISTER.csv` `IFC-F3F5DA500E`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings and building-heater sections |
| Fire & Gas / Safety Systems | Applicable interface; building fire & gas detection, alarming, and life-safety tie-ins shall be field-installed and integrated with facility systems. Package-specific F&G content is TBD. | Workbook Packages row 40; `INTERFACE_REGISTER.csv` `IFC-C4BE8B720F` |
| Maintenance Access | Applicable interface; equipment doors shall be sized for, or include removable transom sections to allow, removal of the largest equipment; equipment placement and cable tray routing shall preserve maintenance access. | Workbook Packages row 40; `INTERFACE_REGISTER.csv` `IFC-B981842FD5`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section |
| Grading / Site Drainage / Spill Containment | Applicable interface; site grading and drainage around the elevated building shall be coordinated with the facility civil/site basis. | Workbook Packages row 40; `INTERFACE_REGISTER.csv` `IFC-7D68588C25` |
| Structural / Foundations / Supports | Applicable interface; the building shall be elevated and installed on piles. Foundation, pile, settlement, frost protection, and structural-support requirements shall be confirmed against the final geotechnical report. | Workbook Packages row 40; `INTERFACE_REGISTER.csv` `IFC-846DEC98C2`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section |
| Area classification / hazardous-area constraints | Electrical buildings shall be located in general-purpose (non-hazardous) areas; installation methods shall respect the area classification assigned at detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Area Classification section |
| Climate / environmental basis | Cables installed in tray shall be rated for -40 deg C; building HVAC shall be sized n + 1 for climate redundancy. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Cable, Wire, and Raceways and Electrical Buildings sections |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package fabrication and supply | Package Vendor responsibility (vendor-owned Electrical package). The building is shop-fabricated, modular, with shop-installed lighting and electrical wiring terminated at a skid-edge junction box. | `PACKAGE_REGISTER.csv` row `PKG-038`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Cable, Wire, and Raceways (shop wiring paragraph) |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-038` |
| Construction work package artifact | Integrator-authored construction work package for physical installation, construction, and tie-in to larger systems. | `ARTIFACT_REGISTER.csv` row `ART-9F12F8D18F` |
| Installation and tie-in workface plan | Workface-planning evidence for installing/building the package and connecting it to adjacent utility, electrical, controls, civil, structural, and safety systems as applicable. | `ARTIFACT_REGISTER.csv` row `ART-A7B67360EB` |
| Construction interface and turnover checklist | Construction-facing interface, tie-in, inspection, and turnover evidence for the approved package. | `ARTIFACT_REGISTER.csv` row `ART-C554CB9646` |
| Civil / foundations / supports | Building shall be elevated and installed on piles. Site grading, foundations, electrical buildings, pipe racks, and field interconnections fall inside construction scope; package-specific foundation, pile, and settlement detail is TBD pending detailed design and geotechnical confirmation. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings; geotechnical considerations are addressed in DBM but specific values for `PKG-038` are TBD |
| Building setting and rigging | Offloading and setting of the modular building module(s) is in EPC construction scope. Package-specific lift plan, crane size, rigging design, and shipping splits are TBD pending vendor data. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings (modular building basis); source gap for package-specific values |
| Electrical installation work | Home-run cabling, terminations, and field interconnections are inside construction scope. Incoming and outgoing 600 V cables shall use bottom entry. Tray cables shall be TECK 90, ACWU, or ACIC, HL rated, -40 deg C rated, aluminum interlocking armor; conductors copper up to #1/0 AWG and ACWU aluminum above #1/0 AWG. EMT conduit shall be used between adjacent equipment (e.g., control panels to contactor panels). Package-specific cable lists, feeder sizing, and conduit/tray routing are TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings and Cable, Wire, and Raceways sections |
| Grounding installation | Major equipment in the building shall be connected to the ground grid at two points; ground wells shall be provided at the electrical building with bolted ground connections; above-grade ground conductors shall be green insulated, run in PVC conduit where mechanical protection is required, with compression-type connections; distribution transformers, panelboards, and three-phase motors larger than 100 hp shall have a separate copper ground conductor sized per CEC. Package-specific conductor sizes are TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Grounding and Bonding section |
| Building HVAC installation | HVAC shall be installed as an n + 1 system so a single HVAC unit failure or maintenance shutdown does not affect building heating and cooling. Specific equipment make/model and duct routing are TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section |
| Inspection and test | Inspection scope shall confirm installation against the construction work package, the package interface requirements matrix, and vendor turnover documentation. Specific QA/QC checklists, ITPs, and hold points are TBD pending vendor and EPC inspection plans. | Source gap; `_REFERENCES.md` |
| Turnover and acceptance | Construction interface and turnover checklist supports the downstream EPC Vendor Package Review and Acceptance (`DEL-038-06`). Turnover content depends on vendor document turnover (`DEL-038-05`) and package datasheet (`DEL-038-02`). | `DELIVERABLE_REGISTER.csv` rows for `DEL-038-05`, `DEL-038-06`; `ARTIFACT_REGISTER.csv` row `ART-C554CB9646` |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-038-03_construction-work-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-038`.
- `ARTIFACT_REGISTER.csv`, rows `ART-9F12F8D18F`, `ART-A7B67360EB`, `ART-C554CB9646` for `DEL-038-03_construction-work-package`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-038` (`IFC-592E5CCFE2`, `IFC-EA9C0A8BD1`, `IFC-C7243E4F80`, `IFC-065DD9678E`, `IFC-8D5F57505E`, `IFC-33A55B6DBB`, `IFC-6F5BF129A3`, `IFC-F3F5DA500E`, `IFC-C4BE8B720F`, `IFC-B981842FD5`, `IFC-7D68588C25`, `IFC-846DEC98C2`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-038-03_construction-work-package` (OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 40.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-buildings list (tag 820-1), Electrical Buildings section, Area Classification, Grounding and Bonding, Cable Wire and Raceways, and shop wiring source slices.
- `_Sources/26020-Package_Requirements.docx`, not opened in this run (binary docx). Package-specific construction content for `PKG-038` is not confirmed from this source in this run.
