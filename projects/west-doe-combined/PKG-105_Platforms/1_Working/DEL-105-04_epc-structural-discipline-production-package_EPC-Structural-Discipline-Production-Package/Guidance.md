# Guidance: DEL-105-04 — EPC / Structural Discipline Production Package

## Purpose

This deliverable exists to produce the **EPC / Structural Discipline Production Package** for `PKG-105 — Platforms`: the discipline-execution view of the non-vendor portion of the Platforms package, carried conservatively from the workbook and DBM source basis (`DELIVERABLE_REGISTER.csv` row `DEL-105-04`).

It complements the three mandatory EPC anchor deliverables for PKG-105 (Scope of Work `DEL-105-01`, Package Datasheet `DEL-105-02`, Construction Work Package `DEL-105-03`) by providing the discipline production unit that the EPC Integrator or assigned discipline subcontractor uses to execute structural production for the Platforms package.

## Principles

- **Source-fidelity over convention.** Discipline production content must trace to workbook (`_Sources/26020-Package_Requirements.docx`) or DBM slices, or be marked TBD. Generic structural conventions must not be substituted for source statements. (Authority: `four-documents` SKILL — source-grounding rule; `DELIVERABLE_REGISTER.csv` Notes for `DEL-105-04`.)
- **Conservative carry-forward.** The deliverable register explicitly characterizes this production unit as "carried conservatively from workbook and DBM support." Where source is silent, this deliverable records the gap rather than inventing requirements.
- **Non-vendor framing.** This unit covers non-vendor scope only; vendor-supplied platform components remain in the EPC anchor stream and are not re-specified here.
- **Interface respect.** Recorded PKG-105 interfaces (Area / Exterior Lighting; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports) are facts (`INTERFACE_REGISTER.csv`); platform-to-equipment tie-ins are routed through the EPC Integrator's 3D model and integrated P&ID set per Gate 6 disposition.

## Considerations

- **Source slices have not been copied during PREPARATION** (`_REFERENCES.md` Missing/Deferred References). Before promoting any structural requirement (loads, material grades, codes, connections, fireproofing, coatings) into the four documents, extract the relevant slice from `_Sources/26020-Package_Requirements.docx` and re-run this skill.
- **Responsible party is TBD.** Until the EPC Integrator vs. discipline subcontractor split is set, ownership of internal subdeliverables (the TBD discipline deliverable register) must remain provisional.
- **No declared upstream/downstream dependencies.** `_DEPENDENCIES.md` records none; this is intentional in DECLARED mode but means coordination with DEL-105-01..03 is not enforced through the dependency graph. Treat the three anchor deliverables as functional upstreams in practice.
- **OBJ mapping is FACT (deliverable-ID-explicit).** `OBJECTIVE_DELIVERABLE_MAP.csv` lists this deliverable explicitly for OBJ-001/005/008/010 — no package heuristic was needed.

## Trade-offs

| Trade-off | Discussion |
|---|---|
| Conservative carry-forward vs. completeness | Marking source-absent items TBD preserves auditability but defers structural-design specificity to a later pass with source-slice access. PROPOSAL: defer until slice extraction. |
| Discipline subcontractor split vs. EPC Integrator self-perform | Source does not prescribe; both are admissible per `PACKAGE_REGISTER.csv` Notes. ASSUMPTION: the choice will be made at Gate 5 disposition and is not within this deliverable's authority. |
| Tie-in detail in this unit vs. EPC 3D model | Gate 6 disposition assigns platform-to-equipment tie-ins to the EPC Integrator's 3D model and integrated P&ID set; this production package should reference, not duplicate, that model. |

## Examples

No source-grounded examples are available for the Platforms structural production unit in the locally accessible references. Section omitted pending source-slice extraction (`TBD`).

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-01 | `_CONTEXT.md` lists Anticipated Artifacts as "Discipline production package basis; TBD discipline deliverable register; source-limited requirements closure record" while `ARTIFACT_REGISTER.csv` for `DEL-105-04` lists only two artifacts (ART-16D83D7454 and ART-10C0D579FC) — the "TBD discipline deliverable register" is not registered. | `_CONTEXT.md` Anticipated Artifacts | `ARTIFACT_REGISTER.csv` rows for `DEL-105-04` | Datasheet Conditions; Specification Documentation; Procedure Records | Accept both: treat the TBD discipline deliverable register as a planned-but-unregistered artifact to be added to `ARTIFACT_REGISTER.csv` when produced. | TBD |
| CT-02 | Responsible party is "TBD; EPC Integrator or discipline subcontractor as assigned" in both `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv`, but no assignment record exists in accessible sources. | `_CONTEXT.md` ResponsibleParty | `DELIVERABLE_REGISTER.csv` Responsible column | Datasheet Identification; Procedure Prerequisites | Defer to Gate 5 disposition. | TBD |
| CT-03 | Governing structural codes/standards are not named in accessible sources, but a structural production package normally relies on a project structural code basis. ASSUMPTION uses inheritance from the EPC anchor (DEL-105-01/02). | Specification Standards (ASSUMPTION) | `_REFERENCES.md` Missing/Deferred References | Specification Standards; Requirements R-08..R-10 | Confirm by workbook slice extraction; if absent, route via DEL-105-02 Package Datasheet basis. | TBD |
