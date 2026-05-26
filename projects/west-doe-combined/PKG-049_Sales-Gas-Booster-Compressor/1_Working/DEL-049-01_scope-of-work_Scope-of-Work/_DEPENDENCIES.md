# Dependencies: DEL-049-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (UPDATE run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

12 rows extracted (all ACTIVE). Schema version: v3.1.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence |
|---|---|---|---|---|---|---|---|---|
| DEP-049-01-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | PACKAGE | PKG-049 | Sales Gas Booster Compressor | HIGH |
| DEP-049-01-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0169 | SOW-0169 (package scope item) | HIGH |
| DEP-049-01-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0170 | SOW-0170 (basic scope) | HIGH |
| DEP-049-01-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0171 | SOW-0171 (major included equipment) | HIGH |
| DEP-049-01-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0172 | SOW-0172 (scope notes and design conditions) | HIGH |
| DEP-049-01-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | GATE-07_Final_Published_2026-05-24 | GATE-07 Final Published PROJECT_DECOMP Snapshot | HIGH |
| DEP-049-01-007 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-049-02_package-datasheet | Package Datasheet | HIGH |
| DEP-049-01-008 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-049-03_construction-work-package | Construction Work Package | HIGH |
| DEP-049-01-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-049-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package | HIGH |
| DEP-049-01-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-049-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance | MEDIUM |
| DEP-049-01-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | PACKAGE | PKG-048 | Inlet / Sales Compressors (PKG-048) | HIGH |
| DEP-049-01-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | PACKAGE | PKG-047 | Vapour Recovery Unit 4-25 (PKG-047) | HIGH |

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; documents found: `_CONTEXT.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, `_REFERENCES.md`
- **ANCHOR_DOC:** AUTO → `_CONTEXT.md` (highest-confidence anchor signal: explicit DeliverableID, ParentPackageID, Covers Scope Items fields)
- **EXECUTION_DOC_ORDER:** AUTO → `Specification.md` (primary), `Procedure.md`, `Datasheet.md`, `Guidance.md`
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — provided via DECOMPOSITION_PATH parameter; confirmed present; PACKAGE_REGISTER.csv, DELIVERABLE_REGISTER.csv, SCOPE_LEDGER.csv, and INTERFACE_REGISTER.csv read for anchor/target validation.
- **No existing Dependencies.csv found** — new register created.
- **Pass 1 (ANCHOR):** 1 IMPLEMENTS_NODE (PKG-049) + 4 TRACES_TO_REQUIREMENT (SOW-0169..0172) emitted. All identifiers confirmed in decomposition registers. CONSERVATIVE posture: objective anchors (OBJ-001, OBJ-003..010) are labeled ASSUMPTION in _CONTEXT.md source (package-grouping heuristic); not emitted under CONSERVATIVE strictness.
- **Pass 2 (EXECUTION):** 7 EXECUTION rows emitted. Decomposition snapshot cited as PREREQUISITE (explicit in Procedure.md). Four downstream ENABLES edges to PKG-049 sibling deliverables (DEL-049-02, 03, 04, 06) per Specification.md § Documentation and § Verification. Two UPSTREAM INTERFACE edges: PKG-048 (sales compressor discharge suction tie-in, R-049-01-16) and PKG-047 (VRU suction header vent routing, R-049-01-13). DEL-049-05 not included: Specification.md lists it in the documentation set but does not state an explicit information-transfer dependency FROM this deliverable to that one; DEL-049-05 is a vendor-owned artifact.
- **CONSERVATIVE posture applied:** Only edges with explicit evidence in source documents extracted. No coordination-only or structural-adjacency edges emitted.
- **[WARNING] FLOATING_NODE check:** 1 parent anchor found (DEP-049-01-001, IMPLEMENTS_NODE, PKG-049). OK — no floating node.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 12 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 12 |

| DependencyClass | ACTIVE count |
|---|---|
| ANCHOR | 5 |
| EXECUTION | 7 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — UPDATE run; MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE; decomposition path provided (GATE-07_Final_Published_2026-05-24); new register created; 12 rows extracted (5 ANCHOR, 7 EXECUTION); all ACTIVE; schema v3.1; validation: VALID.
