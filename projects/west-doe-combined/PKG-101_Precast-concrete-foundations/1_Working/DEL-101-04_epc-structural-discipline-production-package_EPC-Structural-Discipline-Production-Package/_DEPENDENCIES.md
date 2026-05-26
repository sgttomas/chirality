# Dependencies: DEL-101-04_epc-structural-discipline-production-package — EPC / Structural Discipline Production Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-26)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1). This file is the human-readable index and declared-list surface.

---

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

---

## Extracted Dependency Register

`Dependencies.csv` generated 2026-05-26 by `TASK + dependency-extract` (MODE=UPDATE, STRICTNESS=CONSERVATIVE).

### Summary counts

| DependencyClass | AnchorType / DependencyType | Direction | Status | Count |
|---|---|---|---|---|
| ANCHOR | IMPLEMENTS_NODE | UPSTREAM | ACTIVE | 1 |
| ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | ACTIVE | 3 |
| EXECUTION | PREREQUISITE | UPSTREAM | ACTIVE | 3 |
| EXECUTION | INTERFACE | UPSTREAM | ACTIVE | 1 |
| EXECUTION | CONSTRAINT | UPSTREAM | ACTIVE | 1 |
| **Total ACTIVE** | | | | **9** |
| **Total RETIRED** | | | | **0** |

### Compact table (ACTIVE rows)

| DependencyID | Class | AnchorType / DepType | Direction | TargetType | TargetName | Confidence |
|---|---|---|---|---|---|---|
| DEP-101-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | WBS_NODE | PKG-101 — Precast concrete foundations | HIGH |
| DEP-101-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | SOW-0257 | HIGH |
| DEP-101-04-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | OBJ-001 | HIGH |
| DEP-101-04-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | OBJ-008 | HIGH |
| DEP-101-04-005 | EXECUTION | PREREQUISITE | UPSTREAM | DOCUMENT | GATE-07 PROJECT_DECOMP snapshot | HIGH |
| DEP-101-04-006 | EXECUTION | PREREQUISITE | UPSTREAM | DOCUMENT | Workbook Packages row 102 (26020-Packages_Interfaces_4_export.xlsx) | HIGH |
| DEP-101-04-007 | EXECUTION | INTERFACE | UPSTREAM | DELIVERABLE | DEL-101-02 — Package Datasheet (interface facts carrier) | HIGH |
| DEP-101-04-008 | EXECUTION | CONSTRAINT | UPSTREAM | EXTERNAL | Human responsibility assignment record | HIGH |
| DEP-101-04-009 | EXECUTION | PREREQUISITE | UPSTREAM | DOCUMENT | 26020-Package_Requirements.docx | LOW |

---

## Lifecycle Summary

| Dimension | Count |
|---|---|
| ACTIVE | 9 |
| RETIRED | 0 |
| SatisfactionStatus = TBD | 8 |
| SatisfactionStatus = PENDING | 1 (DEP-101-04-008 — human responsibility assignment) |
| Confidence = HIGH | 8 |
| Confidence = LOW | 1 (DEP-101-04-009 — 26020-Package_Requirements.docx) |

**Tree integrity:** 1 IMPLEMENTS_NODE anchor (DEP-101-04-001). No FLOATING_NODE warning. No AMBIGUOUS_ANCHOR warning.

---

## Run Notes

**Run date:** 2026-05-26
**Mode:** UPDATE
**Strictness:** CONSERVATIVE
**Consumer context:** NONE

**Decomposition path used:**
`/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
(from `_DEPENDENCIES.md` Run Notes and `_REFERENCES.md` Authoritative Decomposition Basis — path confirmed; files accessible)

**Source documents scanned (AUTO):**
- `Datasheet.md` — ANCHOR_DOC (contains identification/traceability fields)
- `Specification.md` — EXECUTION_DOC (contains requirements, standards, scope boundaries)
- `Procedure.md` — EXECUTION_DOC (contains prerequisites, steps, constraints)
- `Guidance.md` — EXECUTION_DOC (contains considerations, interface ownership, trade-off rationale)

Excluded from scan: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`, `_MEMORY.md` (metadata/governance files, not source documents), `_run_records/` (execution records).

**Defaults applied:**
- `SOURCE_DOCS=AUTO` — scanned deliverable folder; four content documents identified.
- `DOC_ROLE_MAP=DEFAULT` — Datasheet.md as ANCHOR_DOC (contains identification/traceability); Specification.md, Procedure.md, Guidance.md as EXECUTION_DOCs.
- `ANCHOR_DOC=AUTO` → Datasheet.md (highest-confidence traceability signal).
- `EXECUTION_DOC_ORDER=AUTO` → Specification.md, Procedure.md, Guidance.md.

**Pass 1 (ANCHOR) notes:**
- Parent anchor DEP-101-04-001: confirmed PKG-101 in PACKAGE_REGISTER.csv.
- Requirement traces DEP-101-04-002..004: SOW-0257, OBJ-001, OBJ-008 confirmed in SCOPE_LEDGER.csv and OBJECTIVE_DELIVERABLE_MAP.csv.
- CONF-101-04-03 in Guidance.md flagged OBJ-001/OBJ-008 as ASSUMPTION; OBJECTIVE_DELIVERABLE_MAP.csv rows confirmed both → recorded as FACT in Notes.

**Pass 2 (EXECUTION) notes:**
- Sibling deliverable boundary references (DEL-101-01..03) in Specification.md §Scope are structural adjacency, not information-flow dependencies → excluded per skill rules.
- DEP-101-04-007 (INTERFACE, DEL-101-02): explicit statement in Guidance.md that interface facts IFC-26343B703C and IFC-BED3DE4194 are "recorded primarily as datasheet evidence under DEL-101-02" and that DEL-101-04 "must coordinate" with those interface facts for R-101-04-04 compliance. This is an explicit information-transfer/constraint relationship, not pure coordination.
- DEP-101-04-008 (CONSTRAINT, human assignment): R-101-04-08 in Specification.md and Procedure.md Prerequisites are explicit; K-AUTH-1 governance makes this a hard constraint. SatisfactionStatus=PENDING.
- DEP-101-04-009 (PREREQUISITE, 26020-Package_Requirements.docx): Procedure Step 3 requires this document to be opened; applicability is ASSUMPTION per Specification.md; Confidence=LOW, Explicitness=IMPLICIT.
- DBM-Deepcut SEC-11 (also mentioned in Procedure Step 3 and Specification §Standards): parallel candidate source to 26020-Package_Requirements.docx. Not emitted as a separate row because no stable document identifier is resolvable to a canonical pointer in _REFERENCES.md; would duplicate low-confidence intent of DEP-101-04-009. Noted here for downstream attention — if DBM-Deepcut SEC-11 is opened as a source slice it should be registered as a separate PREREQUISITE DOCUMENT row.

**Warnings:**
- None. No FLOATING_NODE, no AMBIGUOUS_ANCHOR, no MISSING_DECOMPOSITION.

---

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-26 — First extraction run. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition: GATE-07_Final_Published_2026-05-24 (confirmed accessible). 9 ACTIVE rows written (4 ANCHOR, 5 EXECUTION). 0 RETIRED. No integrity warnings.
