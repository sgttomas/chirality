# Procedure: DEL-090-03 — Construction Work Package (Vapour Recovery Unit 3-25)

## Purpose

This procedure describes how to **produce** the Construction Work Package artifact and the supporting installation and tie-in workface plan and turnover checklist, and how to **execute** the resulting plan on site for the PKG-090 VRU 3-25 install. It is operational; it does not redefine the requirements in `Specification.md`.

## Prerequisites

### Declared upstream dependencies

- `_DEPENDENCIES.md` lists no declared upstream dependencies as of PREPARATION (2026-05-24). Effective upstream inputs are therefore derived from references and decomposition context; declared coordination edges should be added to `_DEPENDENCIES.md` once known.

### Effective upstream inputs (best-effort, source-grounded)

- Accepted Gate 7 PROJECT_DECOMP snapshot (`_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`), specifically:
  - `PACKAGE_REGISTER.csv` row `PKG-090`
  - `DELIVERABLE_REGISTER.csv` row `DEL-090-03_construction-work-package`
- `_Sources/26020-Package_Requirements.docx`, section `26020-01-PT-12-002 - Vapour Recovery Unit` (in full, including the Physical Interface Summary table and the Vendor Engineering Deliverables table)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-06 ("Vapour Recovery"), SEC-04 (SCA reconciliation), and SEC-05 (compressor area context)
- Vendor engineering deliverables listed under `26020-01-PT-12-002 / Vendor Engineering Deliverables` (core vendor documents, core package engineering, rotating equipment, relief/flare/vent design, process piping, utility piping, drainage/containment, electrical/lighting/EHT/grounding, I&C, fire and gas, structural). These are external inputs to construction; their availability gates several steps below.

### Required references (existence / locally accessible)

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (present)
- 26020 package requirements section PT-12-002 (present)
- 3-25 DBM SEC-06 (present)
- Vendor MEC/PIP/ELE/INS/STR/REG packages — TBD; not present in local source set. Steps that depend on these are flagged ".

## Steps

### Phase A — Build the Construction Work Package artifact

1. Read in full: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, the GATE-07 PROJECT_DECOMP `PACKAGE_REGISTER.csv` row for PKG-090, the GATE-07 `DELIVERABLE_REGISTER.csv` row for DEL-090-03, the 26020 PT-12-002 section, and DBM SEC-06.
2. Confirm the vendor/EPC split as captured in `PACKAGE_REGISTER.csv` PKG-090. Record exclusions (Section 1 "Out of scope" of `Specification.md`) and confirm the "by others" items (shipping, install on piles, tie-in piping, electrical, instrumentation) are explicitly carried as EPC scope.
3. Populate the CWP scope and requirements directly from `Specification.md` (do not paraphrase requirements; reference R-CWP-090-001 through R-CWP-090-017 verbatim and add CWP-specific narrative).
4. Build the construction interface and turnover checklist as a 1:1 mapping to the PT-12-002 Physical Interface Summary `Yes` rows. Each row gets: interface name, scope owner (EPC or vendor), tie-in tag/location (TBD until vendor PIP-004 Tie-In List is received), acceptance test, sign-off owner.
5. Build the installation and tie-in workface plan as the sequenced execution view (Phase B steps below) with workpack-sized scopes.
6. Identify all dependencies on vendor deliverables (MEC-016/017/018, PIP-004/008/009/024/025, ELE-029/030, INS-008, STR-005/006/013, REG-022, TSF-009/011). Mark each as REQUIRED-FOR-EXECUTION with the workface step it gates.
7. Capture all TBD items and route open Conflict Table items (`Guidance.md` CFLT-090-03-001/002/003) for ruling before the CWP is approved for execution.

### Phase B — Execute the installation and tie-in workface plan

8. Foundation readiness. Verify foundation, anchor bolts, and embedments are in place per vendor STR-005/006/013. Hold-point: vendor anchor-bolt pattern reconciled with as-built civil work. (R-CWP-090-016)
9. Lift and set. Execute lifting per vendor MEC-018 Lifting/Handling Study. Set the VRU building / compressor train modules in the lead-lag configuration. Verify dimensional alignment against MEC-016/017. (R-CWP-090-001, R-CWP-090-015)
10. Mechanical hookup of vendor scope. Allow the vendor to complete internal package mechanical hookup per their package design (Plan-53 seal buffer system, internal compressor piping, motor coupling). EPC verifies completion before adding facility tie-ins. (R-CWP-090-002, R-CWP-090-004)
11. Process piping tie-ins. Execute tie-in piping to vendor flanges per vendor PIP-004 Tie-In List and PIP-008 Isometric Drawings. Install:
   - VRU suction header (from tank vapour systems and selected process vents);
   - LP flare bypass V-ball valve on the suction header with free-drain slope to flare KO interface (R-CWP-090-006);
   - Recycle line (second-stage discharge to first-stage suction) (R-CWP-090-007);
   - Make-up / blanket gas line from LP fuel gas with regulator (R-CWP-090-008);
   - Discharge line to the 04-25 SOC suction (R-CWP-090-005; do not install any 03-25 local SOC tie-in).
   All sour-service welds: NACE-qualified materials, weld procedures, and NDE per the piping ITP. (R-CWP-090-003)
