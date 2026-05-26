# Dependencies: DEL-079-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (Dependencies.csv v3.1)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register; this file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Register produced by `TASK + dependency-extract` (UPDATE mode, CONSERVATIVE strictness). Source: two-pass extraction from Datasheet.md, Specification.md, Procedure.md, Guidance.md, and _CONTEXT.md.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetID / TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-079-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-079 — Instrument Air Building | HIGH | ACTIVE |
| DEP-079-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0131 | HIGH | ACTIVE |
| DEP-079-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0132 | HIGH | ACTIVE |
| DEP-079-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0133 | HIGH | ACTIVE |
| DEP-079-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0134 | HIGH | ACTIVE |
| DEP-079-02-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-079-01_scope-of-work | MEDIUM | ACTIVE |
| DEP-079-02-007 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-079-04_vendor-engineered-equipment-package | HIGH | ACTIVE |
| DEP-079-02-008 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-079-05_vendor-document-turnover-package | HIGH | ACTIVE |
| DEP-079-02-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-079-06_epc-vendor-package-review-and-acceptance | HIGH | ACTIVE |
| DEP-079-02-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | 26020-Packages_Interfaces_4_export.xlsx | HIGH | ACTIVE |
| DEP-079-02-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | 26020-Package_Requirements.docx | HIGH | ACTIVE |
| DEP-079-02-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | EXTERNAL | RFQ 26020-01-PT-RFQ-39-001 (not locally accessible) | MEDIUM | ACTIVE |

**Total ACTIVE rows: 12** (5 ANCHOR, 7 EXECUTION)
**RETIRED rows: 0**

## Run Notes

- **Run date:** 2026-05-25
- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **Source documents scanned (AUTO):** Datasheet.md, Specification.md, Procedure.md, Guidance.md, _CONTEXT.md
- **ANCHOR_DOC (AUTO):** Datasheet.md (filename contains `datasheet` — highest-confidence ANCHOR_DOC match)
- **EXECUTION_DOC_ORDER (AUTO):** Procedure.md, Specification.md, Guidance.md (procedure/specification/guidance heuristic order)
- **Decomposition path:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — LOCATED and used for anchor validation. PKG-079 confirmed in PACKAGE_REGISTER.csv. SOW-0131 through SOW-0134 confirmed in SCOPE_LEDGER.csv. All six DEL-079-0x deliverables confirmed in DELIVERABLE_REGISTER.csv.
- **_REFERENCES.md:** Read; no stable local paths to resolve document target locations beyond those already in source docs.
- **Tree x DAG integrity:** 1 IMPLEMENTS_NODE anchor (DEP-079-02-001) — no FLOATING_NODE or AMBIGUOUS_ANCHOR warnings.
- **[NOTE] DEP-079-02-006 (upstream PREREQUISITE to DEL-079-01):** ASSUMPTION label applies — DEL-079-01 and DEL-079-02 share the same PREPARATION source basis and fileset. The dependency reflects the logical peer relationship (scope of work basis informs datasheet), not a hard production gate within the decomposition. Confidence=MEDIUM.
- **[NOTE] DEP-079-02-012 (RFQ constraint):** The RFQ basis document `26020-01-PT-RFQ-39-001_Instr_Air_Bldg_R1.docx` is cited in the source-basis table but is not locally accessible (Guidance CT-04). TargetLocation=`location TBD`. SatisfactionStatus=TBD pending staging in `_Sources`.
- **[NOTE] Interface scope (R7.1):** Ten applicable interface types confirmed (Utility Piping; Drain/Containment; Electrical Power; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports). These are carried as evidence within this deliverable per _CONTEXT.md note; no separate interface deliverables were extracted as execution edges because the interface register (DEP-079-02-010) captures the source constraint.
- **Accepted upstream decomposition snapshot:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`

## Lifecycle Summary

| Metric | Count |
|---|---|
| ACTIVE rows | 12 |
| RETIRED rows | 0 |
| ANCHOR / EXECUTION split | 5 ANCHOR, 7 EXECUTION |
| SatisfactionStatus=TBD | 12 |
| SatisfactionStatus=PENDING | 0 |
| SatisfactionStatus=SATISFIED | 0 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full two-pass extraction run (UPDATE, CONSERVATIVE). 12 rows extracted (5 ANCHOR, 7 EXECUTION). Schema validation: VALID (29 columns, 12 data rows). No warnings. Decomposition confirmed.
