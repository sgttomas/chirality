# Dependencies: DEL-042-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (Dependencies.csv v3.1 is canonical)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is canonical; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Dependencies.csv last updated: 2026-05-25. Schema: v3.1. Total ACTIVE rows: 16.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetID / TargetName | SatisfactionStatus | Confidence |
|---|---|---|---|---|---|---|---|---|
| DEP-042-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0043 — Control Room Building Scope Item | TBD | HIGH |
| DEP-042-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-002 | TBD | HIGH |
| DEP-042-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | TBD | HIGH |
| DEP-042-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | TBD | HIGH |
| DEP-042-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | TBD | HIGH |
| DEP-042-02-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | TBD | HIGH |
| DEP-042-02-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | TBD | HIGH |
| DEP-042-02-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | TBD | HIGH |
| DEP-042-02-009 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | TBD | HIGH |
| DEP-042-02-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-042-01_scope-of-work — Scope of Work | TBD | HIGH |
| DEP-042-02-011 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-042-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package | TBD | HIGH |
| DEP-042-02-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-042-06_epc-vendor-package-review-and-acceptance — EPC Vendor Package Review and Acceptance | TBD | HIGH |
| DEP-042-02-013 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-042-03_construction-work-package — Construction Work Package | TBD | MEDIUM |
| DEP-042-02-014 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | Final Geotechnical Report | TBD | HIGH |
| DEP-042-02-015 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | DBM-Deepcut — 4-25_Deepcut_DBM.md | SATISFIED | HIGH |
| DEP-042-02-016 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | DBM-Comp_and_Liquids — 3-25_Comp_and_Liquids_DBM.md | SATISFIED | HIGH |

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 16 |
| RETIRED | 0 |

| DependencyClass | ACTIVE count |
|---|---|
| ANCHOR | 9 |
| EXECUTION | 7 |

| SatisfactionStatus | Count (ACTIVE) |
|---|---|
| TBD | 14 |
| SATISFIED | 2 |

Parent anchor (IMPLEMENTS_NODE) count: 1 (DEP-042-02-001 → SOW-0043). Tree integrity: OK.

## Run Notes

**Run date:** 2026-05-25
**Mode:** UPDATE
**Strictness:** CONSERVATIVE
**Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`
**DECOMPOSITION_PATH (brief override):** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/GATE-07_Final_Published_2026-05-24` — path does not exist as a direct symlink; resolved to the canonical snapshot path from `_REFERENCES.md` and `_CONTEXT.md`.
**Consumer context:** NONE
**Source docs (AUTO):** Datasheet.md (ANCHOR_DOC), Procedure.md, Specification.md
**Anchor doc:** Datasheet.md (matched heuristic: filename contains "datasheet")
**Execution doc order:** Procedure.md (matched: "procedure"), Specification.md (remaining)

**Defaults applied:**
- SOURCE_DOCS=AUTO: scanned deliverable folder; excluded `_CONTEXT.md`, `_STATUS.md`, `_MEMORY.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_run_records/`.
- DOC_ROLE_MAP=DEFAULT: Datasheet.md → ANCHOR_DOC; Procedure.md, Specification.md → EXECUTION_DOC.
- STRICTNESS=CONSERVATIVE: ANCHOR rows emitted only for explicitly stated identifiers (SOW-0043, OBJ-002/004–010). No plausible-only anchors emitted.

**Assumptions recorded in rows:**
- DEP-042-02-013 (HANDOVER to DEL-042-03): Confidence=MEDIUM. Specification.md excludes CWP from this deliverable's scope, which implies it is a downstream consumer of the interface matrix; no explicit handover statement found. ASSUMPTION noted in Notes column.

**Warnings:**
- None. Parent anchor present (DEP-042-02-001). No floating node.

**Validation:**
- Schema: VALID (29 columns, 16 data rows, all DependencyIDs unique).

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First EXTRACTED run. Mode=UPDATE, Strictness=CONSERVATIVE. Decomposition: GATE-07_Final_Published_2026-05-24 (snapshot confirmed). Source docs: Datasheet.md (ANCHOR), Procedure.md, Specification.md. Emitted 9 ANCHOR rows + 7 EXECUTION rows. Schema VALID. No warnings.
