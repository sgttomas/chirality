# Guidance — DEL-055-04 Vendor Engineered Equipment Package (LP Flare KO Drum, 4-25)

> Directional guidance for the Package Vendor and EPC Integrator working
> together on the LP Flare KO Drum package. Captures purpose, principles,
> considerations, trade-offs, and known conflicts that need human ruling.

## Purpose

The vendor engineered equipment package is the physical realization of the LP
flare knock-out duty at the 04-25 facility. It exists to:

- Translate the EPC-authored Scope of Work (DEL-055-01) and Package Datasheet
  (DEL-055-02) into a fabricable, registerable, shop-built module that the EPC
  Integrator can incorporate into the wider 04-25 facility. [`_CONTEXT.md` scope]
- Protect the LP flare stack and downstream personnel by removing entrained
  liquids from LP flare relief and blowdown vapours. [Specification REQ-055-04-01]
- Provide a clean equipment / documentation interface for facility-level
  integration, construction, turnover, and EPC acceptance. [PACKAGE_REGISTER.csv
  PKG-055; sibling deliverables DEL-055-03, DEL-055-05, DEL-055-06]

## Principles

1. **Vendor owns the package; EPC owns the facility integration.** The vendor
   produces a self-consistent package design (drum, pump, module skid,
   documentation). The EPC Integrator owns tie-ins, constructability, and
   facility-level interfaces. The line is drawn at the declared interface set
   in PACKAGE_REGISTER row PKG-055.
2. **Decomposition routes; sources determine.** The PROJECT_DECOMP routes this
   work to a vendor package; the 4-25 Deepcut DBM source slices set the
   technical envelope (service, header sizes, materials, regulatory bases).
3. **Source-grounded values only.** Values not in accessible source slices are
   carried as `TBD` and resolved during detailed engineering, not invented.
4. **Conservative on sour service.** The 04-25 facility envelope is sour; in
   the absence of an explicit sour-service material directive for this drum,
   apply NACE MR0175 / ISO 15156 as `ASSUMPTION` and let the vendor proposal
   confirm or refine.
5. **Freeze protection is the default for LP flare lines outside heated
   buildings.** The DBM explicit rule is on the HP system; LP carries
   condensable liquid and water and is treated equivalently here as an
   `ASSUMPTION` until ruled.

## Considerations

- **Module 390-1 is shop-built.** The package vendor should optimize for shop
  fabrication and modular transport rather than stick-build. Lift points,
  transport dimensions, and shipping-loose items should be identified early.
  [`4-25_Deepcut_DBM.md` line 2783]
- **Sour-service compatibility.** Wetted materials, weld procedures, hardness
  control, and NDE coverage should anticipate sour service. Confirm metallurgy
  proposal against the relief-stream compositions defined in detailed
  engineering.
- **LP header backpressure interaction.** The drum vapour outlet and downstream
  routing affect LP flare built-up backpressure. The DBM gives an HP/cryo
  built-up backpressure estimate of 695 kPag and a PSV-flange limit of 1172
  kPag at 150# rating; LP-specific built-up backpressure is `TBD`. The vendor
  package should not introduce nozzle, inlet device, or demister selections
  that compromise this envelope. [`4-25_Deepcut_DBM.md` line 2044]
- **Common LP source list is broad.** LP flare connects amine regen, TEG
  regen, VRU, reciprocating compressor seal pot, VRU blowdown, VRU suction
  bypass, primary seal vent, and contaminated mole-sieve regen blowdown.
  Composition variation matters for materials and corrosion allowance. [`4-25_Deepcut_DBM.md` lines 2029, 1781, 1787, 1801, 1702]
- **Liquids routing.** Collected liquids leave via `P-3900-1` to truck-out and
  may also route to the condensate slop tank low-pressure pump header. The
  vendor pump duty should bracket both cases. [`4-25_Deepcut_DBM.md` lines 2029, 1665]
- **Plot clearance.** The DBM imposes a 10 m clearance from KO drums to
  vegetation / fire hazards (OGAOM §9.6.15). The package footprint and skid
  layout should leave the EPC plot plan room to meet this rule. [`4-25_Deepcut_DBM.md` line 287]
