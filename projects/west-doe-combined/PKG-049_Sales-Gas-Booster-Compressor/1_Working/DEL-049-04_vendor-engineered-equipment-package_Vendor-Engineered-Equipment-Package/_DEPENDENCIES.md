# Dependencies: DEL-049-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** DECLARED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill; UPDATE run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Extracted from source documents on 2026-05-25. Total ACTIVE rows: 10. Breakdown:

| DependencyClass | AnchorType | Direction | DependencyType | Count |
|---|---|---|---|---|
| ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | 1 |
| ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | 4 |
| EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | 2 |
| EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | 2 |
| EXECUTION | NOT_APPLICABLE | DOWNSTREAM | INTERFACE | 1 |

### Compact Register Table

| DependencyID | Class | AnchorType | Direction | Type | TargetType | Target | Confidence | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-049-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-049 Sales Gas Booster Compressor | HIGH | ACTIVE |
| DEP-049-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0169 | HIGH | ACTIVE |
| DEP-049-04-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0170 | HIGH | ACTIVE |
| DEP-049-04-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0171 | HIGH | ACTIVE |
| DEP-049-04-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0172 | HIGH | ACTIVE |
| DEP-049-04-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-049-01 Scope of Work | HIGH | ACTIVE |
| DEP-049-04-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-049-02 Package Datasheet | HIGH | ACTIVE |
| DEP-049-04-008 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-049-05 Vendor Document Turnover Package | HIGH | ACTIVE |
| DEP-049-04-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-049-06 EPC Vendor Package Review and Acceptance | HIGH | ACTIVE |
| DEP-049-04-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | INTERFACE | DELIVERABLE | DEL-049-03 Construction Work Package | HIGH | ACTIVE |

## Run Notes

- **Run date:** 2026-05-25
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` (resolved from invoker context; GATE-07 snapshot)
- **SOURCE_DOCS:** AUTO — scanned: `Datasheet.md`, `Guidance.md`, `Procedure.md`, `Specification.md`; excluded: `_CONTEXT.md`, `_DEPENDENCIES.md`, `_MEMORY.md`, `_REFERENCES.md`, `_STATUS.md`
- **ANCHOR_DOC:** `Datasheet.md` (contains identification/traceability signals)
- **EXECUTION_DOC_ORDER:** `Procedure.md` (workflow/execution signals), `Specification.md`, `Guidance.md`
- **Decomposition validation:** GATE-07 snapshot used to confirm parent `PKG-049`, canonical deliverable IDs `DEL-049-01` through `DEL-049-06`, and SOW references. All resolved.
- **Tree x DAG integrity:** One IMPLEMENTS_NODE anchor found (DEP-049-04-001). No FLOATING_NODE or AMBIGUOUS_ANCHOR warnings.
- **Assumptions:** None. All rows are sourced from explicit text in source documents.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract skill UPDATE run; MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE; decomposition GATE-07 snapshot; 10 ACTIVE rows extracted (1 IMPLEMENTS_NODE, 4 TRACES_TO_REQUIREMENT, 5 EXECUTION); no warnings.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 10 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 10 |
