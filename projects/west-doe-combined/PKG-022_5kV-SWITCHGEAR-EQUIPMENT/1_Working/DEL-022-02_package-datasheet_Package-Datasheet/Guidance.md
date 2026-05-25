# Guidance: DEL-022-02_package-datasheet

## Purpose

The Package Datasheet exists to convert the accepted Gate 7 package basis for `PKG-022` into a source-supported technical handoff document. It should let the Package Vendor understand the EPC integration basis for the 5kV SWITCHGEAR EQUIPMENT package while keeping EPC-owned facility interfaces distinct from vendor-owned package design.

## Principles

- Preserve source spelling and identity. The package name is carried as "5kV SWITCHGEAR EQUIPMENT" because that is the workbook and Gate 7 register spelling, even where the DBM nominal voltage levels are stated differently.
- Treat workbook interface `X` facts as evidence under the Package Datasheet, not as separate deliverables.
- Keep vendor-owned design work with the Package Vendor and facility-level integration with the EPC Integrator.
- Use `TBD` for nominal voltage rating, bus ampacity, short-circuit rating, breaker complement, protection-and-control configuration, electrical-building assignment, and physical/support details until a source-supported package-specific basis is available.
- Use DBM electrical basis only at the level it supports: governing equipment specification (`ELC-QAS-000007-001`), facility voltage system, UPS-fed MV breaker control and protective relays, electrical-building housing possibilities, grounding/bonding, cable specifications, and maintenance-access constraints.

## Considerations

The DBM electrical design basis does not literally instantiate a "5 kV" facility distribution level. The medium-voltage backbone is 13.8 kV, with 6.9 kV and 4.160 kV process MV services. The string "5 kV" appears in the DBM cable specification table only as the insulation class of 4.160 kV cables ("Three-conductor copper TECK cable rated 5 kV with 100 percent insulation"). The workbook label "5kV SWITCHGEAR EQUIPMENT" is therefore an identity label whose technical voltage class requires human ruling.

The DBM equipment list identifies "Medium Voltage Switchgear" quantity 1 and identifies an "810-1 13.8kV Switchgear Electrical Building" (shop). Allocation of either line item to `PKG-022` is not confirmed by an accessible source slice.

The DBM electrical and instrumentation specifications table (Table 12-1) identifies `ELC-QAS-000007-001` Medium Voltage Switchgear (Revision 1) as the governing equipment specification and `ELC-QAS-000003-001` Electrical Requirements for Packaged Equipment (Revision 2) as the governing packaged-equipment specification. Both are applicable; their actual document locations are not present in the deliverable folder.

Grounding and bonding are applicable interface topics. The DBM source defines two-point grounding for major electrical equipment, ground wells at electrical buildings, and separate CEC-sized copper ground conductors for certain electrical equipment. The datasheet should require coordination with this basis while avoiding unsupported package-specific conductor sizing or connection details.

Maintenance access, I&C / control cabling, and communications / network are all explicit workbook interface facts and are also DBM routing/architecture constraints. The datasheet should require electrical routing, physical placement, and control/communications connectivity to preserve maintenance access and align with the facility controls architecture, but detailed clearances, signal lists, and network topology remain `TBD`.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Nominal voltage rating | Mark `TBD` and surface as a conflict for human ruling. | Workbook name says "5kV" but DBM does not instantiate a 5 kV distribution level; "5 kV" appears only as 4.16 kV cable insulation class. |
| Switchgear unit allocation | Mark `TBD`. | DBM equipment list shows MV Switchgear quantity 1 and a 13.8 kV Switchgear Electrical Building, but neither is explicitly tied to `PKG-022`. |
| Governing specifications | Cite `ELC-QAS-000007-001` and `ELC-QAS-000003-001` with locations TBD. | Both are named in DBM Table 12-1; documents themselves are not in deliverable folder. |
| Electrical-building location | Identify as possible context, not a confirmed location. | DBM lists multiple buildings that may house switchgear but does not locate `PKG-022`. |
| Cable insulation class | Defer cable insulation selection to nominal voltage resolution. | DBM cable table maps insulation class to nominal voltage; class cannot be chosen before voltage is ruled. |

## Examples

- Acceptable datasheet entry: "Applicable interfaces: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: Workbook Packages row 24 and `INTERFACE_REGISTER.csv`."
- Acceptable source-gap entry: "Nominal voltage rating: TBD pending human ruling on package name versus DBM voltage levels."
- Not acceptable without new source: "Nominal voltage is 5 kV, 3 phase, 3 wire, 60 Hz." The accessible source set does not establish a 5 kV facility distribution level.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-022-02-001 | Workbook/registers call the package "5kV SWITCHGEAR EQUIPMENT", but the DBM medium-voltage system has no "5 kV" distribution level — only 13.8 kV main, 6.9 kV, and 4.160 kV process services; "5 kV" appears only as 4.16 kV cable insulation class. | Workbook Packages row 24; `PACKAGE_REGISTER.csv` row `PKG-022` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, system voltages and cable specifications tables | Datasheet Attributes/Construction; Specification Requirements; Procedure Steps | Treat "5kV" as a workbook identity label only and keep nominal voltage `TBD` until human ruling confirms intended class (likely 4.160 kV given the "5 kV insulation" cable mapping, but not confirmed by source). | TBD |
| HRR-022-02-002 | DBM equipment list shows "Medium Voltage Switchgear" quantity 1 and identifies an "810-1 13.8kV Switchgear Electrical Building" (shop), but allocation of these line items to `PKG-022` is not confirmed. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, equipment list and electrical building list | Workbook Packages row 24; Gate 7 `PACKAGE_REGISTER.csv` | Datasheet Attributes; Specification Requirements | Do not assign quantity, building, or shop/field execution to `PKG-022` until confirmed; record as `TBD`. | TBD |
| HRR-022-02-003 | Governing specifications `ELC-QAS-000007-001` (Medium Voltage Switchgear) and `ELC-QAS-000003-001` (Electrical Requirements for Packaged Equipment) are named in the DBM specifications table but the documents themselves are not present in the deliverable reference set. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical and instrumentation specifications table | `_REFERENCES.md` (no local copies of the QAS documents) | Specification Standards; Datasheet Attributes | Cite the QAS designations as governing with `location TBD`; do not derive clause-level requirements until the documents are accessible. | TBD |
