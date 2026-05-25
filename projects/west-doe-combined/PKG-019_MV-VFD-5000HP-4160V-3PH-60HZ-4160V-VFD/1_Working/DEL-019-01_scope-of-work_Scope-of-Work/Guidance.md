# Guidance: DEL-019-01 Scope of Work

## Purpose

This Scope of Work exists to give the EPC Integrator a bounded, source-traceable package integration basis for PKG-019 (`MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD`) before downstream package datasheet, construction work package, vendor package production, vendor document turnover, and EPC acceptance work proceeds.

The source basis is intentionally narrow. Workbook row 21 establishes the package identity and interface flags; Gate 7 establishes the mandatory EPC anchor deliverable role and the Package Vendor / EPC Integrator responsibility split; the DBM Comp and Liquids electrical sections provide MV electrical facility context (13.8 kV / 4.16 kV / 12 MVA transformer feeding the 4160V MCC; inlet compressor motors with starting-VFD basis per SCA-001 VE #34). Package-specific VFD design details remain `TBD` unless later source material provides them.

## Principles

- Preserve the source package name `MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD` in identity fields because it is the accepted workbook/Gate 7 spelling.
- Treat the Scope of Work as an EPC integration document, not a vendor design document.
- Keep Package Vendor responsibilities (package engineering, design, vendor documentation, equipment supply) separate from EPC Integrator responsibilities (integration, interfaces, tie-ins, constructability, procurement/construction coordination, acceptance).
- Include only source-supported package interfaces (the six listed for PKG-019).
- Use the DBM MV electrical basis as facility context only; do not infer drive topology, harmonic filter design, transformer/reactor configuration, enclosure, cooling, or footprint from it.
- Prefer `TBD` over inferred technical values where accessible sources do not provide package-specific detail.
- Do not silently reconcile the voltage / horsepower mismatch between the package title and the DBM motor basis; carry it as a human ruling item.

## Considerations

The package title indicates a medium-voltage VFD rated 5000 HP at 4160 V, 3-phase, 60 Hz, intended for the 4160V system. The DBM identifies the inlet compressor motors served by the 4160V MCC as 4,000 V, three-phase, 60 Hz, approximately 3,878 kW / 5,200 hp continuous-inverter-duty motors with starting VFDs per SCA-001 VE #34. The package likely supports these or analogous large 4000V-class motors, but the accessible sources do not state explicit allocation, count, redundancy, or starting-vs-running duty for the PKG-019 VFD(s). Carry these as `TBD` and surface the voltage/horsepower mismatch for human ruling.

The workbook and Gate 7 interface basis flags Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. These should drive the SOW boundary narrative and later construction coordination, and align with the DBM EtherNet-to-plant-PLC basis for the 4160V MCC for the Communications/Network interface. They should not be expanded to additional interface categories unless later accepted sources add them.

The DBM also notes SCA-001 VE #37 removes capacitor banks from the synchronous bus on MCC-8200 where VFDs are present, and that harmonic / reactive-power mitigation shall be determined by detailed electrical studies. The Scope of Work should reference this as a facility-level integration consideration without prescribing harmonic-mitigation design choices.

## Trade-offs

| Topic | Conservative treatment | Risk if overstated |
|---|---|---|
| Driven-equipment allocation | Reference the DBM inlet compressor motor basis as facility context; keep PKG-019 driven-equipment tags `TBD`. | The SOW could pre-allocate VFDs to specific motor tags before vendor or facility integration data confirms it. |
| Drive rating / voltage / HP | Carry the package title rating as identity; record the DBM 4,000 V / 5,200 HP motor basis as facility context; flag mismatch for human ruling. | Picking one figure could silently overwrite accepted upstream truth or vendor design intent. |
| EPC responsibility | State facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and acceptance review. | EPC scope could accidentally absorb vendor VFD design obligations. |
| Harmonic / reactive mitigation | Reference SCA-001 VE #37 and the DBM detailed-study requirement; do not prescribe filter topology. | Premature filter/topology choices could conflict with later detailed electrical studies. |
| Technical values | Use only source-supported values and `TBD` elsewhere. | Unsupported values could propagate into datasheets, procurement, or construction packages. |

## Examples

- Acceptable SOW language: "PKG-019 is the workbook-defined Electrical package `MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD`, WBS 02, tracking number `26020-02-30-009`; the Package Vendor owns package engineering/design/vendor documentation/equipment and the EPC Integrator owns facility integration and interface coordination."
- Acceptable SOW language: "The DBM identifies a 13.8 kV to 4.16 kV / 12 MVA transformer feeding the 4160V MCC, which serves large 4000V motors with starting VFDs per SCA-001 VE #34; package-specific VFD allocation to specific motor tags is TBD."
- Acceptable SOW language: "Drive topology, harmonic mitigation, transformer/reactor configuration, enclosure, cooling, weights, and footprint are TBD pending vendor/source data."
- Avoid: "The EPC Integrator shall design the VFD package." Gate 7 assigns package engineering and design to the Package Vendor.
- Avoid: "The VFD shall be rated 5000 HP at 4160 V driving motors `KM-2150` / `KM-2250`." Allocation is not confirmed in accessible sources, and the DBM motor basis is 4,000 V / ~5,200 HP.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HR-019-01-01 | Package title rating (5000 HP / 4160 V) differs from DBM motor basis (~5,200 HP / 4,000 V). | Gate 7 `PACKAGE_REGISTER.csv` row PKG-019; workbook Packages row 21. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 324, 744, 752. | Datasheet Identification/Conditions, Specification Requirements SOW-019-07/10, Procedure verification steps. | Preserve accepted package name as identity; carry DBM motor basis as facility context; do not normalize either value until human/vendor ruling. | TBD |
| HR-019-01-02 | Tagged equipment allocation (whether PKG-019 VFDs serve inlet compressor motors `KM-2150` / `KM-2250` and at what count / duty / redundancy) is not stated in accessible sources. | Workbook Packages row 21; Gate 7 `PACKAGE_REGISTER.csv` row PKG-019. | DBM Comp and Liquids lines 324-326, 533, 752-756 (motors and starting-VFD basis only). | Datasheet Attributes (tagged equipment), Specification SOW-019-10, Procedure Steps. | Keep tagged equipment `TBD` until source data confirms VFD-to-motor allocation. | TBD |
| HR-019-01-03 | SCA-001 (VE #34 starting-VFD requirement; VE #37 capacitor-bank removal where VFDs are present) is cited by the DBM but the SCA-001 document text is not directly accessible in the source set. | DBM Comp and Liquids lines 326, 533, 756. | No directly accessible SCA-001 document. | Datasheet Conditions, Specification Standards, Guidance Considerations. | Cite SCA-001 via the DBM; mark direct location TBD; do not derive clause-level requirements. | TBD |
