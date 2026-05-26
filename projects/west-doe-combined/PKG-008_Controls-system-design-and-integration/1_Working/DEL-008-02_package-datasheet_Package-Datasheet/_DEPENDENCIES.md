# Dependencies: DEL-008-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1, 29 required columns). This file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Dependencies.csv produced by `TASK + dependency-extract` on 2026-05-25.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-008-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0008 | Scope decision SOW-0008 — Controls system design and integration | ACTIVE |
| DEP-008-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | Project Objective OBJ-001 — 04-25 Deepcut facility scope | ACTIVE |
| DEP-008-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-003 | Project Objective OBJ-003 — Commercial stream disposition and facility boundary interfaces | ACTIVE |
| DEP-008-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Project Objective OBJ-005 — Electrical power basis and integration | ACTIVE |
| DEP-008-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Project Objective OBJ-006 — Controls instrumentation and integration | ACTIVE |
| DEP-008-02-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | Project Objective OBJ-007 — Shared utilities and ancillary support systems | ACTIVE |
| DEP-008-02-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 — Safety regulatory and protection requirements | ACTIVE |
| DEP-008-02-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 — Operability maintainability and handoff closure | ACTIVE |
| DEP-008-02-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-008-01_scope-of-work | Scope of Work — PKG-008 | ACTIVE |
| DEP-008-02-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | ART-436DB2FC91 | Gate 7 ARTIFACT_REGISTER.csv — ART-436DB2FC91 | ACTIVE |
| DEP-008-02-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-D2D1BD1026 | Gate 7 INTERFACE_REGISTER.csv — IFC-D2D1BD1026 (Process Piping) | ACTIVE |
| DEP-008-02-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-75266A066A | Gate 7 INTERFACE_REGISTER.csv — IFC-75266A066A (Electrical Power) | ACTIVE |
| DEP-008-02-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-4CEE0807EF | Gate 7 INTERFACE_REGISTER.csv — IFC-4CEE0807EF (I&C / Control Cabling) | ACTIVE |

**Total ACTIVE rows:** 13 (8 ANCHOR, 5 EXECUTION)
**Total RETIRED rows:** 0

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 13 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 13 |

**Anchor integrity:** 1 IMPLEMENTS_NODE row (DEP-008-02-001) — no FLOATING_NODE warning. No AMBIGUOUS_ANCHOR.

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; docs found: Datasheet.md (ANCHOR_DOC by heuristic — contains "datasheet"), Specification.md, Procedure.md, Guidance.md (EXECUTION_DOC candidates).
- **ANCHOR_DOC:** Datasheet.md (auto-selected; highest-confidence match for anchor signals — "datasheet" keyword, identification table with Scope item field).
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — used to validate SOW-0008 and all objective traces, and to resolve canonical labels. Anchor validated against SCOPE_LEDGER.csv and DELIVERABLE_REGISTER.csv.
- **RUN_ROOT:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined`
- **No MISSING_DECOMPOSITION warning:** decomposition path was provided and resolved successfully.
- DEP-008-02-009 (PREREQUISITE to DEL-008-01_scope-of-work) is emitted as IMPLICIT / ASSUMPTION under CONSERVATIVE strictness. The source documents do not state an explicit prerequisite on the scope-of-work deliverable, but the Datasheet.md construction section requires package identity and function as inputs, which are the primary output of DEL-008-01. Marked ASSUMPTION in Notes.
- Interface rows DEP-008-02-011 through DEP-008-02-013 are a representative sample of the eight interface facts explicitly cited in Datasheet.md Conditions table. The remaining five interface IDs (IFC-6C2256AC08, IFC-E03E8F6BE7, IFC-BF775689A9, IFC-0B74978715, IFC-1D7716801B) were not emitted separately to avoid row proliferation under CONSERVATIVE strictness; the interface matrix is captured structurally by DEP-008-02-011 to DEP-008-02-013 with the same evidence file. If AGGRESSIVE strictness or CONSUMER_CONTEXT=AGGREGATION is requested, emit one row per interface IFC ID.
- `_REFERENCES.md` is present in the deliverable folder; no new `TargetType=DOCUMENT` rows were derived solely from `_REFERENCES.md` — evidence must appear in source documents per skill contract.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — EXTRACTED run by TASK + dependency-extract. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition: GATE-07_Final_Published_2026-05-24 (resolved). 13 ACTIVE rows emitted (8 ANCHOR, 5 EXECUTION). No FLOATING_NODE. No prior CSV existed; created fresh.
