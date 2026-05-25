# Datasheet: DEL-026-02_package-datasheet

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-026-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable name | Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-026` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | Transformer TXP-8300-2 - STEP DOWN DISTRIBUTION TRANSFORMER - 20/26MVA 13.8kV/6.9kV/0.4kV | Workbook Packages row 28; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 26 / row 28 | Workbook Packages row 28; `PACKAGE_REGISTER.csv` |
| WBS | 02 | Workbook Packages row 28; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-02-30-017 | Workbook Packages row 28; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 28; `_CONTEXT.md` |
| Deliverable type | EPC Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-026` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-026` |
| Package function | Step-down distribution transformer (designation TXP-8300-2) within the facility medium-voltage distribution scheme. | Workbook Packages row 28; `PACKAGE_REGISTER.csv` |
| Primary voltage rating (from name) | 13.8 kV (primary, facility medium-voltage backbone). | Workbook Packages row 28 (package name); `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis (13.8 kV switchgear distributes radially through step-down transformers). |
| Secondary voltage rating (from name) | 6.9 kV (medium-voltage process drive bus). | Workbook Packages row 28 (package name); `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage and service table (6.9 kV, 3-phase, 3-wire, 60 Hz, LRG for AC inverter-drive motors rated 5,500 hp and above). |
| Tertiary voltage rating (from name) | 0.4 kV winding indicated in the package name. The DBM electrical voltage/service table does not list a facility 0.4 kV service class; tertiary winding purpose, loading, and grounding basis are `TBD`. | Workbook Packages row 28 (package name); `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage and service table — no 0.4 kV service identified. |
| Power rating (from name) | 20/26 MVA (dual rating, ONAN/ONAF or equivalent cooling-stage basis assumed). Cooling-class designation and ambient basis are `TBD`. | Workbook Packages row 28 (package name); no accessible source slice resolves cooling-class designation. |
| Frequency | 60 Hz. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage and service table. |
| Phase configuration | 3-phase. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage and service table (13.8 kV and 6.9 kV medium-voltage services are 3-phase, 3-wire). |
| Insulating medium | Oil-filled (ASSUMPTION). The DBM electrical section describes large oil-filled transformers as the facility convention and references an "Oil-Filled Transformers" QAS line item, but does not confirm the medium for this specific package. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers paragraph and QAS table row `ELC-QAS-000011-001`. |
| Downstream service | Feeds the 6.9 kV Inlet/Sales Compressor Electrical Building (820-1) bus serving the inlet/sales compressor process drives (KM-2150/2250-class motors with starting VFDs). ASSUMPTION based on facility distribution narrative; precise feeder allocation is `TBD`. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, step-down distribution list and electrical buildings table. |
| Upstream source | Fed radially from the 13.8 kV main switchgear (810-1 13.8 kV Switchgear Electrical Building) sub-fed from the BC Hydro 25 kV/13.8 kV 50 MVA utility supply. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, facility electrical system and electrical buildings table. |
| Neutral grounding (secondary 6.9 kV) | Each 6.9 kV transformer shall be grounded using a 100 A, 10 s neutral grounding resistor and shall operate as a tripping system. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraph (6.9 kV neutral grounding resistor). |
| Neutral grounding (0.4 kV tertiary) | `TBD`. DBM does not establish a 0.4 kV grounding basis; the 600 V class uses 5 A continuous high-resistance grounding, but 0.4 kV is a separate, source-unconfirmed voltage class. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraph. |
| Vector group / impedance / tap range / BIL | `TBD`. No accessible source slice defines vector group, impedance, tap range, or basic insulation level for TXP-8300-2. | Source gap; `26020-Package_Requirements.docx` not searched for accessible package-specific match in this run. |
| Cooling class and ambient basis | `TBD`. The 20/26 MVA dual rating implies a stage-cooled design, but cooling-class code (e.g., ONAN/ONAF/KNAN) and ambient design basis are not stated in accessible sources. | Source gap. |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to `PKG-026` and must be represented in the package interface requirements matrix. | Workbook Packages row 28; `INTERFACE_REGISTER.csv` `IFC-E9FC2B952D`. |
| Grounding / Bonding | Interface fact applies to `PKG-026` and must be represented in the package interface requirements matrix. | Workbook Packages row 28; `INTERFACE_REGISTER.csv` `IFC-FE5C9BD828`. |
| Area / Exterior Lighting | Interface fact applies to `PKG-026` and must be represented in the package interface requirements matrix. | Workbook Packages row 28; `INTERFACE_REGISTER.csv` `IFC-0230019D52`. |
| I&C / Control Cabling | Interface fact applies to `PKG-026` and must be represented in the package interface requirements matrix. | Workbook Packages row 28; `INTERFACE_REGISTER.csv` `IFC-25E2CF2BD9`. |
| Communications / Network | Interface fact applies to `PKG-026` and must be represented in the package interface requirements matrix. | Workbook Packages row 28; `INTERFACE_REGISTER.csv` `IFC-E6E0E1FA2B`. |
| Maintenance Access | Interface fact applies to `PKG-026` and must be represented in the package interface requirements matrix. | Workbook Packages row 28; `INTERFACE_REGISTER.csv` `IFC-93877B34D5`. |
| Structural / Foundations / Supports | Interface fact applies to `PKG-026` and must be represented in the package interface requirements matrix. | Workbook Packages row 28; `INTERFACE_REGISTER.csv` `IFC-7DD82CAE51`. |
| CEC spacing | Large oil-filled transformers shall be spaced in accordance with CEC requirements; secondary containment requirements shall be reviewed and selection shall avoid or limit containment requirements where practical. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers paragraph. |
| Grounding design basis | Major electrical equipment shall be directly connected to the ground grid at two points; ground wells at power transformers shall be provided for maintenance/operational testing; CEC-sized separate copper ground conductors for distribution transformers. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs. |
| 6.9 kV medium-voltage cable basis | Three-conductor copper TECK cable rated 8 kV with 100% insulation, shielded. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable types table. |
| 13.8 kV medium-voltage cable basis | Three-conductor copper TECK cable rated 15 kV with 133% insulation, shielded. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable types table. |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-026`. |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-026`. |
| Foundation basis | Transformers are generally supported on precast concrete bearing foundations; the DBM electrical section also notes installation on structural steel transformer bases. Final foundation type for TXP-8300-2 is `TBD` pending detailed civil/structural design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, foundations table and transformers paragraph. |
| Installation location | ASSUMPTION: located adjacent to the 820-1 6.9 kV Inlet/Sales Compressor Electrical Building to supply the 6.9 kV bus. The accessible source set does not explicitly assign TXP-8300-2 to a specific physical pad. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings table. |
| Secondary containment | Secondary containment requirements shall be reviewed; transformer selection shall avoid or limit containment requirements where practical. Final containment requirement for this transformer is `TBD`. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers paragraph. |
| Vendor design data (impedance, losses, sound, tap-changer, cooling controls, monitoring) | `TBD` until vendor package data is issued. | Source gap. |
| Communications / Network and I&C interfaces | Required interface facts per Gate 7 register; specific monitoring (e.g., temperature, gas, tap-position) and protocol bindings are `TBD` pending vendor data and detailed engineering. | `INTERFACE_REGISTER.csv` rows `IFC-25E2CF2BD9`, `IFC-E6E0E1FA2B`. |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-026-02_package-datasheet`.
- `PACKAGE_REGISTER.csv`, row `PKG-026`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-026-02_package-datasheet`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-026` (`IFC-E9FC2B952D`, `IFC-FE5C9BD828`, `IFC-0230019D52`, `IFC-25E2CF2BD9`, `IFC-E6E0E1FA2B`, `IFC-93877B34D5`, `IFC-7DD82CAE51`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-026-02_package-datasheet`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 28.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis source slices for facility electrical system, voltage/service table, transformers, electrical buildings, grounding/bonding, cable basis, and foundations.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical interface context for the 03-25/04-25 facility split (transformer feeders described for the companion 03-25 facility).
- `_Sources/26020-Package_Requirements.docx`, package-specific requirements document (not extracted for this run; clause-level content `TBD`).
