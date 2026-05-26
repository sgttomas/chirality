# Guidance — DEL-064-03 Construction Work Package

Directional guidance for the EPC Integrator drafting the Construction Work Package for PKG-064 "Tanks, Water (API 650) 4-25".

## Purpose

PKG-064 is a Package Vendor production unit: the Vendor owns package engineering, design, vendor documentation, and the physical equipment package. The EPC Integrator owns integration into the functional process facility — interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration (PACKAGE_REGISTER.csv PKG-064 ResponsibilityModel). The Construction Work Package is the EPC Integrator's mandatory anchor deliverable that converts that integration responsibility into an executable field plan.

It exists so that, given a vendor-engineered tank package and a defined set of facility interfaces, the construction crew has a single coherent description of what to build, how the interfaces close, who is responsible, what evidence is required, and how the package is turned over to operations.

## Principles

1. **Decomposition routes; sources govern.** The decomposition tells you that PKG-064 contains two Process Water Storage Tanks and nine EPC-managed interface types. The DBM-Deepcut source and the SOW-* scope ledger entries tell you what those tanks actually are, how they are designed, what they connect to, and what is excluded. Build the Construction Work Package off the source slices, not off the register summary.
2. **Construct against the integration boundary, not the package boundary.** The Package Vendor's deliverable ends at the package boundary (mechanical / electrical / I&C / piping termination points and shipped-loose items). The Construction Work Package owns everything from there to the live facility, including by-others scope (foundations, mounting, electrical/instrumentation, platforms, staircases — SOW-0236).
3. **Treat interface rows as work items, not paperwork.** Each row in INTERFACE_REGISTER.csv for PKG-064 is an EPC-managed field activity. The construction interface and turnover checklist should mirror those rows one-for-one.
4. **Respect the construction responsibility split.** DBM-Deepcut SEC-01 assigns field construction to Tourmaline Oil Corporation. The Construction Work Package coordinates that party; it does not re-assign the work.
5. **Preserve the arctic / sub-arctic posture.** Tank installation choices (insulation, heat tracing, blanket-gas connection, drainage slope, snow loading, freeze-thaw exposure) must follow from the -40 °C minimum site temperature and the SOW-0235 freeze-protection requirement.

## Considerations

- **Plot plan dependency.** Final equipment coordinates and layout verification depend on the project plot plan; that plot plan status is TBD in DBM-Deepcut SEC-02. The Construction Work Package should treat spacing-criteria compliance (DBM SEC-02 tables) as a set-out check, not a fixed coordinate set, until the plot plan is issued.
- **Permit clearances.** DBM-Deepcut SEC-01 establishes that the BC Energy Regulator permit amendment is in place subject to a Section 12.4 site alteration permit; specific construction-execution clearances are governed by the regulatory section of the DBM (location TBD). The Construction Work Package should leave a documented hook for that clearance evidence rather than asserting a specific permit-step sequence.
- **Acid-gas / sour-vapour caveats do not apply to clean process water.** SOW-0235 states the fluid is "Non sour clean treated water"; however, the DBM Produced Water tank narrative discusses sour vapour isolation philosophy as a design check for similar tankage. For the Process Water package (TK-5317-1, TK-5318-1) the construction crew should not import the produced-water sour-vapour isolation requirements unless detailed engineering re-classifies the service. Carry as ASSUMPTION; flag at construction kickoff.
- **Make-up water service downstream link.** DBM-Deepcut notes "Make-up water, if required during upset operation, is supplied from the process water storage tank. Final make-up water routing remains to be confirmed by detailed engineering." Construction Work Package piping tie-ins for make-up routing should remain flexible until the routing is confirmed (location TBD).
- **Heat tracing and insulation circuit ownership.** Electrical and instrumentation termination work is assigned to Tourmaline field construction scope (DBM SEC-01), but heat-trace circuit design is normally upstream engineering. The Construction Work Package should distinguish circuit installation from circuit design and not assume design ownership.
- **Downstream consumer expectation.** DEL-064-06 (EPC Vendor Package Review and Acceptance) is the natural consumer of the Construction Work Package turnover evidence. The Construction Work Package should pre-shape its turnover dossier to satisfy that acceptance checklist; this is ASSUMPTION pending dependency declaration.

