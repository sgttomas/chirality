# Specification: DEL-045-03 Construction Work Package

## Scope

This specification governs the initial construction work package document set for `PKG-045 - Instrumentation (outside of Mechanical Packages only)`, WBS `03`, discipline Instrumentation.

The construction work package shall describe the physical installation, construction, tie-in, inspection, and turnover basis for this instrumentation package, including the workface plan and construction interface/turnover checklist. Source: `DELIVERABLE_REGISTER.csv`, row `DEL-045-03_construction-work-package`; `ARTIFACT_REGISTER.csv`, rows `ART-F6FBF7A832`, `ART-2D467E7301`, `ART-618CCB3675`.

Exclusions:

- Tagged instrument lists, loop counts, signal counts, panel quantities, cable schedules, and field termination tolerances are `TBD` because they are not present in the accessible source slices.
- Final hazardous-area classification, instrument environmental ratings, and EMC/grounding criteria are `TBD` pending design-basis source access.
- Package-specific construction schedule, crew plan, and means/methods are `TBD`.

## Requirements

| ID | Requirement | Source / status | Verification |
|---|---|---|---|
| CWP-REQ-001 | The CWP shall identify the package as `PKG-045 - Instrumentation (outside of Mechanical Packages only)`, WBS `03`, discipline Instrumentation, tied to workbook row 47. | `PACKAGE_REGISTER.csv`, row `PKG-045`; workbook row 47. | Datasheet and cover metadata review. |
| CWP-REQ-002 | The CWP shall include or reference the three required artifact outputs: construction work package, installation and tie-in workface plan, and construction interface and turnover checklist. | `_CONTEXT.md`; `ARTIFACT_REGISTER.csv`, rows `ART-F6FBF7A832`, `ART-2D467E7301`, `ART-618CCB3675`. | Deliverable package completeness check. |
| CWP-REQ-003 | The CWP shall address the source-confirmed interface types: Process Piping; Utility Piping; Electrical Power; I&C / Control Cabling; Communications / Network. | `INTERFACE_REGISTER.csv`, rows `IFC-33F8A9F366`, `IFC-AE76B11E50`, `IFC-2D030CA850`, `IFC-210F46B073`, `IFC-9DAC4D3C4D`. | Interface checklist review. |
| CWP-REQ-004 | The CWP shall include instrumentation field supports, power, and communications in package scope as appropriate, per the Gate 6 plug-n-play package philosophy disposition. | `INTERFACE_REGISTER.csv`, rows 307-311 (Notes column). | Scope inclusion review against the workface plan. |
| CWP-REQ-005 | The CWP shall not close tagged instrument list, instrument data sheets, loop wiring, or termination acceptance criteria until upstream `DEL-045-01_scope-of-work` and `DEL-045-02_package-datasheet` provide source-supported equipment and interface data. | `SCOPE_LEDGER.csv`, row `SOW-0046` (deliverable chain); `DELIVERABLE_REGISTER.csv` rows 248-250. | Open-item review; upstream-handoff confirmation. |
| CWP-REQ-006 | The CWP shall preserve the workbook package row as authoritative and shall not merge duplicate workbook tracking numbers across packages. | `SCOPE_LEDGER.csv`, row `SOW-0046` (Notes); `PACKAGE_REGISTER.csv` row 47. | Source-identity check. |
| CWP-REQ-007 | The CWP shall address tie-in to Process and Utility Piping interfaces where instrumentation taps, sample lines, or analytical hookups cross package boundaries. | `INTERFACE_REGISTER.csv`, rows `IFC-33F8A9F366`, `IFC-AE76B11E50`. | Drainage/process tie-in review. |
| CWP-REQ-008 | The CWP shall address tie-in to Electrical Power and I&C / Control Cabling interfaces for instrument loop power, signal cabling, and control system terminations. | `INTERFACE_REGISTER.csv`, rows `IFC-2D030CA850`, `IFC-210F46B073`. | Electrical / I&C interface review. |
| CWP-REQ-009 | The CWP shall address tie-in to the Communications / Network interface for instrument network segments and remote I/O communications. | `INTERFACE_REGISTER.csv`, row `IFC-9DAC4D3C4D`. | Network interface review. |
| CWP-REQ-010 | ASSUMPTION: The EPC Integrator shall coordinate discipline subcontractor inputs because the package responsibility model is source-dependent and no vendor-package ownership model is inferred. | `PACKAGE_REGISTER.csv`, row `PKG-045`. | Responsibility assignment review. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Accepted Gate 7 PROJECT_DECOMP snapshot | Authoritative decomposition truth for package, deliverable, objective, artifact, and interface identity. | Available locally. |
| Workbook `Packages` sheet row 47 | Authoritative package row, WBS, discipline, and interface flags. | Source row exists; raw cells not copied locally — `location TBD` for cell-level citations. |
| `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` | Cited by `PACKAGE_REGISTER.csv` row 47 as supporting basis for this package. | Cited in registers; slice content not extracted for this deliverable — `location TBD`. |
| Instrumentation discipline standards (e.g., ISA, IEC, local code) | Governing for instrument design, hazardous-area classification, loop wiring, and signal integrity. | `TBD` — no specific instrumentation standard cited in accessible source slices; treat as **ASSUMPTION** until upstream deliverables confirm. |
| Detailed IFC instrumentation drawings (loop sheets, P&IDs, layout, cable schedules) | Required to close execution criteria, quantities, tolerances, inspection hold points, and construction sequencing. | TBD - not locally available. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity and traceability | Compare CWP metadata to `_CONTEXT.md`, `PACKAGE_REGISTER.csv`, and `DELIVERABLE_REGISTER.csv`. | All IDs, names, WBS, and source refs match. |
| Interface coverage | Check workface plan and checklist against `INTERFACE_REGISTER.csv` for PKG-045. | All five source-confirmed interface types are covered or marked `TBD` with rationale. |
| Plug-n-play scope inclusion | Confirm field supports, power, and communications inclusion treatment matches Gate 6 disposition. | Scope statements reflect the disposition without overstating package boundaries. |
| Upstream handoff control | Review CWP for instrument list and loop acceptance criteria. | Tagged-equipment-dependent values remain `TBD` until `DEL-045-01` / `DEL-045-02` provide them. |
| Turnover readiness | Confirm a construction interface and turnover checklist exists. | Checklist identifies required records and open `TBD` signoffs. |

## Documentation

The CWP package shall include, at minimum:

- Construction work package (`ART-F6FBF7A832`).
- Installation and tie-in workface plan (`ART-2D467E7301`).
- Construction interface and turnover checklist (`ART-618CCB3675`).
- Source and traceability register for Gate 7 snapshot, workbook row 47, PKG-045 registers, and the cited DBM source.
- Open-item list for tagged instrument list, IFC instrumentation drawings, cable schedules, loop ITP/hold points, hazardous-area classification, and turnover signoff matrix.
