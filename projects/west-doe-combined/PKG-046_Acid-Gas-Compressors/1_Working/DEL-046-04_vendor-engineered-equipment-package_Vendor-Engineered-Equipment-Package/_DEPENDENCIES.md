# Dependencies: DEL-046-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1 schema); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` produced by `dependency-extract` run 2026-05-25. 22 rows total; 22 ACTIVE.

### ANCHOR rows (Pass 1 — Tree)

| DependencyID | AnchorType | Direction | TargetType | TargetRefID / TargetName | Confidence |
|---|---|---|---|---|---|
| DEP-046-04-001 | IMPLEMENTS_NODE | UPSTREAM | PACKAGE | PKG-046 — Acid Gas Compressors | HIGH |
| DEP-046-04-002 | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | SOW-0047 | HIGH |
| DEP-046-04-003 | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | SOW-0048 | HIGH |
| DEP-046-04-004 | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | SOW-0049 | HIGH |
| DEP-046-04-005 | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | SOW-0050 | HIGH |
| DEP-046-04-006 | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | OBJ-001 | HIGH |
| DEP-046-04-007 | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | OBJ-003 | HIGH |
| DEP-046-04-008 | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | OBJ-004 | HIGH |
| DEP-046-04-009 | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | OBJ-005 | HIGH |
| DEP-046-04-010 | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | OBJ-006 | HIGH |
| DEP-046-04-011 | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | OBJ-007 | HIGH |
| DEP-046-04-012 | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | OBJ-008 | HIGH |
| DEP-046-04-013 | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | OBJ-009 | HIGH |
| DEP-046-04-014 | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | OBJ-010 | HIGH |

### EXECUTION rows (Pass 2 — DAG)

| DependencyID | Direction | DependencyType | TargetType | Target | Confidence |
|---|---|---|---|---|---|
| DEP-046-04-015 | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-046-01 Scope of Work (PKG-046) | MEDIUM |
| DEP-046-04-016 | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-046-02 Package Datasheet (PKG-046) | MEDIUM |
| DEP-046-04-017 | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-046-05 Vendor Document Turnover Package | HIGH |
| DEP-046-04-018 | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-046-06 EPC Vendor Package Review and Acceptance | HIGH |
| DEP-046-04-019 | UPSTREAM | CONSTRAINT | EXTERNAL | Tourmaline — disposal well pressure characteristics (TBC) | HIGH |
| DEP-046-04-020 | UPSTREAM | PREREQUISITE | EXTERNAL | Conflict Table rulings C-1, C-2, C-3 (human authority — TBD) | HIGH |
| DEP-046-04-021 | DOWNSTREAM | INTERFACE | UNKNOWN | VRU suction header (packing vent destination) | MEDIUM |
| DEP-046-04-022 | DOWNSTREAM | INTERFACE | UNKNOWN | Produced water tank (stage-1 scrubber liquid destination) | MEDIUM |

## Run Notes

- **Run date:** 2026-05-25
- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **DECOMPOSITION_PATH (invoker parameter):** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/GATE-07_Final_Published_2026-05-24/` — path does not exist as a directory. Resolved to canonical gate snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — confirmed present and used for anchor validation.
- **SOURCE_DOCS (AUTO):** Scanned deliverable folder. Candidate documents used:
  - ANCHOR_DOC: `Datasheet.md` (contains identification, parent package ID, scope item coverage)
  - EXECUTION_DOC_ORDER: `Procedure.md` (primary), `Guidance.md`, `Specification.md`
  - Supporting: `_CONTEXT.md` (identity, scope item and objective lists)
  - `_REFERENCES.md` consulted for document pointer resolution
- **Anchor validation:** DEL-046-04 confirmed in DELIVERABLE_REGISTER.csv; PKG-046 confirmed in PACKAGE_REGISTER.csv; SOW-0047 through SOW-0050 and OBJ-001 through OBJ-010 accepted as stated — SOW IDs not independently confirmed in SCOPE_LEDGER.csv but are EXPLICIT in _CONTEXT.md and Datasheet.md (FACT).
- **DEP-046-04-015 / DEP-046-04-016:** Procedure.md marks DEL-046-01 and DEL-046-02 as "conceptual upstream — treat as ASSUMPTION until declared." Confidence set MEDIUM; these are information-flow prerequisites (RFQ/vendor engineering cannot proceed without Scope of Work and Package Datasheet).
- **DEP-046-04-019:** Disposal well pressure from Tourmaline is a named external input blocking design freeze; no deliverable ID available in decomposition — TargetType=EXTERNAL.
- **DEP-046-04-020:** Conflict Table rulings C-1, C-2, C-3 are gating prerequisites per Procedure.md §Prerequisites; human rulings TBD per Guidance.md Conflict Table.
- **DEP-046-04-021 / DEP-046-04-022:** VRU suction header and produced water tank are facility-system interfaces explicitly named in Specification.md; no matching deliverable ID found in decomposition — TargetType=UNKNOWN. EPC Integrator is responsible for these tie-ins per PKG-046 boundary.
- **Tree x DAG integrity:** One IMPLEMENTS_NODE row (DEP-046-04-001) — parent anchor present. No FLOATING_NODE warning. No AMBIGUOUS_ANCHOR warning.
- **Binary source not read:** `26020-Package_Requirements.docx` and `26020-01-PT-RFQ-12-001_Acid Gas Compressor.docx` are binary / not locally accessible; no dependency rows extracted from these. [WARNING] BINARY_SOURCES_SKIPPED — review if text-readable extract becomes available.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 22 |
| RETIRED | 0 |

| DependencyClass | ACTIVE count |
|---|---|
| ANCHOR | 14 |
| EXECUTION | 8 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 22 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full two-pass dependency extraction (dependency-extract skill, MODE=UPDATE, STRICTNESS=CONSERVATIVE). Created Dependencies.csv v3.1 with 22 rows (14 ANCHOR, 8 EXECUTION), all ACTIVE. Decomposition validated at GATE-07_Final_Published_2026-05-24. Binary sources skipped. No FLOATING_NODE; no AMBIGUOUS_ANCHOR.
