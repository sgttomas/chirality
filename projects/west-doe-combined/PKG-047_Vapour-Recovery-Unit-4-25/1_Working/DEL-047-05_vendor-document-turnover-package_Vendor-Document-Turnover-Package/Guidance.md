# Guidance: Vendor Document Turnover Package (DEL-047-05)

## Purpose

Why this deliverable exists: the VRU 4-25 package is a vendor-built skidded compression unit (Ro-Flo two-stage rotary vane, lead-lag two-train, sour service) acquired as a packaged scope. The Owner and EPC Integrator do not author its engineering content; they receive and integrate it. The vendor document turnover package is the controlled corridor through which the vendor's engineering output enters the project record, is reviewed, accepted, and retained as the as-built evidence base for operations, maintenance, regulatory registration, and future modification.

(Source: `_CONTEXT.md` scope; 26020-Package_Requirements.docx, "26020-01-PT-12-002 - Vapour Recovery Unit", Basic Scope and Vendor Engineering Deliverables.)

## Principles

- **Vendor authors, EPC integrates.** The register tracks documents authored by the Package Vendor. EPC Integrator review is a fitness-for-integration check, not an author role. (Source: `_CONTEXT.md` ResponsibleParty.)
- **Index-first.** PRQ-009 Vendor Document Index is the live spine; nothing reaches turnover that is not registered in PRQ-009. (Source: 26020-Package_Requirements.docx, Vendor Engineering Deliverables → Core vendor documents.)
- **Procedure-governed.** All numbering, revision, transmittal, review-status, and supersession rules live in DOC-008 and are not re-invented per submittal. (Same source.)
- **Source rows as evidence, not deliverables.** Where individual source vendor document rows exist, they remain artifacts/evidence inside this turnover package and are not promoted to standalone project deliverables. (Source: `_CONTEXT.md` Notes.)
- **Sour service awareness.** Material certificates and NACE compliance evidence in the data book are first-order, not boilerplate, because the package is in sour service (0.3557 mol% H2S, 0.9434 mol% CO2). (Source: 26020-Package_Requirements.docx Major Included Equipment.)
- **Two-train symmetry.** Documentation must clearly distinguish Train 1 vs Train 2 artifacts where they differ (serial numbers, MTRs, FAT results), and identify shared artifacts where applicable (building, common utilities). (Source: same; Basic Scope.)
- **Turnover is the last gate, not the first.** PRQ-016 + QLT-021 close the package. Holding open items at turnover converts them into operations-phase debt and must be explicitly flagged.

## Considerations

- **Pressure equipment registration (REG-022) jurisdiction.** The applicable regulatory regime (e.g., ABSA/CRN if in Alberta) is not stated in the available source slice. The vendor needs the jurisdiction settled early because nameplate, MTR retention, and registration application content are jurisdiction-specific. **TBD** — needs human ruling.
- **Review-status code set.** DOC-008 prescribes the controlling procedure, but the exact review-status code mapping the EPC Integrator will use (Code 1 / 2 / 3 style or equivalent) is not in the consulted slice. **TBD**.
- **Acceptance signature path.** The available source identifies the artifacts that constitute final turnover but not the named signature path for EPC Integrator acceptance of PRQ-016 / QLT-021. **TBD**.
- **Interface document drift.** The source references `26020-Packages_Interfaces.3.xlsx`; the locally available export appears to be `26020-Packages_Interfaces_4_export.xlsx`. Where interface tie-ins are documented in vendor submittals (PIP-004 Tie-In List, CTL-026 Package Vendor Interface Specification), reviewers should confirm the controlling interface revision before accepting. **ASSUMPTION**: revision drift exists; **CONFLICT-1** captured below.
- **Cross-discipline coverage.** The source enumerates an extensive cross-discipline deliverable list (process, mechanical, electrical, I&C, structural, fire & gas). The register must not silently drop a discipline because no row was transmitted; absence is itself a status to track.
- **FAT evidence.** MEC-021/MEC-022 are pre-shipment hold points. Their acceptance status should drive the release-to-ship decision and propagate into PRQ-013 Logistics / Shipping Plan readiness.
- **Spares continuity.** PRQ-015 SPIR drives long-lead spares ordering. Delay in SPIR delays operations readiness independent of mechanical completion.

## Trade-offs

- **Register granularity vs maintainability.** Tracking every row in the source's Vendor Engineering Deliverables table maximizes auditability but increases register maintenance load. The required granularity is row-per-source-row; sub-row breakdown (e.g., per-vessel data sheet) is recommended only where the vendor's own document numbering already requires it.
- **Early partial transmittal vs single-final-package.** Earlier discipline transmittals support parallel EPC review and reduce end-of-project pile-up, but multiply transmittal handling. The default expectation under DOC-008 is rolling transmittal with consolidation into PRQ-016 at the end; pure-single-package turnover is not the source's stated mode. (ASSUMPTION: rolling transmittal is the operative mode.)
- **Strict vendor-numbering preservation vs project-numbering re-mapping.** Preserving vendor numbering simplifies vendor's internal traceability and reduces transcription error; re-mapping to project numbering simplifies EPC and Owner search. DOC-008 governs the chosen convention; in the absence of explicit direction, the register should carry both as parallel columns.

## Examples

The source's Vendor Engineering Deliverables table is itself the canonical example of the register's expected row coverage. See `Datasheet.md` Construction section for the enumerated rows. Worked-out examples of individual transmittal forms, review-comment logs, and turnover acceptance letters are **TBD** (not present in the consulted source slice).

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONFLICT-1 | Interface workbook revision drift: VRU section in `26020-Package_Requirements.docx` cites `26020-Packages_Interfaces.3.xlsx`; locally available file is `26020-Packages_Interfaces_4_export.xlsx`. | 26020-Package_Requirements.docx, "26020-01-PT-12-002 - Vapour Recovery Unit", Physical Interface Summary | `_Sources/26020-Packages_Interfaces_4_export.xlsx` (filename only) | Datasheet References; Guidance Considerations; tie-in artifacts in register (PIP-004, CTL-026) | PROPOSAL: treat `_4_export` as the latest available export and verify content equivalence with the `.3` revision before accepting any vendor interface submittal that references `.3`. | TBD |
| CONFLICT-2 | Final-acceptance gate: source lists PRQ-016 and QLT-021 as final consolidations but does not state which one is the formal acceptance trigger. | 26020-Package_Requirements.docx, Vendor Engineering Deliverables, PRQ-016 row | Same source, QLT-021 row | Specification R-14; Procedure final steps | PROPOSAL: treat PRQ-016 as the master turnover artifact, with QLT-021 indexed inside it. | TBD |
| CONFLICT-3 | REG-022 jurisdiction not stated in available source slice. | 26020-Package_Requirements.docx, Rotating equipment / compressors, REG-022 row | _CONTEXT.md (no jurisdictional field) | Specification R-9 and Standards; Procedure Step 8 | PROPOSAL: surface to the Owner / EPC Integrator project controls function for jurisdictional confirmation before vendor REG-022 work product is finalized. | TBD |
