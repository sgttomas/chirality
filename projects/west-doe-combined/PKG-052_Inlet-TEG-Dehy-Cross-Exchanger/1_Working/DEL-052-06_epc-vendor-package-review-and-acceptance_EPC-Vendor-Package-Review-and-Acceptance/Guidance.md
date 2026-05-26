# Guidance — DEL-052-06 EPC Vendor Package Review and Acceptance

## Purpose

This deliverable is the EPC Integrator's record of having reviewed, integrated, and accepted the vendor-engineered PKG-052 (Inlet / TEG Dehy Cross Exchanger E-5718-1) package against the EPC Scope of Work, Package Datasheet, and Construction Work Package. It is framed in the decomposition as an additional Gate 5 deliverable carrying "EPC-integrator review and acceptance evidence" (`DELIVERABLE_REGISTER.csv` notes column).

It exists because PKG-052 is owned across two parties: the Package Vendor owns package engineering/design/documentation/equipment, and the EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, and procurement/construction coordination (`PACKAGE_REGISTER.csv` row PKG-052, Responsibility column). The review/acceptance record is the seam where vendor work crosses into integrator custody.

## Principles

1. **Integration acceptance, not vendor authorship.** The EPC Integrator does not re-author vendor engineering. The review confirms fitness against EPC-side requirements (SOW, Datasheet, CWP) and against source-required vendor documentation. Source: `_CONTEXT.md` Scope; `PACKAGE_REGISTER.csv` Responsibility column.
2. **Trace every acceptance entry.** Each disposition (accept / accept-with-comment / reject) should point back to a specific requirement in DEL-052-01, DEL-052-02, DEL-052-03, or a source clause in `26020-Package_Requirements.docx` package heading 7. ASSUMPTION: this trace discipline aligns with the EPC review/acceptance role declared in `_CONTEXT.md` Scope.
3. **Interface-led review.** Use the PKG-052 interface inventory (`INTERFACE_REGISTER.csv`) as the spine for integration acceptance: each interface type (Process Piping; Utility Piping; Drain / Containment; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports) is a distinct acceptance lane.
4. **Vendor inputs are authoritative for their own scope.** Vendor engineering (DEL-052-04) and vendor documents (DEL-052-05) are the authoritative inputs to review; the reviewer cites them rather than re-deriving them.
5. **Source-grounded acceptance criteria.** Acceptance criteria for factory/shop tests, inspections, and submittals are derived from `26020-Package_Requirements.docx` package heading 7 and from the vendor RFQ (`26020-01-PT-RFQ-16-001-Heat_Ex_ST.docx`). Where those sources are not locally accessible, the criteria remain `TBD` rather than being inferred.

## Considerations

- **Binary sources not yet text-accessible.** The package requirements doc and the interfaces workbook are present as `.docx`/`.xlsx` under `_Sources/`, but their text content is not accessible during this drafting pass. The decomposition snapshot registers (`PACKAGE_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`) carry distilled facts and are used as the immediate accessible authority. Re-running with extracted source slices is expected to sharpen acceptance criteria from `TBD` to concrete numeric/clause requirements.
- **RFQ basis missing.** `PACKAGE_REGISTER.csv` row PKG-052 cites `Bid Docs/Budgetary/26020-01-PT-RFQ-16-001-Heat_Ex_ST.docx` as the Word Source Basis, but that file is not present under `_Sources/`. Acceptance criteria that would normally derive from the RFQ are explicitly TBD.
- **Objective association is heuristic.** The objective list inherited from `_CONTEXT.md` (`OBJ-001`, `OBJ-003`–`OBJ-010`) was assigned by the PACKAGE_HEURISTIC mode at the package level; deliverable-level mapping is best-effort, not source-confirmed.
- **No declared dependencies.** `_DEPENDENCIES.md` records no declared Upstream/Downstream edges. The dependencies implied by the review/acceptance role (DEL-052-01, -02, -03 as authority basis; DEL-052-04, -05 as inputs) are operationally necessary but not formally declared. Surface this when `Dependencies.csv` is generated.
- **One package, one acceptance record.** This deliverable applies only to PKG-052. Equivalent PKG-NNN reviews are separate deliverables and must not be folded into this folder.

## Trade-offs

- **Checklist depth vs. reviewer load.** A line-per-source-requirement checklist is the most defensible acceptance record but is heavy to maintain. A coarser checklist grouped by artifact stream is lighter but weakens traceability. Resolution: prefer line-per-requirement once the source clauses are extracted; until then, keep the checklist organized by the three registered artifact streams (review log, acceptance/turnover checklist, test/inspection evidence) plus the interface inventory.
- **Accept-with-comment vs. reject.** "Accept with comment" is fast but leaks residual risk forward to construction and turnover. Prefer reject-and-resubmit when a comment would otherwise become a punch list item.
- **Factory test reliance vs. site verification.** Heavy reliance on factory/shop test evidence reduces site rework but assumes vendor test scope mirrors integrated facility conditions. Capture the gap explicitly in the turnover record.

## Examples

(None drawn from source — source clauses for example acceptance criteria are not locally text-accessible. TBD: populate with concrete examples once `26020-Package_Requirements.docx` package heading 7 and the vendor RFQ are extracted.)

## Conflict Table (for human ruling)

None at this pass. No conflicts surfaced between accessible sources (decomposition snapshot registers, `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`).
