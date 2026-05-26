# Guidance — DEL-101-02 Package Datasheet (PKG-101 Precast concrete foundations)

> Directional rationale for assembling, reviewing, and using the PKG-101 Package Datasheet. This document does not impose requirements; the Specification governs.

## Purpose

The Package Datasheet is the mandatory EPC Integrator technical-handoff record that carries the source-supported design basis, applicable standards, governing geotechnical assumptions, and interface facts required for third-party vendor or discipline package engineering and design of precast concrete foundations on the West Doe Deepcut expansion. `_CONTEXT.md` Notes identifies this as a "mandatory Gate 5 EPC anchor deliverable" and explicitly states that "interface facts are intentionally carried here as evidence rather than standalone deliverables" — the datasheet is therefore the single source of truth for PKG-101 interface evidence, not the construction work package or the scope-of-work deliverable.

## Principles

- **Source-grounded, not invented.** Every non-trivial value cites a local source slice; absent values are TBD. Decomposition prose routes; sources determine substance (`four-documents` SKILL § Authority hierarchy).
- **Carry, do not create, requirements.** The package datasheet exposes what already exists in the DBM `4-25_Deepcut_DBM.md` civil/structural basis (piles-and-foundations table, governing standards, geotechnical TBDs) and in the GATE-07 registers. The datasheet does not invent foundation sizes, pile counts, or dynamic-analysis results.
- **Distinguish package responsibility from vendor package ownership.** Per PACKAGE_REGISTER.csv row PKG-101, responsibility is "EPC Integrator or discipline subcontractor… source-dependent; no separate vendor-package ownership model is inferred." Do not assume a vendor-package handoff in the same sense as a packaged equipment vendor (e.g., PKG-047 VRU).
- **Surface TBDs.** Geotechnical bearing capacity, dynamic criteria, and compressor dynamic analysis are all TBD and must remain visible. Treat them as gates on downstream foundation engineering, not as drafting gaps to be filled.
- **Use interface evidence as the integration spine.** Only two interface types are registered for PKG-101: "Grading / Site Drainage / Spill Containment" and "Structural / Foundations / Supports." Limit the interface matrix to what is in INTERFACE_REGISTER.csv; do not add interface types not in source.

## Considerations

- **Precast scope inside the DBM.** The DBM identifies precast specifically for transformers ("generally supported on precast concrete bearing foundations") and for compressors ("precast concrete block supported on driven steel piles, subject to dynamic analysis"). The PKG-101 datasheet is the right place to surface both, including the alternate compressor concept (direct skid-to-pile welding, currently TBD and considered unlikely for the compressor size).
- **Pile interaction.** Even though the package is titled "Precast concrete foundations," in the DBM most precast usage sits on driven steel piles. The datasheet should make the precast-on-piles relationship clear so vendor/discipline engineering does not size precast as a standalone bearing element.
- **Grading interface.** Top-of-pile-cap elevations and pad slope (1.5% nominal, reducible to 1.0%) are coupled — vendor engineering of precast cap/block elevations must coordinate with pad grading. Spill containment / surface control is the second registered interface; foundation block geometry should not block surface-control features.
- **Construction and testing.** CSA A23.1/A23.2 is the construction and testing basis. The datasheet should cite the standard but not transcribe code clauses.

## Trade-offs

- **Carry vs. defer.** Workbook row 102 cell-level details and the `26020-Package_Requirements.docx` PKG-101 section were not directly opened in this run (no matched docx package heading per PACKAGE_REGISTER.csv `DocxPackageMatched=FALSE`). The trade-off is between marking those slices `location TBD` (preferred per skill rules) and waiting on a follow-up read. The datasheet records them as `location TBD` so handoff is not blocked, but vendor engineering should obtain the source slices before relying on cell-level values.
- **Direct skid-to-pile welding vs. precast block.** The DBM flags the alternate concept as TBD and unlikely. The datasheet preserves both options rather than pre-selecting precast, because Propak verification is the gating decision.

## Examples

- **Compressor foundation precast block.** Record in the datasheet that compressor foundations are precast concrete block on driven steel piles per DBM § "Piles and Foundations" (line 2746), with a TBD pointer to dynamic analysis results (line 2852). Do not write a numeric block size — it is not in source.
- **Transformer precast bearing foundation.** Record per DBM line 2745 with no open requirement. Do not derive bearing-capacity values; those are TBD pending geotechnical report.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-101-02-01 | Package title says "Precast concrete foundations" but DBM default foundation basis is driven steel piles, and precast usage in DBM is mostly precast block on piles (compressors) or precast bearing foundations (transformers). | PACKAGE_REGISTER.csv row PKG-101 Name; `_CONTEXT.md` PackageName | DBM `4-25_Deepcut_DBM.md` § "Piles and Foundations" (lines 2740, 2745-2749) | Datasheet Attributes; Specification REQ-101-02-06; Guidance "Pile interaction" | PROPOSAL: read package title as the precast component of compound precast-on-piles foundations and as standalone precast bearing foundations (transformers); preserve pile carrier where DBM specifies it. | TBD |
| CONF-101-02-02 | Objective-to-deliverable association OBJ-001; OBJ-008 is consumed via PACKAGE_HEURISTIC; objective texts were not consulted in this run, so directional support is asserted on register evidence alone. | DELIVERABLE_REGISTER.csv SupportsObjectives | OBJECTIVE_REGISTER.csv (not consulted this run) | Specification REQ-101-02-14 | PROPOSAL: keep ASSUMPTION (best-effort mapping) until objective texts are read or human confirms. | TBD |
| CONF-101-02-03 | Workbook Packages row 102 cell-level data and `26020-Package_Requirements.docx` PKG-101 slice were not directly read; PACKAGE_REGISTER.csv `DocxPackageMatched=FALSE`. The datasheet's "carried" workbook facts therefore rely on register fields rather than original cells. | PACKAGE_REGISTER.csv row PKG-101 (DocxPackageMatched=FALSE) | `_Sources/26020-Packages_Interfaces_4_export.xlsx`; `_Sources/26020-Package_Requirements.docx` | Datasheet References; Specification REQ-101-02-15 | PROPOSAL: mark unread cell-level / docx-section facts as `location TBD` and require resolution before vendor engineering relies on them. | TBD |
