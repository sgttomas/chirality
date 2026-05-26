# Guidance: DEL-074-05 — Vendor Document Turnover Package

## Purpose

This deliverable consolidates the vendor-side documentation deliverables for the Caustic Treating (NGL Mercaptan Removal) package (`PKG-074`): the document register, submittals, source-required vendor documentation, and turnover records. It exists so that the Package Vendor has one accountable production unit for documentation, distinct from the engineered equipment package (`DEL-074-04`) and from the EPC review/acceptance evidence (`DEL-074-06`).

## Principles

- **One vendor documentation production unit per package.** Vendor document register, submittals, source-required vendor documentation, and turnover records are consolidated here rather than spread across separate deliverables (decomposition row 274).
- **Source rows as artifacts.** Individual source vendor document table rows are carried inside this deliverable as evidence/artifacts; they are not promoted to standalone deliverables.
- **Vendor produces; EPC reviews.** The Package Vendor owns production and submission; the EPC Integrator owns interface/integration review. Acceptance evidence is consolidated in `DEL-074-06`, not here (ASSUMPTION based on package-structure separation across DEL-074-01..06).
- **Source-grounding over convention.** Where `26020-Package_Requirements.docx` heading 28 specifies required documents or turnover content, that source governs; conventions fill gaps only where source is silent or unavailable.

## Considerations

- The source slice from `26020-Package_Requirements.docx` package heading 28 is not locally accessible as text in this run, so the exact required-document list, submittal cycle, and turnover record composition remain `TBD`.
- `_DEPENDENCIES.md` declares no upstream or downstream edges. Logical upstream (EPC Scope of Work, Package Datasheet) and logical downstream (EPC Vendor Package Review and Acceptance) relationships should be declared explicitly when dependency extraction is performed.
- The objective associations (`OBJ-001`, `OBJ-003` through `OBJ-010`) are recorded as `ASSUMPTION` under the `PACKAGE_HEURISTIC` mode and should be confirmed against the objective-deliverable map once a deliverable-ID-level mapping is available.

## Trade-offs

- **Consolidating source rows as artifacts vs. promoting them to deliverables.** The decomposition explicitly keeps them as artifacts. This keeps the deliverable count flat and the documentation responsibility in one place, at the cost of larger artifact bundles inside this deliverable.
- **Register-driven vs. submittal-driven control.** A register-first approach (every required document enumerated up front) is more auditable; a submittal-first approach is more responsive to vendor reality. The skill cannot decide between these without source guidance — TBD.
- **Vendor format vs. project format.** Where vendor-native documentation formats differ from project document-control conventions, accepting vendor-native formats reduces vendor cost but burdens EPC review; the project-format path improves integration but may not be supported by all vendor systems. TBD pending project document-control rules.

## Examples

- TBD — concrete examples (sample register row, sample submittal log entry, sample turnover record line) require access to the package requirements source slice or to a sibling vendor-document-turnover deliverable that has been resolved.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-074-05-01 | Objective association at deliverable-ID level vs. package-grouping heuristic. `_CONTEXT.md` lists `OBJ-001`, `OBJ-003`..`OBJ-010` as supported objectives, but this is recorded as `ASSUMPTION (PACKAGE_HEURISTIC)`; an authoritative deliverable-ID-level mapping is not visible in this run. | `_CONTEXT.md` Supports Objectives | `OBJECTIVE_DELIVERABLE_MAP.csv` (Gate 7 snapshot) | Datasheet Identification; this Guidance file | Confirm the package-heuristic association unless the objective-deliverable map specifies different rows for `DEL-074-05`. | TBD |
| CONF-074-05-02 | Required-document list cannot be enumerated because `26020-Package_Requirements.docx` heading 28 is not locally accessible as text. Decomposition narrative names categories at a high level only. | Decomposition row 274 narrative | `26020-Package_Requirements.docx` heading 28 (binary) | Specification REQ-074-05-01..-03; Procedure Steps | Treat decomposition narrative as scoping context only; do not synthesize a document list from convention. Resolve once the source slice is accessible. | TBD |
| CONF-074-05-03 | Acceptance-evidence boundary between this deliverable (turnover records) and `DEL-074-06` (EPC review and acceptance). | Decomposition row 274 | Decomposition row 275 | Specification REQ-074-05-05, -06; Procedure Verification | Vendor produces turnover records here; EPC review log and acceptance checklist live in `DEL-074-06`. ASSUMPTION pending human confirmation. | TBD |
