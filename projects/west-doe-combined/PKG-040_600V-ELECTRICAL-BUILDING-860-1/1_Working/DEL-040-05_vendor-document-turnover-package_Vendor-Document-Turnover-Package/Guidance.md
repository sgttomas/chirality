# Guidance: DEL-040-05_vendor-document-turnover-package

## Purpose

The Vendor Document Turnover Package exists so that the Package Vendor's engineering, design, and equipment record for `PKG-040` (600V ELECTRICAL BUILDING, 860-1 — "600V General Area / Tank Farm Electrical Building" per DBM-Deepcut) is delivered to the EPC Integrator in a register-controlled, reviewable form that supports facility integration, construction, commissioning, and operations. The deliverable consolidates vendor documents into a single package boundary so that EPC interface, integration, and acceptance reviews (`DEL-040-06`) can be performed against a defined set of vendor records rather than ad-hoc submittals.

## Principles

- **Vendor ownership, EPC review.** The Package Vendor authors and submits the documents; the EPC Integrator reviews for interface, integration, tie-in, constructability, and facility-level fit. Authority and ownership do not change because a document is reviewed.
- **Register-driven turnover.** The vendor document register is the control surface for the turnover package. Items not on the register are not part of the turnover; gaps on the register are explicit and traceable.
- **Source-supported scope.** Vendor document scope is grounded in the DBM-Deepcut SEC-12 Electrical Basis and the package interface set. New requirements are not invented from decomposition prose when source text is silent.
- **Code-anchored compliance.** Electrical equipment, ratings, and installation provisions trace back to CSA C22.1-21 and the project electrical specifications listed in DBM Table 12-1.
- **Artifacts versus deliverables.** Individual vendor document rows are artifacts/evidence within this single deliverable, not separate deliverables. The package is the unit of turnover.

## Considerations

- The accessible source set does not contain a PKG-040-specific vendor-document specification. Detailed numbering, submittal workflow, turnover record templates, and acceptance criteria are `TBD` and should be resolved via the project vendor-document control specification when accessible.
- The 600V Electrical Building has a broad interface set (twelve facts in `INTERFACE_REGISTER.csv`). Vendor documents that omit any applicable interface create an integration gap that EPC review will surface.
- SEC-12 Electrical Basis is the closest source-text statement of the scope vendor documentation must cover for an electrical building package. It enumerates discipline scope (power distribution, standby power, electrical buildings, grounding/bonding, cable/raceway, lighting/receptacles, heat tracing, building heaters, cathodic protection interfaces), governing codes, project electrical specifications (Table 12-1), and required studies. Vendor documentation should evidence each applicable item.
- Several DBM-Deepcut electrical-design parameters (standby generator sizing, transfer-switch ratings, paralleling provisions, load-shedding/sequencing, incoming-power metering and protection split) are explicitly `TBD` in source; vendor documentation cannot pre-resolve them and should reflect the same `TBD` until project electrical studies close them.
- The deliverable feeds `DEL-040-06_epc-vendor-package-review-and-acceptance`; turnover content gaps will propagate to acceptance.

## Trade-offs

- **Broad register vs. focused register.** A broad register increases EPC review burden but reduces the chance of missed integration evidence. A focused register is easier to review but risks omitting documentation that becomes important during construction or commissioning. The bias here is toward a broad, gap-explicit register.
- **Early turnover vs. late turnover.** Early partial turnover allows EPC interface checks during vendor engineering but creates rework if vendor design changes. Late turnover reduces rework but risks discovering interface conflicts after vendor design is fixed. Sequencing is governed by procurement and project schedule, not by this specification.
- **Pre-study vs. post-study scope freeze.** Some vendor documents (equipment ratings, protection settings, arc-flash labels) depend on completed electrical studies. Freezing vendor scope before studies close risks rework; deferring risks late turnover. The default disposition is to mark study-dependent items as `TBD` and resolve under change control once studies are accepted.

## Examples

Examples of vendor document categories warranted by SEC-12 Electrical Basis and applicable to a 600V General Area / Tank Farm Electrical Building:

