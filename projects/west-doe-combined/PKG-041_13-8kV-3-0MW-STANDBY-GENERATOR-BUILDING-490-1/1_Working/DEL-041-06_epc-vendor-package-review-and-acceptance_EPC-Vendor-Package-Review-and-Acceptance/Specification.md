# Specification — DEL-041-06 EPC Vendor Package Review and Acceptance

## Scope

### In scope
- EPC Integrator-led review, integration acceptance, and handoff-readiness evidence for the PKG-041 standby-generator-building vendor package, evaluated against:
  - the EPC Scope of Work (`DEL-041-01`),
  - the EPC Package Datasheet (`DEL-041-02`),
  - the EPC Construction Work Package (`DEL-041-03`),
  - the Vendor Engineered Equipment Package (`DEL-041-04`),
  - the Vendor Document Turnover Package (`DEL-041-05`).
  Source: GATE-07 `DELIVERABLE_REGISTER.csv` row `DEL-041-06`; GATE-07 `SCOPE_LEDGER.csv` row `SOW-0042`.
- Production of the three registered artifacts for this deliverable:
  - vendor document review and comment log (`ART-9E33107762`),
  - vendor package acceptance and turnover checklist (`ART-0E8BDED2A8`),
  - factory/shop test and inspection evidence (`ART-53AD41FE27`).
  Source: GATE-07 `ARTIFACT_REGISTER.csv` rows for `DEL-041-06`.
- Coverage of all applicable PKG-041 interface types declared in GATE-07 `INTERFACE_REGISTER.csv` (Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports).

### Out of scope
- Authoring of the EPC Scope of Work, Package Datasheet, or Construction Work Package (owned by upstream EPC deliverables `DEL-041-01`/`-02`/`-03`).
- Vendor-owned engineering, design, fabrication, or vendor documentation authoring (owned by `DEL-041-04` and `DEL-041-05`; per `PACKAGE_REGISTER.csv` row `PKG-041` responsibility split).
- Resolution of the workbook-vs-DBM electrical-architecture conflict (see Guidance Conflict Table `CONF-041-06-001`); acceptance criteria here are conditioned on whichever electrical architecture the human ruling selects.
- Approval-for-reliance authority (humans only; per `K-AUTH-1`).

## Requirements

| ID | Requirement | Source / basis |
|---|---|---|
| REQ-041-06-01 | The deliverable shall produce a vendor document review and comment log capturing EPC Integrator review of vendor documentation against the EPC Scope of Work, Package Datasheet, and Construction Work Package. | GATE-07 `ARTIFACT_REGISTER.csv` row `ART-9E33107762`; `DELIVERABLE_REGISTER.csv` row `DEL-041-06` |
| REQ-041-06-02 | The deliverable shall produce a vendor package acceptance and turnover checklist evidencing integration acceptance and handoff readiness for the PKG-041 package. | GATE-07 `ARTIFACT_REGISTER.csv` row `ART-0E8BDED2A8`; `DELIVERABLE_REGISTER.csv` row `DEL-041-06` |
| REQ-041-06-03 | The deliverable shall capture factory/shop test and inspection evidence applicable to the vendor-supplied standby-generator package. | GATE-07 `ARTIFACT_REGISTER.csv` row `ART-53AD41FE27` |
| REQ-041-06-04 | Acceptance evidence shall cover each applicable PKG-041 interface type: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. | GATE-07 `INTERFACE_REGISTER.csv` rows for `PKG-041` |
| REQ-041-06-05 | Acceptance shall verify the vendor package supports the facility's emergency-power architecture as governed by the accepted design basis. The current DBM basis is LV standby generation on the LV MCC with transfer switch; the 13.8 kV / 3 MW concept is recorded as superseded. Acceptance shall confirm with vendor data which architecture is being supplied and shall record any inconsistency for human ruling. | DBM-Comp_and_Liquids `3-25_Comp_and_Liquids_DBM.md` line 505; DBM-Deepcut `4-25_Deepcut_DBM.md` line 175; Guidance Conflict Table `CONF-041-06-001` |
| REQ-041-06-06 | Acceptance shall verify the fuel-gas supply interface for the emergency generator: less than 66 psig during normal operation; design flow 0.468 MMSCFD (13.2 e3m3/d); start-gas flow 3.6 MMSCFD for 30 s (TBC); local fuel-gas particulate filter at the generator. | DBM-Deepcut `4-25_Deepcut_DBM.md` lines 1848, 1866, 1870 |
| REQ-041-06-07 | Acceptance shall verify the building/enclosure envelope basis: vendor-supplied weather-protective outdoor enclosure; 1 m access walkway; overhead lift provisions confirmed by MLE per the selected generator package. | DBM-Deepcut `4-25_Deepcut_DBM.md` lines 2074-2080 |
| REQ-041-06-08 | Acceptance shall record TBD items for vendor parameters not yet defined: generator make / model / rating, LV switchgear assignment, transfer switch configuration, fuel selection, battery/charger sizing, diesel storage (if selected), generator count. Each TBD shall be tracked to closure on the punch list. | DBM-Deepcut `4-25_Deepcut_DBM.md` line 1836; line 175 |
| REQ-041-06-09 | All accepted evidence shall cite its source artifact, vendor document number, and review disposition; unsupported claims shall be recorded as `TBD` rather than asserted. | Governing invariant `K-PROV-1` (mandatory provenance); skill source-grounding rule |
| REQ-041-06-10 | Only humans may issue binding acceptance / approval-for-reliance. Agents produce proposals and recommendations only. | Governing invariant `K-AUTH-1` |
| REQ-041-06-11 (ASSUMPTION) | Detailed clause-level acceptance criteria for the standby-generator package (e.g., engine and generator standards, fuel-gas-system standards, emissions, packaged-enclosure standards, electrical-area-classification) shall follow the standards cited in the Package Datasheet once those clauses are locally accessible. | ASSUMPTION — standards listed in `_REFERENCES.md` for `DEL-041-02` not accessible in this run; `location TBD`. |

