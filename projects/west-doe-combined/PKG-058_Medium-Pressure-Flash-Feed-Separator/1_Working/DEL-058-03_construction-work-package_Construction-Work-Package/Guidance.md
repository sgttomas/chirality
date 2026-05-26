# Guidance — Construction Work Package (DEL-058-03)

## Purpose

This Construction Work Package (CWP) is the EPC Integrator's anchor deliverable describing how the `PKG-058 Medium Pressure Flash Feed Separator` package (shop-fabricated modules `710-1` and `730-1`) is physically installed, built, inspected, turned over, and tied into the larger 04-25 Deepcut facility. It exists so that the Tourmaline field construction organization, which holds most field execution scope, has an integrated EPC-authored package-level workface plan to execute against, including handoff and interface points for the vendor-engineered equipment package (`DEL-058-04`). Reference: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 100-127 (Construction Responsibility table) and `_CONTEXT.md` Scope.

## Principles

- **Source-grounded scope.** The construction responsibility split between EPC Integrator and Tourmaline is normatively defined by the DBM Construction Responsibility table (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 105-126). Do not author CWP work that contradicts that split.
- **Two parallel units, independently maintainable.** Modules `710-1` and `730-1` are duplicate 100% units (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2366). Construction sequencing should preserve the unit-basis maintenance-isolation philosophy (line 2408) so a single unit can be brought online while the other remains under construction or rework.
- **Preserve optionality pending heater bundle disposition.** Because the MPFF hydrocarbon liquid heater bundle (`E-7120-1`) retention is under engineering reassessment (line 674), the CWP should preserve nozzle provisions and heat-medium tie-in stubs rather than commit to either fit-or-cap until disposition is confirmed.
- **Tie-in joint planning.** Tie-ins to existing or related facilities require joint planning, and tie-in timing is established as the project progresses (line 127). The CWP should not assume a fixed tie-in window.
- **Cold-weather constructability.** Site design ambient down to -40 °C and snow loads up to Ss = 2.5 kPa (lines 198, 206-207) shape sequencing, lifting plans, hydrotest fluid choice, and curing windows.

## Considerations

- **Module fabrication source.** Modules `710-1` and `730-1` are shop-built (lines 2804, 2806). Off-loading, setting, and mechanical hookup are Tourmaline field-construction scope (lines 112-114). The CWP is therefore primarily an EPC-authored work-pack handed to Tourmaline execution crews, not a self-perform package.
- **Vessel layout and instrumentation enclosure.** The MPFF package is configured similarly to the inlet separator, with a self-framing building enclosing instrumentation and one end of the vessel (line 672). Building close-up sequencing affects instrument access, F&G loop checks, and winter heat tracing.
- **Methanol injection retention.** Methanol injection upstream of the MPFF inlet LV/PV is a retained safeguard (line 674). The CWP should treat the methanol tie-in as part of mechanical completion, not as a deferred future-tie-in.
- **Foundation handoff is gated by geotechnical.** Foundation, piling, and bearing-capacity criteria depend on the geotechnical report (line 2834). The CWP cannot specify final foundation acceptance criteria without that input; carry as `TBD` until released.

## Trade-offs

| Trade-off | Direction supported by source | Rationale |
|---|---|---|
| Pre-installing the heater bundle vs. installing nozzle blanks | Install with nozzle preservation; do not commit | Bundle retention is under reassessment (line 674); committing prematurely creates rework |
| Shop pre-fit-up of methanol injection vs. field tie-in | Maximize shop pre-fit | Reduces cold-weather field welding; consistent with shop-fabrication module strategy (lines 2804, 2806) |
| Setting both modules concurrently vs. staggered | Staggered, preserving the unit-basis maintenance philosophy | Source line 2408 favors independent unit isolation; staggered set/test allows one unit to mechanical-complete while the other is in rework |

## Examples

- **Tie-in workface example.** A workface plan for the MPFF inlet line should reference the upstream inlet separator liquid outlet header (per MPFF feed routing described in `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 668) and identify the level control valve tie-in as the point where methanol injection (R6) is installed.
- **Pressure-control tie-in example.** MPFF overhead vapour is pressure-regulated to SOC third-stage suction (line 672). The CWP should treat that tie-in as a category-A interface requiring per-tie-in responsibility confirmation (R4).

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-1 | Module 710-1 and 730-1 are both labelled "Medium Pressure Flash Feed Module" but vessel-tag-to-module pairing not explicit in accessible source | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2804 (`710-1`) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2806 (`730-1`) | Datasheet Identification; Procedure Steps | Datasheet records `V-7110-1` for `710-1` and `V-7310-1` for `730-1` per `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 672 nomenclature; confirm during detailed engineering | TBD |
| C-2 | Heater bundle disposition (retain/de-rate/remove) | DBM source line 674 (under reassessment) | (No competing source) | Spec R5, R10, R12 | Hold nozzle/tie-in preservation until disposition confirmed | TBD |
| C-3 | Construction code/standard citations (ASME, B31.3, etc.) not explicitly tied to this CWP scope in accessible sources | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (regulatory section referenced but not parsed for this slice) | `26020-Package_Requirements.docx` package heading 13 (location TBD) | Spec Standards | Adopt typical EPC code set as ASSUMPTION; replace with explicit source citations when `26020-Package_Requirements.docx` slice is rendered locally | TBD |
