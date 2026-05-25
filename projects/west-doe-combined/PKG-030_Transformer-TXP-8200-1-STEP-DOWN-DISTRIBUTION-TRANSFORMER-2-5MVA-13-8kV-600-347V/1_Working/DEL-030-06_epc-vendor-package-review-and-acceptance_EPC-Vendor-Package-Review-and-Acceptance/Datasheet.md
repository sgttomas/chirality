# Datasheet: DEL-030-06_epc-vendor-package-review-and-acceptance

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-030-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md` |
| Deliverable name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-030` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | Transformer TXP-8200-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V | Workbook Packages row 32; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 30 / row 32 | `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-021 | `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | `PACKAGE_REGISTER.csv`; `_CONTEXT.md` |
| Deliverable type | EPC Vendor Package Acceptance | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-030` |
| Covers scope items | `SOW-0031` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Supports objectives | `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-008`, `OBJ-009`, `OBJ-010` (ASSUMPTION: package-grouping heuristic) | `OBJECTIVE_DELIVERABLE_MAP.csv` (package-heuristic association) |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Acceptance class | EPC Integrator review and acceptance evidence against the EPC Scope of Work (DEL-030-01), Package Datasheet (DEL-030-02), and Construction Work Package (DEL-030-03). | `DELIVERABLE_REGISTER.csv` row `DEL-030-06`; `_CONTEXT.md` |
| Subject package class | Vendor-owned Electrical package (step-down distribution transformer). | `PACKAGE_REGISTER.csv` row `PKG-030` |
| Subject package function | Step-down distribution transformer rated 2.5 MVA, 13.8 kV / 600/347 V; receives 13.8 kV from plant switchgear and feeds 600 V plant distribution (and 347 V where applicable). | Workbook Packages row 32; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` electrical distribution paragraphs (13.8 kV switchgear distributes radially through step-down transformers to 600 V services) |
| Vendor inputs under review | Vendor engineered equipment package (DEL-030-04) and vendor document turnover package (DEL-030-05). | `DELIVERABLE_REGISTER.csv` rows `DEL-030-04`, `DEL-030-05` |
| Acceptance basis documents | EPC SoW (DEL-030-01), Package Datasheet (DEL-030-02), Construction Work Package (DEL-030-03). | `DELIVERABLE_REGISTER.csv` rows `DEL-030-01`, `DEL-030-02`, `DEL-030-03` |
| Detailed transformer ratings (cooling class, BIL, impedance, vector group, taps, temperature rise, NLL/LL, noise) | TBD. Accessible sources confirm voltage and power rating only; vendor data is required for the remaining nameplate parameters. | Source gap; `26020-Package_Requirements.docx` not opened for package-specific match |
| Containment, oil-fill, and secondary containment | Large oil-filled transformers shall be spaced per CEC; secondary containment requirements shall be reviewed and transformer selection shall avoid or limit containment where practical. Package-specific selection (oil-filled vs. dry-type) for TXP-8200-1 is TBD pending vendor data. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Transformers paragraph |

## Conditions

| Interface / condition | Acceptance basis | Source |
|---|---|---|
| Electrical Power | Acceptance evidence shall confirm the vendor package satisfies the Electrical Power interface fact for PKG-030, including 13.8 kV primary connection from plant switchgear and 600 V secondary distribution. | Workbook Packages row 32; `INTERFACE_REGISTER.csv` `IFC-009C48E7FF`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` distribution paragraph |
| Grounding / Bonding | Acceptance evidence shall confirm the transformer is directly connected to the ground grid at two points; 600 V transformer secondary shall be grounded by a 5 A continuous high-resistance grounding resistor; a separate copper ground conductor connected directly to ground shall be provided for the distribution transformer per CEC sizing. | `INTERFACE_REGISTER.csv` `IFC-6C663BF69D`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs (600 V transformer grounding; ground grid two-point connection; distribution-transformer separate ground conductor) |
| Area / Exterior Lighting | Acceptance evidence shall confirm interface fact applicability; package-specific lighting interfaces TBD. | `INTERFACE_REGISTER.csv` `IFC-0B28AED229` |
| I&C / Control Cabling | Acceptance evidence shall confirm interface fact applicability for transformer monitoring/protection control cabling. | `INTERFACE_REGISTER.csv` `IFC-D000451C37` |
| Communications / Network | Acceptance evidence shall confirm interface fact applicability for any vendor-provided monitoring/network ties. | `INTERFACE_REGISTER.csv` `IFC-9EF13A0FC1` |
| Maintenance Access | Acceptance evidence shall confirm cable tray and conduit routing do not interfere with maintenance access and that vendor layout preserves required clearances. | `INTERFACE_REGISTER.csv` `IFC-345609CB34`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs |
| Structural / Foundations / Supports | Acceptance evidence shall confirm the transformer is mounted per the DBM expectation (transformers generally supported on precast concrete bearing foundations and/or structural steel transformer bases as applicable). | `INTERFACE_REGISTER.csv` `IFC-4B50D76AF1`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, foundations and Transformers paragraphs |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Vendor document review log (ART-0FE3BFB82C) | EPC review evidence for vendor documentation and integration requirements; one record per submittal cycle with disposition (accepted / accepted with comments / rejected) and traceable comment closure. | `ARTIFACT_REGISTER.csv` row `ART-0FE3BFB82C` |
| Package acceptance and turnover checklist (ART-6934DD5E20) | EPC acceptance evidence for integration into the facility, signed at acceptance gate by EPC Integrator with Package Vendor input. | `ARTIFACT_REGISTER.csv` row `ART-6934DD5E20` |
| Factory / shop test and inspection evidence (ART-F13347A23A) | Vendor test evidence packaged with EPC review notes; detailed required tests are source-specific and TBD where not stated. | `ARTIFACT_REGISTER.csv` row `ART-F13347A23A` |
| Field installation and tie-in inspection evidence | EPC-managed evidence collected against the Construction Work Package (DEL-030-03). | `DELIVERABLE_REGISTER.csv` row `DEL-030-03` |
| Turnover record set | Compiled at handoff; includes signed acceptance checklist, closed comment log, accepted test/inspection evidence, and any open-item disposition. | `DELIVERABLE_REGISTER.csv` row `DEL-030-06` |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-030-06_epc-vendor-package-review-and-acceptance` and related rows `DEL-030-01`..`DEL-030-05`.
- `PACKAGE_REGISTER.csv`, row `PKG-030`.
- `ARTIFACT_REGISTER.csv`, rows `ART-0FE3BFB82C`, `ART-6934DD5E20`, `ART-F13347A23A`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-030` (Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, Structural / Foundations / Supports).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, package-grouping rows for `PKG-030` (ASSUMPTION: package-heuristic association).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 32.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, distribution, transformers, foundations, grounding, cable tray, and conduit source slices.
- `_Sources/26020-Package_Requirements.docx`, location TBD; no package-specific PKG-030 slice opened for this pass.
