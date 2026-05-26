# Dependencies: DEL-090-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED
**Dependency tracking mode:** DECLARED + EXTRACTED
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1 schema). This file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Run completed: 2026-05-26 | MODE: UPDATE | STRICTNESS: CONSERVATIVE | CONSUMER_CONTEXT: NONE

**Counts (ACTIVE):** 12 total — 5 ANCHOR, 7 EXECUTION
**Counts (RETIRED):** 0

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-090-01-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | PACKAGE | PKG-090 | Vapour Recovery Unit 3-25 | HIGH | ACTIVE |
| DEP-090-01-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0249 | SOW-0249 | HIGH | ACTIVE |
| DEP-090-01-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0250 | SOW-0250 | HIGH | ACTIVE |
| DEP-090-01-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0251 | SOW-0251 | HIGH | ACTIVE |
| DEP-090-01-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0252 | SOW-0252 | HIGH | ACTIVE |
| DEP-090-01-006 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-090-02_package-datasheet | Package Datasheet | HIGH | ACTIVE |
| DEP-090-01-007 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-090-03_construction-work-package | Construction Work Package | HIGH | ACTIVE |
| DEP-090-01-008 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-090-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package | HIGH | ACTIVE |
| DEP-090-01-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-090-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance | HIGH | ACTIVE |
| DEP-090-01-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | DBM-SEC-06 | Project DBM SEC-06 Vapour Recovery | HIGH | ACTIVE |
| DEP-090-01-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | DOCUMENT | SCA-002 | SCA-002 Supersession (VRU discharge routing) | HIGH | ACTIVE |
| DEP-090-01-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | VENDOR-RFQ-090 | 26020-03-PT-RFQ-12-001_VRU_1_R0.docx (Vendor RFQ) | MEDIUM | ACTIVE |

## Run Notes

**Run parameters:**
- SCOPE: DEL-090-01
- RUN_ROOT: /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined
- DECOMPOSITION_PATH (resolved): `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — resolved via `_REFERENCES.md` §Authoritative Decomposition Basis. GATE-07_Final_Published_2026-05-24 confirmed present in filesystem. Invoking brief specified `GATE-07_Final_Published_2026-05-24` directory as DECOMPOSITION_PATH; that exact directory does not exist (no trailing file named `PROJECT_DECOMP.md` missing); resolved to the gate snapshot directory which contains `PROJECT_DECOMP.md`. Run Note: brief-supplied DECOMPOSITION_PATH `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/GATE-07_Final_Published_2026-05-24/` did not exist at that exact location; resolved via `_REFERENCES.md` to the canonical location `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`. Non-blocking per skill contract.
- MODE: UPDATE
- STRICTNESS: CONSERVATIVE
- CONSUMER_CONTEXT: NONE
- SOURCE_DOCS: AUTO — scanned Datasheet.md, Specification.md, Procedure.md, Guidance.md
- ANCHOR_DOC: Datasheet.md (highest-confidence match per DEFAULT heuristic — filename contains `datasheet`)
- EXECUTION_DOC_ORDER: Procedure.md, Guidance.md, Specification.md (procedure/guidance first per heuristic; specification carries execution signals)

**Decomposition used:** DELIVERABLE_REGISTER.csv row 564 confirmed DEL-090-01 under PKG-090. PACKAGE_REGISTER.csv row 100 confirmed PKG-090 identity. Anchor targets resolved against decomposition.

**Warnings:**
- No FLOATING_NODE: one IMPLEMENTS_NODE parent anchor present (DEP-090-01-001 → PKG-090).
- No AMBIGUOUS_ANCHOR: exactly one IMPLEMENTS_NODE row.
- Note: IMPLEMENTS_NODE targets `TargetType=PACKAGE` (PKG-090) rather than `WBS_NODE` because the decomposition structure uses package IDs as the parent definition nodes for deliverables; WBS=03 is a grouping attribute not a standalone tree node in the register.

**Open items:**
- DEP-090-01-012: Vendor RFQ `26020-03-PT-RFQ-12-001_VRU_1_R0.docx` is a required input for capacity/sizing (Specification R-090-11) but is NOT located under `_Sources/`. SatisfactionStatus=PENDING. This is a known gap recorded in Guidance §Conflict Table C-090-01 and C-090-02.
- SOW item detailed text (SOW-0249..SOW-0252) not locally accessible — source references preserved; TargetRefID set to SOW identifiers from DELIVERABLE_REGISTER row 564.
- Objective associations (OBJ-002..OBJ-010) are ASSUMPTION/PACKAGE_HEURISTIC per Guidance §Considerations C-090-03; not emitted as dependency rows (these are decomposition tree associations, not information-flow edges — out of scope for this skill).

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-26 — First dependency-extract run. MODE: UPDATE. STRICTNESS: CONSERVATIVE. CONSUMER_CONTEXT: NONE. Decomposition: GATE-07_Final_Published_2026-05-24 (resolved from _REFERENCES.md; brief-supplied path did not exist at exact location). 5 ANCHOR rows, 7 EXECUTION rows. All ACTIVE. Schema validation: PASSED. No FLOATING_NODE. No AMBIGUOUS_ANCHOR. 1 open item: vendor RFQ missing from _Sources/ (DEP-090-01-012, SatisfactionStatus=PENDING).

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 12 |
| RETIRED | 0 |

| SatisfactionStatus | Count (ACTIVE) |
|---|---|
| TBD | 11 |
| PENDING | 1 |
