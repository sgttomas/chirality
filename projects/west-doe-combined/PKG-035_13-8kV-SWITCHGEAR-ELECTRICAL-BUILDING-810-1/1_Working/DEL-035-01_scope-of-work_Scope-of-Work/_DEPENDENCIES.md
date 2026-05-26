# Dependencies: DEL-035-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED
**Dependency tracking mode:** EXTRACTED (dependency-extract run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is canonical; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

16 rows extracted (all ACTIVE). Schema version: v3.1.

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-035-01-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0036 | Scope item SOW-0036 | HIGH | ACTIVE |
| DEP-035-01-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | OBJ-001 | HIGH | ACTIVE |
| DEP-035-01-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | OBJ-004 | HIGH | ACTIVE |
| DEP-035-01-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | OBJ-005 | HIGH | ACTIVE |
| DEP-035-01-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | OBJ-006 | HIGH | ACTIVE |
| DEP-035-01-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | OBJ-007 | HIGH | ACTIVE |
| DEP-035-01-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | OBJ-008 | HIGH | ACTIVE |
| DEP-035-01-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | OBJ-009 | HIGH | ACTIVE |
| DEP-035-01-009 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | OBJ-010 | HIGH | ACTIVE |
| DEP-035-01-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | GATE-07-DECOMP | Gate 7 PROJECT_DECOMP Snapshot | HIGH | ACTIVE |
| DEP-035-01-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | WB-PKG-ROW-37 | Workbook Packages row 37 | HIGH | ACTIVE |
| DEP-035-01-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | DBM-DEEPCUT-4-25 | DBM-Deepcut 4-25_Deepcut_DBM.md | HIGH | ACTIVE |
| DEP-035-01-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | DBM-COMP-3-25 | DBM-Comp_and_Liquids 3-25_Comp_and_Liquids_DBM.md | HIGH | ACTIVE |
| DEP-035-01-014 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-035-02_package-datasheet | Package Datasheet (DEL-035-02) | HIGH | ACTIVE |
| DEP-035-01-015 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-035-03_construction-work-package | Construction Work Package (DEL-035-03) | HIGH | ACTIVE |
| DEP-035-01-016 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-035-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package (DEL-035-04) | MEDIUM | ACTIVE |

## Run Notes

- MODE: UPDATE
- STRICTNESS: CONSERVATIVE
- CONSUMER_CONTEXT: NONE
- SOURCE_DOCS: AUTO — scanned deliverable folder; Specification.md (ANCHOR_DOC), Datasheet.md, Procedure.md, Guidance.md, _CONTEXT.md used.
- ANCHOR_DOC: Specification.md (contains explicit SOW and scope references); Datasheet.md used to confirm identity fields.
- DECOMPOSITION_PATH: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — used to validate SOW-0036, PKG-035, DEL-035-0x IDs, and objective IDs.
- Pass 1 (ANCHOR): 1 IMPLEMENTS_NODE (SOW-0036 as WBS_NODE — the canonical scope ledger node for this deliverable), 8 TRACES_TO_REQUIREMENT (OBJ-001, OBJ-004 through OBJ-010). No WBS numeric code found in sources; SOW-0036 is used as the primary definition node per SCOPE_LEDGER.csv and _CONTEXT.md.
- Pass 2 (EXECUTION): 4 UPSTREAM PREREQUISITE (Gate 7 snapshot, workbook row 37, DBM-Deepcut, DBM-Comp_and_Liquids — all explicitly listed in Procedure.md Prerequisites). 3 DOWNSTREAM ENABLES (DEL-035-02, DEL-035-03, DEL-035-04 — explicitly named in Specification.md Scope as downstream consumers). DEL-035-05 (vendor document turnover) and DEL-035-06 (EPC review/acceptance) are listed in SCOPE_LEDGER SOW-0036 but Specification.md names them only by category without an explicit information-transfer statement; not extracted under CONSERVATIVE strictness.
- No existing Dependencies.csv found; new register created.
- No legacy rows to retire.
- ASSUMPTION on DEP-035-01-016: DEL-035-04 folder name in filesystem may differ from SCOPE_LEDGER canonical ID; matched best-effort.

## Lifecycle Summary

- ACTIVE: 16
- RETIRED: 0
- ANCHOR rows (ACTIVE): 9 (1 IMPLEMENTS_NODE + 8 TRACES_TO_REQUIREMENT)
- EXECUTION rows (ACTIVE): 7 (4 UPSTREAM PREREQUISITE + 3 DOWNSTREAM ENABLES)
- SatisfactionStatus breakdown: SATISFIED = 13 (anchors + upstream prereqs already available), TBD = 3 (downstream enables — not yet closed)

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract UPDATE run; MODE=UPDATE; STRICTNESS=CONSERVATIVE; CONSUMER_CONTEXT=NONE; decomposition=GATE-07_Final_Published_2026-05-24; 16 rows extracted (all ACTIVE); no prior rows retired; schema v3.1.
