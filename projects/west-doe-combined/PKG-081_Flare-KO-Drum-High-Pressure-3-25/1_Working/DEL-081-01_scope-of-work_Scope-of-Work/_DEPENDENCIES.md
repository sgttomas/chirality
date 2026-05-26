# Dependencies: DEL-081-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-26)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1 schema); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` produced by `TASK + dependency-extract` run 2026-05-26.

**Schema version:** v3.1  
**Total rows:** 20  
**ACTIVE rows:** 20  
**RETIRED rows:** 0

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-081-01-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | PACKAGE | PKG-081 | Flare KO Drum (High Pressure) 3-25 | HIGH | ACTIVE |
| DEP-081-01-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0071 | Carry PKG-081 as distinct flat project package | HIGH | ACTIVE |
| DEP-081-01-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0072 | Basic scope: supply two HP flare KO drums and two dedicated transfer pumps | HIGH | ACTIVE |
| DEP-081-01-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0073 | Major included equipment: V-4100-2, V-4150-2, P-4100-2, P-4150-2 | HIGH | ACTIVE |
| DEP-081-01-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0074 | Scope conflict open item — flare system boundary ruling required | HIGH | ACTIVE |
| DEP-081-01-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-002 | Facility-level objective OBJ-002 | MEDIUM | ACTIVE |
| DEP-081-01-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Facility-level objective OBJ-004 | MEDIUM | ACTIVE |
| DEP-081-01-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Facility-level objective OBJ-005 | MEDIUM | ACTIVE |
| DEP-081-01-009 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Facility-level objective OBJ-006 | MEDIUM | ACTIVE |
| DEP-081-01-010 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | Facility-level objective OBJ-007 | MEDIUM | ACTIVE |
| DEP-081-01-011 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Facility-level objective OBJ-008 | MEDIUM | ACTIVE |
| DEP-081-01-012 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Facility-level objective OBJ-009 | MEDIUM | ACTIVE |
| DEP-081-01-013 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Facility-level objective OBJ-010 | MEDIUM | ACTIVE |
| DEP-081-01-014 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-081-02_package-datasheet | Package Datasheet | HIGH | ACTIVE |
| DEP-081-01-015 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-081-03_construction-work-package | Construction Work Package | HIGH | ACTIVE |
| DEP-081-01-016 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-081-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package | HIGH | ACTIVE |
| DEP-081-01-017 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-081-05_vendor-document-turnover-package | Vendor Document Turnover Package | HIGH | ACTIVE |
| DEP-081-01-018 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-081-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance | HIGH | ACTIVE |
| DEP-081-01-019 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | GATE-07_Final_Published_2026-05-24 | Gate-7 PROJECT_DECOMP snapshot | HIGH | ACTIVE |
| DEP-081-01-020 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | DBM-3-25 | _Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md | HIGH | ACTIVE |

**ANCHOR rows:** 13 (1 IMPLEMENTS_NODE + 4 SOW requirement traces + 8 OBJ requirement traces)  
**EXECUTION rows:** 7 (5 DOWNSTREAM HANDOVER + 2 UPSTREAM PREREQUISITE)

## Run Notes

- **Run date:** 2026-05-26
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **RUN_ROOT:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined`
- **DECOMPOSITION_PATH (resolved):** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - Provided path `GATE-07_Final_Published_2026-05-24` in brief did not exist at `projects/west-doe-combined/GATE-07_Final_Published_2026-05-24/`. Resolved via `_REFERENCES.md` "Authoritative Decomposition Basis" section, which points to the gate snapshot under `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`. Path confirmed accessible. NON-BLOCKING.
- **SOURCE_DOCS (AUTO):** `Datasheet.md` (ANCHOR_DOC — contains 'scope', 'datasheet', identification table), `Specification.md`, `Procedure.md`, `Guidance.md`
- **ANCHOR_DOC (AUTO):** `Datasheet.md` — highest-confidence match (contains 'datasheet', 'scope'; identification table with Covers Scope Items and Supports Objectives)
- **EXECUTION_DOC_ORDER (AUTO):** `Procedure.md` (primary — contains 'procedure'; explicit prerequisites/purpose), `Specification.md`, `Guidance.md`
- **Pass 1 (ANCHOR):** Parent anchor `IMPLEMENTS_NODE` to PKG-081 confirmed via PACKAGE_REGISTER.csv and DELIVERABLE_REGISTER.csv. Four SOW scope item traces (SOW-0071..SOW-0074) and eight objective traces (OBJ-002, OBJ-004..OBJ-010) confirmed via Datasheet.md identification table, Specification.md REQ-SOW-* rows, and SCOPE_LEDGER.csv / OBJECTIVE_DELIVERABLE_MAP.csv.
- **Pass 2 (EXECUTION):** Five downstream HANDOVER edges extracted from Procedure.md § Purpose, which explicitly names DEL-081-02 through DEL-081-06 as consumers. Two upstream PREREQUISITE edges (Gate-7 snapshot, 3-25 DBM) extracted from Procedure.md § Prerequisites.
- **OBJ traces:** Labeled ASSUMPTION (PACKAGE_HEURISTIC) per Datasheet.md and Specification.md REQ-SOW-10; Confidence=MEDIUM per skill CONSERVATIVE posture.
- **Inaccessible sources:** `26020-Package_Requirements.docx` (binary) and `W242510-PRC-REP-000003-001` (not in workspace) are noted in source documents as `location TBD`. No EXECUTION dependency rows emitted for these; they are cited within source-document evidence but do not constitute explicit information-flow dependencies that can be conservatively extracted.
- **No upstream deliverable dependencies:** Procedure.md § Prerequisites "Declared upstream dependencies: None declared at PREPARATION." No upstream deliverable-level execution edges extracted.
- **Parent anchor check:** 1 IMPLEMENTS_NODE row found. OK.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-26 — TASK+dependency-extract run; MODE=UPDATE; STRICTNESS=CONSERVATIVE; CONSUMER_CONTEXT=NONE; decomposition resolved via _REFERENCES.md; 20 rows extracted (13 ANCHOR + 7 EXECUTION); all ACTIVE.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 20 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 20 |

| DependencyClass | Count |
|---|---|
| ANCHOR | 13 |
| EXECUTION | 7 |
