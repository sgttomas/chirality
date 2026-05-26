# Dependencies: DEL-073-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (Dependencies.csv v3.1)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

**Last extraction:** 2026-05-25 | Mode: UPDATE | Strictness: CONSERVATIVE

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-073-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-073 | Amine Treating Unit | HIGH | ACTIVE |
| DEP-073-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0051 | Carry ATU as distinct flat package | HIGH | ACTIVE |
| DEP-073-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0052 | ATU basic scope — MDEA supply | HIGH | ACTIVE |
| DEP-073-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0053 | ATU major included equipment list | HIGH | ACTIVE |
| DEP-073-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0054 | ATU scope notes and open items | HIGH | ACTIVE |
| DEP-073-02-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-073-01_scope-of-work | Scope of Work (PKG-073) | HIGH | ACTIVE |
| DEP-073-02-007 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-073-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package | HIGH | ACTIVE |
| DEP-073-02-008 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-073-03_construction-work-package | Construction Work Package | HIGH | ACTIVE |
| DEP-073-02-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-073-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance | HIGH | ACTIVE |
| DEP-073-02-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | DBM-Deepcut-4-25 | Design Basis Memorandum — Deepcut DBM | HIGH | ACTIVE |
| DEP-073-02-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | PACKAGE | (PKG-046 per source text) | Acid-Gas Compressor | MEDIUM | ACTIVE |

**Counts:** 11 ACTIVE rows — 5 ANCHOR, 6 EXECUTION. 0 RETIRED.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 11 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 11 |

| DependencyClass | Count |
|---|---|
| ANCHOR | 5 |
| EXECUTION | 6 |

## Run Notes

- **Run date:** 2026-05-25
- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
- **Source documents scanned (AUTO):** `Datasheet.md`, `Guidance.md`, `Specification.md` (ANCHOR_DOC: `Datasheet.md`; EXECUTION_DOC_ORDER: `Specification.md`, `Guidance.md`, `Datasheet.md`)
- **`_CONTEXT.md` read:** yes — used for scope item and objective coverage confirmation
- **`_REFERENCES.md` read:** yes — used to resolve decomposition and source document paths

**Anchor validation:** Parent anchor DEP-073-02-001 (IMPLEMENTS_NODE → PKG-073) confirmed in PACKAGE_REGISTER.csv row 49 and DELIVERABLE_REGISTER.csv row DEL-073-02. Four trace anchors (SOW-0051–SOW-0054) confirmed in SCOPE_LEDGER.csv.

**Target resolution notes:**
- DEL-073-01, DEL-073-03, DEL-073-04, DEL-073-06 confirmed in DELIVERABLE_REGISTER.csv under PKG-073.
- DEP-073-02-011: acid-gas compressor referenced as "PKG-046" in `Specification.md` §R-PKG-073-02-010 verification row. `TargetPackageID` left empty; `TargetName` carries the label. ASSUMPTION noted; marked MEDIUM confidence.
- DBM document path resolved via `_REFERENCES.md` shared source root.

**Binary sources not parsed:** `26020-Package_Requirements.docx` heading 27 and `26020-Packages_Interfaces_4_export.xlsx` were referenced in `_REFERENCES.md` but are binary files not locally parsed in this run. Interface schedule values remain `TBD` in the datasheet (C-073-02-02). No additional dependency rows were extracted from these sources.

**Objective associations (OBJ-001 / OBJ-003–OBJ-010):** Observed in `_CONTEXT.md` and `Datasheet.md` Coverage section. Objective-deliverable map (`OBJECTIVE_DELIVERABLE_MAP.csv`) was not opened; association is inherited via PACKAGE_HEURISTIC. Not emitted as TRACES_TO_REQUIREMENT rows under CONSERVATIVE strictness due to ASSUMPTION label in source (see C-073-02-04 in `Guidance.md`).

**No RETIRED rows** — this is the first extraction run; no prior register existed.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First extraction run; UPDATE mode; CONSERVATIVE strictness; decomposition GATE-07 confirmed; 11 ACTIVE rows written (5 ANCHOR, 6 EXECUTION); schema VALID (29 columns, 11 rows).
