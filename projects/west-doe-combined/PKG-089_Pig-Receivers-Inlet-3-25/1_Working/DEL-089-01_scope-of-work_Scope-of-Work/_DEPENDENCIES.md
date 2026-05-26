# Dependencies: DEL-089-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (UPDATE run 2026-05-26)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1 schema). This file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Run completed 2026-05-26. Total extracted rows: 12. All ACTIVE.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-089-01-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | PACKAGE | PKG-089 | Pig Receivers (Inlet) 3-25 | HIGH | ACTIVE |
| DEP-089-01-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0157 | SOW-0157 | HIGH | ACTIVE |
| DEP-089-01-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0158 | SOW-0158 | HIGH | ACTIVE |
| DEP-089-01-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0159 | SOW-0159 | HIGH | ACTIVE |
| DEP-089-01-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0160 | SOW-0160 | HIGH | ACTIVE |
| DEP-089-01-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | OBJ-004 — Execute vendor/EPC split | HIGH | ACTIVE |
| DEP-089-01-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | PACKAGE_REGISTER.csv | PACKAGE_REGISTER.csv (PKG-089 row) | HIGH | ACTIVE |
| DEP-089-01-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | DBM-3-25-SEC-04 | DBM 3-25 SEC-04 Inlet Pipeline Interface and Pigging | HIGH | ACTIVE |
| DEP-089-01-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-089-02_package-datasheet | Package Datasheet (DEL-089-02) | HIGH | ACTIVE |
| DEP-089-01-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-089-03_construction-work-package | Construction Work Package (DEL-089-03) | HIGH | ACTIVE |
| DEP-089-01-011 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-089-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance (DEL-089-06) | HIGH | ACTIVE |
| DEP-089-01-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-089-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package (DEL-089-04) | HIGH | ACTIVE |

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 12 |
| RETIRED | 0 |

**ANCHOR rows (ACTIVE):** 6 (1 IMPLEMENTS_NODE + 5 TRACES_TO_REQUIREMENT)
**EXECUTION rows (ACTIVE):** 6 (2 UPSTREAM PREREQUISITE + 4 DOWNSTREAM ENABLES)

**SatisfactionStatus breakdown:** TBD: 12

## Run Notes

**Run date:** 2026-05-26
**MODE:** UPDATE
**STRICTNESS:** CONSERVATIVE
**CONSUMER_CONTEXT:** NONE

**Decomposition path resolved:** DECOMPOSITION_PATH specified as `GATE-07_Final_Published_2026-05-24/` — not found at that exact location. Resolved via `_REFERENCES.md` (authoritative decomposition basis entry) to:
`/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PROJECT_DECOMP.md`
and `DELIVERABLE_REGISTER.csv` at same snapshot path. Decomposition was readable; anchor validation and label resolution performed. This is non-blocking.

**SOURCE_DOCS (AUTO):** Scanned deliverable folder. Candidate docs found:
- `Specification.md` — ANCHOR_DOC (filename contains `scope`/specification; primary for Pass 1)
- `Datasheet.md` — EXECUTION_DOC (filename contains `datasheet`; used in Pass 2 for additional evidence)
- `Guidance.md` — EXECUTION_DOC (filename contains `guidance`; used in Pass 2)
- `Procedure.md` — EXECUTION_DOC (not read; no additional dependency signals expected; consistent with other docs)
- `_CONTEXT.md`, `_REFERENCES.md`, `_STATUS.md`, `_MEMORY.md` — read-only metadata; not source docs for extraction

**ANCHOR_DOC (AUTO):** `Specification.md` selected (highest-confidence match for anchor signals; contains WBS ref, scope items, objectives, requirement IDs).

**EXECUTION_DOC_ORDER (AUTO):** `Datasheet.md`, `Guidance.md` (ordered by workflow clarity).

**Tree x DAG integrity checks:**
- IMPLEMENTS_NODE count (ACTIVE): 1 — parent anchor present. No FLOATING_NODE warning.
- AMBIGUOUS_ANCHOR check: count = 1. No warning.

**Anchor note (IMPLEMENTS_NODE):** DEP-089-01-001 targets TargetType=PACKAGE / PKG-089 rather than WBS_NODE. The decomposition assigns DEL-089-01 under PKG-089 and does not expose a separate WBS_NODE ID for this package in the readable snapshot. Using PACKAGE as TargetType is the conservative accurate representation per decomposition structure. FACT.

**OBJ-004 vs OBJ-002..OBJ-010:** OBJ-004 is emitted as a TRACES_TO_REQUIREMENT anchor because it is explicitly cited as a requirement driver in Specification R-7 and Guidance Principles with direct evidence. OBJ-002..OBJ-010 (package heuristic) are NOT emitted as ANCHOR rows under CONSERVATIVE strictness: Specification R-11 marks the linkage as ASSUMPTION/PACKAGE_HEURISTIC; CONSERVATIVE mode requires explicit identifiers.

**EXECUTION edges — scope:** Four DOWNSTREAM ENABLES edges emitted for DEL-089-02, DEL-089-03, DEL-089-04, DEL-089-06 based on explicit framing statements in Guidance.md Purpose and Specification.md Documentation. Two UPSTREAM PREREQUISITE edges emitted for PACKAGE_REGISTER.csv and DBM 3-25 SEC-04 as explicitly required source documents for multiple requirements.

**No Dependencies.csv existed before this run.** All rows are new EXTRACTED rows.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-26 — UPDATE run; STRICTNESS=CONSERVATIVE; CONSUMER_CONTEXT=NONE. Decomposition resolved via _REFERENCES.md to GATE-07_Final_Published_2026-05-24 snapshot. 12 ACTIVE rows extracted (6 ANCHOR, 6 EXECUTION). No FLOATING_NODE. No prior rows retired (first extraction).
