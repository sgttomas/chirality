# Procedure — DEL-079-06 EPC Vendor Package Review and Acceptance

## Purpose

Operate the EPC Integrator's review and acceptance loop for the PKG-079 Instrument Air Building vendor package, producing the four artifacts listed in `_CONTEXT.md` (vendor document review log, package acceptance checklist, test/inspection evidence, turnover evidence) against the EPC anchor deliverables (DEL-079-01, DEL-079-02, DEL-079-03) and the vendor deliverables (DEL-079-04, DEL-079-05). Source: `_CONTEXT.md` Scope; DELIVERABLE_REGISTER PKG-079.

## Prerequisites

- EPC Package Datasheet (DEL-079-02) issued at a revision the vendor is working to. Source: DELIVERABLE_REGISTER PKG-079.
- EPC Scope of Work (DEL-079-01) issued. Source: DELIVERABLE_REGISTER PKG-079.
- EPC Construction Work Package (DEL-079-03) issued or in-progress with the construction interface/turnover checklist (ART-10C3D82526) defined. Source: ARTIFACT_REGISTER ART-10C3D82526.
- Vendor Engineered Equipment Package (DEL-079-04) and Vendor Document Turnover Package (DEL-079-05) submitted by the Package Vendor. Source: DELIVERABLE_REGISTER PKG-079.
- Access to source materials referenced in `_REFERENCES.md` (Workbook Packages row 69; `26020-Package_Requirements.docx` package heading 32; RFQ `26020-01-PT-RFQ-39-001_Instr_Air_Bldg_R1.docx`; `DBM-Deepcut/4-25_Deepcut_DBM.md`). Acceptance steps that require source-text resolution remain `TBD` if those slices are not locally available.
- No declared upstream blockers (per `_DEPENDENCIES.md` Declared Upstream Dependencies: none declared).

## Steps

1. **Initialize the acceptance workspace.**
   - Confirm `_STATUS.md` indicates a state that permits work (`OPEN` or `INITIALIZED`).
   - Create the four artifact stubs in this deliverable folder: vendor document review log, package acceptance checklist, test/inspection evidence record, turnover evidence record. (Each stub is bounded to this deliverable folder.)
2. **Load the acceptance basis.**
   - Read DEL-079-01 (Scope of Work), DEL-079-02 (Package Datasheet), and DEL-079-03 (Construction Work Package) at their current as-issued revisions. Note revisions in the acceptance checklist header.
   - Extract from SCOPE_LEDGER PKG-079 the SOW-0131..SOW-0134 acceptance criteria (equipment count/ratings, pressures, dew point, design conditions, by-others carve-outs).
   - Extract from INTERFACE_REGISTER PKG-079 the ten interface IDs (IFC-E7D3353482 .. IFC-0EC9E5E722) and seed one acceptance checklist row per interface.
3. **Build the vendor document review log.**
   - Enumerate vendor documents from DEL-079-05's vendor document register (ART-95A888C02E) and from each vendor document category (e.g., ART-33E3E7FE46 Core vendor documents, plus child rows ART-F8BF3DB9AA Vendor Document Index, ART-D103DDD65D Vendor Document Control Procedure, ART-CACD5074F8 Supplier Quality Plan).
   - For each row, capture: document title, source ID (e.g., PRQ-009, DOC-008, QLT-006), received revision, reviewer, review date, disposition (ACCEPTED / ACCEPTED WITH COMMENTS / REJECTED), comment-resolution reference.
4. **Execute equipment count/rating review (Specification R2).**
   - Reconcile vendor general arrangement and equipment list against SOW-0132/SOW-0133: 2 compressors at 1113 SCFM @ 861 kPag, 2 x 250 HP motors (soft-start/VFD-ready, anti-condensation heaters), 1 wet receiver, 2 dryer pre-filters, 1 regenerative desiccant dryer (2 towers, 100%), 1 after-filter, 1 (or 2 x 50%) dry receivers. Record disposition per item.
