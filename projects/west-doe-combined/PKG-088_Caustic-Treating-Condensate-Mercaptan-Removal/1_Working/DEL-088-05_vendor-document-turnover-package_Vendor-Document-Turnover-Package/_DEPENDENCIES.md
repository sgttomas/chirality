# Dependencies: DEL-088-05_vendor-document-turnover-package — Vendor Document Turnover Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-26)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1 schema); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Extraction run completed 2026-05-26. Total rows: 6 ACTIVE, 0 RETIRED.

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetID / TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-088-05-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | PACKAGE | PKG-088 — Caustic Treating (Condensate Mercaptan Removal) | HIGH | ACTIVE |
| DEP-088-05-002 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-088-01_scope-of-work — Scope of Work | HIGH | ACTIVE |
| DEP-088-05-003 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-088-02_package-datasheet — Package Datasheet | HIGH | ACTIVE |
| DEP-088-05-004 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-088-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package | HIGH | ACTIVE |
| DEP-088-05-005 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-088-06_epc-vendor-package-review-and-acceptance — EPC Vendor Package Review and Acceptance | HIGH | ACTIVE |
| DEP-088-05-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | 26020-Package_Requirements.docx (heading 41) | MEDIUM | ACTIVE |

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 6 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 5 |
| PENDING | 1 |

ANCHOR rows (IMPLEMENTS_NODE, ACTIVE): 1 — no FLOATING_NODE warning.

## Run Notes

**Run date:** 2026-05-26
**MODE:** UPDATE
**STRICTNESS:** CONSERVATIVE
**CONSUMER_CONTEXT:** NONE

**Decomposition path resolved:** GATE-07 snapshot not found at the exact `DECOMPOSITION_PATH` parameter value (`projects/west-doe-combined/GATE-07_Final_Published_2026-05-24/`) — that path does not exist. Resolved via `_REFERENCES.md` §Authoritative Decomposition Basis to:
`/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PROJECT_DECOMP.md`
and `DELIVERABLE_REGISTER.csv` at the same snapshot path. Non-blocking; resolution recorded here per skill instructions.

**SOURCE_DOCS:** AUTO — scanned deliverable folder. Documents in scope:
- `Datasheet.md` (ANCHOR_DOC: matched heuristic `datasheet`)
- `Specification.md` (EXECUTION_DOC, heuristic `spec`)
- `Procedure.md` (EXECUTION_DOC, heuristic `procedure`)
- `Guidance.md` (EXECUTION_DOC, heuristic `guidance`)

Excluded from extraction scope: `_STATUS.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_MEMORY.md`, `_run_records/` (dependency/coordination artifacts and non-source files).

**ANCHOR_DOC:** AUTO → `Datasheet.md` (highest-confidence match for `datasheet` heuristic).
**EXECUTION_DOC_ORDER:** AUTO → `Procedure.md`, `Specification.md`, `Guidance.md`.

**`_REFERENCES.md` usage:** Used to locate decomposition snapshot path. No `TargetType=DOCUMENT` rows resolved via `_REFERENCES.md` beyond the 26020 reference, which has `TargetLocation=location TBD` per source.

**Warnings:**
- `[WARNING] DECOMP_PATH_NOT_AT_PARAM_LOCATION` — DECOMPOSITION_PATH parameter `projects/west-doe-combined/GATE-07_Final_Published_2026-05-24/` does not exist at that exact path; resolved via `_REFERENCES.md`. Non-blocking.
- DEP-088-05-006 (26020-Package_Requirements.docx heading 41) has `SatisfactionStatus=PENDING` because the source document is referenced but locally inaccessible. Closure of REQ-088-05-04 depends on this source.

**No [WARNING] FLOATING_NODE:** Exactly one IMPLEMENTS_NODE anchor (DEP-088-05-001) found. Tree integrity satisfied.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-26 — EXTRACTED run via dependency-extract skill. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition resolved via _REFERENCES.md to GATE-07 snapshot. 6 rows extracted (1 ANCHOR + 5 EXECUTION), 0 RETIRED. DECOMP_PATH_NOT_AT_PARAM_LOCATION warning recorded; non-blocking.
