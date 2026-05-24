---
doc_id: WEST-DOE-COMBINED-PROJECT-DECOMP
package_role: working_surface
doc_kind: decomposition.project
status: gate3_approved_pending_gate4_review
revision: 0.7
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
| Gate 3 — Objectives | APPROVED (2026-05-24) | User approved the EPC-integrator-centric objective set as the Gate 3 basis. |
| Gate 4 — Packages | ACTIVE REVIEW | Package partition is locked to the workbook breakdown; all workbook package rows now have `PKG-XXX` identifiers and `Yard Lighting` is `PKG-106`. |
| Gate 5 — Deliverables | Drafted, pending Gate 4 acceptance | Mechanical package deliverables are grouped from Word vendor-document categories; non-mechanical detail remains open where source detail is absent. |
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
| `OBJECTIVE_REGISTER.csv` | authoritative companion register | Approved objective statements, review focus, evidence basis, and traceability counts. |
| `OBJECTIVE_SCOPE_MAP.csv` | authoritative companion register | Objective-to-scope traceability rows. |
| `OBJECTIVE_PACKAGE_MAP.csv` | authoritative companion register | Objective-to-package traceability rows. |
| `OBJECTIVE_DELIVERABLE_MAP.csv` | authoritative companion register | Objective-to-deliverable traceability rows. |
| `VOCABULARY_MAP.csv` | authoritative companion register | Canonical term map. |
| `OPEN_ISSUES.csv` | authoritative companion register | Open issue register. |
| `COVERAGE_TELEMETRY.json` | authoritative companion register | Machine-readable coverage and validation summary. |
| `VALIDATION_REPORT.md` | snapshot / handoff artifact | Generated validation summary for this run. |
| `_GateSnapshots/GATE-01_Intake_Approved_2026-05-24/Snapshot_Manifest.md` | snapshot / handoff artifact | Immutable Gate 1 approval snapshot. |
| `_GateSnapshots/GATE-02_SSOW_Vocabulary_Approved_2026-05-24/Snapshot_Manifest.md` | snapshot / handoff artifact | Immutable Gate 2 approval snapshot. |
| `_GateSnapshots/GATE-03_Objectives_Approved_2026-05-24/Snapshot_Manifest.md` | snapshot / handoff artifact | Immutable Gate 3 approval snapshot. |

## 4. References

| RefID | Source | Role | Notes |
|---|---|---|---|
| SRC-001 | `_Sources/26020-Packages_Interfaces_4_export.xlsx` | Authoritative package register | One `Packages` sheet; package rows and interface `X` columns are authoritative. |
| SRC-002 | `_Sources/26020-Package_Requirements.docx` | Detailed process mechanical package scope | 52 package sections and vendor-documentation tables. |
| SRC-003 | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` | Integral DBM source | 3-25 compression and liquids design basis. |
| SRC-004 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` | Integral DBM source | 4-25 Deepcut design basis. |

## 5. Gate 3 Accepted Basis — Objectives

Gate 3 was approved on 2026-05-24. The accepted objective set is EPC-integrator-centric: it uses facility/process outcomes, vendor package obligations, and EPC integration controls as decomposition success criteria. The objective set below is derived from the accepted Gate 2 scope ledger, the workbook package breakdown, the DBMs, the package requirements document, and the accepted vendor/EPC responsibility clarification.

