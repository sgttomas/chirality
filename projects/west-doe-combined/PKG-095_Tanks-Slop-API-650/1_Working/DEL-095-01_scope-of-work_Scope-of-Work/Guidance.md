# Guidance — DEL-095-01 Scope of Work (PKG-095 Tanks, Slop (API 650))

## Purpose

This Scope of Work is the EPC Integrator's anchoring statement of *what the package is and how it integrates into the facility*. It is the upstream deliverable that the Package Datasheet, Construction Work Package, vendor production unit, vendor document turnover, and EPC review/acceptance deliverables for `PKG-095` all consume (per `DELIVERABLE_REGISTER.csv`). Getting identity, function, boundary, responsibility, and interface set correct here prevents downstream rework when the vendor receives the technical handoff.

Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`; package note "Mandatory Gate 5 EPC anchor deliverable defined by user instruction".

## Principles

1. **Vendor owns the package; EPC owns the integration.** Package engineering, design, vendor documentation, and equipment supply belong to the Package Vendor. Interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration belong to the EPC Integrator. This split is the controlling responsibility model for `PKG-095`. Source: `PACKAGE_REGISTER.csv` ResponsibilityModel.
2. **Source-anchored content; no invention.** Every non-trivial statement should cite Workbook Packages row 91, `26020-Package_Requirements.docx` package heading 47, the 3-25 Comp_and_Liquids DBM, or another locally accessible source slice. Where a value is not in an accessible slice, mark `TBD` with `location TBD` rather than inferring it. Source: SKILL `four-documents` source-grounding rule.
3. **Interface set is exhaustive at the package boundary.** The nine interface types in `INTERFACE_REGISTER.csv` for `PKG-095` form the integration surface. Omitting any of them in the SOW will create a hidden EPC scope item downstream. Source: `INTERFACE_REGISTER.csv`.
4. **Slop service is segregation-driven.** The package exists to segregate off-spec or contaminated hydrocarbon liquids from on-spec condensate product. Slop sources are diverse (off-spec condensate, tank drains, KO drum pump-out, VRU/scrubber liquids, treating-unit drains). The SOW must preserve the open-item status of the final source list, disposition path, and design basis. Source: `SCOPE_LEDGER.csv` SOW-0214/0216.
5. **API 650 modified — the "modified" word matters.** Source labels the tank as API 650 *modified atmospheric*. The specific deviations (appendices, design temperature, internal lining, foundation rules) are not in locally accessible slices and must remain `TBD` rather than be assumed to standard API 650 base scope. Source: `SCOPE_LEDGER.csv` SOW-0215; `DELIVERABLE_REGISTER.csv` PackageName.

## Considerations

- **Tag preservation, with provisional caveat.** SOW-0215 names the tank as "likely `TK-9130-2`". Carry the tag explicitly with an ASSUMPTION label so downstream P&ID and datasheet work tracks the provisional status; confirm with process/vendor before promoting it to firm.
- **Cathodic protection vs. grounding/bonding.** `INTERFACE_REGISTER.csv` for `PKG-095` lists both Cathodic Protection and Grounding / Bonding as separate interfaces. For atmospheric tanks on concrete or earthen foundations, ownership of CP system (anodes, rectifier, reference cells) vs. tank grounding (lightning protection, static dissipation, electrical bonding) is a frequent ambiguity. Resolve in Datasheet/Construction Work Package; capture as Conflict ID `CONF-095-01-03` below.
- **Slop disposition: truck-out, recycle, or both.** SOW-0215 mentions "drain/recycle/truck-out systems" as a class; the actual disposition path (which sources route to recycle vs. truck-out, and what loading provisions are required) is an open process item per SOW-0216. The SOW must not pre-commit a path the process basis has not confirmed.
- **No package-folder brief.md/DOCX/PDF source.** `PACKAGE_REGISTER.csv` SourceRefRaw explicitly records that no package-folder brief.md, DOCX, or PDF scope source was found for `PKG-095`. The Word Source Basis is therefore "PE definition of slop service plus 3-25 DBM/package-structure analog". This raises the burden on `26020-Package_Requirements.docx` heading 47 extraction for downstream datasheet work.
- **Spill containment is an EPC scope item.** The Grading / Site Drainage / Spill Containment interface puts secondary containment volume, slope, and drainage outside the vendor package boundary. The SOW must explicitly assign this to the EPC Integrator scope so it is not lost in handoff.

## Trade-offs

- **Specificity vs. source coverage.** The locally accessible source slices (workbook row, scope ledger, package register, interface register) describe identity, function, equipment list, responsibility, and interface set, but do not provide clause-level design conditions, tank sizing, materials, or API 650 modification scope. SOW content should be specific where source supports it and explicitly `TBD` (with `location TBD`) elsewhere. Pushing more detail into the SOW than source supports compromises auditability.
- **EPC-authored vs. vendor-authored content.** This SOW is EPC-authored; technical design content belongs in the Package Datasheet (`DEL-095-02`) and the vendor's engineered equipment package (`DEL-095-04`). Resist drift of vendor design content into this deliverable.
- **Interface enumeration vs. interface design.** Naming the nine applicable interfaces in this SOW satisfies the integration narrative requirement; interface *design* (sizes, ratings, materials, connection details) belongs in the Package Datasheet and downstream EPC discipline deliverables.

## Examples

Source-grounded statement (good):
> "The package supplies one API 650 modified atmospheric slop storage tank (preliminary tag `TK-9130-2`) with tank appurtenances, connections to drain/recycle/truck-out systems, and standard tank instrumentation (SOW-0215; `26020-Package_Requirements.docx` heading 47, Major included equipment)."

Insufficiently grounded statement (avoid):
> "The slop tank is 30 ft diameter by 32 ft tall, 150,000 USG capacity, A36 carbon steel, designed for 14.9 psig and 150 F." — there is no locally accessible source slice for these values; mark `TBD` with `location TBD`.

Avoid promoting "likely":
> "The slop tank tag is `TK-9130-2`." — source qualifies the tag as "likely". Carry as ASSUMPTION until confirmed.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CONF-095-01-01 | Final slop source list, disposition path (recycle vs. truck-out routing), and tank design basis are explicitly flagged as requiring process confirmation. | `SCOPE_LEDGER.csv` SOW-0216 ("Final source list, disposition path, and tank design basis require process confirmation.") | `_REFERENCES.md` (no copied process basis slice) | Datasheet "Conditions"; Specification R04; Procedure step 3 | PROPOSAL: defer detailed disposition/design-basis content to `DEL-095-02_package-datasheet` after process engineering confirmation; the SOW carries the open-item status verbatim. | TBD |
| CONF-095-01-02 | Tank design conditions (capacity, dimensions, P, T, materials, API 650 "modified" appendix selections) are not in locally accessible source slices but are required by downstream Package Datasheet. | `_REFERENCES.md` (no copied slices) | `PACKAGE_REGISTER.csv` SourceRefRaw (`26020-Package_Requirements.docx` heading 47 detail text exists in source but is not locally extracted) | Datasheet "Conditions"; Specification Standards | PROPOSAL: extract design conditions and API 650 modification basis from `26020-Package_Requirements.docx` package heading 47 into a deliverable-local source slice before producing `DEL-095-02_package-datasheet`. | TBD |
| CONF-095-01-03 | Ownership of Cathodic Protection vs. Grounding / Bonding at the tank base is not delineated. | `INTERFACE_REGISTER.csv` PKG-095 (lists both as separate interfaces, no ownership split) | `PACKAGE_REGISTER.csv` ResponsibilityModel (general vendor/EPC split, no per-interface allocation) | Specification R06; Datasheet "Construction"; Procedure step 3 | PROPOSAL: assign tank CP system (anodes/rectifier/reference cells) ownership to EPC Integrator under Cathodic Protection; assign tank grounding/bonding (lightning protection, static dissipation, electrical bonding) ownership to EPC Integrator under Grounding / Bonding; both interfaces are facility-level. | TBD |
| CONF-095-01-04 | "Tanks, Slop (API 650)" package name implies API 650 base while SOW-0215 says "API 650 modified atmospheric" — the modification scope is undefined in locally accessible material. | `DELIVERABLE_REGISTER.csv` / `PACKAGE_REGISTER.csv` PackageName | `SCOPE_LEDGER.csv` SOW-0215 | Datasheet "Conditions" (Design code row); Specification Standards | PROPOSAL: defer enumeration of API 650 modifications to Package Datasheet; flag both Datasheet and Specification with explicit "TBD — modification scope" notes. | TBD |
