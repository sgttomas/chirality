# Datasheet: DEL-036-02_package-datasheet

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-036-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable name | Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-036` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 6.9kV SWITCHGEAR ELECTRICAL BUILDING (830-1) | Workbook Packages row 38; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 36 / row 38 | Workbook Packages row 38; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 38; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-027 | Workbook Packages row 38; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 38; `_CONTEXT.md` |
| Deliverable type | EPC Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-036` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-036` |
| Package function | 6.9 kV switchgear electrical building (modular, prefabricated). Per workbook identity the building serves a 6.9 kV switchgear/MCC scope for medium-voltage process drives. | Workbook Packages row 38; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §Electrical Buildings (L2971-2979); §Medium-voltage services (L2935) |
| Building tag | 830-1 (carried per workbook spelling) | Workbook Packages row 38 |
| Medium-voltage service basis | 6.9 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded; serves facility process AC inverter-drive motors rated 5,500 hp and above. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2935 |
| Electrical-building scope basis | Electrical buildings shall be prefabricated, modular buildings located in general purpose areas, and shall house, as required by detailed design, medium-voltage switchgear, MCCs, RVSSs, VFDs, 600 V MCCs, 120 V AC and 125 V DC UPS systems with battery banks and distribution panels, distribution transformers and panelboards, contactor panels, PLC control panels, and network racks. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §Electrical Buildings (L2973) |
| Building HVAC basis | Climate-controlled with HVAC sized as an n + 1 system so the cooling system can tolerate failure or maintenance shutdown of one HVAC unit without affecting building heating and cooling. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2975 |
| Cable entry basis | Designed for bottom entry of incoming and outgoing power cables; buildings elevated and installed on piles to provide cable-tray space beneath the building. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2977 |
| Cable type basis | Electrical buildings shall be wired with TECK and ACIC cables. EMT conduit shall be used for equipment located adjacent to each other. An outdoor GFI receptacle shall be provided for exterior maintenance. Equipment doors shall be sized for, or include removable transom sections to allow, removal of the largest equipment. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2979 |
| Area classification basis | Electrical buildings shall be located in general purpose areas for convenient power distribution. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2911 |
| Distance basis | Minimum 25 m (82 ft) between fired heater and control room or electrical buildings (OGAOM Sec. 9.6.15). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L298 |
| Switchgear count basis | DBM electrical equipment list identifies Medium Voltage Switchgear quantity 1 across the facility; package-specific allocation to PKG-036 is `TBD`. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2880 |
| 6.9 kV vs 830-1 building identity | `CONFLICT`. Workbook Packages row 38 names PKG-036 "6.9kV SWITCHGEAR ELECTRICAL BUILDING (830-1)", but the DBM electrical building list shows 830-1 as "4.16kV Acid Gas / Overheads Compressor Electrical Building" and 820-1 as "6.9kV Inlet / Sales Compressor Electrical Building". Datasheet preserves the workbook spelling pending human ruling (see Guidance Conflict Table). | Workbook Packages row 38; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2811-2816, L2921 |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Utility Piping | Applicable interface fact carried as datasheet evidence (not a separate deliverable). | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-9188C9FD26` |
| Drain / Containment | Applicable interface fact carried as datasheet evidence. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-628EF275F0` |
| Electrical Power | Applicable interface fact carried as datasheet evidence. Plant feed is radial from the 13.8 kV switchgear via step-down transformers to medium-voltage electrical buildings. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-3B6012818E`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2919-2925 |
| Grounding / Bonding | Applicable interface fact. Major electrical equipment shall be directly connected to the ground grid at two points. Each 6.9 kV transformer shall be grounded using a 100 A, 10 s neutral grounding resistor and shall operate as a tripping system. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-B6F77BBE8A`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2985, L2989 |
| Area / Exterior Lighting | Applicable interface fact carried as datasheet evidence. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-D49FB38D6F` |
| I&C / Control Cabling | Applicable interface fact. MV equipment to include Ethernet communication ports for plant PLC integration. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-972B08F285`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2955 |
| Communications / Network | Applicable interface fact carried as datasheet evidence; building houses network racks. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-349D2200D1`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2973 |
| Building HVAC / Services | Applicable interface fact. Building HVAC sized n + 1. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-C81A342112`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2975 |
| Fire & Gas / Safety Systems | Applicable interface fact carried as datasheet evidence. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-2C313DA749` |
| Maintenance Access | Applicable interface fact. Cable tray and conduit routing shall not interfere with maintenance access; equipment doors shall accommodate removal of the largest equipment. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-21B90D3691`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2979, L2999 |
| Grading / Site Drainage / Spill Containment | Applicable interface fact carried as datasheet evidence. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-DC7DB17C89` |
| Structural / Foundations / Supports | Applicable interface fact. Building elevated and installed on piles to allow bottom-entry cable trays. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-BDE626F7DD`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2977 |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-036` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-036` |
| Building construction type | Prefabricated, modular electrical building, shop-built. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2811-2816, L2973 |
| Foundation/support | Elevated on piles with cable-tray space beneath; bottom cable entry. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2977 |
| Cabling | TECK and ACIC cables in building; EMT conduit for adjacent equipment; 6.9 kV MV cable is three-conductor copper TECK rated 8 kV with 100% insulation, shielded. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2979, L3008 |
| Interior equipment scope | `TBD` until detailed design. Candidate scope per DBM: 6.9 kV switchgear, 6.9 kV MCC, RVSS/VFDs, 600 V MCC, 120 V AC and 125 V DC UPS systems with battery banks and distribution panels, distribution transformers and panelboards, contactor panels, PLC control panels, and network racks. Package-specific equipment list is not available in source. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2973; `26020-Package_Requirements.docx` has no accessible PKG-036 package-specific slice |
| Building location | `TBD`. DBM states electrical buildings are located in general purpose areas; no source slice fixes a coordinate for 830-1. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2911 |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-036-02_package-datasheet`.
- `PACKAGE_REGISTER.csv`, row `PKG-036`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-036-02_package-datasheet`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-036` (12 applicable interface facts).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-036-02_package-datasheet` (OBJ-001, OBJ-004 through OBJ-010).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 38.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis source slices: Electrical Buildings (L2971-2979), Medium-voltage services (L2935), Power distribution (L2917-2925), Grounding (L2985-2989), Cable/raceway (L2999, L3008), Area classification (L2911), Distance criteria (L298), Equipment list (L2879-2880), Electrical building list (L2811-2816), 6.9 kV MCC scope (L2955).
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific 6.9 kV switchgear electrical building content; no PKG-036 / 830-1 specific match was located in this run.
