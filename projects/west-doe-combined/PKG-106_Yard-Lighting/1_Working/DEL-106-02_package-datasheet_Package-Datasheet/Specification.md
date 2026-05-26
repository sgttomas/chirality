# Specification — DEL-106-02 Package Datasheet (Yard Lighting)

> Pass: P1_P2 (four-documents skill, 2026-05-25). Requirements derived only from accessible sources; inferred requirements are labeled `ASSUMPTION`; missing values are marked `TBD`.

## Scope

This Specification governs the EPC-Integrator-authored Package Datasheet deliverable (`DEL-106-02_package-datasheet`) for `PKG-106 Yard Lighting`. It defines the package technical handoff data required for third-party (Package Vendor) engineering and design of the yard / area exterior lighting equipment package, the interface-fact evidence carried with the Datasheet, and the verification approaches the EPC Integrator will use against the resulting vendor submissions.

**In scope of this Datasheet deliverable:**

- Package technical datasheet for the Yard Lighting package (artifact `ART-AE8A9D9DB8`).
- Vendor engineering handoff basis (artifact `ART-9E11FA7FB5`).
- Package interface requirements matrix carrying workbook interface facts (artifact `ART-51069C3B2D`).
- Interface-fact evidence for Electrical Power, Grounding/Bonding, and Area/Exterior Lighting (artifacts `ART-B670C2963F`, `ART-0686DF8D13`, `ART-9F2D1E8063`).

Source: `ARTIFACT_REGISTER.csv` rows 167-172.

**Out of scope of this Datasheet deliverable** (handled by sibling deliverables in `PKG-106`):

- Scope of Work, integration narrative, tagged equipment identity → `DEL-106-01_scope-of-work`.
- Construction work package, installation/tie-in workface plan → `DEL-106-03_construction-work-package`.
- Vendor engineering, design, fabrication, and physical supply → `DEL-106-04_vendor-engineered-equipment-package`.
- Vendor document register, submittals, and turnover records → `DEL-106-05_vendor-document-turnover-package`.
- EPC vendor package review and acceptance → `DEL-106-06_epc-vendor-package-review-and-acceptance`.

