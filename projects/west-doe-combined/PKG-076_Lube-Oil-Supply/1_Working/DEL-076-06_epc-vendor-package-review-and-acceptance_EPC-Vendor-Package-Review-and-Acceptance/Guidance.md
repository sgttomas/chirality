# Guidance: DEL-076-06 — EPC Vendor Package Review and Acceptance

## Purpose

This deliverable exists to provide the EPC Integrator's documented review, integration acceptance, and handoff-readiness disposition for the vendor-supplied Lube Oil Supply package (PKG-076). It is the evidence record that confirms the vendor package — engineered, supplied, and documented by the Package Vendor under DEL-076-04 and DEL-076-05 — meets the EPC-side baselines defined in DEL-076-01 (Scope of Work), DEL-076-02 (Package Datasheet), and DEL-076-03 (Construction Work Package), and is integration-ready for the West Doe Deepcut facility. (Source: `_CONTEXT.md` Scope; DELIVERABLE_REGISTER.csv Notes column for DEL-076-06.)

## Principles

- **EPC owns acceptance; Vendor owns supply.** The responsibility split is normative: the Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; the EPC Integrator owns integration into the functional process facility (interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration). (Source: PACKAGE_REGISTER.csv `ResponsibilityModel`.)
- **Acceptance derives from accepted baselines, not from the vendor's own claims.** Pass/fail criteria flow from the EPC Scope of Work, Package Datasheet, and Construction Work Package, which are sibling deliverables.
- **Interfaces are the primary integration surface.** PKG-076 declares eight active interface types in the workbook; each must have an acceptance disposition.
- **Source fidelity over convenience.** Where detailed acceptance criteria are not locally machine-readable (the `.docx` package requirements heading and DBM source slices were not extracted at PREPARATION), prefer `TBD` over invention.

## Considerations

- **Cross-deliverable dependency on siblings.** `_DEPENDENCIES.md` declares no upstream edges at PREPARATION, but functionally this deliverable cannot reach acceptance until DEL-076-01, DEL-076-02, DEL-076-03, DEL-076-04, and DEL-076-05 are sufficiently mature. This is captured here as guidance, not as a declared dependency.
- **Two-actor coordination.** The deliverable is led by the EPC Integrator with Package Vendor input (per `_CONTEXT.md` ResponsibleParty); the acceptance log and checklist therefore have two-actor input fields.
- **Sweet and sour service.** Material/seal selection scrutiny during acceptance should reflect the declared sweet+sour service for the lube oils (ART-D795C57849).
- **Tagged equipment specificity.** The equipment baseline is concretely tagged (P-9240-1, P-9250-1, horizontal split storage tank); acceptance evidence should reference these tag numbers explicitly.
- **Eight named interface types** form an interface acceptance matrix. Treat absence of evidence for any one as an open acceptance item, not as silent pass.

## Trade-offs

- **Documentary-only acceptance vs. witnessed test acceptance.** Documentary review (review log + checklist) is always required; the level of witnessed factory/shop test and inspection coverage is source-specific (`location TBD`). Heavier witness coverage increases assurance but extends schedule.
- **Acceptance scope breadth.** Limiting acceptance strictly to the eight declared interfaces simplifies the matrix but may miss integration risks not captured by interface types alone (e.g., commissioning sequence, spare parts logistics). Broader inclusion adds rigor but blurs the boundary with adjacent EPC packages.
- **Conditional acceptance.** Accepting the package with open items vs. holding acceptance until all items close trades schedule predictability against turnover risk; the choice is project-policy-driven (TBD).

## Examples

Examples drawn from the source set: TBD (`26020-Package_Requirements.docx` package heading 30 not extracted; DBM-Deepcut sections relevant to acceptance: `location TBD`).
