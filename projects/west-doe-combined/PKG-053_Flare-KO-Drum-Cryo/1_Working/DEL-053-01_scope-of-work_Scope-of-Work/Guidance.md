# Guidance: DEL-053-01_scope-of-work — Scope of Work

## Purpose

This guidance supports drafting and review of the `PKG-053 — Flare KO Drum (Cryo)` EPC scope of work. The deliverable exists to turn the accepted decomposition basis for SOW-0067 through SOW-0070 into a bounded vendor-engineered Mechanical package scope with clear interfaces, source basis, responsibility split, and integration narrative for the West Doe Deepcut (04-25) facility.

## Principles

- Preserve the Gate 7 package identity exactly: `PKG-053`, `Flare KO Drum (Cryo)`, Mechanical, WBS 01, CoA tracking number `26020-01-17-001` (`PACKAGE_REGISTER.csv`, PKG-053).
- Preserve the tagged equipment exactly as the source uses them: V-4110-1 for the cryogenic flare KO drum and H-4112-1 for the electric immersion heater (`4-25_Deepcut_DBM.md`, SEC-09 Flare Systems; Tagged Equipment table row 11).
- Treat the workbook row and Gate 7 registers as the authoritative decomposition truth for package membership and deliverable identity, and the 04-25 Deepcut DBM SEC-09 as the authoritative source for cryogenic flare system basis.
- Use `TBD` for package-specific design values (drum dimensions, MAWP, MDMT, nozzle schedule, heater rating and control philosophy, instrumentation, foundation loads, tie-in coordinates). Do not infer values from package name or generic flare conventions.
- Keep the Package Vendor vs EPC Integrator responsibility split explicit and conservative: Package Vendor owns engineering, design, vendor documentation, and physical equipment; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration (`PACKAGE_REGISTER.csv`, PKG-053).
- Treat the non-sour service classification as a brief-level statement and flag it for source-basis re-confirmation; do not silently propagate it as a finalized service basis (`SCOPE_LEDGER.csv`, SOW-0070).

## Considerations

The Flare KO Drum (Cryo) is a vendor-engineered Mechanical package with an unusually broad interface footprint for a single drum: nine declared interface types covering process piping, the cryogenic relief header, drains, electrical power for the immersion heater, EHT, grounding/bonding, controls cabling, maintenance access, and structural/foundations (`INTERFACE_REGISTER.csv`, PKG-053). The scope-of-work narrative should treat the interface set as the primary structuring spine of the deliverable.

The DBM places this package squarely inside the cryogenic flare subsystem: cryogenic-unit reliefs and molecular-sieve-dehydrated streams relieving below -45.5 deg C connect to a 610 mm (24 in) relief header that feeds V-4110-1, and the cryogenic flare header then combines with the HP flare header downstream of both KO drums before the common HP/cryo stack (`4-25_Deepcut_DBM.md`, SEC-09 Flare Systems). The scope of work should describe both battery limits (upstream relief header tie-in, downstream combination point) and explicitly exclude V-4100-1 (HP), V-3900-1 (LP), and the common stack.

The immersion heater (H-4112-1) is included in the package and drives the Electrical Power, EHT, and I&C / Control Cabling interfaces. The integration narrative should highlight that the heater is a single integrated supply with the drum and that EPC Integrator scope must coordinate power, area classification, and heater control philosophy.

Drain handling is unusual for this service: the cryogenic drain header is a segregated header with minimum 300# ANSI design-pressure basis, is not heat traced because no water is expected (mole-sieve dehydration upstream), and is insulated only for personnel protection in accessible areas (`4-25_Deepcut_DBM.md`, SEC-09 Drains; Cryogenic drain row). The scope should explicitly state these basis items so they are not lost when downstream design teams interpret "drain" by analogy with hot/wet services.

Relief volumes for the cryogenic flare are TBD at this stage; preliminary Aspen Flare System Analyzer models support current header sizing but the drum sizing case must be confirmed at detailed engineering. The scope of work should route drum sizing inputs explicitly to DEL-053-02 (Package Datasheet) rather than attempting to specify them here.

