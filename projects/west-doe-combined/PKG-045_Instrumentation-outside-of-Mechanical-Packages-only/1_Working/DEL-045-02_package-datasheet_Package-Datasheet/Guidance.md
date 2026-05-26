# Guidance — DEL-045-02 Package Datasheet (PKG-045 Instrumentation, WBS 03)

## Purpose

PKG-045 is the WBS 03 Instrumentation package at 03-25, covering instrumentation outside of mechanical/vendor packages. The Package Datasheet is the EPC Integrator's mandatory technical-handoff document that lets a third-party vendor or discipline package engineer engineer and design the in-scope instrumentation. Per Gate 6 disposition (recorded in `INTERFACE_REGISTER.csv` PKG-045 notes), the package interface facts are carried as evidence in this datasheet rather than as standalone deliverables — so the datasheet doubles as the package's interface requirements matrix.

## Principles

- **Source authority before convention.** The DBM (`3-25_Comp_and_Liquids_DBM.md`) and the GATE-07 registers (`DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`) are the authoritative ground. Workbook Packages row 47 is the upstream anchor but is not parsed as a local slice; treat its values as carried via the registers.
- **Plug-n-play philosophy.** Per Gate 6 disposition for PKG-045 interface notes: instrumentation field supports, power, and communications are included in each package scope as appropriate. The datasheet should make this scope explicit rather than leaving it implied.
- **Safety-driven detector basis.** Detector quantity, placement, voting, set points, and calibration are explicitly TBD pending HAZOP/SIL outcomes. The datasheet should never invent these values.
- **Shared utilities posture.** 03-25 instrument air is supplied from 04-25 under SCA-006 — the datasheet must surface this dependency to any vendor reading it, since it changes the in-scope utility tie list.
- **Ambient governs field hardware.** -40 deg C is the design floor for exposed instrumentation, panels, and field devices unless a worse process/vendor condition applies.
- **Use established platforms.** BPCS = Allen-Bradley ControlLogix; RIO = Flex5000 over PRP; detector basis = MSA / General Monitors. The datasheet should align vendor expectations to these.

## Considerations

- **Outside of mechanical packages only.** PKG-045's scope explicitly excludes instrumentation integral to mechanical/vendor packages. The vendor reading this datasheet should expect to handle field-mounted, shipped-loose, and area-wide instrumentation — not skid-mounted instruments that travel with mechanical packages.
- **Wiring economy.** Detector and ESD pushbutton signals should home-run to the nearest Remote I/O panel where practical, to reduce field wiring. The datasheet should communicate this preference because it shapes panel placement and cable routing.
- **Detection scope breadth.** Fire, LEL, H2S, and methyl mercaptan detection are all in scope. Methyl mercaptan is unusual and matters specifically for caustic/DSO systems — vendors should not assume a generic gas-detection scope.
- **Alarm differentiation.** Visual (red beacon: Fire / LEL / ESD) and audible (distinct horn tones: fire / LEL / H2S / ESD trip) differentiation is required; the final tone mapping is detailed-design but the differentiation principle is set.
- **Open building list.** ESD pushbutton quantity and building-by-building placement track the final building list. The datasheet should not freeze counts that depend on a list that is not yet final.
- **Cable separation.** 13.8 kV / 4,160 V / 600 V power must be separated from control and instrument circuits by distance, shielding, or routing per project electrical specifications. This affects how a vendor lays out junction boxes, conduit, and trays in their package buildings.

## Trade-offs

- **Vendor specification vs. EPC integrator standardization.** Naming MSA / General Monitors as the manufacturer basis simplifies maintenance, sparing, and integrator alignment, but constrains vendor choice on detection hardware. The DBM has already taken this trade-off; the datasheet should reflect it without re-litigating.
- **Centralized vs. distributed I/O.** "Wired to the nearest Remote I/O control panel where practical" trades centralized BPCS panel count against distributed RIO panel proliferation; the practical-judgment clause is intentional, and the datasheet should preserve it rather than collapsing it to a single rule.
- **TBD vs. early freeze.** Freezing detector counts, tags, or set points before HAZOP/SIL would create rework risk. The datasheet's correct posture is to mark TBD and route to detailed-design.

## Examples

Authoritative examples are limited to what the DBM and registers provide. Two illustrative TBD patterns the datasheet should honor:

- ESD pushbutton table: location ("outside all building exterior doors"), wiring ("to nearest RIO panel where practical"), platform ("Allen-Bradley ControlLogix BPCS with Flex5000 RIO over PRP"), enclosure/classification/SIL = "TBD by detailed design, HAZOP, SIL".
- Instrument-air interface: supply ("from 04-25 under SCA-006"), 03-25 demand ("393 SCFM TBC"), combined demand ("1,113 SCFM TBC"), local 03-25 IA compressor ("none; superseded").

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-01 | Workbook Packages row 47 is named as the upstream source authority for the package but the source slice is not locally accessible as a parsed artifact; all package values are routed through the registers. | `_REFERENCES.md` "Source Materials Referenced By Decomposition Row"; `PACKAGE_REGISTER.csv` PKG-045 "Source" field | `_REFERENCES.md` "Missing / Deferred References" (no slices copied during PREPARATION) | Datasheet Identification & Attributes; Specification R-01 | Treat the GATE-07 registers as the proxy authority for workbook fields until the row-47 slice is parsed into `_Sources`. | TBD |
| CONF-02 | The shared HP/Cryo and LP dual flare stack and incinerator service split between 03-25 and 04-25 is an open interface item; PKG-045 instrumentation that ties to flare/vent interfaces inherits this uncertainty. | DBM SEC-04 (line 56) | DBM SEC-14 detector-placement narrative (flare/vent interfaces listed) | Datasheet Conditions; Specification R-15 | Flag the affected flare/vent instrumentation tie-ins as TBD pending the 03-25/04-25 allocation ruling; do not invent ownership. | TBD |
| CONF-03 | `_DEPENDENCIES.md` declares no Upstream/Downstream dependencies, yet DBM SEC-14 explicitly couples this package to SEC-07 (Electrical) and SEC-13 (Controls), and to HAZOP/SIL. | `_DEPENDENCIES.md` "Declared Upstream Dependencies: None declared" | DBM SEC-13 (line 774); SEC-14 narrative | Datasheet Construction; Specification R-13 | Carry SEC-07/SEC-13/HAZOP-SIL coordination as a Procedure prerequisite, mark the declared-dependency gap as a NEEDS_HUMAN_RULING for the dependency-extract pass. | TBD |
