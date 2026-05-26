# Guidance — DEL-088-03 Construction Work Package

> Directional guidance for producing and using the EPC Construction Work Package for PKG-088. This file is non-normative: requirements live in `Specification.md`; clause-level adjudication belongs in source-grounded review.

## Purpose

The Construction Work Package translates the EPC Scope of Work (`DEL-088-01`) and the Package Datasheet (`DEL-088-02`) into an executable plan for physically installing the non-regenerable caustic treating package, hooking it into the 03-25 facility, and turning it over for commissioning. (Source: `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` DEL-088-03 description.)

## Principles

- **EPC integration scope, not vendor design.** This deliverable describes execution and integration; package engineering and physical equipment design remain with the Package Vendor (DEL-088-04). (Source: `PACKAGE_REGISTER.csv` PKG-088 Boundaries.)
- **Interface-anchored.** The 13 declared interface types in PKG-088 are the spine of the work package; every interface type should resolve to one or more field tie-in entries with assigned execution responsibility. (Source: `PACKAGE_REGISTER.csv` PKG-088 Interface Types.)
- **Caustic-aware material discipline.** Caustic handling drives material-of-construction, drain pressure-temperature ratings, and the aluminum exclusion in the caustic building. Treat these as construction-phase quality holds, not as advisory items. (Source: `3-25_Comp_and_Liquids_DBM.md` "Condensate Mercaptan Treating", "Drains".)
- **Source-first reconciliation.** Where construction-execution requirements are present in `26020-Package_Requirements.docx` package heading 41, those clauses are authoritative over generic EPC convention; reconcile them into the specification before issue for construction.

## Considerations

- **Modularization split.** PKG-088's modularization split between shop and field is not fixed in the current source set. Plan for flexible offloading/setting sequencing until the Package Vendor's modular split is confirmed.
- **Utility cross-facility dependence.** Instrument air is supplied from 04-25 (no local IA compressor); LP fuel-gas serves caustic treating overhead dilution. Construction tie-ins must coordinate with 04-25 utility availability and SCA-006 basis. (Source: `3-25_Comp_and_Liquids_DBM.md`.)
- **Drain segregation.** Caustic drain segregation, ANSI rating uplift (300# minimum), and embrittlement-aware material selection are high-risk construction items; HAZOP-led segregation review should precede final piping ISO release. (Source: `3-25_Comp_and_Liquids_DBM.md` "Drains".)
- **Geotechnical confirmation.** Foundation, pile, settlement, and frost-protection design values from the DBM are placeholders until the final geotechnical report is accepted; sequence construction releases accordingly. (Source: `3-25_Comp_and_Liquids_DBM.md` line 141.)
- **Hazard review precedes commissioning.** Methyl mercaptan toxicity drives purge and analyzer maintenance practices; commissioning sequencing in the work package should reference the formal hazard review outcome rather than assume generic practice. (Source: `3-25_Comp_and_Liquids_DBM.md` "Fuel-Gas Sulphur and Purge Hazard Basis".)
- **Turnover register alignment.** The final miscellaneous facilities list must align with plot plan, equipment list, and construction work package register before IFC; build that alignment check into work-package release gates. (Source: `3-25_Comp_and_Liquids_DBM.md` line 661.)

## Trade-offs

- **Detailed clause carry vs. concise execution plan.** Pulling every clause from `26020-Package_Requirements.docx` heading 41 into the work package risks duplicating the SoW and Datasheet; favour a traceability table referencing those upstream deliverables and only restate clauses that drive construction execution.
- **Shop assembly vs. field installation.** Greater shop modularization reduces field tie-in count but raises offloading and crane logistics. The work package should defer the final split to the Package Vendor selection but pre-stage both options for civil/lift planning.
- **Centralized vs. discipline-split work fronts.** Mechanical, civil, electrical, and I&C tie-ins can be executed in discipline silos or by an integrated work front for the caustic package; integrated execution tends to compress commissioning interfaces and is preferred where caustic-building access permits.

## Examples

Concrete examples are not extracted from source materials in this Pass-1/2 run; downstream passes may incorporate examples once Pass 3 lensing and source-slice extraction from `26020-Package_Requirements.docx` are complete. (`TBD`.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-088-03-01 | Modularization split for PKG-088 not fixed in current source basis | `3-25_Comp_and_Liquids_DBM.md` line 294 (analogy for compressor packages) | `26020-Package_Requirements.docx` heading 41 (not extracted) | Datasheet "Construction"; Specification R7; Procedure step S3 | Defer to Package Vendor selection (DEL-088-04) | TBD |
| C-088-03-02 | Caustic drain max temperature listed as 121 deg C / 250 deg F TBC | `3-25_Comp_and_Liquids_DBM.md` "Drains" | Vendor datasheet (not yet issued, DEL-088-04) | Specification R4; Procedure verification | Carry as TBC until vendor confirms | TBD |
| C-088-03-03 | Caustic solution SG basis listed as 1.75 TBC | `3-25_Comp_and_Liquids_DBM.md` "Condensate Mercaptan Treating" | Vendor datasheet (not yet issued) | Datasheet Conditions | Carry as TBC | TBD |
| C-088-03-04 | Objective association from `_CONTEXT.md` (OBJ-002..OBJ-010) derives from package-grouping heuristic, not explicit deliverable-level mapping | `_CONTEXT.md` Supports Objectives | `OBJECTIVE_DELIVERABLE_MAP.csv` (deliverable-level mapping ambiguity) | All four documents (context only) | Treat as ASSUMPTION pending human confirmation | TBD |
