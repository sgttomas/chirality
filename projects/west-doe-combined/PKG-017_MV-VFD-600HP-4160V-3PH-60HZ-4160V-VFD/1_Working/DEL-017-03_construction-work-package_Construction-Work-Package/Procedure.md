# Procedure: DEL-017-03_construction-work-package

## Purpose

Produce, verify, and turn over the Construction Work Package (CWP) for `PKG-017`, the "MV VFD - 600HP, 4160V, 3PH, 60HZ - 4160V VFD" package, such that field execution of installation, tie-ins, inspection, and handover is authorized against source-grounded requirements and Gate 7 register facts.

This procedure covers both (a) the steps to **produce** the CWP artifact set and (b) the field steps the CWP itself shall require for **installation and turnover**.

## Prerequisites

- Accepted Gate 7 snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- Workbook Packages row 19 and `PACKAGE_REGISTER.csv` row `PKG-017`.
- `INTERFACE_REGISTER.csv` rows `IFC-5E50E5F700`, `IFC-1340C6D795`, `IFC-6ECD9C92A1`, `IFC-FB4034716A`, `IFC-A807F5E0B3`, `IFC-34EB597147` for PKG-017.
- `ARTIFACT_REGISTER.csv` rows `ART-1C1724D3C4`, `ART-65539C633A`, `ART-3A7676CD16` for DEL-017-03.
- DBM source slice: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — Construction Scope Summary, electrical supply table, 4160V MCC, Electrical Buildings/Raceways, foundations, and roads/access paragraphs.
- Logical upstream (not yet declared in `_DEPENDENCIES.md`): DEL-017-01 Scope of Work and DEL-017-02 Package Datasheet for PKG-017 — see HRR-017-03-003.
- Accepted detailed-design issuances (electrical, civil/structural, controls) for PKG-017 prior to issue-for-construction. Status: TBD pending project schedule.

## Steps

### A. Produce the CWP artifact set

1. Confirm package identity, responsibility split, interfaces, and artifacts against Gate 7 registers; record source pointers.
2. Read DBM source slices listed in `_REFERENCES.md` and the accessible electrical/construction paragraphs; record per-claim source citations.
3. Draft the construction work package (ART-1C1724D3C4) describing the installation, tie-in, inspection, and turnover scope at workface level, grouped by interface fact.
4. Draft the installation and tie-in workface plan (ART-65539C633A) sequencing module receipt, foundation/anchor verification, equipment setting, electrical/control tie-ins, and pre-energization tests.
5. Draft the construction interface and turnover checklist (ART-3A7676CD16) listing hold points, sign-off authorities, and turnover records to commissioning.
6. Mark unsupported values `TBD` (driven-machine identity, exact location, foundation drawings, cooling provisions, lift weights, cable schedules) rather than inventing them.
7. Cross-check Datasheet, Specification, Guidance, and Procedure for consistent identity, interfaces, and TBDs.
8. Submit to EPC Integrator review; resolve open items or surface them as Human-Ruling items in Guidance Conflict Table.

### B. Field installation and turnover (steps the CWP shall require)

9. Verify foundation pour, cure, anchor location, and elevation per accepted civil/structural drawings; record inspection.
10. Receive and inspect the vendor MV VFD package (rigging plan, lift weights, no-shock indicators); record receipt inspection.
11. Set the package on its foundation; level, grout, and torque anchors per accepted procedures; record anchor-torque sheet.
12. Install MV power cabling from the designated feeder (4160V MCC or detailed-design-identified source) to the VFD enclosure with project-specified segregation from control/instrument circuits.
13. Install grounding/bonding from the VFD enclosure to the facility ground grid per CEC and project electrical specifications; record continuity test.
14. Install I&C / control cabling and terminations; record loop checks.
15. Install communications / network cabling from the VFD to the plant PLC central control panel via the 4160V MCC EtherNet path unless detailed design specifies otherwise; record communication test.
16. Verify maintenance-access clearances and cable tray/conduit routing against the layout; record walkdown.
17. Perform pre-energization tests: insulation, hi-pot (if required by detailed design), phase rotation, protective-relay setting verification; record test sheets and hold-point sign-offs.
18. Complete the construction interface and turnover checklist (ART-3A7676CD16); transfer custody to commissioning.

## Verification

- Identity, responsibility, interface, and artifact completeness checks per Specification Verification table.
- Each non-trivial CWP value carries a cited source slice or is marked `TBD`/`ASSUMPTION`.
- Pre-energization hold points completed and signed off prior to first energization.
- Turnover checklist closed with no open construction items at handover, or open items explicitly carried forward with owner and date.

## Records

- The three required artifacts: ART-1C1724D3C4 (CWP), ART-65539C633A (workface plan), ART-3A7676CD16 (interface and turnover checklist).
- Foundation inspection record; anchor-torque sheet.
- Grounding continuity test record; MV insulation/hi-pot test records; phase-rotation record; relay-setting verification record.
- I&C loop-check and communication-loop test records.
- Construction interface walkdown record.
- Source-gap / `TBD` list and Human-Ruling Conflict Table closures.
- TASK run record at `_run_records/`.
