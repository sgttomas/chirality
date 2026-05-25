# Datasheet: DEL-030-03_construction-work-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-030-03_construction-work-package` | `_CONTEXT.md` |
| Deliverable name | Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-030` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | Transformer TXP-8200-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V | Workbook Packages row 32; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 30 / row 32 | Workbook Packages row 32; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 32; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-021 | Workbook Packages row 32; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 32; `_CONTEXT.md` |
| Deliverable type | EPC Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-030` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package; EPC Integrator owns construction/integration of the package into the facility | `PACKAGE_REGISTER.csv` row `PKG-030` |
| Package function | Step-down distribution transformer rated 2.5 MVA, primary 13.8 kV to secondary 600/347 V, fed from the facility 13.8 kV switchgear bus and feeding the plant 600 V distribution system | Workbook Packages row 32; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical power distribution section (13.8 kV switchgear distributes radially through step-down transformers; 600 V low-voltage services) |
| Construction responsibility | Tourmaline Oil Corporation field construction scope per DBM Construction Responsibility section; activities include grading/piling/foundation work, setting modules and equipment on foundations, mechanical hookup, installation of shipped-loose components, structural supports, home-run cable installation, electrical terminations, and area lighting. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility section |
| Tie-in coordination | Joint planning required for tie-ins to existing or related facilities; tie-in timing established as project progresses. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility / tie-in paragraph |
| Foundation basis | Transformers generally supported on precast concrete bearing foundations; large oil-filled transformers spaced per CEC requirements and generally installed on structural steel transformer bases. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, foundation and Transformers paragraphs |
| Secondary containment | Secondary containment requirements shall be reviewed; transformer selection shall avoid or limit containment where practical. Package-specific containment configuration is `TBD`. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Transformers paragraph |
| Secondary-system grounding | 600 V transformer secondary shall be grounded by a 5 A continuous high-resistance grounding resistor; 600 V services are high-resistance grounded with a 5 A continuous resistor. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, low-voltage services row and neutral grounding resistor paragraph |
| Installation location (electrical building / outdoor pad) | `TBD`. The DBM identifies electrical buildings as housing for MV switchgear and related equipment but does not assign PKG-030 transformer to a specific building, pad, or outdoor location. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| Module/skid lift, set, and shipping basis | `TBD`. Vendor package lift plan, shipping configuration, off-loading sequence, and rigging details are vendor-package outputs not yet available in the source set. | Source gap; vendor engineered package (`DEL-030-04`) not yet produced |
| Turnover and handover basis | `TBD`. Construction interface and turnover checklist artifact required; detailed turnover acceptance criteria depend on vendor package documents and facility electrical commissioning plan. | `ARTIFACT_REGISTER.csv` row `ART-E6DA4BF5C2`; source gap on vendor turnover content |

## Conditions

