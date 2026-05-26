# Dependencies: DEL-103-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (Dependencies.csv v3.1 produced)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

---

## Extracted Dependency Register

**Total ACTIVE rows:** 15  
**Schema version:** v3.1  
**Last extraction run:** 2026-05-26 (MODE=UPDATE, STRICTNESS=CONSERVATIVE)

### Summary Table

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName (short) | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-103-01-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0259 | Scope Item SOW-0259 — Pipe Rack Modules | ACTIVE |
| DEP-103-01-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-002 | OBJ-002 — 03-25 compressor station scope | ACTIVE |
| DEP-103-01-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | OBJ-005 — Electrical power basis | ACTIVE |
| DEP-103-01-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | OBJ-006 — Controls / I&C / comms | ACTIVE |
| DEP-103-01-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | OBJ-007 — Shared utilities | ACTIVE |
| DEP-103-01-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | OBJ-008 — Civil / structural / pipe rack | ACTIVE |
| DEP-103-01-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | OBJ-009 — Sour-service safety / regulatory | ACTIVE |
| DEP-103-01-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | OBJ-010 — Operability / turnover closure | ACTIVE |
| DEP-103-01-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | Gate-07 PROJECT_DECOMP snapshot | ACTIVE |
| DEP-103-01-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | Final geotechnical report | ACTIVE |
| DEP-103-01-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | DOCUMENT | — | HAC classification drawings | ACTIVE |
| DEP-103-01-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | Plot plan / 3D model | ACTIVE |
| DEP-103-01-013 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-103-02_package-datasheet | Package Datasheet — DEL-103-02 | ACTIVE |
| DEP-103-01-014 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-103-03_construction-work-package | Construction Work Package — DEL-103-03 | ACTIVE |
| DEP-103-01-015 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-103-04_epc-structural-discipline-production-package | EPC / Structural Discipline Production Package — DEL-103-04 | ACTIVE |

---

## Run Notes

**Run date:** 2026-05-26  
**Mode:** UPDATE  
**Strictness:** CONSERVATIVE  
**Consumer context:** NONE  
**Source documents scanned (AUTO):** Datasheet.md, Specification.md, Guidance.md, Procedure.md  
**Anchor doc (AUTO):** Datasheet.md (contains explicit traceability fields: Covers Scope Item, Supports Objectives)  
**Execution doc order (AUTO):** Procedure.md (workflow/prerequisites), Specification.md (requirements), Guidance.md (constraints/conflicts)  
**Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`  
**Decomposition status:** FOUND — used for anchor validation and label resolution  
**`_REFERENCES.md` used:** Yes — confirmed decomposition path and shared source root  

**Decomposition note:** DECOMPOSITION_PATH parameter supplied as `GATE-07_Final_Published_2026-05-24/` path; resolved to `_GateSnapshots/GATE-07_Final_Published_2026-05-24/` under `_Decomposition/PROJECT_DECOMP/`. Gate-07 is the authoritative published snapshot.

**Pass 1 (ANCHOR) findings:**
- One IMPLEMENTS_NODE anchor to SOW-0259 confirmed in SCOPE_LEDGER row 260. Parent anchor count = 1. No FLOATING_NODE or AMBIGUOUS_ANCHOR warnings.
- Seven TRACES_TO_REQUIREMENT anchors to OBJ-002, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 — all confirmed in DELIVERABLE_REGISTER row 584 Objectives column and OBJECTIVE_REGISTER.

**Pass 2 (EXECUTION) findings:**
- DEP-103-01-009: Gate-07 decomposition snapshot — all source registers explicitly listed as required inputs in Procedure.md Prerequisites before drafting can proceed. UPSTREAM PREREQUISITE.
- DEP-103-01-010: Final geotechnical report — DBM-Comp_and_Liquids line 688 states this is required upstream of foundation design closure; applies to rack supports per Datasheet Conditions. TargetLocation=TBD (report not in accessible sources). UPSTREAM PREREQUISITE, SatisfactionStatus=PENDING.
- DEP-103-01-011: Hazardous area classification drawings — DBM-Comp_and_Liquids line 722 and CONF-103-01-02 state classification drawings are required to override the non-hazardous default for outdoor pipe racks. TargetLocation=TBD. UPSTREAM CONSTRAINT, SatisfactionStatus=PENDING.
- DEP-103-01-012: Plot plan / 3D model — PACKAGE_REGISTER row 104 note and SPEC-103-01-R08/R13 require this for tagged-equipment list and commodity confirmation. TargetLocation=TBD. UPSTREAM PREREQUISITE, SatisfactionStatus=PENDING.
- DEP-103-01-013/014/015: Three sibling deliverables (DEL-103-02, DEL-103-03, DEL-103-04) explicitly identified in SPEC-103-01-R14 and DELIVERABLE_REGISTER rows 585-587. SoW is the Gate 5 anchor enabling all three. DOWNSTREAM ENABLES.

**Excluded (CONSERVATIVE, out of scope):**
- Nine interface types (Process Piping, Utility Piping, etc.) listed in PACKAGE_REGISTER row 104 — these are interface types, not information-flow dependencies between deliverables. No source states a specific data/artifact transfer to specific deliverables from these interfaces at this stage.
- OBJ-001 — not listed in DELIVERABLE_REGISTER row 584 (WBS-01 objective; PKG-103 is WBS-03).
- DEC-001 (open decision attached to SOW-0259) — this is an open issue/decision, not an information-flow dependency edge. It is surfaced in the source documents but does not constitute a PREREQUISITE or CONSTRAINT on information transfer between specific deliverables.

---

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 15 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 12 |
| PENDING | 3 |

**PENDING rows (open dependencies with known gap):**
- DEP-103-01-010 — Final geotechnical report (location TBD)
- DEP-103-01-011 — HAC classification drawings (location TBD)
- DEP-103-01-012 — Plot plan / 3D model (location TBD)

**Tree x DAG integrity:**
- Parent anchor (IMPLEMENTS_NODE): 1 — OK
- No FLOATING_NODE warning
- No AMBIGUOUS_ANCHOR warning

---

## Run History

| Date | Mode | Strictness | Decomposition | Warnings | ACTIVE rows |
|---|---|---|---|---|---|
| 2026-05-24 | — | — | DECLARED init (PREPARATION) | None | 0 (declared only) |
| 2026-05-26 | UPDATE | CONSERVATIVE | GATE-07_Final_Published_2026-05-24 (FOUND) | None | 15 |
