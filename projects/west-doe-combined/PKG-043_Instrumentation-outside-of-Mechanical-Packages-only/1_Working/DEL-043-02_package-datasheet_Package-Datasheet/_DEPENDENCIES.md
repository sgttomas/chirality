# Dependencies: DEL-043-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is authoritative (v3.1 schema, 29 columns); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

---

## Extracted Dependency Register

**Total rows:** 10 ACTIVE | 0 RETIRED
**ANCHOR rows:** 7 (1 IMPLEMENTS_NODE + 6 TRACES_TO_REQUIREMENT)
**EXECUTION rows:** 3 (1 UPSTREAM PREREQUISITE + 2 DOWNSTREAM HANDOVER)

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | SatisfactionStatus | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| DEP-043-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0044 | Instrumentation (outside of Mechanical Packages only) — WBS 01 | TBD | HIGH |
| DEP-043-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | Provide the 04-25 Deepcut facility scope | TBD | MEDIUM |
| DEP-043-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-003 | Preserve commercial stream disposition and facility boundary interfaces | TBD | MEDIUM |
| DEP-043-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | TBD | TBD | MEDIUM |
| DEP-043-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | TBD | TBD | MEDIUM |
| DEP-043-02-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | TBD | TBD | MEDIUM |
| DEP-043-02-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | TBD | TBD | MEDIUM |
| DEP-043-02-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-043-01_scope-of-work | Scope of Work (Tagged equipment and package identity list) | PENDING | HIGH |
| DEP-043-02-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-043-03_construction-work-package | Construction Work Package | TBD | MEDIUM |
| DEP-043-02-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-043-04_epc-instrumentation-discipline-production-package | EPC / Instrumentation Discipline Production Package | TBD | MEDIUM |

---

## Run Notes

**Run date:** 2026-05-25
**Mode:** UPDATE
**Strictness:** CONSERVATIVE
**DependencyID format:** DEP-043-02-NNN
**Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
**Decomposition status:** FOUND — used for anchor validation, label resolution, and target ID confirmation.
**CONSUMER_CONTEXT:** NONE

**SOURCE_DOCS scanned (AUTO):**
- `Datasheet.md` — ANCHOR_DOC (contains "datasheet" in filename; carries identification, scope items, objectives, and interface inventory)
- `_CONTEXT.md` — supporting anchor/scope confirmation
- `Specification.md` — execution signals (out-of-scope / downstream deliverable statements)
- `Procedure.md` — execution signals (prerequisite: DEL-043-01 tagged equipment list)
- `Guidance.md` — directional context; no new execution edges beyond what Procedure/Specification provide

**Pass 1 — ANCHOR:**
- Parent anchor (IMPLEMENTS_NODE): SOW-0044 confirmed in SCOPE_LEDGER.csv and DELIVERABLE_REGISTER.csv row 241. Confidence HIGH.
- Trace anchors (TRACES_TO_REQUIREMENT): OBJ-001, OBJ-003, OBJ-005, OBJ-006, OBJ-007, OBJ-010 — confirmed in OBJECTIVE_DELIVERABLE_MAP.csv but recorded under PACKAGE_HEURISTIC. Confidence MEDIUM (ASSUMPTION noted per source). OBJ-001 and OBJ-003 labels resolved from OBJECTIVE_REGISTER.csv. OBJ-005/006/007/010 labels not read in this pass; TargetName set to TBD.

**Pass 2 — EXECUTION:**
- DEP-043-02-008 (UPSTREAM PREREQUISITE): Procedure.md Step 6 explicitly states "Cross-reference DEL-043-01 Tagged equipment and package identity list (ART-75803D0212) once produced"; SatisfactionStatus=PENDING (DEL-043-01 not yet produced).
- DEP-043-02-009 (DOWNSTREAM HANDOVER): Specification.md explicitly demarcates DEL-043-03 as the downstream consumer for construction execution; datasheet is the Gate 5 EPC anchor technical basis.
- DEP-043-02-010 (DOWNSTREAM HANDOVER): Specification.md explicitly demarcates DEL-043-04 as the downstream discipline production package; datasheet is the anchor basis cited there.
- Interface dependency edges (IFC-AE83B2D0FC, IFC-F41620D435, IFC-E5A8000199, IFC-4929B68CCD, IFC-35EBF9CD91): The five Gate 6 interface facts are carried as evidence within this deliverable (not external dependencies); no execution dependency edge emitted — consistent with _CONTEXT.md Notes stating "interface facts are intentionally carried here as evidence rather than standalone deliverables."

**Warnings:**
- None. One parent anchor found (IMPLEMENTS_NODE). No FLOATING_NODE. No AMBIGUOUS_ANCHOR.

---

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 10 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 9 |
| PENDING | 1 |

| DependencyClass | ACTIVE |
|---|---|
| ANCHOR | 7 |
| EXECUTION | 3 |

---

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract skill run; MODE=UPDATE, STRICTNESS=CONSERVATIVE; decomposition=GATE-07_Final_Published_2026-05-24; 10 rows extracted (7 ANCHOR, 3 EXECUTION), 0 RETIRED; schema VALID (29 columns); no warnings.
