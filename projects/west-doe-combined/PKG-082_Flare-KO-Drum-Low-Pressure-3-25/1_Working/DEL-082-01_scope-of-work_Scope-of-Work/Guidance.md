# Guidance — DEL-082-01 Scope of Work (LP Flare KO Drum Package)

## Purpose

The Scope of Work for PKG-082 exists to give the EPC Integrator and the Package Vendor a single source-anchored statement of what the LP flare KO drum package is, what it does in the facility, where the responsibility line falls, and what governing source material the rest of the PKG-082 deliverables (Datasheet, Construction Work Package, Vendor Engineered Equipment Package, Vendor Document Turnover, EPC Acceptance) inherit from. [SourcePath: DELIVERABLE_REGISTER.csv row 300; `_CONTEXT.md`]

## Principles

- **Source-anchored scope.** Equipment identity, services, and sparing come from the accessible DBM source slice for LP flare/KO service; anything not stated in source is `TBD`, not invented. [SourcePath: DBM-Comp_and_Liquids §"Flare and Blowdown", §"Sparing Philosophy"]
- **Vendor / EPC split is explicit.** Package Vendor owns package engineering, design, vendor documentation, and the physical equipment package; EPC Integrator owns the integration boundary, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. [SourcePath: PACKAGE_REGISTER.csv row 56 ScopeNotes]
- **Facility integration is first-class.** Even though the package is a single-drum scope, ten interface types apply (process piping; relief/flare/vent; drain/containment; electrical power; EHT; grounding/bonding; area/exterior lighting; I&C/control cabling; maintenance access; structural/foundations/supports). None of them may be silently dropped. [SourcePath: PACKAGE_REGISTER.csv row 56 ApplicableInterfaceTypes]
- **Mandatory Gate 5 EPC anchor.** Per the decomposition Notes field, this is a mandatory Gate 5 EPC anchor deliverable defined by user instruction; it cannot be reduced or merged into another deliverable. [SourcePath: DELIVERABLE_REGISTER.csv row 300 Notes]

## Considerations

- **Shared flare infrastructure.** The LP flare stack and KO drum sit inside a shared HP/Cryo + LP dual flare stack arrangement associated with 03-25 and shared with 04-25. SoW boundaries must respect that the LP relief header (508 mm / 20 in basis) and the LP flare stack are facility-shared infrastructure, not package-internal. [SourcePath: DBM-Comp_and_Liquids L497, L499]
- **Upstream services define sizing intent.** TEG regeneration, VRU, and compressor seal-pot services feed the LP relief header. Changes upstream (e.g., VRU sparing or seal-pot routing) propagate to the KO drum sizing premise. [SourcePath: DBM-Comp_and_Liquids L499]
- **Blowdown coordination is external.** Final blowdown sequencing is governed by W242510-PRC-REP-000003-001 (location TBD). The SoW must point downstream deliverables (datasheet, vendor design basis) at that document once accessible, not at a locally invented sequence. [SourcePath: DBM-Comp_and_Liquids L501]
- **Source-text inaccessibility is recorded, not papered over.** The two named source artifacts (`26020-Package_Requirements.docx` heading 35; `26020-Packages_Interfaces_4_export.xlsx` row 56) are present at `_Sources/` but are binary; until extracted, package-specific scope-text from those sources is `TBD: location TBD`. The DBM markdown source provides the load-bearing equipment, service, and sparing slice used to draft this SoW.

## Trade-offs

- **Source slice vs. complete enumeration.** Using only the accessible DBM slice keeps content source-anchored, but it under-specifies project standards and vendor-documentation requirements that almost certainly live in the `26020-Package_Requirements.docx` package heading 35. Resolving that source is the highest-leverage Pass 1.5 / Pass 2 follow-up.
- **Margin defaults vs. vendor design basis.** The DBM equipment-margin table (vessels 10 percent on flow, process pumps 15 percent on flow) is general; using it as a starting requirement (R-082-01-10) is conservative but is explicitly an **ASSUMPTION** until the vendor package datasheet supersedes.

## Examples

- **Example — interface ownership.** Process piping at the LP relief header tie-in is *facility* scope: the EPC Integrator delivers the header up to the package nozzle and the Vendor delivers the drum nozzle/flange and any package-internal piping. EHT and area lighting follow the same vendor-edge / EPC-edge logic per the ApplicableInterfaceTypes list. [SourcePath: PACKAGE_REGISTER.csv row 56 ApplicableInterfaceTypes]
- **Example — liquid disposition.** P-3900-2 transfers collected liquid to slop (DBM L499). The SoW therefore points to a slop interface, not a produced-water or condensate interface; the slop tie-in is in EPC scope.

## Conflict Table (for human ruling)

No active source/source conflicts were detected in the accessible slices. Pass 2 mini-sweep — none. If the binary source files are later extracted and contradict the DBM slice, add rows here in Pass 3.

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| (none) | | | | | | |
