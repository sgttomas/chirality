# Guidance — DEL-049-03 Construction Work Package (Sales Gas Booster Compressor)

> Directional guidance for executing the Construction Work Package (CWP) for `PKG-049 Sales Gas Booster Compressor`. Source-anchored to `_Sources/26020-Package_Requirements.docx` heading 4 (`26020-01-PT-12-004`). Inferences are marked `ASSUMPTION`; unresolved items are `TBD`.

## Purpose

The CWP exists because the Sales Gas Booster Compressor is a vendor-supplied skidded package whose installation, tie-in piping, electrical connections, mounting platform, and stairs are explicitly delegated to the EPC Integrator ("By others" in the source SGBC Scope Notes). Without a deliberate CWP, no party owns the workface plan that converts a delivered skid into an installed, tested, and turned-over piece of facility equipment. The CWP is the EPC Integrator's instrument for owning that gap.

## Principles

1. **Source-grounded scope demarcation.** Treat the SGBC "By others" list in the source as authoritative for the EPC Integrator's construction scope boundary: shipping to site, installation on piles, tie-in piping, electrical connections, mounting platform, and stairs.
2. **Vendor artifacts are construction inputs, not substitutes for the CWP.** The vendor's `MEC-017` installation/setting drawings, `STR-013` anchor bolt drawings, `MEC-018` lifting study, and `STR-014` transport analysis define geometry and load paths; the CWP supplies the workface plan, schedule, resource loading, sequencing, and acceptance evidence.
3. **One package, many disciplines.** The SGBC interface applicability table shows ten "Yes" interfaces. The CWP must integrate piping, electrical, instrumentation, fire & gas, and structural disciplines under a single workface plan rather than running parallel discipline plans that converge late.
4. **Build for turnover.** Every construction activity should generate the records required by `R-CWP-12`–`R-CWP-17`. Records collected at the activity are cheap; records reconstructed at turnover are not.
5. **Maintain interface evidence.** The package row in `26020-Packages_Interfaces.3.xlsx` (row 80) is the canonical interface-level evidence for this package; the CWP should not silently re-baseline these interfaces.

## Considerations

- **Tie-in piping is the largest field-of-fire.** Process, utility, relief/vent, and drain are all "Yes" in the SGBC interface summary, and the source confirms tie-in piping is "By others". Expect tie-in piping to be the dominant driver of schedule risk and weld-volume; sequence hot-work, line-clearance, and hydrotest packs accordingly.
- **Suction/discharge design pressures are high.** Discharge design is 12,866 kPag (1,866 psig) and suction design is 6,137 kPag (890 psig) per the SGBC Scope Notes. Hydrotest pack boundaries, blind locations, and pressure-test medium decisions are non-trivial; project pressure-test specification is `TBD` and must be obtained before fixing test pressures.
- **Motor is large and 4000 V.** The 1,000 kW (1,340 HP) 4000 V motor implies switchgear coordination, motor starting study (`ELE-011`), high-voltage cable termination, and energization sequencing that benefits from early engagement of the electrical commissioning lead.
- **API 661 air coolers require careful setting.** Forced-air intercoolers per stage need clear airflow, plenum integrity, and louver control wiring — protect them during adjacent construction (welding, grinding, scaffold).
- **Filter coalescer protects downstream sales gas equipment.** Cleanliness during piping flush/dry is therefore not optional; the CWP should require flush certification upstream of the coalescer reload.
- **Inspection Release Certificate (`QLT-020`) gates receipt.** Use it as the receiving inspection trigger before any setting work begins, and reflect that in the workface plan sequence.
- **Pressure Equipment Registration (`REG-022`) is a parallel critical path.** Many jurisdictions require registration evidence before pressurization; do not let it become a turnover surprise.

## Trade-offs

- **Pre-set vs. tie-in last.** Setting the package early gives downstream piping crews a fixed reference but exposes the skid to extended weather and adjacent-trade damage. Late setting protects the skid but compresses tie-in piping into a shorter window. The CWP should make this trade-off explicitly, not by default.
- **Stick-build vs. spool-yard for tie-in piping.** Spool-yard fabrication compresses field welding but requires accurate as-found dimensions of the installed skid. A laser-scan of the set package before final spool release reduces field re-work; the time cost is small relative to weld re-work cost.
- **Loop check before or after motor solo run.** Doing loops first protects the motor from spurious trips during solo run; doing solo run first proves the motor circuit before extensive loop work. The default ASSUMPTION is: loops first, then motor solo, then string test — record the project-specific choice in the workface plan.
- **Single MC at package level vs. multi-stage MC by sub-system.** Single MC is simpler administratively but delays sub-system handovers. Multi-stage MC enables commissioning to start on electrical/piping early but increases punch-list and re-walk overhead. The CWP should pick one explicitly and align the turnover checklist accordingly.

## Examples

- "By others" list applied to scope demarcation: The SGBC source SGBC Scope Notes / Open Items entry — "By others: Shipping compressor package to site, installation on piles, tie-in piping, electrical connections. Mounting platform and stairs" — translates one-for-one into EPC Integrator workface plan headings (Shipping & Receiving; Piling & Setting; Tie-In Piping; Electrical Connections; Platform & Stairs). This keeps the CWP traceable to the source language rather than to a generic CWP template.
- Construction interface applicability example: Because the SGBC Physical Interface Summary marks Cathodic Protection = "No", the CWP should NOT include a cathodic protection scope item; if a site condition emerges that requires CP, that is a scope change rather than a CWP gap.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority | Human ruling |
|---|---|---|---|---|---|---|
| C-1 | RFQ document name `26020-01-PT-RFQ-12-004-Sales Booster Comp.docx` is cited as source basis in `26020-Package_Requirements.docx` but is not present under `_Sources/`. | `_Sources/26020-Package_Requirements.docx` SGBC Source Basis | Local `_Sources/` directory listing | Datasheet References; any spec requirement that would otherwise derive from RFQ | PROPOSAL: treat RFQ as cited-but-inaccessible; do not derive requirements from it | TBD |
| C-2 | Source SGBC Scope Notes lists "Mounting platform and stairs" as "By others"; the SGBC Vendor Engineering Deliverables list includes `STR-011 Platform / Access Structure Drawings`. Whether the vendor supplies drawings only (with EPC fabricating/installing) or supplies the platform itself is ambiguous in the accessible source. | `_Sources/26020-Package_Requirements.docx` SGBC Scope Notes | `_Sources/26020-Package_Requirements.docx` SGBC Vendor Engineering Deliverables list | R-CWP-11; Procedure step on platform/stair installation | PROPOSAL: ASSUMPTION — vendor supplies design (`STR-011`); EPC fabricates and installs | TBD |
| C-3 | Interface row 80 reference points to `26020-Packages_Interfaces.3.xlsx`, but the file present under `_Sources/` is `26020-Packages_Interfaces_4_export.xlsx`. Version mismatch is unresolved at the document level. | `_Sources/26020-Package_Requirements.docx` SGBC Physical Interface Summary | `_Sources/26020-Packages_Interfaces_4_export.xlsx` (only file present) | Datasheet Construction Interface Applicability | PROPOSAL: use the `_4_export` file as the working interface evidence; treat row 80 mapping as ASSUMPTION pending row-level verification | TBD |
