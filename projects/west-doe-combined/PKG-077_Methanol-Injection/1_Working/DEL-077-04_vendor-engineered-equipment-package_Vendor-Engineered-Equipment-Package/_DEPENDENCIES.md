# Dependencies: DEL-077-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** DECLARED
**Dependency tracking mode:** EXTRACTED (Dependencies.csv v3.1)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

6 rows extracted (all ACTIVE). See `Dependencies.csv` for full detail.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-077-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | Methanol Injection (PKG-077) | HIGH | ACTIVE |
| DEP-077-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0143 | HIGH | ACTIVE |
| DEP-077-04-003 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | Scope of Work (DEL-077-01) | HIGH | ACTIVE |
| DEP-077-04-004 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | Package Datasheet (DEL-077-02) | HIGH | ACTIVE |
| DEP-077-04-005 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | Vendor Document Turnover Package (DEL-077-05) | HIGH | ACTIVE |
| DEP-077-04-006 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | CONSTRAINT | DELIVERABLE | EPC Vendor Package Review and Acceptance (DEL-077-06) | HIGH | ACTIVE |

## Lifecycle Summary

- ACTIVE rows: 6
- RETIRED rows: 0
- ANCHOR rows (ACTIVE): 2 — 1 × IMPLEMENTS_NODE, 1 × TRACES_TO_REQUIREMENT
- EXECUTION rows (ACTIVE): 4 — 2 × UPSTREAM PREREQUISITE, 1 × DOWNSTREAM HANDOVER, 1 × DOWNSTREAM CONSTRAINT
- SatisfactionStatus breakdown: 6 × TBD

## Run Notes

- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **Source docs scanned (AUTO):** `Datasheet.md`, `Guidance.md`, `Procedure.md`, `Specification.md`
- **Anchor doc (AUTO):** `Datasheet.md` (contains Identification table with ParentPackageID, Covers Scope Items)
- **Execution docs (AUTO order):** `Procedure.md` (primary — explicit prerequisites and hand-off steps), `Specification.md` (requirements R2, R5, R7), `Guidance.md` (supporting context)
- **Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`
- **Decomposition status:** Located and used for anchor validation (DELIVERABLE_REGISTER.csv row 399, PACKAGE_REGISTER.csv row 72, SCOPE_LEDGER.csv SOW-0143 row).
- **DECOMPOSITION_PATH param (invoker):** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/GATE-07_Final_Published_2026-05-24/` — path does not exist; auto-discovered from `_REFERENCES.md` authoritative decomposition basis instead. No impact on output quality.
- **Tree x DAG integrity:** Parent anchor count = 1 (IMPLEMENTS_NODE). No FLOATING_NODE warning. No AMBIGUOUS_ANCHOR warning.
- **Excluded from extraction:** `_CONTEXT.md`, `_MEMORY.md`, `_REFERENCES.md`, `_STATUS.md`, `_run_records/` — not source documents for dependency extraction.
- **No deliverable-local source slices present** (`_REFERENCES.md` Missing / Deferred References). Technical process conditions, standards, and equipment-level dependencies are TBD; this does not affect structural dependency rows.
- **Gate 6 disposition (Conflict C-077-04-001):** DEL-077-04 treated as the PKG-077 vendor production unit of record per DELIVERABLE_REGISTER.csv row 399. Gate 6 scope-integration question is noted in Guidance.md; no dependency row emitted (no explicit information-flow artifact transfer stated for Cryogenic Unit linkage — CONSERVATIVE).
- **Objective associations (OBJ-001, OBJ-004..OBJ-010):** Not emitted as TRACES_TO_REQUIREMENT rows; Datasheet.md flags these as ASSUMPTION (PACKAGE_HEURISTIC). CONSERVATIVE strictness does not emit implicit/assumed requirement traces.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract run: MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition auto-discovered from _REFERENCES.md (invoker path not found). 6 rows extracted (2 ANCHOR, 4 EXECUTION), all ACTIVE. Schema validation: VALID (29 columns, 6 data rows).
