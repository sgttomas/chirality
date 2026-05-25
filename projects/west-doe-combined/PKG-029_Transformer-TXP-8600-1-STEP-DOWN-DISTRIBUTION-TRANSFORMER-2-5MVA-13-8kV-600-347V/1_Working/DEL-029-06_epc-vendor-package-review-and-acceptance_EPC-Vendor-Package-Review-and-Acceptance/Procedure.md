# Procedure: DEL-029-06_epc-vendor-package-review-and-acceptance

## Purpose

Operational procedure for the EPC Integrator to execute review and acceptance of the Package Vendor deliverable set for `PKG-029` (Transformer TXP-8600-1, 2.5 MVA, 13.8 kV / 600 / 347 V) and to produce the four anticipated acceptance artifacts.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- Deliverable-local truth set: `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md` (placeholder).
- Accessible source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- EPC Scope of Work for `PKG-029` (`DEL-029-01`) — required input; mark `TBD` if not yet INITIALIZED.
- Package Datasheet for `PKG-029` (`DEL-029-02` family) — required input; mark `TBD` if not yet available.
- Construction Work Package for `PKG-029` — required input; mark `TBD` if not yet available.
- Package Vendor submittal package — required input from vendor.
- Declared upstream dependencies per `_DEPENDENCIES.md` (currently: none declared).

## Steps

1. **Initiate the acceptance review.** Open the review with package identity (`PKG-029`, tag TXP-8600-1, CoA 26020-01-30-020) and tie the review record to the deliverable folder.
2. **Inventory vendor submittals.** List every vendor submittal received; assign a submittal ID; record submittal date, document type, and revision in the vendor document review log.
3. **Identity check.** Verify each vendor submittal references the correct package and equipment identity per `PACKAGE_REGISTER.csv`. Record discrepancies as findings.
4. **Interface coverage check.** For each `INTERFACE_REGISTER.csv` row attached to `PKG-029` (Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports), confirm the vendor submittal addresses the interface. Log gaps as findings.
5. **Source-fidelity check.** For acceptance assertions about voltage, grounding, transformer spacing, foundation, and standby coordination, cite the relevant DBM slice (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §Electrical Power System / §System Voltages / §Transformers / §System Grounding / §Standby Power). Mark unsupported claims `TBD`.
6. **Cross-reference EPC anchors.** Map each EPC SOW requirement and Package Datasheet line to a submittal section in the package acceptance checklist; record acceptance status (ACCEPT / ACCEPT-WITH-COMMENT / REJECT / TBD).
7. **Test and inspection evidence.** Collect vendor factory test reports (FAT) and any executed site inspection records. Map each test to the requirement(s) it discharges. Mark missing tests `TBD`.
8. **Turnover evidence assembly.** Compile records demonstrating package readiness for operations/commissioning handoff per the Construction Work Package; include outstanding-items list referencing this deliverable's `TBD` set.
9. **Findings disposition.** For every finding recorded in steps 3-8, propose disposition (e.g., accept-with-condition, vendor action, EPC action, defer to human ruling). Do not declare binding acceptance.
10. **Closeout proposal.** Assemble the four anticipated artifacts in the deliverable folder, surface remaining `TBD`/`HRR` items, and prepare the proposal for human approval (K-AUTH-1).

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity verified | Step 3 records pass | Matches `PACKAGE_REGISTER.csv` |
| Interface coverage | Step 4 matrix | All seven interface rows addressed or recorded as findings |
| Source fidelity | Step 5 citations | Each non-trivial acceptance assertion cites a source slice or is `TBD` |
| EPC anchor coverage | Step 6 checklist | All EPC SOW / Datasheet / CWP rows accounted for |
| Test evidence | Step 7 mapping | Required tests linked to requirements or marked `TBD` |
| Turnover evidence | Step 8 set | Operations-handoff readiness recorded |
| Findings disposition | Step 9 log | Each finding has proposed disposition; none silently accepted |
| Closeout authorization | Step 10 proposal | Human-authorized acceptance per K-AUTH-1 |

## Records

The deliverable folder shall, at successful closeout, contain or reference:

- Vendor document review log (per-submittal disposition).
- Package acceptance checklist (EPC SOW / Datasheet / CWP rows mapped to acceptance status).
- Test/inspection evidence set (FAT and site test records).
- Turnover evidence set (handoff readiness records).
- Findings log with proposed dispositions and outstanding `TBD`/`HRR` items.
- This `Procedure.md`, `Specification.md`, `Guidance.md`, and `Datasheet.md` (deliverable kit).
- Run record under `_run_records/`.
