# Guidance — DEL-088-05 Vendor Document Turnover Package

## Purpose

The Vendor Document Turnover Package consolidates everything the Package Vendor must hand over so that the EPC Integrator (and ultimately the Owner) can integrate, operate, and maintain the caustic mercaptan treating unit. It is the durable evidence layer that connects vendor engineering, fabrication, and quality records to the project's plant lifecycle. Per the decomposition, this is a Gate 5 deliverable for PKG-088 and is paired with the EPC review-and-acceptance deliverable (DEL-088-06).

## Principles

- **Register before submittal.** A complete, current register is the single index of truth for the package's documentation set. A submittal without a register entry is incomplete.
- **Source-required documents are mandatory.** Items enumerated by 26020-Package_Requirements.docx package heading 41 are not negotiable; missing items leave the package not turned-over.
- **Single ownership, dual review.** The Package Vendor authors and submits; the EPC Integrator reviews for interface and integration fit. Neither side certifies plant-level reliance unilaterally.
- **Traceability over volume.** A small, well-indexed, well-revisioned set is more useful than a large, ambiguous dump.
- **Turnover is a milestone, not a date.** Turnover is reached when the register, submittals, source-required documents, and signed records are all present and consistent.

## Considerations

- **Scope sharpness.** PKG-088 is the caustic mercaptan treating package as defined by the DBM (non-regenerative caustic unit, 20,000 bbl/d C5+ condensate, Merichem or equivalent — DBM line 389). Vendor documents outside that package boundary do not belong here; they belong to the upstream/downstream package's turnover.
- **Source inaccessibility.** The authoritative package-requirements document (26020-Package_Requirements.docx heading 41) is referenced by the decomposition but is not locally accessible to this drafting run. Several content fields (column schema, exact required-document list, language/units rules) are therefore marked TBD. Detailed drafting must reopen that source before issue.
- **Interaction with DEL-088-04.** The Vendor Engineered Equipment Package (DEL-088-04) produces much of the engineering content that flows into this turnover. Coordinate revision codes and document numbering between the two.
- **Interaction with DEL-088-06.** EPC Vendor Package Review and Acceptance is the downstream gate that consumes this turnover. The register and submittals must be in a state that the reviewer can act on (no ambiguity about revision status).
- **Hazardous-service context.** The package handles caustic, mercaptan-bearing C5+ condensate, and DSO/spent-caustic streams (DBM lines 389-400). Material-of-construction certificates, sour-service compliance, and aluminum-prohibition compliance (DBM line 402) are particularly important to retain in the turnover set.

## Trade-offs

- **Early vs. late submittal.** Earlier vendor submittals accelerate EPC integration but increase rework risk if vendor design is still maturing. Late submittals reduce rework but compress EPC review time. The register's revision-history column is the mechanism that lets both modes coexist.
- **Register granularity.** Too coarse (one row per binder) loses traceability; too fine (one row per page) overwhelms reviewers. ASSUMPTION: one row per controlled document number is the right granularity; confirm against project document-control standard.
- **Hardcopy vs. electronic.** The accessible sources do not state a preference. ASSUMPTION: electronic is the working medium; hardcopy needs are TBD.

## Examples

- A typical register row would identify the Merichem (or equivalent) unit P&ID by its vendor document number, give the current revision (e.g., Rev B for IFA), the EPC transmittal reference, and the intended use (IFC, IFR, FOR INFO).
- A typical source-required item would be the vendor's material test reports for caustic-service piping and tanks; storage of these MTRs is essential because aluminum is prohibited in the caustic building (DBM line 402) and material-traceability is the verification trail.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-088-05-01 | Exact list of source-required vendor documents is referenced but not locally accessible. | _REFERENCES.md cites 26020-Package_Requirements.docx heading 41 | No local copy of that .docx content available to this run | Specification REQ-088-05-04; Datasheet "Source-required documentation"; Guidance Principles | Reopen the .docx and enumerate the required documents into Specification before issue. | TBD |
| C-088-05-02 | Objective association (OBJ-002 through OBJ-010) used by _CONTEXT.md is package-grouped, not deliverable-specific. | _CONTEXT.md Supports Objectives | OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC (best-effort) | Datasheet Attributes | Retain as ASSUMPTION until objective-to-deliverable mapping is confirmed at deliverable-ID level. | TBD |
