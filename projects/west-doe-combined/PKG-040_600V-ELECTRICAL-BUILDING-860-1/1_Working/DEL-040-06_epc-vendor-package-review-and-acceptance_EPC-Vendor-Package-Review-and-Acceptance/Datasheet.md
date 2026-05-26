# Datasheet: DEL-040-06_epc-vendor-package-review-and-acceptance

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-040-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md` |
| Deliverable name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-040-06` |
| Parent package | `PKG-040` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row `PKG-040` |
| Package name | 600V ELECTRICAL BUILDING (860-1) | Workbook Packages row 42; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 40 / row 42 | `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-031 | `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Deliverable type | EPC Vendor Package Acceptance | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Building tag | 860-1 (600 V General Area / Tank Farm Electrical Building) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2816; package title |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-040` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Review scope | EPC Integrator review and acceptance of the Package Vendor's engineered electrical building package (`DEL-040-04`), vendor document turnover (`DEL-040-05`), and integration readiness against `DEL-040-01` (Scope of Work), `DEL-040-02` (Package Datasheet), and `DEL-040-03` (Construction Work Package). | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-040-06` |
| Package class | Vendor-owned Electrical package: prefabricated, modular 600 V electrical building for the General Area / Tank Farm service (building 860-1). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2816, 2971-2979; `PACKAGE_REGISTER.csv` row `PKG-040` |
| Voltage class basis | 600 V, 3 phase, 3 wire, 60 Hz, high-resistance grounded with 5 A continuous resistor (facility low-voltage service). Building is fed from a step-down transformer off the 13.8 kV facility backbone. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2919-2925, 2937, 2985 |
| Equipment to be housed (per facility basis) | As required by detailed design, may house 600 V MCCs, 600 V SCR heater-control panels, 600 V to 208/120 V distribution transformers and panelboards, 120 V AC UPS with battery banks and distribution panels, 125 V DC UPS with battery banks and distribution panels, 208/120 V contactor panels, plant PLC control panels, and network racks. ASSUMPTION: medium-voltage switchgear/VFDs are not housed in 860-1, which is a 600 V building serving General Area / Tank Farm; final equipment list is `TBD` pending vendor general arrangement. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2973 |
| Construction basis | Prefabricated, modular building; climate controlled with HVAC sized as n+1; designed for bottom entry of incoming and outgoing power cables; elevated on piles to provide space beneath the building for cable trays to the 600 V MCC main incoming section; wired with TECK and ACIC cables; EMT conduit between adjacent equipment; outdoor GFI receptacle for exterior maintenance; equipment doors sized (or with removable transom sections) for removal of the largest equipment. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2973-2979 |
| Grounding basis | 600 V transformer secondary (feeding this building) grounded by a 5 A continuous high-resistance grounding resistor; 600 V MCCs to include power metering and ground/resistor fault detection; ground-fault protection on 600 V systems is alarm-only to maintain continuity of operations. Major electrical equipment connected to ground grid at two points (facility-typical). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2985 |
| Location basis | Electrical buildings located in general purpose (unclassified) areas for convenient power distribution; minimum 25 m (82 ft) from fired heaters per OGAOM Sec. 9.6.15 cited in source. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 298, 2911 |
| Standby-power interface | TOU standby generators connect at the low-voltage (600 V MCC) level via transfer switches and supply both 04-25 and 03-25 facilities; building 860-1 MCC participation in this scheme is `TBD` pending vendor single-line confirmation. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2943 |
| Vendor document set basis | Vendor document register, submittals, and turnover records are produced under `DEL-040-05`; EPC review-and-comment evidence is captured under this deliverable. | `DELIVERABLE_REGISTER.csv` rows `DEL-040-05`, `DEL-040-06`; `ARTIFACT_REGISTER.csv` row `ART-127E61EEAE` |
| Factory/shop test evidence | Expected package test/inspection evidence; detailed test scope is `TBD` pending Package Datasheet / vendor ITP finalization. | `ARTIFACT_REGISTER.csv` row `ART-993D18AF3B` |
| Acceptance evidence | Vendor package acceptance and turnover checklist is the principal acceptance artifact carried by this deliverable for integration into the facility. | `ARTIFACT_REGISTER.csv` row `ART-F627B8462B` |

