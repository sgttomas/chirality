# Procedure — DEL-062-05 Vendor Document Turnover Package

This procedure describes how the Package Vendor produces and submits the Vendor Document Turnover Package and how the EPC Integrator receives and reviews it. The acceptance decision itself is recorded under `DEL-062-06`.

## Prerequisites

1. **Upstream inputs in place** (per `_DEPENDENCIES.md`, no upstream edges currently declared at this deliverable; the following are operational prerequisites derived from the EPC anchor deliverables in PKG-062):
   - EPC Scope of Work (`DEL-062-01`) issued.
   - EPC Package Datasheet (`DEL-062-02`) issued.
   - Construction Work Package (`DEL-062-03`) sufficiently mature to anchor turnover content for installation/commissioning interface.
   - Vendor Engineered Equipment Package (`DEL-062-04`) producing the engineering content this turnover compiles.
2. **Vendor Document Control Procedure (DOC-008)** issued and accepted. (`TBD` until issued — see Guidance Conflict Table C-02, C-03.)
3. **Vendor Document Index (PRQ-009)** initialized with rows for every source-required deliverable enumerated in `Datasheet.md`.
4. **Source slice** `26020-Package_Requirements.docx` heading 16 available as the authoritative document-scope reference.
5. **Interface workbook** (locally: `_Sources/26020-Packages_Interfaces_4_export.xlsx`) available for cross-checks. See Guidance C-04.
6. EPC Integrator review path and reviewer assignments confirmed (interface to `DEL-062-06`).
7. Package fluid-service naming reconciled (NGL vs LPG — Guidance C-01) before final issue.

## Steps

### Vendor-side steps

#### Step 1 — Initialize the Vendor Document Index (PRQ-009)
1.1. For each source-required ID enumerated in `Datasheet.md` (heading 16 vendor deliverables table), create one row in PRQ-009 with: Source ID, Source Name, Vendor Doc Number (TBD until vendor numbering issued), Title, Discipline group, Per-tag applicability (where relevant for the four pump tags P9510/20/30/40-1), Planned issue stage(s), Planned issue date(s).
1.2. Reconcile to the source table — no rows missing, no extra rows without a scope-change record.

#### Step 2 — Issue the Vendor Document Control Procedure (DOC-008)
2.1. Define numbering scheme, revision states, transmittal mechanics, hold/review codes, and acceptance flow.
2.2. Submit to EPC Integrator for review; reissue at IFC.

#### Step 3 — Stage-by-stage submittal
3.1. For each document in PRQ-009, issue at each stage required by DOC-008 (e.g., Bid → IFR → IFA → IFC → As-Built — stage labels `ASSUMPTION` pending DOC-008).
3.2. Each submittal carries a transmittal cover sheet citing the documents enclosed, their revision, and the transmittal date.
3.3. Update PRQ-009 with every transmittal event.

#### Step 4 — Pump hydraulics, motor sizing, and TDH confirmation
4.1. Issue `MEC-007 Pump Data Sheets` per pump tag (P9510-1, P9520-1, P9530-1, P9540-1).
4.2. Issue `PRO-013 Pump Hydraulic / NPSH Calculations` covering the four-pump parallel configuration at design capacity (68 m³/hr per unit @ 345 kPad / 300 USGPM @ 50 psid) and confirming the finalized TDH (resolving the source TBC — see Guidance C-05).
4.3. Issue `ELE-011 Motor Starting Study` covering the cited cold-start case (inlet stabilizer composition density at -40 °C).
4.4. Issue `MEC-019 Mechanical Seal / Lube Oil Specification` for the Blackmer LGL4B rotary vane configuration.
4.5. Issue `MEC-004 Rotating Equipment Specifications` consolidating the rotating-equipment specification basis.

#### Step 5 — Loading / metering package documentation
5.1. Issue `INS-015 Metering Package Specification` for the truck-loading metering interface.
5.2. Issue `PRO-025 Operating Guidelines / Startup-Shutdown Narrative` covering normal LPG truck-loading service and cold-start.
5.3. Issue `PIP-004 Tie-In List / Tie-In Scope Sheets` and `PIP-018 Valve Data Sheets` for the loading interface.

#### Step 6 — Quality and inspection evidence
6.1. Maintain `QLT-006 Supplier Quality Plan` and `QLT-003 ITP` as the working quality basis.
6.2. As materials are received, file `QLT-013 Material Test Reports / Certificates` per pump tag.
6.3. At hold points, issue `QLT-020 Inspection Release Certificates`.
6.4. Build `QLT-021 Manufacturing Record Book / Vendor Data Book` progressively per pump tag.

#### Step 7 — FAT and energization evidence
7.1. Issue `MEC-021 Equipment FAT / Performance Test Procedure`. Procedure SHALL include a per-pump capacity / TDH point that reconciles MEC-007.
7.2. Execute FAT for each pump tag; issue `MEC-022 Equipment FAT / Performance Test Report` (per tag or consolidated by tag, per DOC-008).
7.3. Issue `ELE-029 Electrical FAT / SAT Procedure` and `ELE-030 Electrical Test Records / Energization Package`, including motor starting evidence consistent with ELE-011.

