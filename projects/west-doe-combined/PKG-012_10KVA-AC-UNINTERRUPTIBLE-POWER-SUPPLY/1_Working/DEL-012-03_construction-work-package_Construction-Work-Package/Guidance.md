# Guidance: DEL-012-03 Construction Work Package

## Purpose

This guidance explains how to prepare the construction work package for PKG-012 so that field installation, tie-in, inspection, and turnover are aligned with the accepted Gate 7 package basis and the DBM electrical basis.

## Principles

- Treat the Gate 7 snapshot as accepted upstream truth for package identity, deliverable ownership, artifacts, objectives, and declared interfaces.
- Treat the workbook row and interface X-column facts as the source for construction-facing interface coverage.
- Keep EPC Integrator construction and facility integration responsibilities separate from Package Vendor engineering, design, documentation, and physical equipment supply.
- Use the DBM electrical basis to frame UPS service context, but do not infer final design values not present in the accessible sources.
- Mark unsupported feeder, breaker, cable, battery, mounting, clearance, and test values as TBD until issued design or vendor documents are available.

## Considerations

The construction work package should be organized around field execution readiness: what must be installed, what must be tied in, what must be checked before energization, and what evidence must be turned over. For this package, the source-supported construction interface set is Electrical Power, Grounding / Bonding, Maintenance Access, and Structural / Foundations / Supports.

The DBM identifies UPS services as 120 VAC / 125 VDC for control system, selected emergency/critical lighting, MV breaker control, and MV protective relay. It also distinguishes UPS 10 kVA or smaller from larger UPS services in the voltage/service table. Because the deliverable-specific sources do not provide final equipment configuration or connection details, the construction package should carry placeholders rather than design assumptions.

## Trade-offs

| Topic | Guidance |
|---|---|
| Detail level | Include enough construction detail to support field planning and turnover, but do not create vendor or issued-for-construction design values where the source basis is silent. |
| Interface coverage | Cover each declared interface even when detailed drawings are not yet available; use TBD fields for missing values. |
| Responsibility boundary | Route vendor design, datasheets, and equipment-specific instructions to the vendor package deliverables; keep this deliverable focused on EPC construction execution and integration. |
| Energization readiness | Require verification hooks before energization, but keep final energization criteria TBD where source documents do not state acceptance values. |

## Examples

| Construction package section | Source-grounded content example |
|---|---|
| Interface checklist | Include rows for Electrical Power, Grounding / Bonding, Maintenance Access, and Structural / Foundations / Supports because those interfaces are marked applicable in Workbook Packages row 14 and the Gate 7 interface register. |
| Tie-in plan | State that UPS service context must align with DBM SEC-12 UPS services, while final feeder/circuit details remain TBD pending issued design. |
| Turnover package | Include inspection, interface, tie-in, test, and turnover evidence because ART-DF82A3314B defines construction-facing interface, tie-in, inspection, and turnover evidence. |

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HRR-001 | Package name states "10KVA AC UNINTERRUPTIBLE POWER SUPPLY", while DBM voltage table distinguishes "UPS 10 kVA or smaller" and "UPS larger than 10 kVA"; final service classification for this specific package is not confirmed by a package datasheet or issued design document. | PACKAGE_REGISTER.csv row PKG-012; 26020-Packages_Interfaces_4_export.xlsx row 14 | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md SEC-12 Electrical Basis | Datasheet Conditions; Specification CWP-005/CWP-006; Procedure pre-energization checks | Use package name for identity and DBM SEC-12 only as service-context basis; keep final connection values TBD until issued design/vendor documents confirm. | TBD |
