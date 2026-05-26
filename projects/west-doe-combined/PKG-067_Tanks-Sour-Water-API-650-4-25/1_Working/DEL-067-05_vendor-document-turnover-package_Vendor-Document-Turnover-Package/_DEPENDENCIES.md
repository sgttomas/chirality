# Dependencies: DEL-067-05_vendor-document-turnover-package — Vendor Document Turnover Package

**Coordination Mode:** DECLARED
**Dependency tracking mode:** DECLARED + EXTRACTED
**Default maturity threshold:** INITIALIZED
**Register convention:** Prefer `Dependencies.csv` when produced by `TASK + dependency-extract`; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

**Register file:** `Dependencies.csv` (v3.1 schema, 10 rows)

**Summary counts (ACTIVE):**

| DependencyClass | AnchorType / DependencyType | Direction | Count |
|---|---|---|---|
| ANCHOR | IMPLEMENTS_NODE | UPSTREAM | 1 |
| ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | 4 |
| EXECUTION | PREREQUISITE | UPSTREAM | 3 |
| EXECUTION | PREREQUISITE (DOCUMENT) | UPSTREAM | 1 |
| EXECUTION | HANDOVER | DOWNSTREAM | 1 |
| **TOTAL ACTIVE** | | | **10** |

**Compact table:**

| DependencyID | Class | AnchorType/DepType | Direction | TargetType | TargetID / TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|
| DEP-067-05-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | PACKAGE | PKG-067 | HIGH | ACTIVE |
| DEP-067-05-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | SOW-0225 | HIGH | ACTIVE |
| DEP-067-05-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | SOW-0226 | HIGH | ACTIVE |
| DEP-067-05-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | SOW-0227 | HIGH | ACTIVE |
| DEP-067-05-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | SOW-0228 | HIGH | ACTIVE |
| DEP-067-05-006 | EXECUTION | PREREQUISITE | UPSTREAM | DELIVERABLE | DEL-067-01_scope-of-work | HIGH | ACTIVE |
| DEP-067-05-007 | EXECUTION | PREREQUISITE | UPSTREAM | DELIVERABLE | DEL-067-02_package-datasheet | HIGH | ACTIVE |
| DEP-067-05-008 | EXECUTION | PREREQUISITE | UPSTREAM | DELIVERABLE | DEL-067-04_vendor-engineered-equipment-package | HIGH | ACTIVE |
| DEP-067-05-009 | EXECUTION | HANDOVER | DOWNSTREAM | DELIVERABLE | DEL-067-06_epc-vendor-package-review-and-acceptance | HIGH | ACTIVE |
| DEP-067-05-010 | EXECUTION | PREREQUISITE | UPSTREAM | DOCUMENT | 26020-Package_Requirements.docx heading 22 | MEDIUM | ACTIVE |

## Run Notes

**Run configuration:**
- MODE: UPDATE
- STRICTNESS: CONSERVATIVE
- CONSUMER_CONTEXT: NONE
- SOURCE_DOCS: AUTO (scanned deliverable folder)
- ANCHOR_DOC: Datasheet.md (highest-confidence anchor match; contains Identification, WBS, scope items, parent package)
- EXECUTION_DOC_ORDER: Procedure.md (primary execution signal), Specification.md, Guidance.md
- DECOMPOSITION_PATH: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` (resolved from _CONTEXT.md; gate snapshot confirmed present)
- Invoker-supplied DECOMPOSITION_PATH (`GATE-07_Final_Published_2026-05-24/`) was not directly reachable as a file path — used canonical gate snapshot directory.

**Defaults applied:**
- DOC_ROLE_MAP: DEFAULT (no override)
- ANCHOR_DOC: AUTO → resolved to Datasheet.md
- EXECUTION_DOC_ORDER: AUTO → Procedure.md first (explicit prerequisites section), then Specification.md, Guidance.md

**Decomposition validation:**
- PKG-067 confirmed in PACKAGE_REGISTER.csv (row 94)
- DEL-067-01 through DEL-067-06 confirmed in DELIVERABLE_REGISTER.csv under PKG-067
- SOW-0225/0226/0227/0228 confirmed in DELIVERABLE_REGISTER.csv Covered Scope Items column for DEL-067-05

**Warnings:**
- None. Parent anchor (IMPLEMENTS_NODE → PKG-067) is present; no FLOATING_NODE condition.

**Source binary limitation:**
- `26020-Package_Requirements.docx` and Workbook Packages row 94 are binary sources not converted to text. The dependency on heading 22 (DEP-067-05-010) is extracted from explicit prose citations in Procedure.md and Specification.md; confidence set to MEDIUM because the source document itself was not directly readable.

## Lifecycle Summary

| Dimension | Count |
|---|---|
| ACTIVE rows | 10 |
| RETIRED rows | 0 |
| SatisfactionStatus=TBD | 10 |
| SatisfactionStatus=SATISFIED | 0 |

All rows are ACTIVE/TBD — initial extraction run; no closure state established yet.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full two-pass extraction run (dependency-extract skill, MODE=UPDATE, STRICTNESS=CONSERVATIVE). Created Dependencies.csv v3.1 with 10 rows (5 ANCHOR, 5 EXECUTION). No warnings. Decomposition path: GATE-07_Final_Published_2026-05-24 (confirmed). All targets resolved from decomposition registers or explicit source text.
