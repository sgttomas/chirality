# Dependencies: DEL-027-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** ACCEPTED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1 schema). This file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` contains 12 ACTIVE rows (8 ANCHOR + 4 EXECUTION).

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-027-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0028 | SOW-0028 — PKG-027 scope item | ACTIVE |
| DEP-027-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | OBJ-001 | ACTIVE |
| DEP-027-04-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | OBJ-004 | ACTIVE |
| DEP-027-04-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | OBJ-005 | ACTIVE |
| DEP-027-04-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | OBJ-006 | ACTIVE |
| DEP-027-04-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | OBJ-008 | ACTIVE |
| DEP-027-04-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | OBJ-009 | ACTIVE |
| DEP-027-04-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | OBJ-010 | ACTIVE |
| DEP-027-04-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-027-01_scope-of-work | Scope of Work | ACTIVE |
| DEP-027-04-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-027-02_package-datasheet | Package Datasheet | ACTIVE |
| DEP-027-04-011 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-027-05_vendor-document-turnover-package | Vendor Document Turnover Package | ACTIVE |
| DEP-027-04-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-027-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance | ACTIVE |

## Lifecycle Summary

| Dimension | Count |
|---|---|
| ACTIVE rows | 12 |
| RETIRED rows | 0 |
| ANCHOR / IMPLEMENTS_NODE | 1 |
| ANCHOR / TRACES_TO_REQUIREMENT | 7 |
| EXECUTION / UPSTREAM (PREREQUISITE) | 2 |
| EXECUTION / DOWNSTREAM (HANDOVER) | 2 |
| SatisfactionStatus = TBD | 12 |

## Run Notes

- **Run date:** 2026-05-25
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned: `_CONTEXT.md`, `Datasheet.md`, `Specification.md`, `Procedure.md`, `Guidance.md`
- **ANCHOR_DOC:** `Datasheet.md` (contains datasheet / identification signals; also `_CONTEXT.md` used for scope/objective anchors)
- **EXECUTION_DOC_ORDER:** `Procedure.md` (primary; explicit prerequisites and step outputs), `Specification.md` (requirements cross-check), `Guidance.md` (supplemental context)
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — used for anchor label resolution and sibling deliverable ID confirmation. Note: the BRIEF specified a GATE-07 path under a `projects/west-doe-combined/GATE-07_Final_Published_2026-05-24/` folder that does not exist; the canonical snapshot was located at the above path and used instead.
- **Parent anchor:** DEP-027-04-001 — SOW-0028 identified in `_CONTEXT.md § Covers Scope Items` and confirmed in SCOPE_LEDGER.csv GATE-07 snapshot. Single IMPLEMENTS_NODE row; no FLOATING_NODE or AMBIGUOUS_ANCHOR warning.
- **Objective traces:** 7 rows (OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010) — all confirmed in GATE-07 DELIVERABLE_REGISTER.csv.
- **Execution prerequisites:** `Procedure.md § Prerequisites` explicitly states DEL-027-01 and DEL-027-02 as required inputs before vendor engineering begins. Emitted as UPSTREAM PREREQUISITE rows.
- **Execution handovers:** `Procedure.md § Steps Step 7` explicitly names DEL-027-05 and DEL-027-06 as downstream consumers of vendor outputs (ART-6FA1DBA3D1 and ART-0723EEECE8). Emitted as DOWNSTREAM HANDOVER rows.
- **Not extracted (low signal):** Interface IDs from `INTERFACE_REGISTER.csv` (IFC-*) were noted in source documents but represent EPC-defined interface definitions that this deliverable must comply with rather than information-flow dependencies to specific deliverables; no explicit artifact-transfer statement was found linking this deliverable to a separate interface-definition deliverable.
- **Gate 7 decomp snapshot note:** The BRIEF referenced `GATE-07_Final_Published_2026-05-24` at a path (`projects/west-doe-combined/GATE-07_Final_Published_2026-05-24/`) that does not exist. The decomposition snapshot was successfully located at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`. Anchor and sibling ID resolution proceeded normally.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract skill run; MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. 12 rows extracted (8 ANCHOR, 4 EXECUTION). No RETIRED rows. Schema validation: VALID.
