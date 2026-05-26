# Dependencies: DEL-048-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (Dependencies.csv v3.1)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register; this file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

---

## Extracted Dependency Register

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetID / TargetName | Status |
|---|---|---|---|---|---|---|---|
| DEP-048-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-048 Inlet / Sales Compressors | ACTIVE |
| DEP-048-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0115 | ACTIVE |
| DEP-048-04-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0116 | ACTIVE |
| DEP-048-04-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0117 | ACTIVE |
| DEP-048-04-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0118 | ACTIVE |
| DEP-048-04-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-048-01_scope-of-work | ACTIVE |
| DEP-048-04-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-048-02_package-datasheet | ACTIVE |
| DEP-048-04-008 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-048-05_vendor-document-turnover-package | ACTIVE |
| DEP-048-04-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-048-06_epc-vendor-package-review-and-acceptance | ACTIVE |
| DEP-048-04-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | 26020-Package_Requirements.docx | ACTIVE |

**Total ACTIVE rows:** 10 (5 ANCHOR, 5 EXECUTION)
**Total RETIRED rows:** 0

---

## Run Notes

- **Run date:** 2026-05-25
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; documents in scope: `_CONTEXT.md`, `Datasheet.md`, `Guidance.md`, `Procedure.md`, `Specification.md`, `_REFERENCES.md`
- **ANCHOR_DOC:** `Datasheet.md` (heuristic match on filename containing "datasheet"); corroborated by `_CONTEXT.md`
- **EXECUTION_DOC_ORDER:** `Procedure.md` (primary), `Guidance.md`, `Specification.md`
- **DECOMPOSITION_PATH used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — NOTE: the invoker's DECOMPOSITION_PATH pointed to a path that does not exist as a directory; the correct path was resolved by reading `_CONTEXT.md` and `_REFERENCES.md`. The correct snapshot folder was used for anchor validation.
- **Anchor validation:** PKG-048 confirmed in GATE-07 PACKAGE_REGISTER. Scope items SOW-0115..SOW-0118 confirmed in GATE-07 DELIVERABLE_REGISTER row for DEL-048-04.
- **CONF-002 resolution:** Guidance.md documents a conflict between the role description (which names DEL-048-01 and DEL-048-02 as upstream basis) and the previously empty declared dependency list. Procedure.md explicitly lists these as prerequisites. Both extracted as EXECUTION/PREREQUISITE rows (DEP-048-04-006, DEP-048-04-007) per CONSERVATIVE strictness — evidence is explicit in Procedure.md, not merely implied.
- **Tree x DAG integrity:** One parent anchor (IMPLEMENTS_NODE → PKG-048) found. No FLOATING_NODE or AMBIGUOUS_ANCHOR warnings.
- **Schema validation:** VALID — 29 required columns, 10 data rows.

---

## Lifecycle Summary

| Dimension | Count |
|---|---|
| ACTIVE rows | 10 |
| RETIRED rows | 0 |
| ANCHOR / IMPLEMENTS_NODE | 1 |
| ANCHOR / TRACES_TO_REQUIREMENT | 4 |
| EXECUTION / UPSTREAM / PREREQUISITE | 3 |
| EXECUTION / DOWNSTREAM / HANDOVER | 2 |
| SatisfactionStatus = TBD | 10 |
| SatisfactionStatus = PENDING | 0 |
| SatisfactionStatus = SATISFIED | 0 |

---

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full two-pass extraction run (UPDATE / CONSERVATIVE / CONSUMER_CONTEXT=NONE). Created Dependencies.csv v3.1 with 10 ACTIVE rows (5 ANCHOR, 5 EXECUTION). No RETIRED rows. Schema VALID. No integrity warnings.
