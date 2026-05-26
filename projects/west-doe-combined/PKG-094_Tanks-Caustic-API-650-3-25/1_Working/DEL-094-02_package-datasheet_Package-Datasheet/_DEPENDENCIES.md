# Dependencies: DEL-094-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** DECLARED + EXTRACTED
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` (v3.1) is authoritative structured register; this file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Extracted by `TASK + dependency-extract` on 2026-05-26. MODE=UPDATE; STRICTNESS=CONSERVATIVE; CONSUMER_CONTEXT=NONE.

**Total rows: 14 | ACTIVE: 14 | RETIRED: 0**

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-094-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-094 | Tanks Caustic (API 650) 3-25 | HIGH | ACTIVE |
| DEP-094-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0193 | Scope Item SOW-0193 | HIGH | ACTIVE |
| DEP-094-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0194 | Scope Item SOW-0194 | HIGH | ACTIVE |
| DEP-094-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0195 | Scope Item SOW-0195 | HIGH | ACTIVE |
| DEP-094-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0196 | Scope Item SOW-0196 | HIGH | ACTIVE |
| DEP-094-02-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | DBM-3-25 | 3-25 Composition and Liquids DBM | HIGH | ACTIVE |
| DEP-094-02-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | GATE-07-DECOMP | GATE-07 Final Published PROJECT_DECOMP Snapshot | HIGH | ACTIVE |
| DEP-094-02-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | RFQ-26020-PKG-46 | 26020-Package_Requirements.docx heading 46 | MEDIUM | ACTIVE |
| DEP-094-02-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-094-01_scope-of-work | Scope of Work | HIGH | ACTIVE |
| DEP-094-02-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-094-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package | HIGH | ACTIVE |
| DEP-094-02-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-94BBAEE00A | Structural / Foundations / Supports Interface | MEDIUM | ACTIVE |
| DEP-094-02-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-AFD520D296 | Relief / Flare / Vent Interface | HIGH | ACTIVE |
| DEP-094-02-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-12C92E9A0A | Process Piping Interface | HIGH | ACTIVE |
| DEP-094-02-014 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-DA053E0FE2 | Drain / Containment Interface | HIGH | ACTIVE |

**ANCHOR rows (ACTIVE): 5** — 1 IMPLEMENTS_NODE + 4 TRACES_TO_REQUIREMENT
**EXECUTION rows (ACTIVE): 9** — 4 UPSTREAM/PREREQUISITE, 4 UPSTREAM/INTERFACE, 1 DOWNSTREAM/HANDOVER

## Run Notes

- **Run date:** 2026-05-26
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SCOPE:** DEL-094-02
- **RUN_ROOT:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined`
- **DECOMPOSITION_PATH (resolved):** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`
  - Resolution note: Brief specified `GATE-07_Final_Published_2026-05-24/` under RUN_ROOT; actual location is under `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`. Resolved successfully. `_REFERENCES.md` confirms this path. Non-blocking.
- **SOURCE_DOCS (AUTO):** Datasheet.md (ANCHOR_DOC), Specification.md, Guidance.md, Procedure.md, _CONTEXT.md, _REFERENCES.md
  - ANCHOR_DOC heuristic: `Datasheet.md` matched role `datasheet` — selected as Pass 1 primary.
  - EXECUTION_DOC_ORDER: Procedure.md (contains prerequisites / workflow), Specification.md (scope exclusions, sibling relationships), Guidance.md (interface coordination), Datasheet.md (interface summary table).
- **Decomposition files read:** DELIVERABLE_REGISTER.csv, PACKAGE_REGISTER.csv, SCOPE_LEDGER.csv (GATE-07 snapshot)
- **Existing Dependencies.csv:** None found — created fresh.
- **Existing _DEPENDENCIES.md:** DECLARED-only stub — declared sections preserved; extracted sections added.
- **Tree x DAG integrity:**
  - ACTIVE IMPLEMENTS_NODE count: 1 — OK (no FLOATING_NODE, no AMBIGUOUS_ANCHOR)
  - Parent anchor validated against PACKAGE_REGISTER.csv (PKG-094 confirmed in GATE-07 snapshot)
- **Anchor label resolution:** PKG-094 label "Tanks, Caustic (API 650) 3-25" confirmed in PACKAGE_REGISTER.csv. SOW-0193–SOW-0196 confirmed in SCOPE_LEDGER.csv. All resolved at HIGH confidence.
- **Interface rows (DEP-094-02-011 through DEP-094-02-014):** Only the four interfaces explicitly cited by ID in Datasheet.md §Interface Summary or with explicit design data in the source text are emitted. The remaining five interfaces (Grounding/Bonding IFC-35E994F2DE, Area/Exterior Lighting IFC-946F48A91C, Cathodic Protection IFC-7EBC5D8325, I&C/Control Cabling IFC-15D9C87C0A, Grading/Site Drainage IFC-61D7941475) appear in the Interface Summary table but do not carry explicit information-flow evidence in the source text sufficient for CONSERVATIVE extraction as EXECUTION edges; they are not emitted per CONSERVATIVE strictness.
- **Vendor RFQ (DEP-094-02-008):** SatisfactionStatus=PENDING because the binary source (`26020-Package_Requirements.docx`) is not locally parsed; Guidance.md Conflict CONF-094-02-006 tracks resolution.
- **No FLOATING_NODE warning** — one ACTIVE IMPLEMENTS_NODE parent anchor present.
- **No MISSING_DECOMPOSITION warning** — decomposition resolved successfully.
- **No AMBIGUOUS_ANCHOR warning** — exactly one IMPLEMENTS_NODE.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 14 |
| RETIRED | 0 |
| **Total** | **14** |

| SatisfactionStatus | ACTIVE rows |
|---|---|
| TBD | 13 |
| PENDING | 1 |
| IN_PROGRESS | 0 |
| SATISFIED | 0 |
| WAIVED | 0 |
| NOT_APPLICABLE | 0 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-26 — dependency-extract UPDATE run (CONSERVATIVE, CONSUMER_CONTEXT=NONE). Created Dependencies.csv v3.1 with 14 ACTIVE rows (5 ANCHOR, 9 EXECUTION). Decomposition resolved to GATE-07_Final_Published_2026-05-24. No integrity warnings. Validator: python3 tools/validation/validate_dependencies_schema.py — PASS.
