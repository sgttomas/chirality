# Dependencies: DEL-081-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-26)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` (v3.1) is the canonical structured register; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

---

## Extracted Dependency Register

Produced by `dependency-extract` skill run on 2026-05-26. See `Dependencies.csv` for full row details.

**Total rows: 14 | ACTIVE: 14 | RETIRED: 0**

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-081-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-081 | Flare KO Drum (High Pressure) 3-25 | HIGH | ACTIVE |
| DEP-081-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0071 | Scope Item SOW-0071 | HIGH | ACTIVE |
| DEP-081-04-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0072 | Scope Item SOW-0072 | HIGH | ACTIVE |
| DEP-081-04-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0073 | Scope Item SOW-0073 | HIGH | ACTIVE |
| DEP-081-04-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0074 | Scope Item SOW-0074 | MEDIUM | ACTIVE |
| DEP-081-04-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-002 | Objective OBJ-002 | MEDIUM | ACTIVE |
| DEP-081-04-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Objective OBJ-004 | HIGH | ACTIVE |
| DEP-081-04-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | Objective OBJ-007 | HIGH | ACTIVE |
| DEP-081-04-009 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Objective OBJ-009 | HIGH | ACTIVE |
| DEP-081-04-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-081-01_scope-of-work | Scope of Work | HIGH | ACTIVE |
| DEP-081-04-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-081-02_package-datasheet | Package Datasheet | HIGH | ACTIVE |
| DEP-081-04-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-081-05_vendor-document-turnover-package | Vendor Document Turnover Package | HIGH | ACTIVE |
| DEP-081-04-013 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-081-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance | HIGH | ACTIVE |
| DEP-081-04-014 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-081-03_construction-work-package | Construction Work Package | HIGH | ACTIVE |

**ANCHOR rows:** 9 (1 IMPLEMENTS_NODE + 8 TRACES_TO_REQUIREMENT)
**EXECUTION rows:** 5 (2 UPSTREAM PREREQUISITE + 3 DOWNSTREAM)

---

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 14 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 10 |
| PENDING | 2 |

**Open prerequisite items (PENDING):**
- DEP-081-04-010: DEL-081-01 Scope of Work not yet issued.
- DEP-081-04-011: DEL-081-02 Package Datasheet not yet issued — all design conditions (pressure, temperature, relief load) remain TBD pending this deliverable.

---

## Run Notes

**Run date:** 2026-05-26
**MODE:** UPDATE
**STRICTNESS:** CONSERVATIVE
**CONSUMER_CONTEXT:** NONE
**SOURCE_DOCS:** AUTO

**Decomposition path:**
- Provided path `GATE-07_Final_Published_2026-05-24/` did not exist at the exact invocation path.
- Resolved via `_REFERENCES.md` and confirmed under: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PROJECT_DECOMP.md`
- PACKAGE_REGISTER.csv, DELIVERABLE_REGISTER.csv, SCOPE_LEDGER.csv, and INTERFACE_REGISTER.csv from that snapshot were used to validate anchors and resolve canonical labels.
- This path resolution is non-blocking per skill instructions.

**Source documents scanned (AUTO):**
- `Datasheet.md` — used as ANCHOR_DOC (contains Identification/Attributes with WBS ref, scope items, objectives)
- `Specification.md` — EXECUTION_DOC (requirements, explicit prerequisites)
- `Procedure.md` — EXECUTION_DOC (procedure steps, explicit prerequisites, handovers)
- `Guidance.md` — EXECUTION_DOC (purpose section, downstream consumer explicit references)
- `_CONTEXT.md` — read-only context (identity, scope items, objectives)

**ANCHOR_DOC chosen:** `Datasheet.md` (contains explicit Identification/parent/scope-item fields — highest-confidence anchor doc)
**EXECUTION_DOC_ORDER:** Procedure.md, Specification.md, Guidance.md (procedure has most explicit prerequisites and handover steps)

**Defaults applied:**
- `DOC_ROLE_MAP`: DEFAULT (Datasheet.md matched `datasheet` pattern → ANCHOR_DOC; Procedure.md matched `procedure` → EXECUTION)
- All other defaults per SKILL.md.

**Tree x DAG integrity:**
- 1 IMPLEMENTS_NODE row found (DEP-081-04-001 → PKG-081). No FLOATING_NODE warning.
- No AMBIGUOUS_ANCHOR warning (single parent anchor only).

**Objective rows (OBJ-005, OBJ-006, OBJ-008, OBJ-010) not emitted:**
- CONSERVATIVE mode: objectives OBJ-005, OBJ-006, OBJ-008, OBJ-010 are listed in _CONTEXT.md and Datasheet.md with the qualifier "ASSUMPTION: PACKAGE_HEURISTIC mapping". Only objectives with a clear and explicit connection to this deliverable's core function were emitted (OBJ-002 = 03-25 facility, OBJ-004 = vendor package model, OBJ-007 = flare/vent/utilities, OBJ-009 = safety/relief). The remaining four are plausible but the source carries only a heuristic mapping note; CONSERVATIVE posture omits them to avoid overloading the trace register.

**Warnings:** None (no FLOATING_NODE, no MISSING_DECOMPOSITION, no AMBIGUOUS_ANCHOR).

---

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-26 — dependency-extract skill run (MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE). First extraction run. 14 rows written (9 ANCHOR, 5 EXECUTION). Decomposition resolved via _REFERENCES.md to GATE-07 snapshot. No integrity warnings.
