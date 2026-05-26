# Dependencies: DEL-048-06_epc-vendor-package-review-and-acceptance — EPC Vendor Package Review and Acceptance

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract run complete)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1). This file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` has been generated. Schema version: v3.1. Row count: 11 rows (all ACTIVE).

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetID / TargetName | Confidence |
|---|---|---|---|---|---|---|---|
| DEP-048-06-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | PACKAGE | PKG-048 — Inlet / Sales Compressors | HIGH |
| DEP-048-06-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0115 — Package Vendor / EPC Integrator scope split | HIGH |
| DEP-048-06-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0116 — Equipment count / model / sizing | HIGH |
| DEP-048-06-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0117 — Driver and auxiliary equipment requirements | HIGH |
| DEP-048-06-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0118 — Scope notes: capacities pressures connected load by-others | HIGH |
| DEP-048-06-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-048-01 — Scope of Work | HIGH |
| DEP-048-06-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-048-02 — Package Datasheet | HIGH |
| DEP-048-06-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-048-03 — Construction Work Package | HIGH |
| DEP-048-06-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-048-04 — Vendor Engineered Equipment Package | HIGH |
| DEP-048-06-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-048-05 — Vendor Document Turnover Package | HIGH |
| DEP-048-06-011 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | EXTERNAL | Commissioning and operations handoff | MEDIUM |

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; source documents used: `Datasheet.md` (ANCHOR_DOC), `Specification.md`, `Procedure.md`, `Guidance.md` (EXECUTION_DOCS).
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — used for anchor validation and target ID resolution.
- **ANCHOR_DOC:** `Datasheet.md` (highest-confidence match for anchor signals; contains explicit ParentPackageID, ScopeItemsCovered, ObjectivesSupported).
- **EXECUTION_DOC_ORDER:** `Specification.md`, `Procedure.md`, `Guidance.md`.
- **Parent anchor (IMPLEMENTS_NODE):** PKG-048 confirmed in GATE-07 PACKAGE_REGISTER and DELIVERABLE_REGISTER row 359.
- **Requirement traces:** SOW-0115 through SOW-0118 confirmed in GATE-07 SCOPE_LEDGER rows 116-119.
- **Downstream HANDOVER (DEP-048-06-011):** Target is external commissioning/operations handoff; no specific receiving deliverable identified in sources — TargetType=EXTERNAL, Confidence=MEDIUM.
- **Excluded:** Objective associations (OBJ-001, OBJ-003..OBJ-010) are package-level structural associations carried identically by all PKG-048 deliverables; not emitted as ANCHOR rows per information-flow-only and no-structural-adjacency rules (ASSUMPTION: package-level objective mapping is decomposition-structural; only direct information/artifact transfers extracted).
- **TBD items:** Conflict CFLT-1 (driver rated power ruling) and CFLT-2 (preferred motor make/frame as acceptance criterion) are documented in Guidance.md; these affect acceptance checklist execution but do not create additional dependency rows — they are intra-deliverable resolution items.
- No `[WARNING] FLOATING_NODE` — parent anchor (IMPLEMENTS_NODE) present.
- No `[WARNING] AMBIGUOUS_ANCHOR` — exactly one IMPLEMENTS_NODE row.
- No `[WARNING] MISSING_DECOMPOSITION` — decomposition confirmed at GATE-07 path.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 11 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 11 |

| DependencyClass | ACTIVE count |
|---|---|
| ANCHOR | 5 |
| EXECUTION | 6 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract run; MODE=UPDATE; STRICTNESS=CONSERVATIVE; CONSUMER_CONTEXT=NONE; decomposition=GATE-07 confirmed; 11 rows extracted (5 ANCHOR + 6 EXECUTION); all ACTIVE; no warnings.
