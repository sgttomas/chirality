# Dependencies: DEL-024-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

17 rows total — 17 ACTIVE, 0 RETIRED.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-024-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0025 | Scope decision SOW-0025 — MV VFD 2000HP 4160V VFD | HIGH | ACTIVE |
| DEP-024-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | Project Objective OBJ-001 — 04-25 Deepcut facility scope | HIGH | ACTIVE |
| DEP-024-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Project Objective OBJ-004 — Vendor-owned package execution | HIGH | ACTIVE |
| DEP-024-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Project Objective OBJ-005 — Facility electrical power basis | HIGH | ACTIVE |
| DEP-024-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Project Objective OBJ-006 — Controls instrumentation interfaces | HIGH | ACTIVE |
| DEP-024-02-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Project Objective OBJ-008 — Civil structural foundations | HIGH | ACTIVE |
| DEP-024-02-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 — Safety regulatory standards | HIGH | ACTIVE |
| DEP-024-02-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 — Operability maintainability handoff | HIGH | ACTIVE |
| DEP-024-02-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-024-01_scope-of-work | Scope of Work — PKG-024 | HIGH | ACTIVE |
| DEP-024-02-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-024-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package — PKG-024 | HIGH | ACTIVE |
| DEP-024-02-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-68C5E24846 | Interface Fact — Electrical Power (PKG-024) | HIGH | ACTIVE |
| DEP-024-02-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-F8A6E25E1C | Interface Fact — Grounding / Bonding (PKG-024) | HIGH | ACTIVE |
| DEP-024-02-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-8062D6F881 | Interface Fact — I&C / Control Cabling (PKG-024) | HIGH | ACTIVE |
| DEP-024-02-014 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-22E88310C9 | Interface Fact — Communications / Network (PKG-024) | HIGH | ACTIVE |
| DEP-024-02-015 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-DD889EF8E3 | Interface Fact — Maintenance Access (PKG-024) | HIGH | ACTIVE |
| DEP-024-02-016 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-850A8082BB | Interface Fact — Structural / Foundations / Supports (PKG-024) | HIGH | ACTIVE |
| DEP-024-02-017 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | DBM-Deepcut 4-25_Deepcut_DBM.md — Electrical Design Basis | HIGH | ACTIVE |

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 17 |
| RETIRED | 0 |
| **Total** | **17** |

**SatisfactionStatus breakdown (ACTIVE rows):**

| SatisfactionStatus | Count |
|---|---|
| TBD | 17 |

## Run Notes

- **Run date:** 2026-05-25
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; source documents found: `Datasheet.md`, `_CONTEXT.md`, `_REFERENCES.md`
- **ANCHOR_DOC:** `Datasheet.md` (heuristic match: filename contains `datasheet`)
- **EXECUTION_DOCS:** `Datasheet.md`, `_CONTEXT.md`, `_REFERENCES.md`
- **DECOMPOSITION_PATH:** `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — resolved via `_CONTEXT.md` Decomposition Reference field. Note: brief supplied path `GATE-07_Final_Published_2026-05-24/` at run root did not resolve; actual path located at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`.
- **Parent anchor:** DEP-024-02-001 → SOW-0025 confirmed in SCOPE_LEDGER.csv. No FLOATING_NODE warning.
- **Objective traces:** 7 objectives (OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010) confirmed in DELIVERABLE_REGISTER.csv.
- **Execution edges:** 9 rows extracted from `Datasheet.md` — 1 PREREQUISITE upstream (DEL-024-01 SOW), 1 HANDOVER downstream (DEL-024-04 vendor package), 6 INTERFACE upstream (interface register facts explicitly required by Datasheet.md Conditions table), 1 PREREQUISITE upstream (DBM-Deepcut source document).
- **`_REFERENCES.md` note:** References file confirms no deliverable-specific source slices were copied during PREPARATION; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` path used as documented in Datasheet.md.
- **TBD fields:** Driven equipment tag/service not assigned in sources; MV VFD topology TBD; installation location TBD. These are not dependency rows — they are source gaps noted in Datasheet.md.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract skill run; MODE=UPDATE; STRICTNESS=CONSERVATIVE; CONSUMER_CONTEXT=NONE; decomposition path resolved to `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`; 17 rows extracted (8 ANCHOR, 9 EXECUTION); 0 retired; all rows ACTIVE.
