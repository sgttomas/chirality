# Guidance — DEL-068-04 Vendor Engineered Equipment Package (TEG Dehydration Unit)

## Purpose

This deliverable is the **Package Vendor production unit** for PKG-068 TEG Dehydration Unit. It exists because the EPC Integrator delivers a Scope of Work (DEL-068-01) and Package Datasheet (DEL-068-02) that hand off design responsibility to a third-party package vendor for engineering, fabrication, and supply of the physical TEG dehydration package. The unit is anchored by the EPC handoff and reviewed back through EPC Vendor Package Review and Acceptance (DEL-068-06).

(Source: `_Decomposition/.../DELIVERABLE_REGISTER.csv` row DEL-068-04; `_CONTEXT.md`.)

## Principles

1. **EPC anchor, vendor execution.** The EPC Scope of Work and Package Datasheet are the contractual envelope. The vendor's engineering must trace requirements back to those EPC documents, not invent new scope.
2. **Source-anchored design basis.** The TEG package process basis is fixed by the governed DBM (SEC-05 of `3-25_Comp_and_Liquids_DBM.md`) plus accepted SCA-002 supersession state. Vendor proposals that deviate from the cited basis must be raised as deviations, not silently re-baselined.
3. **One-by-100 percent reliability posture.** The package is intentionally single-train; equipment selection, monitoring, and turnaround planning must reflect that there is no parallel dehydration redundancy. (SEC-05 / TEG Dehydration Basis.)
4. **Sour-service discipline.** Compressor composition basis includes approximately 0.296 mol% H2S; materials, weld procedures, and inspection plans must satisfy applicable sour-service practice. (SEC-05 / Compression Design Conditions.)
5. **Interface-first design.** The package has well-defined upstream (compressor discharge at 800 psig under SCA-002) and downstream (export to 04-25, flash gas to 04-25 SOC first-stage suction) interfaces. Pressure, temperature, and routing assumptions must be confirmed against the latest accepted SCA basis.
6. **Utility coherence.** TEG stripping is an explicit LP fuel-gas user, and TEG regeneration relief routes via LP KO drum V-3900-2 to the LP flare. Vendor utility loads must be reconciled against the facility utility basis, not stated as standalone assumptions.

## Considerations

- **Performance guarantee scope.** The 4 lb H2O/MMSCF outlet specification is a hard process target; the contactor design (structured packing, three theoretical stages minimum, Fs not more than 3.0, demisters) is the published path to it. Performance guarantee conditions, witnessed-test protocol, and turndown demonstration approach are not specified in source and should be agreed during vendor engagement.
- **Maximum flow rating.** Source records normal/design at 82.5 MMSCFD with maximum TBC. The vendor's proposed maximum should be defended with a clear basis (mechanical, hydraulic, regeneration thermal duty).
- **Filtration strategy.** The full-flow 5 micron filter plus 20 percent carbon slipstream architecture is the source basis. Substitution (e.g., 100 percent full-flow carbon) is a deviation, not a vendor preference.
- **Makeup tank design.** Atmospheric, fuel-gas blanketed, heated/insulated, and explicitly NOT connected to the VRU. This is a deliberate utility/safety choice that may differ from a vendor's default standard.
- **Flash gas routing.** Flash gas is pressure-regulated to the 04-25 SOC first-stage suction. Backpressure variability at that interface affects flash drum operation and must be reviewed.
- **Methanol disposition.** Source states methanol disposition downstream of the inlet separator boot is TBD. If vendor design touches methanol handling, raise it as an open item.
- **Pumps.** TEG pumps are two-by-100 percent rotary gear or positive-displacement with single mechanical seals. Vendor seal selection should consider rich-TEG service and any solids carryover risk.

## Trade-offs

| Trade-off | Position (source-grounded) | Source / Note |
|---|---|---|
| One TEG train vs parallel trains | One-by-100 percent | SEC-05 |
| Structured packing vs trays in contactor | Structured packed, at least three theoretical stages, Fs not more than 3.0 | SEC-05 |
| Full-flow carbon vs slipstream carbon | 20 percent slipstream carbon plus full-flow 5 micron solids | SEC-05 |
| Flash gas to flare vs flash gas to suction | Pressure-regulated to 04-25 SOC first-stage suction | SEC-05 |
| TEG makeup tank on VRU vs blanketed atmospheric | Atmospheric, fuel-gas blanketed, NOT connected to VRU | SEC-05 |
| Pump type | Rotary gear OR positive-displacement, 2 x 100 percent | SEC-05 |

## Examples

Source provides a complete equipment list (inlet filter coalescer, contactor, level pot, cooler, flash drum, solids filters, charcoal filter, lean/rich exchanger, rich TEG solids filter, TEG pumps, still column, stripping column, reflux condenser, reboiler, surge drum, regen cooler, regen overhead scrubber, regen overhead pumps, makeup tank, makeup pump) that should be treated as the minimum equipment manifest for vendor proposals. Vendor add-ons (e.g., additional buffer tanks, redundant filtration vessels) are acceptable but must be flagged as add-ons rather than silently included as base scope.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-068-04-01 | Inlet pressure table lists "Inlet pressure low = 4,502 kPag" and "Inlet pressure design = 4,502 kPag" identically, while "normal = 5,378 kPag" sits above both. The low/design coincidence is unusual and may indicate a source typo. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-05 / TEG Dehydration Basis table | (same — internal table) | Datasheet Attributes; Spec R-068-04-03 | Carry source values verbatim as FACT and flag to EPC Integrator for review against 26020-Package_Requirements.docx package heading 23 | TBD |
| C-068-04-02 | Source specifies "no more than 4 lb H2O/MMSCF" outlet water but does not state contractual measurement reference conditions or sampling location. | SEC-05 / TEG Dehydration Basis table | — | Spec R-068-04-02; Procedure verification | Adopt vendor-standard measurement protocol referenced to package outlet downstream of outlet demister; require EPC concurrence | TBD |
| C-068-04-03 | Maximum gas flow listed TBC in source; vendor performance envelope cannot be fixed without it. | SEC-05 / TEG Dehydration Basis table | — | Spec R-068-04-18; Datasheet | Vendor proposes max flow with basis; EPC accepts as part of DEL-068-06 | TBD |
| C-068-04-04 | Governing standards are not enumerated in available source slices; listed in Specification as ASSUMPTION. | (absent in source) | — | Specification / Standards | Vendor confirms applicable standards (ASME VIII, NACE MR0175, GPSA, B31.3, etc.) in design basis submittal | TBD |
| C-068-04-05 | SOW item text (SOW-0237..SOW-0240) is referenced in `_CONTEXT.md` but not extracted into the deliverable folder; cannot directly verify vendor scope alignment from local sources alone. | `_CONTEXT.md` Covers Scope Items | `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 97 (binary) | Specification scope; Procedure prerequisites | Extract SOW row text into deliverable references; resolve alignment in DEL-068-01 and DEL-068-02 | TBD |
