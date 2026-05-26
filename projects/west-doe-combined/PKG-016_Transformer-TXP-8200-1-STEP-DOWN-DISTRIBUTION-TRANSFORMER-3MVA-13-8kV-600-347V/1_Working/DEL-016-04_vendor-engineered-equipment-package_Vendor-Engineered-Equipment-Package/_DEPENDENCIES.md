# Dependencies: DEL-016-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** DECLARED + EXTRACTED
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1); this file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Extracted by `dependency-extract` skill run on 2026-05-25. Mode: UPDATE. Strictness: CONSERVATIVE.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-016-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0017 | Scope decision SOW-0017 — Transformer TXP-8200-1 (WBS 02) | HIGH | ACTIVE |
| DEP-016-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-002 | Project Objective OBJ-002 — 03-25 compressor station and liquids hub scope | HIGH | ACTIVE |
| DEP-016-04-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Project Objective OBJ-004 — Vendor-owned electrical and mechanical equipment packages | HIGH | ACTIVE |
| DEP-016-04-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Project Objective OBJ-005 — Facility electrical power basis and electrical infrastructure | HIGH | ACTIVE |
| DEP-016-04-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Project Objective OBJ-006 — Controls instrumentation communications and package control interfaces | HIGH | ACTIVE |
| DEP-016-04-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Project Objective OBJ-008 — Civil structural site buildings and foundations scope | HIGH | ACTIVE |
| DEP-016-04-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 — Safety relief flare drain containment fire/gas shutdown regulatory scope | HIGH | ACTIVE |
| DEP-016-04-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 — Operability maintainability vendor documentation commissioning and turnover | HIGH | ACTIVE |
| DEP-016-04-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-016-01_scope-of-work | Scope of Work — DEL-016-01 | HIGH | ACTIVE |
| DEP-016-04-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-016-02_package-datasheet | Package Datasheet — DEL-016-02 | HIGH | ACTIVE |
| DEP-016-04-011 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-016-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance — DEL-016-06 | HIGH | ACTIVE |
| DEP-016-04-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-016-05_vendor-document-turnover-package | Vendor Document Turnover Package — DEL-016-05 | HIGH | ACTIVE |
| DEP-016-04-013 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | INTERFACE | UNKNOWN | IFC-E3BE98E89B | EPC civil/structural foundation and support design for TXP-8200-1 | MEDIUM | ACTIVE |
| DEP-016-04-014 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | UNKNOWN | IFC-0C63CABBEC | 13.8 kV primary feed from upstream 04-25 Main Switchgear Electrical Building | HIGH | ACTIVE |

**Counts:** 14 ACTIVE rows (8 ANCHOR, 6 EXECUTION); 0 RETIRED.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 14 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 14 |

| DependencyClass | Count |
|---|---|
| ANCHOR | 8 |
| EXECUTION | 6 |

Parent anchor (IMPLEMENTS_NODE): 1 (DEP-016-04-001 → SOW-0017). No floating-node warning.

## Run Notes

- **Run date:** 2026-05-25
- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; candidate documents: `Datasheet.md` (ANCHOR_DOC, contains identification/attributes/conditions/references), `Specification.md` (EXECUTION_DOC, requirements), `Procedure.md` (EXECUTION_DOC, prerequisites/steps/records), `Guidance.md` (informational, not scanned for execution edges).
- **ANCHOR_DOC:** `Datasheet.md` (highest-confidence match: contains deliverable identification and decomposition references).
- **EXECUTION_DOC_ORDER:** `Specification.md`, `Procedure.md`.
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — located via `_REFERENCES.md`. Decomposition confirmed present; anchors validated against SCOPE_LEDGER.csv, DELIVERABLE_REGISTER.csv, and OBJECTIVE_DELIVERABLE_MAP.csv.
- **_REFERENCES.md:** Present; used to resolve decomposition path and sibling deliverable pointers.
- **Anchor resolution:** SOW-0017 confirmed in SCOPE_LEDGER.csv as parent scope decision for PKG-016. OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010 confirmed in DELIVERABLE_REGISTER.csv row for DEL-016-04.
- **EXECUTION edges:** DEL-016-01 and DEL-016-02 identified as explicit upstream prerequisites from Datasheet.md References section. DEL-016-05 and DEL-016-06 identified as explicit downstream handover targets from Procedure.md. Two interface edges (IFC-E3BE98E89B structural loading; IFC-0C63CABBEC electrical power feed) extracted from Specification.md and Datasheet.md; target deliverable IDs not resolved (TargetType=UNKNOWN; raw interface IDs preserved).
- **Excluded (low signal):** General "coordination" statements in Guidance.md were not scanned per skill rules. Scheduling dependencies and structural adjacency not extracted.
- **No warnings:** Parent anchor present (1 × IMPLEMENTS_NODE). Decomposition confirmed present.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First extraction run. Mode: UPDATE. Strictness: CONSERVATIVE. Decomposition: GATE-07_Final_Published_2026-05-24 (confirmed). 14 ACTIVE rows written (8 ANCHOR, 6 EXECUTION). 0 RETIRED. Schema: v3.1.
