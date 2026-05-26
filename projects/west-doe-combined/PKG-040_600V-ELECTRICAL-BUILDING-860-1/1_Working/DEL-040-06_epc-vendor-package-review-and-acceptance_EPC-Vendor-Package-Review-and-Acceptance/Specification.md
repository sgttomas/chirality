# Specification: DEL-040-06_epc-vendor-package-review-and-acceptance

## Scope

This specification defines the EPC Integrator's review and acceptance scope for the Package Vendor's engineered 600 V electrical building package (building 860-1, General Area / Tank Farm). It covers vendor document review, integration acceptance, and handoff readiness against the EPC Scope of Work (`DEL-040-01`), Package Datasheet (`DEL-040-02`), and Construction Work Package (`DEL-040-03`).

**In scope:**
- Review-and-comment of the Vendor Document Turnover Package (`DEL-040-05`) against EPC Package Datasheet and facility electrical design basis.
- Interface-by-interface acceptance evaluation for the twelve applicable interface types declared for `PKG-040`.
- Factory/shop test and inspection evidence intake.
- Acceptance and turnover checklist for integration into the facility.

**Out of scope:**
- Vendor package engineering, design, and supply (covered by `DEL-040-04`).
- Construction execution and tie-in workface planning (covered by `DEL-040-03`).
- Vendor document register authoring (covered by `DEL-040-05`).
- Cross-package re-engineering of the facility electrical design basis.

Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-040-06`; `SCOPE_LEDGER.csv` row `SOW-0041`.

## Requirements

Each requirement traces to source. Inferred requirements are labeled `ASSUMPTION`. Unknown specifics are `TBD`.

| ID | Requirement | Source | Status |
|---|---|---|---|
| REQ-040-06-01 | The EPC Integrator shall maintain a vendor document review and comment log capturing each vendor submittal, the Package Datasheet requirement(s) being verified, EPC review disposition, and the closure action. | `ARTIFACT_REGISTER.csv` row `ART-127E61EEAE` | Required |
| REQ-040-06-02 | The EPC Integrator shall produce a single-record vendor package acceptance and turnover checklist with explicit pass / conditional / fail markings for each of the twelve `PKG-040` interface types and for the vendor document register. | `ARTIFACT_REGISTER.csv` row `ART-F627B8462B`; `INTERFACE_REGISTER.csv` rows `IFC-C7A10165E0`, `IFC-84254E4D74`, `IFC-01418C7B46`, `IFC-1AFD94C7C5`, `IFC-31FBC53269`, `IFC-4924815E92`, `IFC-07F9E1739B`, `IFC-E5C808A2AF`, `IFC-AB1228ED22`, `IFC-DD57C5C1B0`, `IFC-CB9A638F41`, `IFC-327D21980E` | Required |
| REQ-040-06-03 | Factory acceptance test (FAT) reports, routine test records, and shop inspection evidence shall be received from the Package Vendor and preserved alongside the acceptance record. Specific test scope shall align with the vendor inspection-and-test plan and the Package Datasheet. | `ARTIFACT_REGISTER.csv` row `ART-993D18AF3B` | Required; ITP-specific list `TBD` |
| REQ-040-06-04 | Vendor electrical-power interface evidence shall confirm 600 V, 3-phase, 3-wire, 60 Hz HRG service architecture with bottom-entry incoming and outgoing power cables and 600 V MCC as the main building distribution. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2937, 2959, 2977 | Required |
| REQ-040-06-05 | Vendor grounding/bonding evidence shall confirm 5 A continuous high-resistance grounding for the 600 V transformer feeding the building, 600 V MCC power metering and ground/resistor fault detection, and alarm-only ground-fault protection on 600 V systems. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2985 | Required |
| REQ-040-06-06 | Vendor HVAC evidence shall confirm an n+1 building HVAC arrangement such that failure or maintenance shutdown of one HVAC unit does not affect building heating/cooling. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2975 | Required |
| REQ-040-06-07 | Vendor building construction evidence shall confirm prefabricated modular construction, pile-elevated structure with cable-tray space beneath the building, bottom-entry cable design, TECK/ACIC cabling, EMT for adjacent-equipment runs, an outdoor GFI receptacle, and equipment doors sized (or with removable transom sections) for removal of the largest equipment. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2977-2979 | Required |
| REQ-040-06-08 | Vendor electrical-area classification evidence shall confirm the building is sited in a general purpose (unclassified) area and meets the 25 m (82 ft) minimum spacing from fired heaters. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 298, 2911 | Required |
| REQ-040-06-09 | Vendor equipment-housed list shall be reviewed against the building's 600 V scope (e.g., 600 V MCCs, SCR heater-control panels, 600 V to 208/120 V distribution transformers and panelboards, 120 V AC UPS, 125 V DC UPS, 208/120 V contactor panels, plant PLC control panels, network racks). ASSUMPTION: medium-voltage switchgear/VFDs are not housed in 860-1. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2969, 2973 | Required |
| REQ-040-06-10 | Vendor standby-power interface evidence (if applicable to 860-1 MCC) shall confirm the TOU standby-generator transfer-switch arrangement at the 600 V MCC level. Applicability for 860-1 is `TBD`. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2943 | Conditional; applicability `TBD` |
| REQ-040-06-11 | Vendor F&G evidence shall confirm fire-and-gas detection, alarm, and shutdown interface compliance for an unclassified electrical building. Specific device list shall match the Package Datasheet. | `INTERFACE_REGISTER.csv` row `IFC-AB1228ED22` | Required; device list `TBD` |
| REQ-040-06-12 | Vendor structural/foundation evidence shall confirm pile-supported elevated structure, load data, and anchor patterns against the EPC structural/foundation interface requirement. | `INTERFACE_REGISTER.csv` row `IFC-327D21980E`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2977 | Required |
| REQ-040-06-13 | EPC acceptance shall not be issued until all vendor document register items reach EPC review disposition and no `fail` markings remain on the acceptance checklist for interface compliance. Conditional acceptances shall list the open items, owners, and closure dates. ASSUMPTION: this two-gate closure rule follows standard EPC package acceptance practice; not explicitly stated in accessible source. | ASSUMPTION (EPC integration practice consistent with `_CONTEXT.md` scope) | Required (assumed) |

## Standards

| Reference | Scope | Status |
|---|---|---|
| Facility Electrical Design Basis | DBM-Deepcut SEC-12 Electrical Basis (and the source slices cited above) governs voltage levels, grounding, building construction, HVAC, and standby power. | Accessible: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| OGAOM Sec. 9.6.15 | Minimum 25 m (82 ft) separation between fired heaters and control room / electrical buildings (as quoted in DBM table). | Indirect: quoted in `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 298; primary text `location TBD` |
| Canadian Electrical Code (CEC) | Transformer spacing and installation; provincial AHJ. | Mentioned by DBM (line 2951); primary text `location TBD` |
| Vendor package requirements document | `_Sources/26020-Package_Requirements.docx`. | Accessible at the root; package-specific section for `PKG-040` `TBD` (not identified during PREPARATION). |
| Project workbook | Packages row 42 and the twelve `PKG-040` interface columns. | Indirect: rendered into `PACKAGE_REGISTER.csv`, `INTERFACE_REGISTER.csv`. |

