# Datasheet: DEL-024-06_epc-vendor-package-review-and-acceptance

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-024-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Deliverable name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-024` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | MV VFD - 2000HP, 4160V, 3PH, 60HZ - 4160V VFD | Workbook Packages row 26; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 24 / row 26 | Workbook Packages row 26; `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` row `PKG-024` |
| CoA tracking number | 26020-01-30-015 | `PACKAGE_REGISTER.csv` row `PKG-024` |
| Discipline | Electrical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Deliverable type | EPC Vendor Package Acceptance | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Covers scope | `SOW-0025` | `_CONTEXT.md`; `SCOPE_LEDGER.csv` |
| Supports objectives | `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-008`, `OBJ-009`, `OBJ-010` | `_CONTEXT.md`; `OBJECTIVE_DELIVERABLE_MAP.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-024` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Acceptance role | EPC Integrator-led review and acceptance against the EPC Scope of Work (`DEL-024-01`), Package Datasheet (`DEL-024-02`), and Construction Work Package (`DEL-024-03`). | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` rows `DEL-024-01`/`DEL-024-02`/`DEL-024-03` |
| Subject under review | Package Vendor's Vendor Engineered Equipment Package (`DEL-024-04`) and Vendor Document Turnover Package (`DEL-024-05`) for the MV VFD - 2000HP, 4160V, 3PH, 60HZ - 4160V VFD package. | `DELIVERABLE_REGISTER.csv` rows `DEL-024-04`/`DEL-024-05` |
| Review scope basis | EPC Scope of Work for `PKG-024`, EPC Package Datasheet for `PKG-024`, and EPC Construction Work Package for `PKG-024`. | `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` |
| Acceptance evidence set | Vendor document review and comment log; vendor package acceptance and turnover checklist; factory/shop test and inspection evidence. | `ARTIFACT_REGISTER.csv` rows `ART-803E267B52`, `ART-6136727237`, `ART-A9C4AF8FF5` |
| Anticipated artifacts | Vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence. | `_CONTEXT.md` Anticipated Artifacts |
| Vendor package class | Vendor-owned Electrical package; medium-voltage variable frequency drive (VFD) rated 2,000 hp at 4,160 V, 3-phase, 60 Hz, 4,160 V VFD output. | Workbook Packages row 26 (package name); `PACKAGE_REGISTER.csv` row `PKG-024` |
| Applicable interfaces (EPC integration scope) | Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. | `INTERFACE_REGISTER.csv` rows `IFC-68C5E24846`, `IFC-F8A6E25E1C`, `IFC-8062D6F881`, `IFC-22E88310C9`, `IFC-DD889EF8E3`, `IFC-850A8082BB` |

## Conditions

