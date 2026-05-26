# Guidance — DEL-050-04 Vendor Engineered Equipment Package (Stabilizer Overheads Compressors)

## Purpose

This deliverable is the Package Vendor's engineered, fabricated, and supplied SOC equipment package, produced from the EPC Scope of Work (DEL-050-01) and Package Datasheet (DEL-050-02). It is the physical answer to PKG-050: two (2) Ariel KBC/6 four-stage reciprocating SOC packages that compress and recycle flashed and stabilizer-overhead vapours into the amine treating section at the 04-25 Deepcut facility. Source: `_CONTEXT.md`; SOW-0174; DBM §SEC-04 L714, L728.

## Principles

1. **Vendor / EPC split of responsibility is hard.** The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment. The EPC Integrator owns facility-level integration: interfaces, tie-ins, constructability, foundations, site installation, electrical connections, mounting structures. Source: `PACKAGE_REGISTER.csv` row PKG-050; SOW-0176.
2. **The package is one of multiple SOC inlet sources, not a stand-alone compressor.** Stage suction headers carry side streams from MPFF (Stage 3), stabilizer overheads (Stage 2), and a heterogeneous Stage 1 manifold (stabilizer flash-feed, both VRUs, amine flash gas, TEG glycol flash, pressurised caustic drain drum, possibly NGL regen sources). The package design must accommodate large variability and intermittent flow, not steady-state nominal alone. Source: DBM L744–L760.
3. **Recycle and large excess capacity are deliberate.** Design excess capacity is 151 %–206 % of expected winter flow per stage; a single full-range recycle valve sized for 100 % recycle at 40 % speed is the principal means of matching variable upstream demand without flaring. Source: DBM L730–L737, L826.
4. **Dewpoint discipline is non-negotiable.** Heavy hydrocarbon composition through Stages 2–4 means cooler outlet temperatures must remain above hydrocarbon dewpoint; Stage 2 margin is narrow and must be re-checked. Winter-stable cooler controls (warm-air recirc, plenum heater, automated louvers) are mandatory. Source: DBM L817–L824.
5. **Sour service.** Inlet H2S to Stage 1 is ~1.37 mol % with trace mercaptans, CS2, and BTEX. Materials, gasketing, sealing, and elastomer selection should be treated as sour service even where the DBM does not explicitly invoke NACE. Source: DBM L779–L805. **ASSUMPTION:** project applies sour-service material practice consistent with provincial regulator expectations.
6. **Two packages, 100 % each, but both may run together.** Sparing philosophy is operating + standby, but upset / line-pack conditions may require both packages simultaneously to avoid flaring. Vendor controls and shared-suction design should not assume single-package operation. Source: DBM L718, L728.
7. **The Vendor scope is bounded by the package skid edge.** Site civil, tie-in piping, and tie-in electrical are by others; the Vendor's interfaces are defined at the package envelope plus the unit control panel I/O to the BoP DCS. Source: SOW-0176; DBM L813.

## Considerations

- **Stage-MAWP gaps.** Only Stage 1 suction (1,723 kPag at 149 °C) and Stage 4 discharge (9,101 kPag at 177 °C) MAWPs are fixed in the basis. Intermediate-stage MAWPs are TBC and will be set by Vendor analysis. EPC review should confirm MAWP cascade is consistent with relief device sizing and inter-stage isolation philosophy.
- **Inlet liquid density 0.61 SG.** Scrubber sizing leans on this assumption; if upstream sour-water / methanol carry-over is heavier, capacity range tightens. Source: DBM L815.
- **Recycle valve fail position.** Currently TBC — fail-open is the conventional safe choice for surge / overload but conflicts with depressurisation philosophy in some unit control schemes. Surface explicitly to the human owner. Source: DBM L826.
- **Start-up philosophy.** The package shall be capable of start without prior blowdown. Equalised-start vs. normal-operating-pressure start is to be evaluated during detailed engineering and affects valve sizing and motor in-rush. Source: DBM L826.
- **Building and shipping.** Self-framing buildings + three-piece shipment is the baseline. Single-piece shipment (TBC) reduces site assembly risk but constrains transport route. Source: DBM L728.
- **Composition is TBC.** SOC composition is the governing basis but is flagged "to be reviewed during detailed engineering due to transient inlet streams." Material and corrosion-allowance selections made early should be revisited after FEED close-out. Source: DBM L777.
- **NGL regen sources.** "NGL Regen Vapour" and "NGL Regen Gas" remain listed but the current scope retired the regenerative NGL caustic basis. Vendor should not size for those sources at their legacy regenerative values. Source: DBM L760.

## Trade-offs

| Trade-off | Discussion |
|---|---|
| Excess capacity vs. cost | The 150 %+ stage excess capacity simplifies operability and absorbs upset cases, at higher capital cost. Removing it to "right-size" would re-expose the facility to flaring during line-pack and transients. |
| Two 100 % packages vs. one larger machine | Two-package philosophy supports maintenance availability and parallel operation under upset; rejects a single-train cost optimisation. |
| ET-type fail-closed suction PCVs | Fail-closed protects the SOC from over-pressure / liquid carry-over but isolates side-streams on power loss; relief and venting must absorb the resulting upstream pressure rise. Source: DBM L815. |
| Building enclosure | Self-framing building protects winter operability and personnel but adds shipping bulk and complicates single-piece shipment. Source: DBM L728. |

## Examples

- **Stage-3 MPFF transient.** MPFF design flow is 11.1 MMSCFD against an expected winter of 2.757 MMSCFD; Stage 3 is sized at 17 MMSCFD design. The recycle valve and dewpoint margin must hold during the swing. Source: DBM L756, L734–L737.
- **Both packages on during line-pack.** Upset / line-pack conditions may require both SOC packages on simultaneously rather than treating the second as cold standby; control philosophy and shared suction header design must support hot parallel operation. Source: DBM L728.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CONF-01 | Direct package-vendor source document `26020-Package_Requirements.docx` is referenced as the authoritative Word source basis but is not directly readable in the workspace (binary `.docx`). Source slices reach this deliverable only via SOW extracts. | `_REFERENCES.md` "Source Materials" entry; `PACKAGE_REGISTER.csv` Word Source Basis | `SCOPE_LEDGER.csv` rows SOW-0173/0174/0175/0176 (extract-only) | Datasheet References; Specification Standards / Documentation | PROPOSAL — convert the .docx to markdown via `tools/pdf2md/` or equivalent and re-cite clauses directly | TBD |
| CONF-02 | DELIVERABLE_REGISTER and `_CONTEXT.md` list nine objectives (OBJ-001, 003–010) against this deliverable; OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC means the mapping is package-grouped, not deliverable-specific. | `_CONTEXT.md` "Supports Objectives"; DELIVERABLE_REGISTER row DEL-050-04 | OBJECTIVE_DELIVERABLE_MAP.csv (package-row grain) | Datasheet Identification | PROPOSAL — accept package-heuristic objective set as directional context only until human confirms deliverable-level mapping | TBD |
| CONF-03 | Recycle-valve fail position is TBC; project safety-system convention is not stated in the accessible slice. | DBM L826 | (none) | Specification R-9 | PROPOSAL — adopt fail-open as default for anti-surge / overload protection pending HAZOP | TBD |
| CONF-04 | Stage 2 cooler discharge (87.78 °C) is only 2.47 °C above the Stage 2 hydrocarbon dewpoint (85.31 °C). | DBM L821 | DBM L822 | Specification R-6; Guidance Considerations | PROPOSAL — Vendor to re-rate Stage 2 cooler with additional surface area or raise outlet setpoint | TBD |
