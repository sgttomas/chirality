# Specification: DEL-020-06_epc-vendor-package-review-and-acceptance

## Scope

### In scope

- EPC Integrator review of the Package Vendor's engineering, design, documentation, and physical equipment package for `PKG-020` (13.8kV SWITCHGEAR EQUIPMENT), as supplied through DEL-020-04 (Vendor Engineered Equipment Package) and DEL-020-05 (Vendor Document Turnover Package).
- Acceptance evidence demonstrating that the vendor package conforms to:
  - the EPC Scope of Work for PKG-020 (DEL-020-01),
  - the EPC Package Datasheet for PKG-020 (DEL-020-02),
  - the Construction Work Package for PKG-020 (DEL-020-03).
- Integration acceptance: verification that vendor package interfaces (Electrical Power, Grounding/Bonding, I&C/Control Cabling, Communications/Network, Maintenance Access, Structural/Foundations/Supports) are reconciled with facility-level integration requirements. (`INTERFACE_REGISTER.csv` rows for `PKG-020`.)
- Handoff readiness: production of the four anticipated artifacts — vendor document review log, package acceptance checklist, test/inspection evidence, turnover evidence. (`_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`.)

### Out of scope

- Authoring the vendor package itself (DEL-020-04, DEL-020-05).
- Authoring the EPC Scope of Work, Package Datasheet, or Construction Work Package (DEL-020-01, DEL-020-02, DEL-020-03).
- Binding contractual acceptance: TBD pending project commercial/approval workflow.

## Requirements

