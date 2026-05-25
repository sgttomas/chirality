# Procedure: DEL-027-05_vendor-document-turnover-package

## Purpose

This procedure describes how to produce, review, and close out the Vendor Document Turnover Package for `PKG-027` — Transformer TXP-8301-1 (20/26 MVA, 13.8 kV / 6.9 kV / 0.4 kV). It covers vendor authorship of the documentation set and EPC interface/integration review through turnover.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- Workbook Packages row 29 (source for package identity, discipline, and interface fact set).
- `PACKAGE_REGISTER.csv` row `PKG-027`, `DELIVERABLE_REGISTER.csv` row `DEL-027-05_vendor-document-turnover-package`, `ARTIFACT_REGISTER.csv` rows for the deliverable (including `ART-AACDC8D0FF`), `INTERFACE_REGISTER.csv` rows for `PKG-027`, and `OBJECTIVE_DELIVERABLE_MAP.csv` rows for the deliverable.
- DBM electrical source slices at `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` for transformer, grounding, neutral grounding, and foundation basis.
- Declared upstream/downstream dependencies (currently none declared in `_DEPENDENCIES.md`).
- Resolved (or explicitly deferred) rulings for HRR-027-05-001, HRR-027-05-002, and HRR-027-05-003 in `Guidance.md`.
- Selected Package Vendor scope and EPC document-control standard (both TBD in current source set).

## Steps

1. **Confirm identity and scope.** Verify package identity (`PKG-027`, Workbook Packages row 29, WBS 01, CoA 26020-01-30-018, discipline Electrical, package name as published) against Gate 7 registers. Record any mismatch as a conflict; do not silently normalize.
2. **Establish vendor document register skeleton.** Create the register with one row per anticipated vendor document, anchored on (a) the seven `PKG-027` interface facts and (b) the DBM-anchored topics (grounding/bonding, neutral grounding, foundations/installation). Mark register schema and numbering as `TBD` until the EPC document-control standard is provided.
3. **Populate source-grounded entries first.** Add vendor-document entries for:
   - grounding/bonding documentation consistent with DBM two-point ground-grid connection and ground-well-at-power-transformer requirements;
   - neutral grounding configuration documentation for the 6.9 kV winding consistent with the 100 A, 10 s tripping resistor basis (mark ASSUMPTION pending confirmation);
   - foundation/installation documentation consistent with precast concrete bearing foundation and structural steel base.
   Cite the source slice for each entry.
4. **Mark source gaps as `TBD`.** For items where the source set is silent (e.g., factory test list, oil quality acceptance, vendor document numbering, submittal/return-code workflow, spare parts list, warranty), record the entry with status `TBD` and a reference to `ART-AACDC8D0FF`. Do not invent content.
5. **Issue submittals against the register.** As vendor data becomes available, submit per entry and track revisions and return codes per the EPC document-control standard (when provided). Maintain traceability from submittal to register row.
6. **EPC interface/integration review.** EPC Integrator reviews each submittal against the applicable `PKG-027` interface facts and the DBM electrical basis. Disposition each submittal (e.g., accepted, accepted-with-comments, rejected). Record disposition in the register.
7. **Compile turnover records.** Assemble the turnover set (factory test reports, oil reports, nameplate records, as-built drawings, O&M manuals, spare parts list, warranty documents — exact list `TBD`). Confirm each is traceable to a register entry and to a `PKG-027` interface fact or DBM-anchored topic.
8. **Verify and close out.** Run the verification table in `Specification.md`. Resolve outstanding `TBD`s by either (a) accepted source-grounded values, (b) accepted vendor-provided values with vendor citation, or (c) explicit deferral. Mark deliverable for handoff to `DEL-027-06_epc-vendor-package-review-and-acceptance`.

## Verification

| Verification | How performed | Acceptance |
|---|---|---|
| Identity check | Compare register identity fields to Gate 7 registers and Workbook Packages row 29. | All identity fields match accepted source. |
| Interface coverage | Compare register entries to `INTERFACE_REGISTER.csv` rows for `PKG-027`. | Each of the seven interface facts is evidenced by at least one register entry. |
| Source grounding | Spot-check non-trivial entries against cited source slices (DBM electrical sections, Gate 7 registers). | Each non-trivial entry has a source citation or is marked `TBD`/`ASSUMPTION`. |
| Submittal disposition completeness | Check that every issued submittal has a recorded EPC disposition. | No undispositioned submittals at turnover. |
| Turnover completeness | Compare turnover records to the agreed turnover-records list. | All agreed turnover items present and traceable. |
| Cross-document consistency | Compare Datasheet, Specification, Guidance, Procedure terminology, IDs, interfaces, and TBDs. | No internal inconsistency. |

## Records

The deliverable shall retain:

- The vendor document register (final revision) and revision history.
- All vendor document submittals with EPC dispositions.
- Source-required vendor documentation (e.g., grounding evidence, neutral-grounding configuration, foundation/installation evidence).
- Turnover records (factory test reports, oil reports, nameplate records, as-built drawings, O&M manuals, spare parts list, warranty documents — exact list `TBD`).
- The source-gap / `TBD` log (anchored on `ART-AACDC8D0FF`) and the resolution status of each item.
- Citations to the Gate 7 snapshot, Workbook Packages row 29, applicable Gate 7 registers, and the DBM electrical source slices.
