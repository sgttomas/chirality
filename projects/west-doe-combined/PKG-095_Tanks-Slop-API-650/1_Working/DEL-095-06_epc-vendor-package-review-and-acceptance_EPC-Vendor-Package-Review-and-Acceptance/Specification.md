# Specification — DEL-095-06 EPC Vendor Package Review and Acceptance (PKG-095)

> **Normative scope:** Requirements the EPC Integrator must satisfy to perform vendor package review, integration acceptance, and handoff readiness for the PKG-095 slop tank vendor package.
> **Authority:** EPC Scope of Work, Package Datasheet, Construction Work Package (sibling deliverables DEL-095-01/02/03), Gate 7 PROJECT_DECOMP, and locally accessible source slices.

## Scope

### In scope

- Review of vendor-supplied package engineering, design, vendor documentation, and physical equipment package against the EPC Scope of Work (DEL-095-01), Package Datasheet (DEL-095-02), and Construction Work Package (DEL-095-03). (Source: DELIVERABLE_REGISTER.csv DEL-095-06 description.)
- Production and maintenance of the vendor document review log, package acceptance checklist, test/inspection evidence record, and turnover evidence record. (Source: `_CONTEXT.md` Anticipated Artifacts; DELIVERABLE_REGISTER.csv.)
- Confirmation of facility-level integration readiness across the applicable interface types declared for PKG-095. (Source: PACKAGE_REGISTER.csv PKG-095 row.)
- Coverage of scope items SOW-0213, SOW-0214, SOW-0215, SOW-0216. (Source: `_CONTEXT.md`.)

### Out of scope

- Vendor's own package engineering, design, fabrication, supply, and vendor documentation production work (these are the upstream PKG-095 vendor deliverables, not this acceptance deliverable). (Source: PACKAGE_REGISTER.csv PKG-095 ownership statement.)
- Whole-facility process basis or non-PKG-095 package scope.

## Requirements

Each requirement is identified `R-095-06-NN`. Unless otherwise noted, requirements derive from `_CONTEXT.md`, the DELIVERABLE_REGISTER.csv DEL-095-06 row, and the PACKAGE_REGISTER.csv PKG-095 row.

| ID | Requirement | Source / Status |
|---|---|---|
| R-095-06-01 | The EPC Integrator shall maintain a vendor document review log covering all vendor submittals received for PKG-095. | DELIVERABLE_REGISTER.csv (anticipated artifacts) |
| R-095-06-02 | The EPC Integrator shall produce and maintain a package acceptance checklist that explicitly references the EPC Scope of Work (DEL-095-01), Package Datasheet (DEL-095-02), and Construction Work Package (DEL-095-03) as the basis of acceptance. | DELIVERABLE_REGISTER.csv DEL-095-06 description |
| R-095-06-03 | The EPC Integrator shall record test and inspection evidence demonstrating the vendor package meets the Package Datasheet criteria. | DELIVERABLE_REGISTER.csv (anticipated artifacts) |
| R-095-06-04 | The EPC Integrator shall record turnover evidence demonstrating handoff readiness for facility integration. | DELIVERABLE_REGISTER.csv (anticipated artifacts) |
| R-095-06-05 | The acceptance scope shall include verification of each applicable PKG-095 interface type: Process Piping; Relief / Flare / Vent; Drain / Containment; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. | PACKAGE_REGISTER.csv PKG-095 row |
| R-095-06-06 | Acceptance shall confirm slop-service routings into the vendor package are consistent with the design basis: LP fuel-gas scrubber V-3210-2 routes liquids to slop TK-9130-2; LP KO drum V-3900-2 pumps liquids via P-3900-2 to slop; HP KO drum pumps P-4100-2 and P-4150-2 truck out or transfer liquids to slop. | `3-25_Comp_and_Liquids_DBM.md` lines 463, 497, 499 (ASSUMPTION: PKG-095 follows the 3-25 analog routing; needs human ruling to confirm) |
| R-095-06-07 | Acceptance shall confirm the tank's design code declaration (API 650) is reflected in the vendor's submittals. | `_CONTEXT.md`; package name "Tanks, Slop (API 650)" |
| R-095-06-08 | The acceptance checklist shall record the result for each scope item SOW-0213, SOW-0214, SOW-0215, SOW-0216. | DELIVERABLE_REGISTER.csv |
| R-095-06-09 | Acceptance shall verify winterization provisions (heat tracing, tank heating, insulation) appropriate to -40 deg C minimum ambient. | `3-25_Comp_and_Liquids_DBM.md` lines 145, 770 |
| R-095-06-10 | Acceptance shall verify foundation design closure against the final geotechnical report and snow/wind/seismic, frost, vibration, settlement, and maintenance-access criteria applicable to tanks. | `3-25_Comp_and_Liquids_DBM.md` lines 688, 700 (ASSUMPTION: applies via the 3-25 analog) |
| R-095-06-11 | Sour-service applicability for slop service shall be reviewed and either confirmed or excluded with documented basis. | `TBD` — source slice does not state slop-service sour requirements explicitly |
| R-095-06-12 | Slop-tank capacity (bbl), design SG, design pressure/temperature, internal coating, and vent/relief configuration shall be confirmed against the Package Datasheet before acceptance signoff. | `TBD` — values not stated in available slice |
| R-095-06-13 | Acceptance shall confirm package-specific exclusions are explicitly stated in the Package Datasheet; if no exclusions apply, this shall be recorded. | PACKAGE_REGISTER.csv PKG-095 (current exclusions field is `TBD; no package-specific exclusions stated in source materials`) |
| R-095-06-14 | Vendor document review log entries shall reference the source vendor document table rows where they exist (per PKG-095 Vendor Document Turnover Package, DEL-095-05). | Cross-reference to DEL-095-05 (sibling); ASSUMPTION based on standard PKG vendor turnover pattern |
| R-095-06-15 | The acceptance package shall not certify or approve work; binding approvals are recorded by humans only. | Project governing rule (Chirality K-AUTH-1); applied here as a documentary discipline requirement |

