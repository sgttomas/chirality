# Procedure: DEL-012-03 Construction Work Package

## Purpose

Define the procedure for producing and using the PKG-012 construction work package for installation, tie-in, inspection, and turnover of the 10KVA AC UNINTERRUPTIBLE POWER SUPPLY package.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot is available.
- Deliverable-local _CONTEXT.md, _REFERENCES.md, and _DEPENDENCIES.md are available.
- Workbook Packages row 14 and Gate 7 registers are available for package identity, artifacts, objectives, and interfaces.
- DBM-Comp_and_Liquids SEC-12 Electrical Basis is available for UPS service context.
- Declared upstream dependencies: none declared in _DEPENDENCIES.md.
- Issued design/vendor documents for final feeder, breaker, cable, battery, mounting, clearance, and test values: TBD.

## Steps

1. Confirm package identity.
   - Verify deliverable ID DEL-012-03_construction-work-package, parent package PKG-012, WBS 02, tracking number 26020-02-30-003, and package name against _CONTEXT.md and PACKAGE_REGISTER.csv.

2. Establish responsibility boundaries.
   - Record that the EPC Integrator owns facility integration, tie-ins, constructability, procurement/construction coordination, and facility-level integration.
   - Record that the Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package.

3. Build the workface plan.
   - Include physical installation sequence, work area readiness, access constraints, interface hold/check points, and turnover checkpoints.
   - Mark final field values TBD when issued design/vendor documents are not available.

4. Add electrical power interface controls.
   - Include source isolation, tie-in location, cable/termination checks, pre-energization checks, and test evidence placeholders.
   - Align the UPS service narrative with DBM SEC-12 120 VAC / 125 VDC UPS service context.
   - Keep final feeder, breaker, cable, battery, and test values TBD unless supported by issued design/vendor documents.

5. Add grounding and bonding controls.
   - Include grounding/bonding connection checks, inspection signoff, and turnover evidence fields.
   - Keep final conductor and routing details TBD unless supported by issued design/vendor documents.

6. Add maintenance access controls.
   - Include access, clearance, maintainability, and obstruction checks.
   - Keep final clearance dimensions TBD unless supported by issued design/vendor documents.

7. Add structural/foundations/supports controls.
   - Include support, anchorage, mounting, housekeeping pad, or foundation checks as applicable.
   - Keep final anchorage/support details TBD unless supported by issued design/vendor documents.

8. Assemble turnover checklist.
   - Include inspection records, interface completion evidence, tie-in evidence, test records, and turnover acceptance fields.

9. Perform cross-document consistency review.
   - Check that Datasheet attributes, Specification requirements, Guidance rationale, and Procedure verification hooks use the same package identity, interface list, and TBD values.

## Verification

| Check | Acceptance basis |
|---|---|
| Identity check | Matches _CONTEXT.md, PACKAGE_REGISTER.csv row PKG-012, and DELIVERABLE_REGISTER.csv row DEL-012-03. |
| Artifact completeness | Construction work package, installation and tie-in workface plan, and construction interface and turnover checklist are present. |
| Interface coverage | Electrical Power, Grounding / Bonding, Maintenance Access, and Structural / Foundations / Supports are each addressed. |
| Electrical basis consistency | UPS service discussion is consistent with DBM SEC-12 and does not assert unsupported final values. |
| Responsibility boundary | EPC Integrator and Package Vendor responsibilities are separated. |
| TBD discipline | Unsupported design/construction values remain TBD. |
| Turnover readiness | Inspection, tie-in, test, and turnover evidence fields are included. |

## Records

- Completed construction work package.
- Installation and tie-in workface plan.
- Construction interface and turnover checklist.
- Electrical power tie-in/pre-energization checklist.
- Grounding/bonding inspection record.
- Maintenance access and clearance check record.
- Structural/foundations/supports check record.
- Open TBD and Human Ruling Required log.
