# Guidance — DEL-083-04 Vendor Engineered Equipment Package (Inlet Separators 3-25)

## Purpose

This deliverable produces the physical and engineered output that the Package Vendor delivers for the PKG-083 Inlet Separators 3-25 production unit. It anchors vendor execution against the EPC Scope of Work (`DEL-083-01`) and the EPC Package Datasheet (`DEL-083-02`), and feeds downstream EPC review (`DEL-083-06`) and turnover (`DEL-083-05`). Source: `_CONTEXT.md` Scope; decomposition row DEL-083-04.

## Principles

- **Source-anchored vendor engineering.** Vendor design choices for V-1600-2 and V-1700-2 shall be traceable to the EPC Scope of Work, EPC Package Datasheet, and the 03-25 DBM. Where the DBM marks a value `TBD` or `TBC`, vendor proposals must be raised as engineering queries, not unilaterally fixed.
- **50/50 capacity philosophy.** Both separators are equally sized at half facility capacity with no spare; reliability is achieved through identical parallel trains, not redundancy. Source: DBM line 570.
- **Sour service first.** Material selection, coating (Devchem 253), corrosion allowance, and inspection access are governed by sour-service requirements; vendor shall not value-engineer these without explicit EPC ruling. Source: DBM lines 256, 611.
- **Interface discipline.** Drive-gas recycle, ESDV setpoints, methanol drain handling, and inlet PCV symmetry are interfaces with EPC piping and 04-25 facilities; vendor terminations must match.
- **Building extent deferred.** Heated self-framing building scope is `TBD` at this stage and shall be resolved jointly with the EPC Integrator before vendor finalizes the package GA. Source: DBM line 260.

## Considerations

- **Capacity-sparing language reconciliation.** The DBM carries both `2 x 50%` (current) and older `2 x 100%` language; the vendor shall execute against the current basis and surface any references that suggest otherwise. Source: line 570.
- **Inlet temperature reconciliation.** The DBM notes that downstream excerpts may require confirmation against the inlet design temperature (8.3 deg C). Vendor sizing of demisters, level controls, and slug volume must use the reconciled basis. Source: line 258.
- **Slug and flowback.** Frac flowback (not pigging) is the governing transient liquid case; vendor separator volume (~38 m3) and downstream stabilization at 04-25 (six-hour processing window) bound the operational envelope. Source: lines 255, 270.
- **Methanol disposition.** Methanol is expected at the separator boot; downstream routing is `TBD` and may impose vendor drain design changes when resolved. Source: line 218.
- **Building/utility interfaces.** Inlet separator package buildings are listed in the facility building inventory and tie to shared utilities; vendor heating, instrument-air supply (from 04-25), and electrical feeds must be coordinated with EPC. Source: line 706.

## Trade-offs

- **Single combined skid vs split skids.** Source does not prescribe vendor skid breakdown; vendor may propose a single skid per separator or a split arrangement provided transport, FAT, and field tie-in remain practical. Treat as `PROPOSAL` until EPC accepts.
- **Internal coating scope.** Devchem 253 is required internally; piping is uncoated under the current basis. Extending coating to ancillary piping for life-cycle reasons is a vendor `PROPOSAL` and requires EPC ruling.
- **Building enclosure extent.** Smaller enclosed envelope reduces capex/footprint but may compromise winter operability; larger envelope improves operability at higher cost. Resolve once building extent `TBD` is closed.

## Examples

- **Sparing example.** Two identical 40 MMSCFD separators handle full 80 MMSCFD facility capacity with no installed spare; planned outages take the facility to 50% throughput. Source: DBM line 570, line 244.
- **Control-valve example.** Per package: ≥ 2 parallel inlet PCVs (balanced globe, hardened trim, ΔP ≤ 5 psid) and ≥ 2 parallel produced-water LCVs. Source: line 266.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted Sections | Proposed Authority (PROPOSAL) | Human Ruling |
|---|---|---|---|---|---|---|
| C-01 | Sparing philosophy: `2 x 50%` vs `2 x 100%` | DBM 3-25 line 570 (`2 x 50%`, current) | DBM 3-25 line 570 (older `2 x 100%` language flagged for reconciliation) | Datasheet Construction; Spec R1.1, R1.3 | Use `2 x 50%` per current basis | TBD |
| C-02 | Inlet design temperature 8.3 deg C vs downstream excerpts requiring confirmation | DBM 3-25 line 258 (inlet feed table) | DBM 3-25 line 258 note (downstream excerpts) | Spec R4.3 | Carry 8.3 deg C as basis; require EPC reconciliation before final datasheets | TBD |
| C-03 | Building extent for inlet separator packages | DBM 3-25 line 260 (`exact building extent remains TBD`) | DBM 3-25 line 706 (package buildings listed as known) | Spec R7.1; Datasheet Construction | Vendor proposes minimal heated envelope for instruments + one end; revise on EPC ruling | TBD |
| C-04 | Pig receiver size | DBM 3-25 line 230 (`size is TBD`) | n/a | Vendor coordination interface (not vendor scope but adjacent) | Defer to EPC SoW | TBD |
