# Datasheet: DEL-039-06_epc-vendor-package-review-and-acceptance

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-039-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md` |
| Deliverable name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-039` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 600V ELECTRICAL BUILDING (850-1) | Workbook Packages row 41; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 39 / row 41 | Workbook Packages row 41; `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` row `PKG-039` |
| CoA tracking number | 26020-01-30-030 | `PACKAGE_REGISTER.csv` row `PKG-039` |
| Discipline | Electrical | `PACKAGE_REGISTER.csv`; `_CONTEXT.md` |
| Deliverable type | EPC Vendor Package Acceptance | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-039` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Review subject | Package Vendor production unit for the 850-1 600 V electrical building (DEL-039-04) and the Vendor Document Turnover Package (DEL-039-05). | `DELIVERABLE_REGISTER.csv` rows `DEL-039-04`, `DEL-039-05`, `DEL-039-06` |
| Acceptance basis (anchor documents) | EPC Scope of Work (`DEL-039-01`), EPC Package Datasheet (`DEL-039-02`), and EPC Construction Work Package (`DEL-039-03`). | `DELIVERABLE_REGISTER.csv` rows `DEL-039-01`..`DEL-039-03`; `_CONTEXT.md` Scope |
| Review log artifact | Vendor document review and comment log (`ART-3910447327`). | `ARTIFACT_REGISTER.csv` row `ART-3910447327` |
| Acceptance checklist artifact | Vendor package acceptance and turnover checklist (`ART-AA4BFB86C9`). | `ARTIFACT_REGISTER.csv` row `ART-AA4BFB86C9` |
| Test / inspection evidence artifact | Factory/shop test and inspection evidence (`ART-0156F0196A`); detailed requirements are source-specific where available. | `ARTIFACT_REGISTER.csv` row `ART-0156F0196A` |
| Turnover evidence | Turnover evidence is part of the acceptance/checklist artifact set; package-specific records (Form/index) `TBD` until vendor documentation set is received. | `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row `DEL-039-06` |
| Equipment scope reviewed | 600 V electrical building 850-1 (Sales/Overheads Compressor Electrical Building per DBM electrical distribution narrative); housed equipment per detailed design may include 600 V MCCs, 120 V AC UPS, 125 V DC UPS, 600 V to 208/120 V distribution transformers and panelboards, 208/120 V contactor panels, plant PLC control panels, and network racks. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Electrical Buildings" and "Power Distribution" paragraphs; equipment-list rows 2811-2816 |
| Construction / fabrication mode | Shop-fabricated prefabricated modular electrical building. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Electrical Buildings" paragraph; equipment-list row 2815 |
| Vendor package contents to be evidenced | Vendor engineered physical equipment package and vendor package design basis / datasheet set per `DEL-039-04`; vendor document register, submittals, source-required vendor documentation, and turnover records per `DEL-039-05`. | `DELIVERABLE_REGISTER.csv` rows `DEL-039-04`, `DEL-039-05` |

## Conditions

