# Dependencies: DEL-075-05_vendor-document-turnover-package — Vendor Document Turnover Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Register schema: v3.1 | Total rows: 9 | ACTIVE: 9 | RETIRED: 0

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetID / TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-075-05-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-075 — Cryogenic Unit (Deepcut) | HIGH | ACTIVE |
| DEP-075-05-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0063 | HIGH | ACTIVE |
| DEP-075-05-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0064 | HIGH | ACTIVE |
| DEP-075-05-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0065 | HIGH | ACTIVE |
| DEP-075-05-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0066 | HIGH | ACTIVE |
| DEP-075-05-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-075-01_scope-of-work | HIGH | ACTIVE |
| DEP-075-05-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-075-02_package-datasheet | HIGH | ACTIVE |
| DEP-075-05-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-075-04_vendor-engineered-equipment-package | HIGH | ACTIVE |
| DEP-075-05-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-075-06_epc-vendor-package-review-and-acceptance | HIGH | ACTIVE |

### ANCHOR rows (5)

- **DEP-075-05-001** — IMPLEMENTS_NODE → PKG-075: parent package anchor; confirmed via DELIVERABLE_REGISTER.csv row 280 and PACKAGE_REGISTER.csv row 52.
- **DEP-075-05-002** — TRACES_TO_REQUIREMENT → SOW-0063: scope item confirmed in SCOPE_LEDGER.csv and DELIVERABLE_REGISTER.csv.
- **DEP-075-05-003** — TRACES_TO_REQUIREMENT → SOW-0064: scope item confirmed in SCOPE_LEDGER.csv and DELIVERABLE_REGISTER.csv.
- **DEP-075-05-004** — TRACES_TO_REQUIREMENT → SOW-0065: scope item confirmed in SCOPE_LEDGER.csv and DELIVERABLE_REGISTER.csv.
- **DEP-075-05-005** — TRACES_TO_REQUIREMENT → SOW-0066: scope item confirmed in SCOPE_LEDGER.csv and DELIVERABLE_REGISTER.csv.

### EXECUTION rows (4)

- **DEP-075-05-006** — UPSTREAM PREREQUISITE ← DEL-075-01 (Scope of Work): EPC scope of work defines what vendor must engineer and document; Procedure.md Prerequisites explicit.
- **DEP-075-05-007** — UPSTREAM PREREQUISITE ← DEL-075-02 (Package Datasheet): technical handoff basis (interface requirements, vendor engineering criteria); Procedure.md Prerequisites explicit.
- **DEP-075-05-008** — UPSTREAM PREREQUISITE ← DEL-075-04 (Vendor Engineered Equipment Package): physical package basis for all turnover records (as-builts, FAT reports, MTRs, manufacturing records); Procedure.md Prerequisites and Specification Out of scope explicit.
- **DEP-075-05-009** — DOWNSTREAM HANDOVER → DEL-075-06 (EPC Vendor Package Review and Acceptance): completed vendor document set is handed to DEL-075-06 for EPC Integrator review and acceptance; Procedure.md Step 6 and Datasheet Conditions explicit.

## Run Notes

- **Run date:** 2026-05-25
- **Mode:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; sources used: `Datasheet.md` (ANCHOR_DOC — contains Identification/WBS/SOW fields), `Specification.md`, `Procedure.md`, `Guidance.md`
- **DOC_ROLE_MAP:** DEFAULT — `Datasheet.md` matched as ANCHOR_DOC (contains "datasheet"); `Specification.md`, `Procedure.md`, `Guidance.md` used as EXECUTION_DOCS
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — used to validate anchors, resolve canonical labels, and confirm sibling deliverable IDs DEL-075-01 through DEL-075-06
- **DECOMPOSITION_STATUS:** Found and used for anchor/target validation. GATE-07_Final_Published_2026-05-24 confirmed in `_REFERENCES.md`.
- **ANCHOR_DOC selected:** `Datasheet.md` — contains explicit ParentPackageID and Covers Scope Items fields.
- **EXECUTION_DOC_ORDER:** `Procedure.md` (primary; contains explicit prerequisite and handover statements), `Specification.md`, `Guidance.md`

**Integrity checks:**
- Parent anchor (IMPLEMENTS_NODE) count: 1 — PASS
- DependencyID uniqueness: all 9 IDs are unique — PASS
- All ACTIVE rows have EvidenceFile + SourceRef — PASS
- No targets invented; all deliverable targets resolved via DELIVERABLE_REGISTER.csv; SOW targets confirmed in SCOPE_LEDGER.csv

**Exclusion notes (CONSERVATIVE mode):**
- Objective associations (OBJ-001, OBJ-003–010) not extracted as ANCHOR rows because Datasheet.md and DELIVERABLE_REGISTER.csv mark these as ASSUMPTION (package-grouping heuristic); they carry insufficient evidence for CONSERVATIVE extraction. Noted as ASSUMPTION in HRR-075-05-004.
- No edges emitted for DEL-075-03 (Construction Work Package): Specification.md states it is out of scope but does not explicitly state an information or artifact flow from it to this deliverable. Excluded per information-flow-only rule.
- No edges emitted for "coordination" or scheduling relationships mentioned in Guidance.md trade-offs section.

## Lifecycle Summary

| Metric | Count |
|---|---|
| Total rows | 9 |
| ACTIVE | 9 |
| RETIRED | 0 |
| ANCHOR / IMPLEMENTS_NODE | 1 |
| ANCHOR / TRACES_TO_REQUIREMENT | 4 |
| EXECUTION / UPSTREAM PREREQUISITE | 2 |
| EXECUTION / UPSTREAM PREREQUISITE (equipment) | 1 |
| EXECUTION / DOWNSTREAM HANDOVER | 1 |
| SatisfactionStatus = TBD | 9 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full two-pass extraction run (dependency-extract skill, MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE). 9 rows extracted and registered. Schema v3.1. Decomposition: GATE-07_Final_Published_2026-05-24 (used for anchor validation and target resolution). No warnings. Status: VALID.