## Trade-offs

| Topic | Guidance |
|---|---|
| Early scope completeness vs source fidelity | Include the required EPC scope-of-work structure and battery-limit narrative now, but leave drum and heater design values as `TBD` and route them to the Package Datasheet. |
| Package Vendor vs EPC Integrator wording | Use the `PACKAGE_REGISTER.csv` responsibility text verbatim as the canonical split; do not paraphrase the boundary. |
| Service classification (sour vs non-sour) | Carry the non-sour brief statement but flag it as requiring source-basis re-confirmation; the cost of being wrong here is material (metallurgy, MDMT, NACE compliance). |
| Header and drain sizing | Use DBM SEC-09 values (610 mm relief header; 300# ANSI segregated drain) directly; do not derive flow or pressure design from package-level assumptions. |
| Spacing and plot plan | Cite the 10 m KO-drum-to-fire-hazard spacing from SEC-02 as a basis; defer final plot plan verification to the issued site layout. |
| Heater control philosophy | Acknowledge the heater is included but leave duty, rating, control logic, and area classification details as `TBD` in this deliverable. |

## Examples

- Acceptable wording: "PKG-053 supplies V-4110-1 (cryogenic flare KO drum) and H-4112-1 (electric immersion heater) as a single equipment package serving cryogenic-unit reliefs and molecular-sieve-dehydrated systems relieving below -45.5 deg C."
- Acceptable wording: "Drum sizing, MAWP, MDMT, and immersion heater duty are TBD and will be issued via DEL-053-02 Package Datasheet."
- Acceptable wording: "The cryogenic flare header (610 mm, 24 in) ties into V-4110-1 upstream and combines with the HP flare header downstream of both KO drums before the common HP/cryo stack."
- Avoid: "The cryogenic flare KO drum shall be sized for X minutes of holdup" unless a cited source provides that holdup basis.
- Avoid: "The package is supplied by the EPC Integrator" — the package responsibility model is Package Vendor for engineering/design/equipment and EPC Integrator for facility integration.
- Avoid: "The drum is in sour service" — the brief states non-sour; do not flip the basis without source-supported re-confirmation.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-053-01 | Service classification: brief states non-sour, but no detailed source-level service review of cryogenic-flare contributing streams has been recorded in the deliverable-local source slices. | `SCOPE_LEDGER.csv`, SOW-0070 (non-sour per brief) | `4-25_Deepcut_DBM.md`, SEC-09 Flare Systems (does not explicitly classify cryogenic flare KO drum service as sour or non-sour) | Datasheet Conditions; Specification REQ-053-06; Procedure Steps | Carry non-sour as the working basis with an explicit re-confirmation action at DEL-053-02 issue. | TBD |
| HRR-053-02 | Drum-level design parameters (sizing, MAWP, MDMT, nozzles, heater duty/control, materials) are not stated in accessible source slices at the deliverable level. | `PACKAGE_REGISTER.csv`, PKG-053 (interfaces and basic scope only) | `4-25_Deepcut_DBM.md`, SEC-09 Flare Systems (header sizing and service basis only) | Datasheet Construction; Specification REQ-053-14; Procedure Steps | Mark all drum/heater design values as TBD and route to DEL-053-02 Package Datasheet rather than inferring them at scope-of-work issue. | TBD |
| HRR-053-03 | Common HP/cryo stack location: SEC-09 places the common HP/cryo flare stack physically at 03-25 and shared with 04-25, while PKG-053 is a 04-25 (Deepcut) package. The scope-of-work battery limit at the HP/cryo header combine point is clear, but the downstream stack scope split is not closed in deliverable-local references. | `4-25_Deepcut_DBM.md`, SEC-09 Flare Systems (common HP/cryo stack at 03-25) | `PACKAGE_REGISTER.csv`, PKG-053 (4-25 facility, WBS 01) | Specification REQ-053-09; Guidance Considerations; Procedure Steps | Set PKG-053 battery limit at the cryogenic-to-HP combine point downstream of V-4110-1 and exclude the common stack from this scope. | TBD |
