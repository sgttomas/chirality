# Specification: DEL-050-03 — Construction Work Package

## Scope

This specification covers the EPC Integrator's Construction Work Package for `PKG-050 Stabilizer Overheads Compressors`. It defines the requirements for physically installing, building, inspecting, turning over, and tying the package into the larger facility systems.

**Includes:**
- Construction execution planning for two (2x) induction motor-driven separable reciprocating compressor packages at 2x100% capacity (PACKAGE_REGISTER row PKG-050).
- Installation and tie-in work covering all applicable facility-level interfaces listed below.
- Construction interface management with the Package Vendor scope (DEL-050-04).
- Turnover documentation and checklist execution.

**Excludes:**
- Package engineering, design, fabrication/supply, and vendor documentation — owned by Package Vendor (DEL-050-04, DEL-050-05) per PACKAGE_REGISTER row PKG-050 (ResponsibilityModel).
- Package datasheet authorship — covered by DEL-050-02.
- Vendor package review and acceptance — covered by DEL-050-06.
- Package-specific construction exclusions: none stated in accessible source materials (PACKAGE_REGISTER row PKG-050, Exclusions = TBD).

## Requirements

| Req ID | Requirement | Source |
|---|---|---|
| R-050-03-01 | The Construction Work Package shall describe physical installation, build, inspection, turnover, and facility tie-in activities for `PKG-050`. | `_CONTEXT.md` Scope; DELIVERABLE_REGISTER row DEL-050-03 (ScopeDescription) |
| R-050-03-02 | The package shall plan installation of two (2x) identical induction motor-driven separable reciprocating compressor packages, each at 100% capacity. | PACKAGE_REGISTER row PKG-050 (ScopeDescription) |
| R-050-03-03 | The work package shall address each applicable interface type: Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports. | PACKAGE_REGISTER row PKG-050 (InterfaceTypes) |
| R-050-03-04 | The work package shall coordinate constructability, procurement, and construction execution as part of facility-level integration owned by the EPC Integrator. | PACKAGE_REGISTER row PKG-050 (ResponsibilityModel) |
| R-050-03-05 | The work package shall include an installation and tie-in workface plan. | `_CONTEXT.md` Anticipated Artifacts; DELIVERABLE_REGISTER row DEL-050-03 |
| R-050-03-06 | The work package shall include a construction interface and turnover checklist. | `_CONTEXT.md` Anticipated Artifacts; DELIVERABLE_REGISTER row DEL-050-03 |
| R-050-03-07 | The work package shall demonstrate satisfaction of covered scope items SOW-0173, SOW-0174, SOW-0175, SOW-0176. | DELIVERABLE_REGISTER row DEL-050-03 (CoversScopeItems) |
| R-050-03-08 | The work package shall align facility tie-ins so that compressor suction (50 psig) and discharge (1100 psig) routings to the amine inlet filter coalescer and the first-stage recycle are constructed per process basis. | PACKAGE_REGISTER row PKG-050 (ScopeDescription) |
| R-050-03-09 | ASSUMPTION — Construction work shall conform to project-level construction standards, area classification, and HSE requirements as defined in higher-level facility documents. (No project-level construction standards register accessible in this run.) | ASSUMPTION; location TBD |
| R-050-03-10 | Inspection and test plans shall provide objective evidence supporting turnover and acceptance by DEL-050-06. | Derived from DELIVERABLE_REGISTER row DEL-050-06 (EPC Vendor Package Review and Acceptance) |

## Standards

| Standard / Code | Applicability | Status |
|---|---|---|
| Project construction execution standards | Construction methods, QA/QC | location TBD — not in accessible source slice |
| API 618 (reciprocating compressors for petroleum/chemical service) | Installation acceptance for reciprocating compressor packages | ASSUMPTION: likely applicable to vendor package; location TBD |
| Area electrical classification (NEC / IEC 60079 family) | Electrical installation in classified area | ASSUMPTION; location TBD |
| Project welding, NDE, and pressure testing specifications | Process and utility piping tie-ins | TBD |
| Facility grounding/bonding and EHT specifications | Electrical Power, Grounding/Bonding, EHT interfaces | TBD |
| Fire & gas / safety system installation specifications | F&G interface | TBD |

Concrete clause-level standards traceability requires extraction from `26020-Package_Requirements.docx` heading 5 and the project HSE / construction execution documents; not available in this run.

## Verification

| Req ID | Verification Method |
|---|---|
| R-050-03-01 | Document review against `_CONTEXT.md` Scope |
| R-050-03-02 | Document review: equipment count and capacity philosophy reflected in installation plan |
| R-050-03-03 | Checklist completeness review against the InterfaceTypes list |
| R-050-03-04 | Walkthrough with EPC Integrator and construction lead; constructability review records |
| R-050-03-05 | Inspection of workface plan artifact |
| R-050-03-06 | Inspection of turnover checklist artifact |
| R-050-03-07 | Traceability matrix to SOW-0173..0176 |
| R-050-03-08 | Process tie-in walkdown vs. P&IDs (TBD — P&ID set not in this scope) |
| R-050-03-09 | Cross-reference to project-level construction standards (TBD) |
| R-050-03-10 | Test/inspection records feed DEL-050-06 acceptance package |

## Documentation

Required artifacts (from `_CONTEXT.md` Anticipated Artifacts):
- Construction work package (master)
- Installation and tie-in workface plan
- Construction interface and turnover checklist

Derived supporting documentation:
- Interface register entries / matrix for the 13 applicable interface types (per R-050-03-03)
- Inspection and Test Plan (ITP) — content TBD
- Punch list and turnover acceptance records (feeds DEL-050-06)
- Traceability matrix to SOW-0173..0176
