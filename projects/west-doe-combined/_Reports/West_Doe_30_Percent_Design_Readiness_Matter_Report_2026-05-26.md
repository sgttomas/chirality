# West Doe 30% Design Readiness Matter Report

| Field | Value |
|---|---|
| Report date | 2026-05-26 |
| Project root | `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/` |
| Report status | `DERIVATIVE_PLANNING_REPORT` |
| Accepted upstream decomposition snapshot | [Gate 7 Final Published PROJECT_DECOMP](</Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/Snapshot_Manifest.md>) |
| Primary source corpus | [4-25 Deepcut DBM](</Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md>); [3-25 Compressor and Liquids DBM](</Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md>); [Package Requirements docx](</Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Package_Requirements.docx>); [Package Interfaces workbook](</Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx>) |
| Limitation | This report is not professional authentication, engineering issue approval, or a substitute for source truth. It records planning evidence and recommended next work only. |

## Executive Summary

The West Doe Combined decomposition is structurally complete against the accepted Gate 7 PROJECT_DECOMP basis. It establishes the package universe, scope ledger, deliverable scaffold, objective mappings, artifact evidence, and workbook interface facts needed to plan downstream work.

30% Design readiness is not established by that structural completeness. The deliverable kits are derivative drafts and contain pervasive `TBD`, `HRR`, `CONFLICT`, `ASSUMPTION`, and `PROPOSAL` markers. The source basis also contains material gaps: missing or unavailable appendices, unresolved process/design values, source-version weak points, package identity mismatches, and cross-facility interface items that need human or professional ruling before issue.

The next work should therefore be a governed readiness/audit phase: define the 30% Design gate criteria, build a source-basis gap register, audit high-risk packages and interfaces, and terminate in a readiness snapshot plus handoff state.

## Operating Frame

This report follows the governing thesis posture for the repository:

- Filesystem state is the operational record; material reliance requires a versioned file.
- Source truth, accepted decomposition truth, derivative packages, audits, and snapshots are separate classes of evidence.
- A derivative package may cite accepted upstream truth, but must not replace it.
- Where the source corpus is incomplete or conflicting, the correct label is `TBD`, `HRR`, `CONFLICT`, `ASSUMPTION`, or `PROPOSAL`; the report does not invent closure.
- A 30% Design submission is a project-level gate, not a deliverable lifecycle state.
- Advancement to professional issue requires human/professional authentication; this report is not professional authentication.

## Accepted Decomposition State

Accepted decomposition truth is the Gate 7 final published PROJECT_DECOMP snapshot. The live root registers were reported as byte-identical to that accepted snapshot during the evidence pass.

| Register / fact set | Count / status | Evidence |
|---|---:|---|
| Packages | 105 | [PACKAGE_REGISTER.csv](</Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/PACKAGE_REGISTER.csv>) |
| Scope ledger rows | 261 | [SCOPE_LEDGER.csv](</Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/SCOPE_LEDGER.csv>) |
| Deliverables | 594 | [DELIVERABLE_REGISTER.csv](</Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/DELIVERABLE_REGISTER.csv>) |
| Artifacts | 8,035 | [ARTIFACT_REGISTER.csv](</Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/ARTIFACT_REGISTER.csv>) |
| Interface facts | 921 | [INTERFACE_REGISTER.csv](</Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/INTERFACE_REGISTER.csv>) |
| Objectives | 10 | [OBJECTIVE_REGISTER.csv](</Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/OBJECTIVE_REGISTER.csv>) |
| Decomposition validation | PASS, no blocking issues | [VALIDATION_REPORT.md](</Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/VALIDATION_REPORT.md>) |

Key downstream-governing decisions from the accepted decomposition:

- Workbook package rows are authoritative and are not merged by repeated name or CoA tracking number.
- Workbook `ID #` values form `PKG-XXX`; Yard Lighting is `PKG-106`.
- Workbook interface `X` columns are interface facts, not packages.
- Vendor-document rows are artifacts under vendor document turnover deliverables.
- Electrical and mechanical packages are vendor-owned for package engineering/design/documentation/equipment; EPC owns facility integration.
- Every package has three mandatory EPC anchors: Scope of Work, Package Datasheet, and Construction Work Package.

The decomposition proves structural coverage. It does not prove engineering correctness, vendor data maturity, calculation adequacy, code compliance, or 30% Design readiness.

## Evidence Pass Summary

