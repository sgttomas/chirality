# Dependencies: DEL-011-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill, UPDATE mode)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is authoritative (v3.1 schema); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Extracted by `TASK + dependency-extract` skill — UPDATE mode — 2026-05-25.

**Counts:** 13 ACTIVE rows (8 ANCHOR, 5 EXECUTION). 0 RETIRED rows.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetID / TargetRefID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-011-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0012 | Scope decision SOW-0012 — 4160V SWITCHGEAR EQUIPMENT (WBS 02) | HIGH | ACTIVE |
| DEP-011-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-002 | Project Objective OBJ-002 — 03-25 compressor station and liquids hub scope | HIGH | ACTIVE |
| DEP-011-04-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Project Objective OBJ-004 — vendor-owned package execution responsibility model | HIGH | ACTIVE |
| DEP-011-04-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Project Objective OBJ-005 — facility electrical power basis and switchgear/MCC/VFD integration | HIGH | ACTIVE |
| DEP-011-04-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Project Objective OBJ-006 — controls instrumentation and communications integration | HIGH | ACTIVE |
| DEP-011-04-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Project Objective OBJ-008 — civil structural and foundations scope | HIGH | ACTIVE |
| DEP-011-04-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 — sour-service safety regulatory and codes requirements | HIGH | ACTIVE |
| DEP-011-04-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 — operability maintainability vendor documentation and turnover | HIGH | ACTIVE |
| DEP-011-04-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-011-01_scope-of-work | Scope of Work | HIGH | ACTIVE |
| DEP-011-04-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-011-02_package-datasheet | Package Datasheet | HIGH | ACTIVE |
| DEP-011-04-011 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-011-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance | HIGH | ACTIVE |
| DEP-011-04-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-011-05_vendor-document-turnover-package | Vendor Document Turnover Package | MEDIUM | ACTIVE |
| DEP-011-04-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DELIVERABLE | DEL-011-03_construction-work-package | Construction Work Package | MEDIUM | ACTIVE |

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; found: `Datasheet.md`, `Specification.md`, `Procedure.md`, `Guidance.md`
- **ANCHOR_DOC:** `Datasheet.md` (contains identification, WBS Ref, Scope Item, Objectives — highest anchor signal)
- **EXECUTION_DOC_ORDER:** `Procedure.md`, `Specification.md`, `Guidance.md`, `Datasheet.md`
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — used to validate anchors, resolve SOW-0012 and objective labels, and confirm sibling deliverable IDs.
- **BRIEF DECOMPOSITION_PATH:** `GATE-07_Final_Published_2026-05-24` — path in brief (`GATE-07_Final_Published_2026-05-24/` at run root) resolved to `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` via `_REFERENCES.md`.
- **Pass 1 (ANCHOR):** SOW-0012 confirmed as parent scope node from SCOPE_LEDGER.csv. Objectives OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010 confirmed from DELIVERABLE_REGISTER.csv and OBJECTIVE_DELIVERABLE_MAP.csv.
- **Pass 2 (EXECUTION):** Four execution edges extracted: two UPSTREAM PREREQUISITE (DEL-011-01, DEL-011-02), one DOWNSTREAM HANDOVER (DEL-011-06), one DOWNSTREAM HANDOVER (DEL-011-05, MEDIUM confidence), one UPSTREAM INTERFACE (DEL-011-03, MEDIUM confidence).
- **Confidence notes:** DEP-011-04-012 and DEP-011-04-013 are MEDIUM because the handover and interface relationships are strongly implied by package structure and stated interface types respectively, but verbatim transfer statements are not present in source text for those specific sibling pairs.
- **Tree x DAG integrity:** 1 IMPLEMENTS_NODE anchor found (SOW-0012). Parent anchor check: PASS.
- No FLOATING_NODE or AMBIGUOUS_ANCHOR warnings.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 13 |
| RETIRED | 0 |
| **Total** | **13** |

**SatisfactionStatus breakdown (ACTIVE rows):** All 13 rows: `TBD`

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract skill; UPDATE mode; CONSERVATIVE strictness; decomposition GATE-07_Final_Published_2026-05-24 used; 13 ACTIVE rows extracted (8 ANCHOR, 5 EXECUTION); 0 RETIRED; no warnings.
