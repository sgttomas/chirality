# Datasheet: DEL-040-03_construction-work-package — Construction Work Package

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-040-03_construction-work-package |
| Deliverable name | Construction Work Package |
| Parent package | PKG-040 — 600V ELECTRICAL BUILDING (860-1) |
| Parent workbook row | Workbook Packages row 42 |
| Discipline | Electrical |
| Type | EPC Construction Work Package |
| Responsible party | EPC Integrator |
| Scope item | SOW-0041 |
| Supported objectives | OBJ-001; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 (ASSUMPTION: package-grouping heuristic from PROJECT_DECOMP OBJECTIVE_SCOPE_MAP rows for PKG-040/SOW-0041) |

## Attributes

| Attribute | Current value | Source |
|---|---|---|
| Facility/WBS basis | WBS 01 / 04-25 Deepcut facility basis | 26020-Packages_Interfaces_4_export.xlsx, Packages row 42; PACKAGE_REGISTER.csv PKG-040 |
| CoA tracking number | 26020-01-30-031 | PACKAGE_REGISTER.csv PKG-040 (Workbook Packages row 42) |
| Package discipline | Electrical | PACKAGE_REGISTER.csv PKG-040 (Workbook Packages row 42) |
| Building basis | 860-1 600V General Area / Tank Farm Electrical Building; prefabricated, modular, shop-built electrical building located in a general purpose area. | DBM-Deepcut/4-25_Deepcut_DBM.md, SEC-11 (Buildings table row 860-1); SEC-12 Electrical Buildings |
| Voltage class | 600 V low-voltage MCC building; 600 V is 3 phase, 3 wire, 60 Hz, high-resistance grounded with 5 A continuous resistor. | DBM-Deepcut/4-25_Deepcut_DBM.md, SEC-12 System Voltages |
| Package interfaces | Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports | 26020-Packages_Interfaces_4_export.xlsx, Packages row 42; INTERFACE_REGISTER.csv rows for PKG-040 |
| Construction responsibility basis | Field construction is assigned to Tourmaline Oil Corporation in the 04-25 DBM (including field-erected buildings, off-loading/setting modules on foundations, mechanical hookup, field-installed home-run cables, electrical terminations, and area lighting); EPC Integrator remains the deliverable owner per Gate 7. | DBM-Deepcut/4-25_Deepcut_DBM.md, Construction Responsibility; DELIVERABLE_REGISTER.csv row DEL-040-03 |
| Package vendor / EPC split | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | PACKAGE_REGISTER.csv PKG-040 (Vendor Scope Type description) |
| Deliverable artifact set | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist | DELIVERABLE_REGISTER.csv row DEL-040-03; ARTIFACT_REGISTER.csv rows for DEL-040-03 (location TBD; artifact register rows not opened in this pass) |

## Conditions

