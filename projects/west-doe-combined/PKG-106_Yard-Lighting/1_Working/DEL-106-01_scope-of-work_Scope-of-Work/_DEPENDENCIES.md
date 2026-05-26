# Dependencies: DEL-106-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** DECLARED + EXTRACTED
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1). This file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Last extraction run: 2026-05-26 (MODE=UPDATE, STRICTNESS=CONSERVATIVE)

**Counts:**
- Total rows: 13
- ACTIVE: 12
- RETIRED: 1 (DEP-106-01-E001 — decomposition-snapshot authoring prerequisite; retired as self-referential process input, not a peer-deliverable dependency)

### ANCHOR rows (ACTIVE: 7)

| DependencyID | AnchorType | Direction | TargetType | TargetRefID / TargetName | Confidence |
|---|---|---|---|---|---|
| DEP-106-01-A001 | IMPLEMENTS_NODE | UPSTREAM | WBS_NODE | PKG-106 Yard Lighting | HIGH |
| DEP-106-01-A002 | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | SOW-0011 | HIGH |
| DEP-106-01-A003 | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | OBJ-001 | MEDIUM |
| DEP-106-01-A004 | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | OBJ-004 | MEDIUM |
| DEP-106-01-A005 | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | OBJ-005 | MEDIUM |
| DEP-106-01-A006 | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | OBJ-009 | MEDIUM |
| DEP-106-01-A007 | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | OBJ-010 | MEDIUM |

### EXECUTION rows (ACTIVE: 5, RETIRED: 1)

| DependencyID | Direction | DependencyType | TargetDeliverableID | Status |
|---|---|---|---|---|
| DEP-106-01-E001 | UPSTREAM | PREREQUISITE | DEL-106-01_scope-of-work (self) | RETIRED |
| DEP-106-01-E002 | DOWNSTREAM | HANDOVER | DEL-106-02_package-datasheet | ACTIVE |
| DEP-106-01-E003 | DOWNSTREAM | HANDOVER | DEL-106-03_construction-work-package | ACTIVE |
| DEP-106-01-E004 | DOWNSTREAM | HANDOVER | DEL-106-04_vendor-engineered-equipment-package | ACTIVE |
| DEP-106-01-E005 | DOWNSTREAM | HANDOVER | DEL-106-05_vendor-document-turnover-package | ACTIVE |
| DEP-106-01-E006 | DOWNSTREAM | HANDOVER | DEL-106-06_epc-vendor-package-review-and-acceptance | ACTIVE |

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; documents used: `Datasheet.md` (ANCHOR_DOC), `Procedure.md`, `Specification.md` (EXECUTION_DOC_ORDER), `_CONTEXT.md`
- **ANCHOR_DOC:** `Datasheet.md` (highest-confidence anchor signal by filename heuristic `scope`/`datasheet`)
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — confirmed present; anchor validation performed against PACKAGE_REGISTER.csv, DELIVERABLE_REGISTER.csv, SCOPE_LEDGER.csv, OBJECTIVE_REGISTER.csv
- **Declared DECOMPOSITION_PATH** from `_REFERENCES.md`: `GATE-07_Final_Published_2026-05-24` snapshot — used as authoritative
- **[NOTE] DECOMPOSITION_PATH** provided via `DECOMPOSITION_PATH` parameter was `GATE-07_Final_Published_2026-05-24`; actual path resolved to `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` under RUN_ROOT.
- **Parent anchor:** PKG-106 confirmed in PACKAGE_REGISTER.csv (GATE-07). Single IMPLEMENTS_NODE row emitted — Tree integrity OK.
- **Objective associations** (OBJ-001, OBJ-004, OBJ-005, OBJ-009, OBJ-010): confidence MEDIUM because association is at PACKAGE_HEURISTIC granularity, recorded as ASSUMPTION in Datasheet.md.
- **Downstream handover edges** (DEL-106-02 through DEL-106-06): extracted from Specification.md Excludes section and Procedure.md Prerequisites note ("Downstream deliverables DEL-106-02 … DEL-106-06 consume this SOW."). These are explicit information-flow handovers, not coordination.
- **DEP-106-01-E001 RETIRED:** The decomposition-snapshot read prerequisite is a process/authoring input (tool access), not a peer-deliverable dependency edge; retired immediately to avoid false execution edges.
- **No UPSTREAM execution dependencies extracted:** Procedure.md states "No declared upstream deliverable dependencies" and no source document explicitly states this deliverable requires an artifact from a peer deliverable before it can be produced.

## Lifecycle Summary

| Class | ACTIVE | RETIRED | Total |
|---|---|---|---|
| ANCHOR | 7 | 0 | 7 |
| EXECUTION | 5 | 1 | 6 |
| **Total** | **12** | **1** | **13** |

SatisfactionStatus: all ACTIVE rows are `TBD` (no closure evidence available at INITIALIZED state).

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-26 — dependency-extract skill run (MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE). Created Dependencies.csv v3.1 with 13 rows (12 ACTIVE, 1 RETIRED). Schema VALID (29 columns). All enums validated. Parent anchor: DEP-106-01-A001 (PKG-106, IMPLEMENTS_NODE). Downstream handover edges: DEL-106-02 through DEL-106-06. No upstream execution edges. Decomposition path: GATE-07_Final_Published_2026-05-24.
