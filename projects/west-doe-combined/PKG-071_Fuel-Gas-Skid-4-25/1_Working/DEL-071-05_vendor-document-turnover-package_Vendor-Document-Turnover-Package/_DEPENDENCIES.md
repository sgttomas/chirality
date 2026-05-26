# Dependencies: DEL-071-05_vendor-document-turnover-package — Vendor Document Turnover Package

**Coordination Mode:** DECLARED
**Dependency tracking mode:** EXTRACTED (first run)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1); this file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Total ACTIVE rows: 10
Total RETIRED rows: 0

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetID / TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-071-05-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-071 Fuel Gas Skid 4-25 | HIGH | ACTIVE |
| DEP-071-05-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0099 | HIGH | ACTIVE |
| DEP-071-05-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0100 | HIGH | ACTIVE |
| DEP-071-05-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0101 | HIGH | ACTIVE |
| DEP-071-05-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0102 | HIGH | ACTIVE |
| DEP-071-05-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-071-01_scope-of-work | HIGH | ACTIVE |
| DEP-071-05-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-071-02_package-datasheet | HIGH | ACTIVE |
| DEP-071-05-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DELIVERABLE | DEL-071-04_vendor-engineered-equipment-package | HIGH | ACTIVE |
| DEP-071-05-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | EXTERNAL | EPC interface documents (P&IDs; line list; etc.) | HIGH | ACTIVE |
| DEP-071-05-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-071-03_construction-work-package | MEDIUM | ACTIVE |

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 10 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| SATISFIED | 5 (ANCHOR rows — decomposition identity established) |
| TBD | 5 (EXECUTION rows — open pending vendor engagement and project progression) |

## Run Notes

- **Run date:** 2026-05-25
- **Mode:** UPDATE (first-run; no prior Dependencies.csv existed)
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE

**Source documents scanned (AUTO):**
- `Datasheet.md` — used as ANCHOR_DOC (primary identification and scope item signals)
- `Specification.md` — used as EXECUTION_DOC (requirements R-1 through R-9 providing explicit dependency signals)
- `Procedure.md` — used as EXECUTION_DOC (prerequisites and steps providing prerequisite/handover signals)
- `Guidance.md` — used as EXECUTION_DOC (principles and considerations providing interface/constraint signals)

**Decomposition path used:**
- GATE-07 snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
- DELIVERABLE_REGISTER.csv confirmed DEL-071-05 row with PKG-071, SOW-0099/0100/0101/0102, and sibling deliverable IDs.
- SCOPE_LEDGER.csv confirmed SOW items and deliverable coverage.

**Note on DECOMPOSITION_PATH parameter:** The invoker specified `GATE-07_Final_Published_2026-05-24/` under the RUN_ROOT as `DECOMPOSITION_PATH`; the directory does not exist at that path. The GATE-07 snapshot was located at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` and used instead. No warning needed — snapshot located and used successfully.

**Binary source inaccessibility:** `26020-Package_Requirements.docx` heading 25 and `26020-Packages_Interfaces_4_export.xlsx` Workbook Packages row 61 are not locally readable in plain-text form. No dependency rows were generated solely from these binary sources; all EXECUTION rows are grounded in locally readable source docs (Specification, Procedure, Guidance).

**Pass 1 (ANCHOR) findings:**
- 1 parent anchor emitted: DEP-071-05-001 (IMPLEMENTS_NODE → PKG-071). Count = 1; no FLOATING_NODE or AMBIGUOUS_ANCHOR warning.
- 4 trace anchors emitted: DEP-071-05-002 through DEP-071-05-005 (SOW-0099/0100/0101/0102).

**Pass 2 (EXECUTION) findings:**
- 5 execution rows emitted.
- 3 UPSTREAM edges: DEL-071-01 (PREREQUISITE), DEL-071-02 (PREREQUISITE), DEL-071-04 (INTERFACE).
- 1 UPSTREAM CONSTRAINT: EPC interface documents (P&IDs, line list, etc.) — TargetType=EXTERNAL because these are EPC discipline deliverables not represented as a single decomposed deliverable ID.
- 1 DOWNSTREAM HANDOVER: DEL-071-03 Construction Work Package (MEDIUM confidence; marked ASSUMPTION in Notes).

**Signals not extracted (by CONSERVATIVE rule):**
- DBM-Deepcut design basis (L1839-L1905) referenced in Specification R-3: this is a source document providing technical content, not a dependency relationship to another deliverable or entity. Not emitted.
- OBJ-001/004/005/006/007/008/009/010 objective associations: per Guidance, these are PACKAGE_HEURISTIC associations not confirmed at deliverable-ID resolution. Not emitted as TRACES_TO_REQUIREMENT rows (no explicit evidence at deliverable level).
- DEL-071-06_epc-vendor-package-review-and-acceptance: referenced in SCOPE_LEDGER but no explicit dependency signal found in source documents for DEL-071-05. Not emitted.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION). No Dependencies.csv.
- 2026-05-25 — First extraction run. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition: GATE-07_Final_Published_2026-05-24 (located at _GateSnapshots path). 10 ACTIVE rows written (5 ANCHOR, 5 EXECUTION). Schema validated VALID.
