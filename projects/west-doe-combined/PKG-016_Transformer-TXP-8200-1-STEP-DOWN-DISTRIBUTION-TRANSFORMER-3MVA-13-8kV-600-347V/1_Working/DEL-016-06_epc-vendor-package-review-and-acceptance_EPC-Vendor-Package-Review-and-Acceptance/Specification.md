# Specification: DEL-016-06_epc-vendor-package-review-and-acceptance

## Scope

### In scope

- EPC Integrator-led review, integration acceptance, and handoff readiness assessment of the PKG-016 vendor package (13.8 kV / 600 V, 3 MVA step-down distribution transformer TXP-8200-1, with 600/347 V secondary) against:
  - DEL-016-01 EPC Scope of Work,
  - DEL-016-02 EPC Package Datasheet,
  - DEL-016-03 EPC Construction Work Package.
- Production and maintenance of the four acceptance artifacts identified in `_CONTEXT.md`:
  - Vendor document review log,
  - Package acceptance checklist,
  - Test/inspection evidence record,
  - Turnover evidence record.
- Coverage of the PKG-016 declared interface types (Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports) per `INTERFACE_REGISTER.csv`.
- Source-grounding traceability back to `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` for facility-level electrical bases the vendor package must satisfy.

### Out of scope

- Vendor package engineering, design, fabrication, documentation, and physical supply — owned by Package Vendor in DEL-016-04 / DEL-016-05.
- Production of the EPC Scope of Work, Package Datasheet, or Construction Work Package (those are DEL-016-01 / -02 / -03).
- Facility-wide commissioning and operations beyond turnover from this package.
- Authoring binding approvals or signoffs; per K-AUTH-1, only humans author binding approval records.

## Requirements

> Requirement IDs use the form `REQ-016-06-NN`. Each requirement carries a source pointer or is labelled `ASSUMPTION` / `TBD` when not source-anchored.

| ID | Requirement | Source / status |
|---|---|---|
| REQ-016-06-01 | The acceptance record SHALL document review of the vendor package against DEL-016-01, DEL-016-02, and DEL-016-03 as the EPC reference set. | `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` row `DEL-016-06` |
| REQ-016-06-02 | The acceptance record SHALL produce the four artifacts declared in `_CONTEXT.md`: vendor document review log, package acceptance checklist, test/inspection evidence, turnover evidence. | `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row `DEL-016-06` |
| REQ-016-06-03 | The vendor document review log SHALL be reconciled against the DEL-016-05 Vendor Document Turnover Package register and shall identify any missing or non-conforming vendor documents. | `DELIVERABLE_REGISTER.csv` row `DEL-016-05` |
| REQ-016-06-04 | The package acceptance checklist SHALL include line items for each PKG-016 declared interface type (Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports). | `INTERFACE_REGISTER.csv` rows for `PKG-016`; `PACKAGE_REGISTER.csv` row `PKG-016` |
| REQ-016-06-05 | The acceptance evidence SHALL confirm vendor compliance with the facility primary feed: 13.8 kV, 3 phase, 3 wire, 60 Hz LRG sub-feed from the 04-25 13.8 kV Main Switchgear. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, "System Voltages" and "Incoming Power and Transformers" |
| REQ-016-06-06 | The acceptance evidence SHALL confirm vendor compliance with the facility LV service: 600 V, 3 phase, 3 wire, 60 Hz HRG with 5 A continuous resistor, feeding the 600 V MCC. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, "System Voltages" and "600V MCC and Standby Power" |
| REQ-016-06-07 | The acceptance evidence SHALL record the basis used to satisfy the 600/347 V package title (e.g., 4-wire secondary, separate dry-type, or other vendor configuration), since the DBM "System Voltages" table identifies only the 600 V 3-wire LV service. ASSUMPTION-flagged interpretations SHALL be resolved or escalated as conflict items. | Workbook Packages row 18 (title); `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, "System Voltages"; see Guidance Conflict Table |
| REQ-016-06-08 | The acceptance evidence SHALL record vendor compliance with the -40 deg C minimum ambient site basis, or document a more severe vendor-imposed condition. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, site basis paragraph |
| REQ-016-06-09 | The acceptance evidence SHALL confirm vendor data supports area classification consistent with the facility basis (Class I Zone 2, Gas Groups IIA/IIB unless detailed classification drawings identify otherwise). | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, "Area Classification" |
| REQ-016-06-10 | The acceptance evidence SHALL confirm vendor grounding/bonding arrangement is compatible with the project HRG/LRG bases and with CEC grounding practice for distribution transformers. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, raceways/grounding paragraphs |
| REQ-016-06-11 | The acceptance evidence SHALL confirm vendor cable/conduit routing data is compatible with the EPC raceway design and does not impair maintenance access; circuit separation between 13.8 kV / 4,160 V / 600 V power circuits and control/instrument circuits SHALL be preserved. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, "Electrical Buildings, Raceways..." |
| REQ-016-06-12 | The test/inspection evidence SHALL include vendor factory test reports for the transformer (e.g., routine tests per the governing transformer standard). Specific routine, type, and special tests applicable to TXP-8200-1 SHALL be listed in the checklist when the governing transformer standard is identified. | TBD — governing transformer standard not stated in accessible sources; see REQ-016-06-13 |
| REQ-016-06-13 | The acceptance package SHALL cite the governing transformer standard(s) (e.g., CSA C88, IEEE C57 series) that the vendor design and tests comply with, as confirmed in DEL-016-02 EPC Package Datasheet or DEL-016-04 vendor data. | TBD — standard not enumerated in accessible sources |
| REQ-016-06-14 | The turnover evidence SHALL include vendor installation, operation, and maintenance documentation; nameplate verification; protective-device settings basis (if supplied by vendor or required for handoff); and any spare-parts list per DEL-016-05. | `DELIVERABLE_REGISTER.csv` row `DEL-016-05`; ASSUMPTION on protective-device settings basis pending DEL-016-02 |
| REQ-016-06-15 | The acceptance record SHALL preserve traceability between each disposition (Accept / Accept-with-comment / Reject-and-resubmit) and the vendor document, requirement, or interface it addresses. | ASSUMPTION — disposition vocabulary not defined in accessible sources |
| REQ-016-06-16 | The acceptance record SHALL NOT certify, approve, sign, or issue the vendor package for reliance. Binding approvals are reserved to humans per K-AUTH-1. | Project governance: `docs/CONTRACT.md` K-AUTH-1 |

