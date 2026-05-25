# Datasheet: DEL-030-04_vendor-engineered-equipment-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-030-04_vendor-engineered-equipment-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Engineered Equipment Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-030` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | Transformer TXP-8200-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V | Workbook Packages row 32; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 30 / row 32 | Workbook Packages row 32; `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` row `PKG-030` |
| CoA tracking number | 26020-01-30-021 | `PACKAGE_REGISTER.csv` row `PKG-030` |
| Discipline | Electrical | Workbook Packages row 32; `_CONTEXT.md` |
| Deliverable type | Vendor Package Production Unit | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-030` |
| Covered Scope of Work item | `SOW-0031` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Supported objectives | `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-008`, `OBJ-009`, `OBJ-010` (ASSUMPTION: package-grouping heuristic, `OBJECTIVE_DELIVERABLE_MAP.csv` confirms explicit DEL-030-04 rows) | `OBJECTIVE_DELIVERABLE_MAP.csv` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-030` |
| Package function | Step-down distribution transformer package, nameplate 2.5 MVA, 13.8 kV / 600 V / 347 V class. | Workbook Packages row 32; `PACKAGE_REGISTER.csv` row `PKG-030` |
| Vendor-engineered scope | Engineering, design, fabrication/supply, and the physical equipment package developed from the EPC package Scope of Work and Package Datasheet. | `DELIVERABLE_REGISTER.csv` row `DEL-030-04`; `_CONTEXT.md` |
| Primary system voltage (incoming) | 13.8 kV, 3-phase, 3-wire, 60 Hz, low-resistance grounded medium-voltage service. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical voltages and services table |
| Low-voltage secondary basis | 600 V, 3-phase, 3-wire, 60 Hz, high-resistance grounded with 5 A continuous resistor (facility low-voltage service basis for 04-25). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical voltages and services table |
| 347 V derivation | TBD. The workbook package name carries "600/347V"; the accessible DBM source supports 600 V LV service but does not establish a 347 V derivation specific to this transformer (347 V is the 600 V phase-to-neutral value where a neutral is brought out; no source slice confirms a 4-wire secondary configuration for this unit). | Workbook Packages row 32; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| 13.8 kV → 600 V step-down role | The 13.8 kV switchgear distributes radially through step-down transformers to facility electrical buildings and loads; 13.8 kV → 600 V transformers feed plant 600 V MCCs. Allocation of this specific unit to a specific electrical building/MCC is `TBD`. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical distribution narrative and cable types table |
| Transformer class / construction | Oil-filled transformer construction is the source-supported general basis for large facility transformers; final selection (oil-filled vs. dry-type, secondary containment requirements, enclosure) is vendor-engineered per CEC spacing and project requirements. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers paragraph (CEC spacing and structural-steel bases; oil-filled identified in equipment list) |
| Quantity | TBD. The 04-25 equipment list identifies "Oil-Filled Transformers" quantity 2 in aggregate; the allocation to `PKG-030` is not separately confirmed by an accessible package-specific source slice. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, equipment list |
| Neutral grounding (HV side) | Each 600 V transformer secondary shall be grounded by a 5 A continuous high-resistance grounding resistor per facility electrical design basis (applicable to the secondary of this 13.8 kV / 600 V unit). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs |
| Mounting basis | Generally supported on precast concrete bearing foundations and/or structural-steel transformer bases per facility civil/structural basis; vendor base details `TBD`. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers and structural paragraphs |

## Conditions

