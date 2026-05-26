# Dependencies: DEL-008-03_construction-work-package — Construction Work Package

**Coordination Mode:** DECLARED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1). This file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

16 rows extracted and registered. All rows ACTIVE.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName (short) | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-008-03-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0008 | Scope decision SOW-0008 — Controls system design and integration | HIGH | ACTIVE |
| DEP-008-03-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | Project Objective OBJ-001 | HIGH | ACTIVE |
| DEP-008-03-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-003 | Project Objective OBJ-003 | HIGH | ACTIVE |
| DEP-008-03-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Project Objective OBJ-005 | HIGH | ACTIVE |
| DEP-008-03-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Project Objective OBJ-006 | HIGH | ACTIVE |
| DEP-008-03-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | Project Objective OBJ-007 | HIGH | ACTIVE |
| DEP-008-03-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Project Objective OBJ-008 | HIGH | ACTIVE |
| DEP-008-03-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 | HIGH | ACTIVE |
| DEP-008-03-009 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 | HIGH | ACTIVE |
| DEP-008-03-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | Gate 7 PROJECT_DECOMP snapshot | HIGH | ACTIVE |
| DEP-008-03-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | DBM-Deepcut SEC-12 Cable Wire and Raceways | HIGH | ACTIVE |
| DEP-008-03-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | DBM-Deepcut SEC-13 Controls System Basis | HIGH | ACTIVE |
| DEP-008-03-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | DBM-Deepcut SEC-14 Instrumented Protection Basis | HIGH | ACTIVE |
| DEP-008-03-014 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | EXTERNAL | — | Client IT/OT — IDMZ / enterprise network / switch config | MEDIUM | ACTIVE |
| DEP-008-03-015 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | DOCUMENT | — | Final detailed-design docs / construction drawings / safety studies | HIGH | ACTIVE |
| DEP-008-03-016 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-008-04_epc-controls-discipline-production-package | EPC / Controls Discipline Production Package | MEDIUM | ACTIVE |

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 16 |
| RETIRED | 0 |

**ANCHOR rows:** 9 (1 IMPLEMENTS_NODE + 8 TRACES_TO_REQUIREMENT)
**EXECUTION rows:** 7 (5 UPSTREAM, 1 DOWNSTREAM, 1 mixed-direction constraint)

SatisfactionStatus breakdown:
- SATISFIED: 1 (DEP-008-03-010 — Gate 7 snapshot available at run)
- PENDING: 4 (DEP-008-03-011, 012, 013, 014, 015)
- TBD: 10 (all ANCHOR rows + DEP-008-03-016)

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned: `Datasheet.md`, `Procedure.md`, `Guidance.md`, `Specification.md`, `_CONTEXT.md`, `_REFERENCES.md`
- **ANCHOR_DOC:** `Datasheet.md` (highest-confidence match; contains identification, scope item, and objective cross-references)
- **EXECUTION_DOC_ORDER:** `Procedure.md` (primary execution signals), `Guidance.md` (constraint/trade-off signals), `Datasheet.md` (supplementary)
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — resolved from `_REFERENCES.md` and confirmed present. Brief specified path `GATE-07_Final_Published_2026-05-24/` (not found at brief-specified location); resolved to actual path under `_Decomposition/PROJECT_DECOMP/_GateSnapshots/`. No decomposition warning required — snapshot located.
- **DependencyID format:** DEP-008-03-NNN
- Parent anchor confirmed: 1 IMPLEMENTS_NODE row (DEP-008-03-001, SOW-0008). No FLOATING_NODE warning.
- No AMBIGUOUS_ANCHOR — exactly one IMPLEMENTS_NODE.
- DEP-008-03-015 carries source text label ASSUMPTION (Procedure.md explicitly uses that epistemic label for the detailed-design documents dependency).
- DEP-008-03-016 boundary relationship with DEL-008-04 extracted from Guidance.md trade-off table; direction DOWNSTREAM because CWP boundary definition constrains/handovers to the sibling production package boundary. Conservative — not a hard blocking prerequisite.
- Client IT/OT (DEP-008-03-014): TargetLocation TBD — no local path exists; client governance artifact.
- Final detailed-design docs (DEP-008-03-015): TargetLocation TBD — not currently in `_Sources`.
- No `_REFERENCES.md` document pointers resolve to local paths beyond the DBM and decomposition already cited.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract skill run. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition: GATE-07_Final_Published_2026-05-24 (located). Source docs scanned: Datasheet.md, Procedure.md, Guidance.md. 16 rows extracted (9 ANCHOR, 7 EXECUTION). 0 rows retired. Warnings: none.
