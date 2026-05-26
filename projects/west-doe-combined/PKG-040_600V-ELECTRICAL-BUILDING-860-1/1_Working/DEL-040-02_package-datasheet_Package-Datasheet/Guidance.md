# Guidance — DEL-040-02 Package Datasheet (PKG-040 600V Electrical Building 860-1)

> Directional guidance for the EPC Integrator who populates this Package Datasheet and the reviewers who consume it. Not a substitute for the Specification.

## Purpose

The Package Datasheet exists because the 600V Electrical Building (860-1) is procured as a **shop-fabricated, modular package** under a Package Vendor, while integration into the facility — site, civil, interfaces, tie-ins — is owned by the EPC Integrator. The datasheet is the **handoff artifact** that lets a third-party vendor (or a discipline-only engineering office) design and build the package without reading the entire project DBM, and lets EPC Integration verify that the resulting package fits the facility.

This is the Gate 5 EPC anchor deliverable for PKG-040. By project decision (see `_CONTEXT.md` Notes), interface facts are intentionally carried **here** as evidence rather than spun out into standalone deliverables.

Sources: `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row 42; `DELIVERABLE_REGISTER.csv` DEL-040-02 Notes.

## Principles

1. **Source authority above narrative authority.** When the DBMs and the decomposition narrative diverge, the DBMs win. Cite source slice (file + section) for every non-trivial claim.
2. **Mark TBD; do not invent.** The datasheet is consumed by an external vendor. Inventing a transformer kVA or a heater rating creates a fictitious envelope the vendor will price against. Better to publish `TBD — pending detailed electrical engineering`.
3. **Boundary clarity over completeness.** The most important value the datasheet provides is a clear vendor / EPC boundary. If a value is unclear, label its owner (Package Vendor or EPC Integrator) even if the value itself is `TBD`.
4. **Interface-row discipline.** Every interface type registered in `INTERFACE_REGISTER.csv` must surface as a row in the datasheet's interface matrix. Do not collapse or merge — downstream tools rely on the type vocabulary.
5. **Carry evidence forward, not inferences.** The Notes on `_CONTEXT.md` explicitly state interface facts are "carried here as evidence rather than standalone deliverables." Cite where each interface fact came from (DBM section, vendor proposal, drawing) rather than restating it as if novel.

## Considerations

### Carrying the 12 interfaces

The decomposition registers 12 interface types for this package (`INTERFACE_REGISTER.csv` rows 262–273). For a 600V electrical building specifically:
- **Electrical Power** and **Grounding / Bonding** are the primary interfaces — the building is itself a power distribution hub.
- **I&C / Control Cabling** and **Communications / Network** matter because the building houses PLC panels and network racks per `4-25_Deepcut_DBM.md` Electrical Buildings.
- **Building HVAC / Services** is non-trivial because n+1 HVAC is mandated.
- **Utility Piping**, **Drain / Containment**, **Grading / Site Drainage / Spill Containment** apply at the building envelope and the under-building space (the building is elevated on piles per the DBM).
- **Fire & Gas / Safety Systems** matters because the building is sited in a GP area adjacent to classified areas — detector and ESD interfaces cross the wall.
- **Maintenance Access** matters because equipment doors must accommodate the largest housed equipment per the DBM.
- **Structural / Foundations / Supports** is owned at the EPC side (foundation design) and the vendor side (skid structure).

### Standby power

The current basis (`4-25_Deepcut_DBM.md` Standby Power) is **LV standby generators with transfer switches at the 600 V MCC level**, replacing the prior centralized 13.8 kV emergency-generator concept. Generator count, ratings, and load-shedding logic are explicitly TBD. Do not promise a generator topology in the datasheet — describe the **tie-in point** and the **interface envelope**.

### Building heater clause

`4-25_Deepcut_DBM.md` states "Electric building heaters shall be provided as 600 V, 3 phase rated equipment." This is unusually specific in the DBM and should be carried verbatim in the datasheet's design conditions — it tells the vendor exactly what to spec.

### Equipment door sizing

`4-25_Deepcut_DBM.md` requires that "Equipment doors shall be sized for, or include removable transom sections to allow, removal of the largest equipment." For a 600V general-area building, the largest equipment is typically the MCC main incoming section or the largest distribution transformer. The datasheet should require the vendor to identify the **governing equipment** for door sizing.

## Trade-offs

| Trade-off | Direction |
|---|---|
| Specify every value vs. leave fields TBD | Prefer TBD where source is silent. A TBD with a named owner is more useful to the vendor than a guessed number that gets renegotiated. |
| Replicate DBM text vs. cite it | Cite the DBM and quote only the operative clauses (color schedule, heater voltage, n+1 HVAC, bottom entry). Don't restate the whole electrical basis. |
| Bundle interfaces vs. list them individually | List individually — the 12-row interface matrix is the decomposition's chosen granularity. |
| Carry vendor design choices vs. carry only envelope | Carry envelope only. Vendor design choices belong in DEL-040-04 (Vendor Engineered Equipment Package). |

## Examples

**Good datasheet row (sourced):**
> Building HVAC: HVAC sized as n+1 system; cooling system tolerates failure or maintenance shutdown of one HVAC unit without affecting building heating and cooling. *Source: `4-25_Deepcut_DBM.md` Electrical Buildings.*

**Good TBD row (sourced as TBD):**
> Standby generator count, rating, transfer-switch type, automatic vs. manual transfer, paralleling provisions, load-shedding sequence: **TBD pending electrical studies and TOU standard confirmation**. *Source: `4-25_Deepcut_DBM.md` Standby Power.*

**Bad row (invented):**
> Standby generator: 1 x 600 V, 500 kW, automatic transfer at 600 V MCC. *(No source — this value is not in either DBM and would commit the project to a topology that has not been studied.)*

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CF-001 | Building 860-1 is labelled "600V General Area / Tank Farm Electrical Building" in Deepcut DBM building list, but the project package name is "600V ELECTRICAL BUILDING (860-1)" with no general-area / tank-farm qualifier. | `4-25_Deepcut_DBM.md` Building list (#56) — "600V General Area / Tank Farm Electrical Building" | `PACKAGE_REGISTER.csv` row 42 / `_CONTEXT.md` — "600V ELECTRICAL BUILDING (860-1)" | Datasheet Identification; Specification scope | PROPOSAL: treat the Deepcut DBM building list as the descriptive authority for what loads the building serves (general area + tank farm), while keeping the package register name as the canonical Package Name. Document both in the Datasheet Identification table. | TBD |
| CF-002 | Power System bullet list in `4-25_Deepcut_DBM.md` Power System enumerates four downstream electrical buildings (6.9 kV, 4.16 kV, 600 V Acid Gas, 600 V Sales/Overheads, 4.16 kV/600 V General/Tank/Process) — the **600V General Area / Tank Farm** (#860-1) appears in the building list but is not separately enumerated in the Power System bullets; the closest match is "4.16 kV/600 V General Area/Tank Farm/Process Electrical Building." | `4-25_Deepcut_DBM.md` Building list (#56 "860-1") | `4-25_Deepcut_DBM.md` Power System "4.16 kV/600 V General Area/Tank Farm/Process Electrical Building" | Datasheet Power System Context; Specification R9 (voltages housed) | PROPOSAL: ASSUMPTION — 860-1 is the 600 V section of the combined 4.16 kV/600 V general-area building family. Confirm scope split (does 860-1 contain only 600V equipment, or is it the 600V half of a combined building?). | TBD |
| CF-003 | The PKG-040 register lists package exclusions as "TBD; no package-specific exclusions stated in source materials." | `PACKAGE_REGISTER.csv` row 42 | (no countering source) | Datasheet Exclusions | PROPOSAL: confirm with EPC Integrator that there are genuinely no exclusions for this package (e.g., cathodic protection is excluded from facility design scope per `4-25_Deepcut_DBM.md` Cathodic Protection — does that exclusion flow down to this package?). | TBD |
