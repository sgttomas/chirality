# Dependencies: DEL-038-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (v3.1)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

16 rows extracted. All rows ACTIVE.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetID / TargetName | Confidence | SatisfactionStatus |
|---|---|---|---|---|---|---|---|---|
| DEP-038-01-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0039 — 600V ELECTRICAL BUILDING (820-1) | HIGH | SATISFIED |
| DEP-038-01-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | HIGH | SATISFIED |
| DEP-038-01-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | HIGH | SATISFIED |
| DEP-038-01-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | HIGH | SATISFIED |
| DEP-038-01-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | HIGH | SATISFIED |
| DEP-038-01-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | HIGH | SATISFIED |
| DEP-038-01-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | HIGH | SATISFIED |
| DEP-038-01-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | HIGH | SATISFIED |
| DEP-038-01-009 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | HIGH | SATISFIED |
| DEP-038-01-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | Gate 7 PROJECT_DECOMP Snapshot | HIGH | SATISFIED |
| DEP-038-01-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | Workbook Packages Row 40 | HIGH | SATISFIED |
| DEP-038-01-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | DBM Deepcut Electrical Design Basis | HIGH | SATISFIED |
| DEP-038-01-013 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-038-02 Package Datasheet | HIGH | PENDING |
| DEP-038-01-014 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-038-03 Construction Work Package | HIGH | PENDING |
| DEP-038-01-015 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-038-04 Vendor Engineered Equipment Package | HIGH | PENDING |
| DEP-038-01-016 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-038-06 EPC Vendor Package Review and Acceptance | MEDIUM | PENDING |

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 16 |
| RETIRED | 0 |
| **Total** | **16** |

| SatisfactionStatus | Count |
|---|---|
| SATISFIED | 12 |
| PENDING | 4 |
| TBD | 0 |

### Class breakdown (ACTIVE rows)

| DependencyClass | Count |
|---|---|
| ANCHOR | 9 |
| EXECUTION | 7 |

### Anchor integrity

- IMPLEMENTS_NODE rows (ACTIVE): 1 — parent anchor present. No FLOATING_NODE warning.
- TRACES_TO_REQUIREMENT rows (ACTIVE): 8

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — used for anchor validation and label resolution.
- **SOURCE_DOCS (AUTO):** Specification.md (ANCHOR_DOC — contains identity, requirements, traceability); Datasheet.md (attributes, objective list); Guidance.md (trade-off context); Procedure.md (EXECUTION_DOC — prerequisites and cross-check steps); _CONTEXT.md (identity confirmation).
- **ANCHOR_DOC:** Specification.md selected as primary anchor doc (contains identity, WBS ref, scope-item, objectives).
- **EXECUTION_DOC_ORDER:** Procedure.md (primary); Specification.md (secondary); Datasheet.md (supporting).
- Anchor DEP-038-01-001 resolved to scope item `SOW-0039` confirmed in SCOPE_LEDGER.csv. `TargetType=WBS_NODE` used (SOW-0039 is the flat scope ledger node for PKG-038 per decomposition).
- Objective trace anchors (DEP-038-01-002 through 009) confirmed in DELIVERABLE_REGISTER.csv and OBJECTIVE_DELIVERABLE_MAP.csv.
- Three upstream PREREQUISITE DOCUMENT edges (DEP-038-01-010 through 012) drawn from explicit prerequisite statements in Procedure.md.
- Downstream HANDOVER edges (DEP-038-01-013, 014) drawn from explicit "cross-check" and "downstream" statements in Procedure.md Step 12 and Specification.md § Scope.
- Downstream ENABLES edges (DEP-038-01-015, 016) drawn from Specification.md § Scope explicit statement that SOW is the upstream basis for vendor package production and EPC acceptance.
- No AGGRESSIVE extractions. All rows are CONSERVATIVE evidence-backed EXPLICIT rows.
- `_Sources/26020-Package_Requirements.docx` not parsed (source-gap noted in Datasheet.md); no additional rows emitted from that gap.
- No rows for DEL-038-05 (Vendor Document Turnover): Specification.md cites "vendor document turnover" as a downstream consumer but only in a list also naming DEL-038-04 and DEL-038-06; the dependency is structurally implicit through the vendor package chain rather than explicitly stated as a direct handover from the SOW. Omitted per CONSERVATIVE strictness.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract UPDATE run; MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE; decomposition path resolved; 16 rows extracted (9 ANCHOR, 7 EXECUTION); schema validation VALID; no warnings.