## Standards

| Standard | Applicability | Status |
|---|---|---|
| API 650 | Welded tanks for oil storage — designated by the package name "Tanks, Slop (API 650)" | Locally accessible standard text TBD; location TBD |
| API 650 Modified (per 3-25 DBM analog) | Atmospheric tank class used in the 3-25 produced-water and condensate tank designs | `3-25_Comp_and_Liquids_DBM.md` line 421 (analog; slop-specific clause references TBD) |
| Sour-service rules (e.g., NACE MR0175 / ISO 15156) | Conditional on R-095-06-11 ruling | `TBD` |
| Project DBM (3-25) | Site basis, winterization, heat-tracing | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |

## Verification

| Requirement | Verification approach | Evidence target |
|---|---|---|
| R-095-06-01 | Inspection of vendor document review log | Vendor document review log artifact |
| R-095-06-02 | Inspection of package acceptance checklist | Package acceptance checklist artifact |
| R-095-06-03 | Inspection of test/inspection records | Test/inspection evidence artifact |
| R-095-06-04 | Inspection of turnover records | Turnover evidence artifact |
| R-095-06-05 | Walk-down per interface type; checklist completion | Acceptance checklist (interface section) |
| R-095-06-06 | Cross-check vendor P&IDs and tag list against design-basis slop routings | Vendor document review log entry |
| R-095-06-07 | Document review — vendor data report referencing API 650 | Vendor data report review entry |
| R-095-06-08 | Checklist cross-reference to each SOW item | Acceptance checklist (scope coverage matrix) |
| R-095-06-09 | Design review of vendor winterization provisions | Acceptance checklist (winterization section) |
| R-095-06-10 | Design review of foundation and anchorage submittals | Acceptance checklist (civil/foundation section) |
| R-095-06-11 | Documented ruling on sour-service applicability | Acceptance checklist (open items / HRR) |
| R-095-06-12 | Cross-reference to Package Datasheet values | Acceptance checklist + Datasheet cross-reference matrix |
| R-095-06-13 | Documented confirmation of exclusion statement | Acceptance checklist (exclusions section) |
| R-095-06-14 | Cross-reference to DEL-095-05 register | Vendor document review log |
| R-095-06-15 | Documentary review — absence of agent-issued approval; human signoff entries only | Acceptance package cover sheet |

## Documentation

The following artifacts shall exist in this deliverable folder at completion (per `_CONTEXT.md` Anticipated Artifacts):

- Vendor document review log
- Package acceptance checklist
- Test/inspection evidence record
- Turnover evidence record
- Conflict/Open-items log (this run's Guidance.md Conflict Table is the seed)
