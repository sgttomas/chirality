# Guidance: DEL-039-06_epc-vendor-package-review-and-acceptance

## Purpose

This guidance supports EPC Integrator review and acceptance of the vendor package for `PKG-039 -- 600V ELECTRICAL BUILDING (850-1)`. The deliverable exists to show that the Package Vendor's engineered equipment package, vendor documentation, test/inspection evidence, and turnover records are ready for facility integration against the EPC Scope of Work, Package Datasheet, and Construction Work Package.

The accepted upstream decomposition identifies this as an EPC Integrator-led acceptance deliverable with Package Vendor input. The primary local evidence is the Gate 7 `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`, and the DBM electrical design basis in `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.

## Principles

1. Treat the EPC anchor documents as the acceptance basis. The Scope of Work, Package Datasheet, and Construction Work Package define what the vendor package must be checked against; vendor material does not replace those EPC anchors.
2. Keep responsibility boundaries explicit. The Package Vendor owns package engineering, design, vendor documentation, and physical equipment. The EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level acceptance evidence.
3. Accept by evidence, not by description. The review log, acceptance checklist, factory/shop test and inspection evidence, and turnover evidence must show what was reviewed, what remains open, and what was accepted by an authorized human reviewer.
4. Use interface rows as a checklist backbone. The twelve `PKG-039` interface rows in `INTERFACE_REGISTER.csv` provide the minimum interface topics that should be represented in acceptance review.
5. Preserve source gaps as `TBD`. Vendor ITP details, vendor document register contents, test thresholds, witness points, and turnover index format are not fully available in the current local source set.

## Considerations

### Vendor Review Log

The vendor document review and comment log (`ART-3910447327`) should be structured so each comment can be traced to an EPC anchor document, a vendor submittal, an interface row, or a DBM electrical basis item. Useful fields include source document, reviewer, comment, vendor response, disposition, closure evidence, and residual risk.

### Acceptance Checklist

The acceptance and turnover checklist (`ART-AA4BFB86C9`) should cover, at minimum:

- package identity and responsibility model from `PACKAGE_REGISTER.csv` row `PKG-039`;
- vendor engineered equipment package and vendor document turnover package linkage from `DELIVERABLE_REGISTER.csv` rows `DEL-039-04` and `DEL-039-05`;
- all `PKG-039` interface rows from `INTERFACE_REGISTER.csv`;
- electrical design basis checks from the DBM source, including prefabricated modular building basis, bottom cable entry, elevated/pile-supported installation, HVAC redundancy, grounding/bonding, cable/raceway basis, lighting basis, and electrical code compliance;
- factory/shop test and inspection evidence (`ART-0156F0196A`), with detailed ITP criteria marked `TBD` until the vendor ITP is received.

### Interface Evidence

Electrical Power, Grounding / Bonding, Building HVAC / Services, Maintenance Access, and Structural / Foundations / Supports have direct DBM support and should receive explicit acceptance checks. Utility Piping, Drain / Containment, Fire & Gas / Safety Systems, and Grading / Site Drainage / Spill Containment are present in the interface register but lack detailed local source slices in the current deliverable package; acceptance language should remain at matrix/checklist level unless the EPC Package Datasheet or vendor documents provide more detail.

### Authority

Agent-produced drafts are not acceptance. Binding acceptance should remain with the EPC Integrator's authorized reviewer. Where this guidance suggests checklist content or disposition logic, it is a drafting aid for human review, not a sign-off.

## Trade-offs

| Topic | Practical trade-off | Recommended handling |
|---|---|---|
| Interface coverage vs. source specificity | The interface register lists twelve topics, but several topics have no detailed local source criteria. | Include all interface rows in the checklist; mark source-specific criteria `TBD` where the EPC Package Datasheet or vendor submittal is needed. |
| Vendor ITP detail vs. acceptance readiness | Factory/shop evidence is expected, but test types and thresholds are vendor-ITP dependent. | Require an evidence record now; defer test thresholds to the vendor ITP and human-reviewed acceptance checklist. |
| Document completeness vs. unresolved comments | Vendor turnover can appear complete while technical comments remain open. | Separate completeness checks from technical acceptance; do not close the acceptance checklist until critical comments are dispositioned. |
| Human sign-off vs. generated draft artifacts | Generated drafts can organize evidence but cannot authorize package acceptance. | Keep all generated content in proposal state until reviewed and signed by the authorized EPC Integrator reviewer. |

## Examples

### Review-Log Entry Pattern

| Field | Example content |
|---|---|
| Source basis | `INTERFACE_REGISTER.csv` row `IFC-9653B84E14`; DBM "Grounding and Bonding" |
| Vendor evidence | Vendor grounding drawing / grounding detail, document number `TBD` |
| Review comment | Confirm two-point connection to facility ground grid and ground well provision at the electrical building. |
| Disposition | `TBD` pending vendor response and reviewer closeout. |

### Acceptance-Checklist Line Pattern

| Checklist topic | Acceptance question | Evidence |
|---|---|---|
| Building structural/foundation interface | Does vendor building evidence support elevated, pile-supported installation and bottom-entry cable routing? | Vendor building GA/foundation interface drawing `TBD`; DBM "Electrical Buildings"; `IFC-E3D0A5A836` |
| Factory/shop test evidence | Are factory/shop tests, inspections, and any witness/hold points complete per vendor ITP? | Vendor ITP and test reports `TBD`; `ART-0156F0196A` |

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-039-06-01 | Acceptance scope includes vendor document turnover under the same review authority as vendor engineered equipment, but source detail for the vendor document register is incomplete. | `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row `DEL-039-06` | `ARTIFACT_REGISTER.csv` row `ART-A64A8A25DC` says detailed vendor-document requirements are not present in current source material. | Specification REQ-039-06-11/13; Procedure steps 3-6 | Treat document-turnover review as in scope, but mark detailed register/checklist criteria `TBD` until vendor document requirements are received. | TBD |
