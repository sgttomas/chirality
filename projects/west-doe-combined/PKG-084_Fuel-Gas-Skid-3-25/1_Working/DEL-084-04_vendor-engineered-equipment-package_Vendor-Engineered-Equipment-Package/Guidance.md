# Guidance: DEL-084-04 — Vendor Engineered Equipment Package (Fuel Gas Skid)

> Pass 1/2 draft. Rationale and considerations are drawn from accessible DBM source slices.
> Speculative content beyond what the source supports is left as `TBD` or surfaced in the
> Conflict Table.

## Purpose

This deliverable produces the physically engineered and vendor-supplied fuel-gas skid
package for `PKG-084`. The decomposition frames it as a Package Vendor production unit
developed from the EPC Scope of Work (`DEL-084-01`) and EPC Package Datasheet
(`DEL-084-02`), with subsequent EPC review and acceptance via `DEL-084-06`.

The underlying purpose of the fuel-gas skid is to take pipeline / plant fuel-gas supply,
condition it (knock out liquids, heat as needed, regulate pressure), and distribute it
reliably to the wide range of low-pressure plant fuel-gas users described in the DBM
sources: TEG stripping, blanketing, purge, dilution / enrichment, building heaters,
emergency-generator fuel, flare pilots / purge, and compressor purge / sweep gas.

## Principles

1. **Source-grounded vendor scope.** The vendor design shall be anchored in the project
   DBM source slices and the EPC Scope of Work / Package Datasheet. Where DBM source
   text labels a value `TBC`/`TBD`, the vendor design shall close it explicitly rather
   than silently assume.
2. **Sparing and maintainability over single-point optimization.** The DBM is explicit
   about 2 x 100% regulator sparing, individual regulator isolation, outlet pressure
   test connections, and that main regulators must not be sized to carry combined
   plant + emergency-generator start-gas demand after a parallel-regulator failure.
   These reflect a deliberate operations-first philosophy.
3. **Treat the emergency generator as a distinct service.** The DBM separates plant
   fuel-gas service from emergency-generator service: dedicated local particulate
   filtration, quick-acting internally sensing start-gas regulators, < 66 psig
   supply ceiling for electrical classification compliance, and explicit start-gas
   flow profile (3.6 MMSCFD for 30 seconds).
4. **Cold-weather design is governing, not optional.** The site basis (-40 deg C to
   +35 deg C) governs exposed equipment, package buildings, control panels,
   instrumentation, and field devices unless a stricter package basis applies.
5. **Hazard discipline around sulphur / mercaptan and sweet-gas purge.** Methyl
   mercaptan toxicity and odour are flagged in the 3-25 DBM as requiring a formal
   hazard review before finalizing purge and analyzer maintenance practices.

## Considerations

- **Buyback gas pressure class.** Buyback MAOP is estimated at 9,928 kPag, but the
  DBM explicitly requires detailed-engineering verification. Pressure-class selection
  on the skid (and PSV philosophy) should not be locked until this verification is
  complete.
- **Liquid-knockout destination.** The two DBM sources point at different slop tank
  tags (`TK-9130-1` vs. `TK-9130-2`). This is downstream of the skid battery limit
  but affects drain routing and vapour-return basis; resolve as part of CONFLICT C-01.
- **Buyback regulator station location.** Per 4-25 DBM, the TCPL buyback regulators
  and PSV are assumed to be installed in the sales gas splitter building, not on the
  fuel-gas skid. The vendor scope split should be confirmed against the EPC Scope of
  Work to avoid double-scoping or gap-scoping.
- **Inter-facility demand split.** The fuel-gas system serves both 04-25 and 03-25
  users; the DBM notes the 03-25/04-25 demand split is not closed. Sizing margins on
  the skid should accommodate this open item.
- **Generator testing case.** Because emergency-generator testing may occur at design
  operating conditions, the package must accommodate simultaneous design operating
  flow and generator start-gas flow rather than treating them as mutually exclusive
  cases.

