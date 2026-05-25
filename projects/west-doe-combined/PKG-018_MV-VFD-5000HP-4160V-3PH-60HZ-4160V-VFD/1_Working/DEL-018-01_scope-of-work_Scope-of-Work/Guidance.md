# Guidance: DEL-018-01_scope-of-work — Scope of Work

## Purpose

This guidance supports drafting and review of the `PKG-018 — MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD` EPC scope of work. The deliverable exists to turn the accepted decomposition basis for SOW-0019 into a bounded Electrical package scope with clear interfaces, source basis, EPC vs Package Vendor responsibility assignment, and integration narrative.

## Principles

- Preserve the Gate 7 package identity exactly: `PKG-018`, "MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD", Electrical, WBS 02, CoA tracking number `26020-02-30-009` (`PACKAGE_REGISTER.csv`, PKG-018).
- Treat the workbook row and Gate 7 registers as authoritative for package membership and deliverable identity.
- Use the 03-25 DBM Electrical sections as the source for medium-voltage service basis, 4160 V MCC context, VFD-related SCAs, BPCS/RIO controls platform, and cable separation requirements.
- Use `TBD` for package-specific design values not present in accessible sources (drive topology, sizing, harmonic mitigation, transformer arrangement, motor coordination, tagged-equipment IDs).
- Keep the EPC vs Package Vendor responsibility split conservative and aligned to `PACKAGE_REGISTER.csv` PKG-018; do not redistribute scope between EPC and vendor without source or human ruling.

## Considerations

PKG-018 is a vendor-responsible Electrical package whose facility-level integration is owned by the EPC Integrator. The scope of work should focus on (1) identity and source basis, (2) the six declared interfaces, (3) the EPC vs Vendor responsibility split, and (4) the facility integration narrative tying the MV VFD into the 4160 V MCC, the 13.8 kV / 4.16 kV transformer chain, the BPCS/RIO controls platform, and the grounding, communications, structural, and maintenance interfaces.

The 03-25 DBM medium-voltage service basis explicitly supports inverter-drive motors from 250 hp to 5,500 hp at 4,160 V, 3-phase, 60 Hz — which is consistent with a 5,000 hp 4160 V VFD. The DBM also names KM-2150 and KM-2250 (inlet compressors) as the 4000 V motors served by the 4160 V MCC, with starting VFDs required by SCA-001 VE #34. Whether PKG-018 supplies one of these compressor-motor drives, a different MV VFD, or a generic vendor MV VFD scope is not closed by accessible source material. Treat tag-level association as `TBD` and flag the SCA association as ASSUMPTION.

The DBM describes KM-2150 / KM-2250 motors as 4,000 V three-phase 60 Hz machines fed from a 4160 V MCC, while the PKG-018 title labels the VFD as "4160V". This is consistent with normal MV practice (4160 V system / 4000 V motor) but should be confirmed during vendor handoff.

## Trade-offs

| Topic | Guidance |
|---|---|
| Early scope completeness vs source fidelity | Include the required EPC scope-of-work structure now; leave drive topology, sizing, and tagged-equipment IDs as `TBD`. |
| Tag association of PKG-018 to specific motors | Do not assert that PKG-018 supplies the KM-2150 or KM-2250 starting VFDs; carry the SCA-001 VE #34 reference as ASSUMPTION-level context. |
| EPC vs Vendor split | Follow `PACKAGE_REGISTER.csv` PKG-018 verbatim; do not infer vendor scope into EPC scope or vice versa. |
| Harmonics / reactive power | Carry as detailed-design items per SCA-001 VE #34 / VE #37; do not propose mitigation methods in the scope of work. |
| Interface inclusion | Include all six declared interfaces; do not add or remove interface types not present in `INTERFACE_REGISTER.csv` PKG-018. |

## Examples

- Acceptable wording: "The package includes Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports interfaces, per Gate 7 interface register."
- Acceptable wording: "Driven-motor tag, drive tag, and transformer arrangement are TBD pending vendor handoff and human ruling on tagged-equipment association."
- Avoid: "The MV VFD shall supply KM-2150" unless human ruling associates the package to a specific compressor tag.
- Avoid: "EPC Integrator shall perform vendor engineering" — the package register assigns vendor engineering to the Package Vendor.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-018-01-001 | Tagged equipment association for PKG-018 is unresolved: no specific motor or drive tag is mapped to PKG-018 in the artifact register, yet the DBM names KM-2150 / KM-2250 as 4000V inlet compressors with starting VFDs under SCA-001 VE #34. | `ARTIFACT_REGISTER.csv` PKG-018 rows (no tagged-equipment IDs) | `3-25_Comp_and_Liquids_DBM.md`, SCA-001 VE #34 and 4160V MCC narrative (KM-2150/KM-2250) | Datasheet Identification/Attributes; Specification Requirements REQ-018-01-10; Procedure Step on tagged-equipment list | Carry tag-association as TBD; flag SCA-001 VE #34 as ASSUMPTION-level context until human ruling. | TBD |
| HRR-018-01-002 | Package title says "4160V VFD"; DBM motor data for KM-2150 / KM-2250 says 4,000 V at the motor. | `PACKAGE_REGISTER.csv`, PKG-018 (title); workbook row 20 | `3-25_Comp_and_Liquids_DBM.md`, 4160V MCC section (4000 V motors) | Datasheet Identification; Specification REQ-018-01-06; Guidance Considerations | Treat as standard MV system/motor convention (4160 V system feeding 4000 V motors) and retain both values verbatim; require vendor confirmation at handoff. | TBD |
| HRR-018-01-003 | Package-specific exclusions for PKG-018 are not stated in source materials. | `PACKAGE_REGISTER.csv`, PKG-018 (exclusions TBD) | None | Datasheet Attributes; Specification Scope / REQ-018-01-11 | Carry exclusions as TBD and require human ruling before any interface-split change. | TBD |
