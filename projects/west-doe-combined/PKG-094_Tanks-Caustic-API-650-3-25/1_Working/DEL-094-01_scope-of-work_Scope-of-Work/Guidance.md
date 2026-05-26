# Guidance — DEL-094-01 Scope of Work, PKG-094 Tanks, Caustic (API 650) 3-25

> Directional guidance for authors of the EPC Scope of Work deliverable. Rationale grounded in locally accessible source slices; conflicts surfaced in the Conflict Table for human ruling (HRR).

## Purpose

The Scope of Work is the EPC Integrator's anchor deliverable for PKG-094. It exists so that:

- The Package Vendor (engineering/design/equipment) and EPC Integrator (facility integration) share a single, source-grounded statement of what the caustic tank package is, what it does, and where the boundaries lie.
- Downstream EPC Integrator deliverables (Package Datasheet DEL-094-02, Construction Work Package DEL-094-03, Vendor Package Review and Acceptance DEL-094-06) can rely on a stable anchor.
- Vendor-side deliverables (Vendor Engineered Equipment Package DEL-094-04, Vendor Document Turnover DEL-094-05) have a clear input contract.

Source: `DELIVERABLE_REGISTER.csv` rows DEL-094-01..06; `_CONTEXT.md`.

## Principles

1. **Source fidelity over restatement.** Carry SOW-0193..0196 language verbatim where the source is specific (e.g., TK-6930-2 design pressure, heater minimum 32.2 °C). Paraphrase only where source language is itself narrative.
2. **Distinguish package scope from facility integration.** The package vendor produces tanks; the EPC Integrator integrates them into the 03-25 Liquids Hub caustic mercaptan treating system. The SoW must make both visible.
3. **Preserve "by others" items as first-class scope statements.** Foundations, mounting, E/I, platforms, and staircase exclusions per SOW-0196 are facility-side and must not be lost.
4. **Carry TBD/TBC forward.** Source-declared opens (capacity/throughput TBC, per-item flow rate TBD, SG 1.75 TBC, caustic tank material/coating TBC) must remain visible, not silently filled.
5. **Reference the live decomposition snapshot.** Use the GATE-07_Final_Published_2026-05-24 snapshot as the authoritative basis; do not re-derive scope from mutable working files.
6. **Mechanical discipline reads first; package functional reads second.** When authoring tagged-equipment content, lead with mechanical/API 650 considerations and then capture process function from SOW-0194.

## Considerations

- **Site basis (-40 °C minimum ambient)** drives winterization, heating, insulation, and metallurgy. The SoW should explicitly acknowledge the DBM site basis for the caustic tank package even though SOW-0196 abbreviates this as "minimum ambient temperature."
- **Caustic chemistry.** 50 wt% NaOH/H2O (SG 1.75 TBC) is corrosive and drives material/coating selection, aluminum prohibition in the caustic building, and ventilation/blanket strategy.
- **Vent and truck-out.** Spent caustic tank vents through a flame arrestor to the incinerator header and supports truck-out — these are facility-integration paths owned by the EPC Integrator.
- **VRU exclusion.** Fresh caustic tank is explicitly not connected to the VRU.
- **Heater design.** Heater is vendor-designed, but minimum service condition (32.2 °C / 90 °F) is set by source. Do not invent a heater duty in the SoW.
- **Interface scope.** The PKG-094 interfaces enumerated in `INTERFACE_REGISTER.csv` (9 disciplines) are the package-to-facility integration surface. The SoW should name each, even when downstream deliverables carry the details.

## Trade-offs

- **Detail vs anchor stability.** The SoW is an anchor; pushing too much vendor-specific detail into it weakens the anchor. Detail belongs in the Package Datasheet (DEL-094-02).
- **Verbatim source quoting vs readable narrative.** Direct quotes from SOW-0194/0195 preserve auditability; narrative paraphrase improves readability. Prefer verbatim for any specific number or constraint and narrative for transitions.
- **Mandatory vs additional Gate-5 deliverables.** DEL-094-01/02/03 are mandatory EPC anchors; DEL-094-04/05/06 are additional Gate-5 deliverables. The SoW should reflect this asymmetry in responsibility framing.

## Examples (source-grounded only)