| Interface / condition | Datasheet basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to `PKG-030`; vendor package shall conform to the EPC interface requirements matrix. | Workbook Packages row 32; `INTERFACE_REGISTER.csv` `IFC-009C48E7FF` |
| Grounding / Bonding | Interface fact applies; bonding to facility ground grid is required at two points for major electrical equipment; separate copper ground conductor required for distribution transformers per CEC sizing. | `INTERFACE_REGISTER.csv` `IFC-6C663BF69D`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs |
| Area / Exterior Lighting | Interface fact applies; vendor package shall coordinate exterior/area lighting requirements at the transformer pad/yard with EPC. Package-specific lighting details `TBD`. | `INTERFACE_REGISTER.csv` `IFC-0B28AED229` |
| I&C / Control Cabling | Interface fact applies; vendor shall provide transformer monitoring/protection signal interface (e.g., winding/oil temperature, gas/pressure, sudden-pressure, where applicable). Specific signal list `TBD`. | `INTERFACE_REGISTER.csv` `IFC-D000451C37` |
| Communications / Network | Interface fact applies; communications/network requirements (e.g., to MV protective relay or facility SCADA) are coordinated by EPC. Package-specific protocol/port assignments `TBD`. | `INTERFACE_REGISTER.csv` `IFC-9EF13A0FC1` |
| Maintenance Access | Interface fact applies; cable tray and conduit routing shall not interfere with maintenance access to the transformer (including bushing/tap-changer access where applicable). | `INTERFACE_REGISTER.csv` `IFC-345609CB34`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs |
| Structural / Foundations / Supports | Interface fact applies; vendor package shall coordinate foundation and support requirements with EPC civil/structural. Generally precast concrete bearing foundations and/or structural-steel transformer bases. | `INTERFACE_REGISTER.csv` `IFC-4B50D76AF1`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers paragraph |
| CEC spacing (oil-filled) | Large oil-filled transformers shall be spaced in accordance with CEC requirements; secondary containment requirements shall be reviewed and minimized where practical. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers paragraph |
| MV cable basis | 13.8 kV feed shall be three-conductor copper TECK cable rated 15 kV with 133 % insulation, shielded (facility MV cable basis). Cable termination and bushing arrangement at the transformer are vendor-engineered. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable types table |
| Secondary connection basis | 600 V transformer secondary to plant 600 V MCC shall be ACWU; single-conductor cables avoided. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable types table |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering, design, fabrication/supply, physical package | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-030`; `DELIVERABLE_REGISTER.csv` row `DEL-030-04` |
| Facility integration, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility (integration review). | `PACKAGE_REGISTER.csv` row `PKG-030`; `DELIVERABLE_REGISTER.csv` row `DEL-030-04` |
| Installation location | TBD. The DBM identifies electrical buildings and 13.8 kV switchgear distribution but does not assign `PKG-030` to a specific building/skid/yard pad. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| Foundation / supports | Generally precast concrete bearing foundations and/or structural-steel transformer bases; package-specific support detail is vendor-engineered. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers and structural-foundations paragraphs |
| Containment / spill control | Secondary containment shall be reviewed and transformer selection shall avoid or limit containment requirements where practical. Package-specific containment provision `TBD`. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers paragraph |
| Test and inspection scope | Factory/shop test and inspection evidence is an expected vendor-side artifact; specific test list `TBD` pending vendor specification or detailed engineering. | `ARTIFACT_REGISTER.csv` rows for `DEL-030-06` (Factory/shop test and inspection evidence) — referenced for EPC acceptance basis; vendor-side test list itself `TBD` |
| Vendor design basis and datasheet set | Vendor package design basis and datasheet set are anticipated artifacts; detailed content is `TBD` until vendor data is issued. | `ARTIFACT_REGISTER.csv` row `ART-0A27405282`; `DELIVERABLE_REGISTER.csv` row `DEL-030-04` |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `_DEPENDENCIES.md`, declared dependency view (no declared edges at PREPARATION).
- `DELIVERABLE_REGISTER.csv`, row `DEL-030-04_vendor-engineered-equipment-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-030`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-030-04_vendor-engineered-equipment-package` (`ART-69E26F40CD`, `ART-0A27405282`).
- `INTERFACE_REGISTER.csv`, rows for `PKG-030` (`IFC-009C48E7FF`, `IFC-6C663BF69D`, `IFC-0B28AED229`, `IFC-D000451C37`, `IFC-9EF13A0FC1`, `IFC-345609CB34`, `IFC-4B50D76AF1`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-030-04_vendor-engineered-equipment-package`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 32.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical voltages/services, transformers, grounding/bonding, cable types, electrical buildings, and structural/foundations source slices.
- `_Sources/26020-Package_Requirements.docx`, searched for `PKG-030`-specific vendor requirements; no `PKG-030` package-specific match was confirmed during this run.
