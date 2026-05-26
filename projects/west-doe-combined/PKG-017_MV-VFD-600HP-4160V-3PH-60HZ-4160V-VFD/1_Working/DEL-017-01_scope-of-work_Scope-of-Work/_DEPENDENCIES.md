# Dependencies: DEL-017-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill; first run)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1). This file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

**Schema version:** v3.1
**Total rows (ACTIVE):** 14
**ANCHOR rows (ACTIVE):** 8 (1 IMPLEMENTS_NODE + 7 TRACES_TO_REQUIREMENT)
**EXECUTION rows (ACTIVE):** 6 (3 UPSTREAM PREREQUISITE + 3 DOWNSTREAM HANDOVER)
**RETIRED rows:** 0

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName (short) | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-017-01-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0018 | Scope decision SOW-0018 (PKG-017 parent) | HIGH | ACTIVE |
| DEP-017-01-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-002 | 03-25 compressor station and liquids hub scope | HIGH | ACTIVE |
| DEP-017-01-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Vendor-owned package responsibility model | HIGH | ACTIVE |
| DEP-017-01-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Facility electrical power and equipment basis | HIGH | ACTIVE |
| DEP-017-01-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Controls instrumentation and communications | HIGH | ACTIVE |
| DEP-017-01-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Civil structural site and construction-support | HIGH | ACTIVE |
| DEP-017-01-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Safety regulatory codes and standards | HIGH | ACTIVE |
| DEP-017-01-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Operability maintainability turnover closure | HIGH | ACTIVE |
| DEP-017-01-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | Gate 7 PROJECT_DECOMP snapshot (PACKAGE/DELIVERABLE registers) | HIGH | ACTIVE |
| DEP-017-01-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | INTERFACE_REGISTER.csv — PKG-017 rows (6 interfaces) | HIGH | ACTIVE |
| DEP-017-01-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | DBM 3-25_Comp_and_Liquids electrical source slices | HIGH | ACTIVE |
| DEP-017-01-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-017-02_package-datasheet | Package Datasheet | HIGH | ACTIVE |
| DEP-017-01-013 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-017-03_construction-work-package | Construction Work Package | HIGH | ACTIVE |
| DEP-017-01-014 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-017-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package | HIGH | ACTIVE |

## Run Notes

- **Run date:** 2026-05-25
- **Mode:** UPDATE (first run; no existing Dependencies.csv)
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **Source docs scanned (AUTO):** `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, `_CONTEXT.md`, `_REFERENCES.md`
- **Anchor doc (AUTO):** `Datasheet.md` (contains "scope" signal; identity/traceability fields)
- **Execution docs (AUTO order):** `Procedure.md` (procedure/prerequisites), `Specification.md` (requirements/scope), `Guidance.md` (considerations/trade-offs)
- **Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
- **Decomposition status:** FOUND — SCOPE_LEDGER.csv and DELIVERABLE_REGISTER.csv used to confirm SOW-0018 parent anchor and objective trace list.
- **ID format used:** DEP-017-01-NNN (three-digit sequence)
- **Pass 1 (ANCHOR):** SOW-0018 confirmed as IMPLEMENTS_NODE via SCOPE_LEDGER.csv. OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010 confirmed as TRACES_TO_REQUIREMENT via DELIVERABLE_REGISTER.csv.
- **Pass 2 (EXECUTION):** Three upstream PREREQUISITE edges extracted from explicit Procedure.md prerequisites (Gate 7 snapshot, INTERFACE_REGISTER.csv, DBM electrical slices). Three downstream HANDOVER edges extracted from Specification.md scope statement and DELIVERABLE_REGISTER.csv sibling deliverables (DEL-017-02, DEL-017-03, DEL-017-04).
- **TargetLocation note (DEP-017-01-011):** DBM source `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` not registered by stable path in `_REFERENCES.md` for this deliverable; TargetLocation left as decomposition snapshot folder. Evidence path recorded in EvidenceFile.
- **Tree integrity:** 1 IMPLEMENTS_NODE (DEP-017-01-001) — no FLOATING_NODE warning. No AMBIGUOUS_ANCHOR.
- **Excluded (conservative):** No edges emitted for pure coordination or structural adjacency (e.g., "keep aligned with other electrical packages"). No edges emitted for DEL-017-05 or DEL-017-06 as the Scope of Work does not explicitly state it produces information consumed by those deliverables beyond what is captured in the vendor package handover chain.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 14 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 11 |
| PENDING | 3 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First EXTRACTED run via dependency-extract skill. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition FOUND. 14 ACTIVE rows written (8 ANCHOR, 6 EXECUTION). No RETIRED rows. No integrity warnings.
