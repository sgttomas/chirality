# Dependencies: DEL-076-05_vendor-document-turnover-package — Vendor Document Turnover Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1 schema). This file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Register produced by `dependency-extract` skill run on 2026-05-25.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | Target | Status |
|---|---|---|---|---|---|---|---|
| DEP-076-05-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-076 (Lube Oil Supply) | ACTIVE |
| DEP-076-05-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0135 | ACTIVE |
| DEP-076-05-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0136 | ACTIVE |
| DEP-076-05-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0137 | ACTIVE |
| DEP-076-05-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0138 | ACTIVE |
| DEP-076-05-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-076-01_scope-of-work | ACTIVE |
| DEP-076-05-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-076-02_package-datasheet | ACTIVE |
| DEP-076-05-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DELIVERABLE | DEL-076-04_vendor-engineered-equipment-package | ACTIVE |
| DEP-076-05-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-076-06_epc-vendor-package-review-and-acceptance | ACTIVE |

**ANCHOR rows:** 5 (1 IMPLEMENTS_NODE + 4 TRACES_TO_REQUIREMENT)
**EXECUTION rows:** 4 (3 UPSTREAM + 1 DOWNSTREAM)
**Total ACTIVE:** 9 | **RETIRED:** 0

## Run Notes

- **Run date:** 2026-05-25
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; used Datasheet.md (ANCHOR_DOC), Procedure.md, Specification.md, Guidance.md (EXECUTION_DOCS). Excluded _DEPENDENCIES.md, _REFERENCES.md, _STATUS.md, _CONTEXT.md, _MEMORY.md, _run_records/.
- **ANCHOR_DOC:** Datasheet.md (selected as highest-confidence anchor doc; filename contains "datasheet"; matches DEFAULT heuristic).
- **EXECUTION_DOC_ORDER:** Procedure.md, Specification.md, Guidance.md.
- **DECOMPOSITION_PATH used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` — snapshot located; anchors and target IDs validated against this file.
- **DECOMPOSITION_PATH in brief:** `GATE-07_Final_Published_2026-05-24` — path provided in brief did not resolve directly; actual snapshot found at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`. Used GATE-07 snapshot for all anchor and target resolution.
- **Parent anchor check:** 1 IMPLEMENTS_NODE row (DEP-076-05-001) — no FLOATING_NODE warning.
- **OBJ trace anchors:** Objectives (OBJ-001, OBJ-004..OBJ-010) listed in Datasheet.md `SupportsObjectives` are marked `ASSUMPTION: PACKAGE_HEURISTIC` in the source; not extracted as TRACES_TO_REQUIREMENT rows under CONSERVATIVE mode.
- **DEP-076-05-008 note:** ASSUMPTION — DEL-076-04 interface is implied by the Specification exclusion clause ("Engineering, design, and physical fabrication covered by DEL-076-04") rather than a direct prerequisite statement. Confidence set to MEDIUM.
- **Project hazardous-material list:** Referenced in sources (DBM 3-25 line 507) but no stable deliverable/package ID available; not emitted as a dependency row (no artifact transfer target can be resolved). Recorded here as TBD.
- **Project document control procedure:** Referenced in sources but no stable deliverable/package ID available; not emitted. Recorded here as TBD.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 9 |
| RETIRED | 0 |
| **Total** | **9** |

| SatisfactionStatus | Count |
|---|---|
| TBD | 5 (ANCHOR rows — closure not applicable) |
| PENDING | 4 (EXECUTION rows — not yet satisfied) |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full two-pass extraction run by `dependency-extract` skill. MODE=UPDATE, STRICTNESS=CONSERVATIVE. 9 ACTIVE rows written to Dependencies.csv (v3.1). Schema validation: VALID (29 columns, 9 data rows). Decomposition path: GATE-07_Final_Published_2026-05-24 snapshot.
