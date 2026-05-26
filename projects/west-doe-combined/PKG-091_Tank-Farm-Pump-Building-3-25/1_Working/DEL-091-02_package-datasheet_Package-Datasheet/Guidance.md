# Guidance — DEL-091-02 Package Datasheet (Tank Farm Pump Building 3-25)

## Purpose

The Package Datasheet exists so that a third-party package vendor or discipline engineering group can perform package engineering and design for PKG-091 Tank Farm Pump Building 3-25 from a single source-grounded EPC technical handoff. Per DELIVERABLE_REGISTER, this deliverable is a "mandatory Gate 5 EPC anchor deliverable" and intentionally carries interface facts as evidence rather than spawning separate interface deliverables (_CONTEXT.md Notes; DELIVERABLE_REGISTER notes).

## Principles

- **Source fidelity over completeness.** The workbook row 84 and Word heading 44 source slices contain many TBC/TBD entries. The datasheet preserves them; it does not invent values to look complete (skill authority hierarchy; SKILL.md Step 4 source-grounding rule).
- **Responsibility split.** Package Vendor owns engineering/design/vendor documentation/physical equipment. EPC Integrator owns integration into the functional process facility — interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration (PACKAGE_REGISTER responsibility-mode cell).
- **Interface coverage by enumeration.** Fifteen interface types apply; none are out of scope; the datasheet enumerates each with its InterfaceID so downstream integration is unambiguous (INTERFACE_REGISTER.csv).
- **Anchor for vendor production unit.** The Package Datasheet plus the EPC Scope of Work (DEL-091-01) jointly anchor the Vendor Engineered Equipment Package (DEL-091-04) per the DELIVERABLE_REGISTER note.

## Considerations

- The Word source has visible truncations (the "Condensate." sentence; trailing "Powered by." for Condensate Sweetening feed pumps; "Condensate Loading." in throughput). The datasheet reproduces these as authored and flags them rather than guessing.
- Several pumps share seal plan API-682 Plan 14/52; the vertical inline centrifugal family should be treated as a seal-plan-consistent set when soliciting vendor proposals.
- All motors must be sized for inlet stabilizer composition density at −40 °C start-up — this is the binding sizing condition and should drive vendor motor sizing calculations even when other operating conditions are TBC.
- Starting method (DOL or VFD) is alternative; the EPC Integrator must rule on which is required by service before vendor RFQ closes (NEEDS_HUMAN_RULING when reaching that gate).
- The package is mechanical/process-mechanical; electrical, I&C, civil/structural, and HVAC interfaces are EPC Integrator deliverables that connect through the fifteen-row interface matrix.

## Trade-offs

- **TBC retention vs. closure.** Preserving source-stated TBC values protects against fabrication but defers decisions. Downstream tasks must close these (operating/design conditions, sour condensate booster capacity, sweet condensate feed capacity, condensate booster capacity, condensate loading capacity) before vendor commitment.
- **Per-equipment datasheet vs. package-level datasheet.** This deliverable is the package-level datasheet only. Individual equipment datasheets remain Package Vendor scope (DEL-091-04). ASSUMPTION: vendor will produce equipment-level datasheets as part of their engineered package; this is not explicitly stated in the carried source slice (location TBD in vendor documentation requirements).
- **DOL vs. VFD.** Source allows both; choice affects motor sizing, MCC bucket sizing, and harmonic profile. Decision deferred; capture as TBD with proposal at vendor RFQ stage.

## Examples

Example interface row to be carried in the datasheet (illustrative, drawn from INTERFACE_REGISTER row IFC-4A728F3420):

```
InterfaceID:   IFC-4A728F3420
Package:       PKG-091 — Tank Farm Pump Building 3-25
Type:          Process Piping
Applies:       YES
Owner:         EPC Integrator (facility-level integration)
Vendor scope:  Package nozzle locations, ratings, and pipe-class break points within the vendor skid
EPC scope:     Tie-in piping outside the skid, including produced water suction/discharge, sour/sweet condensate routing, and discharge to the produced water pipeline
Source:        Workbook Packages row 84
```

Example equipment row (illustrative, from SOW-0187 P-9290/9293-2):

```
Tag:           P-9290-2 / P-9293-2 (2x)
Service:       Water Transfer Pumps
Type:          Radial centrifugal
Seal plan:     Single mechanical
Power:         150 kW (200 HP)
Driver:        575 V / 3 Ph / 60 Hz
Sizing basis:  −40 °C inlet stabilizer composition density start-up
```

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CF-1 | Source truncation: "Condensate." sentence in process function ends abruptly. | PACKAGE_REGISTER.csv PKG-091 process function | SCOPE_LEDGER SOW-0186 | Datasheet > Construction; Guidance > Purpose | PROPOSAL: retain truncation, mark downstream condensate routing as TBD pending fuller Word slice. | TBD |
| CF-2 | Voltage line for Condensate Sweetening Feed Pumps reads "Powered by." with no value. | SCOPE_LEDGER SOW-0187 | SOW-0188 site/driver default 575 V / 3 Ph / 60 Hz | Datasheet > Attributes (P-9210/9220-2) | PROPOSAL: apply package-wide 575 V / 3 Ph / 60 Hz default; label ASSUMPTION until vendor confirms. | TBD |
| CF-3 | "TBC" capacity values for Sour Condensate Booster, Sweet Condensate Feed, Condensate Booster, Condensate Loading. | SCOPE_LEDGER SOW-0188 | (none) | Datasheet > Conditions; Spec R-3, R-12 | PROPOSAL: hold as TBC; resolve at vendor RFQ via DEL-091-04 inputs. | TBD |
