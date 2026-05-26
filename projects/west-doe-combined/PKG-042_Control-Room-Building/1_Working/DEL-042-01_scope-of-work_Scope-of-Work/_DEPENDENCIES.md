# Dependencies: DEL-042-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is canonical; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` generated 2026-05-25. Schema version: v3.1. Row count: 12 ACTIVE rows.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-042-01-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0043 | Scope Ledger SOW-0043 — Control Room Building (WBS 03) | HIGH | ACTIVE |
| DEP-042-01-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | REQ-042-01-01 | REQ-042-01-01 — Package identification | HIGH | ACTIVE |
| DEP-042-01-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | REQ-042-01-02 | REQ-042-01-02 — Function and integration narrative | HIGH | ACTIVE |
| DEP-042-01-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | REQ-042-01-05 | REQ-042-01-05 — EPC integration boundary by interface type | HIGH | ACTIVE |
| DEP-042-01-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | REQ-042-01-08 | REQ-042-01-08 — Consistency with SCOPE_LEDGER.csv SOW-0043 | HIGH | ACTIVE |
| DEP-042-01-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | PACKAGE_REGISTER | PACKAGE_REGISTER.csv row PKG-042 (GATE-07) | HIGH | ACTIVE |
| DEP-042-01-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | INTERFACE_REGISTER | INTERFACE_REGISTER.csv rows for PKG-042 (GATE-07) | HIGH | ACTIVE |
| DEP-042-01-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | SCOPE_LEDGER | SCOPE_LEDGER.csv row SOW-0043 (GATE-07) | HIGH | ACTIVE |
| DEP-042-01-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-042-02_package-datasheet | Package Datasheet (DEL-042-02) | HIGH | ACTIVE |
| DEP-042-01-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-042-03_construction-work-package | Construction Work Package (DEL-042-03) | HIGH | ACTIVE |
| DEP-042-01-011 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-042-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package (DEL-042-04) | MEDIUM | ACTIVE |
| DEP-042-01-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-042-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance (DEL-042-06) | MEDIUM | ACTIVE |

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder: Specification.md (ANCHOR_DOC), Datasheet.md, Procedure.md, Guidance.md (EXECUTION_DOCs)
- **ANCHOR_DOC:** Specification.md (selected: filename contains "scope"; primary requirements holder)
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` (FACT — path confirmed present; registers read: SCOPE_LEDGER.csv, DELIVERABLE_REGISTER.csv, PACKAGE_REGISTER.csv confirmed)
- **Brief DECOMPOSITION_PATH:** `GATE-07_Final_Published_2026-05-24` — note the brief listed `projects/west-doe-combined/GATE-07_Final_Published_2026-05-24/` which does not exist; resolved to canonical path above per `_REFERENCES.md` and `_DEPENDENCIES.md` Run Notes.

**Pass 1 (ANCHOR):**
- One IMPLEMENTS_NODE anchor found: SOW-0043 (WBS_NODE) — explicitly named in Specification.md REQ-042-01-08 and confirmed in SCOPE_LEDGER.csv. Parent anchor count = 1. No FLOATING_NODE or AMBIGUOUS_ANCHOR warnings.
- Four TRACES_TO_REQUIREMENT anchors emitted for REQ-042-01-01, REQ-042-01-02, REQ-042-01-05, REQ-042-01-08 (explicit in Specification.md; conservative selection of highest-traceability requirements).

**Pass 2 (EXECUTION):**
- Three UPSTREAM PREREQUISITE edges to decomposition register documents (PACKAGE_REGISTER.csv, INTERFACE_REGISTER.csv, SCOPE_LEDGER.csv) — all explicitly named as required inputs in Specification.md and Procedure.md.
- Four DOWNSTREAM ENABLES edges to sibling deliverables DEL-042-02, DEL-042-03, DEL-042-04, DEL-042-06 — all explicitly referenced in Specification.md Out of Scope or DELIVERABLE_REGISTER.csv as downstream consumers or dependents of this deliverable. DEL-042-05 (Vendor Document Turnover Package) not emitted as a downstream edge because no explicit information-flow statement from this deliverable to DEL-042-05 was found in source (only structural decomposition adjacency — excluded per information-flow-only rule).

**Warnings:**
- None. No FLOATING_NODE, AMBIGUOUS_ANCHOR, or MISSING_DECOMPOSITION.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 12 |
| RETIRED | 0 |

| DependencyClass | ACTIVE |
|---|---|
| ANCHOR | 5 |
| EXECUTION | 7 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 12 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract skill run; MODE=UPDATE; STRICTNESS=CONSERVATIVE; CONSUMER_CONTEXT=NONE; SOURCE_DOCS=AUTO; decomposition=GATE-07_Final_Published_2026-05-24 (confirmed present); 12 rows extracted (5 ANCHOR, 7 EXECUTION); schema v3.1; validation VALID.
