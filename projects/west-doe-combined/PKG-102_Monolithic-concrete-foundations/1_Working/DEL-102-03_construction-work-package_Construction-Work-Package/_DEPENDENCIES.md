# Dependencies: DEL-102-03_construction-work-package — Construction Work Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (UPDATE run 2026-05-26)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1 schema, 29 columns). This file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

---

## Extracted Dependency Register

**Total ACTIVE rows:** 11
**Schema version:** v3.1
**Last extraction:** 2026-05-26

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetID / TargetRefID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-102-03-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0258 | Monolithic concrete foundations — PKG-102 scope item | HIGH | ACTIVE |
| DEP-102-03-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | Provide 04-25 Deepcut facility scope for sour gas processing | MEDIUM | ACTIVE |
| DEP-102-03-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Provide civil/structural/site scope for facility installation | MEDIUM | ACTIVE |
| DEP-102-03-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Maintain operability/commissioning/turnover evidence | MEDIUM | ACTIVE |
| DEP-102-03-005 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-102-04_epc-structural-discipline-production-package | EPC / Structural Discipline Production Package | HIGH | ACTIVE |
| DEP-102-03-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-102-01_scope-of-work | Scope of Work | MEDIUM | ACTIVE |
| DEP-102-03-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-102-02_package-datasheet | Package Datasheet | MEDIUM | ACTIVE |
| DEP-102-03-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | EXTERNAL | GEO-TBD | Project Geotechnical Report (bearing capacity / LPILE / dynamic) | HIGH | ACTIVE |
| DEP-102-03-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | IFC-1EDEDC0453 | Grading / Site Drainage / Spill Containment interface counterpart | HIGH | ACTIVE |
| DEP-102-03-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | IFC-8283744B5B | Structural / Foundations / Supports interface counterpart | HIGH | ACTIVE |
| DEP-102-03-011 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | EXTERNAL | COMMISSIONING-TBD | Commissioning — PKG-102 turnover dossier | HIGH | ACTIVE |

### Counts by class

| DependencyClass | ACTIVE |
|---|---|
| ANCHOR | 4 |
| EXECUTION | 7 |
| **Total** | **11** |

---

## Run Notes

**Run date:** 2026-05-26
**Mode:** UPDATE
**Strictness:** CONSERVATIVE
**Consumer context:** NONE

**Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`
- Snapshot exists and was used to validate anchor identifiers (SOW-0258, OBJ-001, OBJ-008, OBJ-010) and deliverable IDs (DEL-102-01, DEL-102-02, DEL-102-04).
- Interface IDs IFC-1EDEDC0453 and IFC-8283744B5B confirmed in INTERFACE_REGISTER.csv.

**Source documents scanned (AUTO):**
- `Procedure.md` — primary execution doc (ANCHOR_DOC for execution signals; contains explicit prerequisites)
- `Guidance.md` — execution/principles doc
- `Specification.md` — requirements doc (also used for anchor signals via R-series requirements)
- `Datasheet.md` — anchor doc (identification, scope items, objectives)
- `_CONTEXT.md` — identity and scope reference
- `_REFERENCES.md` — document pointer resolution

**DOC_ROLE_MAP:** DEFAULT heuristic applied.
- ANCHOR_DOC: `Datasheet.md` (contains identification fields, scope items, objectives)
- EXECUTION_DOC_ORDER: `Procedure.md`, `Guidance.md`, `Specification.md`

**Defaults recorded:**
- MODE: UPDATE — no prior Dependencies.csv existed; fresh creation.
- STRICTNESS: CONSERVATIVE — only emitted rows where identifiers appear explicitly in source text.
- CONSUMER_CONTEXT: NONE — no downstream handoff notes section added.

**Warnings / open items:**
- [WARNING] DEP-102-03-008 geotechnical report TargetRefID is placeholder `GEO-TBD` — actual report ID not in accessible sources.
- [WARNING] DEP-102-03-011 commissioning entity TargetRefID is placeholder `COMMISSIONING-TBD` — commissioning entity ID not in accessible sources.
- OBJ-001/OBJ-008/OBJ-010 objective associations are PACKAGE_HEURISTIC (Conflict C-2 in Guidance.md); marked ASSUMPTION with MEDIUM confidence.
- Source materials `26020-Package_Requirements.docx` and `26020-Packages_Interfaces_4_export.xlsx` not accessed (binary format; not converted). These may contain additional execution dependencies. See Guidance.md Conflict C-3.
- No prior Dependencies.csv existed (first extraction run).

**Tree x DAG integrity:**
- Parent anchor check: 1 IMPLEMENTS_NODE row (DEP-102-03-001). OK — no FLOATING_NODE warning.
- No AMBIGUOUS_ANCHOR — exactly one IMPLEMENTS_NODE row.

---

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 11 |
| RETIRED | 0 |
| **Total** | **11** |

| SatisfactionStatus | Count |
|---|---|
| TBD | 11 |

---

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-26 — UPDATE run; MODE=UPDATE; STRICTNESS=CONSERVATIVE; CONSUMER_CONTEXT=NONE; decomposition=GATE-07_Final_Published_2026-05-24; 11 rows extracted (4 ANCHOR + 7 EXECUTION); 0 RETIRED; schema v3.1 validated VALID; all enums validated.
