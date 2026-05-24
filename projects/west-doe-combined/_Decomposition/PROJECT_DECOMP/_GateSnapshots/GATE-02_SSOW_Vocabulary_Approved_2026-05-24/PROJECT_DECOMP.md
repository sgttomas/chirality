---
doc_id: WEST-DOE-COMBINED-PROJECT-DECOMP
package_role: working_surface
doc_kind: decomposition.project
status: gate2_approved_pending_gate3_review
revision: 0.3
created: 2026-05-24
governed_by:
  - AGENT_PROJECT_DECOMP.md
  - AGENT_DECOMP_BASE.md
---

# PROJECT_DECOMP — West Doe Combined

## 1. Intake Summary

This PROJECT_DECOMP working package decomposes the West Doe Combined source corpus into a flat package register, scope ledger, deliverable register, artifact register, interface register, objective register, vocabulary map, open issue register, and coverage telemetry.

The workbook `26020-Packages_Interfaces_4_export.xlsx` is the authoritative package breakdown. Package rows are not merged when package names or CoA tracking numbers repeat. The Word package requirements document supplies detailed process mechanical equipment scope and vendor-documentation requirements where its package sections can be matched to workbook rows. The two DBM folders are integral design-basis sources for objectives, boundaries, and source context.

Responsibility model clarified before Gate 1 acceptance: each electrical and mechanical package is treated as a vendor-owned package. The Package Vendor is responsible for that package's engineering, design, vendor documentation, and physical equipment package. The central EPC company is treated as the EPC Integrator responsible for integrating all vendor packages into a functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

## 2. Gate Status

| Gate | Status | Notes |
|---|---|---|
| Gate 1 — Intake | APPROVED (2026-05-24) | User approved intake understanding, source authority order, vendor/EPC responsibility split, and Yard Lighting ID resolution. |
| Gate 2 — SSOW + Vocabulary | APPROVED (2026-05-24) | User approved the generated scope ledger and vocabulary map as-is. |
| Gate 3 — Objectives | ACTIVE REVIEW | Objectives derived from workbook, DBMs, and package requirements; ready for human review. |
| Gate 4 — Packages | Drafted, pending human confirmation | All workbook package rows now have `PKG-XXX` identifiers; `Yard Lighting` is `PKG-106`. |
| Gate 5 — Deliverables | Drafted with open issues | Mechanical package deliverables are grouped from Word vendor-document categories; non-mechanical detail remains open where source detail is absent. |
| Gate 6 — Coverage | Drafted, pending human confirmation | Coverage checks are in `COVERAGE_TELEMETRY.json` and `VALIDATION_REPORT.md`; no blocking validation issue is currently open. |
| Gate 7 — Publish | Not accepted | Final acceptance requires remaining gate confirmations. |

## 3. Companion Inventory

| Artifact | Role | Authority |
|---|---|---|
| `PROJECT_DECOMP.md` | working surface | Human-facing control surface. |
| `PACKAGE_REGISTER.csv` | authoritative companion register | Authoritative package rows derived from the workbook. |
| `SCOPE_LEDGER.csv` | authoritative companion register | Authoritative scope-item mapping and coverage ledger. |
| `DELIVERABLE_REGISTER.csv` | authoritative companion register | Authoritative deliverable rows. |
| `ARTIFACT_REGISTER.csv` | authoritative companion register | Anticipated artifact instances under deliverables. |
| `INTERFACE_REGISTER.csv` | authoritative companion register | Workbook interface facts. |
| `OBJECTIVE_REGISTER.csv` | authoritative companion register | Objective statements and deliverable mappings. |
| `VOCABULARY_MAP.csv` | authoritative companion register | Canonical term map. |
| `OPEN_ISSUES.csv` | authoritative companion register | Open issue register. |
| `COVERAGE_TELEMETRY.json` | authoritative companion register | Machine-readable coverage and validation summary. |
| `VALIDATION_REPORT.md` | snapshot / handoff artifact | Generated validation summary for this run. |
| `_GateSnapshots/GATE-01_Intake_Approved_2026-05-24/Snapshot_Manifest.md` | snapshot / handoff artifact | Immutable Gate 1 approval snapshot. |
| `_GateSnapshots/GATE-02_SSOW_Vocabulary_Approved_2026-05-24/Snapshot_Manifest.md` | snapshot / handoff artifact | Immutable Gate 2 approval snapshot. |

## 4. References

| RefID | Source | Role | Notes |
|---|---|---|---|
| SRC-001 | `_Sources/26020-Packages_Interfaces_4_export.xlsx` | Authoritative package register | One `Packages` sheet; package rows and interface `X` columns are authoritative. |
| SRC-002 | `_Sources/26020-Package_Requirements.docx` | Detailed process mechanical package scope | 52 package sections and vendor-documentation tables. |
| SRC-003 | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` | Integral DBM source | 3-25 compression and liquids design basis. |
| SRC-004 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` | Integral DBM source | 4-25 Deepcut design basis. |

## 5. Objectives

