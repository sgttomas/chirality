# Procedure — DEL-048-05 Vendor Document Turnover Package

This procedure describes how the Package Vendor produces and submits the Vendor Document Turnover Package and how the EPC Integrator receives and reviews it. The acceptance decision itself is recorded under `DEL-048-06`.

## Prerequisites

1. **Upstream inputs in place** (per `_DEPENDENCIES.md`, no upstream edges currently declared; the following are operational prerequisites derived from the sibling EPC anchor deliverables in PKG-048):
   - EPC Scope of Work (`DEL-048-01`) issued.
   - EPC Package Datasheet (`DEL-048-02`) issued.
   - Construction Work Package (`DEL-048-03`) sufficiently mature to anchor turnover content for installation/commissioning interface.
   - Vendor Engineered Equipment Package (`DEL-048-04`) producing the engineering content this turnover compiles.
2. **Vendor Document Control Procedure (DOC-008)** issued and accepted. (`TBD` until issued — see Guidance Conflict Table C-02, C-03, C-04.)
3. **Vendor Document Index (PRQ-009)** initialized with rows for every source-required deliverable enumerated in `Datasheet.md`, reconciled against heading 3 of `26020-Package_Requirements.docx` once extracted (Guidance C-01).
4. **Source slice** `26020-Package_Requirements.docx` heading 3 (Inlet / Sales Compressors) extracted to markdown and available as the authoritative document-scope reference. (Currently `TBD` — slice not yet extracted.)
5. **Interface workbook** (locally: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, row 65) available for cross-checks. See Guidance C-05.
6. EPC Integrator review path and reviewer assignments confirmed (interface to `DEL-048-06`).

## Steps

### Vendor-side steps

#### Step 1 — Initialize the Vendor Document Index (PRQ-009)
1.1. For each source-required ID enumerated in `Datasheet.md` (and reconciled to heading 3), create one row in PRQ-009 with: Source ID, Source Name, Vendor Doc Number (TBD until vendor numbering issued), Title, Discipline group, Unit/duty attribute (inlet vs sales), Planned issue stage(s), Planned issue date(s).
1.2. Reconcile to the source heading 3 table — no rows missing, no extra rows without a scope-change record.

#### Step 2 — Issue the Vendor Document Control Procedure (DOC-008)
2.1. Define numbering scheme, revision states, transmittal mechanics, hold/review codes, and acceptance flow.
2.2. Submit to EPC Integrator for review; reissue at IFC.

#### Step 3 — Stage-by-stage submittal
3.1. For each document in PRQ-009, issue at each stage required by DOC-008 (e.g., Bid -> IFR -> IFA -> IFC -> As-Built — stage labels `ASSUMPTION` pending DOC-008).
3.2. Each submittal carries a transmittal cover sheet citing the documents enclosed, their revision, and the transmittal date.
3.3. Update PRQ-009 with every transmittal event.

#### Step 4 — Quality and inspection evidence
4.1. Maintain the Supplier Quality Plan (QLT-006) and ITP (QLT-003) as the working quality basis.
4.2. As materials are received, file Material Test Reports / Certificates (QLT-013) with explicit NACE compliance flags where the item is in sour-service scope (Specification REQ-12; Guidance C-06).
4.3. At hold points, issue Inspection Release Certificates (QLT-020).
4.4. Build the Manufacturing Record Book / Vendor Data Book (QLT-021) progressively.

#### Step 5 — FAT and energization evidence
5.1. Issue Equipment FAT / Performance Test Procedure (MEC-021) for review and acceptance before FAT.
5.2. Execute FAT for each inlet-duty and sales-duty unit; issue Equipment FAT / Performance Test Report (MEC-022) per unit.
5.3. Issue Electrical FAT / SAT Procedure (ELE-029) and Electrical Test Records / Energization Package (ELE-030) per equipment energization sequence.

#### Step 6 — Logistics and spares
6.1. Issue Logistics / Shipping Plan (PRQ-013) ahead of shipment.
6.2. Issue Spare Parts Interchangeability Record (PRQ-015) ahead of turnover.

