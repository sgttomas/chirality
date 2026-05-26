# Guidance — DEL-089-02 Package Datasheet

> Directional guidance for the EPC Integrator and Package Vendor when producing and consuming this datasheet. Includes the Conflict Table (CFT) of items requiring human ruling.

## Purpose

`FACT` (`_CONTEXT.md`; SOW-0157) The Package Datasheet is the EPC Integrator's mandatory technical handoff that the Package Vendor uses as the binding basis for vendor engineering, design, and equipment supply of the Pig Receivers (Inlet) 3-25. It also frames the construction work package (`DEL-089-03`) and the vendor package review and acceptance (`DEL-089-06`). Interface facts that elsewhere would live as standalone deliverables are intentionally carried here as evidence (per `_CONTEXT.md` Notes).

## Principles

1. **Source over convention.** Use SOW-0157..0160 and the DBM §Inlet Pipeline Interface and Pigging section as the binding basis. Do not generate equipment counts, sizes, or pressure ratings from convention when source data exists.
2. **Plant inlet boundary discipline.** The first aboveground flange within the lease boundary is the scope-transfer flange (DBM). The Package Vendor's responsibility starts at the receiver inlet flange and ends at the receiver outlet flange; everything else is "By Others" (SOW-0160).
3. **Sour-service conservatism.** With unresolved H2S basis (CFT-02), the more restrictive value (DBM design 0.3 mol% with license value 2.0 mol%) shall govern material selection until a human ruling is recorded.
4. **Interface evidence in one place.** All ten Mechanical-package interfaces (workbook row 77) are present in this datasheet so the Package Vendor has a single integration view.
5. **Slug and pigging operability.** The operator manages pigging rate and flowback to avoid exceeding downstream stabilization capacity (DBM §Inlet Separation); the receiver scope must support that operability without imposing additional process restrictions.

## Considerations

- **Receiver count ambiguity (CFT-01).** The package source (SOW-0158/0159) specifies two receivers tagged `PR-1010-2` and `PR-1020-2`, while DBM §Inlet Pipeline Interface and Pigging describes "A single combined three-phase pig receiver." Until human ruling, treat the package-source as authoritative and design for two receivers; a single-receiver ruling would significantly change skid layout, foundation loads (IFC-7BEBBC1154), and interfacing piping (IFC-1AA715D034).
- **Sour H2S basis (CFT-02).** Materials selection (NACE MR0175 partial-pressure thresholds) is sensitive to this ruling. The economic gap between 0.1 mol% and 2.0 mol% is significant. Vendor should flag this in the equipment datasheet.
- **Frac flowback and pigging slugs.** Slugs are processed downstream over ~6 hours by 04-25 stabilization (DBM §Inlet Separation). The pig-receiver liquid drain and barrel volume must accommodate operational pigging without overwhelming this downstream capacity.
- **Winterization.** With −40 °C ambient design (SOW-0160), EHT (IFC-9EA22696F8) and insulation are critical. Sweet-gas purge dewpoint must be tracked to prevent hydrate formation when isolating the receiver for pig retrieval.
- **HP flare vent sizing.** The vent (REQ-3.2; IFC-8FDDF0DF74) must accommodate barrel depressurization to retrievable pressure within an operationally acceptable time without exceeding HP flare header capacity.

## Trade-offs

- **Two receivers vs. single combined receiver.** Two receivers (per SOW) give redundancy and align with the two-train inlet-separator basis (V-1600-2 / V-1700-2). A single combined receiver (per DBM) reduces skid count and footprint but creates a single point of failure on the plant inlet.
- **Conservatism on H2S basis.** Designing to the license value (2.0 mol%) reduces rework risk but increases material cost (likely higher-spec clad/CRA). Designing to 0.1 mol% optimizes cost but introduces compliance risk if operating H2S excursions occur within license envelope.
- **Quick-opening closure type.** Threaded vs. bayonet vs. clamp closures trade operator safety, opening time, and capital cost. Selection is `ASSUMPTION` / Vendor preference unless EPC issues a project standard.

## Examples

`ASSUMPTION` — illustrative only (no example pig-receiver datasheet was located inside the accessible source slices):
- Tagging convention `PR-1010-2` / `PR-1020-2` follows the facility numbering used in DBM §Inlet Separation for inlet separators V-1600-2 / V-1700-2 (i.e., facility designator `-2` for the 03-25 facility).
- Typical 24-inch pig receiver barrel: ~3 m barrel length; major reducer to ~12-inch nominal pipeline tie-in — not specified in source for this package; `TBD`.

## Conflict Table (for human ruling)

Conflicts captured here are open items requiring an HRR (Human Ruling Required) to close. Each row identifies the disagreement, source pointers, impacted artifact sections, a proposed authority, and the placeholder for the ruling.

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFT-01 | Number of pig receivers: 2 receivers vs. 1 combined receiver. | SOW-0158 and SOW-0159 (`SCOPE_LEDGER.csv`) — "(2x) Pig receiver assemblies (PR-1010/1020-2)" | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §Inlet Pipeline Interface and Pigging — "A single combined three-phase pig receiver is provided." | Datasheet §Attributes/Quantity; Specification §REQ-1; Guidance §Considerations; Procedure §Steps (vendor RFQ scope) | PROPOSAL: SOW package basis (two receivers) is authoritative because it is the package-level source heading 42 and the workbook row 77 driver. DBM may reflect an earlier facility-level summary. | TBD |
| CFT-02 | Sour-service H2S basis: 0.1 mol% (package) vs. 0.3 mol% design / 2.0 mol% license (DBM). | SOW-0159 (`SCOPE_LEDGER.csv`) — "Sour service: Design is 0.1 mol%" | DBM §Raw Gas and Water Design Conditions — "H2S, mol% ... design 0.3, license 2.0" | Datasheet §Service and Materials; Specification §REQ-5.4, §REQ-6.2; Guidance §Principles, §Trade-offs | PROPOSAL: governing material-selection basis = license value (2.0 mol%) for safety/regulatory conservatism; governing process-design basis = DBM design (0.3 mol%). Reconcile package text to DBM. | TBD |
| CFT-03 | Inlet ESDV shutdown pressures: 635 psig (inlet separator ESDV per DBM) and "delivery-point ESDV shutdown pressure TBC" (DBM) vs. package MAWP 635 psig (SOW-0160). | SOW-0160 — MAWP 635 psig | DBM §Inlet Pipeline Interface and Pigging — "635 psig at the inlet separator ESDV, with delivery-point ESDV shutdown pressure still TBC" | Datasheet §Process Conditions; Specification §REQ-2.4, §REQ-4.4 | PROPOSAL: align delivery-point ESDV shutdown with MAWP 635 psig pending pipeline-side input; carry as `TBC` until ruling. | TBD |
| CFT-04 | Authority of `26020-Package_Requirements.docx` clause-level requirements not yet locally accessible as markdown (e.g., codes, standards, vendor-doc table entries for this package). | Inferred (REQ-6 set as `ASSUMPTION`) | `_Sources/26020-Package_Requirements.docx` (binary; not converted) — package heading 42 | Specification §REQ-6, §REQ-9; Datasheet §References | PROPOSAL: convert package heading 42 to local markdown via `tools/pdf2md` (or equivalent for docx) and re-run four-documents Pass 2 to replace ASSUMPTION code/standards entries. | TBD |
