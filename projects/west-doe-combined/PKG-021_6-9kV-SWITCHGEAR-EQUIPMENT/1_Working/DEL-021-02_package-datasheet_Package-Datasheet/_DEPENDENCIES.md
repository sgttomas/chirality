# Dependencies: DEL-021-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

**Total ACTIVE rows:** 12
**ANCHOR rows (ACTIVE):** 8 (1 IMPLEMENTS_NODE + 7 TRACES_TO_REQUIREMENT)
**EXECUTION rows (ACTIVE):** 4 (2 UPSTREAM + 1 UPSTREAM INTERFACE + 1 DOWNSTREAM HANDOVER)
**RETIRED rows:** 0

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-021-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0022 | HIGH | ACTIVE |
| DEP-021-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | HIGH | ACTIVE |
| DEP-021-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | HIGH | ACTIVE |
| DEP-021-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | HIGH | ACTIVE |
| DEP-021-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | HIGH | ACTIVE |
| DEP-021-02-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | HIGH | ACTIVE |
| DEP-021-02-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | HIGH | ACTIVE |
| DEP-021-02-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | HIGH | ACTIVE |
| DEP-021-02-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | Gate 7 PROJECT_DECOMP snapshot | HIGH | ACTIVE |
| DEP-021-02-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | PACKAGE | PKG-036 — 6.9kV SWITCHGEAR ELECTRICAL BUILDING (830-1) | HIGH | ACTIVE |
| DEP-021-02-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | UNKNOWN | 13.8 kV switchgear (upstream feed; allocation TBD) | MEDIUM | ACTIVE |
| DEP-021-02-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | UNKNOWN | Package Vendor — vendor package engineering | HIGH | ACTIVE |

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; documents in scope: `Datasheet.md`, `Guidance.md`, `Procedure.md`, `Specification.md`, `_CONTEXT.md`, `_REFERENCES.md`
- **ANCHOR_DOC:** `Datasheet.md` (filename contains "datasheet"; highest-confidence match per DEFAULT DOC_ROLE_MAP heuristic)
- **EXECUTION_DOC_ORDER:** `Procedure.md` (contains "procedure"); `Guidance.md` (contains "guidance"); `Datasheet.md` (cross-checked for explicit interface statements); `_CONTEXT.md`
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — used to validate anchors; SOW-0022 confirmed in SCOPE_LEDGER.csv; OBJ-001/004/005/006/008/009/010 confirmed in OBJECTIVE_DELIVERABLE_MAP.csv.
- **RUN_ROOT:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined`
- **Pass 1 (ANCHOR):** SOW-0022 confirmed as parent scope decision node (SCOPE_LEDGER.csv). Seven objective trace anchors confirmed (DELIVERABLE_REGISTER.csv, OBJECTIVE_DELIVERABLE_MAP.csv).
- **Pass 2 (EXECUTION):** Three UPSTREAM edges extracted: Gate 7 snapshot as explicit PREREQUISITE (Procedure.md); PKG-036 scope boundary as INTERFACE (Guidance.md conflict table); 13.8 kV switchgear feed as INTERFACE (Datasheet.md). One DOWNSTREAM HANDOVER to Package Vendor (_CONTEXT.md).
- Interface register facts (IFC-9D7DF96637, IFC-2ACD080082, IFC-B44478ADB6, IFC-FC8113A0CE, IFC-9E975838A2, IFC-A795E61D99) were reviewed; these register the existence of interface topics for PKG-021 but do not state a specific information-artifact transfer with another deliverable. Per CONSERVATIVE strictness, no additional EXECUTION rows were emitted for the six interface facts alone — they are evidenced within the datasheet itself as conditions, not as incoming artifact transfers from other deliverables.
- **[NOTE]** UPS package control-power interface (DEP-021-02-011 / Datasheet.md control-power row) involves a coordination relationship to UPS packages but no specific transferring deliverable ID was found in accessible source at CONSERVATIVE strictness; 13.8 kV switchgear feeder is the primary upstream interface row extracted.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 12 |
| RETIRED | 0 |

| SatisfactionStatus | ACTIVE rows |
|---|---|
| TBD | 8 (all ANCHOR rows) |
| PENDING | 4 (all EXECUTION rows) |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full extraction run; MODE=UPDATE; STRICTNESS=CONSERVATIVE; CONSUMER_CONTEXT=NONE; decomposition path confirmed; 12 rows written (8 ANCHOR + 4 EXECUTION); 0 RETIRED; schema validation VALID. (dependency-extract skill)