- **Radiation envelope.** BCER radiation limits including a 0.7888 kW/m2 solar
  allowance apply at grade. The vendor package should not preclude the EPC
  radiation analysis from closing. [`4-25_Deepcut_DBM.md` lines 2050-2057]

## Trade-offs

- **Vertical vs horizontal drum orientation.** Not stated in accessible
  source slice. Horizontal is the typical industry default for flare KO duty
  (`ASSUMPTION`); the trade-off is plot footprint (horizontal larger) versus
  inlet/demister design simplicity (vertical typically needs taller stack).
  The package vendor proposes; EPC accepts in DEL-055-06.
- **Demister vs vane pack vs no internal.** Selection drives turn-down,
  fouling tolerance (amine and glycol carryover), and pressure drop budget.
  Trade-off not closed by accessible source slice.
- **EHT scope on the package skid vs EPC scope at the battery limit.** Either
  is defensible. EHT included in the vendor package limits coordination work
  but raises vendor scope and cost. The interface declaration in the package
  register lists EHT; the package datasheet (DEL-055-02) should resolve the
  exact battery limit before vendor RFQ.
- **Truck-out vs slop-header as primary destination for collected liquids.**
  Both are mentioned in source slices. The primary destination affects pump
  sizing, control philosophy, and tankage interaction. The package datasheet
  should pin this before vendor commits.

## Examples

> Examples are deliberately sparse here because illustrative cases from
> accessible source slices are not detailed at the equipment level beyond the
> tagged drum and pump. The DBM equipment-list rows are the closest local
> exemplars:

- LP Flare KO Drum at 4-25: V-3900-1 (one unit); transfer pump P-3900-1
  (one unit). [`4-25_Deepcut_DBM.md` lines 2581-2582]
- Companion HP service: V-4100-1 with pump P-4100-1 and truck-out (HP
  equivalent; see HP FKOD budgetary go-by `24292-02-PT-ENR-17-201_HP FKOD_R2.pdf`,
  location TBD).
- Companion cryogenic service: V-4110-1 with immersion heater. [`4-25_Deepcut_DBM.md` lines 2027, 2578]

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-055-04-01 | Equipment-list quantity column shows "2" for Flare KO Drum (Low Pressure) 2 at 4-25, but per-item rows list 1 of V-3900-1 and 1 of P-3900-1. | `4-25_Deepcut_DBM.md` line 2535 | `4-25_Deepcut_DBM.md` lines 2581-2582 | Datasheet (Identification, Attributes, Construction); Specification REQ-055-04-01..04 | Quantity column "2" counts the two distinct equipment items in the package (drum + pump), not two drums. Proposed authority: per-item rows. | TBD |
| CONF-055-04-02 | EHT freeze-protection rule in DBM is explicit for HP flare headers; LP flare freeze-protection rule is not stated. | `4-25_Deepcut_DBM.md` line 2033 | (absence) | Specification REQ-055-04-14; Guidance Principles | LP outdoor lines treated equivalently because LP carries water/condensable liquid. Mark ASSUMPTION until EPC confirms. | TBD |
| CONF-055-04-03 | Sour-service materials directive for the LP FKOD is not stated in accessible source slices, but the 04-25 facility envelope is sour. | `4-25_Deepcut_DBM.md` lines 5, 7, 2029 | (absence of specific material call-out) | Specification REQ-055-04-07; Datasheet Construction (materials) | Apply NACE MR0175 / ISO 15156 as ASSUMPTION; vendor metallurgy proposal confirms. | TBD |
| CONF-055-04-04 | Two binary reference sources cited in `_REFERENCES.md` (Workbook Packages row 57 and 26020-Package_Requirements.docx heading 10) are not accessible in text in this run. | `_REFERENCES.md` | (no text slice) | All four documents — content limited to accessible DBM and CSV slices | Treat the package register row as proxy for the workbook row; mark .docx-only content as TBD. | TBD |
