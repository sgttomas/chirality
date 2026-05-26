# Dependencies: DEL-073-03_construction-work-package — Construction Work Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` (v3.1, 12 rows) is the canonical register; this file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

12 rows extracted (all ACTIVE). Schema: v3.1, 29 columns.

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetID / TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-073-03-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | PACKAGE | PKG-073 — Amine Treating Unit | HIGH | ACTIVE |
| DEP-073-03-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | WBS_NODE | WBS-01 (Mechanical) | HIGH | ACTIVE |
| DEP-073-03-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0051 | HIGH | ACTIVE |
| DEP-073-03-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0052 | HIGH | ACTIVE |
| DEP-073-03-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0053 | HIGH | ACTIVE |
| DEP-073-03-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0054 | HIGH | ACTIVE |
| DEP-073-03-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-073-01 — Scope of Work | HIGH | ACTIVE |
| DEP-073-03-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-073-02 — Package Datasheet | HIGH | ACTIVE |
| DEP-073-03-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-073-04 — Vendor Engineered Equipment Package | HIGH | ACTIVE |
| DEP-073-03-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-073-05 — Vendor Document Turnover Package | HIGH | ACTIVE |
| DEP-073-03-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-073-06 — EPC Vendor Package Review and Acceptance | HIGH | ACTIVE |
| DEP-073-03-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-073-06 — EPC Vendor Package Review and Acceptance | HIGH | ACTIVE |

## Run Notes

- **Run date:** 2026-05-25
- **Mode:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned: Datasheet.md (ANCHOR_DOC), Specification.md, Procedure.md, Guidance.md, _CONTEXT.md
- **DOC_ROLE_MAP:** DEFAULT — Datasheet.md selected as ANCHOR_DOC (filename contains "datasheet"); Specification.md and Procedure.md are primary EXECUTION_DOCs
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — resolved from `_CONTEXT.md` Decomposition Reference; path exists and was used to validate anchor identifiers.
- **[NOTE] DECOMPOSITION_PATH in task brief** pointed to `GATE-07_Final_Published_2026-05-24/` under RUN_ROOT but the directory does not exist there; resolved correctly via `_CONTEXT.md` reference to `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- **Anchor validation:** PKG-073 confirmed in PACKAGE_REGISTER.csv; DEL-073-01 through DEL-073-06 all confirmed in DELIVERABLE_REGISTER.csv; WBS-01 confirmed in PACKAGE_REGISTER row PKG-073.
- **SOW items:** SOW-0051..SOW-0054 are stated explicitly in _CONTEXT.md and Datasheet.md; emitted as TRACES_TO_REQUIREMENT rows per CONSERVATIVE strictness.
- **Objective associations (OBJ-001, OBJ-003..OBJ-010):** These are present in _CONTEXT.md but are flagged as `ASSUMPTION: package-heuristic mapping` (OBJECTIVE_ASSOCIATION_MODE: PACKAGE_HEURISTIC). Under CONSERVATIVE strictness, heuristic-mode objective associations are NOT emitted as TRACES_TO_REQUIREMENT rows; they are advisory metadata only.
- **DEL-073-06 appears as both UPSTREAM (DEP-073-03-011) and DOWNSTREAM (DEP-073-03-012):** This is correct and reflects two distinct relationships — DEL-073-03 requires DEL-073-06 acceptance of vendor docs before the commissioning handoff (upstream input), and DEL-073-03 also produces the MC evidence package that DEL-073-06 formalises acceptance of (downstream handover). These are non-circular information flows per the source evidence.
- **Binary sources not accessible:** `26020-Package_Requirements.docx` (package heading 27) and `26020-Packages_Interfaces_4_export.xlsx` are binary; no clause-level dependency signal extracted from these in this run (location TBD per Specification.md Standards table).
- **[WARNING] FLOATING_NODE check:** One IMPLEMENTS_NODE row (DEP-073-03-001) is ACTIVE with TargetType=PACKAGE. This satisfies the parent anchor requirement (anchors to PKG-073); no FLOATING_NODE warning triggered. Note: TargetType=PACKAGE (not WBS_NODE) is appropriate because the canonical parent is a decomposition package node, not a generic WBS entry.

## Lifecycle Summary

| Dimension | Count |
|---|---|
| ACTIVE rows | 12 |
| RETIRED rows | 0 |
| ANCHOR rows (ACTIVE) | 6 |
| EXECUTION rows (ACTIVE) | 6 |
| IMPLEMENTS_NODE (ACTIVE) | 1 |
| TRACES_TO_REQUIREMENT (ACTIVE) | 5 |
| SatisfactionStatus = PENDING | 5 |
| SatisfactionStatus = TBD | 7 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract skill run; MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition path resolved to GATE-07_Final_Published_2026-05-24 snapshot. 12 rows extracted (6 ANCHOR, 6 EXECUTION), all ACTIVE. Schema validation: VALID (29 columns, 12 data rows). No prior rows to retire.
