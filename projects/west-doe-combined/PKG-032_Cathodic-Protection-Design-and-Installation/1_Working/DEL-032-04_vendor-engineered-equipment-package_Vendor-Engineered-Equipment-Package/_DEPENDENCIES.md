# Dependencies: DEL-032-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

16 rows extracted (all ACTIVE). Schema version: v3.1.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | SatisfactionStatus | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| DEP-032-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0033 | Cathodic Protection Design and Installation scope item | SATISFIED | HIGH |
| DEP-032-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-002 | 03-25 compressor station and liquids hub scope | SATISFIED | HIGH |
| DEP-032-04-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Electrical/mechanical vendor-owned package execution | SATISFIED | HIGH |
| DEP-032-04-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Facility electrical power basis incl. cathodic protection | SATISFIED | HIGH |
| DEP-032-04-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Controls instrumentation communications integration | SATISFIED | HIGH |
| DEP-032-04-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Safety regulatory codes and standards requirements | SATISFIED | HIGH |
| DEP-032-04-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Vendor documentation commissioning turnover closure | SATISFIED | HIGH |
| DEP-032-04-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-032-01_scope-of-work | Scope of Work | TBD | HIGH |
| DEP-032-04-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-032-02_package-datasheet | Package Datasheet | TBD | HIGH |
| DEP-032-04-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | DELIVERABLE | DEL-032-03_construction-work-package | Construction Work Package | TBD | HIGH |
| DEP-032-04-011 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-032-05_vendor-document-turnover-package | Vendor Document Turnover Package | TBD | HIGH |
| DEP-032-04-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-032-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance | TBD | HIGH |
| DEP-032-04-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | UNKNOWN | IFC-C2719906C1 | Electrical Power interface | TBD | HIGH |
| DEP-032-04-014 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | UNKNOWN | IFC-F1FE9DF9DD | Grounding / Bonding interface | TBD | HIGH |
| DEP-032-04-015 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | UNKNOWN | IFC-4D092EC70F | I&C / Control Cabling interface | TBD | HIGH |
| DEP-032-04-016 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | UNKNOWN | IFC-8594557BD3 | Communications / Network interface | TBD | HIGH |

## Run Notes

- **Run date:** 2026-05-25
- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **Source docs scanned (AUTO):** `_CONTEXT.md`, `Datasheet.md`, `Procedure.md`, `Specification.md`, `Guidance.md`
- **Anchor doc (AUTO):** `Datasheet.md` (contains explicit WBS, scope item, and objective references)
- **Execution docs (AUTO order):** `Procedure.md` (prerequisites/steps), `Specification.md` (scope/requirements/exclusions), `Guidance.md` (principles/conflict table)
- **Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`
  - SOW-0033 validated in SCOPE_LEDGER.csv — FOUND
  - All six objective IDs (OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-009, OBJ-010) validated in OBJECTIVE_REGISTER.csv — FOUND
  - DEL-032-01 through DEL-032-06 validated in DELIVERABLE_REGISTER.csv — FOUND
- **`_REFERENCES.md` used:** Yes — for TargetLocation path resolution on deliverable targets. Interface register IDs sourced from `INTERFACE_REGISTER.csv` as cited in source documents.
- **DECOMPOSITION_PATH from brief:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/GATE-07_Final_Published_2026-05-24/` — path did not exist as provided; actual snapshot located at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` via `_CONTEXT.md` Decomposition Reference — used actual path.
- **Interface rows (DEP-032-04-013 through -016):** `TargetType=UNKNOWN` because INTERFACE_REGISTER row type is not a canonical TargetType; `TargetRefID` carries the IFC identifier as the stable pointer.
- **Parent anchor check:** 1 IMPLEMENTS_NODE row (DEP-032-04-001) — OK.
- **No warnings:** No FLOATING_NODE; no AMBIGUOUS_ANCHOR; no MISSING_DECOMPOSITION.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 16 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| SATISFIED | 7 (anchor rows — parent node and objectives confirmed in decomposition) |
| TBD | 9 (execution rows — not yet closeable at deliverable initialization) |

| DependencyClass | ACTIVE count |
|---|---|
| ANCHOR | 7 |
| EXECUTION | 9 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — EXTRACTED run; MODE=UPDATE; STRICTNESS=CONSERVATIVE; CONSUMER_CONTEXT=NONE; 16 rows written (7 ANCHOR, 9 EXECUTION); schema v3.1; decomposition validated at GATE-07_Final_Published_2026-05-24; no warnings.
