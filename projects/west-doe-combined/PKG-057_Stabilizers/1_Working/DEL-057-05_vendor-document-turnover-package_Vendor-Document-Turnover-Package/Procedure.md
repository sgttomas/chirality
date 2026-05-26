# Procedure — Vendor Document Turnover Package (DEL-057-05)

> Operational view. Describes the steps to **produce** the Vendor Document Turnover Package for the Stabilizers (`PKG-057`) Inlet Stabilizers supply and to **use** it as the turnover record at EPC Integrator acceptance.

## Purpose

Produce, control, submit, and finally turn over the vendor documentation for the three (3) Inlet Stabilizer Packages (`26020-01-PT-17-005`) to the EPC Integrator, in accordance with the Vendor Engineering Deliverables list in `_Sources/26020-Package_Requirements.docx`.

## Prerequisites

- `_Sources/26020-Package_Requirements.docx` (Inlet Stabilizers section) accessible.
- Project Vendor Document Control Procedure (DOC-008) issued and accessible — **TBD** (referenced by ID only in accessible source slice).
- Project Vendor Document Index template (PRQ-009) issued — **TBD**.
- Vendor purchase order awarded and the three Inlet Stabilizer Package supplier(s) identified.
- Declared upstream dependencies: none declared in `_DEPENDENCIES.md` at this state; treat sibling deliverables DEL-057-02, DEL-057-03, DEL-057-04 as parallel producers whose engineering outputs are tracked by this register.

## Steps

### 1. Stand up the Vendor Document Index (PRQ-009)
1.1 Instantiate the project PRQ-009 template, scoping it to PKG-057 Inlet Stabilizers.
1.2 Populate one row per document required for the package. The starter row set is the union of every document ID listed under `26020-01-PT-17-005 - Inlet Stabilizers > Vendor Engineering Deliverables` (reproduced in `Datasheet.md` § Construction).
1.3 For each row, capture: document ID, title, owning discipline, planned submittal lifecycle codes and dates, current revision, current status, EPC Integrator reviewer, due-back date.
1.4 Issue PRQ-009 rev A to EPC Integrator for alignment.

### 2. Adopt the Vendor Document Control Procedure (DOC-008)
2.1 Read DOC-008 in full; capture any project-specific transmittal numbering, revision conventions, file naming, native-format requirements, and lifecycle codes.
2.2 If DOC-008 is unavailable, raise a clarification before issuing any IFR/IFA submittal (record as Conflict C-01 in `Guidance.md`).

### 3. Per-category submittal execution
For each section banner in the Inlet Stabilizers Vendor Engineering Deliverables table (Core vendor documents; Core package engineering; Static pressure equipment; Relief/Flare/Vent; Process piping; Utility piping; Drainage; Electrical/Lighting/EHT/Grounding; I&C; Fire & Gas; Structural), execute:

3.1 Schedule the submittal milestone in PRQ-009.
3.2 Produce / receive the document instance per its native owner discipline (engineering content is owned by DEL-057-02 / DEL-057-04; this procedure does not author engineering content).
3.3 Issue a transmittal to EPC Integrator per DOC-008.
3.4 Track EPC Integrator review status in PRQ-009; incorporate comments; reissue at the next lifecycle revision until status reaches the accepted code (code TBD — see C-01).

### 4. Assemble the quality record set
4.1 Maintain QLT-003 (ITP) execution evidence: signed-off inspection points, NDE reports, witness/hold-point sign-offs.
4.2 Collect QLT-013 (Material Test Reports / Certificates) from sub-suppliers and bind them to the Manufacturing Record Book (QLT-021) per heat/serial.
4.3 Issue QLT-020 (Inspection Release Certificate) prior to shipment.
4.4 Compile QLT-021 (Manufacturing Record Book) per package serial number.

### 5. Pre-shipment package
5.1 Deliver PRQ-013 (Logistics / Shipping Plan).
5.2 Deliver PRQ-015 (SPIR).
5.3 Deliver MEC-024 (Mechanical Spares / Special Tools Requirements).
5.4 Confirm REG-022 (Pressure Equipment Registration Package) is registered with the applicable jurisdictional authority (jurisdiction TBD — Conflict C-03).

### 6. Final turnover compilation
6.1 Assemble PRQ-016 (Vendor Data Book / Final Supplier Documentation) and MEC-023 (Vendor Data Book / Mechanical Final Documentation) using the table-of-contents pattern proposed in `Guidance.md` § Examples.
6.2 Include the final, accepted-status revision of every PRQ-009 row.
6.3 Include FAT/performance evidence (MEC-022) and IOM manuals (MEC-025).
6.4 Deliver native files where required (requirement scope TBD — Conflict-adjacent; resolve under DOC-008).

### 7. Handoff to DEL-057-06
7.1 Transmit the complete Vendor Document Turnover Package to EPC Integrator with a turnover transmittal referencing PRQ-009 (final revision) as its manifest.
7.2 Acceptance of the package is recorded under DEL-057-06 (EPC Vendor Package Review and Acceptance), not under this deliverable.

## Verification

| Check | Method |
|---|---|
| PRQ-009 row coverage | Every document ID in `Datasheet.md` § Construction is present as a row in the final PRQ-009 instance. |
| Lifecycle completeness | Every PRQ-009 row reaches the project's accepted status code (status code list TBD). |
| Quality records bound | Every package serial number has a corresponding QLT-021 with QLT-013 traceable to heats/serials and a QLT-020 IRC. |
| Data Books assembled | PRQ-016 and MEC-023 exist, contain the final-revision artifacts, and pass an EPC Integrator completeness review. |
| Source fidelity | Every category banner from the Inlet Stabilizers Vendor Engineering Deliverables source table is represented in the submittal schedule. |

## Records

- Final PRQ-009 (Vendor Document Index) revision.
- Per-category transmittals and review logs.
- QLT-003 (executed ITP) + QLT-013 + QLT-020 + QLT-021 (per package serial).
- PRQ-013, PRQ-015, MEC-024.
- PRQ-016 and MEC-023 final Vendor Data Books.
- REG-022 (Pressure Equipment Registration Package).
- All accepted-status engineering submittals listed in `Datasheet.md` § Construction.
