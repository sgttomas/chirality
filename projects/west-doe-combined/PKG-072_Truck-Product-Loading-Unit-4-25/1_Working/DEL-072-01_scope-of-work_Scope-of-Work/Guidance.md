# Guidance — DEL-072-01 Scope of Work

## Purpose

This Scope of Work is the EPC Integrator's anchor statement of what PKG-072 (Truck Product Loading Unit 4-25) is, what is included, what is excluded, and how the package fits into the wider West Doe Deep Cut Facility. It is the Gate 5 EPC anchor deliverable from which the Package Datasheet, Construction Work Package, vendor engineered package, vendor document turnover package, and EPC review/acceptance deliverables derive. Source: DELIVERABLE_REGISTER.csv row 558 Notes; PACKAGE_REGISTER.csv row 99.

## Principles

1. **Source fidelity over convention.** Package identity, equipment list, function statement, conditions, and exclusions must match the workbook row 99 and `26020-Package_Requirements.docx` package heading 26 text exactly. Where the source uses TBD, this Scope of Work uses TBD; values are not interpolated. Source: PACKAGE_REGISTER.csv row 99; SCOPE_LEDGER.csv SOW-0246/0247/0248.
2. **Vendor/EPC responsibility split is non-negotiable.** Package Vendor owns engineering, design, vendor documentation, and the physical equipment package. EPC Integrator owns integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. This split flows from OBJ-004 and PACKAGE_REGISTER.csv row 99 ResponsibilityModel and must be preserved verbatim in sibling deliverables.
3. **Interfaces are the EPC integration surface.** The eleven applicable interface types in PACKAGE_REGISTER.csv row 99 (Process Piping, Drain/Containment, Electrical Power, Grounding/Bonding, Area/Exterior Lighting, I&C/Control Cabling, Building HVAC/Services, Fire & Gas/Safety Systems, Grading/Site Drainage/Spill Containment, Structural/Foundations/Supports, Product Loading) are the contract for what the EPC Integrator must engineer around the vendor package; they should not be expanded or trimmed without traceable rationale.
4. **Open items are visible, not buried.** Final Flow, MAWP, and heater capacity are TBD in the source (SOW-0247, SOW-0248) and must remain visible as open items in downstream deliverables; OBJ-010 makes controlled open-item closure a handoff success condition.

## Considerations

- **Facility context.** The package serves the West Doe Deep Cut Facility low-pressure fuel gas system (SCOPE_LEDGER.csv SOW-0246). OBJ-001 establishes the 04-25 Deepcut facility scope that this package supports. Source: OBJECTIVE_REGISTER.csv row OBJ-001.
- **Sour service and safety.** OBJ-009 carries sour-service safety, relief, fire/gas, shutdown, environmental, and regulatory requirements into package scopes; this Scope of Work should not assume these are someone else's problem. (Specific clause-level requirements are TBD pending source slice access to DBM SEC-09/SEC-14/SEC-15.)
- **Electrical infrastructure.** The heater driver is a 600 V SCR control panel located in the electrical building (SCOPE_LEDGER.csv SOW-0247, SOW-0248), aligning with OBJ-005 (facility electrical basis including transformers, switchgear, MCC/VFD/UPS). The EPC Integrator owns the electrical building tie-in.
- **Controls and instrumentation.** OBJ-006 requires controls, instrumentation, fire/gas, and shutdown integration across EPC/vendor boundaries; package-vendor control system scope and signal lists belong in the Package Datasheet, not this Scope of Work.
- **By-others items.** Shipping, installation, tie-in piping, and electrical tie-in are explicitly "by others" (SCOPE_LEDGER.csv SOW-0248). The EPC Integrator picks these up; this should be stated, not assumed.
- **Commercial accountability.** OBJ-003 preserves commercial stream disposition and metering accountability across boundaries; for a fuel gas heater/scrubber skid, commercial metering exposure is limited but the integration narrative should explicitly state any metering interface or its absence (currently TBD).

## Trade-offs

- **Wording detail vs. document control.** The source slice in `26020-Package_Requirements.docx` heading 26 has not yet been extracted into the deliverable folder. Drafting from the SCOPE_LEDGER summary preserves traceability but loses some source nuance (e.g., heater capacity rationale, scrubber sizing notes). Trade-off: accept summary-level fidelity now and tighten when the source slice is extracted; do not invent the missing nuance.
- **Vendor sizing latitude.** SOW-0247 instructs that "Vendor to design" the fuel gas scrubber using the k-factor cap. The Scope of Work must carry the cap as a hard constraint but should not preempt the vendor's sizing methodology. Source: SCOPE_LEDGER.csv SOW-0247.
- **Heater capacity TBD.** Heater capacity is TBD pending design flow finalization. The Scope of Work should hold this as TBD rather than freeze a placeholder, since OBJ-010 makes controlled open-item closure a Gate 5 condition.

## Examples

- **Package function statement (verbatim from source):** "Skid will serve the low-pressure fuel gas system for the West Doe Deep Cut Facility." Source: SCOPE_LEDGER.csv SOW-0246.
- **Responsibility statement (verbatim from source):** "Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration." Source: PACKAGE_REGISTER.csv row 99 ResponsibilityModel.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted Sections | Proposed Authority (PROPOSAL) | Human Ruling |
|---|---|---|---|---|---|---|
| C-072-01-01 | Package name disagreement: PACKAGE_REGISTER.csv row 99 PackageName is "Truck Product Loading Unit 4-25", but the same row's PackageNameSource26020 field carries "26020-01-PT-23-001 - Condensate Truck Loading Stations" — a different package identity. The deliverable folder, `_CONTEXT.md`, and SCOPE_LEDGER rows all use "Truck Product Loading Unit 4-25" describing a Low Pressure Fuel Gas Skid. | PACKAGE_REGISTER.csv row 99, PackageName + PackageNameSourceWorkbook (Truck Product Loading Unit 4-25 / low-pressure fuel gas package) | PACKAGE_REGISTER.csv row 99, PackageNameSource26020 column (Condensate Truck Loading Stations / 26020-01-PT-23-001) | Datasheet Identification; Specification Scope; this Guidance | PROPOSAL: treat the workbook row 99 name "Truck Product Loading Unit 4-25" and the SCOPE_LEDGER SOW-0246/47/48 process content (Low Pressure Fuel Gas Skid) as authoritative; flag the "Condensate Truck Loading Stations" reference as a likely cross-reference to a different package row that needs human confirmation against `26020-Package_Requirements.docx`. | TBD |
| C-072-01-02 | Source slice not deliverable-local: `_REFERENCES.md` lists `26020-Package_Requirements.docx` heading 26 as the source basis but states no deliverable-specific source slices were copied during PREPARATION; the Word source is only globally accessible under `_Sources/`. | `_REFERENCES.md` Missing/Deferred References | `_Sources/26020-Package_Requirements.docx` exists at the project root | All four documents (location TBD markers) | PROPOSAL: extract the package heading 26 source slice into a deliverable-local reference file as a follow-up TASK so future drafts can cite specific source location, not just document-level reference. | TBD |
