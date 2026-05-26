# Dependencies: DEL-104-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-26)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` produced by `TASK + dependency-extract` — 2026-05-26 run.

**Total rows: 12 | ACTIVE: 12 | RETIRED: 0**

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetRefID / TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-104-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-104 — Structural steel - outside of modules | HIGH | ACTIVE |
| DEP-104-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0260 | HIGH | ACTIVE |
| DEP-104-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | MEDIUM | ACTIVE |
| DEP-104-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | MEDIUM | ACTIVE |
| DEP-104-02-005 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | GATE-07-SNAPSHOT — Gate 7 decomposition snapshot | HIGH | ACTIVE |
| DEP-104-02-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | DBM-DEEPCUT — 4-25_Deepcut_DBM.md | HIGH | ACTIVE |
| DEP-104-02-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | DBM-COMP-LIQUIDS — 3-25_Comp_and_Liquids_DBM.md | HIGH | ACTIVE |
| DEP-104-02-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | PACKAGE | PKG-001 — Earthworks for foundations (WBS 01) | HIGH | ACTIVE |
| DEP-104-02-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | PACKAGE | PKG-003 — Site Grading (WBS 01) | HIGH | ACTIVE |
| DEP-104-02-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | EXTERNAL | GEOTECH-REPORT — Geotechnical report (TBD) | HIGH | ACTIVE |
| DEP-104-02-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | PKG-REQ-DOC — 26020-Package_Requirements.docx parsed slice | HIGH | ACTIVE |
| DEP-104-02-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | IFC-REGISTER-DOC — 26020-Packages_Interfaces_4_export.xlsx parsed slice | HIGH | ACTIVE |

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 12 |
| RETIRED | 0 |

**SatisfactionStatus breakdown (ACTIVE rows):**

| SatisfactionStatus | Count |
|---|---|
| SATISFIED | 3 (DEP-104-02-005, DEP-104-02-006, DEP-104-02-007) |
| PENDING | 2 (DEP-104-02-008, DEP-104-02-009) |
| TBD | 7 (DEP-104-02-001 through -004, -010, -011, -012) |

**Tree x DAG integrity:**
- IMPLEMENTS_NODE rows (ACTIVE): 1 — DEP-104-02-001 (PKG-104). No floating-node warning.
- AMBIGUOUS_ANCHOR: Not applicable (single parent anchor).

## Run Notes

**Run date:** 2026-05-26
**Mode:** UPDATE
**Strictness:** CONSERVATIVE
**Consumer context:** NONE
**Source documents scanned (AUTO):** Datasheet.md, Guidance.md, Procedure.md, Specification.md, _CONTEXT.md, _REFERENCES.md
**ANCHOR_DOC (AUTO):** Datasheet.md (filename contains "datasheet" — highest-confidence match)
**EXECUTION_DOC_ORDER (AUTO):** Procedure.md, Specification.md, Guidance.md, Datasheet.md

**Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
- Note: DECOMPOSITION_PATH parameter was given as `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/GATE-07_Final_Published_2026-05-24/` (does not exist). Resolved to the actual Gate 7 snapshot at the path recorded in `_REFERENCES.md` and `_CONTEXT.md`. Recorded here per skill default-path-logging requirement.

**Defaults applied:**
- `SOURCE_DOCS=AUTO`: scanned all non-artifact `.md` files in deliverable folder.
- `DOC_ROLE_MAP=DEFAULT`: Datasheet.md identified as ANCHOR_DOC; Procedure.md and Specification.md as EXECUTION_DOCS.
- `ANCHOR_DOC=AUTO`: Datasheet.md chosen.
- `EXECUTION_DOC_ORDER=AUTO`: Procedure.md first (workflow/procedure signal), Specification.md second (requirements signal), Guidance.md third.
- `MODE=UPDATE`: no existing Dependencies.csv; all rows are new.
- `STRICTNESS=CONSERVATIVE`: ANCHOR rows emitted only when identifiers appear explicitly. OBJ-001 and OBJ-008 anchors included because they appear explicitly in _CONTEXT.md; recorded as ASSUMPTION per Guidance.md CONF-104-02-01 and Datasheet.md (PACKAGE_HEURISTIC mode).

**Warnings / open items:**
- OBJ-001 and OBJ-008 anchor rows (DEP-104-02-003, DEP-104-02-004) are ASSUMPTION: objective association is via PACKAGE_HEURISTIC, not confirmed at deliverable-ID level. See Guidance.md CONF-104-02-01.
- Geotechnical report (DEP-104-02-010) identity and path are unknown; recorded as EXTERNAL/TBD.
- 26020-Package_Requirements.docx (DEP-104-02-011) and 26020-Packages_Interfaces_4_export.xlsx (DEP-104-02-012) are binary sources in _Sources/; no parsed slices available. These are blocking prerequisites for completing the supported-equipment list and interface matrix (Specification R-8). SatisfactionStatus=PENDING.
- No downstream dependency rows extracted: Guidance.md describes DEL-104-02 as read "alongside" DEL-104-01, DEL-104-03, DEL-104-04 — these are co-reference relationships, not explicit artifact-transfer edges; excluded per skill methodology (information-flow-only rule).

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-26 — First EXTRACTED run via `TASK + dependency-extract`. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. 12 rows extracted (4 ANCHOR, 8 EXECUTION); all ACTIVE. Schema: v3.1. Decomposition: GATE-07_Final_Published_2026-05-24. Warnings: OBJ heuristic anchors (2 rows ASSUMPTION); geotechnical report TBD; two binary source prerequisites unresolved.
