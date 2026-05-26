# Guidance: DEL-045-01_scope-of-work — Scope of Work

## Purpose

This deliverable exists so that the EPC Integrator can establish a single, source-grounded statement of what PKG-045 "Instrumentation (outside of Mechanical Packages only)" contains, who is responsible for it, where its boundaries lie, and how it integrates into the West Doe facility. It is the Gate 5 EPC anchor for the package and the upstream basis for the Package Datasheet (DEL-045-02), the Construction Work Package (DEL-045-03), and the EPC/Discipline Production Package (DEL-045-04). [Source: DELIVERABLE_REGISTER.csv; ARTIFACT_REGISTER.csv]

## Principles

- **Plug-n-play package philosophy.** Per the Gate 6 disposition recorded on every active interface for PKG-045, instrumentation field supports, power, and communications are included in each package scope as appropriate. This applies even where the workbook did not originally tick these marks, because the package philosophy assumes the package carries what it needs. [Source: INTERFACE_REGISTER.csv]
- **Outside-of-Mechanical-Packages framing.** The package title itself draws the primary boundary: instrumentation that is inside a vendor mechanical package's boundary is not in this scope. The Scope of Work must make that exclusion explicit so downstream production work does not redundantly engineer in-package instruments. [Source: PACKAGE_REGISTER.csv (package name)]
- **Source fidelity over convention.** Tags, equipment text, exclusions, and interfaces are recorded from accessible sources; absent source support, items are TBD rather than inferred from generic instrumentation practice. [Source: docs/CONTRACT.md K-PROV-1; this skill's authority hierarchy]
- **Decomposition routes; sources determine content.** The decomposition register tells us this deliverable must exist and what artifacts it owns; the DBM and workbook tell us what the deliverable must say. Do not promote decomposition narrative wording to requirement language. [Source: skills/four-documents/SKILL.md Authority hierarchy]

## Considerations

- **Instrument-air interface is dispositioned.** SCA-006 supplies instrument air to 03-25 from 04-25. The Scope of Work should not include a 03-25 instrument-air compressor controls scope; the 03-25 instrument-air interface (393 SCFM TBC; combined 1,113 SCFM TBC) is carried as a monitored interface item. [Source: 3-25_Comp_and_Liquids_DBM.md]
- **-40 deg C site basis.** Exposed instrumentation, control panels, and field devices in scope must be qualified for -40 deg C unless a more severe process/vendor condition governs. The Scope of Work should highlight this as a package-wide environmental driver. [Source: 3-25_Comp_and_Liquids_DBM.md]
- **Power-and-control separation is project-wide.** The DBM imposes electrical/control circuit separation at 13.8 kV / 4,160 V / 600 V. The Scope should reference this rather than redefining it. [Source: 3-25_Comp_and_Liquids_DBM.md]
- **Responsibility split is source-dependent.** The package register notes "EPC Integrator or discipline subcontractor responsibility is source-dependent; no separate vendor-package ownership model is inferred." The Scope of Work should record EPC Integrator responsibility and flag any discipline-subcontractor handoff as a source-supported addition, not a default. [Source: PACKAGE_REGISTER.csv]
- **Detailed major-equipment text is thin.** The DBM addresses 03-25 instrumentation primarily at the utility-interface level (instrument air, electrical, controls separation). The full instrument-by-instrument list for "outside-of-mechanical-packages" scope is not present in the source slice currently locally accessible and is TBD. [Source: 3-25_Comp_and_Liquids_DBM.md; Workbook row 47 location TBD]

## Trade-offs

- **Breadth vs. source-fidelity.** A traditional EPC Scope of Work would enumerate every loose instrument and field device. With only DBM-level source slices locally accessible, this Scope of Work trades enumeration breadth for fidelity: tagged-equipment content is TBD pending the workbook source slice, and Package Datasheet (DEL-045-02) carries the interface-fact evidence. The trade is conservative and reversible: once the workbook row 47 slice is local, the tagged equipment list can be filled without rework.
- **Carrying instrumentation into the package vs. discipline production.** The plug-n-play disposition pulls field supports, power, and communications into this package. The trade-off is that DEL-045-04 (Discipline Production Package) becomes thinner; this is acknowledged in the decomposition note that "Detailed non-vendor package deliverable requirements are source-limited and remain open for Gate 5 disposition."
- **Strict exclusion of vendor-package instrumentation.** Excluding instruments inside vendor mechanical packages avoids double-engineering, but creates a coordination obligation: each vendor mechanical package's boundary must be checked so no instrument falls through the seam. The Scope of Work should call this out.

## Examples

- **Boundary example — Process Piping interface (IFC-33F8A9F366).** Instrumentation installed on process piping outside vendor mechanical packages (e.g., loose-installed flow elements, pressure taps, thermowells on inter-package piping) is in PKG-045 scope; instrumentation pre-installed inside a vendor package's skid boundary is excluded. Field supports, power, and comms for the in-scope instruments are included per the Gate 6 disposition. [Source: INTERFACE_REGISTER.csv]
- **Boundary example — Instrument Air interface.** The 03-25 instrument-air header originating from 04-25 is the supply boundary. Take-offs to in-scope instruments are inside PKG-045; the 04-25 compressor scope is outside. [Source: 3-25_Comp_and_Liquids_DBM.md]

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFLCT-045-01-01 | INTERFACE_REGISTER notes "Field supports, power, and comms not marked unless confirmed by package scope" while Gate 6 disposition on the same row states these are included per plug-n-play philosophy. | INTERFACE_REGISTER.csv (original note) | INTERFACE_REGISTER.csv (Gate 6 disposition note) | Specification R-045-01-06; Guidance Principles | PROPOSAL: Gate 6 disposition supersedes the original mark; treat as included unless a specific package-scope statement excludes. | TBD |
| CFLCT-045-01-02 | Decomposition narrative says the deliverable shall cover "tagged equipment" but the locally accessible source slices do not enumerate tagged instruments for outside-of-mechanical-packages scope. | DELIVERABLE_REGISTER.csv (scope text) | 3-25_Comp_and_Liquids_DBM.md (no instrument tag list); Workbook row 47 (slice not local) | Datasheet Construction; Specification R-045-01-02 | PROPOSAL: keep R-045-01-02 normative and carry tagged-equipment content as TBD until the workbook source slice is brought local. | TBD |
| CFLCT-045-01-03 | Responsibility: DELIVERABLE_REGISTER.csv assigns "EPC Integrator" while PACKAGE_REGISTER.csv carries "responsibility is source-dependent; no separate vendor-package ownership model is inferred." | DELIVERABLE_REGISTER.csv | PACKAGE_REGISTER.csv | Datasheet Identification; Specification R-045-01-04 | PROPOSAL: record EPC Integrator as the responsible party and flag any discipline-subcontractor handoff only when source-supported. | TBD |
