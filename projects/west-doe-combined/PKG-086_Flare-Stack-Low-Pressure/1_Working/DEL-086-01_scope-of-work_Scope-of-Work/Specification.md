# Specification: DEL-086-01_scope-of-work — Scope of Work

> Normative specification for the EPC Integrator Scope of Work for PKG-086 (Flare Stack — Low Pressure). Requirements are derived from the Gate 7 PROJECT_DECOMP snapshot. Where source detail beyond the decomposition is required, items are marked `TBD` with `location TBD`.

## Scope

### In Scope

This Scope of Work shall define the EPC Integrator's package-level scope for the Low-Pressure Flare Stack package (`PKG-086`), including:

- Package identity and tagged equipment list for the LP flare stack and the associated LP flare stack blower. [Source: `SCOPE_LEDGER.csv` SOW-0091, SOW-0092, SOW-0093]
- Package function and whole-facility integration narrative. [Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-086-01]
- Source basis citations to the workbook and package requirements document. [Source: `DELIVERABLE_REGISTER.csv` SourceRef]
- Responsibility assignment between Package Vendor and EPC Integrator. [Source: `PACKAGE_REGISTER.csv` PKG-086 responsibility column]
- Package boundaries and applicable facility-integration interfaces. [Source: `INTERFACE_REGISTER.csv` rows scoped to PKG-086]

### Out of Scope (delegated to sibling deliverables)

- Detailed technical datasheet content for vendor handoff — delegated to **DEL-086-02 Package Datasheet**.
- Construction installation, tie-in workface planning, and turnover checklists — delegated to **DEL-086-03 Construction Work Package**.
- Vendor engineering, design, fabrication/supply, and physical equipment package — owned by **DEL-086-04 Vendor Engineered Equipment Package** (Package Vendor).
- Vendor document register and document submittals/turnover — owned by **DEL-086-05 Vendor Document Turnover Package**.
- Vendor package review/acceptance evidence — delegated to **DEL-086-06 EPC Vendor Package Review and Acceptance**.

[Source for sibling delegation: `DELIVERABLE_REGISTER.csv` rows DEL-086-02 through DEL-086-06.]

## Requirements

| ID | Requirement | Source |
|---|---|---|
| REQ-086-01-001 | The Scope of Work shall identify `PKG-086` as a distinct WBS-02 Mechanical package carrying the workbook-defined vendor-responsible package "Flare Stack (Low Pressure)". | `SCOPE_LEDGER.csv` SOW-0091 |
| REQ-086-01-002 | The Scope of Work shall list the major included equipment: LP flare stack, air-assist blower, pilot, pilot proving, auto-ignition, supplemental fuel gas/dilution gas provisions, and stack interface details. | `SCOPE_LEDGER.csv` SOW-0093 (source: 26020-Package_Requirements.docx package heading 39, "Major included equipment") |
| REQ-086-01-003 | The Scope of Work shall record the package function as a reference/interface package for the LP flare stack and associated LP flare stack blower. | `SCOPE_LEDGER.csv` SOW-0092; `PACKAGE_REGISTER.csv` PKG-086 |
| REQ-086-01-004 | The Scope of Work shall assign Package Vendor responsibility for package engineering, package design, vendor documentation, and the physical equipment package; and shall assign EPC Integrator responsibility for facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` PKG-086 responsibility column |
| REQ-086-01-005 | The Scope of Work shall enumerate the applicable interfaces between PKG-086 and the facility: Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; Grounding / Bonding; I&C / Control Cabling; Fire & Gas / Safety Systems; Structural / Foundations / Supports. | `INTERFACE_REGISTER.csv` PKG-086 rows (8) |
| REQ-086-01-006 | The Scope of Work shall preserve the procurement-authority note that both line items are identified as 4-25 shared assets excluded from 3-25 DBM scope and that procurement authority rests with the 4-25 scope unless the boundary ruling changes. | `SCOPE_LEDGER.csv` SOW-0094 |
| REQ-086-01-007 | The Scope of Work shall reference the upstream source basis (Workbook Packages row 59; 26020-Package_Requirements.docx package heading 39) and the design-basis documents identified for the related objectives. | `DELIVERABLE_REGISTER.csv` SourceRef; `PACKAGE_REGISTER.csv` PKG-086 references |
| REQ-086-01-008 | The Scope of Work shall demonstrate coverage of supported objectives OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 by stating, for each, how the package contributes. | `DELIVERABLE_REGISTER.csv` SupportsObjectives; `OBJECTIVE_REGISTER.csv` |
| REQ-086-01-009 | The Scope of Work shall identify the tagged equipment list per the source package heading. Where the source slice is not yet available locally, the SoW shall mark the tag list `TBD` with `location TBD`. | `_CONTEXT.md` Anticipated Artifacts; ASSUMPTION pending source slice |
| REQ-086-01-010 | The Scope of Work shall not duplicate normative datasheet content, construction workface content, vendor design content, or vendor-document turnover content owned by sibling deliverables DEL-086-02 through DEL-086-06. | `DELIVERABLE_REGISTER.csv` rows DEL-086-02..06 |

## Standards

| Topic | Governing Standard | Status |
|---|---|---|
| Flare design (sour service, low-pressure flare) | API Standard 537 (Flare Details); API Standard 521 (Pressure-Relieving and Depressuring Systems). ASSUMPTION: likely applicable based on service. | `location TBD` — source clause citation not yet copied locally |
| Sour-service materials | NACE MR0175 / ISO 15156. ASSUMPTION based on OBJ-009 sour-service safety scope. | `location TBD` |
| Regulatory, codes, and standards basis | As listed in 4-25 DBM SEC-15 and 3-25 DBM SEC-15. | `location TBD` (source slices not yet copied locally) |

Per the four-documents authority hierarchy, clause-level requirements shall not be derived from the standards above until the relevant source slices are locally accessible.

## Verification

| Requirement | Verification Approach |
|---|---|
| REQ-086-01-001..003 | Cross-check SoW package identification against `PACKAGE_REGISTER.csv` row PKG-086 and `SCOPE_LEDGER.csv` rows SOW-0091..0093. |
| REQ-086-01-004 | Cross-check responsibility statements against `PACKAGE_REGISTER.csv` PKG-086 responsibility column verbatim. |
| REQ-086-01-005 | Cross-check enumerated interfaces against `INTERFACE_REGISTER.csv` rows with ParentPackageID `PKG-086`; count shall be 8 with `Applicable = YES`. |
| REQ-086-01-006 | Cross-check procurement-authority statement against `SCOPE_LEDGER.csv` SOW-0094 verbatim. |
| REQ-086-01-007 | Confirm source basis citations include Workbook Packages row 59 and 26020-Package_Requirements.docx package heading 39. |
| REQ-086-01-008 | For each of OBJ-002, OBJ-004..010, confirm a contribution statement is present in the SoW. |
| REQ-086-01-009 | Confirm tagged-equipment list is either present with source citations or explicitly marked `TBD` with `location TBD`. |
| REQ-086-01-010 | Confirm SoW does not contain datasheet attribute tables, construction workface plans, vendor design content, or vendor-document register content beyond a delegation pointer to siblings. |

## Documentation

The Scope of Work deliverable shall produce the following anticipated artifacts within the deliverable folder:

- Package scope of work narrative
- Tagged equipment and package identity list (with `TBD` markers where source slices are not yet local)
- Package function and integration narrative
- Responsibility assignment record (Package Vendor vs EPC Integrator)

[Source: `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` AnticipatedArtifacts.]
