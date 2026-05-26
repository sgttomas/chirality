# Dependencies: DEL-087-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** DECLARED + EXTRACTED
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1 schema). This file is the human-readable view and index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` produced by `TASK + dependency-extract` on 2026-05-26.

**Counts (ACTIVE):**
- ANCHOR rows: 5 (1 × IMPLEMENTS_NODE + 4 × TRACES_TO_REQUIREMENT)
- EXECUTION rows: 6

**Compact table (ACTIVE rows only):**

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetID / Name | Confidence |
|---|---|---|---|---|---|---|---|
| DEP-087-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-087 — Incinerator (WBS 02) | HIGH |
| DEP-087-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0111 | HIGH |
| DEP-087-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0112 | HIGH |
| DEP-087-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0113 | HIGH |
| DEP-087-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0114 | HIGH |
| DEP-087-02-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-087-01_scope-of-work | MEDIUM |
| DEP-087-02-007 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-087-03_construction-work-package | HIGH |
| DEP-087-02-008 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-087-04_vendor-engineered-equipment-package | HIGH |
| DEP-087-02-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-087-06_epc-vendor-package-review-and-acceptance | HIGH |
| DEP-087-02-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | Shared-interface 03-25/04-25 allocation (open) | HIGH |
| DEP-087-02-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | PACKAGE | PKG-065 — Tanks Caustic (spent caustic tank) | HIGH |

## Run Notes

- **Run date:** 2026-05-26
- **SCOPE:** DEL-087-02
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; source documents found: `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, `_CONTEXT.md`, `_REFERENCES.md`
- **ANCHOR_DOC:** AUTO → resolved to `Datasheet.md` (filename matches `datasheet` heuristic; primary identification and traceability signals present)
- **EXECUTION_DOC_ORDER:** AUTO → `Guidance.md` (considerations/constraints), `Specification.md` (requirements/out-of-scope), `Procedure.md` (prerequisites/steps), `Datasheet.md` (interface evidence)
- **DECOMPOSITION_PATH resolved:** `_REFERENCES.md` pointed to `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PROJECT_DECOMP.md`. Invoked DECOMPOSITION_PATH `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/GATE-07_Final_Published_2026-05-24/` did not exist at that location; resolved via `_REFERENCES.md` to the canonical Gate 7 snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`. Anchor and scope-ledger validation proceeded against that snapshot. **Non-blocking.**
- **Decomposition validation:** Anchor PKG-087 confirmed in `PACKAGE_REGISTER.csv`. Scope items SOW-0111–SOW-0114 confirmed in `SCOPE_LEDGER.csv` with DEL-087-02_package-datasheet listed in DeliverableID(s). Sibling deliverable IDs confirmed in `DELIVERABLE_REGISTER.csv`. PKG-065 confirmed in `PACKAGE_REGISTER.csv` as spent-caustic-tank package.
- **Parent anchor count:** 1 (DEP-087-02-001) — IMPLEMENTS_NODE for PKG-087. No `[WARNING] FLOATING_NODE` or `[WARNING] AMBIGUOUS_ANCHOR`.
- **`[WARNING] MISSING_DECOMPOSITION`:** NOT issued — decomposition resolved successfully via `_REFERENCES.md`.
- **CONSERVATIVE posture applied:** No ASSUMPTION-only ANCHOR rows emitted. All EXECUTION edges have explicit source text. DEL-087-05 (Vendor Document Turnover) not emitted — Specification.md names it as out-of-scope sibling but does not state an explicit information-transfer relationship with this deliverable.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 11 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 11 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-26 — `TASK + dependency-extract` UPDATE run; CONSERVATIVE; CONSUMER_CONTEXT=NONE. Produced Dependencies.csv v3.1 with 11 ACTIVE rows (5 ANCHOR + 6 EXECUTION). Decomposition resolved via `_REFERENCES.md`. No warnings.
