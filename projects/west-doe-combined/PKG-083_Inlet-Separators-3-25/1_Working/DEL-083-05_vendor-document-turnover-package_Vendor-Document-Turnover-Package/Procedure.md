# Procedure — DEL-083-05 Vendor Document Turnover Package

## Purpose

Operational steps to **assemble, control, accept, and turn over** the Vendor Document Turnover Package for `PKG-083 Inlet Separators 3-25`. This procedure covers both:

- producing the turnover package (Package Vendor authoring + EPC Integrator review); and
- using it at turnover (acceptance, handover to operations).

## Prerequisites

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` for this deliverable have been read.
- `26020-Package_Requirements.docx` heading 36 is available (it is, locally) — the vendor engineering deliverables table is the composition basis.
- A Package Vendor is under contract for PKG-083 with the 26020 package requirements flowed into the PO.
- `DOC-008 Vendor Document Control Procedure` has been issued by the vendor and accepted by the EPC Integrator (this is itself a row in the register).
- `PRQ-009 Vendor Document Index` has been initialized by the vendor at PO award (this is itself a row in the register).

Declared upstream dependencies in `_DEPENDENCIES.md`: none. No upstream blocker is recorded; integration timing constraints are governed by execution scheduling rather than declared edges.

## Steps

### Step 1 — Initialize the register (PRQ-009)

1. Vendor instantiates PRQ-009 using the full row set in REQ-VDT-01 of `Specification.md` (which mirrors the 26020 vendor engineering deliverables table for PKG-083).
2. Each row records: source deliverable ID, document title, current revision, status (IFR/IFA/IFC/Final), transmittal reference, acceptance reference, applicable units (e.g., "both separators" or specific serial number).
3. EPC Integrator confirms row-for-row coverage against the 26020 source before any submittals are accepted.

`TBD`: whether PRQ-009 is maintained in vendor-native format (Excel) or an EPC document control system. Defer to DOC-008.

### Step 2 — Vendor submittals

1. For each register row, vendor issues a submittal per DOC-008 (with rev code, transmittal number).
2. Submittal filename or transmittal metadata SHALL carry the source deliverable ID (REQ-VDT-04).
3. Vendor updates PRQ-009 to reflect the submittal.
4. Critical-path early submittals (for downstream integration): `MEC-016` GA, `MEC-017` Installation/Setting, `PRO-008` P&IDs, `INS-002` Instrument Index, `STR-005/006` Foundation Design/Drawings, `CTL-003` Control Narrative, `CTL-005` Cause & Effect, `CTL-026` Vendor Interface Spec. These unblock EPC Integrator deliverables and SHOULD be transmitted early in execution.

### Step 3 — EPC Integrator review

1. Reviewer organizes the review by interface family (Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports — source: `PACKAGE_REGISTER.csv` row PKG-083 / 26020 source physical interface table).
2. Reviewer issues comments per DOC-008. Vendor revises and re-submits.
3. Acceptance is recorded against the register row (PRQ-009) by a human reviewer with authority (K-AUTH-1).

### Step 4 — Manufacturing, FAT, and inspection records

1. As manufacturing progresses, `QLT-013` Material Test Reports / Certificates accumulate; vendor attaches to PRQ-009 row and to the manufacturing record book (`QLT-021`).
2. `MEC-021` FAT/Performance Test Procedure SHALL be accepted by the EPC Integrator before FAT.
3. FAT witnessed; `MEC-022` FAT Report issued and accepted.
4. `QLT-020` Inspection Release Certificate issued at completion of inspection.
5. `REG-022` Pressure Equipment Registration Package compiled and submitted to the jurisdictional regulator (ASSUMPTION: ABSA in Alberta).

### Step 5 — Logistics and field-arrival documents

1. `PRQ-013` Logistics / Shipping Plan, `MEC-018` Lifting / Handling Study, and `MEC-024` Spares / Special Tools Requirements transmitted before shipment.
2. `PRQ-015` SPIR updated to reflect final spares package.

### Step 6 — Final Vendor Data Book and turnover acceptance

1. Vendor compiles the final Vendor Data Book covering at minimum: `PRQ-016`, `QLT-021`, `MEC-023`, plus all As-Built revisions of the design and engineering rows.
2. Vendor reconciles PRQ-009 to ensure every register row is at an accepted final revision (or carries a documented and ruled exception).
3. EPC Integrator performs the acceptance review against REQ-VDT-05 (Specification):
   - (a) every required row has an accepted submittal in PRQ-009;
   - (b) `QLT-021` and `PRQ-016` are at IFC/Final;
   - (c) `MEC-022`, `QLT-020`, `MEC-023` are transmitted and accepted;
   - (d) interface/integration review is recorded for the integration-relevant rows.
4. The Turnover Acceptance Record is produced and signed by the human authorities on both sides (K-AUTH-1).
5. The accepted Vendor Data Book + PRQ-009 + Turnover Acceptance Record become the turnover output handed to operations/maintenance.

### Step 7 — Handover to operations

1. The accepted Vendor Data Book (with `MEC-025 Mechanical Equipment IOM Manual` as the operating spine) is transferred to the operating-asset document library.
2. PRQ-009 is preserved as the audit trail of what was turned over.

## Verification

- Audit PRQ-009 row-by-row against the 26020 vendor engineering deliverables table — zero unmatched rows (REQ-VDT-01).
- Confirm every submittal in the deliverable folder appears in PRQ-009 and carries its source deliverable ID (REQ-VDT-02, REQ-VDT-04).
- Confirm DOC-008 is at Final and that all submittals follow its rev coding (REQ-VDT-03).
- Verify the four sub-conditions of REQ-VDT-05 before signing the Turnover Acceptance Record.
- Confirm raw source artifacts (where supplied per `_CONTEXT.md` anticipated artifacts) are attached to the correct PRQ-009 register row rather than registered as separate deliverables (REQ-VDT-07; Gate 5 ruling).

## Records

- `PRQ-009 Vendor Document Index` — final accepted revision (the register).
- The set of all accepted vendor submittals named per DOC-008 with source-ID preservation.
- Transmittal log per DOC-008.
- Final Vendor Data Book(s): `PRQ-016`, `QLT-021`, `MEC-023`.
- `QLT-020` Inspection Release Certificate; `MEC-022` FAT Report; `REG-022` Pressure Equipment Registration Package.
- Turnover Acceptance Record (signed; human-authored per K-AUTH-1).

Storage location of the records inside this deliverable folder at the executing-project stage: `TBD` (set by the executing project, not by this procedure).
