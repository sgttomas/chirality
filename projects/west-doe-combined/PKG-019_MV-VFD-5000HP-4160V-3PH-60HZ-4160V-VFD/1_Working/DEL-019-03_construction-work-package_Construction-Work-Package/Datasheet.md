# Datasheet: Construction Work Package

## Identification

| Field | Value |
|---|---|
| Deliverable ID | `DEL-019-03_construction-work-package` |
| Deliverable name | Construction Work Package |
| Parent package | `PKG-019` - MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD |
| Workbook row | 21 |
| WBS | 02 |
| CoA tracking number | `26020-02-30-009` |
| Discipline | Electrical |
| Responsible party | EPC Integrator |
| Deliverable type | EPC Construction Work Package |
| Scope item | `SOW-0020` |

Sources: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-019-03_construction-work-package`; `PACKAGE_REGISTER.csv` row `PKG-019`.

## Attributes

| Attribute | Current basis | Source |
|---|---|---|
| Package name | MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD | `PACKAGE_REGISTER.csv` row `PKG-019` |
| Package responsibility model | Package Vendor owns package engineering, design, vendor documentation, and physical equipment package; EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility integration. | `PACKAGE_REGISTER.csv` row `PKG-019` |
| Package scope basis | Workbook-defined vendor-owned Electrical package for the MV VFD under WBS 02 with the Package Vendor owning package engineering/design/equipment and the EPC Integrator owning facility integration. | `PACKAGE_REGISTER.csv` row `PKG-019` |
| Applicable interface types | Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports | `PACKAGE_REGISTER.csv` row `PKG-019`; `INTERFACE_REGISTER.csv` rows `IFC-63D8BC58F2`, `IFC-6119784E41`, `IFC-4C2D177FE7`, `IFC-18DDF1CC28`, `IFC-031AC14F4D`, `IFC-FABC00F58B` |
| Construction work package artifacts | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist | `DELIVERABLE_REGISTER.csv` row `DEL-019-03_construction-work-package` |
| Driven equipment context | The 4160V VFD is the starting-VFD basis for inlet compressor motors KM-2150 and KM-2250 (4,000 V, three-phase, 60 Hz, NEMA MG1, TEFC or WPII, Class F insulation/Class B rise, ~891 rpm 8-pole, continuous inverter duty), per SCA-001 VE #34. | `3-25_Comp_and_Liquids_DBM.md` lines 324-326, 533 |
| Source MV electrical system context | The 4160V MCC is fed from the 13.8 kV to 4.16 kV, 12 MVA transformer and serves 4000V motors including KM-2150 and KM-2250; SCA-001 VE #37 removes capacitor banks from the synchronous bus on MCC-8200 where VFDs are present, with harmonic and reactive-power mitigation deferred to detailed electrical studies. | `3-25_Comp_and_Liquids_DBM.md` 4160V MCC section, lines 744-756 |
| Declared upstream dependencies | None declared during PREPARATION | `_DEPENDENCIES.md` |
| Declared downstream dependencies | None declared during PREPARATION | `_DEPENDENCIES.md` |

## Conditions

| Condition | Current basis | Source |
|---|---|---|
| Facility context | 03-25 West Doe Compressor Station and Liquids Hub includes electrical, electrical building, instrumentation, controls, communications, foundations, structural supports, and tie-ins within the broader construction scope. | `3-25_Comp_and_Liquids_DBM.md` Facility Overview; Construction Scope Summary |
| Ambient design implication | The -40 deg C minimum ambient governs exposed equipment, package buildings, control panels, instrumentation, and field devices unless a more severe condition applies. | `3-25_Comp_and_Liquids_DBM.md` SEC-02 Design Implications |
| Geotechnical status | Final geotechnical report is required before foundation design closure; current geotechnical values are placeholders where marked. This bears on VFD enclosure/skid foundations and structural supports. | `3-25_Comp_and_Liquids_DBM.md` SEC-02 Geotechnical and Seismic Basis; SEC-11 Site and Civil Conditions |
| MV starting-VFD basis | KM-2150 and KM-2250 use starting VFDs; soft starts are not the current basis. VFD sizing is an electrical detailed-design item. | `3-25_Comp_and_Liquids_DBM.md` lines 324-326 |
| Harmonic / reactive-power mitigation | Capacitor banks are removed from the synchronous bus on MCC-8200 where VFDs are present; harmonic and reactive-power mitigation shall be determined by detailed electrical studies. | `3-25_Comp_and_Liquids_DBM.md` 4160V MCC section (line 756) |
| MV control/protection | The 4160V MCC provides field-fused contactors, motor protection relays, and an EtherNet port to the plant PLC central control panel for data acquisition; MV breaker control and MV protective relay are UPS-served (120 VAC / 125 VDC). | `3-25_Comp_and_Liquids_DBM.md` 4160V MCC section; UPS services row (line 736) |
| Standards status | Where a standard is referenced but unavailable in the workspace, verify the citation before final issue for construction. | `3-25_Comp_and_Liquids_DBM.md` SEC-15 Specifications, Codes, and Standards |

## Construction

| Construction data item | Value |
|---|---|
| Work package boundary | Physical installation, construction, inspection, turnover, and tie-in of the MV VFD package to the 4160V MCC, the driven compressor motors (KM-2150 / KM-2250), grounding, control cabling, communications/network, structural foundations/supports, and maintenance access. |
| Workface plan minimum contents | Installation sequence, work area limits, equipment offload/setting, tie-in/interface checkpoints (Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports), inspection points, turnover records, and unresolved `TBD` criteria. |
| Interface checklist minimum contents | Electrical Power tie-in checks; Grounding / Bonding checks; I&C / Control Cabling checks (to plant PLC / MCC); Communications / Network checks (EtherNet to plant PLC central control panel); Maintenance Access checks; Structural / Foundations / Supports checks. |
| Detailed VFD ratings (kVA, topology, cooling, enclosure, harmonic filter, output filter, bypass, input transformer) | TBD - not defined in accessible source slices; VFD sizing is an electrical detailed-design item per SCA-001 VE #34. |
| Foundation, structural support, and seismic detailing for the VFD enclosure/skid | TBD - depends on final geotechnical report and vendor equipment loads. |
| Harmonic and reactive-power mitigation requirements | TBD - to be determined by detailed electrical studies per the 4160V MCC basis. |
| Inspection and acceptance criteria | TBD - to be confirmed from IFC electrical drawings, project electrical specifications, vendor commissioning procedures, and protection/coordination studies. |

## References

- `_CONTEXT.md`
- `_DEPENDENCIES.md`
- `_REFERENCES.md`
- Gate 7 `DELIVERABLE_REGISTER.csv`
- Gate 7 `PACKAGE_REGISTER.csv`
- Gate 7 `ARTIFACT_REGISTER.csv`
- Gate 7 `INTERFACE_REGISTER.csv`
- Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv`
- `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`
