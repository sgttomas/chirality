# Specification: DEL-018-01_scope-of-work — Scope of Work

## Scope

This deliverable specifies the EPC scope-of-work content for `PKG-018 — MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD`, a vendor-responsible Electrical WBS 02 package. It covers package identity, source basis, boundaries, applicable interface types, package function, whole-facility integration narrative, and the EPC vs Package Vendor responsibility assignment record.

Included scope:

- Carry SOW-0019: workbook-defined vendor-responsible Electrical package "MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD" as a distinct flat project package for WBS 02 (`SCOPE_LEDGER.csv`, SOW-0019).
- Document the six declared interface types: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports (`INTERFACE_REGISTER.csv`, PKG-018).
- Anchor the medium-voltage service context to the 03-25 DBM electrical basis (4,160 V, 3-phase, 60 Hz, LRG; inverter-drive motor class 250 - 5,500 hp) (`3-25_Comp_and_Liquids_DBM.md`, Electrical SEC).
- Identify missing package-specific design values (VFD topology, sizing, harmonics, motor coordination) as `TBD`.

Excluded or deferred scope:

- Package-specific exclusions are `TBD`; none stated for PKG-018 in `PACKAGE_REGISTER.csv`.
- Package Vendor engineering, design, vendor documentation, and physical equipment supply are scoped to vendor deliverables (DEL-018-04, DEL-018-05) and are not duplicated here.
- Detailed VFD sizing, harmonic and reactive-power mitigation, transformer arrangement, drive cooling, and enclosure rating are detailed-design items and remain `TBD` for the EPC scope of work.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| REQ-018-01-01 | The scope of work shall identify `PKG-018 — MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD` as a vendor-responsible Electrical package under WBS 02 with CoA tracking number `26020-02-30-009`. | `PACKAGE_REGISTER.csv`, PKG-018 |
| REQ-018-01-02 | The scope of work shall identify SOW-0019 as the covered scope item and retain PKG-018 as a distinct flat project package. | `SCOPE_LEDGER.csv`, SOW-0019 |
| REQ-018-01-03 | The scope of work shall include the mandatory EPC scope-of-work artifacts: package scope of work, tagged equipment and package identity list, package function and integration narrative, and responsibility assignment record. | `DELIVERABLE_REGISTER.csv`, DEL-018-01_scope-of-work; `ARTIFACT_REGISTER.csv` PKG-018 rows |
| REQ-018-01-04 | The scope of work shall include the declared interface types: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. | `INTERFACE_REGISTER.csv`, PKG-018 |
| REQ-018-01-05 | The scope of work shall assign Package Vendor responsibility for package engineering, package design, vendor documentation, and the physical equipment package, and EPC Integrator responsibility for facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv`, PKG-018 |
| REQ-018-01-06 | The scope of work shall anchor the medium-voltage electrical interface to the DBM basis of 4,160 V, 3-phase, 3-wire, 60 Hz, LRG service for inverter-drive motors. | `3-25_Comp_and_Liquids_DBM.md`, Electrical SEC Medium-voltage service table |
| REQ-018-01-07 | The scope of work shall require that VFD provisions follow accepted SCAs (SCA-001 VE #34 starting-VFD basis; SCA-001 VE #37 capacitor-bank removal where VFDs are present) and that harmonic and reactive-power mitigation be determined by detailed electrical studies. | `3-25_Comp_and_Liquids_DBM.md`, SCA-001 VE #34 and VE #37 |
| REQ-018-01-08 | The scope of work shall require that controls integration follow the BPCS/RIO platform basis (Allen-Bradley ControlLogix with Flex5000 RIO over PRP). | `3-25_Comp_and_Liquids_DBM.md`, BPCS/RIO platform table |
| REQ-018-01-09 | The scope of work shall require cable separation between 13.8 kV, 4,160 V, and 600 V power circuits and control/instrument circuits per project electrical specifications and detailed design. | `3-25_Comp_and_Liquids_DBM.md`, Electrical SEC cable separation |
| REQ-018-01-10 | Tagged equipment association (driven-motor tag, drive tag, transformer tag) shall remain `TBD` until source-supported mapping is established; ASSUMPTION-level association to the 03-25 MV inverter-drive motor class shall be flagged and not treated as confirmed. | `ARTIFACT_REGISTER.csv` PKG-018 rows; `3-25_Comp_and_Liquids_DBM.md`, Electrical SEC |
| REQ-018-01-11 | The scope of work shall carry package-specific exclusions as `TBD` and require human ruling before final issue if vendor-vs-EPC interface splits are altered. | `PACKAGE_REGISTER.csv`, PKG-018 |

## Standards

| Standard or governing content | Status | Source |
|---|---|---|
| Project electrical specifications (medium-voltage service, MCC, VFD, grounding/bonding, cable separation) | Applicable; clause locations TBD | `3-25_Comp_and_Liquids_DBM.md`, Electrical SEC |
| SCA-001 VE #34 (starting VFD basis for KM-2150 / KM-2250) | Applicable as governing scope-change basis; package mapping ASSUMPTION pending human ruling | `3-25_Comp_and_Liquids_DBM.md`, SCA-001 VE #34 |
| SCA-001 VE #37 (capacitor bank removal where VFDs present) | Applicable | `3-25_Comp_and_Liquids_DBM.md`, SCA-001 VE #37 |
| BPCS/RIO controls platform (Allen-Bradley ControlLogix; Flex5000 RIO; PRP) | Applicable to controls interface | `3-25_Comp_and_Liquids_DBM.md`, BPCS/RIO platform table |
| Harmonic and reactive-power mitigation studies | Required as detailed-design verification; specific standards location TBD | `3-25_Comp_and_Liquids_DBM.md`, VFD/SCA references |
| Vendor data, factory test, and turnover documentation standards | Carried to DEL-018-05 (Vendor Document Turnover) and DEL-018-06 (EPC Review); location TBD here | `DELIVERABLE_REGISTER.csv`, DEL-018-05 / DEL-018-06 |

## Verification

| Requirement IDs | Verification approach |
|---|---|
| REQ-018-01-01 through REQ-018-01-04 | Check identity, deliverable contents, and interface tables against Gate 7 registers and workbook row 20. |
| REQ-018-01-05 | Check responsibility-assignment record against PKG-018 row in `PACKAGE_REGISTER.csv`. |
| REQ-018-01-06 | Check medium-voltage interface narrative against DBM Electrical SEC Medium-voltage service table. |
| REQ-018-01-07 | Confirm SCA-001 VE #34 and VE #37 are cited and that harmonic / reactive-power studies are listed as detailed-design items. |
| REQ-018-01-08 | Check controls interface against BPCS/RIO platform table; require detailed I/O list at vendor handoff (DEL-018-02). |
| REQ-018-01-09 | Check cable-separation requirement against detailed electrical design when available. |
| REQ-018-01-10 | Obtain human ruling on tagged-equipment association (e.g., driven motor tag, drive tag) before final issue. |
| REQ-018-01-11 | Obtain human ruling on any exclusion or interface-split changes before final issue. |

## Documentation

The scope-of-work package shall produce or reference:

- Package scope of work.
- Tagged equipment and package identity list (carrying `TBD` for tag IDs until source-supported mapping is accepted).
- Package function and whole-facility integration narrative.
- Responsibility assignment record (EPC Integrator vs Package Vendor).
- Interface summary for all six declared interface types.
- Source basis and open/TBD item list.
- Human-ruling list for tagged-equipment association and any interface-split changes.
