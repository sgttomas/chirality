# Specification — DEL-056-05 Vendor Document Turnover Package (PKG-056 Inlet Separators 4-25)

## Scope

### In Scope

This specification governs the **Vendor Document Turnover Package** for the PKG-056 Inlet Separators 4-25 package. It specifies:

- the master vendor document register (VDR) the Package Vendor shall maintain and submit;
- the required vendor documents and submittals produced by the Package Vendor through engineering, fabrication, inspection, test, FAT, shipment, site installation, commissioning, and turnover;
- the source-required vendor documentation explicitly mandated by `26020-Package_Requirements.docx` heading 11 (location TBD — package-specific list to be reconciled when source extracted);
- the turnover records, certifications, and as-built documentation issued at handover from Package Vendor to EPC Integrator and Owner;
- the EPC Integrator review/acceptance interface against vendor documents (review status codes only; the acceptance decision deliverable itself is `DEL-056-06`).

Scope items covered: `SOW-0127`, `SOW-0128`, `SOW-0129`, `SOW-0130` (per `_CONTEXT.md`).

### Out of Scope

- Authoring of EPC Integrator deliverables (Scope of Work `DEL-056-01`, Package Datasheet `DEL-056-02`, Construction Work Package `DEL-056-03`, EPC Vendor Package Review and Acceptance `DEL-056-06`).
- Engineering of the physical equipment package itself (`DEL-056-04`).
- Generation of individual source vendor documents as separate decomposition deliverables (these remain artifacts/evidence per `_CONTEXT.md` Notes).

## Requirements

### R1 — Master Vendor Document Register (VDR)

R1.1 The Package Vendor shall maintain a master Vendor Document Register that indexes every vendor document for PKG-056. (**Source:** `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617 — "Package deliverables shall include … vendor document registers".)

R1.2 The VDR shall record, for each document at minimum: document number, title, revision, status (planned / issued / approved / as-built), transmittal number, issue date, EPC review code, and turnover-status flag. (**ASSUMPTION** — standard vendor-document register convention; package-specific minimum fields TBD pending `26020-Package_Requirements.docx` heading 11.)

R1.3 The VDR shall be re-issued at each submittal milestone and at final turnover. (**ASSUMPTION** — typical vendor submittal practice; specific cadence TBD pending heading 11.)

### R2 — Required Vendor Documents (Cross-Package Baseline)

R2.1 The vendor document set shall include, at minimum:

- equipment and process datasheets;
- cause-and-effect inputs;
- utility load summaries;
- relief/load data;
- field tie-in lists;
- operating and design envelopes;
- sparing philosophy;
- materials and coating basis;
- maintenance access drawings/notes;
- shipped-loose item lists;
- vendor document register (per R1).

(**Source:** `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617.)

R2.2 The vendor document set shall additionally satisfy the package-specific required-document list at `26020-Package_Requirements.docx` heading 11. **Location TBD** until that source is extracted; when extracted, heading 11 governs over R2.1 where they differ.

### R3 — Submittal Lifecycle and Status Codes

R3.1 Each vendor document shall progress through a defined submittal lifecycle: Issue-for-Review → Issue-for-Approval → Issue-for-Construction → As-Built / Turnover. (**ASSUMPTION** — standard mechanical-package submittal lifecycle; package-specific lifecycle and status codes TBD pending heading 11.)

R3.2 EPC review codes shall be assigned by the EPC Integrator for each vendor document submittal and recorded against the VDR row. The specific review code set used by EPC for PKG-056 is **TBD** (defined by EPC project document control procedure, not by the Package Vendor specification).

### R4 — Source-Required Documentation

R4.1 Every vendor document explicitly required by `26020-Package_Requirements.docx` heading 11 shall be produced, submitted, reviewed, and included in turnover. (**Location TBD** until extraction.)

R4.2 Where a source-required document corresponds to an existing artifact row in `ARTIFACT_REGISTER.csv` (e.g., ART-* rows under DEL-056-05 when populated), the vendor document shall carry that artifact identity in the VDR. **TBD** — no DEL-056-05-specific artifact rows are populated in the current `ARTIFACT_REGISTER.csv` snapshot (only `DEL-056-01` / `DEL-056-02` artifact rows are present).

