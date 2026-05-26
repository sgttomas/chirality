# Dependencies: DEL-036-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (Dependencies.csv v3.1 produced)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` produced by `TASK + dependency-extract` (run 2026-05-25).

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-036-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | WBS-01 | WBS 01 — PKG-036 facility scope node | ACTIVE |
| DEP-036-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0037 | SOW-0037 — 6.9kV SWITCHGEAR ELECTRICAL BUILDING package scope item | ACTIVE |
| DEP-036-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | OBJ-001 | ACTIVE |
| DEP-036-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | OBJ-004 | ACTIVE |
| DEP-036-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | OBJ-005 | ACTIVE |
| DEP-036-02-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | OBJ-006 | ACTIVE |
| DEP-036-02-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | OBJ-007 | ACTIVE |
| DEP-036-02-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | OBJ-008 | ACTIVE |
| DEP-036-02-009 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | OBJ-009 | ACTIVE |
| DEP-036-02-010 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | OBJ-010 | ACTIVE |
| DEP-036-02-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-036-01_scope-of-work | Scope of Work — DEL-036-01 | ACTIVE |
| DEP-036-02-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-036-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package — DEL-036-04 | ACTIVE |
| DEP-036-02-013 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-036-03_construction-work-package | Construction Work Package — DEL-036-03 | ACTIVE |

**Totals:** 13 rows — 10 ANCHOR + 3 EXECUTION; all ACTIVE.

## Run Notes

- **Run date:** 2026-05-25
- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **SOURCE_DOCS (AUTO):** Datasheet.md (ANCHOR_DOC), Guidance.md (EXECUTION_DOC), _CONTEXT.md (identity/scope resolution)
- **Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
- **Decomposition status:** PRESENT — WBS, SOW, objective, and sibling deliverable IDs resolved from PACKAGE_REGISTER.csv, SCOPE_LEDGER.csv, DELIVERABLE_REGISTER.csv.
- **Parent anchor check:** 1 IMPLEMENTS_NODE row (DEP-036-02-001 → WBS-01). PASS.
- **ID format:** FromPackageID = PKG-036, FromDeliverableID = DEL-036-02_package-datasheet. No anomalies.
- **Enum normalization:** No legacy variants encountered.
- **Tree x DAG integrity:** PASS. One parent anchor; eight requirement trace anchors (OBJ-001, OBJ-004 through OBJ-010); one SOW trace anchor.
- **EXECUTION pass notes:**
  - DEP-036-02-011 (UPSTREAM PREREQUISITE → DEL-036-01): Explicit in Guidance.md — "The Package Datasheet exists to convert the accepted Gate 7 package basis for PKG-036 into a source-supported technical handoff document." Confidence HIGH.
  - DEP-036-02-012 (DOWNSTREAM ENABLES → DEL-036-04): Explicit in Datasheet.md Identification — datasheet is the "vendor engineering handoff basis." Confidence HIGH.
  - DEP-036-02-013 (DOWNSTREAM ENABLES → DEL-036-03): Implicit — datasheet Construction section provides the integration and interface basis used in the CWP. Marked ASSUMPTION. Confidence MEDIUM.
- **No warnings issued.**

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 13 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| SATISFIED | 10 |
| TBD | 3 |

ANCHOR rows (10) are SATISFIED as they bind to confirmed decomposition identifiers. EXECUTION rows (3) carry TBD satisfaction pending downstream consumption and explicit fulfillment acknowledgment.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract run; MODE=UPDATE; STRICTNESS=CONSERVATIVE; CONSUMER_CONTEXT=NONE; decomposition PRESENT; 13 rows extracted (10 ANCHOR + 3 EXECUTION); schema VALID; no warnings. (TASK + dependency-extract)
