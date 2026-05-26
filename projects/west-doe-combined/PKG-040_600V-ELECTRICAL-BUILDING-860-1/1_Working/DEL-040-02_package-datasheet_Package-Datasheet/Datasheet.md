# Datasheet — DEL-040-02 Package Datasheet (PKG-040 600V Electrical Building 860-1)

> Source authority: Workbook Packages row 42; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
> Unknowns are recorded as `TBD`. Inferences are labelled `ASSUMPTION`.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-040-02_package-datasheet | `_CONTEXT.md` Identity |
| Deliverable Name | Package Datasheet | `_CONTEXT.md` Identity |
| Parent Package ID | PKG-040 | `_CONTEXT.md` Identity |
| Parent Workbook ID | 40 | `_CONTEXT.md` Identity |
| Package Name | 600V ELECTRICAL BUILDING (860-1) | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row 42 |
| Building Tag | 860-1 | `4-25_Deepcut_DBM.md` Building list (#56), "860-1 600V General Area / Tank Farm Electrical Building" |
| Building Function (per Deepcut DBM) | 600V General Area / Tank Farm Electrical Building | `4-25_Deepcut_DBM.md` Building list |
| Discipline | Electrical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row 42 |
| Deliverable Type | EPC Package Datasheet | `_CONTEXT.md` Identity |
| Responsible Party | EPC Integrator | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row 42 |
| WBS | 01 | `PACKAGE_REGISTER.csv` row 42 |
| Workbook Equipment Code | 26020-01-30-031 | `PACKAGE_REGISTER.csv` row 42 |
| Construction Mode | Shop (prefabricated, modular) | `4-25_Deepcut_DBM.md` Building list (`Shop`); Electrical Buildings section |

## Scope and Boundaries (Attributes)

| Attribute | Value | Source |
|---|---|---|
| Scope statement | Mandatory EPC Integrator technical handoff containing the package data required for third-party vendor or discipline package engineering and design of the 600V Electrical Building (860-1). | `_CONTEXT.md` Scope |
| Package vendor ownership | Package engineering, package design, vendor documentation, physical equipment package. | `PACKAGE_REGISTER.csv` row 42 |
| EPC Integrator ownership | Integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration. | `PACKAGE_REGISTER.csv` row 42 |
| Scope item covered | SOW-0041 | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package exclusions | TBD — no package-specific exclusions stated in source materials. | `PACKAGE_REGISTER.csv` row 42 ("TBD") |

## Design Conditions

| Condition | Value | Source |
|---|---|---|
| Building location | General purpose (non-hazardous) area; convenient for power distribution. | `4-25_Deepcut_DBM.md`, "Outdoor pipe racks shall be general purpose areas. Electrical buildings shall be located in general purpose areas for convenient power distribution." |
| Area classification basis | Class I Zone 2, Gas Groups IIA and IIB facility-wide default; electrical building itself sited in general purpose area. | `3-25_Comp_and_Liquids_DBM.md` Area Classification; `4-25_Deepcut_DBM.md` Electrical Buildings |
| Climate control | HVAC, n+1 redundancy, tolerant of single-unit failure or maintenance shutdown without affecting heating/cooling. | `4-25_Deepcut_DBM.md` Electrical Buildings |
| Cable entry | Bottom entry for incoming and outgoing power cables; building elevated on piles to provide under-building space for incoming-cable trays to 600V MCC main incoming section. | `4-25_Deepcut_DBM.md` Electrical Buildings |
| Wiring methods | TECK and ACIC cables; EMT conduit between adjacent equipment (e.g., control panel to contactor panel); outdoor GFI receptacle provided for exterior maintenance. | `4-25_Deepcut_DBM.md` Electrical Buildings |
| Equipment access | Equipment doors sized for, or include removable transom sections to allow, removal of the largest equipment. | `4-25_Deepcut_DBM.md` Electrical Buildings |
| Building heaters | 600 V, 3 phase rated. | `4-25_Deepcut_DBM.md` "Electric building heaters shall be provided as 600 V, 3 phase rated equipment." |
| Foundation/anchorage | Equipment-specific foundation and anchorage checks required for electrical buildings; foundations designed for geotechnical report, equipment loads, snow/wind/seismic, frost protection, vibration, settlement, maintenance access. | `3-25_Comp_and_Liquids_DBM.md` Foundations |

## Power System Context (this building's role)

| Item | Value | Source |
|---|---|---|
| Position in facility distribution | 600 V general-area/tank-farm/process distribution; one of several electrical buildings fed radially from the 13.8 kV plant main switchgear via step-down transformers. | `4-25_Deepcut_DBM.md` Power System; building list (#56 #860-1). |
| Service voltages housed (typical) | 600 V, 3 phase, 3 wire, 60 Hz, high-resistance grounded with 5 A continuous resistor (motors 3/4 hp to 250 hp DOL; lighting/utility distribution transformers; building heaters; UPS > 10 kVA). 208/120 V, 3 phase, 4 wire derived from 600 V distribution transformer (lighting, receptacles, EHT, small loads). 120 VAC / 125 VDC UPS for controls, emergency/critical lighting, MV breaker control circuits. | `4-25_Deepcut_DBM.md` System Voltages |
| Equipment likely housed (per DBM Electrical Buildings paragraph) | 600 V MCCs; 600 V to 208/120 V distribution transformers and panelboards; 208/120 V contactor panels; 120 V AC UPS systems with battery banks and distribution panels; 125 V DC UPS systems with battery banks and distribution panels; plant PLC control panels; network racks; SCR heater-control panels (where required). | `4-25_Deepcut_DBM.md` Electrical Buildings; "208/120 V Systems and SCR Heater Controls" |
| Grounding of 600 V transformer feeding this MCC | 5 A continuous high-resistance grounding resistor; ground-fault protection on 600 V systems alarm-only to maintain continuity of operations. | `4-25_Deepcut_DBM.md` Grounding and Bonding |
| Standby power interface | LV standby generators with transfer switch tie-in at the 600 V MCC level; generator count, ratings, transfer-switch type, load-shedding/critical-load list TBD. | `3-25_Comp_and_Liquids_DBM.md` 600V MCC and Standby Power; `4-25_Deepcut_DBM.md` Standby Power |

## Construction

| Item | Value | Source |
|---|---|---|
| Construction mode | Prefabricated, modular building — shop fabricated. | `4-25_Deepcut_DBM.md` Electrical Buildings; Building list (`Shop`) |
| Mounting | Elevated on piles; ground grid interconnection via driven piles as ground electrodes. | `4-25_Deepcut_DBM.md` Electrical Buildings; Grounding and Bonding |
| Building color (flashing, doors, trim) | Cloverdale #2593 "Safety Green" (project building color schedule). | `4-25_Deepcut_DBM.md` Buildings color schedule |
| Ground connection | Two-point direct connection to ground grid; ground wells with bolted test connections provided at electrical buildings for maintenance/operational testing. | `4-25_Deepcut_DBM.md` Grounding and Bonding |
| Cable tray | Main cable tray runs pre-installed in shop; field-run cable tray limited to field-constructed portions; armored cable (TECK 90, ACWU, ACIC), HL rated, -40 °C. | `4-25_Deepcut_DBM.md` Cable, Wire, and Raceways |

## Specific Interface Set (carried as evidence per `_CONTEXT.md` Notes)

The following interface types apply to this package per `PACKAGE_REGISTER.csv` row 42 and the rows in `INTERFACE_REGISTER.csv` (IFC-C7A10165E0 .. IFC-327D21980E):

| Interface ID | Type |
|---|---|
| IFC-C7A10165E0 | Utility Piping |
| IFC-84254E4D74 | Drain / Containment |
| IFC-01418C7B46 | Electrical Power |
| IFC-1AFD94C7C5 | Grounding / Bonding |
| IFC-31FBC53269 | Area / Exterior Lighting |
| IFC-4924815E92 | I&C / Control Cabling |
| IFC-07F9E1739B | Communications / Network |
| IFC-E5C808A2AF | Building HVAC / Services |
| IFC-AB1228ED22 | Fire & Gas / Safety Systems |
| IFC-DD57C5C1B0 | Maintenance Access |
| IFC-CB9A638F41 | Grading / Site Drainage / Spill Containment |
| IFC-327D21980E | Structural / Foundations / Supports |

Source: `_Decomposition/.../GATE-07_Final_Published_2026-05-24/INTERFACE_REGISTER.csv` rows 262–273.

## Anticipated Artifacts (produced under this deliverable)

- Package technical datasheet (this document, when populated to vendor-issue level — many values currently TBD pending detailed engineering).
- Vendor engineering handoff basis (consolidated reference set drawn from sources cited herein).
- Package interface requirements matrix (the interface table above is the seed; per-interface technical values are TBD).
- Source-supported equipment and design criteria (above sections).

Source: `_CONTEXT.md` Anticipated Artifacts.

## References

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (deliverable folder).
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` row 42.
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/INTERFACE_REGISTER.csv` rows 262–273.
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` DEL-040-02 row.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — Area Classification, Power System (incl. 600V MCC and Standby Power), Electrical Buildings/Raceways.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — SEC-12 Electrical Basis, Electrical Buildings, Grounding & Bonding, Cable specifications, building list (Building #56 / "860-1"), building color schedule, building heaters statement.
- Workbook Packages row 42 (workbook artifact: `_Sources/26020-Packages_Interfaces_4_export.xlsx`; not directly read as text — cited via decomposition registers).

## TBD / location-TBD items

- Exact equipment list (MCC bucket counts, transformer kVA, UPS sizing, panel quantities) — TBD pending detailed electrical engineering.
- Standby generator count, rating, transfer-switch arrangement — TBD per `3-25_Comp_and_Liquids_DBM.md` 600V MCC and Standby Power.
- Specific 600 V loads in general-area / tank-farm coverage — TBD pending facility load list.
- Package-specific exclusions — TBD (no exclusions in source materials per `PACKAGE_REGISTER.csv`).
- Per-interface technical envelope (sizes, tags, set-points) — TBD; only interface types are currently registered.
