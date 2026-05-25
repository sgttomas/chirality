# Guidance: Construction Work Package

## Purpose

The Construction Work Package translates the accepted PKG-009 controls package basis into construction-facing work planning and turnover evidence. Its job is to show how the controls system design and integration package will be physically installed, built, inspected, tied into adjacent systems, and turned over to the larger facility systems.

Sources: `DELIVERABLE_REGISTER.csv` row `DEL-009-03_construction-work-package`; `PROJECT_DECOMP.md` lines 118-127 and 205.

## Principles

- Keep the CWP bounded to `PKG-009 - Controls system design and integration` and WBS 02. Do not merge with adjacent WBS 01 or WBS 03 controls rows, even though they share the same package title and tracking number. Source: `SCOPE_LEDGER.csv` row `SOW-0009`.
- Treat applicable workbook interfaces as construction checklist headings. For PKG-009 these are Process Piping, Utility Piping, Relief / Flare / Vent, Electrical Power, I&C / Control Cabling, Communications / Network, Building HVAC / Services, and Fire & Gas / Safety Systems. Source: workbook export `Packages` sheet row for WBS 02 controls package.
- Use the Gate 7 decomposition as the accepted scope and deliverable basis; do not reinterpret the raw corpus into different package or deliverable ownership.
- Mark missing package-specific construction quantities, locations, drawings, and installation details as `TBD` until a later accepted source provides them.
- Preserve unresolved source questions as human-ruling items rather than resolving them by construction convention.

## Considerations

- The DBM controls basis says BPCS process and safety devices are wired to the nearest Remote I/O control panel where practical. Construction planning should therefore identify Remote I/O routing/readiness or explicitly mark exceptions as `TBD`. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 806, 840, and 853.
- The site basis includes a -40 deg C minimum ambient condition affecting exposed control panels, instrumentation, field devices, and package buildings unless a more severe process or vendor condition applies. The CWP should not assume suitability without supporting equipment or installation evidence. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 145.
- Electrical buildings may include plant PLC control panels and network racks, and adjacent control-panel-to-contactor-panel wiring may use EMT conduit. Apply this only where the PKG-009 scope has an electrical-building/control-panel installation interface; otherwise mark applicability as `TBD`. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2973 and 2979.
- Local unit control panel push buttons shall trip local unit emergency shutdown mode where applicable. For PKG-009, applicability to specific unit panels is `TBD` until the actual panel and safety cause/effect scope is available. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 3232, 3272, and 3304.

## Trade-offs

| Topic | Guidance |
|---|---|
| Interface completeness vs. source limits | Include every declared PKG-009 interface as a checklist heading, but use `TBD` for package-specific detail not available in the accepted sources. |
| Gate 7 basis vs. raw-source reinterpretation | Follow the accepted Gate 7 snapshot for package/deliverable identity. Use source materials only to ground details, not to reopen decomposition scope. |
| Controls power-panel interfaces | Gate 6 disposition keeps controls power-panel interfaces as facts/artifacts under the package datasheet with no separate package/deliverable. Because the source row still asks for confirmation, keep this visible as a human-ruling item. |
| Generic construction practice | Avoid turning generic practice into requirements. If a work step or inspection is not grounded in accessible sources, label it `ASSUMPTION` or `TBD`. |

## Examples

Source-grounded example checklist rows for the workface plan:

| Interface | Construction planning entry |
|---|---|
| I&C / Control Cabling | Confirm Remote I/O panel routing/readiness for BPCS process and safety devices where practical; mark exceptions `TBD`. |
| Communications / Network | Confirm network rack/control system communication tie-ins where the PKG-009 installation scope interfaces with electrical buildings or PLC/network infrastructure; package-specific ports and cables are `TBD`. |
| Fire & Gas / Safety Systems | Confirm local emergency shutdown push-button interface where unit control panels are in scope; specific units and cause/effect references are `TBD`. |
| Building HVAC / Services | Confirm environmental/service support for controls equipment or buildings where applicable; package-specific HVAC loads and locations are `TBD`. |

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HRR-009-03-001 | The workbook/register source asks whether controls power-panel interfaces should be tracked separately; Gate 6 disposition says they remain interface facts/artifacts under the package datasheet and no separate package or deliverable is created. | `PACKAGE_REGISTER.csv` row `PKG-009`; `INTERFACE_REGISTER.csv` rows for `PKG-009` | Gate 6 disposition text carried in the same register rows | `Datasheet.md` Construction; `Specification.md` Requirements; `Procedure.md` Steps/Verification | Follow accepted Gate 7/Gate 6 disposition for this run; keep as visible open human-ruling item for later confirmation. | TBD |
