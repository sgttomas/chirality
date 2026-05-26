# Specification: DEL-075-06 — EPC Vendor Package Review and Acceptance (Cryogenic Unit / PKG-075)

## Scope

This Specification defines what the EPC Integrator must do to **review and accept** the Cryogenic Unit (PKG-075) vendor package against the EPC Scope of Work, the Package Datasheet, and the Construction Work Package, culminating in package handoff readiness.

**In scope**
- Vendor document review of the UltraTEF cryogenic unit package (BAHX, cold separator, J-T valve, turbo-expander/compressor, propane absorber, deethanizer, deethanizer reflux system, reboiler, expander aftercooler, methanol injection and storage, lube-oil and seal-gas auxiliaries).
- Integration acceptance against upstream (molecular-sieve dehydration / MRU / dust filter) and downstream (sales gas compression, NGL treating, drains, flare, fuel gas, heat medium, VRU) interfaces defined in DBM SEC-06.
- Handoff readiness: test/inspection evidence collation and turnover-records acceptance.

**Out of scope**
- Engineering, design, fabrication, or supply of the vendor package itself (that is `DEL-075-04_vendor-engineered-equipment-package`, ASSUMPTION by analogy to the sibling-row pattern at `DELIVERABLE_REGISTER.csv` L45-L101).
- Vendor document register, submittals, and turnover records authorship (that is `DEL-075-05_vendor-document-turnover-package`, same ASSUMPTION basis).
- Process design basis changes — the DBM SEC-06 basis is authoritative input, not reopened by this deliverable.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| R-01 | EPC Integrator shall review all vendor documents in the PKG-075 vendor document submittal package and record a disposition (accept / accept-with-comments / reject) for each. | `_CONTEXT.md` "Anticipated Artifacts" — "Vendor document review log" |
| R-02 | The accepted vendor package shall demonstrate UltraTEF expander-mode performance consistent with the DBM design point: inlet 7,129 kPag, design winter 14.2 °C / summer 40.5 °C, sales flow at BAHX C-pass outlet 281.2 MMSCFD (summer) / 286 MMSCFD (winter). | DBM L1305-L1312 |
| R-03 | BAHX shall be ALPEMA 3rd-Edition + manufacturer-practice compliant with vendor exceptions documented; ASME U Stamp and BC CRN required; minimum 10 % excess area on all passes; 0 mm corrosion allowance; maximum design temperature 150 °F (66 °C). EPC acceptance shall verify exception list, U Stamp, and CRN records. | DBM L1324 |
| R-04 | Turbo-expander/compressor package shall be supplied with: SCR-controlled electric seal-gas heater; 2 × 100 % duplex seal-gas filters; 2 × 100 % lead/lag lube-oil pumps; aerial lube-oil cooler in expander building; dual bladder lube-oil accumulators sized for ≥ 1 minute lube-oil flow after ESD; duplex lube-oil filters; x/y bearing vibration monitoring. EPC acceptance shall verify each subsystem against vendor data sheets and test records. | DBM L1323 |
| R-05 | J-T valve shall be supplied with mechanical stop or physical stroke limit such that control-failure mass flow to the propane absorber does not exceed cryogenic flare design flow. EPC acceptance shall verify the stroke limit setting against the cryogenic flare design flow. | DBM L1321 |
| R-06 | Methanol injection system shall provide injection capability to BAHX pass inlets (upstream of strainers), J-T valve inlet, inlet separators (upstream of PCV and upstream of HCL/water dump valves), and the acid-gas compressor package; designed for one-point-at-a-time injection. Capacities and required injection-point list remain TBC (DBM L1392). EPC acceptance shall confirm vendor-supplied points against the final approved injection-point list. | DBM L1328; L1392 |
| R-07 | Pumps (absorber bottoms, deethanizer reflux) shall be single-stage vertical inline API-610 with dual mechanical seal API-682 Plan 14/52 (Plan 13/52 or modified 13/52 acceptable for reflux pumps) and space/anti-condensation heater; 2 × 115 % winter-case sizing. EPC acceptance shall verify API compliance and seal-plan implementation. | DBM L1331; L1335 |
| R-08 | Deethanizer reboiler shall be TEMA BKU with hot-oil tube-side service at 350 °F heat medium and ≥ 25 °F (13.9 °C) minimum approach in expander mode. EPC acceptance shall verify thermal-design data against this basis. | DBM L1336 |
| R-09 | Cryogenic dry-out plan shall be reviewed and accepted before start-up (initial dry-out header operating pressure ~250 psig assumption, header MAWP and sales compressor discharge pressure assumptions remain to be confirmed per DBM L1390). EPC acceptance shall include a dry-out procedure review record. | DBM L1285; L1347; L1390 |
| R-10 | Integration with upstream molecular-sieve dehydration shall protect BAHX from over-temperature on new-bed bring-online (gas temperature ≤ 66 °C). EPC acceptance shall verify the interlock against this limit. | DBM L1257 |
| R-11 | Mercury protection: vendor shall describe BAHX mercury-tolerant features (TBD per DBM L1393). EPC acceptance shall record the vendor's mercury-tolerance approach and flag any open issues as `NEEDS_HUMAN_RULING` for project decision. | DBM L1324; L1393 |
| R-12 | Construction Work Package alignment: vendor package shall be reviewed for installability against the outdoor multilevel cryogenic-module installation basis. | DBM L1134-L1135 |
| R-13 | EPC Integrator shall produce and accept a package acceptance checklist covering all R-01 through R-12 items plus turnover evidence (test/inspection records). | `_CONTEXT.md` "Anticipated Artifacts" |
| R-14 | Detailed clause-level vendor requirements derived from 26020-Package_Requirements.docx package heading 29 — `location TBD` (not locally accessible in this run); EPC acceptance shall map each clause to a checklist row when that source is opened. | `_REFERENCES.md` "Source Materials Referenced By Decomposition Row" |

