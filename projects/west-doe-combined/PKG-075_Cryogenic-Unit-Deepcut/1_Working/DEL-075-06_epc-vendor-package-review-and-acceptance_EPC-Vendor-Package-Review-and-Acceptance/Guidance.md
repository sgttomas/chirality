# Guidance: DEL-075-06 — EPC Vendor Package Review and Acceptance (Cryogenic Unit / PKG-075)

## Purpose

This Guidance frames how the EPC Integrator should approach review and acceptance of the PKG-075 Cryogenic Unit vendor package so that interface integrity, performance basis, safety functions, and turnover evidence are preserved through handoff. It is directional context for the Specification's normative requirements; it is not itself a binding requirements set.

## Principles

1. **Source authority is the DBM, not vendor literature.** The UltraTEF cryogenic unit basis (DBM SEC-06, L1098-L1396) governs what "acceptable" means. Vendor performance claims that exceed or conflict with the DBM basis shall be flagged, not silently adopted.
2. **Acceptance protects interfaces first.** PKG-075 sits between molecular-sieve-dried feed gas and sales-gas / NGL-treating downstream. Off-basis vendor decisions ripple to sales-gas total sulphur compliance, NGL treating loading, BAHX integrity, and flare loading. (Source: DBM L1113; L1122-L1123; L1369-L1378; L442.)
3. **Operating-mode duality is non-negotiable.** Expander mode is normal; J-T mode is for start-up and off-design. Both must be acceptable in vendor scope. (Source: DBM L1341-L1347.)
4. **TBD/TBC items in the DBM are not closed by acceptance.** Many UltraTEF items are explicitly `TBC` (e.g., J-T-mode C4+ recoveries, methanol injection capacity, BAHX mercury tolerance, A-pass bypass capacity, F-pass bleed) — DBM L1349-L1351 and L1391-L1395. EPC acceptance shall record these as open items, not as resolved.

## Considerations

### Performance and operating modes

The UltraTEF unit must deliver 99+ % propane recovery in expander mode and at least 27 % C3 recovery in J-T mode for sales-gas total sulphur compliance (DBM L1345-L1346; sales-gas total-sulphur dependence on cryogenic recovery is DBM L442). Vendor performance evidence shall cover both modes; expander-only test evidence is insufficient for full acceptance.

### Safety and protective functions

Key protective functions cited in DBM L1363 must each have a verifiable vendor implementation:

- J-T valve pressure control with **mechanical stroke limit** so control-failure flow does not exceed cryogenic flare design flow (DBM L1321; L1363).
- Turbo-expander **anti-surge recycle** with seal-gas and lube-oil permissives, and ESD-rundown lube-oil accumulator capacity ≥ 1 minute (DBM L1322-L1323; L1363).
- **BAHX A-pass bypass** temperature control and **E-pass bypass** MDMT protection (DBM L1326; L1333; L1363).
- **Methanol injection** for hydrate/freezing management (DBM L1328; L1363).
- **Cryogenic dry-out at low pressure** to prevent freezing/overcooling (DBM L1347; L1363).

### BAHX integrity

BAHX is the highest-consequence single asset in the package. Acceptance must confirm: ALPEMA + manufacturer practice with documented vendor exceptions; ASME U Stamp; BC CRN; ≥ 10 % excess area on all passes; 0 mm corrosion allowance; 150 °F (66 °C) maximum design temperature; mercury-tolerant features as developed; methanol injection at each pass inlet; tee strainers upstream of each pass with start-up fine-mesh and normal baskets; ≤ 2 psid clean ΔP and ≤ 15 psid change-out ΔP (DBM L1324-L1325). The 66 °C limit is reinforced by the upstream molecular-sieve bed-bring-online rule (DBM L1257) — a facility-shutdown condition.

### Interface validation

Interface scope at acceptance (DBM L1365-L1378) covers: upstream molecular-sieve and mercury-removal feeds, sales-gas compression downstream of BAHX/expander compressor outlet, NGL treating downstream of the deethanizer bottoms, dry-out header, fuel gas, heat medium (350 °F to deethanizer reboiler), VRU, produced-water/drain routing for cryogenic liquids, and flare loading (cryogenic flare design flow as the J-T stroke-limit basis).

### Trade-offs

| Trade-off | Discussion |
|---|---|
| Single design point (summer, expander) vs. winter performance check | DBM L1299 sets only one design point; winter is expected performance and must be checked in towers, pumps, and reboiler for hydraulics. EPC acceptance shall require a winter check rather than treating summer-design certification as sufficient. |
| Future NGL interface provisions vs. current scope | Future deethanizer bottoms exchanger and cooler (DBM L1337-L1338) are future-scope provisions; vendor package shall include provisions without committing to future equipment supply. Conflate-or-defer trade-off should default to defer. |
| Mercury tolerance — vendor approach vs. mercury-removal-unit dependence | MRU upstream of cryogenic unit is the primary mercury barrier (DBM L1243; L1362). BAHX mercury tolerance is a defense-in-depth item. Acceptance shall capture the vendor's stance and not double-credit MRU performance. |

### Examples / illustrations from source

- Sales-gas total sulphur recoverability driven by cryogenic-unit recovery is described at DBM L442; this couples PKG-075 performance to commercial pipeline acceptability.
- The UltraTEF area is "outdoor cryogenic modules with cold separator, J-T valve, turbo-expander/compressor building, six-pass BAHX, methanol injection, propane absorber, absorber bottoms pumps, deethanizer, deethanizer reflux system, deethanizer reboiler, future bottoms exchanger/cooler provisions, and expander aftercooler" (DBM L1135) — the acceptance scope mirrors this equipment list.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-01 | Detailed package-clause requirements (26020-Package_Requirements.docx package heading 29) are referenced by the decomposition row but not locally accessible. | `_REFERENCES.md` "Source Materials Referenced By Decomposition Row" | `_Sources/` (file `26020-Package_Requirements.docx` present but `.docx` not parsable in this run) | Specification R-14; Procedure step "Vendor document review" | PROPOSAL: convert `.docx` to `.md` and reread before acceptance signoff; until then, mark all heading-29-derived requirements `location TBD`. | TBD |
| C-02 | Objective-to-deliverable association for `DEL-075-06` is package-heuristic (PKG-075 grouping) per `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC`; not deliverable-ID explicit. | `_CONTEXT.md` "Supports Objectives" | Gate-07 `OBJECTIVE_DELIVERABLE_MAP.csv` (deliverable-ID explicit mapping not verified in this run) | Datasheet "Supports Objectives" | PROPOSAL: retain as ASSUMPTION until objective map is opened and confirmed. | TBD |
