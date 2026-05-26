# Dependencies: DEL-069-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1). This file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

8 rows total — 8 ACTIVE, 0 RETIRED.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetID / TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-069-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-069 — Mole Sieve Drier Unit (Gas) | HIGH | ACTIVE |
| DEP-069-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0144 | HIGH | ACTIVE |
| DEP-069-04-003 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-069-01_scope-of-work | HIGH | ACTIVE |
| DEP-069-04-004 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-069-02_package-datasheet | HIGH | ACTIVE |
| DEP-069-04-005 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | DBM-SEC-06 (4-25 Deepcut DBM) | HIGH | ACTIVE |
| DEP-069-04-006 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-069-03_construction-work-package | HIGH | ACTIVE |
| DEP-069-04-007 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-069-05_vendor-document-turnover-package | HIGH | ACTIVE |
| DEP-069-04-008 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | INTERFACE | DELIVERABLE | DEL-069-06_epc-vendor-package-review-and-acceptance | HIGH | ACTIVE |

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; source documents used: `_CONTEXT.md`, `Datasheet.md`, `Specification.md`, `Procedure.md`, `Guidance.md`, `_REFERENCES.md`
- **ANCHOR_DOC:** `Datasheet.md` (contains explicit ParentPackageID, Covers Scope Items, and source references — highest-confidence anchor signal)
- **EXECUTION_DOC_ORDER:** `Procedure.md` (primary; explicit prerequisites and handover steps), then `Specification.md` (secondary; confirms interface relationships)
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — found and used for anchor validation and target label resolution. Note: the DECOMPOSITION_PATH parameter in the invocation cited a path that does not exist on disk; the actual GATE-07 snapshot at the path above was used instead.
- **DECOMPOSITION STATUS:** Snapshot found. PKG-069 and all DEL-069-0x IDs confirmed in PACKAGE_REGISTER.csv and DELIVERABLE_REGISTER.csv. SOW-0144 confirmed in SCOPE_LEDGER.csv.

**Pass 1 (ANCHOR):**
- One IMPLEMENTS_NODE anchor found: PKG-069, confirmed in decomposition PACKAGE_REGISTER. FACT.
- One TRACES_TO_REQUIREMENT anchor found: SOW-0144, confirmed in SCOPE_LEDGER. FACT.
- Objective associations (OBJ-001, OBJ-003–010) are noted in _CONTEXT.md but not individually emitted as TRACES_TO_REQUIREMENT rows under CONSERVATIVE strictness, per Guidance.md Conflict C-4: association was under PACKAGE_HEURISTIC basis and not individually re-verified at deliverable-ID level.

**Pass 2 (EXECUTION):**
- DEL-069-01 and DEL-069-02 extracted as PREREQUISITE UPSTREAM from Procedure.md Prerequisites (explicit language: "must be issued to vendor").
- DBM SEC-06 extracted as PREREQUISITE UPSTREAM from Procedure.md Prerequisites (explicit: "available to vendor as design basis reference").
- DEL-069-03 extracted as HANDOVER DOWNSTREAM from Procedure.md Step 6.1 (explicit: "input to DEL-069-03 Construction Work Package").
- DEL-069-05 extracted as HANDOVER DOWNSTREAM from Procedure.md Steps 5.5 and 6.1 (explicit: "inputs to DEL-069-05 Vendor Document Turnover Package").
- DEL-069-06 extracted as INTERFACE DOWNSTREAM from Procedure.md Step 6.2 (explicit: "Coordinate with EPC Integrator (DEL-069-06 review and acceptance) for site receipt and integration").
- Upstream TEG dehydration and downstream UltraTEF cryogenic scopes mentioned in Specification.md / Guidance.md as process context; NOT extracted as dependencies because no explicit artifact/data transfer to a specific deliverable ID is stated — coordination/process context only.

**Tree x DAG integrity:** IMPLEMENTS_NODE count = 1. No FLOATING_NODE or AMBIGUOUS_ANCHOR warnings.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 8 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| SATISFIED | 2 (anchors — confirmed in decomposition) |
| PENDING | 5 (EXECUTION rows — not yet fulfilled) |
| TBD | 0 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION). No Dependencies.csv generated.
- 2026-05-25 — dependency-extract full run. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition: GATE-07_Final_Published_2026-05-24 (found). Extracted 8 rows (2 ANCHOR, 6 EXECUTION). All ACTIVE. Schema validated VALID. Row count: 8.