| Interface / condition | Construction-package basis | Source |
|---|---|---|
| Electrical Power | Construction work package shall plan and execute installation/termination of 13.8 kV primary and 600/347 V secondary connections from the facility power distribution system to the transformer, consistent with the DBM medium-voltage and 600 V cable schedule basis. | Workbook Packages row 32; `INTERFACE_REGISTER.csv` `IFC-009C48E7FF`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical power distribution and cable schedule sections |
| Grounding / Bonding | Construction shall implement two-point ground-grid connection for major electrical equipment, separate copper ground conductor sized per CEC for distribution transformers, ground wells at power transformers, bolted/compression ground connections, and the DBM-specified 5 A continuous high-resistance grounding resistor on the 600 V secondary; package-specific conductor sizing and routing shall be confirmed by detailed design. | Workbook Packages row 32; `INTERFACE_REGISTER.csv` `IFC-6C663BF69D`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs |
| Area / Exterior Lighting | Construction work package shall include area lighting (Tourmaline field construction scope) coordinated with the transformer pad/electrical-building location and maintenance access. | Workbook Packages row 32; `INTERFACE_REGISTER.csv` `IFC-0B28AED229`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility section |
| I&C / Control Cabling | Construction work package shall include installation and termination of transformer protection, monitoring, and control cabling routed in plant cable tray and conduit; cable type/sizing per DBM cable schedule basis; detailed terminations `TBD` pending vendor package data. | Workbook Packages row 32; `INTERFACE_REGISTER.csv` `IFC-D000451C37`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit / cable schedule sections |
| Communications / Network | Construction work package shall include any network/communications cabling required for transformer monitoring or protective-relay integration into the plant control/monitoring network; package-specific scope `TBD` pending vendor data. | Workbook Packages row 32; `INTERFACE_REGISTER.csv` `IFC-9EF13A0FC1` |
| Maintenance Access | Cable tray, conduit routing, and physical placement shall not interfere with maintenance access to the transformer (oil sampling, tap-changer access, bushing access, cooling-system access). Detailed clearances `TBD`. | Workbook Packages row 32; `INTERFACE_REGISTER.csv` `IFC-345609CB34`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs |
| Structural / Foundations / Supports | Foundation and support design per DBM foundation basis (precast concrete bearing foundations / structural steel transformer base, CEC spacing for oil-filled transformers); execution by Tourmaline field construction scope; package-specific loads `TBD` pending vendor data. | Workbook Packages row 32; `INTERFACE_REGISTER.csv` `IFC-4B50D76AF1`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, foundation and Transformers paragraphs |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Construction execution party | Tourmaline Oil Corporation field construction scope for grading/piling/foundations, setting modules and equipment on foundations, mechanical hookup, installation of shipped-loose components, structural supports, home-run cable installation, electrical terminations, and area lighting. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility section |
| EPC Integrator scope | Facility integration, tie-ins, constructability, procurement/construction coordination, and facility-level integration for the package. | `PACKAGE_REGISTER.csv` row `PKG-030` |
| Package Vendor scope | Package engineering, package design, vendor documentation, and the physical equipment package — not facility construction. | `PACKAGE_REGISTER.csv` row `PKG-030` |
| Workface planning artifact | Installation and tie-in workface plan covering process, utility, electrical, controls, civil, structural, and safety systems as applicable to a transformer package. | `ARTIFACT_REGISTER.csv` row `ART-370E7F8537` |
| Construction interface and turnover artifact | Construction-facing interface, tie-in, inspection, and turnover checklist evidence for the approved package. | `ARTIFACT_REGISTER.csv` row `ART-E6DA4BF5C2` |
| Tie-in timing | Established as project progresses; joint planning required for tie-ins to existing or related facilities. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility / tie-in paragraph |
| Transformer rating used in planning | 2.5 MVA, 13.8 kV primary, 600/347 V secondary (carried from package title). Detailed nameplate values, BIL, impedance, cooling class, tap configuration, oil volume, and weights are `TBD` pending vendor data. | Workbook Packages row 32; source gap pending `DEL-030-04` vendor outputs |
| Primary cable schedule basis | 13.8 kV three-conductor copper TECK rated 15 kV with 133 percent insulation, shielded, per DBM cable schedule. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable schedule, 13.8 kV row |
| Secondary cable schedule basis | 600 V transformer secondary to plant 600 V MCCs shall use ACWU cable; single-conductor cables avoided. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable schedule, 600 V transformer-secondary row |
| Pre-commissioning / energization | `TBD`. Insulation testing, oil testing, protective-relay testing, ground continuity testing, and energization sequence are typical for an oil-filled MV transformer but are not specified by an accessible source slice for PKG-030. Detailed steps and acceptance values shall be established during detailed engineering and vendor coordination. | Source gap; not derived from decomposition prose |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-030-03_construction-work-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-030`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-030-03_construction-work-package` (`ART-8A966A4CD7`, `ART-370E7F8537`, `ART-E6DA4BF5C2`).
- `INTERFACE_REGISTER.csv`, rows for `PKG-030` (`IFC-009C48E7FF`, `IFC-6C663BF69D`, `IFC-0B28AED229`, `IFC-D000451C37`, `IFC-9EF13A0FC1`, `IFC-345609CB34`, `IFC-4B50D76AF1`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-030-03_construction-work-package` (OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 32.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility, foundation basis, Transformers, electrical power distribution, low-voltage services, cable schedule (13.8 kV and 600 V transformer-secondary rows), grounding and bonding, neutral grounding resistor, cable tray, and conduit source slices.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific transformer-construction content; no source slice locally accessible for PKG-030 construction execution detail (recorded as `TBD`/`location TBD`).