12. Utility piping tie-ins. Connect LP fuel gas (make-up regulator and Plan-53 seal buffer supply) and instrument air (from 04-25 per SCA-006). Confirm by walkdown that no local 03-25 instrument-air or local SOC tie-ins were inadvertently installed.
13. Relief, flare, vent tie-ins. Tie in primary seal vent to LP flare; PSV discharges per vendor PRO-014/015/016. Verify slope and free-drain back toward the flare KO drum interface. (R-CWP-090-004, R-CWP-090-006)
14. Drain and containment tie-ins. Tie in compressor packing drains / seal pot vapour line to the relevant VRU suction / vacuum pump interface as defined in the vendor package design (cross-reference DBM SEC-05 compressor drain/vent practice). Close any closed-drain interfaces.
15. Electrical, lighting, EHT, grounding. Pull motor feeders to each 200 HP VFD driver, complete EHT circuits, run area/exterior lighting, complete grounding/bonding. Run electrical FAT/SAT per ELE-029, capture energization test records per ELE-030. (R-CWP-090-014)
16. I&C / control cabling. Pull instrument and control cabling between vendor marshalling and facility DCS/SIS per vendor CTL-026 Package Vendor Interface Specification, INS-008 Loop Diagrams, and INS-011 Cable Schedule. Execute instrument loop checks. (R-CWP-090-014)
17. Fire and gas / safety systems. Install F&G detectors and ESD interfaces per vendor TSF-003/004 and SRS per TSF-011. Confirm SIL implementation per TSF-009. (R-CWP-090-009)
18. Pre-commissioning checks. Hydrotest new tie-in piping per PIP-024 Hydrotest Packages; flush, clean, and dry per PIP-025. (R-CWP-090-013)
19. Pressure equipment registration. Confirm vendor REG-022 Pressure Equipment Registration Package is accepted by the AHJ before any pressurization. (R-CWP-090-017)
20. Punch-list and mechanical completion. Close construction punch items; capture as-builts (PIP-028, INS-029, vendor red-lines).
21. Turnover to commissioning. Walk the construction interface and turnover checklist (Phase A step 4) with the commissioning lead; record sign-offs.

## Verification

| Step | Verification |
|---|---|
| Phase A step 4 | The construction interface and turnover checklist has one row per PT-12-002 `Yes` interface; each row has an acceptance test and an owner. |
| Phase A step 5 | The workface plan covers every Phase B step; each workpack has prerequisites traceable to vendor deliverables. |
| Phase B step 8 | Foundation/anchor inspection report on file; no anchor-pattern non-conformances open. |
| Phase B step 9 | Lift records and module set survey reports show modules placed within tolerance. |
| Phase B step 11 | Tie-in walkdown confirms (a) discharge routed to 04-25 SOC suction, (b) LP flare bypass V-ball installed and stroke-tested, (c) suction header free-drains toward flare KO interface, (d) no 03-25 local-SOC tie-in present. Sour-service NDE records on file. |
| Phase B step 13 | Seal vent line continuity confirmed to LP flare. |
| Phase B step 15-16 | ELE-029/030 records on file; instrument loops closed per INS-008; F&G loop tests complete. |
| Phase B step 18 | PIP-024 hydrotest packages signed off; PIP-025 flush/clean/dry records on file. |
| Phase B step 19 | AHJ-accepted REG-022 pressure equipment registration on file. |
| Phase B step 21 | Construction-to-commissioning turnover checklist signed by both parties. |

## Records

Records produced by this procedure (to be filed in the project document control system, with pointers placed into the CWP):

- Construction Work Package (artifact this deliverable produces).
- Installation and tie-in workface plan (artifact this deliverable produces).
- Construction interface and turnover checklist (artifact this deliverable produces).
- Foundation/anchor inspection reports.
- Lift execution records.
- Hydrotest packages (PIP-024).
- Flushing / cleaning / drying records (PIP-025).
- Electrical FAT/SAT records (ELE-029) and energization records (ELE-030).
- Instrument loop check records.
- F&G commissioning records.
- AHJ-accepted pressure equipment registration package (REG-022).
- Punch list closure record and mechanical completion certificate.
- As-built drawings (PIP-028, INS-029, vendor red-lines).
- Turnover-to-commissioning sign-off.

## Open items / TBD

- Vendor deliverables (MEC, PIP, ELE, INS, STR, REG, TSF) are not in the local source set; their content gates Phase B steps and is treated as TBD until received.
- Conflict Table items in `Guidance.md` (CFLT-090-03-001/002/003) must be ruled before the CWP is approved for execution.
- Specific code clauses for sour-service piping (NACE), pressure equipment registration (BC), electrical (CEC) and fire & gas / SIL standards: location TBD.
