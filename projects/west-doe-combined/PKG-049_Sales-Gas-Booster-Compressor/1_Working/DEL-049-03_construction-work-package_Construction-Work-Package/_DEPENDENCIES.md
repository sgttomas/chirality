# Dependencies: DEL-049-03_construction-work-package — Construction Work Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract run completed)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

**Total ACTIVE rows:** 16
**ANCHOR rows (ACTIVE):** 5 (1 × IMPLEMENTS_NODE, 4 × TRACES_TO_REQUIREMENT)
**EXECUTION rows (ACTIVE):** 11
**RETIRED rows:** 0

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetID / TargetName | Confidence |
|---|---|---|---|---|---|---|---|
| DEP-049-03-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-049 Sales Gas Booster Compressor | HIGH |
| DEP-049-03-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0169 | HIGH |
| DEP-049-03-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0170 | HIGH |
| DEP-049-03-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0171 | HIGH |
| DEP-049-03-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0172 | HIGH |
| DEP-049-03-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-049-01_scope-of-work | MEDIUM |
| DEP-049-03-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-049-02_package-datasheet | MEDIUM |
| DEP-049-03-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-049-04_vendor-engineered-equipment-package | HIGH |
| DEP-049-03-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-049-05_vendor-document-turnover-package | HIGH |
| DEP-049-03-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-049-06_epc-vendor-package-review-and-acceptance | MEDIUM |
| DEP-049-03-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | QLT-020 Inspection Release Certificate | HIGH |
| DEP-049-03-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | REG-022 Pressure Equipment Registration Package | HIGH |
| DEP-049-03-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | PIP-024 Hydrotest / Pressure Test Packages | HIGH |
| DEP-049-03-014 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | MEC-017 Equipment Installation / Setting Drawings | HIGH |
| DEP-049-03-015 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | MEC-018 Lifting / Handling Study for Major Equipment | HIGH |
| DEP-049-03-016 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | CTL-005 Cause and Effect Matrix | HIGH |

## Run Notes

**Run date:** 2026-05-25
**Mode:** UPDATE
**Strictness:** CONSERVATIVE
**Consumer context:** NONE

**Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`
- Status: FOUND and used for anchor validation and canonical label resolution.

**Source documents scanned (AUTO):**
- `Datasheet.md` — ANCHOR_DOC (contains identification, parent package, SOW trace, interface applicability)
- `Specification.md` — EXECUTION_DOC (normative requirements referencing upstream artifacts)
- `Procedure.md` — EXECUTION_DOC (explicit prerequisites, site execution sequence, turnover)
- `Guidance.md` — EXECUTION_DOC (principles and considerations; lower extraction yield)

**Source documents excluded (dependency artifacts / generated):**
- `_DEPENDENCIES.md` (this file)
- `Dependencies.csv`
- `_REFERENCES.md`, `_CONTEXT.md`, `_STATUS.md`, `_MEMORY.md` (governance/coordination files)

**Defaults applied:**
- `SOURCE_DOCS=AUTO`: all non-dependency, non-governance markdown files in deliverable folder scanned.
- `ANCHOR_DOC=AUTO`: Datasheet.md selected as highest-confidence anchor doc (contains explicit ParentPackageID and SOW IDs).
- `EXECUTION_DOC_ORDER=AUTO`: Specification.md, Procedure.md, Guidance.md.

**ASSUMPTION notes:**
- DEP-049-03-006 / DEP-049-03-007: Procedure.md explicitly labels DEL-049-01 and DEL-049-02 as `(ASSUMPTION: precedes CWP issue)`; reflected in MEDIUM confidence.
- DEP-049-03-010: Handover to DEL-049-06 is inferred from decomposition structure (DEL-049-06 explicitly consumes test/inspection evidence and turnover evidence per DELIVERABLE_REGISTER.csv). Marked IMPLICIT + MEDIUM confidence.
- Vendor artifact document IDs (MEC-017, MEC-018, QLT-020, REG-022, PIP-024, CTL-005) are extracted because they represent explicit information-transfer gates stated in normative requirements (R-CWP-3, R-CWP-4, R-CWP-6, R-CWP-9, R-CWP-12, R-CWP-15). Additional vendor artifact IDs (PIP-004, ELE-011, INS-005, etc.) were reviewed but not extracted individually — they are enumerated within broader requirement rows rather than forming distinct information-transfer gates beyond what is already represented.

**TBD items noted in source:**
- Project pressure-test specification not accessible; exact hydrotest pressures TBD (Specification R-CWP-6).
- Project MC procedure not accessible; turnover boundaries TBD (Specification R-CWP-14).
- Project welding / NDE specifications TBD.
- Pressure equipment registration jurisdictional procedure TBD.

**Warnings:** None. Parent anchor resolved (1 × IMPLEMENTS_NODE). No FLOATING_NODE or AMBIGUOUS_ANCHOR condition.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 16 |
| RETIRED | 0 |
| **Total** | **16** |

| SatisfactionStatus | Count |
|---|---|
| SATISFIED | 5 (ANCHOR rows — decomposition linkage confirmed) |
| TBD | 11 (EXECUTION rows — open pending work execution) |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full two-pass extraction run (dependency-extract skill, UPDATE mode, CONSERVATIVE strictness). Created Dependencies.csv v3.1 with 16 ACTIVE rows (5 ANCHOR, 11 EXECUTION). No prior rows to retire. Decomposition path GATE-07_Final_Published_2026-05-24 used for anchor validation. Schema validation: VALID.
