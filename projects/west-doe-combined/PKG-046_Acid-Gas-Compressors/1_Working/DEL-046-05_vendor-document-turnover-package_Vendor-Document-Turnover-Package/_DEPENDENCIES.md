# Dependencies: DEL-046-05_vendor-document-turnover-package — Vendor Document Turnover Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is canonical; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Extracted from source documents on 2026-05-25. All rows ACTIVE.

**Total ACTIVE rows: 10** (5 ANCHOR + 5 EXECUTION)

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence |
|---|---|---|---|---|---|---|---|---|
| DEP-046-05-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-046 | PKG-046 — Acid Gas Compressors | HIGH |
| DEP-046-05-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0047 | SOW-0047 — Acid Gas Compressors scope basis | HIGH |
| DEP-046-05-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0048 | SOW-0048 — Acid Gas Compressors scope basis | HIGH |
| DEP-046-05-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0049 | SOW-0049 — Acid Gas Compressors scope basis | HIGH |
| DEP-046-05-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0050 | SOW-0050 — Acid Gas Compressors scope basis | HIGH |
| DEP-046-05-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-046-01_scope-of-work | Scope of Work (DEL-046-01) | HIGH |
| DEP-046-05-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-046-02_package-datasheet | Package Datasheet (DEL-046-02) | HIGH |
| DEP-046-05-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DELIVERABLE | DEL-046-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package (DEL-046-04) | HIGH |
| DEP-046-05-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | DOCUMENT | REQ-046-05-R-01 | 26020-Package_Requirements.docx package heading 1 | MEDIUM |
| DEP-046-05-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-046-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance (DEL-046-06) | HIGH |

## Run Notes

- **Run date:** 2026-05-25
- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **Source docs (AUTO):** Datasheet.md, Guidance.md, Procedure.md, Specification.md
- **ANCHOR_DOC (AUTO):** Datasheet.md (contains Identification table with WBS/package/SOW references)
- **EXECUTION_DOC_ORDER (AUTO):** Procedure.md (workflow signals), Specification.md (requirement/interface signals), Guidance.md (consideration signals), Datasheet.md (identification/conditions)
- **Decomposition path:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` (resolved from `_REFERENCES.md`; the DECOMPOSITION_PATH param `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/GATE-07_Final_Published_2026-05-24/` did not exist at run time)
- **Decomposition validation:** Used `DELIVERABLE_REGISTER.csv` to confirm DEL-046-05 exists in PKG-046; confirmed SOW refs SOW-0047 through SOW-0050 and objective refs OBJ-001 through OBJ-010.
- **[WARNING] NOTE — Objectives not individually traced:** DELIVERABLE_REGISTER.csv lists OBJ-001; OBJ-003; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010. Under CONSERVATIVE strictness these are not emitted as individual TRACES_TO_REQUIREMENT rows because the source documents do not individually call them out by ID; they appear only in the decomposition register. They are noted here for human review.
- **[WARNING] TBD_SOURCE:** `26020-Package_Requirements.docx` and `26020-Packages_Interfaces_4_export.xlsx` are not locally text-accessible. VDR composition, revision lexicon, milestone schedule, and standards clause references remain TBD. DEP-046-05-009 captures this constraint at MEDIUM confidence with TargetLocation TBD.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 10 |
| RETIRED | 0 |
| **Total** | **10** |

| Class | ACTIVE |
|---|---|
| ANCHOR | 5 |
| EXECUTION | 5 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 10 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First extraction run; dependency-extract skill; MODE=UPDATE; STRICTNESS=CONSERVATIVE; CONSUMER_CONTEXT=NONE; decomposition GATE-07 snapshot located under `_Decomposition/PROJECT_DECOMP/_GateSnapshots/`; 10 rows extracted (5 ANCHOR, 5 EXECUTION); schema VALID.
