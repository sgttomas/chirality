# Dependencies: DEL-096-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-26)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1 schema); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Extracted by: `dependency-extract` skill, MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE
Run date: 2026-05-26
Source documents scanned (AUTO): `_CONTEXT.md`, `Datasheet.md`, `Guidance.md`, `Procedure.md`, `Specification.md`
Decomposition: GATE-07_Final_Published_2026-05-24 (resolved path — see Run Notes)

**Counts (ACTIVE):** 14 rows total — 5 ANCHOR, 9 EXECUTION

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-096-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-096 (Tanks Sour Condendate API 650) | HIGH | ACTIVE |
| DEP-096-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0217 | HIGH | ACTIVE |
| DEP-096-04-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0218 | HIGH | ACTIVE |
| DEP-096-04-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0219 | HIGH | ACTIVE |
| DEP-096-04-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0220 | HIGH | ACTIVE |
| DEP-096-04-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-096-01 Scope of Work | HIGH | ACTIVE |
| DEP-096-04-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-096-02 Package Datasheet | HIGH | ACTIVE |
| DEP-096-04-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | 26020-Package_Requirements.docx heading 48 | HIGH | ACTIVE |
| DEP-096-04-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | Final Tank Register | HIGH | ACTIVE |
| DEP-096-04-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | Final Geotechnical Report | MEDIUM | ACTIVE |
| DEP-096-04-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | VRU Header Tie-in Pressure and Design Data | HIGH | ACTIVE |
| DEP-096-04-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-096-03 Construction Work Package | HIGH | ACTIVE |
| DEP-096-04-013 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-096-05 Vendor Document Turnover Package | HIGH | ACTIVE |
| DEP-096-04-014 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-096-06 EPC Vendor Package Review and Acceptance | HIGH | ACTIVE |

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 14 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 10 |
| PENDING | 4 |

## Run Notes

- **MODE:** UPDATE (default)
- **STRICTNESS:** CONSERVATIVE (default)
- **CONSUMER_CONTEXT:** NONE (default)
- **DECOMPOSITION_PATH resolution:** Invocation specified `GATE-07_Final_Published_2026-05-24/` under RUN_ROOT; that exact path did not exist as stated. Resolved via `_REFERENCES.md` in this deliverable folder to: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PROJECT_DECOMP.md` (and sibling CSV registers). This is non-blocking per skill instructions.
- **SOURCE_DOCS:** AUTO — scanned `_CONTEXT.md`, `Datasheet.md`, `Guidance.md`, `Procedure.md`, `Specification.md`. Excluded dependency artifacts and `_STATUS.md`, `_MEMORY.md`.
- **ANCHOR_DOC:** `Datasheet.md` selected (AUTO heuristic: highest-confidence ANCHOR_DOC candidate by filename pattern containing `datasheet`).
- **EXECUTION_DOC_ORDER:** `Procedure.md` first (filename contains `procedure`), then `Specification.md`, `Guidance.md`, `Datasheet.md` (supplementary).
- **Parent anchor:** DEP-096-04-001 — PKG-096 confirmed as parent in GATE-07 DELIVERABLE_REGISTER and PACKAGE_REGISTER. Single IMPLEMENTS_NODE anchor emitted. Tree integrity: OK.
- **SOW trace anchors:** SOW-0217, SOW-0218, SOW-0219, SOW-0220 — listed explicitly in `_CONTEXT.md` § Covers Scope Items and confirmed in GATE-07 DELIVERABLE_REGISTER row for DEL-096-04. Objective IDs (OBJ-002..OBJ-010) are confirmed in decomposition but not emitted as separate ANCHOR rows because the CONTEXT.md lists them under "Supports Objectives" (not deliverable-level requirement IDs); CONSERVATIVE posture: SOW scope items are the binding trace anchors.
- **DEP-096-04-008 (26020-Package_Requirements.docx):** SatisfactionStatus=PENDING because source is binary and not locally accessible (Guidance CT-05). This is a blocking prerequisite for completeness.
- **DEP-096-04-009 (Final Tank Register):** SatisfactionStatus=PENDING; Procedure and Specification R-13 state fabrication must not be released until final tank register confirmed.
- **DEP-096-04-010 (Final Geotechnical Report):** SatisfactionStatus=PENDING; Procedure states required before foundation load deliverable finalized. Confidence=MEDIUM (prerequisite is for a specific sub-deliverable, not the whole package gate).
- **DEP-096-04-011 (VRU Header Data):** External interface — no target deliverable ID assignable from decomposition (this is an EPC-level data input not assigned to a specific deliverable in the PKG-096 register). TargetType=EXTERNAL.
- **No deprecated/legacy enum values used.** All enums are canonical v3.1 write form.
- **Schema validation:** Passed (see Run History).

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION). No Dependencies.csv produced.
- 2026-05-26 — First extraction run. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition resolved via _REFERENCES.md to GATE-07_Final_Published_2026-05-24. 14 ACTIVE rows produced (5 ANCHOR, 9 EXECUTION). Schema validation: PASSED. No FLOATING_NODE warning. No AMBIGUOUS_ANCHOR warning.
