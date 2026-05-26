# Specification: DEL-076-06 — EPC Vendor Package Review and Acceptance

## Scope

This deliverable specifies the EPC Integrator-led review, integration acceptance, and handoff readiness evaluation for the Lube Oil Supply package (PKG-076) supplied by the Package Vendor. The acceptance is performed against three accepted EPC-side baselines: the EPC Scope of Work (DEL-076-01), the Package Datasheet (DEL-076-02), and the Construction Work Package (DEL-076-03). (Source: `_CONTEXT.md` Scope; DELIVERABLE_REGISTER.csv row DEL-076-06.)

**In scope:**
- Documentary review of vendor-supplied engineering, fabrication, and turnover documentation (against DEL-076-05).
- Integration acceptance against the EPC-defined interfaces enumerated in INTERFACE_REGISTER.csv for PKG-076.
- Handoff readiness check for the physical package supplied by the vendor (DEL-076-04).
- Acceptance and turnover record assembly.

**Out of scope:**
- Package vendor engineering, design, or fabrication (owned by Package Vendor under DEL-076-04 / DEL-076-05). (Source: PACKAGE_REGISTER.csv `ResponsibilityModel`.)
- Authorship of the EPC Scope of Work, Package Datasheet, or Construction Work Package (those are sibling EPC Integrator deliverables). (Source: DELIVERABLE_REGISTER.csv.)
- Package-specific exclusions: TBD; no package-specific exclusions stated in PACKAGE_REGISTER.csv `Exclusions` field.

## Requirements

| ID | Requirement | Source | Notes |
|---|---|---|---|
| R-076-06-01 | The deliverable SHALL produce a vendor document review and comment log covering vendor documentation submitted under DEL-076-05. | ARTIFACT_REGISTER.csv ART-CE37DAAF83; `_CONTEXT.md` Anticipated Artifacts | |
| R-076-06-02 | The deliverable SHALL produce a vendor package acceptance and turnover checklist. | ARTIFACT_REGISTER.csv ART-36208600FC; `_CONTEXT.md` Anticipated Artifacts | |
| R-076-06-03 | The deliverable SHALL include factory/shop test and inspection evidence for the supplied equipment. | ARTIFACT_REGISTER.csv ART-F44CA74291; `_CONTEXT.md` Anticipated Artifacts | Detailed test/inspection requirements are source-specific (`location TBD`, `26020-Package_Requirements.docx` package heading 30). |
| R-076-06-04 | Acceptance SHALL confirm each of the eight EPC-identified interfaces for PKG-076 has been addressed by vendor scope and EPC-side tie-in design: Utility Piping; Drain/Containment; Electrical Power; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Maintenance Access; Structural/Foundations/Supports. | INTERFACE_REGISTER.csv (IFC-B592C2D9F7, IFC-09EA6BEDB8, IFC-4D53A7E70E, IFC-7117284B73, IFC-986D504634, IFC-8C17CDE23B, IFC-6D43DAF029, IFC-ACA2756AA0) | |
| R-076-06-05 | Acceptance SHALL verify the package as constructed/supplied includes the major equipment baseline: P-9240-1 (Cylinder Lube Oil Transfer Pump), P-9250-1 (Crankcase Lube Oil Transfer Pump), horizontal split storage tank (crankcase + compressor packing), electric motor drive, sweet and sour service. | ART-D795C57849 | |
| R-076-06-06 | Acceptance SHALL not approve the package until the responsible EPC Integrator confirms turnover-readiness evidence for handoff to operations/commissioning. | `_CONTEXT.md` Scope ("handoff readiness"); ART-36208600FC | Specific turnover gates: TBD (governed by project-level turnover procedures not in deliverable-local scope). |
| R-076-06-07 | Detailed pass/fail acceptance criteria SHALL be derived from the accepted Scope of Work (DEL-076-01), Package Datasheet (DEL-076-02), and Construction Work Package (DEL-076-03) when those siblings reach an INITIALIZED-or-better state. | DELIVERABLE_REGISTER.csv; `_CONTEXT.md` Scope | ASSUMPTION: cross-deliverable dependency; `_DEPENDENCIES.md` declares no upstream edges at PREPARATION, so this is a semantic dependency surfaced here. |

## Standards

- Source-cited governing standards specific to package acceptance: TBD (`26020-Package_Requirements.docx` package heading 30 not extracted; DBM source citations for clause-level acceptance criteria: location TBD).
- ASSUMPTION: facility-level project execution standards (turnover, QA/QC, factory acceptance test conventions) likely apply per industry practice but no clause-level basis is locally accessible at PREPARATION.

## Verification

| Requirement | Verification Approach |
|---|---|
| R-076-06-01 | Inspection of the completed vendor document review log against the vendor document register (DEL-076-05). |
| R-076-06-02 | Inspection of the completed acceptance and turnover checklist with each line item dispositioned. |
| R-076-06-03 | Document review of factory/shop test and inspection records; witness/hold-point evidence where required (`location TBD`). |
| R-076-06-04 | Cross-check each of the eight INTERFACE_REGISTER rows against vendor-supplied interface evidence and EPC tie-in design. |
| R-076-06-05 | Tagged-equipment cross-check between vendor as-built/as-supplied documentation and ART-D795C57849 equipment list. |
| R-076-06-06 | Sign-off on turnover-readiness statement by the EPC Integrator. |
| R-076-06-07 | Traceability matrix mapping each acceptance line back to its origin in DEL-076-01 / DEL-076-02 / DEL-076-03 once available. |

## Documentation

Required artifacts upon completion (from `_CONTEXT.md` and artifact register):

- Vendor document review log (ART-CE37DAAF83)
- Package acceptance checklist (ART-36208600FC)
- Test/inspection evidence (ART-F44CA74291)
- Turnover evidence (per `_CONTEXT.md` Anticipated Artifacts; specific artifact ID TBD)
