# Datasheet: DEL-031-06_epc-vendor-package-review-and-acceptance

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-031-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md` |
| Deliverable name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-031` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | Transformer TXP-8500-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 3MVA 13.8kV/600/347V | Workbook Packages row 33; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 31 / row 33 | Workbook Packages row 33; `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-022 | `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Deliverable type | EPC Vendor Package Acceptance | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Equipment tag | TXP-8500-1 | Workbook Packages row 33; package title |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-031` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Review scope | EPC Integrator review and acceptance of the Package Vendor's engineered equipment package, vendor document turnover, and integration readiness against `DEL-031-01` (Scope of Work), `DEL-031-02` (Package Datasheet), and `DEL-031-03` (Construction Work Package). | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-031-06` |
| Package class | Vendor-owned Electrical package, step-down distribution transformer (3 MVA, 13.8 kV primary / 600 V secondary; 347 V phase-to-neutral implied by 600 V wye system). | `PACKAGE_REGISTER.csv` row `PKG-031`; package title |
| Voltage class basis | 13.8 kV primary aligns with the facility 13.8 kV medium-voltage backbone; 600 V secondary aligns with the facility 600 V three-phase three-wire low-voltage distribution. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical voltage and service table |
| Grounding basis | 600 V transformer secondary shall be grounded by a 5 A continuous high-resistance grounding resistor per the facility electrical design basis; primary-side grounding shall follow the medium-voltage system grounding architecture; major electrical equipment connected to the ground grid at two points. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs |
| Supports / foundations basis | Transformers are generally supported on precast concrete bearing foundations and installed on structural steel transformer bases; secondary containment requirements shall be reviewed and selection should avoid or limit containment where practical. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, foundations and transformers paragraphs |
| Spacing basis | Large oil-filled transformers shall be spaced per CEC requirements. ASSUMPTION: transformer oil/dry type for TXP-8500-1 is not explicitly stated in accessible source slices; spacing applicability is `TBD` pending vendor data. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers paragraph |
| Vendor document set basis | Vendor document register, submittals, and turnover records are produced under `DEL-031-05` (Vendor Document Turnover Package); EPC review and comment evidence is captured under this deliverable. | `DELIVERABLE_REGISTER.csv` rows `DEL-031-05`, `DEL-031-06`; `ARTIFACT_REGISTER.csv` row `ART-8D69884269` |
| Factory/shop test evidence | Expected test and inspection evidence accompanies the vendor package; specific test scopes are vendor-specification driven. Detailed test scope is `TBD` pending Package Datasheet / vendor ITP. | `ARTIFACT_REGISTER.csv` row `ART-0D8191743E` |
| Acceptance evidence | Vendor package acceptance and turnover checklist is the principal acceptance artifact carried by this deliverable for integration into the facility. | `ARTIFACT_REGISTER.csv` row `ART-E97EECD60B` |

## Conditions

