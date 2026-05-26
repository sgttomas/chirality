# Dependencies: DEL-071-03_construction-work-package — Construction Work Package

**Coordination Mode:** EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill)
**Default maturity threshold:** ACCEPTED
**Register convention:** `Dependencies.csv` is the authoritative structured register (v3.1). This file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

11 rows total — 11 ACTIVE, 0 RETIRED.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetID / TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-071-03-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-071 — Fuel Gas Skid 4-25 | HIGH | ACTIVE |
| DEP-071-03-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0099 | HIGH | ACTIVE |
| DEP-071-03-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0100 | HIGH | ACTIVE |
| DEP-071-03-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0101 | HIGH | ACTIVE |
| DEP-071-03-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0102 | HIGH | ACTIVE |
| DEP-071-03-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-071-01_scope-of-work | HIGH | ACTIVE |
| DEP-071-03-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-071-02_package-datasheet | HIGH | ACTIVE |
| DEP-071-03-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-071-04_vendor-engineered-equipment-package | HIGH | ACTIVE |
| DEP-071-03-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-071-06_epc-vendor-package-review-and-acceptance | HIGH | ACTIVE |
| DEP-071-03-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | DOCUMENT | TSF-002 — Facility F&G Philosophy | HIGH | ACTIVE |
| DEP-071-03-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | UNKNOWN | CONF-FGS-CWP-01 ruling (Electrical Power conflict) | HIGH | ACTIVE |

## Run Notes

- **Run date:** 2026-05-25
- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **Source documents scanned:** `_CONTEXT.md`, `Specification.md`, `Procedure.md`, `Guidance.md`, `Datasheet.md` (read; no additional dependency signals beyond those in Procedure/Guidance/Specification)
- **ANCHOR_DOC (AUTO):** `_CONTEXT.md` (identity/traceability signals); `Specification.md` (requirements traceability)
- **EXECUTION_DOC_ORDER (AUTO):** `Procedure.md` (primary — explicit prerequisites and handovers), `Guidance.md` (constraints and conflicts), `Specification.md` (scope exclusions confirm downstream deliverable boundaries)
- **Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — confirmed GATE-07 snapshot exists; DELIVERABLE_REGISTER.csv confirms DEL-071-03_construction-work-package, PKG-071, SOW-0099–SOW-0102 references.
- **DECOMPOSITION_PATH param:** Invoker supplied `GATE-07_Final_Published_2026-05-24/` under `west-doe-combined/` (no such top-level path); resolved to correct gate snapshot under `_Decomposition/PROJECT_DECOMP/_GateSnapshots/`. Recorded in Run Notes per skill contract.
- **_REFERENCES.md:** Read — no stable document paths to resolve for DOCUMENT-type targets; TSF-002 location recorded as `location TBD`.
- **Pass 1 (ANCHOR):** One IMPLEMENTS_NODE parent anchor to PKG-071 (WBS_NODE); four TRACES_TO_REQUIREMENT anchors to SOW-0099–SOW-0102 (from `_CONTEXT.md` Covers Scope Items). Objectives OBJ-001/OBJ-004–OBJ-010 listed in `_CONTEXT.md` but not emitted as ANCHOR rows — the skill emits REQUIREMENT-type traces only when scope item IDs are explicitly stated; objective IDs are structural context, not dependency edges.
- **Pass 2 (EXECUTION):** Six execution rows. DEL-071-05 (Vendor Document Turnover) not extracted — Specification.md Excluded section names it as out of scope for this deliverable; no explicit information handover stated from this CWP to DEL-071-05. Facility-level inputs (piping code, hazardous area class, seismic class) listed in Specification.md as TBD — not emitted as EXECUTION rows because no stable target ID or document reference was assertable from source; recorded here as advisory.
- **Advisory — unresolved facility inputs (not emitted as rows):** Specification.md / Standards section lists facility piping code, structural code, electrical code, and hazardous area classification as TBD/ASSUMPTION. These are not emitted as dependency rows because no stable target identifier was available and CONSERVATIVE strictness precludes speculative rows. Flag for resolution when facility design basis location is identified.
- **[WARNING] CONF-FGS-CWP-01:** Human ruling on Electrical Power applicability conflict is pending (TBD). Electrical tie-in scope (DEP-071-03-011) is ACTIVE but SatisfactionStatus=TBD. Construction cannot start that scope until ruling is issued.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 11 |
| RETIRED | 0 |
| **Total** | **11** |

| SatisfactionStatus | Count |
|---|---|
| SATISFIED | 5 (ANCHOR rows — decomposition traceability confirmed) |
| TBD | 6 (EXECUTION rows — not yet verified at construction) |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First extraction run. Mode: UPDATE. Strictness: CONSERVATIVE. Decomposition: GATE-07_Final_Published_2026-05-24 (confirmed). Source docs: _CONTEXT.md, Specification.md, Procedure.md, Guidance.md. 11 rows extracted (5 ANCHOR, 6 EXECUTION), all ACTIVE. Schema validated VALID (29 columns, 11 data rows). No prior rows to retire.
