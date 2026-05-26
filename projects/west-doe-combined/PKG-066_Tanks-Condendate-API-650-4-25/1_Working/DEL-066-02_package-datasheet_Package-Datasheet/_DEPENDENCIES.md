# Dependencies: DEL-066-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1 schema); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

10 rows extracted (all ACTIVE). Schema version: v3.1.

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetID / TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-066-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | PACKAGE | PKG-066 — Tanks, Condendate (API 650) 4-25 | HIGH | ACTIVE |
| DEP-066-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0205 | HIGH | ACTIVE |
| DEP-066-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0206 | HIGH | ACTIVE |
| DEP-066-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0207 | HIGH | ACTIVE |
| DEP-066-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0208 | HIGH | ACTIVE |
| DEP-066-02-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-066-01_scope-of-work | HIGH | ACTIVE |
| DEP-066-02-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | 4-25 Deep Cut Gas Plant DBM | HIGH | ACTIVE |
| DEP-066-02-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | 03-25 Compressor & Liquids Hub DBM | HIGH | ACTIVE |
| DEP-066-02-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-066-04_vendor-engineered-equipment-package | HIGH | ACTIVE |
| DEP-066-02-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | INTERFACE | DELIVERABLE | DEL-066-06_epc-vendor-package-review-and-acceptance | MEDIUM | ACTIVE |

## Run Notes

- **Run date:** 2026-05-25
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; docs in scope: `Datasheet.md`, `Guidance.md`, `Procedure.md`, `_CONTEXT.md`, `_REFERENCES.md`
- **ANCHOR_DOC:** `Datasheet.md` (heuristic match: filename contains "datasheet")
- **EXECUTION_DOC_ORDER:** `Procedure.md` (primary; contains prerequisite signals), `Guidance.md` (secondary; context/trade-off signals), `Datasheet.md` (interface section)
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — USED; anchors validated against `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `SCOPE_LEDGER.csv`
- **Decomposition status:** VALID — PKG-066 and DEL-066-02 confirmed in registers; SOW-0205/0206/0207/0208 confirmed in SCOPE_LEDGER.csv
- **IMPLEMENTS_NODE parent anchor:** 1 row (DEP-066-02-001) — parent anchor count OK
- **Prior Dependencies.csv:** Did not exist; created fresh.
- **Legacy normalization:** No legacy INBOUND/OUTBOUND values encountered.
- **TBD markers carried forward:** DEL-066-01 prerequisite is stated as "recommended coordination dependency, not a declared blocker" in the pre-run `_DEPENDENCIES.md`; extracted as PREREQUISITE because Procedure.md states an explicit state-gate condition ("at INITIALIZED or later"). Conservative extraction — row carries FACT label in Notes.
- **Inaccessible source:** `26020-Package_Requirements.docx` package heading 21 not locally readable; no execution edges invented from this source. All TBD construction and nozzle-schedule items remain TBD in the Datasheet; no dependency rows created for unresolvable targets.
- **CONF-066-02-01 scope conflict:** Scope of condensate tank equipment is unresolved (04-25 vs 03-25 location); no dependency edges depend on this resolution. Human ruling still required per Guidance.md Conflict Table.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 10 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 10 |

| DependencyClass | Count |
|---|---|
| ANCHOR | 5 |
| EXECUTION | 5 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full two-pass extraction run (dependency-extract skill, MODE=UPDATE, STRICTNESS=CONSERVATIVE). 10 rows created (5 ANCHOR + 5 EXECUTION). All ACTIVE. Schema v3.1. Decomposition GATE-07_Final_Published_2026-05-24 used for anchor validation.
