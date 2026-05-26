# Guidance — DEL-061-02 Package Datasheet (PKG-061)

## Purpose

This deliverable is the mandatory **Gate 5 EPC anchor** package datasheet for PKG-061 (NGL Booster and Transfer Pumps Building). It is the EPC Integrator's technical handoff that lets a package vendor (or another discipline) take ownership of detailed package engineering. The datasheet is intentionally a **carrier of interface and design-basis facts** rather than a standalone vendor specification. Source: `_CONTEXT.md` "Notes"; PACKAGE_REGISTER.csv ResponsibilityDescription.

## Principles

1. **Source-grounded.** Every non-trivial value originates in `26020-Package_Requirements.docx` (package heading 17, `26020-01-PT-18-004 - LPG Booster`), the DBM row, or PACKAGE_REGISTER.csv. Where the source carries `TBC`/`TBD`, the datasheet carries it forward verbatim rather than inventing values.
2. **EPC vs. vendor ownership boundary.** Package vendor owns package engineering, design, vendor documentation, and physical equipment. EPC Integrator owns integration into the functional process facility (interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration). Source: PACKAGE_REGISTER.csv.
3. **API 610 multi-stage can family.** The two booster pumps are explicitly vertical multistage can-type and API 610 — this fixes the rotating-equipment archetype before vendor selection. Source: docx; DBM row 58.
4. **Booster sizing carries a real ΔP target.** 25 psid / 172 kPad differential is a hard sizing requirement from the source. TDH (and thus motor power) depends on system layout and is TBD until the hydraulic study (PRO-013) is closed.
5. **Interface applicability is a register fact; row-level rows are TBC.** Treat the PKG-061 applicable interface types as governing applicability; reconcile each row against `26020-Packages_Interfaces_4_export.xlsx` in the package-interface deliverable, not here.
6. **By-others items are exclusions, not gaps.** DCS integration, foundations, and MCC electrical supply belong to EPC Integrator scope, not the package vendor. The datasheet must declare these explicitly so the vendor does not double-quote them.

## Considerations

- **Naming vs. service.** Building name ("NGL Booster and Transfer Pumps Building") and Word section title ("LPG Booster") disagree on service fluid. Treat **LPG** as the service per accessible sources; the "NGL" building label is likely a building-grouping name. Surface this as a conflict (see Conflict Table).
- **Single Word heading, two pumps.** Both P-9570-1 and P-9580-1 are covered by one Word package heading; treat the heading as the package source slice for both pumps.
- **Building / enclosure.** Package name implies a building; docx lists "HVAC/enclosure" but does not detail building construction. Treat building scope as **ASSUMPTION** pending coordination with civil/structural discipline.
- **Seal plan 13/52.** API 682/API 610 Plan 13 (vent to suction) with auxiliary Plan 52 (unpressurised buffer) implies a hydrocarbon flashing service — consistent with LPG.
- **Motor voltage.** 575 V matches Canadian industrial mid-voltage; consistent with project facility convention seen across the DBM.

## Trade-offs

- **Booster pump count vs. redundancy.** Two parallel pumps each sized for 150% capacity gives N+1-like redundancy at full design flow; vendor sizing must confirm individual-pump operation does not under-deliver against system curve.
- **Can-type vs. horizontal multistage.** Vertical can layout reduces footprint and improves NPSH-available margin for low-margin LPG service but raises maintenance access requirements — reflected as a register-applicable "Maintenance Access" interface.
- **CRN / TSBC scope.** Registering the pressure boundary as a CRN'd package (vs. component-level CRN by vendor) shifts the project's regulatory acceptance pathway. Datasheet states "as applicable" — leave the choice with the vendor pending B.C. jurisdiction confirmation.

## Examples

- Sister package PKG (e.g., NGL Loading Pumps Building, DBM row 59) uses rotary-vane pumps for a different LPG-product service — confirms that the multi-stage can selection here is service-specific, not a default. Source: DBM row 59.
- Tank Farm Pump Building 2 (DBM rows 80-84) couples water/condensate/caustic transfer pumps in a single building — supports the precedent that "Pumps Building" packages bundle multiple skids; PKG-061 in contrast is a single-skid pump package per the Word source.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONFLICT-01 | Service fluid label: "NGL" (building name) vs "LPG" (Word heading + Basic Scope) | `_CONTEXT.md` PackageName "NGL Booster and Transfer Pumps Building"; DBM row 58 row title | `_Sources/26020-Package_Requirements.docx` §26020-01-PT-18-004 "LPG Booster"; Basic Scope "LPG storage to the LACT unit"; PACKAGE_REGISTER.csv BasicScope | Datasheet "Identification", "Attributes", "Conditions"; Specification §Scope, R-2/R-6 | PROPOSAL: treat service fluid as LPG per Word heading and Basic Scope; retain the building/folder name as a label of record; update folder/decomposition name in a separate change | TBD |
| CONFLICT-02 | Building scope (self-framing/HVAC/electrical room) implied by package name but not detailed in Word source | Package/folder name "Pumps Building" | docx §26020-01-PT-18-004 lists "HVAC/enclosure" only | Datasheet "Construction"; Specification R-8 | PROPOSAL: keep building scope as ASSUMPTION; defer detailed building scope to civil/structural deliverables in PKG-061 | TBD |
| CONFLICT-03 | TDH and motor power not specified at source; only ΔP and flow are pinned | docx §26020-01-PT-18-004 "Scope Notes / Open Items" ("TBD TDH") | None | Datasheet "Conditions" R-6 row; Specification R-6 | PROPOSAL: carry TDH/power as TBD until PRO-013 (Pump Hydraulic / NPSH Calculations) is closed | TBD |

## TBD register

- TDH per pump
- Motor power per pump
- Operating temperature/pressure envelope (LPG service detail)
- Materials of construction
- Area classification
- Detailed interface row applicability (deferred to package-interface deliverable)
- Building/enclosure detailed scope (Conflict-02)
