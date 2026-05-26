# Dependencies: DEL-019-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is canonical; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

### Counts

| Class | Direction | Count |
|---|---|---|
| ANCHOR | UPSTREAM | 8 |
| EXECUTION | UPSTREAM | 8 |
| EXECUTION | DOWNSTREAM | 2 |
| **Total ACTIVE** | | **18** |

### Compact Table

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence |
|---|---|---|---|---|---|---|---|---|
| DEP-019-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0020 | Scope decision SOW-0020 — MV VFD package | HIGH |
| DEP-019-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-002 | Project Objective OBJ-002 | HIGH |
| DEP-019-04-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Project Objective OBJ-004 | HIGH |
| DEP-019-04-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Project Objective OBJ-005 | HIGH |
| DEP-019-04-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Project Objective OBJ-006 | HIGH |
| DEP-019-04-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Project Objective OBJ-008 | HIGH |
| DEP-019-04-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 | HIGH |
| DEP-019-04-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 | HIGH |
| DEP-019-04-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-019-01_scope-of-work | EPC Scope of Work — PKG-019 | HIGH |
| DEP-019-04-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-019-02_package-datasheet | EPC Package Datasheet — PKG-019 | HIGH |
| DEP-019-04-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | DOCUMENT | SCA-001-VE-34 | SCA-001 VE #34 — Starting VFDs required | HIGH |
| DEP-019-04-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EQUIPMENT | KM-2150 | Inlet Compressor Motor KM-2150 | HIGH |
| DEP-019-04-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EQUIPMENT | KM-2250 | Inlet Compressor Motor KM-2250 | HIGH |
| DEP-019-04-014 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EQUIPMENT | MCC-8200 | 4160V MCC (MCC-8200) line-side interface | HIGH |
| DEP-019-04-015 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | DOCUMENT | SCA-001-VE-37 | SCA-001 VE #37 — Capacitor bank removal | HIGH |
| DEP-019-04-016 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | UNKNOWN | HRR-019-04-001 | Human Ruling HRR-019-04-001 (motor basis resolution) | HIGH |
| DEP-019-04-017 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-019-05_vendor-document-turnover-package | Vendor Document Turnover Package | HIGH |
| DEP-019-04-018 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-019-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance | HIGH |

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 18 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 16 |
| PENDING | 1 (DEP-019-04-016 — HRR-019-04-001 awaiting human ruling) |

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; candidate documents found: `Datasheet.md`, `Specification.md`, `Procedure.md`, `Guidance.md`
- **ANCHOR_DOC:** `Datasheet.md` (selected as highest-confidence anchor doc: contains explicit DeliverableID, ParentPackageID, Covers Scope Items, Supports Objectives fields)
- **EXECUTION_DOC_ORDER:** `Procedure.md` (primary execution signals — prerequisites, steps, handoffs), `Specification.md` (requirements and standards constraints), `Guidance.md` (conflict table and authority chain)
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — used successfully; anchor identifiers validated against SCOPE_LEDGER.csv, DELIVERABLE_REGISTER.csv, and OBJECTIVE_REGISTER.csv
- **Pass 1 (ANCHOR):** One IMPLEMENTS_NODE anchor to SOW-0020 (confirmed in SCOPE_LEDGER.csv). Seven TRACES_TO_REQUIREMENT anchors to OBJ-002 through OBJ-010 (all confirmed in OBJECTIVE_REGISTER.csv and DELIVERABLE_REGISTER.csv).
- **Pass 2 (EXECUTION):** Eight upstream edges extracted (two prerequisite deliverables DEL-019-01 and DEL-019-02; two regulatory constraint documents SCA-001 VE #34 and VE #37; two equipment interface targets KM-2150 and KM-2250; one equipment interface MCC-8200; one prerequisite human ruling HRR-019-04-001). Two downstream handover edges to DEL-019-05 and DEL-019-06.
- **HRR-019-04-001 note:** Motor basis vs. workbook title conflict is unresolved (TBD human ruling); SatisfactionStatus set to PENDING for this dependency row. This is a design-freeze gate per Specification.md REQ-019-04-11 and Procedure.md Prerequisites.
- **Detailed electrical studies dependency:** DBM §756 defers harmonic/reactive-power mitigation to detailed electrical studies; vendor design must accept study outputs as design inputs (REQ-019-04-10). No specific deliverable ID is available for the electrical study output in accessible sources; not extracted as a dependency row (TargetType would be UNKNOWN with no stable ID). Recorded here as a known open dependency — recommend declaring once the study deliverable is identified.
- **SCA-001 VE #34 and VE #37:** Classified as DOCUMENT TargetType; no stable document path available in accessible source slices; TargetLocation left blank.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full extraction run; MODE=UPDATE; STRICTNESS=CONSERVATIVE; CONSUMER_CONTEXT=NONE; decomposition path confirmed; 18 ACTIVE rows written to Dependencies.csv (1 IMPLEMENTS_NODE anchor, 7 TRACES_TO_REQUIREMENT anchors, 10 EXECUTION rows). Schema validation: VALID.
