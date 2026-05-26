# Datasheet — DEL-082-03 Construction Work Package (LP Flare KO Drum, 3-25)

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-082-03_construction-work-package |
| Name | Construction Work Package |
| ParentPackageID | PKG-082 |
| PackageName | Flare KO Drum (Low Pressure) 3-25 |
| Discipline | Mechanical |
| Type | EPC Construction Work Package |
| ResponsibleParty | EPC Integrator |
| AssociatedTag — LP Flare KO Drum | V-3900-2 (SourcePath: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SectionRef: SEC-07 Flare and Blowdown, line 499) |
| AssociatedTag — LP KO Drum Transfer Pump | P-3900-2 (SourcePath: same, SectionRef: SEC-07 Flare and Blowdown, line 499) |
| Facility | 03-25 West Doe Compressor Station and Liquids Hub, LSD 03-25-80-15W6 (SourcePath: same, SectionRef: SEC-01 Site & Facility, line 12) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Service | LP relief: TEG regeneration, VRU, and compressor seal-pot services routed to LP KO drum V-3900-2 | DBM SEC-07, line 499 |
| LP relief header size | 508 mm (20 inch) — current source basis | DBM SEC-07, line 499 |
| LP flare stack OD | TBD (current source carries OD as TBD) | DBM SEC-07, line 499 |
| KO drum liquid disposition | Pump P-3900-2 transfers to slop | DBM SEC-07, line 499 |
| KO drum vessel dimensions / MAWP / materials | TBD (not in accessible source slice) | location TBD |
| Sparing — LP flare KO drum transfer pump | 1 x 100 percent | DBM SEC-09 Sparing Philosophy, line 584 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Sour service classification | Sour hydrocarbon service applies — isolation, vent, and drain segregation required | DBM SEC-09 Isolation Philosophy, line 607 |
| Blowdown basis | Staggered blowdown required to limit maximum relief | DBM SEC-07, line 501 |
| Final blowdown sequencing source | Plant Shutdown and Blowdown Philosophy W242510-PRC-REP-000003-001 (referenced; not in accessible workspace) | location TBD |
| Design ambient / seismic / wind / snow | TBD (site at elevation 673 m AMSL near Dawson Creek, BC per DBM SEC-02) | partial — DBM SEC-02 line 85 |

## Construction

ASSUMPTION (EPC Integrator convention; not stated in accessible source): construction scope of this CWP includes foundations and anchorage; mechanical setting of V-3900-2 and P-3900-2; LP relief header tie-ins to TEG regeneration, VRU, and compressor seal-pot system tie-in points; instrumentation and electrical hook-up; pressure testing; pre-commissioning cleaning and purging; mechanical completion turnover.

- Foundations and anchorage: per geotechnical and equipment-load checks — TBD source values (DBM SEC-09 Foundations narrative, line 700, requires equipment-specific values not in accessible slice).
- Skid/vessel setting: tag V-3900-2 LP KO drum and pump P-3900-2.
- Piping tie-ins: 508 mm LP relief header to LP flare stack; transfer line from P-3900-2 to slop.
- Sour-service isolation provisions: double block/bleed or equivalent per HAZOP — TBD final list (DBM SEC-09 Isolation Philosophy, line 607).
- Pressure testing, NDE, and PWHT requirements: TBD (not in accessible source slice).

## References

- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — 3-25 Comp & Liquids Design Basis Memo, SEC-07 (Flare and Blowdown) and SEC-09 (Plant Design Requirements and Mechanical Package Structure).
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` — DEL-082-03 row.
- Referenced but not locally accessible: `26020-Package_Requirements.docx` package heading 35; `W242510-PRC-REP-000003-001` Plant Shutdown and Blowdown Philosophy. location TBD.
