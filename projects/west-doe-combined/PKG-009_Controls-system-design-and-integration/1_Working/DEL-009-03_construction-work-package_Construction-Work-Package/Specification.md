# Specification: Construction Work Package

## Scope

This specification defines the minimum content and verification expectations for `DEL-009-03_construction-work-package`, the EPC Integrator construction work package for `PKG-009 - Controls system design and integration`.

The Construction Work Package covers physical installation, construction, tie-in, inspection, turnover, and integration into larger facility systems for the WBS 02 controls package. It includes:

- construction work package;
- installation and tie-in workface plan;
- construction interface and turnover checklist.

Exclusions:

- Package-specific exclusions are `TBD`; the package register states no package-specific exclusions in the source materials.
- Separate controls power-panel deliverables are not created by the Gate 7 basis; related facts remain package interface facts/artifacts unless a human ruling changes that basis.

Sources: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-009-03_construction-work-package`; `PACKAGE_REGISTER.csv` row `PKG-009`; `PROJECT_DECOMP.md` lines 118-127 and 205.

## Requirements

| ID | Requirement | Source / basis | Verification |
|---|---|---|---|
| CWP-REQ-001 | The deliverable shall be produced by or under the responsibility of the EPC Integrator. | `DELIVERABLE_REGISTER.csv` row `DEL-009-03_construction-work-package` | Confirm responsible-party field and approval routing in the CWP cover/check sheet. |
| CWP-REQ-002 | The CWP shall describe physical installation, construction, tie-in, inspection, turnover, and connection to larger facility systems for the PKG-009 controls package. | `DELIVERABLE_REGISTER.csv`; `PROJECT_DECOMP.md` lines 124-127 | Verify CWP sections exist for installation, construction, tie-in, inspection, turnover, and system integration. |
| CWP-REQ-003 | The CWP shall include a construction work package, installation and tie-in workface plan, and construction interface and turnover checklist. | `DELIVERABLE_REGISTER.csv`; `ARTIFACT_REGISTER.csv` rows `ART-30F1E682E4`, `ART-80DA88C819`, `ART-1D954E6A4A` | Confirm all three artifacts are present or explicitly listed as controlled attachments. |
| CWP-REQ-004 | The workface plan shall address the applicable PKG-009 interfaces: Process Piping, Utility Piping, Relief / Flare / Vent, Electrical Power, I&C / Control Cabling, Communications / Network, Building HVAC / Services, and Fire & Gas / Safety Systems. | Workbook export `26020-Packages_Interfaces_4_export.xlsx`, `Packages` sheet row for WBS 02 controls package; `PACKAGE_REGISTER.csv`; `INTERFACE_REGISTER.csv` rows for `PKG-009` | Confirm each applicable interface has a tie-in, constraint, readiness, or `TBD` entry in the interface checklist. |
| CWP-REQ-005 | Controls construction planning shall account for Remote I/O wiring where practical for BPCS process and safety devices. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 806, 840, 853 | Verify I&C / control cabling workface plan includes Remote I/O panel routing or a `TBD`/exception entry. |
| CWP-REQ-006 | Safety-related local unit control panel push buttons, where in scope, shall be tied to local unit emergency shutdown mode. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 3232, 3272, 3304 | Verify Fire & Gas / Safety Systems interface checklist includes local ESD push-button tie-in confirmation where applicable. |
| CWP-REQ-007 | Controls construction planning shall consider -40 deg C minimum ambient for exposed control panels, instrumentation, field devices, and package buildings unless a more severe process or vendor condition applies. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 145 | Verify environmental readiness/installation checklist includes ambient suitability or `TBD` for affected controls equipment. |
| CWP-REQ-008 | The CWP shall preserve the source issue on controls power-panel interface treatment as an open human-ruling item unless resolved by a later accepted snapshot. | `PACKAGE_REGISTER.csv` row `PKG-009`; `INTERFACE_REGISTER.csv` rows for `PKG-009` | Confirm open item appears in the checklist, risk/open-item log, or human ruling section. |

## Standards

| Standard / governing basis | Status |
|---|---|
| Gate 7 final published PROJECT_DECOMP snapshot dated 2026-05-24 | Authoritative accepted decomposition truth for this run. |
| `26020-Packages_Interfaces_4_export.xlsx` workbook export | Accessible local source for package row/interface facts. |
| `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` | Accessible local source for controls ambient and Remote I/O wiring basis. |
| `DBM-Deepcut/4-25_Deepcut_DBM.md` | Accessible local source for electrical building/control panel and local emergency shutdown interface basis. |
| Code/standard clauses specific to construction work packaging | TBD. No clause-level construction standard or project execution procedure was copied as an accessible deliverable-specific source slice. |

## Verification

The CWP is acceptable for initialization when:

- the three anticipated artifacts are present or explicitly controlled as attachments;
- every applicable PKG-009 interface has a construction/tie-in/turnover checklist row or a `TBD` entry;
- BPCS Remote I/O wiring, safety push-button tie-ins, ambient suitability, electrical power, communications/network, building HVAC/services, and Fire & Gas / Safety Systems interfaces are addressed where applicable;
- package-specific unknowns remain marked `TBD`;
- the controls power-panel interface issue is surfaced for human ruling rather than silently resolved.

## Documentation

Required documentation set:

- construction work package;
- installation and tie-in workface plan;
- construction interface and turnover checklist;
- open-item/human-ruling log for source-limited or unresolved interface treatment;
- turnover evidence showing inspection and construction interface closure.
