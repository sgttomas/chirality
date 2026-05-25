# Procedure: Vendor Engineered Equipment Package

## Purpose

Define the bounded procedure for producing and checking the vendor engineered equipment package deliverable for `DEL-012-04_vendor-engineered-equipment-package`, using the accepted Gate 7 decomposition basis and local deliverable context.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot is available.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_STATUS.md`, and `_DEPENDENCIES.md` are available.
- Current package identity is confirmed as `PKG-012`, 10KVA AC Uninterruptible Power Supply, WBS 02, tracking number `26020-02-30-003`.
- Declared upstream dependencies: none declared during PREPARATION.
- Declared downstream dependencies: none declared during PREPARATION.
- EPC package Scope of Work, EPC Package Datasheet, and detailed vendor/EPC source slices are TBD if needed for clause-level technical detail.

## Steps

1. Confirm deliverable identity against Gate 7 `DELIVERABLE_REGISTER.csv` row `DEL-012-04_vendor-engineered-equipment-package`.
2. Confirm package identity and responsibility model against Gate 7 `PACKAGE_REGISTER.csv` row `PKG-012`.
3. Establish the vendor package boundary: Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration and interface review.
4. Prepare the vendor engineered physical equipment package evidence. If detailed vendor design content is unavailable, mark the missing content `TBD` rather than deriving values from generic UPS practice.
5. Prepare the vendor package design basis and datasheet set. Include package identity, vendor/EPC responsibility split, artifact expectations, supported objectives, and interface types.
6. Address each Gate 7 interface type: Electrical Power; Grounding / Bonding; Maintenance Access; Structural / Foundations / Supports. Record unavailable detailed values such as loads, grounding points, clearances, access envelopes, and support loads as `TBD`.
7. Separate this package evidence from the related `PKG-012` deliverables for vendor document turnover and EPC vendor package review/acceptance.
8. Maintain an open technical values list for unsupported values, including vendor standards, inspections/tests, enclosure details, battery autonomy, charger/bypass configuration, and environmental criteria.
9. Submit the package for EPC Integrator review only after identity, responsibility split, anticipated artifacts, and declared interface types are visible in the package evidence.

## Verification

| Check | Acceptance Criterion |
|---|---|
| Identity check | Deliverable ID, package ID, package name, workbook row, WBS, and tracking number match Gate 7 rows. |
| Responsibility check | Vendor-owned and EPC-owned responsibilities are both present and not conflated. |
| Artifact check | Vendor engineered physical equipment package and vendor package design basis/datasheet set are present or explicitly marked `TBD`. |
| Interface check | Electrical Power, Grounding / Bonding, Maintenance Access, and Structural / Foundations / Supports are addressed or marked `TBD` with owner/action. |
| Source fidelity check | No unsupported UPS-specific design values are introduced without accepted source support. |
| Dependency check | No blockers are asserted from undeclared dependencies; current declared upstream/downstream lists are empty. |

## Records

- Vendor engineered physical equipment package evidence.
- Vendor package design basis and datasheet set.
- Interface matrix or equivalent section covering Electrical Power, Grounding / Bonding, Maintenance Access, and Structural / Foundations / Supports.
- Open technical values and human ruling log.
- EPC Integrator review comments and acceptance evidence, when produced by the separate EPC review/acceptance deliverable.

