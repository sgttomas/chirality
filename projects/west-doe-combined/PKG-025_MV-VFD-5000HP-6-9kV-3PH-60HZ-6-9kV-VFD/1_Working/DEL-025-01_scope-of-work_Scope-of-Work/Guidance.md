# Guidance: DEL-025-01 Scope of Work

## Purpose

This Scope of Work exists to give the EPC Integrator a bounded, source-traceable package integration basis for PKG-025 (`MV VFD - 5000HP, 6.9kV, 3PH, 60HZ - 6.9kV VFD`) before downstream package datasheet, construction work package, vendor package production, vendor document turnover, and EPC acceptance work proceeds.

The source basis is intentionally narrow. Workbook row 27 establishes the package identity and interface flags. Gate 7 establishes the mandatory EPC anchor deliverable role and the Package Vendor / EPC Integrator responsibility split. The Deepcut DBM provides facility-level 6.9 kV MV service context (distribution voltage, grounding, MV cabling, MV motor starting basis, and electrical building basis). Package-specific MV VFD design details remain `TBD` unless later source material provides them.

## Principles

- Preserve the source spelling `MV VFD - 5000HP, 6.9kV, 3PH, 60HZ - 6.9kV VFD` in identity fields because it is the accepted workbook/Gate 7 package name.
- Treat the Scope of Work as an EPC integration document, not a vendor design document.
- Keep Package Vendor responsibilities (package engineering, design, vendor documentation, physical equipment) separate from EPC Integrator responsibilities (facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, acceptance review).
- Include only source-supported package interfaces (six interface categories per workbook row 27 and Gate 7).
- Use the DBM MV electrical basis as facility context only; do not infer VFD topology, harmonic mitigation, output filtering, input/isolation transformer arrangement, bypass arrangement, enclosure, cooling, or driven-equipment identity from it.
- Prefer `TBD` over inferred technical values where accessible sources do not provide package-specific detail.

## Considerations

The package title identifies a 5,000 hp, 6.9 kV, 3-phase, 60 Hz MV VFD. The DBM identifies the facility 6.9 kV MV bus basis as "facility process AC inverter-drive motors rated 5,500 hp and above," and identifies Starting VFDs for the KM-2150/2250 inlet/sales compressor motors on the 6.9 kV system, where the compressor driver is documented at 6,700 hp. The rating bands in the title (5,000 hp at 6.9 kV) and the DBM (6.9 kV used for 5,500 hp and above) appear inconsistent at a precise level, and the package title rating does not match the inlet/sales compressor driver rating. This is recorded in the Conflict Table; the SOW should not silently bind PKG-025 to the inlet/sales compressor application without human ruling.

The workbook and Gate 7 interface basis flags six interfaces for PKG-025. These interfaces should drive the SOW boundary narrative and later construction coordination. They should not be expanded to additional interface categories unless later accepted sources add them.

## Trade-offs

| Topic | Conservative treatment | Risk if overstated |
|---|---|---|
| Package function | Describe as an MV VFD package serving a 5,000 hp / 6.9 kV / 3PH / 60 Hz process motor; mark driven-equipment identity `TBD`. | The SOW could incorrectly bind PKG-025 to a specific compressor or pump train before source/vendor data confirms it. |
| EPC responsibility | State facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and acceptance review. | EPC scope could accidentally absorb vendor package design obligations. |
| Technical values | Use only source-supported values and `TBD` elsewhere. | Unsupported values (e.g., VFD topology, harmonic filter, bypass) could propagate into datasheets, procurement, or construction packages. |
| Rating reconciliation | Note that 5,000 hp at 6.9 kV (title) is not exactly matched in the DBM rating bands (6.9 kV for 5,500 hp and above) and is not equal to the 6,700 hp inlet/sales compressor driver. Carry to Conflict Table. | Treating the title rating and DBM bands as identical, or binding PKG-025 to the inlet/sales compressor without ruling, would propagate an unsupported equivalence. |
| Source spelling | Preserve the workbook/Gate 7 package name verbatim. | Normalizing punctuation/spelling could break register traceability or appear to alter accepted upstream truth. |

## Examples

- Acceptable SOW language: "PKG-025 is the workbook-defined Electrical package `MV VFD - 5000HP, 6.9kV, 3PH, 60HZ - 6.9kV VFD`, WBS 01, tracking number `26020-01-30-016`; the Package Vendor owns package engineering/design/equipment and the EPC Integrator owns facility integration and interface coordination."
- Acceptable SOW language: "The package interfaces with the facility 6.9 kV, 3-phase, 60 Hz, low-resistance-grounded MV system; the driven-equipment identity, VFD topology, harmonic mitigation, input/isolation transformer arrangement, and bypass arrangement are TBD pending vendor/source data."
- Avoid: "The EPC Integrator shall design the MV VFD package." Gate 7 assigns package engineering and design to the Package Vendor.
- Avoid: "PKG-025 is the Starting VFD for the inlet/sales gas compressors KM-2150/2250." Accessible sources document those compressor drivers at 6,700 hp, not 5,000 hp; binding the package without ruling is unsupported.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HR-025-01 | Driven-equipment identity for PKG-025 is not directly stated. The DBM names Starting VFDs on the 6.9 kV bus for the KM-2150/2250 inlet/sales compressor motors, but those compressor drivers are documented at 6,700 hp rather than 5,000 hp. | DBM Deepcut line 2955 (Starting VFDs for KM-2150/2250 on 6.9 kV MCC); DBM Deepcut line 893 (inlet/sales compressor driver at 6,700 hp). | Workbook Packages row 27 and Gate 7 `PACKAGE_REGISTER.csv` row PKG-025 (package title states 5,000 hp at 6.9 kV). | Datasheet Conditions, Specification Requirements, Guidance Considerations, Procedure Steps. | Do not bind PKG-025 to a specific driven-equipment tag until human ruling; treat title rating as authoritative for package identity and treat DBM MV starter content as facility context only. | TBD |
| HR-025-02 | The DBM states the 6.9 kV MV bus serves "facility process AC inverter-drive motors rated 5,500 hp and above," but the package title rates this VFD at 5,000 hp on 6.9 kV. | DBM Deepcut line 2935 (rating band 5,500 hp and above on 6.9 kV). | Workbook Packages row 27 (title: 5000HP, 6.9kV). | Datasheet Conditions; Specification Standards/Verification. | Carry the apparent rating-band mismatch as a documented inconsistency; do not "correct" the package title; resolve in detailed engineering or accept a documented variance. | TBD |
| HR-025-03 | Package-specific MV VFD design values (topology, output filter / dV/dt, harmonic compliance basis, input/isolation transformer, bypass, cooling, enclosure rating, footprint, weights) are not exposed in accessible sources. | Workbook row 27 gives identity and interface flags only. | DBM electrical sections give facility-level service basis but not package configuration. | Datasheet Conditions, Specification Requirements, Procedure Steps. | Keep all package-specific MV VFD design values as `TBD` pending vendor/source data. | TBD |
