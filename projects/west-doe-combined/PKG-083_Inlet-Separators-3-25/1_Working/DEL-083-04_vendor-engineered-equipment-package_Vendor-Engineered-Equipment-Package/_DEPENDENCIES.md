# Dependencies: DEL-083-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract run completed 2026-05-26)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1 schema); this file is the human-readable view.

---

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

---

## Extracted Dependency Register

**Total ACTIVE rows:** 13
**Total RETIRED rows:** 0

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetID / Name | Confidence | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-083-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-083 — Inlet Separators 3-25 | HIGH | ACTIVE |
| DEP-083-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0123 | HIGH | ACTIVE |
| DEP-083-04-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0124 | HIGH | ACTIVE |
| DEP-083-04-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0125 | HIGH | ACTIVE |
| DEP-083-04-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0126 | HIGH | ACTIVE |
| DEP-083-04-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-083-01 — Scope of Work | HIGH | ACTIVE |
| DEP-083-04-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-083-02 — Package Datasheet | HIGH | ACTIVE |
| DEP-083-04-008 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-083-05 — Vendor Document Turnover Package | HIGH | ACTIVE |
| DEP-083-04-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-083-06 — EPC Vendor Package Review and Acceptance | HIGH | ACTIVE |
| DEP-083-04-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-083-03 — Construction Work Package | HIGH | ACTIVE |
| DEP-083-04-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | EPC Integrator — building-extent ruling | HIGH | ACTIVE |
| DEP-083-04-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | EXTERNAL | 04-25 Facilities — instrument-air/electrical feeds | MEDIUM | ACTIVE |
| DEP-083-04-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | EXTERNAL | EPC Integrator — inlet-temperature reconciliation ruling | HIGH | ACTIVE |

**ANCHOR rows:** 5 (1 IMPLEMENTS_NODE + 4 TRACES_TO_REQUIREMENT)
**EXECUTION rows:** 8 (2 UPSTREAM PREREQUISITE; 2 DOWNSTREAM HANDOVER/ENABLES; 3 UPSTREAM INTERFACE/CONSTRAINT + 1 DOWNSTREAM ENABLES)

---

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 13 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 13 |

---

## Run Notes

**Run date:** 2026-05-26
**SCOPE:** DEL-083-04
**MODE:** UPDATE
**STRICTNESS:** CONSERVATIVE
**CONSUMER_CONTEXT:** NONE

**Defaults applied:**
- `SOURCE_DOCS`: AUTO — scanned all files in deliverable folder: `Datasheet.md`, `Guidance.md`, `Procedure.md`, `Specification.md`, `_CONTEXT.md`, `_REFERENCES.md`
- `DOC_ROLE_MAP`: DEFAULT — ANCHOR_DOC heuristic matched `Datasheet.md` (contains "datasheet"); EXECUTION_DOCs: `Procedure.md`, `Guidance.md`, `Specification.md`
- `ANCHOR_DOC`: `Datasheet.md` (highest-confidence match for ANCHOR pass)
- `EXECUTION_DOC_ORDER`: `Procedure.md` (primary workflow), `Guidance.md` (principles/considerations), `Specification.md` (requirements)

**DECOMPOSITION_PATH resolution:**
- Supplied path `GATE-07_Final_Published_2026-05-24` did not exist at the exact location provided in the brief (`/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/GATE-07_Final_Published_2026-05-24/`).
- Resolved via `_REFERENCES.md` (Authoritative Decomposition Basis section) to: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PROJECT_DECOMP.md`
- DELIVERABLE_REGISTER.csv at same gate snapshot used to validate all anchor and target IDs.
- **Non-blocking.** Path recorded here per skill contract.

**Tree x DAG integrity:**
- Parent anchor (IMPLEMENTS_NODE): 1 row — `[OK]`
- No FLOATING_NODE warning.
- No AMBIGUOUS_ANCHOR warning.

**MISSING_DECOMPOSITION:** Not applicable — decomposition resolved successfully.

**Source notes:**
- `26020-Package_Requirements.docx` (package heading 36) is a binary file not extracted; referenced in Specification.md Standards table as `location TBD`. No dependency rows emitted solely from this reference.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` is the primary technical source. Evidence citations from Datasheet.md, Procedure.md, Guidance.md, and Specification.md all trace to DBM line references. Dependency rows cite the deliverable document that stated the dependency signal, not the raw DBM directly.
- DEP-083-04-011 (building-extent EPC ruling) and DEP-083-04-013 (inlet-temperature reconciliation) are TargetType=EXTERNAL because no distinct registered deliverable was identified for these EPC ruling artifacts in the decomposition. If a specific EPC deliverable is later identified, rows should be updated.

---

## Run History

| Date | Mode | Strictness | Decomposition | Warnings | ACTIVE Count |
|---|---|---|---|---|---|
| 2026-05-24 | — | — | — | Initialized dependency view in DECLARED mode (PREPARATION) | 0 |
| 2026-05-26 | UPDATE | CONSERVATIVE | Resolved to GATE-07_Final_Published_2026-05-24 (via _REFERENCES.md) | None | 13 |
