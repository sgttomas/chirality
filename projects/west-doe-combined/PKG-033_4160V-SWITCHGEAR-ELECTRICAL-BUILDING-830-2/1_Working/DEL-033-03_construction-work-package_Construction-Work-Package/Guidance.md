# Guidance: DEL-033-03_construction-work-package

## Purpose

The Construction Work Package exists to convert the accepted Gate 7 package basis for `PKG-033` into a source-supported, EPC-owned installation, inspection, tie-in, and turnover plan for the 4160V SWITCHGEAR ELECTRICAL BUILDING (830-2). It should let construction execute the package within the facility-level integration boundary while keeping vendor package engineering/design responsibility with the Package Vendor.

## Principles

- Preserve source spelling and identity. The package name is carried as "4160V SWITCHGEAR ELECTRICAL BUILDING (830-2)" because that is the workbook and Gate 7 register spelling.
- Treat the twelve workbook interface `X` facts for `PKG-033` as construction-package evidence and coordination scope, not as separate deliverables.
- Keep vendor-owned design and equipment supply with the Package Vendor; the construction work package describes installation, tie-in, inspection, and turnover, not switchgear internals.
- Use `TBD` for 830-2 building location/process service, switchgear bus/breaker/protection details, foundation/pile loads, schedule/tie-in windows, and per-circuit cable schedules until source-supported package-specific data is available.
- Use the Deepcut DBM electrical basis only at the level it supports: medium-voltage service, electrical-building housing and installation conventions, grounding/bonding, cable tray, conduit, motor starting, and HVAC.

## Considerations

The Deepcut DBM electrical design basis supports a 4.160 kV, 3-phase, 3-wire, 60 Hz, low-resistance-grounded medium-voltage service basis serving facility process AC inverter-drive motors rated 250 hp up to 5,500 hp, and specifies 5 kV three-conductor copper TECK cable for medium-voltage runs. The 4.16 kV motor starting (VFD/soft-starter) requirements are explicitly TBD in source and must remain TBD here.

The DBM defines electrical buildings as prefabricated modular buildings located in general-purpose areas, elevated on piles to allow bottom-entry cable trays beneath, with n+1 HVAC, TECK/ACIC cabling, EMT conduit between adjacent equipment, an outdoor GFI receptacle, and equipment doors (or removable transom sections) sized for largest-equipment removal. These conventions are the source basis for the construction work package's installation and tie-in scope.

The DBM electrical building list identifies an `830-1 4.16 kV Acid Gas / Overheads Compressor Electrical Building` shipped from shop. It does not separately confirm a `830-2` variant. The construction work package should preserve the workbook designation `830-2` (as `PACKAGE_REGISTER.csv` and Workbook row 35 require) and explicitly note that the building's specific process service and physical location remain TBD pending source confirmation.

Grounding and bonding installation has direct DBM support (two-point ground-grid connection, ground wells with bolted test points, compression-type connections, PVC-conducted above-grade ground wires). These are construction-installable requirements that the package should carry without overstating package-specific conductor sizing.

The Comp_and_Liquids DBM references a separate facility's `4160V MCC` for 4000 V motors fed from a 13.8 kV to 4.16 kV transformer in the 03-25 facility. That is contextual evidence that 4.16 kV switchgear/MCC arrangements exist in the workbook scope, but it is not a substitute for a PKG-033-specific source slice.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| 830-2 building identity | Carry workbook spelling and treat the -2 location/service assignment as TBD. | Workbook row 35 and `PACKAGE_REGISTER.csv` define the name; the DBM list only confirms an 830-1 variant. |
| Switchgear bus / breaker / protection | Mark `TBD` pending vendor package data. | Source set does not contain a package-specific PKG-033 switchgear basis. |
| Foundation/pile design | Reference elevation-on-piles convention; defer pile size/loads to detailed design. | DBM gives convention; not loads. |
| Schedule and tie-in windows | Defer to construction schedule; do not invent windows. | Not present in accessible source. |
| Standards | List CEC, area classification, and project electrical specifications as governing bases with locations TBD. | DBM references these bases; detailed clauses/specs are not in the deliverable folder. |

## Examples

- Acceptable construction-package entry: "Applicable interfaces: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. Source: Workbook Packages row 35 and `INTERFACE_REGISTER.csv`."
- Acceptable source-gap entry: "830-2 building physical location: TBD. DBM electrical building list confirms 830-1 only."
- Not acceptable without new source: "830-2 will be located adjacent to Building 830-1 and house breakers X, Y, Z." The accessible source set does not establish these values.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-033-03-001 | Workbook and Gate 7 registers name the package "4160V SWITCHGEAR ELECTRICAL BUILDING (830-2)", but the DBM electrical building list only enumerates an `830-1 4.16 kV Acid Gas / Overheads Compressor Electrical Building`. | Workbook Packages row 35; `PACKAGE_REGISTER.csv` row `PKG-033` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical building list table | Datasheet Identification/Construction; Specification Scope/Requirements; Procedure Steps | Treat `830-2` as the authoritative package identity per Gate 7 and Workbook; keep the building's process-service assignment and physical location `TBD` until a source slice confirms the -2 variant. | TBD |
| HRR-033-03-002 | The accessible source set does not contain a package-specific switchgear bus, breaker count, protection scheme, or per-circuit cable schedule for PKG-033. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis (general only) | `_REFERENCES.md` (no copied package-specific source slices) | Datasheet Attributes/Construction; Specification Requirements; Procedure Steps | Defer all switchgear bus/breaker/protection and per-circuit construction details to vendor package data and detailed design; do not invent values. | TBD |
