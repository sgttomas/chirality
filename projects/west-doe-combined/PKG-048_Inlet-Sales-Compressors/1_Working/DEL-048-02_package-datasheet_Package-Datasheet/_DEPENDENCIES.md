# Dependencies: DEL-048-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (Dependencies.csv v3.1 is authoritative)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register; this file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Dependencies.csv produced by `TASK + dependency-extract` run 2026-05-25. Total ACTIVE rows: 19.

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-048-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-048 — Inlet / Sales Compressors | HIGH | ACTIVE |
| DEP-048-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0115 | HIGH | ACTIVE |
| DEP-048-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0116 | HIGH | ACTIVE |
| DEP-048-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0117 | HIGH | ACTIVE |
| DEP-048-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0118 | HIGH | ACTIVE |
| DEP-048-02-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | MEDIUM | ACTIVE |
| DEP-048-02-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-003 | MEDIUM | ACTIVE |
| DEP-048-02-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | MEDIUM | ACTIVE |
| DEP-048-02-009 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | MEDIUM | ACTIVE |
| DEP-048-02-010 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | MEDIUM | ACTIVE |
| DEP-048-02-011 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | MEDIUM | ACTIVE |
| DEP-048-02-012 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | MEDIUM | ACTIVE |
| DEP-048-02-013 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | MEDIUM | ACTIVE |
| DEP-048-02-014 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | MEDIUM | ACTIVE |
| DEP-048-02-015 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | DBM-Deepcut/4-25_Deepcut_DBM.md | HIGH | ACTIVE |
| DEP-048-02-016 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | GATE-07 Final Published PROJECT_DECOMP snapshot | HIGH | ACTIVE |
| DEP-048-02-017 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-048-04 Vendor Engineered Equipment Package | HIGH | ACTIVE |
| DEP-048-02-018 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-048-06 EPC Vendor Package Review and Acceptance | HIGH | ACTIVE |
| DEP-048-02-019 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | INTERFACE | PACKAGE | PKG-049 — Sales Gas Booster Compressors | MEDIUM | ACTIVE |

## Run Notes

- **Run date:** 2026-05-25
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, `_CONTEXT.md`, `_REFERENCES.md`
- **ANCHOR_DOC:** `Datasheet.md` (heuristic match on `datasheet` keyword)
- **EXECUTION_DOC_ORDER:** `Procedure.md`, `Specification.md`, `Guidance.md`, `Datasheet.md`
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — confirmed reachable; DELIVERABLE_REGISTER.csv and PACKAGE_REGISTER.csv consulted for anchor validation and target label resolution.
- **NOTE — DECOMPOSITION_PATH supplied as `GATE-07_Final_Published_2026-05-24` in task parameters:** The path `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/GATE-07_Final_Published_2026-05-24/` referenced in the task parameters did not exist at that location. The correct path under `_Decomposition/PROJECT_DECOMP/_GateSnapshots/` was used instead; the discrepancy is recorded here per skill contract.
- **Objective trace rows (DEP-048-02-006 through -014):** Marked MEDIUM confidence and ASSUMPTION because the objective association is package-grouped heuristic (per brief `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC`). Awaits human ruling per Conflict C-048-02-009 in `Guidance.md`.
- **PKG-049 interface row (DEP-048-02-019):** TargetDeliverableID left blank; source names only "downstream sales-gas booster" (system/package level), not a specific DEL-049 deliverable. `TargetPackageID=PKG-049` resolved from PACKAGE_REGISTER.
- **inaccessible sources:** `26020-Package_Requirements.docx` heading 3 and `Bid Docs/Budgetary/RFQ/Bid Docs/26020-01-PT-RFQ-12-003-Inlet Sales Comp.docx` are not locally accessible as Markdown. No dependency rows were emitted based solely on those sources; fields dependent on them are marked `location TBD` in the datasheet.
- **Tree x DAG integrity:** Exactly one IMPLEMENTS_NODE anchor (DEP-048-02-001) found — no FLOATING_NODE or AMBIGUOUS_ANCHOR warnings.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 19 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 19 |

| DependencyClass | ACTIVE count |
|---|---|
| ANCHOR | 14 |
| EXECUTION | 5 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full two-pass extraction run. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition snapshot GATE-07_Final_Published_2026-05-24 used. 19 ACTIVE rows produced (14 ANCHOR, 5 EXECUTION). No RETIRED rows. Schema validated VALID.
