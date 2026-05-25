# Datasheet: DEL-018-01_scope-of-work — Scope of Work

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-018-01_scope-of-work |
| Deliverable name | Scope of Work |
| Parent package | PKG-018 — MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD |
| Workbook basis | Workbook Packages row 20 |
| WBS | 02 |
| CoA tracking number | 26020-02-30-009 |
| Discipline | Electrical |
| Deliverable type | EPC Scope of Work |
| Responsible party | EPC Integrator |
| Scope item covered | SOW-0019 |
| Supported objectives | OBJ-002; OBJ-004; OBJ-005; OBJ-006; OBJ-008; OBJ-009; OBJ-010 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package role | Workbook-defined vendor-responsible Electrical package carried as a distinct flat project package for WBS 02 | `SCOPE_LEDGER.csv`, SOW-0019 |
| Package scope description | Vendor-owned Electrical package for "MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD" under WBS 02 with package engineering, design, vendor documentation, and physical equipment package by the Package Vendor and facility-level integration by the EPC Integrator | `PACKAGE_REGISTER.csv`, PKG-018 |
| Applicable interface types | Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports | `PACKAGE_REGISTER.csv`, PKG-018; `INTERFACE_REGISTER.csv`, PKG-018 |
| Responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration | `PACKAGE_REGISTER.csv`, PKG-018 |
| Package-specific exclusions | TBD; no package-specific exclusions stated in source materials | `PACKAGE_REGISTER.csv`, PKG-018 |
| Tagged equipment list | TBD; no tagged equipment IDs are listed for PKG-018 in `ARTIFACT_REGISTER.csv`. ASSUMPTION: the MV VFD package supports an inverter-driven medium-voltage motor consistent with the DBM 4,160 V process AC inverter-drive motor class (250 hp - 5,500 hp). Final tagged-equipment association is source-dependent. | `ARTIFACT_REGISTER.csv` PKG-018 rows; `3-25_Comp_and_Liquids_DBM.md`, SEC Electrical (Medium-voltage service table) |

## Conditions

| Condition | Current basis | Source |
|---|---|---|
| Facility context | 03-25 West Doe Compressor Station and Liquids Hub | `3-25_Comp_and_Liquids_DBM.md`, SEC-01 Facility Overview |
| Medium-voltage service basis | 4,160 V, 3 phase, 3 wire, 60 Hz LRG supplying process AC inverter-drive motors from 250 hp to 5,500 hp | `3-25_Comp_and_Liquids_DBM.md`, Electrical SEC Medium-voltage service table (line 733) |
| 4160 V MCC context | 4160 V MCC provides field-fused contactors, motor protection relays, and EtherNet to the plant PLC central control panel; serves large 4000 V motors including inlet compressors KM-2150 and KM-2250 | `3-25_Comp_and_Liquids_DBM.md`, SEC 4160V MCC |
| Upstream transformation | 13.8 kV to 4.16 kV, 12 MVA transformer feeds the 4160V MCC for 4000V motors | `3-25_Comp_and_Liquids_DBM.md`, Electrical SEC transformer table |
| VFD basis | Starting VFDs required by SCA-001 VE #34 for KM-2150 and KM-2250; soft starts are not the current basis. Capacitor banks removed from the synchronous bus on MCC-8200 where VFDs are present (SCA-001 VE #37). Harmonic and reactive-power mitigation determined by detailed electrical studies. ASSUMPTION: PKG-018 implements the medium-voltage VFD scope governed by these SCAs; final mapping is source-dependent. | `3-25_Comp_and_Liquids_DBM.md`, SCA references (VE #34, VE #37) |
| Cable separation | Power circuits at 13.8 kV, 4,160 V, and 600 V shall be separated from control and instrument circuits by distance, shielding, or routing | `3-25_Comp_and_Liquids_DBM.md`, Electrical SEC cable separation |
| Detailed VFD sizing and harmonic studies | TBD; flagged as electrical detailed-design item | `3-25_Comp_and_Liquids_DBM.md`, SCA-001 VE #34 |

## Construction

| Item | Value |
|---|---|
| Scope-of-work deliverable contents | Package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record |
| Boundaries to define | Electrical Power tie-in (4160 V), Grounding / Bonding, I&C / Control Cabling to BPCS, Communications / Network (PRP/EtherNet), Maintenance Access, Structural / Foundations / Supports; EPC vs Vendor split per `PACKAGE_REGISTER.csv` PKG-018 |
| Detailed VFD topology, harmonic mitigation, transformer arrangement, drive cooling, drive enclosure rating, motor coordination, and tie-in coordinates | TBD; not derivable from accessible source slices for PKG-018 specifically |
| Required verification interfaces | 4160 V MCC interface, BPCS/RIO controls interface (Allen-Bradley ControlLogix with Flex5000 RIO over PRP), grounding and bonding, communications, maintenance access, foundations/supports |

## References

- `_CONTEXT.md`, DEL-018-01_scope-of-work.
- `_REFERENCES.md`, DEL-018-01_scope-of-work.
- `_DEPENDENCIES.md`, DEL-018-01_scope-of-work.
- `PACKAGE_REGISTER.csv`, PKG-018.
- `DELIVERABLE_REGISTER.csv`, DEL-018-01_scope-of-work.
- `SCOPE_LEDGER.csv`, SOW-0019.
- `INTERFACE_REGISTER.csv`, PKG-018.
- `ARTIFACT_REGISTER.csv`, DEL-018-01_scope-of-work rows.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, DEL-018-01_scope-of-work.
- `26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 20.
- `3-25_Comp_and_Liquids_DBM.md`, Electrical sections (Medium-voltage service; 4160V MCC; VFD/SCA-001 VE #34, VE #37; cable separation; BPCS/RIO).
