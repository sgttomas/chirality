# Dependencies: DEL-078-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1); this file is the human-readable index.

---

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

---

## Extracted Dependency Register

Register produced by `dependency-extract` skill run 2026-05-25. All rows are ACTIVE.

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetID / TargetRefID | TargetName | Confidence |
|---|---|---|---|---|---|---|---|---|
| DEP-078-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-078 | PKG-078 — Pig Receivers (Inlet) 4-25 | HIGH |
| DEP-078-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0161 | SOW-0161 — PKG-078 workbook package item | HIGH |
| DEP-078-04-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0162 | SOW-0162 — Basic scope: 3x pig receivers with HIPPS | HIGH |
| DEP-078-04-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0163 | SOW-0163 — Major included equipment list | HIGH |
| DEP-078-04-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0164 | SOW-0164 — Design conditions MAWP 1440 psig | HIGH |
| DEP-078-04-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-078-01_scope-of-work | Scope of Work — PKG-078 | HIGH |
| DEP-078-04-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-078-02_package-datasheet | Package Datasheet — PKG-078 | HIGH |
| DEP-078-04-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DELIVERABLE | DEL-078-03_construction-work-package | Construction Work Package — PKG-078 | HIGH |
| DEP-078-04-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-078-05_vendor-document-turnover-package | Vendor Document Turnover Package — PKG-078 | HIGH |
| DEP-078-04-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | INTERFACE | DELIVERABLE | DEL-078-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance — PKG-078 | HIGH |

**Counts:** 10 ACTIVE rows — 5 ANCHOR, 5 EXECUTION; 0 RETIRED.

---

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 10 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| SATISFIED | 5 (ANCHOR rows — traceability confirmed against GATE-07) |
| TBD | 5 (EXECUTION rows — satisfaction depends on sibling deliverable maturity) |

---

## Run Notes

**Run date:** 2026-05-25
**Mode:** UPDATE
**Strictness:** CONSERVATIVE
**Consumer context:** NONE
**Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
**Decomposition status:** FOUND — GATE-07 Final Published 2026-05-24 used for anchor validation and target resolution.

**Source documents scanned (AUTO):**
- `Datasheet.md` — ANCHOR_DOC (contains identification, WBS ref, parent package, and traceability signals)
- `Specification.md` — EXECUTION_DOC (requirements, scope split, interface list)
- `Procedure.md` — EXECUTION_DOC (prerequisites, steps, handover routing)
- `Guidance.md` — EXECUTION_DOC (principles, considerations)

**Excluded from scan (dependency artifacts / generated):** `_DEPENDENCIES.md`, `Dependencies.csv`, `_CONTEXT.md`, `_MEMORY.md`, `_REFERENCES.md`, `_STATUS.md`, `_run_records/`

**Defaults applied:**
- `SOURCE_DOCS=AUTO` — four source documents discovered and scanned.
- `ANCHOR_DOC=AUTO` — `Datasheet.md` selected as highest-confidence anchor (contains `DeliverableID`, `Parent Package`, WBS ref, and source traceability fields).
- `EXECUTION_DOC_ORDER=AUTO` — ordered: `Procedure.md`, `Specification.md`, `Guidance.md`.

**Anchor validation:** PKG-078 confirmed in GATE-07 `PACKAGE_REGISTER.csv` row 78. DEL-078-04 confirmed in `DELIVERABLE_REGISTER.csv` line 435. SOW-0161–SOW-0164 confirmed in `SCOPE_LEDGER.csv` with explicit DEL-078-04 membership.

**Integrity checks:**
- Parent anchor (IMPLEMENTS_NODE) count: 1 — OK.
- No FLOATING_NODE warning.
- No AMBIGUOUS_ANCHOR warning.

**Open items / TBD flags carried from sources:**
- RFQ `26020-01-PT-RFQ-35-001-Pig_Recv_2.docx` and `26020-Package_Requirements.docx` heading 31 are not locally rendered. No additional dependency rows were inferred from these documents (CONSERVATIVE mode). Quantitative design parameters (vessel design pressure, temperature, materials) remain TBD in source documents and were not converted into dependency rows.
- HIPPS architecture and setpoints TBD pending detailed engineering (noted in Specification REQ-08 and Guidance §Considerations) — no dependency row created as this is an internal TBD within the vendor scope, not an external information-flow dependency.
- Conflict table entries C-01, C-02, C-03 in Guidance.md require human ruling; dependency register does not encode contested assertions.

---

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — EXTRACTED run: dependency-extract skill, MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition GATE-07 found and used. 10 rows written (5 ANCHOR, 5 EXECUTION), all ACTIVE. Schema validation: VALID (29 columns, 10 data rows).