- **Verbatim equipment line from source:** "Item No. 1, Spent Caustic Storage Tank: (TK-6930-2); Spent caustic from Mercaptan Treating Unit is level-controlled to this tank; Quantity: 1; Design & fabrication to modified API 650, 400 bbl, nominal capacity; Design pressure: 32 Oz, 1.0 Oz Vacuum.; Atmospheric pressure tank.; c/w heater at 32.2 °C (90 °F) minimum. Vendor to design the heater." (`SCOPE_LEDGER.csv` SOW-0195)
- **Verbatim "by others" line:** "By others: Foundations, mounting tanks at site, electrical/instrumentation, platforms, staircase etc." (`SCOPE_LEDGER.csv` SOW-0196)

## Conflict Table (for human ruling)

Items here require human ruling (HRR) before downstream production deliverables can rely on them. Each row is `PROPOSAL` until ruled.

| Conflict ID | Conflict (short) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-094-01 | Fresh Caustic Tank tag and exact capacity not stated in source; SOW-0194 names function only; SOW-0196 "Item 2" implies parallel 400 bbl basis. | `SCOPE_LEDGER.csv` SOW-0194 ("one (1) fresh caustic tank") | `SCOPE_LEDGER.csv` SOW-0196 (Item 2: Atmospheric; Minimum ambient temperature; Flow rate: TBD; 400bbl) | Datasheet: Tagged Equipment; Specification: R2.2 | PROPOSAL: Treat Fresh Caustic Tank as 400 bbl atmospheric matching Item 2; obtain tag from Package Datasheet DEL-094-02. | TBD |
| CONF-094-02 | Caustic solution SG (1.75) and aluminum prohibition come from DBM (facility design basis), not directly from PKG-094 source heading. | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Caustic Mercaptan Treating section, lines ~389-402) | `26020-Package_Requirements.docx` heading 46 (text not locally accessible) | Datasheet: Conditions; Specification: R4.3 | PROPOSAL: Adopt DBM values as facility-design-basis context; flag SG 1.75 as TBC per DBM text; verify against package heading 46 when text is extractable. | TBD |
| CONF-094-03 | Heater service minimum stated as 32.2 °C (90 °F) in SOW-0195 but "vendor to design heater" — relationship between this minimum and the -40 °C site ambient is not explicitly bridged in source. | `SCOPE_LEDGER.csv` SOW-0195 ("heater at 32.2 °C (90 °F) minimum") | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Site basis: -40 °C minimum ambient) | Datasheet: Conditions; Specification: R4.1, R4.2; Procedure: heater verification step | PROPOSAL: Read 32.2 °C as caustic-process minimum maintained inside the tank; -40 °C drives external winterization load. Vendor designs heater to bridge. | TBD |
| CONF-094-04 | Objective association: `_CONTEXT.md` lists OBJ-002..010 supported by this deliverable, but `OBJECTIVE_DELIVERABLE_MAP.csv` may not list this deliverable ID explicitly (package-grouped mapping). | `_CONTEXT.md` (Supports Objectives) | `OBJECTIVE_PACKAGE_MAP.csv` (rows for PKG-094 list OBJ-002..010 at package level) | Specification: R8.1; downstream traceability | PROPOSAL: Hold OBJ-002..010 association as `ASSUMPTION: PACKAGE_HEURISTIC` until human ruling per `OBJECTIVE_ASSOCIATION_MODE` override. | TBD |
| CONF-094-05 | Authoritative-source text for 26020-Package_Requirements.docx package heading 46 not locally extractable in this run; current grounding relies on the SCOPE_LEDGER extract and DBM. | `26020-Package_Requirements.docx` (referenced in `_REFERENCES.md` and decomposition rows) | `SCOPE_LEDGER.csv` SOW-0193..0196 (extracted from same source) | All four documents | PROPOSAL: Treat SCOPE_LEDGER extracts as faithful proxies; re-verify against package heading 46 text when locally extracted; do not invent additional clause-level content in the interim. | TBD |
| CONF-094-06 | RFQ source (`26020-03-PT-RFQ-19-002_Tanks_Caust_1_R0.docx`) referenced via OBJECTIVE_PACKAGE_MAP word source basis was not opened in this run; may contain commercial/scope language relevant to the SoW. | `OBJECTIVE_PACKAGE_MAP.csv` (Word Source Basis column) | not read | Specification: R5/R6; Procedure: prerequisites | PROPOSAL: Schedule a follow-on read of the RFQ; treat any RFQ-only content as `TBD` in the current SoW. | TBD |
