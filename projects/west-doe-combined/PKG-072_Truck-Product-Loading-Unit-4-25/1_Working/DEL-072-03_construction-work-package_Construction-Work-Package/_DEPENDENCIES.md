# Dependencies: DEL-072-03_construction-work-package — Construction Work Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` (v3.1) is the canonical register; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

31 rows extracted (ACTIVE). 0 rows RETIRED.

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-072-03-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | — | PKG-072 — Truck Product Loading Unit 4-25 | HIGH | ACTIVE |
| DEP-072-03-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0245 | SOW-0245 | HIGH | ACTIVE |
| DEP-072-03-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0246 | SOW-0246 | HIGH | ACTIVE |
| DEP-072-03-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0247 | SOW-0247 | HIGH | ACTIVE |
| DEP-072-03-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0248 | SOW-0248 | HIGH | ACTIVE |
| DEP-072-03-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-072-01_scope-of-work | Scope of Work (DEL-072-01) | HIGH | ACTIVE |
| DEP-072-03-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-072-02_package-datasheet | Package Datasheet (DEL-072-02) | MEDIUM | ACTIVE |
| DEP-072-03-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-072-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package (DEL-072-04) | HIGH | ACTIVE |
| DEP-072-03-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-072-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance (DEL-072-06) | MEDIUM | ACTIVE |
| DEP-072-03-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | PRQ-013 | PRQ-013 Logistics/Shipping Plan | HIGH | ACTIVE |
| DEP-072-03-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | STR-006 | STR-006 Foundation Drawings | HIGH | ACTIVE |
| DEP-072-03-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | STR-013 | STR-013 Anchor Bolt / Embedment Drawings | HIGH | ACTIVE |
| DEP-072-03-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | MEC-017 | MEC-017 Installation/Setting Drawings | HIGH | ACTIVE |
| DEP-072-03-014 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | MEC-018 | MEC-018 Lifting/Handling Study | HIGH | ACTIVE |
| DEP-072-03-015 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | PIP-004 | PIP-004 Tie-In List / Tie-In Scope Sheets | HIGH | ACTIVE |
| DEP-072-03-016 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | PIP-024 | PIP-024 Hydrotest / Pressure Test Packages | HIGH | ACTIVE |
| DEP-072-03-017 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | PIP-025 | PIP-025 Flushing/Cleaning/Drying Procedure | HIGH | ACTIVE |
| DEP-072-03-018 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | ELE-027 | ELE-027 Electrical Installation Details | HIGH | ACTIVE |
| DEP-072-03-019 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | ELE-028 | ELE-028 Interconnection / Connection Diagrams | HIGH | ACTIVE |
| DEP-072-03-020 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | INS-005 | INS-005 Instrument Location Plans | HIGH | ACTIVE |
| DEP-072-03-021 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | INS-006 | INS-006 Hook-Up Drawings | HIGH | ACTIVE |
| DEP-072-03-022 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | INS-009 | INS-009 Wiring/Termination Diagrams | HIGH | ACTIVE |
| DEP-072-03-023 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | INS-011 | INS-011 Cable Schedule | HIGH | ACTIVE |
| DEP-072-03-024 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | TSF-004 | TSF-004 Fire and Gas Detector Layout Drawings | HIGH | ACTIVE |
| DEP-072-03-025 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | CIV-003 | CIV-003 Grading Plan | HIGH | ACTIVE |
| DEP-072-03-026 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | CIV-004 | CIV-004 Drainage/Stormwater Management Report | HIGH | ACTIVE |
| DEP-072-03-027 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | CTL-006 | CTL-006 I/O List | HIGH | ACTIVE |
| DEP-072-03-028 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | CTL-026 | CTL-026 Package Vendor Interface Specification | HIGH | ACTIVE |
| DEP-072-03-029 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | EXTERNAL | LACT-DECISION | LACT Scope/Ownership Decision | HIGH | ACTIVE |
| DEP-072-03-030 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | EXTERNAL | PERMIT-TRUCK-RACK | Truck Rack Permit Amendment | HIGH | ACTIVE |
| DEP-072-03-031 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | QLT-013 | QLT-013 Material Test Reports | HIGH | ACTIVE |

