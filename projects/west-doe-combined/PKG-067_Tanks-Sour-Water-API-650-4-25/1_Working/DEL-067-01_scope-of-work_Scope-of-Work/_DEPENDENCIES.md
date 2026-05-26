# Dependencies: DEL-067-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Register extracted 2026-05-25 (MODE=UPDATE, STRICTNESS=CONSERVATIVE). 14 rows total; 14 ACTIVE.

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetID / TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-067-01-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | PACKAGE | PKG-067 — Tanks, Sour Water (API 650) 4-25 | HIGH | ACTIVE |
| DEP-067-01-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0225 | HIGH | ACTIVE |
| DEP-067-01-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0226 | HIGH | ACTIVE |
| DEP-067-01-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0227 | HIGH | ACTIVE |
| DEP-067-01-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0228 | HIGH | ACTIVE |
| DEP-067-01-006 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-067-02_package-datasheet | HIGH | ACTIVE |
| DEP-067-01-007 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-067-03_construction-work-package | HIGH | ACTIVE |
| DEP-067-01-008 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-067-04_vendor-engineered-equipment-package | HIGH | ACTIVE |
| DEP-067-01-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-067-05_vendor-document-turnover-package | MEDIUM | ACTIVE |
| DEP-067-01-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-067-06_epc-vendor-package-review-and-acceptance | MEDIUM | ACTIVE |
| DEP-067-01-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | PACKAGE | PKG-060 — Produced Water Transfer Pumps | HIGH | ACTIVE |
| DEP-067-01-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | GATE-07_Final_Published_2026-05-24 (PROJECT_DECOMP snapshot) | HIGH | ACTIVE |
| DEP-067-01-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | 26020-Package_Requirements.docx (heading 26020-01-PT-19-005) | HIGH | ACTIVE |
| DEP-067-01-014 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | 4-25_Deepcut_DBM.md (Produced Water section) | HIGH | ACTIVE |

## Run Notes

**Run parameters:**
- SCOPE: DEL-067-01
- RUN_ROOT: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined`
- DECOMPOSITION_PATH: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` (explicit; confirmed present)
- SOURCE_DOCS: AUTO — scanned deliverable folder; sources used: `Specification.md` (ANCHOR_DOC by filename heuristic), `Datasheet.md`, `Guidance.md`, `Procedure.md`, `_CONTEXT.md`
- DOC_ROLE_MAP: DEFAULT
- ANCHOR_DOC: `Specification.md` (highest-confidence match; contains "scope", traceability fields, requirement IDs)
- EXECUTION_DOC_ORDER: `Guidance.md`, `Procedure.md`, `Datasheet.md`
- MODE: UPDATE
- STRICTNESS: CONSERVATIVE
- CONSUMER_CONTEXT: NONE

**Decomposition validation:** GATE-07 snapshot confirmed present. PKG-067 resolved from PACKAGE_REGISTER.csv row 94. DEL-067-01 confirmed in DELIVERABLE_REGISTER.csv row 528. Scope items SOW-0225–SOW-0228 taken from DELIVERABLE_REGISTER row 528 directly. Downstream deliverable IDs DEL-067-02 through DEL-067-06 confirmed in DELIVERABLE_REGISTER.csv rows 529–533.

**ID resolution notes:**
- `TargetDeliverableID` for DEL-067-02 through DEL-067-06 populated from DELIVERABLE_REGISTER rows 529–533 (all confirmed active).
- PKG-060 resolved from Guidance.md and Datasheet.md cross-reference; full package name "Tank Farm Pump Building 2 / 4-25 Produced Water Transfer Pumps". `TargetDeliverableID` left empty (target is a package, not a deliverable).
- Document targets (rows DEP-067-01-012 through DEP-067-01-014) use `TargetType=DOCUMENT` with `TargetRefID` and `TargetLocation` populated from `_REFERENCES.md`.

**Tree x DAG integrity:**
- Parent anchor (IMPLEMENTS_NODE): 1 row — DEP-067-01-001, targeting PKG-067. No FLOATING_NODE warning.
- Trace anchors (TRACES_TO_REQUIREMENT): 4 rows (SOW-0225 through SOW-0228). No AMBIGUOUS_ANCHOR.

**Extraction posture notes (CONSERVATIVE):**
- Objective associations (OBJ-001, OBJ-003–OBJ-010) listed in `_CONTEXT.md` and DELIVERABLE_REGISTER row 528 were not emitted as TRACES_TO_REQUIREMENT rows because the mapping is via PACKAGE_HEURISTIC (ASSUMPTION), not explicit deliverable-level traceability. Emitting them under CONSERVATIVE would overstate certainty. They are documented here as a non-extracted reference.
- No inferred or PROPOSAL-class rows emitted; all rows are EXPLICIT/HIGH or EXPLICIT/MEDIUM.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 14 |
| RETIRED | 0 |
| **Total** | **14** |

**SatisfactionStatus breakdown (ACTIVE rows):** All 14 rows: `TBD`

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full two-pass extraction run (MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE). 14 rows extracted; 0 retired; 0 declared rows preserved. Decomposition validated against GATE-07 snapshot. No warnings.
