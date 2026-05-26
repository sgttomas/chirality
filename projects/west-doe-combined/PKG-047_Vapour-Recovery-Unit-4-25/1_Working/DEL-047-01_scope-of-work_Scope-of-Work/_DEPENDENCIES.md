# Dependencies: DEL-047-01_scope-of-work — Scope of Work

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

**Register:** `Dependencies.csv` (v3.1) — 13 rows, all ACTIVE.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence |
|---|---|---|---|---|---|---|---|---|
| DEP-047-01-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-047 | Vapour Recovery Unit 4-25 | HIGH |
| DEP-047-01-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0253 | Scope of Work — Package scope of work artifact | HIGH |
| DEP-047-01-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0254 | Package scope of work — tagged equipment and package identity list | HIGH |
| DEP-047-01-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0255 | Package function and integration narrative | HIGH |
| DEP-047-01-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0256 | Responsibility assignment record | HIGH |
| DEP-047-01-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | DELIVERABLE_REGISTER-ROW570 | PROJECT_DECOMP Gate-07 Deliverable Register (row 570) | HIGH |
| DEP-047-01-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | DBM-Deepcut 4-25_Deepcut_DBM.md (primary technical source) | HIGH |
| DEP-047-01-008 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-047-02_package-datasheet | Package Datasheet | HIGH |
| DEP-047-01-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-047-03_construction-work-package | Construction Work Package | MEDIUM |
| DEP-047-01-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | PREREQUISITE | DELIVERABLE | DEL-047-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package | HIGH |
| DEP-047-01-011 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-047-05_vendor-document-turnover-package | Vendor Document Turnover Package | MEDIUM |
| DEP-047-01-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-047-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance | MEDIUM |
| DEP-047-01-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | — | 03-25 VRU Package (cross-facility scope) | MEDIUM |

**ANCHOR rows:** 5 (1 IMPLEMENTS_NODE + 4 TRACES_TO_REQUIREMENT)
**EXECUTION rows:** 8 (2 UPSTREAM, 6 DOWNSTREAM)

---

## Run Notes

- **Run date:** 2026-05-25
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; found `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` as source documents. `_CONTEXT.md`, `_REFERENCES.md`, `_STATUS.md`, `_MEMORY.md` read-only inputs.
- **DOC_ROLE_MAP:** DEFAULT — `Specification.md` selected as ANCHOR_DOC (filename contains "scope" / specification signals); `Procedure.md`, `Guidance.md`, `Datasheet.md` as EXECUTION_DOC_ORDER.
- **ANCHOR_DOC:** `Specification.md` (highest anchor signal); cross-validated against `Datasheet.md` §Identification.
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` — confirmed PKG-047 and DEL-047-01 exist in register; row 570 used for anchor resolution. Note: DECOMPOSITION_PATH in run brief referenced `GATE-07_Final_Published_2026-05-24/` as a direct path which does not exist; resolved to `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` per `_REFERENCES.md`.
- **Parent anchor:** DEP-047-01-001 (IMPLEMENTS_NODE → PKG-047) confirmed against decomposition. Count = 1. No FLOATING_NODE or AMBIGUOUS_ANCHOR warnings.
- **26020-Package_Requirements.docx** and **26020-Packages_Interfaces_4_export.xlsx** are not locally extracted (flagged as `location TBD` in source documents). No dependency rows emitted for these sources as prerequisite documents — they appear in `_REFERENCES.md` as deferred/missing; Procedure §Prerequisites explicitly flags them. CONSERVATIVE strictness: no rows emitted without explicit evidence text.
- **Cross-facility coupling (03-25 VRU):** Row DEP-047-01-013 emitted as EXTERNAL INTERFACE based on explicit statement in Guidance §Cross-Facility Coupling. This is flagged for tracking in the integration narrative per that guidance section.
- **No rows retired** — this is the first extraction run; no prior register existed.

---

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 13 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 13 |

| DependencyClass | ACTIVE count |
|---|---|
| ANCHOR | 5 |
| EXECUTION | 8 |

---

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First extraction run. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition: GATE-07_Final_Published_2026-05-24 (confirmed). Created Dependencies.csv v3.1 with 13 ACTIVE rows (5 ANCHOR, 8 EXECUTION). No warnings. Schema validation: VALID.
