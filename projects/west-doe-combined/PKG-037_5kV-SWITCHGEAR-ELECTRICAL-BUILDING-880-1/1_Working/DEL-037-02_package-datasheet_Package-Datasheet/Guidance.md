# Guidance: DEL-037-02_package-datasheet

## Purpose

The Package Datasheet exists to convert the accepted Gate 7 package basis for `PKG-037` into a source-supported technical handoff document. It should let the Package Vendor understand the EPC integration basis for the 5kV SWITCHGEAR ELECTRICAL BUILDING (880-1) package while keeping EPC-owned facility interfaces distinct from vendor-owned package design.

## Principles

- Preserve source spelling and identity. The package name is carried as "5kV SWITCHGEAR ELECTRICAL BUILDING (880-1)" because that is the workbook and Gate 7 register spelling.
- Treat workbook interface `X` facts as evidence under the Package Datasheet, not as separate deliverables. All twelve applicable interfaces are carried.
- Keep vendor-owned design work with the Package Vendor (electrical building module fabrication, switchgear/MCC/UPS internals, and vendor documentation) and facility-level integration with the EPC Integrator (tie-ins, foundations, cable routing, grounding to plant grid, utility interfaces).
- Use `TBD` for confirmed bus voltage, building siting, equipment lineups, ratings, and quantities until a source-supported package-specific basis is available.
- Use DBM electrical basis only at the level it supports: building construction, area classification, voltage system table, grounding and bonding, cable tray, conduit, building HVAC, and maintenance access constraints.

## Considerations

The DBM electrical design basis supports building-level facts for prefabricated, modular, pile-elevated, bottom-entry electrical buildings located in general purpose areas, with HVAC sized n + 1 and TECK/ACIC cabling with EMT conduit between adjacent panels. These facts apply to electrical buildings generally and to PKG-037 by inheritance.

The DBM voltage and service table identifies a 13.8 kV facility backbone, 6.9 kV, 4.16 kV, and 600 V distribution classes, and 120 V AC / 125 V DC UPS classes. The DBM medium-voltage cable table identifies three-conductor copper TECK cable "rated 5 kV with 100 percent insulation" associated with 4.16 kV medium-voltage cabling — not a 5 kV switchgear bus class. The DBM Electrical Buildings list enumerates buildings `810-1` (13.8 kV main), `820-1` (6.9 kV), `830-1` (4.16 kV), `840-1` (600 V), `850-1` (600 V), and `860-1` (600 V). The accessible source slices do not establish a "5 kV" switchgear bus or a building `880-1`. The datasheet must therefore preserve the workbook name as identity while marking the technical voltage rating and the `880-1` identifier as `TBD` and surfacing the discrepancy for human ruling.

Grounding and bonding are explicit applicable interface topics. The DBM grounding basis (two-point ground grid connection, ground wells at electrical buildings, compression-type connections, green insulated above-grade conductors in PVC) applies to this building and shall be reflected in the package interface matrix without inventing package-specific conductor sizes.

Maintenance access is both an explicit workbook interface fact and a DBM routing constraint for cable tray and conduit. The datasheet should require electrical routing and physical placement to preserve maintenance access, and require doors sized for the largest installed equipment (or removable transom sections). Detailed clearances remain `TBD` unless issued by detailed design or vendor data.

The package-specific Word requirements source did not produce a PKG-037 match during this run; therefore, vendor-facing datasheet content should remain conservative until the missing detailed requirements are resolved.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| "5kV" voltage class | Treat "5kV" as the package title token only and mark the confirmed switchgear bus voltage `TBD`. | DBM voltage table lists 13.8 kV, 4.16 kV, and 600 V switchgear/MCC classes; the only "5 kV" appearance is the TECK cable insulation rating associated with 4.16 kV cabling. |
| Building identifier `880-1` | Carry as workbook identity; mark physical building assignment `TBD`. | DBM Electrical Buildings list enumerates 810/820/830/840/850/860 series buildings; `880-1` is not in the accessible source slice. |
| Internal equipment lineup | List allowable equipment classes from DBM; mark PKG-037-specific lineup `TBD`. | DBM enumerates electrical-building allowable content but does not assign a specific lineup to PKG-037. |
| Standards | List CEC, area classification, and project electrical specifications as governing bases with locations `TBD`. | DBM references these bases but detailed clauses/specification documents are not available in the deliverable folder. |
| Building siting | Identify "general purpose area" as the required classification; mark siting coordinates `TBD`. | DBM states electrical buildings shall be located in general purpose areas but does not place `880-1`. |

## Examples

- Acceptable datasheet entry: "Applicable interfaces: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. Source: Workbook Packages row 39 and `INTERFACE_REGISTER.csv`."
- Acceptable source-gap entry: "Switchgear bus voltage: TBD. DBM voltage table does not establish a 5 kV switchgear class; reconciliation pending."
- Not acceptable without new source: "Building 880-1 houses 5 kV switchgear at <rating> A." The accessible source set does not establish a 5 kV bus or this building's lineup.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-037-02-001 | Workbook/PACKAGE_REGISTER name asserts a "5kV" switchgear class, but the DBM voltage table establishes 13.8 kV, 4.16 kV, and 600 V switchgear/MCC classes; the only "5 kV" appearance is the TECK cable insulation rating associated with 4.16 kV cabling. | Workbook Packages row 39; `PACKAGE_REGISTER.csv` row `PKG-037` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical voltage/service table and medium-voltage cable table | Datasheet Identification/Attributes; Specification Requirements REQ-037-02-005; Procedure Steps | Carry "5kV" as workbook identity only; mark confirmed bus voltage `TBD` until reconciled by detailed design or accepted source update. | TBD |
| HRR-037-02-002 | Workbook/PACKAGE_REGISTER references building `880-1`, but the DBM Electrical Buildings list enumerates buildings `810-1`, `820-1`, `830-1`, `840-1`, `850-1`, and `860-1` only. | Workbook Packages row 39; `PACKAGE_REGISTER.csv` row `PKG-037` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings list | Datasheet Identification/Attributes; Specification Requirements REQ-037-02-006; Procedure Steps | Carry `880-1` as workbook identity; mark physical building assignment `TBD` pending reconciliation. | TBD |
| HRR-037-02-003 | Internal equipment lineup (switchgear, MCC, UPS, transformer, panel, network rack) for PKG-037 is not established by an accessible source slice; the package-specific Word requirements source produced no PKG-037 match. | `PACKAGE_REGISTER.csv` row `PKG-037`; Workbook Packages row 39 | `_Sources/26020-Package_Requirements.docx` (no PKG-037 match); `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings allowable-content paragraph | Datasheet Attributes/Construction; Specification Requirements REQ-037-02-010 | Mark detailed lineup `TBD`; do not assign quantities, ratings, or BoM until vendor data or detailed source is accepted. | TBD |
