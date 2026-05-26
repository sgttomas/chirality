# Guidance — DEL-077-02 Package Datasheet (PKG-077 Methanol Injection)

> Directional document. Captures purpose, principles, considerations, trade-offs. Source-grounded; inferences labeled `ASSUMPTION`.

## Purpose

The PKG-077 Package Datasheet exists so a third-party (Package Vendor or another discipline performing package engineering and design) can engineer, design, and supply the methanol-injection package and so the EPC Integrator can correctly integrate it into the 4-25 Deepcut facility. Per `_CONTEXT.md`, this is a mandatory Gate 5 EPC anchor deliverable, and interface facts are intentionally **carried in this datasheet as evidence** rather than appearing as standalone deliverables.

## Principles

1. **Source fidelity over convention.** Every non-trivial datasheet value must trace to an accessible source (currently `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, the decomposition registers, or `_CONTEXT.md`). Convention or sibling-package patterns are not authority.
2. **TBD over invention.** Where source values are TBC ("to be confirmed") or TBD, those qualifiers propagate to the datasheet. This includes per-point injection capacities, J-T-mode injection rates, methanol tank SG, and acid-gas-compressor injection details (DBM-Deepcut L1328, L1351, L1392).
3. **Single-point-at-a-time operating premise.** All capacity, sizing, and control-narrative discussion in the datasheet assumes the system injects to one point at a time (DBM-Deepcut L1328). Any future relaxation of this premise invalidates pump/storage sizing and must be flagged.
4. **Transient-only role for methanol.** The facility uses methanol for **transient** hydrate management; continuous suppression in raw inlet piping is explicitly out of scope (DBM-Deepcut L428). Datasheet language must avoid implying steady-state methanol service.
5. **Responsibility split must be visible.** The datasheet is an EPC Integrator artifact, but it hands off to a Package Vendor for the actual engineered package; both ownerships must appear so neither side assumes the other's scope (PACKAGE_REGISTER.csv PKG-077).
6. **Interface evidence carried, not duplicated.** Because the package has many interface types (PACKAGE_REGISTER.csv), the datasheet should carry an interface requirements matrix internally rather than spawn per-interface child deliverables (`_CONTEXT.md` Notes).

## Considerations

- **Cryogenic-area design intent vs. injection-point list.** The DBM states (L1153) that the cryogenic area is designed to maintain ~6 degC of margin above hydrate temperature and "no methanol injection provisions are made in this area," yet (L1135, L1324, L1328) BAHX pass-inlet injection and J-T-valve injection points are required. These are reconciled by treating methanol as a **transient/protective contingency** in the cryogenic area, not part of steady-state design margin. The datasheet should reflect this distinction.
- **Acid-gas-compressor injection provisions are TBD** (DBM-Deepcut L1371). Until confirmed, the datasheet should list the injection point with a TBD capacity rather than omit it.
- **Methanol tank SG = 1.00 (pure)** is design-intent but TBC (DBM-Deepcut L1329, L1351, L1392). Triplex pump sizing depends on this; carrying the TBC explicitly preserves the linkage.
- **BAHX downstream temperature limits.** Methanol-system materials and any tracing/insulation choices at BAHX pass inlets must respect the BAHX 150 degF max design temperature (DBM-Deepcut L1324).
- **Gate 6 packaging disposition (see Conflict Table CT-1).** PACKAGE_REGISTER notes a Gate 6 disposition that methanol-injection scope is **included with the Cryogenic Unit package scope**, while DEL-077-02 is being produced as a standalone PKG-077 datasheet. The datasheet should produce content suitable either as a standalone or as a section folded into the Cryogenic Unit package datasheet; human ruling required to confirm intended consumer.

## Trade-offs

- **One-point-at-a-time vs. multi-point injection.** Single-point design minimizes pump rating and tank inventory but requires manual/sequenced operator action during multi-area transient events. Source basis explicitly chose single-point (DBM-Deepcut L1328); revisiting this premise increases vendor scope.
- **Atmospheric double-walled tank vs. pressurized storage.** Atmospheric double-walled storage (chosen per DBM-Deepcut L1329) minimizes regulatory and certification scope at the cost of relying on pump suction for distribution pressure.
- **Standalone PKG-077 datasheet vs. embedding within Cryogenic Unit datasheet.** See CT-1.

## Examples

- DBM-Deepcut L1328 enumerates the canonical injection-point list and is the primary example of the datasheet's required injection-point table.
- DBM-Deepcut Equipment List rows 54-55 (L2605-L2606) are the canonical example of tagged equipment entries.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-1 | Is PKG-077 Methanol Injection a standalone EPC package datasheet, or is its scope included in the Cryogenic Unit package datasheet per Gate 6 disposition? | PACKAGE_REGISTER.csv row PKG-077 (Gate 6 note: "Methanol Injection scope is included with the Cryogenic Unit package scope.") | DELIVERABLE_REGISTER.csv row `DEL-077-02_package-datasheet` (treats PKG-077 as a standalone package with its own Package Datasheet); `_CONTEXT.md` | Datasheet identification; downstream consumer (DEL-077-04 Vendor Engineered Equipment Package vs. Cryogenic Unit package); interface matrix scoping | Treat PKG-077 datasheet as standalone for now and design its content to be embeddable in the Cryogenic Unit package datasheet without rework. | TBD |
| CT-2 | Cryogenic area is described as having no methanol injection provisions (DBM L1153) yet BAHX pass-inlet and J-T-valve injection points are required (DBM L1135, L1324, L1328). | DBM-Deepcut L1153 | DBM-Deepcut L1135, L1324, L1328 | Datasheet "Injection Points", Guidance "Considerations", Specification R-3, R-9 | Read L1153 as referring to **steady-state hydrate margin** (no continuous suppression provided in cryogenic area), and L1135/L1324/L1328 as **transient/protective** injection points. Datasheet language adopts this reconciliation. | TBD |
| CT-3 | Acid-gas-compressor methanol injection provisions: required point (DBM L1328) but capacities/provisions are TBD (DBM L1371, L1351). | DBM-Deepcut L1328 | DBM-Deepcut L1371, L1351 | Datasheet "Injection Points"; Specification R-3, R-7 | Carry the injection point in the datasheet with capacity `TBD`, with a forward action to confirm at acid-gas-compressor vendor selection. | TBD |
