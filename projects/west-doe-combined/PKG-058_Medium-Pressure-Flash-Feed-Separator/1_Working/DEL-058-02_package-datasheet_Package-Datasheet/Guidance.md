# Guidance — DEL-058-02 Package Datasheet (PKG-058 Medium Pressure Flash Feed Separator)

> Directional guidance for producing and consuming the PKG-058 Package Datasheet. Rationale is grounded in accessible source slices; speculative considerations are explicitly labeled.

## Purpose

This deliverable is the Gate 5 EPC anchor for PKG-058. It hands off package process basis to vendor engineering or to a downstream discipline. The datasheet is intentionally a single source of process truth for the MPFF separators and their HCL heater bundles, with interface facts carried as evidence rather than published as standalone deliverables (per `_CONTEXT.md` Notes).

## Principles

1. **Source fidelity over convention.** Values come from DBM-Deepcut §"MPFF Operating and Capacity Basis" and the heat-medium duty table. Do not back-fill from generic separator practice when the source either states a value or explicitly states TBD.
2. **Carry TBDs forward.** Source-declared TBDs (low/high operating pressure, post-HEX inlet temperature, heater bundle disposition, 03-25 routing) are surfaced — they are not resolved at this stage.
3. **Train coupling is structural.** MPFF and stabilizer are mechanically paired one-to-one. Treat MPFF availability as bounded by stabilizer availability; do not specify independent MPFF redundancy.
4. **Interface evidence belongs in this deliverable.** Per `_CONTEXT.md`, PKG-058 carries interface facts here. Downstream consumers should look in §Interfaces of the Datasheet and R5 of the Specification before searching standalone interface deliverables.
5. **No sparing for line-pack maximum.** The design 12.91 MMSCFD case requires both packages operational. Operational planning and turnaround scheduling MUST respect this.

## Considerations

- **Heater bundle option space.** The bundle may be retained, de-rated, or removed. The Datasheet preserves nozzle provisions and original sizing values so any disposition is implementable after thermal re-simulation.
- **Methanol as safeguard, not normal practice.** Methanol injection upstream of the MPFF inlet LCV remains in scope as a hydrate-suppression safeguard; vendor design should not assume continuous injection.
- **Pressure control via SOC third stage.** Overhead vapour routing to SOC stage 3 (per SOC source capacity table) drives both the MPFF operating-pressure setpoint and the high-flow line-pack response. Any change in SOC stage configuration affects MPFF basis.
- **Purge gas hierarchy.** LP fuel gas purge maintains MPFF pressure above the downstream stabilizer flash/feed separator. This hierarchy MUST be preserved when any pressure setpoint is adjusted.
- **Source extracts not locally available.** 26020-Package_Requirements.docx package heading 13 and the Packages_Interfaces export are referenced by decomposition but not locally accessible as markdown. Treat their absence as a known gap and mark dependent fields `location TBD`.

## Trade-offs

| Trade-off | Direction | Source / Rationale |
|---|---|---|
| Heater bundle retention vs. removal | Defer — preserve nozzle provisions | DBM-Deepcut §"MPFF Operating and Capacity Basis"; uncertainty after upstream HEX install |
| Tighter operating-pressure window vs. broader Low/High range | Defer until source TBDs resolve | DBM-Deepcut §"MPFF Operating and Capacity Basis"; Low/High = TBD |
| Independent MPFF sparing vs. train pairing | Train pairing is fixed by piping arrangement | DBM-Deepcut §"MPFF and Stabilizer Train Relationship" |
| Tabulating interfaces here vs. standalone interface deliverable | Tabulate here | `_CONTEXT.md` Notes: interface facts carried as evidence in this deliverable |

## Examples

- Example heater bundle row (Datasheet §Construction): `E-7120-1 / E-7320-1 — U-bundle (BKU); design duty 762 kW (2.6 MM BTU/h) each; HM supply 118 deg C, return 80 deg C; disposition TBD pending thermal re-simulation` (DBM-Deepcut §"Heat Medium Users and Duties").
- Example interface row: `MPFF overhead → SOC third-stage suction; V-7110-1 / V-7310-1; design 11.1 MMSCFD per source capacity table` (DBM-Deepcut SOC source capacity table).

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CF-058-02-01 | MPFF inlet design temperature: 40 deg C "assumed from system-level equipment data" vs. inlet-side narrative saying post-HEX temperatures are TBD/TBC | DBM-Deepcut §"MPFF Operating and Capacity Basis" (40 deg C ASSUMPTION) | DBM-Deepcut §"MPFF Operating and Capacity Basis" (post-HEX inlet temps TBD/TBC) | Datasheet §Operating Conditions; Specification R2 | PROPOSAL: keep 40 deg C as labeled ASSUMPTION until thermal re-simulation; do not promote to design value | TBD |
| CF-058-02-02 | Inlet separator quantity legacy "4 vessels" annotation in MPFF source table vs. installed-separator basis elsewhere | DBM-Deepcut §"MPFF Operating and Capacity Basis" (legacy 4-vessel reference) | DBM-Deepcut §"Inlet Separator" basis (current installed quantity) | Datasheet §Open Items | PROPOSAL: carry as upstream conflict; do not reflect "4 vessels" in MPFF basis | TBD |
| CF-058-02-03 | Heater-bundle 350 deg F supply (original basis) vs. heat-medium duty table 118/245 deg C-F supply for E-7120-1/E-7320-1 | DBM-Deepcut §"MPFF Operating and Capacity Basis" (350 deg F original) | DBM-Deepcut §"Heat Medium Users and Duties" (118 deg C / 245 deg F) | Datasheet §Construction; Specification R4 | PROPOSAL: cite both — current single-loop basis is 118/245, original sizing basis is 350 deg F TBC | TBD |
| CF-058-02-04 | Decomposition source pointer 26020-Package_Requirements.docx package heading 13 not locally accessible | `_REFERENCES.md` (decomposition row) | local source root (no extract) | All sections drawing from package requirements doc | PROPOSAL: mark dependent fields `location TBD` rather than invent | TBD |
