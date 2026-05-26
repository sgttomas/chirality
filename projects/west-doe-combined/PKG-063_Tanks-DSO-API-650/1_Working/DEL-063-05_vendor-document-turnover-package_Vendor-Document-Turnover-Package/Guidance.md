# Guidance — DEL-063-05 Vendor Document Turnover Package

> Directional guidance for assembling and reviewing the Vendor Document Turnover Package for PKG-063 Tanks, DSO (API 650).

## Purpose

This guidance exists to help the Package Vendor (the responsible party for vendor documentation) and the EPC Integrator (interface/integration reviewer) converge on a complete, traceable, and acceptable turnover package. It frames intent and rationale; binding requirements live in `Specification.md`.

The deliverable closes the documentation thread for PKG-063 across SOW-0209 through SOW-0212 and the nine supported objectives (OBJ-001, OBJ-003..OBJ-010). It is the artifact a downstream owner/operator and the EPC Integrator rely on to demonstrate that the engineered equipment package (`DEL-063-04`) was supplied, fabricated, inspected, and handed over conformably with the source requirements (26020-Package_Requirements.docx heading 18, location TBD) and the EPC handoff basis (`DEL-063-01`, `DEL-063-02`).

Source: `_CONTEXT.md`; DELIVERABLE_REGISTER row 508.

## Principles

1. **Source heading 18 is the registry of truth for required vendor documents.** Until the source slice is accessible, the heading-18 required-document list is TBD; never substitute decomposition prose or generic conventions for the source list. (Source: skill authority hierarchy; `_REFERENCES.md`.)
2. **The register is the spine.** The vendor document register is the single index against which submittals, reviews, and turnover records are tracked. If a document is not in the register, it is not part of the turnover. (ASSUMPTION: industry convention.)
3. **Evidence over assertion.** Each documentation requirement (R-01..R-09) is closed by an artifact, not by narrative claim. (Aligns with `Procedure.md` Records.)
4. **Carry source rows as artifacts.** Per decomposition Notes (row 508), individual source-document table rows remain artifacts/evidence within this deliverable — not separate deliverables.
5. **EPC review is integration-focused.** EPC Integrator review concentrates on interface and integration fitness against `DEL-063-01` and `DEL-063-02`; vendor engineering correctness within the package is the vendor's accountability under `DEL-063-04`.
6. **Status discipline.** Document state transitions (IFR → IFC → IFU → As-Built → Final) should be reflected in the register and supported by transmittal evidence. (ASSUMPTION: industry convention; specific state set TBD per source.)

## Considerations

- **Source access gating.** As of PREPARATION, `_REFERENCES.md` notes that no deliverable-specific source slices have been copied locally. Drafting agents and reviewers must resolve heading-18 access before normative R-01 closure.
- **Acronym ambiguity.** "DSO" in the package name is not explicitly expanded in the accessible decomposition; "Diesel Service Oil" is an inference. Service category may change inspection/testing requirements (e.g., cleanliness, coating); confirm before finalizing.
- **API 650 scope.** API 650 governs welded atmospheric tanks for oil storage; for non-oil services or pressurized configurations, alternative codes may apply. Confirm tank service and design conditions against `DEL-063-02` Package Datasheet before relying on R-08.
- **EPC handoff coupling.** Vendor submittals draw their requirements partly from `DEL-063-01` (SOW) and `DEL-063-02` (Datasheet). Changes upstream may invalidate already-submitted vendor documents; revision-control discipline (R-09) is the mitigation.
- **Downstream consumer.** `DEL-063-06_epc-vendor-package-review-and-acceptance` consumes this deliverable; the EPC review log and acceptance checklist there should reference register entries from here by document number and revision.

## Trade-offs

| Trade-off | Option A | Option B | Notes |
|---|---|---|---|
| Register granularity | Coarse (one row per document) | Fine (one row per submittal/transmittal) | Fine granularity better supports R-05 (turnover record traceability) at the cost of register size. |
| Source-row capture | Capture every source vendor-document row as a separate artifact | Capture only those rows for which the vendor produced an artifact | Decomposition Notes lean toward "as artifacts where available" — Option B. |
| Review timing | Review every submittal individually | Review on milestone batches | Batch review (Option B) reduces EPC integrator overhead; individual review (Option A) shortens defect feedback. ASSUMPTION until project process is confirmed. |
| Conformance evidence assembly | Aggregate into a single conformance index | Leave with original submittals | A single index simplifies R-08 verification; original-attached approach better preserves provenance. |

## Examples

- *(Examples deferred.)* Concrete examples for register row layout, transmittal log format, and turnover acceptance form depend on the source heading-18 prescription and on project-level documentation standards not present in the accessible reference set. Mark TBD; populate from source when accessible.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-01 | Heading-18 source slice not locally accessible; R-01/R-02 substance cannot be source-grounded | `_REFERENCES.md` "Missing / Deferred References" | Skill authority hierarchy (sources are authority #1) | Datasheet Attributes; Specification R-01, R-02, R-09; Procedure Steps S-02, S-03 | Defer R-01/R-02 finalization until source slice is extracted into `_Sources` as text | TBD |
| C-02 | DSO acronym is not explicitly expanded in accessible decomposition | DELIVERABLE_REGISTER row 508 PackageName ("Tanks, DSO (API 650)") | n/a (no second source) | Datasheet Conditions; Guidance Considerations | Treat as ASSUMPTION ("Diesel Service Oil"); confirm at human review | TBD |
| C-03 | Governing tank code (API 650) inferred only from package name, not from a read source clause | DELIVERABLE_REGISTER row 508 PackageName | n/a | Specification Standards; R-08 | Treat API 650 as the working assumption pending source confirmation in `DEL-063-02` Package Datasheet | TBD |