- Building and equipment datasheets (Package Vendor copies; distinct from EPC `DEL-040-02_package-datasheet`).
- 600V MCC, distribution, and transformer datasheets and outline drawings.
- UPS datasheet and battery/charger details (if installed in this building).
- Area-classification basis and equipment ratings for the building envelope and any forced-ventilation provisions.
- Load list, short-circuit, coordination, arc-flash, and load-flow study inputs as required by SEC-12 electrical studies.
- Grounding and bonding details supporting building tie-in to the plant ground grid.
- Cable and raceway schedules, including I&C / control cabling and communications/network cabling routed through the building.
- Lighting, receptacle, and electric heat tracing details (including building exterior lighting where relevant to the package boundary).
- Electric building heater and HVAC coordination data (per DBM building-HVAC basis).
- Maintenance access drawings or callouts; shipped-loose item lists; materials and coating basis for the building, raceways, and exposed steel.
- Compliance evidence for CSA C22.1-21 and ELC-QAS-000003-001 ("Electrical Requirements for Packaged Equipment").

Categories where no source-supported content is available are recorded as `TBD` in the register, not invented.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-040-05-001 | The DBM-Deepcut SEC-12 Electrical Basis enumerates the discipline scope and governing specifications for electrical packages but does not itemize a "vendor document deliverable list" the way mechanical packages are itemized. Deriving a vendor-document register from SEC-12 requires interpretive mapping from scope/specifications/studies to per-document content. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-12 §"Discipline Scope" and §"Governing Codes, Standards, Specifications, and Studies" | DBM-Comp_and_Liquids mechanical-package deliverable paragraph (used in mechanical-package siblings) | Datasheet Attributes (Turnover content basis); Specification REQ-040-05-004; Guidance Examples | PROPOSAL: use SEC-12 discipline scope + Table 12-1 specifications + electrical studies table as the minimum baseline for the vendor document register; defer per-document content/format to ELC-QAS-000003-001 and the project vendor document control specification when accessible. | TBD — requires human ruling on whether SEC-12 is the correct minimum baseline for electrical-package vendor documentation in the absence of a mechanical-equivalent paragraph. |
| HRR-040-05-002 | The accessible source set has no PKG-040 vendor-document detail (numbering scheme, submittal workflow, turnover record format, acceptance criteria). `ART-EF224E6F34` records this as a "Vendor Documentation Gap." | `ARTIFACT_REGISTER.csv` row `ART-EF224E6F34` | `_Sources/26020-Package_Requirements.docx` (no accessible PKG-040 match in this run) | Datasheet Attributes (turnover record format, detailed list); Specification Standards (project vendor document control specification); Procedure Steps | PROPOSAL: defer numbering/workflow/format definition to the project vendor document control specification (and to ELC-QAS-000003-001 for packaged-equipment electrical content) when accessible; keep specification requirements format-neutral until then. | TBD — requires confirmation that a project vendor document control specification exists and is the governing source. |
| HRR-040-05-003 | `OBJECTIVE_DELIVERABLE_MAP.csv` lists eight objectives (`OBJ-001`, `OBJ-004`–`OBJ-010`) supported by this deliverable using a package-grouping pattern. The mapping is package-level, not deliverable-specific. | `_Decomposition/.../OBJECTIVE_DELIVERABLE_MAP.csv` rows for `DEL-040-05` | `_CONTEXT.md` Supports Objectives list | Datasheet Attributes (supported objectives row) | PROPOSAL: treat objective association as `ASSUMPTION (PACKAGE_HEURISTIC)` per `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC` until a deliverable-level objective mapping is published. | TBD — requires human confirmation or refined objective map. |
| HRR-040-05-004 | Several electrical scope parameters (standby generator sizing, transfer switch ratings, paralleling, load-shedding/sequencing, incoming-power metering and protection coordination split) are explicitly `TBD` in DBM-Deepcut SEC-12 pending electrical studies and TOU standard confirmation. Some vendor documentation depends on these. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §"Standby Power" (line 2945); §"Power System" (line 2927) | Vendor document categories listed under Examples | Specification REQ-040-05-004, REQ-040-05-006; Procedure Step "Resolve gaps and TBDs" | PROPOSAL: hold study-dependent vendor documents as `TBD` in the register; release under change control after the relevant electrical study or TOU standard is accepted. | TBD — requires confirmation of the change-control mechanism that will release these items. |