## Verification

| Requirement(s) | Verification approach | Evidence artifact |
|---|---|---|
| REQ-040-06-01 | Document-by-document review; log entries cross-link Package Datasheet requirement IDs. | Vendor document review and comment log (`ART-127E61EEAE`). |
| REQ-040-06-02 | Checklist walkthrough by interface type with EPC discipline reviewers; conditional items tracked to closure. | Vendor package acceptance and turnover checklist (`ART-F627B8462B`). |
| REQ-040-06-03 | Receipt and review of FAT/routine/shop inspection records against vendor ITP and Package Datasheet test requirements. | Factory/shop test and inspection evidence (`ART-993D18AF3B`). |
| REQ-040-06-04, REQ-040-06-05, REQ-040-06-07, REQ-040-06-09 | Vendor single-line, general arrangement, panel schedules, bill of materials, and cable schedule cross-checked against DBM source slices. | Vendor document review log + acceptance checklist. |
| REQ-040-06-06 | Vendor HVAC datasheet and sizing calculation review; n+1 confirmation. | Vendor document review log + acceptance checklist. |
| REQ-040-06-08 | Site layout / area classification drawing review against facility electrical area classification and spacing tables. | Vendor document review log + acceptance checklist. |
| REQ-040-06-10 | Single-line review for standby/transfer-switch arrangement; confirm or formally exclude 860-1 MCC participation. | Vendor document review log; open item record where applicable. |
| REQ-040-06-11 | Vendor F&G device schedule and shutdown matrix review against facility F&G interface basis. | Vendor document review log + acceptance checklist. |
| REQ-040-06-12 | Vendor structural drawings and anchor/load data reviewed against EPC structural interface requirement. | Vendor document review log + acceptance checklist. |
| REQ-040-06-13 | Closeout gate review: all log items disposed, no `fail` markings, conditional items have owners and dates. | Acceptance and turnover checklist + closeout sign-off. |

## Documentation

Required artifacts produced by this deliverable (from `_CONTEXT.md` and `ARTIFACT_REGISTER.csv` for `DEL-040-06`):

- Vendor document review and comment log (`ART-127E61EEAE`).
- Vendor package acceptance and turnover checklist (`ART-F627B8462B`).
- Factory/shop test and inspection evidence packet (`ART-993D18AF3B`).
- Turnover evidence packet (composed from `DEL-040-05` outputs and the acceptance checklist).

Required upstream documentation consulted (read-only inputs):

- `DEL-040-01` Scope of Work; `DEL-040-02` Package Datasheet; `DEL-040-03` Construction Work Package.
- `DEL-040-04` Vendor Engineered Equipment Package submittals.
- `DEL-040-05` Vendor Document Turnover Package register and submittals.
