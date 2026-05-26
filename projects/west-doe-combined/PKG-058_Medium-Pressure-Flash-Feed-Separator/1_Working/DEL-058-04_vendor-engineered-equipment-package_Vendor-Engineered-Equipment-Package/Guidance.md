# Guidance — DEL-058-04 Vendor Engineered Equipment Package (Medium Pressure Flash Feed Separator)

## Purpose

This deliverable exists because the EPC Integrator hands engineering and physical supply of the MPFF separator package to a Package Vendor, while retaining integration responsibility. The vendor production unit is anchored by:
- the EPC Scope of Work (`DEL-058-01`), and
- the EPC Package Datasheet (`DEL-058-02`),

and feeds:
- the Construction Work Package (`DEL-058-03`),
- the Vendor Document Turnover Package (`DEL-058-05`), and
- the EPC Vendor Package Review and Acceptance (`DEL-058-06`).

The MPFF separator is a critical inlet-liquids processing vessel (V-7110-1, V-7310-1) on each of two trains; together with the stabilizer flash/feed and stabilizer tower, it constitutes the front of condensate stabilization for the 04-25 Deepcut configuration. [Source: DBM-Deepcut process arrangement; MPFF and Stabilizer Train Relationship]

## Principles

1. **EPC inputs are authoritative.** The vendor designs *from* `DEL-058-01` and `DEL-058-02`, not from independent process interpretation. Where the EPC Package Datasheet conflicts with DBM-derived guidance, the Package Datasheet governs because it is the controlled handoff document. [Source: `_CONTEXT.md`; decomposition row 71]
2. **Stricter requirement governs.** The DBM-Deepcut explicitly states that where unit-specific or vendor requirements are stricter than the broader DBM, the stricter requirement applies. [Source: DBM-Deepcut]
3. **Preserve options under thermal-re-simulation uncertainty.** Nozzle provisions for the MPFF hydrocarbon liquid heater bundle (E-7120-1 and parallel) shall be preserved even if retention is under evaluation; this avoids stranding the heater bundle option. [Source: DBM-Deepcut MPFF feed conditions]
4. **Mistex internals, no internal coating** are the source-default. Departures require source-supported rationale. [Source: DBM-Deepcut MPFF feed conditions]
5. **Cold-site discipline.** -40 deg C ambient governs unless a more severe condition applies; this is not optional. [Source: DBM-Comp_and_Liquids site basis]
6. **Vendor-package scope discipline.** Keep clear boundaries with electrical/controls, civil, field construction, and cross-facility utilities. Resist absorbing scope that belongs to the EPC. [Source: DBM-Comp_and_Liquids mechanical packaging discipline paragraph]

## Considerations

- **Heater bundle disposition is open.** Retention is "under evaluation after upstream HEX installation." Vendor design should accommodate either outcome without forcing a redesign of the vessel envelope. [Source: DBM-Deepcut MPFF feed conditions]
- **Inlet conditions are TBD.** MPFF inlet temperatures and low/high operating pressures are TBD/TBC in source; designing rigidly to a single point is risky. Carry margin and surface the TBDs in the vendor design basis. [Source: DBM-Deepcut MPFF Operating and Capacity Basis]
- **Methanol injection retained as safeguard.** Even if upstream HEX outlet temperatures appear adequate, the safeguard remains. Vendor should preserve the injection nozzle and piping interface. [Source: DBM-Deepcut MPFF feed conditions]
- **Pressure regulation interaction.** MPFF pressure is set above the downstream stabilizer flash/feed separator (50 psig basis at the stabilizer flash/feed) and routed overhead to SOC third-stage suction. Pressure-control interactions cross into the SOC vendor scope; verify with the EPC Package Datasheet. [Source: DBM-Deepcut MPFF feed conditions; stabilizer flash/feed paragraph]
- **Sparing reality.** 2 x 100% normal but no spare for line-pack maximum-flow. Vendor should not over-promise capacity continuity for line-pack scenarios. [Source: DBM-Deepcut Sparing table; MPFF and Stabilizer Train Relationship]
- **Building enclosure.** "Self-framing building enclosing instrumentation and one end of the vessel" mirrors the inlet-separator pattern; do not propose substantially different enclosure types without EPC concurrence. [Source: DBM-Deepcut MPFF feed conditions]

## Trade-offs

- **Conservative heater nozzle reservation vs. shipping cost.** Reserving heater bundle nozzles when the bundle may be removed increases fabrication cost slightly but avoids a costly retrofit if retained. Source clearly directs preserving nozzle provisions. [Source: DBM-Deepcut MPFF feed conditions]
- **Coating absent (Mistex bare) vs. corrosion margin.** Source explicitly states no internal coating is specified for MPFF (compare Devchem 253 on stabilizer flash/feed). If service experience indicates otherwise, raise as a Conflict for human ruling rather than unilaterally adding coating. [Source: DBM-Deepcut MPFF feed conditions; stabilizer flash/feed paragraph]
- **TBD parameters: design now vs. wait for resolution.** Most vendor-package timelines cannot wait for full TBD resolution. Vendor design basis should explicitly list TBDs and the margin carried for each.

## Examples

- Equipment Schedule references for inclusion in the vendor scope:
  - Line 52: Medium Pressure Flash Feed Separator (MEDIUM PRESSURE FLASH FEED SEPARATOR x2) — V-7110-1
  - Line 53: Medium Pressure Flash Feed Separator (MEDIUM PRESSURE F.F. HCL HEATER BUNDLE x2) — E-7120-1
  [Source: DBM-Deepcut Equipment Schedule]
- Module assignment context: 710-1 and 730-1 are MPFF modules shipped from the shop. [Source: DBM-Deepcut Module/Shop assignment table]

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| C-058-04-001 | DBM-Deepcut specifies no MPFF relief routing explicitly while it does specify HP-flare routing for stabilizer flash/feed; required MPFF relief destination is not stated. | DBM-Deepcut MPFF feed conditions paragraph | DBM-Deepcut stabilizer flash/feed paragraph | Datasheet "Blowdown"; Specification R2.6; Procedure Step 6 | EPC Package Datasheet (`DEL-058-02`) is the controlling source for vendor relief routing. | TBD |
| C-058-04-002 | DBM lists `ISO 13631 / API SPEC 11P` for packaged reciprocating gas compressors only; no MPFF-separator-specific governing code/edition is in the locally accessible source set. | DBM-Deepcut standards table | _REFERENCES.md (no MPFF-specific standard listed) | Specification "Standards"; Verification table | EPC Package Datasheet (`DEL-058-02`) shall enumerate applicable code editions for vessel design. | TBD |
| C-058-04-003 | Workbook Packages row 71 and `26020-Package_Requirements.docx` heading 13 are referenced as source basis but are not locally accessible in text form; vendor scope details that depend solely on those sources are TBD. | `_REFERENCES.md` "Missing / Deferred References" | Decomposition row 71 | All sections relying on `26020-Package_Requirements.docx` | Convert source slices to locally accessible text before final vendor scope freeze. | TBD |
