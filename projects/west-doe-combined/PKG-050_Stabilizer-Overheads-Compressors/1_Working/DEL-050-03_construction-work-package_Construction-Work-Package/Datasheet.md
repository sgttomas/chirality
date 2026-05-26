# Datasheet: DEL-050-03 — Construction Work Package

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-050-03_construction-work-package` | `_CONTEXT.md` |
| Name | Construction Work Package | `_CONTEXT.md` |
| ParentPackageID | `PKG-050` | `_CONTEXT.md` |
| PackageName | Stabilizer Overheads Compressors | `_CONTEXT.md`; PACKAGE_REGISTER row PKG-050 |
| Discipline | Mechanical | `_CONTEXT.md`; PACKAGE_REGISTER row PKG-050 |
| Type | EPC Construction Work Package | `_CONTEXT.md` |
| ResponsibleParty | EPC Integrator | `_CONTEXT.md`; PACKAGE_REGISTER row PKG-050 (ResponsibilityModel) |
| Covers Scope Items | SOW-0173; SOW-0174; SOW-0175; SOW-0176 | `_CONTEXT.md`; DELIVERABLE_REGISTER row DEL-050-03 |
| Supports Objectives | OBJ-001; OBJ-003; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 | `_CONTEXT.md`; DELIVERABLE_REGISTER row DEL-050-03 |
| WBS | 01 | PACKAGE_REGISTER row PKG-050 |
| CoA Tracking Number | 26020-01-12-005 | PACKAGE_REGISTER row PKG-050 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package process function | Compresses and recycles multiple streams from 50 psig to 1100 psig; final discharge gas routed to amine inlet filter coalescer or recycled back to first stage | PACKAGE_REGISTER row PKG-050 (ScopeDescription) |
| Equipment configuration | Two (2x) identical induction motor-driven separable reciprocating compressor packages; each designed for 100% capacity | PACKAGE_REGISTER row PKG-050 (ScopeDescription) |
| Driver type | Induction motor (electric) | PACKAGE_REGISTER row PKG-050 |
| Compressor type | Separable reciprocating | PACKAGE_REGISTER row PKG-050 |
| Capacity philosophy | 2 x 100% | PACKAGE_REGISTER row PKG-050 |
| Suction pressure | 50 psig | PACKAGE_REGISTER row PKG-050 |
| Discharge pressure | 1100 psig | PACKAGE_REGISTER row PKG-050 |
| Downstream routing | Amine inlet filter coalescer; first-stage recycle | PACKAGE_REGISTER row PKG-050 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Area classification | TBD (not stated in accessible registers) | location TBD — `26020-Package_Requirements.docx` heading 5 |
| Design ambient envelope | TBD | location TBD — DBM-Comp_and_Liquids / DBM-Deepcut |
| Seismic / wind basis | TBD | location TBD |
| Noise design limits | TBD | location TBD |

## Construction

| Item | Value | Source |
|---|---|---|
| Applicable interface types | Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports | PACKAGE_REGISTER row PKG-050 (InterfaceTypes) |
| EPC Integrator construction responsibilities | Integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration | PACKAGE_REGISTER row PKG-050 (ResponsibilityModel) |
| Vendor scope boundary | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package | PACKAGE_REGISTER row PKG-050 (ResponsibilityModel) |
| Foundations / structural supports | TBD — design dependent (DEL-050-02 Package Datasheet downstream); ASSUMPTION: vendor skid mounted with EPC-supplied foundations | PACKAGE_REGISTER row PKG-050 (InterfaceTypes); ASSUMPTION |
| Constructability exclusions | TBD; no package-specific exclusions stated in source materials | PACKAGE_REGISTER row PKG-050 (Exclusions) |

## Anticipated Artifacts

- Construction work package (master document)
- Installation and tie-in workface plan
- Construction interface and turnover checklist

Source: `_CONTEXT.md`; DELIVERABLE_REGISTER row DEL-050-03 (Artifacts).

## References

- `_CONTEXT.md` (this deliverable)
- `_REFERENCES.md` (this deliverable)
- GATE-07 PROJECT_DECOMP snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `DELIVERABLE_REGISTER.csv` — row DEL-050-03
  - `PACKAGE_REGISTER.csv` — row PKG-050
  - `INTERFACE_REGISTER.csv` — location TBD (slice not extracted)
  - `OBJECTIVE_DELIVERABLE_MAP.csv` — location TBD (slice not extracted)
- `_Sources/26020-Package_Requirements.docx` heading 5 — not parseable in this run; clause-level content TBD
- `_Sources/DBM-Deepcut/` and `_Sources/DBM-Comp_and_Liquids/` — design basis materials; not slice-extracted in this run; details TBD
