# Guidance: DEL-028-04_vendor-engineered-equipment-package

## Purpose

The Vendor Engineered Equipment Package exists to convert the accepted EPC Scope of Work (`DEL-028-01`) and EPC Package Datasheet (`DEL-028-02`) for `PKG-028` into a vendor-owned engineered, designed, fabricated, and supplied physical transformer package. It should keep Package Vendor responsibility for package engineering and equipment distinct from EPC Integrator responsibility for facility integration, tie-ins, and constructability, while preserving the source-supported electrical basis from the Deepcut DBM.

## Principles

- Preserve source spelling and identity. The package name is carried as "Transformer TXP-8801-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 7.5MVA 13.8kV/4160/2400V" because that is the workbook and Gate 7 register spelling.
- Treat the EPC Scope of Work (`DEL-028-01`) and EPC Package Datasheet (`DEL-028-02`) as the authoritative upstream EPC anchors for the vendor production unit; do not invent vendor scope outside those anchors.
- Carry the seven workbook interface facts as evidence under this vendor production unit; do not promote them to standalone deliverables.
- Use `TBD` for transformer parameters not present in accessible source slices (cooling, vector group, impedance, BIL, tap changer, insulating medium, 4160 V and 2400 V service definitions, site environment, hazardous-area classification, factory tests, installation location) until the EPC anchors or vendor design basis supply them.
- Use Deepcut DBM electrical basis only at the level it supports: 13.8 kV facility distribution and primary feed basis, transformer general practice (spacing, foundations, containment review), grounding/bonding, and maintenance access constraints.

## Considerations

The Deepcut DBM facility electrical system narrative establishes that the 4-25 facility is fed from a BC Hydro utility supply through a 25 kV to 13.8 kV, 50 MVA utility-supplied transformer to a local 13.8 kV switchgear bus, and that the 13.8 kV switchgear distributes radially through step-down transformers to facility electrical buildings. The medium-voltage service basis is 13.8 kV, 3-phase, 3-wire, 60 Hz LRG. These slices support a primary-feed basis for TXP-8801-1 but do not identify the package by tag or assign a specific feeder.

The Deepcut DBM voltage/service table lists 13.8 kV medium-voltage service and 600 V low-voltage service, but does not list 4,160 V or 2,400 V service tiers. The 4160 V and 2400 V secondaries carried in the TXP-8801-1 package name are therefore not corroborated by the accessible Deepcut DBM voltage/service table and should be clarified through the EPC anchor deliverables (HRR-028-04-001).

The DBM Transformers section supports general design constraints: large oil-filled transformers shall be spaced per CEC, generally installed on structural steel transformer bases or precast concrete bearing foundations, and selection should aim to avoid or limit secondary-containment requirements where practical. The grounding/bonding paragraphs support two-point ground-grid connection for major electrical equipment and separate CEC-sized copper ground conductors for distribution transformers, panelboards, and three-phase motors larger than 100 hp. These apply as integration constraints on the TXP-8801-1 vendor package without overstating package-specific values.

The package-specific Word requirements source did not produce a PKG-028 match during this run; detailed transformer cooling class, vector group, impedance, BIL, tap-changer, insulating medium, factory tests, and environmental design conditions therefore remain `TBD` until the EPC Package Datasheet, EPC Scope of Work, or vendor design basis populates them.

The objective associations carried by `_CONTEXT.md` (OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010) come via the package-grouping heuristic at the deliverable level; they are recorded as ASSUMPTION (best-effort mapping) and should not be treated as hard requirements without human confirmation.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| 4160 V and 2400 V secondary services | Carry as named secondaries from package identity, mark service basis and load lists `TBD`. | Deepcut DBM voltage/service table does not list 4,160 V or 2,400 V services; package-name spelling alone does not define the services. |
| Cooling, vector group, impedance, BIL, tap changer, insulating medium | Mark all as `TBD` pending EPC Package Datasheet and vendor design basis. | No accessible source slice supplies these; vendor selection follows EPC anchors and standards. |
| Insulating medium and containment | If oil-filled is selected, apply CEC spacing and secondary-containment review per DBM general practice; bias toward limiting containment where practical. | DBM Transformers section explicitly directs this conservative selection posture. |
| Standards | List CEC, project electrical specifications, area classification, and transformer standards (IEEE C57 / IEC 60076 / CSA) as governing/likely-applicable bases with clause locations TBD. | DBM and EPC scope reference electrical standards; transformer standards are not text-accessible in this run. |
| Installation location | Identify electrical-building / yard context as TBD. | DBM describes the 4-25 facility and 880-1 area in general terms but does not assign TXP-8801-1 to a specific pad, building, or yard. |
| Quantity per package | Treat as 1 based on the single TXP-8801-1 tag; record as ASSUMPTION. | Workbook row uses a single tag, but no source explicitly states "Quantity = 1". |

## Examples

- Acceptable datasheet entry: "Primary supply 13.8 kV, 3-phase, 3-wire, 60 Hz LRG from the Deepcut 4-25 facility 13.8 kV distribution. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` facility electrical system narrative."
- Acceptable source-gap entry: "Cooling class: TBD. No package-specific source slice available."
- Not acceptable without new source: "Transformer is ONAN/ONAF, 7% impedance, vector group Dyn1, with 5-position DETC tap changer." The accessible source set does not establish these values.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-028-04-001 | Package name carries 4160 V and 2400 V secondaries, but the Deepcut DBM voltage/service table does not list 4,160 V or 2,400 V services. | Workbook Packages row 30; `PACKAGE_REGISTER.csv` row `PKG-028` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` voltage/service table | Datasheet Attributes; Specification REQ-028-04-003 | Carry 4160 V and 2400 V as named secondaries from package identity, but keep service basis and load lists `TBD` pending the EPC Package Datasheet or vendor design basis. | TBD |
| HRR-028-04-002 | The Deepcut DBM does not identify TXP-8801-1 by tag or assign a specific 13.8 kV feeder; primary-feed basis is inferred from the facility 13.8 kV distribution narrative. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` facility electrical system narrative | Workbook Packages row 30; `PACKAGE_REGISTER.csv` row `PKG-028` | Datasheet Attributes; Specification REQ-028-04-003 | Treat the DBM facility 13.8 kV distribution as the primary-feed basis for TXP-8801-1 and require EPC anchors to confirm the tag-to-feeder mapping before fabrication release. | TBD |
| HRR-028-04-003 | Insulating medium (oil-filled vs dry-type) for TXP-8801-1 is not stated; DBM general practice references oil-filled spacing and secondary-containment review. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Transformers section | Workbook Packages row 30 | Datasheet Attributes; Specification REQ-028-04-009 | Defer insulating-medium selection to vendor design basis with the EPC bias to limit containment where practical; carry as TBD until selection. | TBD |