5. **Execute pressure and dew-point verification (R3).**
   - Verify PSV nameplate setpoints = 948 kPag (137.5 psig).
   - Verify delivered air max dew point = -73.3 °C at 1000 kPag via dryer FAT or performance curve.
   - Verify compressor max discharge / shutdown ≤ 1000 kPag; system design ≤ 1034 kPag (150 psig); system min 551 kPag (80 psig); facility shutdown 482 kPag (70 psig); design temperature -40 °C to 38 °C envelope.
6. **Execute electrical driver verification (R4).**
   - Reconcile motor data sheet against 200-250 HP, 600 V / 3PH / 60 Hz, TEFC, non-classified, soft-start or VFD-ready. Speed is vendor-determined; do not flag as nonconformance unless DEL-079-02 fixes a value.
7. **Close interface rows (R5).**
   - For each of the ten PKG-079 interface IDs, record evidence (vendor drawing or EPC interface confirmation) and closure status: CLOSED / OPEN / WAIVED (with reason). Acceptance is not completed while any interface is OPEN without an authorized waiver.
8. **Capture test/inspection evidence (R7).**
   - Attach or reference FAT and SAT records, PSV calibration certificates, dryer performance/dew-point records, and motor commissioning records. Where the project FAT/SAT split is not stated in accessible sources, mark TBD pending DEL-079-02 issuance or human ruling.
9. **Capture turnover evidence (R8).**
   - Cross-walk turnover documentation against ART-10C3D82526 Construction Interface and Turnover Checklist. Record any gaps as OPEN items with owner and target date.
10. **Compile the acceptance disposition.**
    - Roll up all acceptance checklist rows into an overall package disposition: ACCEPTED / ACCEPTED WITH COMMENTS / REJECTED. Any REJECTED row blocks overall acceptance unless explicitly waived.
11. **Apply source-fidelity discipline (R9).**
    - Confirm every acceptance row cites SOW-013x, IFC-*, ART-*, or a vendor document ID. Replace unverifiable inferences with `TBD`; label vendor-side judgement calls `ASSUMPTION` where retained.
12. **Update lifecycle state.**
    - On submission of the completed artifact set for human review, request the human-authorized `_STATUS.md` transition. Do not author binding acceptance approvals within this procedure (K-AUTH-1).

## Verification

| Step | Verification Check |
|---|---|
| 1 | Four artifact stubs exist in `{DELIVERABLE_PATH}` and contain headings only — no fabricated content. |
| 2 | Acceptance checklist header lists the current as-issued revisions of DEL-079-01/02/03 and references the SOW and IFC source rows. |
| 3 | Vendor document review log row count is ≥ the count of source vendor-document rows in ARTIFACT_REGISTER PKG-079 for DEL-079-05. |
| 4-6 | Each verification row cites the SOW row (SOW-0132/0133/0134) or DEL-079-02 datasheet requirement it satisfies. |
| 7 | Exactly ten interface closure rows, one per IFC-* listed for PKG-079, each with a closure status. |
| 8-9 | Each evidence reference resolves to a real attachment, vendor document ID, or `TBD` with the reason for the gap. |
| 10 | Package disposition is consistent with the row-level dispositions (no overall ACCEPTED while any row is REJECTED without waiver). |
| 11 | No acceptance row is unsourced; `ASSUMPTION` and `TBD` are explicit where used. |
| 12 | `_STATUS.md` transition is requested via the human approval path; no agent-authored acceptance approval (K-AUTH-1). |

## Records

The following records SHALL exist in this deliverable folder upon completion:

- `Datasheet.md` (this set).
- `Specification.md` (this set).
- `Guidance.md` (this set).
- `Procedure.md` (this set).
- Vendor document review log artifact.
- Package acceptance checklist artifact (with SOW, interface, and equipment-condition rows).
- Test/inspection evidence record.
- Turnover evidence record.
- `_run_records/TASK_RUN_*.md` for each TASK invocation that touched this deliverable.
- Updated `_STATUS.md` reflecting authorized lifecycle transitions only.