## Standards

| Standard | Application | Local accessibility |
|---|---|---|
| ALPEMA 3rd Edition | BAHX design | not locally available; cited via DBM L1324 (`location TBD`) |
| ASME (U Stamp) | BAHX pressure-vessel certification | not locally available (`location TBD`) |
| BC CRN | BAHX provincial registration | not locally available (`location TBD`) |
| API 610 | Centrifugal pumps (absorber bottoms, deethanizer reflux) | not locally available; cited via DBM L1331; L1335 |
| API 682 | Pump mechanical seal plans (Plan 14/52; Plan 13/52 acceptable for reflux) | not locally available; cited via DBM L1331; L1335 |
| TEMA (BKU) | Deethanizer reboiler shell type | not locally available; cited via DBM L1336 |

## Verification

| Requirement | Verification approach |
|---|---|
| R-01 | Vendor document review log — disposition per document |
| R-02 | Performance review against DBM SEC-06 design point; vendor process simulation records |
| R-03 | Document review — vendor exception list, U-Stamp data report, BC CRN registration |
| R-04 | Sub-component datasheet review; FAT records for lube-oil and seal-gas auxiliaries |
| R-05 | Mechanical-stop setting inspection / certificate review against the cryogenic flare design flow |
| R-06 | Injection-point P&ID review against the approved injection-point list (closure of DBM L1392 TBC required) |
| R-07 | API-610 data sheet review and API-682 seal-plan drawing review |
| R-08 | Reboiler thermal data-sheet review |
| R-09 | Dry-out procedure document review and acceptance signoff |
| R-10 | Interlock logic / cause-and-effect review (BAHX over-temperature ≤ 66 °C) |
| R-11 | Vendor mercury-tolerance description review; open-issue log |
| R-12 | Module installation drawing review against site multilevel arrangement |
| R-13 | Checklist closeout review |
| R-14 | Cross-reference matrix to 26020-Package_Requirements.docx heading 29 (TBD until that source is opened) |

## Documentation

The deliverable shall produce, per `_CONTEXT.md`:

- Vendor document review log
- Package acceptance checklist (closing R-01 through R-13; R-14 deferred TBD)
- Test/inspection evidence file
- Turnover evidence file
