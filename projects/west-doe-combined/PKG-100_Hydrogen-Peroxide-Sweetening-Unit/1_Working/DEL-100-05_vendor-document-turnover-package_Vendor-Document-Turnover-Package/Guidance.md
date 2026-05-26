# Guidance: DEL-100-05 — Vendor Document Turnover Package

## Purpose

The Vendor Document Turnover Package exists so that, at PKG-100 handover, the EPC Integrator and the owner have a **complete, consistent, and traceable** set of vendor-produced documentation for the Hydrogen Peroxide Sweetening Unit. The register, submittals, and turnover records together establish what was promised, what was delivered, what was reviewed, and what was accepted — a single audit trail spanning vendor production and EPC review.

The decomposition basis (`_CONTEXT.md`) names this deliverable as the Gate 5 additional deliverable for vendor documentation; individual source document rows remain artifacts/evidence within this package rather than being lifted into separate deliverables.

## Principles

1. **Register-first.** The Vendor Document Register is the spine of this deliverable. Submittals and turnover records both reference and update register rows. (Source: DBM SEC-09 line 617 — "Package deliverables shall include … vendor document registers.")
2. **Source-grounded scope.** The set of required documents is governed by `26020-Package_Requirements.docx` package heading 52 (PROPOSAL — clause-level content not locally accessible; treat as **location TBD** until the source slice is read).
3. **Single chain of custody.** Every submittal flows through controlled document control: vendor issue → EPC review → comment resolution → accepted → turnover.
4. **Evidence, not duplication.** Where the source set already lists vendor documents in a table, register rows reference those source rows as evidence rather than re-authoring them.
5. **Interface-aware review.** The EPC Integrator's interface/integration review confirms that vendor documents are consistent with adjacent packages (tie-ins, utilities, controls) and with the design envelope (e.g., -40 deg C ambient minimum, sour-water service) and the explicit PKG-100 interface scope listed in `PACKAGE_REGISTER.csv` row 63.
6. **Chemical-handling discipline.** Because the package handles hydrogen peroxide (an oxidizer) in sour-water service, vendor documentation shall explicitly address materials compatibility, segregation from incompatibles, spill containment, and operator safety. Reviewers should treat absence of H2O2-handling content as a defect.
7. **Status discipline.** Register status fields (submitted / under review / commented / accepted / superseded) drive the turnover acceptance decision. No row may close as "Accepted" without acceptance evidence.

## Considerations

- **Source accessibility.** `26020-Package_Requirements.docx` heading 52 and `26020-Packages_Interfaces_4_export.xlsx` are referenced by upstream but not parseable as markdown in the workspace at the time of drafting. Clause-level requirements from those sources are **TBD** until accessible.
- **Discipline scope.** PKG-100 is Mechanical (H2O2 sweetening package), but vendor documents will span chemical/process, electrical, instrumentation/controls, structural, coatings, and QA/QC content. The register must accommodate all disciplines that the vendor's documentation reaches.
- **Decomposition vs. source authority.** Where decomposition prose and source text disagree, source text governs (skill rule). For this deliverable, decomposition prose (`_CONTEXT.md` Notes) explicitly tells us NOT to promote source vendor document rows to separate deliverables — this is a routing rule, not a requirements claim, and is consistent with source authority.
- **Boundary with DEL-100-06.** EPC review and acceptance workflow execution lives in `DEL-100-06`; this deliverable provides the documentation substrate that flows through that workflow. Avoid duplicating workflow content here.
- **Boundary with DEL-100-04.** Engineered equipment design content (datasheets, drawings, calculations) is the substance the vendor produces; this deliverable governs how it is organized, submitted, reviewed, and turned over — not its engineering correctness.
- **Capacity note.** DBM SEC-06 line 427 lists package capacity as 3,840 m3/d "TBC" — vendor documentation should record the as-built capacity unambiguously and reconcile any deviation from the DBM basis.

## Trade-offs

- **Register granularity.** Finer-grained registers (e.g., per-drawing rows) improve traceability but raise maintenance load; coarser registers (e.g., per-document-set rows) reduce overhead but lose row-level acceptance evidence. PROPOSAL: row-per-document with a parent-set grouping column. Confirm against `26020-Package_Requirements.docx` heading 52 when accessible.
- **Native source rows vs. authored register rows.** Carrying native source vendor document table rows as evidence preserves provenance but creates two parallel structures (source view and register view). The `_CONTEXT.md` notes resolve this by treating source rows as evidence under register rows.
- **Acceptance threshold.** Accepting documents on a row-by-row basis enables earlier partial turnover; whole-package acceptance is simpler but blocks any early use. PROPOSAL: row-by-row acceptance with whole-package turnover gate at handover.

## Examples

Representative register row shape (PROPOSAL — confirm columns against source):

| DocNo | Title | Type | Rev | Submitted | Review Status | Turnover Status | SOW Item(s) |
|---|---|---|---|---|---|---|---|
| (vendor-assigned) | (e.g., "Hydrogen Peroxide Reactor Mechanical Datasheet") | Datasheet | A | 2026-MM-DD | Under review / Commented / Accepted | Pending / Accepted | `SOW-0107` |
| (vendor-assigned) | (e.g., "Static Mixer GA Drawing") | Drawing | A | 2026-MM-DD | … | … | `SOW-0108` |
| (vendor-assigned) | (e.g., "H2O2 Injection Pump IOM Manual") | Manual | A | 2026-MM-DD | … | … | `SOW-0109` |

Concrete document numbers and titles — **TBD** pending vendor selection and source heading-52 access.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-1 | Source-required document list cannot be enumerated because the source heading is not locally accessible | `_CONTEXT.md` Source Reference (`26020-Package_Requirements.docx` heading 52) | DBM SEC-09 line 617 (generic mechanical-package convention) | Specification R-2, R-5, R-10; Datasheet "Construction" rows | Treat as TBD until source slice is accessible; use heading-52 as authority once read | TBD |
| C-2 | H2O2 service introduces oxidizer-handling, materials-compatibility, and safety-documentation requirements not enumerated in any locally accessible standard | DBM SEC-06 lines 214-216 (H2O2 process basis) | No locally accessible safety/handling standard text | Specification Standards row "Hydrogen peroxide handling / safety standards"; Datasheet "Chemical handled" row | Carry as ASSUMPTION; once project safety basis or vendor safety basis is accessible, replace with cited authority | TBD |
| C-3 | Package capacity recorded as "3,840 m3/d TBC" in DBM | DBM SEC-06 line 427 | No reconciled basis in accessible sources | Datasheet "Package capacity (context)" row | Carry DBM value as TBC; vendor as-built value governs at turnover | TBD |
