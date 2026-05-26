# Dependencies: DEL-054-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** DECLARED + EXTRACTED
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Total rows: 20 | ACTIVE: 20 | RETIRED: 0

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName (short) | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-054-01-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | — | PKG-054 | HIGH | ACTIVE |
| DEP-054-01-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | OBJ-001 | HIGH | ACTIVE |
| DEP-054-01-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | OBJ-004 | HIGH | ACTIVE |
| DEP-054-01-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | OBJ-005 | HIGH | ACTIVE |
| DEP-054-01-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | OBJ-006 | HIGH | ACTIVE |
| DEP-054-01-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | OBJ-007 | HIGH | ACTIVE |
| DEP-054-01-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | OBJ-008 | HIGH | ACTIVE |
| DEP-054-01-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | OBJ-009 | HIGH | ACTIVE |
| DEP-054-01-009 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | OBJ-010 | HIGH | ACTIVE |
| DEP-054-01-010 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0075 | SOW-0075 | HIGH | ACTIVE |
| DEP-054-01-011 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0076 | SOW-0076 | HIGH | ACTIVE |
| DEP-054-01-012 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0077 | SOW-0077 | HIGH | ACTIVE |
| DEP-054-01-013 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0078 | SOW-0078 | HIGH | ACTIVE |
| DEP-054-01-014 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-054-02_package-datasheet | DEL-054-02 Package Datasheet | HIGH | ACTIVE |
| DEP-054-01-015 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-054-03_construction-work-package | DEL-054-03 Construction Work Package | HIGH | ACTIVE |
| DEP-054-01-016 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-054-04_vendor-engineered-equipment-package | DEL-054-04 Vendor Engineered Equipment Package | HIGH | ACTIVE |
| DEP-054-01-017 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-054-05_vendor-document-turnover-package | DEL-054-05 Vendor Document Turnover Package | HIGH | ACTIVE |
| DEP-054-01-018 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-054-06_epc-vendor-package-review-and-acceptance | DEL-054-06 EPC Vendor Package Review and Acceptance | HIGH | ACTIVE |
| DEP-054-01-019 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | GATE-07 PROJECT_DECOMP snapshot | HIGH | ACTIVE |
| DEP-054-01-020 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | DOCUMENT | — | 26020-Package_Requirements.docx heading 9 | MEDIUM | ACTIVE |

## Run Notes

- **Run date:** 2026-05-25
- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **Source docs:** AUTO — scanned deliverable folder; docs found: Datasheet.md (ANCHOR_DOC by heuristic match on "datasheet"), Specification.md, Guidance.md, Procedure.md (EXECUTION_DOC candidates).
- **Anchor doc used:** Datasheet.md (highest-confidence anchor match).
- **Execution doc order:** Procedure.md, Guidance.md, Specification.md.
- **Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` (resolved from `_REFERENCES.md`; GATE-07 snapshot confirmed present).
- **_REFERENCES.md used:** Yes — resolved decomposition path and confirmed no deliverable-specific source slices were copied.
- **Pass 1 (ANCHOR):** 1 IMPLEMENTS_NODE anchor to PKG-054 (WBS_NODE); 8 TRACES_TO_REQUIREMENT anchors to objectives OBJ-001/004/005/006/007/008/009/010; 4 TRACES_TO_REQUIREMENT anchors to scope items SOW-0075/0076/0077/0078. All IDs validated against GATE-07 OBJECTIVE_DELIVERABLE_MAP.csv, SCOPE_LEDGER.csv, PACKAGE_REGISTER.csv. Parent anchor count = 1 (no FLOATING_NODE or AMBIGUOUS_ANCHOR warning).
- **Pass 2 (EXECUTION):** 5 DOWNSTREAM HANDOVER edges to sibling deliverables DEL-054-02 through DEL-054-06 (explicit in Guidance.md Purpose statement and Specification exclusions); 1 UPSTREAM PREREQUISITE to GATE-07 PROJECT_DECOMP snapshot document (explicit in Procedure.md Prerequisites); 1 UPSTREAM CONSTRAINT to 26020-Package_Requirements.docx (explicit in Guidance Conflict Table CONF-054-01-02 — design conditions not locally extracted; location TBD).
- **Excluded from EXECUTION pass:** The interface register rows (Process Piping; Relief / Flare / Vent; etc.) represent scope content to be stated in the SOW artifact, not information-flow edges; not emitted as dependency rows. EHT ownership conflict (CONF-054-01-01) is a human-ruling item, not an explicit artifact dependency.

## Lifecycle Summary

| Dimension | Count |
|---|---|
| ACTIVE rows | 20 |
| RETIRED rows | 0 |
| ANCHOR / IMPLEMENTS_NODE | 1 |
| ANCHOR / TRACES_TO_REQUIREMENT | 12 |
| EXECUTION / UPSTREAM | 2 |
| EXECUTION / DOWNSTREAM | 5 |
| SatisfactionStatus = TBD | 20 |
| SatisfactionStatus = SATISFIED | 0 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION). No Dependencies.csv generated.
- 2026-05-25 — UPDATE run; CONSERVATIVE; CONSUMER_CONTEXT=NONE; decomposition GATE-07 snapshot used; 20 ACTIVE rows extracted (13 ANCHOR + 7 EXECUTION); Dependencies.csv created; schema VALID; no FLOATING_NODE or AMBIGUOUS_ANCHOR warnings.
