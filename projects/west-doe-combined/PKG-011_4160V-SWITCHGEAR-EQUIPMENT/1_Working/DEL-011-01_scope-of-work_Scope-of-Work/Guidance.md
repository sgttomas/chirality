# Guidance: DEL-011-01 Scope of Work

## Purpose

The Scope of Work exists to anchor the PKG-011 package before vendor production, construction planning, and EPC acceptance activities proceed. It should make the package identity, function, responsibility split, and whole-facility interfaces explicit enough that downstream package datasheet, construction work package, vendor engineered equipment package, vendor document turnover, and EPC vendor package review deliverables preserve the same boundaries.

Source: Gate 7 `PROJECT_DECOMP.md` Section 7; Gate 7 `DELIVERABLE_REGISTER.csv` row DEL-011-01; Gate 7 `SCOPE_LEDGER.csv` row SOW-0012.

## Principles

- Preserve workbook authority. PKG-011 is carried from Workbook Packages row 13 as a distinct flat project package and should not be merged with other switchgear or electrical packages. Source: Gate 7 `PROJECT_DECOMP.md` Decision DEC-001; Gate 7 `SCOPE_LEDGER.csv` row SOW-0012.
- Keep the vendor/EPC boundary explicit. The vendor owns package engineering/design/equipment/documentation; the EPC Integrator owns integration and interface coordination. Source: Gate 7 `PACKAGE_REGISTER.csv` row PKG-011.
- Use interface facts as boundaries, not separate packages. PKG-011 interface facts should be listed and managed as integration constraints. Source: Gate 7 `PROJECT_DECOMP.md` Decision DEC-003; Gate 7 `INTERFACE_REGISTER.csv` PKG-011 rows.
- Use DBM electrical basis where it directly supports switchgear/MCC context, but do not turn unresolved DBM items into completed design values. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 unresolved electrical basis table.

## Considerations

The scope should distinguish package-level responsibility from facility-level integration. For example, the 03-25 DBM states that the 4160V MCC provides field-fused contactors, motor protection relays, and an EtherNet communication port to the plant PLC central control panel for data acquisition. The Scope of Work can use that as interface context, but final MCC design, ratings, and studies should remain with the appropriate vendor/design deliverables unless explicitly assigned. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 `4160V MCC`.

The shared 04-25/03-25 power basis may affect how PKG-011 is integrated. The 03-25 DBM describes incoming power from 04-25 and a 13.8 kV to 4.16 kV transformer feeding the 4160V MCC for 4000V motors. The 04-25 DBM also records shared power coordination items as unresolved. Treat these as coordination and `TBD` items unless later source material closes them. Sources: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 `Incoming Power and Transformers`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 unresolved electrical basis table.

## Trade-offs

| Topic | Guidance |
|---|---|
| Detail versus boundary control | Include enough technical basis to identify the package and interfaces, but avoid replacing vendor engineering or detailed electrical studies. |
| Interface completeness versus overclaiming | List all Gate 7 declared interface categories, but mark detailed interface values `TBD` if they are not present in accessible source slices. |
| Standards citation versus clause-level requirements | Cite governing standards and project specification families from the DBM; do not derive clause-level requirements without the actual standard/specification text. |
| Scope closure versus source gaps | Use `TBD` for package-specific exclusions, ratings, and unresolved electrical coordination items where source materials do not close them. |

## Examples

Acceptable scope wording pattern:

> PKG-011 is a vendor-responsible Electrical package for 4160V switchgear equipment under WBS 02. The Package Vendor owns package engineering, design, documentation, and equipment supply. The EPC Integrator owns facility integration, including electrical power, grounding/bonding, I&C/control cabling, communications/network, maintenance access, and structural/foundation/support interfaces.

Source basis: Gate 7 `PACKAGE_REGISTER.csv` row PKG-011 and Gate 7 `INTERFACE_REGISTER.csv` PKG-011 rows.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-001 | Whether PKG-011 Scope of Work should define package-specific exclusions beyond `TBD`. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-011: package-specific exclusions are `TBD`; no source-specific exclusions stated. | No copied deliverable-specific source slice available in `_REFERENCES.md`. | Datasheet Conditions; Specification Scope; Procedure Verification | Keep exclusions as `TBD` until a human or later source slice identifies package-specific exclusions. | TBD |
| HRR-002 | Whether 4.16 kV motor starting requirements for PKG-011 are closed or remain design-development `TBD`. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12: SCA-001 VE #34 requires starting VFDs for KM-2150 and KM-2250. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 unresolved electrical basis table: 4.16 kV motor starting VFD and soft-starter requirements are `TBD`. | Specification Requirements; Procedure Verification | Treat KM-2150/KM-2250 starting VFD basis as source-supported for those motors, but keep broader 4.16 kV motor starting requirements as `TBD`. | TBD |