## Conditions

Interface-by-interface acceptance-review basis derived from `INTERFACE_REGISTER.csv` rows for `PKG-040` (twelve applicable interface types per Workbook Packages row 42) and the electrical design basis source slices.

| Interface / condition | Acceptance-review basis | Source |
|---|---|---|
| Utility Piping | Vendor package shall demonstrate any utility-piping tie-ins (e.g., HVAC condensate, washdown if any) align with EPC Package Datasheet and avoid conflicts with bottom-entry cable routing. Specific tie-ins are `TBD` pending vendor general arrangement. | `INTERFACE_REGISTER.csv` row `IFC-C7A10165E0`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2977 |
| Drain / Containment | Vendor package shall expose drain/containment provisions consistent with facility drainage philosophy; building elevation on piles is consistent with grade drainage clearance. Specific drain tie-ins are `TBD`. | `INTERFACE_REGISTER.csv` row `IFC-84254E4D74`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2977 |
| Electrical Power | Vendor package shall demonstrate compliance with EPC Package Datasheet electrical power interface requirements: 600 V, 3-phase, 3-wire, 60 Hz HRG service fed from a step-down transformer off the 13.8 kV backbone; bottom-entry incoming and outgoing power cables; 600 V MCCs as the building's main 600 V distribution. | `INTERFACE_REGISTER.csv` row `IFC-01418C7B46`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2919-2925, 2937, 2959, 2977 |
| Grounding / Bonding | Vendor package shall demonstrate connection to the facility ground grid and conformance to the 5 A HRG architecture for the 600 V system, with 600 V MCC ground/resistor fault detection and alarm-only ground-fault protection. | `INTERFACE_REGISTER.csv` row `IFC-1AFD94C7C5`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2985 |
| Area / Exterior Lighting | Vendor package layout shall not impair or be impaired by area/exterior lighting; outdoor GFI receptacle provision for exterior maintenance shall be present. | `INTERFACE_REGISTER.csv` row `IFC-31FBC53269`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2979 |
| I&C / Control Cabling | Vendor package shall house plant PLC control panels and network racks as required by detailed design and shall expose terminations for facility I&C and control cabling consistent with the Package Datasheet. EMT conduit shall be used for adjacent-equipment runs. | `INTERFACE_REGISTER.csv` row `IFC-4924815E92`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2973, 2979 |
| Communications / Network | Vendor package shall accommodate network racks per facility design; specific network/communications interfaces are `TBD` pending Package Datasheet finalization. | `INTERFACE_REGISTER.csv` row `IFC-07F9E1739B`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2973 |
| Building HVAC / Services | Vendor package HVAC shall be n+1 sized so failure or maintenance shutdown of one unit does not affect building heating/cooling; electric building heaters of Ruffneck-type are the default where heat-medium heaters are not practical. | `INTERFACE_REGISTER.csv` row `IFC-E5C808A2AF`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2210, 2975 |
| Fire & Gas / Safety Systems | Vendor package shall demonstrate compliance with facility fire and gas detection, alarm, and shutdown interface requirements for an unclassified-area electrical building. Specific F&G device list is `TBD` pending Package Datasheet. | `INTERFACE_REGISTER.csv` row `IFC-AB1228ED22` |
| Maintenance Access | Equipment doors sized (or with removable transom sections) for removal of the largest equipment; cable tray and conduit routing shall preserve maintenance and replacement access; outdoor GFI receptacle for exterior maintenance. | `INTERFACE_REGISTER.csv` row `IFC-DD57C5C1B0`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2979 |
| Grading / Site Drainage / Spill Containment | Building location in a general purpose area with pile-elevated structure; site grading and drainage at the building footprint shall be consistent with facility drainage and spacing requirements. Specific grading details are `TBD`. | `INTERFACE_REGISTER.csv` row `IFC-CB9A638F41`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2911, 2977 |
| Structural / Foundations / Supports | Building elevated and installed on piles to provide space beneath the building for incoming/outgoing cable trays; pile design and structural support per Package Datasheet and facility structural basis. Load data and anchor patterns shall be confirmed against vendor general arrangement. | `INTERFACE_REGISTER.csv` row `IFC-327D21980E`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2977 |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Vendor package engineering, design, fabrication, and supply | Package Vendor responsibility, reviewed by EPC Integrator under this deliverable. | `PACKAGE_REGISTER.csv` row `PKG-040`; `DELIVERABLE_REGISTER.csv` row `DEL-040-04` |
| Facility integration, tie-ins, constructability | EPC Integrator responsibility; verified during package acceptance against the Construction Work Package (`DEL-040-03`). | `PACKAGE_REGISTER.csv` row `PKG-040`; `DELIVERABLE_REGISTER.csv` row `DEL-040-03` |
| Vendor document review log | Maintained by the EPC Integrator across vendor submittals; entries reference the Package Datasheet requirements being verified. | `ARTIFACT_REGISTER.csv` row `ART-127E61EEAE` |
| Acceptance checklist | Single-record acceptance and turnover checklist with explicit pass / conditional / fail markings for each interface and the vendor document register. | `ARTIFACT_REGISTER.csv` row `ART-F627B8462B` |
| Test/inspection evidence | Factory acceptance test (FAT) reports, routine test records, and shop inspection evidence preserved alongside the acceptance record. Specific test list is `TBD` pending vendor ITP. | `ARTIFACT_REGISTER.csv` row `ART-993D18AF3B` |
| Turnover evidence | Turnover records for the vendor package are received from `DEL-040-05` and incorporated into the acceptance evidence. | `DELIVERABLE_REGISTER.csv` row `DEL-040-05`; `_CONTEXT.md` anticipated artifacts |
| Installation location | Building 860-1 (General Area / Tank Farm). Specific pad/site coordinates are `TBD`. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2816 |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `_DEPENDENCIES.md`, declared dependencies (none at PREPARATION).
- `DELIVERABLE_REGISTER.csv`, row `DEL-040-06_epc-vendor-package-review-and-acceptance` and sibling rows `DEL-040-01` through `DEL-040-05`.
- `PACKAGE_REGISTER.csv`, row `PKG-040`.
- `ARTIFACT_REGISTER.csv`, rows `ART-127E61EEAE`, `ART-F627B8462B`, `ART-993D18AF3B`.
- `INTERFACE_REGISTER.csv`, twelve `PKG-040` interface rows: `IFC-C7A10165E0`, `IFC-84254E4D74`, `IFC-01418C7B46`, `IFC-1AFD94C7C5`, `IFC-31FBC53269`, `IFC-4924815E92`, `IFC-07F9E1739B`, `IFC-E5C808A2AF`, `IFC-AB1228ED22`, `IFC-DD57C5C1B0`, `IFC-CB9A638F41`, `IFC-327D21980E`.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows associating `DEL-040-06` with OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010.
- `SCOPE_LEDGER.csv`, row `SOW-0041`.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis source slices: facility electrical-building list (line 2816), spacing (line 298), location (line 2911), distribution and feeders (lines 2919-2925, 2937), 600 V MCC / SCR / heater architecture (lines 2959, 2969), electrical buildings (lines 2971-2979), standby power (line 2943), grounding (line 2985), building heaters (line 2210).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 42.
- `_Sources/26020-Package_Requirements.docx`, package-specific vendor-document requirements: `TBD`; no package-specific match identified during PREPARATION.
