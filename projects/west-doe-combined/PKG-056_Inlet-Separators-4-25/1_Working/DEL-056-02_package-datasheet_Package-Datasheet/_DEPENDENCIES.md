# Dependencies: DEL-056-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (Dependencies.csv v3.1 — 10 ACTIVE rows)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register; this file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Two-pass extraction completed 2026-05-25. Mode: UPDATE. Strictness: CONSERVATIVE.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetID / TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-056-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-056 — Inlet Separators 4-25 | HIGH | ACTIVE |
| DEP-056-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0127 | HIGH | ACTIVE |
| DEP-056-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0128 | HIGH | ACTIVE |
| DEP-056-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0129 | HIGH | ACTIVE |
| DEP-056-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0130 | HIGH | ACTIVE |
| DEP-056-02-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-056-01_scope-of-work | HIGH | ACTIVE |
| DEP-056-02-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | GATE-07 decomposition snapshot | HIGH | ACTIVE |
| DEP-056-02-008 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-056-03_construction-work-package | HIGH | ACTIVE |
| DEP-056-02-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-056-04_vendor-engineered-equipment-package | HIGH | ACTIVE |
| DEP-056-02-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | Vendor RFQ 26020-01-PT-RFQ-17-004 (TBD) | MEDIUM | ACTIVE |

**Totals:** 10 ACTIVE, 0 RETIRED. Anchor rows: 5 (1 IMPLEMENTS_NODE + 4 TRACES_TO_REQUIREMENT). Execution rows: 5 (2 UPSTREAM, 3 DOWNSTREAM).

## Run Notes

- **Run date:** 2026-05-25
- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — confirmed present; PACKAGE_REGISTER.csv, DELIVERABLE_REGISTER.csv, and SCOPE_LEDGER.csv all read and used for anchor validation.
- **DECOMPOSITION_PATH param:** `GATE-07_Final_Published_2026-05-24` was passed as the run root path `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/GATE-07_Final_Published_2026-05-24`, which does not exist as a top-level path. The equivalent snapshot was resolved via `_Decomposition/PROJECT_DECOMP/_GateSnapshots/` — same content. No data loss.
- **Source documents scanned (AUTO):** `Datasheet.md`, `Procedure.md`, `Guidance.md` (ANCHOR_DOC: `Datasheet.md` by heuristic; EXECUTION_DOCS: `Procedure.md`, `Guidance.md`). `Specification.md` not present in folder; not scanned.
- **_REFERENCES.md:** read; used to confirm decomposition path and shared source root.
- **Parent anchor check:** 1 IMPLEMENTS_NODE row found (DEP-056-02-001). No FLOATING_NODE warning.
- **Vendor RFQ (DEP-056-02-010):** source document is a binary `.docx` not yet extracted; TargetLocation is `location TBD`. Carried as MEDIUM confidence INTERFACE.
- **DEL-056-06 not extracted as DOWNSTREAM:** Guidance.md and Procedure.md do not explicitly state DEL-056-06 consumes the Datasheet (only DEL-056-03 and DEL-056-04 are named); conservative extraction omits it. It may be added via a DECLARED edge or a later run when evidence is found.
- **No MPFF execution edge extracted:** Guidance.md mentions downstream MPFF operability precondition but frames it as a process interface note, not an explicit artifact/data handoff from this deliverable. CONSERVATIVE strictness excludes it.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 10 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 10 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full two-pass extraction (dependency-extract, UPDATE, CONSERVATIVE). 10 ACTIVE rows written to Dependencies.csv v3.1. Schema validation: VALID (29 columns, 10 rows). Decomposition path resolved via _GateSnapshots/GATE-07_Final_Published_2026-05-24. No warnings.
