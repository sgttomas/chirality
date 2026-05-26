# Dependencies: DEL-026-02_package-datasheet — Package Datasheet

**Coordination Mode:** EXTRACTED
**Dependency tracking mode:** EXTRACTED (Dependencies.csv v3.1)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

**Last extraction:** 2026-05-25 | MODE: UPDATE | STRICTNESS: CONSERVATIVE

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetRefID / TargetDeliverableID | TargetName | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-026-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0027 | Scope decision SOW-0027 — TXP-8300-2 (WBS 02) | ACTIVE |
| DEP-026-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-002 | Project Objective OBJ-002 | ACTIVE |
| DEP-026-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Project Objective OBJ-004 | ACTIVE |
| DEP-026-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Project Objective OBJ-005 | ACTIVE |
| DEP-026-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Project Objective OBJ-006 | ACTIVE |
| DEP-026-02-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Project Objective OBJ-008 | ACTIVE |
| DEP-026-02-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 | ACTIVE |
| DEP-026-02-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 | ACTIVE |
| DEP-026-02-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-026-01_scope-of-work | Scope of Work — PKG-026 | ACTIVE |
| DEP-026-02-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-026-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package — PKG-026 | ACTIVE |
| DEP-026-02-011 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-026-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance — PKG-026 | ACTIVE |
| DEP-026-02-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | IFC-E9FC2B952D | Interface IFC-E9FC2B952D — Electrical Power | ACTIVE |
| DEP-026-02-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | IFC-FE5C9BD828 | Interface IFC-FE5C9BD828 — Grounding / Bonding | ACTIVE |
| DEP-026-02-014 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | IFC-0230019D52 | Interface IFC-0230019D52 — Area / Exterior Lighting | ACTIVE |
| DEP-026-02-015 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | IFC-25E2CF2BD9 | Interface IFC-25E2CF2BD9 — I&C / Control Cabling | ACTIVE |
| DEP-026-02-016 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | IFC-E6E0E1FA2B | Interface IFC-E6E0E1FA2B — Communications / Network | ACTIVE |
| DEP-026-02-017 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | IFC-93877B34D5 | Interface IFC-93877B34D5 — Maintenance Access | ACTIVE |
| DEP-026-02-018 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | IFC-7DD82CAE51 | Interface IFC-7DD82CAE51 — Structural / Foundations / Supports | ACTIVE |

**Total rows: 18 | ACTIVE: 18 | RETIRED: 0**

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 18 |
| RETIRED | 0 |
| **Total** | **18** |

| SatisfactionStatus | Count |
|---|---|
| TBD | 18 |

| DependencyClass | Count |
|---|---|
| ANCHOR | 8 |
| EXECUTION | 10 |

ANCHOR breakdown: 1 IMPLEMENTS_NODE, 7 TRACES_TO_REQUIREMENT. Parent anchor check: exactly 1 IMPLEMENTS_NODE (SOW-0027) — no FLOATING_NODE or AMBIGUOUS_ANCHOR warnings.

## Run Notes

- **Run date:** 2026-05-25
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; source documents used: `Datasheet.md` (ANCHOR_DOC), `Procedure.md`, `Specification.md`, `Guidance.md` (EXECUTION_DOC_ORDER).
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — used for anchor validation and label resolution.
- **RUN_ROOT:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined`

**Defaults applied:**
- ANCHOR_DOC: `Datasheet.md` (contains explicit `Identification` and `References` sections with WBS/scope/objective IDs).
- EXECUTION_DOC_ORDER: `Procedure.md`, then `Specification.md`, then `Guidance.md`.
- Parent anchor resolved: `SOW-0027` confirmed in `SCOPE_LEDGER.csv` as the scope decision node for `PKG-026`.
- Objective traces (OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010) confirmed in `SCOPE_LEDGER.csv` row `SOW-0027` and `_CONTEXT.md`.
- Interface IDs (IFC-E9FC2B952D, IFC-FE5C9BD828, IFC-0230019D52, IFC-25E2CF2BD9, IFC-E6E0E1FA2B, IFC-93877B34D5, IFC-7DD82CAE51) confirmed in `Datasheet.md` Conditions table with explicit `INTERFACE_REGISTER.csv` citations.

**Warnings / Notes:**
- No FLOATING_NODE, AMBIGUOUS_ANCHOR, or MISSING_DECOMPOSITION warnings.
- `TargetDeliverableID` for EXTERNAL rows intentionally empty; `TargetRefID` carries the IFC stable ID per schema rule (non-deliverable targets use TargetRefID, not TargetDeliverableID).
- No `TargetPackageID` or `TargetDeliverableID` populated for WBS_NODE, REQUIREMENT, or EXTERNAL rows — correct per schema.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First extraction run; MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. 18 rows created (8 ANCHOR, 10 EXECUTION); all ACTIVE. Schema: v3.1. Decomposition snapshot: GATE-07_Final_Published_2026-05-24. No warnings.
