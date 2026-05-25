# Guidance: Vendor Engineered Equipment Package

## Purpose

This deliverable exists to keep the 10KVA AC Uninterruptible Power Supply package as a vendor-owned production unit while preserving EPC Integrator review and facility integration responsibilities. Gate 7 assigns package engineering, package design, vendor documentation, and physical equipment package ownership to the Package Vendor, while the EPC Integrator owns integration into the functional process facility.

## Principles

- Preserve the vendor/EPC responsibility split. Do not recast vendor engineering or package design as EPC production work. Source: Gate 7 `PACKAGE_REGISTER.csv`, row `PKG-012`; `PROJECT_DECOMP.md`, objective `OBJ-004`.
- Keep the package anchored to accepted package identity: `PKG-012`, 10KVA AC Uninterruptible Power Supply, WBS 02, tracking number `26020-02-30-003`. Source: Gate 7 `PACKAGE_REGISTER.csv`, row `PKG-012`.
- Treat Electrical Power, Grounding / Bonding, Maintenance Access, and Structural / Foundations / Supports as the visible interface families for this Phase 2.2 package. Source: Gate 7 `PACKAGE_REGISTER.csv`, row `PKG-012`.
- Keep unsupported technical detail as `TBD`. The accepted local source slices do not provide UPS-specific ratings beyond package name, nor vendor standards, test requirements, enclosure details, autonomy, or accessory details.

## Considerations

- `OBJ-004` is directly relevant because the package is electrical and vendor-owned; the strongest governance concern is preserving vendor engineering and EPC integration as separate responsibilities.
- `OBJ-005` is relevant because the package is part of the facility electrical power basis and vendor-load/interface integration.
- `OBJ-008` is relevant through maintenance access and structural/foundation/support interfaces.
- `OBJ-009` is relevant as a safety, regulatory, codes, and standards carry-through objective, but no clause-level safety or code requirements are available in the deliverable-local source slices.
- `OBJ-010` is relevant through operability, maintainability, vendor-documentation, commissioning, turnover, and open-item closure evidence.
- ASSUMPTION: Detailed electrical design criteria should be taken from the EPC package Scope of Work, EPC Package Datasheet, vendor submittals, and applicable standards when those are accepted into the deliverable source set.

## Trade-offs

| Topic | Guidance |
|---|---|
| Source fidelity vs. completeness | Prefer `TBD` over invented UPS details. A sparse but source-grounded package is better than a complete-looking package with unsupported values. |
| Vendor autonomy vs. EPC integration | Vendor design ownership should be preserved, but EPC needs enough interface evidence to review power, grounding/bonding, access, and support/foundation impacts. |
| Package evidence vs. turnover evidence | This deliverable covers the vendor engineered equipment package and design basis/datasheet set. Vendor document turnover and EPC acceptance are separate deliverables in Gate 7 for `PKG-012`. |

## Examples

- Acceptable source-grounded statement: "The package interface types are Electrical Power, Grounding / Bonding, Maintenance Access, and Structural / Foundations / Supports." Source: Gate 7 `PACKAGE_REGISTER.csv`, row `PKG-012`.
- Acceptable TBD statement: "Battery autonomy: TBD; no accepted local source slice provides this value."
- Not acceptable without later source support: assigning a specific autonomy, enclosure rating, make/model, or test protocol solely from generic UPS practice.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HR-012-04-001 | The accepted Gate 7 package basis lists only high-level package identity and interfaces; detailed UPS source slices were not copied during PREPARATION. | `_REFERENCES.md`, Missing / Deferred References | Gate 7 `PACKAGE_REGISTER.csv`, row `PKG-012` lists DBM-Comp_and_Liquids/3-25 source ref but no clause slice | Datasheet Conditions/Construction; Specification Requirements/Standards; Procedure Steps | Use Gate 7 rows as current authority and keep detailed UPS values `TBD` until accepted vendor/EPC source slices are added. | TBD |

