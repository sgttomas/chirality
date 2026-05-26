# Procedure: DEL-074-05 — Vendor Document Turnover Package

## Purpose

Procedure to **produce and submit** the Vendor Document Turnover Package for `PKG-074` (Caustic Treating — NGL Mercaptan Removal): vendor document register, vendor document submittals, source-required vendor documentation, and turnover records, for EPC Integrator review.

## Prerequisites

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` initialized for this deliverable (present).
- Gate 7 Final Published PROJECT_DECOMP snapshot available at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`.
- Access to the package requirements source slice: `26020-Package_Requirements.docx` package heading 28 (location TBD — currently binary, not locally accessible as text).
- (Logical, ASSUMPTION) Upstream EPC Scope of Work (`DEL-074-01`) and Package Datasheet (`DEL-074-02`) at INITIALIZED or higher maturity. Not declared in `_DEPENDENCIES.md`.
- Project document-control rules (numbering, revision conventions, status codes) — TBD.

## Steps

1. **Confirm scope** — Read `_CONTEXT.md` and the deliverable's decomposition entry (row 274 of `DELIVERABLE_REGISTER.csv`). Confirm the package, responsible party, and that source-document rows are to be carried as artifacts rather than separate deliverables.
2. **Resolve source slice (TBD when not accessible)** — Locate and read `26020-Package_Requirements.docx` package heading 28 to enumerate the required vendor documents and turnover content. If the source slice is not locally accessible as text, mark the required-document list `TBD` and do not synthesize it from convention.
3. **Build the vendor document register** — Enumerate each required vendor document with: document ID, title, type, originator, planned submittal class/revision, planned issue date, status. Populate from the source slice (Step 2). For source-required documents, mark them as such. (Detailed schema TBD pending source.)
4. **Collect source vendor document table rows as artifacts** — For each source-listed vendor document, include the source table row as embedded evidence (file pointer or excerpt) so the source basis is traceable.
5. **Plan submittals** — For each register entry, define submittal stages (e.g., issued for review, issued for approval, issued for construction, certified) — exact stage names TBD pending project document-control rules.
6. **Produce and submit vendor document submittals** — Execute submittals through revision cycles. Record each submittal transmittal in a submittal/transmittal log. Update register status accordingly.
7. **Assemble turnover records** — Compile turnover record set covering the source-required vendor documentation and any project-required turnover content (TBD pending source). Confirm each register entry has a turnover record disposition.
8. **Issue to EPC Integrator for review** — Make the register, submittals, and turnover records available to the EPC Integrator for interface/integration review. Acceptance evidence is consolidated by `DEL-074-06`, not regenerated here.
9. **Close out** — Confirm register fully populated, all required submittals dispositioned, turnover records complete, and EPC review acknowledgements received. Set deliverable status accordingly through `_STATUS.md` once human-approved.

## Verification

| Step | Verification |
|---|---|
| 1 | `_CONTEXT.md` identity matches decomposition row 274. |
| 2 | Source slice resolved or `TBD` marker present with reason. |
| 3 | Register contains a row for every source-required document (once Step 2 is resolved). |
| 4 | Each source-required register entry has an attached source-row artifact. |
| 5 | Submittal plan reconciles to project document-control rules (when available). |
| 6 | Submittal log entries exist for every register entry that has been issued; register status reflects log. |
| 7 | Turnover record set exists and ties back to register entries 1:1 for source-required items. |
| 8 | EPC Integrator received the package; receipt evidence exists (transmittal acknowledgement or equivalent). |
| 9 | All register entries closed; `_STATUS.md` only advanced under safe-update rules and human approval. |

## Records

- `Vendor Document Register` (artifact)
- Submittal transmittals / submittal log (artifact)
- Source vendor document table rows (artifact / evidence)
- Turnover record set (artifact)
- EPC review transmittal acknowledgements (evidence)
- `_run_records/TASK_RUN_*.md` for any TASK-driven updates to this deliverable
