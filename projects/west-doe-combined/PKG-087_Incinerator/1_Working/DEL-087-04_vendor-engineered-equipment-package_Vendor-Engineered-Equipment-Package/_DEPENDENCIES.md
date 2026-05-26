# Dependencies: DEL-087-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** DECLARED
**Dependency tracking mode:** EXTRACTED (dependency-extract run 2026-05-26)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is authoritative (v3.1 schema, 29 required columns); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Run date: 2026-05-26 | Mode: UPDATE | Strictness: CONSERVATIVE | Schema: v3.1 | Rows: 10 ACTIVE, 0 RETIRED

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | Target | Confidence | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-087-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-087 Incinerator | HIGH | ACTIVE |
| DEP-087-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | WBS_NODE | OBJ-002 — 03-25 Compressor Station and Liquids Hub | HIGH | ACTIVE |
| DEP-087-04-003 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-087-01 Scope of Work | HIGH | ACTIVE |
| DEP-087-04-004 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-087-02 Package Datasheet | HIGH | ACTIVE |
| DEP-087-04-005 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-087-05 Vendor Document Turnover Package | HIGH | ACTIVE |
| DEP-087-04-006 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-087-06 EPC Vendor Package Review and Acceptance | HIGH | ACTIVE |
| DEP-087-04-007 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-087-03 Construction Work Package | HIGH | ACTIVE |
| DEP-087-04-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | EXTERNAL | Shared-interface allocation 03-25 / 04-25 | HIGH | ACTIVE |
| DEP-087-04-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | EXTERNAL | Inlet stream composition from upstream caustic-treating package | HIGH | ACTIVE |
| DEP-087-04-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | WBS_NODE | OBJ-006 — Controls / I&C topology | HIGH | ACTIVE |

## Lifecycle Summary

- ACTIVE rows: 10
- RETIRED rows: 0
- ANCHOR rows (ACTIVE): 2 (1 × IMPLEMENTS_NODE, 1 × TRACES_TO_REQUIREMENT)
- EXECUTION rows (ACTIVE): 8 (2 UPSTREAM PREREQUISITE, 2 UPSTREAM CONSTRAINT, 1 UPSTREAM INTERFACE, 3 DOWNSTREAM HANDOVER)
- SatisfactionStatus breakdown: PENDING = 8, TBD = 2

## Run Notes

**Run parameters:**
- SCOPE: DEL-087-04
- DELIVERABLE_PATH: `.../PKG-087_Incinerator/1_Working/DEL-087-04_vendor-engineered-equipment-package_Vendor-Engineered-Equipment-Package`
- RUN_ROOT: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined`
- MODE: UPDATE
- STRICTNESS: CONSERVATIVE
- CONSUMER_CONTEXT: NONE
- SOURCE_DOCS: AUTO (scanned all non-dependency files in deliverable folder)
- ANCHOR_DOC: `Datasheet.md` (matched by filename heuristic; contains Identification table with ParentPackageID, Facility Anchor)
- EXECUTION_DOC_ORDER: `Procedure.md` (primary), `Specification.md`, `Guidance.md`

**Decomposition path resolution:**
- Provided DECOMPOSITION_PATH (`GATE-07_Final_Published_2026-05-24/`) was not a direct file. Resolved via `_REFERENCES.md` and confirmed at:
  `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PROJECT_DECOMP.md`
- Confirmed DEL-087-04 exists in `DELIVERABLE_REGISTER.csv`; PKG-087, OBJ-002, OBJ-004–OBJ-010 all confirmed in decomposition. Non-blocking.

**Extraction notes:**
- Pass 1 (ANCHOR): One IMPLEMENTS_NODE anchor to PKG-087 (WBS_NODE); one TRACES_TO_REQUIREMENT anchor to OBJ-002 (Facility Anchor stated explicitly in Datasheet). OBJ-004 through OBJ-010 are objective traces evidenced in Specification and Procedure but these are captured implicitly via INTERFACE edges and CONSTRAINT rows rather than separate TRACES_TO_REQUIREMENT rows to avoid redundant anchor inflation under CONSERVATIVE strictness — only the explicit facility anchor OBJ-002 emitted as TRACES_TO_REQUIREMENT.
- Pass 2 (EXECUTION): Eight EXECUTION rows extracted from Procedure (prerequisites), Specification (scope inclusions/exclusions and requirements), and Guidance (principles).
- DEL-087-01 and DEL-087-02 are UPSTREAM PREREQUISITEs (hard gates for kickoff and design freeze respectively), explicitly stated in Procedure Prerequisites.
- DEL-087-03, DEL-087-05, DEL-087-06 are DOWNSTREAM HANDOVERs: physical equipment to DEL-087-03, vendor docs to DEL-087-05, acceptance presentation to DEL-087-06.
- Two EXTERNAL CONSTRAINT rows: (1) shared-interface 03-25/04-25 allocation, (2) inlet stream composition from caustic-treating package — both explicitly flagged as open prerequisites in Procedure.
- OBJ-006 (controls topology) extracted as UPSTREAM INTERFACE — Specification R5.1 explicitly states package controls must integrate with EPC controls topology defined under OBJ-006.
- `location TBD` entries in source (PFD, vendor document tables, `26020-Packages_Interfaces.3.xlsx`) were not emitted as rows because the sources do not explicitly state them as required inputs to this deliverable; they are source-document gaps noted in Guidance CONF-03.
- No ASSUMPTION-flagged rows were emitted; all rows have EXPLICIT evidence under CONSERVATIVE strictness.

**QA checks:**
- Schema: VALID (29 required columns, 10 data rows) — confirmed by `validate_dependencies_schema.py`.
- Parent anchor check: 1 IMPLEMENTS_NODE row — OK.
- DependencyID uniqueness: confirmed.
- EvidenceFile and SourceRef populated on all ACTIVE rows.
- No legacy INBOUND/OUTBOUND values used.
- TargetDeliverableID populated only for TargetType=DELIVERABLE rows; empty for WBS_NODE/EXTERNAL rows per schema rules.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-26 — dependency-extract UPDATE run (CONSERVATIVE, CONSUMER_CONTEXT=NONE). 10 ACTIVE rows extracted (2 ANCHOR, 8 EXECUTION). Schema VALID. No warnings.
