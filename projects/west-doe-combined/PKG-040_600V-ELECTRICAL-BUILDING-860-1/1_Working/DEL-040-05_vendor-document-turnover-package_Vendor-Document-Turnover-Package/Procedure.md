# Procedure: DEL-040-05_vendor-document-turnover-package

## Purpose

This procedure describes the steps to produce and deliver the Vendor Document Turnover Package for `PKG-040` (600V ELECTRICAL BUILDING, 860-1 — "600V General Area / Tank Farm Electrical Building" per DBM-Deepcut) to the EPC Integrator for interface/integration review and onward acceptance under `DEL-040-06_epc-vendor-package-review-and-acceptance`.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` (deliverable, package, artifact, interface, and objective registers).
- `_CONTEXT.md`, `_REFERENCES.md`, and `_DEPENDENCIES.md` for this deliverable.
- Accessible source slices:
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (SEC-12 Electrical Basis: Discipline Scope, Governing Codes / Table 12-1 / studies, Area Classification, Power System, Standby Power; building list line 2816).
  - `_Sources/26020-Packages_Interfaces_4_export.xlsx` (Packages sheet row 42).
- Vendor engineering basis from the Package Vendor (vendor design output is an input to the register; the vendor produces the documents themselves).
- No declared upstream dependencies in `_DEPENDENCIES.md`; declared dependency coordination is `DECLARED` mode.

## Steps

1. **Confirm package identity.** Verify package identity fields (`PKG-040`, workbook row 42, WBS 01, CoA 26020-01-30-031, discipline Electrical, package name "600V ELECTRICAL BUILDING (860-1)") against `PACKAGE_REGISTER.csv` and the workbook source row.
2. **Establish the register baseline.** Build the vendor document register baseline from SEC-12 Electrical Basis (Discipline Scope, Table 12-1 electrical specifications, and the electrical studies table), filtered to items applicable to a 600V General Area / Tank Farm Electrical Building. Apply ELC-QAS-000003-001 ("Electrical Requirements for Packaged Equipment") as the specific governing electrical specification for packaged-equipment vendor scope. Record items deferred to electrical studies (standby generator sizing, transfer switches, protection coordination split) as `TBD` linked to the relevant DBM clause.
3. **Map register entries to interface facts.** For each `PKG-040` interface fact in `INTERFACE_REGISTER.csv` (twelve facts), associate at least one register entry that will carry vendor documentation supporting that interface, or record an explicit gap. `TBD` is allowed where source-supported content is absent.
4. **Collect vendor submittals.** Receive Package Vendor submittals against the register: building and electrical equipment datasheets (transformers, 600V MCC, distribution, UPS where installed), area-classification basis, load/short-circuit/coordination/arc-flash/load-flow study inputs, grounding/bonding details, cable and raceway schedules, lighting/receptacle and electric heat-tracing details, electric building heater and HVAC coordination data, maintenance access content, shipped-loose item lists, materials/coating basis, and any additional documents required by the project vendor document control specification (when accessible).
5. **Capture source vendor document rows as artifacts.** Where the source data (workbook, vendor data tables) provides vendor document rows specific to PKG-040, capture them as artifacts/evidence within this single deliverable. Do not promote individual document rows to separate deliverables.
6. **Evidence code and specification compliance.** Confirm vendor documents demonstrate compliance with CSA C22.1-21 (Canadian Electrical Code), applicable BC provincial/local electrical codes, and the relevant Table 12-1 ELC-QAS specifications (in particular ELC-QAS-000003-001 for packaged equipment).
7. **Produce turnover records.** Compile the turnover records (transmittal log, receipt records, status of each register item: submitted, accepted, deferred, gap). Format and template are `TBD` until the project vendor document control specification is accessible.
8. **EPC interface/integration review.** Submit the assembled register, submittals, and turnover records to EPC Integrator for interface/integration review. Capture review comments and dispositions.
9. **Resolve gaps and TBDs.** For each gap or `TBD`, either close it with source-supported content, record a human-ruling item (link to the Guidance Conflict Table), or escalate to `DEL-040-06` for acceptance with documented rationale. Study-dependent items released through change control once the relevant electrical study or TOU standard is accepted.
10. **Hand off to acceptance.** Deliver the reviewed turnover package to `DEL-040-06_epc-vendor-package-review-and-acceptance`. The handoff record includes the register, submittals, source-row artifacts, turnover records, EPC review comments and dispositions, and the open `TBD`/gap list.

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity verified | Compare against `PACKAGE_REGISTER.csv` row `PKG-040` and workbook row 42. | Match. |
| Register baseline source-grounded | Confirm each register entry traces to SEC-12 Discipline Scope, Table 12-1, the electrical studies table, or to a recorded gap. | Trace present for every entry. |
| Interface coverage | Confirm each of the twelve PKG-040 interface facts has at least one register entry or explicit gap. | Coverage matrix complete. |
| Submittal completeness | Confirm Package Vendor submittals match the register and are received against the turnover log. | Status recorded per item. |
| Code/spec compliance evidence | Confirm vendor documents cite CSA C22.1-21 and the applicable ELC-QAS specifications (including ELC-QAS-000003-001). | Compliance statements or test/inspection records present. |
| Source vendor rows captured | Confirm artifacts include source vendor document rows where the source data supplies them. | Artifacts present or absence justified. |
| Turnover records produced | Confirm transmittal log, receipt records, and per-item status are present. | Records present, even if format is `TBD`. |
| EPC review performed | Confirm EPC review comments and dispositions are recorded. | Review evidence present. |
| Handoff to `DEL-040-06` | Confirm the assembled package is delivered with the open `TBD`/gap list. | Handoff record present. |

## Records

The procedure shall produce or preserve:

- Vendor document register (with source trace per entry).
- Vendor document submittals (per item, with status).
- Source vendor document table rows captured as artifacts (where available).
- Turnover records (transmittal log, receipts, per-item status, gap/`TBD` list).
- Code and specification compliance evidence (CSA C22.1-21; Table 12-1 ELC-QAS specifications, including ELC-QAS-000003-001).
- EPC interface/integration review comments and dispositions.
- Handoff record to `DEL-040-06_epc-vendor-package-review-and-acceptance`.
- Open `TBD` and human-ruling items linked to the Guidance Conflict Table.