#### Step 7 — As-builts
7.1. After installation, reconcile piping and instrument drawings against as-built field marks.
7.2. Issue PIP-028 Piping As-Built Drawings and INS-029 Instrument As-Built Drawings.

#### Step 8 — Regulatory packages
8.1. Compile and submit Pressure Equipment Registration Package (REG-022) to the applicable jurisdiction (`TBD` — see Guidance C-07).
8.2. Compile Fire Code / Building Code Compliance Package (REG-021) (`TBD` code reference — see Guidance C-08).

#### Step 9 — Final consolidated turnover
9.1. Issue Vendor Data Book / Final Supplier Documentation (PRQ-016) and Vendor Data Book / Mechanical Final Documentation (MEC-023) consolidating all final-issue documents.
9.2. Issue the closed-out Vendor Document Index (PRQ-009) with all rows at final status.
9.3. Transmit the consolidated turnover package to the EPC Integrator with a final transmittal cover sheet.

### EPC-Integrator-side steps

#### Step 10 — Receive and log
10.1. Log every transmittal into the EPC document control system on receipt.
10.2. Acknowledge receipt to the vendor within the review turnaround defined in the project document-control matrix (`TBD` — see Guidance C-04).

#### Step 11 — Review
11.1. Route each document to the discipline reviewer.
11.2. Apply review code per DOC-008 (e.g., Code 1 / 2 / 3 — codes `ASSUMPTION` pending DOC-008).
11.3. Return comments to the vendor; vendor revises and re-issues.

#### Step 12 — Interface to acceptance
12.1. As each document reaches its accepted state, mark PRQ-009 accordingly.
12.2. Feed the cumulative reviewed package into `DEL-048-06_epc-vendor-package-review-and-acceptance` as the evidence base. The acceptance decision is recorded there, not here.

## Verification

| Check | Method | Pass criterion |
|---|---|---|
| V-01 — Document-set completeness | Compare closed PRQ-009 rows to the enumeration in `Datasheet.md` (reconciled to heading 3) | One PRQ-009 row per source-required ID; no unexplained additions |
| V-02 — Revision states final | Inspect PRQ-009 status column | All rows at the contractually required final revision per DOC-008 |
| V-03 — Transmittal trail | Inspect EPC document control log | Every PRQ-009 row has at least one transmittal record |
| V-04 — NACE evidence | Inspect QLT-013 entries flagged for sour-service items | Every sour-service item has a cert with explicit NACE compliance statement |
| V-05 — FAT/SAT evidence | Inspect MEC-022, ELE-030 inclusion per unit | Present and accepted for each inlet-duty and sales-duty unit |
| V-06 — As-builts | Inspect PIP-028, INS-029 inclusion | Present and reconciled to IFC |
| V-07 — Regulatory submissions | Inspect REG-021, REG-022 status | Submitted and acknowledged by jurisdiction |
| V-08 — Final data books | Inspect PRQ-016 and MEC-023 | Issued, transmitted, and indexed in PRQ-009 |
| V-09 — Acceptance interface | Inspect handoff to DEL-048-06 | DEL-048-06 review log references this turnover package |
| V-10 — Unit-duty disambiguation | Inspect PRQ-009 unit/duty attribute | Every unit-specific row carries inlet vs sales attribute |

## Records

The following records exit this procedure as the deliverable:
- Closed-out Vendor Document Index (PRQ-009)
- All vendor documents enumerated in `Datasheet.md` at final accepted revision
- Final consolidated Vendor Data Books (PRQ-016, MEC-023, QLT-021)
- Transmittal log and EPC review log entries
- FAT / SAT reports per unit (MEC-022, ELE-030)
- Material certificates (QLT-013), inspection release certificates (QLT-020)
- As-built drawings (PIP-028, INS-029)
- Regulatory submission acknowledgements (REG-021, REG-022)
- Logistics record (PRQ-013), SPIR (PRQ-015)

These records form the evidence base consumed by `DEL-048-06_epc-vendor-package-review-and-acceptance`.
