# Dependencies: DEL-017-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` produced by `TASK + dependency-extract` on 2026-05-25.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-017-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0018 | Scope decision SOW-0018 — MV VFD PKG-017 | ACTIVE |
| DEP-017-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-002 | Project Objective OBJ-002 | ACTIVE |
| DEP-017-04-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Project Objective OBJ-004 | ACTIVE |
| DEP-017-04-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Project Objective OBJ-005 | ACTIVE |
| DEP-017-04-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Project Objective OBJ-006 | ACTIVE |
| DEP-017-04-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Project Objective OBJ-008 | ACTIVE |
| DEP-017-04-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 | ACTIVE |
| DEP-017-04-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 | ACTIVE |
| DEP-017-04-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-017-01_scope-of-work | Scope of Work (PKG-017) | ACTIVE |
| DEP-017-04-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-017-02_package-datasheet | Package Datasheet (PKG-017) | ACTIVE |
| DEP-017-04-011 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-017-05_vendor-document-turnover-package | Vendor Document Turnover Package | ACTIVE |
| DEP-017-04-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-017-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance | ACTIVE |

**Totals:** 12 rows — 8 ANCHOR, 4 EXECUTION; all ACTIVE.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 12 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 12 |

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; source documents in scope: `Datasheet.md`, `Guidance.md`, `Procedure.md`, `_CONTEXT.md`
- **ANCHOR_DOC:** `Datasheet.md` (highest-confidence anchor signal; contains explicit SOW/OBJ references)
- **EXECUTION_DOC_ORDER:** `Procedure.md` (primary workflow signal), `Guidance.md`, `Datasheet.md`
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — used to validate SOW-0018 anchor and resolve OBJ-* canonical labels; SCOPE_LEDGER.csv and DELIVERABLE_REGISTER.csv consulted.
- **Pass 1 (ANCHOR):** SOW-0018 confirmed in SCOPE_LEDGER.csv. OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010 confirmed in DELIVERABLE_REGISTER.csv row DEL-017-04.
- **Pass 2 (EXECUTION):** Two UPSTREAM prerequisites (DEL-017-01, DEL-017-02) explicitly stated in Procedure.md Prerequisites. Two DOWNSTREAM handovers (DEL-017-05, DEL-017-06) explicitly stated in Procedure.md Step 7 and confirmed in Guidance.md Purpose and Datasheet.md Construction section.
- **Interfaces noted but not extracted as EXECUTION edges:** Six package interfaces (IFC-5E50E5F700, IFC-1340C6D795, IFC-6ECD9C92A1, IFC-FB4034716A, IFC-A807F5E0B3, IFC-34EB597147) are design-engineering inputs to the vendor; they do not constitute explicit information-flow dependencies between deliverables per skill MODEL rules. Not extracted.
- **FLOATING_NODE check:** 1 IMPLEMENTS_NODE row (DEP-017-04-001) — no warning needed.
- **AMBIGUOUS_ANCHOR check:** Exactly 1 IMPLEMENTS_NODE — no warning needed.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract run; MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE; decomposition GATE-07_Final_Published_2026-05-24 used; 12 rows extracted (8 ANCHOR, 4 EXECUTION); all ACTIVE; schema validated VALID.
