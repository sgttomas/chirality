# Specification — DEL-069-05 Vendor Document Turnover Package

## Scope

This specification governs the **vendor document turnover package** to be produced by the Package Vendor for **PKG-069 Mole Sieve Drier Unit (Gas)**, including the vendor document register, vendor submittals, source vendor document table rows retained as artifacts where available, and the final turnover records, subject to EPC Integrator interface/integration review.

**In scope:**
- Vendor document register and its maintenance through the project lifecycle.
- Vendor submittal package (drawings, datasheets, calculations, manuals, certifications, test records) for the equipment scope listed in the Datasheet.
- Source vendor document table rows preserved as evidence/artifacts (per `_CONTEXT.md` Notes).
- Final turnover records suitable for mechanical-completion handover and operations/maintenance use.

**Out of scope (not this deliverable):**
- Vendor scope-of-work definition (covered by DEL-069-01).
- Package datasheet (covered by DEL-069-02).
- Construction work package (covered by DEL-069-03).
- Vendor-engineered-equipment package (covered by DEL-069-04).
- EPC review acceptance record (covered by DEL-069-06).

## Requirements

| ID | Requirement | Source / Basis |
|---|---|---|
| REQ-VDT-01 | The Package Vendor shall maintain a **Vendor Document Register** listing every document required by the purchase contract, with at minimum: document number, title, current revision, status (issued for review / approved / as-built), submittal transmittal reference, and turnover status. | _CONTEXT.md Anticipated Artifacts; ASSUMPTION for column set (industry-standard VDR composition; project-specific column set TBD pending Workbook Packages row 73). |
| REQ-VDT-02 | The vendor document submittal scope shall cover the molecular-sieve drier unit equipment list per DBM equipment-by-package table row 56 (PKG-069), including tags AC-6180-1, K-6190-1, K-6195-1, F-5910-1, F-5920-1, F-6151-1, F-6155-1, E-6170-1, V-6160-1, V-6130-1, V-6140-1, V-6150-1, V-6185-1. | DBM-Deepcut/4-25_Deepcut_DBM.md line 2607 |
| REQ-VDT-03 | Vendor submittals for the adsorber vessels (V-6130-1, V-6140-1, V-6150-1 — three driers per DBM "Adsorber vessels" basis) shall include code certifications appropriate to the 900# flange rating service required by the molecular sieve system. | DBM-Deepcut/4-25_Deepcut_DBM.md lines 628, 1263; vessel-to-tag mapping ASSUMPTION (DBM does not enumerate tag-to-function mapping for V-6130/40/50; classification by quantity match — 3 driers, 3 V-tags in 6130 series). |
| REQ-VDT-04 | Vendor documentation shall include adsorbent specification confirming **3A molecular sieve** with silica gel protective layer; 4A and 5A adsorbents are not permitted. | DBM-Deepcut/4-25_Deepcut_DBM.md lines 1269, 1270 |
| REQ-VDT-05 | Vendor documentation shall include process guarantees and acceptance criteria covering at minimum: bed pressure drop (SOL <4 psid; EOL incl. vessel nozzles <10 psid), molecular-sieve regeneration thermal efficiency target (<40%), adsorbent life basis (typical 3 years, with 5-year extension TBC), and outlet water content (expected <0.1 ppmv H2O / dewpoint < -90 degC; maximum <1 ppmv / dewpoint -75 degC; required value TBD). | DBM-Deepcut/4-25_Deepcut_DBM.md lines 1254, 1268, 1271, 1272 |
| REQ-VDT-06 | Vendor documentation shall include the regeneration loop equipment design basis: regeneration gas compressor (single-stage vertical inline centrifugal, 25 MMSCFD basis, 2 x 100% with installed standby), regeneration gas heater (BEU shell-and-tube; regeneration temperature unresolved between 450 degF and 460 degF — CONFLICT to be ruled), regeneration gas cooler, regeneration gas scrubber, and recycle return arrangement. | DBM-Deepcut/4-25_Deepcut_DBM.md lines 1279, 1280, 1281, 1282, 1283 |
| REQ-VDT-07 | Vendor documentation shall include controls and protection deliverables consistent with the molecular-sieve dehydration controls basis: operator-initiated HMI blowdown only; separate adsorption and regeneration blowdown valves; 50 psi/min depressurization rate limit; regeneration compressor automated blowdown on start; compressor seal vent to flare with pressure monitoring; regeneration compressor bypass to prevent reverse rotation. | DBM-Deepcut/4-25_Deepcut_DBM.md line 1361 |
| REQ-VDT-08 | All vendor documents shall be submitted in a revision-controlled, transmittal-tracked workflow. The vendor shall accept and re-issue documents in response to EPC Integrator review comments until acceptance. | _CONTEXT.md ResponsibleParty; ASSUMPTION on review/comment cycle mechanics (project document control procedure TBD). |
| REQ-VDT-09 | The final turnover record set shall be sufficient to support mechanical completion certification and to enable operations and maintenance use, including: as-built drawings, vendor manuals (operating, maintenance, troubleshooting), vendor data books, spare parts and consumables lists, certificates of conformity, inspection and test reports, and welding/NDE records as applicable. | ASSUMPTION (standard EPC turnover-record composition; specific list TBD pending Workbook Packages row 73 and project document control matrix). |
| REQ-VDT-10 | Source vendor document table rows shall be preserved as **artifacts/evidence** within the deliverable, not promoted to separate deliverables. | _CONTEXT.md Notes |

