# Guidance — DEL-058-06 EPC Vendor Package Review and Acceptance

## Purpose

This deliverable provides the EPC Integrator's binding evidence that the Package Vendor's engineered package and turnover documentation for PKG-058 Medium Pressure Flash Feed Separator (MPFF) — separators V-7110-1, V-7310-1 and HCL heater bundles E-7120-1, E-7320-1 within shop-assembled modules 710-1 and 730-1 — satisfy the EPC anchor deliverables (`DEL-058-01` Scope of Work, `DEL-058-02` Package Datasheet, `DEL-058-03` Construction Work Package) and are ready for integration into the broader 4-25 West Doe Deepcut inlet liquids processing train.

Sources: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §"MPFF Operating and Capacity Basis"; §"MPFF and Stabilizer Train Relationship"; `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`.

## Principles

- **Acceptance is integrator-led, not vendor-self-certified.** `_CONTEXT.md` and the decomposition register assign EPC Integrator as the lead responsible party with Package Vendor input.
- **Evidence is anchored to the source's enumerated artifacts.** The `26020-Package_Requirements.docx` package heading 13 enumeration is the canonical vendor-deliverable artifact set; the DBM-Deepcut MPFF slice is the design-basis source. Acceptance does not invent new artifact requirements; it confirms presence and adequacy.
- **Train coupling is preserved.** Acceptance must verify the one-MPFF-to-one-stabilizer coupling and the 2 x 100% sparing basis; deviations would invalidate the inlet liquids processing operating envelope.
- **Open items are surfaced, not silently closed.** The DBM-Deepcut MPFF slice carries explicit open items (heater bundle disposition, post-HEX inlet temperatures, methanol injection retention, 350 deg F supply basis, tube-sheet seal-weld requirements, stabilizer sparing / operating split). The acceptance pack records explicit disposition for each.
- **Numeric design values come from vendor submittals.** Until the vendor Pressure Vessel Data Sheet, process datasheet, heat-medium duty calc, and mechanical calc package are accepted, numeric values remain `TBD` rather than asserted from decomposition prose. (ASSUMPTION — typical EPC practice; aligns with source's own TBD/TBC markers.)
- **Binding acceptance requires human sign-off.** Per `K-AUTH-1`, no agent may certify or approve acceptance. The acceptance evidence is the proposal; the human EPC Integrator authority is the decider.

## Considerations

- **HCL heater bundle disposition is a live design decision.** DBM-Deepcut states retention, de-rating, removal, supply-temperature basis (originally 350 deg F), and tube-sheet seal-weld requirements are all TBC after thermal re-simulation. The acceptance pack should not lock in vendor build for the bundle until the disposition memo is issued; vessel nozzle provisions are preserved as a hedge.
- **Methanol injection safeguard.** Source retains methanol injection upstream of the MPFF inlet level/pressure control valve as a hydrate-suppression safeguard pending confirmation that upstream HEX outlet temperatures satisfy hydrate margins. The acceptance pack should verify the injection point is present and configured even if not always in service.
- **Overhead routing to SOC.** Source confirms overhead vapour pressure-regulated to SOC third-stage suction. The acceptance pack must verify the SOC interface in the as-built package, not merely the MPFF outlet flange.
- **LP fuel-gas purge.** Source requires LP fuel gas (downstream of the fuel-gas scrubber) regulated to maintain MPFF pressure above the downstream stabilizer flash/feed separator, and available for sour-gas sweep during maintenance. The vendor package must include the purge connection and its regulator/check arrangement; this is an explicit operational interface, not just a tie-in.
- **Module / shop-assembly basis.** Modules 710-1 and 730-1 are shop-assembled with self-framing buildings enclosing instrumentation and one end of the vessel. Acceptance walk-downs need to be planned against shop-assembled rather than stick-built configuration.
- **Interface evidence depth.** The `26020-Packages_Interfaces_4_export.xlsx` row for PKG-058 is a binary source — exact column-level interface marks are TBD in this drafting pass. Acceptance reviewers must consult that row directly.

## Trade-offs

- **Depth of vendor re-engineering review vs. timeline.** EPC Integrator review must be deep enough to find configuration mismatches against `DEL-058-02` but cannot substitute for vendor engineering. The default disposition for purely vendor-engineering details with consistent source-grounded inputs is "accepted on evidence" rather than re-derivation.
- **Heater bundle retention vs. removal acceptance strategy.** If the upstream disposition is "retain", acceptance must verify heat-medium duty (762 kW / bundle) and revised supply temperature. If "remove", acceptance must verify nozzle blinding and any bypass piping. The acceptance pack should be drafted to support either branch.
- **Open-items closure vs. carryover.** Items that cannot be closed before package handoff should be carried with named owners (e.g., heater bundle disposition memo carried with process engineering lead) rather than left silent; this preserves traceability into commissioning.
- **Single acceptance bundle vs. staged acceptance.** A staged approach (engineering acceptance → fabrication acceptance → turnover acceptance) aligns with the artifact maturity progression. (ASSUMPTION — staging not mandated in source.)

## Examples

- **Acceptance checklist structuring.** Mirror the artifact groupings typically found in `26020-Package_Requirements.docx` vendor-deliverable enumerations (core vendor documents; core package engineering; static pressure equipment; heat exchanger; process piping interfaces; relief / flare / vent; drainage / containment; electrical / EHT / grounding; I&C). Reviewers audit one functional area at a time. (ASSUMPTION — exact grouping for heading 13 to be confirmed from the binary source.)
- **Open-items log row.** For "heater bundle disposition", row carries: source citation = DBM-Deepcut §"MPFF Operating and Capacity Basis"; owner = process engineering lead; disposition decision date target = before fabrication release; current state = open; vendor-package consequence = nozzle provisions preserved; affected acceptance requirements = `R-058-06-09`, `R-058-06-10`.
- **Interface acceptance row.** For "heat medium supply to E-7120-1", row carries: condition = 118 deg C / 245 deg F supply; vendor artifact = heat-medium piping iso + heater bundle datasheet; verification = walk-down + thermal performance test record; status = TBD until vendor docs submitted.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| `CONF-058-06-01` | DBM-Deepcut §"MPFF Operating and Capacity Basis" records the heater bundle 350 deg F supply basis as "TBC" / superseded after thermal re-simulation, while the same source's Heat Medium Users table shows 118 deg C / 245 deg F supply for E-7120-1 / E-7320-1. | DBM-Deepcut §"MPFF Operating and Capacity Basis" | DBM-Deepcut §"Heat Medium Users and Duties" | `Datasheet.md` Conditions table (heater bundle supply); `Specification.md` `R-058-06-09`, `R-058-06-10` | Treat the Heat Medium Users table (118 deg C / 245 deg F) as the current basis; treat 350 deg F as a legacy figure to be confirmed against the post-HEX thermal re-simulation outcome. | TBD — pending upstream heat-medium duty / re-simulation ruling. |
| `CONF-058-06-02` | DBM-Deepcut §"MPFF and Stabilizer Train Relationship" states 3 installed stabilizer units at 04-25 on a 3 x 40% design basis, while equipment register row for "Inlet Stabilizers" enumerates units 1, 2, and 4 (skipping 3). | DBM-Deepcut §"MPFF and Stabilizer Train Relationship" | DBM-Deepcut equipment register (Inlet Stabilizers rows) | Acceptance verification of MPFF-to-stabilizer pairing (`R-058-06-05`) | This conflict is upstream of MPFF acceptance; for this deliverable, document which MPFF (V-7110-1 vs V-7310-1) is paired to which installed stabilizer per the as-built and carry the equipment-register-numbering discrepancy as an upstream open item. | TBD — pending stabilizer package owner ruling. |
