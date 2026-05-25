# Procedure: DEL-026-06_epc-vendor-package-review-and-acceptance

## Purpose

Produce the EPC Integrator's review and acceptance evidence for `PKG-026` (Transformer TXP-8300-2, 20/26 MVA, 13.8 kV / 6.9 kV / 0.4 kV) by reviewing vendor submittals, validating conformance to the EPC anchor deliverables, witnessing/accepting test and inspection evidence, and producing the turnover checklist.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot (`GATE-07_Final_Published_2026-05-24`).
- Accepted EPC anchor deliverables for `PKG-026`:
  - `DEL-026-01` Scope of Work
  - `DEL-026-02` Package Datasheet
  - `DEL-026-03` Construction Work Package
- Vendor production deliverables available for review:
  - `DEL-026-04` Vendor Engineered Equipment Package
  - `DEL-026-05` Vendor Document Turnover Package
- `_REFERENCES.md` for this deliverable identifies the accepted source set.
- HRR / Conflict items in `Guidance.md` are open and visible to reviewers.

Declared upstream dependencies in `_DEPENDENCIES.md`: none.

## Steps

1. **Initialize acceptance scope.** Confirm identity (`PKG-026`, workbook row 28, WBS 02, CoA 26020-02-30-017) and responsibility split against `PACKAGE_REGISTER.csv` and `DELIVERABLE_REGISTER.csv`. Confirm the seven applicable interface types from `INTERFACE_REGISTER.csv`.
2. **Compile vendor document review log.** For every entry in the `DEL-026-05` vendor document register, record received-date, reviewer, comments, vendor disposition, and final acceptance status. Record gaps as open log rows with status "TBD — register entry missing or not received."
3. **Map acceptance criteria to EPC anchors.** For every applicable requirement in `DEL-026-02` and every construction acceptance item in `DEL-026-03`, record a checklist row keyed to acceptance evidence. Where a `DEL-026-02` requirement is `TBD` (e.g., transformer rating allocation, impedance, vector group, BIL, grounding scheme), record the acceptance row as "Conditional — basis TBD" and open an HRR.
4. **Review vendor design submittals.** Verify that `DEL-026-04` design content satisfies each non-TBD `DEL-026-02` requirement. Record comment disposition and re-submittal status in the review log.
5. **Witness / accept factory and shop tests.** Cross-check test results against the test list derived from `DEL-026-02` and the vendor design basis. Record method, witness (EPC / vendor / third party), result, and acceptance disposition. Where the test list itself is `TBD`, defer and open an HRR.
6. **Verify interface coverage.** For each `PKG-026` interface type (Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports), confirm vendor submittals and EPC integration documents address it. Record any uncovered interface as a turnover open item.
7. **Compile turnover checklist.** Aggregate review log status, acceptance checklist rows, test/inspection evidence, and interface coverage into a turnover packet. Mark each item Accepted / Accepted-with-comment / Conditional / Open-Item.
8. **Resolve or escalate open items.** For every Conditional or Open-Item entry, record either (a) human ruling resolution, (b) carryover to operations with explicit risk acceptance, or (c) re-submittal request to the Package Vendor.
9. **Issue acceptance disposition.** EPC Integrator (human authority — agents do not certify) records the final acceptance disposition for the vendor package against `PKG-026`. Acceptance is binding only when authored by a human per K-AUTH-1.
10. **Archive evidence.** Place the review log, acceptance/turnover checklist, test/inspection evidence, and HRR resolutions in the deliverable folder. Update `_STATUS.md` per the lifecycle rules (human-authored state changes only after acceptance).

## Verification

| Verification check | Method | Acceptance basis |
|---|---|---|
| Every `DEL-026-05` register entry is dispositioned in the review log | Cross-check register vs. log | 100% coverage; gaps recorded as TBD with cause |
| Every applicable `DEL-026-02` requirement maps to an acceptance row | Cross-check requirements vs. checklist | 100% coverage; conditional rows reference open HRRs |
| Every `PKG-026` interface in `INTERFACE_REGISTER.csv` is addressed | Cross-check interface list vs. acceptance evidence | Each of seven interfaces is Accepted, Conditional, or Open-Item |
| No invented technical values | Source-fidelity review | Package-specific transformer values without source remain `TBD` |
| No silent reconciliation of conflicts | HRR review | All conflicts present in `Guidance.md` Conflict Table |
| Human-authored acceptance | Authority check | Final acceptance disposition is human-authored (K-AUTH-1) |

## Records

- Vendor document review and comment log (`ART-AF00FF6B63`).
- Vendor package acceptance and turnover checklist (`ART-28805E8681`).
- Factory/shop test and inspection evidence (`ART-063BACA4E7`).
- HRR / Conflict resolution log (cross-referenced to `Guidance.md`).
- Final acceptance disposition record (human-authored).
- `_STATUS.md` lifecycle history.
