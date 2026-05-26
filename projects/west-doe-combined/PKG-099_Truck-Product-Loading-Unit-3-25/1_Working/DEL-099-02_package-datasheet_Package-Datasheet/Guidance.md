# Guidance — DEL-099-02 Package Datasheet (Truck Product Loading Unit 3-25)

Pass set: P1_P2 (drafted 2026-05-25 by TASK+four-documents)

## Purpose

The Package Datasheet exists because `PKG-099 — Truck Product Loading Unit 3-25` is a vendor-supplied (`PT`, package type) scope item that must be tendered, engineered, and delivered by a third party while remaining auditable inside the EPC Integrator's `26020-03 3-25 Liquids Hub` workscope. The datasheet is the single artifact that consolidates package identity, scope boundary, design conditions, equipment list, interface applicability, and the vendor engineering deliverable index in a form a discipline engineer (process, electrical, I&C, civil, structural, F&G) can consume without re-deriving facts from RFQ prose or the project-wide Package Requirements document. Per `_CONTEXT.md`, interface facts are intentionally carried here rather than as standalone deliverables; this concentrates the package's evidentiary footprint into one auditable file.

## Principles

- **Source-anchored.** Every non-trivial entry on the Datasheet should cite a source slice (`26020-Package_Requirements.docx` §, or the interface workbook row/column). Inference is permitted only when explicitly labelled ASSUMPTION.
- **Boundary clarity over completeness.** The By-Others list (shipping, installation on piles, tie-ins, electrical connection installation, mounting platform / stairs) is as important as the included scope; ambiguity at the boundary causes commercial disputes.
- **Interface applicability is binary, then qualified.** The `Yes/No` matrix from §Physical Interface Summary is consumed by other discipline packages as a hard fact; qualifications belong in notes, not in the applicability column.
- **Carry only what is sourced.** If the source says "-" or "TBD" (e.g., capacity/design throughput rollup; Interface Coordination Notes), the Datasheet must reflect that, not invent a value.
- **The vendor deliverable list is the contract for engineering progress measurement.** The grouped list under §Vendor Engineering Deliverables (Core vendor, Core package engineering, Loading/metering, Process piping, Drainage/containment, Electrical, I&C, F&G, Structural, Civil) drives both progress S-curves and document-control workflows.

## Considerations

- **Custody-transfer metering.** Truck loading typically involves custody transfer of product. The source identifies flow transmitters and a metering package (`INS-015`) but does not specify accuracy class, proving requirements, or regulatory category. Treat custody-transfer specification as a **TBD** to be resolved during vendor selection.
- **ESDV count and SIL.** Source states "Emergency Shut Down Valve (ESDV)" without quantity per station or per header, and does not specify SIL classification. SIL is captured in the vendor deliverable set (`TSF-009` SIL Determination Report, `TSF-011` SRS, `TSF-013` Supplier SIL Documentation), so this is a deferred design item, not a Datasheet gap — but the Datasheet should note that the SIL determination depends on vendor scope.
- **Interface workbook version drift.** Source references `26020-Packages_Interfaces.3.xlsx` inline (e.g., row 98 col M for lighting). The current Gate-7 source bundle includes `26020-Packages_Interfaces_4_export.xlsx`. Confirm the row/column mapping survived the `.3 → _4_export` revision before treating row 98 as authoritative.
- **Two stations, four lines.** The Datasheet carries 103 m³/h per station and 415 m³/h total header (4 lines). Per station = 2 trucks simultaneously × 2 stations = 4 loading positions = 4 lines. 4 × 103 = 412 ≈ 415 within rounding. Treat the per-station and header values as consistent; do not "correct" the small discrepancy without source authority.
- **By-Others and structural interface.** The package excludes installation on piles, tie-in piping, and mounting platforms; yet the interface matrix declares Structural/Foundations/Supports as `Yes`. This is consistent: the vendor must supply the structural design / loads / anchor information needed by the EPC for the by-Others foundation work. Make sure structural deliverables (`STR-005`, `STR-006`, `STR-013`, `STR-014`) reach the EPC civil/structural team.
- **Maintenance Access declared "No".** This is unusual for a loading station and likely means "no separate maintenance access deliverable from the vendor" rather than "no maintenance access required". Confirm interpretation during design review.

## Trade-offs

- **Carrying interfaces here vs. as standalone deliverables.** Concentrating interface facts in the Datasheet (per `_CONTEXT.md` Notes) reduces deliverable count and keeps facts adjacent to the equipment they describe, at the cost of making cross-package interface reporting depend on parsing each package datasheet. Decomposition has accepted this trade.
- **Detailed design conditions vs. RFQ deferral.** The Datasheet captures only what the Package Requirements document states. Anything beyond (e.g., truck connection type, vapour recovery on loading) lives in the RFQ and vendor proposal. Pulling those into the Datasheet would duplicate the RFQ and create version-skew risk.

## Examples

- The Datasheet's Physical Interface Summary table is a 1:1 transcription of source §Physical Interface Summary (with the one explicit source-cited cell preserved verbatim: "Area / Exterior Lighting: Yes — `26020-Packages_Interfaces.3.xlsx` column M (row 98)").
- The Vendor Engineering Deliverables list in Specification §REQ-099-02-40 preserves the source's category groupings ("Core vendor documents", "Core package engineering", "Loading / metering package", etc.) so the EPC document controller can apply the same grouping in the vendor document index (`PRQ-009`).

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-001 | Package title in `_CONTEXT.md` is "Truck Product Loading Unit 3-25"; source Heading1 is "26020-03-PT-23-001 — Condensate Truck Loading Stations". | `_CONTEXT.md` §Identity | `_Sources/26020-Package_Requirements.docx` Heading1 (heading 18191) | Datasheet §Identification, Specification §Scope | Treat source title as the formal package title; treat `_CONTEXT.md` name as the decomposition shorthand. | TBD |
| C-002 | Per-station × 4-line arithmetic (4 × 103 = 412) does not equal the stated header total (415 m³/h). | `26020-Package_Requirements.docx` §Scope Notes (per-station 103 m³/h) | Same §Scope Notes (header total 415 m³/h) | Datasheet §Design Conditions; Specification §REQ-099-02-12/13 | Carry both values verbatim; do not reconcile until source confirms whether 415 includes margin or rounding. | TBD |
| C-003 | Source cites `26020-Packages_Interfaces.3.xlsx` for the Area/Exterior Lighting interface fact, but the Gate-7 source bundle contains `26020-Packages_Interfaces_4_export.xlsx`. | `26020-Package_Requirements.docx` §Physical Interface Summary (heading 18225) | `_Sources/26020-Packages_Interfaces_4_export.xlsx` (filename in `_Sources/`) | Datasheet §Physical Interface Summary; Specification §REQ-099-02-32 | Reconcile row 98 / col M in `_4_export` workbook and update the citation when confirmed. | TBD |
| C-004 | Interface matrix declares Maintenance Access = "No"; this is atypical for a truck loading station. | `26020-Package_Requirements.docx` §Physical Interface Summary | Generic discipline expectation | Datasheet §Physical Interface Summary; Guidance §Considerations | "No" reflects "no separate maintenance access deliverable from vendor", not "no maintenance access required". Confirm with project. | TBD |
| C-005 | Source §Interface Coordination Notes is "TBD". | `26020-Package_Requirements.docx` §Interface Coordination Notes (heading 18547) | — | Datasheet §Open Items; Specification §Verification | Carry as TBD; do not invent coordination notes. | TBD |
