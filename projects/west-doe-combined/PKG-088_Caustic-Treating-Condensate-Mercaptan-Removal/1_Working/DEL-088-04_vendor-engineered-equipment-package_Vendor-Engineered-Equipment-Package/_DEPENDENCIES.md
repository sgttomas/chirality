# Dependencies: DEL-088-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract run 2026-05-26)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1 schema). This file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

**Total ACTIVE rows:** 9
**ANCHOR rows (ACTIVE):** 5 (1 IMPLEMENTS_NODE + 4 TRACES_TO_REQUIREMENT)
**EXECUTION rows (ACTIVE):** 4 (2 UPSTREAM PREREQUISITE + 2 DOWNSTREAM HANDOVER)
**RETIRED rows:** 0

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetID / TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-088-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-088 Caustic Treating (Condensate Mercaptan Removal) | HIGH | ACTIVE |
| DEP-088-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0055 | HIGH | ACTIVE |
| DEP-088-04-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0056 | HIGH | ACTIVE |
| DEP-088-04-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0057 | HIGH | ACTIVE |
| DEP-088-04-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0058 | HIGH | ACTIVE |
| DEP-088-04-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-088-01_scope-of-work | HIGH | ACTIVE |
| DEP-088-04-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-088-02_package-datasheet | HIGH | ACTIVE |
| DEP-088-04-008 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-088-05_vendor-document-turnover-package | HIGH | ACTIVE |
| DEP-088-04-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-088-06_epc-vendor-package-review-and-acceptance | HIGH | ACTIVE |

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 9 |
| RETIRED | 0 |

**SatisfactionStatus breakdown (ACTIVE rows):** 9 TBD

## Run Notes

- **Run date:** 2026-05-26
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; documents found: `Datasheet.md` (ANCHOR_DOC, highest-confidence anchor signal), `Specification.md`, `Guidance.md`, `Procedure.md` (EXECUTION_DOC_ORDER: Procedure first, then Specification, then Guidance).
- **ANCHOR_DOC chosen:** `Datasheet.md` (contains explicit parent package, scope items, and anchoring deliverables fields).
- **DECOMPOSITION_PATH resolved:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — GATE-07 snapshot confirmed present. Provided path `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/GATE-07_Final_Published_2026-05-24/` did not exist at that exact location; resolved via `_CONTEXT.md` Decomposition Reference and `_REFERENCES.md` to the canonical snapshot path above. Non-blocking.
- **Decomposition validation:** DEL-088-04 confirmed in DELIVERABLE_REGISTER.csv row 4 of PKG-088 block. PKG-088 confirmed in PACKAGE_REGISTER.csv. All target deliverable IDs (DEL-088-01, -02, -05, -06) confirmed present in DELIVERABLE_REGISTER.csv.
- **Pass 1 (ANCHOR):** Emitted one IMPLEMENTS_NODE anchor to PKG-088 (WBS_NODE). Emitted four TRACES_TO_REQUIREMENT anchors to SOW-0055, SOW-0056, SOW-0057, SOW-0058 — all four scope items are explicitly listed in Datasheet.md §Identification and confirmed in _CONTEXT.md.
- **Pass 2 (EXECUTION):** Emitted two UPSTREAM PREREQUISITE edges (DEL-088-01, DEL-088-02) from Procedure.md §Prerequisites (explicit text: "issued by EPC Integrator and provided to Package Vendor"). Emitted two DOWNSTREAM HANDOVER edges (DEL-088-05, DEL-088-06) from Specification.md §Documentation and §Verification (explicit named references).
- **No FLOATING_NODE warning:** One IMPLEMENTS_NODE anchor found (DEP-088-04-001).
- **No AMBIGUOUS_ANCHOR warning:** Exactly one IMPLEMENTS_NODE anchor.
- **No MISSING_DECOMPOSITION warning:** Decomposition resolved and validated.
- **Excluded (low-signal):** DBM-Comp_and_Liquids source reference — read-only evidence source, not a dependency edge. `26020-Package_Requirements.docx` referenced as binary source; no explicit artifact transfer stated beyond scope ledger entries already captured via SOW rows. Volatile mercaptan waiver open item (SOW-0058 waiver confirmation) — tracked as TBC in source documents; a human ruling is required (Specification REQ-088-04-06); not a dependency edge.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-26 — dependency-extract UPDATE run (CONSERVATIVE, CONSUMER_CONTEXT=NONE). Decomposition resolved to GATE-07 snapshot. Generated 9 ACTIVE rows: 1 IMPLEMENTS_NODE + 4 TRACES_TO_REQUIREMENT + 2 UPSTREAM PREREQUISITE + 2 DOWNSTREAM HANDOVER. Schema validated VALID.
