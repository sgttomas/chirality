# Procedure — DEL-053-05 Vendor Document Turnover Package (Flare KO Drum, Cryo)

> Operational procedure for producing, reviewing, and turning over the vendor documentation set for PKG-053. Stepwise sequencing is normative where source-supported; vendor schedule details remain TBD.

## Purpose

Establish a repeatable sequence by which the Package Vendor assembles required documents, EPC Integrator reviews them, and the consolidated set is turned over via the Final Vendor Data Book (PRQ-016).

## Prerequisites

| Prerequisite | Source / Status |
|---|---|
| DEL-053-01 Scope of Work issued (defines EPC/Vendor split, package boundary) | DELIVERABLE_REGISTER.csv DEL-053-01 (ASSUMPTION: upstream sequencing) |
| DEL-053-02 Package Datasheet issued (technical handoff, interface facts) | DELIVERABLE_REGISTER.csv DEL-053-02 (ASSUMPTION: upstream sequencing) |
| Vendor award and Vendor Document Control Procedure (DOC-008) in place | ARTIFACT_REGISTER.csv ART-E1545FE7B1 |
| Vendor Document Index (PRQ-009) prepared | ARTIFACT_REGISTER.csv ART-BE9ACF9A83 |
| Project document-control infrastructure (transmittals, numbering, retention) | TBD (location TBD) |
| ITP (QLT-003) reviewed and accepted with EPC witness/hold-points | ART-459B3C4CAD |
| Access to project sources: `26020-Package_Requirements.docx` (heading 8); DBM-Deepcut cryogenic flare row; PACKAGE_REGISTER.csv row 53 | `_REFERENCES.md` |

## Steps

### Step 1 — Initialize the Vendor Document Register
1.1 Vendor populates the register from PRQ-009 Vendor Document Index, covering every row of the source Vendor Engineering Deliverables table (cross-walked against ARTIFACT_REGISTER.csv DEL-053-05).
1.2 Each row records: Source Doc Ref, Vendor Document Number, Title, Category, planned submittal date, revision.
1.3 Rows whose categories are not in vendor scope (per DEL-053-01) are flagged N/A with rationale rather than omitted.

### Step 2 — Issue Document Control Procedure
2.1 Vendor issues DOC-008 (ART-E1545FE7B1) for EPC review.
2.2 EPC reviews; comments incorporated; baseline revision accepted before substantive document submittals.

### Step 3 — Engineering and design documents (Core package engineering, Static pressure, Relief/Flare)
3.1 Vendor issues for review:
   - MEC-001 Mechanical Design Basis; MEC-002 Equipment List; MEC-003 Equipment Data Sheets.
   - MEC-005 Static Equipment Specifications; MEC-009 Pressure Vessel Data Sheets; MEC-014 Mechanical Calculation Package.
   - PRO-014 Relief and Flare Design Basis; PRO-015 PSV Sizing; PRO-016 Relief Valve Data Sheets; PRO-017 Flare Load Summary; PRO-018 Blowdown / Depressurization Study.
3.2 Cryogenic-service inputs (sub -45.5 degC MDMT, 304SS 610 mm cryogenic flare header context) are confirmed against the DBM cryogenic flare row before sizing/data sheets are finalized.
3.3 EPC reviews; vendor incorporates comments; revisions advance toward IFC.

### Step 4 — Drawings and arrangement documents
4.1 Vendor issues for review:
   - MEC-016 Equipment GA Drawing; MEC-017 Installation/Setting Drawings; MEC-018 Lifting/Handling Study.
   - PIP-006 Equipment Arrangement / Piping GA; PIP-007 Piping Plans and Sections; PIP-008 Piping Isometrics; PIP-009 Fabrication Isometrics with BOM.
   - Structural drawings (GA, foundation, anchor bolt, platform/access, lifting lug) per ARTIFACT_REGISTER structural rows.
4.2 EPC reviews against DEL-053-02 interface facts and DEL-053-03 construction work package; tie-in alignment verified via PIP-004 Tie-In List.

### Step 5 — I&C and electrical interface documents
5.1 Vendor issues:
   - INS-002 Index, INS-003 Data Sheets, INS-005..INS-029 interface set; INS-016/017 valve data sheets.
   - CTL-003 Control Narrative; CTL-005 Cause and Effect Matrix; CTL-006 DCS I/O List; CTL-026 Package Vendor Interface Specification.
   - Electrical artifacts per ARTIFACT_REGISTER (Load List, SLDs, Cable Schedule, Layout, Interconnection, FAT/SAT, Energization, Heat Tracing, Grounding).
5.2 CTL-026 / CTL-006 are cross-checked against the DEL-053-02 interface facts (workbook X-column rows). Discrepancies are surfaced via the Guidance.md Conflict Table, not silently reconciled.