| ObjectiveID | Statement | MappedDeliverables | OpenIssue |
|---|---|---:|---|
| OBJ-001 | Preserve the workbook package breakdown as the authoritative flat project package partition for downstream work. | 902 | FALSE |
| OBJ-002 | Carry the 4-25 Deepcut design basis, package scopes, and package interfaces into package-level decomposition outputs. | 542 | FALSE |
| OBJ-003 | Carry the 3-25 compression and liquids design basis, package scopes, and package interfaces into package-level decomposition outputs. | 356 | FALSE |
| OBJ-004 | Maintain vendor-owned engineering, design, physical equipment package, and vendor-documentation traceability for electrical and mechanical packages. | 848 | FALSE |
| OBJ-005 | Make discipline and physical-interface coordination explicit without creating interface packages or nested package structures. | 902 | FALSE |
| OBJ-006 | Surface unresolved package identity, interface, and non-mechanical scope-detail gaps as explicit open issues before final acceptance. | 902 | FALSE |

## 6. Package Summary

- Package rows: 105
- Accepted `PKG-XXX` IDs: 105
- Missing package IDs: 0
- Electrical/mechanical vendor-owned package rows: 87
- Discipline counts: Civil 7, Controls 3, Electrical 33, Instrumentation 3, Mechanical 54, Structural 5
- Package register authority: `PACKAGE_REGISTER.csv`.

The package list is intentionally not duplicated in full here. `PACKAGE_REGISTER.csv` is the authoritative companion register for package identity, source rows, discipline, WBS, scope description, interface types, and source references.

## 7. Deliverable Summary

- Deliverables: 902
- Artifacts: 4886
- Electrical and mechanical package deliverables assign package engineering/design/equipment responsibility to the Package Vendor and integration responsibility to the EPC Integrator.
- Mechanical vendor-document deliverables are grouped by source-table category rather than by individual document row.
- Non-mechanical package detail is carried conservatively from workbook and DBM sources, with open issues where discipline-specific detailed source material is absent.

## 8. Coverage & Telemetry

| Metric | Value |
|---|---:|
| ScopeItemCount | 252 |
| PackageCount | 105 |
| DeliverableCount | 902 |
| ObjectiveCount | 6 |
| UnassignedScopeItems | 0 |
| ScopeItemsWithoutDeliverableMapping | 0 |
| UnmappedObjectives | 0 |
| OpenIssueCount | 67 |
| BlockingOpenIssueCount | 0 |

Open issue counts by type: INTERFACE_NOTE_CONFIRMATION=8, MISSING_DETAILED_PACKAGE_REQUIREMENTS=56, UNMATCHED_WORD_PACKAGE_SECTION=3.

## 9. Open Issues

| IssueID | Severity | Type | RelatedID | Statement |
|---|---|---|---|---|
| ISS-001 | ACTION | MISSING_DETAILED_PACKAGE_REQUIREMENTS | PKG-001 | No matching detailed package requirements section was found for workbook package 'Earthworks for foundations'. |
| ISS-002 | ACTION | MISSING_DETAILED_PACKAGE_REQUIREMENTS | PKG-002 | No matching detailed package requirements section was found for workbook package 'Earthworks for foundations'. |
| ISS-003 | ACTION | MISSING_DETAILED_PACKAGE_REQUIREMENTS | PKG-003 | No matching detailed package requirements section was found for workbook package 'Site Grading'. |
| ISS-004 | ACTION | MISSING_DETAILED_PACKAGE_REQUIREMENTS | PKG-004 | No matching detailed package requirements section was found for workbook package 'Site Grading'. |
| ISS-005 | ACTION | MISSING_DETAILED_PACKAGE_REQUIREMENTS | PKG-005 | No matching detailed package requirements section was found for workbook package 'Site Grading'. |
| ISS-006 | ACTION | MISSING_DETAILED_PACKAGE_REQUIREMENTS | PKG-006 | No matching detailed package requirements section was found for workbook package 'Containment Berms'. |
| ISS-007 | ACTION | MISSING_DETAILED_PACKAGE_REQUIREMENTS | PKG-007 | No matching detailed package requirements section was found for workbook package 'Retention Pond'. |
| ISS-008 | ACTION | INTERFACE_NOTE_CONFIRMATION | PKG-008 | Confirm whether controls power-panel interfaces should be tracked separately. |
| ISS-009 | ACTION | MISSING_DETAILED_PACKAGE_REQUIREMENTS | PKG-008 | No matching detailed package requirements section was found for workbook package 'Controls system design and integration'. |
| ISS-010 | ACTION | INTERFACE_NOTE_CONFIRMATION | PKG-009 | Confirm whether controls power-panel interfaces should be tracked separately. |
| ISS-011 | ACTION | MISSING_DETAILED_PACKAGE_REQUIREMENTS | PKG-009 | No matching detailed package requirements section was found for workbook package 'Controls system design and integration'. |
| ISS-012 | ACTION | INTERFACE_NOTE_CONFIRMATION | PKG-010 | Confirm whether controls power-panel interfaces should be tracked separately. |
| ISS-013 | ACTION | MISSING_DETAILED_PACKAGE_REQUIREMENTS | PKG-010 | No matching detailed package requirements section was found for workbook package 'Controls system design and integration'. |
| ISS-014 | ACTION | MISSING_DETAILED_PACKAGE_REQUIREMENTS | PKG-106 | No matching detailed package requirements section was found for workbook package 'Yard Lighting'. |
| ISS-015 | ACTION | MISSING_DETAILED_PACKAGE_REQUIREMENTS | PKG-011 | No matching detailed package requirements section was found for workbook package '4160V SWITCHGEAR EQUIPMENT'. |
| ISS-016 | ACTION | MISSING_DETAILED_PACKAGE_REQUIREMENTS | PKG-012 | No matching detailed package requirements section was found for workbook package '10KVA AC UNINTERRUPTIBLE POWER SUPPLY'. |
| ISS-017 | ACTION | MISSING_DETAILED_PACKAGE_REQUIREMENTS | PKG-013 | No matching detailed package requirements section was found for workbook package '100A DC UNINTERUPTIBLE POWER SUPPLY'. |
| ISS-018 | ACTION | MISSING_DETAILED_PACKAGE_REQUIREMENTS | PKG-014 | No matching detailed package requirements section was found for workbook package 'CONTACTOR PANELS - LIGHTING / EXHAUST FAN CONTACTOR PANELS - LOW VOLTAGE'. |
| ISS-019 | ACTION | MISSING_DETAILED_PACKAGE_REQUIREMENTS | PKG-015 | No matching detailed package requirements section was found for workbook package 'Transformer TXP-8300-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 12/15MVA 13.8kV/4160/2400V'. |
| ISS-020 | ACTION | MISSING_DETAILED_PACKAGE_REQUIREMENTS | PKG-016 | No matching detailed package requirements section was found for workbook package 'Transformer TXP-8200-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 3MVA 13.8kV/600/347V'. |
| ... | ... | ... | ... | See `OPEN_ISSUES.csv` for all 67 open issues. |

