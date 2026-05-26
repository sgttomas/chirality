# Dependencies: DEL-090-05_vendor-document-turnover-package — Vendor Document Turnover Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** DECLARED + EXTRACTED
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1). This file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` produced by `TASK + dependency-extract` (2026-05-26).

**Counts:** 10 rows total — 10 ACTIVE, 0 RETIRED.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-090-05-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-090 | PKG-090 | HIGH | ACTIVE |
| DEP-090-05-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0249 | SOW-0249 | HIGH | ACTIVE |
| DEP-090-05-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0250 | SOW-0250 | HIGH | ACTIVE |
| DEP-090-05-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0251 | SOW-0251 | HIGH | ACTIVE |
| DEP-090-05-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0252 | SOW-0252 | HIGH | ACTIVE |
| DEP-090-05-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-002 | OBJ-002 | MEDIUM | ACTIVE |
| DEP-090-05-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | OBJ-004 | HIGH | ACTIVE |
| DEP-090-05-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | OBJ-010 | HIGH | ACTIVE |
| DEP-090-05-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-090-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package | HIGH | ACTIVE |
| DEP-090-05-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-090-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance | HIGH | ACTIVE |

**Breakdown by class:** ANCHOR = 8, EXECUTION = 2.
**Breakdown by direction:** UPSTREAM = 9, DOWNSTREAM = 1.

## Run Notes

- **Run date:** 2026-05-26
- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **Source docs (AUTO):** Datasheet.md (ANCHOR_DOC — matched heuristic: contains "datasheet"), Specification.md, Guidance.md, Procedure.md (EXECUTION_DOCS — Procedure.md is primary execution signal)
- **Anchor doc selected:** Datasheet.md (highest-confidence match for Pass 1 vertical anchor)
- **Execution doc order:** Procedure.md (primary), Specification.md, Guidance.md
- **Decomposition path (resolved):** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PROJECT_DECOMP.md`
  - Resolution note: Supplied DECOMPOSITION_PATH `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/GATE-07_Final_Published_2026-05-24/` did not exist at that exact location. Resolved via `_REFERENCES.md` (authoritative decomposition basis entry) and confirmed under `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`. This is non-blocking per skill rules.
- **Pass 1 (ANCHOR):** One parent anchor (IMPLEMENTS_NODE → PKG-090) confirmed via Datasheet.md and DELIVERABLE_REGISTER.csv. Four scope-item traces (SOW-0249 to SOW-0252) confirmed via SCOPE_LEDGER.csv. Three objective traces selected from OBJ-002..OBJ-010 per CONSERVATIVE posture: OBJ-002 (general facility scope, MEDIUM confidence — package-heuristic), OBJ-004 (vendor documentation responsibility — HIGH confidence, direct semantic match), OBJ-010 (vendor-documentation and turnover evidence — HIGH confidence, direct semantic match). Remaining objectives (OBJ-003, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009) are listed in Datasheet.md as ASSUMPTION/package-heuristic with no direct semantic match to this deliverable type; omitted under CONSERVATIVE strictness.
- **Pass 2 (EXECUTION):** Two edges extracted. (1) UPSTREAM PREREQUISITE to DEL-090-04 — explicitly stated in Procedure.md Prerequisites; evidence-strong. (2) DOWNSTREAM HANDOVER to DEL-090-06 — explicitly stated in Procedure.md Step 7 and Specification.md R-7. DEL-090-01 and DEL-090-02 mentioned in Procedure.md Prerequisites with note "context only; not declared upstream" — omitted under CONSERVATIVE strictness as the source document itself qualifies these as context-only.
- **`_REFERENCES.md` usage:** Used to resolve decomposition path. No `TargetType=DOCUMENT` rows were emitted from `_REFERENCES.md` entries (no source explicitly states them as required inputs producing a specific information transfer).
- **Tree x DAG integrity:** One parent anchor (DEP-090-05-001); no FLOATING_NODE or AMBIGUOUS_ANCHOR warnings.

## Lifecycle Summary

| Dimension | Count |
|---|---|
| ACTIVE rows | 10 |
| RETIRED rows | 0 |
| ANCHOR rows (ACTIVE) | 8 |
| EXECUTION rows (ACTIVE) | 2 |
| SatisfactionStatus = TBD | 10 |
| SatisfactionStatus = SATISFIED | 0 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-26 — `dependency-extract` UPDATE run; CONSERVATIVE strictness; CONSUMER_CONTEXT=NONE. Created Dependencies.csv (v3.1, 10 ACTIVE rows). Decomposition path resolved from `_REFERENCES.md` (supplied path not found at exact location — non-blocking). No integrity warnings. Schema validation: VALID.
