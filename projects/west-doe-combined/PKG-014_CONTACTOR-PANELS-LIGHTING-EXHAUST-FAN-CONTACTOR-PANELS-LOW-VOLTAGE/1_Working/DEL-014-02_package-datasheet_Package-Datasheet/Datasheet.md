# Datasheet: DEL-014-02_package-datasheet

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-014-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable name | Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-014` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | CONTACTOR PANELS - LIGHTING / EXHAUST FAN CONTACTOR PANELS - LOW VOLTAGE | Workbook Packages row 16; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 14 / row 16 | Workbook Packages row 16; `PACKAGE_REGISTER.csv` |
| WBS | 02 | Workbook Packages row 16; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-02-30-005 | Workbook Packages row 16; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 16; `_CONTEXT.md` |
| Deliverable type | EPC Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-014` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package, low-voltage class | `PACKAGE_REGISTER.csv` row `PKG-014` |
| Package function | Low-voltage contactor panels providing switching/control for lighting circuits and building exhaust-fan circuits within the facility electrical distribution scheme. | Workbook Packages row 16; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` "208/120 V Systems and SCR Heater Controls" and "Electrical Buildings" sections |
| Nominal voltage class | 208/120 V, 3 phase, 4 wire, 60 Hz, solidly grounded (Lighting and utility services). Specific contactor-panel input voltage and ratings are TBD pending detailed design / vendor data. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` section "Voltage Levels and Services" and "208/120 V Systems and SCR Heater Controls" |
| Source / upstream supply | 208/120 V distribution panelboards established by 600 V to 208/120 V distribution transformers in the electrical building; transformer neutral solidly grounded; each transformer feeds its own 208/120 V distribution panelboard. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` "208/120 V Systems and SCR Heater Controls" |
| Loads served (lighting) | Lighting and receptacles, including general purpose 120/208 V lighting fed from the nearest power distribution centre, MCC room flat-panel LED fixtures, process-area and outdoor LED fixtures, and emergency lighting (battery-backed) per building code. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` "Lighting and Receptacles" |
| Loads served (exhaust fans) | Building exhaust fans (including forced-ventilation modules/buildings whose ventilation maintains area classification), building heater blower fans, and packaged equipment requiring 208/120 V power. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` "208/120 V Systems and SCR Heater Controls"; "Area Classification and Hazardous Locations" (forced-ventilation interlock paragraph) |
| Housing / location | Located within prefabricated modular electrical buildings, which house, as required by detailed design, "208/120 V contactor panels" alongside MCCs, UPS systems, distribution transformers/panelboards, plant PLC panels, and network racks. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` "Electrical Buildings" |
| Quantity / panel count | TBD. The accessible source set confirms 208/120 V contactor panels are housed in electrical buildings "as required by detailed design," but does not enumerate panel count, feeder count, or per-panel circuit load lists for PKG-014. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` "Electrical Buildings"; no PKG-014 match in `26020-Package_Requirements.docx` |
| Forced-ventilation control interlock | Forced-ventilation process modules or buildings that rely on ventilation to maintain area classification shall include exhaust-fan control and monitoring; an interlock shall be initiated in the plant control system to support safe operation of electrical equipment when required to maintain the classification basis. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` "Area Classification and Hazardous Locations" |
| Exhaust-fan / heater control I/O | Remote I/O nodes (Allen-Bradley Flex5000 at remote distribution centres) may support building exhaust fan and heater controls. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 804 (Remote I/O / RDC paragraph) |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to `PKG-014` and shall be represented in the package interface requirements matrix; upstream 208/120 V distribution panelboards sourced from 600 V/208-120 V distribution transformers. | Workbook Packages row 16; `INTERFACE_REGISTER.csv` `IFC-78CF31138D`; DBM "208/120 V Systems" |
| Grounding / Bonding | Interface fact applies to `PKG-014` and shall be represented in the matrix. Distribution transformers and panelboards require a separate copper ground conductor sized per CEC, in addition to grounding conductor run with power wiring. 208/120 V system transformer neutral is solidly grounded. | Workbook Packages row 16; `INTERFACE_REGISTER.csv` `IFC-31C88BB424`; DBM "Grounding and Bonding"; DBM "208/120 V Systems" |
| Area / Exterior Lighting | Interface fact applies to `PKG-014`; lighting circuits supplied through the lighting contactor panels include general-purpose 120/208 V LED lighting, MCC-room flat-panel LED fixtures, process-area and outdoor LED fixtures, post lighting for the overall area where required, and emergency/exit lighting with battery backup. | Workbook Packages row 16; `INTERFACE_REGISTER.csv` `IFC-EF784327FA`; DBM "Lighting and Receptacles"; DBM "post lighting shall be provided for the overall area" |
| I&C / Control Cabling | Interface fact applies to `PKG-014`; control signals between contactor panels and the plant control system (including exhaust-fan and heater control I/O at RDC nodes) shall use the project I&C cabling and remote I/O conventions. | Workbook Packages row 16; `INTERFACE_REGISTER.csv` `IFC-C715E9AA3E`; DBM "Remote I/O" / RDC paragraphs |
| Communications / Network | Interface fact applies to `PKG-014`; communications between PLC-resident control logic and remote I/O nodes uses the project I/O Network (PRP configuration). Specific contactor-panel network ports are TBD. | Workbook Packages row 16; `INTERFACE_REGISTER.csv` `IFC-2D60238809`; DBM Control Systems paragraphs |
| Maintenance Access | Interface fact applies to `PKG-014`; equipment doors shall be sized for or include removable transom sections to allow removal of the largest equipment; cable tray and conduit routing shall not interfere with maintenance access. | Workbook Packages row 16; `INTERFACE_REGISTER.csv` `IFC-52B07B0D36`; DBM "Electrical Buildings"; DBM "Cable, Wire, and Raceways" |
| Structural / Foundations / Supports | Interface fact applies to `PKG-014`. Electrical buildings are elevated and installed on piles; the building ground grid uses driven piles as ground electrodes interconnected by a main #2/0 green insulated grounding conductor. Package-specific support basis is TBD. | Workbook Packages row 16; `INTERFACE_REGISTER.csv` `IFC-53646D26A1`; DBM "Electrical Buildings"; DBM "Grounding and Bonding" |
| Raceway / wiring methods | Within electrical buildings, EMT conduit may be used for equipment located adjacent to each other, such as control panels to contactor panels. Building lighting, exhaust fans, receptacles, and switches in shop-fabricated/erected buildings shall use rigid conduit; EMT may be used in non-process locations such as MCC buildings, control rooms, offices, and warehouses. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` "Electrical Buildings"; "Cable, Wire, and Raceways" |
| Area classification | Contactor-panel housing within general-purpose electrical buildings is the default; lighting fixtures and receptacles shall be suitable for the area classification in which they are installed. | DBM "Lighting and Receptacles"; "Electrical Buildings" |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-014` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-014` |
| Installation location | Within prefabricated modular electrical buildings in general-purpose areas; precise building/room assignment for PKG-014 contactor panels is TBD pending detailed design. | DBM "Electrical Buildings" |
| Foundations / supports | Buildings are pile-supported and elevated; package-specific in-building mounting/support basis is TBD. | DBM "Electrical Buildings" |
| Cable entry | Electrical buildings are designed for bottom entry of incoming and outgoing power cables. | DBM "Electrical Buildings" |
| Climate control | Electrical buildings are climate-controlled with HVAC sized as an n + 1 system. | DBM "Electrical Buildings" |
| Internal panel layout, circuit count, contactor ratings | TBD unless defined by vendor package data and detailed design. | Source gap; `26020-Package_Requirements.docx` has no accessible PKG-014 match |
| Emergency lighting | At least two emergency lighting fixtures shall be provided in each building for power-outage conditions; exit lights battery-backed per building code. | DBM "Lighting and Receptacles" |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-014-02_package-datasheet`.
- `PACKAGE_REGISTER.csv`, row `PKG-014`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-014-02_package-datasheet`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-014` (`IFC-78CF31138D`, `IFC-31C88BB424`, `IFC-EF784327FA`, `IFC-C715E9AA3E`, `IFC-2D60238809`, `IFC-52B07B0D36`, `IFC-53646D26A1`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-014-02_package-datasheet`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 16.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, sections: "Voltage Levels and Services", "208/120 V Systems and SCR Heater Controls", "Electrical Buildings", "Grounding and Bonding", "Cable, Wire, and Raceways", "Lighting and Receptacles", "Area Classification and Hazardous Locations" (forced-ventilation interlock).
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, sections on lighting/utility service, electrical buildings/raceways/lighting/heat tracing, and Remote I/O (exhaust-fan and heater control).
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific PKG-014 content; no package-specific match found.
