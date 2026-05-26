# Dependencies: DEL-023-03_construction-work-package — Construction Work Package

**Coordination Mode:** EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1). This file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Register produced by `TASK + dependency-extract` run on 2026-05-25.

**Total rows:** 24
**ACTIVE:** 24
**RETIRED:** 0

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-023-03-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0024 | Scope decision SOW-0024 — MV VFD 1500HP 4160V VFD | HIGH | ACTIVE |
| DEP-023-03-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | Project Objective OBJ-001 | HIGH | ACTIVE |
| DEP-023-03-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Project Objective OBJ-004 | HIGH | ACTIVE |
| DEP-023-03-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Project Objective OBJ-005 | HIGH | ACTIVE |
| DEP-023-03-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Project Objective OBJ-006 | HIGH | ACTIVE |
| DEP-023-03-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Project Objective OBJ-008 | HIGH | ACTIVE |
| DEP-023-03-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 | HIGH | ACTIVE |
| DEP-023-03-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 | HIGH | ACTIVE |
| DEP-023-03-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | WBS_NODE | DEC-001 | Gate 7 PROJECT_DECOMP accepted snapshot | HIGH | ACTIVE |
| DEP-023-03-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-023-01_scope-of-work | Scope of Work — PKG-023 | MEDIUM | ACTIVE |
| DEP-023-03-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-023-02_package-datasheet | Package Datasheet — PKG-023 | MEDIUM | ACTIVE |
| DEP-023-03-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | IFC-2F6B2D3B80 | Interface IFC-2F6B2D3B80 — Electrical Power | HIGH | ACTIVE |
| DEP-023-03-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | IFC-CEF43B776E | Interface IFC-CEF43B776E — Grounding / Bonding | HIGH | ACTIVE |
| DEP-023-03-014 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | IFC-488756F914 | Interface IFC-488756F914 — I&C / Control Cabling | HIGH | ACTIVE |
| DEP-023-03-015 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | IFC-FF4188D90D | Interface IFC-FF4188D90D — Communications / Network | HIGH | ACTIVE |
| DEP-023-03-016 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | IFC-38BEE3F6CC | Interface IFC-38BEE3F6CC — Maintenance Access | HIGH | ACTIVE |
| DEP-023-03-017 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | IFC-0AED039BBE | Interface IFC-0AED039BBE — Structural / Foundations / Supports | HIGH | ACTIVE |
| DEP-023-03-018 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-023-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package — PKG-023 | HIGH | ACTIVE |
| DEP-023-03-019 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-023-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package — PKG-023 | MEDIUM | ACTIVE |
| DEP-023-03-020 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | DOCUMENT | — | DBM Construction Responsibility section | HIGH | ACTIVE |
| DEP-023-03-021 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | DOCUMENT | — | DBM medium-voltage services table | HIGH | ACTIVE |
| DEP-023-03-022 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | DOCUMENT | — | DBM cable schedule | HIGH | ACTIVE |
| DEP-023-03-023 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | DOCUMENT | — | DBM grounding and bonding paragraphs | HIGH | ACTIVE |
| DEP-023-03-024 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | DOCUMENT | — | DBM motors / area classification paragraph | HIGH | ACTIVE |

## Run Notes

**Run date:** 2026-05-25
**MODE:** UPDATE
**STRICTNESS:** CONSERVATIVE
**CONSUMER_CONTEXT:** NONE
**SOURCE_DOCS:** AUTO — scanned deliverable folder; source documents found: `Datasheet.md`, `Specification.md`, `Procedure.md`, `Guidance.md`
**ANCHOR_DOC:** AUTO — `Datasheet.md` selected (contains `Identification` table with WBS/scope/objective references)
**EXECUTION_DOC_ORDER:** AUTO — `Specification.md` (requirements), `Procedure.md` (procedure steps/prerequisites), `Datasheet.md` (conditions/construction tables)
**DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` (resolved from `_REFERENCES.md`; used for anchor and target ID resolution)

**Anchors resolved:**
- SOW-0024 confirmed in `SCOPE_LEDGER.csv` as parent scope decision node for PKG-023.
- OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010 confirmed in `DELIVERABLE_REGISTER.csv` and `OBJECTIVE_DELIVERABLE_MAP.csv`.

**DOCUMENT targets (IFC-* rows):** Six interface IDs (IFC-2F6B2D3B80, IFC-CEF43B776E, IFC-488756F914, IFC-FF4188D90D, IFC-38BEE3F6CC, IFC-0AED039BBE) are sourced from `INTERFACE_REGISTER.csv`; `TargetType=DOCUMENT` used because the IFC records are register rows, not deliverables. `TargetRefID` carries the stable IFC identifier.

**DBM source-slice rows:** Four CONSTRAINT rows (DEP-023-03-020 through 023) point to named sections of `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`. `TargetType=DOCUMENT`; no `TargetRefID` (no stable section ID exists in the register); raw section name preserved in `TargetName`.

**No warnings.**

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 24 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 24 |

| DependencyClass | ACTIVE count |
|---|---|
| ANCHOR | 8 |
| EXECUTION | 16 |

Parent anchor (IMPLEMENTS_NODE) count: 1 — tree integrity OK.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First extraction run. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition: GATE-07_Final_Published_2026-05-24 (resolved). 24 ACTIVE rows extracted (8 ANCHOR, 16 EXECUTION). No warnings.
