# Datasheet — DEL-082-01 Scope of Work (LP Flare KO Drum Package)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-082-01_scope-of-work | `_CONTEXT.md` |
| Name | Scope of Work | `_CONTEXT.md` |
| ParentPackageID | PKG-082 | `_CONTEXT.md` |
| Package Name | Flare KO Drum (Low Pressure) 3-25 | `_CONTEXT.md`; PACKAGE_REGISTER.csv row 56 |
| Package Workbook Row | 56 | PACKAGE_REGISTER.csv row 56 |
| Package Tag Number | 26020-02-PT-17-002 | PACKAGE_REGISTER.csv row 56 (PackageTagNumber) |
| WBS | 02 | PACKAGE_REGISTER.csv row 56 |
| Discipline | Mechanical | `_CONTEXT.md`; PACKAGE_REGISTER.csv row 56 |
| Deliverable Type | EPC Scope of Work | DELIVERABLE_REGISTER.csv row 300 |
| Responsible Party | EPC Integrator | DELIVERABLE_REGISTER.csv row 300 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package function | Supply one LP flare KO drum and one LP flare KO drum transfer pump | PACKAGE_REGISTER.csv row 56 (Description) |
| Tagged equipment — LP flare KO drum | V-3900-2 | DBM-Comp_and_Liquids §"Flare and Blowdown" L499 |
| Tagged equipment — LP flare KO drum transfer pump | P-3900-2 | DBM-Comp_and_Liquids §"Flare and Blowdown" L499 |
| Sparing — LP flare KO drum transfer pump | 1 x 100 percent | DBM-Comp_and_Liquids §"Sparing Philosophy" L584 |
| Upstream services received | TEG regeneration, VRU, and compressor seal-pot services routed to LP relief | DBM-Comp_and_Liquids L499 |
| Liquid disposition route | KO drum pump P-3900-2 transfers liquids to slop | DBM-Comp_and_Liquids L499 |
| LP relief header size (current basis) | 508 mm, 20 inch | DBM-Comp_and_Liquids L499 |
| Associated flare stack | Shared HP/Cryo and LP dual flare stack at/associated with 03-25, shared with 04-25 | DBM-Comp_and_Liquids L497, L499 |
| LP flare stack OD | TBD (location TBD — DBM L499) | DBM-Comp_and_Liquids L499 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service | Low-pressure flare relief knock-out | DBM-Comp_and_Liquids §"Flare and Blowdown" |
| Plant location | 03-25 facility, with shared flare infrastructure shared with 04-25 | DBM-Comp_and_Liquids L497, L499 |
| Blowdown coordination | Staggered blowdown required to limit maximum relief | DBM-Comp_and_Liquids L501 |
| Detailed blowdown sequencing source | Plant Shutdown and Blowdown Philosophy W242510-PRC-REP-000003-001 (external; location TBD) | DBM-Comp_and_Liquids L501 |

## Construction

| Element | Basis | Source |
|---|---|---|
| Package boundary — supply | One LP flare KO drum (V-3900-2) and one LP flare KO drum transfer pump (P-3900-2) | PACKAGE_REGISTER.csv row 56; DBM L499, L584 |
| Vendor scope | Package engineering, package design, vendor documentation, and the physical equipment package | PACKAGE_REGISTER.csv row 56 (ScopeNotes) |
| EPC Integrator scope | Integration into the functional process facility — interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration | PACKAGE_REGISTER.csv row 56 (ScopeNotes) |
| Applicable interface types | Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports | PACKAGE_REGISTER.csv row 56 (ApplicableInterfaceTypes) |
| Sparing — KO drum transfer pump | 1 x 100 percent | DBM-Comp_and_Liquids L584 |
| Vessel design margin (general) | 10 percent on flow (vessel class) | DBM-Comp_and_Liquids §"Equipment Design Margins" L598 |
| Process pump design margin (general) | 15 percent on flow, unless package-specific design requires otherwise | DBM-Comp_and_Liquids §"Equipment Design Margins" L595 |
| Exclusions | TBD — no package-specific exclusions stated in source materials | PACKAGE_REGISTER.csv row 56 (Exclusions) |

## References

- `_REFERENCES.md`
- DELIVERABLE_REGISTER.csv row 300 (GATE-07 snapshot)
- PACKAGE_REGISTER.csv row 56 (GATE-07 snapshot)
- OBJECTIVE_DELIVERABLE_MAP.csv (GATE-07 snapshot) — OBJ-002 / OBJ-004 / OBJ-005 / OBJ-006 / OBJ-007 / OBJ-008 / OBJ-009 / OBJ-010 mapped to DEL-082-01
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — §"Flare and Blowdown" (L495–501); §"Sparing Philosophy" L584; §"Equipment Design Margins" L588–599
- `_Sources/26020-Package_Requirements.docx` (binary `.docx`, package heading 35) — **location TBD: source not locally machine-readable**
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` (binary `.xlsx`, Workbook Packages row 56) — **location TBD: source not locally machine-readable**
