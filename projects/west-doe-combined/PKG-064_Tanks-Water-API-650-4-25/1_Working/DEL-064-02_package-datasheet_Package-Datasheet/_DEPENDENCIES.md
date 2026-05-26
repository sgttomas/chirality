# Dependencies: DEL-064-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract run completed)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1 schema); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` produced by `TASK + dependency-extract` — 10 rows, all ACTIVE.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-064-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-064 | Package PKG-064 — Tanks Water (API 650) 4-25 | HIGH | ACTIVE |
| DEP-064-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0233 | Scope decision SOW-0233 | HIGH | ACTIVE |
| DEP-064-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0234 | Scope item SOW-0234 — basic scope (2x 2000 bbl tanks) | HIGH | ACTIVE |
| DEP-064-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0235 | Scope item SOW-0235 — major included equipment | HIGH | ACTIVE |
| DEP-064-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0236 | Scope item SOW-0236 — scope notes and open items | HIGH | ACTIVE |
| DEP-064-02-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-064-01_scope-of-work | Scope of Work — PKG-064 | HIGH | ACTIVE |
| DEP-064-02-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | GATE-07 | GATE-07 PROJECT_DECOMP Snapshot | HIGH | ACTIVE |
| DEP-064-02-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | DBM-Deepcut | DBM-Deepcut — 4-25_Deepcut_DBM.md | HIGH | ACTIVE |
| DEP-064-02-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | PACKAGE | PKG-060 | Tank Farm Pump Building 4-25 (P-5317-1/P-5318-1 interface) | MEDIUM | ACTIVE |
| DEP-064-02-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-064-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package — PKG-064 | HIGH | ACTIVE |

## Run Notes

- **Run date:** 2026-05-25
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; Datasheet.md identified as ANCHOR_DOC (contains "datasheet" keyword and identification/traceability tables); Guidance.md, Specification.md, Procedure.md used as EXECUTION_DOC sources.
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — verified present; used to validate anchor identifiers (PKG-064, SOW-0233–SOW-0236, DEL-064-01, DEL-064-04, PKG-060).
- **RUN_ROOT:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined`

**Assumptions and resolutions recorded:**
- PKG-064 confirmed as parent package node in GATE-07 DELIVERABLE_REGISTER and PACKAGE_REGISTER (workbook row 96).
- SOW-0233, SOW-0234, SOW-0235, SOW-0236 confirmed in GATE-07 SCOPE_LEDGER as CoveredScopeItems for DEL-064-02.
- DEL-064-01 (Scope of Work) confirmed in GATE-07 DELIVERABLE_REGISTER as peer deliverable under PKG-064.
- DEL-064-04 (Vendor Engineered Equipment Package) confirmed in GATE-07 DELIVERABLE_REGISTER as the downstream vendor production unit consuming this datasheet.
- Datasheet.md references "Tank Farm Pump Building 2, row 83" for the process water transfer pump interface. GATE-07 PACKAGE_REGISTER row 83 is Storage Bullets (PKG-059), not a pump building. PKG-060 (Tank Farm Pump Building 4-25, workbook row 85) explicitly includes "2 Identical Pumps for Process water Transfer" matching P-5317-1/P-5318-1. DEP-064-02-009 records PKG-060 as target with Confidence=MEDIUM and ASSUMPTION note. [WARNING] label discrepancy "row 83" in Datasheet.md vs. decomposition requires human confirmation.

**[WARNING] LABEL_DISCREPANCY:** Datasheet.md cites "Tank Farm Pump Building 2, row 83" for the process water transfer pump interface. GATE-07 PACKAGE_REGISTER workbook row 83 = Storage Bullets (PKG-059). Likely the correct package is PKG-060 (Tank Farm Pump Building 4-25, row 85), which explicitly includes process water transfer pumps. Recorded as PKG-060 with Confidence=MEDIUM; requires human confirmation.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 10 |
| RETIRED | 0 |

**By DependencyClass:**
- ANCHOR: 5 (1 × IMPLEMENTS_NODE, 4 × TRACES_TO_REQUIREMENT)
- EXECUTION: 5 (2 × UPSTREAM PREREQUISITE DOCUMENT, 1 × UPSTREAM PREREQUISITE DELIVERABLE, 1 × UPSTREAM INTERFACE PACKAGE, 1 × DOWNSTREAM HANDOVER DELIVERABLE)

**SatisfactionStatus:** All 10 rows = TBD (not yet consumed by downstream workflows).

**Parent anchor check:** 1 ACTIVE ANCHOR IMPLEMENTS_NODE row (DEP-064-02-001). No FLOATING_NODE or AMBIGUOUS_ANCHOR warnings.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full two-pass dependency extraction (dependency-extract skill; MODE=UPDATE; STRICTNESS=CONSERVATIVE; CONSUMER_CONTEXT=NONE). Decomposition: GATE-07_Final_Published_2026-05-24 (verified). Produced 10 ACTIVE rows (5 ANCHOR, 5 EXECUTION). [WARNING] LABEL_DISCREPANCY on Tank Farm Pump Building "row 83" reference — recorded with Confidence=MEDIUM pending human confirmation.
