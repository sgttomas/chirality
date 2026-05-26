# Guidance: DEL-093-05 — Vendor Document Turnover Package

## Purpose

The Vendor Document Turnover Package exists so that, at PKG-093 handover, the EPC Integrator and the owner have a **complete, consistent, and traceable** set of vendor-produced documentation for the API 650 water tanks package. The register, submittals, and turnover records together establish what was promised, what was delivered, what was reviewed, and what was accepted — a single audit trail spanning vendor production and EPC review.

The decomposition basis (`_CONTEXT.md`) names this deliverable as the Gate 5 additional deliverable for vendor documentation; individual source document rows remain artifacts/evidence within this package rather than being lifted into separate deliverables.

## Principles

1. **Register-first.** The Vendor Document Register is the spine of this deliverable. Submittals and turnover records both reference and update register rows. (Source: DBM line 617 — "Package deliverables shall include … vendor document registers.")
2. **Source-grounded scope.** The set of required documents is governed by `26020-Package_Requirements.docx` package heading 45 (PROPOSAL — clause-level content not locally accessible; treat as **location TBD** until the source slice is read).
3. **Single chain of custody.** Every submittal flows through controlled document control: vendor issue → EPC review → comment resolution → accepted → turnover.
4. **Evidence, not duplication.** Where the source set already lists vendor documents in a table, register rows reference those source rows as evidence rather than re-authoring them.
5. **Interface-aware review.** The EPC Integrator's interface/integration review confirms that vendor documents are consistent with adjacent packages (tie-ins, utilities, controls) and with the design envelope (e.g., -40 deg C ambient minimum, API 650 governance).
6. **Status discipline.** Register status fields (submitted / under review / commented / accepted / superseded) drive the turnover acceptance decision. No row may close as "Accepted" without acceptance evidence.

## Considerations

- **Source accessibility.** `26020-Package_Requirements.docx` heading 45 and `26020-Packages_Interfaces_4_export.xlsx` are referenced by upstream but not available as markdown in the workspace at the time of drafting. Clause-level requirements from those sources are **TBD** until accessible.
- **Discipline scope.** PKG-093 is Mechanical (API 650 tanks), but vendor documents will typically include electrical, controls, coatings, and QA/QC content. The register must accommodate all disciplines that the vendor's documentation reaches.
- **Decomposition vs. source authority.** Where decomposition prose and source text disagree, source text governs (skill rule). For this deliverable, decomposition prose (`_CONTEXT.md` Notes) explicitly tells us NOT to promote source vendor document rows to separate deliverables — this is a routing rule, not a requirements claim, and is consistent with source authority.
- **Boundary with DEL-093-06.** EPC review and acceptance workflow execution lives in `DEL-093-06`; this deliverable provides the documentation substrate that flows through that workflow. Avoid duplicating workflow content here.
- **Boundary with DEL-093-04.** Engineered equipment design content (datasheets, drawings, calculations) is the substance the vendor produces; this deliverable governs how it is organized, submitted, reviewed, and turned over — not its engineering correctness.

## Trade-offs

- **Register granularity.** Finer-grained registers (e.g., per-drawing rows) improve traceability but raise maintenance load; coarser registers (e.g., per-document-set rows) reduce overhead but lose row-level acceptance evidence. PROPOSAL: row-per-document with a parent-set grouping column. Confirm against `26020-Package_Requirements.docx` heading 45 when accessible.
- **Native source rows vs. authored register rows.** Carrying native source vendor document table rows as evidence preserves provenance but creates two parallel structures (source view and register view). The `_CONTEXT.md` notes resolve this by treating source rows as evidence under register rows.
- **Acceptance threshold.** Accepting documents on a row-by-row basis enables earlier partial turnover; whole-package acceptance is simpler but blocks any early use. PROPOSAL: row-by-row acceptance with whole-package turnover gate at handover.

## Examples

Representative register row shape (PROPOSAL — confirm columns against source):

| DocNo | Title | Type | Rev | Submitted | Review Status | Turnover Status | SOW Item(s) |
|---|---|---|---|---|---|---|---|
| (vendor-assigned) | (e.g., "Tank Mechanical Datasheet — Sour PW Tank") | Datasheet | A | 2026-MM-DD | Under review / Commented / Accepted | Pending / Accepted | `SOW-0229` |
| (vendor-assigned) | (e.g., "Tank Foundation Loading Drawing") | Drawing | A | 2026-MM-DD | … | … | `SOW-0230` |

Concrete document numbers and titles — **TBD** pending vendor selection and source heading-45 access.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-1 | Source-required document list cannot be enumerated because the source heading is not locally accessible | `_CONTEXT.md` Source Reference (26020-Package_Requirements.docx heading 45) | DBM line 617 (generic mechanical-package convention) | Specification R-2, R-5, R-9; Datasheet "Construction" rows | Treat as TBD until source slice is accessible; use heading-45 as authority once read | TBD |
| C-2 | API 650 is named only by package title; specific clauses governing vendor documentation content are not located | PKG-093 title (`_CONTEXT.md`) | No locally accessible API 650 clause text | Specification Standards table; Datasheet "Governing design standard" row | Carry API 650 as governing standard with "location TBD" until clause slices are accessible | TBD |
