# Dependencies: DEL-003-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** DECLARED + EXTRACTED
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1); this file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

**Total rows:** 15 | **ACTIVE:** 15 | **RETIRED:** 0

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetName / TargetRefID | Status |
|---|---|---|---|---|---|---|---|
| DEP-003-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0003 — Site Grading (WBS 01) | ACTIVE |
| DEP-003-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 — 04-25 Deepcut facility scope | ACTIVE |
| DEP-003-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 — Shared utilities and ancillary support | ACTIVE |
| DEP-003-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 — Civil/structural/site scope | ACTIVE |
| DEP-003-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 — Safety/regulatory/codes and standards | ACTIVE |
| DEP-003-02-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-003-01_scope-of-work | ACTIVE |
| DEP-003-02-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | Gate 7 decomposition registers | ACTIVE |
| DEP-003-02-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | Workbook Packages row 4 | ACTIVE |
| DEP-003-02-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | Geotechnical assessment report | ACTIVE |
| DEP-003-02-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | Topographical survey / grade surface file | ACTIVE |
| DEP-003-02-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | Plot plan (retention pond location and capacity) | ACTIVE |
| DEP-003-02-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | Detailed drainage engineering (IDF curve) | ACTIVE |
| DEP-003-02-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | DBM-Deepcut SEC-11 civil source sections | ACTIVE |
| DEP-003-02-014 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-003-03_construction-work-package | ACTIVE |
| DEP-003-02-015 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-003-04_epc-civil-discipline-production-package | ACTIVE |

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 15 |
| RETIRED | 0 |

| SatisfactionStatus | Count (ACTIVE rows) |
|---|---|
| TBD | 8 |
| PENDING | 4 |
| SATISFIED | 3 |
| NOT_APPLICABLE | 0 |

## Run Notes

**Run date:** 2026-05-25
**Mode:** UPDATE
**Strictness:** CONSERVATIVE
**Decomposition path used:** `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` (from DECOMPOSITION_PATH brief parameter; confirmed via _REFERENCES.md)
**Source documents scanned (AUTO):**
- `Datasheet.md` — ANCHOR_DOC (contains "datasheet" in filename; primary anchor signals)
- `Procedure.md` — EXECUTION_DOC (contains "procedure"; explicit prerequisite signals)
- `Guidance.md` — EXECUTION_DOC (supporting execution context)
**DOC_ROLE_MAP:** DEFAULT
**Consumer context:** NONE
**Decomposition status:** Located and read successfully. SOW-0003, PKG-003, DEL-003-02, OBJ-001/007/008/009 all confirmed in registers.

**Pass 1 (ANCHOR) summary:**
- 1 IMPLEMENTS_NODE anchor: SOW-0003 (confirmed in SCOPE_LEDGER.csv and Datasheet.md Identification table).
- 4 TRACES_TO_REQUIREMENT anchors: OBJ-001, OBJ-007, OBJ-008, OBJ-009 (confirmed in DELIVERABLE_REGISTER.csv and OBJECTIVE_DELIVERABLE_MAP.csv).
- No FLOATING_NODE or AMBIGUOUS_ANCHOR warning: exactly one IMPLEMENTS_NODE anchor found.

**Pass 2 (EXECUTION) summary:**
- 10 EXECUTION rows extracted (8 UPSTREAM, 2 DOWNSTREAM).
- 4 PENDING upstream PREREQUISITE rows for external documents not yet available in _Sources (geotechnical assessment, topographical survey, plot plan, detailed drainage engineering).
- 3 SATISFIED upstream rows (Gate 7 registers, Workbook row 4, DBM-Deepcut SEC-11) — source confirmed accessible.
- 1 UPSTREAM PREREQUISITE to DEL-003-01 (Scope of Work) per package structure.
- 2 DOWNSTREAM ENABLES rows to DEL-003-03 and DEL-003-04 within PKG-003 per DELIVERABLE_REGISTER.

**Assumptions and epistemic labels:**
- FACT: All anchor IDs confirmed in Gate 7 decomposition registers.
- FACT: External document dependencies (geotechnical, survey, plot plan, drainage) are explicitly listed as open in Datasheet.md Attributes and Conditions tables.
- FACT: Gate 7 registers and DBM-Deepcut are confirmed available in _Sources.
- The downstream ENABLES rows (DEL-003-03, DEL-003-04) are Confidence=MEDIUM because explicit handover statements appear in DELIVERABLE_REGISTER descriptions and Guidance.md Purpose, not in a direct cross-deliverable source quote.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract run; MODE=UPDATE; STRICTNESS=CONSERVATIVE; decomposition confirmed at GATE-07_Final_Published_2026-05-24; 15 rows extracted (5 ANCHOR, 10 EXECUTION); schema validated VALID.
