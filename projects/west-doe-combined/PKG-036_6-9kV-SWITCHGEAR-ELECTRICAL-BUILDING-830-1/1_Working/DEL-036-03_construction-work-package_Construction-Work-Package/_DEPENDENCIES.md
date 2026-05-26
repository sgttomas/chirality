# Dependencies: DEL-036-03_construction-work-package — Construction Work Package

**Coordination Mode:** DECLARED
**Dependency tracking mode:** DECLARED + EXTRACTED
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1 schema); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

---

## Extracted Dependency Register

Extracted by `dependency-extract` skill run 2026-05-25. Source documents scanned: `Procedure.md`, `Guidance.md`, `Specification.md`, `Datasheet.md`.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetID / TargetRefID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-036-03-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0037 | Scope Item SOW-0037 — 6.9kV SWITCHGEAR ELECTRICAL BUILDING (830-1) CWP | HIGH | ACTIVE |
| DEP-036-03-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Objective OBJ-005 — Electrical infrastructure and vendor-load integration | MEDIUM | ACTIVE |
| DEP-036-03-003 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-036-01_scope-of-work | Scope of Work | HIGH | ACTIVE |
| DEP-036-03-004 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-036-02_package-datasheet | Package Datasheet | HIGH | ACTIVE |
| DEP-036-03-005 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-036-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package | MEDIUM | ACTIVE |
| DEP-036-03-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | IFC-3B6012818E | Electrical Power — 13.8 kV feed to 6.9 kV distribution | HIGH | ACTIVE |
| DEP-036-03-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | IFC-B6F77BBE8A | Grounding / Bonding — facility ground grid | HIGH | ACTIVE |
| DEP-036-03-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | IFC-BDE626F7DD | Structural / Foundations — piled foundation | HIGH | ACTIVE |
| DEP-036-03-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | IFC-972B08F285 | I&C / Control Cabling — adjacent skids and PLC racks | MEDIUM | ACTIVE |
| DEP-036-03-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | IFC-2C313DA749 | Fire & Gas / Safety Systems tie-in | MEDIUM | ACTIVE |
| DEP-036-03-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | SOW-0037 | Gate 7 Decomposition Snapshot (DELIVERABLE / ARTIFACT / INTERFACE registers) | HIGH | ACTIVE |

**Row counts:** 11 total — 2 ANCHOR, 9 EXECUTION. All ACTIVE.

---

## Run Notes

- **Run date:** 2026-05-25
- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — confirmed available and used for anchor validation and target label resolution.
- **SOURCE_DOCS (AUTO):** `Procedure.md` (EXECUTION_DOC), `Guidance.md` (EXECUTION_DOC), `Specification.md` (ANCHOR_DOC heuristic — contains scope/requirements), `Datasheet.md` (ANCHOR_DOC heuristic — contains identification/interface table).
- **ANCHOR_DOC selected:** `Datasheet.md` (identification table is the primary anchor signal; `Specification.md` provides requirement trace support).
- **EXECUTION_DOC_ORDER:** `Procedure.md`, `Guidance.md`, `Specification.md`, `Datasheet.md`.
- **Parent anchor (IMPLEMENTS_NODE):** Anchored to SOW-0037 (scope item node) confirmed in `DELIVERABLE_REGISTER.csv`. PKG-036 WBS=01 confirmed in `PACKAGE_REGISTER.csv`. One parent anchor emitted.
- **Objective trace:** OBJ-005 selected as the primary trace anchor from the PACKAGE_HEURISTIC mapping (eight objectives mapped); carried as ASSUMPTION per HRR-036-03-003 in Guidance.md.
- **Sibling deliverable prerequisites:** DEL-036-01 and DEL-036-02 are explicitly named in Procedure.md Prerequisites as upstream context providers; recorded as UPSTREAM PREREQUISITE edges.
- **Interface edges:** 5 of 12 declared interface types extracted as explicit EXECUTION rows where the source documents state construction tie-in requirements. The remaining 7 interface types (Utility Piping, Drain/Containment, Area/Exterior Lighting, Communications/Network, Building HVAC/Services, Maintenance Access, Grading/Site Drainage/Spill Containment) are declared in `INTERFACE_REGISTER.csv` and mentioned in REQ-036-03-008 but do not carry distinct information-flow statements beyond "to be planned in workface plan." Under CONSERVATIVE strictness these are not promoted to separate EXECUTION rows; they are represented by the Gate 7 snapshot prerequisite (DEP-036-03-011) which gates the workface planning step.
- **No DEL-036-04 loop concern:** The DOWNSTREAM HANDOVER to DEL-036-04 captures the explicit scope boundary statement (Specification.md Scope) and the turnover-checklist handoff. It does not create a circular dependency — DEL-036-03 is the EPC integration layer; DEL-036-04 is the vendor engineering layer.
- **[WARNING] MISSING_DECOMPOSITION PATH:** The brief specified `DECOMPOSITION_PATH: /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/GATE-07_Final_Published_2026-05-24/` which does not exist as a direct path. Resolved to the actual location under `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`. Used resolved path; no anchor validation skipped.

---

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First dependency-extract run. Mode=UPDATE, Strictness=CONSERVATIVE. Decomposition path resolved to `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`. Source docs: Procedure.md, Guidance.md, Specification.md, Datasheet.md. Emitted 11 rows (2 ANCHOR, 9 EXECUTION). All ACTIVE. Schema validated VALID.

---

## Lifecycle Summary

| Metric | Value |
|---|---|
| Total rows | 11 |
| ACTIVE | 11 |
| RETIRED | 0 |
| ANCHOR rows (ACTIVE) | 2 |
| EXECUTION rows (ACTIVE) | 9 |
| IMPLEMENTS_NODE anchors | 1 |
| TRACES_TO_REQUIREMENT anchors | 1 |
| SatisfactionStatus=TBD | 11 |
