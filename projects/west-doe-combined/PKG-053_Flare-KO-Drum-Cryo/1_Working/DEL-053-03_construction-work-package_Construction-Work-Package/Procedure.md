# Procedure — DEL-053-03 Construction Work Package (Flare KO Drum, Cryo)

## Purpose

This Procedure defines the operational steps to **produce, issue, and execute** the Construction Work Package (CWP) for `PKG-053 Flare KO Drum (Cryo)`. It addresses both:

- the document-production workflow that issues the CWP for construction (EPC Integrator activity), and
- the field-execution workflow that uses the CWP to install, inspect, commission, and turn over the package.

Where the CWP itself is the deliverable, "verification" means the document is complete and accepted; where the CWP is executed in the field, "verification" means the constructed equipment passes its ITP.

## Prerequisites

### Upstream Inputs (must be available before issuing the CWP)

- `DEL-053-02 Package Datasheet` — IFC vendor handoff datasheet (sibling deliverable in PKG-053; current state per `_STATUS.md`).
- `DEL-053-04 Vendor Engineered Equipment Package` — vendor IFC drawings, weld procedures, NDE plan, vessel and heater data reports.
- IFC P&IDs covering the cryogenic flare relief network and the combined HP/cryo header — sourced from project engineering (not in accessible local source slice; **location TBD**).
- IFC plot plan and module-set drawings for module `410-1`.
- Decomposition snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`.
- Cross-facility interface agreement with the 03-25 common HP/cryo flare stack interface owner (Conflict Table item `C-053-03-02` — currently TBD).
- Joint-CWP decision with `DEL-054-03` resolved (Conflict Table item `C-053-03-01` — currently TBD).

### Declared Dependencies

- `_DEPENDENCIES.md` declares **no upstream or downstream dependencies** at present. Practical (undeclared) upstream dependence on `DEL-053-02` and `DEL-053-04` is noted as ASSUMPTION pending dependency-extract.

### Required References

- `DBM-Deepcut/4-25_Deepcut_DBM.md` §SEC-04, §SEC-09, §Equipment List, §Modularization.
- `26020-Package_Requirements.docx` heading 8 — binary; **location TBD**.

## Steps

### Phase A — Produce and Issue the CWP (EPC Integrator)

1. **Confirm prerequisites.** Verify all upstream inputs are IFC. If any are not, raise RFI and defer CWP issue.
2. **Assemble package equipment list.** Tags `V-4110-1` (Cryo Flare KO Drum) and `H-4112-1` (Cryo Flare KO Drum Immersion Heater) — source DBM-Deepcut §Equipment List rows 11-12.
3. **Define module / set scope.** Module `410-1 HP / Cryo Flare KO Drum Module`, shop-built. Confirm joint-CWP boundary with `DEL-054-03` per resolution of Conflict `C-053-03-01`.
4. **Build the tie-in register** from IFC P&IDs, isometrics, and the cross-facility interface agreement: cryo relief header (610 mm 304SS), combined HP/cryo outlet (762 mm 304SS), electrical, instrument-air, drain, vent, and instrument loops.
5. **Develop installation workface plan** including foundation set, levelling, grout, anchor, and module/vessel lift studies. Capture heat-trace EXCLUSION zones on the cryogenic header.
6. **Compile weld procedure register, NDE plan, and pressure-test plan** referencing governing codes (PROPOSAL: ASME B31.3 + ASME BPVC Sec VIII Div 1, pending Conflict `C-053-03-03`).
7. **Compile Inspection and Test Plan (ITP)** mapping each Specification requirement (R1-R9) to a verification step and evidence record.
8. **Compile pre-commissioning procedures**: cleaning, drying for cryogenic service (no internal water permitted), purge, lock-out, and dryness acceptance (dewpoint, method `location TBD`).
9. **Compile construction interface register and turnover checklist** (MC / RFC / RFSU gates with punchlist closeout structure).
10. **Verify foundation and anchorage package** (geotechnical report values, snow/wind/seismic, frost, vibration, settlement, anchor-bolt design) and incorporate as-built recording template.
11. **Internal review and IFC issue.** Document control issues the CWP for construction; revision log retained in turnover dossier.

### Phase B — Execute the CWP (Construction Contractor under EPC Integrator)

12. Site receipt and inspection of module `410-1` and ancillary components.
13. Foundation as-built and anchor-bolt installation; record pull-test data.
14. Set, level, grout, and anchor module 410-1 per workface plan.
15. Tie-in execution per tie-in register; track via tie-in punchlist.
16. Weld and NDE per weld procedure register and NDE plan; retain records.
17. Confirm cryo-header heat-trace EXCLUSION by walk-down with photographic evidence.
18. Pressure-test vessel and piping; certify.
19. Pre-commission: clean, dry, purge; record dewpoint per acceptance procedure.
20. Electrical/instrument commissioning for `H-4112-1` immersion heater (continuity, IR, control-loop function).
21. Walk down spacing compliance against IFC plot plan (OGAOM 9.6.15 distances).
22. Resolve punchlist; close out interface items with PKG-054 and the 03-25 stack interface owner.
23. Sign Mechanical Completion → RFC → RFSU certificates; assemble turnover dossier.
24. Hand off turnover dossier to `DEL-053-06 EPC Vendor Package Review and Acceptance`.

## Verification

| Step | Verification Check | Evidence |
|---|---|---|
| 1 | All upstream inputs IFC | Input register; RFI log |
| 2-3 | Equipment list and module boundary match DBM and decomposition | CWP cover page; cross-reference matrix |
| 4 | Tie-in register reconciles to IFC P&IDs (no orphan tie-ins) | Tie-in register reconciliation report |
| 5 | Workface plan reviewed and approved | Approved workface plan |
| 6 | Weld procedure register and NDE plan reference governing codes | Weld procedure register; NDE plan |
| 7 | ITP fully maps Specification R1-R9 | ITP traceability matrix |
| 8 | Pre-commissioning dryness acceptance defined | Procedure with acceptance criteria |
| 9 | Turnover checklist covers MC / RFC / RFSU gates | Checklist template |
| 10 | Foundation package complete; as-built template included | Foundation drawing log |
| 11 | Document Control IFC stamp | IFC transmittal |
| 13 | Anchor-bolt pull tests pass | Pull-test report |
| 14 | Module set within tolerance | Survey report |
| 15-16 | Tie-ins welded, NDE passed, punchlist clean | NDE log; punch closeout |
| 17 | Cryo header heat-trace EXCLUSION confirmed | Walk-down record + photos |
| 18 | Pressure test passes | Hydrotest/pneumatic test certificate |
| 19 | Dryness meets acceptance | Dewpoint record |
| 20 | Immersion heater commissioned | Electrical commissioning report |
| 21 | Spacing compliance verified | Dimensional verification record |
| 22 | All punchlist items closed; interfaces signed off | Punchlist closeout log; interface sign-off |
| 23 | MC/RFC/RFSU certificates issued | Signed certificates |

## Records

The Construction Work Package produces and retains the following records (delivered to turnover dossier and ultimately to `DEL-053-06`):

- IFC Construction Work Package (this document set, as issued)
- Installation workface plan and lift plans (approved)
- Tie-in register and tie-in punchlist (closed)
- Weld procedure register and NDE records
- Inspection and Test Plan (signed)
- Pre-commissioning procedures and dryness/cleanliness records
- Construction interface register (signed off with PKG-054 and 03-25 stack interface owner)
- Foundation as-built drawings and anchor-bolt pull-test records
- Pressure-test certificates
- Electrical and instrument commissioning records (immersion heater H-4112-1)
- Spacing/plot-plan compliance verification
- Mechanical Completion, Ready-for-Commissioning, Ready-for-Start-Up certificates
- Final turnover dossier (the anticipated artifacts per `_CONTEXT.md`)
