# Guidance: DEL-033-01 Scope of Work

## Purpose

This Scope of Work exists to give the EPC Integrator a bounded, source-traceable package integration basis for PKG-033 (the `4160V SWITCHGEAR ELECTRICAL BUILDING (830-2)`) before downstream package datasheet, construction work package, vendor engineered equipment package, vendor document turnover, and EPC vendor package review and acceptance work proceeds.

The source basis is intentionally narrow. Workbook row 35 establishes the package identity, WBS, tracking number, discipline, and interface flags; Gate 7 establishes the mandatory EPC anchor deliverable and the Package Vendor / EPC Integrator responsibility split; the DBM Comp and Liquids document provides facility-level context for the 13.8 kV incoming feed, the 13.8 kV / 4.16 kV step-down transformer, the 4,160 V service, the 4160V MCC, electrical-building scope, and cable/control separation. Package-specific switchgear and electrical-building design details remain `TBD` unless later source material provides them.

## Principles

- Preserve the source spelling `4160V SWITCHGEAR ELECTRICAL BUILDING (830-2)` in identity fields because it is the accepted workbook/Gate 7 package name.
- Treat the Scope of Work as an EPC integration document, not a vendor design document.
- Keep Package Vendor responsibilities (package engineering, design, vendor documentation, physical equipment) separate from EPC Integrator responsibilities (facility integration, interfaces, tie-ins, constructability, coordination, acceptance).
- Include all twelve source-supported package interfaces from the Gate 7 interface register.
- Use the DBM electrical sections as facility context only; do not infer switchgear bus rating, short-circuit/withstand rating, breaker count, protective relaying scheme, enclosure/NEMA rating, building dimensions, HVAC capacity, or foundation loads from facility-level prose.
- Prefer `TBD` over inferred technical values where accessible sources do not provide package-specific detail.

## Considerations

The package is identified as the 4160V switchgear electrical building (tag `830-2`). The DBM establishes that the 03-25 facility receives 13.8 kV incoming power from 04-25, steps it down through a 13.8 kV / 4.16 kV / 12 MVA transformer, and uses a 4,160 V service for process AC inverter-drive motors from 250 hp to 5,500 hp (the 4160V MCC explicitly serves KM-2150 and KM-2250). This supports identifying the package's facility-level function (housing 4,160 V switchgear and associated distribution within an electrical building) and the integration interfaces, but does not support detailed switchgear lineup or building sizing decisions.

The Gate 7 PKG-033 interface basis is broader than several other packages: twelve interfaces are flagged YES, including Utility Piping, Drain / Containment, Building HVAC, Fire & Gas, Communications / Network, and Area / Exterior Lighting. The SOW should treat each flagged interface as in-scope for EPC coordination even when downstream design details are not yet available. Hazardous area classification coordination (Class I Zone 2 basis, with forced-ventilation monitoring) is a meaningful constraint on building HVAC and electrical equipment selection and should be carried as an integration consideration.

The `830-2` suffix appears to be a building/area tag. The accessible sources do not define `830-2` explicitly; treat it as identity carried from the workbook and surface it as a human ruling item.

## Trade-offs

| Topic | Conservative treatment | Risk if overstated |
|---|---|---|
| Package function | Describe as a 4,160 V switchgear electrical building serving the 03-25 facility MV distribution; mark detailed switchgear lineup, bus/breaker ratings, and protective relaying `TBD`. | The SOW could prematurely fix vendor scope before vendor data is available. |
| EPC responsibility | State facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and acceptance review. | EPC scope could accidentally absorb vendor package engineering/design obligations. |
| Building scope | State that the package includes the electrical building enclosing the 4,160 V switchgear and associated distribution and HVAC, per DBM Electrical Buildings basis; mark building dimensions, HVAC capacity, foundation loads, and ventilation rates `TBD`. | The SOW could incorrectly size or commit to building-level parameters not in the accepted source. |
| Interface scope | Include all twelve Gate 7 YES interfaces, with package-specific values `TBD` where not source-supported. | Reducing the interface set could drop scope; expanding beyond the twelve could exceed accepted source. |
| Source spelling | Preserve `4160V SWITCHGEAR ELECTRICAL BUILDING (830-2)` and the `830-2` tag as written. | Normalizing the spelling or dropping `830-2` could break register traceability. |

## Examples

- Acceptable SOW language: "PKG-033 is the workbook-defined Electrical package `4160V SWITCHGEAR ELECTRICAL BUILDING (830-2)`, WBS 02, tracking number `26020-02-30-024`; the Package Vendor owns package engineering/design/equipment and the EPC Integrator owns facility integration and interface coordination across the twelve Gate 7 YES interfaces."
- Acceptable SOW language: "The 4,160 V service is supplied from a 13.8 kV / 4.16 kV, 12 MVA transformer fed from 04-25; package-specific switchgear bus rating, short-circuit/withstand rating, breaker count and ratings, and protective relaying scheme are TBD pending vendor/source data."
- Avoid: "The EPC Integrator shall design the 4,160 V switchgear lineup." Gate 7 assigns package engineering and design to the Package Vendor.
- Avoid: "The switchgear shall be rated [specific kA short-circuit / bus ampacity]." No accessible source slice supports those values.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HR-033-01 | The `830-2` tag in the package name is not defined in accessible sources (no building register or tag list provides its expanded meaning). | Workbook Packages row 35 and Gate 7 `PACKAGE_REGISTER.csv` row PKG-033. | No accessible glossary or building tag register. | Identity sections; integration narrative. | Preserve `830-2` as accepted package identity; flag for future controlled definition. | TBD |
| HR-033-02 | Package-specific MV switchgear and electrical-building design values (bus rating, short-circuit/withstand, breaker count and ratings, protective relaying, enclosure rating, building dimensions, HVAC capacity, foundation loads, ventilation, fire/gas scheme) are not exposed in accessible sources. | Workbook row 35 gives identity and interface flags only. | DBM Comp and Liquids gives facility-level MV/4,160 V service, transformer feed, 4160V MCC, electrical-building scope, and cable-separation context, but no package-specific switchgear or building configuration. | Datasheet Conditions; Specification Requirements; Procedure Steps. | Treat DBM as facility context and keep package-specific switchgear/building values `TBD` pending vendor/source data. | TBD |
| HR-033-03 | The DBM 4160V MCC section describes a 4160V MCC serving KM-2150/KM-2250; it does not clearly distinguish the MCC equipment from the switchgear lineup expected inside PKG-033. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 752-756 (4160V MCC). | Gate 7 `PACKAGE_REGISTER.csv` row PKG-033 (4160V Switchgear Electrical Building). | Datasheet Attributes/Construction; Specification Scope. | Treat the 4160V MCC as a related but distinct facility element fed from / coordinated with the 4,160 V switchgear; do not assume the MCC is in PKG-033 scope absent confirmation. | TBD |
