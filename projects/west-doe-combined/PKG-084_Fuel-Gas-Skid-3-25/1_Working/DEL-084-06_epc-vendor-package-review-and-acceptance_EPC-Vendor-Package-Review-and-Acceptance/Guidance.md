# Guidance — DEL-084-06 EPC Vendor Package Review and Acceptance

## Purpose

This guidance explains why the EPC Vendor Package Review and Acceptance deliverable exists and how the EPC Integrator should approach reviewing the Fuel Gas Skid 3-25 vendor package. It is the EPC Integrator's evidence that the vendor package conforms with the EPC Scope of Work, Package Datasheet, and Construction Work Package, and that the package is ready for integration handoff (source: _CONTEXT.md; DELIVERABLE_REGISTER.csv row 329).

## Principles

- **Acceptance ≠ certification.** The EPC Integrator records review and acceptance evidence. Final certification of code-regulated items remains with the qualified authority. (ASSUMPTION: aligns with K-AUTH-1 governance posture.)
- **Source-anchored conformance.** Every accepted requirement must trace to an accessible source slice — either the EPC SOW/Package Datasheet/CWP for this package, or the 3-25 DBM where those documents are themselves grounded.
- **Open items remain open.** Unresolved interface items (e.g., emergency buyback fuel gas — see Conflict Table) must be carried as TBD on the acceptance checklist; do not silently resolve them at acceptance time.
- **Integration before isolation.** The fuel-gas skid is part of a shared 03-25/04-25 utility system (3-25_Comp_and_Liquids_DBM.md sec. Utilities; sec. Fuel Gas). Acceptance must explicitly check the package boundary against the 04-25-supplied utility scope.

## Considerations

- **Cross-facility utility coupling.** Fuel gas is supplied primarily through the 04-25 sales-gas splitter with Alliance secondary (DBM sec. Fuel Gas). Acceptance must confirm that the skid's inlet conditions match the 04-25 supply envelope, not just the vendor's nominal design.
- **Demand envelope.** The DBM gives normal 1.382 MMSCFD and design >1.5 MMSCFD for the LP fuel-gas system (DBM sec. Fuel Gas). The LP fuel-gas design flow is itself TBC. Acceptance should verify the vendor's design margin against whichever value DEL-084-02 ultimately publishes.
- **Site-driven design.** The -40 deg C minimum ambient governs exposed equipment, panels, instrumentation, and field devices unless a stricter package-specific basis applies (DBM sec. Site Conditions). Acceptance should specifically inspect winterization, heat tracing, and panel ratings.
- **Hazard basis.** Sweet-gas purge supply touches methyl mercaptan toxicity and odour considerations; a formal hazard review is required before finalizing purge and analyzer maintenance practices (DBM sec. Fuel-Gas Sulphur and Purge Hazard Basis). Acceptance should confirm that this hazard review either exists or is captured as an open item.
- **Sibling deliverable maturity.** DEL-084-01, DEL-084-02, DEL-084-03, DEL-084-04, DEL-084-05 are also currently OPEN (PKG-084 1_Working folder inspection). Acceptance evidence cannot be finalized before those acceptance-basis documents are themselves at INITIALIZED or later maturity.

## Trade-offs

- **Strict conformance vs. interface flexibility.** Where the DBM carries unresolved items (e.g., emergency buyback), strict conformance is impossible. The Integrator should prefer documenting the gap over forcing closure.
- **Vendor scope vs. EPC scope at the skid edge.** Isolation at skid edge for maintenance is a stated requirement at the facility level (DBM sec. Isolation). Acceptance should not absorb work that the SOW assigns outside the vendor's battery limit.
- **Document review depth.** TBD — the depth of vendor document review (e.g., full calculation re-check vs. document-completeness check) is a judgment call that should be governed by DEL-084-01.

## Examples

- An acceptance checklist line for REQ-5 may read: "Vendor inlet rating ≥ 04-25 sales-gas-splitter maximum supply pressure: ACCEPTED — vendor doc VND-XYZ rev 0, Table 3. (Source: DEL-084-02 sec. Interfaces; vendor doc location TBD.)"
- An open-items entry for REQ-9 may read: "Emergency buyback fuel gas applicability: TBD pending human ruling per Conflict Table CONFLICT-1."

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONFLICT-1 | Emergency buyback fuel gas applicability | 3-25_Comp_and_Liquids_DBM.md sec. Fuel Gas (W242510: not required) | 3-25_Comp_and_Liquids_DBM.md sec. Fuel Gas (Process_DBM_fixed: included in 04-25 utility package) | Datasheet (Conditions); Specification REQ-5, REQ-9; Procedure step 5 | PROPOSAL: defer to DEL-084-02 once issued; treat as not required at the 3-25 skid scope absent contrary instruction | TBD |
| CONFLICT-2 | Acceptance-basis document availability | _CONTEXT.md / decomposition expects DEL-084-01/02/03 as acceptance basis | PKG-084 1_Working folder shows DEL-084-01/02/03 currently OPEN (not yet drafted) | All requirements REQ-1 through REQ-4 | PROPOSAL: hold acceptance execution until sibling deliverables reach INITIALIZED at minimum | TBD |
