# Guidance — DEL-091-01 Scope of Work (PKG-091 Tank Farm Pump Building 3-25)

> Directional guidance for drafting and using the Scope of Work for the
> Tank Farm Pump Building 3-25 package (PKG-091). This document explains why
> the Scope of Work is structured as it is, what principles to apply when
> filling in `TBD`/`TBC` values from later sources, and what trade-offs to
> consider when ruling on open items.

## Purpose

PKG-091 is one of the Gate-5 EPC anchor deliverables for the project
(`_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`; SCOPE_LEDGER SOW-0185). It is the
mandatory EPC Integrator deliverable that:

1. Carries the workbook-defined vendor-responsible Mechanical package
   "Tank Farm Pump Building 3-25" forward as a distinct flat project package
   for WBS 03 (SCOPE_LEDGER SOW-0185).
2. States the package function, tagged equipment list, and basic scope so
   that downstream sibling deliverables (Package Datasheet, Construction Work
   Package, Vendor Package, Vendor Document Turnover, EPC Vendor Package
   Review and Acceptance) can be produced against a single, source-anchored
   reference.
3. Records the responsibility split between Package Vendor and EPC Integrator
   (`PACKAGE_REGISTER.csv` ResponsibilityModel).
4. Provides the whole-facility integration narrative covering the 15
   applicable interface types (`INTERFACE_REGISTER.csv` PKG-091 rows).

The Scope of Work is not a per-tag datasheet, not a construction plan, and not
a vendor scope. It is the source-of-truth narrative the other five PKG-091
deliverables build from.

## Principles

1. **Source over convention.** When the workbook row, Word source heading,
   or GATE-07 register row states a value, use the source value. Do not
   substitute a project-generic convention.
2. **Carry open items as open.** Where the source records `TBC` or "Open
   items" (SCOPE_LEDGER SOW-0188 explicitly tags multiple parameters as TBC),
   carry the same `TBC`/`TBD` marker forward. Do not promote an inference to
   a value.
3. **Inferences are labeled.** Any drafting inference (e.g., voltage on
   pumps not explicitly tagged with 575 V / 3 Ph / 60 Hz) is labeled
   `ASSUMPTION` and the basis recorded.
4. **One package per scope.** PKG-091 is a flat package; do not roll PKG-060
   (Tank Farm Pump Building 4-25) content into this Scope of Work even though
   the two packages parallel each other.
5. **Battery-limit clarity.** The narrative shall distinguish what the
   Package Vendor delivers at the package battery limit from what the EPC
   Integrator delivers in facility-level integration. The 15 interface types
   are the structural skeleton of that distinction.
6. **Objectives traceability is heuristic.** The OBJ-002…OBJ-010 mapping is
   inherited from the package-grouping objective-deliverable map; record it as
   `ASSUMPTION (PACKAGE_HEURISTIC)` until the human owner confirms.

## Considerations

- **The Word source and Packages workbook are authoritative but not text-accessible.**
  `_Sources/26020-Package_Requirements.docx` (heading 44) and
  `_Sources/26020-Packages_Interfaces_4_export.xlsx` (row 84) are cited by the
  decomposition but cannot be read as text in this run. The GATE-07 registers
  carry the relevant slices into accessible CSV rows; treat those rows as the
  local authoritative source. If a downstream question requires text not in
  the registers, flag it as `NEEDS_HUMAN_RULING` rather than guess.
- **The DBM is not authoritative for this package.** `3-25_Comp_and_Liquids_DBM.md`
  is the design basis memo for the broader 3-25 Comp_and_Liquids scope but
  has no Tank Farm Pump Building section as of the GATE-07 snapshot. Do not
  draft requirements citing DBM content that is not actually present.
- **Sour-service applicability.** Sour-condensate pumps are explicitly in
  scope (SOW-0186, SOW-0187). NACE/sour-service material requirements are
  not stated in accessible sources; they must be developed against the
  facility-wide materials specification (TBD) and reflected in DEL-091-02.
