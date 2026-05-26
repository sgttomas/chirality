# Guidance — DEL-090-04 Vendor Engineered Equipment Package (PKG-090 Vapour Recovery Unit 3-25)

> Directional view. Rationale and considerations derived from accessible source material; missing items remain `TBD` rather than invented.

## Purpose

DEL-090-04 carries the Package Vendor's engineered and physically supplied VRU package for PKG-090. It is the vendor-side counterpart to the EPC Integrator deliverables (`DEL-090-01` Scope of Work and `DEL-090-02` Package Datasheet) and is the production unit through which engineering, design, fabrication / supply, and the physical equipment package are realized. The package supports vapour recovery from condensate and produced-water tank systems at the 03-25 Liquids Hub and routes recovered vapours to the 04-25 SOC suction under SCA-002. (Sources: `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row 567; `3-25_Comp_and_Liquids_DBM.md` L20-L40, L434-L438.)

## Principles

1. **Source-anchored vendor scope.** Vendor engineering, design, vendor documentation, and physical equipment are the vendor's responsibility; facility-level integration is owned by the EPC Integrator. The package must not encroach on the integration boundary. (PACKAGE_REGISTER.csv row 100.)
2. **Two anchoring EPC deliverables.** The package is developed from the EPC Scope of Work (DEL-090-01) and the EPC Package Datasheet (DEL-090-02). Where these documents constrain the vendor, the vendor's design must reflect them; where they leave choices open, the vendor's choices must be documented in the design basis and datasheet set. (`_CONTEXT.md` Notes; DELIVERABLE_REGISTER.csv rows 564, 565, 567.)
3. **SCA-002 superseded routing.** The package shall not assume any local 03-25 SOC. VRU discharge is rerouted to 04-25 SOC suction. (DBM L36, L66, L436.)
4. **2 x 100% lead-lag.** Both trains are sized for full duty independently; only one runs at a time under normal lead-lag operation. Sizing redundancy basis carried in the facility DBM is "VRU 50 percent on flow." (DBM L574, L597; PACKAGE_REGISTER.csv row 100.)
5. **Stable suction pressure under turndown.** Recycle valve and make-up / blanket regulator together maintain a stable suction pressure across the operating range, including minimum driver speed and lowest discharge pressure. (DBM L438.)
6. **Bypass to LP flare on suction overpressure.** The LP flare bypass V-ball valve on the suction header protects upstream tank systems and provides a defined relief path. The header must free-drain or slope toward the flare KO interface. (DBM L438.)

## Considerations

- **Sour service materials and protection.** Sour service is stated; specific NACE / ISO citations and material grades remain `TBD` pending access to `26020-Package_Requirements.docx` package heading 43.
- **Interface coverage.** The package touches a broad set of facility interfaces (process / utility piping; relief / flare / vent; drain / containment; electrical power; EHT; grounding / bonding; lighting; I&C / control cabling; building HVAC; F&G / safety; maintenance access; structural / foundations / supports). Each interface needs a clear hand-off line at the package boundary documented in the interface register. (PACKAGE_REGISTER.csv row 100.)
- **Single-building arrangement.** Both trains share one building. Building HVAC, F&G coverage, area classification, lighting, and noise / vibration design must accommodate both trains simultaneously, even if normally only one runs. (PACKAGE_REGISTER.csv row 100.)
- **Vapour-source variability.** Vapours originate from condensate and produced-water tank systems and selected process vents; composition and flow may vary as tank fill levels and weather change. Sizing must reflect the lead-lag duty plus the make-up / blanket arrangement. (DBM L436, L438.)
- **Recycle-valve failure action.** For the inlet compressor packages the DBM notes recycle valves are expected fail-open with final action TBC. The VRU recycle valve failure action should be confirmed against the EPC package datasheet and facility safety review; carried as `ASSUMPTION` until VRU-specific source language is reviewed. (DBM L334.)
- **Vendor documentation list.** The exact document list (drawings, datasheets, calculations, manuals, ITPs, certifications) lives in `26020-Package_Requirements.docx` heading 43 (`location TBD` until accessible). The vendor turnover scope is handled separately under `DEL-090-05`. (DELIVERABLE_REGISTER.csv row 568.)

## Trade-offs

- **2 x 100% lead-lag vs. 2 x 50% parallel.** The accepted basis is 2 x 100% (lead-lag), prioritizing availability under maintenance over splitting steady-state load. The vendor should not propose alternative arrangements without an EPC-acknowledged change.
- **Make-up gas vs. flare bypass.** Both maintain suction conditions but in opposite directions (make-up adds gas at low suction pressure; flare bypass relieves at high). Set-points and valve sizing should be coordinated to avoid simultaneous operation under normal swings.
- **Modularization vs. field assembly.** The DBM only states modularization explicitly for the inlet compressor packages (DBM L294). For the VRU, modularization is an `ASSUMPTION` pending the source heading; tighter modularization reduces site work but constrains transport corridors.

## Examples

No vendor-specific examples are quoted from the accessible DBM slices. Pattern reference: the inlet compressor packages (PKG-077 / KM-2150, KM-2250) provide an analogous example of a vendor-supplied modularized compressor package with EPC integration responsibility; design specifics differ. (DBM §"Inlet compression" L294-L334.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted Sections | Proposed Authority (PROPOSAL) | Human Ruling (TBD) |
|---|---|---|---|---|---|---|
| (none identified this pass) | No source / source conflict identified within the accessible reference set. Several requirement candidates depend on `26020-Package_Requirements.docx` heading 43 which is not locally readable; those items are carried as `TBD` rather than as conflicts. | — | — | — | — | — |
