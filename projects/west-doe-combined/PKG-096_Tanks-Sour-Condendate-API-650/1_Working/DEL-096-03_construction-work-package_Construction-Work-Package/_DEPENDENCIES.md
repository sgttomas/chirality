# Dependencies: DEL-096-03_construction-work-package — Construction Work Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract run 2026-05-26)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1 schema, 29 columns). This file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

---

## Extracted Dependency Register

**Register:** `Dependencies.csv` — v3.1 schema — 19 rows (19 ACTIVE, 0 RETIRED)

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-096-03-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | — | PKG-096 — Tanks Sour Condensate (API 650) | HIGH | ACTIVE |
| DEP-096-03-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0217 | SOW-0217 | HIGH | ACTIVE |
| DEP-096-03-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0218 | SOW-0218 | HIGH | ACTIVE |
| DEP-096-03-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0219 | SOW-0219 | HIGH | ACTIVE |
| DEP-096-03-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0220 | SOW-0220 | HIGH | ACTIVE |
| DEP-096-03-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | 26020-Package_Requirements.docx-H1-48 | 26020-Package_Requirements.docx H1 #48 | HIGH | ACTIVE |
| DEP-096-03-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | INTERFACE_REGISTER.csv-PKG-096 | INTERFACE_REGISTER.csv entries for PKG-096 | HIGH | ACTIVE |
| DEP-096-03-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | OBJECTIVE_DELIVERABLE_MAP.csv-DEL-096-03 | OBJECTIVE_DELIVERABLE_MAP.csv row(s) for DEL-096-03 | MEDIUM | ACTIVE |
| DEP-096-03-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | EXTERNAL | MEC-016 | MEC-016 Equipment General Arrangement Drawing | HIGH | ACTIVE |
| DEP-096-03-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | EXTERNAL | MEC-017 | MEC-017 Equipment Installation / Setting Drawings | HIGH | ACTIVE |
| DEP-096-03-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | EXTERNAL | MEC-018 | MEC-018 Lifting / Handling Study | HIGH | ACTIVE |
| DEP-096-03-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | EXTERNAL | PIP-004 | PIP-004 Tie-In List / Tie-In Scope Sheets | HIGH | ACTIVE |
| DEP-096-03-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | EXTERNAL | PIP-007 | PIP-007 Piping Plans and Sections | HIGH | ACTIVE |
| DEP-096-03-014 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | EXTERNAL | PIP-024 | PIP-024 Hydrotest / Pressure Test Packages | HIGH | ACTIVE |
| DEP-096-03-015 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | EXTERNAL | MEC-025 | MEC-025 Mechanical Equipment IOM Manual | HIGH | ACTIVE |
| DEP-096-03-016 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | EXTERNAL | QLT-003 | QLT-003 Inspection and Test Plan (ITP) | HIGH | ACTIVE |
| DEP-096-03-017 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DELIVERABLE | DEL-096-01_scope-of-work | Scope of Work (DEL-096-01) | HIGH | ACTIVE |
| DEP-096-03-018 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DELIVERABLE | DEL-096-02_package-datasheet | Package Datasheet (DEL-096-02) | HIGH | ACTIVE |
| DEP-096-03-019 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-096-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package (DEL-096-04) | HIGH | ACTIVE |

**Counts:** 5 ANCHOR rows (1 IMPLEMENTS_NODE + 4 TRACES_TO_REQUIREMENT), 14 EXECUTION rows (all UPSTREAM). 0 DOWNSTREAM edges extracted (no explicit downstream consumers stated in source documents).

---

## Run Notes

**Run date:** 2026-05-26
**MODE:** UPDATE
**STRICTNESS:** CONSERVATIVE
**CONSUMER_CONTEXT:** NONE

**Defaults applied:**
- `SOURCE_DOCS`: AUTO — scanned all `.md` files in deliverable folder (Procedure.md, Datasheet.md, Specification.md, Guidance.md, _CONTEXT.md, _REFERENCES.md).
- `ANCHOR_DOC`: AUTO — Datasheet.md selected (contains `datasheet` in filename; highest-confidence anchor signal per DOC_ROLE_MAP DEFAULT).
- `EXECUTION_DOC_ORDER`: AUTO — Procedure.md (primary), then Specification.md, Guidance.md.
- `DOC_ROLE_MAP`: DEFAULT.

**Decomposition path resolution:**
- Provided `DECOMPOSITION_PATH`: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/GATE-07_Final_Published_2026-05-24/` — path does NOT exist at that exact location.
- Resolved via `_REFERENCES.md` "Authoritative Decomposition Basis" entry: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
- Decomposition found and read at resolved path. Anchor validation performed. No MISSING_DECOMPOSITION warning applies.

**Integrity checks:**
- Parent anchor (IMPLEMENTS_NODE) count: 1 — OK. No FLOATING_NODE or AMBIGUOUS_ANCHOR warnings.
- All ACTIVE rows have `EvidenceFile` and `SourceRef` populated.
- `DependencyID` values are unique within the register.
- All enum values are canonical v3.1 write-form.
- No DOWNSTREAM edges extracted: no source document states an explicit information/artifact transfer FROM this deliverable to another named deliverable. The construction output artifacts (turnover dossier, ITRs, signed checklists) are turnover deliverables documented in the deliverable but no explicit downstream consumer deliverable ID is named in source.

**Schema validation:** VALID (29 required columns; 19 data rows). Validated by `python3 tools/validation/validate_dependencies_schema.py`.

---

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 19 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 5 (ANCHOR rows) |
| PENDING | 14 (EXECUTION rows) |

---

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-26 — UPDATE run by TASK + dependency-extract (MODE=UPDATE; STRICTNESS=CONSERVATIVE; CONSUMER_CONTEXT=NONE). Decomposition resolved to GATE-07 snapshot. 19 rows extracted (5 ANCHOR + 14 EXECUTION). Schema VALID. No warnings.
