# Dependencies: DEL-058-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` generated 2026-05-25 by TASK + dependency-extract (MODE=UPDATE, STRICTNESS=CONSERVATIVE).

**ACTIVE row counts:**

| DependencyClass | AnchorType / DependencyType | Direction | Count |
|---|---|---|---|
| ANCHOR | IMPLEMENTS_NODE | UPSTREAM | 1 |
| ANCHOR | TRACES_TO_REQUIREMENT (SOW) | UPSTREAM | 4 |
| ANCHOR | TRACES_TO_REQUIREMENT (OBJ) | UPSTREAM | 8 |
| EXECUTION | PREREQUISITE | UPSTREAM | 1 |
| EXECUTION | ENABLES | DOWNSTREAM | 3 |
| EXECUTION | INTERFACE (DOCUMENT) | UPSTREAM | 3 |
| **Total ACTIVE** | | | **20** |

**Compact register:**

| DependencyID | Class | AnchorType / DepType | Dir | TargetType | TargetRefID / TargetDeliverableID | TargetName |
|---|---|---|---|---|---|---|
| DEP-058-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | WBS_NODE | PKG-058 | Medium Pressure Flash Feed Separator |
| DEP-058-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | SOW-0139 | SOW-0139 — MPFF package as distinct flat project package |
| DEP-058-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | SOW-0140 | SOW-0140 — MPFF basic scope |
| DEP-058-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | SOW-0141 | SOW-0141 — MPFF major included equipment |
| DEP-058-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | SOW-0142 | SOW-0142 — MPFF scope notes and open items |
| DEP-058-02-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | OBJ-001 | OBJ-001 — 04-25 Deepcut facility scope |
| DEP-058-02-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | OBJ-004 | OBJ-004 — Vendor/EPC package execution model |
| DEP-058-02-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | OBJ-005 | OBJ-005 — Electrical power basis and interfaces |
| DEP-058-02-009 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | OBJ-006 | OBJ-006 — Controls / instrumentation / fire-gas |
| DEP-058-02-010 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | OBJ-007 | OBJ-007 — Shared utilities / heat medium / methanol |
| DEP-058-02-011 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | OBJ-008 | OBJ-008 — Civil / structural / site / foundations |
| DEP-058-02-012 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | OBJ-009 | OBJ-009 — Safety / relief / flare / regulatory |
| DEP-058-02-013 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | OBJ-010 | OBJ-010 — Operability / vendor docs / turnover |
| DEP-058-02-014 | EXECUTION | PREREQUISITE | UPSTREAM | DELIVERABLE | DEL-058-01_scope-of-work | Scope of Work |
| DEP-058-02-015 | EXECUTION | ENABLES | DOWNSTREAM | DELIVERABLE | DEL-058-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package |
| DEP-058-02-016 | EXECUTION | ENABLES | DOWNSTREAM | DELIVERABLE | DEL-058-05_vendor-document-turnover-package | Vendor Document Turnover Package |
| DEP-058-02-017 | EXECUTION | ENABLES | DOWNSTREAM | DELIVERABLE | DEL-058-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance |
| DEP-058-02-018 | EXECUTION | INTERFACE | UPSTREAM | DOCUMENT | — | DBM-Deepcut 4-25_Deepcut_DBM.md |
| DEP-058-02-019 | EXECUTION | INTERFACE | UPSTREAM | DOCUMENT | — | 26020-Package_Requirements.docx heading 13 |
| DEP-058-02-020 | EXECUTION | INTERFACE | UPSTREAM | DOCUMENT | — | 26020-Packages_Interfaces_4_export.xlsx row 71 |

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — found and read. Decomposition path in task invocation referenced `GATE-07_Final_Published_2026-05-24` which does not exist at the `RUN_ROOT` level; actual path resolved via `_CONTEXT.md §Decomposition Reference`.
- **SOURCE_DOCS:** AUTO — scanned deliverable folder. ANCHOR_DOC: `Datasheet.md` (contains `datasheet` keyword, matches ANCHOR_DOC heuristic). EXECUTION_DOCS (in order): `Procedure.md`, `Specification.md`, `Guidance.md`.
- **ANCHOR_DOC:** `Datasheet.md` (auto-selected; highest-confidence ANCHOR_DOC heuristic match).
- **_REFERENCES.md:** Present and read; used to resolve document pointers.
- **[WARNING] MISSING_DECOMPOSITION_PATH_AS_SUPPLIED:** The `DECOMPOSITION_PATH` parameter `GATE-07_Final_Published_2026-05-24` was supplied as a top-level run root path but does not exist there. Path was resolved from `_CONTEXT.md §Decomposition Reference` instead. No data loss; anchors validated against the correct snapshot.
- **DEP-058-02-014 (prerequisite DEL-058-01):** Procedure explicitly labels sibling deliverables as "advisory only; this procedure does not cross-edit." Dependency captured at MEDIUM confidence, ASSUMPTION label in Notes, as the datasheet logically requires the SOW scope boundary to be settled before final issue — but Procedure does not make it a hard blocking prerequisite.
- **DEP-058-02-019 / DEP-058-02-020:** Source documents not locally accessible as markdown. `SatisfactionStatus=PENDING` to flag that these document inputs are unresolved gaps.
- **Tree x DAG integrity:** One IMPLEMENTS_NODE parent anchor found (DEP-058-02-001, PKG-058). No FLOATING_NODE warning. No AMBIGUOUS_ANCHOR warning.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 20 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 18 |
| PENDING | 2 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full two-pass dependency extraction run (TASK + dependency-extract). MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition: GATE-07_Final_Published_2026-05-24 (resolved via _CONTEXT.md). 20 ACTIVE rows emitted (13 ANCHOR, 7 EXECUTION). No prior Dependencies.csv; created fresh. Warnings: MISSING_DECOMPOSITION_PATH_AS_SUPPLIED (path resolved from _CONTEXT.md; no data impact).