| ObjectiveID | Success Criterion | Derived Source Intent | Test Criteria | Scope Items | Packages | Deliverables | Gate 3 Review Focus |
|---|---|---|---|---:|---:|---:|---|
| OBJ-001 | Provide the 04-25 Deepcut facility scope required to process sour raw gas through inlet separation and stabilization, compression, amine treating, gas dehydration, cryogenic C3+ recovery, product handling, acid-gas handling, and supporting systems. | The 04-25 DBM defines a 300 MMSCFD deep cut sour gas processing expansion and supporting facility systems. | The 04-25 package set preserves process and support-system scope, interfaces, source references, deliverables, and open issues for the Deepcut design basis. | 151 | 61 | 546 | Confirm this objective captures the 04-25 facility outcome at the right level for package/deliverable mapping. |
| OBJ-002 | Provide the 03-25 compressor station and liquids hub scope required for Doe field inlet receipt and separation, inlet compression, sour-gas dehydration and export, condensate storage and treating, produced-water handling, vapour recovery, product loading, utilities, and construction support. | The 03-25 DBM defines the compressor station, liquids hub, produced-water, VRU, product-handling, and supporting facility scope. | The 03-25 package set preserves process and support-system scope, interfaces, source references, deliverables, and open issues for the compression and liquids design basis. | 101 | 44 | 356 | Confirm this objective captures the 03-25 facility outcome at the right level for package/deliverable mapping. |
| OBJ-003 | Preserve commercial stream disposition, metering accountability, and facility boundary interfaces for sales gas, NGL, condensate, acid gas, produced water, LACT/tie-in limits, truck loading, and cross-facility 03-25/04-25 exchanges. | Both DBMs define product, third-party, metering, and inter-facility boundaries that must remain explicit in downstream package execution. | Stream-handling and boundary packages expose product/disposition interfaces, tie-in limits, metering/control implications, and open boundary issues. | 146 | 44 | 528 | Confirm commercial and stream-boundary accountability should be a distinct decomposition objective. |
| OBJ-004 | Execute each electrical and mechanical equipment package as a vendor-owned package with vendor engineering, package design, vendor documentation, physical equipment supply, and EPC integration review preserved as separate responsibilities. | The user clarified that electrical and mechanical packages are developed by vendors while the EPC integrates them into the facility. | Electrical and mechanical package deliverables assign package engineering/design/equipment/documentation to the Package Vendor and integration/interface review to the EPC Integrator. | 234 | 87 | 848 | Confirm the vendor/EPC split is stated strongly enough and does not assign vendor design work to the EPC Integrator. |
| OBJ-005 | Provide and integrate the facility electrical power basis, electrical buildings, transformers, switchgear, MCC/VFD/UPS equipment, standby power, grounding and bonding, lighting, EHT, cathodic protection, and electrical interfaces to vendor packages. | Both DBMs define electrical infrastructure and package power/interface requirements as facility success conditions. | Electrical packages and electrical interface facts identify power, grounding, lighting, EHT, cathodic protection, building-service, and vendor-load responsibilities. | 242 | 95 | 872 | Confirm electrical infrastructure and vendor-load integration should be a separate objective. |
| OBJ-006 | Provide and integrate controls, instrumentation, communications, package control interfaces, fire and gas detection, alarm and shutdown interfaces, and operating data pathways across EPC and vendor package boundaries. | The DBMs define controls topology, package interfaces, instrumentation, fire/gas detection, alarms, shutdowns, and operating-data integration. | Controls, instrumentation, and package interface deliverables expose I&C, communications, fire/gas, shutdown, metering, and vendor control-system requirements. | 238 | 91 | 857 | Confirm controls, instrumentation, communications, and shutdown integration are covered at the correct level. |
| OBJ-007 | Provide and integrate shared utilities and ancillary support systems including fuel gas, instrument air, drains, flare/blowdown/vent systems, heat medium, HVAC/building services, emergency power interfaces, methanol, lube oil, analyzers, and utility tie-ins. | The DBMs define utilities and ancillary systems as cross-facility and cross-package supports required for operation. | Utility and support-system packages expose utility service boundaries, tie-ins, source dependencies, package loads, relief/drain/vent routing, and open service-allocation issues. | 223 | 76 | 792 | Confirm the utilities/support-system scope is neither too broad nor missing key DBM utility systems. |
| OBJ-008 | Provide civil, structural, site, buildings, foundations, grading, containment, access, pipe rack, platform, and construction-support scope needed to install, support, access, and maintain the facility and vendor packages. | The DBMs and workbook define civil/structural/construction support as required facility scope for modules, packages, buildings, and site systems. | Civil/structural/site packages and interface facts preserve foundation, support, access, grading, drainage, containment, construction, building, pipe-rack, and platform requirements. | 244 | 97 | 876 | Confirm civil/structural/site/construction support is scoped correctly for package integration. |
| OBJ-009 | Carry sour-service safety, relief, flare, blowdown, drain/containment, fire/gas, shutdown, environmental, emissions, regulatory, codes, and standards requirements into package scopes and interfaces. | The DBMs define sour-service, safety, emissions, environmental, regulatory, and protection constraints that must be visible in package execution. | Safety and regulatory package mappings expose fire/gas, shutdown, relief/flare, drain/containment, emissions, environmental, sour-service, and code/standard responsibilities or open issues. | 243 | 96 | 875 | Confirm this objective captures safety and compliance without becoming a generic quality objective. |
| OBJ-010 | Maintain operability, maintainability, sparing, isolation, winterization, vendor-documentation, commissioning, turnover, and controlled open-item closure evidence for package procurement and downstream facility handoff. | The DBMs and package requirements document define sparing, isolation, maintenance access, vendor document registers, package deliverables, and open design-development items as closure conditions. | Package deliverables and open issues show vendor documents, package engineering basis, sparing/isolation/access/winterization assumptions, commissioning/turnover needs, and unresolved DBM/package TBDs. | 242 | 95 | 872 | Confirm open-item and handoff readiness evidence should remain a Gate 3 objective. |