| Interface / condition | Acceptance-review basis | Source |
|---|---|---|
| Electrical Power | Vendor package shall demonstrate compliance with the EPC Package Datasheet electrical power interface requirements for the 13.8 kV primary feed and 600 V secondary distribution. | Workbook Packages row 33; `INTERFACE_REGISTER.csv` `IFC-E6C51663E5` |
| Grounding / Bonding | Vendor package shall demonstrate compliance with grounding/bonding interface requirements, including connection to the facility ground grid at two points and resistor-grounding architecture for the 600 V secondary system. | Workbook Packages row 33; `INTERFACE_REGISTER.csv` `IFC-2DE626B361`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Area / Exterior Lighting | Vendor package layout shall not impair or be impaired by area/exterior lighting; lighting fixture and pole locations relative to the transformer pad shall be reviewed. | Workbook Packages row 33; `INTERFACE_REGISTER.csv` `IFC-9BF05B6DCC` |
| I&C / Control Cabling | Vendor package shall expose terminations and provisions for control cabling per the EPC Package Datasheet (e.g., temperature, tap-changer, alarm, status). Specific I&C points are `TBD` pending Package Datasheet finalization. | Workbook Packages row 33; `INTERFACE_REGISTER.csv` `IFC-5DCD93CE40` |
| Communications / Network | Vendor package communications/network provisions (if any) shall be reviewed against the EPC Package Datasheet. ASSUMPTION: distribution transformers typically have limited or no native network interface; final scope is `TBD`. | Workbook Packages row 33; `INTERFACE_REGISTER.csv` `IFC-452A0203CB` |
| Maintenance Access | Vendor package layout shall preserve maintenance access including operator clearances, oil sampling/handling access (if oil-filled), bushing replacement, and de-energization isolation. Cable tray and conduit routing shall not interfere with maintenance access. | Workbook Packages row 33; `INTERFACE_REGISTER.csv` `IFC-3A6221E4CB`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs |
| Structural / Foundations / Supports | Vendor package shall be supported per the package datasheet foundation/support basis; concrete pad/steel base details, anchor patterns, and load data shall be confirmed against vendor general arrangement. | Workbook Packages row 33; `INTERFACE_REGISTER.csv` `IFC-15FCC571C7`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, foundations paragraph |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Vendor package engineering, design, and supply | Package Vendor responsibility, reviewed by EPC Integrator under this deliverable. | `PACKAGE_REGISTER.csv` row `PKG-031`; `DELIVERABLE_REGISTER.csv` row `DEL-031-04` |
| Facility integration, tie-ins, constructability | EPC Integrator responsibility; verified during package acceptance against the Construction Work Package (`DEL-031-03`). | `PACKAGE_REGISTER.csv` row `PKG-031`; `DELIVERABLE_REGISTER.csv` row `DEL-031-03` |
| Vendor document review log | Maintained by EPC Integrator across vendor submittals; entries reference the Package Datasheet requirements being verified. | `ARTIFACT_REGISTER.csv` row `ART-8D69884269` |
| Acceptance checklist | Single-record acceptance and turnover checklist with explicit pass/conditional/fail markings for each interface and the vendor document register. | `ARTIFACT_REGISTER.csv` row `ART-E97EECD60B` |
| Test/inspection evidence | Factory acceptance test (FAT) reports, routine test records, and shop inspection evidence preserved alongside the acceptance record. Specific test list is `TBD` pending vendor ITP. | `ARTIFACT_REGISTER.csv` row `ART-0D8191743E` |
| Turnover evidence | Turnover records for the vendor package are received from `DEL-031-05` and incorporated into the acceptance evidence. | `DELIVERABLE_REGISTER.csv` row `DEL-031-05`; `_CONTEXT.md` anticipated artifacts |
| Installation location | `TBD`. Source material does not assign TXP-8500-1 to a specific building, pad, or area; transformer is feasible at indoor (electrical building) or outdoor pad locations per facility-typical practice. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings and transformers paragraphs |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `_DEPENDENCIES.md`, declared dependencies (none at PREPARATION).
- `DELIVERABLE_REGISTER.csv`, row `DEL-031-06_epc-vendor-package-review-and-acceptance` and sibling rows `DEL-031-01` through `DEL-031-05`.
- `PACKAGE_REGISTER.csv`, row `PKG-031`.
- `ARTIFACT_REGISTER.csv`, rows `ART-8D69884269`, `ART-E97EECD60B`, `ART-0D8191743E`.
- `INTERFACE_REGISTER.csv`, rows `IFC-E6C51663E5`, `IFC-2DE626B361`, `IFC-9BF05B6DCC`, `IFC-5DCD93CE40`, `IFC-452A0203CB`, `IFC-3A6221E4CB`, `IFC-15FCC571C7` for `PKG-031`.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows associating `DEL-031-06` with OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 33.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis source slices: voltage/service table, transformers, grounding and bonding, electrical buildings, cable tray and conduit, foundations.
- `_Sources/26020-Package_Requirements.docx`, searched for `PKG-031`/transformer-specific acceptance content; no package-specific match identified.
