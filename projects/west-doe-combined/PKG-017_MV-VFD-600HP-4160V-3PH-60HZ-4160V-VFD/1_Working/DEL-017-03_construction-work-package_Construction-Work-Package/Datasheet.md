# Datasheet: DEL-017-03_construction-work-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-017-03_construction-work-package` | `_CONTEXT.md` |
| Deliverable name | Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-017` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | MV VFD - 600HP, 4160V, 3PH, 60HZ - 4160V VFD | Workbook Packages row 19; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 17 / row 19 | Workbook Packages row 19; `PACKAGE_REGISTER.csv` |
| WBS | 02 | Workbook Packages row 19; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-02-30-008 | Workbook Packages row 19; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 19; `_CONTEXT.md` |
| Deliverable type | EPC Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-017` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-017` |
| Package function | Medium-voltage Variable Frequency Drive at 4160 V, 3-phase, 60 Hz, nameplate motor service 600 HP per package title. | Workbook Packages row 19; `PACKAGE_REGISTER.csv` |
| MV electrical supply context | The 03-25 facility 4160 V supply originates from a 13.8 kV to 4.16 kV, 12 MVA transformer feeding the 4160V MCC; the 4160V MCC provides field-fused contactors, motor protection relays, and an EtherNet communication port to the plant PLC central control panel. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical supply table and 4160V MCC section |
| MV VFD design basis statement | Source explicitly identifies starting VFDs at the 4160 V level only for inlet compressors KM-2150 and KM-2250 under SCA-001 VE #34, with capacitor banks removed from the synchronous bus where VFDs are present (SCA-001 VE #37); harmonic and reactive-power mitigation are detailed-design items. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, lines 326, 756 |
| 600 HP motor service basis | TBD. Accessible DBM source does not describe a 4160 V, 600 HP motor or VFD load in the 03-25 electrical basis; only large 4000 V inlet compressor motors (5,200 hp / 3,878 kW) are explicitly covered. The "600HP" element of the package title is not corroborated by an accessible source slice. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, line 324; source gap |
| Construction scope context | Project construction scope includes construction management, grading, piling, foundations, roads, field buildings, offloading and setting of modules, mechanical hookups, installation of shipped-loose instruments and valves, pipe supports, ISBL/OSBL interconnecting piping, home-run cabling, terminations, area lighting, fencing, security systems, control room and maintenance systems. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Construction Scope Summary (line 73) |
| Electrical building housing basis | Electrical buildings shall house MCCs, switchgear, distribution equipment, and associated HVAC/ventilation; MV cable routing shall comply with project electrical specifications and detailed design. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Electrical Buildings paragraph (lines 766-768) |
| Driven-equipment tie-in target | TBD. The package title and registers do not identify which specific 4160 V motor or compressor the VFD serves; allocation to a specific driven machine is not confirmed by an accessible source. | Source gap |

## Conditions

| Interface / condition | Construction-work-package basis | Source |
|---|---|---|
| Electrical Power (`IFC-5E50E5F700`) | The CWP shall describe MV power tie-in from the 4160V MCC (or upstream feeder defined by detailed design) to the VFD enclosure, including phasing/rotation verification before energization. | Workbook Packages row 19; `INTERFACE_REGISTER.csv` |
| Grounding / Bonding (`IFC-1340C6D795`) | The CWP shall describe grounding/bonding of the VFD enclosure to the facility ground grid in accordance with CEC and project electrical specifications. | Workbook Packages row 19; `INTERFACE_REGISTER.csv`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |
| I&C / Control Cabling (`IFC-6ECD9C92A1`) | The CWP shall describe routing, segregation, termination, and continuity checks for VFD control, signaling, and feedback wiring. Power and control circuits shall be separated by distance, shielding, or routing per project electrical specifications. | Workbook Packages row 19; `INTERFACE_REGISTER.csv`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, line 768 |
| Communications / Network (`IFC-FB4034716A`) | The CWP shall describe network-port cabling and termination from the VFD package to the plant PLC central control panel via the EtherNet path defined for the 4160V MCC. | Workbook Packages row 19; `INTERFACE_REGISTER.csv`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160V MCC paragraph |
| Maintenance Access (`IFC-A807F5E0B3`) | The CWP shall preserve clearances around the VFD package for inspection, MOV/contactor replacement, cooling-system service, and door swing. Cable tray and conduit routing shall not interfere with maintenance access. | Workbook Packages row 19; `INTERFACE_REGISTER.csv`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |
| Structural / Foundations / Supports (`IFC-34EB597147`) | The CWP shall describe foundation, anchorage, and structural support installation for the VFD enclosure, with anchor pattern, levelling, grouting, and seismic/wind/snow loading per project criteria. | Workbook Packages row 19; `INTERFACE_REGISTER.csv`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, line 700 |
| Area classification | TBD; VFD installation location and resulting hazardous/non-hazardous classification not identified in accessible source for PKG-017. | Source gap |
| Environmental design basis | -40 deg C design temperature applies to outdoor construction and road/access provisions referenced in DBM. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, line 696 |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility (engineering, design, vendor documentation, equipment package). | `PACKAGE_REGISTER.csv` row `PKG-017` |
| Facility integration, interfaces, tie-ins | EPC Integrator responsibility (constructability, procurement/construction coordination, facility-level integration). | `PACKAGE_REGISTER.csv` row `PKG-017` |
| Installation location | TBD. Source confirms MV equipment generally resides in electrical buildings, but PKG-017 is not assigned to a specific building, room, skid, or outdoor pad in accessible source. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Electrical Buildings paragraph |
| Module delivery / offloading | Project construction scope covers offloading and setting of modules; VFD-specific rigging plan, lift weights, and crane access TBD pending vendor data. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, line 73 |
| Foundations / anchorage | Structural / foundations / supports interface applies; package-specific foundation drawings, anchor type, and grout schedule TBD pending vendor and civil detailed design. | Workbook Packages row 19; `INTERFACE_REGISTER.csv`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, line 700 |
| Cable / conduit / tray installation | Power circuits at 4,160 V shall be separated from control and instrument circuits; cable tray, conduit, grounding, and bonding shall comply with project electrical specifications and detailed design. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, line 768 |
| Cooling / HVAC interface | TBD; VFD cooling provisions (forced air, liquid, or building HVAC) not identified in accessible source for PKG-017. | Source gap |
| Pre-energization checks | Project electrical detailed design defines MV commissioning tests (insulation, hi-pot, phase rotation, relay coordination); CWP shall include hold points for these tests prior to energization. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical sections; `ASSUMPTION` for hold-point convention |
| Turnover evidence | The CWP shall produce a construction interface and turnover checklist (ART-3A7676CD16) as an EPC deliverable. | `ARTIFACT_REGISTER.csv` row `ART-3A7676CD16` |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-017-03_construction-work-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-017`.
- `ARTIFACT_REGISTER.csv`, rows `ART-1C1724D3C4`, `ART-65539C633A`, `ART-3A7676CD16`.
- `INTERFACE_REGISTER.csv`, rows `IFC-5E50E5F700`, `IFC-1340C6D795`, `IFC-6ECD9C92A1`, `IFC-FB4034716A`, `IFC-A807F5E0B3`, `IFC-34EB597147`.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-017-03_construction-work-package` (OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 19.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Construction Scope Summary, Electrical Supply, 4160V MCC, Electrical Buildings/Raceways, foundations, and roads/access paragraphs.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific MV VFD content; no PKG-017 match found in accessible slices.