## Run Notes

- **Run date:** 2026-05-25
- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **Source documents scanned (AUTO):** Procedure.md, Specification.md, Guidance.md, Datasheet.md, _CONTEXT.md
- **Anchor doc:** Datasheet.md (role: ANCHOR_DOC — contains identification table, parent package, scope items)
- **Execution docs (in order):** Procedure.md (primary — explicit field execution sequence and prerequisites), Specification.md (requirements), Guidance.md (principles, conflicts, constraints)
- **Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv`
  - GATE-07 snapshot confirmed present and used to validate parent anchor (PKG-072) and sibling deliverable IDs (DEL-072-01 through DEL-072-06).
- **_REFERENCES.md:** No deliverable-specific source slices present; document pointers remain `location TBD` for vendor deliverable refs.
- **Pass 1 (ANCHOR):** 1 parent anchor (IMPLEMENTS_NODE → PKG-072), 4 trace anchors (SOW-0245 through SOW-0248).
- **Pass 2 (EXECUTION):** 26 execution edges — 3 DELIVERABLE targets (DEL-072-01, -02, -04 upstream; DEL-072-06 downstream), 21 DOCUMENT targets (vendor engineering deliverables named explicitly in Procedure.md / Specification.md), 2 EXTERNAL constraint targets (LACT decision, truck-rack permit).
- **Tree x DAG integrity:** 1 parent anchor found (IMPLEMENTS_NODE). No FLOATING_NODE warning. No AMBIGUOUS_ANCHOR warning.
- **STRICTNESS=CONSERVATIVE:** Only explicit references emitted. Vendor engineering deliverable rows (STR-006 etc.) reflect explicit naming in Procedure.md prerequisites and Specification.md requirements; each has EvidenceFile + SourceRef.
- **TargetLocation for DOCUMENT rows:** `location TBD` — source files are not locally accessible text (binary `.docx`/`.xlsx`); vendor deliverable ref IDs preserved in TargetRefID.
- **Note on GATE-07 path mismatch:** `_CONTEXT.md` and `_REFERENCES.md` reference `GATE-07_Final_Published_2026-05-24` under `_Decomposition/PROJECT_DECOMP/_GateSnapshots/`. This path is confirmed to exist. The `DECOMPOSITION_PATH` parameter referenced `GATE-07_Final_Published_2026-05-24` under the run root directly; that top-level path did not exist — resolved by using the confirmed snapshot under `_Decomposition/`.

## Lifecycle Summary

- **ACTIVE rows:** 31
- **RETIRED rows:** 0
- **ANCHOR / IMPLEMENTS_NODE:** 1
- **ANCHOR / TRACES_TO_REQUIREMENT:** 4
- **EXECUTION / UPSTREAM / PREREQUISITE (DELIVERABLE):** 3
- **EXECUTION / UPSTREAM / PREREQUISITE (DOCUMENT):** 21
- **EXECUTION / UPSTREAM / CONSTRAINT (EXTERNAL):** 2
- **EXECUTION / DOWNSTREAM / HANDOVER (DELIVERABLE):** 1
- **Open constraints (SatisfactionStatus=PENDING):** 2 (LACT decision DEP-072-03-029, truck-rack permit DEP-072-03-030)
- **SatisfactionStatus=TBD:** 29 rows
- **SatisfactionStatus=SATISFIED:** 0 rows

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full two-pass extraction run (dependency-extract skill, UPDATE mode, CONSERVATIVE strictness). 31 ACTIVE rows written. Dependencies.csv v3.1 created. Validated against GATE-07 decomposition snapshot.
