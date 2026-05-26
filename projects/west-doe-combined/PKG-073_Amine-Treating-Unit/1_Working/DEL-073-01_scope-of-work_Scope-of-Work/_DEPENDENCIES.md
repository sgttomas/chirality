# Dependencies: DEL-073-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (Dependencies.csv is canonical)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is canonical (produced by `TASK + dependency-extract`); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` produced by `TASK + dependency-extract` — UPDATE run 2026-05-25.

**Summary:** 19 rows total — 10 ANCHOR rows + 9 EXECUTION rows; all ACTIVE.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-073-01-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0051 | Scope decision SOW-0051 — Amine Treating Unit | ACTIVE |
| DEP-073-01-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | Project Objective OBJ-001 | ACTIVE |
| DEP-073-01-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-003 | Project Objective OBJ-003 | ACTIVE |
| DEP-073-01-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Project Objective OBJ-004 | ACTIVE |
| DEP-073-01-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Project Objective OBJ-005 | ACTIVE |
| DEP-073-01-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Project Objective OBJ-006 | ACTIVE |
| DEP-073-01-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | Project Objective OBJ-007 | ACTIVE |
| DEP-073-01-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Project Objective OBJ-008 | ACTIVE |
| DEP-073-01-009 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 | ACTIVE |
| DEP-073-01-010 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 | ACTIVE |
| DEP-073-01-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | GATE-07 Final Published PROJECT_DECOMP snapshot | ACTIVE |
| DEP-073-01-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | 26020-Package_Requirements.docx heading 27 | ACTIVE |
| DEP-073-01-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | 26020-01-PT-RFQ-27-001 Bid Doc Appendix A | ACTIVE |
| DEP-073-01-014 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-073-02_package-datasheet | Package Datasheet (DEL-073-02) | ACTIVE |
| DEP-073-01-015 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-073-03_construction-work-package | Construction Work Package (DEL-073-03) | ACTIVE |
| DEP-073-01-016 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-073-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package (DEL-073-04) | ACTIVE |
| DEP-073-01-017 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-073-05_vendor-document-turnover-package | Vendor Document Turnover Package (DEL-073-05) | ACTIVE |
| DEP-073-01-018 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-073-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance (DEL-073-06) | ACTIVE |
| DEP-073-01-019 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | INTERFACE | PACKAGE | PKG-046 | Acid Gas Compressors (PKG-046) | ACTIVE |

## Run Notes

**Run date:** 2026-05-25
**Mode:** UPDATE
**Strictness:** CONSERVATIVE
**Consumer context:** NONE
**Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` (confirmed present)
**Source docs scanned (AUTO):** `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, `_CONTEXT.md`, `_REFERENCES.md`
**Anchor doc (AUTO):** `Datasheet.md` (contains explicit WBS, package identity, and source basis references)
**Execution doc order (AUTO):** `Procedure.md` (explicit prerequisites), `Guidance.md` (explicit considerations), `Specification.md` (requirements)

**Defaults applied:**
- MODE: UPDATE (no existing Dependencies.csv — created fresh)
- STRICTNESS: CONSERVATIVE — ANCHOR rows emitted only for identifiers appearing explicitly in source documents; EXECUTION rows emitted only for explicit stated prerequisites and information-transfer relationships
- CONSUMER_CONTEXT: NONE — no downstream handoff notes section generated

**Decomposition path note:** DECOMPOSITION_PATH parameter referenced `GATE-07_Final_Published_2026-05-24/` which does not exist as a standalone path at the RUN_ROOT. Resolved to confirmed location at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`. Anchor IDs validated against this snapshot.

**Warnings:**
- None. Parent anchor (IMPLEMENTS_NODE) found: DEP-073-01-001 → SOW-0051. No FLOATING_NODE condition.
- DEP-073-01-012 (26020-Package_Requirements.docx heading 27): SatisfactionStatus=PENDING — clause-level text not accessible as markdown. Tracked in Conflict C-073-01-01 in Guidance.md.
- DEP-073-01-013 (Bid Doc Appendix A): SatisfactionStatus=PENDING — file not present in `_Sources`. Tracked in Conflict C-073-01-02 in Guidance.md. TargetLocation=`location TBD`.

## Lifecycle Summary

| Dimension | Count |
|---|---|
| Total rows | 19 |
| ACTIVE | 19 |
| RETIRED | 0 |
| ANCHOR rows (ACTIVE) | 10 |
| EXECUTION rows (ACTIVE) | 9 |
| SatisfactionStatus=TBD | 16 |
| SatisfactionStatus=SATISFIED | 1 |
| SatisfactionStatus=PENDING | 2 |

**Tree x DAG integrity:**
- Parent anchor (IMPLEMENTS_NODE): 1 — DEP-073-01-001 → SOW-0051. PASS.
- Trace anchors (TRACES_TO_REQUIREMENT): 9 — OBJ-001 through OBJ-010 (excluding OBJ-002 which is not listed for this deliverable).

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — UPDATE run; MODE=UPDATE; STRICTNESS=CONSERVATIVE; CONSUMER_CONTEXT=NONE; decomposition=GATE-07_Final_Published_2026-05-24 (confirmed present); created Dependencies.csv (19 rows, all ACTIVE); schema VALID (29 columns); no FLOATING_NODE; 2 PENDING prerequisites (Word heading 27 clause extract; Bid Doc Appendix A).
