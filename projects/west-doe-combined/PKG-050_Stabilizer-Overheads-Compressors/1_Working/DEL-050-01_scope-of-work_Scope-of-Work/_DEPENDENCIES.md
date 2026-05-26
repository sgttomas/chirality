# Dependencies: DEL-050-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1); this file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Extraction run: 2026-05-25 | Mode: UPDATE | Strictness: CONSERVATIVE | Rows: 9 ACTIVE

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-050-01-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-050 | PKG-050 — Stabilizer Overheads Compressors | HIGH | ACTIVE |
| DEP-050-01-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0173 | SCOPE_LEDGER SOW-0173 — Package anchor and responsibility | HIGH | ACTIVE |
| DEP-050-01-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0174 | SCOPE_LEDGER SOW-0174 — Basic scope and process function | HIGH | ACTIVE |
| DEP-050-01-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0175 | SCOPE_LEDGER SOW-0175 — Major included equipment list | HIGH | ACTIVE |
| DEP-050-01-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0176 | SCOPE_LEDGER SOW-0176 — Operating/design conditions | HIGH | ACTIVE |
| DEP-050-01-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | GATE-07-SNAPSHOT | Gate 7 Final Published PROJECT_DECOMP snapshot | HIGH | ACTIVE |
| DEP-050-01-007 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-050-02_package-datasheet | DEL-050-02 — Package Datasheet | HIGH | ACTIVE |
| DEP-050-01-008 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-050-03_construction-work-package | DEL-050-03 — Construction Work Package | MEDIUM | ACTIVE |
| DEP-050-01-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-050-04_vendor-engineered-equipment-package | DEL-050-04 — Vendor Engineered Equipment Package | HIGH | ACTIVE |

## Run Notes

- **Run date:** 2026-05-25
- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; documents used: `Specification.md` (ANCHOR_DOC, primary; contains identity, requirements, source citations), `Guidance.md` (EXECUTION signal; purpose, principles, boundary), `Procedure.md` (EXECUTION signal; prerequisites, steps), `Datasheet.md` (corroborating evidence; Identification, Attributes, Conditions, Interfaces). `_DEPENDENCIES.md` and `_REFERENCES.md` read for context; not source docs.
- **DOC_ROLE_MAP:** DEFAULT heuristic applied. `Specification.md` matched ANCHOR_DOC pattern (`spec`). `Procedure.md` and `Guidance.md` matched EXECUTION_DOC patterns.
- **ANCHOR_DOC:** `Specification.md` (highest-confidence; explicit source citations for all SCOPE_LEDGER rows, PACKAGE_REGISTER, INTERFACE_REGISTER).
- **EXECUTION_DOC_ORDER:** `Procedure.md` (most explicit prerequisite/handoff statements), `Guidance.md` (boundary and flow context), `Datasheet.md` (corroborating).
- **DECOMPOSITION_PATH used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — validated PKG-050, DEL-050-01 through DEL-050-04, SOW-0173 through SOW-0176 from live registers. Note: invoker supplied path `GATE-07_Final_Published_2026-05-24` under `RUN_ROOT`; actual path resolved under `_Decomposition/PROJECT_DECOMP/_GateSnapshots/`.
- **Pass 1 (ANCHOR):** One IMPLEMENTS_NODE row emitted for PKG-050 (WBS_NODE). Four TRACES_TO_REQUIREMENT rows emitted for SOW-0173, SOW-0174, SOW-0175, SOW-0176 — all explicitly cited in Specification.md requirements table with column `Source`.
- **Pass 2 (EXECUTION):** One UPSTREAM PREREQUISITE for GATE-07 snapshot (explicitly stated in Procedure.md). Three DOWNSTREAM ENABLES rows for DEL-050-02, DEL-050-03, DEL-050-04 — all named in Specification.md out-of-scope section; DEL-050-04 additionally corroborated by DELIVERABLE_REGISTER.csv notes ("developed from the EPC package Scope of Work").
- **Excluded (conservative):** DEL-050-05 (Vendor Document Turnover) and DEL-050-06 (EPC Vendor Package Review and Acceptance) are named in Specification out-of-scope but no explicit enables/handover statement connects them directly to the SOW output; omitting to stay CONSERVATIVE.
- **[WARNING] NONE** — parent anchor (IMPLEMENTS_NODE) is present (DEP-050-01-001).

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 9 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| SATISFIED | 6 |
| TBD | 3 |

ANCHOR rows (6): IMPLEMENTS_NODE=1, TRACES_TO_REQUIREMENT=4, (+ 1 PREREQUISITE EXECUTION row marked SATISFIED as snapshot is already accepted).
EXECUTION rows (3 of 4 total): PREREQUISITE=1 (SATISFIED), ENABLES=3 (TBD — downstream deliverables not yet accepted).

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract skill run; MODE=UPDATE; STRICTNESS=CONSERVATIVE; CONSUMER_CONTEXT=NONE; decomposition: GATE-07_Final_Published_2026-05-24; 9 rows extracted (1 IMPLEMENTS_NODE + 4 TRACES_TO_REQUIREMENT + 1 PREREQUISITE + 3 ENABLES); 0 RETIRED; schema validated VALID.
