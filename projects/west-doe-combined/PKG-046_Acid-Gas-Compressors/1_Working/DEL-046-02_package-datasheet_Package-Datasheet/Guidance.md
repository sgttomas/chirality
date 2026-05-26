# Guidance — PKG-046 Acid Gas Compressors (Package Datasheet)

> Rationale, principles, considerations, and trade-offs supporting the requirements in `Specification.md`. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-05.

## Purpose

This deliverable is the mandatory Gate-5 EPC anchor "Package Datasheet" for PKG-046 Acid Gas Compressors. Its purpose is to consolidate package-level design basis, requirements, and interface evidence into a single technical handoff sufficient for third-party vendor or discipline package engineering. Per `_CONTEXT.md`, interface facts are intentionally carried here as evidence rather than standalone deliverables.

Supports objectives OBJ-001 and OBJ-003 through OBJ-010 (ASSUMPTION via PACKAGE_HEURISTIC; see Notes).

## Principles

1. **Source primacy.** Design data and requirements derive from DBM-Deepcut SEC-05 source slices. Where the source is silent or location is unknown, the package datasheet records `TBD` rather than synthesizing a value.
2. **Leakage-point minimization for acid-gas service.** The DBM intentionally excludes adjustable volume pockets and manual recycle isolation valves to reduce acid-gas leakage paths. Vendor proposals shall preserve this principle.
3. **Sequencing automation.** All routine operating sequences (isolation, purging, pressurization, depressurization, lubrication, start-up, loading, unloading, cooldown, shutdown) are automated to limit operator exposure to H2S service.
4. **Recycle-first capacity control.** Capacity control uses VFD speed and recycle, supporting both startup with cascading recycle and water-knockout via recycle cooling.
5. **Disposal interface fidelity.** The disposal well pressure characteristics are Tourmaline-provided; the compressor lifetime envelope cannot be finalized until those data are confirmed.

## Considerations

- **Configuration choice (2x100% + spare vs 3x50%).** The current basis is 2x100% plus a spare; a 3x50% alternative is unresolved. The 3x50% case would change capacity, redundancy, and likely cylinder/driver sizing; if revisited, R-46-01, R-46-03, and R-46-04 require revision.
- **Composition envelope.** The High-CO2 case (CO2/H2S swapped) is a conservative envelope for thermodynamic and metallurgical analyses. Vendor performance and material selection shall be checked against design, start-up, and High-CO2 cases.
- **Minimum methane content.** A floor of 0.5 mol% C1 in the design case (vs ~1.4 mol% C1 in turndown/start-up) affects compressibility and lube selection; vendor compression calcs shall use the floor.
- **Mercaptan condensation.** At low temperatures, mercaptan condensation can require three-phase separation and materially affect dehydration, recycle rate, and efficiency. This is a known sensitivity area to be evaluated during detailed engineering (R-46-19).
- **Dehydration option.** Recycle-based dehydration to 35-60 lb H2O/MMSCF is conditional on the disposal system's water tolerance; not a base requirement.
- **Aftercooler freeze protection.** Winter operation requires warm-air recirculation and heat-medium heating on the air coolers; loss of either function imperils stable discharge temperature and downstream injection-pipeline hydrate margin.
- **Injection pipeline NPS assumption (3 in. NPS per Tourmaline).** Compressor hydraulics and 5th-stage discharge pressure are sensitive to final pipeline sizing.

## Trade-offs

| Trade-off | Decision in DBM-Deepcut SEC-05 | Implication |
|---|---|---|
| Volume pockets vs leakage points | Excluded | Slightly less efficient capacity control; significantly fewer leak paths for sour service. |
| Manual recycle isolation vs leakage points | Excluded | Reduced isolation flexibility for maintenance; reduced acid-gas leakage points. |
| 2x100% + spare vs 3x50% | 2x100% + spare (current) | Higher single-unit redundancy; larger individual units; 3x50% remains TBD. |
| LP vs HP disposal metering | HP Coriolis downstream of compression | Lower water content, lower pressure drop, better accuracy than LP metering. |
| Adjustable bypass on blowdown | Not anticipated | Simpler package; start-up reliance on equalization + cascading recycle. |

## Examples

### Worked example — startup sequence concept (illustrative, source-supported)
Per DBM-Deepcut SEC-05, start-up is from equalization pressure with the VFD at 3:1 turndown plus cascading recycle. The HP and LP recycle valves provide a continuous gas circuit at minimum driver speed, max suction pressure, and minimum injection pipeline pressure, allowing the package to spin up without an additional automated bypass.

