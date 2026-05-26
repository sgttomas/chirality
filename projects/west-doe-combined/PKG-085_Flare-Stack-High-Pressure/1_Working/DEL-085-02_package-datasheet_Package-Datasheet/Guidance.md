# Guidance — DEL-085-02 Package Datasheet (PKG-085 Flare Stack, High Pressure)

> Directional guidance for the EPC Integrator preparing the Package Datasheet and for the Package Vendor consuming it. Explains *why* the datasheet is structured as it is and where judgment is required.

## Purpose

The Package Datasheet is the *technical companion* to the EPC Scope of Work (DEL-085-01). Where the SOW defines what the package is and who owns what, this datasheet hands the Package Vendor the values they need to engineer, design, fabricate, and supply the HP/Cryo flare stack package (PACKAGE_REGISTER.csv PKG-085 OwnershipResponsibility column). It exists because PKG-085 carries facility-shared interfaces (HP/Cryo + LP dual stack shared between 03-25 and 04-25; common incinerator service), so the datasheet must communicate not only stack-vendor parameters but also the interface boundaries with the rest of the facility (DBM-Comp_and_Liquids lines 56, 497-499; DBM-Deepcut line 1570).

## Principles

1. **EPC Integrator sets the inputs; Vendor sets the design.** The datasheet is a frozen input set, not a design document. Any value the Vendor needs to design the stack must either be in the datasheet, in a referenced source, or explicitly TBD. Source: PACKAGE_REGISTER.csv (PKG-085 OwnershipResponsibility).
2. **Source fidelity over decomposition prose.** Where the DBM gives a value (e.g., 660 mm OD x 60,957 mm tall, sonic tip — DBM-Comp_and_Liquids line 499), the datasheet uses that value. Where only decomposition narrative exists, the datasheet treats the narrative as *scope*, not as a *value source*, and marks the value TBD.
3. **Open interfaces are surfaced, not silently resolved.** The HP/Cryo + LP dual stack is a shared system whose 03-25/04-25 ownership split is an open interface item (DBM-Comp_and_Liquids line 56). The datasheet must surface that openness rather than assume an allocation.
4. **Regulatory caveats are kept visible.** OGPFR thermal-radiation references are not in the available input package and must be verified at detailed design (DBM-Deepcut line 289). The datasheet preserves that caveat alongside the numeric limits.
5. **Budgetary go-bys are not engineering authority.** The "Self Supported Dual Flare Stack" budgetary PDF can inform pricing/delivery posture but is not a basis for binding design values (PACKAGE_REGISTER.csv, SourcePath field).

## Considerations

- **Cryogenic relief interaction.** The HP/Cryo stack receives cryogenic flare flow; the J-T valve mechanical stroke limit governs the bounding cryogenic-flare flow case (DBM-Deepcut line 1321). The Vendor must size the cryogenic case at or below that limit, and the EPC Integrator must confirm the limit value upstream before issuing the datasheet for vendor engineering.
- **Sour service.** HP relief comes from sour service (compressor area KO drum V-4100-2 and tank-farm KO drum V-4150-2 — DBM-Comp_and_Liquids line 497; many sour-service tie-ins from DBM-Deepcut process sections). Metallurgy, drainage, and pilot/ignition selection must respect sour-service conditions.
- **Shared incinerator co-location.** The incinerator is physically located at 03-25 "near the flare stacks" and services 04-25 NGL mercaptan treating (DBM-Deepcut line 1570). The datasheet must reference this co-location because it affects plot-plan placement, spacing, and Fire & Gas interfaces.
- **Spacing and thermal-radiation drive plot plan.** The 25/80/50/30.48/10 m spacing values and 9/5 kW/m^2 radiation limits (DBM-Deepcut lines 280-287) determine where the stack can sit relative to property line, equipment, tanks, bullets, and vegetation. These are constraint inputs for the Vendor's tip selection and stack-height analysis, and constraints for the EPC Integrator's plot plan.
- **Interface matrix gap.** The eight package-level interface types are known (PACKAGE_REGISTER.csv), but the tag-to-tag matrix lives in the binary 26020-Packages_Interfaces_4_export.xlsx and is not extracted. Until extraction, the datasheet should treat the interface matrix as a structured TBD, not an absence.

## Trade-offs

- **Issue-with-TBDs vs. wait-for-extraction.** Issuing the datasheet with explicit TBDs (clause-level requirements from 26020-Package_Requirements.docx; interface matrix from 26020-Packages_Interfaces_4_export.xlsx; OGPFR text) keeps PKG-085 moving but obliges a controlled revision cycle once those sources are extracted. Waiting blocks DEL-085-04 (Vendor Engineered Equipment Package). The recommended posture is issue-with-TBDs, with TBDs clearly bounded.
- **Sonic tip vs. other tip types.** The DBM records sonic for the HP/Cryo stack (line 499). Holding to sonic preserves the stack geometry already carried in source; revisiting tip type would re-open height, radiation, and noise basis. Trade-off: change only if final flare studies force it.
- **Self-supported vs. derrick-supported.** Budgetary go-by suggests self-supported (PACKAGE_REGISTER.csv reference). Final structural type is a Vendor decision against site loads, height, and foundation envelope.

## Examples

- *Example value carriage.* Datasheet row "HP/Cryo flare stack height = 60,957 mm" cites `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (line 499)`. This is the form required by R-10.
- *Example TBD carriage.* Datasheet row "HP relief / blowdown load = TBD" cites `DBM-Comp_and_Liquids (line 548) — final flare studies required; location TBD`. This is the required form when the source acknowledges the gap.
- *Example ASSUMPTION carriage.* "Stack support: self-supported dual stack — ASSUMPTION based on budgetary go-by document." This is the required form when only a non-authoritative source supports the statement.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-01 | Ownership of the HP/Cryo + LP dual stack between 03-25 and 04-25 is recorded as a shared-interface open item. | DBM-Comp_and_Liquids line 56 ("shared-interface systems governed by the current 03-25/04-25 allocation … carried as open interface items") | PACKAGE_REGISTER.csv (PKG-085) treats the package as a single 03-25-anchored vendor package | Datasheet Identification, Conditions (Shared service split); Specification R-04 | PROPOSAL: keep package single-anchored at 03-25 in the Datasheet, but explicitly carry the 03-25/04-25 service-split as an open interface item. | TBD |
| CT-02 | Thermal-radiation flux limits (9/5 kW/m^2) carry OGPFR Appendix 1 Schedule 1 Sec. 2 citation, but DBM explicitly states OGPFR references are not in the available input package. | DBM-Deepcut lines 285-286 | DBM-Deepcut line 289 (caveat) | Datasheet Conditions (thermal radiation rows); Specification R-06 | PROPOSAL: carry the values verbatim with the DBM caveat repeated; do not derive design margins until OGPFR text is verified. | TBD |
| CT-03 | Budgetary go-by document ("Self Supported Dual Flare Stack") is referenced by PACKAGE_REGISTER but not present in `_Sources`. | PACKAGE_REGISTER.csv (PKG-085, SourcePath) | `_Sources/` directory listing (document absent) | Datasheet Construction (stack support); References | PROPOSAL: label as ASSUMPTION/go-by only; do not use as engineering authority. | TBD |
| CT-04 | LP stack OD is recorded as TBD in the same source that gives HP/Cryo OD. | DBM-Comp_and_Liquids line 499 ("LP stack OD remains TBD") | — | Datasheet Attributes (LP stack OD) | PROPOSAL: carry as TBD; flag for resolution by final flare studies. | TBD |
