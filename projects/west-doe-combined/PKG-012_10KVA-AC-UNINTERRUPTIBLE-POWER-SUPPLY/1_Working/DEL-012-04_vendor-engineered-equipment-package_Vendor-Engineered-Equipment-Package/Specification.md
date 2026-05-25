# Specification: Vendor Engineered Equipment Package

## Scope

This specification covers the vendor engineered equipment package production unit for `PKG-012`, the 10KVA AC Uninterruptible Power Supply package. The deliverable is a Package Vendor production unit for engineering, design, fabrication/supply, and the physical equipment package developed from the EPC package Scope of Work and Package Datasheet.

The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. Source: Gate 7 `PACKAGE_REGISTER.csv`, row `PKG-012`; `DELIVERABLE_REGISTER.csv`, row `DEL-012-04_vendor-engineered-equipment-package`.

Excluded from this deliverable unless explicitly assigned by later accepted source truth: EPC facility design, construction work package production, EPC vendor package review and acceptance records, and vendor document turnover package compilation. Package-specific exclusions are otherwise TBD because no package-specific exclusions are stated in the available Gate 7 source slices.

## Requirements

| Req ID | Requirement | Verification |
|---|---|---|
| REQ-012-04-001 | The vendor package shall be produced as the vendor-owned engineering/design/equipment deliverable for the 10KVA AC Uninterruptible Power Supply package. Source: Gate 7 `DELIVERABLE_REGISTER.csv`, row `DEL-012-04_vendor-engineered-equipment-package`. | Confirm deliverable identification, package name, and responsible party in vendor package index and transmittal. |
| REQ-012-04-002 | The vendor package shall preserve the Package Vendor responsibility for package engineering, package design, vendor documentation, and physical equipment package. Source: Gate 7 `PACKAGE_REGISTER.csv`, row `PKG-012`. | Verify responsibility matrix or vendor package cover sheet assigns vendor-owned work to Package Vendor. |
| REQ-012-04-003 | The vendor package shall preserve EPC Integrator responsibility for facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. Source: Gate 7 `PACKAGE_REGISTER.csv`, row `PKG-012`. | Verify EPC review boundary and integration hold points are visible in package submittal or review checklist. |
| REQ-012-04-004 | The vendor package shall address, or explicitly mark TBD for EPC resolution, the declared interface types: Electrical Power; Grounding / Bonding; Maintenance Access; Structural / Foundations / Supports. Source: Gate 7 `PACKAGE_REGISTER.csv`, row `PKG-012`. | Verify interface matrix or design-basis section includes each interface type or records it as TBD with owner. |
| REQ-012-04-005 | The vendor package shall include vendor engineered physical equipment package evidence and vendor package design basis/datasheet evidence. Source: Gate 7 `ARTIFACT_REGISTER.csv`, rows `ART-F3CC1D5672` and `ART-7A2DEBA163`. | Confirm both anticipated artifacts are present or formally listed as TBD/open. |
| REQ-012-04-006 | Detailed UPS technical values not present in the accepted source slices, including enclosure, battery autonomy, charger, bypass, load list, protection, environmental ratings, and inspection/test requirements, shall remain `TBD` until accepted vendor or EPC source material is available. Source: `_REFERENCES.md`, Missing / Deferred References; Gate 7 `PACKAGE_REGISTER.csv`, row `PKG-012`. | Review documents for invented vendor-specific values; unresolved values remain `TBD`. |

## Standards

| Standard / Basis | Status |
|---|---|
| Gate 7 final PROJECT_DECOMP snapshot | Governing accepted decomposition basis for this Phase 2.2 run. |
| Workbook Packages row 14 | Authoritative workbook basis as represented in Gate 7 registers. |
| DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md | Listed in Gate 7 `PACKAGE_REGISTER.csv` source refs for `PKG-012`; no deliverable-specific clause slice was copied into this deliverable folder during PREPARATION. |
| Electrical/vendor UPS standards | TBD; no clause-level standard text is available in the deliverable-local accepted source slices. |

## Verification

| Verification Item | Method | Acceptance Basis |
|---|---|---|
| Identity verification | Compare package ID, deliverable ID, package name, workbook row, WBS, and tracking number against Gate 7 registers | Gate 7 `PACKAGE_REGISTER.csv` and `DELIVERABLE_REGISTER.csv` |
| Responsibility split | Review responsibility matrix, vendor transmittal, or package cover sheet | Package Vendor/EPC Integrator split in Gate 7 `PACKAGE_REGISTER.csv`, row `PKG-012` |
| Artifact completeness | Check for vendor engineered physical equipment package evidence and vendor package design basis/datasheet set | Gate 7 `ARTIFACT_REGISTER.csv` rows for `DEL-012-04` |
| Interface coverage | Check package interface matrix or design basis for electrical power, grounding/bonding, maintenance access, and structural/foundation/support interfaces | Gate 7 `PACKAGE_REGISTER.csv`, row `PKG-012` |
| Open technical values | Confirm unsupported values remain `TBD` and are not treated as accepted design criteria | `_REFERENCES.md` missing/deferred references and Gate 7 source limits |

## Documentation

Required or expected package evidence:

- Vendor engineered physical equipment package.
- Vendor package design basis and datasheet set.
- ASSUMPTION: Vendor documentation should expose interface data sufficient for EPC Integrator review, because Gate 7 assigns facility integration and interface review to the EPC Integrator. Detailed document register rows are TBD until accepted vendor/EPC source material is available.
- Open technical values and human rulings log, as needed, for values not present in accepted source slices.

