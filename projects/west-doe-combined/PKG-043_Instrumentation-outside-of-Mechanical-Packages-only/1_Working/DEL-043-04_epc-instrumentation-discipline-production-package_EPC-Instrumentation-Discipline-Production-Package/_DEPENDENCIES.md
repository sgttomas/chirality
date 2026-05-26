# Dependencies: DEL-043-04_epc-instrumentation-discipline-production-package — EPC / Instrumentation Discipline Production Package

**Coordination Mode:** DECLARED
**Dependency tracking mode:** DECLARED + EXTRACTED
**Default maturity threshold:** INITIALIZED
**Register convention:** Prefer `Dependencies.csv` when produced by `TASK + dependency-extract`; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Total rows: 13 | ACTIVE: 13 | RETIRED: 0

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-043-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-043 | PKG-043 — Instrumentation (outside of Mechanical Packages only) | ACTIVE |
| DEP-043-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0044 | SOW-0044 — Carry Instrumentation package | ACTIVE |
| DEP-043-04-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | OBJ-001 | ACTIVE |
| DEP-043-04-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-003 | OBJ-003 | ACTIVE |
| DEP-043-04-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | OBJ-005 | ACTIVE |
| DEP-043-04-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | OBJ-006 | ACTIVE |
| DEP-043-04-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | OBJ-007 | ACTIVE |
| DEP-043-04-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | OBJ-010 | ACTIVE |
| DEP-043-04-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | GATE-07 Final Published PROJECT_DECOMP Snapshot | ACTIVE |
| DEP-043-04-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DELIVERABLE | DEL-043-01_scope-of-work | Scope of Work — DEL-043-01 | ACTIVE |
| DEP-043-04-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DELIVERABLE | DEL-043-02_package-datasheet | Package Datasheet — DEL-043-02 | ACTIVE |
| DEP-043-04-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DELIVERABLE | DEL-043-03_construction-work-package | Construction Work Package — DEL-043-03 | ACTIVE |
| DEP-043-04-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | — | INTERFACE_REGISTER.csv rows IFC-AE83B2D0FC … IFC-35EBF9CD91 | ACTIVE |

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned Datasheet.md, Guidance.md, Procedure.md, Specification.md
- **ANCHOR_DOC (AUTO):** Datasheet.md (contains explicit identification fields with DeliverableID, ParentPackageID, CoversScopeItems, SupportsObjectives)
- **EXECUTION_DOC_ORDER (AUTO):** Procedure.md (explicit prerequisites section), Specification.md (requirements table), Guidance.md (considerations)
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP` (live working surface; GATE-07 snapshot referenced in _REFERENCES.md). Note: `DECOMPOSITION_PATH` brief parameter pointed to a non-existent directory (`GATE-07_Final_Published_2026-05-24` at run root); resolved to live decomposition surface. No GATE-07 snapshot subdirectory found at the provided path — used live decomposition surface for validation.
- **[WARNING] DECOMPOSITION_SNAPSHOT_PATH_NOT_FOUND:** Brief-supplied `DECOMPOSITION_PATH` `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/GATE-07_Final_Published_2026-05-24/` does not exist. Fallback: used live PROJECT_DECOMP surface. Anchor IDs confirmed against DELIVERABLE_REGISTER.csv and PACKAGE_REGISTER.csv — no resolution gap.
- Pass 1 (ANCHOR): 1 parent anchor (IMPLEMENTS_NODE → PKG-043) and 7 trace anchors (SOW-0044 + 6 objectives). Objectives marked ASSUMPTION/MEDIUM confidence per Guidance.md note that the mapping is PACKAGE_HEURISTIC.
- Pass 2 (EXECUTION): 5 execution edges extracted. GATE-07 snapshot access is an explicit stated prerequisite. Three companion deliverables (DEL-043-01, -02, -03) listed under Procedure.md Prerequisites with clear artifact-transfer signal (scope basis, technical handoff basis, workface plan). Interface register rows are an explicit requirement (REQ-043-04-05 in Specification.md). DBM-Deepcut reference not emitted as an EXECUTION row — described as TBD/deferred, no explicit artifact transfer stated yet.
- No downstream dependencies emitted — no evidence of explicit downstream consumers stated in source documents.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 13 |
| RETIRED | 0 |
| **Total** | **13** |

| SatisfactionStatus | Count |
|---|---|
| TBD | 13 |

| DependencyClass | ACTIVE count |
|---|---|
| ANCHOR | 8 |
| EXECUTION | 5 |

Parent anchor (IMPLEMENTS_NODE) count: 1 — OK.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — UPDATE run; STRICTNESS=CONSERVATIVE; CONSUMER_CONTEXT=NONE; SOURCE_DOCS=AUTO. Extracted 13 rows (8 ANCHOR, 5 EXECUTION). Schema validation: VALID. [WARNING] DECOMPOSITION_SNAPSHOT_PATH_NOT_FOUND — brief path did not exist; used live decomposition surface; no resolution gap.
