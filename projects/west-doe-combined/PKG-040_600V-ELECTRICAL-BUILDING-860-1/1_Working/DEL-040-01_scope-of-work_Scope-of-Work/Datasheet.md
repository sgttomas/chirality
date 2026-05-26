# Datasheet: DEL-040-01 Scope of Work

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-040-01_scope-of-work | `_CONTEXT.md` Identity |
| Deliverable name | Scope of Work | `_CONTEXT.md` Identity |
| Parent package | PKG-040 | `_CONTEXT.md` Identity; Gate 7 `PACKAGE_REGISTER.csv` row PKG-040 |
| Package name | 600V ELECTRICAL BUILDING (860-1) | Gate 7 `PACKAGE_REGISTER.csv` row PKG-040; `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 42 |
| Workbook ID / row | ID 40 / row 42 | `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 42; Gate 7 `PACKAGE_REGISTER.csv` row PKG-040 |
| WBS | 01 | Gate 7 `PACKAGE_REGISTER.csv` row PKG-040 |
| Tracking number | 26020-01-30-031 | Gate 7 `PACKAGE_REGISTER.csv` row PKG-040 |
| Discipline | Electrical | `_CONTEXT.md` Identity; Gate 7 `PACKAGE_REGISTER.csv` row PKG-040 |
| Deliverable type | EPC Scope of Work | `_CONTEXT.md` Identity; Gate 7 `DELIVERABLE_REGISTER.csv` row DEL-040-01_scope-of-work |
| Responsible party | EPC Integrator | `_CONTEXT.md` Identity; Gate 7 `DELIVERABLE_REGISTER.csv` row DEL-040-01_scope-of-work |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package execution model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-040 |
| Mandatory EPC anchor deliverable | Scope of Work is the mandatory EPC Integrator anchor deliverable for every approved package. | Gate 7 `DELIVERABLE_REGISTER.csv` row DEL-040-01_scope-of-work (Notes); Gate 7 `PROJECT_DECOMP.md` Gate 5 EPC anchor basis |
| Scope item | SOW-0041 | `_CONTEXT.md` Covers Scope Items; Gate 7 `SCOPE_LEDGER.csv` row SOW-0041 (location TBD) |
| Supported objectives | OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv` rows for DEL-040-01_scope-of-work |
| Anticipated artifacts | Package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record. | `_CONTEXT.md` Anticipated Artifacts; Gate 7 `ARTIFACT_REGISTER.csv` rows ART-95D8796E51, ART-22111E8269, ART-EBFDF9B165, ART-1C1CC3907A |
| Tagged equipment | TBD; no individual equipment tags exposed in the accessible workbook row 42 or Gate 7 PKG-040 row. Building number 860-1 is identified. | Workbook Packages row 42; Gate 7 `PACKAGE_REGISTER.csv` row PKG-040 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Building identity in facility electrical hierarchy | Building 860-1 is named "860-1 600V General Area / Tank Farm Electrical Building" in the DBM electrical buildings list. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2816 |
| Low-voltage service basis | 600 V, 3 phase, 3 wire, 60 Hz, high-resistance grounded with 5 A continuous resistor. Serves motors 3/4 hp through 250 hp with direct-on-line starting; lighting and utility distribution transformers; building heaters; UPS systems larger than 10 kVA. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2937 |
| Building type | Prefabricated modular electrical building located in a general purpose area. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2911, 2971-2973 |
| Possible building contents (facility basis, not package-specific allocation) | As required by detailed design: 600 V MCCs, 120 V AC UPS systems with battery banks and distribution panels, 125 V DC UPS systems with battery banks and distribution panels, 600 V to 208/120 V distribution transformers and panelboards, 208/120 V contactor panels, plant PLC control panels, and network racks. Medium-voltage equipment (13.8 kV switchgear, MV MCCs/RVSS/VFDs) is associated with other electrical buildings in the facility hierarchy. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2973, 2919-2925 |
| HVAC basis | Climate-controlled with n + 1 HVAC sizing so cooling can tolerate failure or maintenance shutdown of one HVAC unit without affecting building heating and cooling. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2975 |
| Cable entry basis | Designed for bottom entry of incoming and outgoing power cables; building elevated and installed on piles to provide space beneath for MCC incoming cables in trays to the 600 V MCC main incoming section; outgoing 600 V MCC cables also bottom entry. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2977 |
| Internal wiring basis | TECK and ACIC cables; EMT conduit for adjacent equipment (e.g., control panels to contactor panels); outdoor GFI receptacle for exterior maintenance; equipment doors sized for, or with removable transom sections to allow, removal of the largest equipment. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2979 |
| Grounding basis (system) | 600 V transformer grounded by a 5 A continuous high-resistance grounding resistor; 600 V MCCs include power metering and ground/resistor fault detection; ground-fault protection on 600 V systems is alarm-only to maintain continuity of operations. Major electrical equipment connected to the ground grid at two points; ground wells at electrical buildings for maintenance and operational testing with bolted ground connections at test points. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2985, 2987, 2989 |
| Standby power interface | TOU standby generators connected at the low-voltage MCC level with transfer switches. Generator sizing, count, connection points, transfer switch ratings, transfer mode, paralleling, and load-shedding/sequencing remain TBD per DBM Assumptions/TBDs. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2943, 3086 |
| Building heaters | Electric building heaters at 600 V, 3 phase. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 3071 |
| Service area orientation (descriptive) | DBM building-list naming ties building 860-1 to "General Area / Tank Farm"; specific tank-farm loads served by 860-1 are TBD pending detailed engineering. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2816 |
| Package interfaces (workbook X-column) | Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. | Workbook Packages row 42; Gate 7 `INTERFACE_REGISTER.csv` PKG-040 rows IFC-C7A10165E0, IFC-84254E4D74, IFC-01418C7B46, IFC-1AFD94C7C5, IFC-31FBC53269, IFC-4924815E92, IFC-07F9E1739B, IFC-E5C808A2AF, IFC-AB1228ED22, IFC-DD57C5C1B0, and the remaining two PKG-040 interface rows in `INTERFACE_REGISTER.csv` |
| Package-specific exclusions | TBD; no package-specific exclusions are stated in accessible source materials. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-040 |
| Package-specific equipment lineup, ratings, dimensions, weights, loads | TBD; not present in accessible source slices for this deliverable. | Workbook Packages row 42; Gate 7 PKG-040 rows; DBM electrical buildings basis |

## Construction

| Construction / integration topic | Scope-of-work treatment |
|---|---|
| EPC integration boundary | Include facility-level integration, tie-ins, constructability, procurement/construction coordination, and interface management; do not assign vendor package engineering or design to the EPC Integrator. |
| Electrical Power | Coordinate building incoming feeder from the facility medium-voltage distribution (via step-down transformer to 600 V) and outgoing 600 V feeders to facility loads in the general area / tank farm; preserve bottom-entry cable basis. |
| Grounding / Bonding | Carry grounding/bonding as an interface, including connection to the plant main ground grid, two ground-grid connection points, ground well at the building, and 5 A continuous high-resistance grounding for the 600 V system. |
| Area / Exterior Lighting | Carry as an interface for coordination with facility exterior lighting strategy and pole/mast locations in the general area / tank farm. |
| I&C / Control Cabling | Coordinate cable routing, junction boxes at building/skid edge, and connection of plant PLC and contactor panels housed in the building. |
| Communications / Network | Coordinate network rack location, fiber/Ethernet routing, and connection to plant networks. |
| Building HVAC / Services | Coordinate the n+1 HVAC basis, building heaters, and utility services to the building. |
| Fire & Gas / Safety Systems | Coordinate interface with facility F&G/safety systems serving the building; specific area-classification at the 860-1 location is TBD. |
| Maintenance Access | Coordinate building location, door sizes, transoms, exterior GFI receptacle, and cable tray routing so they do not interfere with maintenance access. |
| Utility Piping | Coordinate utility piping interfaces serving the building. |
| Drain / Containment, Grading / Site Drainage / Spill Containment | Coordinate site drainage and containment at the building location, with consideration for adjacent tank-farm containment basis (specific containment requirements TBD). |
| Structural / Foundations / Supports | Carry pile foundations supporting the elevated building basis and cable-tray modules; package-specific loads remain TBD pending vendor data. |

## References

- `_CONTEXT.md`, DEL-040-01 identity, scope, artifacts, objective context.
- `_DEPENDENCIES.md`, declared dependency state.
- `_REFERENCES.md`, Gate 7 source pointers and shared source root.
- Gate 7 `PROJECT_DECOMP.md`, Gate 5 mandatory EPC anchor deliverable basis.
- Gate 7 `PACKAGE_REGISTER.csv`, row PKG-040.
- Gate 7 `DELIVERABLE_REGISTER.csv`, row DEL-040-01_scope-of-work.
- Gate 7 `INTERFACE_REGISTER.csv`, PKG-040 rows (twelve interface flags).
- Gate 7 `ARTIFACT_REGISTER.csv`, rows for DEL-040-01_scope-of-work (ART-95D8796E51, ART-22111E8269, ART-EBFDF9B165, ART-1C1CC3907A).
- Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for DEL-040-01_scope-of-work.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages row 42 (binary workbook; locally present but not text-extracted into a deliverable-local slice — clause-level workbook content cited only where mirrored by Gate 7 registers).
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis: power distribution (lines 2919-2937), MCCs (line 2959), electrical buildings (lines 2911, 2971-2981), grounding and bonding (lines 2985-2991), building heaters (line 3071), standby power (line 2943), Assumptions/TBDs (lines 3079-3090), and facility electrical-building list (line 2816 for building 860-1).