| Condition | Current basis | Source |
|---|---|---|
| Area classification | Electrical buildings shall be located in general purpose areas for convenient power distribution; outdoor process and pipe-rack areas are generally Class I Zone 2, Gas Groups IIA and IIB. | DBM-Deepcut/4-25_Deepcut_DBM.md, SEC-12 Area Classification |
| Site/environmental load basis | Dawson Creek BC climate basis; design ambient -40 deg C to +35 deg C; snow load Ss 2.5 kPa, Sr 0.2 kPa; hourly wind pressure q1/50 0.40 kPa; spectral acceleration values per SEC-02. | DBM-Deepcut/4-25_Deepcut_DBM.md, SEC-02 Site Data Basis |
| Foundation basis | Driven steel piles are the default support basis for buildings unless detailed engineering confirms a different basis; electrical buildings shall be elevated on piles to allow bottom entry of incoming/outgoing power cables. | DBM-Deepcut/4-25_Deepcut_DBM.md, SEC-11 Piles and Foundations; SEC-12 Electrical Buildings |
| Geotechnical basis | Bearing capacity, lateral pile data, LPILE curves, dynamic criteria, and pavement design remain TBD pending geotechnical assessment report. | DBM-Deepcut/4-25_Deepcut_DBM.md, SEC-11 External Dependencies / Assumptions |
| Topographical basis | Existing grade surface file assumed suitable for grading and drainage design; final format and contents TBD pending survey completion. | DBM-Deepcut/4-25_Deepcut_DBM.md, SEC-11 External Dependencies |
| Plot plan / location | Final building coordinates, road and access geometry, and inter-unit spacing depend on plot plan CIV-235633-5002, which is not included in the available source package; final equipment placement is TBD. | DBM-Deepcut/4-25_Deepcut_DBM.md, SEC-02 Plot Plan Status |
| HVAC basis | Electrical buildings shall be climate controlled with HVAC sized as an n+1 system so cooling can tolerate single-unit failure or maintenance shutdown. | DBM-Deepcut/4-25_Deepcut_DBM.md, SEC-12 Electrical Buildings |
| Grounding basis | Plant electrical grounding uses driven piles as ground electrodes interconnected by a main #2/0 green insulated grounding conductor; major equipment connected at two points; 600 V system high-resistance grounded with 5 A continuous resistor; ground-fault protection on 600 V is alarm-only. | DBM-Deepcut/4-25_Deepcut_DBM.md, SEC-12 Grounding and Bonding |
| Cable basis | Cables installed in tray shall be armored (TECK 90, ACWU, or ACIC); aluminum interlocking armor, HL-rated, rated for -40 deg C; copper conductors up to #1/0 AWG, ACWU above #1/0 AWG. | DBM-Deepcut/4-25_Deepcut_DBM.md, SEC-12 Cable, Wire, and Raceways |
| Lighting basis | All lighting LED type; suitable for area classification; emergency LED fixtures with battery backup; receptacles 120 V suitable for area classification with GFI as required. | DBM-Deepcut/4-25_Deepcut_DBM.md, SEC-12 Lighting and Receptacles |
| Building heaters | Electric building heaters provided as 600 V, 3 phase rated equipment. | DBM-Deepcut/4-25_Deepcut_DBM.md, SEC-12 Building Heaters |
| Exterior finish | Flashing/doors/trim Cloverdale #2593 "Safety Green"; exterior walls and roof galvanized metal with pre-painted trim; interior walls Bright White QC8783. | DBM-Deepcut/4-25_Deepcut_DBM.md, SEC-11 (Building color table) |
| Standby power interface | Standby basis is TOU standby generators connected at the 600 V MCC level via transfer switches; sizing, transfer-switch ratings, and sequencing are TBD pending electrical studies. | DBM-Deepcut/4-25_Deepcut_DBM.md, SEC-01 Open Basis Items; SEC-12 Standby Power |
| Electrical studies prerequisite | Hazardous-area classification, load analysis, short-circuit, relay coordination/arc-flash, and load-flow studies are required before finalizing equipment ratings and suitability. | DBM-Deepcut/4-25_Deepcut_DBM.md, SEC-12 Governing Codes/Standards |
| Cathodic protection | Cathodic protection engineering and supply are excluded from the facility design scope; the facility shall support owner CP interfaces only. | DBM-Deepcut/4-25_Deepcut_DBM.md, SEC-12 Cathodic Protection |

## Construction

| Construction topic | Current basis |
|---|---|
| Work package boundary | Covers the PKG-040 600V Electrical Building (860-1) construction package for physical installation, construction, inspection, turnover, and tie-in to larger facility systems. The package is shop-built and shipped; field activities cover off-loading, setting on foundations, mechanical/electrical hookup, home-run cabling, and terminations. Source: PACKAGE_REGISTER.csv PKG-040; DBM-Deepcut SEC-11 (Buildings table) and SEC-12 (Electrical Buildings); DBM Construction Responsibility. |
| Included field activities | Construction management; grading, piling, and foundation work; off-loading the 860-1 building module at site; setting the building on piles/foundations; mechanical hookup of interconnecting piping/utilities; installation of shipped-loose instruments, valves, and components; installation of miscellaneous structural supports; field installation of home-run cables; electrical terminations; area lighting. Source: DBM-Deepcut/4-25_Deepcut_DBM.md, Construction Responsibility. |
| Tie-in / interface controls | Must address the full PKG-040 interface set: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. Tie-in timing TBD; joint planning with Tourmaline field construction required. |
| Bottom-entry cable provisions | Electrical building shall be elevated and installed on piles to provide space beneath the building for MCC incoming/outgoing cables in trays. Source: DBM-Deepcut SEC-12 Electrical Buildings. |
| Equipment removal access | Equipment doors sized for, or include removable transom sections to allow, removal of the largest equipment. Source: DBM-Deepcut SEC-12 Electrical Buildings. |
| Quantities and coordinates | TBD; not provided in locally accessible source slices for this deliverable. |
| Inspection and turnover forms | TBD; source set identifies a checklist artifact but does not provide approved form content. |
| Field construction execution | Per DBM, assigned to Tourmaline Oil Corporation; EPC Integrator remains the deliverable owner. CONFLICT recorded in Guidance Conflict Table. |

## References

- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx`, `Packages` row 42. (location TBD: xlsx source not opened directly in this pass; facts mirrored from PACKAGE_REGISTER.csv and INTERFACE_REGISTER.csv which cite Workbook Packages row 42.)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility; SEC-02 Site Data and Plot Plan; SEC-11 Civil/Buildings basis; SEC-12 Electrical Basis (Area Classification, Power System, Electrical Buildings, Grounding and Bonding, Cable/Wire/Raceways, Lighting/Receptacles, Building Heaters, Cathodic Protection).
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv`, row `DEL-040-03_construction-work-package`.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv`, row `PKG-040`.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/INTERFACE_REGISTER.csv`, rows for `PKG-040`.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/OBJECTIVE_SCOPE_MAP.csv`, rows for `SOW-0041` / `PKG-040`.
