# Procedure — Construction Work Package (DEL-058-03)

## Purpose

This procedure describes the sequenced steps to produce the EPC Integrator Construction Work Package (CWP) artifact set for `PKG-058 Medium Pressure Flash Feed Separator` (modules `710-1` and `730-1`) and to execute construction interface and turnover. Both authoring and execution-interface steps are included because the EPC Integrator authors the CWP and Tourmaline field construction executes most field steps (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 100-127).

## Prerequisites

- Upstream `DEL-058-01 Scope of Work` issued (covers `SOW-0139`-`SOW-0142`).
- Upstream `DEL-058-02 Package Datasheet` issued (vendor engineering handoff basis).
- Accepted decomposition snapshot `GATE-07_Final_Published_2026-05-24`.
- Locally accessible DBM source slice (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility, MPFF system, Module list).
- Geotechnical report release — TBD (required for foundation acceptance criteria).
- Vendor package engineering progress sufficient to confirm equipment tags, nozzle layouts, shipped-loose registers — sourced from `DEL-058-04` when issued.

## Steps

### Authoring steps (EPC Integrator)

1. **Confirm module inventory.** Cross-check module IDs `710-1` and `730-1` and tagged vessels `V-7110-1` / `V-7310-1` (and optional `E-7120-1`) against `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2544, 2603-2604, 2804, 2806.
2. **Document responsibility split.** Author a per-activity responsibility matrix from the DBM Construction Responsibility table (lines 105-126), explicitly flagging activities that are EPC-authored work-pack content versus Tourmaline-executed field scope.
3. **Author installation and tie-in workface plan.** For each ISBL/OSBL tie-in, define:
   - tie-in tag and P&ID reference,
   - upstream/downstream isolation provisions (per maintenance-isolation philosophy, line 2408),
   - per-tie-in responsibility (line 117),
   - timing window (joint-planning placeholder per line 127).
4. **Author construction interface and turnover checklist.** Include foundation acceptance, module-set sign-off, mechanical hookup completion, instrumentation install/calibration, electrical termination, loop checks, hydrotest/pneumatic test, blowdown valve stroke test (per R10), methanol injection install verification (per R6), self-framing building close-up, and turnover document gating.
5. **Mark TBDs.** Record items dependent on geotechnical, heater bundle disposition, or `26020-Package_Requirements.docx` clauses as `TBD` rather than inferring values.
6. **Issue CWP for review.** Route through `DEL-058-06 EPC Vendor Package Review and Acceptance` interfaces for acceptance.

### Execution-interface steps (EPC Integrator coordinates; Tourmaline executes)

7. **Foundation handoff.** Confirm foundation acceptance certificate from Tourmaline civil before module set.
8. **Module shipping receipt.** Verify shop fabrication completion documents and shipping manifests for `710-1` and `730-1` (Tourmaline off-loads per line 112).
9. **Module setting.** Witness setting on foundation; sign module-set milestone.
10. **Mechanical hookup.** Verify interconnect piping, skid-edge isolation, and structural support installation per workface plan (lines 113-116, 2454).
11. **Shipped-loose installation.** Confirm shipped-loose instruments, valves, and components installed per vendor turnover register (line 115; `DEL-058-05`).
12. **Tie-in execution.** For each ISBL/OSBL tie-in, execute per per-tie-in responsibility log (R4) and joint-planning schedule.
13. **Electrical terminations and home-run cables.** Witness Tourmaline electrical scope completion (lines 118-119).
14. **Self-framing building close-up.** Verify building lighting, F&G, HVAC (if any — TBD), and instrumentation enclosure (R7).
15. **Test and pre-commissioning.** Witness hydrotest/pneumatic test, loop checks, blowdown valve stroke test (R10), methanol injection line check (R6), purge-gas regulator setpoint verification (R11).
16. **Punch-list closure.** Drive punch list to zero category-A items.
17. **Turnover.** Issue mechanical completion package per turnover checklist; obtain Tourmaline operations acceptance signature.

## Verification

- Per-step sign-offs collected on the construction interface and turnover checklist.
- Authoring-step QA: cross-document terminology and value consistency (Datasheet ↔ Specification ↔ Guidance ↔ Procedure).
- Execution-step QA: each tie-in has an entry in the per-tie-in responsibility log; each module has a signed mechanical completion package.
- All `TBD` items remaining at turnover are surfaced to the deliverable `MEMORY.md` (not modified by this skill run) for downstream resolution.

## Records

- Construction work package document (this deliverable).
- Installation and tie-in workface plan.
- Construction interface and turnover checklist.
- Per-tie-in responsibility log.
- Foundation acceptance certificates (`710-1`, `730-1`).
- Module-set milestone records.
- Mechanical completion packages per module.
- Hydrotest, loop check, calibration, stroke test records (referenced from vendor turnover package `DEL-058-05`).
- Punch-list register and closure record.
- Turnover acceptance signature page.
