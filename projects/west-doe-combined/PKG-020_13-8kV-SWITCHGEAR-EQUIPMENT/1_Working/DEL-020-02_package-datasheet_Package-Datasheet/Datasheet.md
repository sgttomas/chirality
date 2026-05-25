# Datasheet: DEL-020-02_package-datasheet

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-020-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable name | Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-020` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 13.8kV SWITCHGEAR EQUIPMENT | Workbook Packages row 22; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 20 / row 22 | Workbook Packages row 22; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 22; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-011 | Workbook Packages row 22; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 22; `_CONTEXT.md` |
| Deliverable type | EPC Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-020` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-020` |
| Package function | Plant main power distribution center: the 13.8 kV switchgear shall be designed, purchased, and installed as the plant main power distribution center, sized for the full facility scope and distributing power to facility electrical buildings. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Power System section (lines 2917-2919) |
| Bus voltage / phase / frequency / grounding | 13.8 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, System Voltages table (line 2934) |
| Incoming source | Fed from a 25 kV to 13.8 kV, 50 MVA utility-supplied transformer stepping down from BC Hydro 25 kV (TBC). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Power System (line 2917) |
| Utility neutral grounding | BC Hydro utility transformer grounded using a 200 A, 10 s neutral grounding resistor; operates as a tripping system. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Grounding and Bonding (line 2985) |
| Bus sizing basis | Bus shall be sized for the full facility scope. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Power System (line 2917) |
| Radial distribution feeders | 13.8 kV switchgear shall distribute power radially through step-down transformers to: 6.9 kV Inlet/Sales Compressor EB; 4.16 kV Acid Gas/Overheads Compressor EB; 600 V Acid Gas Compressor EB; 600 V Sales/Overheads Compressor EB; 4.16 kV/600 V General Area/Tank Farm/Process EB. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Power System (lines 2919-2925) |
| Cross-facility tie | The 03-25 facility is sub-fed from the 04-25 13.8 kV Main Switchgear Electrical Building (incoming feed at 13.8 kV, 3 phase, 3 wire, 60 Hz, LRG). | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Power Supply (lines 732, 740) |
| Standby/emergency power role | The prior centralized 13.8 kV emergency-generator concept has been replaced by TOU standby generators at the 600 V MCC level with transfer switches. The 13.8 kV switchgear is not the connection point for the current standby-power basis. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Standby Power (line 2943); `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (line 505) |
| Switchgear protective relay control power | Medium-voltage breaker control circuits and medium-voltage protective relays are served by 120 VAC / 125 VDC UPS systems. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, System Voltages UPS row (line 2939) |
| Housing | The 13.8 kV main switchgear is housed in a prefabricated electrical building (810-1 13.8kV Switchgear Electrical Building) located in a general-purpose area, climate-controlled with n+1 HVAC, designed for bottom entry of incoming and outgoing power cables. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Modular Buildings list (line 2811); Electrical Buildings (lines 2973-2977) |
| Medium-voltage cable basis | 13.8 kV medium-voltage cables are three-conductor copper TECK rated 15 kV with 133 percent insulation; shielded. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Cable, Wire, and Raceways (line 3007) |
| Power-vs-signal separation | Power circuits at 13.8 kV (and 4,160 V and 600 V) shall be separated from control and instrument circuits by distance, shielding, or routing as required to minimize interference. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (line 768) |
| Detailed equipment configuration | Number of incoming and outgoing breakers, breaker ratings (continuous and interrupting), bus ampacity, short-circuit/withstand rating, metering, protection scheme, arc-flash mitigation, and lineup arrangement. | TBD pending vendor data and project electrical specifications (ELC-QAS-000007-001 Medium Voltage Switchgear). |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to PKG-020 and must be represented in the package interface requirements matrix. | Workbook Packages row 22; `INTERFACE_REGISTER.csv` `IFC-611474D99C` |
| Grounding / Bonding | Interface fact applies to PKG-020 and must be represented in the package interface requirements matrix. | Workbook Packages row 22; `INTERFACE_REGISTER.csv` `IFC-F3098CE7CD` |
| I&C / Control Cabling | Interface fact applies to PKG-020 and must be represented in the package interface requirements matrix. | Workbook Packages row 22; `INTERFACE_REGISTER.csv` `IFC-8BF7209227` |
| Communications / Network | Interface fact applies to PKG-020 and must be represented in the package interface requirements matrix. | Workbook Packages row 22; `INTERFACE_REGISTER.csv` `IFC-340091634A` |
| Maintenance Access | Interface fact applies to PKG-020 and must be represented in the package interface requirements matrix. | Workbook Packages row 22; `INTERFACE_REGISTER.csv` `IFC-2FB786FC10` |
| Structural / Foundations / Supports | Interface fact applies to PKG-020 and must be represented in the package interface requirements matrix. | Workbook Packages row 22; `INTERFACE_REGISTER.csv` `IFC-08E563D004` |
| Grounding design basis | All major electrical equipment shall be directly connected to the ground grid at two points. The plant grounding system uses driven piles as ground electrodes interconnected by a main #2/0 green insulated grounding conductor run in the highest-voltage carrying tray. Ground wells at electrical buildings shall be provided. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Grounding and Bonding (lines 2987-2989) |
| Cable / conduit routing | Cable tray and conduit routing shall preserve maintenance access; bottom entry for building cables is required. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings (line 2977) |
| Area classification | The switchgear electrical building is located in a general-purpose area. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Area Classification (line 2911); Electrical Buildings (line 2973) |
| Protection coordination / metering | Incoming power metering at the facility boundary, protection coordination, and emergency/standby power scope split remain to be confirmed during detailed engineering. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Power System (line 2927) |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-020` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-020` |
| Installation location | The 13.8 kV main switchgear is housed in the 810-1 13.8kV Switchgear Electrical Building (prefabricated/modular, shop). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Modular Buildings list (line 2811) |
| Foundations / supports | Electrical buildings shall be elevated and installed on piles with space beneath for incoming cable trays; structural/foundation interface applies. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings (line 2977); `INTERFACE_REGISTER.csv` `IFC-08E563D004` |
| Cable entry | Bottom entry for incoming and outgoing power cables. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings (line 2977) |
| HVAC | n+1 HVAC sized so the cooling system can tolerate failure or maintenance shutdown of one HVAC unit without affecting building heating and cooling. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings (line 2975) |
| Building wiring | TECK and ACIC cables; EMT conduit for adjacent equipment runs. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings (line 2979) |
| Breaker count, ratings, lineup, arc-flash, metering, relaying scheme | TBD until vendor package data is issued, per ELC-QAS-000007-001 Medium Voltage Switchgear and detailed engineering. | Source gap; project electrical specifications listed in `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Table 12-1 (lines 2872-2889) |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-020-02_package-datasheet`.
- `PACKAGE_REGISTER.csv`, row `PKG-020`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-020-02_package-datasheet`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-020`.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-020-02_package-datasheet`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 22.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Power System, System Voltages, Standby Power, Electrical Buildings, Grounding and Bonding, Cable/Wire/Raceways, and SEC-12 Electrical Basis source slices.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 03-25 power supply, standby, and routing source slices.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific 13.8 kV switchgear content; no PKG-020 match was confirmed.
