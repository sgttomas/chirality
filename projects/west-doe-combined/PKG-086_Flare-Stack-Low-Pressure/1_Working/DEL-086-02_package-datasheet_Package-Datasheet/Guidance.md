# Guidance — DEL-086-02 Package Datasheet (Flare Stack (Low Pressure))

## Purpose

This deliverable exists to give the Package Vendor a single, source-grounded technical basis for engineering, designing, fabricating, and supplying the Low-Pressure flare stack and associated LP flare stack blower for `PKG-086`. The Datasheet is the principal EPC-to-Vendor handoff artifact: it is the means by which the EPC Integrator translates facility-level relief, emissions, structural, electrical, and safety requirements into a discrete vendor scope. (Source: `_CONTEXT.md`; PACKAGE_REGISTER.csv row 59.)

It is paired with `DEL-086-01` (Scope of Work) on the EPC-author side and feeds `DEL-086-04` (Vendor Engineered Equipment Package) on the vendor-execute side.

## Principles

1. **Source-grounded, not convention-grounded.** Every non-trivial value, dimension, or requirement carries a source citation, or is explicitly marked `TBD` / `ASSUMPTION`. The LP stack OD is a deliberate `TBD` in the DBM itself and MUST stay `TBD` here until a downstream source resolves it. (DBM §"Flare and Blowdown" line 499.)
2. **Interface facts live here.** Per the deliverable note in DELIVERABLE_REGISTER.csv: "interface facts are intentionally carried here as evidence rather than standalone deliverables." The Datasheet is therefore the canonical evidence record for the LP flare stack's interfaces with utility piping, relief/flare/vent, drains, electrical power, grounding, I&C, fire & gas, and structural systems. (Source: PACKAGE_REGISTER.csv row 59 interface list.)
3. **Shared-facility transparency.** The LP flare stack is part of a dual flare stack arrangement shared between 03-25 and 04-25. Where the service split or owner interface is unresolved in source, the Datasheet must surface that openly rather than implying a settled state. (DBM §3.1 line 56.)
4. **Conservative inference.** Where a budgetary go-by document is named (e.g., self-supported dual flare stack PDF), it is treated as a directional hint only and labeled `ASSUMPTION` until a binding source is available. (PACKAGE_REGISTER.csv row 59 Source Basis.)

## Considerations

- **Stack height, OD, and tip selection** are coupled to LP relief load, smokeless turndown, radiation criteria, dispersion, and adjacent occupied/operable areas. None of these inputs are fully resolved in the accessible source set; final values depend on the flare study and Plant Shutdown and Blowdown Philosophy `W242510-PRC-REP-000003-001`. (DBM §"Flare and Blowdown" line 501.)
- **Service composition.** The LP flare receives TEG regeneration, VRU, and compressor seal-pot services. The presence of TEG and seal-pot streams informs material selection, tip/seal design, and liquid carryover protection at the upstream LP KO drum `V-3900-2` (out of scope here but immediately upstream). (DBM §"Flare and Blowdown" line 499.)
- **Sour-service applicability** is unresolved in source. The facility-wide isolation philosophy language suggests sour-service treatment may be required on the wetted relief envelope; this should be confirmed by process simulation / HAZOP rather than assumed in either direction in the Datasheet's binding values. (DBM §isolation philosophy line 607.)
- **Foundations and anchorage** for a tall flare stack require equipment-specific design against final geotechnical and site civil criteria (wind, snow, seismic, frost). The DBM names this category at the facility level but does not give the LP-stack-specific values. (DBM §"Foundations" line 700.)
- **Emissions and permit values** for combustion efficiency, smokeless design point, and permit-relevant inputs remain TBD per the DBM emissions note; the Datasheet should leave these as `TBD` rather than introduce placeholder values. (DBM §"Emissions Basis" line 555.)
- **Cross-facility shared scope** between 03-25 and 04-25 must be reflected in the interface matrix; open owner interfaces should be carried as items requiring resolution rather than silently allocated. (DBM §3.1 line 56.)

## Trade-offs

- **Speed of vendor handoff vs. source-truth completeness.** Pushing the Datasheet forward with conjectured numeric values would accelerate vendor engagement but would corrupt the source-grounded record and create later rework. The skill mandate ("TBD over guessing") is upheld here. (`skills/four-documents/SKILL.md` Step 5.)
- **Single-source-citation vs. multi-source corroboration.** The accessible source set is narrow (one DBM file plus the GATE-07 registers). Multi-source corroboration is not currently possible; the Datasheet therefore relies primarily on the DBM, and conflicts (if any) will surface when the package requirements Word document and interfaces export are parsed in a later pass.
- **Self-supported vs. guyed vs. derrick stack.** The budgetary go-by pointer suggests self-supported; committing to a stack support type in the Datasheet before the vendor performs structural analysis is a tradeoff between procurement clarity and engineering rigor. ASSUMPTION recorded; binding value: TBD.

## Examples

- The HP/Cryo companion stack in the DBM is cited as 660 mm OD x 60,957 mm tall (sonic). This provides an order-of-magnitude reference only for the LP stack; LP stack OD and height MUST NOT be inferred from the HP/Cryo values. (DBM §"Flare and Blowdown" line 499.)
- The interface type list ("Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; Grounding / Bonding; I&C / Control Cabling; Fire & Gas / Safety Systems; Structural / Foundations / Supports") is taken verbatim from PACKAGE_REGISTER.csv row 59 and is the authoritative shape of the Datasheet's interface matrix.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| (none currently) | No conflicts surfaced between accessible source slices and decomposition narrative in this initialization pass. | — | — | — | — | TBD |
