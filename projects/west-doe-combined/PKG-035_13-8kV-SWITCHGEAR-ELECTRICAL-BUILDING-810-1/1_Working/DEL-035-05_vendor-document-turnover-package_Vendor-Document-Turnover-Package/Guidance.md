# Guidance: DEL-035-05 — Vendor Document Turnover Package

## Purpose

This deliverable consolidates the Package Vendor's documentation lifecycle for the 13.8kV Switchgear Electrical Building (`PKG-035`) into a single turnover package that the EPC Integrator can review (`DEL-035-06`), accept, and hand off downstream. It is the canonical "what documents must accompany this package, and in what shape, to be considered complete." Source: `_CONTEXT.md` (Scope; Anticipated Artifacts); `DELIVERABLE_REGISTER.csv` rows `DEL-035-05` and `DEL-035-06`.

## Principles

1. **Single composite deliverable, many artifacts.** Individual vendor document rows are not separate decomposition deliverables; they are evidence/artifacts inside this turnover package. Treat the Vendor Document Register as the deliverable artifact and individual documents as register entries. Source: `_CONTEXT.md` (Notes).
2. **Baseline = Table 4 Core + applicable disciplines.** The Core vendor documents (Table 4 rows 1–11) apply to every package without exception. Discipline-specific families apply per workbook row 37 cross-discipline flags. Source: `_Sources/26020-Package_Requirements.docx` Table 4; `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 37.
3. **Package-specific applicability is set by EPC sibling deliverables.** The exact subset of Electrical-family and cross-discipline documents required for `PKG-035` is governed by the EPC Scope of Work (`DEL-035-01`) and the Package Datasheet (`DEL-035-02`). Until those are drafted, treat the Datasheet/Specification tables here as the working baseline. Source: `DELIVERABLE_REGISTER.csv` rows `DEL-035-01`, `DEL-035-02`.
4. **Register-first thinking.** PRQ-009 (Vendor Document Index) is the spine. Every other vendor document exists as a row in PRQ-009 with status and disposition. Source: `_Sources/26020-Package_Requirements.docx` Table 4 row 2.
5. **Turnover compilation is anchored by three documents.** PRQ-009 (final index), QLT-021 (Manufacturing Record Book / Vendor Data Book), and PRQ-016 (Vendor Data Book / Final Supplier Documentation) together constitute the turnover compilation. Source: Table 4 rows 2, 8, 11.
6. **EPC review happens elsewhere.** Review and acceptance is `DEL-035-06`. This deliverable's job is to be reviewable, not to perform the review. Source: `DELIVERABLE_REGISTER.csv` row `DEL-035-06`.

## Considerations

- **Workbook row 37 governs cross-discipline scope.** Families marked `X` on row 37 are in-scope for vendor documentation; families marked `None` are out-of-scope and should not appear in the turnover package as standalone documents. Source: `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 37.
- **No package-specific section exists in the Package Requirements doc.** `_Sources/26020-Package_Requirements.docx` does not contain a Heading 1 section for `PKG-035` or "13.8kV Switchgear Electrical Building." Treat the generic Table 4 as the only directly applicable source until a package-specific requirement document is added. Source: heading scan of `_Sources/26020-Package_Requirements.docx` (no match for `13.8`, `switchgear`, or `30-026`).
- **DBM sources do not cover switchgear documentation.** `DBM-Comp_and_Liquids` and `DBM-Deepcut` are process-unit DBMs. They contribute no requirements for this electrical deliverable. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- **EHT is excluded for this package.** Workbook row 37 marks EHT as None; ELE-018 and the piping heat-tracing items (PIP-020, PIP-021) are therefore outside the vendor document scope for `PKG-035`. Source: workbook row 37.
- **`Communications / Network`, `Building HVAC / Services`, `Maintenance Access`, `Grading / Site Drainage / Spill Containment`, `Utility Piping`** are `X`-flagged on row 37 but have no dedicated Table 4 family. Specific document IDs are `TBD` until the EPC Scope of Work or a project document-control standard names them.

## Trade-offs

- **Comprehensive register vs reviewability.** A register that lists every conceivable document maximizes traceability but creates review burden; a minimal register risks omissions. Recommendation (PROPOSAL): include every Core document unconditionally; include discipline documents only when workbook flags or `DEL-035-01`/`DEL-035-02` confirm applicability; mark `N/A` rather than omit, so the absence is auditable.
- **Embedded vs referenced turnover compilation.** Embedding all vendor documents inside QLT-021/PRQ-016 maximizes self-containment but inflates package size; referencing keeps the package compact but depends on document-control stability. Decision is `TBD` pending project document-control standard.
- **Vendor-authored vs EPC-supplied register format.** Allowing the vendor's native register format is faster but produces heterogeneous registers across packages; requiring an EPC-supplied template is slower but more consistent. Decision is `TBD` pending project document-control standard.

## Examples

No package-specific examples are present in the accessible source set (`_Sources/26020-Package_Requirements.docx` has no Heading 1 section for `PKG-035`; DBM sources are unrelated). Examples are deferred until project-level reference vendor data books are supplied.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-035-05-001 | Workbook row 37 flags Building HVAC / Services, Communications / Network, Maintenance Access, Grading / Site Drainage / Spill Containment, and Utility Piping as `X` for `PKG-035`, but `_Sources/26020-Package_Requirements.docx` Table 4 has no dedicated vendor-document family for these scopes. Vendor document IDs to require for these families cannot be derived from accessible sources. | `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 37 | `_Sources/26020-Package_Requirements.docx` Table 4 (no matching family) | Specification R-035-05-007; Datasheet "Cross-discipline document families" | Treat as `TBD` rows in the Vendor Document Register; defer document-ID enumeration to EPC Scope of Work (`DEL-035-01`) and Package Datasheet (`DEL-035-02`). | TBD |
| HRR-035-05-002 | Required field set for the Vendor Document Register (R-035-05-008) is conventional and not specified in accessible sources. | Inferred convention | `_Sources/26020-Package_Requirements.docx` (DOC-008 row exists but its content is not in the accessible source) | Specification R-035-05-008; Procedure step 4 | Adopt the proposed conventional field set as a working baseline; replace with project document-control standard when supplied. | TBD |
| HRR-035-05-003 | Turnover compilation format (embedded vs referenced; native vendor format vs EPC template) is not specified in accessible sources. | Inferred convention | None | Specification R-035-05-009; Procedure step 7; Guidance "Trade-offs" | Default to referenced compilation under PRQ-009 / QLT-021 / PRQ-016 anchors; revisit when project document-control standard is supplied. | TBD |
| HRR-035-05-004 | Applicable MV-switchgear test/standards (e.g., IEEE C37, IEC 62271) are not enumerated for `PKG-035` in the accessible Package Requirements source. | Convention / engineering practice | `_Sources/26020-Package_Requirements.docx` (no clause references for `PKG-035`) | Specification "Standards"; R-035-05-006 | Carry as ASSUMPTION at standards-family level only; do not derive clause-level requirements until source is supplied or `DEL-035-01`/`DEL-035-02` names specific standards. | TBD |