Objective source references, expected downstream evidence, and mapping basis live in `OBJECTIVE_REGISTER.csv`. Row-level traceability lives in `OBJECTIVE_SCOPE_MAP.csv`, `OBJECTIVE_PACKAGE_MAP.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.

Not included as standalone objectives: package-ID hygiene, workbook-authority policy, duplicate-row preservation, open-issue bookkeeping, and register maintenance. Those remain required decisions, invariants, or telemetry controls, but they are not Gate 3 success criteria.

## 6. Gate 4 Review Surface — Package Partition

Gate 4 asks whether the flat package partition is correct and whether each accepted scope item belongs to exactly one package. For this project, the package partition is not inferred: it is locked to the `26020-Packages_Interfaces_4_export.xlsx` workbook package rows.

Gate 4 review should confirm:

- the 105 workbook package rows remain the authoritative flat package list;
- package IDs use workbook `ID #` as `PKG-XXX`, including `Yard Lighting` as `PKG-106`;
- duplicate package names and repeated CoA tracking numbers remain separate where the workbook gives separate rows;
- design package assignments remain discipline-exclusive according to the workbook discipline column;
- workbook interface `X` columns remain interface facts, not separate packages;
- each `IN` scope item maps to exactly one `PackageID` in `SCOPE_LEDGER.csv`;
- package responsibility text preserves vendor ownership for electrical/mechanical package engineering, design, vendor documentation, and physical equipment, with EPC Integrator responsibility for facility integration.

The full package list is authoritative in `PACKAGE_REGISTER.csv`; it is summarized here to keep the main document usable as a control surface.

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
| ObjectiveCount | 10 |
| UnassignedScopeItems | 0 |
| ScopeItemsWithoutDeliverableMapping | 0 |
| UnmappedObjectives | 0 |
| OpenIssueCount | 67 |
| BlockingOpenIssueCount | 0 |

Open issue counts by type: INTERFACE_NOTE_CONFIRMATION=8, MISSING_DETAILED_PACKAGE_REQUIREMENTS=56, UNMATCHED_WORD_PACKAGE_SECTION=3.

## 9. Open Issues

The live open issues do not block Gate 4 package-partition review. They are retained for later deliverable and coverage gates where detailed source gaps and interface-note dispositions matter.

| Issue Type | Count | Gate Focus | Review Note |
|---|---:|---|---|
| INTERFACE_NOTE_CONFIRMATION | 8 | Gate 5 / Gate 6 | Confirm workbook interface notes before final deliverable and coverage acceptance. |
| MISSING_DETAILED_PACKAGE_REQUIREMENTS | 56 | Gate 5 | Non-mechanical and unmatched package details remain source-limited; do not invent requirements. |
| UNMATCHED_WORD_PACKAGE_SECTION | 3 | Gate 5 | Resolve whether Word package sections are superseded, renamed, or manually mapped. |
| All open issues | 67 | See register | Full details are authoritative in `OPEN_ISSUES.csv`. |

