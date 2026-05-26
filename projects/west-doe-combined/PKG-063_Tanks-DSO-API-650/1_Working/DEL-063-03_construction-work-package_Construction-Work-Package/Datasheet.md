# Datasheet — DEL-063-03 Construction Work Package (Tanks, DSO (API 650))

> Descriptive datasheet for the Construction Work Package (CWP) deliverable for `PKG-063 Tanks, DSO (API 650)`. Values are sourced from the accessible Comp & Liquids Design Basis Memorandum slice covering DSO/spent-caustic handling under the non-regenerative caustic mercaptan treating package, and from this deliverable's `_CONTEXT.md`. Missing values are marked `TBD`; inferences are labelled `ASSUMPTION`.

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-063-03_construction-work-package` |
| Name | Construction Work Package |
| ParentPackageID | `PKG-063` |
| ParentWorkbookID | 63 |
| PackageName | Tanks, DSO (API 650) |
| Discipline | Mechanical (lead) with Civil/Structural, Piping, Electrical, I&C, Fire & Gas interfaces (ASSUMPTION based on tankage construction conventions; package-level interface row in `26020-Packages_Interfaces_4_export.xlsx` row 90 not directly excerpted into `_REFERENCES.md` — location TBD) |
| Type | EPC Construction Work Package |
| ResponsibleParty | EPC Integrator |
| Decomposition Snapshot | `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Construction object | DSO (disulphide oil) storage tank(s) serving the non-regenerative C5+ caustic mercaptan treating package; part of the "caustic C5+ contactor, pre-heater, caustic outlet filter, water wash, DSO/spent/fresh-caustic/fresh-water tanks, and incinerator overhead/dilution/enrichment-gas interfaces" list | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 400 |
| Tank standard | API 650 (Modified) atmospheric construction is the basis explicitly stated for the produced-water tank family in the same DBM; the DSO tank size, plate basis, and Modified clause set are `TBD` (DSO-specific tank datasheet not present in accessible sources). ASSUMPTION: DSO tank is also API 650 (Modified) atmospheric given the package name `Tanks, DSO (API 650)`. | `_CONTEXT.md` PackageName; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 421 |
| Service | DSO (disulphide oil) — by-product of non-regenerative caustic mercaptan treating of C5+ condensate | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 389, 396–402 |
| DSO entrainment (process basis) | Expected 30 ppmw S; design 50 ppmw S, TBC vendor | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 396–397 |
| Associated process pumps | DSO pumps, 2 × 100 % (pump installation is package-internal; CWP construction scope confirms pump bases/anchorage but pumps may be supplied with the package — TBD) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 577 |
| Tank count | TBD (DBM lists tank functions in the caustic system but does not enumerate a discrete count for the DSO tank — `_REFERENCES.md` has no DSO-specific tank register slice) | TBD |
| Tank capacity / dimensions | TBD (not in accessible DBM slice; vendor/EPC tank datasheet not present in `_Sources/`) | TBD |
| Internal coating | TBD for DSO service; the DBM specifies Devchem 253 for produced-water tank internals (line 256, 421) — coating selection for DSO service requires sour/sulphur compatibility review. ASSUMPTION pending detailed design. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 256, 421 |
| Insulation / heating | Externally insulated and heated is the basis stated for the produced-water tank family (line 421). ASSUMPTION DSO tank requires equivalent winterization given the −40 °C site basis (line 145). | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 145, 421 |
| Vent / blanket | TBD. Caustic-system tanks (fresh/spent caustic) are LP fuel-gas blanketed (line 402); spent caustic vents through a flame arrestor to the incinerator header (line 402). Whether DSO tank shares incinerator-header venting or has independent vent disposition is `TBD`. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 402 |
| Construction scope demarcation | "By others" scope for vendor-supplied tankage is not enumerated in the accessible DBM slice. ASSUMPTION: per the package-requirements convention used by sibling EPC CWPs (e.g. `DEL-049-03`), the EPC Integrator owns shipping/site receipt, foundation, erection (field-erected API 650 tank work), tie-in piping, electrical connections, EHT, instrumentation hook-up, painting/coating field touch-up, and platform/stairs unless vendor scope explicitly states otherwise. | ASSUMPTION; sibling-pattern reference `DEL-049-03` |

## Conditions (Construction-Relevant)

