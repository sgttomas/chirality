# Dependencies: DEL-032-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (v3.1)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

8 rows extracted (all ACTIVE). Schema version: v3.1.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetID / Ref | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-032-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | WBS-03 | WBS 03 — Electrical | HIGH | ACTIVE |
| DEP-032-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0033 | SOW-0033 Package Requirements Reference | HIGH | ACTIVE |
| DEP-032-02-003 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-032-01_scope-of-work | Scope of Work (PKG-032) | HIGH | ACTIVE |
| DEP-032-02-004 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | GATE-07 | Gate 7 Final Published PROJECT_DECOMP Snapshot | HIGH | ACTIVE |
| DEP-032-02-005 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | INTERFACE_REGISTER | INTERFACE_REGISTER.csv (Gate 7 snapshot) — PKG-032 rows | HIGH | ACTIVE |
| DEP-032-02-006 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-032-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package (PKG-032) | HIGH | ACTIVE |
| DEP-032-02-007 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-032-03_construction-work-package | Construction Work Package (PKG-032) | MEDIUM | ACTIVE |
| DEP-032-02-008 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-032-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance (PKG-032) | HIGH | ACTIVE |

## Run Notes

- **Run date:** 2026-05-25
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; documents in scope: `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`
- **ANCHOR_DOC:** `Datasheet.md` (AUTO — matches `datasheet` heuristic; highest-confidence anchor signal)
- **EXECUTION_DOC_ORDER:** `Procedure.md` (primary execution signal), `Specification.md`, `Guidance.md`, `Datasheet.md`
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — used to validate anchors and resolve canonical labels. Note: brief specified `GATE-07_Final_Published_2026-05-24` under `RUN_ROOT`; this path was resolved from `_REFERENCES.md` which points to the same snapshot.
- **Pass 1 (ANCHOR):** Two rows emitted — one `IMPLEMENTS_NODE` anchor to WBS-03 (explicit in Datasheet Identification table and PACKAGE_REGISTER.csv), one `TRACES_TO_REQUIREMENT` anchor to SOW-0033 (explicit in DELIVERABLE_REGISTER.csv).
- **Pass 2 (EXECUTION):** Six rows emitted — three UPSTREAM (DEL-032-01 Scope of Work, Gate 7 snapshot, INTERFACE_REGISTER.csv) and three DOWNSTREAM (DEL-032-04, DEL-032-03, DEL-032-06). DEL-032-04 and DEL-032-06 are HIGH confidence (DELIVERABLE_REGISTER.csv names the Datasheet explicitly). DEL-032-03 is MEDIUM confidence (direction implied through Procedure Step 10 and Construction Work Package scope).
- **Tree x DAG integrity:** 1 IMPLEMENTS_NODE anchor found — no floating-node warning. No ambiguous-anchor warning.
- **[WARNING] MISSING_GATE_PATH:** The brief specified `DECOMPOSITION_PATH: /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/GATE-07_Final_Published_2026-05-24/` — this path does not exist at that location. The snapshot was resolved from `_REFERENCES.md` to the correct path under `_Decomposition/PROJECT_DECOMP/_GateSnapshots/`. All anchor lookups succeeded using the resolved path.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 8 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| SATISFIED | 3 |
| TBD | 5 |

ANCHOR rows (2): both SATISFIED (decomposition truth accepted at Gate 7).
EXECUTION UPSTREAM rows (3): Gate 7 snapshot SATISFIED; DEL-032-01 and INTERFACE_REGISTER SATISFIED as source inputs already consumed in producing this deliverable. Downstream HANDOVER rows (3) remain TBD pending vendor and construction deliverables.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First EXTRACTED run. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. 8 rows extracted (2 ANCHOR, 6 EXECUTION). Schema v3.1. 0 rows retired. Decomposition path resolved from _REFERENCES.md (brief path not found at specified location — see Run Notes warning).