## 10. Decision Log

| DecisionRef | Decision | Source |
|---|---|---|
| DEC-001 | Workbook package rows are authoritative and are not merged by name or repeated CoA tracking number. | User instruction; `26020-Packages_Interfaces_4_export.xlsx` |
| DEC-002 | Workbook `ID #` is used as `PKG-XXX`; the initially missing Yard Lighting ID was resolved as workbook ID 106 / `PKG-106`. | User-selected implementation policy and source workbook update |
| DEC-003 | Interface `X` columns are represented as interface facts in `INTERFACE_REGISTER.csv`, not as separate packages. | User instruction; PROJECT_DECOMP flat-package invariant |
| DEC-004 | Word vendor-document rows are represented as artifacts under category-level PROJECT_DECOMP deliverables. | PROJECT_DECOMP design-deliverable granularity rule |
| DEC-005 | Non-mechanical detail is not invented; where detailed source material is absent, deliverables are marked TBD and open issues are recorded. | No-invention invariant |
| DEC-006 | Electrical and mechanical packages are vendor-owned for package engineering, design, vendor documentation, and physical equipment; the central EPC company owns integration into the full process facility. | Human Gate 1 clarification |
| DEC-007 | Gate 1 intake understanding is approved; proceed to Gate 2 SSOW and Vocabulary review. | Human Gate 1 approval on 2026-05-24 |
| DEC-008 | Gate 2 SSOW and Vocabulary are approved as-is; proceed to Gate 3 Objectives review. | Human Gate 2 approval on 2026-05-24 |
| DEC-009 | Gate 3 objectives were rebuilt before Gate 3 approval to function as source-derived, testable decomposition success criteria rather than broad umbrella labels or internal register controls. | PROJECT_DECOMP reassessment before Gate 3 acceptance |
| DEC-010 | Gate 3 objectives are approved; proceed to Gate 4 package partition review using the workbook package breakdown as the authoritative flat package list. | Human Gate 3 approval on 2026-05-24 |

## 11. DBM Section Coverage Notes

The DBMs were ingested as design-basis sources and cited by WBS grouping. Representative top-level sections discovered:

| DBM | Top-level section count | First sections |
|---|---:|---|
| DBM-Comp_and_Liquids | 16 | SEC-01 - Document Control, Facility Overview, and Scope; SEC-02 - Site-Specific Design Data; SEC-03 - Feeds, Products, and Wastes; SEC-04 - Compressor Station Inlet, Separation, and Sour-Gas Export; SEC-05 - Inlet Compression and Sour-Gas Dehydration |
| DBM-Deepcut | 16 | SEC-01 - Project and Document Basis; SEC-02 - Site, Layout, and Spacing Basis; SEC-03 - Feed, Product, Waste, and Metering Basis; SEC-04 - Inlet, Separation, Stabilization, and Stabilizer Overheads Basis; SEC-05 - Compression and Acid Gas Handling Basis |

## 12. Handoff State

- Accepted upstream snapshots: `_GateSnapshots/GATE-01_Intake_Approved_2026-05-24/Snapshot_Manifest.md`, `_GateSnapshots/GATE-02_SSOW_Vocabulary_Approved_2026-05-24/Snapshot_Manifest.md`, and `_GateSnapshots/GATE-03_Objectives_Approved_2026-05-24/Snapshot_Manifest.md` record the accepted Gate 1, Gate 2, and Gate 3 basis.
- Derivative-package status: Gate 1, Gate 2, and Gate 3 snapshots are accepted decomposition-state records; the live Gate 4 package partition remains under active review. The source documents remain upstream source truth.
- Closure verdict: Gates 1-3 closed; Gate 4 is active. Overall decomposition is not closed until Gates 4-7 are accepted.
- Rerun requirements: rerun `scripts/build_project_decomp.py` after workbook ID correction, package source additions, or human disposition of open issues.
- Remaining blockers: none.
