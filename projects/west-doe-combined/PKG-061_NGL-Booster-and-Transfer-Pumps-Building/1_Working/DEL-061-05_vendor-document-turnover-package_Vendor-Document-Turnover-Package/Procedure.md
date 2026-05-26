# Procedure — DEL-061-05 Vendor Document Turnover Package

## Purpose

To produce, control, and turn over the vendor document set for PKG-061 from kickoff through handover acceptance by the EPC Integrator.

## Prerequisites

- Upstream package basis: EPC Scope of Work (`DEL-061-01`) and Package Datasheet (`DEL-061-02`) accepted by the EPC Integrator (declared upstream dependencies in PREPARATION were `none`; ASSUMPTION based on PKG-061 deliverable order).
- Vendor contract awarded with PKG-061 scope.
- Project document control procedure (DOC-008 basis) in place.
- Access to:
  - `_Sources/26020-Package_Requirements.docx` (vendor deliverables list, Tank Pumps section as nearest comparator; building wrapper location TBD).
  - `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 75 (interface applicability for PKG-061).
  - Decomposition snapshot `GATE-07_Final_Published_2026-05-24`.

## Steps

### Step 1 — Establish Vendor Document Index (PRQ-009)
1. Draft PRQ-009 using the Datasheet "Construction" table as the baseline document list.
2. Filter using Workbook row 75 interface applicability — mark interface-specific documents N/A where the interface is not flagged.
3. Add vendor-native numbering aligned to project numbering per DOC-008.
4. Issue PRQ-009 IFR for EPC Integrator review.

**Verification:** PRQ-009 reviewed by EPC; baseline locked.

### Step 2 — Establish Vendor Document Control Procedure (DOC-008)
1. Confirm vendor's document numbering, revision, status, and transmittal mechanics conform to project DOC-008 basis.
2. Issue DOC-008 instance for PKG-061.

**Verification:** EPC document control accepts DOC-008.

### Step 3 — Produce and submit engineering documents
1. Produce documents per the Datasheet "Construction" table by group (core vendor, core package engineering, rotating equipment, relief/flare/vent, piping interfaces, utility, drainage, electrical, I&C, building/HVAC, fire & gas, structural).
2. Submit through project document control workflow at successive revisions (IFR / IFA / IFC, then AB as applicable — workflow detail `location TBD`).
3. Update PRQ-009 status on every transmittal.

**Verification:** Submittal log reconciles against PRQ-009; EPC review comments tracked to closure.

### Step 4 — Produce quality and inspection records
1. Issue QLT-006 (Supplier Quality Plan), QLT-003 (ITP) early.
2. During fabrication: collect QLT-013 (MTR/Certificates).
3. Before shipment: issue QLT-020 (Inspection Release Certificate), MEC-021/022 (FAT procedure/report).

**Verification:** Quality records complete per ITP hold/witness points.

### Step 5 — Produce logistics and spares documents
1. Issue PRQ-013 (Logistics/Shipping Plan) ahead of shipment window.
2. Issue PRQ-015 (SPIR) ahead of EPC spare-parts procurement window.

**Verification:** EPC confirms timing supports procurement and site logistics.

### Step 6 — EPC Integrator interface reviews
1. EPC reviews documents at each flagged interface from Workbook row 75 (13 interfaces).
2. Disposition comments per EPC review log; vendor responds and re-issues.

**Verification:** EPC review log shows each interface reviewed and dispositioned.

### Step 7 — Assemble Vendor Data Book and turnover records
1. Compile final-issue documents into Vendor Data Book (PRQ-016 / MEC-023 / QLT-021 — Manufacturing Record Book / Vendor Data Book).
2. Produce turnover records:
   - Transmittal log (full history).
   - Final document status report (every PRQ-009 line at final accepted revision or formally waived).
   - EPC acceptance sign-off.
3. Transmit Vendor Data Book + turnover records to EPC.

**Verification:** EPC accepts turnover; sign-off recorded.

### Step 8 — As-built closeout
1. After construction/commissioning, issue as-built revisions (e.g., PIP-028, INS-029) as applicable.
2. Update PRQ-009 to as-built revisions.
3. Re-issue Vendor Data Book if material as-built changes occurred (PROPOSAL — confirm with EPC).

**Verification:** PRQ-009 closed; as-built Data Book accepted.

## Verification

| Step | Verification artifact |
|---|---|
| 1-2 | PRQ-009 IFR + DOC-008 with EPC acceptance markup |
| 3 | Submittal log, EPC review log |
| 4 | ITP records, MTRs, IRC, FAT report |
| 5 | PRQ-013, PRQ-015 issued; EPC schedule confirmation |
| 6 | EPC interface review log |
| 7 | Vendor Data Book + EPC turnover sign-off |
| 8 | As-built PRQ-009; updated/accepted Data Book |

## Records

- PRQ-009 Vendor Document Index (live and final-issue revisions).
- DOC-008 Vendor Document Control Procedure.
- Transmittal log (cumulative).
- Final document status report at turnover.
- Vendor Data Book / Manufacturing Record Book (PRQ-016 / QLT-021 / MEC-023 consolidated).
- EPC review log and disposition records.
- EPC turnover acceptance sign-off.
- As-built document set (post-construction).
