# Dependencies: DEL-012-05_vendor-document-turnover-package — Vendor Document Turnover Package

**Coordination Mode:** DECLARED
**Dependency tracking mode:** DECLARED + EXTRACTED
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Register produced by `TASK + dependency-extract` on 2026-05-25. Schema version: v3.1. Total rows: 10.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-012-05-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0013 | Scope decision SOW-0013 — 10KVA AC UNINTERRUPTIBLE POWER SUPPLY (WBS 02) | ACTIVE |
| DEP-012-05-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-002 | Project Objective OBJ-002 — 03-25 compressor station and liquids hub scope | ACTIVE |
| DEP-012-05-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Project Objective OBJ-004 — vendor-owned package execution with vendor engineering and EPC integration review | ACTIVE |
| DEP-012-05-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Project Objective OBJ-005 — facility electrical power basis and electrical interfaces to vendor packages | ACTIVE |
| DEP-012-05-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Project Objective OBJ-008 — civil structural site foundations grading containment access and construction-support scope | ACTIVE |
| DEP-012-05-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 — sour-service safety relief flare shutdown environmental and regulatory requirements | ACTIVE |
| DEP-012-05-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 — operability maintainability vendor-documentation commissioning turnover and controlled open-item closure evidence | ACTIVE |
| DEP-012-05-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | GATE-07_Final_Published_2026-05-24 | Gate 7 final published PROJECT_DECOMP snapshot dated 2026-05-24 | ACTIVE |
| DEP-012-05-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | UNKNOWN | — | Vendor document register (or interim gap record) | ACTIVE |
| DEP-012-05-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-012-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance | ACTIVE |

**ACTIVE count:** 10 (7 ANCHOR, 3 EXECUTION)
**RETIRED count:** 0

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; source documents used: `Datasheet.md` (ANCHOR_DOC), `Procedure.md`, `Specification.md`, `Guidance.md` (EXECUTION_DOC_ORDER)
- **ANCHOR_DOC:** `Datasheet.md` (highest-confidence match per heuristic — contains identification, scope item, and supported objectives)
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — confirmed accessible; used to validate SOW-0013 anchor and OBJ traces via `SCOPE_LEDGER.csv`, `DELIVERABLE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- **DependencyID format:** DEP-012-05-NNN
- **Pass 1 (ANCHOR):** One parent anchor (IMPLEMENTS_NODE → SOW-0013) and six objective trace anchors (OBJ-002 through OBJ-010 excluding OBJ-003, OBJ-006, OBJ-007) emitted. All confirmed explicitly in `Datasheet.md` and validated against Gate 7 registers.
- **Pass 2 (EXECUTION):** Three EXECUTION rows emitted under CONSERVATIVE strictness:
  - DEP-012-05-008: Gate 7 snapshot as explicit document prerequisite (Procedure.md prerequisite list).
  - DEP-012-05-009: Vendor document register as explicit UPSTREAM PREREQUISITE; marked PENDING SatisfactionStatus because Gate 7 records only a TBD placeholder artifact (ART-68AD3064DD). RequiredMaturity set to ACCEPTED.
  - DEP-012-05-010: DOWNSTREAM HANDOVER to DEL-012-06 — the EPC Vendor Package Review and Acceptance deliverable explicitly consumes this turnover package for vendor document review log and acceptance checklist. Confirmed via DELIVERABLE_REGISTER.csv DEL-012-06 anticipated artifacts.
- **Signals not extracted (CONSERVATIVE):** No additional inter-deliverable prerequisites emitted because Procedure.md does not explicitly name other PKG-012 deliverables as required inputs by artifact transfer. The EPC Integrator review path (DEL-012-06) is captured as a DOWNSTREAM HANDOVER rather than an UPSTREAM PREREQUISITE because the direction of explicit artifact flow is from this deliverable to DEL-012-06, not the reverse.
- **ASSUMPTION noted in DEP-012-05-010 Notes:** DEL-012-06 is the named downstream consumer based on decomposition structure. No other deliverable in PKG-012 explicitly claims this handover role.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 10 |
| RETIRED | 0 |

| SatisfactionStatus | Count (ACTIVE rows) |
|---|---|
| TBD | 9 |
| PENDING | 1 |

**Tree x DAG integrity:**
- Parent anchor (IMPLEMENTS_NODE): 1 — OK
- Trace anchors (TRACES_TO_REQUIREMENT): 6 — OK
- No FLOATING_NODE or AMBIGUOUS_ANCHOR warnings.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First extraction run; MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition: GATE-07_Final_Published_2026-05-24 (accessible). 10 rows ACTIVE (7 ANCHOR, 3 EXECUTION). No warnings.