| Evidence scope | Outcome |
|---|---|
| 04-25 Deepcut DBM | 04-25 is the dominant risk center: nominal 300 MMSCFD greenfield deepcut facility with unresolved plot, metering, LACT, compression, acid gas, sales gas, utility, electrical, and appendix-source issues. |
| 03-25 Compressor/Liquids DBM | 03-25 is an 80 MMSCFD compressor station and liquids hub with critical cross-facility dependencies: sour gas export, condensate transfer, produced water, VRU/TEG flash gas, fuel gas, instrument air, electrical, flare/incinerator, and controls. |
| Package Requirements docx and workbook | Workbook covers all 105 packages; docx provides detailed vendor/package sections for 52 packages. The remaining 53 packages are source-thin, mainly electrical, civil, structural, controls, and instrumentation. |
| PROJECT_DECOMP registers | Gate 7 decomposition is accepted and structurally complete, but root frontmatter and coordination latest pointer contain stale metadata. |
| Deliverable kits | 2,376 derivative draft files across 594 deliverables contain high marker density and require readiness cleanup before 30% use. |

## Source Evidence Findings

### 04-25 Deepcut DBM

The 04-25 facility is a largely greenfield sour-gas deepcut expansion at LSD 04-25-80-15W6. It is described as a nominal 300 MMSCFD facility with inlet separation, compression, amine, TEG, molecular sieve dehydration, UltraTEF cryogenic recovery, NGL/product handling, acid gas compression, utilities, electrical, controls, and civil/site systems.

High-risk `TBD` / `CONFLICT` themes for 30% Design:

- Facility capacity and design case basis: 300 vs 303 MMSCFD, Doe 02-11 treatment, and high/license H2S/CO2/sulphur/mercury cases.
- Missing plot plan and metering schematic, blocking layout, access, spacing, roads, rack, tank, metering, and mass-balance closure.
- LACT responsibility appears both included and excluded; this remains an `HRR` / `TBD`.
- Compressor, acid gas, sales gas, separator, stabilizer, VRU, flare, heat medium, and shared utility details contain unresolved values or conflicts.
- External appendices are unavailable and must not be treated as direct design authority.

Priority 04-25 package clusters include `PKG-046`, `PKG-048`, `PKG-049`, `PKG-052` through `PKG-059`, `PKG-061` through `PKG-079`, electrical packages `PKG-020` through `PKG-043`, and structural/civil packages `PKG-001`, `PKG-003`, `PKG-101`, `PKG-102`, `PKG-104`, and `PKG-105`.

### 03-25 Compressor and Liquids DBM

The 03-25 facility is the West Doe Compressor Station and Liquids Hub at LSD 03-25-80-15W6. It receives Doe sour wellstream, separates gas/condensate/water, compresses and dehydrates sour gas, exports sour gas to 04-25, sends raw condensate to 04-25 stabilization, receives stabilized condensate back for treating/storage/export, and handles produced water.

High-risk `TBD` / `CONFLICT` themes for 30% Design:

- Shared 03-25/04-25 flare/incinerator allocation remains open.
- Feed composition and operating envelope gaps include liquid normal flow, high H2S/CO2 basis, trace sulphur, water SG, mercaptans, and inlet temperature reconciliation.
- Produced-water design contains unresolved combined values and specific gravity differences between pump and tank basis.
- Emergency buyback fuel gas is a source conflict requiring human authority.
- Geotech, hydrology, drainage, plot plan, equipment layout, and building list are not closed.
- Controls, fire and gas, ESD, SIL/HAZOP, and cause-and-effect details remain detailed-design items.

Priority 03-25 package clusters include civil/layout packages `PKG-002`, `PKG-004` through `PKG-007`, `PKG-103`; controls/instrumentation `PKG-009`, `PKG-010`; electrical `PKG-011` through `PKG-019`; and mechanical/liquids packages `PKG-089` through `PKG-100`.

### Package Requirements And Interface Workbook

The workbook is the authoritative package/interface matrix for this planning scope. It has one sheet, 105 package rows, and 24 columns. Interface density is high: Structural/Foundation/Supports, I&C/Control Cabling, Grounding/Bonding, Electrical Power, Area/Exterior Lighting, Drain/Containment, and Maintenance Access all affect many packages.

The package requirements docx adds detailed package-level source content for 52 packages. Each section generally includes Basic Scope, Major Included Equipment, Physical Interface Summary, Vendor Engineering Deliverables, and Interface Coordination Notes.

Source-basis weaknesses:

