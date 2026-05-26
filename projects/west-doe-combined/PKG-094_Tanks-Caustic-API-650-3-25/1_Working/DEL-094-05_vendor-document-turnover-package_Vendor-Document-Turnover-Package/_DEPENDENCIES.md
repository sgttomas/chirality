# Dependencies: DEL-094-05_vendor-document-turnover-package — Vendor Document Turnover Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-26)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` (v3.1) is the canonical structured register; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

**Schema version:** v3.1
**Last extraction run:** 2026-05-26
**Mode:** UPDATE | **Strictness:** CONSERVATIVE | **Consumer context:** NONE

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetID / TargetRefID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-094-05-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | PACKAGE | PKG-094 | Tanks, Caustic (API 650) 3-25 | HIGH | ACTIVE |
| DEP-094-05-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0193 | SOW-0193 — Carry caustic tanks package as distinct flat project package | HIGH | ACTIVE |
| DEP-094-05-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0194 | SOW-0194 — Basic scope: supply one spent caustic tank and one fresh caustic tank | HIGH | ACTIVE |
| DEP-094-05-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0195 | SOW-0195 — Major included equipment; API 650 modified; TK-6930-2 | HIGH | ACTIVE |
| DEP-094-05-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0196 | SOW-0196 — Scope notes and open items; by-others exclusions | HIGH | ACTIVE |
| DEP-094-05-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-094-01_scope-of-work | Scope of Work | HIGH | ACTIVE |
| DEP-094-05-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-094-02_package-datasheet | Package Datasheet | HIGH | ACTIVE |
| DEP-094-05-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-094-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package | HIGH | ACTIVE |
| DEP-094-05-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DELIVERABLE | DEL-094-03_construction-work-package | Construction Work Package | HIGH | ACTIVE |
| DEP-094-05-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-094-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance | HIGH | ACTIVE |

**Total ACTIVE rows:** 10 (5 ANCHOR, 5 EXECUTION)
**Total RETIRED rows:** 0

## Run Notes

- **Run date:** 2026-05-26
- **Mode:** UPDATE | **Strictness:** CONSERVATIVE | **Consumer context:** NONE
- **SOURCE_DOCS:** AUTO — scanned Datasheet.md (ANCHOR_DOC, heuristic: contains "datasheet"), Guidance.md, Procedure.md, Specification.md (EXECUTION_DOCS)
- **ANCHOR_DOC chosen:** Datasheet.md (highest-confidence anchor signal per DEFAULT DOC_ROLE_MAP heuristic)
- **EXECUTION_DOC_ORDER chosen:** Procedure.md (primary workflow signal), Specification.md, Guidance.md
- **DECOMPOSITION_PATH resolved:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PROJECT_DECOMP.md` — resolved via `_REFERENCES.md` (GATE-07_Final_Published_2026-05-24 path). Provided DECOMPOSITION_PATH (`GATE-07_Final_Published_2026-05-24` at run-root) did not exist at that exact location; resolved to gate snapshot under `_Decomposition/PROJECT_DECOMP/_GateSnapshots/`. Non-blocking.
- **Anchor validation:** DEL-094-05, PKG-094, SOW-0193–SOW-0196 all confirmed in DELIVERABLE_REGISTER.csv, PACKAGE_REGISTER.csv, and SCOPE_LEDGER.csv of the gate snapshot.
- **Objective association:** Datasheet lists OBJ-002 through OBJ-010 with ASSUMPTION flag (package-grouping heuristic). Not emitted as TRACES_TO_REQUIREMENT rows under CONSERVATIVE strictness; confirmed in HRR-008.
- **DEP-094-05-008 RequiredMaturity:** Set to IN_PROGRESS (not ACCEPTED) consistent with Procedure.md statement "in progress; vendor authoring documents per its design basis."
- **Tree x DAG integrity:** Parent anchor (IMPLEMENTS_NODE) count = 1 — OK. No AMBIGUOUS_ANCHOR.
- **No FLOATING_NODE warning.**
- **No MISSING_DECOMPOSITION warning** — decomposition resolved via _REFERENCES.md.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-26 — dependency-extract skill run; MODE=UPDATE; STRICTNESS=CONSERVATIVE; CONSUMER_CONTEXT=NONE; decomposition resolved via _REFERENCES.md gate snapshot; 10 rows extracted (5 ANCHOR, 5 EXECUTION); 0 RETIRED; schema validation PASSED.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 10 |
| RETIRED | 0 |
| **Total** | **10** |

| SatisfactionStatus | Count |
|---|---|
| TBD | 10 |
