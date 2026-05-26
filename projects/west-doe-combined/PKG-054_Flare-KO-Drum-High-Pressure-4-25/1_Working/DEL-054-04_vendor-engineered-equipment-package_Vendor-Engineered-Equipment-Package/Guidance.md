# Guidance: DEL-054-04 Vendor Engineered Equipment Package

## Purpose

This deliverable exists because PKG-054 is a vendor-supplied High-Pressure Flare KO Drum package. The EPC Integrator authors the Scope of Work (DEL-054-01) and Package Datasheet (DEL-054-02); the Package Vendor consumes those inputs and produces a complete engineered package - design, datasheets, and the physical equipment - that the EPC Integrator can review (DEL-054-06), receive turnover for (DEL-054-05), and install (DEL-054-03). [Source: `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` rows DEL-054-01 through DEL-054-06]

## Principles

- **Vendor as production unit, not standalone designer.** The vendor's engineering authority is bounded by the EPC Scope of Work and Package Datasheet; the vendor does not redefine package scope, battery limits, or facility-level basis. [Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-054-04`]
- **HP flare is the integrating system.** The KO drum's role is to protect the common HP/cryo stack; vendor design choices that affect flare header, backpressure, knockout efficiency, or stack feed are facility-level decisions and require EPC Integrator concurrence. [Source: `4-25_Deepcut_DBM.md` lines 2028, 2033]
- **Conservative on open items.** Where the DBM marks values open (relief volumes, backpressures, shared 03-25/04-25 allocation, stack opacity scenarios, air-assist basis), the vendor design carries placeholders or TBDs until detailed engineering and the flare stack vendor confirm. [Source: `4-25_Deepcut_DBM.md` lines 1834, 2021, 2186, 2294]
- **Anchor on tags, not narrative.** Anchor vendor design on V-4100-1 and P-4100-1 tags rather than on prose paraphrases of facility scope. [Source: `4-25_Deepcut_DBM.md` lines 2028, 2534]

## Considerations

- **Material consistency.** The DBM identifies SA-333 as the HP flare MOC reference; align package pressure-containing components with this reference, but confirm during detailed engineering because the cited line is for HP flare stack/header rather than the KO drum specifically. [Source: `4-25_Deepcut_DBM.md` line 2039]
- **Freeze protection.** Outside-of-heated-building HP flare piping needs electrical heat trace and insulation; PSV outlets are an explicit exception. The vendor should not extend freeze protection to PSV outlet free-drain stubs. [Source: `4-25_Deepcut_DBM.md` line 2033]
- **Spacing-driven layout.** A minimum 10 m clearance from vegetation/fire hazards applies to KO drums; ensure the vendor's layout submittal carries this dimension. [Source: `4-25_Deepcut_DBM.md` line 287]
- **Truck-out provision.** P-4100-1 supports truck-out; the vendor should size and locate the loading interface to be accessible from grade without obstructing flare stack approaches. [Source: `4-25_Deepcut_DBM.md` line 2028]
- **Combination point downstream.** HP flare combines with the cryogenic flare downstream of both KO drums before the common HP/cryo stack; vendor piping termination must permit this without rework. [Source: `4-25_Deepcut_DBM.md` line 2028]

## Trade-offs

- **Package vendor scope vs. EPC scope at the relief header tie-in.** Where the vendor's package ends and the EPC piping begins is a recurring trade-off. Use DEL-054-02 (Package Datasheet) as the controlling artifact. [Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-054-02`]
- **Conservative sizing vs. open relief volumes.** Vendor may favor conservative sizing margins while relief volumes remain TBD, but excess capacity affects pump P-4100-1 sizing and truck-out cadence. Document margin assumptions in the vendor design basis. [Source: `4-25_Deepcut_DBM.md` line 2021]
- **Vendor-standard documentation vs. EPC document register.** Vendor-standard datasheet templates may not match the EPC vendor document register format; conform to DEL-054-05 register conventions to avoid rework. [Source: `DELIVERABLE_REGISTER.csv` row `DEL-054-05`]

## Examples

The DBM equipment register lists "Flare KO Drum (High Pressure) 2" entries at 4-25 (Deepcut) with associated tags "HP FLARE K.O. DRUM TRANSFER PUMP" and "H.P. FLARE K.O. DRUM" - this is the concrete equipment scope the vendor must engineer and supply. [Source: `4-25_Deepcut_DBM.md` line 2534]

Further worked examples (sizing tables, P&ID excerpts, GA references) are TBD pending issue of DEL-054-02 Package Datasheet.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| (none identified) | No source-vs-source conflicts identified within available source slices. Conflicts may emerge once DEL-054-02 Package Datasheet and 26020-Package_Requirements.docx package heading 9 are read at clause level. | - | - | - | - | TBD |
