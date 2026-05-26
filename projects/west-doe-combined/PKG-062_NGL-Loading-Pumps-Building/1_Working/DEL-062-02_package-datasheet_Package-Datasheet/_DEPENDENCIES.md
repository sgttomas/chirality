# Dependencies: DEL-062-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** ACCEPTED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1 schema); this file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Total rows: 14 | ACTIVE: 14 | RETIRED: 0

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-062-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-062 | NGL Loading Pumps Building | HIGH | ACTIVE |
| DEP-062-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0153 | Scope Item SOW-0153 | HIGH | ACTIVE |
| DEP-062-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0154 | Scope Item SOW-0154 | HIGH | ACTIVE |
| DEP-062-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0155 | Scope Item SOW-0155 | HIGH | ACTIVE |
| DEP-062-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0156 | Scope Item SOW-0156 | HIGH | ACTIVE |
| DEP-062-02-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-062-01_scope-of-work | Scope of Work (DEL-062-01) | HIGH | ACTIVE |
| DEP-062-02-007 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-062-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package | HIGH | ACTIVE |
| DEP-062-02-008 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-062-05_vendor-document-turnover-package | Vendor Document Turnover Package | MEDIUM | ACTIVE |
| DEP-062-02-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-062-03_construction-work-package | Construction Work Package | MEDIUM | ACTIVE |
| DEP-062-02-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-062-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance | MEDIUM | ACTIVE |
| DEP-062-02-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | — | EPC Integrator — DCS integration scope | HIGH | ACTIVE |
| DEP-062-02-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | — | EPC Integrator — Foundations scope | HIGH | ACTIVE |
| DEP-062-02-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | — | EPC Integrator — Electrical supply to MCC scope | HIGH | ACTIVE |
| DEP-062-02-014 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | 26020-Package_Requirements.docx (section 26020-01-PT-18-003) | HIGH | ACTIVE |

### Anchor summary

- ACTIVE IMPLEMENTS_NODE rows: 1 (DEP-062-02-001 — PKG-062) — parent anchor present, no FLOATING_NODE warning.
- ACTIVE TRACES_TO_REQUIREMENT rows: 4 (SOW-0153, SOW-0154, SOW-0155, SOW-0156).

### Execution edge summary

- UPSTREAM PREREQUISITE: 2 (DEL-062-01 SOW; 26020-Package_Requirements.docx)
- UPSTREAM INTERFACE: 3 (DCS integration by others; foundations by others; electrical supply to MCC by others)
- DOWNSTREAM HANDOVER: 4 (DEL-062-04 vendor package; DEL-062-05 vendor document turnover; DEL-062-03 construction work package; DEL-062-06 review and acceptance)

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 14 |
| RETIRED | 0 |
| **Total** | **14** |

| SatisfactionStatus | Count |
|---|---|
| TBD | 14 |

## Run Notes

- **Run date:** 2026-05-25
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **Source docs scanned (AUTO):** `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, `_CONTEXT.md`
- **ANCHOR_DOC (AUTO selection):** `Datasheet.md` (filename contains "datasheet" — highest-confidence ANCHOR_DOC match per DEFAULT heuristic)
- **EXECUTION_DOC_ORDER (AUTO):** `Procedure.md`, `Specification.md`, `Guidance.md`, `Datasheet.md`
- **DECOMPOSITION_PATH used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — anchor identifiers validated against `PACKAGE_REGISTER.csv` and `DELIVERABLE_REGISTER.csv`. Labels resolved.
- **_REFERENCES.md used:** Yes — confirmed 26020-Package_Requirements.docx local path; used to populate TargetLocation for DOCUMENT row.
- **Existing Dependencies.csv:** Not present — created new file.
- **Pass 1 (ANCHOR):** Parent anchor resolved to PKG-062 (WBS_NODE) from Datasheet.md Identification table and PACKAGE_REGISTER.csv. Four requirement trace anchors emitted for SOW-0153..SOW-0156 per Datasheet.md Scope Items Covered and _CONTEXT.md.
- **Pass 2 (EXECUTION):** Six sibling-deliverable edges extracted (DEL-062-01 upstream prerequisite; DEL-062-03, -04, -05, -06 downstream handovers). Three EPC by-others boundary interfaces extracted from Datasheet.md Construction / Exclusions (DCS integration, foundations, electrical supply to MCC). One source document prerequisite row (26020-Package_Requirements.docx).
- **CONSERVATIVE posture applied:** No edges extracted from "coordination only" or structural adjacency signals. Co-package siblings included only where explicit information transfer is stated (scope boundary, handoff, interface matrix, vendor deliverables list).
- **No TBD/UNKNOWN target IDs:** All deliverable targets resolved by name against DELIVERABLE_REGISTER.csv. External targets recorded as TargetType=EXTERNAL with TargetName.
- **[INFO]** DEL-062-06 target path assumed conventional folder pattern — confirm path if sibling folder name differs.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First extracted run. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition: GATE-07_Final_Published_2026-05-24. Created Dependencies.csv (v3.1). 14 rows ACTIVE (5 ANCHOR, 9 EXECUTION). No RETIRED rows. Schema validated VALID.
