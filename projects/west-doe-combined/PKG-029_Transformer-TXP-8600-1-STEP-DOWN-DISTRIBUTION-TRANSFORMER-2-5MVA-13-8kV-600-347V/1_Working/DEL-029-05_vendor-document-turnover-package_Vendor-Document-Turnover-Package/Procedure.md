# Procedure: DEL-029-05_vendor-document-turnover-package

## Purpose

Produce, control, review, and turn over the vendor document set for `PKG-029` (Transformer TXP-8600-1 - STEP DOWN DISTRIBUTION TRANSFORMER, 2.5 MVA, 13.8 kV / 600 / 347 V) so that the EPC Integrator can review for integration and accept the package at handoff.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md` present in this deliverable folder.
- Workbook Packages row 31; `PACKAGE_REGISTER.csv` row `PKG-029`; `INTERFACE_REGISTER.csv` rows for `PKG-029`; `ARTIFACT_REGISTER.csv` row `ART-91D8A203E0`.
- Accessible DBM source slices: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, mechanical packages paragraph (line 617), transformers and foundations paragraphs (lines 2745, 2949), voltage and grounding paragraphs (lines 2937, 2985, 2989, 2991).
- Upstream/Downstream dependencies: none declared during PREPARATION (`_DEPENDENCIES.md`). EPC reviewing deliverable (`DEL-029-06`) consumes turnover records.
- ASSUMPTION: a project document control procedure exists and governs submittal numbering, transmittal, review disposition, and turnover handoff; document location TBD.

## Steps

1. **Confirm identity.** Verify `PKG-029` identity (workbook row 31; WBS 01; CoA 26020-01-30-020; discipline Electrical; tagged equipment TXP-8600-1) against `PACKAGE_REGISTER.csv` and Workbook Packages row 31. Record any discrepancy as a turnover gap.
2. **Establish the vendor document register.** Open or create the vendor document register for `PKG-029`. Required columns: document number, title, revision, status, submittal date, review disposition, turnover status. ASSUMPTION: column set per project document control procedure; default minimum applies when the procedure is not yet accessible.
3. **Seed minimum document classes.** Add register rows for the minimum vendor document set: certified general arrangement; electrical schematics; foundation/anchorage drawings; nameplate data; factory acceptance test reports; O&M manuals; recommended spare parts; warranty documentation. Mark additional classes (e.g., oil sampling procedure, containment design, network/communications configuration) `TBD` pending vendor scope confirmation from `DEL-029-04`.
4. **Map interface facts.** For each `PKG-029` interface fact (Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, Structural / Foundations / Supports), confirm that at least one vendor document in the register addresses it. Where coverage is missing, record a `TBD` row with owner = Package Vendor.
5. **Apply DBM-anchored review checks.** When vendor documents are submitted, verify:
   - foundation/anchorage submittal is consistent with structural steel transformer base on precast concrete bearing foundation (DBM line 2745, 2949);
   - grounding submittal shows two-point ground-grid connection and (if a distribution transformer per CEC) a separate copper ground conductor sized per CEC (DBM lines 2989, 2991);
   - if supplied oil-filled, the submittal addresses CEC spacing and secondary containment review (DBM line 2949);
   - secondary-side grounding/configuration is stated and is consistent with the plant 600 V high-resistance-grounded system context (DBM lines 2937, 2985), or is explicitly reconciled where the package name implies a 347 V phase-to-ground tap (see Guidance Conflict Table CFT-029-05-002).
6. **EPC interface/integration review.** EPC Integrator reviews each submittal for interface/integration consistency and dispositions per project document control procedure. Record review disposition in the register.
7. **Track submittal stages.** Maintain register status as documents progress (e.g., preliminary → approval → certified-for-fabrication → certified-for-record). ASSUMPTION: stage names per project document control procedure.
8. **Collect turnover records.** At package acceptance readiness, assemble certified-for-record documents, completed FAT evidence, warranty/spares documentation, and any other turnover-required content identified by the project document control procedure or `DEL-029-06`.
9. **Hand off to EPC review and acceptance.** Provide the turnover record set to `DEL-029-06` (EPC Vendor Package Review and Acceptance). Record handoff date and turnover gap list in the register.
10. **Close out.** Update `_STATUS.md` through the safe state path as the deliverable matures. Surface unresolved `TBD` items and Guidance Conflict Table entries for human ruling.

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity verified | Field-by-field compare to workbook row 31 and Gate 7 registers. | Match. |
| Register present and structured | Inspect register for required columns and seeded rows. | All required columns; all minimum classes seeded. |
| Interface coverage | Compare register rows to `INTERFACE_REGISTER.csv` rows for `PKG-029`. | All seven interface facts addressed or marked `TBD` with owner. |
| DBM-anchored review applied | Inspect review records for foundation, grounding, and containment checks. | Each applicable DBM check recorded as PASS, FAIL, or `TBD` with action. |
| Turnover record completeness | Inspect turnover record set at handoff to `DEL-029-06`. | Set is sufficient for EPC acceptance; gaps recorded as `TBD`. |
| Cross-document consistency | Compare register entries and turnover content to Datasheet, Specification, and Guidance. | No internal inconsistency; conflicts captured in Guidance Conflict Table. |

## Records

- Vendor document register (current revision).
- Vendor document submittals (per register).
- Source vendor document table rows captured as artifacts/evidence (where available).
- EPC review dispositions per submittal.
- Turnover record set delivered to `DEL-029-06`.
- `TBD` / open-item list including the Guidance Conflict Table entries (CFT-029-05-001, CFT-029-05-002) until ruled.
- Run record at `_run_records/TASK_RUN_2026-05-24_1859.md` for this initialization.
