# Procedure — Vendor Engineered Equipment Package (DEL-099-04)

> Operational document. Because this deliverable is a vendor *production unit* (design + fabricate + supply + deliver), the procedure below covers the steps to **produce** the deliverable artifact (the engineered equipment package + design basis / datasheet set). Operating procedures for the installed loading stations are out of scope of this vendor production unit and belong with later operations documentation.

## Purpose

Provide a repeatable workflow by which the Package Vendor produces the engineered equipment package for the 03-25 Truck Product Loading Unit, against the EPC Scope of Work (`DEL-099-01`) and EPC Package Datasheet (`DEL-099-02`), with EPC Integrator integration review, satisfying `Specification.md` REQ-VEEP-001 through REQ-VEEP-016.

## Prerequisites

Declared upstream dependencies (`_DEPENDENCIES.md`): **None declared** during PREPARATION. Treat the following as *practical* prerequisites even though not declared as hard upstream edges:

1. EPC Scope of Work `DEL-099-01` issued (currently `OPEN`) — `TBD` blocker; see Guidance CT-01.
2. EPC Package Datasheet `DEL-099-02` issued (currently `OPEN`) — `TBD` blocker; see Guidance CT-01.
3. Access to the cited source materials (`26020-Package_Requirements.docx` heading 51; `Workbook Packages` row 98) in text-extractable form — currently inaccessible; see Guidance CT-02.
4. Access to the 03-25 Compressor Station and Liquids Hub DBM (`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`) — **available** in this run.
5. Confirmed site basis: LSD 03-25-80-15 W6M, elevation 673 m AMSL (DBM SEC-02 line 85).
6. Confirmed product service: stabilized C5+ condensate at hub basis 20,000 bbl/d (DBM SEC-06 line 376).
7. VRU interface envelope (suction pressure, header sizing) coordinated with VRU vendor / EPC.

## Steps

1. **Receive EPC anchors.** Receive `DEL-099-01` Scope of Work and `DEL-099-02` Package Datasheet from the EPC Integrator. Log issued revision. (Blocker today — see Prerequisites #1, #2.)
2. **Establish vendor design basis.** Compile a vendor design basis document combining (a) the EPC Package Datasheet inputs, (b) the source-grounded values from this `Specification.md` (REQ-VEEP-001 through 010), and (c) site/environmental envelope values resolved from the EPC anchors. Resolve every `TBD` against EPC anchors before freezing.
3. **Process design.** Develop loading-station P&IDs, line/equipment lists, and a hydraulic model spanning product-condensate tank → booster pump → loading pump → loading-station hose connection. Reconcile booster duty (165 m³/h at 35 m TDH, DBM SEC-06 line 412) with loading-station duty (103 m³/h at 345 kPad, DBM SEC-06 line 415); see Guidance CT-03.
4. **Mechanical and skid design.** Produce GA drawings, structural skid design, piping isometrics, and material take-offs for three stations and three loading pumps. Confirm modular split sizes against project transport envelope.
5. **Electrical and instrumentation.** Produce single-line diagrams, motor schedules, area-classification drawings, cable schedules, and grounding/bonding scheme per CEC and project electrical specifications (REQ-VEEP-008). Resolve area classification and grounding scheme (REQ-VEEP-013, 014) against EPC ruling.
6. **Controls and safety integration.** Develop package PLC logic, alarm/trip list, and a draft cause-and-effect matrix for integration with BPCS / ESD (REQ-VEEP-007; DBM SEC-12 line 862). Coordinate F&G detector placement for the loading apron with the EPC Integrator (REQ-VEEP-006; DBM SEC-12 line 838).
7. **Hazard and integration reviews.** Participate in HAZOP / LOPA / area-classification reviews as called by the EPC Integrator. Update vendor design basis with accepted actions.
8. **Vendor datasheet set.** Produce the vendor datasheet set (loading station, loading pump, motor, instruments, valves) cross-referenced to REQ-VEEP-* IDs (REQ-VEEP-015).
9. **EPC integration review.** Submit the design package to the EPC Integrator for integration review (vendor → EPC). Resolve comments. Issue revision.
10. **Procurement and fabrication.** Procure long-lead items, fabricate skid(s), and assemble.
11. **Factory acceptance test (FAT).** Perform FAT covering pump performance at duty point (REQ-VEEP-002), instrument loop checks, PLC logic, and ESD interfaces.
12. **Ship and turn over to construction.** Ship the package to site and turn over to `DEL-099-03` (Construction Work Package) execution.
13. **Support construction and SAT.** Provide vendor support during installation, commissioning, and site acceptance test (SAT). Resolve any deviations as field engineering changes traceable back to the vendor design basis.
14. **Hand off to vendor document turnover.** Compile vendor documentation per `DEL-099-05` (Vendor Document Turnover Package).
15. **EPC vendor package review and acceptance.** Support `DEL-099-06` review/acceptance with traceability evidence linking REQ-VEEP-* → vendor design → FAT/SAT records.

## Verification

For each requirement in `Specification.md`, the corresponding verification approach is recorded in the Spec's *Verification* section. Record per step:

| Step | Verification Check |
|---|---|
| 2 | Vendor design basis traces every value to a source (EPC anchor, DBM, or human ruling). No unsourced values. |
| 3 | Hydraulic model demonstrates 103 m³/h per station at 345 kPad with the booster + loading pump combination (REQ-VEEP-002, 003, 004). |
| 4 | GA drawings show 3 stations + 3 pumps; skid modular split fits transport envelope. |
| 5 | Electrical drawings comply with CEC and project electrical specifications; grounding scheme documented (REQ-VEEP-008, 013, 014 once resolved). |
| 6 | Cause-and-effect matrix exists; F&G placement coordinated with EPC layout (REQ-VEEP-006, 007). |
| 9 | EPC Integrator review comments resolved; revision issued. |
| 11 | FAT records show pump performance at duty point; PLC and ESD interfaces functional. |
| 13 | SAT records demonstrate installed system meets duty at site. |
| 15 | Traceability matrix REQ-VEEP-* → design doc → FAT/SAT record is complete; `DEL-099-06` accepts. |

## Records

Vendor records produced by this Procedure:

- Vendor design basis document.
- Vendor datasheet set (loading station, loading pumps, motors, instruments, valves).
- P&IDs, GA drawings, isometrics, single-line diagrams, cable schedules, area-classification drawings.
- Hydraulic model report.
- Package PLC logic and cause-and-effect matrix (vendor draft, accepted EPC version).
- HAZOP/LOPA action close-out evidence.
- Procurement records, material certificates, code stamps (as applicable).
- FAT and SAT records.
- Shipping and turn-over packing list.
- Traceability matrix REQ-VEEP-* → design → test.

These records flow into `DEL-099-05` (Vendor Document Turnover Package) and underpin `DEL-099-06` acceptance.
