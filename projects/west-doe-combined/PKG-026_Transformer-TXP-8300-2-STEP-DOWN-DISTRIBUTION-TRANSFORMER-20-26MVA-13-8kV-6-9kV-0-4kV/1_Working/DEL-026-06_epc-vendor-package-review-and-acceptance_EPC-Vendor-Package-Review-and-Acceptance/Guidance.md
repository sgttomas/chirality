# Guidance: DEL-026-06_epc-vendor-package-review-and-acceptance

## Purpose

`DEL-026-06` exists as the EPC Integrator's evidence that the vendor-engineered transformer package for `PKG-026` (TXP-8300-2, 20/26 MVA, 13.8 kV / 6.9 kV / 0.4 kV) has been reviewed, accepted, and integration-ready. It closes the loop between the EPC anchor deliverables (`DEL-026-01` Scope of Work, `DEL-026-02` Package Datasheet, `DEL-026-03` Construction Work Package) and the vendor production units (`DEL-026-04` Vendor Engineered Equipment Package, `DEL-026-05` Vendor Document Turnover Package).

This deliverable is review-and-acceptance evidence — not new design and not construction execution. It exists to record that the vendor package conforms to the EPC basis, that vendor documentation is complete and dispositioned, that test/inspection results are accepted, and that the package is ready for facility turnover.

## Principles

- **Review, do not re-author.** The acceptance deliverable carries review and acceptance evidence; technical content remains in `DEL-026-02` and `DEL-026-04`.
- **Single basis of acceptance.** The acceptance basis is the set of accepted EPC anchor deliverables and the workbook/source-supported package definition. Acceptance criteria not anchored in those documents are surfaced as HRRs, not silently introduced.
- **Source fidelity over convenience.** Package-specific technical values (rating allocation, impedance, vector group, BIL, grounding scheme, etc.) are `TBD` unless `DEL-026-02`, `DEL-026-04`, or an accepted source slice supports them.
- **Interface coverage is explicit.** Each `PKG-026` interface type from `INTERFACE_REGISTER.csv` is addressed or explicitly deferred; coverage is not implicit.
- **Conflicts surface, not silently reconciled.** Disagreements between vendor submittals and EPC anchors are routed to the Conflict Table for human ruling.

## Considerations

- The EPC Integrator is acceptance authority for facility integration; the Package Vendor is acceptance contributor for vendor design and equipment. Acceptance language must not blur this split.
- Vendor documentation completeness is governed by `DEL-026-05`; the review log here references that register and adds disposition, not new register rows.
- Factory/shop test scope and acceptance criteria flow from `DEL-026-02` and the vendor design basis; if either is incomplete, acceptance is conditional and a Conflict/HRR item is opened.
- Construction tie-in and physical installation acceptance is governed by `DEL-026-03`; this deliverable cites those records but does not re-author them.
- Long-lead and certification-dependent items (factory testing, transport, site receipt) typically gate facility energization; sequence these explicitly in `Procedure.md`.

## Trade-offs

- **Acceptance breadth vs. evidence cost.** Broader checklists give stronger acceptance evidence but cost more EPC review effort; narrow checklists reduce cost but increase residual integration risk. Default to the union of `DEL-026-02` requirements and `INTERFACE_REGISTER.csv` interface coverage.
- **Closing items at acceptance vs. carrying them as turnover open-items.** Closing forces resolution before turnover but can delay schedule; carrying open-items accelerates turnover but transfers risk to operations. The default in this skill is to record open-items as HRRs and not silently close them.
- **Vendor-led testing vs. EPC-witnessed testing.** Witnessed testing strengthens acceptance evidence; unwitnessed testing depends on vendor certification. The choice is governed by `DEL-026-02` and the project test plan (TBD).

## Examples

Examples are not authored here. Concrete acceptance evidence examples are produced when `DEL-026-02`, `DEL-026-04`, and `DEL-026-05` provide the underlying technical content. Until then, example acceptance rows and test evidence are `TBD`.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-026-06-001 | The PKG-026 package name describes a 13.8 kV / 6.9 kV / 0.4 kV, 20/26 MVA step-down distribution transformer. The accessible 03-25 Comp_and_Liquids DBM source lists 13.8 kV→4.16 kV (12 MVA) and 13.8 kV→600 V (3 MVA) transformers, not a 13.8/6.9/0.4 kV 20/26 MVA unit. The TXP-8300-2 voltage/rating set is not supported by an accepted source slice. | `PACKAGE_REGISTER.csv` row `PKG-026` (package name) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` "Incoming Power and Transformers" table | Datasheet.Conditions; Specification.Standards; Procedure.Verification | Treat the package-name voltages/rating as identifier only; keep technical parameters `TBD` until `DEL-026-02` or a vendor source confirms the actual ratings and grounding scheme. | TBD |
| HRR-026-06-002 | The DBM-Comp_and_Liquids and DBM-Deepcut source files do not contain a slice specific to TXP-8300-2 or PKG-026 transformer ratings, impedance, vector group, taps, cooling class, BIL, grounding scheme, or hazardous-area classification. | `_REFERENCES.md`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` | Gate 7 registers (do not carry parameter values) | Datasheet.Conditions; Datasheet.Construction; Specification.Standards | Carry all package-specific transformer parameters as `TBD` and propagate them as acceptance gaps until `DEL-026-02` and/or `DEL-026-04` resolve them; the acceptance package documents the gap rather than fabricating values. | TBD |
| HRR-026-06-003 | Objective associations (`OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010`) are inherited from the package-level objective mapping. `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC` means the per-deliverable association is best-effort, not asserted as a hard requirement. | `_CONTEXT.md` (Supports Objectives) | `OBJECTIVE_DELIVERABLE_MAP.csv` (package-grouped) | Datasheet.Identification; Specification.Scope | Treat objective association as ASSUMPTION until the human or a deliverable-level mapping confirms it. | TBD |
| HRR-026-06-004 | The vendor document register, vendor test list, and acceptance criteria for `PKG-026` are not present in the deliverable folder or in accessible sources; they are expected to come from `DEL-026-02`, `DEL-026-04`, and `DEL-026-05`. | `_REFERENCES.md`; `ARTIFACT_REGISTER.csv` rows for `PKG-026` | Companion deliverable folders (not read here, out of scope) | Specification.Requirements (REQ-026-06-003 to REQ-026-06-005); Procedure.Steps | Defer concrete vendor document list and test list to the corresponding companion deliverables; do not invent here. | TBD |
