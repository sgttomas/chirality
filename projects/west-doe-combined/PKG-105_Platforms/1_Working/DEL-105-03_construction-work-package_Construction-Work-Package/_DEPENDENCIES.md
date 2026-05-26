# Dependencies: DEL-105-03_construction-work-package — Construction Work Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-26)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1 schema); this file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` produced by `TASK + dependency-extract` on 2026-05-26. Schema version v3.1. 12 rows total; 12 ACTIVE.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-105-03-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0261 | Scope decision SOW-0261 — Platforms (WBS 01) | HIGH | ACTIVE |
| DEP-105-03-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | Project Objective OBJ-001 — 04-25 Deepcut facility scope | HIGH | ACTIVE |
| DEP-105-03-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Project Objective OBJ-005 — Electrical power and lighting basis | HIGH | ACTIVE |
| DEP-105-03-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Project Objective OBJ-008 — Civil/structural/site scope | HIGH | ACTIVE |
| DEP-105-03-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 — Operability/maintainability/turnover/handoff closure | HIGH | ACTIVE |
| DEP-105-03-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-105-01_scope-of-work | Scope of Work | HIGH | ACTIVE |
| DEP-105-03-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-105-02_package-datasheet | Package Datasheet | HIGH | ACTIVE |
| DEP-105-03-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-105-04_epc-structural-discipline-production-package | EPC / Structural Discipline Production Package | HIGH | ACTIVE |
| DEP-105-03-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | — | Gate 7 decomposition registers | HIGH | ACTIVE |
| DEP-105-03-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | — | Workbook Packages row ID# 105 | HIGH | ACTIVE |
| DEP-105-03-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | Project 3D model snapshot (tie-in confirmation) | HIGH | ACTIVE |
| DEP-105-03-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | Integrated P&ID set (tie-in confirmation) | HIGH | ACTIVE |

## Run Notes

- **Run date:** 2026-05-26
- **Mode:** UPDATE (no prior Dependencies.csv; created fresh)
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` (resolved from `_REFERENCES.md` Authoritative Decomposition Basis; directory exists and validated)
- **DECOMPOSITION_PATH parameter:** GATE-07_Final_Published_2026-05-24 (supplied via RUN_ROOT reference; note: the path supplied in the task invocation (`GATE-07_Final_Published_2026-05-24` under RUN_ROOT) did not exist as a top-level directory; resolved to the equivalent path under `_Decomposition/PROJECT_DECOMP/_GateSnapshots/`)
- **Source documents scanned (AUTO):** `Datasheet.md`, `Procedure.md`, `Specification.md`, `Guidance.md` — all present; `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` read for context
- **ANCHOR_DOC (AUTO):** `Datasheet.md` (contains identification table with WBS Ref, ScopeItem, Objectives — highest anchor signal)
- **EXECUTION_DOC_ORDER (AUTO):** `Procedure.md` (primary workflow signal), `Specification.md` (requirements), `Guidance.md` (principles/considerations)
- **_REFERENCES.md:** present; used to resolve decomposition path and workbook source pointer
- **Anchor pass result:** 1 IMPLEMENTS_NODE (SOW-0261) + 4 TRACES_TO_REQUIREMENT (OBJ-001, OBJ-005, OBJ-008, OBJ-010). No FLOATING_NODE warning — parent anchor found.
- **Execution pass result:** 7 EXECUTION rows (3 DELIVERABLE prerequisites, 2 DOCUMENT interfaces, 2 DOCUMENT prerequisites for TBD 3D model / P&ID)
- **TBD items:** Project 3D model snapshot ID and integrated P&ID set revision identifier are both TBD (location TBD) per Procedure.md Prerequisites — recorded as PENDING EXECUTION rows rather than omitted.
- **Conflict table items:** CFT-105-03-001, CFT-105-03-002, CFT-105-03-003 from Guidance.md are noted but do not affect dependency extraction; no new conflicts introduced.
- **Assumption boundary:** DEL-105-01, DEL-105-02, and DEL-105-04 prerequisites are ASSUMPTION-flagged in Notes per Procedure.md (handoff implied by deliverable ordering; not declared in _DEPENDENCIES.md during PREPARATION).

## Lifecycle Summary

| Dimension | Count |
|---|---|
| Total rows | 12 |
| ACTIVE | 12 |
| RETIRED | 0 |
| ANCHOR / IMPLEMENTS_NODE | 1 |
| ANCHOR / TRACES_TO_REQUIREMENT | 4 |
| EXECUTION | 7 |
| SatisfactionStatus = TBD | 8 |
| SatisfactionStatus = PENDING | 3 |
| SatisfactionStatus = SATISFIED | 2 |
| Confidence = HIGH | 12 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-26 — dependency-extract skill run; MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE; decomposition path resolved to GATE-07_Final_Published_2026-05-24; 12 rows extracted (5 ANCHOR, 7 EXECUTION); all ACTIVE; Dependencies.csv created (v3.1 schema, 29 required columns).
