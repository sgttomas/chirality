# Dependencies: DEL-021-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is authoritative; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

20 rows extracted (all ACTIVE). Summary by class:

| DependencyClass | AnchorType | Direction | Count |
|---|---|---|---|
| ANCHOR | IMPLEMENTS_NODE | UPSTREAM | 1 |
| ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | 7 |
| EXECUTION | NOT_APPLICABLE | UPSTREAM | 7 |
| EXECUTION | NOT_APPLICABLE | DOWNSTREAM | 5 |

### Compact Table

| DependencyID | Class | Direction | Type | Target | Status |
|---|---|---|---|---|---|
| DEP-021-01-001 | ANCHOR | UPSTREAM | OTHER | SOW-0022 (WBS_NODE) | ACTIVE |
| DEP-021-01-002 | ANCHOR | UPSTREAM | OTHER | OBJ-001 (REQUIREMENT) | ACTIVE |
| DEP-021-01-003 | ANCHOR | UPSTREAM | OTHER | OBJ-004 (REQUIREMENT) | ACTIVE |
| DEP-021-01-004 | ANCHOR | UPSTREAM | OTHER | OBJ-005 (REQUIREMENT) | ACTIVE |
| DEP-021-01-005 | ANCHOR | UPSTREAM | OTHER | OBJ-006 (REQUIREMENT) | ACTIVE |
| DEP-021-01-006 | ANCHOR | UPSTREAM | OTHER | OBJ-008 (REQUIREMENT) | ACTIVE |
| DEP-021-01-007 | ANCHOR | UPSTREAM | OTHER | OBJ-009 (REQUIREMENT) | ACTIVE |
| DEP-021-01-008 | ANCHOR | UPSTREAM | OTHER | OBJ-010 (REQUIREMENT) | ACTIVE |
| DEP-021-01-009 | EXECUTION | UPSTREAM | INTERFACE | Gate 7 decomposition registers (DOCUMENT) | ACTIVE — SATISFIED |
| DEP-021-01-010 | EXECUTION | UPSTREAM | INTERFACE | DBM-Deepcut 4-25_Deepcut_DBM.md (DOCUMENT) | ACTIVE — SATISFIED |
| DEP-021-01-011 | EXECUTION | UPSTREAM | PREREQUISITE | Short-circuit study (DOCUMENT) | ACTIVE — PENDING |
| DEP-021-01-012 | EXECUTION | UPSTREAM | PREREQUISITE | ELC-QAS-000007-001 MV Switchgear spec (DOCUMENT) | ACTIVE — PENDING |
| DEP-021-01-013 | EXECUTION | UPSTREAM | PREREQUISITE | ELC-QAS-000008-001 MV MCC spec (DOCUMENT) | ACTIVE — PENDING |
| DEP-021-01-014 | EXECUTION | UPSTREAM | INTERFACE | PKG-020 13.8kV Switchgear (PACKAGE) | ACTIVE — TBD |
| DEP-021-01-015 | EXECUTION | UPSTREAM | INTERFACE | PKG-027 TXP-8301-1 13.8kV/6.9kV transformer (PACKAGE) | ACTIVE — TBD |
| DEP-021-01-016 | EXECUTION | DOWNSTREAM | ENABLES | DEL-021-02 Package Datasheet (DELIVERABLE) | ACTIVE — TBD |
| DEP-021-01-017 | EXECUTION | DOWNSTREAM | ENABLES | DEL-021-03 Construction Work Package (DELIVERABLE) | ACTIVE — TBD |
| DEP-021-01-018 | EXECUTION | DOWNSTREAM | ENABLES | DEL-021-04 Vendor Engineered Equipment Package (DELIVERABLE) | ACTIVE — TBD |
| DEP-021-01-019 | EXECUTION | DOWNSTREAM | ENABLES | DEL-021-05 Vendor Document Turnover Package (DELIVERABLE) | ACTIVE — TBD |
| DEP-021-01-020 | EXECUTION | DOWNSTREAM | ENABLES | DEL-021-06 EPC Vendor Package Review and Acceptance (DELIVERABLE) | ACTIVE — TBD |

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; candidate source documents used: `Datasheet.md`, `Procedure.md`
- **ANCHOR_DOC:** `Datasheet.md` (contains `Identification` and `Conditions` blocks with explicit SOW and objective references)
- **EXECUTION_DOC_ORDER:** `Procedure.md` (contains explicit prerequisite and downstream handoff declarations), `Datasheet.md` (supplementary)
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — located from `_REFERENCES.md`; used to validate anchor IDs (SOW-0022, OBJ-001 through OBJ-010), resolve canonical labels, and confirm downstream deliverable IDs.
- **DependencyID format:** DEP-021-01-NNN (three-digit sequence)
- Parent anchor: DEP-021-01-001 — SOW-0022 confirmed in SCOPE_LEDGER.csv; no FLOATING_NODE warning.
- Upstream power interface edges (DEP-021-01-014, DEP-021-01-015) set to MEDIUM confidence — ASSUMPTION that PKG-020 is the plant main 13.8 kV switchgear source and PKG-027 (TXP-8301-1) is the specific feed transformer for the 6.9 kV building; confirmation requires single-line diagram.
- Governing specifications ELC-QAS-000007-001 and ELC-QAS-000008-001 extracted as PREREQUISITE PENDING; documents not yet in `_Sources`.
- Short-circuit study extracted as PREREQUISITE PENDING; resolution path cited as DBM short-circuit study row.
- No `_SEMANTIC.md` deletion file noted in this deliverable folder; no semantic conflicts observed.
- Specification.md and Guidance.md present in folder but not scanned as source documents for dependency extraction (no additional dependency signals beyond those in Datasheet.md and Procedure.md; CONSERVATIVE strictness applied).

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract skill run; MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE; 20 rows extracted (all ACTIVE); 1 IMPLEMENTS_NODE anchor, 7 TRACES_TO_REQUIREMENT anchors, 7 UPSTREAM EXECUTION edges, 5 DOWNSTREAM ENABLES edges.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 20 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 15 |
| SATISFIED | 2 |
| PENDING | 3 |
