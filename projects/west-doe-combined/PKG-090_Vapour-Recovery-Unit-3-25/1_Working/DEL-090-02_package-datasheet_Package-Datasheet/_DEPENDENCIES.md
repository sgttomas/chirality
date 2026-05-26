# Dependencies: DEL-090-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill; UPDATE run)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register; this file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

---

## Extracted Dependency Register

**Schema version:** v3.1
**Total rows:** 12
**ACTIVE rows:** 12
**RETIRED rows:** 0

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetID / TargetRefID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-090-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-090 | Vapour Recovery Unit 3-25 | HIGH | ACTIVE |
| DEP-090-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0249 | SOW-0249 | HIGH | ACTIVE |
| DEP-090-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0250 | SOW-0250 | HIGH | ACTIVE |
| DEP-090-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0251 | SOW-0251 | HIGH | ACTIVE |
| DEP-090-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0252 | SOW-0252 | HIGH | ACTIVE |
| DEP-090-02-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-090-01_scope-of-work | Scope of Work (DEL-090-01) | HIGH | ACTIVE |
| DEP-090-02-007 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-090-03_construction-work-package | Construction Work Package (DEL-090-03) | HIGH | ACTIVE |
| DEP-090-02-008 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-090-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package (DEL-090-04) | HIGH | ACTIVE |
| DEP-090-02-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-090-05_vendor-document-turnover-package | Vendor Document Turnover Package (DEL-090-05) | MEDIUM | ACTIVE |
| DEP-090-02-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-090-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance (DEL-090-06) | MEDIUM | ACTIVE |
| DEP-090-02-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | SCA-002 | 04-25 SOC Suction Interface (SCA-002) | HIGH | ACTIVE |
| DEP-090-02-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | EXTERNAL | SCA-006 | 04-25 Instrument Air Supply (SCA-006) | HIGH | ACTIVE |

**ANCHOR rows:** 5 (1 × IMPLEMENTS_NODE, 4 × TRACES_TO_REQUIREMENT)
**EXECUTION rows:** 7 (1 UPSTREAM PREREQUISITE, 1 UPSTREAM INTERFACE, 1 UPSTREAM CONSTRAINT, 4 DOWNSTREAM HANDOVER)

---

## Run Notes

**Run date:** 2026-05-26
**Mode:** UPDATE
**Strictness:** CONSERVATIVE
**Consumer context:** NONE

**Decomposition path resolution:**
- Specified DECOMPOSITION_PATH `GATE-07_Final_Published_2026-05-24/` did not resolve at the invoker-supplied root path.
- Resolved via `_REFERENCES.md` in the deliverable folder to:
  `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PROJECT_DECOMP.md`
- Anchor identifiers validated against `DELIVERABLE_REGISTER.csv` in that snapshot. Resolved path is non-blocking.

**Source documents scanned (AUTO):**
- `Datasheet.md` — ANCHOR_DOC (filename matches `datasheet` heuristic)
- `Specification.md` — EXECUTION_DOC (contains requirements and interface constraints)
- `Procedure.md` — EXECUTION_DOC (contains workflow, prerequisites, handoff steps)
- `Guidance.md` — EXECUTION_DOC (supporting context; no additional dependency signals beyond those in Procedure.md)
- `_CONTEXT.md` — supplemental read for identity and scope items
- `_REFERENCES.md` — supplemental read for document pointer resolution

**Excluded from scanning (dependency artifacts):**
- `_DEPENDENCIES.md` (this file)
- `_STATUS.md`, `_MEMORY.md`, `_run_records/` (non-source)

**Defaults applied:**
- `SOURCE_DOCS`: AUTO
- `DOC_ROLE_MAP`: DEFAULT
- `ANCHOR_DOC`: AUTO → `Datasheet.md`
- `EXECUTION_DOC_ORDER`: AUTO → `Procedure.md`, `Specification.md`, `Guidance.md`

**Pass 1 — ANCHOR (Tree):**
- One IMPLEMENTS_NODE anchor found: `PKG-090` (confirmed in DELIVERABLE_REGISTER.csv).
- Four TRACES_TO_REQUIREMENT anchors found: SOW-0249, SOW-0250, SOW-0251, SOW-0252 — explicitly listed in `_CONTEXT.md` and `Datasheet.md`.
- Objective associations (OBJ-002 through OBJ-010) are explicitly labeled ASSUMPTION/PACKAGE_HEURISTIC in sources; not emitted as ANCHOR rows under CONSERVATIVE strictness.

**Pass 2 — EXECUTION (DAG):**
- DEL-090-01 (UPSTREAM PREREQUISITE): Procedure.md explicitly states implicit information dependency on the package SOW; emitted as ASSUMPTION in Notes with Confidence=HIGH since evidence is explicit.
- DEL-090-03/04/05/06 (DOWNSTREAM HANDOVER): Procedure.md Step 8 and Specification.md Out of scope explicitly name all four consumers.
- SCA-002 / 04-25 SOC suction interface (UPSTREAM INTERFACE): Datasheet.md and Procedure.md explicitly note that 04-25 SOC suction design conditions are required but TBD; emitted as EXTERNAL with TargetLocation=`location TBD`.
- SCA-006 / 04-25 IA supply (UPSTREAM CONSTRAINT): Specification R-5.1 and Datasheet.md explicitly state IA from 04-25 under SCA-006; this is a binding constraint on the datasheet content.

**Signals NOT emitted (CONSERVATIVE exclusions):**
- LP fuel-gas blanket/make-up supply: cross-facility utility relationship; no explicit data/artifact transfer stated.
- Electrical power: cross-facility utility; structural adjacency only.
- LP flare / KO drum interface (V-3900-2 / P-3900-2): coordination-level interface; detailed design resolution noted as TBD in source — not a current explicit artifact transfer.
- Plant Shutdown and Blowdown Philosophy (W242510-PRC-REP-000003-001): referenced as an inaccessible source; no artifact transfer currently active.

**Warnings:**
- None. One IMPLEMENTS_NODE anchor confirmed (no FLOATING_NODE warning). Single parent anchor (no AMBIGUOUS_ANCHOR warning).

---

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 12 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 12 |

| DependencyClass | ACTIVE count |
|---|---|
| ANCHOR | 5 |
| EXECUTION | 7 |

---

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-26 — dependency-extract skill UPDATE run; MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition resolved via `_REFERENCES.md` to GATE-07_Final_Published_2026-05-24. 12 rows extracted (5 ANCHOR, 7 EXECUTION); all ACTIVE. No warnings.
