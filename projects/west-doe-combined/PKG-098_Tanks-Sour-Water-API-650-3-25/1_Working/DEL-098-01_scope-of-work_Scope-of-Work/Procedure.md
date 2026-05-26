# Procedure — DEL-098-01 Scope of Work

> Operational procedure for producing the EPC Integrator Scope of Work for PKG-098.

## Purpose

Produce the PKG-098 Scope of Work artifact set (package scope of work narrative, tagged-equipment and identity list, package function and integration narrative, responsibility assignment record) in a source-faithful, traceable manner suitable for downstream consumption by DEL-098-02 through DEL-098-06.

## Prerequisites

- Read access to `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md` in this deliverable folder.
- Access to authoritative sources:
  - `_Sources/26020-Package_Requirements.docx`, §`26020-03-PT-19-007 - Tanks, Sour Water`.
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
- Access to GATE-07 PROJECT_DECOMP snapshot (deliverable register, objective-scope map).
- Declared dependencies: none (PREPARATION declared no upstream/downstream).
- Acknowledged inaccessible sources (carry as TBD per source-grounding rule):
  - `Bid Docs/Budgetary/26020-03-PT-RFQ-19-007 - Sour Water Tanks.docx` (incl. Appendix A).
  - `26020-Packages_Interfaces.3.xlsx`.

## Steps

1. **Confirm package identity.** From `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv` row `DEL-098-01_scope-of-work`, record DeliverableID, parent package, discipline, responsible party, covered scope items (SOW-0221–SOW-0224), supported objectives (OBJ-002 through OBJ-010). [Verification: each field matches both files.]

2. **Extract authoritative source slice.** Open `26020-Package_Requirements.docx` §`26020-03-PT-19-007 - Tanks, Sour Water`. Capture: Location/Status row; Basic Scope; Major Included Equipment (Items 1–3 with tags and common technical basis); Scope Notes / Open Items (operating/design conditions, "by others" exclusions, capacity reference to Appendix A, Item-2 temperature TBD, Driver TBD); Physical Interface Summary applicability matrix and interface-source identifier; Vendor Engineering Deliverables full enumeration; Interface Coordination Notes ("TBD."). [Verification: every value carried to Datasheet/Specification traces to a captured slice line.]

3. **Extract corroborating DBM context.** From `3-25_Comp_and_Liquids_DBM.md`, capture: facility receives statement; Liquids Hub function statement; liquids hub equipment basis sentence (eleven 3,800 bbl condensate + seven 3,800 bbl produced-water tanks); produced-water system paragraph (five sour + two sweet; modified API 650; Devchem 253; insulation/heating; SG 1.25 TBC / 1.18 pump basis); sour-service pressure-vessel statement. [Verification: every DBM citation in the four documents matches captured slice.]

4. **Draft Datasheet.** Populate Identification, Attributes (Items 1–3 tagged equipment table), Conditions (operating + design envelope with Item-2 temperature TBD; capacity location TBD), Construction (modified API 650, coating, insulation/heating, skim, material TBD, exclusions), Integration narrative, References. [Verification: every non-trivial value has a Source column or inline citation; no values invented.]

5. **Draft Specification.** Define Scope (Included / Excluded), Requirements R-1 through R-11 each citing source, Standards (API 650 modified; sour-service ASSUMPTION; BC regulatory context), Verification table mapping each R-* to a check, Documentation list aligned to anticipated artifacts. [Verification: each requirement has at least one cited source; ASSUMPTION/TBD labels present where required.]

6. **Draft Guidance.** State Purpose; six Principles; package-specific Considerations; trade-off framing; one worked example using source-faithful phrasing; populate the Conflict Table CFT-098-01-01 through CFT-098-01-07 with Source A / Source B / impacted sections / PROPOSAL / TBD human ruling. [Verification: each conflict has both sources or explicit "(no resolving source)" entry.]

7. **Draft Procedure (this document).** Capture Purpose, Prerequisites, Steps, Verification, Records.

8. **Cross-document consistency sweep (Pass 2).** Check that:
   - Tank tags and quantities match in Datasheet, Specification, Guidance.
   - Operating/design values are identical across documents (atmospheric; 10 °C; TBD Item 2; 32 oz; -40/60 °C).
   - "Modified API 650" wording is used consistently (not bare "API 650").
   - Coating spelling "Devchem 253" consistent; skim "Kennilworth type HCL" consistent.
   - Source citation paths use the same absolute or relative form throughout.
   - Conflict Table IDs referenced from Datasheet/Specification resolve in Guidance.
   [Verification: a manual line-by-line diff against the source slice. Any inconsistency is corrected against source; if unresolvable, added to the Conflict Table.]

9. **Update `_STATUS.md` safely.** Only if current state is `OPEN`, run `tools/scaffolding/write_status.sh` to advance to `INITIALIZED` with actor token `TASK+four-documents`. Otherwise, skip.

10. **Write run record.** Append `_run_records/TASK_RUN_2026-05-25_<HHMM>.md` summarizing pass directive (`P1_P2`), files written, source slices consulted, conflicts surfaced, and RUN_STATUS.

## Verification

- All four documents present in `{DELIVERABLE_PATH}`.
- Default schema sections present in each.
- Every non-trivial fact in Datasheet/Specification cites either Package Requirements §`26020-03-PT-19-007` or `3-25_Comp_and_Liquids_DBM.md` (or is labelled TBD/ASSUMPTION with reason).
- Conflict Table contains entries for each known source-vs-source or source-vs-absence disagreement.
- `_STATUS.md` advanced OPEN → INITIALIZED only if it was OPEN.

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md` (with Conflict Table), `Procedure.md` (this file) in `{DELIVERABLE_PATH}`.
- `_STATUS.md` history line for OPEN → INITIALIZED transition (when applicable).
- `_run_records/TASK_RUN_2026-05-25_<HHMM>.md` capturing the Pass 1 + Pass 2 run.
- (Future, by `lens-register` skill) `_SEMANTIC_LENSING.md` to drive a subsequent Pass 3 enrichment via `RUN_PASSES: P3_ONLY`.
