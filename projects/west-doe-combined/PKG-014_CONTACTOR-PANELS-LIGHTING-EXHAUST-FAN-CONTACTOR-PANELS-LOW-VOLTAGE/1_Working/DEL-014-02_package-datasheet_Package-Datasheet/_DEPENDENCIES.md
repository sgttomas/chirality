# Dependencies: DEL-014-02_package-datasheet — Package Datasheet

**Coordination Mode:** EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register; this file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Total rows: 18 | ACTIVE: 18 | RETIRED: 0

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-014-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0015 | Scope decision SOW-0015 — CONTACTOR PANELS LOW VOLTAGE (WBS 02) | HIGH | ACTIVE |
| DEP-014-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-002 | Project Objective OBJ-002 — 03-25 compressor station and liquids hub scope | HIGH | ACTIVE |
| DEP-014-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Project Objective OBJ-004 — Vendor-owned package execution with EPC integration review | HIGH | ACTIVE |
| DEP-014-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Project Objective OBJ-005 — Facility electrical power basis and electrical infrastructure | HIGH | ACTIVE |
| DEP-014-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Project Objective OBJ-006 — Controls instrumentation communications and package control interfaces | HIGH | ACTIVE |
| DEP-014-02-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Project Objective OBJ-008 — Civil structural site buildings and construction-support scope | HIGH | ACTIVE |
| DEP-014-02-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 — Safety relief flare regulatory and codes requirements | HIGH | ACTIVE |
| DEP-014-02-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 — Operability maintainability vendor documentation and turnover | HIGH | ACTIVE |
| DEP-014-02-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-014-01_scope-of-work | Scope of Work — PKG-014 | HIGH | ACTIVE |
| DEP-014-02-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-014-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package — PKG-014 | HIGH | ACTIVE |
| DEP-014-02-011 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-014-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance — PKG-014 | HIGH | ACTIVE |
| DEP-014-02-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-78CF31138D | Interface IFC-78CF31138D — Electrical Power (PKG-014) | MEDIUM | ACTIVE |
| DEP-014-02-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-31C88BB424 | Interface IFC-31C88BB424 — Grounding / Bonding (PKG-014) | MEDIUM | ACTIVE |
| DEP-014-02-014 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-EF784327FA | Interface IFC-EF784327FA — Area / Exterior Lighting (PKG-014) | MEDIUM | ACTIVE |
| DEP-014-02-015 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-C715E9AA3E | Interface IFC-C715E9AA3E — I&C / Control Cabling (PKG-014) | MEDIUM | ACTIVE |
| DEP-014-02-016 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-2D60238809 | Interface IFC-2D60238809 — Communications / Network (PKG-014) | MEDIUM | ACTIVE |
| DEP-014-02-017 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-52B07B0D36 | Interface IFC-52B07B0D36 — Maintenance Access (PKG-014) | MEDIUM | ACTIVE |
| DEP-014-02-018 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-53646D26A1 | Interface IFC-53646D26A1 — Structural / Foundations / Supports (PKG-014) | MEDIUM | ACTIVE |

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 18 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 18 |

| DependencyClass | ACTIVE |
|---|---|
| ANCHOR | 8 |
| EXECUTION | 10 |

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; primary anchor doc identified as `Datasheet.md` (filename contains `datasheet`); execution docs: `_CONTEXT.md`, `GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv`, `GATE-07_Final_Published_2026-05-24/SCOPE_LEDGER.csv`.
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — resolved from `_CONTEXT.md` Decomposition Reference field. Confirmed accessible; used for anchor validation and label resolution.
- **RUN_ROOT:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined`
- Pass 1 (ANCHOR): SOW-0015 confirmed in SCOPE_LEDGER.csv as parent node. Seven objective traces (OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010) confirmed in DELIVERABLE_REGISTER.csv row DEL-014-02.
- Pass 2 (EXECUTION): DEL-014-01 identified as upstream PREREQUISITE (Scope of Work precedes Package Datasheet in mandatory EPC deliverable sequence per DELIVERABLE_REGISTER.csv). DEL-014-04 and DEL-014-06 identified as downstream HANDOVER targets (DELIVERABLE_REGISTER.csv Notes columns explicitly state Package Datasheet as input/baseline). Seven interface register facts (IFC-*) cited explicitly in Datasheet.md Conditions table as required interface inputs.
- **Tree x DAG integrity:** 1 IMPLEMENTS_NODE row (DEP-014-02-001) — no FLOATING_NODE or AMBIGUOUS_ANCHOR warnings.
- No legacy enum normalization required (all values written in canonical form).

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full extraction run; dependency-extract skill; MODE=UPDATE; STRICTNESS=CONSERVATIVE; CONSUMER_CONTEXT=NONE; decomposition=GATE-07_Final_Published_2026-05-24 (confirmed); 18 rows created (8 ANCHOR, 10 EXECUTION); no warnings.
