# Dependencies: DEL-063-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract run completed)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

---

## Extracted Dependency Register

Run completed: 2026-05-25 | Mode: UPDATE | Strictness: CONSERVATIVE

**Counts:** 10 ACTIVE rows (0 RETIRED)

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-063-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-063 | Tanks, DSO (API 650) | HIGH | ACTIVE |
| DEP-063-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0209 | SOW-0209 — Vendor-responsible Mechanical package | HIGH | ACTIVE |
| DEP-063-04-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0210 | SOW-0210 — Basic scope: supply one atmospheric DSO storage tank | HIGH | ACTIVE |
| DEP-063-04-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0211 | SOW-0211 — Major included equipment requirements | HIGH | ACTIVE |
| DEP-063-04-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0212 | SOW-0212 — Scope notes and exclusions (foundations by others) | HIGH | ACTIVE |
| DEP-063-04-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-063-01_scope-of-work | Scope of Work | HIGH | ACTIVE |
| DEP-063-04-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-063-02_package-datasheet | Package Datasheet | HIGH | ACTIVE |
| DEP-063-04-008 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-063-05_vendor-document-turnover-package | Vendor Document Turnover Package | HIGH | ACTIVE |
| DEP-063-04-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-063-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance | HIGH | ACTIVE |
| DEP-063-04-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DELIVERABLE | DEL-063-03_construction-work-package | Construction Work Package | MEDIUM | ACTIVE |

---

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 10 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 10 |

| DependencyClass | Count |
|---|---|
| ANCHOR | 5 |
| EXECUTION | 5 |

---

## Run Notes

- **Run date:** 2026-05-25
- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **Source docs:** AUTO — scanned deliverable folder; found `_CONTEXT.md`, `Datasheet.md`, `Procedure.md`, `Guidance.md`, `Specification.md`, `_REFERENCES.md`.
- **Anchor doc (Pass 1):** `_CONTEXT.md` (primary identity and scope item list); cross-validated against DELIVERABLE_REGISTER.csv and PACKAGE_REGISTER.csv in Gate-07 snapshot.
- **Execution docs (Pass 2):** `Procedure.md` (primary execution workflow), `Specification.md` (scope boundaries/exclusions), `Guidance.md` (context).
- **Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
- **Parent anchor:** DEP-063-04-001 — PKG-063 (WBS_NODE) — IMPLEMENTS_NODE. Single parent anchor confirmed. No FLOATING_NODE or AMBIGUOUS_ANCHOR warnings.
- **Scope items SOW-0209 through SOW-0212:** All four scope items listed in `_CONTEXT.md / Covers Scope Items` confirmed in SCOPE_LEDGER.csv row entries for PKG-063.
- **Upstream prerequisites (DEL-063-01, DEL-063-02):** Both explicitly named in `Procedure.md / Prerequisites` section.
- **Downstream handovers (DEL-063-05, DEL-063-06):** Both explicitly named in `Procedure.md / Step 9` and `Specification.md / Exclusions`.
- **Interface edge (DEL-063-03):** MEDIUM confidence — explicit exclusion boundary in Specification.md names DEL-063-03; the bidirectional transfer detail (vendor GA / foundation-interface drawing to CWP) is implicit from the exclusion statement and SOW-0212 ("foundations by others"). Conservative classification as INTERFACE UPSTREAM.
- **Binary source (26020-Package_Requirements.docx):** Not locally extracted; scope items SOW-0209–SOW-0212 are available as text in SCOPE_LEDGER.csv and serve as the authoritative text extraction of that document's package heading 18.
- **No MISSING_DECOMPOSITION warning:** Gate-07 snapshot present and readable.

---

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full two-pass dependency-extract run (UPDATE / CONSERVATIVE). 10 rows extracted (5 ANCHOR, 5 EXECUTION). Schema VALID. No warnings.
