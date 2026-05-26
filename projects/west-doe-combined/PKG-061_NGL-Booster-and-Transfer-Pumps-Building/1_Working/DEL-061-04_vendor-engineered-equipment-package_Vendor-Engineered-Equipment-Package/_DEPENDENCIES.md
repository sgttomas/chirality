# Dependencies: DEL-061-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is canonical; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

10 rows extracted (10 ACTIVE, 0 RETIRED). Schema version: v3.1.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetID / TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-061-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-061 — NGL Booster and Transfer Pumps Building | HIGH | ACTIVE |
| DEP-061-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0149 | HIGH | ACTIVE |
| DEP-061-04-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0150 | HIGH | ACTIVE |
| DEP-061-04-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0151 | HIGH | ACTIVE |
| DEP-061-04-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0152 | HIGH | ACTIVE |
| DEP-061-04-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-061-01_scope-of-work | HIGH | ACTIVE |
| DEP-061-04-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-061-02_package-datasheet | HIGH | ACTIVE |
| DEP-061-04-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DELIVERABLE | DEL-061-03_construction-work-package | MEDIUM | ACTIVE |
| DEP-061-04-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-061-05_vendor-document-turnover-package | HIGH | ACTIVE |
| DEP-061-04-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-061-06_epc-vendor-package-review-and-acceptance | HIGH | ACTIVE |

## Run Notes

- **Run date:** 2026-05-25
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; found: `Datasheet.md`, `Guidance.md`, `Procedure.md`, `Specification.md`, `_CONTEXT.md`, `_REFERENCES.md`
- **DOC_ROLE_MAP:** DEFAULT — `Datasheet.md` treated as ANCHOR_DOC (matches `datasheet` keyword); `Procedure.md` and `Guidance.md` treated as EXECUTION_DOC primary sources; `Specification.md` used as corroborating execution evidence
- **ANCHOR_DOC:** `Datasheet.md` (highest-confidence anchor doc per DEFAULT heuristic)
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — used for anchor validation. Note: `DECOMPOSITION_PATH` in brief pointed to a non-existent path; resolved to actual gate snapshot location via discovery under `_Decomposition/`.
- **Prior Dependencies.csv:** not present — created fresh.
- **Pass 1 (ANCHOR):** Parent anchor `PKG-061` confirmed in `DELIVERABLE_REGISTER.csv` row 417 and Datasheet identification table. Four SOW requirement anchors (`SOW-0149..SOW-0152`) confirmed in Specification R-061-04-10 and DELIVERABLE_REGISTER row 417. Objective anchors (`OBJ-001`, `OBJ-003..OBJ-010`) noted in Datasheet but not emitted as separate rows — they are associated at package level (ASSUMPTION: PACKAGE_HEURISTIC per DELIVERABLE_REGISTER) and their individual traceability belongs in PKG-level or SSOW-level registers.
- **Pass 2 (EXECUTION):** Five execution edges extracted: two upstream prerequisites (`DEL-061-01`, `DEL-061-02`) from Procedure Prerequisites; one upstream interface (`DEL-061-03`) from Guidance building/enclosure integration consideration; two downstream handovers (`DEL-061-05`, `DEL-061-06`) from Procedure Steps 14 and 7.
- **Integrity:** 1 parent anchor found (DEP-061-04-001). No FLOATING_NODE, no AMBIGUOUS_ANCHOR warnings.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full two-pass extraction run (dependency-extract skill, UPDATE, CONSERVATIVE). Created `Dependencies.csv` v3.1 with 10 ACTIVE rows. Decomposition path resolved to GATE-07_Final_Published_2026-05-24 snapshot.

## Lifecycle Summary

- **ACTIVE rows:** 10
- **RETIRED rows:** 0
- **ANCHOR rows (ACTIVE):** 5 (1 IMPLEMENTS_NODE + 4 TRACES_TO_REQUIREMENT)
- **EXECUTION rows (ACTIVE):** 5 (2 UPSTREAM PREREQUISITE + 1 UPSTREAM INTERFACE + 2 DOWNSTREAM HANDOVER)
- **SatisfactionStatus breakdown:** 10 TBD
- **Parent anchor check:** PASS — 1 IMPLEMENTS_NODE row present (DEP-061-04-001)