## Standards

| Standard / source | Role | Status |
|---|---|---|
| `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` | Facility-level electrical design basis (system voltages, incoming power and transformers, area classification, raceways, site basis). | Locally accessible |
| Workbook Packages row 18 | Package identity and interface declarations. | Locally accessible (via `PACKAGE_REGISTER.csv` and `INTERFACE_REGISTER.csv`) |
| Gate 7 PROJECT_DECOMP snapshot (`DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`) | Decomposition truth for package, deliverable, interfaces, and objectives. | Locally accessible |
| CSA C22.1 Canadian Electrical Code (CEC) | Governing electrical installation code (general reference per project context; specific clauses TBD). | TBD — location TBD |
| CSA C88 / IEEE C57 (transformer standards) | Likely governing transformer design and test standards. | ASSUMPTION — not enumerated in accessible sources; resolve via DEL-016-02 / DEL-016-04 |
| Project electrical specifications | Detailed cable, raceway, grounding, and bonding requirements referenced by DBM raceways section. | TBD — location TBD |

## Verification

| Requirement | Verification approach | Records |
|---|---|---|
| REQ-016-06-01 | Documented review walkthrough cross-referencing each EPC reference document to vendor submittals. | Vendor document review log |
| REQ-016-06-02 | Existence and completeness check on the four named artifacts. | Acceptance file index |
| REQ-016-06-03 | Reconciliation matrix: DEL-016-05 vendor document register vs. submittals received. | Vendor document review log; gap list |
| REQ-016-06-04 | Checklist line items mapped to each `INTERFACE_REGISTER.csv` row for `PKG-016`. | Package acceptance checklist |
| REQ-016-06-05, REQ-016-06-06 | Verification of vendor nameplate, primary/secondary voltage, capacity, and impedance against DBM system-voltage and incoming-power tables. | Test/inspection evidence; nameplate record |
| REQ-016-06-07 | Recorded resolution of the 600/347 V interpretation (e.g., 4-wire secondary acceptance basis or downstream dry-type). | Acceptance record + Conflict Table closure |
| REQ-016-06-08 | Vendor cold-weather/winterization confirmation (temperature rating, oil viscosity if applicable, heating provisions). | Test/inspection evidence |
| REQ-016-06-09 | Confirmation of hazardous-area applicability for the transformer location. | Acceptance record |
| REQ-016-06-10 | Inspection of vendor grounding/bonding drawings against project HRG/LRG and CEC grounding sizing practice. | Inspection record |
| REQ-016-06-11 | Layout/routing review against EPC raceway and maintenance-access drawings. | Inspection record |
| REQ-016-06-12, REQ-016-06-13 | Receipt and review of vendor factory test reports against the cited governing standard. | Test reports; standard citation log |
| REQ-016-06-14 | Turnover document checklist closure. | Turnover evidence record |
| REQ-016-06-15 | Disposition register entries traceable to each line item. | Disposition log |
| REQ-016-06-16 | Self-check: no binding approval text issued in any acceptance artifact. | Acceptance record review |

## Documentation

Per `_CONTEXT.md` Anticipated Artifacts and the requirements above, the deliverable produces:

- Vendor document review log (input: DEL-016-05 vendor register; output: per-document disposition).
- Package acceptance checklist (interface-by-interface and requirement-by-requirement disposition).
- Test/inspection evidence record (factory test reports, site inspection records, nameplate verification, energization checks where applicable).
- Turnover evidence record (installation/operation/maintenance documentation, spare-parts list, protective-device settings basis where in vendor scope).

All four artifacts remain within `{DELIVERABLE_PATH}` and are referenced by the EPC Integrator's facility-level handoff to commissioning. Binding approvals are reserved to humans (K-AUTH-1).
