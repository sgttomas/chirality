# Dependencies: DEL-029-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED
**Dependency tracking mode:** EXTRACTED (updated from DECLARED — 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` generated 2026-05-25 by `TASK + dependency-extract` (MODE=UPDATE, STRICTNESS=CONSERVATIVE).

**Row counts:** 17 total — 17 ACTIVE, 0 RETIRED.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-029-01-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0030 | SOW-0030 — PKG-029 Scope Item (WBS 01) | HIGH | ACTIVE |
| DEP-029-01-002 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | PACKAGE | PKG-029 | PKG-029 — Transformer TXP-8600-1 | HIGH | ACTIVE |
| DEP-029-01-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | OBJ-001 — Project Objective | MEDIUM | ACTIVE |
| DEP-029-01-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | OBJ-004 — Project Objective | MEDIUM | ACTIVE |
| DEP-029-01-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | OBJ-005 — Project Objective | MEDIUM | ACTIVE |
| DEP-029-01-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | OBJ-006 — Project Objective | MEDIUM | ACTIVE |
| DEP-029-01-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | OBJ-008 — Project Objective | MEDIUM | ACTIVE |
| DEP-029-01-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | OBJ-009 — Project Objective | MEDIUM | ACTIVE |
| DEP-029-01-009 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | OBJ-010 — Project Objective | MEDIUM | ACTIVE |
| DEP-029-01-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | Gate 7 PACKAGE_REGISTER.csv | HIGH | ACTIVE |
| DEP-029-01-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | Gate 7 INTERFACE_REGISTER.csv | HIGH | ACTIVE |
| DEP-029-01-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | _Sources/DBM-Deepcut/4-25_Deepcut_DBM.md | HIGH | ACTIVE |
| DEP-029-01-013 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-029-02_package-datasheet | Package Datasheet (DEL-029-02) | HIGH | ACTIVE |
| DEP-029-01-014 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-029-03_construction-work-package | Construction Work Package (DEL-029-03) | HIGH | ACTIVE |
| DEP-029-01-015 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-029-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package (DEL-029-04) | HIGH | ACTIVE |
| DEP-029-01-016 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-029-05_vendor-document-turnover-package | Vendor Document Turnover Package (DEL-029-05) | HIGH | ACTIVE |
| DEP-029-01-017 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-029-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance (DEL-029-06) | HIGH | ACTIVE |

## Run Notes

- **Run date:** 2026-05-25
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned: `Specification.md` (ANCHOR_DOC + EXECUTION_DOC), `Datasheet.md` (EXECUTION_DOC), `Guidance.md` (EXECUTION_DOC, supporting context), `_CONTEXT.md` (identity), `_REFERENCES.md` (reference resolution)
- **ANCHOR_DOC selected:** `Specification.md` (contains explicit WBS, scope-item, objective, and requirement references)
- **DECOMPOSITION_PATH used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — FOUND; used to confirm SOW-0030, PKG-029, and objective IDs
- **`_REFERENCES.md` used:** Yes — to resolve Gate 7 register paths and source document locations

**Pass 1 — Anchor (Tree):**
- One canonical scope-item anchor emitted: DEP-029-01-001 (IMPLEMENTS_NODE → SOW-0030, WBS_NODE). SOW-0030 confirmed in SCOPE_LEDGER.csv.
- One package-level anchor emitted: DEP-029-01-002 (IMPLEMENTS_NODE → PKG-029, PACKAGE). Per skill method, two IMPLEMENTS_NODE rows are present (SOW-0030 and PKG-029); the SOW-0030 row is the canonical decomposition node anchor; the PKG-029 row captures the package-level anchor for completeness.
  - [WARNING] AMBIGUOUS_ANCHOR: Two IMPLEMENTS_NODE rows present (SOW-0030 node + PKG-029 package). The SOW-0030 row (DEP-029-01-001) is the canonical Tree anchor; DEP-029-01-002 is supplementary. Both are retained with Notes explaining the distinction. Downstream aggregation should treat DEP-029-01-001 as the primary anchor.
- Seven objective trace anchors emitted (DEP-029-01-003 through DEP-029-01-009) — all marked ASSUMPTION per OBJECTIVE_ASSOCIATION_MODE = PACKAGE_HEURISTIC (confirmed in Datasheet and Guidance).

**Pass 2 — Execution (DAG):**
- Three UPSTREAM PREREQUISITE document edges extracted: Gate 7 PACKAGE_REGISTER, INTERFACE_REGISTER, and DBM-Deepcut source — all explicitly cited in Specification requirements (SOW-029-01 through SOW-029-09) as verification sources.
- Five DOWNSTREAM ENABLES deliverable edges extracted: DEL-029-02 through DEL-029-06 — all explicitly named in Specification scope section as downstream consumers of this deliverable's scope boundaries, assumptions, TBDs, and open items.
- No pure-coordination or structural-adjacency edges emitted.

**Warnings:**
- [WARNING] AMBIGUOUS_ANCHOR: Two IMPLEMENTS_NODE rows present — see Pass 1 notes above.
- Objective traces (DEP-029-01-003 through -009) carry ASSUMPTION labels; human confirmation of deliverable-level objective mapping is pending.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 17 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| SATISFIED | 2 (DEP-029-01-001, DEP-029-01-002 — decomposition anchors accepted at Gate 7) |
| SATISFIED | 2 (DEP-029-01-010, DEP-029-01-011 — Gate 7 register documents accepted) |
| SATISFIED | 1 (DEP-029-01-012 — DBM-Deepcut source available and used) |
| TBD | 12 (objective traces + downstream enables — pending deliverable progress) |

**Closure-state breakdown:**
- ANCHOR rows: 9 total (1 canonical IMPLEMENTS_NODE SOW-0030, 1 supplementary IMPLEMENTS_NODE PKG-029, 7 TRACES_TO_REQUIREMENT objectives)
- EXECUTION rows: 8 total (3 UPSTREAM PREREQUISITE documents, 5 DOWNSTREAM ENABLES deliverables)

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First extraction run. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition found at GATE-07_Final_Published_2026-05-24. 17 ACTIVE rows written (9 ANCHOR, 8 EXECUTION). [WARNING] AMBIGUOUS_ANCHOR: two IMPLEMENTS_NODE rows; see Run Notes.
