# Specification — DEL-095-02 Package Datasheet

Authority: normative requirements that the package datasheet artifact must satisfy when issued by the EPC Integrator for vendor handoff.

## Scope

This Specification establishes the required content, sources, and verification of the **Package Datasheet** for `PKG-095` (Tanks, Slop — API 650). The datasheet is the EPC Integrator technical handoff to a Package Vendor for the slop storage tank package.

**Covers scope items:** `SOW-0213`, `SOW-0214`, `SOW-0215`, `SOW-0216` (per DELIVERABLE_REGISTER row `DEL-095-02_package-datasheet`).

**Excludes:** Vendor-owned package engineering, design, fabrication, and detailed vendor documentation (those belong to `DEL-095-04_vendor-engineered-equipment-package` and `DEL-095-05_vendor-document-turnover-package`). The package datasheet hands off the EPC-side basis, not the vendor's design output.

## Requirements

### R1 — Identification

R1.1 The datasheet SHALL identify the package using `PKG-095`, workbook row 91, WBS 03, and CoA tracking number `26020-03-19-004`. (Source: PACKAGE_REGISTER.csv)

R1.2 The datasheet SHALL list the major included equipment item with its tag where source-supported. Source identifies `TK-9130-2` as the likely slop tank tag (ASSUMPTION; DBM line 463 references slop `TK-9130-2` in scrubber drain routing).

### R2 — Service Definition

R2.1 The datasheet SHALL state the package service as off-spec / contaminated hydrocarbon liquid storage segregated from on-spec product condensate. (Source: PACKAGE_REGISTER.csv; DBM 3-25 line 406)

R2.2 The datasheet SHALL identify upstream sources of liquid into the slop tank, including but not limited to:
- LP fuel-gas scrubber V-3210-2 liquid routing (DBM line 463),
- LP KO drum pump P-3900-2 (DBM line 499),
- HP KO drum pumps P-4100-2 / P-4150-2 truck-out or transfer (DBM line 497).

### R3 — Tank Basis

R3.1 The tank SHALL be designed to API 650. (Source: package name `Tanks, Slop (API 650)`; PACKAGE_REGISTER.csv)

R3.2 ASSUMPTION: API 650 Modified atmospheric construction applies, consistent with the produced-water tank family at the same facility (DBM line 421). The datasheet SHALL confirm or correct this in detailed design.

R3.3 Tank count SHALL be one (1). (Source: DBM line 406)

R3.4 Nominal capacity is TBD; DBM line 406 places the slop tank within the eleven-tank 3,800 bbl condensate family but does not separately confirm the slop tank capacity. The datasheet SHALL carry capacity as TBD until confirmed against final tank register.

R3.5 Internal coating, external insulation, and external heating are TBD for the slop tank specifically. The produced-water family carries Devchem 253 internal coating and external insulation and heating (DBM line 421); the datasheet SHALL NOT assert the same for slop without confirmation.

### R4 — Interfaces

R4.1 The datasheet SHALL include an interface requirements matrix listing every interface row recorded for `PKG-095` in INTERFACE_REGISTER.csv (nine interfaces, all marked YES at Gate 7).

R4.2 For each interface, the datasheet SHALL identify the facility-side scope owner (EPC Integrator) and the package-side boundary the vendor must accommodate.

### R5 — Standards and Codes

R5.1 The package design SHALL be compliant with API 650 (or API 650 Modified per facility basis). (Source: package name; DBM line 421 family basis)

R5.2 Other applicable standards (welding, coating, electrical area classification, cathodic protection, grounding/bonding) are TBD pending source-slice access to the package requirements document (`26020-Package_Requirements.docx` package heading 47) and project-level standards lists.

### R6 — Documentation

R6.1 The datasheet SHALL list the vendor documentation deliverables required for turnover. The core vendor documents are defined in ARTIFACT_REGISTER rows under `DEL-095-05_vendor-document-turnover-package` (Vendor Document Index `PRQ-009`, Vendor Document Control Procedure `DOC-008`, Supplier Quality Plan `QLT-006`, Inspection and Test Plan `QLT-003`, and additional rows in that register).

R6.2 The datasheet SHALL identify the vendor engineering deliverables expected from heading "Vendor Engineering Deliverables table" in `26020-Package_Requirements.docx` package heading 47. Specific row content is TBD pending source access.

## Standards

| Standard | Status | Location |
|---|---|---|
| API 650 (Modified) | Applicable (package basis) | DBM 3-25 line 421 (family); package name |
| 26020 Package Requirements (project-internal) | Applicable | `26020-Package_Requirements.docx` heading 47; location TBD |
| Welding, NDE, coating, hazardous area, CP, bonding standards | TBD | location TBD |

## Verification

| Requirement | Verification Approach |
|---|---|
| R1.* Identification | Cross-check against PACKAGE_REGISTER row and `_CONTEXT.md` identity block |
| R2.* Service definition | Cross-check against DBM 3-25 sections covering slop routing |
| R3.* Tank basis | Cross-check against final tank register (when issued) and against API 650 |
| R4.* Interface matrix | Cross-check against INTERFACE_REGISTER rows for `PKG-095` |
| R5.* Standards | Cross-check against project standards list (TBD source) |
| R6.* Documentation | Cross-check against `DEL-095-05` vendor documentation register |

## Documentation

The artifact register lists the following required artifacts under this deliverable (must all be present in or referenced by the issued datasheet):

- `ART-47EC8124AF` — Package technical datasheet
- `ART-FC38B263CA` — Vendor engineering handoff basis
- `ART-3D3791F640` — Package interface requirements matrix
- `ART-340A371C42` — Major included equipment evidence
- Interface-fact artifacts `ART-050B40690B` through `ART-50BA5F1C69` (nine rows, one per applicable interface)
