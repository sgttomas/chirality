# Dependencies: DEL-007-04_epc-civil-discipline-production-package — EPC / Civil Discipline Production Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** DECLARED + EXTRACTED (dependency-extract run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1). This file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` generated 2026-05-25 by `TASK + dependency-extract`.

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetRefID / TargetDeliverableID | TargetName | Status | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| DEP-007-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0007 | Scope decision SOW-0007 — Retention Pond (WBS 02) | ACTIVE | HIGH |
| DEP-007-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-002 | Project Objective OBJ-002 — 03-25 compressor station and liquids hub scope | ACTIVE | HIGH |
| DEP-007-04-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | Project Objective OBJ-007 — Shared utilities and ancillary support systems | ACTIVE | HIGH |
| DEP-007-04-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Project Objective OBJ-008 — Civil structural site buildings grading containment | ACTIVE | HIGH |
| DEP-007-04-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 — Safety relief flare drain containment environmental regulatory | ACTIVE | HIGH |
| DEP-007-04-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | CIV-235633-5002-001 | Plot plan drawing CIV-235633-5002-001 — approximate retention pond location | ACTIVE | HIGH |
| DEP-007-04-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | EXTERNAL | GEOTECH-REPORT | Geotechnical assessment report — bearing capacity lateral pile design pavement design | ACTIVE | HIGH |
| DEP-007-04-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | EXTERNAL | TOPO-SURVEY | Topographical survey and grade surface file — existing ground model grading drainage | ACTIVE | HIGH |
| DEP-007-04-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | EXTERNAL | DRAINAGE-DESIGN | Detailed engineering drainage design — final IDF duration ditch culvert sizing pond capacity | ACTIVE | HIGH |
| DEP-007-04-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-007-01_scope-of-work | Scope of Work — PKG-007 Retention Pond | ACTIVE | MEDIUM |
| DEP-007-04-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-AB14FD2A67 | Interface IFC-AB14FD2A67 — Drain / Containment | ACTIVE | HIGH |
| DEP-007-04-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-1B8CFB3D40 | Interface IFC-1B8CFB3D40 — Grading / Site Drainage / Spill Containment | ACTIVE | HIGH |

**Counts:** 12 ACTIVE rows (5 ANCHOR, 7 EXECUTION); 0 RETIRED.

## Run Notes

- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; source docs used: `Datasheet.md` (ANCHOR_DOC), `Procedure.md`, `Specification.md`, `Guidance.md` (EXECUTION_DOC_ORDER).
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` (resolved via `_REFERENCES.md`; confirmed reachable).
- **Decomposition used for:** anchor validation (SOW-0007 in SCOPE_LEDGER.csv; objectives OBJ-002/007/008/009 in OBJECTIVE_REGISTER.csv; DEL-007-04 in DELIVERABLE_REGISTER.csv).
- **_REFERENCES.md:** Read; used to resolve decomposition path and confirm source slice paths.
- **ANCHOR rows:** 1 IMPLEMENTS_NODE (SOW-0007); 4 TRACES_TO_REQUIREMENT (OBJ-002, OBJ-007, OBJ-008, OBJ-009). All confirmed in Gate 7 registers.
- **EXECUTION rows:** 4 external/document prerequisites (plot plan CIV-235633-5002-001, geotechnical report, topographical survey, detailed drainage design); 1 intra-package deliverable prerequisite (DEL-007-01); 2 interface document dependencies (IFC-AB14FD2A67, IFC-1B8CFB3D40).
- **DEP-007-04-010 note:** ASSUMPTION flag — Procedure.md names the Gate 7 snapshot as a prerequisite; DEL-007-01 Scope of Work is the intra-package deliverable most directly carrying that accepted scope basis. Confidence=MEDIUM.
- **External TargetRefIDs (GEOTECH-REPORT, TOPO-SURVEY, DRAINAGE-DESIGN):** Descriptive IDs assigned; no stable project IDs exist in source for these items. TargetType=EXTERNAL.
- **Interface targets (IFC-AB14FD2A67, IFC-1B8CFB3D40):** Recorded as TargetType=DOCUMENT referencing INTERFACE_REGISTER.csv entries; these are interface facts, not deliverable IDs.
- **No coordination-only or structural-adjacency edges created.**
- **No downstream edges extracted** — no source text states explicit outputs consumed by another identified deliverable.
- **Hydrology uncertainty** (NBCC 2020 proxy) noted in Datasheet.md and Guidance.md; captured in DEP-007-04-009 (drainage design prerequisite) scope; not emitted as a separate row because it is a condition on an existing prerequisite, not a separate information transfer.
- **Tree x DAG integrity:** 1 IMPLEMENTS_NODE anchor found — no FLOATING_NODE or AMBIGUOUS_ANCHOR warnings.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First extraction run: `dependency-extract`, MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Generated `Dependencies.csv` v3.1 with 12 ACTIVE rows (5 ANCHOR, 7 EXECUTION). No retired rows. Schema validation: VALID.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 12 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 12 |
