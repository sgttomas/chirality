# Specification — DEL-082-01 Scope of Work (LP Flare KO Drum Package)

## Scope

This deliverable is the mandatory EPC Integrator Scope of Work for PKG-082 (Flare KO Drum (Low Pressure) 3-25). It defines:

- the tagged equipment and package identity that comprise the LP flare KO drum package;
- the package function and boundary;
- the source basis and applicable facility integration narrative;
- responsibility assignment between Package Vendor and EPC Integrator.

**In scope.** The supply of one LP flare KO drum (V-3900-2) and one LP flare KO drum transfer pump (P-3900-2), plus the facility-level integration of that package into the 03-25 process facility (interfaces, tie-ins, constructability, procurement/construction coordination). [SourcePath: PACKAGE_REGISTER.csv row 56; DBM-Comp_and_Liquids L499, L584]

**Out of scope.** Detailed vendor package engineering and design (carried by DEL-082-04 Vendor Engineered Equipment Package), vendor documentation/turnover (DEL-082-05), and EPC vendor package review/acceptance (DEL-082-06). [SourcePath: DELIVERABLE_REGISTER.csv rows 303–305] No additional package-specific exclusions are stated in source materials — **TBD**. [SourcePath: PACKAGE_REGISTER.csv row 56, Exclusions field]

## Requirements

| Req ID | Requirement | Source / Label |
|---|---|---|
| R-082-01-01 | The package shall include one (1) LP flare KO drum, tag V-3900-2. | DBM-Comp_and_Liquids L499 |
| R-082-01-02 | The package shall include one (1) LP flare KO drum transfer pump, tag P-3900-2, sized 1 x 100 percent. | DBM-Comp_and_Liquids L499, L584 |
| R-082-01-03 | The LP flare KO drum shall receive LP relief services from TEG regeneration, VRU, and compressor seal-pot services. | DBM-Comp_and_Liquids L499 |
| R-082-01-04 | The LP flare KO drum transfer pump shall route collected liquids to slop. | DBM-Comp_and_Liquids L499 |
| R-082-01-05 | The LP relief header tie-in to the package shall be compatible with the current source basis of 508 mm (20 in) header. | DBM-Comp_and_Liquids L499 |
| R-082-01-06 | The Package Vendor shall be responsible for package engineering, package design, vendor documentation, and the physical equipment package. | PACKAGE_REGISTER.csv row 56 (ScopeNotes) |
| R-082-01-07 | The EPC Integrator shall be responsible for integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | PACKAGE_REGISTER.csv row 56 (ScopeNotes) |
| R-082-01-08 | Applicable interface types between Package Vendor and EPC scope shall include Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports. | PACKAGE_REGISTER.csv row 56 (ApplicableInterfaceTypes) |
| R-082-01-09 | Package blowdown contribution shall be coordinated with the facility staggered blowdown sequence per the external Plant Shutdown and Blowdown Philosophy W242510-PRC-REP-000003-001 (location TBD). | DBM-Comp_and_Liquids L501 |
| R-082-01-10 | Vessel and pump design margins shall, at minimum, meet the DBM equipment-class margins (vessels 10 percent on flow; process pumps 15 percent on flow unless package-specific design requires otherwise) unless superseded by vendor package design basis. | DBM-Comp_and_Liquids L595, L598 — **ASSUMPTION** that these general margins apply to PKG-082 until vendor datasheet supersedes |

## Standards

| Standard / Document | Use | Location |
|---|---|---|
| Plant Shutdown and Blowdown Philosophy W242510-PRC-REP-000003-001 | Final blowdown sequencing basis | **location TBD** — referenced but not in accessible workspace (DBM-Comp_and_Liquids L501) |
| 26020-Package_Requirements.docx (package heading 35) | Detailed process mechanical scope and vendor documentation requirements per the Word package section | **location TBD** — file present at `_Sources/` but binary `.docx` not locally machine-readable in this run (PACKAGE_REGISTER.csv row 56 SourceRef) |
| 26020-Packages_Interfaces_4_export.xlsx (Workbook row 56) | Authoritative companion register row | **location TBD** — file present at `_Sources/` but binary `.xlsx` not locally machine-readable in this run |

Project-, statutory-, and discipline-level standards (codes for vessels, pumps, flare service) are not enumerated in the accessible source slices — **TBD** pending detailed-design references.

## Verification

| Req ID | Verification approach |
|---|---|
| R-082-01-01 / R-082-01-02 | Tag confirmation in package datasheet (DEL-082-02) and vendor package register; equipment count check against DBM L499 and DBM L584. |
| R-082-01-03 / R-082-01-04 | Interface drawing review (LP relief inlet header; liquid discharge to slop) confirms upstream/downstream services match DBM L499. |
| R-082-01-05 | Tie-in piping isometric / line list confirms header size matches DBM-stated 508 mm / 20 in basis. |
| R-082-01-06 / R-082-01-07 | Responsibility matrix in this SoW reconciled with PACKAGE_REGISTER.csv row 56 ScopeNotes; reviewed in EPC vendor package review (DEL-082-06). |
| R-082-01-08 | Interface matrix in DEL-082-02 Package Datasheet enumerates all listed interface types; gap items marked TBD. |
| R-082-01-09 | Confirm blowdown contribution accepted by the W242510-PRC-REP-000003-001 sequence once the source becomes accessible — **TBD**. |
| R-082-01-10 | Datasheet design-margin entries (DEL-082-02) reviewed against DBM equipment-margin table; deviations flagged for HAZOP/design review. |

## Documentation

Anticipated artifacts delivered under or supported by this Scope of Work, per `_CONTEXT.md` "Anticipated Artifacts":

- Package scope of work (this deliverable);
- Tagged equipment and package identity list;
- Package function and integration narrative;
- Responsibility assignment record.

Companion deliverables in PKG-082 that consume this SoW: Package Datasheet (DEL-082-02), Construction Work Package (DEL-082-03), Vendor Engineered Equipment Package (DEL-082-04), Vendor Document Turnover Package (DEL-082-05), EPC Vendor Package Review and Acceptance (DEL-082-06). [SourcePath: DELIVERABLE_REGISTER.csv rows 300–305]
