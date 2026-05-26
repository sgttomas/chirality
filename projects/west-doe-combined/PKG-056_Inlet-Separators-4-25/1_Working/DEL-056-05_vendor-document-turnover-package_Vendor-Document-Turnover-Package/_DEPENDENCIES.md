# Dependencies: DEL-056-05_vendor-document-turnover-package — Vendor Document Turnover Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill; UPDATE run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

---

## Extracted Dependency Register

**Total ACTIVE rows:** 10
**Schema version:** v3.1

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetID / TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-056-05-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | PACKAGE | PKG-056 — Inlet Separators 4-25 | HIGH | ACTIVE |
| DEP-056-05-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0127 | HIGH | ACTIVE |
| DEP-056-05-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0128 | HIGH | ACTIVE |
| DEP-056-05-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0129 | HIGH | ACTIVE |
| DEP-056-05-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0130 | HIGH | ACTIVE |
| DEP-056-05-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-056-04 — Vendor Engineered Equipment Package | HIGH | ACTIVE |
| DEP-056-05-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-056-01 — Scope of Work | HIGH | ACTIVE |
| DEP-056-05-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-056-02 — Package Datasheet | HIGH | ACTIVE |
| DEP-056-05-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-056-06 — EPC Vendor Package Review and Acceptance | HIGH | ACTIVE |
| DEP-056-05-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | DOCUMENT | 26020-Package_Requirements.docx heading 11 | MEDIUM | ACTIVE |

---

## Run Notes

**Run timestamp:** 2026-05-25
**Mode:** UPDATE
**Strictness:** CONSERVATIVE
**Consumer context:** NONE

**Decomposition path used:**
`/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`

Note: The `DECOMPOSITION_PATH` parameter provided at invocation (`GATE-07_Final_Published_2026-05-24/` under the project root) resolved to a non-existent directory at that exact path. The correct path was identified from `_REFERENCES.md` and confirmed to exist at the path above. This path was used for all anchor validation and label resolution.

**Source documents scanned (AUTO):**
- `Datasheet.md` — ANCHOR_DOC (contains Identification / ParentPackageID / Scope Items Covered; primary anchor signal)
- `Procedure.md` — EXECUTION_DOC primary (explicit prerequisite sibling list; Step 9 handover to DEL-056-06)
- `Specification.md` — EXECUTION_DOC secondary (R2.2, R4.1 govern heading 11 constraint; R7.2 states DEL-056-06 acceptance record)
- `Guidance.md` — EXECUTION_DOC tertiary (corroborates DEL-056-06 handover; cause-and-effect interface note)

**Defaults applied:**
- `DOC_ROLE_MAP`: DEFAULT heuristic — Datasheet.md matched as ANCHOR_DOC; remaining docs treated as EXECUTION_DOC candidates
- `ANCHOR_DOC`: Datasheet.md (highest-confidence anchor signal: explicit ParentPackageID and Scope Items Covered fields)
- `EXECUTION_DOC_ORDER`: Procedure.md → Specification.md → Guidance.md

**Warnings:**
- None. Parent anchor found (DEP-056-05-001). No ambiguous anchors.
- DEP-056-05-010: `26020-Package_Requirements.docx heading 11` — TargetLocation is `location TBD`; DOCX not locally extracted to markdown. Confidence set to MEDIUM. This is a documented open item in all source documents.

**Pass 1 (ANCHOR) summary:**
- 1 IMPLEMENTS_NODE row (DEP-056-05-001): PKG-056 confirmed in PACKAGE_REGISTER.csv and DELIVERABLE_REGISTER.csv GATE-07 snapshot.
- 4 TRACES_TO_REQUIREMENT rows (DEP-056-05-002 through DEP-056-05-005): SOW-0127, SOW-0128, SOW-0129, SOW-0130 confirmed in SCOPE_LEDGER.csv GATE-07 snapshot as covering DEL-056-05.

**Pass 2 (EXECUTION) summary:**
- 3 UPSTREAM PREREQUISITE rows (DEP-056-05-006, 007, 008): DEL-056-04 (engineering outputs basis), DEL-056-01 (scope of work governing basis), DEL-056-02 (engineering handoff basis)
- 1 DOWNSTREAM HANDOVER row (DEP-056-05-009): DEL-056-06 (EPC review and acceptance; explicit in Procedure.md Step 9 and Guidance.md)
- 1 UPSTREAM CONSTRAINT row (DEP-056-05-010): `26020-Package_Requirements.docx heading 11` — TargetLocation TBD; source-required document list governing constraint

**Cause-and-effect note (not extracted as dependency — low signal / no explicit artifact transfer stated):**
Guidance.md notes that vendor cause-and-effect inputs feed a project-level C&E matrix. This relationship is noted here as context; it was not extracted as an EXECUTION row because no specific artifact transfer to a named deliverable is stated in accessible sources, only a general statement about the project-level C&E matrix. If a specific downstream deliverable consuming the C&E inputs is identified, this should be added as a DOWNSTREAM HANDOVER row.

---

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 10 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 10 |

| DependencyClass | ACTIVE count |
|---|---|
| ANCHOR | 5 |
| EXECUTION | 5 |

---

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full dependency-extract run (MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE). Created Dependencies.csv v3.1 with 10 ACTIVE rows (5 ANCHOR, 5 EXECUTION). No prior rows to retire. Schema validation: VALID. No integrity warnings.