## Standards

| Standard / source | Relevance | Location accessible? |
|---|---|---|
| Facility Design Basis Memorandum (DBM-Deepcut, `4-25_Deepcut_DBM.md`) | Defines facility emergency-power basis, fuel-gas interface, enclosure expectations, and open generator parameters against which the vendor package is integrated. | YES (lines 175, 1836, 1848, 1866, 1870, 2074-2080) |
| Facility Design Basis Memorandum (DBM-Comp_and_Liquids, `3-25_Comp_and_Liquids_DBM.md`) | States that the 13.8 kV / 3 MW emergency-generator concept is superseded by LV standby generation on the LV MCC with transfer switch. | YES (lines 505, 762) |
| Workbook Packages row 43 | Authoritative package-row definition for PKG-041 (carries the legacy 13.8 kV / 3 MW title). | YES (carried via GATE-07 registers) |
| `26020-Package_Requirements.docx` | Likely package-requirements basis | `location TBD` — not parsed in this run (binary; no specific PKG-041 slice extracted) |
| Engine / generator / packaged-enclosure standards (e.g., ISO 8528-series; CSA/IEC equivalents); fuel-gas-train standards | Likely governing for FAT/SAT and packaged-generator acceptance (ASSUMPTION) | `location TBD`; not cited in accessible sources |

## Verification

| Requirement | Verification approach |
|---|---|
| REQ-041-06-01 | Inspection of completed vendor document review and comment log; cross-reference each logged entry against vendor submittals in `DEL-041-05`. |
| REQ-041-06-02 | Inspection of completed vendor package acceptance and turnover checklist; verify every checklist line has a human-signed disposition. |
| REQ-041-06-03 | Inspection of factory/shop test and inspection evidence (witnessed test reports, certificates, punch-list closeout). |
| REQ-041-06-04 | Trace each of the twelve PKG-041 interface types to at least one accepted evidence item; gaps recorded as `TBD` / open punch. |
| REQ-041-06-05 | Verify vendor nameplate / certified data confirms which electrical architecture is supplied (LV standby per DBM, or 13.8 kV / 3 MW per workbook title) and flag inconsistency for human ruling. |
| REQ-041-06-06 | Verify vendor fuel-gas-system data (operating pressure, design flow, start-gas flow, local filtration) against the DBM fuel-gas interface values. |
| REQ-041-06-07 | Verify physical envelope, anchorage, walkway clearance, and lift provisions against DBM enclosure expectations. |
| REQ-041-06-08 | Audit: every named open parameter has a definite value in vendor data or an explicit TBD on the punch list. |
| REQ-041-06-09 | Audit: every accepted item carries source citation; otherwise marked `TBD`. |
| REQ-041-06-10 | Audit: only human-signed records carry acceptance authority. |
| REQ-041-06-11 | Recheck after standards source slices become locally accessible; convert ASSUMPTION items to source-anchored requirements at that time. |

## Documentation

The deliverable shall be documented by:
- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` (this four-document kit).
- Registered artifacts (planned filenames; ASSUMPTION on exact paths):
  - `vendor-document-review-log.md` / `.csv` (`ART-9E33107762`)
  - `vendor-package-acceptance-and-turnover-checklist.md` / `.csv` (`ART-0E8BDED2A8`)
  - `factory-shop-test-and-inspection-evidence/` folder of vendor-supplied PDFs and a manifest (`ART-53AD41FE27`)
- `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_CONTEXT.md` (metadata; not modified by this skill beyond safe `_STATUS.md` update).
