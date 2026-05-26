# Dependencies: DEL-090-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** DECLARED
**Dependency tracking mode:** EXTRACTED (dependency-extract run completed 2026-05-26)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1 schema). This file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` produced by `TASK + dependency-extract` on 2026-05-26.

| DependencyID | Class | AnchorType | Direction | Type | TargetID / TargetRefID | TargetName | Status | Confidence |
|---|---|---|---|---|---|---|---|---|
| DEP-090-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | PKG-090 | Vapour Recovery Unit 3-25 | ACTIVE | HIGH |
| DEP-090-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | SOW-0249 | SOW-0249 | ACTIVE | HIGH |
| DEP-090-04-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | SOW-0250 | SOW-0250 | ACTIVE | HIGH |
| DEP-090-04-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | SOW-0251 | SOW-0251 | ACTIVE | HIGH |
| DEP-090-04-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | SOW-0252 | SOW-0252 | ACTIVE | HIGH |
| DEP-090-04-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | OBJ-002 | OBJ-002 — Provide 03-25 compressor station and liquids hub scope | ACTIVE | HIGH |
| DEP-090-04-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | OBJ-003 | OBJ-003 — Preserve commercial stream disposition and facility boundary interfaces | ACTIVE | HIGH |
| DEP-090-04-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | OBJ-004 | OBJ-004 | ACTIVE | MEDIUM |
| DEP-090-04-009 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | OBJ-005 | OBJ-005 | ACTIVE | MEDIUM |
| DEP-090-04-010 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | OBJ-006 | OBJ-006 | ACTIVE | MEDIUM |
| DEP-090-04-011 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | OBJ-007 | OBJ-007 | ACTIVE | MEDIUM |
| DEP-090-04-012 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | OBJ-008 | OBJ-008 | ACTIVE | MEDIUM |
| DEP-090-04-013 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | OBJ-009 | OBJ-009 | ACTIVE | MEDIUM |
| DEP-090-04-014 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | OBJ-010 | OBJ-010 | ACTIVE | MEDIUM |
| DEP-090-04-015 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DEL-090-01_scope-of-work | Scope of Work | ACTIVE | HIGH |
| DEP-090-04-016 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DEL-090-02_package-datasheet | Package Datasheet | ACTIVE | HIGH |
| DEP-090-04-017 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DEL-090-05_vendor-document-turnover-package | Vendor Document Turnover Package | ACTIVE | HIGH |
| DEP-090-04-018 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DEL-090-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance | ACTIVE | HIGH |

**Total rows:** 18 ACTIVE, 0 RETIRED
**ANCHOR rows:** 14 (1 IMPLEMENTS_NODE + 13 TRACES_TO_REQUIREMENT)
**EXECUTION rows:** 4 (2 UPSTREAM PREREQUISITE + 2 DOWNSTREAM HANDOVER)

## Run Notes

- **Run date:** 2026-05-26
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned all files in deliverable folder: `_CONTEXT.md`, `Datasheet.md`, `Guidance.md`, `Procedure.md`, `Specification.md`, `_REFERENCES.md`.
- **ANCHOR_DOC (Pass 1):** `_CONTEXT.md` — highest-confidence anchor signal (explicit `ParentPackageID`, `Covers Scope Items`, `Supports Objectives`). Secondary confirmation from `Datasheet.md`.
- **EXECUTION_DOC_ORDER (Pass 2):** `Procedure.md` (primary — explicit prerequisite and handover statements), `Specification.md`, `Guidance.md` (secondary — supporting context).
- **DECOMPOSITION_PATH resolved:** `_REFERENCES.md` and `_CONTEXT.md` both point to GATE-07 snapshot. Confirmed at: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PROJECT_DECOMP.md`. Note: `DECOMPOSITION_PATH` brief argument pointed to `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/GATE-07_Final_Published_2026-05-24/` which does not exist at that exact location — resolved via `_REFERENCES.md` to the canonical `_GateSnapshots/` path. Non-blocking.
- **Decomposition validation:** PKG-090 confirmed in PACKAGE_REGISTER.csv row 100; DEL-090-04 confirmed in DELIVERABLE_REGISTER.csv row 567; SOW-0249..SOW-0252 confirmed in DELIVERABLE_REGISTER.csv row 567; OBJ-002..OBJ-010 confirmed in DELIVERABLE_REGISTER.csv row 567. OBJ-004..OBJ-010 canonical label text not extracted from PROJECT_DECOMP.md this pass — full text available in decomposition file; confidence set to MEDIUM.
- **Tree x DAG integrity:** 1 IMPLEMENTS_NODE row found — no FLOATING_NODE warning, no AMBIGUOUS_ANCHOR warning.
- **Execution edges not emitted (conservative exclusion):** Interface coordination with EPC Integrator (Procedure.md Step 4) is structural/coordination adjacency with no specific artifact handover to a named deliverable; excluded per information-flow-only rule. `26020-Package_Requirements.docx` and `26020-Packages_Interfaces_4_export.xlsx` are document prerequisites but `location TBD` — not promoted to EXECUTION rows this pass; these would require TargetType=DOCUMENT if promoted.
- **RUN_ROOT:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined`

## Lifecycle Summary

| Dimension | Count |
|---|---|
| ACTIVE | 18 |
| RETIRED | 0 |
| SatisfactionStatus=TBD | 18 |
| SatisfactionStatus=PENDING | 0 |
| SatisfactionStatus=SATISFIED | 0 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-26 — dependency-extract run completed. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition: GATE-07 snapshot resolved via _REFERENCES.md. 18 ACTIVE rows written (14 ANCHOR + 4 EXECUTION). No warnings.
