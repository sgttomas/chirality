# Datasheet — DEL-089-06 EPC Vendor Package Review and Acceptance (Pig Receivers, Inlet 3-25)

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-089-06_epc-vendor-package-review-and-acceptance` |
| Name | EPC Vendor Package Review and Acceptance |
| ParentPackageID | `PKG-089` |
| PackageName | Pig Receivers (Inlet) 3-25 |
| Discipline | Mechanical |
| Type | EPC Vendor Package Acceptance |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input |
| Source slice | 3-25 Comp_and_Liquids DBM, SEC-04 "Inlet Pipeline Interface and Pigging" |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Equipment scope | Single combined three-phase pig receiver | DBM 3-25 SEC-04 (Inlet Pipeline Interface and Pigging) |
| Skid configuration | Structural steel, non-enclosed skid | DBM 3-25 SEC-04 |
| Receiver size | TBD | DBM 3-25 SEC-04 (explicit "TBD") |
| Purge medium | Sweet-gas purge | DBM 3-25 SEC-04 |
| Vent destination | HP flare vent | DBM 3-25 SEC-04 |
| Inlet ESDV | Full-port, piggable, with position transmitters | DBM 3-25 SEC-04 |
| Inlet ESDV shutdown pressure | 635 psig (at inlet separator ESDV) | DBM 3-25 SEC-04 |
| Delivery-point ESDV shutdown pressure | TBC | DBM 3-25 SEC-04 |
| Inlet pipeline interface | First aboveground flange within lease boundary | DBM 3-25 SEC-04 |
| Inlet pipeline count | Single Doe field inlet pipeline | DBM 3-25 SEC-04 |

## Conditions

| Condition | Value | Source / Status |
|---|---|---|
| Service | Sour wellstream (gas/condensate/produced water, trace sulphur) | DBM 3-25 SEC-04 |
| Inlet design temperature | 8.3 deg C (reconciliation pending in detailed design) | DBM 3-25 SEC-04 (separator basis; receiver-specific value TBD) |
| Code/regulatory regime | CSA Z662 (governing pipeline code referenced for outlet; applicability to inlet/pigging facility TBC) | DBM 3-25 SEC-04 — `ASSUMPTION: likely applicable` to inlet piping |
| Frac flowback / slug | Governs transient liquid case; managed by operator pigging/flowback discipline | DBM 3-25 "Slug and Flowback Basis" |

## Construction

| Item | Basis | Source |
|---|---|---|
| Skid type | Structural steel, non-enclosed | DBM 3-25 SEC-04 |
| Purge/vent provisions | Sweet-gas purge tie-in; HP flare vent tie-in | DBM 3-25 SEC-04 |
| Associated valving | Full-port, piggable inlet ESDV with position transmitters | DBM 3-25 SEC-04 |
| Building enclosure | None for receiver skid (separator building covered separately) | DBM 3-25 SEC-04 |
| Coating | TBD for receiver (separator-internal Devchem 253 noted as separator scope, not receiver) | DBM 3-25 SEC-04 |
| Detailed dimensions / weights | TBD (vendor scope) | TBD |
| Final inlet pipeline configuration | To be confirmed during detailed design | DBM 3-25 SEC-04 |

## References

- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — SEC-04 Inlet Pipeline Interface and Pigging; Slug and Flowback Basis
- Decomposition source ref: Workbook Packages row 77; 26020-Package_Requirements.docx package heading 42 (binary source — `location TBD`)
- GATE-07 PROJECT_DECOMP snapshot — `DELIVERABLE_REGISTER.csv` row `DEL-089-06_epc-vendor-package-review-and-acceptance`
