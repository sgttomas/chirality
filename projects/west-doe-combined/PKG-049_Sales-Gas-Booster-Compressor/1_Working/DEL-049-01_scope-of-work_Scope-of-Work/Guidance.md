# Guidance — DEL-049-01 Scope of Work (Sales Gas Booster Compressor)

> Directional guidance for authoring and reviewing the EPC Scope of Work for PKG-049.
> Pass 1/Pass 2 draft. Rationale is drawn from the locally accessible DBM source; conservative inferences are labeled `ASSUMPTION`.

## Purpose

The Sales Gas Booster Compressor exists because the 04-25 Deep Cut Gas Plant's sales compression train discharges sweet sales gas at a pressure below TC sales pipeline delivery pressure. A dedicated single-stage boost package lifts treated sales gas from sales compressor discharge to the high-pressure sales gas coalescer and splitter that feeds the TC sales pipeline. The EPC Scope of Work is the EPC Integrator's anchor deliverable that bounds package identity, function, source basis, and whole-facility integration so that downstream EPC Integrator deliverables (Datasheet, Construction Work Package, Vendor Acceptance) and the Package Vendor's engineered package (DEL-049-04) and turnover documentation (DEL-049-05) share a single, source-anchored definition. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §SEC-02 Plant Overview, §SEC-05 Compression Configuration and Sales Gas Booster Compressor Basis; `_CONTEXT.md` Scope; GATE-07 PKG-049 deliverable family.

## Principles

- **Source-anchored boundaries.** The DBM is the authoritative source for design conditions, configuration, and integration. Where the DBM marks values as TBD or TBC (e.g., low suction pressure, normal discharge pressure, high/excess capacity, design aftercooler dP, recycle-valve fail position, clearance-pocket selection), the EPC SOW must carry the same markers forward rather than substitute synthetic values. Source: DBM-Deepcut §SEC-05.
- **Single-package, no-spare risk acknowledgement.** The package is 1 × 100% with no spare compressor or spare equipment/instrumentation. SOW reviewers should treat availability, sparing of critical instrumentation, and outage planning as deliberate design decisions inherited from the DBM, not as default vendor options. Source: DBM-Deepcut §SEC-05 Sales Gas Booster Design Conditions.
- **Drier-than-pipeline service.** Inlet gas is < 0.1 ppmv water due to upstream molecular-sieve dehydration. Material selection, hydrate guarding, and start-up sweeping should reflect dry, sweet service rather than wet sour service practice. Source: DBM-Deepcut §SEC-05 Sales Gas Booster Design Conditions.
- **Multi-mode duty.** The booster must perform at design capacity in both J-T and expander modes of the upstream cryogenic unit, with composition shifts between modes (notably propane content). Sizing and turndown decisions must hold across both modes. Source: DBM-Deepcut §SEC-05 booster compositions.
- **External-scope discipline.** Manual sweet-gas purge is explicitly out of package scope and is an external-responsibility interface. The EPC Integrator should keep this interface visible in the SOW so it is not silently absorbed into vendor scope or lost. Source: DBM-Deepcut §SEC-05 booster description.
- **VRU integration of vents.** Seal-pot vapour routes to the VRU suction header; distance-piece sweep purge prevents backflow. SOW review should confirm the VRU interface is coordinated with VRU package owners and not duplicated. Source: DBM-Deepcut §SEC-05 booster description.

## Considerations

- **Composition shift between operating modes.** Expander-mode propane content is 0.03 mol% versus J-T-mode 3.63 mol%. Aftercooler approach to dewpoint, knockout, and recycle behavior should be examined across both modes when reviewing vendor sizing. Source: DBM-Deepcut §SEC-05 booster compositions.
- **Frame and cylinder optimization.** The DBM identifies the Ariel KBK/4 with all cylinders on a single stage but flags evaluation of a larger high-efficiency cylinder on a two-throw design because of the low compression ratio (~2.1 in expander-mode pressure terms). SOW should explicitly preserve this evaluation as detailed-engineering scope rather than freeze the KBK/4 four-throw baseline prematurely. Source: DBM-Deepcut §SEC-05 booster description.
- **Recycle-valve fail position.** The DBM states fail-closed "to be confirmed during detailed engineering" — the EPC Integrator should treat this as an open safety/availability decision, not a defaulted setting. Source: DBM-Deepcut §SEC-05 booster description.
- **Clearance-pocket strategy.** Continuously variable, automated fixed-volume, and manual VVCP options are all in scope for evaluation. Power consumption at high suction pressure and recycle minimization should be the primary evaluation drivers. Source: DBM-Deepcut §SEC-05 booster description.
- **Battery limits and tag-number generation.** Tag numbers are not in the accessible DBM source slice (`location TBD`). The EPC SOW should commit to a tag-assignment process (e.g., facility tag register) rather than leave the gap open at handoff. ASSUMPTION: facility tag registers exist in non-extracted source materials.

## Trade-offs

- **Single-package availability vs. capital and footprint.** The 1 × 100% no-spare arrangement minimizes capital and footprint at the cost of full-throughput unavailability during compressor outages. The SOW carries this trade-off forward without modification per the DBM basis; alternative sparing would require a documented basis change. Source: DBM-Deepcut §SEC-05 Compression Configuration.
- **DOL soft-start vs. VFD/turndown.** The mapped basis is DOL with soft-start and no driver speed turndown. This simplifies the electrical interface (4,000 V bus) versus the upstream inlet/sales compressors that use a starting VFD, at the cost of fixed-speed operation. Source: DBM-Deepcut §SEC-05 booster description; §SEC-05 inlet/sales motor start method.
- **Sweet-gas purge externalization.** Excluding manual sweet-gas purge from the package reduces vendor scope and likely cost but transfers an interface and operational dependency to the facility. The SOW should make this explicit. Source: DBM-Deepcut §SEC-05 booster description.

## Examples

- **Compression ratio example.** Suction 6,137 kPag / discharge 12,866 kPag — a single-stage pressure ratio of approximately 2.1, consistent with the DBM observation that the low compression ratio motivates evaluating a larger cylinder on a two-throw frame. Source: DBM-Deepcut §SEC-05 Sales Gas Booster Design Conditions (calculated ratio).
- **Sales gas downstream routing example.** Plant sales gas is capable of flowing to TC, Enbridge, and Alliance receipt points; the booster targets TC pipeline delivery pressure specifically. The SOW integration narrative should make clear that the booster does not feed Enbridge or Alliance delivery points. Source: DBM-Deepcut §SEC-02 Plant Overview; §SEC-05 Compression Configuration; §SEC-05 booster description.

## Conflict Table (for human ruling)

No source conflicts identified from the locally accessible DBM material in Pass 1 / Pass 2 cross-checks. The locally-not-accessible references (Workbook Packages row 80; 26020-Package_Requirements.docx package heading 4) may introduce conflicts when extracted; surface them in the next pass when source slices become available.

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| (none) | — | — | — | — | — | TBD |
