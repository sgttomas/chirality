# Procedure — DEL-072-03 Construction Work Package (Truck Product Loading Unit 4-25)

## Purpose

Operational procedure to produce, execute, and turn over the Construction Work Package for `PKG-072` Truck Product Loading Unit 4-25 (vendor reference `26020-01-PT-23-001 — Condensate Truck Loading Stations`). Procedure covers both (a) producing the CWP document set and (b) the field execution sequence the CWP governs.

## Prerequisites

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md` present in the deliverable folder. (Confirmed.)
- Access to authoritative sources:
  - `_Sources/26020-Package_Requirements.docx` (Package 23-001 Condensate Truck Loading Stations section).
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
  - GATE-07 decomposition snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- Vendor data baseline available before field execution: MEC-016/017, STR-006/013, ELE-027/028, INS-005/006/009/011, TSF-004, PIP-004, PIP-024/025, CIV-003/004 (per `26020-Package_Requirements.docx` Vendor Engineering Deliverables list).
- Permit amendment for truck rack confirmed in place or staging plan documented (`4-25_Deepcut_DBM.md` line 133).
- LACT scope decision recorded or its impact on this package documented (`4-25_Deepcut_DBM.md` lines 62, 82, 171). `TBD` if undecided.
- Site civil works (CIV-003 grading) sequenced upstream of foundation pours. (No declared upstream dependencies in `_DEPENDENCIES.md`; sequencing inferred from typical EPC practice — ASSUMPTION.)

## Steps

### Part A — Produce the CWP document set

1. Confirm package identity and scope against `_CONTEXT.md` and the GATE-07 `DELIVERABLE_REGISTER.csv` DEL-072-03 row.
2. Resolve the Conflict Table items in `Guidance.md` to whatever extent is possible before issuing the CWP; mark remaining items `TBD` and route to the human reviewer.
3. Compile vendor engineering deliverable references (PIP, ELE, INS, CIV, STR, TSF, MEC, CTL, QLT, PRQ) into the CWP appendix using the list in `26020-Package_Requirements.docx` Vendor Engineering Deliverables for this package.
4. Produce the Installation and Tie-In Workface Plan (referenced by `_CONTEXT.md` Anticipated Artifacts). Steps for the workface plan: TBD per EPC Integrator workface planning standard (`location TBD`).
5. Produce the Construction Interface and Turnover Checklist covering every interface marked "Yes" in the Physical Interface Summary.
6. Walk the CWP through internal QA / discipline checks (civil, structural, piping, electrical, I&C, safety, F&G).
7. Issue the CWP for construction (IFC) when:
   - vendor data baseline is in place,
   - layout meets API 2510 separation distances,
   - permits or staging plan are in place,
   - LACT and off-loading responsibility conflicts are either resolved or explicitly carried as documented holds.

### Part B — Field execution sequence governed by the CWP

1. **Receive at site.** Off-load truck loading station modules per PRQ-013 Logistics/Shipping Plan. (NOTE: confirm responsibility per Conflict CFL-072-03-05.)
2. **Site preparation and civil.** Implement CIV-003 grading, CIV-004 drainage / stormwater, and any CIV-015 containment basin geometry locally required around the loading station. Verify API 2510 separation distances on the as-built layout before foundation pours.
3. **Foundations and supports.** Pour foundations per STR-006; install anchor bolts per STR-013; install structural supports per STR-002 GA and STR-011 platform/access drawings. Record concrete and material certs per QLT-013.
4. **Set the loading station(s).** Lift and set per MEC-018 Lifting/Handling Study and MEC-017 Installation/Setting Drawings.
5. **Process piping tie-ins.** Install per PIP-006-PIP-008 with fabrication isometrics PIP-009 and material per PIP-017 MTO. Pressure test per PIP-024; flush and clean per PIP-025. (Hold metering geometry per LACT decision — Conflict CFL-072-03-04.)
6. **Drainage and spill containment.** Implement per CIV-014 / CIV-015. Verify drainage flow to designed retention/containment.
7. **Electrical.** Install per ELE-014 cable schedule, ELE-015 cable tray, ELE-016 layout, ELE-027 details, ELE-028 interconnection; install lighting per ELE-017; install grounding/bonding per ELE-012 study and ELE-019 layout. Test per ELE-029 / ELE-030.
8. **Instrumentation & Controls.** Install per INS-005 location plans, INS-006 hook-up drawings, INS-009 wiring/termination, INS-011 cable schedule. Loop check per INS-008 loop diagrams. Tie-in to DCS per CTL-006 I/O list and CTL-026 package vendor interface specification.
9. **Fire & Gas.** Install detectors per TSF-004 layout drawings; verify mapping per TSF-003; record SIL/safety documentation per TSF-009/TSF-011/TSF-013.
10. **Pre-commissioning.** Execute discipline pre-commissioning checks; punchlist; sign off.
11. **Turnover.** Complete the Construction Interface and Turnover Checklist; transfer custody to commissioning/operations per project-level turnover procedure (`location TBD`).

## Verification

- API 2510 separation distances (15.24 m / 50 ft) verified by survey before foundation pours. (`4-25_Deepcut_DBM.md` lines 257-258.)
- Foundation acceptance signed off using STR-005 calculations and QLT-013 material test reports. (Vendor deliverable index.)
- Hydrotest packages (PIP-024) signed off for all in-scope piping.
- Electrical test records (ELE-030) and I&C loop check sheets completed.
- F&G detector mapping verification (TSF-003 walkthrough) completed.
- All interfaces marked "Yes" in the Physical Interface Summary closed on the Construction Interface and Turnover Checklist.
- Conflict Table items either resolved (with the ruling recorded in `Guidance.md`) or carried forward with a documented hold.

## Records

- Construction Work Package (IFC) document set (this deliverable's four documents plus formal appendices) — retained in the project document control system.
- Installation and Tie-In Workface Plan (anticipated artifact).
- Construction Interface and Turnover Checklist (anticipated artifact).
- Hydrotest / pressure test packages (PIP-024 records).
- Flushing / cleaning records (PIP-025).
- Electrical test records (ELE-030).
- Instrument loop check sheets (built from INS-008).
- Material test reports / certificates (QLT-013).
- Inspection Release Certificate (QLT-020) and Manufacturing Record Book / Vendor Data Book (QLT-021, MEC-023, PRQ-016).
- Punch list and turnover sign-off (project standard, `location TBD`).
- Run record: `_run_records/TASK_RUN_2026-05-25_0511.md`.