- 53 package rows lack matched docx detail, mainly Electrical, Civil, Structural, Controls, and Instrumentation.
- The docx refers to `26020-Packages_Interfaces.3.xlsx`, while the scoped workbook is `26020-Packages_Interfaces_4_export.xlsx`; this is a source-version weak point.
- Several mappings are semantic renames rather than exact identity matches.
- `26020-01-23-001` is duplicated for Fuel Gas Skid 4-25 and Truck Product Loading Unit 4-25.
- Controls power-panel tracking, instrumentation field supports/power/comms, rack-supported commodities, and platform-to-equipment tie-ins require confirmation by package scope, plot plan, model, or layout.

### Deliverable Kit Marker Inventory

The derivative deliverable kit inventory covered 2,376 draft files across 594 deliverables. Counts overlap and include repeated tables/boilerplate; they are readiness indicators, not verified source truth.

| Marker/theme | Matches |
|---|---:|
| `TBD` / `TBA` | 19,404 |
| `ASSUMPTION` / `ASSUME` | 5,002 |
| `CONFLICT` | 4,109 |
| `PROPOSAL` | 1,493 |
| `GAP` | 953 |
| `HRR` | 950 |
| Open item variants | 513 |
| `RISK` | 351 |
| `BLOCKER` | 47 |
| Total marker matches | 32,822 |

| Cluster | Total markers | Main concern |
|---|---:|---|
| Process/mechanical | 11,097 | Design loads, sour service, flare/relief, vendor handoff values. |
| Electrical/power | 9,679 | Voltage class, building identity, equipment lineup, ratings, source reconciliation. |
| Tanks/storage/loading | 5,977 | Venting, containment, sour service, coatings/material compatibility, stream composition. |
| Other process packages | 2,343 | Package-specific source and interface gaps. |
| Civil/structural/site | 2,119 | Plot, geotech, drainage, support, rack/platform dependencies. |
| Controls/instrumentation | 1,607 | Control topology, data maps, ESD/F&G logic, detector details. |

Highest marker packages reported: `PKG-067`, `PKG-063`, `PKG-052`, `PKG-048`, `PKG-106`, `PKG-064`, `PKG-023`, `PKG-096`, `PKG-094`, and `PKG-059`.

Representative derivative evidence examples include:

- Electrical identity gap: [PKG-037 Guidance.md](</Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/PKG-037_5kV-SWITCHGEAR-ELECTRICAL-BUILDING-880-1/1_Working/DEL-037-02_package-datasheet_Package-Datasheet/Guidance.md>).
- Tank vent/source gap: [PKG-067 Guidance.md](</Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/PKG-067_Tanks-Sour-Water-API-650-4-25/1_Working/DEL-067-02_package-datasheet_Package-Datasheet/Guidance.md>).
- Flare load gap: [PKG-086 Datasheet.md](</Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/PKG-086_Flare-Stack-Low-Pressure/1_Working/DEL-086-02_package-datasheet_Package-Datasheet/Datasheet.md>).
- Truck loading station conflict: [PKG-099 Guidance.md](</Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/PKG-099_Truck-Product-Loading-Unit-3-25/1_Working/DEL-099-03_construction-work-package_Construction-Work-Package/Guidance.md>).

## Priority Audit Slices

| Priority | Slice | Purpose | Expected output |
|---:|---|---|---|
| 1 | 30% readiness checklist and gate criteria | Define what must be firm, what may remain open, and what requires human/professional ruling. | Gate checklist with acceptance criteria and allowed-open rules. |
| 2 | Source-basis gap register | Convert source gaps and derivative markers into a controlled list. | Register with item, source, affected packages, owner-needed, due-needed, and status. |
| 3 | High-risk package audit | Review packages with highest marker density and technical consequence. | Package-level readiness findings and blockers. |
| 4 | Focused discipline/interface audits | Address electrical identity, flare/relief/vent/sour service, vendor handoff, civil/layout, and 03-25/04-25 interfaces. | Discipline/interface findings with `TBD`, `HRR`, `CONFLICT`, `ASSUMPTION`, and `PROPOSAL` labels. |
| 5 | Governed readiness snapshot and handoff | Freeze the planning state for downstream work. | Snapshot package and handoff state naming accepted upstream truth, derivative status, closure verdict, rerun needs, and blockers. |

## Current Git-State Note

At the time of this report, the working tree contains 594 deleted `_SEMANTIC.md` files from the prior script request to remove semantic files from each deliverable. Those deletions are outside this report package. The intended new report-related edits are limited to `_Reports/`.

## Planning Conclusion

The project has a usable accepted decomposition baseline for organizing 30% Design work. It does not yet have a controlled 30% readiness basis. The immediate next assignment should create a readiness checklist, source-basis gap register, priority package audit, focused discipline/interface audits, and a governed readiness snapshot before any claim that the derivative deliverable kit is suitable for a 30% Design submission.