| Review condition | Acceptance basis | Source |
|---|---|---|
| Source-grounded review | Review findings, acceptance entries, and rejections shall cite the EPC SOW, EPC Package Datasheet, EPC CWP, accepted Gate 7 registers, or accessible DBM source slices. | `_REFERENCES.md`; `DELIVERABLE_REGISTER.csv` `DEL-024-01`/`-02`/`-03` |
| MV VFD integration context | DBM identifies 4.16 kV motor control center context and notes that "VFD and soft-starter requirements for 4.16 kV motors are TBD." Detailed integration requirements for the MV VFD package shall be confirmed during EPC review against the EPC Package Datasheet. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 4.16 kV MCC paragraph and electrical TBD list (4.16 kV motor starting) |
| Electrical-building housing context | DBM allows electrical buildings to house, as required by detailed design, medium-voltage VFDs alongside MV switchgear, MCCs, and reduced-voltage soft starters. Final housing/location for this PKG-024 MV VFD package is TBD pending the EPC Package Datasheet and Construction Work Package. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| Hazardous-area marking for VFD-fed motors | Where the VFD feeds motors located in Zone 2 areas, the motors shall be marked accordingly and supplied with a temperature code lower than the temperature code specified on the area-classification drawing or fugitive-emissions study. Applicability to this package's served motor shall be confirmed during EPC review. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, VFD-fed motor paragraph |
| Low-voltage cable from VFDs | Where applicable to this package's cabling scope, low-voltage power cable fed from VFDs shall be copper TECK cable. Applicability shall be confirmed by the EPC Package Datasheet and CWP. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical cable type table |
| Interface acceptance | Each interface listed for `PKG-024` in `INTERFACE_REGISTER.csv` shall be confirmed in the EPC Package Datasheet interface matrix before vendor acceptance is closed. | `INTERFACE_REGISTER.csv` rows for `PKG-024` |
| Responsibility split preservation | Review shall not transfer vendor-owned engineering/design/documentation/equipment scope to the EPC Integrator nor transfer EPC-owned facility integration scope to the Package Vendor. | `PACKAGE_REGISTER.csv` row `PKG-024` |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Acceptance authorship | EPC Integrator authors and owns the review log, acceptance checklist, and acceptance decision; Package Vendor provides supporting input. | `_CONTEXT.md` ResponsibleParty; `DELIVERABLE_REGISTER.csv` |
| Vendor document review log | Maintained by the EPC Integrator; records review status, comments, dispositions, and reference identifiers for each vendor submittal in `DEL-024-05`. | `ARTIFACT_REGISTER.csv` row `ART-803E267B52`; `DELIVERABLE_REGISTER.csv` `DEL-024-05` |
| Package acceptance and turnover checklist | Maintained by the EPC Integrator; records acceptance of vendor package against EPC SOW, EPC Package Datasheet, and EPC CWP scope items and interface facts. | `ARTIFACT_REGISTER.csv` row `ART-6136727237` |
| Factory/shop test and inspection evidence | Collected from the Package Vendor; reviewed and accepted by the EPC Integrator; detailed test/inspection requirements are source-specific where available and otherwise `TBD`. | `ARTIFACT_REGISTER.csv` row `ART-A9C4AF8FF5` |
| Turnover evidence | Collated from accepted vendor documentation, accepted test/inspection evidence, and the acceptance checklist; used as input to facility integration and construction handoff. | `_CONTEXT.md` Anticipated Artifacts |
| Detailed acceptance criteria (per attribute) | TBD pending the issued EPC Package Datasheet (`DEL-024-02`) and EPC Construction Work Package (`DEL-024-03`) content for `PKG-024`. | Source gap: `DEL-024-02` and `DEL-024-03` content not consumed in this run |
| 26020-Package_Requirements content | No accessible PKG-024-specific source slice was extracted in this run; `_Sources/26020-Package_Requirements.docx` was not parsed for package-specific MV VFD acceptance criteria. | `_REFERENCES.md` Missing/Deferred References; source not parsed in this run |

## References

- `_CONTEXT.md`, deliverable identity, scope, and decomposition reference.
- `_REFERENCES.md`, Gate 7 source pointers and shared source root.
- `_DEPENDENCIES.md`, declared upstream/downstream lists (none declared during PREPARATION).
- `DELIVERABLE_REGISTER.csv`, rows `DEL-024-01` through `DEL-024-06`.
- `PACKAGE_REGISTER.csv`, row `PKG-024`.
- `ARTIFACT_REGISTER.csv`, rows `ART-803E267B52`, `ART-6136727237`, `ART-A9C4AF8FF5` for `DEL-024-06`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-024` (Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports).
- `SCOPE_LEDGER.csv`, scope item `SOW-0025`.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows mapping `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-008`, `OBJ-009`, `OBJ-010` to `PKG-024`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 26.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis source slices for 4.16 kV MCC/VFD, electrical buildings, VFD-fed motor area marking, VFD-fed low-voltage cable type, and electrical TBD list (4.16 kV motor starting).
- `_Sources/26020-Package_Requirements.docx`, not parsed in this run; carry as deferred source for downstream Pass 3 enrichment.
