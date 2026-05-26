# Dependencies: DEL-079-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (UPDATE run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

---

## Extracted Dependency Register

Produced by: `TASK + dependency-extract` (skill run 2026-05-25, MODE=UPDATE, STRICTNESS=CONSERVATIVE)

**Total rows:** 13
**ACTIVE:** 13 | **RETIRED:** 0

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetID / TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-079-01-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-079 — Instrument Air Building | HIGH | ACTIVE |
| DEP-079-01-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0131 | HIGH | ACTIVE |
| DEP-079-01-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0132 | HIGH | ACTIVE |
| DEP-079-01-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0133 | HIGH | ACTIVE |
| DEP-079-01-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0134 | HIGH | ACTIVE |
| DEP-079-01-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | HIGH | ACTIVE |
| DEP-079-01-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | HIGH | ACTIVE |
| DEP-079-01-008 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-079-02_package-datasheet | HIGH | ACTIVE |
| DEP-079-01-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-079-03_construction-work-package | HIGH | ACTIVE |
| DEP-079-01-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-079-04_vendor-engineered-equipment-package | HIGH | ACTIVE |
| DEP-079-01-011 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-079-06_epc-vendor-package-review-and-acceptance | HIGH | ACTIVE |
| DEP-079-01-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | INTERFACE_REGISTER.csv (PKG-079 rows) | HIGH | ACTIVE |
| DEP-079-01-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | DELIVERABLE_REGISTER.csv (PKG-079 rows DEL-079-01..06) | HIGH | ACTIVE |

---

## Run Notes

- **Run date:** 2026-05-25
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; documents found: `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, `_CONTEXT.md`, `_REFERENCES.md`
- **ANCHOR_DOC:** `Datasheet.md` (heuristic match: filename contains `datasheet`; confirmed by `_CONTEXT.md`)
- **EXECUTION_DOC_ORDER:** `Specification.md`, `Procedure.md`, `Guidance.md` (heuristic; `Specification.md` chosen first as primary requirements carrier)
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` (resolved from `_REFERENCES.md` and `_CONTEXT.md`)
- **Decomposition status:** PRESENT — used to validate PKG-079 parent anchor and resolve DEL-079-* sibling IDs.
- **Pre-existing `Dependencies.csv`:** MISSING — created new file.

**Pass 1 (ANCHOR) decisions:**
- One `IMPLEMENTS_NODE` anchor to PKG-079 emitted (explicit in Datasheet identification table and `_CONTEXT.md`).
- Four `TRACES_TO_REQUIREMENT` anchors to SOW-0131, SOW-0132, SOW-0133, SOW-0134 emitted (explicit in `_CONTEXT.md` Covers Scope Items and Specification R10).
- Two `TRACES_TO_REQUIREMENT` anchors to OBJ-004 and OBJ-007 emitted as FACT (Guidance explicitly names these as the strongest objective ties). OBJ-001, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010 listed in `_CONTEXT.md` were not emitted as trace anchors under CONSERVATIVE strictness because Guidance explicitly marks these as "directional context, not binding requirements" — best-effort package-grouping heuristic, ASSUMPTION-level per source text.

**Pass 2 (EXECUTION) decisions:**
- Four DOWNSTREAM HANDOVER edges emitted to DEL-079-02, DEL-079-03, DEL-079-04, DEL-079-06 — all explicitly named in Specification In Scope / Out of Scope / Verification sections. DEL-079-05 (Vendor Document Turnover) omitted: Specification names it in the companion deliverable list but does not explicitly state an artifact/information handover from this Scope of Work; emitting it would overstate the evidence under CONSERVATIVE strictness.
- Two UPSTREAM PREREQUISITE edges emitted to INTERFACE_REGISTER.csv (Specification R8 explicitly cites it) and DELIVERABLE_REGISTER.csv (Procedure Prerequisites explicitly lists it as required).
- SCOPE_LEDGER.csv and PACKAGE_REGISTER.csv are decomposition registers consumed implicitly; no explicit "requires receipt of" statement present in source — omitted under CONSERVATIVE strictness.

**Warnings:**
- None. Parent anchor (IMPLEMENTS_NODE) count = 1. No floating node. No ambiguous anchor.

---

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 13 |
| RETIRED | 0 |
| **Total** | **13** |

| SatisfactionStatus | Count |
|---|---|
| TBD | 13 |

| DependencyClass | ACTIVE |
|---|---|
| ANCHOR | 7 |
| EXECUTION | 6 |

---

## Run History

| Date | Mode | Strictness | Decomp Status | Warnings | ACTIVE | RETIRED |
|---|---|---|---|---|---|---|
| 2026-05-24 | — | — | — | Initialized dependency view in DECLARED mode (PREPARATION) | 0 | 0 |
| 2026-05-25 | UPDATE | CONSERVATIVE | PRESENT (GATE-07_Final_Published_2026-05-24) | None | 13 | 0 |