### Worked example — winter freeze-protection (illustrative)
Per DBM-Deepcut SEC-05, each aftercooler bundle uses actuated louver control, automatic warm-air recirculation on low discharge temperature, and heat-medium heating. The 5th-stage cooler outlet of 150 deg F (65.56 deg C) is materially warmer than stages 1-4 (110 deg F) to support the 8.3 deg C above max ambient injection-pipeline temperature setpoint.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short) | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| C-46-01 | Compressor frame: Ariel KBT/6 vs KBK/6 | DBM-Deepcut SEC-05 "Acid Gas Compressor Design Conditions" (KBT/6 stated) | DBM-Deepcut SEC-05 (note: "conflicting KBK/6 reference remains TBD") | Datasheet Identification; R-46-02 | Adopt Ariel KBT/6 as primary; flag KBK/6 for vendor confirmation | TBD |
| C-46-02 | 5th-stage discharge pressure: 1,200 psig normal vs 1,500 psig "design-discharge reference" | DBM-Deepcut SEC-05 "Acid Gas Compressor Design Conditions" (1,200 psig stated as normal/expander/J-T) | DBM-Deepcut SEC-05 (same row notes 1,500 psig reference unresolved) | Datasheet Attributes (Pressures); R-46-05; verification | Use 1,200 psig as normal operating; carry 1,500 psig as MAWP-checking reference pending ruling | TBD |
| C-46-03 | Discharge MAWP (197 psig) lower than suction MAWP (205 psig) for stages 1-2 | DBM-Deepcut SEC-05 MAWP table | Same table (internal inconsistency) | Datasheet Attributes (MAWP); R-46-05 | Verify with source author; pending ruling, quote as-stated and flag in vendor RFQ | TBD |
| C-46-04 | Configuration: 2x100% + spare vs possible 3x50% | DBM-Deepcut SEC-05 "Acid Gas Compressor Design Conditions" | DBM-Deepcut SEC-05 (same row, "possible three x 50% alternative TBD") | R-46-01 | Adopt 2x100% + spare; do not pursue 3x50% without human approval | TBD |
| C-46-05 | Acid gas dehydration: required or conditional | DBM-Deepcut SEC-05 "Acid Gas Composition Basis" ("to be considered if required by the disposal system") | Disposal-well pressure/specification not yet provided by Tourmaline | R-46-18 | Hold dehydration as optional; revisit after Tourmaline disposal-well data | TBD |
| C-46-06 | Disposal well pressure (MAWP, min, max) all TBC | DBM-Deepcut SEC-05 "Acid Gas Disposal Well Interface" disposal well table | None — values absent | Datasheet Conditions; R-46-05; vendor compressor lifetime sizing | Carry as `TBD (Tourmaline)`; gate vendor RFQ acceptance on resolution | TBD |
| C-46-07 | Modification scope at existing 02-25 facility | DBM-Deepcut SEC-01 "Adjacent Plant Interfaces" (TBD on trigger/extent) | DBM-Deepcut SEC-05 "Acid Gas Disposal Well Interface" | Datasheet Interfaces; out-of-scope list | Carry out-of-scope unless explicitly modified | TBD |
| C-46-08 | 26020-Package_Requirements.docx clauses not text-accessible | `_REFERENCES.md` lists the source | Source is .docx (binary) and not text-extracted in this pass | Specification Standards; all R-46 clauses needing 26020 alignment | Extract 26020 text and re-verify; flag any cross-reference as `location TBD` until then | TBD |

## Sources cited (Guidance evidence)

- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-05 "Compression and Acid Gas Handling Basis":
  - "Acid Gas Injection Compression Basis" (composition, MAWP, scrubbers, recycle, blowdown, sequencing).
  - "Acid Gas Disposal Well Interface" (water content cascade, disposal well pressure TBC, injection-pipeline temperature setpoint).
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-01 (project context for shared 02-25 disposal well and adjacent-plant interface treatment).

## Notes / open items

- ASSUMPTION (PACKAGE_HEURISTIC): Objective support listed in `_CONTEXT.md` (OBJ-001, OBJ-003 through OBJ-010) is treated as directionally relevant context per `OBJECTIVE_DELIVERABLE_MAP.csv` package-grouped mapping. Not a hard requirement pending human confirmation.
- ASSUMPTION: Standards list in `Specification.md` includes generally applicable codes (API 618 / 619, ASME VIII, CSA, provincial regs) not enumerated in the accessible source slices; these require human confirmation before vendor RFQ.
- TBD: `INTERFACE_REGISTER.csv` rows for PKG-046 are not yet sliced into this deliverable; cross-reference to specific interface IDs is location TBD.
