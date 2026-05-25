# Guidance: DEL-038-05 — Vendor Document Turnover Package

## Purpose

The Vendor Document Turnover Package consolidates the vendor-originated documentation needed for the EPC Integrator and ultimately the Operator to accept, integrate, operate, and maintain the 600V Electrical Building (820-1) package. It exists so that vendor knowledge, evidence of compliance, and operational information move with the equipment from vendor scope into facility-level operations under a controlled, reviewable trail. (Decomposition basis: Gate 7 `DELIVERABLE_REGISTER.csv`, row DEL-038-05.)

## Principles

- **Single-vendor accountability with EPC review.** The Package Vendor owns documentation production; the EPC Integrator owns interface/integration review. The two roles must remain distinguishable in the register and the review record. (Source: Gate 7 `DELIVERABLE_REGISTER.csv`, ResponsibleParty column.)
- **Source-required documentation is evidence, not separate deliverables.** Individual source vendor document rows are artifacts within this deliverable, not standalone DELs. (Source: Gate 7 `DELIVERABLE_REGISTER.csv` notes column.)
- **Compliance must be traceable.** Vendor documentation must trace to the governing electrical code/standards (CSA C22.1-21 and the broader CSA/API/IEEE/ISA/NEMA set) and to the workbook package-requirements basis. (Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2866.)
- **Construction-basis alignment.** Vendor documentation must reflect the prefabricated, modular electrical-building basis (HVAC n+1; bottom cable entry; TECK/ACIC wiring; two-point ground-grid connections). (Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2971-2999.)

## Considerations

- **Granularity of the document register.** Without a confirmed PKG-038 entry in `26020-Package_Requirements.docx`, the precise document classes required for turnover are not enumerated; the register should be seeded conservatively (drawings, datasheets, certs, FAT, IOM, O&M, spares, turnover) and tightened once the package-requirements row is located. (location TBD.)
- **Revision and approval cycles.** Submittal workflows (IFR/IFA/IFC etc.) are not specified in the available DBM source slice; align with the EPC Integrator's project-wide submittal procedure when established. (location TBD.)
- **Interfaces.** PKG-038 has many applicable interface types (utility piping, drains/containment, electrical power, grounding/bonding, area/exterior lighting, I&C/control cabling, communications/network, building HVAC/services, fire & gas, maintenance access, grading/drainage/spill containment, structural/foundations/supports). Vendor documentation should not silently extend or restrict these interfaces; deviations belong in the EPC review record. (Source: Gate 7 `PACKAGE_REGISTER.csv`, PKG-038 row.)

## Trade-offs

- **Comprehensive register vs. timely submittal.** A wider register catches more risk but slows submittals. Recommended: a conservatively wide register at issue, then ruthless closeout discipline.
- **Vendor narrative vs. EPC-format expectations.** Vendor-native documentation reduces vendor effort; EPC-aligned formats reduce integration friction. Lean toward vendor-native at submittal and EPC-aligned at turnover for documents the Operator will consume.
- **Carrying source rows as artifacts vs. re-authoring.** Carrying source vendor document table rows preserves traceability; re-authoring can improve coherence but breaks provenance. The decomposition note explicitly favors carrying them as artifacts. (Source: Gate 7 `DELIVERABLE_REGISTER.csv` notes.)

## Examples

Not enumerated; concrete examples require the PKG-038 vendor-document list from `26020-Package_Requirements.docx`. (location TBD.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-038-05-001 | The complete vendor-document list for PKG-038 is not enumerated in the accessible DBM slice; `26020-Package_Requirements.docx` is named in `_REFERENCES.md` but the PKG-038-specific row is not locally located. | `_REFERENCES.md` (workbook reference) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (no per-package vendor-document enumeration found) | Datasheet Conditions/Construction; Specification R-038-05-08 | Treat the conservative register (drawings, datasheets, certs, FAT, IOM, O&M, spares, turnover) as a placeholder; finalize once the PKG-038 row in `26020-Package_Requirements.docx` is read. | TBD |
| HRR-038-05-002 | Submittal workflow (issue/review/approval cycles and dispositions) is not specified in available source. | `_CONTEXT.md` (anticipated artifacts) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (no workflow specified) | Specification R-038-05-02; Procedure submittal steps | Adopt the EPC Integrator's project-wide submittal workflow when published; do not invent a workflow here. | TBD |
| HRR-038-05-003 | Turnover-record composition (acceptance checklist, evidence pack contents) is not enumerated; DEL-038-06 (EPC Vendor Package Review and Acceptance) is the natural counterpart. | `_CONTEXT.md` anticipated artifacts | Gate 7 `DELIVERABLE_REGISTER.csv` row DEL-038-06 | Specification R-038-05-04; Procedure turnover steps | Anchor turnover-record composition to the DEL-038-06 acceptance checklist when authored. | TBD |
