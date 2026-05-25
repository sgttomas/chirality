# Specification: Construction Work Package

## Scope

This document specifies the Phase 2.2 content basis for the EPC Integrator Construction Work Package for PKG-022, 5kV SWITCHGEAR EQUIPMENT.

The deliverable covers the EPC Integrator's construction-facing package needed to physically install, build, inspect, turn over, and tie the 5kV switchgear equipment package into larger facility systems. It also covers the installation and tie-in workface plan and the construction interface and turnover checklist.

The deliverable does not assign package engineering, package design, vendor documentation, or physical equipment package ownership to the EPC Integrator. Gate 7 identifies those responsibilities as Package Vendor-owned, with EPC ownership limited to facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Detailed construction means, methods, code clauses, vendor installation instructions, inspection hold points, cable schedule details, equipment tags, switchgear ratings, testing criteria, and commissioning/energization procedures are TBD until locally accessible source slices or vendor documents are resolved.

## Requirements

| ID | Requirement | Basis | Verification |
|---|---|---|---|
| CWP-REQ-001 | The Construction Work Package shall identify DEL-022-03_construction-work-package, PKG-022, package name 5kV SWITCHGEAR EQUIPMENT, discipline Electrical, responsible party EPC Integrator, and scope item SOW-0023. | _CONTEXT.md; DELIVERABLE_REGISTER.csv row `DEL-022-03_construction-work-package` | Confirm identity block matches accepted context and Gate 7 register row. |
| CWP-REQ-002 | The Construction Work Package shall preserve the vendor/EPC split: Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration and interfaces. | PACKAGE_REGISTER.csv row `PKG-022` | Confirm responsibility statements do not move vendor-owned design work into EPC construction scope. |
| CWP-REQ-003 | The Construction Work Package shall include or reference a construction work package, installation and tie-in workface plan, and construction interface and turnover checklist. | DELIVERABLE_REGISTER.csv row `DEL-022-03_construction-work-package`; ARTIFACT_REGISTER.csv rows `ART-31BD60C810`, `ART-474069A619`, `ART-686B185A30` | Confirm the three artifact classes are present in the deliverable package or listed as required records. |
| CWP-REQ-004 | The installation and tie-in planning content shall address the accepted interface types for PKG-022: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. | PACKAGE_REGISTER.csv row `PKG-022`; INTERFACE_REGISTER.csv rows for `PKG-022` | Confirm each interface type has a corresponding planning/checklist line or a TBD marker. |
| CWP-REQ-005 | The package shall treat declared dependency blockers as advisory and limited to declared dependency edges only. | _DEPENDENCIES.md; _Coordination/_COORDINATION.md | Confirm no undeclared sibling package or deliverable is listed as a blocker. |
| CWP-REQ-006 | Where detailed source-backed construction values are unavailable, the package shall mark them TBD rather than inventing requirements. | _REFERENCES.md; four-documents QA_CHECKS.md | Confirm missing source-dependent values are explicitly marked TBD. |
| CWP-REQ-007 | ASSUMPTION: The construction package should carry directionally relevant objective context for OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, and OBJ-010 because Gate 7 maps these objectives to this deliverable via the package-grouping heuristic. | OBJECTIVE_DELIVERABLE_MAP.csv rows for `DEL-022-03_construction-work-package` | Confirm objective references are used as context and not as unverified clause-level requirements. |

## Standards

| Standard or authority | Status |
|---|---|
| Gate 7 final published PROJECT_DECOMP snapshot, 2026-05-24 | Authoritative upstream decomposition truth for this run. |
| Workbook Packages row 24 | Referenced by Gate 7 registers; detailed original workbook content was not reinterpreted in this bounded task. |
| _Sources/DBM-Deepcut/4-25_Deepcut_DBM.md | Referenced by Gate 7 PACKAGE_REGISTER.csv row `PKG-022`; raw source corpus was not reinterpreted in this bounded task per instruction. |
| Electrical installation codes, site standards, vendor installation manuals, commissioning standards | TBD; not available as deliverable-local source slices in this run. |

## Verification

| Verification activity | Acceptance basis |
|---|---|
| Identity verification | Matches _CONTEXT.md and DELIVERABLE_REGISTER.csv row `DEL-022-03_construction-work-package`. |
| Responsibility verification | Vendor/EPC ownership split matches PACKAGE_REGISTER.csv row `PKG-022`. |
| Interface coverage check | Each accepted interface type from INTERFACE_REGISTER.csv rows for `PKG-022` appears in planning, checklist, or TBD sections. |
| Artifact completeness check | Construction work package, installation and tie-in workface plan, and construction interface and turnover checklist are included or explicitly required. |
| Source fidelity check | Unsupported details remain TBD, ASSUMPTION, or human-ruling items. |
| Dependency check | No blockers are asserted because no upstream or downstream dependencies were declared during PREPARATION. |

## Documentation

Required construction package records:

- Construction work package.
- Installation and tie-in workface plan.
- Construction interface and turnover checklist.
- Responsibility assignment evidence preserving the Package Vendor/EPC Integrator split.
- Interface coverage evidence for Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports.
- TBD/open-item log for source-limited construction details.
