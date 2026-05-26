# Procedure: DEL-061-03 — Construction Work Package (NGL Booster and Transfer Pumps Building)

## Purpose

This procedure describes how the EPC Integrator produces the Construction Work Package (CWP) for PKG-061 and how the CWP, once issued, guides field execution from foundation readiness through mechanical completion and turnover. It covers both the authoring path (produce the artifact) and the execution path (use the artifact) at the level of operational steps. Specific design values come from the Package Datasheet (DEL-061-02) and the Vendor Engineered Equipment Package (DEL-061-04); this procedure does not duplicate them.

## Prerequisites

- DEL-061-01 (Scope of Work) initialized at least to `INITIALIZED` so the package scope, equipment basis, and integration boundary are stable. (Reference: sibling deliverable under PKG-061.)
- DEL-061-02 (Package Datasheet) available, at least in draft, so design conditions (especially TDH and any sour/LPG materials requirements) can flow into the CWP as design intent. (Reference: sibling deliverable under PKG-061; SCOPE_LEDGER.csv SOW-0152 TBD TDH.)
- Accessible upstream snapshot: GATE-07 Final Published PROJECT_DECOMP snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`. (Reference: `_REFERENCES.md`.)
- Accessible source slices: SCOPE_LEDGER.csv SOW-0149/0150/0151/0152; PACKAGE_REGISTER.csv row for PKG-061; DBM-Deepcut rows 2548, 2609, 2818 (NGL Booster and Transfer Pumps Building); DBM-Deepcut sparing-table row 2338-2339 (informing context).
- No declared upstream construction blockers (per `_DEPENDENCIES.md`).

`_REFERENCES.md` flags that no deliverable-specific source slices were copied during PREPARATION; drafting therefore uses the decomposition registers as the primary source set and the DBM-Deepcut markdown for cross-referenced equipment context.

## Steps

### Authoring path — produce the CWP

1. **Confirm identity and scope envelope.** Lift DeliverableID, package, equipment tags, and scope-of-work IDs from `_CONTEXT.md` and the deliverable register. Verify the SOW set is `SOW-0149; SOW-0150; SOW-0151; SOW-0152`. (Source: `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row for DEL-061-03.)
2. **Capture the equipment and module basis.** Record P-9570-1 / P-9580-1; vertical multistage can-type API 610 pumps; seal plan 13/52; 575 V / 3 ph / 60 Hz motors; shop-assembled module ("950-1 LPG Booster and Transfer Pump Module"). (Source: SCOPE_LEDGER.csv SOW-0151; DBM-Deepcut/4-25_Deepcut_DBM.md rows 2609, 2818.)
3. **Enumerate applicable interfaces.** Transcribe the 13 PKG-061 interface types into the CWP interface checklist. (Source: PACKAGE_REGISTER.csv row for PKG-061.)
4. **Record EPC-only scope explicitly.** Capture DCS integration, foundations, and electrical supply to MCC as EPC-side items called out in the workface plan. (Source: SCOPE_LEDGER.csv SOW-0152.)
5. **Carry open items forward.** For TDH, materials specification, hazardous area classification clause-level text, and field environment values, record `TBD` with a resolution owner (DEL-061-02 or DEL-061-04) instead of inventing values.
6. **Draft the workface plan.** For each interface in step 3, write tie-in steps in the order: receive → set → connect utility/process → loop-check → pressure/leak test → commissioning support → turnover. Reference upstream design deliverables rather than embedding design content.
7. **Draft the turnover checklist.** Structure as one row per interface; include acceptance criterion (e.g., FAT certificate received, CRN registration verified, loop check signed) and turnover record (e.g., punch-list closure, system-handover form).
8. **Cross-link with companion deliverables.** Add explicit references to DEL-061-01 (SOW), DEL-061-02 (Package Datasheet), DEL-061-04 (Vendor Equipment Package), DEL-061-05 (Vendor Document Turnover Package), and DEL-061-06 (EPC Vendor Package Review and Acceptance).
9. **Author review.** Confirm each requirement in `Specification.md` (R1-R12) maps to at least one CWP section, and that each TBD is preserved (do not silently resolve).

### Execution path — use the CWP in the field

10. **Foundation readiness.** Confirm grout strength, anchor bolt geometry, and level prior to module set, with weights and base plate drawing per DEL-061-02 (TBD pending vendor data). (Source: SCOPE_LEDGER.csv SOW-0152.)
11. **Lift and set.** Execute the lift plan/rigging study for the module envelope; record set elevations and grout fill.
12. **Mechanical tie-in.** Connect process and utility piping per the workface plan; verify seal plan 13/52 receipt; record CRN/TSBC tags as applicable. (Source: SCOPE_LEDGER.csv SOW-0151.)
13. **Electrical and I&C tie-in.** Terminate MCC feeder; verify 575 V / 3 ph / 60 Hz at package terminals; complete loop checks of instrumentation back to the facility DCS. (Source: SCOPE_LEDGER.csv SOW-0151 drive basis; SOW-0152 DCS integration and MCC supply.)
14. **Building services and safety systems.** Verify HVAC/enclosure operation, EHT energization (per design), grounding/bonding continuity, area/exterior lighting, and fire/gas detection per the workface plan. (Source: PACKAGE_REGISTER.csv interface list for PKG-061.)
15. **Pre-commissioning checks.** Confirm punch-list closure for each interface row in the turnover checklist before vendor commissioning support is engaged.
16. **Vendor commissioning support.** Activate vendor commissioning hours per SOW-0151 to support initial start, performance checks, and operability verification.
17. **Turnover.** Sign the turnover checklist, deliver records into the package turnover dossier, and close out the CWP against DEL-061-06.

## Verification

| Step Group | Verification |
|---|---|
| Authoring (1-9) | Author-review checklist confirms identity, scope, interface list completeness, EPC-only items, and TBD preservation. |
| Foundation/set (10-11) | Grout/level inspection records; lift plan execution sign-off. |
| Mechanical tie-in (12) | Tie-in pressure/leak test records; seal plan field verification record; CRN/TSBC verification. |
| Electrical/I&C (13) | Terminal box voltage check record; loop check records signed. |
| Building services / safety (14) | Interface acceptance forms signed per checklist row. |
| Pre-commissioning (15) | Punch-list closure log per interface. |
| Commissioning (16) | Vendor commissioning report; pump performance vs. design (TDH closure when DEL-061-02 firms up). |
| Turnover (17) | Signed turnover checklist; CWP closeout note in DEL-061-06. |

## Records

Records produced by executing this procedure should be retained as part of the package turnover dossier:

- Construction work package document (issued artifact).
- Installation and tie-in workface plan.
- Construction interface and turnover checklist (rows per interface, signed).
- Lift plan / rigging study sign-off.
- Foundation grout, level, and anchor-bolt inspection records.
- Mechanical tie-in pressure/leak test records.
- Electrical termination and verification records (575 V / 3 ph / 60 Hz).
- I&C loop check records.
- CRN/TSBC verification records.
- Vendor commissioning support report.
- Punch-list closure log and signed turnover checklist.
- Open-item register showing closure (or transfer) of TBDs from drafting time.

(Source: DELIVERABLE_REGISTER.csv anticipated artifacts for DEL-061-03; SCOPE_LEDGER.csv SOW-0151 commissioning support; PACKAGE_REGISTER.csv interface list for PKG-061.)