| ID | Requirement | Basis |
|---|---|---|
| REQ-020-06-01 | The acceptance evidence shall demonstrate conformance of the vendor package to the EPC Scope of Work, Package Datasheet, and Construction Work Package for PKG-020. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-020-06...` |
| REQ-020-06-02 | The vendor document review log shall enumerate every Package Vendor submittal in scope for PKG-020 and shall record reviewer, review status, comments, and final disposition for each item. **ASSUMPTION:** review-status taxonomy (e.g., A/B/C/Rev) follows project document-control procedure; specific taxonomy TBD. | `_CONTEXT.md` anticipated artifacts |
| REQ-020-06-03 | The package acceptance checklist shall verify (a) scope conformance against DEL-020-01, (b) datasheet conformance against DEL-020-02, (c) constructability/tie-in conformance against DEL-020-03, (d) interface conformance against `INTERFACE_REGISTER.csv` rows for `PKG-020`, and (e) code/standard conformance against the governing electrical standards. | `_CONTEXT.md`; `INTERFACE_REGISTER.csv`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 |
| REQ-020-06-04 | Acceptance shall not be granted until the required electrical studies (hazardous-area-classification, load, short-circuit, relay-coordination/arc-flash, load-flow) have been completed and their outcomes are reflected in the vendor package ratings and protection settings. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 electrical-studies paragraph |
| REQ-020-06-05 | The acceptance evidence shall confirm that all medium-voltage switchgear equipment supplied is new, of current design, and third-party certified by CSA, ULc, FM, ETL, or another Nationally Recognized Testing Laboratory acceptable for the application. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 codes/standards paragraph |
| REQ-020-06-06 | Equipment compliance shall be verified against ELC-QAS-000007-001 "Medium Voltage Switchgear" (Rev 1) and packaged-equipment compliance against ELC-QAS-000003-001 "Electrical Requirements for Packaged Equipment" (Rev 2). Detailed clause-level acceptance criteria are `location TBD` until those specifications are accessed. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Table 12-1 |
| REQ-020-06-07 | Test and inspection evidence shall include, at minimum, factory acceptance test (FAT) records, site acceptance test (SAT) records, and applicable inspection reports for the vendor package. **ASSUMPTION:** specific FAT/SAT scope and witness requirements TBD pending governing equipment specification review. | `_CONTEXT.md` anticipated artifacts; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Table 12-1 |
| REQ-020-06-08 | Turnover evidence shall be reconciled with the DEL-020-05 Vendor Document Turnover Package and shall demonstrate mechanical completion and EPC acceptance against the facility turnover procedure. Specific turnover-procedure reference is `location TBD`. | `DELIVERABLE_REGISTER.csv` row `DEL-020-05`; `_CONTEXT.md` |
| REQ-020-06-09 | Each PKG-020 interface row in `INTERFACE_REGISTER.csv` (Electrical Power, Grounding/Bonding, I&C/Control Cabling, Communications/Network, Maintenance Access, Structural/Foundations/Supports) shall have a corresponding acceptance-checklist line item verifying that the vendor package satisfies the interface. | `INTERFACE_REGISTER.csv` rows `IFC-611474D99C`, `IFC-F3098CE7CD`, `IFC-8BF7209227`, `IFC-340091634A`, `IFC-2FB786FC10`, `IFC-08E563D004` |
| REQ-020-06-10 | The acceptance evidence shall record any deviation or exception from applicable codes and standards and shall confirm formal approval by Tourmaline Oil Corp before acceptance is granted. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 codes/standards paragraph |
| REQ-020-06-11 | Outputs shall be stored within the deliverable folder under stable, traceable filenames so that the acceptance evidence is auditable. **ASSUMPTION:** project document-control numbering applies; specific numbering scheme TBD. | `_CONTEXT.md`; project convention |

## Standards

| Standard / specification | Role | Source / location |
|---|---|---|
| CSA C22.1-21 Canadian Electrical Code | Governing code for electrical design and installation. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 codes/standards paragraph |
| Applicable BC provincial and local electrical codes and electrical-inspection-authority requirements | Governing regulatory regime. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 codes/standards paragraph |
| CSA, API, IEEE, ISA, NEMA, WorkSafeBC, Technical Safety BC, BCER | Applicable standards and regulatory bodies. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 codes/standards paragraph |
| ELC-QAS-000007-001 "Medium Voltage Switchgear" (Rev 1) | Governing equipment specification for the subject equipment. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Table 12-1. Clause text `location TBD`. |
| ELC-QAS-000003-001 "Electrical Requirements for Packaged Equipment" (Rev 2) | Governing requirements for vendor packaged equipment. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Table 12-1. Clause text `location TBD`. |
| ELC-QAS-000001-001 "Electrical Construction" (Rev 1); ELC-QAS-000002-001 "Electrical Design" (Rev 1) | Supporting governing electrical specifications. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Table 12-1. Clause text `location TBD`. |

## Verification

| Requirement | Verification approach |
|---|---|
| REQ-020-06-01 | Inspection of acceptance checklist against DEL-020-01, DEL-020-02, DEL-020-03 line items. |
| REQ-020-06-02 | Document audit of vendor document review log against the vendor submittals listed in DEL-020-05. |
| REQ-020-06-03 | Inspection of acceptance checklist completeness across scope, datasheet, constructability, interface, and code/standard categories. |
| REQ-020-06-04 | Cross-check of vendor protection settings, ratings, and arc-flash labels against the completed electrical-study outputs. |
| REQ-020-06-05 | Audit of vendor nameplate data and certification records against NRTL list. |
| REQ-020-06-06 | Clause-by-clause checklist against ELC-QAS-000007-001 and ELC-QAS-000003-001 (clause text TBD). |
| REQ-020-06-07 | Inspection of FAT and SAT records for completeness; verification of witness sign-offs where required. |
| REQ-020-06-08 | Reconciliation of turnover evidence against DEL-020-05 turnover index and facility turnover procedure. |
| REQ-020-06-09 | Inspection that every PKG-020 interface row has a matching acceptance-checklist line item. |
| REQ-020-06-10 | Review of deviation/exception register against approval records by Tourmaline Oil Corp. |
| REQ-020-06-11 | File-system audit of deliverable folder for stable filenames and document-control identifiers. |

## Documentation

The following artifacts shall result from this deliverable (as listed in `_CONTEXT.md`):

- Vendor document review log.
- Package acceptance checklist.
- Test/inspection evidence (FAT/SAT and inspection reports).
- Turnover evidence (reconciled with DEL-020-05).

Each artifact shall be retained within the PKG-020 deliverable folder for `DEL-020-06...` and cross-referenced from the acceptance checklist.
