# Guidance: DEL-015-04_vendor-engineered-equipment-package

## Purpose

The Vendor Engineered Equipment Package exists to convert the accepted EPC Scope of Work (`DEL-015-01`) and EPC Package Datasheet (`DEL-015-02`) for `PKG-015` into a vendor-owned engineered, designed, fabricated, and supplied physical transformer package. It should keep Package Vendor responsibility for package engineering and equipment distinct from EPC Integrator responsibility for facility integration, tie-ins, and constructability, while preserving the source-supported electrical basis from the DBM.

## Principles

- Preserve source spelling and identity. The package name is carried as "Transformer TXP-8300-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 12/15MVA 13.8kV/4160/2400V" because that is the workbook and Gate 7 register spelling.
- Treat the EPC Scope of Work (`DEL-015-01`) and EPC Package Datasheet (`DEL-015-02`) as the authoritative upstream EPC anchors for the vendor production unit; do not invent vendor scope outside those anchors.
- Carry the seven workbook interface facts as evidence under this vendor production unit; do not promote them to standalone deliverables.
- Use `TBD` for transformer parameters not present in accessible source slices (cooling, vector group, impedance, BIL, tap changer, insulating medium, 2400 V service definition, site environment, hazardous-area classification, factory tests, installation location) until the EPC anchors or vendor design basis supply them.
- Use DBM electrical basis only at the level it supports: 13.8 kV primary feed basis, 4160 V MCC and VFD-motor service basis, power/control circuit segregation, grounding/bonding, cable tray/conduit constraints, and maintenance access.

## Considerations

The DBM voltage/service table and the Incoming Power and Transformers section establish that primary power to 03-25 is sub-fed from the 04-25 13.8 kV Main Switchgear Electrical Building, that 13.8 kV is a 3-phase, 3-wire, 60 Hz LRG service, and that the 4,160 V MCC serves inverter-drive motors from 250 hp to 5,500 hp. The DBM also explicitly lists a "13.8 kV to 4.16 kV, 12 MVA transformer" feeding the 4160V MCC, which is consistent with the 12/15 MVA / 13.8 kV / 4160 V portion of TXP-8300-1's identity, but it does not separately describe a 2400 V service. The 2400 V secondary carried by the package name is therefore not corroborated by the accessible DBM voltage/service table and should be clarified through the EPC anchor deliverables (HRR-015-04-001).

The DBM electrical sections support general design constraints: power/control separation for 13.8 kV, 4,160 V, and 600 V circuits; two-point ground-grid connection for major electrical equipment; separate CEC-sized copper ground conductors for distribution transformers, panelboards, and certain motors; and cable tray/conduit routing that preserves maintenance access. These should be applied as integration constraints on the vendor package without overstating package-specific values that are not in the accessible source set.

The package-specific Word requirements source did not produce a PKG-015 match during this run; detailed transformer cooling class, vector group, impedance, BIL, tap-changer, insulating medium, factory tests, and environmental design conditions therefore remain `TBD` until the EPC Package Datasheet, EPC Scope of Work, or vendor design basis populates them.

The objective associations carried by `_CONTEXT.md` (OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010) come via the package-grouping heuristic at the deliverable level; they are recorded as ASSUMPTION (best-effort mapping) and should not be treated as hard requirements without human confirmation.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| 2400 V secondary service | Carry as named secondary, mark service basis and load list `TBD`. | DBM voltage/service table does not list a 2400 V service; package-name spelling alone does not define the service. |
| Cooling, vector group, impedance, BIL, tap changer, insulating medium | Mark all as `TBD` pending EPC Package Datasheet and vendor design basis. | No accessible source slice supplies these; vendor selection follows EPC anchors and standards. |
| Standards | List CEC, project electrical specifications, area classification, and transformer standards (IEEE C57 / IEC 60076 / CSA) as governing/likely-applicable bases with clause locations TBD. | DBM and EPC scope reference electrical standards; transformer standards are not text-accessible in this run. |
| Installation location | Identify electrical-building / yard context as TBD. | DBM locates the broader 03-25/04-25 buildings but does not assign TXP-8300-1 to a specific pad, building, or yard. |
| Quantity per package | Treat as 1 based on the single TXP-8300-1 tag; record as ASSUMPTION. | Workbook row uses a single tag, but no source explicitly states "Quantity = 1". |

## Examples

- Acceptable datasheet entry: "Primary supply 13.8 kV, 3-phase, 3-wire, 60 Hz LRG, sub-fed from 04-25 Main Switchgear. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Incoming Power and Transformers."
- Acceptable source-gap entry: "Cooling class: TBD. No package-specific source slice available."
- Not acceptable without new source: "Transformer is ONAN/ONAF, 8% impedance, vector group Dyn1, with 5-position DETC tap changer." The accessible source set does not establish these values.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-015-04-001 | Package name carries a 2400 V secondary, but the DBM voltage/service table does not list a 2400 V service. | Workbook Packages row 17; `PACKAGE_REGISTER.csv` row `PKG-015` | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` voltage/service table | Datasheet Attributes; Specification REQ-015-04-003 | Carry 2400 V as a named secondary from package identity, but keep service basis and load list `TBD` pending the EPC Package Datasheet or vendor design basis. | TBD |
| HRR-015-04-002 | DBM lists "13.8 kV to 4.16 kV, 12 MVA transformer" feeding the 4160V MCC, which is consistent with but not explicitly identified as TXP-8300-1; allocation to PKG-015 is inferred. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Incoming Power and Transformers | Workbook Packages row 17; `PACKAGE_REGISTER.csv` row `PKG-015` | Datasheet Attributes; Specification REQ-015-04-003, REQ-015-04-004; Guidance Considerations | Treat the DBM 12 MVA transformer entry as directionally consistent with TXP-8300-1 but require EPC anchors to confirm the tag-to-feeder mapping before fabrication release. | TBD |
