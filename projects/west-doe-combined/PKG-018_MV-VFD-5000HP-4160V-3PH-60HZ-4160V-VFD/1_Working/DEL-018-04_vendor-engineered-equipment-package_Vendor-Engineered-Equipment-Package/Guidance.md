# Guidance: DEL-018-04 — Vendor Engineered Equipment Package (PKG-018 MV VFD)

Directional guidance for producing and reviewing the Package Vendor production unit for PKG-018. This guidance complements (does not replace) the EPC Scope of Work (`DEL-018-01`), the EPC Package Datasheet (`DEL-018-02`), and accepted DBM source slices.

## Purpose

This deliverable carries the **vendor side** of PKG-018: the engineering, design, fabrication/supply, and physical equipment package for the 4160 V class MV VFD that supports a nominally 5000 HP, 3-phase, 60 Hz motor. The EPC Integrator owns facility-level integration; the vendor owns package engineering, package design, vendor documentation, and the physical equipment package [GATE-07 `PACKAGE_REGISTER.csv` row 20].

## Principles

- **EPC anchors first.** The EPC Scope of Work (`DEL-018-01`) and EPC Package Datasheet (`DEL-018-02`) are the authoritative interface contract for the vendor. Vendor engineering must not derive motor or interface parameters from the package title.
- **DBM context, not requirements.** The 03-25 Comp_and_Liquids DBM and 04-25 Deepcut DBM provide directional electrical basis for the facility but do not stand in for the EPC Package Datasheet. Where DBM and the EPC Package Datasheet disagree, the EPC Package Datasheet governs the vendor.
- **No invention from the title.** "5000 HP" in the package title is an identity label. The DBM places inlet/sales gas compressor motors at 3,878 kW / 5,200 hp (Comp_and_Liquids) and 6,700 hp (Deepcut, conflicted); the Vendor uses confirmed EPC Package Datasheet values, not the package title or DBM narrative.
- **Detailed-design items remain detailed-design items.** VFD sizing is explicitly an electrical detailed-design item per DBM; vendor engineering closes those items with calculations and study outputs.

## Considerations

- **Starting vs continuous service.** Comp_and_Liquids DBM frames the basis as a starting VFD with synchronous transfer; Deepcut DBM keeps 4.16 kV VFD/soft-start requirements as `TBD`. The vendor should clarify which duty the EPC Package Datasheet selects before fixing the drive lineup and cooling design.
- **Harmonic and reactive-power posture.** Capacitor banks at the MCC-8200 synchronous-transfer bus are explicitly removed where VFDs are present (SCA-001 VE #37). Harmonic and reactive-power mitigation is to be set by detailed studies — vendor should plan filter / transformer impedance / multi-pulse topology choices accordingly.
- **Area classification.** When the VFD feeds a motor in a Zone 2 area, the motor T-code requirement is stricter than the area classification or fugitive-emissions study T-code; the vendor's drive output should not push the motor into noncompliance.
- **Building basis.** The facility houses medium-voltage VFDs in prefabricated, modular electrical buildings; vendor lineup dimensions, access, and HVAC heat loads should accommodate that installation context.
- **Communications.** Other MCC lineups in the facility provide EtherNet to the plant PLC central control panel; aligning the VFD HMI/controls communications with that pattern reduces facility-level integration friction.

## Trade-offs

- **Drive topology vs harmonic posture.** Multi-pulse or active-front-end designs reduce harmonic content but increase footprint, transformer count, and cost; passive harmonic filters trade tuning robustness against capital cost.
- **Drive isolation transformer vs direct-coupled.** Isolation transformers ease grounding and common-mode mitigation but add footprint, losses, and weight; direct coupling reduces these costs but pushes more responsibility to motor cabling and bearing protection.
- **Starting-VFD-only vs full-time inverter duty.** A starting VFD with synchronous transfer is mechanically smaller and may be redundant across motors; full-time inverter duty enables turndown but requires continuous-rated cooling, larger filters, and continuous motor inverter-duty insulation systems.
- **Single vendor lineup vs split vendor scope.** A fully integrated vendor lineup simplifies acceptance under `DEL-018-06` but concentrates schedule and quality risk; splitting drive vs transformer vs filter scopes spreads risk but multiplies integration burden for the EPC Integrator.

## Examples

No vendor-package design examples are present in the accessible source set; do not invent examples. See `DEL-018-02` (Package Datasheet) once issued for example terminal-point and interface-matrix patterns.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-018-04-001 | Package title says "5000 HP" but DBM data values for inlet/sales gas compressor motors are "3,878 kW / 5,200 hp" (Comp_and_Liquids) and "6,700 hp" (Deepcut). | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 324, 533 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 893 | Datasheet Attributes; Specification R-018-04-002, R-018-04-012 | Treat the package title "5000 HP" as identity only; defer motor rating to the EPC Package Datasheet (`DEL-018-02`); flag the DBM-to-DBM hp conflict for facility-level resolution rather than vendor-package resolution. | TBD |
| CONF-018-04-002 | DBM disagrees on the 4.16 kV motor starting basis: Comp_and_Liquids treats inlet compressor motors as starting-VFD per SCA-001 VE #34; Deepcut leaves "VFD and soft-starter requirements for 4.16 kV motors are TBD." | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 326, 756 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2957, 3088 | Specification R-018-04-006; Procedure prerequisites and verification | Vendor sizing should not start until the EPC Package Datasheet selects starting-only vs continuous-duty operation; record selection in the Vendor Package Design Basis. | TBD |
| CONF-018-04-003 | Communications topology to the plant PLC is documented at the 4160V MCC level (EtherNet), not at the MV VFD package level, in the accessible source set. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 754; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2957 | (no direct MV VFD-level source slice) | Specification R-018-04-007; Datasheet Construction (Communications) | Carry EtherNet-to-PLC as an **ASSUMPTION** until the EPC Package Datasheet specifies VFD-level communications. | TBD |
| CONF-018-04-004 | Objective-to-deliverable association is by package-grouping heuristic (PACKAGE_HEURISTIC), not by explicit deliverable-ID mapping at row 425/893/1427. | `_CONTEXT.md`; GATE-07 `OBJECTIVE_DELIVERABLE_MAP.csv` rows 425, 893, 1427 | (no explicit deliverable-ID objective binding) | Datasheet Identification (Supports Objectives) | Treat objective association as ASSUMPTION (best-effort mapping) until ORCHESTRATOR confirms. | TBD |
