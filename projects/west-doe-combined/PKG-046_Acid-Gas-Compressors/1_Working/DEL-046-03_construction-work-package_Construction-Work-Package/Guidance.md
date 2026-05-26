# Guidance: DEL-046-03 — Construction Work Package (Acid Gas Compressors)

## Purpose

The Construction Work Package (CWP) for `PKG-046` Acid Gas Compressors is the EPC Integrator's binding plan for physically installing, hooking up, inspecting, and turning over the acid gas injection compression system at the 04-25 Deepcut facility. It exists because the acid gas compressor packages are a sour-service, safety-critical, single-string-with-spare system whose construction touches civil foundations, mechanical setting, sour-service piping, electrical feeders to a 1,300 hp VFD-driven motor, instrumentation and ESD wiring, and a tie-in to an offsite disposal well pipeline. Without a disciplined CWP, the multi-discipline interfaces and the H2S hazard make execution risk and turnover ambiguity unacceptable.

## Principles

1. **Source-anchored installation.** Construction execution shall be traceable to the design basis in `4-25_Deepcut_DBM.md` SEC-05 (compressor configuration, MAWP, cooler, recycle/blowdown arrangement) and the construction responsibility assignment in SEC-01. Field deviations require documented engineering disposition before installation, not after.
2. **Sour-service discipline.** Acid gas service (design 72.95 mol% H2S) makes weld quality, material conformance, gasket and bolt traceability, and packing-vent integrity gating items. Treat them as hold points, not paper checks.
3. **Interface clarity before steel.** Tie-in responsibility at every ISBL/OSBL boundary shall be confirmed in writing before piping is installed across that boundary (`4-25_Deepcut_DBM.md` SEC-01: "External interface responsibility marker; responsibility is to be confirmed for each tie-in").
4. **Spare-compressor symmetry.** Foundation, piping, electrical, and control work for the spare compressor shall be executed to the same standard as the two operating units; the spare is a redundancy guarantee, not a deferred scope.
5. **Construction supports operation.** Maintenance access for cylinders, valve covers, packing replacement, lube-oil change, and scrubber drains must be preserved by the construction sequence and equipment placement.

## Considerations

- **Module split and shipped-loose count are TBD.** Until the vendor packaging design (covered by `DEL-046-04`) is fixed, the workface plan is necessarily provisional. Reserve change-control margin in the schedule.
- **Geotechnical placeholder.** `3-25_Comp_and_Liquids_DBM.md` SEC-02 states foundation values are placeholders until the final geotechnical report is accepted. Foundation construction for the compressor packages should not start until that report is closed.
- **5-stage compressor + sour-service cooler bank.** The stage-by-stage MAWP and design temperature range (`4-25_Deepcut_DBM.md` SEC-05 table) requires segregated hydrotest groups by MAWP class; do not lump-test across stages.
- **Recycle and blowdown valve configuration is design-load-bearing.** Recycle valves are fail-open with no manual isolation, by design, to minimize acid-gas leak points. Construction QC must verify fail position by bench test and confirm manual-isolation absence is intentional, not an omission.
- **Pipeline interface assumption.** The 3 in. NPS acid-gas injection pipeline (TBC) and the disposal well are external responsibilities. The EPC tie-in must be cleanly demarcated, with a blind/spade arrangement that protects the disposal pipeline operator's commissioning sequence.
- **Permitting overlay.** BCER permit conditions (`4-25_Deepcut_DBM.md` SEC-01 Permitting) constrain site disturbance and discharge during construction. Permit obligations should be embedded in the workface plan, not held only by the environmental coordinator.

## Trade-offs

- **Speed of setting vs. quality of foundation grouting:** Compressor reciprocating loads punish weak grout. Prefer schedule float on grout cure over compressed cure schedules.
- **Hydrotest staging vs. throughput:** Multi-MAWP stages tempt combined hydrotests at the lowest common MAWP. Resist; this masks weak welds at higher-MAWP stages.
- **Tie-in concurrency vs. interface risk:** Concurrent tie-ins shorten the schedule but multiply interface failure modes when responsibility is unconfirmed. Tie-in timing should follow R-8 (joint planning) discipline.

## Examples

The DBM does not contain narrative construction examples for this package; examples are not drafted here. Reference to comparable EPC-executed sour-service reciprocating compressor installations may be added by the EPC Integrator using project-internal precedent. **TBD.**

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CWP-046-C1 | Compressor frame model | `4-25_Deepcut_DBM.md` SEC-05 (Ariel KBT/6) | `4-25_Deepcut_DBM.md` SEC-05 (legacy KBK/6 reference) | Datasheet Attributes; Specification R-2 | Treat KBT/6 as the working basis; flag KBK/6 references for resolution | TBD |
| CWP-046-C2 | 5th-stage discharge design pressure | `4-25_Deepcut_DBM.md` SEC-05 (1,200 psig normal) | `4-25_Deepcut_DBM.md` SEC-05 (1,500 psig design-discharge reference unresolved) | Datasheet Conditions; Specification R-9 (hydrotest); Procedure Verification | Use 1,500 psig stage-5 MAWP basis (10,694 kPag) for hydrotest until resolved | TBD |
| CWP-046-C3 | Compressor sparing arrangement | `4-25_Deepcut_DBM.md` SEC-05 (2 x 100% + 1 spare) | `4-25_Deepcut_DBM.md` SEC-05 (possible 3 x 50% alternative TBD) | Datasheet Construction; Specification scope; Procedure foundation/setting | Plan layout and foundations for the 2 x 100% + 1 spare basis; preserve change capability | TBD |
| CWP-046-C4 | Sour-service material standard (R-4) | `4-25_Deepcut_DBM.md` (does not explicitly cite NACE MR0175 / ISO 15156) | EPC convention | Specification R-4, Standards table | Adopt NACE MR0175 / ISO 15156 pending project standards register confirmation | TBD |
| CWP-046-C5 | Piping code (R-9, Standards table) | `4-25_Deepcut_DBM.md` (does not explicitly cite ASME B31.3) | EPC convention | Specification R-9, Standards table | Adopt ASME B31.3 pending project standards register confirmation | TBD |
| CWP-046-C6 | `26020-Package_Requirements.docx` content | `_REFERENCES.md` cites it as a source | Not text-extracted in `_Sources` | All four documents | Extract to markdown and incorporate before SEMANTIC_READY | TBD |
