# Dependencies: DEL-056-03_construction-work-package — Construction Work Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` — 12 rows (all ACTIVE, all EXTRACTED)

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-056-03-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | PACKAGE | PKG-056 — Inlet Separators 4-25 | HIGH | ACTIVE |
| DEP-056-03-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0127 | HIGH | ACTIVE |
| DEP-056-03-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0128 | HIGH | ACTIVE |
| DEP-056-03-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0129 | HIGH | ACTIVE |
| DEP-056-03-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0130 | HIGH | ACTIVE |
| DEP-056-03-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-056-04 Vendor Engineered Equipment Package | HIGH | ACTIVE |
| DEP-056-03-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-056-02 Package Datasheet | HIGH | ACTIVE |
| DEP-056-03-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | UNKNOWN | Foundations and grading acceptance | HIGH | ACTIVE |
| DEP-056-03-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | EXTERNAL | Heat medium selection decision | HIGH | ACTIVE |
| DEP-056-03-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | DBM-Deepcut SEC-01 Construction Responsibility table | HIGH | ACTIVE |
| DEP-056-03-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | DBM-Deepcut SEC-04 Inlet Separation basis | HIGH | ACTIVE |
| DEP-056-03-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-056-06 EPC Vendor Package Review and Acceptance | MEDIUM | ACTIVE |

**ANCHOR rows:** 5 (1 IMPLEMENTS_NODE + 4 TRACES_TO_REQUIREMENT)
**EXECUTION rows:** 7 (6 UPSTREAM + 1 DOWNSTREAM)

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 12 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 12 |

## Run Notes

- **Run date:** 2026-05-25
- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **Source docs (AUTO):** Datasheet.md, Procedure.md, Guidance.md, Specification.md (all scanned; `_CONTEXT.md` referenced in Specification but not separately extracted as a source document)
- **ANCHOR_DOC (AUTO):** Datasheet.md — selected as highest-confidence anchor signal (contains Identification table with Parent Package and WBS fields)
- **EXECUTION_DOC_ORDER (AUTO):** Procedure.md, Specification.md, Guidance.md
- **Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — Gate 7 Final Published snapshot confirmed present and used for anchor validation.
  - NOTE: DECOMPOSITION_PATH parameter supplied as `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/GATE-07_Final_Published_2026-05-24/` — that path does not exist. Actual snapshot located via `_REFERENCES.md` and auto-discovery; path recorded here.
- **Anchor validation:** DEL-056-03 confirmed in DELIVERABLE_REGISTER.csv; PKG-056 confirmed in PACKAGE_REGISTER.csv; SOW-0127 through SOW-0130 confirmed in SCOPE_LEDGER.csv.
- **DEL-056-04 path:** Target path recorded as pattern; actual folder suffix confirmed from DELIVERABLE_REGISTER row `DEL-056-04_vendor-engineered-equipment-package`.
- **Unresolved targets:**
  - DEP-056-03-008: Foundations/grading acceptance prerequisite — no DEL ID resolved; TargetType=UNKNOWN. ASSUMPTION: earthworks packages in PKG-001 through PKG-005 range may satisfy; not confirmed in local sources.
  - DEP-056-03-009: Heat medium selection — EXTERNAL; no internal deliverable owns this decision in local sources reviewed.
- **Objectives not extracted as ANCHOR rows:** OBJ-001 through OBJ-010 appear in Datasheet but are marked ASSUMPTION per `_CONTEXT.md` (package-heuristic association); CONSERVATIVE strictness excludes these as individual TRACES_TO_REQUIREMENT rows. They are noted here for downstream attention.
- **[WARNING] FLOATING_NODE check:** 1 IMPLEMENTS_NODE row found (DEP-056-03-001). Check passes.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full two-pass extraction via dependency-extract skill. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition path resolved via _REFERENCES.md (supplied path did not exist). 12 ACTIVE rows written; 0 RETIRED. Schema validation: VALID (29 columns, 12 data rows).
