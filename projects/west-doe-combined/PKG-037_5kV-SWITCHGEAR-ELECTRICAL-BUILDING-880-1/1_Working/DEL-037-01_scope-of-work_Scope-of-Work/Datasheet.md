# Datasheet: DEL-037-01_scope-of-work — Scope of Work

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-037-01_scope-of-work` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Deliverable name | Scope of Work | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-037` — 5kV SWITCHGEAR ELECTRICAL BUILDING (880-1) | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 37 / row 39 | Workbook Packages row 39; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 39; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-028 | Workbook Packages row 39; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 39; `_CONTEXT.md` |
| Deliverable type | EPC Scope of Work | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Scope item covered | `SOW-0038` | `_CONTEXT.md`; `SCOPE_LEDGER.csv` |
| Supported objectives | `OBJ-001; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010` | `OBJECTIVE_DELIVERABLE_MAP.csv` rows for `DEL-037-01_scope-of-work` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-037` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package class | Vendor-owned Electrical package; EPC-integrated electrical building production unit | `PACKAGE_REGISTER.csv` row `PKG-037` |
| Package function | 5kV switchgear electrical building, designated 880-1 in the package name; intended to house medium-voltage switchgear and associated electrical building equipment as determined by detailed design. | Workbook Packages row 39; `PACKAGE_REGISTER.csv` row `PKG-037` |
| Building identity (880-1) | The "880-1" suffix is the package-defined building tag for this electrical building. The accessible Deepcut DBM building list (Section "Building Designations") enumerates 810-1, 820-1, 830-1, 840-1, 850-1, 860-1, and 800-1 but does NOT list an 880-1 building. The 880-1 tag is therefore carried from the workbook package name with `location TBD` in accessible source. | Workbook Packages row 39; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, building designations table |
| Voltage class basis | The accessible Electrical Basis system-voltages table lists 13.8 kV, 6.9 kV, 4.160 kV, 600 V, 208/120 V, and 120 VAC/125 VDC services. A 5 kV medium-voltage service class is not listed. The 5 kV designator appears in the cable basis as the insulation rating for 4.160 kV medium-voltage cable. ASSUMPTION: "5kV switchgear" in the package name refers to 5 kV class metal-clad switchgear typically used to feed 4.16 kV bus equipment; package-specific bus voltage and rating require human ruling. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 system voltages table and medium-voltage cable table |
| Electrical building basis | Electrical buildings shall be prefabricated, modular buildings located in general purpose areas. They shall house, as required by detailed design, medium-voltage switchgear, motor control centers, soft starters, VFDs, 600 V MCCs, 120 V AC UPS systems, 125 V DC UPS systems, distribution transformers, panelboards, contactor panels, plant PLC control panels, and network racks. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Electrical Buildings" subsection of SEC-12 |
| HVAC basis | Electrical buildings shall be climate controlled with HVAC sized as n + 1. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Electrical Buildings" subsection of SEC-12 |
| Cable entry / elevation basis | Electrical buildings shall be designed for bottom entry of incoming and outgoing power cables and shall be elevated on piles to allow cable trays beneath the building. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Electrical Buildings" subsection of SEC-12 |
| Wiring basis | Electrical buildings shall be wired with TECK and ACIC cables. EMT conduit shall be used for adjacent panel-to-panel interconnections. An outdoor GFI receptacle shall be provided for exterior maintenance. Equipment doors or removable transoms shall accommodate removal of the largest equipment. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Electrical Buildings" subsection of SEC-12 |
| Tagged equipment list | TBD. No package-specific tagged equipment is identified in the accessible Gate 7 artifact rows for `DEL-037-01_scope-of-work` beyond the four scope-of-work artifacts (`ART-53C9B45AD0`, `ART-CD3C1783C4`, `ART-1DFABB8A68`, `ART-833F44316B`). The accessible DBM building list does not enumerate the 880-1 building. | `ARTIFACT_REGISTER.csv` rows for `DEL-037-01_scope-of-work`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, building designations table |
| Package-specific exclusions | TBD; no package-specific exclusions are stated in source materials. | `PACKAGE_REGISTER.csv` row `PKG-037` |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Utility Piping | Interface fact applies to PKG-037 and must be represented in the package scope-of-work integration narrative. | `INTERFACE_REGISTER.csv` `IFC-524BC4670F` |
| Drain / Containment | Interface fact applies to PKG-037 and must be represented in the package scope-of-work integration narrative. | `INTERFACE_REGISTER.csv` `IFC-A8DC0D3056` |
| Electrical Power | Interface fact applies to PKG-037 and must be represented in the package scope-of-work integration narrative. | `INTERFACE_REGISTER.csv` `IFC-35A170DE7F` |
| Grounding / Bonding | Interface fact applies to PKG-037 and must be represented in the package scope-of-work integration narrative. | `INTERFACE_REGISTER.csv` `IFC-E26DA604FB` |
| Area / Exterior Lighting | Interface fact applies to PKG-037 and must be represented in the package scope-of-work integration narrative. | `INTERFACE_REGISTER.csv` `IFC-8F0D1E29F1` |
| I&C / Control Cabling | Interface fact applies to PKG-037 and must be represented in the package scope-of-work integration narrative. | `INTERFACE_REGISTER.csv` `IFC-F5B78B59CE` |
| Communications / Network | Interface fact applies to PKG-037 and must be represented in the package scope-of-work integration narrative. | `INTERFACE_REGISTER.csv` `IFC-1ECBDB6397` |
| Building HVAC / Services | Interface fact applies to PKG-037 and must be represented in the package scope-of-work integration narrative. | `INTERFACE_REGISTER.csv` `IFC-D6D4CB07AF` |
| Fire & Gas / Safety Systems | Interface fact applies to PKG-037 and must be represented in the package scope-of-work integration narrative. | `INTERFACE_REGISTER.csv` `IFC-4D8A22B2CA` |
| Maintenance Access | Interface fact applies to PKG-037 and must be represented in the package scope-of-work integration narrative. | `INTERFACE_REGISTER.csv` `IFC-CE2AC83D1D` |
| Grading / Site Drainage / Spill Containment | Interface fact applies to PKG-037 and must be represented in the package scope-of-work integration narrative. | `INTERFACE_REGISTER.csv` `IFC-65DF6F2E88` |
| Structural / Foundations / Supports | Interface fact applies to PKG-037 and must be represented in the package scope-of-work integration narrative. | `INTERFACE_REGISTER.csv` `IFC-8012069CE2` |
| Area classification | Electrical buildings shall be located in general purpose areas for convenient power distribution. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, area classification paragraph in SEC-12 |
| Grounding design basis | All major electrical equipment shall be directly connected to the ground grid at two points; ground wells at electrical buildings shall be provided for maintenance and operational testing. Detailed grounding-resistor configuration depends on transformer voltage class. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Grounding and Bonding" subsection of SEC-12 |
| Cable / conduit routing | Cable tray and conduit routing shall not interfere with maintenance access; main pipe-rack cable trays are pre-installed in the shop and field tray is limited. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs of SEC-12 |

## Construction

| Item | Value | Source |
|---|---|---|
| Scope-of-work deliverable contents | Package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record. | `DELIVERABLE_REGISTER.csv` row `DEL-037-01_scope-of-work`; `ARTIFACT_REGISTER.csv` rows `ART-53C9B45AD0`, `ART-CD3C1783C4`, `ART-1DFABB8A68`, `ART-833F44316B` |
| Boundaries to define | Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Building HVAC / Services, Fire & Gas / Safety Systems, Utility Piping, Drain / Containment, Maintenance Access, Grading / Site Drainage / Spill Containment, Structural / Foundations / Supports interfaces between PKG-037 and the EPC-integrated facility. | `PACKAGE_REGISTER.csv` row `PKG-037`; `INTERFACE_REGISTER.csv` rows for `PKG-037` |
| Package engineering and physical equipment | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-037` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-037` |
| Installation location | TBD. Accessible building designations table does not list an 880-1 electrical building; site location, area assignment, and adjacent process modules require detailed design or human ruling. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, building designations table |
| Tagged equipment for 880-1 | TBD. The Deepcut equipment list does not associate specific switchgear or auxiliary equipment tags to an 880-1 building. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, equipment list and building designations table |
| Bus voltage and switchgear rating | TBD pending human ruling on "5kV switchgear" interpretation; accessible source enumerates 13.8 kV, 6.9 kV, and 4.160 kV medium-voltage services but not a 5 kV service. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 system-voltages table |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `_DEPENDENCIES.md`, declared upstream/downstream lists (none declared).
- `DELIVERABLE_REGISTER.csv`, row `DEL-037-01_scope-of-work`.
- `PACKAGE_REGISTER.csv`, row `PKG-037`.
- `SCOPE_LEDGER.csv`, row `SOW-0038`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-037-01_scope-of-work`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-037`.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-037-01_scope-of-work`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 39.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 Electrical Basis (system voltages, electrical buildings, grounding and bonding, cable tray and conduit, area classification, building designations).
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific PKG-037 / 880-1 / 5 kV switchgear content; no PKG-037-specific package match was located in accessible material.
