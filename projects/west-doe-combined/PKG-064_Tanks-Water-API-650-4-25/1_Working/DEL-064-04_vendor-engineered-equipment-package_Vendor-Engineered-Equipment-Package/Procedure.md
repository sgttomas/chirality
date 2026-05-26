# Procedure: DEL-064-04 — Vendor Engineered Equipment Package (Tanks, Water (API 650) 4-25)

> Operational procedure to **produce** the vendor engineered equipment package (engineering, design, fabrication/supply, physical delivery) for PKG-064 process water storage tanks at the 4-25 Deepcut facility. Steps requiring values not currently available are marked `TBD`.

## Purpose

Define the end-to-end vendor workflow from EPC Package Datasheet handoff (`DEL-064-02`) through engineered design, fabrication/supply, factory acceptance, and ex-works delivery of the process water storage tank package (`TK-5317-1`, `TK-5318-1`), including the engineering/design deliverables required by EPC Integrator review (`DEL-064-06`) and turnover (`DEL-064-05`).

## Prerequisites

**Declared upstream dependencies (per `_DEPENDENCIES.md`):** None declared during PREPARATION. The following are inferred-required upstream inputs (ASSUMPTION):

- `DEL-064-01` — EPC Scope of Work (PROJECT_DECOMP row 540): scope envelope, boundaries, responsibility assignment.
- `DEL-064-02` — Package Datasheet (PROJECT_DECOMP row 541): tank service, capacity, design SG, material, coating, nozzle/instrument schedule, interface requirements.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — site basis, atmospheric tank discipline, freeze-protection requirement, spacing, applicable standards.
- `_Sources/26020-Package_Requirements.docx` heading 19 — package-level requirements (binary source; extract before vendor design freeze).

**References required:**
- API 650 (current edition) — tank fabrication standard.
- API 2000 — venting / blanket-gas sizing.
- OGAOM — plant spacing.
- Applicable AB/BC pressure-equipment regulations, CSA, ASME B31.3 for tank-package piping, AWS welding codes.

**Information required at kickoff (raise TBD/Conflict if not provided):**
- Process water composition and design specific gravity.
- Tank capacity per tank.
- Material of construction direction.
- Coating direction.
- VRU connectivity ruling (per Guidance — CFT-064-04-03).
- Nozzle list, instrument I/O list, electrical/utility loads expected by EPC Integrator.

## Steps

1. **Receive and review handoff.**
   1.1 Receive `DEL-064-02` Package Datasheet from EPC Integrator.
   1.2 Receive and check `DEL-064-01` Scope of Work for scope boundaries and exclusions.
   1.3 Reconcile package line-item equipment list against PROJECT_DECOMP row 2628 (`TK-5317-1`, `TK-5318-1`).
   1.4 Log any missing inputs as `TBD` and escalate to EPC Integrator before design freeze.

2. **Establish vendor package design basis.**
   2.1 Draft vendor package design basis document referencing the EPC Package Datasheet, the West Doe Deepcut DBM, and applicable standards.
   2.2 Document the "Modified API 650" deviations from straight API 650 (test pressure 16 oz/in², 90% max fill, etc., per Specification R-064-04-02/03/04).
   2.3 Capture freeze-protection requirement (Specification R-064-04-05) and PVRV/EPRV approach (R-064-04-06).
   2.4 Issue for EPC Integrator review; revise to address comments.

3. **Engineer and design the tanks.**
   3.1 Produce tank datasheet(s) (one per tank).
   3.2 Produce general arrangement and outline drawings.
   3.3 Produce nozzle schedule and orientation drawing.
   3.4 Produce foundation loading drawing (loads to civil/structural).
   3.5 Specify materials of construction; produce weld procedure and inspection plan.
   3.6 Specify insulation and heat-tracing system.
   3.7 Specify internal coating (if any) consistent with Package Datasheet fluid spec.
   3.8 Specify instrumentation: level, temperature, pressure, PVRV; produce instrument index and loop diagrams for vendor-supplied instruments.
   3.9 Perform vent/relief/blanket-gas sizing per API 2000.
   3.10 Issue engineering package for EPC Integrator review.

4. **Produce interface package for integration review.**
   4.1 Assemble nozzle loads, instrument I/O list, electrical loads, utility connections (instrument air, blanket gas, drain, etc.), and operating/upset case summary.
   4.2 Submit to EPC Integrator for `DEL-064-06` review and acceptance.

5. **Fabricate and supply.**
   5.1 Procure materials per spec; collect mill certificates.
   5.2 Fabricate per API 650; execute weld inspection per ITP.
   5.3 Perform hydrostatic test per API 650.
   5.4 Apply coating(s) per spec; perform coating inspection.
   5.5 Apply insulation and heat trace, or supply for field application per spec.
   5.6 Install/commission vendor-supplied instruments.
   5.7 Produce Manufacturer's Data Report (MDR) per API 650.

6. **Factory acceptance / shop turnover preparation.**
   6.1 Execute Factory Acceptance Test (FAT) per the ITP / Package Datasheet (`TBD` — scope of FAT to be confirmed in Package Datasheet).
   6.2 Assemble vendor document package per `DEL-064-05` turnover spec: datasheets, drawings, MDR, mill certs, weld and inspection records, coating reports, ITP results, O&M manuals, spare parts list.
   6.3 Issue documentation to EPC Integrator for review (`DEL-064-06`).

7. **Deliver to site.**
   7.1 Coordinate delivery, rigging, and offloading with EPC Integrator (handoff to `DEL-064-03` Construction Work Package).
   7.2 Provide vendor field support per Package Datasheet (`TBD` — quantity of vendor field support visits).

## Verification

| Step | Verification |
|---|---|
| 1 | Handoff transmittal record; TBD/conflict log issued before design freeze. |
| 2 | EPC Integrator design-basis review acceptance. |
| 3 | Engineering review comments closed; revisions accepted. |
| 4 | `DEL-064-06` integration-review acceptance record. |
| 5 | API 650 MDR; hydrostatic test report; coating inspection report; weld inspection records. |
| 6 | FAT report; turnover document package complete per `DEL-064-05`. |
| 7 | Delivery/offload sign-off; field-support visit record. |

## Records

- Vendor package design basis document (issued, revised, accepted)
- Tank datasheets (per tank)
- General arrangement / outline drawings
- Foundation loading drawing
- Nozzle schedule and orientation drawing
- Material certificates / mill certs
- Weld procedure specs, welder qualifications, weld inspection records
- Coating spec and inspection reports
- Insulation / heat-trace spec
- Instrumentation index, loop diagrams, factory calibration certificates
- Vent / blanket-gas / PVRV sizing calculations
- Manufacturer's Data Report (API 650 MDR)
- Hydrostatic test report
- Factory Acceptance Test report
- O&M manuals
- Spare parts list
- Interface package transmitted to EPC Integrator for `DEL-064-06`
- Delivery / offload sign-off

Final turnover collection and register are `DEL-064-05` scope.
