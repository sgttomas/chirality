# Dependencies: DEL-038-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1); this file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

9 rows extracted (all ACTIVE). Schema version: v3.1.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetID / TargetName | SatisfactionStatus | Confidence |
|---|---|---|---|---|---|---|---|---|
| DEP-038-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-038 — 600V ELECTRICAL BUILDING (820-1) | TBD | HIGH |
| DEP-038-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0039 | TBD | HIGH |
| DEP-038-04-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | TBD | HIGH |
| DEP-038-04-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | TBD | HIGH |
| DEP-038-04-005 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-038-01_scope-of-work | TBD | HIGH |
| DEP-038-04-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-038-02_package-datasheet | TBD | HIGH |
| DEP-038-04-007 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-038-05_vendor-document-turnover-package | TBD | HIGH |
| DEP-038-04-008 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-038-06_epc-vendor-package-review-and-acceptance | TBD | HIGH |
| DEP-038-04-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | DELIVERABLE | DEL-038-03_construction-work-package | TBD | MEDIUM |

Note on objective traces: Only OBJ-001 and OBJ-004 are extracted as individual rows here (CONSERVATIVE mode). OBJ-005 through OBJ-010 are referenced in DELIVERABLE_REGISTER.csv but are not individually evidenced in the deliverable source documents. The full objective set (OBJ-001; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010) is confirmed by DELIVERABLE_REGISTER.csv but individual rows were not emitted to avoid redundant traces without direct source evidence per CONSERVATIVE strictness.

## Run Notes

- **Run date:** 2026-05-25
- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **Scope:** DEL-038-04
- **Run root:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined`
- **Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` (confirmed present; used for anchor validation and canonical label resolution)
- **DECOMPOSITION_PATH from brief:** `GATE-07_Final_Published_2026-05-24/` — resolved to full path above.
- **Source documents scanned (AUTO):** `Datasheet.md`, `Guidance.md`, `Procedure.md`, `Specification.md`
- **ANCHOR_DOC (AUTO):** `Datasheet.md` (contains identification, parent package, source traceability fields)
- **EXECUTION_DOC_ORDER (AUTO):** `Procedure.md` (primary workflow signals), `Specification.md` (exclusion/requirement signals), `Guidance.md` (considerations)
- **_REFERENCES.md:** Read; confirmed decomposition snapshot path. No local document paths resolved for non-deliverable targets.
- **Existing Dependencies.csv:** Not present — created fresh.

**Warnings:**
- None. One IMPLEMENTS_NODE parent anchor found (DEP-038-04-001). No FLOATING_NODE or AMBIGUOUS_ANCHOR condition.
- CONSERVATIVE strictness applied: objective traces limited to rows with direct in-document evidence (OBJ-001, OBJ-004). Remaining objectives (OBJ-005–OBJ-010) are registered in the decomposition but not individually extracted here; they may be added in a subsequent AGGRESSIVE or DECLARED run.
- CFL-038-04-001 (voltage-class conflict for building 820-1) is an open item carried in source documents; it does not create additional dependency rows but affects SatisfactionStatus for upstream PREREQUISITE rows (kept TBD).

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 9 |
| RETIRED | 0 |
| **Total** | **9** |

| SatisfactionStatus | Count (ACTIVE) |
|---|---|
| TBD | 9 |
| PENDING | 0 |
| SATISFIED | 0 |

| DependencyClass | Count (ACTIVE) |
|---|---|
| ANCHOR | 4 |
| EXECUTION | 5 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — UPDATE run; dependency-extract skill; CONSERVATIVE strictness; decomposition path GATE-07_Final_Published_2026-05-24 confirmed; 9 rows extracted (4 ANCHOR, 5 EXECUTION); no warnings; Dependencies.csv created.
