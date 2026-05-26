# Dependencies: DEL-049-06_epc-vendor-package-review-and-acceptance — EPC Vendor Package Review and Acceptance

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1). This file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

10 rows extracted (10 ACTIVE, 0 RETIRED).

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetID / TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-049-06-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | PACKAGE | PKG-049 Sales Gas Booster Compressor | HIGH | ACTIVE |
| DEP-049-06-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0169 Ownership split | HIGH | ACTIVE |
| DEP-049-06-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0170 Process function | HIGH | ACTIVE |
| DEP-049-06-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0171 Major included equipment | HIGH | ACTIVE |
| DEP-049-06-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0172 Design throughput / driver / by-others | HIGH | ACTIVE |
| DEP-049-06-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-049-02 Package Datasheet | HIGH | ACTIVE |
| DEP-049-06-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-049-03 Construction Work Package | HIGH | ACTIVE |
| DEP-049-06-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-049-04 Vendor Engineered Equipment Package | HIGH | ACTIVE |
| DEP-049-06-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-049-05 Vendor Document Turnover Package | HIGH | ACTIVE |
| DEP-049-06-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | EXTERNAL | Commissioning custody (facility integration handoff) | MEDIUM | ACTIVE |

## Run Notes

- **Run date:** 2026-05-25
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; documents read: Datasheet.md (ANCHOR_DOC), Procedure.md, Specification.md, Guidance.md
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` (provided by invoker as GATE-07_Final_Published_2026-05-24; resolved to _GateSnapshots subfolder)
- **Anchor validation:** PKG-049 confirmed in PACKAGE_REGISTER.csv; DEL-049-06 confirmed in DELIVERABLE_REGISTER.csv; SOW-0169 through SOW-0172 confirmed in SCOPE_LEDGER.csv.
- **Decomposition status:** Available and used for anchor resolution and label lookup.
- **Pass 1 (ANCHOR):** One IMPLEMENTS_NODE row (PKG-049) + four TRACES_TO_REQUIREMENT rows (SOW-0169..0172). No ambiguous anchors.
- **Pass 2 (EXECUTION):** Four PREREQUISITE UPSTREAM rows (DEL-049-02 through -05) from explicit Procedure.md prerequisites. One DOWNSTREAM HANDOVER row to commissioning custody from Procedure.md Step 9.
- **No FLOATING_NODE warning:** One IMPLEMENTS_NODE anchor present.
- **No AMBIGUOUS_ANCHOR warning:** Exactly one IMPLEMENTS_NODE anchor.
- **Downstream handoff notes:** Not generated (CONSUMER_CONTEXT=NONE).
- **Conflict noted (not a dependency row):** C-049-06-01 — filter coalescer rated 100 MMSCFD vs. compressor design throughput 140 MMSCFD. Recorded in Guidance.md Conflict Table; human ruling TBD. Not emitted as a dependency row (structural conflict, not an information-flow edge).

## Lifecycle Summary

| Dimension | Count |
|---|---|
| ACTIVE rows | 10 |
| RETIRED rows | 0 |
| ANCHOR / IMPLEMENTS_NODE | 1 |
| ANCHOR / TRACES_TO_REQUIREMENT | 4 |
| EXECUTION / UPSTREAM / PREREQUISITE | 4 |
| EXECUTION / DOWNSTREAM / HANDOVER | 1 |
| SatisfactionStatus = TBD | 10 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First extraction run via dependency-extract skill. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition: GATE-07_Final_Published_2026-05-24. 10 rows extracted (10 ACTIVE, 0 RETIRED). No warnings.