- **Voltage gaps.** SOW-0187 explicitly states `575V/3Ph/60Hz` for several
  pump tags; SOW-0188 generalizes to "all pumps." The condensate-sweetening
  feed pumps (P-9210/9220-2) text in SOW-0187 trails off without the voltage
  line. Cite SOW-0188 ("All pumps driven by 575V/3PH/60Hz motors") as the
  general rule and flag the per-tag confirmation as `TBC`.
- **Inlet basket strainer (P-9240-2).** Source explicitly states size TBC.
  Carry forward.
- **Pump count between SOW-0186 and SOW-0187.** SOW-0186 lists 2 sour-
  condensate pumps and 2 condensate-sweetening feed pumps as the "basic
  scope"; SOW-0187 enumerates additional sour-condensate recycle, skim,
  booster, and product-recycle pumps. This is not a contradiction (SOW-0186
  is the basic scope statement; SOW-0187 is the major included equipment).
  Carry both into the Scope of Work using the source's own framing.

## Trade-offs

| Choice | Trade-off | Recommended posture |
|---|---|---|
| Include per-tag pump data inline vs. defer to DEL-091-02 | Inline gives readers a single document; defer keeps the Scope of Work short and DEL-091-02 authoritative for per-tag detail | Defer per-tag datasheets to DEL-091-02; keep this Scope of Work to a tagged equipment list with rated points where the source states them |
| Treat "by others" (SOW-0188) as exclusions vs. as integration handoffs | Exclusion framing is cleaner; handoff framing makes the EPC scope explicit | Use both — list "by others" as exclusions and reflect each item as an EPC-owned integration deliverable in the interface narrative (electrical supply ↔ Electrical Power interface; foundations ↔ Structural / Foundations / Supports interface; DCS integration ↔ I&C / Control Cabling and Fire & Gas / Safety Systems interfaces) |
| Include all 15 interface types vs. only the typically active ones | All 15 are explicitly recorded in `INTERFACE_REGISTER.csv`; trimming risks losing record fidelity | Include all 15; mark depth-of-narrative items `TBD` when the source does not state the interface-specific detail |
| Map objectives at deliverable ID vs. at package ID | Deliverable-ID mapping is exact but absent in the GATE-07 register row; package-ID mapping is the recorded form (PACKAGE_HEURISTIC) | Use the package-ID mapping (OBJ-002…OBJ-010) and label `ASSUMPTION` |
| Cite API-682 clause vs. cite seal plan only | Citing the clause requires API-682 text (not locally accessible); citing the plan is what the source states | Cite the seal plan (Plan 14/52) as stated by SOW-0187; mark API-682 clause `location TBD` |

## Examples

- **Tagged equipment list row (good).** "P-9290-2 / P-9293-2 — Water Transfer
  Pumps — radial centrifugal — seal plan: single mechanical — 150 kW (200 HP)
  — 575 V / 3 Ph / 60 Hz — rated 218 m³/d @ 172 kPad (40 USGPM @ 25 psid).
  Source: SCOPE_LEDGER SOW-0187, SOW-0188."
- **Open-item row (good).** "Sour Condensate Booster Pump (P-9215/9216-2)
  rated point — TBC. Source: SCOPE_LEDGER SOW-0188."
- **Invented row (do not do this).** "Sour Condensate Booster Pump rated for
  50 m³/h at 1,500 kPag." — there is no source for that value; record as
  `TBC` instead.
- **Interface narrative row (good).** "Electrical Power — EPC Integrator
  delivers electrical supply to the MCC ('by others' per SOW-0188); package
  vendor supplies pump motors per SOW-0188 (575 V / 3 Ph / 60 Hz)."

## Conflict Table (for human ruling)

No active conflicts were identified between the accessible source slices
(GATE-07 registers) during Pass 1/Pass 2. All identified gaps are recorded as
`TBD`/`TBC` in `Specification.md` and `Datasheet.md` rather than as
contradictions.

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority | Human ruling |
|---|---|---|---|---|---|---|
| (none) | — | — | — | — | — | — |
