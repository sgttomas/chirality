# Dependencies: DEL-061-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (Dependencies.csv produced by TASK + dependency-extract)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Dependencies.csv produced on 2026-05-25. Schema version: v3.1. Total rows: 17. All rows ACTIVE.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName |
|---|---|---|---|---|---|---|---|
| DEP-061-01-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0149 | Scope decision SOW-0149 — NGL Booster and Transfer Pumps Building |
| DEP-061-01-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | Project Objective OBJ-001 |
| DEP-061-01-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-003 | Project Objective OBJ-003 |
| DEP-061-01-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Project Objective OBJ-004 |
| DEP-061-01-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Project Objective OBJ-005 |
| DEP-061-01-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Project Objective OBJ-006 |
| DEP-061-01-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | Project Objective OBJ-007 |
| DEP-061-01-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Project Objective OBJ-008 |
| DEP-061-01-009 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 |
| DEP-061-01-010 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 |
| DEP-061-01-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | — | Gate 7 decomposition registers |
| DEP-061-01-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | DBM-Deepcut 4-25_Deepcut_DBM.md — NGL interface basis |
| DEP-061-01-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | EXTERNAL | — | LACT scope/ownership/design responsibility (TBD facility ruling) |
| DEP-061-01-014 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | 26020-Package_Requirements.docx heading 17 source slice |
| DEP-061-01-015 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-061-02_package-datasheet | Package Datasheet |
| DEP-061-01-016 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-061-03_construction-work-package | Construction Work Package |
| DEP-061-01-017 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-061-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package |

## Run Notes

- **Run date:** 2026-05-25
- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; source documents identified: Datasheet.md (ANCHOR_DOC per `datasheet` pattern), Specification.md, Procedure.md, Guidance.md (EXECUTION_DOCs)
- **DECOMPOSITION_PATH:** Invocation provided `GATE-07_Final_Published_2026-05-24` as a path suffix; resolved to `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PROJECT_DECOMP.md` (and companion CSVs). Confirmed DELIVERABLE_REGISTER.csv and SCOPE_LEDGER.csv for DEL-061-01 and PKG-061.
- **Prior state:** No Dependencies.csv existed; _DEPENDENCIES.md was PREPARATION-initialized with no extracted rows. First extraction run.
- **Pass 1 (ANCHOR):** One IMPLEMENTS_NODE row for SOW-0149 (parent scope decision per SCOPE_LEDGER.csv); nine TRACES_TO_REQUIREMENT rows for OBJ-001 through OBJ-010 (all nine explicitly listed in DELIVERABLE_REGISTER.csv DEL-061-01 row). Decomposition snapshot confirmed all IDs exist.
- **Pass 2 (EXECUTION):** Four upstream rows: two PREREQUISITEs (DBM-Deepcut source, heading 17 source slice), one INTERFACE (Gate 7 decomposition registers — satisfied at current state), one CONSTRAINT (LACT TBD ruling — PENDING). Three downstream ENABLES rows for DEL-061-02, DEL-061-03, DEL-061-04. DEL-061-05 (Vendor Document Turnover) and DEL-061-06 (EPC Vendor Package Review) not emitted as ENABLES rows: the Scope of Work does not explicitly state it produces an artifact directly consumed by DEL-061-05 or DEL-061-06 as a required input in source text; Specification.md only lists them as "related downstream deliverables for traceability" which is structural adjacency, not an explicit information transfer statement.
- **OBJ-006 through OBJ-010:** Full descriptions not read from OBJECTIVE_REGISTER.csv in this run; TargetName populated from ID only. Confidence set to MEDIUM. FACT: IDs are explicitly enumerated in DELIVERABLE_REGISTER.csv row for DEL-061-01.
- **Integrity checks:** One IMPLEMENTS_NODE parent anchor found — no FLOATING_NODE or AMBIGUOUS_ANCHOR warnings. All ACTIVE rows have EvidenceFile and SourceRef populated.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 17 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 11 |
| PENDING | 2 |
| SATISFIED | 4 |

**Anchor rows (ACTIVE):** 10 (1 IMPLEMENTS_NODE + 9 TRACES_TO_REQUIREMENT)
**Execution rows (ACTIVE):** 7 (4 UPSTREAM + 3 DOWNSTREAM)

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First extraction run. MODE=UPDATE; STRICTNESS=CONSERVATIVE; CONSUMER_CONTEXT=NONE. Decomposition: GATE-07_Final_Published_2026-05-24. Created Dependencies.csv v3.1, 17 rows, all ACTIVE. Schema validation: VALID (29 columns). No integrity warnings.