## Standards

| Standard | Applicability | Location |
|---|---|---|
| ASME BPVC Section VIII Div. 1 (or local equivalent) and BC CRN | Adsorber vessels, regeneration scrubber, and other pressure-containing vendor-supplied vessels | ASSUMPTION (location TBD); explicit ASME U-Stamp / BC CRN requirement is stated for BAHX in the same DBM (line 1324); molecular-sieve vessels are not separately enumerated. |
| ALPEMA / vendor exchanger standards | Regeneration heater and cooler (if BAHX-class apparatus); otherwise vendor shell-and-tube standards | DBM line 1280 identifies BEU shell-and-tube for regen heater; ALPEMA applicability ASSUMPTION. |
| Project document control / vendor document procedure | Submittal workflow, transmittal numbering, document-status enums, turnover index format | location TBD — project procedure not in accessible sources. |
| Workbook Packages row 73 vendor document list | Authoritative list of required vendor documents for this package | location TBD — `_Sources/26020-Packages_Interfaces_4_export.xlsx` is binary and was not text-extracted. |

## Verification

| Requirement | Verification Approach |
|---|---|
| REQ-VDT-01 | Document control audit of the Vendor Document Register at each submittal milestone; reconciliation against Workbook Packages row 73 required document list once locally extracted. |
| REQ-VDT-02 | Tag-completeness check against DBM equipment-by-package row 56 tag list (Datasheet > Construction). |
| REQ-VDT-03 | Verification of vessel certifications (U-Stamp / CRN, MTRs, hydrotest reports) on receipt of submittal. |
| REQ-VDT-04 | Adsorbent vendor certificate review (grade confirmation, silica gel layer included). |
| REQ-VDT-05 | Vendor guarantee letter and test data review against the listed acceptance criteria; FAT and SAT records where applicable. |
| REQ-VDT-06 | Equipment datasheet review and regen-loop heat & material balance check by EPC Integrator. |
| REQ-VDT-07 | Cause-and-effect / SAFE chart review against DBM molecular-sieve controls basis. |
| REQ-VDT-08 | Transmittal log audit; closure of review-comment registers. |
| REQ-VDT-09 | Turnover index walkthrough at mechanical completion; signoff against the turnover checklist. |
| REQ-VDT-10 | Artifact retention audit — source rows present in the artifact set; absence of standalone duplicate deliverables. |

## Documentation

The following documents are expected as the deliverable artifact set (per `_CONTEXT.md` Anticipated Artifacts):

- Vendor Document Register (master VDR).
- Vendor Document Submittals (issued documents per the register).
- Source Vendor Document Table Rows (artifacts/evidence).
- Turnover Records (mechanical completion / operations handover packet).

Specific document codes (e.g., MAN-xxx, DRG-xxx, CERT-xxx) are **TBD** pending project document control numbering convention and Workbook Packages row 73 extraction.
