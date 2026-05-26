# Procedure — DEL-082-03 Construction Work Package (LP Flare KO Drum, 3-25)

## Purpose

Describe the operational steps the EPC Integrator follows to produce, execute, and turn over the Construction Work Package for PKG-082 — Flare KO Drum (Low Pressure) 3-25 — covering vessel V-3900-2, pump P-3900-2, the 508 mm LP relief header tie-ins, and the LP flare stack interface within the 03-25 boundary (SourcePath: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SectionRef: SEC-07 Flare and Blowdown).

## Prerequisites

Upstream and reference inputs:

- No upstream dependencies declared in `_DEPENDENCIES.md` at PREPARATION time. ASSUMPTION (industry convention): detailed design deliverables for the LP flare KO drum (process datasheet, mechanical drawings, P&ID, ISOs) and the upstream Plant Shutdown and Blowdown Philosophy W242510-PRC-REP-000003-001 are required before construction execution but were not declared upstream during PREPARATION.
- Accepted decomposition snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- Accessible source reference: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-07 and SEC-09.
- Final geotechnical report (DBM SEC-09 line 700) — required for foundation design acceptance; access status TBD.
- Approved HAZOP closeout for the LP relief path — required for isolation philosophy implementation (DBM SEC-09 line 607); status TBD.

Site / readiness prerequisites:

- Foundations accepted by civil/structural QA before vessel and pump setting.
- Pipe-rack steel for the 508 mm LP relief header in place at the relevant grid.
- Shared flare stack interface allocation between 03-25 and 04-25 confirmed (currently open — DBM SEC-01 line 56). See Conflict C-02 in Guidance.

## Steps

1. **Pre-construction package assembly.**
   - Compile the CWP document set: this Procedure, the Specification, the Datasheet, and the Guidance, plus referenced design deliverables when issued.
   - Issue the installation and tie-in workface plan (anticipated artifact per `_CONTEXT.md`).
   - Issue the construction interface and turnover checklist (anticipated artifact per `_CONTEXT.md`).
2. **Site readiness and foundation acceptance.**
   - Confirm foundation pour, anchor-bolt layout, and grout integrity per the issued civil package; obtain civil acceptance before mechanical setting (DBM SEC-09 line 700 basis).
3. **Mechanical setting.**
   - Set LP flare KO drum V-3900-2 on the accepted foundation.
   - Set transfer pump P-3900-2 (1 x 100 percent per DBM SEC-09 line 584).
   - Record anchor-bolt torque, level, and alignment.
4. **Piping construction — LP relief header.**
   - Fabricate and install the 508 mm (20 inch) LP relief header per ISOs (DBM SEC-07 line 499).
   - Tie in TEG regeneration, VRU, and compressor seal-pot service relief inlets (DBM SEC-07 line 499).
   - Implement isolation philosophy: double block/bleed or equivalent for sour service per HAZOP (DBM SEC-09 line 607).
   - Honor vent/drain segregation by pressure, sour-service, and contamination class (DBM SEC-09 line 607).
5. **Stack interface tie-in.**
   - Execute the 03-25-side tie-in of the LP relief header to the shared HP/Cryo + LP dual flare stack within the 03-25 interface envelope. Defer final stack-side connection pending OD resolution (DBM SEC-07 line 499; Guidance Conflict C-01).
6. **Pump transfer line.**
   - Install P-3900-2 discharge transfer line to slop system (DBM SEC-07 line 499).
7. **Instrumentation and electrical hook-up.**
   - Connect pump electrical feed from the assigned LV MCC; confirm current emergency-power scope under SCA revision before final energization (DBM SEC-07 line 505).
   - Install KO drum level instrumentation and pump controls per the (TBD) IO list.
8. **NDE and pressure testing.**
   - Perform NDE per the issued weld map. Extents — TBD (R-10 of Specification).
   - Pressure-test per the issued test packs. Pressures and medium — TBD (R-10).
   - PWHT, where required by material/thickness rules — TBD.
9. **Pre-commissioning.**
   - Clean and purge per the issued cleaning specification.
   - Verify staggered blowdown logic implementation against the Blowdown Philosophy W242510-PRC-REP-000003-001 (DBM SEC-07 line 501); hold final SIS verification until that document is accessible (Guidance Conflict C-03).
10. **Mechanical completion and turnover.**
    - Complete the construction interface and turnover checklist.
    - Issue Mechanical Completion to commissioning.

## Verification

| Check | Method |
|---|---|
| Foundation acceptance prior to setting | Civil QA sign-off recorded in CWP file. |
| Vessel/pump tag identity (V-3900-2 / P-3900-2) | Tag-stamp and nameplate verification against DBM SEC-07. |
| LP relief header size 508 mm | Material certs and isometric check (DBM SEC-07 line 499). |
| Service inventory at LP KO drum | Walk-down vs P&ID and DBM SEC-07 line 499. |
| Sparing — single LP transfer pump | Equipment list reconciliation vs DBM SEC-09 line 584. |
| Sour-service isolation provisions | HAZOP closeout vs as-built (DBM SEC-09 line 607). |
| Pressure test acceptance | Test packs signed and dated. |
| Blowdown logic | Loop check and SIS proof vs Blowdown Philosophy (hold pending document access). |

## Records

- Mechanical Completion certificate for PKG-082 scope.
- Foundation and anchor-bolt records.
- Weld register and NDE reports.
- PWHT records (where applicable; TBD).
- Pressure-test records.
- Cleaning and purging records.
- Punch list and turnover checklist (Construction → Commissioning).
- HAZOP/PSSR closeout records for the LP KO drum and pump scope.
- As-built redlines for the LP relief header, vessel orientation, pump alignment, and instrumentation routing.
