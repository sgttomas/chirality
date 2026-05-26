# Guidance — DEL-065-04 Vendor Engineered Equipment Package

## Purpose

This deliverable is the Package Vendor's engineered output: the design basis, datasheets, and physical equipment for the two API 650 (modified) caustic tanks of PKG-065. It exists so that the EPC Integrator receives a coherent, source-grounded, vendor-engineered package — including the Spent Caustic Tank (TK-6780-1) and the Fresh Caustic Tank — ready for facility integration, construction installation (DEL-065-03), document turnover (DEL-065-05), and integrator acceptance (DEL-065-06). (Source: `_CONTEXT.md`; SOW-0197.)

## Principles

1. **Responsibility split is binding.** The Package Vendor owns engineering, design, vendor documentation, and the physical equipment; the EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination. Stay strictly inside the vendor lane. (Source: `PACKAGE_REGISTER.csv` row 87.)
2. **Source-grounded design values.** Use values that exist in the workbook/package-requirements source slice (SOW-0197…0200) verbatim. Where source is silent, escalate via the EPC Package Datasheet (DEL-065-02), not assumption.
3. **Modified API 650 is the design code.** The "modified" qualifier is in source; the actual modification list is not. Treat any modifications as TBD until EPC Integrator confirms. (Source: SOW-0199.)
4. **Caustic service governs material selection.** Spent caustic ~14.7 wt% NaOH and fresh caustic 50 wt% NaOH set the corrosion and freezing-risk envelope; do not under-specify by reusing generic atmospheric tank standards. (Source: DBM-Deepcut §Mercaptan Treating Unit.)
5. **Freezing/crystallization is a real risk.** DBM-Deepcut explicitly identifies caustic freezing/crystallization risk and prescribes indoor installation for the broader mercaptan-treating equipment. The vendor-supplied heater on TK-6780-1 (≥ 32.2 °C / 90 °F) is the package-level mitigation for that tank; the Fresh Caustic Tank heater is unspecified in source and should be raised as an open question. (Source: DBM-Deepcut §Mercaptan Treating Unit; SOW-0199.)

## Considerations

- **Heater on Item 2 (Fresh Caustic Tank).** Source explicitly mandates a heater on Item 1 only. If site minimum ambient triggers crystallization risk on a 50 wt% NaOH fluid, raise as a conflict with EPC Integrator rather than silently providing or omitting.
- **Design pressure of the Fresh Caustic Tank.** Source states design pressure for Item 1 (32 oz / 1.0 oz vacuum); Item 2 is silent. Assume parity but confirm.
- **Interface specifics.** PKG-065 has nine declared interface types. None are quantified in the deliverable-local source slice; the vendor design basis should treat each as a parametric interface to be confirmed via DEL-065-02.
- **Tag number for Fresh Caustic Tank.** Source provides TK-6780-1 for the spent caustic tank but no tag for the fresh caustic tank in the slice available locally. Use placeholder and confirm.
- **"By Others" boundary.** Foundations, mounting, electrical/instrumentation install, platforms, staircase are explicitly out of scope. Do not creep into civil/structural/E&I deliverables.

## Trade-offs

| Topic | Trade-off | Recommended Posture |
|---|---|---|
| MOC for spent caustic (carbon steel vs. higher alloy/lined) | Cost vs. service life under ~14.7 wt% NaOH with elevated temperature | Vendor to propose with justification; flag as design-basis decision needing EPC Integrator concurrence. Source is silent on MOC. |
| Single vs. duplex heater design (TK-6780-1) | Reliability vs. cost | Source says only "Vendor to design" — vendor judgment, document rationale in design basis. |
| Atmospheric vent vs. tied-into Relief/Flare/Vent | Operability/emissions vs. complexity | Coordinated through Relief/Flare/Vent interface (IFC-68999FB972). EPC Integrator-owned decision. |
| Insulation / heat tracing extent | Heat loss minimization vs. fabrication cost | Required at minimum to support 32.2 °C maintenance target on TK-6780-1. Extent on Item 2 TBD. |

## Examples

Examples below are illustrative of how to apply the principles above using only source-supported facts.

- *Example A (capacity statement)*: "Both tanks are 400 bbl nominal" — directly sourced (SOW-0199, SOW-0200).
- *Example B (heater scope)*: "Spent Caustic Tank includes vendor-designed heater at 32.2 °C minimum; Fresh Caustic Tank heater requirement is not stated in source and is being confirmed." — sourced + flagged TBD (SOW-0199).
- *Example C (exclusion statement)*: "Foundations, platforms, and electrical/instrumentation installation are excluded from this package and are provided by the EPC Integrator." — directly sourced (SOW-0200).

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-01 | Fresh Caustic Tank design pressure not stated in `26020-Package_Requirements.docx` slice while Spent Caustic Tank is fully specified (32 oz / 1.0 oz vac). Risk: silent omission may indicate different design intent for fresh caustic. | SOW-0198 (`26020-Package_Requirements.docx` pkg heading 20 — Basic scope) | SOW-0199 (same source — Major included equipment, Item 1 only) | Datasheet §Conditions; Specification R-04 | Treat as parity with Item 1 pending DEL-065-02 confirmation; vendor to confirm with EPC Integrator before fabrication. | TBD |
| CONF-02 | Capacity/design throughput and flow rates listed as TBC/TBD in source slice; required to size nozzles and instrumentation. | SOW-0200 (`Scope notes and open items`) | DEL-065-02 EPC Package Datasheet (downstream artifact not yet produced) | Datasheet §Conditions; Specification R-08 | Defer to DEL-065-02 when issued; do not invent values. | TBD |
| CONF-03 | "Modified API 650" — modifications not enumerated in source slice. | SOW-0199 | None (no second source) | Specification R-01; Datasheet §Construction | Vendor to propose modification list as part of design basis; EPC Integrator to accept under DEL-065-06. | TBD |
| CONF-04 | Heater requirement on Fresh Caustic Tank not stated in source; DBM-Deepcut flags caustic freezing/crystallization risk generally. | SOW-0199 (Item 1 heater only) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §Mercaptan Treating Unit (freezing risk) | Datasheet §Conditions row "Minimum process temperature"; Specification R-05; Guidance Considerations | Raise as open question with EPC Integrator; do not silently add a heater nor silently omit. | TBD |
| CONF-05 | Material of construction silent in source; caustic service material selection has significant cost/service-life impact. | SOW-0198/0199/0200 (silent) | DBM-Deepcut §Mercaptan Treating Unit (process basis) | Datasheet §Construction; Specification R-07 | Vendor to propose MOC with justification in vendor design basis; flag as ASSUMPTION until accepted. | TBD |
