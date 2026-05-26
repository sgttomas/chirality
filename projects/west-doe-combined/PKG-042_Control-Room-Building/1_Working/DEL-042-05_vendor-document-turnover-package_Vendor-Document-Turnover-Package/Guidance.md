# Guidance: DEL-042-05_vendor-document-turnover-package

## Purpose

The Vendor Document Turnover Package exists so that the Package Vendor's engineering, design, and equipment record for `PKG-042` (Control Room Building) is delivered to the EPC Integrator in a register-controlled, reviewable form that supports facility integration, construction, commissioning, and operations. The deliverable consolidates vendor documents into a single package boundary so that EPC interface, integration, and acceptance reviews (`DEL-042-06`) can be performed against a defined set of vendor records rather than ad-hoc submittals.

## Principles

- **Vendor ownership, EPC review.** The Package Vendor authors and submits the documents; the EPC Integrator reviews for interface, integration, tie-in, constructability, and facility-level fit. Authority and ownership do not change because a document is reviewed.
- **Register-driven turnover.** The vendor document register is the control surface for the turnover package. Items not on the register are not part of the turnover; gaps on the register are explicit and traceable.
- **Source-supported scope.** Vendor document scope is grounded in the DBM mechanical-package deliverable paragraph and the package interface set. New requirements are not invented from decomposition prose when source text is silent.
- **Artifacts versus deliverables.** Individual vendor document rows are artifacts/evidence within this single deliverable, not separate deliverables. The package is the unit of turnover.

## Considerations

- The accessible source set does not contain a PKG-042-specific vendor-document specification. Detailed numbering, submittal workflow, turnover record templates, and acceptance criteria are `TBD` and should be resolved via the project vendor document control specification when accessible.
- The Control Room Building has a broad interface set (eleven facts in `INTERFACE_REGISTER.csv`). Vendor documents that omit any applicable interface create an integration gap that EPC review will surface. Note that `PKG-042` does not carry the "Maintenance Access" interface fact carried by some other building packages; this does not relieve the package of maintenance-access documentation where required by the DBM, but it does mean the workbook does not enumerate it as a discrete interface for this package.
- The DBM mechanical-package deliverable paragraph is written for mechanical packages but is the closest source-text statement of "what must be in a vendor package." Applying it to a Control Room Building package requires judgment: items such as relief/load data and cause-and-effect inputs may not apply, while datasheets, tie-in lists, maintenance access, shipped-loose lists, and the vendor document register itself remain relevant.
- The deliverable feeds `DEL-042-06_epc-vendor-package-review-and-acceptance`; turnover content gaps will propagate to acceptance.

## Trade-offs

- **Broad register vs. focused register.** A broad register increases EPC review burden but reduces the chance of missed integration evidence. A focused register is easier to review but risks omitting documentation that becomes important during construction or commissioning. The bias here is toward a broad, gap-explicit register.
- **Early turnover vs. late turnover.** Early partial turnover allows EPC interface checks during vendor engineering but creates rework if vendor design changes. Late turnover reduces rework but risks discovering interface conflicts after vendor design is fixed. Sequencing is governed by procurement and project schedule, not by this specification.

## Examples

Examples of vendor document categories that are warranted by the DBM mechanical-package deliverable paragraph and applicable to a Control Room Building package:

- Building and equipment datasheets (Package Vendor copies; distinct from EPC `DEL-042-02_package-datasheet`).
- Utility load summary covering electrical, HVAC, lighting, and control-room equipment loads inside the building.
- Field tie-in lists for utility piping, drains/containment, electrical power, grounding/bonding, I&C/control cabling, communications/network, and building HVAC services.
- Operating and design envelopes for the building and its installed equipment, including thermal/HVAC envelopes for control-room equipment.
- Sparing philosophy and shipped-loose item lists.
- Materials and coating basis for the building, raceways, and exposed steel.
- Maintenance access drawings or callouts (even though not listed as a discrete `PKG-042` interface fact; warranted by DBM where relevant).

Categories where no source-supported content is available are recorded as `TBD` in the register, not invented.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-042-05-001 | The DBM mechanical-package deliverable paragraph (`3-25_Comp_and_Liquids_DBM.md` line 617) is written for mechanical packages but `PKG-042` is an Electrical Control Room Building package. Direct one-to-one application of items such as "relief/load data" and "cause-and-effect inputs" may be inappropriate, while other items remain clearly applicable. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617 (mechanical package deliverable paragraph) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` electrical-buildings section referenced by `PACKAGE_REGISTER.csv` row `PKG-042` | Datasheet Attributes; Specification REQ-042-05-004; Guidance Examples | PROPOSAL: apply the DBM paragraph as a minimum baseline filtered to electrical-building applicability; mark non-applicable items as "N/A — not applicable to control room building" rather than `TBD`. | TBD — requires human ruling on which mechanical-package items are non-applicable to a Control Room Building package. |
| HRR-042-05-002 | The accessible source set has no PKG-042 vendor-document detail (numbering scheme, submittal workflow, turnover record format, acceptance criteria). `ART-F6E4C1C060` records this as a "Vendor Documentation Gap." | `ARTIFACT_REGISTER.csv` row `ART-F6E4C1C060` | `_Sources/26020-Package_Requirements.docx` (no accessible PKG-042 match in this run) | Datasheet Attributes (turnover record format, detailed list); Specification Standards (project vendor document control specification); Procedure Steps | PROPOSAL: defer numbering/workflow/format definition to the project vendor document control specification when accessible; keep specification requirements format-neutral until then. | TBD — requires confirmation that a project vendor document control specification exists and is the governing source. |
| HRR-042-05-003 | `OBJECTIVE_DELIVERABLE_MAP.csv` lists eight objectives (`OBJ-002`, `OBJ-004`–`OBJ-010`) supported by this deliverable using a package-grouping pattern. The mapping is package-level, not deliverable-specific. | `_Decomposition/.../OBJECTIVE_DELIVERABLE_MAP.csv` rows for `DEL-042-05` | `_CONTEXT.md` Supports Objectives list | Datasheet Attributes (supported objectives row) | PROPOSAL: treat objective association as `ASSUMPTION (PACKAGE_HEURISTIC)` per `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC` until a deliverable-level objective mapping is published. | TBD — requires human confirmation or refined objective map. |