#### Step 8 — Logistics and spares
8.1. Issue `PRQ-013 Logistics / Shipping Plan` ahead of shipment.
8.2. Issue `PRQ-015 Spare Parts Interchangeability Record (SPIR)` ahead of turnover.

#### Step 9 — As-builts
9.1. After installation, reconcile piping and instrument drawings against as-built field marks.
9.2. Issue `PIP-028 Piping As-Built Drawings` and `INS-029 Instrument As-Built Drawings`.

#### Step 10 — Regulatory / code package
10.1. Compile `REG-021 Fire Code / Building Code Compliance Package` for the self-framing building per the applicable jurisdiction (`TBD` code reference — see Guidance C-07).
10.2. Do NOT add `REG-022 Pressure Equipment Registration Package` unless a confirmed scope change adds it (see Guidance C-06).

#### Step 11 — Final consolidated turnover
11.1. Issue `PRQ-016 Vendor Data Book / Final Supplier Documentation` and `MEC-023 Vendor Data Book / Mechanical Final Documentation` consolidating all final-issue documents.
11.2. Issue the closed-out `PRQ-009 Vendor Document Index` with all rows at final status.
11.3. Transmit the consolidated turnover package to the EPC Integrator with a final transmittal cover sheet.

### EPC-Integrator-side steps

#### Step 12 — Receive and log
12.1. Log every transmittal into the EPC document control system on receipt.
12.2. Acknowledge receipt to the vendor within the review turnaround defined in the project document-control matrix (`TBD` — see Guidance C-03).

#### Step 13 — Review
13.1. Route each document to the discipline reviewer.
13.2. Apply review code per DOC-008 (e.g., Code 1 / 2 / 3 — codes `ASSUMPTION` pending DOC-008).
13.3. Return comments to the vendor; vendor revises and re-issues.

#### Step 14 — Interface to acceptance
14.1. As each document reaches its accepted state, mark PRQ-009 accordingly.
14.2. Feed the cumulative reviewed package into `DEL-062-06_epc-vendor-package-review-and-acceptance` as the evidence base. The acceptance decision is recorded there, not here.

## Verification

| Check | Method | Pass criterion |
|---|---|---|
| V-01 — Document-set completeness | Compare closed PRQ-009 rows to the enumeration in `Datasheet.md` | One PRQ-009 row per source-required ID; no unexplained additions |
| V-02 — Revision states final | Inspect PRQ-009 status column | All rows at the contractually required final revision per DOC-008 |
| V-03 — Transmittal trail | Inspect EPC document control log | Every PRQ-009 row has at least one transmittal record |
| V-04 — Per-tag pump records | Inspect MEC-007, QLT-013, MEC-022 | Records present per pump tag (P9510-1, P9520-1, P9530-1, P9540-1) |
| V-05 — TDH confirmation | Inspect MEC-007 vs MEC-022 | Finalized TDH consistent across both; reconciles source TBC |
| V-06 — Cold-start motor sizing | Inspect ELE-011 and PRO-013 | Cold-start case (-40 °C stabilizer-density basis) evidenced |
| V-07 — Loading-service evidence | Inspect INS-015, PRO-025 | Truck-loading service narrative and metering spec issued and accepted |
| V-08 — FAT/SAT evidence | Inspect MEC-022, ELE-030 inclusion | Present and accepted |
| V-09 — As-builts | Inspect PIP-028, INS-029 inclusion | Present and reconciled to IFC |
| V-10 — Regulatory submissions | Inspect REG-021 status | Submitted and acknowledged by jurisdiction |
| V-11 — Final data books | Inspect PRQ-016 and MEC-023 | Issued, transmitted, and indexed in PRQ-009 |
| V-12 — Acceptance interface | Inspect handoff to DEL-062-06 | DEL-062-06 review log references this turnover package |
| V-13 — Package naming reconciled | Inspect package datasheet and turnover cover sheet | NGL/LPG service-fluid naming consistent and ruled-on (Guidance C-01) |

## Records

The following records exit this procedure as the deliverable:
- Closed-out Vendor Document Index (PRQ-009)
- All vendor documents enumerated in `Datasheet.md` at final accepted revision
- Final consolidated Vendor Data Books (PRQ-016, MEC-023, QLT-021)
- Transmittal log and EPC review log entries
- Per-tag FAT / SAT reports (MEC-022, ELE-030) for P9510/20/30/40-1
- Material certificates (QLT-013), inspection release certificates (QLT-020)
- As-built drawings (PIP-028, INS-029)
- Fire / building code submission acknowledgement (REG-021)
- Logistics record (PRQ-013), SPIR (PRQ-015)
- Operating Guidelines / Startup-Shutdown Narrative (PRO-025) and Metering Package Specification (INS-015)

These records form the evidence base consumed by `DEL-062-06_epc-vendor-package-review-and-acceptance`.
