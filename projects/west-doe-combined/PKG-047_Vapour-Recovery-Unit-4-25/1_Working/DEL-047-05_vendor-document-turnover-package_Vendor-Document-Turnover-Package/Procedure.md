# Procedure: Vendor Document Turnover Package (DEL-047-05)

This procedure describes how to **assemble, control, review, and turn over** the vendor document package for `PKG-047 — Vapour Recovery Unit 4-25` (equipment tag `26020-01-PT-12-002`). It is operational guidance for the Package Vendor (document controller) and the EPC Integrator (review and acceptance interface). Production of the vendor engineering content itself (data sheets, drawings, calculations, etc.) is governed by the engineering disciplines, not this procedure.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`.
- Available source: `_Sources/26020-Package_Requirements.docx`, section "26020-01-PT-12-002 - Vapour Recovery Unit".
- Available source: `_Sources/26020-Packages_Interfaces_4_export.xlsx` (note revision drift; see Guidance CONFLICT-1).
- Vendor Document Control Procedure (DOC-008) issued by the Package Vendor and acknowledged by EPC Integrator.
- Declared upstream dependencies per `_DEPENDENCIES.md` (none declared during PREPARATION; advisory only).
- EPC Integrator review-status code set agreed in writing. **TBD**.
- Jurisdiction for REG-022 confirmed. **TBD** (see Guidance CONFLICT-3).

## Steps

### Step 1 — Initialize the Vendor Document Index (PRQ-009)

1. Open the source's "Vendor Engineering Deliverables" table for `26020-01-PT-12-002` (Source: `26020-Package_Requirements.docx`).
2. Create one register row per source row, copying group, Doc ID, and Name. (See `Datasheet.md` Construction for the full enumerated set.)
3. Add control columns: vendor document number, current revision, status (Planned / In Progress / Submitted / Under Review / Returned / Accepted / Superseded), last transmittal number, last transmittal date, EPC reviewer, last EPC review-status code, due date, closeout date.
4. Add coverage columns: source row reference, SOW reference (`SOW-0253..0256`), Train 1 / Train 2 / Common indicator where applicable.
5. Issue PRQ-009 Rev A under DOC-008 governance.

### Step 2 — Author and submit individual vendor documents

For each register row:

1. Vendor authors the document under its discipline procedure (not part of this turnover deliverable's scope).
2. Vendor assigns the document number per DOC-008 and updates PRQ-009.
3. Vendor issues a transmittal that lists every document on the transmittal, with current revision and submittal purpose (Information / Review / Approval / As-Built).
4. EPC Integrator logs the transmittal, performs interface/integration review, and returns review-status code per the agreed code set (**TBD**).
5. Vendor revises and resubmits as required. Each revision is a new register entry-state event; superseded revisions are marked Superseded (not deleted).

### Step 3 — Quality records collection (QLT family)

1. Maintain QLT-006 Supplier Quality Plan and QLT-003 ITP as living controlled documents through fabrication.
2. As each hold-point clears, collect QLT-013 Material Test Reports / Certificates and file them under the equipment serial number (Train 1 / Train 2 / Common).
3. Issue QLT-020 Inspection Release Certificates as each major assembly is released.
4. Update PRQ-009 status against each QLT row at each transmittal.

### Step 4 — FAT and release-to-ship

1. Transmit MEC-021 Equipment FAT / Performance Test Procedure for EPC review and acceptance before FAT execution.
2. Witness and execute FAT; produce MEC-022 Equipment FAT / Performance Test Report.
3. Confirm acceptance of MEC-022 before authorizing PRQ-013 Logistics / Shipping Plan execution.
4. Update PRQ-009 with all of MEC-021, MEC-022, PRQ-013, QLT-020 final status.

### Step 5 — Discipline document closeout

For each discipline group enumerated in the source's Vendor Engineering Deliverables table (Core package engineering; Rotating equipment / compressors; Relief / flare / vent; Process piping; Utility piping; Drainage / containment; Electrical / lighting / EHT / grounding; Instrumentation and controls; Fire and gas / technical safety; Structural / foundations / supports / access):

1. Confirm every register row in the group is at Accepted (or explicitly Closed Not Required with EPC Integrator concurrence).
2. Resolve any rows in Returned status with vendor revision and resubmittal.
3. Record any discipline-level open items in the turnover open-items list.

### Step 6 — Spares and operations handover

1. Issue PRQ-015 Spare Parts Interchangeability Record (SPIR).
2. Issue MEC-024 Mechanical Spares / Special Tools Requirements.
3. Issue MEC-025 Mechanical Equipment IOM Manual.
4. Confirm Owner / EPC Integrator receipt and acknowledgment.

### Step 7 — As-built consolidation

1. Collect PIP-028 Piping As-Built Drawings, INS-029 Instrument As-Built Drawings, and ELE-030 Electrical Test Records / Energization Package.
2. Confirm consistency with the latest design revisions in MEC-016 / MEC-017 / PIP-006 / PIP-007 etc.
3. Mark superseded design revisions accordingly in PRQ-009.

### Step 8 — Pressure equipment registration (REG-022)

1. Assemble REG-022 Pressure Equipment Registration Package for the in-scope pressure boundary equipment.
2. Submit to the applicable jurisdiction (jurisdiction **TBD**; see Guidance CONFLICT-3).
3. Record registration numbers and certificates in PRQ-009 against REG-022 and the affected mechanical data sheets (MEC-003, MEC-009 where applicable).

### Step 9 — Final consolidation and turnover

1. Consolidate the accepted-revision set into MEC-023 Vendor Data Book / Mechanical Final Documentation and QLT-021 Manufacturing Record Book / Vendor Data Book.
2. Issue PRQ-016 Vendor Data Book / Final Supplier Documentation as the master turnover artifact, with PRQ-009 (final revision) as the controlling index and QLT-021 indexed inside.
3. Compile the SOW coverage matrix (SOW-0253..0256 ↔ PRQ-009 rows) and attach to PRQ-016.
4. Attach the EPC Integrator review log summary (acceptance status per row).
5. Submit PRQ-016 to EPC Integrator for final acceptance per the agreed acceptance path (path **TBD**; see Guidance CONFLICT-2).
6. On acceptance: mark all register rows Closed; capture the acceptance evidence in the deliverable record.
7. On non-acceptance: triage returned items, schedule remediation, and re-issue PRQ-016 at next revision.

## Verification

- PRQ-009 final revision contains one row per source-listed Vendor Engineering Deliverable row, each at Accepted or Closed-Not-Required.
- Every transmittal in the EPC Integrator review log has a terminal status (Accepted, Closed-Not-Required, or Superseded).
- Every SOW item (`SOW-0253..0256`) maps to at least one accepted register row in the SOW coverage matrix.
- QLT-021 and MEC-023 are present inside PRQ-016 and reference the same revision of every constituent document as PRQ-009.
- REG-022 submission outcomes (registration numbers / certificates) are recorded in PRQ-009 (jurisdiction confirmed beforehand).
- No open conflicts from `Guidance.md` Conflict Table remain unresolved at PRQ-016 acceptance.

## Records

- PRQ-009 Vendor Document Index — final revision.
- PRQ-016 Vendor Data Book / Final Supplier Documentation — issued and accepted.
- QLT-021 Manufacturing Record Book / Vendor Data Book — issued and indexed inside PRQ-016.
- MEC-023 Vendor Data Book / Mechanical Final Documentation.
- ELE-030 Electrical Test Records / Energization Package.
- PIP-028 Piping As-Built Drawings; INS-029 Instrument As-Built Drawings.
- REG-022 Pressure Equipment Registration Package and jurisdiction registration outcomes.
- EPC Integrator review log (every transmittal terminated).
- SOW coverage matrix (`SOW-0253..0256` ↔ register rows).
- Turnover acceptance evidence (signature path **TBD**).
