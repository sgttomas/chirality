# Guidance — DEL-068-01 Scope of Work (PKG-068 TEG Dehydration Unit)

## Purpose

The Scope of Work (SOW) is the EPC Integrator's mandatory Gate 5 anchor deliverable for PKG-068. It establishes the binding scope statement against which the Package Datasheet (DEL-068-02), Construction Work Package (DEL-068-03), Vendor Engineered Equipment Package (DEL-068-04), Vendor Document Turnover (DEL-068-05), and EPC Vendor Package Review and Acceptance (DEL-068-06) are aligned. Without an accepted SOW, no downstream PKG-068 deliverable has a stable parent contract. (Source: `_CONTEXT.md` Notes; `DELIVERABLE_REGISTER.csv` row DEL-068-01.)

## Principles

1. **EPC Integrator owns facility-level integration; Package Vendor owns the package.** The split is binding and originates from `PACKAGE_REGISTER.csv` row PKG-068. The SOW must never collapse the two roles or assign facility-level integration to the vendor.
2. **Source authority precedes decomposition prose.** Where DBM SEC-06 (l.1187–1237) states a process basis, that text governs; the workbook scope statement summarizes but does not override. Where sources are silent (e.g., package-level exclusions), the SOW must mark `TBD` rather than invent.
3. **Process values stay in the Datasheet.** This SOW intentionally avoids carrying detailed design values; values are cited for scope framing only. The authoritative process design envelope lives in DEL-068-02 (Package Datasheet).
4. **Interfaces are enumerated here, sized in the Datasheet.** PKG-068's applicable interface types are fixed by PACKAGE_REGISTER row 97; per-interface design conditions belong in DEL-068-02.

## Considerations

- **Operating pressure basis is unresolved.** DBM SEC-06 l.1207 states both 1100 psig / 7584 kPag (TBC) and 1085 psig / 7481 kPag as candidate operating-pressure bases; the SOW must flag this and direct closure during detailed engineering before the Package Datasheet locks the value. (See Conflict Table below.)
- **TEG contactor sparing configuration is open.** DBM SEC-06 l.1222 and l.1237 leave 1 x 100% versus 2 x 50% open. The SOW should record contactor sparing as `TBD` and route resolution to vendor + EPC during DEL-068-02 development.
- **Warm-side stream identity for the inlet/TEG cross exchanger is unresolved upstream of PKG-068.** DBM SEC-04 l.606 and l.836 flag the warm-side identity (dehydrated TEG contactor outlet vs. warm sweet gas from amine) as an open item. PKG-068 inherits this open interface; the SOW must note that the cross exchanger interface is conditional on upstream closure.
- **Package-level exclusions absent from source.** `PACKAGE_REGISTER.csv` row PKG-068 records exclusions as "TBD; no package-specific exclusions stated in source materials." The SOW exclusions section must be left explicitly `TBD` rather than back-filled.

## Trade-offs

- **Detail in the SOW vs. detail in the Datasheet.** Carrying process values in the SOW risks divergence with the Datasheet. The chosen trade-off is to keep the SOW lean on values, citing DBM only for scope framing, and to push parameter ownership to DEL-068-02.
- **Single-vendor packaged scope vs. EPC-led component buy.** The DBM and PACKAGE_REGISTER both assume a single Package Vendor for the engineered package. Splitting equipment across multiple buys is technically possible but would invalidate the "package" responsibility split assumed here; that path is not supported by the current source basis (ASSUMPTION).
- **Interface design discipline.** Enumerating 13 interface types in scope ensures none are missed but adds coordination overhead. The SOW retains the full list (per PACKAGE_REGISTER row 97) and lets the Datasheet prune any that prove non-applicable with evidence.

## Examples

- **Function statement example (source-anchored).** "The TEG Dehydration Unit removes water from sweet natural gas downstream of amine treating and upstream of molecular-sieve dehydration, delivering gas at <=4 lb H2O/MMSCF (DBM SEC-06 l.1210), with regenerated TEG circulated at design 45 USGPM and 99.80 wt% regenerated purity (DBM SEC-06 l.1225)."
- **Responsibility example (binding).** "Package Vendor: TEG contactor structured packing selection, demister sizing, and outlet blowdown valve to HP flare (DBM SEC-06 l.1222). EPC Integrator: HP flare tie-in piping, blowdown header sizing, and flare loading aggregation."

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFL-068-01-01 | TEG operating pressure basis: 1100 psig / 7584 kPag vs. 1085 psig / 7481 kPag | DBM-Deepcut/4-25_Deepcut_DBM.md SEC-06 l.1207 (1100 psig basis, TBC) | DBM-Deepcut/4-25_Deepcut_DBM.md SEC-06 l.1207 (1085 psig unresolved unit-level basis) | Datasheet `Conditions`; Specification `R-068-01-07` integration narrative; downstream Package Datasheet (DEL-068-02) | Carry 1100 psig as the SOW framing value with explicit "TBC" marker; defer binding selection to DEL-068-02 detailed engineering | TBD |
| CFL-068-01-02 | TEG contactor sparing configuration: 1 x 100% unit-level vs. 2 x 50% contactor-vessel basis | DBM-Deepcut/4-25_Deepcut_DBM.md SEC-06 l.1222 ("Final contactor sparing/configuration is TBD") | DBM-Deepcut/4-25_Deepcut_DBM.md SEC-06 l.1237 ("must remain open until the 1 x 100% unit-level versus 2 x 50% contactor-vessel basis is resolved") | Datasheet equipment list (TEG Contactor row); Specification `R-068-01-02` | Leave sparing TBD in SOW; route resolution to DEL-068-02 with vendor input | TBD |
| CFL-068-01-03 | Inlet/TEG dehy cross exchanger warm-side stream identity (dehydrated TEG contactor outlet vs. warm sweet gas from amine) | DBM-Deepcut/4-25_Deepcut_DBM.md SEC-04 l.606 | DBM-Deepcut/4-25_Deepcut_DBM.md SEC-04 l.836 | Specification `R-068-01-07` integration narrative; Gas/Glycol Exchanger row of Datasheet | Acknowledge open upstream interface in SOW; do not resolve here | TBD |
| CFL-068-01-04 | Package exclusions: PACKAGE_REGISTER row PKG-068 records `exclusions = TBD; no package-specific exclusions stated in source materials` | `PACKAGE_REGISTER.csv` row PKG-068 `exclusions` column | RFQ source `26020-01-PT-RFQ-22-001_TEG Dehy Unit.docx` (not locally accessible) | Specification `R-068-01-11` | Leave exclusions TBD pending RFQ source slice review | TBD |

## TBD / Missing References Register

- `26020-Package_Requirements.docx` package heading 23 — local file present (`_Sources/26020-Package_Requirements.docx`) but binary; specific package heading 23 text slice is not directly readable in this run. (location TBD)
- `Bid Docs/Budgetary/26020-01-PT-RFQ-22-001_TEG Dehy Unit.docx` — not present under `_Sources/`. (location TBD)

Content that depends solely on these sources (governing standards list, finalized exclusions, RFQ-specific commercial terms) is marked `TBD` rather than inferred.
