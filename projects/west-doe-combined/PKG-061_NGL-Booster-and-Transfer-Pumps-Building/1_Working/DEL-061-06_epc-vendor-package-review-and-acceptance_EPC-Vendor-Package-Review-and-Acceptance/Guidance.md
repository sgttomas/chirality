# Guidance — DEL-061-06 EPC Vendor Package Review and Acceptance

## Purpose

This deliverable provides the EPC Integrator's binding evidence that the Package Vendor's engineered package and turnover documentation for the NGL Booster and Transfer Pumps Building (`PKG-061`) satisfy the EPC anchor deliverables — Scope of Work (`DEL-061-01`), Package Datasheet (`DEL-061-02`), and Construction Work Package (`DEL-061-03`) — and are ready for integration into the broader 26020 facility NGL liquids transfer system.

Source: `26020-Package_Requirements.docx` Heading 17 (location TBD — source slice not locally accessible in markdown during this run); `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-061-06`.

## Principles

- **Acceptance is integrator-led, not vendor-self-certified.** `_CONTEXT.md` and the decomposition register assign EPC Integrator as the lead responsible party with Package Vendor input.
- **Evidence is anchored to the source's enumerated artifacts.** The Heading 17 "Vendor Engineering Deliverables" list is the canonical artifact set. Acceptance does not invent new artifact requirements; it confirms the presence and adequacy of those artifacts. (Specific enumerated artifacts TBD until Heading 17 source slice is locally accessible in markdown.)
- **Interface evidence follows the Heading 17 Physical Interface Summary.** Only interfaces marked `Yes` for `PKG-061` row are in scope; the interface workbook (`26020-Packages_Interfaces_4_export.xlsx`, row 75) provides the canonical interface evidence row.
- **Numeric design values come from vendor submittals.** Until the vendor's pump data sheets (`MEC-007`), NPSH calcs (`PRO-013`), and electrical/building submittals are accepted, numeric values remain `TBD` in this evidence pack rather than being asserted from decomposition prose. (ASSUMPTION — typical EPC practice; consistent with PKG-054 sibling acceptance pattern.)
- **Building scope is treated as first-class.** Unlike a pure rotating-equipment package, `PKG-061` bundles a pumps building. Building / enclosure submittals (architectural, structural, HVAC, F&G, area classification) are part of the acceptance evidence, not background context.

## Considerations

- **Combined rotating-equipment + building scope.** The package name explicitly includes "Building." Acceptance must cover both rotating-equipment FAT/performance evidence and building/enclosure submittals; reviewers should not treat the building as a secondary concern. (ASSUMPTION — derived from package name; specific building scope items TBD until Heading 17 is locally accessible.)
- **Hazardous-area classification.** NGL service in an enclosed pumps building drives area-classification, ventilation, and F&G considerations. Acceptance evidence should explicitly confirm area-classification drawings and motor / instrumentation suitability.
- **NGL service properties.** NGL is volatile and flashing-prone; pump NPSHa margin, seal selection, and relief-protection details warrant explicit attention. Specific values TBD until vendor submittals are accepted.
- **Booster vs. transfer pump distinction.** "Booster" and "Transfer" pumps typically have different duty curves and may be configured in series or parallel. Acceptance should verify the configuration matches the EPC Package Datasheet (`DEL-061-02`). (ASSUMPTION — exact configuration TBD until Heading 17 source slice is accessible.)
- **Building-related interfaces.** Foundations, structural anchoring, HVAC, fire/gas, lighting, and grounding inside the building are all interface points; the acceptance pack should treat the building boundary as an explicit interface surface, not a transparent container.

## Trade-offs

- **Depth of vendor re-engineering review vs. timeline.** EPC Integrator review must be deep enough to find configuration mismatches against `DEL-061-02` but cannot substitute for vendor engineering. The default disposition for purely vendor-engineering details with consistent source-grounded inputs is "accepted on evidence" rather than re-derivation.
- **Open-items closure vs. carryover.** Items that cannot be closed before package handoff should be explicitly carried with named owners rather than left silent; this preserves traceability into commissioning.
- **Single acceptance bundle vs. staged acceptance.** A staged approach (engineering acceptance → fabrication acceptance → building turnover acceptance → mechanical turnover acceptance) aligns with the dual nature (equipment + building) of this package. (ASSUMPTION — staging not mandated in source; recommended by analogy to other building-bundled packages.)
- **Reviewer assignment by discipline.** With combined mechanical and building scope, reviewers should be assigned by discipline area (rotating equipment; structural/architectural; HVAC; electrical/area classification; F&G; quality) rather than by document, to avoid gaps.

## Examples

By convention (cross-referenced from the PKG-054 Heading 9 sibling pattern), the Heading 17 "Vendor Engineering Deliverables" enumeration is expected to group vendor artifacts by function (Core vendor documents; Core package engineering; Rotating equipment / pumps; Process piping interfaces; Drainage / containment interfaces; Electrical, lighting, EHT, grounding; Instrumentation and controls interfaces; and, for this package, Building / structural / HVAC interfaces). The acceptance checklist should mirror this grouping so reviewers can audit one functional area at a time. (ASSUMPTION — specific groupings for Heading 17 TBD until source slice is locally accessible.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-061-06-01 | Heading 17 source slice is not locally accessible in markdown during this run; many specifics (equipment tags, enumerated vendor deliverables, interface set, scope notes / open items) carry `TBD` / `location TBD` rather than concrete content. | `_REFERENCES.md` (states no deliverable-specific source slices copied during PREPARATION) | `26020-Package_Requirements.docx` Heading 17 (binary; not converted) | All four documents — Attributes, Conditions, Construction, Requirements, Standards, Considerations | PROPOSAL: Convert Heading 17 to markdown and re-run with `RUN_PASSES=FULL` to replace `TBD` placeholders with source-grounded content. | TBD |
