# Datasheet — DEL-090-04 Vendor Engineered Equipment Package (PKG-090 Vapour Recovery Unit 3-25)

> Descriptive view. Source-grounded to the accessible references for PKG-090; unresolved items marked `TBD`; inferences labeled `ASSUMPTION`.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-090-04_vendor-engineered-equipment-package` | `_CONTEXT.md` Identity |
| Name | Vendor Engineered Equipment Package | `_CONTEXT.md` Identity |
| ParentPackageID | `PKG-090` | `_CONTEXT.md` Identity |
| ParentWorkbookID | 90 (Packages row 100) | `_CONTEXT.md`; PACKAGE_REGISTER.csv row 100 |
| Package Name | Vapour Recovery Unit 3-25 | `_CONTEXT.md`; PACKAGE_REGISTER.csv |
| Package Tag (workbook) | 26020-03-12-001 | PACKAGE_REGISTER.csv row 100 |
| Discipline | Mechanical | `_CONTEXT.md`; PACKAGE_REGISTER.csv |
| Type | Vendor Package Production Unit | `_CONTEXT.md` |
| Responsible Party | Package Vendor (engineering / design / equipment); EPC Integrator performs integration review | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row 567 |
| Anchoring EPC Deliverables | DEL-090-01 Scope of Work; DEL-090-02 Package Datasheet | `_CONTEXT.md` Notes; DELIVERABLE_REGISTER.csv rows 564, 565 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package configuration | Two (2) complete 100% capacity VRU compressor packages in lead-lag configuration, both housed in one building | PACKAGE_REGISTER.csv row 100; `3-25_Comp_and_Liquids_DBM.md` §"Vapour Recovery" L436 |
| Service | Sour service vapour recovery | PACKAGE_REGISTER.csv row 100 |
| Train arrangement | 2 x 100 percent | `3-25_Comp_and_Liquids_DBM.md` L574 |
| Compressor model | Ro-Flo 12S / 212M, two-stage, positive displacement rotary vane | PACKAGE_REGISTER.csv row 100 |
| Driver | 200 HP VFD electric motor per train | PACKAGE_REGISTER.csv row 100; DBM L36, L436, L524 |
| Suction source | Vapours from condensate and produced-water tank systems, plus selected process vents per active process basis | DBM L436 |
| Discharge route | To 04-25 SOC suction under SCA-002 (no local 03-25 SOC retained) | DBM L36, L66, L436 |
| Recycle control | Recycle valve returns second-stage discharge to first-stage suction; sized for 100% flow at minimum driver speed and lowest discharge pressure | DBM L438 |
| Make-up / blanket | Low-pressure fuel-gas make-up / blanket regulator maintains minimum suction pressure at maximum turndown | DBM L438 |
| Suction-header LP bypass | LP flare bypass V-ball valve on VRU suction header, operated by VRU suction pressure; header free-drains / slopes to flare KO interface (final routing per detailed design) | DBM L438 |

## Conditions

| Parameter | Value | Source |
|---|---|---|
| Site | LSD 03-25-80-15 W6M, north of Dawson Creek, BC | DBM §Site, L11-L13, L85, L89 |
| Site elevation | 673 m AMSL | DBM L85 |
| Inlet pressure / temperature | TBD (not stated in accessible DBM extract) | DBM (not located in accessible slice) |
| Discharge pressure | Set by 04-25 SOC suction interface; specific value TBD | DBM L36, L66 (interface stated; numeric value not given in accessible slice) |
| Flow rate per train | TBD | DBM (not located in accessible slice) |
| H2S / sour-service composition | Sour service per facility basis; specific VRU inlet composition TBD | PACKAGE_REGISTER.csv row 100; DBM L309 references 0.296 mol% H2S for inlet compressor train (different service) |
| Sizing redundancy basis | VRU 50 percent on flow | DBM L597 |
| Building | Both trains housed in one building | PACKAGE_REGISTER.csv row 100 |

## Construction

| Item | Value | Source |
|---|---|---|
| Scope of vendor supply | Engineering, design, fabrication / supply, and physical equipment package | `_CONTEXT.md` Scope; DELIVERABLE_REGISTER.csv row 567 |
| Anticipated artifacts | (a) Vendor engineered physical equipment package; (b) Vendor package design basis and datasheet set | `_CONTEXT.md` Anticipated Artifacts |
| Applicable interface types (EPC-integration side) | Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports | PACKAGE_REGISTER.csv row 100 |
| Modularization / shipping splits | TBD (DBM details modularization for inlet compressor packages but does not state explicit modularization for VRU) | DBM L294 (analogous, not for VRU); ASSUMPTION: modularized package per vendor standard |
| Materials of construction | TBD | DBM (not stated for VRU in accessible slice) |
| Electrical area classification | TBD pending area-classification study; sour-service exterior expected | DBM L838 (detector requirements TBD); ASSUMPTION |

## References

- `_CONTEXT.md` — deliverable identity, scope, anticipated artifacts.
- `_REFERENCES.md` — deliverable reference register.
- DELIVERABLE_REGISTER.csv row 567 (`DEL-090-04_vendor-engineered-equipment-package`) — GATE-07 snapshot.
- PACKAGE_REGISTER.csv row 100 (`PKG-090`, Vapour Recovery Unit 3-25) — GATE-07 snapshot.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — §"Vapour Recovery" (L434-L438), §"Tables of equipment / drivers / sizing" (L523-L597), Liquids Hub overview (L20-L40), SCA-002 supersession (L66).
- Inaccessible during this pass (binary): `26020-Package_Requirements.docx` package heading 43; `26020-Packages_Interfaces_4_export.xlsx`; `Bid Docs/Budgetary/26020-03-PT-RFQ-12-001_VRU_1_R0.docx`. Items dependent solely on these sources are marked `TBD`.
