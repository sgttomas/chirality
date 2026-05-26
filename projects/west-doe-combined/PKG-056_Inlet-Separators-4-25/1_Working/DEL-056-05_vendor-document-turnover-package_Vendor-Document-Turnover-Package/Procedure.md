# Procedure — DEL-056-05 Vendor Document Turnover Package (PKG-056 Inlet Separators 4-25)

## Purpose

This procedure describes how to **produce** the Vendor Document Turnover Package for PKG-056 (Package Vendor responsibility) and how the EPC Integrator **uses/reviews** it through the package lifecycle. Producing this deliverable means establishing the master Vendor Document Register, issuing each required vendor document through its submittal lifecycle, capturing turnover records, and transferring the documented package to EPC and Owner.

## Prerequisites

### Inputs / Upstream

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` for this deliverable.
- Accepted PROJECT_DECOMP snapshot: `GATE-07_Final_Published_2026-05-24/`.
- Package-specific required-document list at `26020-Package_Requirements.docx` heading 11. **Location TBD** — content not extracted at time of drafting; resolve before final document set is closed.
- Cross-package baseline of package deliverables (`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617).
- EPC project document-control procedure (transmittals, review codes, revision control). **TBD** — referenced but not in this deliverable's source set.
- Sibling deliverables for cross-reference: `DEL-056-01` Scope of Work, `DEL-056-02` Package Datasheet, `DEL-056-04` Vendor Engineered Equipment Package, `DEL-056-06` EPC Vendor Package Review and Acceptance.

### Declared Dependencies

Per `_DEPENDENCIES.md`: no upstream/downstream dependencies declared during PREPARATION. Functional couplings to `DEL-056-04` (engineered equipment package) and `DEL-056-06` (EPC review and acceptance) exist and should be added when `dependency-extract` is run.

### Required References (locally accessible)

- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (cross-package basis)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (inlet separator system context)
- GATE-07 snapshot registers: `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`

## Steps

### Step 1 — Establish the Vendor Document Register (VDR)

1. Package Vendor instantiates a master VDR for PKG-056 covering all anticipated vendor documents.
2. Each VDR row includes (at minimum, per R1.2): document number, title, revision, status, transmittal number, issue date, EPC review code, turnover-status flag.
3. Initial VDR is issued to the EPC Integrator at project kickoff for that package.

### Step 2 — Reconcile Source-Required Documents

1. Extract the package-specific required-document list from `26020-Package_Requirements.docx` heading 11. **TBD** — extraction action pending.
2. Compare heading 11 list against the cross-package DBM baseline (line 617) and against the VDR.
3. Add any heading-11-only documents to the VDR; flag any baseline document not required by heading 11 for EPC ruling.
4. Where heading-11 documents map to artifact rows in `ARTIFACT_REGISTER.csv`, record the artifact ID against the VDR row.

### Step 3 — Issue Engineering Documents (Issue-for-Review)

1. Vendor issues engineering documents (datasheets, calculations, GAs, P&IDs, instrument lists, electrical schematics, cause-and-effect inputs, utility load summaries, relief/load data) as IFR.
2. Each issuance updates the VDR (revision and status).
3. EPC Integrator returns review codes; Vendor disposes comments and re-issues as IFA.

### Step 4 — Issue Design & Construction Documents (Issue-for-Approval → Issue-for-Construction)

1. Vendor progresses approved IFA documents to IFC.
2. Field tie-in lists, shipped-loose item lists, maintenance access drawings, operating envelopes, sparing philosophy, and materials/coating basis are issued or finalized as IFC content.
3. EPC review codes recorded against the VDR.

### Step 5 — Execute Fabrication, Inspection, and Test (records captured for turnover)

1. Vendor executes fabrication per IFC documents.
2. Material test reports (MTRs), weld procedure records (WPS/PQR), welder qualification, NDE reports (RT/UT/MT/PT), heat-treatment records, and coating-application QA records (Devchem 253, vessels only — `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 646) are captured.
3. Hydrotest and pressure tests executed; certificates issued.
4. ASME Section VIII Div. 1 vessel registration and CRN/jurisdictional registration completed for V-1600-1 and V-1700-1 (and any future-package vessel if authorized). (ASSUMPTION — code applicability not explicitly stated for DEL-056-05.)
5. Factory acceptance tests executed; FAT procedures and reports captured.
6. Instrument calibration certificates captured.
7. Every record above is logged against its VDR row.

### Step 6 — Ship and Install (capture site events)

1. Shipping records, packing lists, and shipped-loose item lists transmitted to EPC.
2. Site installation redlines captured for incorporation into as-builts.

### Step 7 — Commission and Finalize As-Builts

1. Site acceptance test inputs provided; commissioning records captured.
2. Redlines incorporated into final certified drawings.
3. As-built drawings and final certified document set issued.
4. VDR updated to status "As-Built / Turnover" for each document.

### Step 8 — Assemble Turnover Record Book

1. Compile final turnover record set:
   - certified equipment nameplate photographs;
   - MTRs;
   - hydrotest/pressure-test reports;
   - NDE reports;
   - heat-treatment records;
   - coating-application QA records (Devchem 253);
   - ASME Code stamp documentation;
   - CRN/jurisdictional certificates;
   - FAT reports;
   - instrument calibration certificates;
   - as-built/certified-final drawings;
   - vendor certificate of conformance;
   - final VDR.
2. Issue Turnover Record Book to EPC Integrator and Owner per project document-control procedure.

### Step 9 — Support EPC Review and Acceptance

1. Package Vendor supports EPC Integrator's review under `DEL-056-06`.
2. Any review-driven document corrections are revised and reissued; VDR updated.
3. Acceptance is recorded in `DEL-056-06`, not in this deliverable.

## Verification

| Check | How verified | Owner |
|---|---|---|
| VDR exists and is current | EPC document-control walkthrough; VDR version matches latest issuance | EPC Integrator |
| Every R2.1 baseline document is present | Compare delivered set to DBM line 617 list | EPC Integrator |
| Every heading-11 source-required document is present | Compare delivered set to heading 11 list (once extracted) | EPC Integrator |
| Turnover records (R5.1) complete and traceable to tag | Tag-by-tag audit (V-1600-1, V-1700-1) | EPC Integrator + Owner |
| As-builts match site walkdown | Field walkdown vs. certified-finals | EPC Integrator |
| Submittal lifecycle followed | Review-code progression visible in successive VDR revisions | EPC Integrator |
| Code and jurisdictional records present (where applicable) | ASME U-stamp documentation and CRN certificates filed for each coded vessel | EPC Integrator + Owner |

## Records

The following records shall result from execution of this procedure (these are also the turnover deliverables):

- Final Vendor Document Register (VDR) at turnover revision.
- Vendor document submittals (full set, latest approved revision).
- Turnover Record Book containing the artifacts listed in Step 8.
- Vendor certificate of conformance.
- Cross-reference to `DEL-056-06` EPC acceptance record.

Note: Until `26020-Package_Requirements.docx` heading 11 is extracted to markdown and reconciled, the package-specific required-documents list and any heading-11-only turnover records remain **TBD**.