## Trade-offs

| Trade-off | DBM-Anchored Direction | Notes |
|---|---|---|
| Single large regulator vs. 2 x 100% | 2 x 100% sparing required | Improves availability and maintainability; increases footprint and cost. |
| Pilot vs. internally sensing start-gas regulator | Internally sensing quick-acting required for start-gas service | Pilot regulators not permitted for start-gas. |
| Bulk inlet filtration vs. user-side strainers | User-side strainers recommended; bulk inlet filtration not required (except local filter at generator) | Vendor should not over-scope inlet filtration without source basis. |
| Heater duty optimization | Sized for max sales-compressor discharge pressure and winter ambient buyback gas | Conservative envelope; may oversize for normal-mode operation. Duty `TBD`. |
| Carbon-steel vs. upgraded metallurgy | `TBD` pending material spec review | Sour-service governance applies; not resolved in this run. |

## Examples

DBM sources describe `H-3275-1` (heater) and `V-3210-1` / `V-3210-2` (scrubber) as the
anchor equipment for the fuel-gas service. The accessible 4-25 DBM "Fuel Gas Equipment
and Controls" section provides the most complete example of the controls and
maintainability philosophy this skid is expected to embody (skin-T override, outlet-T
control, 2 x 100% regulator sparing with individual isolation and outlet test
connections, separate start-gas regulator class, < 66 psig generator-supply ceiling).

Additional worked examples (sizing calculations, vendor cut sheets, FAT scripts) are
not present in the deliverable folder and remain `TBD`.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-01 | Package name "Fuel Gas Skid 3-25" vs. equipment location. `_CONTEXT.md` (from Workbook Packages row 60 and `26020-Package_Requirements.docx` heading 37) names PKG-084 "Fuel Gas Skid 3-25". The only locally accessible source description of a "Fuel Gas Skid" identifies it as a 4-25 (Deepcut) shared utility (tag IDs `H-3275-1`, `V-3210-1`), serving both 03-25 and 04-25 users. The 03-25 DBM uses `V-3210-2` for an LP fuel-gas scrubber. | `_CONTEXT.md` (Workbook Packages row 60; `26020-Package_Requirements.docx` heading 37 — not parsed) | `4-25_Deepcut_DBM.md` "Fuel Gas Basis" / equipment-tag tables; `3-25_Comp_and_Liquids_DBM.md` "Fuel Gas" | Datasheet "Identification" anchor tags; Specification R-FG-04.3 (drain destination); Guidance "Considerations" (buyback location, inter-facility split) | PROPOSAL: PKG-084 covers the physical fuel-gas skid as a shared utility located at 04-25 that serves 03-25 users; package name "3-25" reflects the consumer-side facility, not the physical location. Confirm by parsing `.docx` heading 37 and reconciling tag set. | TBD |
| C-02 | Emergency buyback fuel gas inclusion. 3-25 DBM "Fuel Gas" notes that W242510 indicates emergency buyback is not required, while Process_DBM_fixed includes emergency buyback in the 04-25 utility package. | 3-25 DBM "Fuel Gas" citing W242510 | 3-25 DBM "Fuel Gas" citing Process_DBM_fixed; 4-25 DBM "Emergency Buyback and Purge" | Specification R-FG-02.2; Datasheet "Service Function" and "Pressure/Flow Basis" buyback rows | PROPOSAL: Include buyback provision in the package scope envelope but flag MAOP and presence as final human ruling before issue. | TBD |
| C-03 | Slop-tank destination for scrubber liquids. 4-25 DBM identifies `TK-9130-1`; 3-25 DBM identifies `TK-9130-2`. | 4-25 DBM "Fuel Gas Equipment and Controls" | 3-25 DBM "Fuel Gas" | Specification R-FG-04.3 | PROPOSAL: Drain destination follows the resolution of CONFLICT C-01 (location of the skid). | TBD |
