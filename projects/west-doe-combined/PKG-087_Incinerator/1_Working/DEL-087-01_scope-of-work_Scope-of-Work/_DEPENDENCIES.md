# Dependencies: DEL-087-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-26)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1 schema). This file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

First extraction run on 2026-05-26 produced 17 ACTIVE rows.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-087-01-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | PACKAGE | PKG-087 | Incinerator | HIGH | ACTIVE |
| DEP-087-01-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0111 | Scope Item SOW-0111 | HIGH | ACTIVE |
| DEP-087-01-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0112 | Scope Item SOW-0112 | HIGH | ACTIVE |
| DEP-087-01-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0113 | Scope Item SOW-0113 | HIGH | ACTIVE |
| DEP-087-01-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0114 | Scope Item SOW-0114 | HIGH | ACTIVE |
| DEP-087-01-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-002 | Objective OBJ-002 | HIGH | ACTIVE |
| DEP-087-01-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Objective OBJ-004 | HIGH | ACTIVE |
| DEP-087-01-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Objective OBJ-005 | HIGH | ACTIVE |
| DEP-087-01-009 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Objective OBJ-006 | HIGH | ACTIVE |
| DEP-087-01-010 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | Objective OBJ-007 | HIGH | ACTIVE |
| DEP-087-01-011 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Objective OBJ-008 | HIGH | ACTIVE |
| DEP-087-01-012 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Objective OBJ-009 | HIGH | ACTIVE |
| DEP-087-01-013 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Objective OBJ-010 | HIGH | ACTIVE |
| DEP-087-01-014 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-087-02_package-datasheet | Package Datasheet | HIGH | ACTIVE |
| DEP-087-01-015 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-087-03_construction-work-package | Construction Work Package | HIGH | ACTIVE |
| DEP-087-01-016 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-087-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance | HIGH | ACTIVE |
| DEP-087-01-017 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-087-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package | MEDIUM | ACTIVE |

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 17 |
| RETIRED | 0 |
| **Total** | **17** |

**ANCHOR rows (ACTIVE):** 13 (1 IMPLEMENTS_NODE + 12 TRACES_TO_REQUIREMENT)
**EXECUTION rows (ACTIVE):** 4 (all DOWNSTREAM HANDOVER)
**SatisfactionStatus:** All rows TBD (first extraction; no closure evidence available)

## Run Notes

**Run parameters:**
- SCOPE: DEL-087-01
- MODE: UPDATE
- STRICTNESS: CONSERVATIVE
- CONSUMER_CONTEXT: NONE
- SOURCE_DOCS: AUTO (scanned: Datasheet.md, Specification.md, Guidance.md, Procedure.md, _CONTEXT.md, _REFERENCES.md)
- ANCHOR_DOC (auto-selected): Datasheet.md (contains "datasheet" in filename; highest-confidence anchor signal)
- EXECUTION_DOC_ORDER (auto-selected): Guidance.md (contains directional/purpose language), Specification.md, Procedure.md

**Decomposition path resolution:**
- Briefed path `GATE-07_Final_Published_2026-05-24/` did not match at the literal RUN_ROOT location (`projects/west-doe-combined/GATE-07_Final_Published_2026-05-24/` — not found).
- Resolved via `_REFERENCES.md` (Authoritative Decomposition Basis section) and confirmed under `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- **Resolved decomposition path (used):** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PROJECT_DECOMP.md`
- Files consulted: `DELIVERABLE_REGISTER.csv` (row 348), `PACKAGE_REGISTER.csv` (row 64), `OBJECTIVE_SCOPE_MAP.csv` (PKG-087 rows).

**Anchor notes:**
- `DEP-087-01-001` IMPLEMENTS_NODE: parent anchor set to `PKG-087` (PACKAGE TargetType) rather than a WBS_NODE because the decomposition uses package IDs as the primary definition node for this project structure. `TargetDeliverableID` is empty; `TargetRefID` = PKG-087. This is non-standard (skill normally expects WBS_NODE) but is the best conservative fit given the decomposition structure. FACT basis: confirmed in DELIVERABLE_REGISTER.csv row 348 and PACKAGE_REGISTER.csv row 64.
- Scope items (SOW-0111..SOW-0114) and objectives (OBJ-002, OBJ-004..OBJ-010): all explicitly listed in `_CONTEXT.md` and confirmed in `DELIVERABLE_REGISTER.csv` row 348. Emitted as TRACES_TO_REQUIREMENT rows.

**Execution edge notes:**
- DEP-087-01-014..016: Guidance.md §Purpose explicitly names DEL-087-02, DEL-087-03, DEL-087-06 as downstream consumers relying on this SOW as the "controlling identity and boundary definition." Emitted as DOWNSTREAM HANDOVER. HIGH confidence.
- DEP-087-01-017: Specification.md §Scope (out-of-scope list) explicitly calls out DEL-087-04 as the deliverable that carries vendor engineering content, establishing a boundary-handover relationship. MEDIUM confidence (out-of-scope framing rather than direct "provides basis to" language, though Guidance.md further implies it).
- No UPSTREAM EXECUTION dependencies identified: Procedure.md lists _CONTEXT.md, _REFERENCES.md, _DEPENDENCIES.md, and the decomposition snapshot as prerequisites for producing this deliverable, but these are not deliverable-to-deliverable information-flow edges within the project DAG.
- No coordination-only or scheduling edges emitted per skill information-flow discipline.

**Warnings:** None. One IMPLEMENTS_NODE anchor found (count = 1; no FLOATING_NODE or AMBIGUOUS_ANCHOR warnings).

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-26 — First extraction run. dependency-extract skill, MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition resolved via _REFERENCES.md to GATE-07_Final_Published_2026-05-24. Produced 17 ACTIVE rows (13 ANCHOR, 4 EXECUTION). Schema validation: VALID.
