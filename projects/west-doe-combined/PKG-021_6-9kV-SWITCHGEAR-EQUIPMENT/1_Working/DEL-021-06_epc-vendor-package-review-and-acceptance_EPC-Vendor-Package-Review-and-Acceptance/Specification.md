# Specification — DEL-021-06 EPC Vendor Package Review and Acceptance

## Scope

### In scope
- EPC Integrator-led review, integration acceptance, and handoff-readiness evidence for the PKG-021 6.9 kV switchgear vendor package, evaluated against:
  - the EPC Scope of Work (`DEL-021-01`),
  - the EPC Package Datasheet (`DEL-021-02`),
  - the EPC Construction Work Package (`DEL-021-03`),
  - the Vendor Engineered Equipment Package (`DEL-021-04`),
  - the Vendor Document Turnover Package (`DEL-021-05`).
  Source: GATE-07 `DELIVERABLE_REGISTER.csv` row `DEL-021-06`; GATE-07 `SCOPE_LEDGER.csv` row `SOW-0022`.
- Production of the three registered artifacts for this deliverable:
  - vendor document review and comment log (`ART-5D5CAC1D6D`),
  - vendor package acceptance and turnover checklist (`ART-4B01C09131`),
  - factory/shop test and inspection evidence (`ART-E523401B0C`).
  Source: GATE-07 `ARTIFACT_REGISTER.csv` rows for `DEL-021-06`.
- Coverage of all applicable PKG-021 interface types declared in GATE-07 `INTERFACE_REGISTER.csv` (Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports).

### Out of scope
- Authoring of the EPC Scope of Work, Package Datasheet, or Construction Work Package (owned by upstream EPC deliverables `DEL-021-01`/`-02`/`-03`).
- Vendor-owned engineering, design, fabrication, or vendor documentation authoring (owned by `DEL-021-04` and `DEL-021-05`; per `PACKAGE_REGISTER.csv` row `PKG-021` responsibility split).
- Approval-for-reliance authority (humans only; per `K-AUTH-1`).

## Requirements

| ID | Requirement | Source / basis |
|---|---|---|
| REQ-021-06-01 | The deliverable shall produce a vendor document review and comment log capturing EPC Integrator review of vendor documentation against the EPC Scope of Work, Package Datasheet, and Construction Work Package. | GATE-07 `ARTIFACT_REGISTER.csv` row `ART-5D5CAC1D6D`; `DELIVERABLE_REGISTER.csv` row `DEL-021-06` |
| REQ-021-06-02 | The deliverable shall produce a vendor package acceptance and turnover checklist evidencing integration acceptance and handoff readiness for the PKG-021 package. | GATE-07 `ARTIFACT_REGISTER.csv` row `ART-4B01C09131`; `DELIVERABLE_REGISTER.csv` row `DEL-021-06` |
| REQ-021-06-03 | The deliverable shall capture factory/shop test and inspection evidence applicable to the vendor-supplied 6.9 kV switchgear package. | GATE-07 `ARTIFACT_REGISTER.csv` row `ART-E523401B0C` |
| REQ-021-06-04 | Acceptance evidence shall cover each applicable PKG-021 interface type: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. | GATE-07 `INTERFACE_REGISTER.csv` rows for `PKG-021` |
| REQ-021-06-05 | Acceptance shall verify the vendor package supports the facility 6.9 kV, 3-phase, 3-wire, 60 Hz, low-resistance-grounded medium-voltage service. | DBM-Deepcut 4-25_Deepcut_DBM.md line 2935 |
| REQ-021-06-06 | Acceptance shall verify grounding compatibility with the facility 6.9 kV neutral grounding scheme (100 A, 10 s resistor; tripping system). | DBM-Deepcut 4-25_Deepcut_DBM.md line 2985 |
| REQ-021-06-07 | Acceptance shall confirm the package is compatible with installation in a prefabricated modular electrical building in a general-purpose area. | DBM-Deepcut 4-25_Deepcut_DBM.md line 2973 |
| REQ-021-06-08 | All accepted evidence shall cite its source artifact, vendor document number, and review disposition; unsupported claims shall be recorded as `TBD` rather than asserted. | Governing invariant `K-PROV-1` (mandatory provenance); skill source-grounding rule |
| REQ-021-06-09 | Only humans may issue binding acceptance/approval-for-reliance. Agents produce proposals and recommendations only. | Governing invariant `K-AUTH-1` |
| REQ-021-06-10 (ASSUMPTION) | Detailed clause-level acceptance criteria for switchgear (e.g., dielectric, partial-discharge, mechanical operation tests) shall follow the standards cited in the Package Datasheet once those clauses are locally accessible. | ASSUMPTION — standards listed in `_REFERENCES.md` for `DEL-021-02` not accessible in this run; `location TBD`. |

## Standards

| Standard / source | Relevance | Location accessible? |
|---|---|---|
| Facility Design Basis Memorandum (DBM-Deepcut, `4-25_Deepcut_DBM.md`) | Defines facility electrical service basis (voltage, grounding, building envelope) against which the vendor package is integrated. | YES (lines 2935, 2973, 2985) |
| Workbook Packages row 23 | Authoritative package-row definition for PKG-021 | YES (carried via GATE-07 registers) |
| `26020-Package_Requirements.docx` | Likely package-requirements basis | location TBD — not parsed in this run (binary; no specific PKG-021 slice extracted) |
| IEEE C37-series (switchgear test/acceptance) and CSA/IEC equivalents | Likely governing for switchgear FAT/SAT (ASSUMPTION) | location TBD; not cited in accessible sources |

## Verification

| Requirement | Verification approach |
|---|---|
| REQ-021-06-01 | Inspection of completed vendor document review and comment log; cross-reference each logged entry against vendor submittals in `DEL-021-05`. |
| REQ-021-06-02 | Inspection of completed vendor package acceptance and turnover checklist; verify every checklist line has a human-signed disposition. |
| REQ-021-06-03 | Inspection of factory/shop test and inspection evidence (witnessed test reports, certificates, punch list closeout). |
| REQ-021-06-04 | Trace each of the six PKG-021 interface types to at least one accepted evidence item; gaps recorded as `TBD` / open punch. |
| REQ-021-06-05 | Verify vendor nameplate / certified data confirms 6.9 kV, 3-phase, 3-wire, 60 Hz service and is consistent with DBM section. |
| REQ-021-06-06 | Verify vendor grounding configuration is compatible with the facility 100 A, 10 s low-resistance grounding scheme. |
| REQ-021-06-07 | Verify physical envelope, anchorage, clearances, and environment are compatible with the modular electrical building. |
| REQ-021-06-08 | Audit: every accepted item carries source citation; otherwise marked `TBD`. |
| REQ-021-06-09 | Audit: only human-signed records carry acceptance authority. |
| REQ-021-06-10 | Recheck after standards source slices become locally accessible; convert ASSUMPTION items to source-anchored requirements at that time. |

## Documentation

The deliverable shall be documented by:
- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` (this four-document kit).
- Registered artifacts (planned filenames; ASSUMPTION on exact paths):
  - `vendor-document-review-log.md` / `.csv` (`ART-5D5CAC1D6D`)
  - `vendor-package-acceptance-and-turnover-checklist.md` / `.csv` (`ART-4B01C09131`)
  - `factory-shop-test-and-inspection-evidence/` folder of vendor-supplied PDFs and a manifest (`ART-E523401B0C`)
- `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_CONTEXT.md` (metadata; not modified by this skill beyond safe `_STATUS.md` update).
