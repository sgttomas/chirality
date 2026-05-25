# Datasheet: DEL-033-02_package-datasheet

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-033-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable name | Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-033` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 4160V SWITCHGEAR ELECTRICAL BUILDING (830-2) | Workbook Packages row 35; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 33 / row 35 | Workbook Packages row 35; `PACKAGE_REGISTER.csv` |
| WBS | 02 | Workbook Packages row 35; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-02-30-024 | Workbook Packages row 35; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 35; `_CONTEXT.md` |
| Deliverable type | EPC Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-033` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package (prefabricated modular electrical building) | `PACKAGE_REGISTER.csv` row `PKG-033`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Electrical Buildings" section |
| Package function | 4160 V (4.16 kV) switchgear housed in a dedicated prefabricated electrical building identified as "830-2". | Workbook Packages row 35; `PACKAGE_REGISTER.csv` |
| Building tag association | `ASSUMPTION`: tag "830-2" follows the DBM electrical-building tagging pattern (e.g., 810-1, 820-1, 830-1 for switchgear/MCC electrical buildings). The accessible source set does not contain an explicit "830-2" entry; the most closely related listed building is "830-1 4.16kV Acid Gas / Overheads Compressor Electrical Building." Confirm assignment via detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, building list (lines 2811-2816) |
| Nominal switchgear voltage | 4.16 kV (4160 V), 3-phase, 60 Hz. Grounding class (LRG) and short-circuit rating `TBD` pending project electrical specifications and detailed-design study results. | Workbook Packages row 35 (package name); DBM medium-voltage services basis |
| Distribution architecture | Power radially distributed from the 13.8 kV main switchgear via step-down transformer to a 4.16 kV electrical building. Specific feeder source for 830-2 `TBD` pending single-line confirmation. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical distribution narrative (lines 2917-2925) |
| Building configuration | Prefabricated modular electrical building, climate-controlled, n+1 HVAC, bottom cable entry, elevated on piles, TECK/ACIC cabling, EMT conduit between adjacent panels, removable transom/door sizing for largest equipment. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Electrical Buildings" section (lines 2971-2981) |
| Anticipated housed equipment | As required by detailed design, may include MV switchgear, MV MCCs, MV RVSS/VFDs, 600 V MCCs, 120 V AC and 125 V DC UPS systems with battery banks and distribution panels, 600 V to 208/120 V distribution transformers, panelboards, PLC control panels, and network racks. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Electrical Buildings" section |
| Switchgear count | `TBD`. DBM equipment list identifies "Medium Voltage Switchgear" quantity 1 for the deep-cut scope; allocation specifically to PKG-033 (830-2) is not confirmed by the accessible source set. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical equipment list (line 2880) |
| Standby/emergency power interface | Standby power supports critical systems during outages; generator sizing, transfer switching, load shedding, sequencing, and TOU standard confirmation remain `TBD`. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, emergency power rows (lines 1836, 2164) |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Utility Piping | Interface fact applies to PKG-033 and must be represented in the package interface requirements matrix. | Workbook Packages row 35; `INTERFACE_REGISTER.csv` `IFC-C55D5117E0` |
| Drain / Containment | Interface fact applies to PKG-033 and must be represented in the package interface requirements matrix. | Workbook Packages row 35; `INTERFACE_REGISTER.csv` `IFC-6D41E81E9D` |
| Electrical Power | Interface fact applies to PKG-033 and must be represented in the package interface requirements matrix. | Workbook Packages row 35; `INTERFACE_REGISTER.csv` `IFC-87E42C897B` |
| Grounding / Bonding | Interface fact applies to PKG-033 and must be represented in the package interface requirements matrix. | Workbook Packages row 35; `INTERFACE_REGISTER.csv` `IFC-68149F738F` |
| Area / Exterior Lighting | Interface fact applies to PKG-033 and must be represented in the package interface requirements matrix. | Workbook Packages row 35; `INTERFACE_REGISTER.csv` `IFC-DEF85D9CD6` |
| I&C / Control Cabling | Interface fact applies to PKG-033 and must be represented in the package interface requirements matrix. | Workbook Packages row 35; `INTERFACE_REGISTER.csv` `IFC-34A8619308` |
| Communications / Network | Interface fact applies to PKG-033 and must be represented in the package interface requirements matrix. | Workbook Packages row 35; `INTERFACE_REGISTER.csv` `IFC-F6B851FF9C` |
| Building HVAC / Services | Interface fact applies; n+1 HVAC sizing required for electrical buildings per DBM. | Workbook Packages row 35; `INTERFACE_REGISTER.csv` `IFC-F6FC5D19F9`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-building HVAC paragraph |
| Fire & Gas / Safety Systems | Interface fact applies to PKG-033 and must be represented in the package interface requirements matrix. | Workbook Packages row 35; `INTERFACE_REGISTER.csv` `IFC-BED07EB56D` |
| Maintenance Access | Interface fact applies; cable tray and conduit routing shall not interfere with maintenance access. | Workbook Packages row 35; `INTERFACE_REGISTER.csv` `IFC-73858A4A80`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray/conduit paragraphs |
| Grading / Site Drainage / Spill Containment | Interface fact applies to PKG-033 and must be represented in the package interface requirements matrix. | Workbook Packages row 35; `INTERFACE_REGISTER.csv` `IFC-9AEF468935` |
| Structural / Foundations / Supports | Interface fact applies; electrical building shall be elevated and installed on piles per DBM. | Workbook Packages row 35; `INTERFACE_REGISTER.csv` `IFC-D7C1CC054F`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-building foundations paragraph |
| Grounding design basis | Major electrical equipment shall be directly connected to the ground grid at two points; ground wells provided at electrical buildings; above-grade conductors green-insulated in PVC conduit where mechanical protection is required; compression-type connections. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraph (line 2989) |
| Area classification | Electrical buildings shall be located in general purpose areas for convenient power distribution. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, area classification paragraph (line 2911) |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-033` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-033` |
| Installation location | Building 830-2 location and orientation `TBD` pending plot plan confirmation; building shall be located in a general purpose area. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, area classification paragraph |
| Foundations / supports | Elevated, pile-supported prefabricated electrical building; bottom cable entry; equipment loads, snow/wind/seismic and frost criteria `TBD` per geotechnical and structural detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, foundations paragraph (line 700) |
| Cable entry / raceway | Bottom entry for incoming/outgoing power cables; TECK/ACIC cables; EMT conduit for adjacent equipment; tray routing preserves maintenance access. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings/raceway paragraphs |
| HVAC | n+1 sized HVAC so that one unit failure or maintenance does not affect building heating/cooling. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph (line 2975) |
| Switchgear ratings, bus capacity, protection scheme | `TBD` pending vendor data, short-circuit study, protection coordination study, and project electrical specifications. | Source gap; `26020-Package_Requirements.docx` not searched at the granularity needed for confirmation |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-033-02_package-datasheet`.
- `PACKAGE_REGISTER.csv`, row `PKG-033`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-033-02_package-datasheet`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-033` (twelve applicable interface facts).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-033-02_package-datasheet`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 35.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis source slices for electrical buildings, distribution architecture, grounding, raceway, HVAC, area classification, and standby power.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, supporting electrical-building and foundations context.
- `_Sources/26020-Package_Requirements.docx`, package-specific requirements; no confirmed PKG-033 (830-2) slice located during this run.