### R5 — Turnover Records

R5.1 At final turnover the Package Vendor shall deliver, at minimum:

- certified equipment nameplate photographs;
- material test reports (MTRs) for code materials;
- pressure-test (hydrotest) reports for vessels and pressure piping;
- NDE reports (RT/UT/MT/PT) per applicable code;
- heat-treatment records (where PWHT applied);
- coating-application QA records (Devchem 253 internal coating on vessels — `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 646);
- ASME Code stamp documentation and CRN/jurisdictional registration certificates for code vessels;
- factory acceptance test (FAT) reports;
- instrument calibration certificates;
- as-built/certified-final drawings;
- vendor certificate of conformance.

(**ASSUMPTION** — typical mechanical-package turnover record set; package-specific turnover record list TBD pending `26020-Package_Requirements.docx` heading 11.)

R5.2 Turnover records shall be cross-referenced by tag number for V-1600-1 and V-1700-1 and any associated tagged equipment within the package boundary. (**Source:** `ARTIFACT_REGISTER.csv` ART-ECFD6FDCD9; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.)

### R6 — As-Built Documentation

R6.1 Marked-up redlines from site installation and commissioning shall be incorporated into final certified drawings. (**ASSUMPTION** pending heading 11.)

R6.2 The final certified document set shall match the as-installed configuration including any approved deviations. (**ASSUMPTION** pending heading 11.)

### R7 — EPC Interface

R7.1 All vendor documents shall be transmitted to the EPC Integrator using the project document-control transmittal mechanism. (**TBD** — EPC project document-control procedure not in scope of this deliverable's source set.)

R7.2 The Package Vendor shall not require Owner sign-off; the EPC Integrator's review-and-acceptance deliverable (`DEL-056-06`) is the binding acceptance record. (**Source:** `_CONTEXT.md` ResponsibleParty; `DELIVERABLE_REGISTER.csv` row for DEL-056-05 and DEL-056-06.)

## Standards

| Standard / Source | Applies to | Status |
|---|---|---|
| `26020-Package_Requirements.docx` heading 11 | Package-specific required-document list and turnover content | **location TBD** — DOCX not locally extracted at time of drafting |
| ASME Section VIII Div. 1 (vessels) | Material test reports, NDE, hydrotest, U-stamp documentation | ASSUMPTION — implied by coded HP separator service; not explicitly stated for DEL-056-05 in accessible sources |
| Provincial / jurisdictional CRN registration | Vessel registration certificates | ASSUMPTION — implied for BC service; explicit source TBD |
| ALPEMA / API references (where called by other deliverables) | Cross-deliverable consistency only | Out of direct scope; cited only for context |
| Project document-control procedure (EPC) | Transmittal format, review codes, revision control | **TBD** — referenced procedure not in this deliverable's source set |

## Verification

| Requirement | Verification Approach |
|---|---|
| R1 (VDR) | EPC Integrator confirms the VDR exists, indexes every issued vendor document, and is re-issued at each milestone and at turnover |
| R2 (Required documents) | EPC Integrator compares delivered document set against R2.1 baseline list and heading 11 list (when extracted); gaps logged in EPC review |
| R3 (Submittal lifecycle) | Review-code progression visible in successive VDR revisions |
| R4 (Source-required) | Cross-check of vendor submissions against `26020-Package_Requirements.docx` heading 11 once extracted |
| R5 (Turnover records) | Turnover record book audit by EPC Integrator and Owner; certificate of conformance signed by Package Vendor |
| R6 (As-built) | Visual comparison of certified-final drawings against site walkdown; redline trace from IFC to certified |
| R7 (EPC interface) | All transmittals logged in EPC document control; final acceptance recorded in `DEL-056-06` |

## Documentation (Required Artifacts)

Per `_CONTEXT.md` anticipated artifacts:

- Vendor document register
- Vendor document submittals
- Source vendor document table rows as artifacts where available
- Turnover records

Note: `ARTIFACT_REGISTER.csv` in the GATE-07 snapshot does not yet contain DEL-056-05-specific artifact rows (`TBD` — artifact rows expected to be populated when `26020-Package_Requirements.docx` heading 11 is extracted and individual source-required vendor documents are catalogued).
