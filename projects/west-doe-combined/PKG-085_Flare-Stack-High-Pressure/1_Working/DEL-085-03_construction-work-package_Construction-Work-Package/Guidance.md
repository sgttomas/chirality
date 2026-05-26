# Guidance — DEL-085-03 Construction Work Package (Flare Stack, High Pressure)

## Purpose

This guidance document orients the EPC Integrator construction team to the
intent behind the PKG-085 Construction Work Package: physically installing,
tying-in, inspecting, and turning over a shared HP/Cryo + LP self-supported
dual flare stack at the 03-25 facility, in coordination with the 04-25 gas
plant
(Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`
lines 56, 497-499, 548; `DELIVERABLE_REGISTER.csv` DEL-085-03).

## Principles

1. **Vendor owns the package; EPC owns the integration.** The Package Vendor is
   responsible for package engineering, design, vendor documentation, and the
   physical equipment package itself. The EPC Integrator is responsible for
   installation, tie-ins, constructability, procurement/construction
   coordination, and facility-level integration
   (Source: `PACKAGE_REGISTER.csv` PKG-085 "Discipline Responsibility Note").

2. **Treat this stack as a shared-interface asset.** It serves both 03-25 and
   04-25 and is governed by the current allocation between those two
   facilities. Coordinate tie-in scheduling, isolation, and turnover with both
   operating sides
   (Source: `3-25_Comp_and_Liquids_DBM.md` lines 56, 548).

3. **Source authority over assumption.** Where vendor or design-basis data
   exists, use it. Where it is not yet locally accessible, mark `TBD` and do
   not derive numeric values from convention.

## Considerations

- **Foundations and tall-equipment erection.** The DBM explicitly lists tall
  vessels and flare/stack elements as requiring equipment-specific foundation
  and anchorage checks against the final geotechnical, snow/wind/seismic,
  frost, vibration, settlement, and access basis
  (Source: `3-25_Comp_and_Liquids_DBM.md` line 700). Plan crane access,
  controlled-lift studies, and dropped-object exclusion zones early.

- **Tie-in sequencing for HP and LP headers.** Both HP and LP relief headers
  are DN 500 / 20 in in the current source basis
  (`3-25_Comp_and_Liquids_DBM.md` line 499). Hot-tap vs cold-tie-in strategy
  depends on whether the upstream KO drum systems (V-4100-2, V-4150-2,
  V-3900-2) are in service at tie-in time. Coordinate with the operations
  isolation plan.

- **KO drum pump interfaces.** P-4100-2 and P-4150-2 (HP) and P-3900-2 (LP)
  transfer or truck out KO drum liquids to slop. Installation of the slop
  routing and truck-out connections is part of the construction interface
  scope (Source: `3-25_Comp_and_Liquids_DBM.md` lines 497, 499, 583-584).

- **F&G placement at the flare/vent interface.** The DBM defers detector
  quantity, tag list, set points, voting logic, placement, and calibration
  requirements to detailed design and safety studies
  (Source: `3-25_Comp_and_Liquids_DBM.md` line 838). Construction shall not
  install detectors until the F&G layout is issued for construction.

## Trade-offs

| Trade-off | Discussion |
|---|---|
| Pre-erected stack vs site-stick-build | Self-supported dual stack vendor design (24292-02-PT-ENR-25-201) is typically delivered in sections; site lift studies and laydown availability drive method selection. ASSUMPTION; vendor erection method: `location TBD`. |
| Hot tie-in vs full shutdown for HP header | Hot tie-in shortens turnaround window but requires more rigorous safety controls; cold tie-in needs operational outage. Decision tied to 03-25/04-25 schedule (TBD). |
| Shared instrument-air supply from 04-25 | Construction-phase utilities (instrument air) must come from 04-25 because 03-25 has no local compression (SCA-006). Plan temporary air for construction/commissioning if 04-25 not yet available (Source: `3-25_Comp_and_Liquids_DBM.md` line 56). |

## Examples

No fully analogous installation examples are present in the locally accessible
sources. (TBD — historical project closeout references not in scope of this
deliverable.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CWP-085-03-CF-001 | Service split and owner interface for the shared HP/Cryo + LP dual flare stack between 03-25 and 04-25 are recorded as open interface items. | `3-25_Comp_and_Liquids_DBM.md` line 56 (open interface items) | `3-25_Comp_and_Liquids_DBM.md` line 548 (basis requires final flare studies) | Specification R-008; Procedure prerequisites; Datasheet "Service split" | PROPOSAL: Defer to 03-25/04-25 interface allocation memo before commencing HP/LP tie-ins. | TBD |
| CWP-085-03-CF-002 | LP stack OD is recorded as TBD in source; HP/Cryo stack OD is 660 mm. | `3-25_Comp_and_Liquids_DBM.md` line 499 | Vendor pkg 24292-02-PT-ENR-25-201 (`location TBD`) | Datasheet attributes | PROPOSAL: Use vendor R1 (or later) datasheet once accessible. | TBD |
| CWP-085-03-CF-003 | F&G detector counts, set points, and placement for flare/vent area are deferred to detailed design and safety studies. | `3-25_Comp_and_Liquids_DBM.md` line 838 | (No competing source) | Specification R-007; Procedure verification | PROPOSAL: Hold F&G installation until issued-for-construction F&G layout is released. | TBD |