## Trade-offs

| Trade-off | Direction this guidance recommends |
|---|---|
| Workface plan granularity vs. workface plan stability | Keep the workface plan at activity-and-interface granularity (one entry per equipment tag and per interface type); finer subdivision should occur in the field, not in this deliverable. |
| Restate vendor requirements vs. reference vendor documents | Reference vendor documents (DEL-064-05) by document number; do not re-state vendor design values in the Construction Work Package unless they drive construction acceptance criteria. |
| Use modified-API-650 wording verbatim vs. construction-acceptance restatement | Use the SOW-0235 wording verbatim where it defines the design basis; restate only as construction-acceptance criteria (nameplate check, dimensional check, weld test acceptance) in the verification table. |
| Coordinate spacing checks against current plot plan (TBD) vs. against DBM SEC-02 spacing tables | Use DBM SEC-02 spacing tables as the governing acceptance basis until a plot plan is issued; treat any plot plan deviation as a deviation log entry. |
| Carry sour-vapour controls from produced-water tankage vs. clean-water service basis | Build to the SOW-0235 clean-treated-water basis; capture sour-vapour controls only if re-classified by detailed engineering. |

## Examples

The DBM-Deepcut Produced Water Tank table provides an example of the level of detail at which a tank-package construction acceptance can be specified (external insulation, internal coating, blanket-gas, PVRV provision, hydrocarbon skim, heater). Construction Work Package authors can use that table as a structural model for the Process Water tank construction acceptance lines, while removing the items that do not apply to clean-treated-water service (internal coating against produced-water chemistry, hydrocarbon skim float, sour-vapour isolation). Source: DBM-Deepcut SEC-, Produced Water Tank rows and the surrounding paragraph (lines around 510–524).

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFL-064-03-01 | Service descriptor: SOW-0234 states "Sweet Produced Water & Process Water"; DBM-Deepcut narrative treats the 4-25 Tanks, Water (API 650) package as Process Water (TK-5317-1 / TK-5318-1) and treats Produced Water as a separate API 650 Sour Water package (TK-9010-1 / TK-9020-1). | SOW-0234 (workbook package heading 19, Basic scope) | DBM-Deepcut equipment/tag table rows 99 and 102 | Datasheet "Service"; Specification R-064-03-01 (equipment scope); Guidance "sour-vapour caveats" paragraph | PROPOSAL: Treat PKG-064 as Process Water (clean treated water) per the DBM equipment-table assignment; carry the workbook descriptor as a documentation discrepancy to be resolved by the EPC Integrator. | TBD |
| CFL-064-03-02 | Construction responsibility for interconnecting piping at ISBL/OSBL tie-ins is flagged in DBM-Deepcut SEC-01 as "External interface responsibility marker; responsibility is to be confirmed for each tie-in", but the Construction Work Package needs a default to plan against. | DBM-Deepcut SEC-01 Construction Responsibility row "Installation of interconnecting piping to ISBL/OSBL tie-in points" | INTERFACE_REGISTER.csv PKG-064 Process Piping row (IFC-53CAD5DFB7) flagged `RequiresEPCManagement = YES` | Specification R-064-03-05, R-064-03-06; Procedure tie-in steps | PROPOSAL: Default to EPC Integrator management of the tie-in execution (consistent with INTERFACE_REGISTER), with per-tie-in confirmation captured in the construction interface and turnover checklist. | TBD |
| CFL-064-03-03 | PVRV / EPRV sizing and blanket-gas detailing are explicitly called out for Produced Water tanks in the DBM but are not separately described for the Process Water tanks; whether the same provisions are applied to PKG-064 affects construction inspection scope. | DBM-Deepcut Produced Water Tank paragraph (PVRV provision and EPRV review during detailed engineering) | SOW-0235 (LP fuel-gas blanket; no PVRV/EPRV detail for PKG-064) | Datasheet Conditions (Blanket gas); Specification R-064-03-04 verification line | PROPOSAL: Construct against SOW-0235 (blanket connection only) and flag PVRV/EPRV provision as a detailed-engineering input; do not assume produced-water tank provisions transfer. | TBD |
