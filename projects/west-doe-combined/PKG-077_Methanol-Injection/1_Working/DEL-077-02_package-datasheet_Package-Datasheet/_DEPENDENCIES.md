# Dependencies: DEL-077-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED
**Dependency tracking mode:** EXTRACTED
**Default maturity threshold:** INITIALIZED
**Register convention:** Prefer `Dependencies.csv` when produced by `TASK + dependency-extract`; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Last extraction run: 2026-05-25 | Mode: UPDATE | Strictness: CONSERVATIVE

**Counts (ACTIVE):** 14 total — 10 ANCHOR, 4 EXECUTION

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence |
|---|---|---|---|---|---|---|---|---|
| DEP-077-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-077 | PKG-077 — Methanol Injection | HIGH |
| DEP-077-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0143 | SOW-0143 — Methanol Injection scope item | HIGH |
| DEP-077-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | OBJ-001 — 04-25 Deepcut facility process scope objective | MEDIUM |
| DEP-077-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | OBJ-004 — Supporting objective | MEDIUM |
| DEP-077-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | OBJ-005 — Supporting objective | MEDIUM |
| DEP-077-02-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | OBJ-006 — Supporting objective | MEDIUM |
| DEP-077-02-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | OBJ-007 — Supporting objective | MEDIUM |
| DEP-077-02-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | OBJ-008 — Supporting objective | MEDIUM |
| DEP-077-02-009 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | OBJ-009 — Supporting objective | MEDIUM |
| DEP-077-02-010 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | OBJ-010 — Supporting objective | MEDIUM |
| DEP-077-02-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-077-01_scope-of-work | Scope of Work — PKG-077 | HIGH |
| DEP-077-02-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-077-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package | HIGH |
| DEP-077-02-013 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-077-03_construction-work-package | Construction Work Package | MEDIUM |
| DEP-077-02-014 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | 26020-Package_Requirements.docx | 26020-Package_Requirements.docx | MEDIUM |

## Run Notes

- **Run date:** 2026-05-25
- **Mode:** UPDATE (no prior Dependencies.csv; created new register)
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **Source documents scanned (AUTO):** Datasheet.md, Specification.md, Guidance.md, Procedure.md, _CONTEXT.md
- **Anchor doc (AUTO heuristic):** Datasheet.md (filename contains "datasheet" — highest-confidence ANCHOR_DOC match)
- **Execution doc order (AUTO heuristic):** Specification.md, Guidance.md, Procedure.md, Datasheet.md
- **Decomposition path used:** `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` (resolved via _CONTEXT.md and _REFERENCES.md)
- **DECOMPOSITION_PATH param:** GATE-07_Final_Published_2026-05-24 path was provided as a parameter stub but the literal path `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/GATE-07_Final_Published_2026-05-24/` does not exist at run-root level; resolved correctly via _CONTEXT.md Decomposition Reference to `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`. No data loss; anchors validated against correct snapshot.
- **Objective anchor confidence:** Objective traces (OBJ-001 through OBJ-010) assigned MEDIUM confidence because Specification R-11 explicitly flags ASSUMPTION — association is by PACKAGE_HEURISTIC, not confirmed at deliverable-ID granularity.
- **DEL-077-01 prerequisite rationale:** Procedure.md step 1 requires reading _CONTEXT.md which establishes scope/responsibility split; Specification R-10 requires the datasheet to state the same split — content logically flows from the SOW deliverable. Explicit evidence: Specification R-10.
- **DEL-077-04 downstream rationale:** Specification § Scope — Excludes explicitly names "Vendor-internal package engineering and design (Package Vendor scope under DEL-077-04)" as out of scope for this deliverable, establishing a direct ENABLES edge.
- **DEL-077-03 downstream rationale:** Specification § Scope — Excludes explicitly names "Construction work package contents (DEL-077-03)" as out of scope; equipment tags and interface matrix produced here are required inputs to CWP.
- **26020-Package_Requirements.docx:** Binary source; TargetLocation marked "location TBD" per source convention. Specification Standards table explicitly cites it.
- **No pure coordination or structural-adjacency edges extracted.** All EXECUTION edges are information/artifact transfers with explicit evidence.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 14 |
| RETIRED | 0 |
| **Total** | **14** |

**Closure breakdown (all ACTIVE rows):**

| SatisfactionStatus | Count |
|---|---|
| TBD | 14 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First extraction run. Mode: UPDATE, Strictness: CONSERVATIVE, Decomp: GATE-07_Final_Published_2026-05-24 (resolved via _CONTEXT.md). Created Dependencies.csv (14 rows, 10 ANCHOR + 4 EXECUTION). Schema validation: VALID (29 columns, 14 data rows). No FLOATING_NODE warning (1 IMPLEMENTS_NODE present). No RETIRED rows.
