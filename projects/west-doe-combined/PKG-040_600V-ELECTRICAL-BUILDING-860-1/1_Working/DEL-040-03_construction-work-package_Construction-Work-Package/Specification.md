# Specification: DEL-040-03_construction-work-package — Construction Work Package

## Scope

This specification defines the minimum content requirements for the PKG-040 Construction Work Package covering the 600V Electrical Building (860-1) — the 600V General Area / Tank Farm Electrical Building. The package covers how the shop-built electrical building module will be physically delivered, installed, hooked up, inspected, turned over, and tied into larger facility systems.

The work package shall include:

- construction work package content for PKG-040;
- installation and tie-in workface plan content for receipt, setting on foundations, mechanical/electrical hookup, and home-run cabling;
- construction interface and turnover checklist content covering all twelve declared PKG-040 interface categories;
- coordination boundary between Package Vendor (engineering/design/equipment) and EPC Integrator (facility integration, interfaces, tie-ins, constructability).

Exclusions are TBD. Gate 7 PACKAGE_REGISTER.csv records package-specific exclusions for PKG-040 as `TBD; no package-specific exclusions stated in source materials`. Cathodic protection engineering and supply are facility-design exclusions per DBM SEC-12.

## Requirements

| Req ID | Requirement | Verification |
|---|---|---|
| CWP-040-001 | The Construction Work Package shall identify the package as PKG-040, 600V Electrical Building (860-1), WBS 01, CoA tracking number 26020-01-30-031, Electrical discipline, scope item SOW-0041. | Check against workbook Packages row 42, PACKAGE_REGISTER.csv, and DELIVERABLE_REGISTER.csv. |
| CWP-040-002 | The Construction Work Package shall include a construction-facing plan for physical installation, construction, inspection, turnover, and tie-in to larger facility systems. | Confirm document sections or attached workface plan cover each named function. |
| CWP-040-003 | The Construction Work Package shall address all twelve PKG-040 interface categories: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. | Cross-check interface matrix/checklist against workbook Packages row 42 and INTERFACE_REGISTER.csv rows for PKG-040. |
| CWP-040-004 | The Construction Work Package shall distinguish Package Vendor scope (package engineering, package design, vendor documentation, physical equipment package) from EPC Integrator scope (facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration). | Confirm responsibility statement or RACI references PACKAGE_REGISTER.csv vendor-scope description. |
| CWP-040-005 | The Construction Work Package shall plan the 860-1 building as a prefabricated, modular, shop-built electrical building located in a general purpose area, elevated on piles with bottom entry of incoming/outgoing power cables. | Check installation plan and foundation drawings against DBM SEC-12 Electrical Buildings. |
| CWP-040-006 | The Construction Work Package shall provide for HVAC sized as an n+1 system so the cooling system can tolerate failure or maintenance shutdown of one HVAC unit. | Confirm HVAC commissioning/turnover step references DBM SEC-12 n+1 basis. |
| CWP-040-007 | The Construction Work Package shall plan grounding installation per SEC-12: driven piles as ground electrodes interconnected by a main #2/0 green insulated grounding conductor, with major electrical equipment connected at two points, ground wells at the electrical building, and a 5 A continuous high-resistance grounding resistor on the 600 V system. | Check grounding installation drawings, test records, and turnover sign-off against DBM SEC-12 Grounding and Bonding. |
| CWP-040-008 | The Construction Work Package shall require armored cable installation in tray (TECK 90, ACWU, or ACIC; aluminum interlocking armor; HL rated; rated for -40 deg C; copper conductors up to #1/0 AWG, ACWU larger than #1/0 AWG). Motor feeders shall run directly to the motor and be free of splices or terminations. | Check cable schedule, tray loading, and field termination records against DBM SEC-12 Cable, Wire, and Raceways. |
| CWP-040-009 | The Construction Work Package shall require LED lighting suitable for the applicable area classification; at least two emergency LED fixtures with battery backup per building; 120 V receptacles suitable for area classification with GFI breakers on outdoor circuits; receptacle and lighting circuits shall not be mixed. | Check lighting and receptacle installation against DBM SEC-12 Lighting and Receptacles. |
| CWP-040-010 | The Construction Work Package shall plan installation of 600 V, 3 phase electric building heaters. | Check heater installation and commissioning records against DBM SEC-12 Building Heaters. |
| CWP-040-011 | The Construction Work Package shall NOT treat building coordinates, road geometry, and inter-unit spacing as final until plot plan CIV-235633-5002 is received and reviewed. | Confirm coordinates and layout entries remain TBD or carry a citation to an approved plot plan/IFC drawing. |
| CWP-040-012 | The Construction Work Package shall NOT treat geotechnical or topographical design parameters as final construction criteria until the geotechnical assessment and topographical survey are completed and reviewed. | Confirm bearing capacity, lateral pile design, LPILE curves, dynamic criteria, pavement design, and pavement layer thicknesses remain TBD or backed by accepted geotechnical data. |
| CWP-040-013 | The Construction Work Package shall not assume final equipment ratings or settings before completion of the required electrical studies: hazardous-area classification, load analysis, short-circuit, relay coordination/arc-flash, and load-flow. | Confirm equipment-rating sections reference completed studies or carry TBD. |
| CWP-040-014 | The Construction Work Package shall identify all unresolved inputs affecting construction readiness, including geotechnical report, topographical survey/grade surface file, plot plan, electrical studies, standby generator sizing/transfer-switch ratings, vendor IFC drawings for 860-1, and approved inspection/turnover forms. | Review open item log and turnover checklist. |
| CWP-040-015 | The Construction Work Package shall plan tie-in coordination with shared utilities, cable tray entries, fire & gas/safety systems, communications/network, and area lighting, including joint planning windows with Tourmaline field construction for ISBL/OSBL tie-in points. | Check tie-in schedule and interface sign-off forms. |
| CWP-040-016 | The Construction Work Package shall exclude cathodic protection engineering and supply from the facility design scope and shall only document owner CP interfaces required within the facility. | Confirm CP exclusion is stated and any CP interface points are referenced to owner scope. |
| CWP-040-017 | ASSUMPTION: Because Gate 7 assigns the deliverable to the EPC Integrator while the 04-25 DBM assigns field construction activities (including field-erected buildings, off-loading, setting on foundations, mechanical hookup, home-run cables, electrical terminations, area lighting) to Tourmaline Oil Corporation, the work package should distinguish document ownership from field execution responsibility. | Human review of responsibility matrix; see Guidance Conflict Table CWP-040-CON-001. |

## Standards

| Standard or basis | Applicability | Source |
|---|---|---|
| CSA C22.1-21 Canadian Electrical Code | Electrical design, installation, conduit/raceway, grounding, and area-classification basis. | DBM-Deepcut SEC-12 Governing Codes/Standards |
| BC provincial and local electrical codes; Technical Safety BC; WorkSafeBC; BCER | Provincial and regulatory electrical inspection authority basis. | DBM-Deepcut SEC-12 Governing Codes/Standards |
| API, IEEE, ISA, NEMA standards (applicable revisions) | Electrical equipment design, fabrication, installation, testing, and inspection basis. | DBM-Deepcut SEC-12 Governing Codes/Standards |
| API RP-505 | Fugitive emission / area classification basis for process modules and buildings. | DBM-Deepcut SEC-12 Area Classification |
| National Building Code of Canada (2020 IDF station data; 2018 BC Building Code site naming) | Building, structural loading, snow/wind/seismic loading basis for the electrical building. | DBM-Deepcut SEC-02 Site Data; SEC-11 Governing Civil/Structural Basis |
| CAN/CSA-S16; CAN/CSA A23.3; Canadian Foundation Engineering Manual; CSA G40.20/G40.21; CSA A23.1/A23.2 | Structural steel, concrete, and foundation design basis for foundations and supports under the electrical building. | DBM-Deepcut SEC-11 |
| NEMA VE2 | Cable tray support basis where a project-issued support detail is not provided. | DBM-Deepcut SEC-12 Cable Tray and Conduit |
| Project electrical/instrumentation specifications ELC-QAS-000001-001 through ELC-QAS-000018-001 | Electrical construction; electrical design; electrical requirements for packaged equipment; LV/MV motors; LV/MV switchgear and MCCs; UPS; oil-filled transformers; electric heat tracing; control panel; instrumentation; gas/fire detection; vibration instrumentation. | DBM-Deepcut SEC-12 Governing Codes/Standards (Table 12-1) |

Third-party certification of supplied equipment shall be CSA, ULc, FM, ETL, or another Nationally Recognized Testing Laboratory acceptable for the application (DBM SEC-12 Governing Codes/Standards).

## Verification

The Construction Work Package is ready for controlled review when:

- identity fields match Gate 7, PACKAGE_REGISTER row PKG-040, and workbook row 42;
- all twelve PKG-040 interface facts are carried into the construction interface checklist;
- all DBM SEC-11 / SEC-12 basis values used in the work package cite the DBM section or an approved downstream engineering document;
- vendor-vs-EPC scope split is explicit and the field construction execution responsibility (Tourmaline) is shown separately from the deliverable ownership (EPC Integrator);
- all missing construction quantities, coordinates, vendor IFC drawings, electrical study outputs, plot plan coordinates, and final geotechnical/topographical inputs are listed as `TBD` or open items;
- inspection and turnover records are named, even where final forms remain `TBD`.

## Documentation

The following documentation shall be produced or attached to the Construction Work Package:

- construction work package;
- installation and tie-in workface plan (receipt of 860-1 module, setting on foundations, bottom-entry cabling, HVAC startup, grounding install/test, lighting, building heaters, hookup of fire & gas, comms/network, I&C cabling, utility piping/drains);
- construction interface and turnover checklist (twelve PKG-040 interface categories);
- responsibility matrix distinguishing Package Vendor, EPC Integrator deliverable ownership, and Tourmaline field construction execution;
- open input and TBD register (geotech, topo, plot plan, electrical studies, standby generator basis, vendor IFC drawings, inspection/turnover forms);
- electrical study readiness register (HAC, load analysis, short-circuit, relay coordination/arc-flash, load-flow);
- inspection and turnover record index, with final forms TBD.
