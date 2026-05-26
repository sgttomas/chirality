# Dependencies: DEL-062-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill; v3.1 schema)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is authoritative; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

22 rows extracted (all ACTIVE). Schema version: v3.1.

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence |
|---|---|---|---|---|---|---|---|---|
| DEP-062-01-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-062 | NGL Loading Pumps Building — PKG-062 (WBS 01) | HIGH |
| DEP-062-01-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0153 | Scope Item SOW-0153 — Vendor/EPC responsibility split | HIGH |
| DEP-062-01-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0154 | Scope Item SOW-0154 — Package function and basic equipment scope | HIGH |
| DEP-062-01-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0155 | Scope Item SOW-0155 — Tagged equipment list and building provision | HIGH |
| DEP-062-01-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0156 | Scope Item SOW-0156 — Performance envelope driver and By-Others exclusions | HIGH |
| DEP-062-01-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | Objective OBJ-001 | MEDIUM |
| DEP-062-01-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-003 | Objective OBJ-003 | MEDIUM |
| DEP-062-01-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Objective OBJ-004 | MEDIUM |
| DEP-062-01-009 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Objective OBJ-005 | MEDIUM |
| DEP-062-01-010 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Objective OBJ-006 | MEDIUM |
| DEP-062-01-011 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | Objective OBJ-007 | MEDIUM |
| DEP-062-01-012 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Objective OBJ-008 | MEDIUM |
| DEP-062-01-013 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Objective OBJ-009 | MEDIUM |
| DEP-062-01-014 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Objective OBJ-010 | MEDIUM |
| DEP-062-01-015 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | SCOPE_LEDGER | SCOPE_LEDGER.csv rows SOW-0153 through SOW-0156 (GATE-07 snapshot) | HIGH |
| DEP-062-01-016 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | DBM-Deepcut-4-25 | 4-25 Deepcut DBM (_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md) | HIGH |
| DEP-062-01-017 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | DELIVERABLE_REGISTER | DELIVERABLE_REGISTER.csv row 420 (GATE-07 snapshot) | HIGH |
| DEP-062-01-018 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-062-02_package-datasheet | Package Datasheet (DEL-062-02) | HIGH |
| DEP-062-01-019 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-062-03_construction-work-package | Construction Work Package (DEL-062-03) | HIGH |
| DEP-062-01-020 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-062-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package (DEL-062-04) | HIGH |
| DEP-062-01-021 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-062-05_vendor-document-turnover-package | Vendor Document Turnover Package (DEL-062-05) | MEDIUM |
| DEP-062-01-022 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-062-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance (DEL-062-06) | MEDIUM |

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 22 |
| RETIRED | 0 |
| **Total** | **22** |

| SatisfactionStatus | Count |
|---|---|
| TBD | 22 |

| DependencyClass | ACTIVE count |
|---|---|
| ANCHOR | 14 |
| EXECUTION | 8 |

## Run Notes

- **Run date:** 2026-05-25
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **Source documents scanned (AUTO):** Datasheet.md, Procedure.md, Specification.md, Guidance.md, _CONTEXT.md
- **ANCHOR_DOC (AUTO):** Datasheet.md (contains "datasheet" in filename — matches ANCHOR_DOC heuristic; also _CONTEXT.md used for identity)
- **EXECUTION_DOC_ORDER (AUTO):** Procedure.md (primary execution signal); Specification.md; Guidance.md
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — verified present; PKG-062 confirmed in PACKAGE_REGISTER.csv; DEL-062-01 confirmed in DELIVERABLE_REGISTER.csv row 420.
- **Parent anchor:** DEP-062-01-001 — `PKG-062` resolved to PACKAGE_REGISTER.csv and confirmed at GATE-07. `TargetType=WBS_NODE` used because PKG-062 is the package/definition node in the decomposition Tree (WBS 01).
- **SOW trace anchors (DEP-062-01-002 through DEP-062-01-005):** FACT — all four SOW IDs appear explicitly in `_CONTEXT.md` Covers Scope Items and are confirmed in SCOPE_LEDGER.csv at GATE-07.
- **Objective trace anchors (DEP-062-01-006 through DEP-062-01-014):** ASSUMPTION — association by PACKAGE_HEURISTIC per `_CONTEXT.md`; Datasheet.md explicitly carries the ASSUMPTION marker. Nine objectives (OBJ-001, OBJ-003..OBJ-010) extracted. Confidence=MEDIUM. Human ruling pending (Conflict Table C-001 in Guidance.md).
- **EXECUTION UPSTREAM rows (DEP-062-01-015 through DEP-062-01-017):** FACT — Procedure.md Prerequisites section explicitly lists SCOPE_LEDGER.csv, 4-25 Deepcut DBM, and DELIVERABLE_REGISTER.csv row 420 as inputs that "must be available before drafting". TargetType=DOCUMENT; TargetDeliverableID left empty per schema rules.
- **EXECUTION DOWNSTREAM rows (DEP-062-01-018 through DEP-062-01-022):** FACT — Guidance.md Purpose section explicitly states "Downstream EPC and Vendor deliverables in PKG-062 (DEL-062-02 through DEL-062-06) consume this SOW as their normative scope reference." All five downstream deliverable IDs confirmed in DELIVERABLE_REGISTER.csv.
- **Note on OBJ-002:** OBJ-002 does not appear in the _CONTEXT.md objective list or PACKAGE_REGISTER.csv for PKG-062. Not extracted (CONSERVATIVE).
- **No _REFERENCES.md document pointers elevated to dependency rows** — _REFERENCES.md lists decomposition and source root pointers only; none are expressed as explicit required inputs beyond what Procedure.md already declares.
- **[WARNING] — Conflict Table C-001 open:** Objective associations are ASSUMPTION only; pending human ruling before upgrading confidence to HIGH.
- **[WARNING] — Conflict Table C-002 open:** `26020-Package_Requirements.docx` package heading 16 not locally extracted; SCOPE_LEDGER fragments are the only accessible portion.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full two-pass extraction (dependency-extract skill); MODE=UPDATE; STRICTNESS=CONSERVATIVE; CONSUMER_CONTEXT=NONE; 22 rows written (14 ANCHOR + 8 EXECUTION), all ACTIVE. Decomposition: GATE-07_Final_Published_2026-05-24 (verified). Warnings: C-001 objective ASSUMPTION open; C-002 source slice deferred.