### Step 6 — Quality and pre-fabrication submittals
6.1 Vendor issues QLT-006 Supplier Quality Plan and QLT-003 ITP.
6.2 EPC reviews ITP and confirms witness/hold/review points; signed ITP returns to vendor.
6.3 If R-4 applies, the Pressure Equipment Registration Package (REG-022) is compiled from MEC-009 and MEC-014 and submitted to the jurisdictional authority (timing: pre-fabrication).

### Step 7 — Fabrication-phase evidence
7.1 During fabrication, vendor accumulates:
   - QLT-013 Material Test Reports / Certificates (including impact-test results for cryogenic-MDMT components).
   - Weld maps, NDE records, dimensional inspection records.
7.2 EPC executes witness/hold points per the accepted ITP.

### Step 8 — FAT and inspection release
8.1 Vendor issues MEC-021 FAT Procedure; EPC reviews and signs.
8.2 FAT executed; MEC-022 FAT Report issued.
8.3 QLT-020 Inspection Release Certificate issued upon successful FAT and inspection completion.

### Step 9 — Logistics and spares
9.1 PRQ-013 Logistics / Shipping Plan and PRQ-015 SPIR issued for EPC review.
9.2 MEC-024 Mechanical Spares / Special Tools Requirements issued.

### Step 10 — Operations and maintenance documentation
10.1 MEC-025 Mechanical Equipment IOM Manual issued.
10.2 Any vendor-supplied operating procedures bundled for inclusion in turnover.

### Step 11 — As-Built and final revisions
11.1 Post-fabrication and post-installation revisions are issued (PIP-028 Piping As-Built, INS-029 Instrument As-Built).
11.2 All documents reach their final revision and are flagged in the register.

### Step 12 — Manufacturing Record Book and Vendor Data Book assembly
12.1 Vendor compiles QLT-021 Manufacturing Record Book during fabrication.
12.2 Vendor compiles PRQ-016 Final Vendor Data Book consolidating: final-revision drawings/data sheets, MTRs, NDE reports, weld maps, FAT reports, calibration certificates, inspection release, REG-022 outcome (where applicable), IOM, SPIR, logistics, and all index/control documents.
12.3 PRQ-016 is the single binding turnover artifact.

### Step 13 — EPC review-and-acceptance handoff
13.1 The completed PRQ-016 and the closed-out register are presented to EPC Integrator under DEL-053-06 (EPC Vendor Package Review and Acceptance).
13.2 EPC review log, package acceptance checklist, and turnover evidence are recorded under DEL-053-06, not under this deliverable.

### Step 14 — Closeout of the vendor document register
14.1 Every register row reaches one of: Final/Accepted, N/A (with rationale), or Open-Item (with target closure).
14.2 Open-items at handoff are recorded in the DEL-053-06 acceptance evidence per OBJ-010 closure expectations. Source: PROJECT_DECOMP OBJ-010.

## Verification

| Check | Method |
|---|---|
| Every ARTIFACT_REGISTER DEL-053-05 row is represented in the register | Cross-walk worksheet |
| All documents in scope reached final revision | Register Revision column inspection |
| EPC review status reached "Reviewed-No-Comment" or "Reviewed-With-Comment (incorporated)" for all in-scope documents | Register Review Status column |
| ITP hold/witness points were executed | Signed ITP returns |
| Cryogenic-service documents reflect sub -45.5 degC basis | Spot-check MEC-009, PRO-015, PRO-018 against DBM-Deepcut cryogenic flare row |
| Interface documents align with DEL-053-02 interface facts | Cross-walk CTL-006/CTL-026 vs. DEL-053-02 interface evidence |
| Final Vendor Data Book (PRQ-016) is complete and EPC-accepted | DEL-053-06 acceptance record |
| No vendor-document row was promoted to a separate deliverable | Audit DELIVERABLE_REGISTER.csv PKG-053 set |

## Records

| Record | Where Held |
|---|---|
| Vendor Document Register (working) | This deliverable; register artifact ART-C0B3DA97E7 |
| Individual document submittals | This deliverable as artifacts (ART-* rows per ARTIFACT_REGISTER) |
| Transmittal log | Vendor document control system (location TBD) |
| Review comments / dispositions | Vendor document control system; summarized in register Review Status |
| Witness/hold-point execution evidence | ITP returns (artifact under QLT-003) |
| Final Vendor Data Book (PRQ-016) | This deliverable (final artifact); referenced by DEL-053-06 acceptance |
| Turnover acceptance | DEL-053-06 (not this deliverable) |
| Pressure equipment registration certificate (if applicable) | REG-022 artifact (ART-97212D01B9) |
