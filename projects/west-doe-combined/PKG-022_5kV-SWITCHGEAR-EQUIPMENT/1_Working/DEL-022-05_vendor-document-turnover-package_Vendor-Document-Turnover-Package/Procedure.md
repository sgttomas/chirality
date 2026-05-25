# Procedure: DEL-022-05_vendor-document-turnover-package

## Purpose

Operational procedure for producing and turning over the PKG-022 Vendor Document Turnover Package: assembling the vendor document register, submittals, source-required documentation captures, and turnover records, with EPC Integrator interface/integration review.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`.
- `DELIVERABLE_REGISTER.csv` row `DEL-022-05_vendor-document-turnover-package` (authoritative identity).
- `PACKAGE_REGISTER.csv` row `PKG-022` (responsibility model).
- `INTERFACE_REGISTER.csv` rows for `PKG-022` (six declared interfaces).
- `ARTIFACT_REGISTER.csv` row `ART-E34A2C824B` (current vendor-document gap state).
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (deliverable-local truth).
- Declared upstream/downstream dependencies: none (per `_DEPENDENCIES.md`).
- Anticipated upstream coordination (not declared, advisory): `DEL-022-04` (Vendor Engineered Equipment Package) — vendor identity and equipment basis.
- Source vendor-document basis for PKG-022 — TBD; not present in `_Sources/26020-Package_Requirements.docx`.

## Steps

1. **Confirm package identity and interfaces.** Reconfirm `PACKAGE_REGISTER.csv` row `PKG-022` and the six `INTERFACE_REGISTER.csv` rows. Record any change.
2. **Identify source-required vendor document rows.** Search `_Sources/26020-Package_Requirements.docx` and any human-supplied project vendor-data requirements document for PKG-022 / 5kV switchgear entries. If none are present, record TBD per Guidance HRR-022-05-002 rather than substituting a generic list.
3. **Initialize the vendor document register.** Replace the current `ART-E34A2C824B` placeholder with a structured register that contains, at minimum: document number, title, revision, status, transmittal reference, review state, source-required-row link (or "none"), and supported interface type(s).
4. **Collect vendor document submittals.** For each register row, obtain the controlled submittal (file or controlled external pointer) from the Package Vendor. Reject rows that lack a controlled source.
5. **Map submittals to interface types.** For each submittal, record which of the six declared interface types it supports. Submittals that do not map to any declared interface are recorded with a human-ruling flag, not silently included.
6. **Capture source-required artifacts.** Where a source-required row exists for the package, capture the corresponding vendor artifact and link it to the row. Where no source-required row exists, leave the source-required link as "none" and do not invent one.
7. **Assemble turnover records.** For every register entry destined for turnover, record the transmittal identifier, transmittal date, acceptance status, and final handoff evidence.
8. **Run EPC Integrator interface and integration review.** EPC Integrator confirms register completeness against the project's vendor-data requirements (when available), traceability to interfaces, and turnover record completeness. Comments are returned to the Package Vendor; the cycle repeats until the register reaches a reviewed state.
9. **Finalize the turnover set.** Lock the vendor document register, archive submittals and turnover records together, and produce the final transmittal package to the EPC Integrator.
10. **Do not perform acceptance.** Acceptance is the responsibility of `DEL-022-06_epc-vendor-package-review-and-acceptance`. This procedure ends at "turnover set delivered for acceptance."

## Verification

- Vendor document register exists, has the field set required by R-1, and supersedes the `ART-E34A2C824B` placeholder.
- Every register row has a controlled submittal (or pointer) per R-2.
- Source-required rows captured per R-3 where present; otherwise marked TBD with a recorded reason.
- Turnover records cover every register entry intended for turnover per R-4.
- Interface coverage trace exists for all six declared interfaces per R-5.
- Responsibility split (Vendor produces; EPC reviews) honored per R-6.
- Traceability map exists per R-7.
- TBD entries match items lacking source backing per R-8.

## Records

- Final vendor document register.
- Controlled set of vendor document submittals (or pointers).
- Source-required vendor-document captures (where applicable).
- Transmittals and acceptance-status log entries.
- Turnover handoff evidence.
- EPC Integrator review comments and disposition log.
- Run record(s) in `_run_records/`.
