# Procedure: DEL-041-04 — Vendor Engineered Equipment Package

## Purpose

Procedure to produce the Vendor Engineered Equipment Package for PKG-041 (13.8 kV, 3.0 MW standby generator building 490-1) from the EPC handoff and to ready it for EPC integration review and acceptance.

## Prerequisites

- EPC Scope of Work (`DEL-041-01`) issued/available.
- EPC Package Datasheet (`DEL-041-02`) issued/available (vendor engineering handoff basis — `ART-8FF7B18574`).
- Package interface requirements matrix (`ART-7F81FF2CB4`) and per-interface facts (`ART-0096A23E12` ... `ART-E2472057A2`) issued/available.
- Vendor engineering and supply contract awarded to a qualified Package Vendor.
- `_REFERENCES.md` deliverable-specific source slices copied where needed (currently noted Missing/Deferred).

Declared upstream dependencies (`_DEPENDENCIES.md`): none declared during PREPARATION — informational dependency on `DEL-041-01` and `DEL-041-02` is ASSUMPTION based on `DELIVERABLE_REGISTER.csv` (GATE-07) Description column.

## Steps

1. **Receive EPC handoff.** Package Vendor receives `DEL-041-01` and `DEL-041-02` from the EPC Integrator. Confirm version and acceptance state.
2. **Establish vendor design basis.** Author the vendor package design basis from `DEL-041-02` (load/duty, voltage, rating, site/environment, codes, interfaces). Output: vendor design basis (component of `ART-0CD9C13301`).
3. **Develop vendor datasheet set.** Produce vendor datasheets for the generator set, generator breaker / switchgear, controls / protective relays, ancillaries (fuel, cooling, exhaust, starting, lube), and building/enclosure as applicable. Output: vendor datasheet set (component of `ART-0CD9C13301`).
4. **Engineer the package.** Perform vendor package engineering (electrical one-lines, protection coordination, control narratives, layout, P&IDs as needed, structural mounting). Cross-check each of the twelve `INTERFACE_REGISTER.csv` rows for design adequacy. `TBD` deliverable-internal engineering checklists pending vendor selection.
5. **Issue for EPC interface review.** Submit vendor design basis and datasheet set to the EPC Integrator for interface compliance review against `DEL-041-02`. Capture review comments and incorporate.
6. **Fabricate / supply.** Fabricate and supply the physical equipment package per the accepted engineered design. Output: `ART-E2164EA14C` (vendor engineered physical equipment package).
7. **Factory/shop testing.** Execute factory/shop test and inspection of the assembled package. Test/inspection evidence flows to `DEL-041-06` as `ART-53AD41FE27`. Specific test list `TBD` (not in accessible sources).
8. **Vendor document compilation.** Compile vendor documentation for turnover via `DEL-041-05`. (Out-of-scope production but enabled by this deliverable.)
9. **Submit for EPC acceptance.** Submit the engineered, fabricated package and supporting documentation to the EPC Integrator for `DEL-041-06` review and acceptance.

## Verification

| Step | Verification |
|---|---|
| 2-3 | Vendor design basis and datasheet set internally reviewed for consistency with `DEL-041-02` |
| 4 | Each `INTERFACE_REGISTER.csv` row for PKG-041 has a design response in the vendor package |
| 5 | EPC interface review comments closed |
| 6 | Receiving inspection at site (out-of-scope, via `DEL-041-03`/`DEL-041-06`) |
| 7 | Factory acceptance test (FAT) report; specific acceptance criteria `TBD` |
| 9 | EPC acceptance recorded per `DEL-041-06` (`ART-0E8BDED2A8`) |

## Records

- Vendor package design basis and datasheet set (`ART-0CD9C13301`).
- Vendor engineered physical equipment package as-delivered evidence (`ART-E2164EA14C`).
- EPC interface review comment log (TBD — captured under `DEL-041-06` `ART-9E33107762`).
- Factory/shop test and inspection evidence (TBD — captured under `DEL-041-06` `ART-53AD41FE27`).
