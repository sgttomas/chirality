# Procedure: DEL-034-05_vendor-document-turnover-package

## Purpose

This procedure describes the steps to produce and deliver the Vendor Document Turnover Package for `PKG-034` (600V ELECTRICAL BUILDING, 820-2) to the EPC Integrator for interface/integration review and onward acceptance under `DEL-034-06_epc-vendor-package-review-and-acceptance`.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` (deliverable, package, artifact, interface, and objective registers).
- `_CONTEXT.md`, `_REFERENCES.md`, and `_DEPENDENCIES.md` for this deliverable.
- Accessible source slices:
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (mechanical-package deliverable paragraph, 600V MCC/standby power, electrical buildings sections).
  - `_Sources/26020-Packages_Interfaces_4_export.xlsx` (Packages sheet row 36).
- Vendor engineering basis from the Package Vendor (vendor design output is an input to the register; the vendor produces the documents themselves).
- No declared upstream dependencies in `_DEPENDENCIES.md`; declared dependency coordination is `DECLARED` mode.

## Steps

1. **Confirm package identity.** Verify package identity fields (`PKG-034`, workbook row 36, WBS 02, CoA 26020-02-30-025, discipline Electrical, package name "600V ELECTRICAL BUILDING (820-2)") against `PACKAGE_REGISTER.csv` and the workbook source row.
2. **Establish the register baseline.** Build the vendor document register baseline from the DBM mechanical-package deliverable paragraph (`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617), filtered to items applicable to a 600V Electrical Building package. Record non-applicable mechanical-only items explicitly.
3. **Map register entries to interface facts.** For each `PKG-034` interface fact in `INTERFACE_REGISTER.csv` (twelve facts), associate at least one register entry that will carry vendor documentation supporting that interface, or record an explicit gap. `TBD` is allowed where source-supported content is absent.
4. **Collect vendor submittals.** Receive Package Vendor submittals against the register: building and equipment datasheets, utility load summary, field tie-in lists, operating/design envelopes, sparing philosophy, shipped-loose item lists, materials/coating basis, maintenance access content, and any additional documents required by the project vendor document control specification (when accessible).
5. **Capture source vendor document rows as artifacts.** Where the source data (workbook, vendor data tables) provides vendor document rows specific to PKG-034, capture them as artifacts/evidence within this single deliverable. Do not promote individual document rows to separate deliverables.
6. **Produce turnover records.** Compile the turnover records (transmittal log, receipt records, status of each register item: submitted, accepted, deferred, gap). Format and template are `TBD` until the project vendor document control specification is accessible.
7. **EPC interface/integration review.** Submit the assembled register, submittals, and turnover records to EPC Integrator for interface/integration review. Capture review comments and dispositions.
8. **Resolve gaps and TBDs.** For each gap or `TBD`, either close it with source-supported content, record a human-ruling item (link to the Guidance Conflict Table), or escalate to `DEL-034-06` for acceptance with documented rationale.
9. **Hand off to acceptance.** Deliver the reviewed turnover package to `DEL-034-06_epc-vendor-package-review-and-acceptance`. The handoff record includes the register, submittals, source-row artifacts, turnover records, EPC review comments and dispositions, and the open `TBD`/gap list.

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity verified | Compare against `PACKAGE_REGISTER.csv` row `PKG-034` and workbook row 36. | Match. |
| Register baseline source-grounded | Confirm each register entry traces to the DBM mechanical-package deliverable paragraph or to a recorded gap. | Trace present for every entry. |
| Interface coverage | Confirm each of the twelve PKG-034 interface facts has at least one register entry or explicit gap. | Coverage matrix complete. |
| Submittal completeness | Confirm Package Vendor submittals match the register and are received against the turnover log. | Status recorded per item. |
| Source vendor rows captured | Confirm artifacts include source vendor document rows where the source data supplies them. | Artifacts present or absence justified. |
| Turnover records produced | Confirm transmittal log, receipt records, and per-item status are present. | Records present, even if format is `TBD`. |
| EPC review performed | Confirm EPC review comments and dispositions are recorded. | Review evidence present. |
| Handoff to `DEL-034-06` | Confirm the assembled package is delivered with the open `TBD`/gap list. | Handoff record present. |

## Records

The procedure shall produce or preserve:

- Vendor document register (with source trace per entry).
- Vendor document submittals (per item, with status).
- Source vendor document table rows captured as artifacts (where available).
- Turnover records (transmittal log, receipts, per-item status, gap/`TBD` list).
- EPC interface/integration review comments and dispositions.
- Handoff record to `DEL-034-06_epc-vendor-package-review-and-acceptance`.
- Open `TBD` and human-ruling items linked to the Guidance Conflict Table.
