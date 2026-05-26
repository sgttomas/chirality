# Dependencies: DEL-026-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1); this file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Run produced 16 rows (all ACTIVE).

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | SatisfactionStatus |
|---|---|---|---|---|---|---|---|---|---|
| DEP-026-01-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0027 | Scope Item SOW-0027 — PKG-026 | HIGH | SATISFIED |
| DEP-026-01-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-002 | OBJ-002 — 03-25 compressor station scope | HIGH | TBD |
| DEP-026-01-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | OBJ-004 — Vendor/EPC package execution | HIGH | TBD |
| DEP-026-01-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | OBJ-005 — Facility electrical power basis | HIGH | TBD |
| DEP-026-01-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | OBJ-006 — Controls and instrumentation integration | HIGH | TBD |
| DEP-026-01-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | OBJ-008 — Civil/structural/foundations scope | HIGH | TBD |
| DEP-026-01-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | OBJ-009 — Safety/regulatory requirements | HIGH | TBD |
| DEP-026-01-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | OBJ-010 — Handoff and closure evidence | HIGH | TBD |
| DEP-026-01-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | PACKAGE_REGISTER.csv (Gate 7) row PKG-026 | HIGH | SATISFIED |
| DEP-026-01-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | DELIVERABLE_REGISTER.csv (Gate 7) rows DEL-026-01..06 | HIGH | SATISFIED |
| DEP-026-01-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | 3-25 Comp_and_Liquids DBM (L720–L750; L505; L762) | HIGH | SATISFIED |
| DEP-026-01-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-026-02_package-datasheet | Package Datasheet (DEL-026-02) | HIGH | TBD |
| DEP-026-01-013 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-026-03_construction-work-package | Construction Work Package (DEL-026-03) | HIGH | TBD |
| DEP-026-01-014 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | INTERFACE | DELIVERABLE | DEL-026-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package (DEL-026-04) | MEDIUM | TBD |
| DEP-026-01-015 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | INTERFACE | DELIVERABLE | DEL-026-05_vendor-document-turnover-package | Vendor Document Turnover Package (DEL-026-05) | MEDIUM | TBD |
| DEP-026-01-016 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | INTERFACE | DELIVERABLE | DEL-026-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance (DEL-026-06) | MEDIUM | TBD |

## Run Notes

- **Run date:** 2026-05-25
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; documents found: Datasheet.md (ANCHOR_DOC), Specification.md, Guidance.md, Procedure.md (EXECUTION_DOC_ORDER)
- **ANCHOR_DOC chosen:** Datasheet.md (contains identification, objectives, scope-item fields; Specification.md also served as primary anchor signal)
- **DECOMPOSITION_PATH used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — confirmed accessible; PACKAGE_REGISTER.csv, DELIVERABLE_REGISTER.csv, SCOPE_LEDGER.csv, OBJECTIVE_REGISTER.csv read for validation and label resolution.
- **Anchor validation:** SOW-0027 confirmed in SCOPE_LEDGER.csv (PKG-026). OBJ-002/004/005/006/008/009/010 confirmed in OBJECTIVE_REGISTER.csv and DELIVERABLE_REGISTER.csv row DEL-026-01.
- **Parent anchor count:** 1 (DEP-026-01-001 IMPLEMENTS_NODE → SOW-0027). No FLOATING_NODE warning.
- **Existing Dependencies.csv:** Did not exist prior to this run; created fresh.
- **No FLOATING_NODE or AMBIGUOUS_ANCHOR warnings.**
- **Open items noted in source documents (not extracted as dependencies — out of scope for this register):**
  - CFL-026-01-01..04 in Guidance.md: identity vs. DBM conflicts (carried in source; not dependency edges).
  - HRR-026-01-001..002: need human ruling on identity reconciliation (carried in Guidance.md; not dependency edges).
  - TBD items (6.9 kV loads, 0.4 kV secondary, cooling class): carried as TBD in source docs; SatisfactionStatus TBD on objective traces.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 16 |
| RETIRED | 0 |

| DependencyClass | ACTIVE |
|---|---|
| ANCHOR | 8 |
| EXECUTION | 8 |

| SatisfactionStatus | Count |
|---|---|
| SATISFIED | 3 |
| TBD | 13 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract skill run; MODE=UPDATE; STRICTNESS=CONSERVATIVE; decomposition GATE-07 snapshot used; 16 ACTIVE rows written to Dependencies.csv (8 ANCHOR + 8 EXECUTION); schema validation VALID.
