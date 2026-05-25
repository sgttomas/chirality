# Guidance: DEL-013-01 Scope of Work

## Purpose

This Scope of Work exists to give the EPC Integrator a bounded, source-traceable package integration basis for PKG-013 before downstream package datasheet, construction work package, vendor package production, vendor document turnover, and EPC acceptance work proceeds.

The source basis is intentionally narrow. Workbook row 15 establishes the package identity and interface flags; Gate 7 establishes the mandatory EPC anchor deliverable and the Package Vendor / EPC Integrator responsibility split; the DBM provides facility-level UPS service context. Package-specific UPS design details remain `TBD` unless later source material provides them.

## Principles

- Preserve the source spelling `100A DC UNINTERUPTIBLE POWER SUPPLY` in identity fields because it is the accepted workbook/Gate 7 package name.
- Treat the Scope of Work as an EPC integration document, not a vendor design document.
- Keep Package Vendor responsibilities separate from EPC Integrator responsibilities.
- Include only source-supported package interfaces.
- Use the DBM UPS service basis as facility context only; do not infer capacity, autonomy, battery chemistry, charger quantity, or enclosure configuration from it.
- Prefer `TBD` over inferred technical values where accessible sources do not provide package-specific detail.

## Considerations

The package title indicates a 100A DC uninterruptible power supply, and the DBM identifies UPS services as 120 VAC / 125 VDC for control system, selected emergency/critical lighting, MV breaker control, and MV protective relay. This supports including facility UPS service context in the Scope of Work. It does not support assuming battery autonomy, charger topology, panel lineup, distribution board details, or vendor equipment configuration.

The workbook and Gate 7 interface basis flags Electrical Power, Grounding / Bonding, Maintenance Access, and Structural / Foundations / Supports. These interfaces should drive the SOW boundary narrative and later construction coordination. They should not be expanded to additional interface categories unless later accepted sources add them.

## Trade-offs

| Topic | Conservative treatment | Risk if overstated |
|---|---|---|
| Package function | Describe as a DC uninterruptible power supply package serving facility UPS/electrical integration context; mark detailed load/service assignments `TBD`. | The SOW could incorrectly allocate loads or define vendor scope before vendor data is available. |
| EPC responsibility | State facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and acceptance review. | EPC scope could accidentally absorb vendor package design obligations. |
| Technical values | Use only source-supported values and `TBD` elsewhere. | Unsupported values could propagate into datasheets, procurement, or construction packages. |
| Source spelling | Preserve `UNINTERUPTIBLE` as the accepted package name and note the source-derived spelling. | Normalizing the spelling could break register traceability or appear to alter accepted upstream truth. |

## Examples

- Acceptable SOW language: "PKG-013 is the workbook-defined Electrical package `100A DC UNINTERUPTIBLE POWER SUPPLY`, WBS 02, tracking number `26020-02-30-004`; the Package Vendor owns package engineering/design/equipment and the EPC Integrator owns facility integration and interface coordination."
- Acceptable SOW language: "Package-specific UPS capacity confirmation, autonomy, battery type, charger configuration, and distribution details are TBD pending vendor/source data."
- Avoid: "The EPC Integrator shall design the UPS package." Gate 7 assigns package engineering and design to the Package Vendor.
- Avoid: "The UPS shall have [specific autonomy or battery type]." No accessible source slice supports those values.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HR-013-01 | Package name appears to contain the spelling `UNINTERUPTIBLE`; standard spelling would normally be `UNINTERRUPTIBLE`. | Workbook Packages row 15 and Gate 7 `PACKAGE_REGISTER.csv` row PKG-013 use `100A DC UNINTERUPTIBLE POWER SUPPLY`. | Common technical spelling, not an accepted project source. | Identity fields in all four documents. | Preserve accepted source spelling for traceability; optionally add a future controlled alias only by human ruling. | TBD |
| HR-013-02 | Package-specific UPS design values are not exposed in accessible sources. | Workbook row 15 gives identity and interface flags only. | DBM electrical table gives facility UPS services as 120 VAC / 125 VDC, but not package-specific configuration. | Datasheet Conditions, Specification Requirements, Procedure Steps. | Treat DBM as facility context and keep package-specific technical values as `TBD` pending vendor/source data. | TBD |
