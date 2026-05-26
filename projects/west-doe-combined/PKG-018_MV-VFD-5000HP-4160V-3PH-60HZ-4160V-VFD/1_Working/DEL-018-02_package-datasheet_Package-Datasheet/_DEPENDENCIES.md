# Dependencies: DEL-018-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract repair run 2026-05-26)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1). This file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` generated for the previously-missing dependency extract on 2026-05-26.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-018-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0019 | Scope decision SOW-0019 — MV VFD 5000HP 4160V WBS 02 | HIGH | ACTIVE |
| DEP-018-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-002 | Project Objective OBJ-002 — 03-25 compressor station and liquids hub scope | HIGH | ACTIVE |
| DEP-018-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Project Objective OBJ-004 — Vendor-owned package responsibility model | HIGH | ACTIVE |
| DEP-018-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Project Objective OBJ-005 — Facility electrical power and equipment basis | HIGH | ACTIVE |
| DEP-018-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Project Objective OBJ-006 — Controls instrumentation and communications | HIGH | ACTIVE |
| DEP-018-02-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Project Objective OBJ-008 — Civil structural site and construction support | HIGH | ACTIVE |
| DEP-018-02-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 — Safety regulatory codes and standards | HIGH | ACTIVE |
| DEP-018-02-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 — Operability maintainability turnover closure | HIGH | ACTIVE |
| DEP-018-02-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-018-01_scope-of-work | Scope of Work | HIGH | ACTIVE |
| DEP-018-02-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | Gate 7 PROJECT_DECOMP snapshot | HIGH | ACTIVE |
| DEP-018-02-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | Workbook Packages row 20 — 26020-Packages_Interfaces_4_export | HIGH | ACTIVE |
| DEP-018-02-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | 3-25 Compressor and Liquids DBM electrical source slices | HIGH | ACTIVE |
| DEP-018-02-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | 4-25 Deepcut DBM electrical source slices | HIGH | ACTIVE |
| DEP-018-02-014 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-81D9418AA1 | Interface — Electrical Power | HIGH | ACTIVE |
| DEP-018-02-015 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-20754345F3 | Interface — Grounding / Bonding | HIGH | ACTIVE |
| DEP-018-02-016 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-EF82F842B4 | Interface — I&C / Control Cabling | HIGH | ACTIVE |
| DEP-018-02-017 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-DC83D04DC5 | Interface — Communications / Network | HIGH | ACTIVE |
| DEP-018-02-018 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-35F60961CA | Interface — Maintenance Access | HIGH | ACTIVE |
| DEP-018-02-019 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-87DE46369F | Interface — Structural / Foundations / Supports | HIGH | ACTIVE |
| DEP-018-02-020 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | Detailed electrical harmonic/reactive-power study | MEDIUM | ACTIVE |
| DEP-018-02-021 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | EXTERNAL | — | Human rulings CT-018-02-01 through CT-018-02-03 | HIGH | ACTIVE |
| DEP-018-02-022 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-018-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package | HIGH | ACTIVE |
| DEP-018-02-023 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-018-03_construction-work-package | Construction Work Package | HIGH | ACTIVE |
| DEP-018-02-024 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-018-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance | HIGH | ACTIVE |

## Run Notes

- **Run date:** 2026-05-26
- **Mode:** UPDATE (first extracted run; no previous `Dependencies.csv`)
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **Source docs scanned:** `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, `_CONTEXT.md`, `_REFERENCES.md`, existing `_DEPENDENCIES.md`
- **Anchor doc:** `_CONTEXT.md` and `Datasheet.md` (scope item and objectives are explicit)
- **Execution docs:** `Procedure.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`
- **Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
- **Pass 1 (ANCHOR):** SOW-0019 and objectives OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010 are explicit in `_CONTEXT.md`.
- **Pass 2 (EXECUTION):** Extracted only explicit information-flow rows: Scope of Work prerequisite, required source documents, six interface facts, pending harmonic/reactive-power study, pending human rulings for CT-018-02-01 through CT-018-02-03, and named downstream consumers DEL-018-04, DEL-018-03, and DEL-018-06.
- **Conservative exclusions:** No dependency row was emitted solely for IEEE 519, electrical-building assumption, or unconfirmed KM-2150/KM-2250 driven-load assignment; those remain source/context issues rather than standalone information-flow edges.
- **Tree integrity:** one `IMPLEMENTS_NODE` anchor found. No `[WARNING] FLOATING_NODE`. No `[WARNING] AMBIGUOUS_ANCHOR`. Decomposition snapshot was found.

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 24 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| TBD | 18 |
| SATISFIED | 4 |
| PENDING | 2 |

| DependencyClass | ACTIVE count |
|---|---:|
| ANCHOR | 8 |
| EXECUTION | 16 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-26 — Dependency extract repair run for missing PKG-018 artifacts; MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Wrote 24 ACTIVE rows to `Dependencies.csv`; no RETIRED rows; no integrity warnings.
