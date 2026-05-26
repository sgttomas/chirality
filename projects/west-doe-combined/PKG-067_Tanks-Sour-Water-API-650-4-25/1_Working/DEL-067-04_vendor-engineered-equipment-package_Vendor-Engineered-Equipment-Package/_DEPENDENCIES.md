# Dependencies: DEL-067-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** DECLARED + EXTRACTED
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1); this file is the human-readable view and declared-list surface.

---

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

---

## Extracted Dependency Register

**Generated:** 2026-05-25 | **Mode:** UPDATE | **Strictness:** CONSERVATIVE

### Summary

| DependencyClass | AnchorType / DependencyType | Direction | Count |
|---|---|---|---|
| ANCHOR | IMPLEMENTS_NODE | UPSTREAM | 1 |
| ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | 4 |
| EXECUTION | PREREQUISITE | UPSTREAM | 2 |
| EXECUTION | HANDOVER | DOWNSTREAM | 2 |
| **TOTAL ACTIVE** | | | **9** |

### Compact Table

| DependencyID | Class | Type | Direction | TargetType | TargetName / TargetID | Confidence | Status |
|---|---|---|---|---|---|---|---|
| DEP-067-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | WBS_NODE | PKG-067 — Tanks, Sour Water (API 650) 4-25 | HIGH | ACTIVE |
| DEP-067-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | SOW-0225 | HIGH | ACTIVE |
| DEP-067-04-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | SOW-0226 | HIGH | ACTIVE |
| DEP-067-04-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | SOW-0227 | HIGH | ACTIVE |
| DEP-067-04-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | SOW-0228 | HIGH | ACTIVE |
| DEP-067-04-006 | EXECUTION | PREREQUISITE | UPSTREAM | DELIVERABLE | DEL-067-01_scope-of-work | HIGH | ACTIVE |
| DEP-067-04-007 | EXECUTION | PREREQUISITE | UPSTREAM | DELIVERABLE | DEL-067-02_package-datasheet | HIGH | ACTIVE |
| DEP-067-04-008 | EXECUTION | HANDOVER | DOWNSTREAM | DELIVERABLE | DEL-067-05_vendor-document-turnover-package | HIGH | ACTIVE |
| DEP-067-04-009 | EXECUTION | HANDOVER | DOWNSTREAM | DELIVERABLE | DEL-067-06_epc-vendor-package-review-and-acceptance | HIGH | ACTIVE |

---

## Run Notes

**Run date:** 2026-05-25
**MODE:** UPDATE
**STRICTNESS:** CONSERVATIVE
**CONSUMER_CONTEXT:** NONE
**SOURCE_DOCS:** AUTO (scanned: Datasheet.md, Specification.md, Procedure.md, Guidance.md, _CONTEXT.md)
**ANCHOR_DOC:** Datasheet.md (primary anchor signal; contains DeliverableID, ParentPackageID, Covers Scope Items)
**EXECUTION_DOC_ORDER:** Procedure.md (primary execution signal), Specification.md, Guidance.md
**DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`
  - Note: The `DECOMPOSITION_PATH` provided in the task invocation (`GATE-07_Final_Published_2026-05-24/`) did not resolve as a direct filesystem path. The actual path was located via `_CONTEXT.md` and `_REFERENCES.md` and confirmed in the `_GateSnapshots` directory. Actual path used is as above.
  - Anchor identifiers (PKG-067, SOW-0225–SOW-0228) validated against PACKAGE_REGISTER.csv and DELIVERABLE_REGISTER.csv in the Gate 7 snapshot.

**Defaults applied:**
- DOC_ROLE_MAP: DEFAULT (Datasheet.md matched ANCHOR_DOC heuristic; Procedure.md matched EXECUTION_DOC heuristic)
- No existing `Dependencies.csv` present; created fresh.

**Assumptions and warnings:**
- ASSUMPTION: Objective associations (OBJ-001, OBJ-003–OBJ-010) were noted in _CONTEXT.md as inherited via PACKAGE_HEURISTIC. Not emitted as ANCHOR rows because individual deliverable-to-objective mapping was not confirmed at deliverable-ID granularity in the decomposition snapshot (no OBJECTIVE_DELIVERABLE_MAP lookup performed). Guidance CT-05 documents this as an open TBD.
- Source `26020-Package_Requirements.docx` is referenced as an authority by `_CONTEXT.md` but is a binary DOCX not readable as text. Not scanned; no dependency rows sourced from it. Guidance CT-04 documents this as an open TBD.
- No DEL-067-03 (Construction Work Package) dependency row emitted: Guidance §Considerations references CWP as a "wrapper" that "governs construction" but states it as structural context, not an explicit prerequisite information transfer to this deliverable. CONSERVATIVE posture — not emitted.
- [WARNING] No `_REFERENCES.md` document pointers resolved to `TargetLocation` for EXECUTION rows. Target deliverable IDs resolved via DELIVERABLE_REGISTER.csv.

---

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 9 |
| RETIRED | 0 |
| **TOTAL** | **9** |

| SatisfactionStatus | Count |
|---|---|
| TBD | 9 |

---

## Run History

| Date | Mode | Strictness | Decomposition | Warnings | ACTIVE rows |
|---|---|---|---|---|---|
| 2026-05-24 | DECLARED init | — | accepted snapshot noted | none | 0 (declared only) |
| 2026-05-25 | UPDATE | CONSERVATIVE | GATE-07_Final_Published_2026-05-24 (resolved via _CONTEXT.md) | DECOMPOSITION_PATH arg did not resolve directly; actual path found via context files | 9 |
