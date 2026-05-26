# Guidance — DEL-075-05 Vendor Document Turnover Package (PKG-075)

## Purpose

This guidance frames how the Vendor Document Turnover Package is to be assembled, interpreted, and reviewed for PKG-075 (Cryogenic Unit "Deepcut" — 300 MMSCFD sour gas deep-cut propane-plus recovery package using the UltraTEF cryogenic turbo-expansion process). It supports `OBJ-001`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (ASSUMPTION — package-grouping heuristic) by ensuring the EPC Integrator receives a complete, traceable vendor documentation set sufficient for facility integration, operations, regulatory readiness, and long-term turnover for the West Doe Deepcut expansion.

## Principles

1. **Source-driven document list.** The applicable document classes come from `_Sources/26020-Package_Requirements.docx` "Vendor Engineering Deliverables" (package heading 29 — Cryogenic Unit). This skill does not invent new document classes for the PKG-075 turnover.
2. **Discipline filtering, not document invention.** The vendor and EPC reviewer apply the source's discipline tables to mark each line APPLICABLE / N/A with a brief rationale, rather than removing or re-inventing IDs.
3. **EPC Integrator as acceptor, not author.** Per `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv` row 280, the Package Vendor authors; the EPC Integrator reviews via `DEL-075-06`. Acceptance is a human decision.
4. **Traceability over volume.** The Vendor Document Index (`PRQ-009`) is the canonical contents list; every document submitted must appear in it with current revision and status. Volume alone is not acceptance.
5. **Codes and standards stay sourced.** Where the accessible source set does not cite a specific standard clause, the turnover set states the applicable standard and leaves clause-level claims to detailed-design documents.
6. **Sour and cryogenic service governs material traceability.** Material Test Reports / Certificates (`QLT-013`) are non-negotiable for pressure-boundary items in sour and/or cryogenic service.

## Considerations

- **Mechanical / Process discipline center.** The package is identified Mechanical (`PACKAGE_REGISTER.csv` row 52), WBS 01. Process, mechanical equipment, piping, pressure-equipment, relief/flare, and drain/containment document classes dominate the applicable list. Electrical and I&C apply because of motor-driven compressors/expanders, instrumentation, ESD, and F&G.
- **Full interface coverage required.** Per `PACKAGE_REGISTER.csv` row 52, applicable interface types include: Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports. Vendor documents must cover each of these interfaces somewhere in the turnover set.
- **Cryogenic flare and incinerator preliminary.** Per DBM line 2186 and 2294, cryogenic and HP flare rates and mercaptan incinerator rates are preliminary and "to be confirmed during detailed engineering by the flare stack vendor." Relief / flare deliverables in the turnover set must carry this disposition status and be reconciled against the as-built flare design.
- **Regulatory and consultation basis.** The West Doe Deepcut expansion is subject to BC Energy Regulator application and waste-management permitting (DBM SEC near line 3320). Vendor documentation that supports regulatory submissions (e.g., pressure-vessel registration, environmental compliance) must be identifiable and traceable in the index.
- **Turnover gate.** Turnover records (`PRQ-016`, `MEC-023`, `ELE-030`, `QLT-020`, `QLT-021`) are the critical evidence for EPC Integrator acceptance. Plan the FAT/SAT/energization milestones backwards from the acceptance gate (`DEL-075-06`).

## Trade-offs

- **Breadth vs. signal.** A wide vendor document set is more defensible at regulatory and operational reviews, but increases review cost and submittal turnaround. Use the discipline applicability call to keep the set tight while preserving traceability — and note that for a cryogenic process package the applicable set is intentionally broad.
- **Early submittal vs. as-built quality.** Releasing documents early gives the EPC Integrator time to coordinate facility-level integration but creates revisioning churn. The Vendor Document Control Procedure (`DOC-008`) should establish a small number of named milestones (e.g., preliminary, certified-for-construction, as-built) rather than continuous trickle.
- **Standalone vendor IOM vs. integrated turnover book.** A combined `PRQ-016` book is easier for operations to use long-term; per-document standalone files are easier for vendor revisioning. Decide upfront and reflect in `DOC-008`.
- **Vendor-supplied vs. EPC-supplied relief/flare data.** The DBM defers cryogenic and HP flare rates to the flare stack vendor (separate package). PKG-075 vendor relief documents must cite the package contribution to the relief load and be reconcilable against the flare stack vendor's design.

## Examples

- The source's "Vendor Engineering Deliverables" template (heading 29 for Cryogenic Unit) defines the same uniform document set used across all packages; the PKG-075 instantiation simply applies the full mechanical/process/piping/relief/electrical/I&C/civil/F&G applicability profile.
- DBM SEC-01 explicitly identifies the cryogenic package as the C3+ recovery unit using the UltraTEF process with 99+ percent propane recovery; vendor performance documentation (test reports, recovery curves) must trace to this performance basis where applicable.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-075-05-001 | Cryogenic and HP flare rates and mercaptan incinerator rates are stated by DBM as preliminary and to be confirmed by the flare stack vendor during detailed engineering. PKG-075 vendor relief/flare documents will inevitably depend on that downstream basis. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2186, 2294 | `_Sources/26020-Package_Requirements.docx` (relief/flare deliverable rows; clause location TBD) | Specification R-5; Datasheet Conditions; Procedure Step 4 | Carry relief / flare vendor deliverables as PRELIMINARY in the Index until the flare stack vendor's design is accepted; require a reconciliation transmittal before turnover acceptance. | TBD |
| HRR-075-05-002 | The accessible sources do not specify clause-level governing codes (e.g., ASME B31.3, ASME BPVC Section VIII, API 521, CSA Z662) for the cryogenic process package, nor submittal cadence and native-file formats. | `_Sources/26020-Package_Requirements.docx` (codes/standards register location TBD) | None | Specification R-13, R-14; Standards table | Carry as TBD in the turnover specification; require the EPC Integrator to set these in the package PO or in `DEL-075-06` review criteria before vendor mobilization. | TBD |
| HRR-075-05-003 | The "Vendor Engineering Deliverables" list in the source covers all package types uniformly; per-line applicability for a sour cryogenic process package requires human disposition (especially for HVAC, area lighting, drain/containment lines that may overlap with facility-level utility scope). | `_Sources/26020-Package_Requirements.docx` (uniform template) | Package-specific reality of a packaged cryogenic process unit | Specification R-4 through R-8 | The Vendor Document Index for PKG-075 marks each line APPLICABLE / N/A with rationale; EPC Integrator confirms in `DEL-075-06`. | TBD |
| HRR-075-05-004 | Per `_CONTEXT.md` PKG-075 supports OBJ-001, 003, 004, 005, 006, 007, 008, 009, 010; this set was derived via the package-grouping heuristic and not from an explicit deliverable-ID objective map. | `_CONTEXT.md` "Supports Objectives" | `OBJECTIVE_DELIVERABLE_MAP.csv` (per `_REFERENCES.md`) | Datasheet Identification; Guidance Purpose | Carry the objectives list as ASSUMPTION until the explicit objective-to-deliverable map confirms or amends the association. | TBD |