| Item | Value | Source |
|---|---|---|
| Site minimum ambient | −40 °C minimum ambient governs exposed equipment, package buildings, control panels, instrumentation, and field devices unless a more severe process or vendor condition applies | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 145 |
| Tank classification | Atmospheric (API 650) — design pressure governed by API 650 plus venting basis (vacuum/pressure relief sizing TBD) | `_CONTEXT.md` PackageName; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 421 (produced-water tank analogue) |
| Process temperature | TBD (DBM does not state DSO tank operating/design temperature) | TBD |
| Material selection | TBD. Caustic compatibility note (line 402) is for caustic tanks (Aluminum prohibited in caustic building); DSO service is hydrocarbon/sulphur — material/coating compatibility requires detailed design review | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 402 |
| Hydrotest / leak-test parameters | TBD (project pressure-test specification not in `_REFERENCES.md`; API 650 hydrostatic test per Section 7.3 of API 650 governs but project addenda are unknown). ASSUMPTION: API 650 hydrostatic test applies. | TBD; ASSUMPTION |
| Drain / containment | Hydrocarbon liquid drain is one of the declared drain systems; minimum drain-header rating 300# ANSI. Containment (bunded area) for DSO tank is `TBD`. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 493 |
| Fire & gas | LEL, H2S, methyl mercaptan, and fire detection devices shall be placed according to process hazards, building layouts, ventilation, equipment spacing, truck loading, tankage, caustic/DSO systems… detector quantity/placement remains TBD pending detailed design | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 838 |

## Construction Scope Items Covered

The CWP discharges these decomposition scope items (Source: `DELIVERABLE_REGISTER.csv` and `_CONTEXT.md` for `DEL-063-03`):

- `SOW-0209`
- `SOW-0210`
- `SOW-0211`
- `SOW-0212`

## Construction Interface Applicability (ASSUMPTION-based pattern)

Source: package-level interface row in `_Sources/26020-Packages_Interfaces_4_export.xlsx` (row 90 cited by `_CONTEXT.md` Source Reference) is not transcribed into `_REFERENCES.md`. The applicability table below is `ASSUMPTION` based on the field-erected API 650 tank type and DBM service context. Confirm against the interface workbook before issue.

| Interface | Applicability (ASSUMPTION) | Notes |
|---|---|---|
| Process Piping | Yes | DSO inlet (from caustic outlet filter / treating package), DSO transfer (DSO pumps 2 × 100 %), drain |
| Utility Piping | Yes | Fuel-gas blanket (if applicable, TBD); steam/glycol/EHT supply for heating |
| Relief / Flare / Vent | Yes (TBD destination) | Vent disposition (incinerator header vs. dedicated stack) TBD |
| Drain / Containment | Yes | Hydrocarbon liquid drain header (300# ANSI) per DBM line 493; tank bund/containment per project standard (TBD) |
| Electrical Power | Yes | DSO pumps, mixer (if any, TBD), instrumentation |
| Area / Exterior Lighting | Yes | Tank platform, valve manifolds, access |
| EHT | Yes | Cold-climate basis; piping freeze protection and tank-side instrument lines |
| Grounding / Bonding | Yes | API 650 tank grounding; truck-out bonding (if applicable, TBD) |
| Cathodic Protection | TBD | Buried inlet/outlet/drain piping and tank bottom CP — project decision |
| I&C / Control Cabling | Yes | Tank level, temperature, vent/blanket pressure, high-level alarms |
| Communications / Network | TBD | Local panel network back to facility DCS |
| Building HVAC / Services | No | Tank is outdoors (ASSUMPTION) |
| Fire & Gas / Safety Systems | Yes | LEL/H2S/methyl-mercaptan/fire detection per DBM line 838 |
| Maintenance Access | Yes | Manway, top platform, stairs |
| Grading / Site Drainage / Spill Containment | Yes | Bunded tank pad; spill drainage to slop/hydrocarbon drain |
| Structural / Foundations / Supports | Yes | Ringwall or pile-supported foundation; tank anchorage for seismic/wind |
| Product Loading | TBD | If DSO is trucked out (spent caustic is trucked out per DBM line 402); truck rack interface TBD |
| Pipeline / Pigging | No (ASSUMPTION) | DSO not a pipeline export |

## Construction Artifacts (Anticipated)

Per `_CONTEXT.md` and the decomposition `Anticipated Artifacts` field:

- Construction work package (master document set)
- Installation and tie-in workface plan
- Construction interface and turnover checklist

## References

- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — lines 145, 256, 389–402, 421, 493, 549, 577, 611, 655, 838
- `_Sources/26020-Package_Requirements.docx` — package heading 18 (cited by `_CONTEXT.md` Source Reference; specific slice not transcribed into `_REFERENCES.md` — **location TBD** for plain-text excerpt)
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — row 90 (cited by `_CONTEXT.md` Source Reference; row-level interface applicability not transcribed — **location TBD**)
- `_CONTEXT.md` (deliverable identity, package association, scope/objective mapping)
- `DELIVERABLE_REGISTER.csv` — GATE-07 snapshot row `DEL-063-03`
- `PACKAGE_REGISTER.csv` — GATE-07 snapshot row `PKG-063`
