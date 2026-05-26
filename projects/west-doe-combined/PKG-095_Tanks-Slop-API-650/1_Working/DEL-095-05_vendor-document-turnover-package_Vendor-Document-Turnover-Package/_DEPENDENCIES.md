# Dependencies: DEL-095-05_vendor-document-turnover-package — Vendor Document Turnover Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-26)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1 schema); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` produced by `TASK + dependency-extract` on 2026-05-26.

**Counts (ACTIVE):** 12 rows total — 5 ANCHOR, 7 EXECUTION
- ANCHOR / IMPLEMENTS_NODE: 1
- ANCHOR / TRACES_TO_REQUIREMENT: 4
- EXECUTION / UPSTREAM / PREREQUISITE: 3 (DEL-095-01, DEL-095-02, heading-47 source doc)
- EXECUTION / UPSTREAM / CONSTRAINT: 1 (project document control basis)
- EXECUTION / UPSTREAM / INTERFACE: 1 (DEL-095-06 review findings back-reference)
- EXECUTION / UPSTREAM / PREREQUISITE (equipment): 1 (DEL-095-04 underway)
- EXECUTION / DOWNSTREAM / HANDOVER: 1 (DEL-095-06 turnover record delivery)

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-095-05-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-095 — Tanks Slop (API 650) | HIGH | ACTIVE |
| DEP-095-05-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0213 | HIGH | ACTIVE |
| DEP-095-05-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0214 | HIGH | ACTIVE |
| DEP-095-05-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0215 | HIGH | ACTIVE |
| DEP-095-05-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0216 | HIGH | ACTIVE |
| DEP-095-05-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-095-01 Scope of Work | HIGH | ACTIVE |
| DEP-095-05-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-095-02 Package Datasheet | HIGH | ACTIVE |
| DEP-095-05-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-095-04 Vendor Engineered Equipment Package | HIGH | ACTIVE |
| DEP-095-05-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-095-06 EPC Vendor Package Review and Acceptance | HIGH | ACTIVE |
| DEP-095-05-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DELIVERABLE | DEL-095-06 EPC Vendor Package Review and Acceptance | HIGH | ACTIVE |
| DEP-095-05-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | 26020-Package_Requirements.docx heading 47 | HIGH | ACTIVE |
| DEP-095-05-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | DOCUMENT | Project document control basis | MEDIUM | ACTIVE |

## Lifecycle Summary

| Dimension | Count |
|---|---|
| ACTIVE rows | 12 |
| RETIRED rows | 0 |
| ANCHOR / IMPLEMENTS_NODE (ACTIVE) | 1 |
| ANCHOR / TRACES_TO_REQUIREMENT (ACTIVE) | 4 |
| EXECUTION (ACTIVE) | 7 |
| SatisfactionStatus = TBD | 10 |
| SatisfactionStatus = PENDING | 2 |

## Run Notes

**Run:** 2026-05-26 | MODE=UPDATE | STRICTNESS=CONSERVATIVE | CONSUMER_CONTEXT=NONE

**Decomposition path resolution:**
- Brief provided `DECOMPOSITION_PATH: /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/GATE-07_Final_Published_2026-05-24/` — not found at that exact location.
- Resolved via `_REFERENCES.md` in this deliverable folder to: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
- Decomposition files confirmed at resolved path: `PROJECT_DECOMP.md`, `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `SCOPE_LEDGER.csv`.
- Resolved path recorded here per skill protocol. Non-blocking.

**Source documents scanned (AUTO):**
- `Datasheet.md` — ANCHOR_DOC (contains ParentPackageID, CoversScopeItems, SupportsObjectives; anchor-doc heuristic match)
- `Specification.md` — EXECUTION_DOC (requirements; workflow signals)
- `Procedure.md` — EXECUTION_DOC (explicit prerequisites and steps)
- `Guidance.md` — EXECUTION_DOC (context, trade-offs, boundary definitions)

**Defaults applied:**
- SOURCE_DOCS: AUTO
- DOC_ROLE_MAP: DEFAULT
- ANCHOR_DOC: Datasheet.md (auto-selected; contains explicit ParentPackageID and scope-items fields)
- EXECUTION_DOC_ORDER: Procedure.md, Specification.md, Guidance.md

**Pass 1 (Anchor — Tree):**
- Parent anchor (IMPLEMENTS_NODE → PKG-095) confirmed from PACKAGE_REGISTER.csv.
- Four scope-item trace anchors (SOW-0213..SOW-0216) confirmed from SCOPE_LEDGER.csv; all confirmed as IN-scope rows assigned to DEL-095-05.
- SupportsObjectives (OBJ-002..OBJ-010) noted but not emitted as separate rows — CONSERVATIVE posture; TargetType=REQUIREMENT trace anchors already cover the traceability adequately via SOW rows.

**Pass 2 (Execution — DAG):**
- Three deliverable prerequisites identified from Procedure §Prerequisites: DEL-095-01, DEL-095-02, DEL-095-04.
- One downstream handover to DEL-095-06 from Procedure §Steps Step 7 (explicit "attach the turnover record to DEL-095-06").
- One upstream interface from DEL-095-06 (review findings back-referenced from register status column) — bidirectional interface with DEL-095-06; two rows emitted (DOWNSTREAM handover + UPSTREAM interface) to capture both directions of information flow.
- Two document prerequisites: heading-47 source table (TBD/PENDING) and project document control basis (TBD/PENDING).

**Integrity checks:**
- Parent anchor count = 1 → OK.
- No FLOATING_NODE warning.
- No AMBIGUOUS_ANCHOR warning.

**Open items noted in sources:**
- heading-47 source slice not locally extracted (binary `26020-Package_Requirements.docx`); SatisfactionStatus=PENDING for DEP-095-05-011.
- Project document control basis not yet published; SatisfactionStatus=PENDING for DEP-095-05-012.
- Equipment tag TK-9130-2 is ASSUMPTION per SOW-0216 open items; not emitted as a dependency row (not an information-flow edge).

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-26 — Full extraction run (dependency-extract skill, MODE=UPDATE, STRICTNESS=CONSERVATIVE). 12 rows written (5 ANCHOR, 7 EXECUTION). Decomposition resolved via _REFERENCES.md. No warnings. Schema validated.
