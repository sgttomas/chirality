# Procedure: DEL-089-03 — Construction Work Package

> **Document role:** Operational — defines the operational sequence by which the EPC Integrator produces the Construction Work Package artifact set for PKG-089 and (through it) governs the field execution of construction, inspection, turnover, and tie-in. Two procedure tracks are defined: (A) Produce the CWP artifact, and (B) Execute construction governed by the CWP.

## Purpose

To define the procedure by which the Construction Work Package for PKG-089 *Pig Receivers (Inlet) 3-25* is produced, verified, and used to govern field construction and turnover. [Source: DELIVERABLE_REGISTER.csv row DEL-089-03]

## Prerequisites

- Accepted upstream decomposition: GATE-07_Final_Published_2026-05-24 PROJECT_DECOMP snapshot.
- Local read access to the following references (per `_REFERENCES.md`):
  - `_Decomposition/.../DELIVERABLE_REGISTER.csv` — row DEL-089-03.
  - `_Decomposition/.../PACKAGE_REGISTER.csv` — row PKG-089.
  - `_Decomposition/.../INTERFACE_REGISTER.csv` — interface entries for PKG-089.
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
  - `_Sources/26020-Package_Requirements.docx` — package heading 42 (binary; **location TBD** for direct read).
  - `_Sources/Bid Docs/26020-02-PT-RFQ-35-001-Pig_Recv_1.docx` — pig receiver RFQ (binary; **location TBD** for direct read).
- Upstream deliverables consumed at IFC:
  - `DEL-089-01_scope-of-work` — package SOW.
  - `DEL-089-02_package-datasheet` — package datasheet.
  - `DEL-089-04_vendor-engineered-equipment-package` — vendor engineered equipment package basis (the receiving artifact of installation).
- Declared upstream dependencies per `_DEPENDENCIES.md`: none declared during PREPARATION (ASSUMPTION: detail-design issuance of DEL-089-01, DEL-089-02, and DEL-089-04 are de-facto prerequisites — confirm via dependency-extract).
- Conflict Table entries (Guidance §Conflict Table) ruled before IFC issuance.

## Steps

### Track A — Produce the CWP artifact

1. **Establish basis.** Read DELIVERABLE_REGISTER.csv row DEL-089-03, PACKAGE_REGISTER.csv row PKG-089, INTERFACE_REGISTER.csv entries for PKG-089, the DBM source slice §SEC-04, and the binary sources for heading 42 and the RFQ. Record any inaccessible source as TBD.
2. **Resolve receiver count/size.** Obtain human ruling on Conflict Table item CFT-089-03-01 and update Datasheet/Specification consistently before drafting the workface plan.
3. **Define construction means and methods.** Document foundation installation, skid set, structural anchoring, alignment, and material/weld/NDE methods consistent with sour service.
4. **Develop the installation and tie-in workface plan.** Sequence skid setting, pipeline tie-in at the lease-boundary first-aboveground flange, tie-ins to V-1600-2 and V-1700-2, relief/flare/vent and drain tie-ins, and electrical/EHT/I&C tie-ins. Include resource loading and schedule windows.
5. **Develop the interface and turnover checklist.** Create one row per interface type from PACKAGE_REGISTER.csv (Process Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; I&C/Control Cabling; Maintenance Access; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports; Pipeline/Pigging), with completion criteria, witness/hold points, and turnover acceptors.
6. **Define inspection and test plan.** Identify pressure test packages, weld inspection (PQR/WPS/NDE), ESDV functional test (full-port, piggable, position transmitter calibration), purge/inert plan, and sour-service material verification. Cite source clauses where accessible; mark **location TBD** otherwise.
7. **Define mechanical completion and turnover.** Define MC walkdowns, punchlist registration and closeout, and operations turnover certificate.
8. **Cross-document consistency.** Verify Datasheet, Specification, Guidance, and Procedure use consistent terminology and values (receiver count/size, ESDV pressures, interface list).
9. **Issue for review (IFR), then for construction (IFC).** Resolve review comments and human rulings on the Conflict Table; reissue at IFC.

### Track B — Execute construction governed by the CWP

10. **Mobilize and pre-construction verification.** Confirm vendor package receipt against DEL-089-02/DEL-089-04 and IFC drawings; verify materials are sour-service compliant.
11. **Foundations and skid set.** Install foundations; set the structural-steel non-enclosed skid(s) per Specification R-089-03-01. [Source: DBM line 237]
12. **Process piping tie-ins.** Tie in to the inlet pipeline at the lease-boundary first-aboveground flange and to the two inlet separators V-1600-2 / V-1700-2 per workface plan. [Sources: DBM lines 228, 244]
13. **Purge/vent/relief tie-ins.** Tie in sweet-gas purge and HP flare vent lines per the relief/flare/vent interface; coordinate with flare system commissioning. [Source: DBM line 238]
14. **Drain/containment, grading, structural, and maintenance access tie-ins.** Execute remaining interface tie-ins per the workface plan and interface checklist.
15. **Electrical, EHT, and I&C tie-ins.** Energize, calibrate, and loop-check, including ESDV position transmitters.
16. **Inspection and testing.** Execute the inspection/test plan (pressure tests, NDE, ESDV functional/stroke tests, purge/inert).
17. **Mechanical completion and punchlist.** Walk down the package against the interface and turnover checklist; register and close punchlist items.
18. **Operations turnover.** Issue the turnover certificate, transfer custody and control to Operations.

## Verification

| Step | Verification |
|---|---|
| A.1 | Reference read log; all listed sources opened or marked TBD with reason. |
| A.2 | Documented human ruling on CFT-089-03-01; receiver count/size consistent across Datasheet, Specification, Procedure. |
| A.3–A.5 | Document review against Specification R-089-03-01..R-089-03-04 and the interface-type list. |
| A.6 | Inspection and test plan covers each requirement that depends on an inspection or test; sour-service compliance is addressed. |
| A.7 | MC and turnover sections present; punchlist register form attached. |
| A.8 | Cross-document consistency check (Spec §5.x review); no terminology or value drift. |
| A.9 | IFR and IFC issue records signed off. |
| B.10–B.18 | Construction QC records, test certificates, calibration records, MC certificate, punchlist closeout, and turnover certificate. |

## Records

- CWP document set (CWP, workface plan, interface/turnover checklist) at IFC, signed.
- Source read log and rulings on Conflict Table items.
- Inspection and test records (pressure-test packages, NDE reports, weld procedure qualifications, ESDV functional/stroke records, purge/inert records).
- Material certifications (sour-service compliance).
- Mechanical completion certificate and punchlist register/closeout.
- Operations turnover certificate.
- Construction interface and turnover checklist (completed, signed).
