# Guidance — Package Datasheet (PKG-094 Tanks, Caustic API 650 3-25)

> Status: INITIALIZED. Directional commentary grounded in the 3-25 DBM. Items requiring
> human ruling are tracked in the Conflict Table below.

## Purpose

This guidance helps the EPC Integrator author of the PKG-094 Package Datasheet make
defensible choices where the source set is silent, incomplete, or carries explicit `TBC`
markers. It is non-binding; the Specification (`Specification.md`) is the normative artifact.

## Principles

- **Source over convention.** When the 3-25 DBM speaks, follow the DBM (e.g., 50 wt%
  NaOH, LP fuel-gas blanket, no aluminum). Do not import generic API 650 boilerplate that
  contradicts the DBM.
- **Hand off enough, not too much.** The datasheet documents facility-side basis (site,
  ambient, interfaces, fluid composition, tie-in ratings) so the vendor can engineer.
  Vendor-domain decisions (shell course thicknesses, weld details, nozzle reinforcement)
  are vendor output, not EPC datasheet input.
- **Carry TBCs forward, do not invent.** Where the DBM is explicit that a value is `TBC`
  (e.g., SG 1.75, drain max temperature 121 °C, caustic tank coating), preserve the TBC
  and require vendor confirmation rather than asserting a value.
- **Treat caustic as embrittlement-relevant.** Material selection must explicitly address
  caustic embrittlement; do not default to standard carbon-steel piping classes for
  caustic drain (DBM §Drains).
- **Atmospheric, blanketed, vented.** Both tanks are atmospheric storage with vapor-space
  management (LP fuel-gas blanket on fresh; flame arrestor to incinerator header on spent).
  Do not let pressure-vessel framing creep into the datasheet.

## Considerations

- **Tank capacity scale.** 400 bbl each is the DBM line-item value. The treating unit
  processes 20,000 bbl/d of C5+ condensate, so tank turnover/refresh frequency drives
  fresh-caustic logistics and spent-caustic truck-out scheduling (DBM lines 389-402).
- **Aluminum prohibition is building-wide.** The DBM says aluminum shall not be used in
  the caustic building. This affects ladders, platforms, conduit, instrument enclosures,
  and lighting fixtures in the package envelope, not just the tank.
- **Spent-caustic vent path.** Vent through flame arrestor to incinerator header is a
  shared-utility interface (incinerator capacity, flame arrestor maintenance access).
  Coordinate with the Relief/Flare/Vent interface (IFC-AFD520D296).
- **VRU exclusion for fresh caustic.** Fresh caustic is explicitly not connected to VRU
  (DBM line 402). Confirm the spent-caustic vent route is incinerator-only and not VRU.
- **Caustic drain governance.** Caustic drain design pressure is governed by the highest
  upstream equipment terminating at a 300# flange at the spent-caustic tank. The package
  datasheet must call out this 300# termination explicitly so the vendor sizes/rates the
  spent-caustic tank inlet accordingly (DBM line 493).
- **Site basis.** Site is north of Dawson Creek, BC at elevation 673 m AMSL; cold-climate
  ambient design, snow loading, and seismic provisions apply (DBM §Site Location, §Ambient,
  §Wind/Snow, §Geotechnical). Pull clause-level numbers from the DBM into the datasheet
  rather than restating generic regional values.

## Trade-offs

- **Heat tracing redundancy (caustic drain).** DBM lists 100 °F heat tracing with redundant
  circuits as "under consideration" (line 493). Datasheet authors should reflect this as a
  design-development item rather than locking it in or removing it.
- **Coating vs. solid-CRA tank wall.** DBM marks coating/MOC as TBC. Trade-off between
  solid CRA tank (capex), lined CS tank (capex + lining inspection regimen), and coated CS
  (lifecycle risk) belongs to the vendor MOC submittal; datasheet should require the trade
  study, not pre-select.
- **Spent caustic disposition.** Truck-out is explicitly supported (DBM line 402). If a
  future pipeline disposition emerges, datasheet must not preclude addition of a pipeline
  manifold connection.

## Examples

- Atmospheric tank, 400 bbl, 50 wt% NaOH service, LP fuel-gas blanket, heated, insulated,
  no aluminum in proximity — this is the fresh-caustic tank as bounded by the DBM.
- Caustic drain inlet at 300# flange minimum — this is the explicit interface governance
  carried forward to the spent-caustic tank inlet.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-094-02-001 | Specific gravity of stored caustic carried as 1.75 but DBM marks it `TBC`. | DBM line 402 ("SG 1.75 TBC") | None | Datasheet §Tank Attributes; Specification R3.2 | PROPOSAL: hold 1.75 as design-point with `TBC` marker; vendor confirms via MOC submittal. | TBD |
| CONF-094-02-002 | Caustic drain max temperature `121 °C / 250 °F TBC` may conflict with insulated/heated tank thermal envelope; vendor design must reconcile. | DBM line 493 | DBM line 402 (heated, insulated) | Datasheet §Process Design Conditions; Specification R6.2 | PROPOSAL: require vendor to confirm tank shell/internal max temperature ≥ caustic drain max; flag if not. | TBD |
| CONF-094-02-003 | Tank material of construction and coating: source explicitly carries `TBC`. | DBM line 402 | None | Datasheet §Materials; Specification R5.2 | PROPOSAL: defer MOC to vendor submittal; specify aluminum prohibition and require caustic-embrittlement-resistant selection. | TBD |
| CONF-094-02-004 | Caustic-drain piping MOC requires detailed review (DBM); not specified at decomposition. | DBM line 493 | None | Specification R5.3 | PROPOSAL: require EPC piping group to issue caustic-drain piping class before vendor design freeze; reference in datasheet as carried interface. | TBD |
| CONF-094-02-005 | API 650 clause text not locally accessible; package title invokes API 650 but DBM does not reproduce clause requirements. | PACKAGE_REGISTER.csv title (API 650) | DBM (no API 650 clauses) | Specification R2.1; Standards table | PROPOSAL: cite API 650 with `location TBD`; require vendor design report to demonstrate compliance. | TBD |
| CONF-094-02-006 | Vendor RFQ source (`26020-Package_Requirements.docx` package heading 46) referenced but not parsed in this environment; may contain additional requirements not reflected. | `_REFERENCES.md`; `_CONTEXT.md` Source Reference | DBM (parsed) | Datasheet References; Specification Standards | PROPOSAL: convert source to .md or parse externally and re-run lensing (Pass 3) before deliverable acceptance. | TBD |

These conflicts are surfaced as `NEEDS_HUMAN_RULING` items. They do not block the
INITIALIZED state but must be resolved before deliverable acceptance.
