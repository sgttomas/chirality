# Dependencies: DEL-006-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Total rows: 7 | ACTIVE: 7 | RETIRED: 0

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-006-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0006 | Scope decision SOW-0006 — Containment Berms (WBS 03) | HIGH | ACTIVE |
| DEP-006-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-002 | Project Objective OBJ-002 — 03-25 compressor station and liquids hub scope | HIGH | ACTIVE |
| DEP-006-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | Project Objective OBJ-007 — Shared utilities and ancillary support systems | HIGH | ACTIVE |
| DEP-006-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Project Objective OBJ-008 — Civil / site / grading / containment scope | HIGH | ACTIVE |
| DEP-006-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 — Safety / drain / containment / regulatory / codes visibility | HIGH | ACTIVE |
| DEP-006-02-006 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-006-03_construction-work-package | Construction Work Package — PKG-006 Containment Berms | HIGH | ACTIVE |
| DEP-006-02-007 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-006-04_epc-civil-discipline-production-package | EPC Civil Discipline Production Package — PKG-006 Containment Berms | MEDIUM | ACTIVE |

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 7 |
| RETIRED | 0 |

Closure state breakdown (SatisfactionStatus):

| SatisfactionStatus | Count |
|---|---|
| TBD | 7 |

## Run Notes

- **Run date:** 2026-05-25
- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **Source docs:** AUTO — scanned Datasheet.md, Procedure.md, Specification.md, Guidance.md
- **Anchor doc (ANCHOR pass):** Datasheet.md (contains explicit identification, scope, and objective mapping tables)
- **Execution docs (EXECUTION pass):** Datasheet.md § Construction, Specification.md § Scope — Excluded scope
- **Decomposition path:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`
- **Decomposition status:** FOUND — used to validate SOW-0006, OBJ-002/007/008/009, DEL-006-03, DEL-006-04 identifiers
- **_REFERENCES.md:** Present and read; paths confirmed; no additional document-level dependency rows emitted (no explicit artifact-transfer statements found beyond those already captured)
- **DependencyID format:** DEP-006-02-NNN
- **Parent anchor count:** 1 (DEP-006-02-001, IMPLEMENTS_NODE → SOW-0006) — OK
- **Integrity checks:** No FLOATING_NODE; no AMBIGUOUS_ANCHOR
- **Notes on DEP-006-02-007:** Specification.md exclusion of discipline production content to DEL-006-04 implies datasheet is the upstream handoff basis; Confidence=MEDIUM per CONSERVATIVE strictness. ASSUMPTION noted in row.
- **Not extracted (CONSERVATIVE):** DEL-006-01 scope-of-work is a sibling deliverable; no explicit artifact-transfer statement found from it to this datasheet in source docs — no EXECUTION edge emitted.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — TASK + dependency-extract skill run; MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Extracted 7 rows (5 ANCHOR, 2 EXECUTION). Decomposition validated. Schema VALID.
