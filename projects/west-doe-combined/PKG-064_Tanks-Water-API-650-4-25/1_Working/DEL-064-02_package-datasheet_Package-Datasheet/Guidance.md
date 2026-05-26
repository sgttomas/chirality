# Guidance — Package Datasheet (DEL-064-02), PKG-064 Tanks, Water (API 650) 4-25

> Directional rationale and trade-offs for the Process Water Storage Tank (PKG-064) Package Datasheet. This document does not establish requirements (see `Specification.md`) but explains intent, principles, and known trade-offs to inform vendor handoff.

## Purpose

The Package Datasheet is the EPC Integrator's mandatory Gate 5 anchor handoff for PKG-064. It carries the full set of package data required for a third-party vendor or discipline package engineer to design, fabricate, and deliver two atmospheric API 650 process-water storage tanks (TK-5317-1, TK-5318-1) for the 04-25 Deepcut facility. Per the deliverable description, interface facts are intentionally carried here as evidence rather than as separate deliverables.

## Principles

- **Source-anchored.** Tag identity, quantity, and tank code are taken from the GATE-07 PACKAGE_REGISTER and the DBM-Deepcut tag/equipment-count tables (lines 2560, 2628). Vendor handoff data must trace back to these authoritative sources or be explicitly raised as TBD.
- **Atmospheric API 650 basis.** The package name and the DBM-Deepcut equipment-count table classify these tanks under "Tanks, Water (API 650)". The datasheet shall reflect API 650 design throughout; modified-API-650 details (e.g., 16 oz test pressure used on produced-water tanks per DBM-Deepcut line 518) are reference only until the vendor confirms.
- **Winter freeze protection is non-negotiable.** The DBM explicitly requires insulation on water tanks to prevent winter freezing (line 2509). This is a plant-wide miscellaneous requirement applied to all water tanks at this site.
- **Interface boundary is the tank nozzle.** The Process Water Transfer Pumps (P-5317-1, P-5318-1) belong to Tank Farm Pump Building 2 (DBM-Deepcut lines 2555, 2621), not to PKG-064. The datasheet defines tank-side interface only.
- **TBD is preferred to invention.** Where the DBM does not state a value (design SG, design pressure, tank dimensions, MOC), the datasheet carries TBD with a named owner. Values are not transferred from sibling tank packages (produced water, condensate, caustic, DSO) because service chemistry and code basis differ.

## Considerations

- **Service chemistry.** Process water at this facility services (a) amine regeneration (Module 530) process-water demand and (b) NGL mercaptan treating make-up water for upset operation (DBM-Deepcut lines 1132, 1183, 1556). MOC and any internal coating selection should consider deionization quality, potential carryover, and freeze-protection heat-tracing chemistry compatibility.
- **Sizing dependence.** Process-water user rates are flagged as TBD/TBC in the DBM (line 1183). Tank volume sizing therefore depends on amine-regeneration steady-state demand, mercaptan-treating upset-case demand, and any surge or make-up philosophy not yet stated. The datasheet should not lock a volume until detailed engineering closes user rates.
- **Two-tank rationale.** Two tanks are specified (DBM line 2560 — "x2"; tag table line 2628 — TK-5317-1, TK-5318-1). The redundancy/operational basis (parallel storage, swing service, maintenance isolation) is not stated in the available source slice and should be confirmed.
- **Venting and overpressure.** The DBM-Deepcut slice does not state PVRV/EPRV provisions for process-water tanks (in contrast to produced-water tank practice at line 524). Atmospheric water tanks typically use simple breather vents; API 650 Appendix F / venting per API 2000 may apply. This must be confirmed before the datasheet is issued for vendor.
- **Spacing.** Atmospheric tank spacing requirements (NFPA 30, API 2510, OGAOM, DPR 48) apply per the DBM plant-layout tables (lines 265-297). The plot plan must respect tank-to-tank, tank-to-bullet, tank-to-road, and tank-to-fired-heater distances.
- **Insulation method.** The DBM requires insulation but does not specify a method (jacketed, batt-and-cladding, sprayed). Heat tracing is not explicitly required by the available slice for process water tanks, but may be necessary given the Alberta winter design temperature implied by the produced-water freeze-protection practice elsewhere in the DBM.