| Interface / condition | Acceptance condition basis | Source |
|---|---|---|
| Utility Piping | Vendor package interface to facility utility piping shall be reviewed and accepted against the EPC Package Datasheet interface matrix. | `INTERFACE_REGISTER.csv` `IFC-A257E2C89C` |
| Drain / Containment | Vendor package drain/containment interface shall be reviewed and accepted against the EPC Package Datasheet interface matrix. | `INTERFACE_REGISTER.csv` `IFC-5C80D8C3EC` |
| Electrical Power | Vendor package electrical power interface (incoming feed, distribution boundary) shall be reviewed and accepted against the EPC Package Datasheet interface matrix and the facility radial distribution from 13.8 kV main switchgear. | `INTERFACE_REGISTER.csv` `IFC-C1DF6B8DD9`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Power Distribution" |
| Grounding / Bonding | Vendor package grounding/bonding interface shall be reviewed against the facility ground-grid two-point connection rule and ground-well requirement at electrical buildings. | `INTERFACE_REGISTER.csv` `IFC-9653B84E14`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Grounding and Bonding" |
| Area / Exterior Lighting | Vendor package exterior/area lighting interface shall be reviewed against the facility lighting basis (LED, area-classification suitability). | `INTERFACE_REGISTER.csv` `IFC-4BC9BD20C1`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Lighting and Receptacles" |
| I&C / Control Cabling | Vendor package I&C/control cabling interface shall be reviewed against the facility cable/raceway basis (ACIC instrumentation cable; cable tray installation). | `INTERFACE_REGISTER.csv` `IFC-3F18DB0D3A`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Cable, Wire, and Raceways" |
| Communications / Network | Vendor package communications/network interface shall be reviewed against the facility communications cable basis (armored, tray-rated). | `INTERFACE_REGISTER.csv` `IFC-B95212AB85`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Cable, Wire, and Raceways" |
| Building HVAC / Services | Vendor package HVAC interface shall be reviewed against the n + 1 HVAC sizing requirement for electrical buildings. | `INTERFACE_REGISTER.csv` `IFC-D8A8F7FEBC`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Electrical Buildings" |
| Fire & Gas / Safety Systems | Vendor package F&G/safety interface shall be reviewed against the EPC Package Datasheet F&G interface matrix. | `INTERFACE_REGISTER.csv` `IFC-9C0AFE36A2` |
| Maintenance Access | Vendor package maintenance-access interface shall be reviewed against the equipment-door sizing/removable-transom requirement and the cable-tray non-interference rule. | `INTERFACE_REGISTER.csv` `IFC-D971A17948`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Electrical Buildings" and "Cable Tray and Conduit" |
| Grading / Site Drainage / Spill Containment | Vendor package site grading/drainage interface shall be reviewed against the EPC Package Datasheet site interface matrix. | `INTERFACE_REGISTER.csv` `IFC-50A5B3F280` |
| Structural / Foundations / Supports | Vendor package foundation/support interface shall be reviewed against the elevated, pile-supported building basis and bottom-entry cable configuration. | `INTERFACE_REGISTER.csv` `IFC-E3D0A5A836`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Electrical Buildings" |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Review and acceptance authority | EPC Integrator leads review and acceptance; Package Vendor provides input, responses, and turnover records. Only humans author binding acceptance/sign-off; agent-produced drafts are proposals. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-039-06`; K-AUTH-1 (CONTRACT) |
| Compliance and inspection regime | Electrical materials and equipment shall be designed, fabricated, installed, tested, and inspected per CSA C22.1-21 Canadian Electrical Code, applicable BC provincial/local codes, and the requirements of the Tourmaline-designated electrical inspection authority. Applicable standards bodies include CSA, API, IEEE, ISA, NEMA, WorkSafeBC, Technical Safety BC, BCER. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical compliance paragraph (line 2866) |
| Factory/shop test and inspection | Shop-fabricated electrical building is subject to factory/shop test and inspection evidence prior to shipment; specific test types, witness points, and acceptance thresholds `TBD` pending vendor inspection and test plan (ITP). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, equipment-list row 2815 ("Shop"); `ARTIFACT_REGISTER.csv` row `ART-0156F0196A` |
| Vendor document register acceptance | Vendor document register, submittals, and source-required vendor documentation are produced under `DEL-039-05`; acceptance under `DEL-039-06` confirms completeness against the EPC Scope of Work, Package Datasheet, and Construction Work Package. | `DELIVERABLE_REGISTER.csv` rows `DEL-039-05`, `DEL-039-06` |
| Turnover / handoff readiness | Handoff readiness is evidenced by acceptance checklist and turnover records; package-specific turnover index format `TBD` pending vendor turnover documentation. | `_CONTEXT.md` Anticipated Artifacts |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-039-06_epc-vendor-package-review-and-acceptance` and sibling rows `DEL-039-01`..`DEL-039-05`.
- `PACKAGE_REGISTER.csv`, row `PKG-039`.
- `ARTIFACT_REGISTER.csv`, rows `ART-3910447327`, `ART-AA4BFB86C9`, `ART-0156F0196A`.
- `INTERFACE_REGISTER.csv`, twelve rows for `PKG-039`.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-039-06` (OBJ-001, OBJ-004..OBJ-010).
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis (sections: Power Distribution; 208/120 V Systems; Electrical Buildings; Grounding and Bonding; Cable, Wire, and Raceways; Cable Tray and Conduit; Lighting and Receptacles; electrical compliance paragraph) and equipment-list row 2815.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 41.
- `_Sources/26020-Package_Requirements.docx`, searched for 850-1 600 V electrical building review/acceptance content; no package-specific match was identified by ID.