Source: `DELIVERABLE_REGISTER.csv` rows 42-47.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| REQ-106-02-001 | The Package Datasheet shall identify the package as `PKG-106 Yard Lighting`, discipline Electrical, CoA tracking `26020-01-30-001`, source-of-record Workbook Packages row 12. | `26020-Packages_Interfaces_4_export.xlsx` row 12; `PACKAGE_REGISTER.csv` row 12. |
| REQ-106-02-002 | The Datasheet shall state EPC Integrator as the deliverable Responsible Party and Package Vendor as the engineering/design/equipment owner; EPC Integrator is responsible for facility-level integration and interfaces. | `PACKAGE_REGISTER.csv` row 12 Responsibility model; `DELIVERABLE_REGISTER.csv` row 43; `OBJECTIVE_REGISTER.csv` OBJ-004. |
| REQ-106-02-003 | All package lighting shall be LED type. | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Lighting and Receptacles (line 3029). |
| REQ-106-02-004 | Process area and outdoor (yard) lighting shall use LED fixtures. | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Lighting and Receptacles (line 3031). |
| REQ-106-02-005 | Fixtures shall be suitable for the area classification in which they are installed. | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Lighting and Receptacles (line 3029). |
| REQ-106-02-006 | Regulatory light-pollution requirements shall be addressed by: LED lighting; selective minimization of exterior lighting to working areas; downward illumination such as downcast floodlights; prohibition of horizontally aimed floodlights; photocell or switch control to minimize emissions; and locating lighting mast poles away from the pad edge where mast poles are required. | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Lighting and Receptacles (line 3035). |
| REQ-106-02-007 | General-purpose lighting shall be supplied at 120/208 V, 3-phase, 4-wire, 60 Hz, solidly grounded, fed from the nearest 208/120 V distribution panelboard sourced via a 600 V → 208/120 V distribution transformer with solidly grounded neutral. | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Power System (lines 2938, 2967); `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §System Voltages (line 735). |
| REQ-106-02-008 | Emergency / critical lighting (where required by building code or facility basis) shall be supplied from 120 VAC UPS sources with battery backup; at least two emergency lighting fixtures shall be provided in each building for power outage conditions. ASSUMPTION: yard package interpretation limited to building-mounted yard fixtures where co-located buildings exist; pure exterior pole/mast emergency-light requirement not stated. | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Lighting and Receptacles (line 3031); §Power System (line 2939). |
| REQ-106-02-009 | Receptacle circuits shall not be mixed with lighting circuits; shared common neutrals shall be avoided where possible. | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Lighting and Receptacles (lines 3029, 3033). |
| REQ-106-02-010 | Lighting conductors from distribution panelboards shall be selected not larger than #10 AWG wherever possible by locating remote distribution centres (RDCs) closer to lighting loads. | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Cable, Wire, and Raceways (line 3001). |
| REQ-106-02-011 | Outdoor / yard cable installed in tray shall be armored cable type (TECK 90, ACWU, or ACIC) with aluminum interlocking armor, HL rated, and rated for -40 °C; copper conductors up to #1/0 AWG; ACWU aluminum for larger sizes. | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Cable, Wire, and Raceways (line 3001). |
| REQ-106-02-012 | Conduit (where used) shall be rigid for shop-fabricated building lighting; minimum 21 mm (3/4 in); sealed at area-classification boundaries; complete conduit systems shall comply with the Canadian Electrical Code and applicable area classification. EMT shall not be used outdoors / in process areas. | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Cable, Wire, and Raceways (line 3025). |
| REQ-106-02-013 | The Datasheet shall carry as evidence the package interface facts for `Electrical Power` (`IFC-6FCF1B30D6`), `Grounding / Bonding` (`IFC-DA0D60681B`), and `Area / Exterior Lighting` (`IFC-ED86F51087`) as marked applicable in workbook row 12. | `26020-Packages_Interfaces_4_export.xlsx` row 12; `INTERFACE_REGISTER.csv` rows 40-42; `ARTIFACT_REGISTER.csv` rows 170-172; `_CONTEXT.md` Notes. |
| REQ-106-02-014 | The Datasheet shall identify as TBD (with provenance) the items not present in accessible source slices, including: photometric levels / illuminance targets, fixture quantities and locations, pole/mast heights and structural details, tagged equipment list for `PKG-106`, and WBS code. | `PACKAGE_REGISTER.csv` row 12 (`WBS TBD`); absence of per-package Yard Lighting row in `26020-Package_Requirements.docx` (verified by full-text scan); absence of photometric tables in accessible DBM sections. |
| REQ-106-02-015 | The Datasheet shall not invent values for items not source-grounded; ASSUMPTION-labelled inferences are limited to those where the facility-wide electrical/lighting basis applies and shall be marked as such. | Skill `four-documents` Method Step 4a; `_REFERENCES.md` authority. |

## Standards

| Standard / Code | Status | Source / Location |
|---|---|---|
| Canadian Electrical Code (CEC) | Governing for conduit, raceway, and electrical installation methods. | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Cable, Wire, and Raceways (line 3025) ("Canadian Electrical Code and the applicable area classification"). |
| NEMA VE2 | Governing for cable-tray support where details not otherwise issued. | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Cable, Wire, and Raceways (line 3019). |
| Local light-pollution regulatory requirements | Applicable; specific regulator and jurisdiction location TBD. | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Lighting and Receptacles (line 3035) ("Regulatory light-pollution requirements"); regulator identity location TBD. |
| Building code (emergency lighting and exit lights) | Applicable to building-mounted lighting only. | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Lighting and Receptacles (line 3031). |
| Illuminance / photometric standards (e.g., IES) | ASSUMPTION: likely applicable; not cited in accessible sources. | location TBD. |

## Verification

| Requirement | Verification Approach |
|---|---|
| REQ-106-02-001, REQ-106-02-002 | Document review against `PACKAGE_REGISTER.csv` row 12 and `DELIVERABLE_REGISTER.csv` row 43. |
| REQ-106-02-003, REQ-106-02-004, REQ-106-02-005 | Vendor submittal review confirming LED fixture type, area-classification ratings, and fixture data sheets. |
| REQ-106-02-006 | Vendor design review confirming downcast/non-horizontal optics, photocell/switch control, mast-pole setback, and conformance to identified regulatory light-pollution constraints. |
| REQ-106-02-007 | Single-line and load-list review confirming source from 208/120 V panelboard fed by a 600 V → 208/120 V distribution transformer. |
| REQ-106-02-008 | Building-code crosswalk for emergency-lighting count and UPS feed at building-mounted fixtures (only where co-located buildings exist). |
| REQ-106-02-009, REQ-106-02-010 | Schedule and circuit-list review (no mixing of receptacle and lighting circuits; conductor size ≤ #10 AWG where practical). |
| REQ-106-02-011, REQ-106-02-012 | Cable schedule and conduit schedule review against tray-cable / conduit construction standards. |
| REQ-106-02-013 | Interface matrix review against `INTERFACE_REGISTER.csv` rows 40-42 and workbook row 12. |
| REQ-106-02-014, REQ-106-02-015 | Source-grounding audit: every non-trivial datasheet value carries a citation (`SourcePath` + `SectionRef`) or is explicitly TBD/ASSUMPTION. |

## Documentation

Expected anticipated artifacts (from `_CONTEXT.md` Anticipated Artifacts and `ARTIFACT_REGISTER.csv` rows 167-172):

- Package technical datasheet (`ART-AE8A9D9DB8`).
- Vendor engineering handoff basis (`ART-9E11FA7FB5`).
- Package interface requirements matrix (`ART-51069C3B2D`).
- Interface-fact evidence rows: Electrical Power (`ART-B670C2963F`), Grounding / Bonding (`ART-0686DF8D13`), Area / Exterior Lighting (`ART-9F2D1E8063`).
- Source-supported equipment and design criteria (carried inside the Datasheet, with TBD where source-limited).

The Datasheet itself does NOT produce: vendor document register, vendor submittals, construction work-package documents, or factory test records (those are produced by sibling deliverables in `PKG-106`).
