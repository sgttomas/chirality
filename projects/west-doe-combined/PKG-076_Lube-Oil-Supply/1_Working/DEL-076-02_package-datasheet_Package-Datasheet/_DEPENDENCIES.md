# Dependencies: DEL-076-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` generated 2026-05-25 by `TASK + dependency-extract` (MODE=UPDATE, STRICTNESS=CONSERVATIVE).

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRef/ID | TargetName | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-076-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-076 | PKG-076 Lube Oil Supply | ACTIVE |
| DEP-076-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0135 | SOW-0135 | ACTIVE |
| DEP-076-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0136 | SOW-0136 | ACTIVE |
| DEP-076-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0137 | SOW-0137 | ACTIVE |
| DEP-076-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0138 | SOW-0138 | ACTIVE |
| DEP-076-02-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | OBJ-001 — Provide 04-25 Deepcut facility scope | ACTIVE |
| DEP-076-02-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | OBJ-004 | ACTIVE |
| DEP-076-02-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | OBJ-005 | ACTIVE |
| DEP-076-02-009 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | OBJ-006 | ACTIVE |
| DEP-076-02-010 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | OBJ-007 | ACTIVE |
| DEP-076-02-011 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | OBJ-008 | ACTIVE |
| DEP-076-02-012 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | OBJ-009 | ACTIVE |
| DEP-076-02-013 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | OBJ-010 | ACTIVE |
| DEP-076-02-014 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-076-01_scope-of-work | Scope of Work — PKG-076 | ACTIVE |
| DEP-076-02-015 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-076-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package — PKG-076 | ACTIVE |
| DEP-076-02-016 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | INTERFACE | DELIVERABLE | DEL-076-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance — PKG-076 | ACTIVE |
| DEP-076-02-017 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | INTERFACE | DELIVERABLE | DEL-076-03_construction-work-package | Construction Work Package — PKG-076 | ACTIVE |
| DEP-076-02-018 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | DOCUMENT | — | Project hazardous-material list | ACTIVE |
| DEP-076-02-019 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | — | 4-25_Deepcut_DBM.md (DBM Deepcut SEC-08) | ACTIVE |
| DEP-076-02-020 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | — | 3-25_Comp_and_Liquids_DBM.md | ACTIVE |

**Totals (ACTIVE):** 20 rows — 13 ANCHOR, 7 EXECUTION.

## Run Notes

- **Run date:** 2026-05-25
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; source documents identified: `Datasheet.md` (ANCHOR_DOC by filename heuristic), `Specification.md`, `Guidance.md`, `Procedure.md` (EXECUTION_DOCS).
- **DOC_ROLE_MAP:** DEFAULT
- **ANCHOR_DOC:** `Datasheet.md` (highest-confidence match; contains `datasheet` keyword and explicit `ParentPackageID` field).
- **EXECUTION_DOC_ORDER:** `Specification.md`, `Guidance.md`, `Procedure.md`
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — located via `_REFERENCES.md`; used to validate PKG-076, DEL-076-02, SOW IDs, and objective IDs. Note: the `DECOMPOSITION_PATH` input parameter referenced `GATE-07_Final_Published_2026-05-24` under the run root — that exact path does not exist as a top-level run-root directory; the canonical snapshot path was resolved via `_REFERENCES.md` to the `_GateSnapshots` subfolder above.
- **_REFERENCES.md:** Present and read; used to resolve decomposition snapshot path and source document locations.
- **Parent anchor:** DEP-076-02-001 (`IMPLEMENTS_NODE` → PKG-076). No `[WARNING] FLOATING_NODE`.
- **Ambiguous anchor check:** Exactly one IMPLEMENTS_NODE row. No `[WARNING] AMBIGUOUS_ANCHOR`.
- **SOW IDs:** SOW-0135, SOW-0136, SOW-0137, SOW-0138 extracted from DELIVERABLE_REGISTER row DEL-076-02; not individually described in decomposition — TargetRefID populated as stated, TargetName carries the ID.
- **Objective IDs:** OBJ-001, OBJ-004–OBJ-010 confirmed against OBJECTIVE_REGISTER and OBJECTIVE_DELIVERABLE_MAP.
- **Hazardous-material list:** Emitted as UPSTREAM CONSTRAINT (DEP-076-02-018); `TargetLocation=location TBD` because the document is not accessible in workspace (explicitly stated in Specification.md REQ-076-02-08 and Standards table). `SatisfactionStatus=PENDING` reflects an open required input.
- **Compressor package interfaces:** The Datasheet §"Interface Summary" documents an interface to served compressor packages (day-tank fill). This interface is a coordination/operational description; no specific deliverable-to-deliverable artifact transfer requiring a separate EXECUTION row is explicitly stated in the source (compressor package IDs are not resolved to DEL IDs in the accessible decomposition slice). Not emitted per CONSERVATIVE strictness and information-flow-only rule.
- **CONSERVATIVE note:** No rows emitted purely from inference. All EXECUTION rows are supported by explicit REQ, description, or named deliverable reference in source documents.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 20 |
| RETIRED | 0 |

| DependencyClass | ACTIVE |
|---|---|
| ANCHOR | 13 |
| EXECUTION | 7 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 19 |
| PENDING | 1 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full two-pass extraction run (dependency-extract skill, MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE). 20 rows extracted (13 ANCHOR, 7 EXECUTION). Schema VALID. No FLOATING_NODE warning. No AMBIGUOUS_ANCHOR warning. Decomposition path resolved via _REFERENCES.md to GATE-07_Final_Published_2026-05-24 GateSnapshot.
