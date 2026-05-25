# Procedure — DEL-017-06 EPC Vendor Package Review and Acceptance

## Purpose

Operational steps to produce the EPC Vendor Package Review and Acceptance record for `PKG-017` (MV VFD - 600HP, 4160V, 3PH, 60HZ - 4160V VFD). This procedure produces the four artifacts in `_CONTEXT.md` Anticipated Artifacts: vendor document review log, package acceptance checklist, test/inspection evidence, turnover evidence.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot (`_REFERENCES.md`).
- Accepted snapshots of:
  - `DEL-017-01_scope-of-work` (EPC Scope of Work)
  - `DEL-017-02_package-datasheet` (EPC Package Datasheet)
  - `DEL-017-03_construction-work-package` (EPC Construction Work Package)
  - `DEL-017-04_vendor-engineered-equipment-package` (Vendor Package Production Unit)
  - `DEL-017-05_vendor-document-turnover-package` (Vendor Document Turnover Package)
  - Status: each at or beyond the `INITIALIZED` maturity threshold per `_DEPENDENCIES.md`; ideally at an accepted/published snapshot before acceptance is finalized.
- EPC Integrator reviewer assignments and Package Vendor counterparts identified.
- Access to vendor submittals listed in DEL-017-05 vendor document register.
- Conflict Table items in `Guidance.md` either resolved by human ruling or carried as explicit holds.

## Steps

1. **Confirm acceptance basis** — record the accepted revision identifiers (snapshot IDs) of DEL-017-01, DEL-017-02, DEL-017-03, DEL-017-04, DEL-017-05, and the Gate 7 decomposition snapshot. Record any that are not yet at an acceptable maturity threshold as explicit prerequisites/holds.
2. **Initialize the vendor document review log** — populate from the DEL-017-05 vendor document register (vendor doc ID, revision, title, EPC reviewer assignment). If the register is not yet available, list the expected document classes and mark each row `TBD`.
3. **Execute document-level review** — for each vendor document, the assigned EPC reviewer records review code, comments, and disposition. Maintain back-references to specific SOW/Datasheet/CWP clauses where applicable.
4. **Build the package acceptance checklist** — instantiate one row per accepted SOW clause, Datasheet requirement, and CWP requirement; link each to the vendor evidence (vendor doc ID + section). For Datasheet rows whose values are `TBD` in DEL-017-02, mark the checklist row `HOLD` and capture rationale.
5. **Cover each interface** — work through every interface listed for PKG-017 (Electrical Power; Grounding/Bonding; I&C/Control Cabling; Communications/Network; Maintenance Access; Structural/Foundations/Supports). For each interface, capture the vendor evidence and any EPC integration commitments. (Source: Gate 7 `PACKAGE_REGISTER.csv` row PKG-017.)
6. **Assemble test/inspection evidence** — gather FAT reports, any site test reports, and hold-point inspection records called out by DEL-017-02 Verification section. Record witnessing arrangement (vendor-led with EPC sampling vs. EPC-led witnessing).
7. **Assemble turnover evidence** — gather mechanical-completion records, energization-readiness records, and care-custody-control transfer records per the DEL-017-03 turnover checklist. Cross-link to any open commissioning items.
8. **Reconcile open items and NCRs** — list every open item or NCR from steps 3–7. For each, record planned closure or explicit acceptance-with-hold (with target closure date and owner).
9. **Resolve or carry Conflict Table items** — for every row in `Guidance.md` Conflict Table, record either the human ruling or that the conflict is being carried as an explicit hold. Update the acceptance record header accordingly.
10. **Compile the acceptance record** — bind the review log, checklist, test/inspection evidence pack, turnover evidence pack, open-item list, and conflict-resolution log into one deliverable record with header citing the accepted snapshots and the Gate 7 decomposition snapshot.
11. **Route for human approval** — submit the assembled acceptance record to the EPC Integrator human approver. (Per K-AUTH-1, only humans author binding approval records; the agent-assembled record is the evidence package.)

## Verification

- Each Specification requirement (R-017-06-01 … R-017-06-10) is satisfied by a numbered step above and produces a citable evidence artifact.
- The acceptance record header cites Gate 7 (Final Published 2026-05-24) and the accepted revisions of DEL-017-01..05.
- The acceptance checklist includes one row per accepted SOW/Datasheet/CWP clause, with vendor-evidence links.
- Each of the six PKG-017 interfaces appears in the checklist with vendor evidence and EPC integration commitments.
- Open items and Conflict Table items are either closed or carried as explicit holds with owners and target closures.
- Test/inspection and turnover packs are complete or have explicit holds matching DEL-017-02 Verification and DEL-017-03 turnover checklist.

## Records

- `Vendor_Document_Review_Log.{csv|md}` (TBD format)
- `Package_Acceptance_Checklist.{csv|md}` (TBD format)
- `Test_Inspection_Evidence/` (pack)
- `Turnover_Evidence/` (pack)
- `Open_Items_and_Holds.{csv|md}` (TBD format)
- `Acceptance_Record.md` — top-level binder citing all of the above and the accepted upstream snapshots

All records are retained in the deliverable folder under EPC Integrator custody and are referenced from any subsequent commissioning or operations turnover packages.
