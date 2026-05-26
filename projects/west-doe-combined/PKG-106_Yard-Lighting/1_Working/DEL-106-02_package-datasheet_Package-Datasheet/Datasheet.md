# Datasheet — DEL-106-02 Package Datasheet (Yard Lighting)

> Pass: P1_P2 (four-documents skill, 2026-05-25). Source-grounded against accessible references; missing values are marked `TBD` and inferences are labeled `ASSUMPTION`.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-106-02_package-datasheet` | `_CONTEXT.md` Identity |
| Name | Package Datasheet | `_CONTEXT.md` Identity |
| ParentPackageID | `PKG-106` | `_CONTEXT.md` Identity |
| ParentWorkbookID | 106 | `_CONTEXT.md` Identity |
| PackageName | Yard Lighting | `_CONTEXT.md` Identity; `26020-Packages_Interfaces_4_export.xlsx` row 12 (`Packages` column) |
| CoA Tracking Number | `26020-01-30-001` | `26020-Packages_Interfaces_4_export.xlsx` row 12 (`CoA Tracking Number` column); `PACKAGE_REGISTER.csv` row 12 |
| Discipline | Electrical | `_CONTEXT.md` Identity; `26020-Packages_Interfaces_4_export.xlsx` row 12 (`Discipline` column) |
| WBS | TBD | `PACKAGE_REGISTER.csv` row 12 records `WBS TBD`; `26020-Packages_Interfaces_4_export.xlsx` row 12 WBS cell empty |
| Type | EPC Package Datasheet | `_CONTEXT.md` Identity; `DELIVERABLE_REGISTER.csv` row 43 |
| ResponsibleParty | EPC Integrator | `_CONTEXT.md` Identity; `DELIVERABLE_REGISTER.csv` row 43 |
| PackageOwner (engineering/design/equipment) | Package Vendor | `PACKAGE_REGISTER.csv` row 12 Responsibility model |
| Source Reference (row of record) | Workbook Packages row 12 | `_CONTEXT.md`; `26020-Packages_Interfaces_4_export.xlsx` row 12 |
| Source basis document | `26020-Packages_Interfaces_4_export.xlsx` (workbook); discipline basis: `DBM-Deepcut/4-25_Deepcut_DBM.md` and `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-12 Electrical Basis | `_REFERENCES.md`; OBJECTIVE_REGISTER.csv OBJ-005 derived-source-intent |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package function (declared) | Provide facility yard/area exterior lighting infrastructure for the West Doe combined facility, integrated into the discipline Electrical scope and supplied as a vendor-owned package with EPC Integrator facility integration. | ASSUMPTION (declared package identity from `PACKAGE_REGISTER.csv` row 12; per-package narrative for "Yard Lighting" is NOT present in `26020-Package_Requirements.docx`) |
| Light source technology | LED type for all lighting (general purpose, process area, outdoor); LED for outdoor/process area lighting | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Lighting and Receptacles (lines 3029, 3031); `DBM-Deepcut/4-25_Deepcut_DBM.md` §Energy and Emissions Design Considerations (line 2183) |
| Lighting supply voltage (general) | 120/208 V, 3 phase, 4 wire, 60 Hz, solidly grounded — serves lighting, receptacles, EHT, small motors, UPS ≤10 kVA | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Power System (line 2938); `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §System Voltages (line 735) |
| Upstream LV source feeding lighting distribution | 600 V, 3-phase, 3-wire, 60 Hz, HRG (5 A continuous resistor); 600 V → 208/120 V distribution transformer with solidly grounded neutral feeding each 208/120 V distribution panelboard | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Power System (lines 2937, 2967); `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §System Voltages (line 734) |
| Emergency / critical lighting source | UPS services 120 VAC / 125 VDC for "selected emergency or critical lighting" | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Power System (line 2939); `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §System Voltages (line 736) |
| Photometric levels / illuminance targets | TBD (not stated in accessible sources) | location TBD |
| Pole heights / mast specifications | TBD specific dimensions; mast poles to be located away from pad edge where required | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Lighting and Receptacles (line 3035) |
| Light-pollution control measures | LED lighting; selective minimization of exterior lighting to working areas; downcast floodlights; prohibition of horizontally aimed floodlights; photocell or switch control to minimize emissions; lighting mast poles located away from pad edge where required | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Lighting and Receptacles (line 3035) |
| Area classification suitability | Fixtures shall be suitable for the area classification in which they are installed | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Lighting and Receptacles (line 3029) |
| Tagged equipment list | TBD (no per-tag list available for Yard Lighting in `26020-Package_Requirements.docx`; workbook row 12 carries package identity but no tagged equipment table) | location TBD |
| Quantity of fixtures / mast count | TBD | location TBD |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service environment | Outdoor / exterior yard; cold-climate site (cable tray rated for -40 °C in facility electrical basis) | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Cable, Wire, and Raceways (line 3001) — applied to facility cabling; ASSUMPTION applied to yard lighting environment |
| Area classification | Mixed hazardous and non-hazardous outdoor yard areas as established by the facility electrical classification drawings | ASSUMPTION (general facility basis; specific area classifications for yard lighting fixtures are TBD) |
| Operating temperature range | TBD; site climate per DBM but specific fixture rating range not stated | location TBD |
| Control method | Photocell or switch control to minimize emissions (for exterior lighting addressing light-pollution requirements) | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Lighting and Receptacles (line 3035) |

## Construction

| Item | Value | Source |
|---|---|---|
| Light fixture type | LED, outdoor/process-area rated, suitable for area classification | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Lighting and Receptacles (lines 3029, 3031) |
| Fixture supply circuit conductors | Lighting conductors from distribution panelboards selected not larger than #10 AWG wherever possible by locating RDCs closer to lighting loads | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Cable, Wire, and Raceways (line 3001) |
| Wiring method (yard / outdoor) | Tray cable: armored (TECK 90, ACWU, or ACIC); aluminum interlocking armor; HL rated; -40 °C rated; copper conductors ≤ #1/0 AWG (aluminum ACWU for larger) | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Cable, Wire, and Raceways (line 3001) |
| Conduit method (where applicable) | Rigid conduit for building lighting where shop-fabricated; EMT in non-process buildings only; minimum 21 mm (3/4 in); sealed at area-classification boundaries; CEC and area-classification compliant | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Cable, Wire, and Raceways (line 3025) |
| Receptacle / lighting circuit segregation | Receptacle circuits shall not be mixed with lighting circuits | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Lighting and Receptacles (line 3033) |
| Shared common neutrals | To be avoided where possible | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Lighting and Receptacles (line 3029) |
| Grounding / bonding | Per facility grounding/bonding interface (declared at workbook row 12) | `26020-Packages_Interfaces_4_export.xlsx` row 12 (Grounding/Bonding = X); `INTERFACE_REGISTER.csv` IFC-DA0D60681B |
| Mast pole construction | TBD specific structural details; pad-edge setback per DBM | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Lighting and Receptacles (line 3035); rest location TBD |

## Interface Summary (carried as datasheet evidence per `_CONTEXT.md` note)

| Interface Type | Applicability | Source | Interface ID |
|---|---|---|---|
| Electrical Power | YES | `26020-Packages_Interfaces_4_export.xlsx` row 12 (col Electrical Power = X) | `IFC-6FCF1B30D6` (`INTERFACE_REGISTER.csv` row 40) |
| Grounding / Bonding | YES | `26020-Packages_Interfaces_4_export.xlsx` row 12 (col Grounding / Bonding = X) | `IFC-DA0D60681B` (`INTERFACE_REGISTER.csv` row 41) |
| Area / Exterior Lighting | YES | `26020-Packages_Interfaces_4_export.xlsx` row 12 (col Area / Exterior Lighting = X) | `IFC-ED86F51087` (`INTERFACE_REGISTER.csv` row 42) |
| All other interface types in `26020-Packages_Interfaces_4_export.xlsx` columns (Process Piping, Utility Piping, Relief/Flare/Vent, Drain/Containment, EHT, Cathodic Protection, I&C/Control Cabling, Communications/Network, Building HVAC, Fire & Gas, Maintenance Access, Grading/Drainage, Structural/Foundations, Product Loading, Pipeline/Pigging) | NOT marked applicable for row 12 | `26020-Packages_Interfaces_4_export.xlsx` row 12 (cells empty) | n/a |

## References

- `_CONTEXT.md` — deliverable identity, scope, anticipated artifacts, covered scope items, supported objectives.
- `_REFERENCES.md` — authority hierarchy and reference register.
- `_DEPENDENCIES.md` — no declared upstream/downstream at PREPARATION.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx` — workbook row 12 (Yard Lighting).
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Package_Requirements.docx` — no per-package row for Yard Lighting (verified by full-text scan); recorded as gap.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — §Lighting and Receptacles (lines 3027-3035); §Power System (lines 2937-2967); §Cable, Wire, and Raceways (lines 2997-3025); §Energy and Emissions (line 2183); §Discipline Scope (line 2860).
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — §Electrical Design Basis (line 718); §System Voltages (lines 734-736); §Electrical Buildings, Raceways, Lighting, and Heat Tracing (lines 764-770).
- GATE-07 snapshot registers: `DELIVERABLE_REGISTER.csv` row 43; `PACKAGE_REGISTER.csv` row 12; `INTERFACE_REGISTER.csv` rows 40-42; `ARTIFACT_REGISTER.csv` rows 167-172; `OBJECTIVE_REGISTER.csv` rows for OBJ-001/004/005/009/010.
