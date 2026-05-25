# Procedure: DEL-030-06_epc-vendor-package-review-and-acceptance

## Purpose

Produce the EPC Integrator review and acceptance evidence set for `PKG-030` (Transformer TXP-8200-1, 2.5 MVA, 13.8 kV / 600/347 V step-down distribution transformer) covering vendor document review, integration acceptance, and turnover readiness against the EPC SoW (DEL-030-01), Package Datasheet (DEL-030-02), and Construction Work Package (DEL-030-03).

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot is available and unchanged for this run.
- `_CONTEXT.md`, `_REFERENCES.md`, and `_DEPENDENCIES.md` for this deliverable are present and have been read.
- Acceptance basis deliverables exist or are explicitly noted as TBD where missing:
  - DEL-030-01 EPC Scope of Work
  - DEL-030-02 Package Datasheet
  - DEL-030-03 Construction Work Package
- Subject vendor deliverables are submitted or scheduled:
  - DEL-030-04 Vendor Engineered Equipment Package
  - DEL-030-05 Vendor Document Turnover Package
- Applicable Gate 7 registers are accessible: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM source slices for distribution, transformers, foundations, grounding, cable tray, and conduit are accessible (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`).
- A designated human EPC Integrator approver is identified for the acceptance signature.

## Steps

1. **Establish review baseline.** Record the acceptance basis: cite the exact rev of DEL-030-01, DEL-030-02, DEL-030-03 used as the baseline. Lock the seven PKG-030 interface facts from `INTERFACE_REGISTER.csv` as the interface checklist scaffold.
2. **Build vendor document review log (ART-0FE3BFB82C).** For each submittal in DEL-030-05's vendor document register, create an entry: submittal ID, title, revision, date received, EPC reviewer, disposition (Accepted / Accepted with Comments / Rejected / Resubmit), comment list, and comment-closure trace.
3. **Build package acceptance and turnover checklist (ART-6934DD5E20).** Sections:
   - Identity verification against `PACKAGE_REGISTER.csv` row `PKG-030` and workbook row 32.
   - Interface verification, one row per PKG-030 interface fact (Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, Structural / Foundations / Supports).
   - Acceptance basis verification: each SoW (DEL-030-01) requirement that bears on PKG-030 has a checklist entry; each Package Datasheet (DEL-030-02) data point has a vendor-evidence reference; each Construction Work Package (DEL-030-03) tie-in step has a field-evidence reference.
   - Grounding/foundation verification against the DBM (two-point ground-grid connection; 600 V HRG resistor; separate copper distribution-transformer ground conductor per CEC; mounting basis).
   - Maintenance access verification (cable tray/conduit do not interfere with maintenance access).
4. **Collect factory/shop test and inspection evidence (ART-F13347A23A).** Reference the vendor-declared test standard family (TBD until confirmed; carry HRR-030-06-001). Attach routine/type/special test reports as provided; mark missing classes as `TBD` open items with owner.
5. **Disposition open items.** Convert every unresolved comment, RFI, or non-conformance into either a closed entry (with closure evidence), an accepted-with-deviation entry (with reference), or an open punch item with owner and due date.
6. **Cross-check.** Verify that Datasheet, Specification, Guidance, and Procedure for this deliverable use the same package name, IDs, interfaces, and TBDs; reconcile inconsistencies inside this deliverable folder only.
7. **Compile turnover record.** Bundle the signed acceptance checklist, closed comment log, accepted test/inspection evidence, open-item register, and citation list (Gate 7 snapshot, workbook row 32, registers, DBM source slices).
8. **Submit for human approval.** Present the turnover record to the designated human EPC Integrator approver for signature. Agent and skill do not sign acceptance (K-AUTH-1).

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare checklist identity fields to workbook row 32 and `PACKAGE_REGISTER.csv` row `PKG-030`. | All fields match accepted source. |
| Interface coverage | Confirm each of the seven PKG-030 interface facts has a checklist entry. | `INTERFACE_REGISTER.csv` rows for `PKG-030` fully represented. |
| Vendor document coverage | Confirm every submittal in DEL-030-05's register has a review-log entry with disposition and closure trace. | No untracked submittals. |
| Grounding/foundation verification | Field evidence vs. DBM basis. | Two-point ground-grid connection, HRG resistor, separate copper ground conductor, and mounting basis recorded as accepted or carried open. |
| Test/inspection completeness | Compare collected evidence to declared test standard family and accepted SoW/datasheet requirements. | Gaps carried as `TBD` or open punch items with owner. |
| Open-item discipline | Inspect open-item register. | Each open item has owner, due date, and disposition path. |
| Authority | Confirm checklist is signed by a human EPC Integrator approver. | K-AUTH-1 satisfied. |
| Source fidelity | Check every non-trivial requirement against cited source slice. | Unsupported claims marked `TBD` or `ASSUMPTION`, not asserted as accepted requirements. |

## Records

- Vendor document review and comment log (ART-0FE3BFB82C).
- Vendor package acceptance and turnover checklist (ART-6934DD5E20), signed by the human EPC Integrator approver.
- Factory/shop test and inspection evidence package (ART-F13347A23A).
- Open-item / punch-list register with owners and due dates.
- Turnover bundle index listing all of the above plus citations to the Gate 7 snapshot, workbook row 32, applicable registers, and DBM source slices.
- Run record at `_run_records/TASK_RUN_<date>_<HHmm>.md`.
