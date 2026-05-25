# Specification: Vendor Document Turnover Package

## Scope

This specification covers the vendor document turnover package for `PKG-012`, 10KVA AC UNINTERRUPTIBLE POWER SUPPLY. The deliverable is a single Package Vendor production unit for the vendor document register, submittals, source-required vendor documentation, and turnover records, with EPC Integrator review.

Exclusions:

- EPC-owned facility design deliverables are excluded except where needed for interface or integration review.
- Detailed vendor-document requirements that are absent from Gate 7 are excluded from definitive requirements and remain `TBD`.
- Raw source corpus reinterpretation is excluded for this Phase 2.2 run.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-012-05-001 | The package shall identify `DEL-012-05_vendor-document-turnover-package`, `PKG-012`, the package name, discipline, deliverable type, and responsible-party split. | Check document cover/register metadata against Gate 7 `DELIVERABLE_REGISTER.csv` and `PACKAGE_REGISTER.csv`. |
| REQ-012-05-002 | The turnover package shall include, at minimum, a vendor document register, vendor document submittals, source-required vendor documentation rows where available, and turnover records. | Review turnover package contents against Gate 7 `DELIVERABLE_REGISTER.csv` anticipated artifacts. |
| REQ-012-05-003 | Vendor documentation shall preserve the Package Vendor ownership of package engineering, package design, vendor documentation, and physical equipment package. | Confirm submitted documents are vendor-owned or vendor-issued where applicable. |
| REQ-012-05-004 | EPC Integrator review shall address facility-level integration and interfaces, including Electrical Power, Grounding / Bonding, Maintenance Access, and Structural / Foundations / Supports where applicable. | Confirm EPC review comments/status explicitly address applicable interface types or state not applicable. |
| REQ-012-05-005 | The package shall not treat the placeholder artifact `TBD vendor document register` as a complete vendor document register. | Confirm a human-approved register or vendor-submitted register replaces the Gate 7 gap artifact before closure. |
| REQ-012-05-006 | Package-specific exclusions, vendor document list requirements, submittal status coding, turnover acceptance criteria, and final as-built/record-document requirements are `TBD` pending human or source confirmation. | Human ruling or later authoritative source slice required. |

## Standards

| Standard / authority | Applicability | Status |
|---|---|---|
| Gate 7 final published PROJECT_DECOMP snapshot | Authoritative decomposition basis for this run | Accessible |
| Workbook Packages row 14 | Source reference for package identity and scope | Referenced by Gate 7; raw workbook not reinterpreted in this run |
| Project/vendor document control procedure | Vendor document register, review status coding, revision control, and turnover acceptance | TBD; not present in accepted Gate 7 package-specific source slices |
| Electrical package interface requirements | Electrical power, grounding/bonding, maintenance access, structural/foundation/support interfaces | Gate 7 identifies interface types; detailed acceptance criteria TBD |

## Verification

Verification shall confirm:

- all required identity fields match Gate 7;
- the vendor document register exists or is explicitly marked as the current gap item;
- vendor submittals and turnover records are traceable to the vendor document register;
- EPC Integrator review status is recorded for integration/interface topics;
- unsupported or unavailable package-specific requirements remain `TBD` instead of being converted into unverified requirements.

## Documentation

Required output artifacts:

- vendor document register;
- vendor document submittals;
- source vendor document table rows as artifacts where available;
- turnover records;
- EPC Integrator review evidence for applicable interfaces;
- human ruling record for unresolved `TBD` items.
