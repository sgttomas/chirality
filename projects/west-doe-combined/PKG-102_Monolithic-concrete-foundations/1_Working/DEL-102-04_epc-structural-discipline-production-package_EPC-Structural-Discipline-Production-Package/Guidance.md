# Guidance: DEL-102-04 — EPC / Structural Discipline Production Package

## Purpose

This deliverable exists to establish the **structural discipline production unit** for the non-vendor scope of PKG-102 (Monolithic concrete foundations). It complements the EPC Integrator anchor deliverables (DEL-102-01 Scope of Work, DEL-102-02 Package Datasheet, DEL-102-03 Construction Work Package) by providing the discipline-level production basis from which structural engineering, design, procurement, and construction handoff can proceed.

Source: `DELIVERABLE_REGISTER.csv` row DEL-102-04; `_CONTEXT.md`.

## Principles

- **Source fidelity over convention.** The deliverable is explicitly source-limited (`_CONTEXT.md` Notes; `ARTIFACT_REGISTER.csv` ART-712FAD4E91). Do not synthesize structural design content (loads, materials, geometry, code clauses) from generic engineering convention; cite the workbook row 103 or DBM-Deepcut slice if a claim is made.
- **Conservative carry.** The carry posture from workbook and DBM support is intentionally conservative (`DELIVERABLE_REGISTER.csv` row DEL-102-04). When in doubt, mark **TBD** and route to the source-limited requirements closure record.
- **Discipline ownership clarity.** Responsibility (EPC Integrator vs. discipline subcontractor) is source-dependent and not predetermined (`PACKAGE_REGISTER.csv` PKG-102 ResponsibilityModel). Treat any assignment as ASSUMPTION until confirmed by the human authority.
- **Interface respect.** The two recorded physical interface types — Grading / Site Drainage / Spill Containment, and Structural / Foundations / Supports — bound how this production unit couples to adjacent civil and structural packages (`INTERFACE_REGISTER.csv` PKG-102 rows).
- **No vendor-package model.** No separate vendor-package ownership exists for PKG-102 (`PACKAGE_REGISTER.csv` PKG-102). Do not author vendor-engineered equipment artifacts under this deliverable.

## Considerations

- **Workbook row 103** is the only direct package-level source reference in the decomposition; the DocxPackageMatched flag is FALSE (`PACKAGE_REGISTER.csv` PKG-102), meaning the package was not matched to a corresponding heading in the requirements docx. This narrows the source basis further.
- **DBM-Deepcut** material is cited as supporting the objective mapping (OBJ-001, OBJ-008 via `OBJECTIVE_PACKAGE_MAP.csv`). Treat DBM content as context-supporting unless a specific slice is copied locally and read.
- **Coupling with DEL-102-02 (Package Datasheet).** Interface facts (ART-05281DC8CE, ART-F35AC96771) are intentionally carried on DEL-102-02, not duplicated here. This production unit should reference, not recreate, those facts.
- **Coupling with DEL-102-03 (Construction Work Package).** The construction tie-in workface plan (ART-E8798F2006) lives on DEL-102-03. This production unit furnishes the discipline basis that the construction work package builds upon.

## Trade-offs

- **Drafting depth vs. source fidelity.** Producing a richer discipline production package would require structural source slices that are not currently accessible. The trade-off is resolved in favor of fidelity: the deliverable remains thin and explicit about gaps until Gate 5 disposition.
- **Single discipline production unit vs. sub-deliverable register.** The anticipated `TBD discipline deliverable register` is left as a structured placeholder rather than a speculative list, to avoid committing the project to sub-deliverables not warranted by source.

## Examples

- TBD — no source-grounded examples available in the current source set.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CONF-01 | Responsible Party stated as "TBD; EPC Integrator or discipline subcontractor as assigned" in `_CONTEXT.md`, while `PACKAGE_REGISTER.csv` PKG-102 ResponsibilityModel states the responsibility is "source-dependent; no separate vendor-package ownership model is inferred." | `_CONTEXT.md` (Identity row Responsible Party) | `PACKAGE_REGISTER.csv` PKG-102 ResponsibilityModel | Datasheet Identification (Responsible Party); Specification R-07; Guidance Principles | PROPOSAL: treat as **non-conflict** — `_CONTEXT.md` is a deliverable-level placeholder consistent with the package-level source-dependent posture; record final assignment via human ruling when made. | TBD |
| CONF-02 | The deliverable's anticipated artifacts include a "source-limited requirements closure record" while `_REFERENCES.md` reports no deliverable-specific source slices were copied during PREPARATION. This makes the closure record's primary content TBD by construction. | `DELIVERABLE_REGISTER.csv` row DEL-102-04 AnticipatedArtifacts; `ARTIFACT_REGISTER.csv` ART-712FAD4E91 | `_REFERENCES.md` Missing/Deferred References | Specification R-05, R-09; Procedure Steps | PROPOSAL: produce the closure record as a gap ledger only (no design content); route detailed requirements to Gate 5 disposition once source slices are obtained. | TBD |
| CONF-03 | Objective mapping OBJ-001 and OBJ-008 are listed on `_CONTEXT.md` "Supports Objectives" while `OBJECTIVE_PACKAGE_MAP.csv` is package-level (PKG-102 → OBJ-001, OBJ-008) and not deliverable-level. | `_CONTEXT.md` Supports Objectives | `OBJECTIVE_PACKAGE_MAP.csv` PKG-102 rows | Datasheet Identification (Supports Objectives); Specification R-08 | PROPOSAL: retain mapping as **ASSUMPTION (PACKAGE_HEURISTIC)** per brief `OBJECTIVE_ASSOCIATION_MODE`; do not treat as a hard requirement until human confirmation. | TBD |