## Trade-offs

- **Carbon steel vs. coated CS vs. stainless.** Carbon steel is the default low-cost option. Internal coating may be warranted if water quality threatens corrosion, but coatings add inspection burden. Stainless avoids coating but increases capex and may be over-spec for non-aggressive process water. TBD pending water-quality definition.
- **Field-erected vs. shop-built.** API 650 tanks are typically field-erected; shop-built options exist for smaller diameters but limit transport. The DBM does not designate a module for these tanks (contrast: HP/Cryo Flare KO Drum is shop-built per Module 410-1 — DBM line 2784). Field erection is the assumed default for API 650 atmospheric tanks at this volume class.
- **Single large vs. two parallel tanks.** Two tanks (as decomposed) support maintenance isolation and reduce single-point-failure risk but increase plot area, foundation count, and instrumentation count vs. a single larger tank. The two-tank decision is taken as given by the decomposition.
- **Heat tracing on the tank vs. on associated lines only.** Insulating the tank and tracing only the suction/fill lines may be acceptable if tank thermal mass and indoor/heated-environment placement prevent freezing. Full tank tracing increases reliability but adds power and maintenance. TBD per winter design-temperature analysis.

## Examples

- *Insulation precedent at this facility:* Produced-water tanks are externally insulated and heated (DBM-Deepcut line 524). For process-water service the available slice mandates insulation but does not specify external heating; vendor should propose with justification.
- *Interface precedent:* The pump-to-tank interface in Tank Farm Pump Building 2 (DBM-Deepcut line 2621) defines the suction-side boundary; the package datasheet inherits the same interface convention.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CF-064-02-001 | Decomposition package name labels the package "Tanks, Water (API 650) 4-25" and PACKAGE_REGISTER lists workbook row 96 / heading 19 of 26020-Package_Requirements.docx, but the locally accessible DBM-Deepcut tag table at line 2628 uses the row label "Tanks, Water (API 650) 2" (and quantity 2). The "2" is consistent with "x2" tank count in line 2560. | GATE-07 PACKAGE_REGISTER (PKG-064) and `_CONTEXT.md` row 96 / heading 19 | DBM-Deepcut tag table line 2628; equipment-count table line 2560 | Datasheet Identification; Spec REQ-064-02-001 | PROPOSAL: Treat as label-style mismatch only (numeric "2" indicates quantity, not a different package). Both rows refer to the same TK-5317-1 / TK-5318-1 pair. | TBD — confirm during EPC review |
| CF-064-02-002 | DBM-Deepcut explicitly requires insulation on water tanks (line 2509) but does not state heat tracing for process water tanks. Produced-water tanks (different package) are externally heated (line 524). | DBM-Deepcut line 2509 | DBM-Deepcut line 524 | Datasheet Attributes (Heat tracing); Spec REQ-064-02-002 | PROPOSAL: Specify insulation per source; heat tracing TBD pending winter-design-temperature analysis, not inherited from produced-water practice. | TBD |
| CF-064-02-003 | The package row references 26020-Package_Requirements.docx heading 19 as the mandatory content source, but the .docx is not parsed in the current source-access pass; clause-level content is therefore not locally accessible. | `_CONTEXT.md` Source Reference; `_REFERENCES.md` | Local file inventory (`_Sources/26020-Package_Requirements.docx` is binary in this pass) | Spec Standards table; Spec REQ-064-02-007 | PROPOSAL: Carry mandatory-content fields as TBD with explicit owner; reopen when the .docx is parsed. | TBD |
