# Dependencies: DEL-066-05_vendor-document-turnover-package — Vendor Document Turnover Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract run 2026-05-25)
**Default maturity threshold:** ACCEPTED
**Register convention:** `Dependencies.csv` is the canonical register; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` generated 2026-05-25 by `TASK + dependency-extract` (MODE=UPDATE, STRICTNESS=CONSERVATIVE).

**Row counts:**
- Total rows: 11
- ACTIVE: 11
- RETIRED: 0

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetID / TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-066-05-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-066 — Tanks Condensate (API 650) 4-25 | HIGH | ACTIVE |
| DEP-066-05-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0205 | HIGH | ACTIVE |
| DEP-066-05-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0206 | HIGH | ACTIVE |
| DEP-066-05-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0207 | HIGH | ACTIVE |
| DEP-066-05-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0208 | HIGH | ACTIVE |
| DEP-066-05-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-066-01_scope-of-work | HIGH | ACTIVE |
| DEP-066-05-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-066-02_package-datasheet | HIGH | ACTIVE |
| DEP-066-05-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DELIVERABLE | DEL-066-03_construction-work-package | HIGH | ACTIVE |
| DEP-066-05-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-066-04_vendor-engineered-equipment-package | HIGH | ACTIVE |
| DEP-066-05-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-066-06_epc-vendor-package-review-and-acceptance | HIGH | ACTIVE |
| DEP-066-05-011 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-066-06_epc-vendor-package-review-and-acceptance | HIGH | ACTIVE |

## Run Notes

- **Run date:** 2026-05-25
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; source documents used: `Datasheet.md` (ANCHOR_DOC), `Procedure.md`, `Guidance.md`, `Specification.md` (EXECUTION_DOC_ORDER)
- **ANCHOR_DOC:** `Datasheet.md` (contains ParentPackageID, scope ledger references — highest-confidence anchor signal)
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — used to validate PKG-066 parent anchor and resolve SOW IDs; DELIVERABLE_REGISTER.csv and SCOPE_LEDGER.csv consulted.
- **Parent anchor:** DEP-066-05-001 — `PKG-066` confirmed in PACKAGE_REGISTER.csv and DELIVERABLE_REGISTER.csv Gate-07. Count = 1; no FLOATING_NODE or AMBIGUOUS_ANCHOR warning.
- **Requirement traces:** SOW-0205..SOW-0208 confirmed in SCOPE_LEDGER.csv Gate-07 with DEL-066-05 listed in each deliverable set.
- **Execution edges:** All five sibling deliverables (DEL-066-01..06) resolved via DELIVERABLE_REGISTER.csv Gate-07. DEP-066-05-010 and DEP-066-05-011 both target DEL-066-06 but represent distinct relationship types (HANDOVER of Final VDB artifact vs. ENABLES the acceptance event); retained as separate rows per evidence distinction.
- **No FLOATING_NODE warning** — parent IMPLEMENTS_NODE anchor confirmed.
- **No AMBIGUOUS_ANCHOR warning** — exactly one IMPLEMENTS_NODE row.
- **No MISSING_DECOMPOSITION warning** — decomposition snapshot located and used.
- **ASSUMPTION noted in Datasheet.md:** Analog basis (3-25 condensate tanks) is the source scope basis; 4-25 RFQ not yet issued. Dependency rows are grounded in the decomposition identifiers and source documents available, not the pending RFQ.

## Lifecycle Summary

| Dimension | Count |
|---|---|
| ACTIVE | 11 |
| RETIRED | 0 |
| ANCHOR rows (ACTIVE) | 5 |
| EXECUTION rows (ACTIVE) | 6 |
| SatisfactionStatus = TBD | 11 |
| SatisfactionStatus = PENDING | 0 |
| SatisfactionStatus = SATISFIED | 0 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full two-pass dependency extraction executed (MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE). 11 rows extracted (5 ANCHOR, 6 EXECUTION). All HIGH confidence. Schema validated VALID. Row count 11.
