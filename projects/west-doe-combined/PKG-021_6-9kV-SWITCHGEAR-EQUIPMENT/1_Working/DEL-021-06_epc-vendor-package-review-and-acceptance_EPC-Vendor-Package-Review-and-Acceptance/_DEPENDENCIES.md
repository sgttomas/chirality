# Dependencies: DEL-021-06_epc-vendor-package-review-and-acceptance — EPC Vendor Package Review and Acceptance

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Dependencies.csv generated 2026-05-25. Total rows: 14. ACTIVE: 14. RETIRED: 0.

| DependencyID | Class | AnchorType / DependencyType | Direction | TargetType | Target | Status |
|---|---|---|---|---|---|---|
| DEP-021-06-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | WBS_NODE | SOW-0022 — 6.9kV SWITCHGEAR EQUIPMENT | ACTIVE |
| DEP-021-06-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | OBJ-001 — 04-25 Deepcut facility scope | ACTIVE |
| DEP-021-06-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | OBJ-004 — Vendor-owned package with EPC integration review | ACTIVE |
| DEP-021-06-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | OBJ-005 — Facility electrical power basis and switchgear integration | ACTIVE |
| DEP-021-06-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | OBJ-006 — Controls and instrumentation integration | ACTIVE |
| DEP-021-06-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | OBJ-008 — Civil/structural/site scope | ACTIVE |
| DEP-021-06-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | OBJ-009 — Safety/regulatory/codes requirements | ACTIVE |
| DEP-021-06-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | OBJ-010 — Operability/maintainability/turnover/handoff | ACTIVE |
| DEP-021-06-009 | EXECUTION | PREREQUISITE | UPSTREAM | DELIVERABLE | DEL-021-01 — EPC Scope of Work | ACTIVE |
| DEP-021-06-010 | EXECUTION | PREREQUISITE | UPSTREAM | DELIVERABLE | DEL-021-02 — EPC Package Datasheet | ACTIVE |
| DEP-021-06-011 | EXECUTION | PREREQUISITE | UPSTREAM | DELIVERABLE | DEL-021-03 — EPC Construction Work Package | ACTIVE |
| DEP-021-06-012 | EXECUTION | PREREQUISITE | UPSTREAM | DELIVERABLE | DEL-021-04 — Vendor Engineered Equipment Package | ACTIVE |
| DEP-021-06-013 | EXECUTION | PREREQUISITE | UPSTREAM | DELIVERABLE | DEL-021-05 — Vendor Document Turnover Package | ACTIVE |
| DEP-021-06-014 | EXECUTION | PREREQUISITE | UPSTREAM | DOCUMENT | DBM-Deepcut 4-25_Deepcut_DBM.md (lines 2935, 2973, 2985) | ACTIVE |

## Lifecycle Summary

- ACTIVE: 14
- RETIRED: 0
- ANCHOR rows (ACTIVE): 8 (1 IMPLEMENTS_NODE + 7 TRACES_TO_REQUIREMENT)
- EXECUTION rows (ACTIVE): 6
- SatisfactionStatus breakdown: TBD=7, PENDING=6, SATISFIED=1

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned: Datasheet.md, Procedure.md, Guidance.md, Specification.md (anchor doc: Datasheet.md; execution docs: Procedure.md, Specification.md, Guidance.md)
- **DECOMPOSITION_PATH:** /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/ — used to validate anchors and resolve canonical labels for SOW-0022 and OBJ IDs.
- **ANCHOR_DOC:** Datasheet.md (contains `CoversScopeItems: SOW-0022` and `SupportsObjectives` — highest-confidence anchor signal).
- **Pass 1 (ANCHOR):** 1 IMPLEMENTS_NODE (SOW-0022) + 7 TRACES_TO_REQUIREMENT (OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010). All confirmed in GATE-07 DELIVERABLE_REGISTER.csv and SCOPE_LEDGER.csv.
- **Pass 2 (EXECUTION):** 5 sibling-deliverable PREREQUISITE edges (DEL-021-01 through DEL-021-05) extracted from explicit prerequisite table in Procedure.md and confirmed in Specification.md scope section. 1 DOCUMENT PREREQUISITE edge for DBM-Deepcut facility electrical design basis (Procedure.md prerequisite row 6, marked OK).
- **SatisfactionStatus for sibling prerequisite edges:** Set to PENDING (documents must reach stable state before acceptance proceeds). DBM-Deepcut set to SATISFIED (locally accessible per Procedure.md status check).
- **Objective traces:** OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010 heuristically attributed via PACKAGE_HEURISTIC in Datasheet.md but confirmed in DELIVERABLE_REGISTER.csv row for DEL-021-06; emitted as EXPLICIT with HIGH confidence.
- **No downstream execution edges extracted:** No source document states an explicit information/artifact output that this deliverable produces for consumption by another specific deliverable. Structural adjacency (e.g., "this feeds construction") is not emitted as an edge per skill rules.
- **Conflict Table note:** Guidance.md CONF-021-06-003 noted that _DEPENDENCIES.md previously declared no upstream edges. This run resolves that gap by extracting the explicit prerequisite edges from Procedure.md and Specification.md.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract skill run. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition: GATE-07_Final_Published_2026-05-24 (confirmed). 14 rows extracted (8 ANCHOR, 6 EXECUTION). All ACTIVE. No RETIRED rows (first extraction run). Warnings: none.
