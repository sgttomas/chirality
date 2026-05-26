# Dependencies: DEL-052-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1 schema). This file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Dependencies.csv produced by dependency-extract run on 2026-05-25. Schema version: v3.1. Total rows: 12. All rows ACTIVE.

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetName / ID | Confidence | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-052-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-052 — Inlet / TEG Dehy Cross Exchanger | HIGH | ACTIVE |
| DEP-052-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0103 | HIGH | ACTIVE |
| DEP-052-04-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0104 | HIGH | ACTIVE |
| DEP-052-04-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0105 | HIGH | ACTIVE |
| DEP-052-04-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0106 | HIGH | ACTIVE |
| DEP-052-04-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-052-01 (Scope of Work) | HIGH | ACTIVE |
| DEP-052-04-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-052-02 (Package Datasheet) | HIGH | ACTIVE |
| DEP-052-04-008 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-052-05 (Vendor Document Turnover Package) | HIGH | ACTIVE |
| DEP-052-04-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-052-06 (EPC Vendor Package Review and Acceptance) | HIGH | ACTIVE |
| DEP-052-04-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | DOCUMENT | 26020-Package_Requirements.docx heading 7 | MEDIUM | ACTIVE |
| DEP-052-04-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | UNKNOWN | Upstream inlet separator overhead piping | MEDIUM | ACTIVE |
| DEP-052-04-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | INTERFACE | UNKNOWN | Downstream warm-side piping (molecular-sieve inlet filter/coalescers) | MEDIUM | ACTIVE |

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; candidate files: `Datasheet.md`, `Guidance.md`, `Procedure.md`, `Specification.md`
- **ANCHOR_DOC:** `Datasheet.md` (contains `DeliverableID`, `ParentPackageID`, `Covers Scope Items` identification fields — highest-confidence match for ANCHOR_DOC heuristic)
- **EXECUTION_DOC_ORDER:** `Procedure.md` (primary workflow/prerequisites signal), `Specification.md` (requirements/interfaces signal), `Guidance.md` (considerations and conflict table — supplemental)
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — located via `_REFERENCES.md`; snapshot exists and was read.
- **NOTE — DECOMPOSITION_PATH param:** The `DECOMPOSITION_PATH` parameter provided in the run invocation (`/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/GATE-07_Final_Published_2026-05-24/`) does not exist on disk. The actual gate snapshot was resolved via `_REFERENCES.md` at the path above. Recorded as informational discrepancy only.
- **ANCHOR validation:** `PKG-052` confirmed in PACKAGE_REGISTER.csv. `DEL-052-04` confirmed in DELIVERABLE_REGISTER.csv. SOW-0103 through SOW-0106 confirmed in DELIVERABLE_REGISTER.csv source coverage column for PKG-052 deliverables.
- **EXECUTION targets:** DEL-052-01, DEL-052-02, DEL-052-05, DEL-052-06 all confirmed in DELIVERABLE_REGISTER.csv for PKG-052. `TargetDeliverableID` populated for all DELIVERABLE-type targets.
- **UNRESOLVED targets:** DEP-052-04-011 and DEP-052-04-012 reference piping interfaces; specific piping deliverable IDs are not resolvable from accessible source slice. Retained as `TargetType=UNKNOWN`.
- **26020-Package_Requirements.docx:** Referenced by decomposition row and Standards table. Full text not extracted to accessible markdown; TargetLocation empty. Marked `Confidence=MEDIUM`.
- **Tree x DAG integrity:** 1 IMPLEMENTS_NODE row (DEP-052-04-001) — no FLOATING_NODE or AMBIGUOUS_ANCHOR warning.

## Lifecycle Summary

| Dimension | Count |
|---|---|
| Total rows | 12 |
| ACTIVE | 12 |
| RETIRED | 0 |
| ANCHOR / IMPLEMENTS_NODE | 1 |
| ANCHOR / TRACES_TO_REQUIREMENT | 4 |
| EXECUTION / UPSTREAM | 4 |
| EXECUTION / DOWNSTREAM | 3 |
| SatisfactionStatus = PENDING | 2 (DEP-052-04-006, DEP-052-04-007) |
| SatisfactionStatus = TBD | 10 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract run; MODE=UPDATE; STRICTNESS=CONSERVATIVE; CONSUMER_CONTEXT=NONE; decomposition path resolved via _REFERENCES.md (gate snapshot 2026-05-24); 12 rows written (all ACTIVE); schema v3.1; no warnings (parent anchor found; no ambiguous anchors).
