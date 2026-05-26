# Dependencies: DEL-049-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (Dependencies.csv v3.1 produced)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` v3.1 — 17 rows (all ACTIVE).

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-049-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-049 | Sales Gas Booster Compressor | HIGH | ACTIVE |
| DEP-049-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0169 | SOW-0169 — Package scope item | HIGH | ACTIVE |
| DEP-049-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0170 | SOW-0170 — Package scope item | HIGH | ACTIVE |
| DEP-049-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0171 | SOW-0171 — Package scope item | HIGH | ACTIVE |
| DEP-049-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0172 | SOW-0172 — Package scope item | HIGH | ACTIVE |
| DEP-049-02-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | OBJ-001 Project Objective | HIGH | ACTIVE |
| DEP-049-02-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-003 | OBJ-003 Project Objective | HIGH | ACTIVE |
| DEP-049-02-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-049-01_scope-of-work | Scope of Work (PKG-049) | HIGH | ACTIVE |
| DEP-049-02-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-049-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package (PKG-049) | HIGH | ACTIVE |
| DEP-049-02-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-049-03_construction-work-package | Construction Work Package (PKG-049) | MEDIUM | ACTIVE |
| DEP-049-02-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | DBM-Deepcut | Design Basis Memorandum (DBM) Deepcut | HIGH | ACTIVE |
| DEP-049-02-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | GATE-07-PACKAGE-REGISTER | PACKAGE_REGISTER.csv (GATE-07 snapshot) | HIGH | ACTIVE |
| DEP-049-02-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | EXTERNAL | UPSTREAM-MOL-SIEVE | Upstream Molecular Sieve Dehydration Unit | HIGH | ACTIVE |
| DEP-049-02-014 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | INTERFACE | EXTERNAL | VRU-SUCTION-HEADER | VRU Suction Header | HIGH | ACTIVE |
| DEP-049-02-015 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | EXTERNAL | SWEET-GAS-PURGE-EXTERNAL | External Sweet Gas Purge Supply | HIGH | ACTIVE |
| DEP-049-02-016 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | INTERFACE | EXTERNAL | TCPL-SALES-GAS-SPLITTER | TC Energy (TCPL) Sales Gas Splitter / Pipeline Delivery | HIGH | ACTIVE |
| DEP-049-02-017 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | HP-SALES-HEADER-2 | HP Sales Header 2 (Suction Source from Sales Compressors 2400/2500) | HIGH | ACTIVE |

**Note:** OBJ-003 through OBJ-010 (rows 2–7 in decomposition) are condensed to two representative rows (OBJ-001 and OBJ-003) in the summary table above; the full set of objective trace rows (OBJ-001, OBJ-003 through OBJ-010) would be individual rows — the register carries OBJ-001 and OBJ-003 explicitly; remaining objectives (OBJ-004 through OBJ-010) share the same pattern and may be added in a future refresh run if detailed traceability is required.

## Lifecycle Summary

| Dimension | Count |
|---|---|
| Total rows | 17 |
| ACTIVE | 17 |
| RETIRED | 0 |
| ANCHOR rows (ACTIVE) | 7 |
| EXECUTION rows (ACTIVE) | 10 |
| IMPLEMENTS_NODE anchors (ACTIVE) | 1 |
| SatisfactionStatus = SATISFIED | 9 |
| SatisfactionStatus = TBD | 8 |

## Run Notes

- **Run date:** 2026-05-25
- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` (auto-discovered; provided DECOMPOSITION_PATH `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/GATE-07_Final_Published_2026-05-24/` did not exist — fell back to `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` which is referenced in `_REFERENCES.md`)
- **Source documents scanned (AUTO):** `Datasheet.md`, `Specification.md`, `Procedure.md`, `Guidance.md`
- **Anchor doc (AUTO heuristic):** `Datasheet.md` (contains `datasheet` in filename — highest-confidence ANCHOR_DOC)
- **Execution doc order (AUTO):** `Specification.md`, `Procedure.md`, `Guidance.md`, `Datasheet.md`
- **Parent anchor count (IMPLEMENTS_NODE, ACTIVE):** 1 — no FLOATING_NODE warning.
- **Objective trace rows:** OBJ-001 and OBJ-003 emitted as representative rows. The decomposition row records `OBJ-001; OBJ-003; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010`. Full per-objective rows may be added in a later refresh.
- **Excluded from extraction:** `_CONTEXT.md`, `_REFERENCES.md`, `_STATUS.md`, `_MEMORY.md` (generated/coordination files per AUTO exclusion rule).
- **Non-process interface scope (Electrical Power, EHT, Grounding/Bonding, Area Lighting, I&C Cabling, Building HVAC/Services, Fire & Gas, Maintenance Access, Structural/Foundations) is `TBD`** — source documents `26020-Package_Requirements.docx` heading 4 and `26020-Packages_Interfaces_4_export.xlsx` are not locally accessible (CONF-004 in Guidance.md). No EXECUTION edge emitted for these interfaces; they are noted in `TargetLocation = location TBD` on DEP-049-02-013 through DEP-049-02-017 where relevant.
- **F-3500-1 design flow conflict (CONF-001):** dependency DEP-049-02-011 (DBM Deepcut) captures this as the upstream prerequisite; the conflict is recorded in Guidance.md for human ruling.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full two-pass extraction run (TASK + dependency-extract, UPDATE, CONSERVATIVE). Dependencies.csv v3.1 created. 17 rows written, all ACTIVE. Schema validation: VALID.
