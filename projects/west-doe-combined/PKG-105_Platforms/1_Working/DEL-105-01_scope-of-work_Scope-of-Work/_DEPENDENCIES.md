# Dependencies: DEL-105-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-26)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register; this file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Register produced by `TASK + dependency-extract` skill run 2026-05-26. Schema v3.1. 11 rows total, all ACTIVE.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-105-01-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0261 | Scope decision SOW-0261 — Platforms (WBS 01) | HIGH | ACTIVE |
| DEP-105-01-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | Project Objective OBJ-001 — 04-25 Deepcut facility scope | MEDIUM | ACTIVE |
| DEP-105-01-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Project Objective OBJ-005 — Electrical power and infrastructure basis | MEDIUM | ACTIVE |
| DEP-105-01-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Project Objective OBJ-008 — Civil/structural/site scope | HIGH | ACTIVE |
| DEP-105-01-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 — Operability/maintainability/handoff closure | MEDIUM | ACTIVE |
| DEP-105-01-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | — | Gate 7 decomposition registers | HIGH | ACTIVE |
| DEP-105-01-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | 26020-Package_Requirements.docx row 106 heading | HIGH | ACTIVE |
| DEP-105-01-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | DBM 4-25_Deepcut_DBM.md — Governing Civil and Structural Basis | HIGH | ACTIVE |
| DEP-105-01-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-105-02_package-datasheet | Package Datasheet | HIGH | ACTIVE |
| DEP-105-01-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-105-03_construction-work-package | Construction Work Package | HIGH | ACTIVE |
| DEP-105-01-011 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-105-04_epc-structural-discipline-production-package | EPC / Structural Discipline Production Package | MEDIUM | ACTIVE |

## Run Notes

- **Run date:** 2026-05-26
- **Mode:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SCOPE:** DEL-105-01
- **RUN_ROOT:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined`
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` (confirmed present; used for anchor validation and label resolution)
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; source documents found: `Datasheet.md` (ANCHOR_DOC), `Specification.md`, `Procedure.md`, `Guidance.md`
- **ANCHOR_DOC:** `Datasheet.md` (highest-confidence anchor match — contains Identification table with explicit WBS/scope/objective references)
- **EXECUTION_DOC_ORDER:** `Procedure.md` (primary execution flow), `Specification.md`, `Guidance.md`

### Anchor resolution
- SOW-0261 confirmed in GATE-07 SCOPE_LEDGER.csv row for PKG-105 (FACT).
- OBJ-001/005/008/010 confirmed in DELIVERABLE_REGISTER.csv row for DEL-105-01. OBJ-001/005/010 carry ASSUMPTION (PACKAGE_HEURISTIC) per Datasheet.md; OBJ-008 is HIGH confidence (explicitly civil/structural/platform scope).

### Execution dependencies
- DEP-105-01-006: Gate 7 registers — SATISFIED (snapshot available and confirmed in _Decomposition).
- DEP-105-01-007: `26020-Package_Requirements.docx` row 106 heading — PENDING (binary; not transcribed). This is the blocking open input for tagged-equipment list and boundaries/exclusions (ART-21C90A2BB4; R-105-01-02; R-105-01-08).
- DEP-105-01-008: DBM — SATISFIED (available at `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`; line references confirmed in Specification.md and Datasheet.md).
- DEP-105-01-009/010/011: Downstream ENABLES edges to sibling deliverables within PKG-105 (DEL-105-02 through DEL-105-04).

### Integrity
- Parent anchor count (IMPLEMENTS_NODE, ACTIVE): 1 — OK.
- No FLOATING_NODE or AMBIGUOUS_ANCHOR warnings.

## Lifecycle Summary

| Category | Count |
|---|---|
| ACTIVE rows | 11 |
| RETIRED rows | 0 |
| ANCHOR / IMPLEMENTS_NODE (ACTIVE) | 1 |
| ANCHOR / TRACES_TO_REQUIREMENT (ACTIVE) | 4 |
| EXECUTION (ACTIVE) | 6 |
| SatisfactionStatus = SATISFIED | 2 |
| SatisfactionStatus = PENDING | 1 |
| SatisfactionStatus = TBD | 8 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-26 — First extraction run by `TASK + dependency-extract`. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition: GATE-07_Final_Published_2026-05-24 (confirmed). 11 rows ACTIVE (1 IMPLEMENTS_NODE, 4 TRACES_TO_REQUIREMENT, 6 EXECUTION). Open blocking input: DEP-105-01-007 (26020-Package_Requirements.docx row 106 slice, PENDING).
