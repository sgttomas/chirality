# Dependencies: DEL-037-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1). This file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Run completed 2026-05-25. Mode: UPDATE. Strictness: CONSERVATIVE.

### Summary

| Metric | Count |
|---|---|
| Total rows | 5 |
| ACTIVE | 5 |
| RETIRED | 0 |
| ANCHOR rows (ACTIVE) | 1 |
| EXECUTION rows (ACTIVE) | 4 |
| UPSTREAM (ACTIVE) | 3 |
| DOWNSTREAM (ACTIVE) | 1 |

### Compact Table (ACTIVE rows)

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetRef / DeliverableID | Statement (short) |
|---|---|---|---|---|---|---|---|
| DEP-037-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0038 | Implements scope ledger node SOW-0038 for PKG-037 |
| DEP-037-04-002 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-037-01_scope-of-work | Vendor package shall be developed from EPC Scope of Work |
| DEP-037-04-003 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-037-02_package-datasheet | Vendor package shall be developed from EPC Package Datasheet |
| DEP-037-04-004 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-037-06_epc-vendor-package-review-and-acceptance | Vendor submits engineered package for EPC Integrator review under DEL-037-06 |
| DEP-037-04-005 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | DOCUMENT | ART-8870C8E2DE / DBM-Deepcut | Vendor package design shall comply with DBM electrical-building basis (multiple requirements) |

## Run Notes

- **Run date:** 2026-05-25
- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **Source documents scanned (AUTO):** Datasheet.md, Specification.md, Procedure.md, Guidance.md, _CONTEXT.md
- **Anchor doc (AUTO heuristic):** Datasheet.md (contains "datasheet" in filename — highest-confidence ANCHOR_DOC match)
- **Execution docs (AUTO order):** Procedure.md (contains "procedure"), Specification.md, Guidance.md
- **Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`
- **Decomposition status:** FOUND — anchors validated against SCOPE_LEDGER.csv, DELIVERABLE_REGISTER.csv, and PACKAGE_REGISTER.csv.
- **_REFERENCES.md consulted:** Yes — used to resolve TargetLocation paths for deliverable and document targets.

### Anchor integrity

- IMPLEMENTS_NODE count (ACTIVE): 1 — DEP-037-04-001 anchors to SOW-0038. No FLOATING_NODE warning.
- No AMBIGUOUS_ANCHOR: exactly one parent anchor.

### Key assumptions and TBDs

- DEP-037-04-005 uses TargetType=DOCUMENT (the DBM source file) rather than creating a spurious deliverable row. TargetRefID carries the artifact ID ART-8870C8E2DE as a stable pointer where available; TargetName and TargetLocation identify the physical file.
- No dependency was extracted for the twelve interface types (Utility Piping, Drain/Containment, etc.) because these are interface facts carried in the package interface requirements matrix, not explicit information-transfer dependencies to named upstream deliverables in accessible source text. Per skill rules, coordination-only / interface-fact relationships are excluded.
- No dependency was extracted on DEL-037-03 (Construction Work Package) or DEL-037-05 (Vendor Document Turnover Package): source documents do not state an explicit information-transfer prerequisite from DEL-037-04 to or from those deliverables.
- ProposedMaturity and RequiredMaturity set to ACCEPTED for all rows reflecting that the Gate 7 decomposition is accepted and the upstream inputs are expected to be at accepted maturity when the vendor engages.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 5 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 5 |

All ACTIVE rows have SatisfactionStatus=TBD — no closure evidence available at time of extraction.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First extraction run. Mode: UPDATE. Strictness: CONSERVATIVE. Decomposition: GATE-07_Final_Published_2026-05-24 (FOUND). Source docs: AUTO (5 docs). Rows written: 5 ACTIVE (1 ANCHOR, 4 EXECUTION). No warnings.