## 10. Decision Log

| DecisionRef | Decision | Source |
|---|---|---|
| DEC-001 | Workbook package rows are authoritative and are not merged by name or repeated CoA tracking number. | User instruction; `26020-Packages_Interfaces_4_export.xlsx` |
| DEC-002 | Workbook `ID #` is used as `PKG-XXX`; missing `ID #` remains a blocker instead of inventing an ID. | User-selected implementation policy |
| DEC-003 | Interface `X` columns are represented as interface facts in `INTERFACE_REGISTER.csv`, not as separate packages. | User instruction; PROJECT_DECOMP flat-package invariant |
| DEC-004 | Word vendor-document rows are represented as artifacts under category-level PROJECT_DECOMP deliverables. | PROJECT_DECOMP design-deliverable granularity rule |
| DEC-005 | Non-mechanical detail is not invented; where detailed source material is absent, deliverables are marked TBD and open issues are recorded. | No-invention invariant |
| DEC-006 | Electrical and mechanical packages are vendor-owned for package engineering, design, vendor documentation, and physical equipment; the central EPC company owns integration into the full process facility. | Human Gate 1 clarification |
| DEC-007 | Gate 1 intake understanding is approved; proceed to Gate 2 SSOW and Vocabulary review. | Human Gate 1 approval on 2026-05-24 |
| DEC-008 | Gate 2 SSOW and Vocabulary are approved as-is; proceed to Gate 3 Objectives review. | Human Gate 2 approval on 2026-05-24 |

## 11. DBM Section Coverage Notes

The DBMs were ingested as design-basis sources and cited by WBS grouping. Representative top-level sections discovered:

| DBM | Top-level section count | First sections |
|---|---:|---|
| DBM-Comp_and_Liquids | 16 | SEC-01 - Document Control, Facility Overview, and Scope; SEC-02 - Site-Specific Design Data; SEC-03 - Feeds, Products, and Wastes; SEC-04 - Compressor Station Inlet, Separation, and Sour-Gas Export; SEC-05 - Inlet Compression and Sour-Gas Dehydration |
| DBM-Deepcut | 16 | SEC-01 - Project and Document Basis; SEC-02 - Site, Layout, and Spacing Basis; SEC-03 - Feed, Product, Waste, and Metering Basis; SEC-04 - Inlet, Separation, Stabilization, and Stabilizer Overheads Basis; SEC-05 - Compression and Acid Gas Handling Basis |

## 12. Handoff State

- Accepted upstream snapshots: `_GateSnapshots/GATE-01_Intake_Approved_2026-05-24/Snapshot_Manifest.md` and `_GateSnapshots/GATE-02_SSOW_Vocabulary_Approved_2026-05-24/Snapshot_Manifest.md` record the accepted Gate 1 and Gate 2 basis.
- Derivative-package status: this decomposition package is authoritative for decomposition truth once human gates are accepted; the source documents remain upstream source truth.
- Closure verdict: Gates 1-2 closed; Gate 3 is active. Overall decomposition is not closed until Gates 3-7 are accepted.
- Rerun requirements: rerun `scripts/build_project_decomp.py` after workbook ID correction, package source additions, or human disposition of open issues.
- Remaining blockers: none.
