# Dependencies: DEL-035-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (Dependencies.csv v3.1)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register; this file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

---

## Extracted Dependency Register

**Total ACTIVE rows:** 25
**Total RETIRED rows:** 0

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | SatisfactionStatus | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| DEP-035-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0036 | 13.8kV SWITCHGEAR ELECTRICAL BUILDING (810-1) — Scope Ledger Node | SATISFIED | HIGH |
| DEP-035-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | Provide the 04-25 Deepcut facility scope | SATISFIED | HIGH |
| DEP-035-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Execute each electrical and mechanical equipment package as a vendor-owned package | SATISFIED | HIGH |
| DEP-035-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Provide and integrate the facility electrical power basis | SATISFIED | HIGH |
| DEP-035-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Provide and integrate controls instrumentation and communications | SATISFIED | HIGH |
| DEP-035-02-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | Provide and integrate shared utilities and ancillary support systems | SATISFIED | HIGH |
| DEP-035-02-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Provide civil structural site buildings foundations and construction support | SATISFIED | HIGH |
| DEP-035-02-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Carry sour-service safety relief fire/gas shutdown environmental and regulatory requirements | SATISFIED | HIGH |
| DEP-035-02-009 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Maintain operability maintainability vendor-documentation commissioning turnover and open-item closure evidence | SATISFIED | HIGH |
| DEP-035-02-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-035-01_scope-of-work | Scope of Work — PKG-035 | TBD | HIGH |
| DEP-035-02-011 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-035-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package — PKG-035 | TBD | HIGH |
| DEP-035-02-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-A5EF521315 | Electrical Power Interface Fact | TBD | HIGH |
| DEP-035-02-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-C11BBF56CD | Grounding / Bonding Interface Fact | TBD | HIGH |
| DEP-035-02-014 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-9214AEAF28 | I&C / Control Cabling Interface Fact | TBD | HIGH |
| DEP-035-02-015 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-00317770B3 | Communications / Network Interface Fact | TBD | HIGH |
| DEP-035-02-016 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-73CF283A27 | Building HVAC / Services Interface Fact | TBD | HIGH |
| DEP-035-02-017 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-C00E60F032 | Fire & Gas / Safety Systems Interface Fact | TBD | HIGH |
| DEP-035-02-018 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-A3B2DADC44 | Maintenance Access Interface Fact | TBD | HIGH |
| DEP-035-02-019 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-A5DBFBF436 | Structural / Foundations / Supports Interface Fact | TBD | HIGH |
| DEP-035-02-020 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-589CAC7BC6 | Grading / Site Drainage / Spill Containment Interface Fact | TBD | HIGH |
| DEP-035-02-021 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-C8A7133D59 | Utility Piping Interface Fact | TBD | HIGH |
| DEP-035-02-022 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-231DB0CBFA | Drain / Containment Interface Fact | TBD | HIGH |
| DEP-035-02-023 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-EB2FA7BDE6 | Area / Exterior Lighting Interface Fact | TBD | HIGH |
| DEP-035-02-024 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | EXTERNAL | — | BC Hydro 25 kV Utility Supply (TBC) | PENDING | MEDIUM |
| DEP-035-02-025 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | Relay Coordination and Arc-Flash Study (TBD) | PENDING | MEDIUM |

---

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 25 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| SATISFIED | 9 |
| TBD | 14 |
| PENDING | 2 |

**ANCHOR rows (ACTIVE):** 9 (1 IMPLEMENTS_NODE + 8 TRACES_TO_REQUIREMENT)
**EXECUTION rows (ACTIVE):** 16

---

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned `Datasheet.md` as primary source (ANCHOR_DOC by heuristic match on "datasheet"). Secondary sources: `DELIVERABLE_REGISTER.csv`, `SCOPE_LEDGER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`, `INTERFACE_REGISTER.csv` (all from decomposition snapshot).
- **ANCHOR_DOC:** `Datasheet.md` (chosen by DOC_ROLE_MAP DEFAULT heuristic; filename contains "datasheet").
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — used for anchor validation and label resolution. All anchors validated against snapshot.
- **Parent anchor (IMPLEMENTS_NODE):** SOW-0036 — confirmed in SCOPE_LEDGER.csv; DEL-035-02_package-datasheet is explicitly listed in SOW-0036 deliverable set.
- **Objective traces:** 8 objectives (OBJ-001, OBJ-004 through OBJ-010) confirmed in OBJECTIVE_DELIVERABLE_MAP.csv.
- **Interface facts:** 12 interface IDs named explicitly in `Datasheet.md` Conditions table; all 12 emitted as EXECUTION/INTERFACE/UPSTREAM rows.
- **Execution edges:** DEL-035-01 (Scope of Work) is upstream prerequisite per decomposition narrative; DEL-035-04 (Vendor Engineered Equipment Package) is explicit downstream consumer per decomposition.
- **BC Hydro constraint:** Utility supply voltage confirmed TBC in source (`Datasheet.md`); emitted as PENDING/CONSTRAINT/EXTERNAL/MEDIUM confidence.
- **Relay coordination / arc-flash study:** Explicitly TBD in `Datasheet.md` Construction section; emitted as PENDING/PREREQUISITE/DOCUMENT/MEDIUM confidence.
- **No `_REFERENCES.md` TargetLocation resolution performed:** `_REFERENCES.md` documents the decomposition root only; no additional document pointers were needed beyond what was accessible.
- **CONSUMER_CONTEXT=NONE:** `EstimateImpactClass` and `ConsumerHint` extension columns not populated.

---

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract UPDATE run; MODE=UPDATE STRICTNESS=CONSERVATIVE CONSUMER_CONTEXT=NONE; decomposition GATE-07_Final_Published_2026-05-24 used; 25 ACTIVE rows written (9 ANCHOR + 16 EXECUTION); schema validation VALID (29 columns, 25 rows); no RETIRED rows; no warnings.
