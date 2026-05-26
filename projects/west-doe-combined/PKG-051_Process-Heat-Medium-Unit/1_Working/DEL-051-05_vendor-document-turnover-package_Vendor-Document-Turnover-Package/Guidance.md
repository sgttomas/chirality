# Guidance: DEL-051-05 — Vendor Document Turnover Package

## Purpose

This deliverable consolidates the vendor's documentation output for the Process Heat Medium Unit (`26020-01-PT-15-001`) into a controlled register, governs its submittal through fabrication and FAT, and culminates in a turnover package that the EPC Integrator can review and integrate into the larger facility document set. It exists because the package is vendor-engineered (per DEL-051-04) but must be integrated by the EPC against the EPC Scope of Work (DEL-051-01) and Package Datasheet (DEL-051-02). (Source: `DELIVERABLE_REGISTER.csv` row DEL-051-05; `_CONTEXT.md`.)

## Principles

- **Source-anchored register.** The register's content is grounded in `26020-Package_Requirements.docx` §6 "Vendor Engineering Deliverables" for the Process Heat Medium Unit. New rows added at execution time must be justified against either source text or the EPC document-control procedure.
- **Artifacts, not deliverables.** Individual source-document table rows from `26020-Package_Requirements.docx` are carried as artifacts/evidence inside this deliverable rather than as separate deliverables. (Source: `_CONTEXT.md` Notes; `DELIVERABLE_REGISTER.csv`.)
- **Vendor authors, EPC integrates.** The Package Vendor is the responsible party for documentation; the EPC Integrator performs interface/integration review only — no certification, approval, or issuance for reliance by an agent. (Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`.)
- **Discipline coverage mirrors interfaces.** The interface matrix in source §6 (Physical Interface Summary) drives which discipline document categories are mandatory in the register: every "Yes" interface row should map to discipline documents in the register (e.g., Electrical Power → ELE-002/003/014…; Utility Piping → PIP-003/008/017/024).

## Considerations

- **Code registration timing.** REG-022 (Pressure Equipment Registration) often gates shipment. Sequence its preparation early; jurisdiction-specific code requirements are not in the accessible source slice (TBD).
- **Hold codes / MDR cadence.** The accessible source does not specify submittal cadence, hold codes, or document-control numbering. These belong in the EPC document-control procedure and must be settled before the vendor index (PRQ-009) is baselined.
- **As-built closure.** PRO-028 and INS-029 (as-builts) are typically issued post-commissioning. Plan the turnover register to remain open through commissioning rather than closing at shipment alone.
- **Spares interface.** PRQ-015 (SPIR) and MEC-024 (Mechanical Spares / Special Tools) should be reconciled before the Vendor Data Book is finalized.
- **FAT vs SAT split.** MEC-021/022 (equipment FAT) and ELE-029/030 (electrical FAT/SAT) are separate streams; both feed the final data book.
- **Objective association is heuristic.** The package-grouping heuristic (PACKAGE_HEURISTIC) maps OBJ-001 / OBJ-004…OBJ-010 to this deliverable via PKG-051. This is recorded as ASSUMPTION until the EPC confirms.

## Trade-offs

- **Single index vs. discipline indices.** A single PRQ-009 simplifies EPC integration but may obscure discipline-level traceability. Discipline-level sub-indices add overhead but make interface reviews crisper.
- **Early baselining vs. flexibility.** Locking the register early prevents scope creep but reduces the vendor's ability to add late-arising sub-vendor documents.
- **Native vendor formats vs. EPC-mandated formats.** Native formats minimize vendor cost; EPC-format conversion improves downstream usability — typically a contractual call (TBD in accessible source).

## Examples

No procedure-level examples are provided in the accessible source slice (TBD). The Datasheet's "Construction" section enumerates every document code that must appear in the register; treat that enumeration as the working example of register contents.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| — | None observed between accessible sources at draft time. | — | — | — | — | TBD |
