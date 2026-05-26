# Datasheet — DEL-070-03 Construction Work Package (Mole Sieve Drier Unit, NGL)

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-070-03_construction-work-package |
| Deliverable Name | Construction Work Package |
| ParentPackageID | PKG-070 |
| Package Name | Mole Sieve Drier Unit (NGL) |
| Package Tag (Source) | 26020-01-PT-22-003 |
| Discipline | Mechanical |
| Type | EPC Construction Work Package |
| Responsible Party | EPC Integrator |
| Authority Snapshot | GATE-07_Final_Published_2026-05-24 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package function | NGL molecular sieve dehydration package | `_Sources/26020-Package_Requirements.docx` heading `26020-01-PT-22-003`, Basic Scope |
| Tower configuration | Three-tower (one adsorbing, one regenerating, one standby) | same, Basic Scope |
| Rated capacity | 2,385 m³/d (15,000 bbl/d) | same, Basic Scope |
| Service | Water-saturated C3+ NGL | same, Basic Scope |
| Outlet water spec | < 7 ppmw | same, Basic Scope |
| Construction status basis | "4-25 NGL service; vetted package scope basis" | same, Location / Status |
| Scope items covered | SOW-0145, SOW-0146, SOW-0147, SOW-0148 | DELIVERABLE_REGISTER.csv row 410 |
| Objectives supported | OBJ-001, OBJ-003 .. OBJ-010 | DELIVERABLE_REGISTER.csv row 410 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Adsorption inlet pressure (design) | 1,978 kPag | source Scope Notes / Operating conditions |
| Adsorption outlet pressure (design) | 1,943 kPag | source Scope Notes / Operating conditions |
| Adsorption inlet temperature | 29.7 °C low / 46.3 °C design / 51.8 °C high | source Scope Notes / Operating conditions |
| Adsorption inlet water | Saturated at design inlet conditions and flow | source Scope Notes / Operating conditions |
| Adsorption bed dP (start of life) | < 4 psid / 27.6 kPad | source Scope Notes / Design conditions |
| Adsorption bed dP (end of life) | < 10 psid (including vessel nozzles) | source Scope Notes / Design conditions |
| Adsorption cycle | 24 hours | source Scope Notes / Cycle basis |
| Regeneration cycle duration | TBC by vendor | source Scope Notes / Cycle basis |

## Construction

Construction attributes asserted from source scope and physical interface table; construction-method specifics (rigging, sequencing, schedule) are TBD pending discipline construction planning.

| Construction Attribute | Value | Source |
|---|---|---|
| Major in-scope equipment to install | Inlet liquid/liquid coalescer with level control; 3x molecular sieve dehydration vessels (3A sieve, silica gel layer, internals, valves, drains); regeneration-gas heater, aerial cooler (split-header, winterized with recirculation louvers, intake louvers, plenum heater), three-phase regen scrubber with mist pad and relief; outlet particulate filter; moisture analyzer with vaporizing regulator; heated building/enclosure for inlet coalescer, inline mixers, settling vessel and regen scrubber as required | source Major Included Equipment |
| Battery-limit tie-ins (in scope) | Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; Area / Exterior Lighting; EHT; Grounding / Bonding; I&C / Control Cabling; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports | source Physical Interface Summary (Applicability = Yes rows) |
| Battery-limit interfaces (not applicable) | Utility Piping; Cathodic Protection; Communications / Network; Building HVAC / Services; Grading / Site Drainage / Spill Containment; Product Loading; Pipeline / Pigging | source Physical Interface Summary (Applicability = No rows) |
| By-others scope explicitly outside this package | Upstream NGL mercaptan treating and caustic process-provider design; downstream NGL storage bullets, NGL loading, LACT, product export; downstream sales-gas and stabilizer-overheads compression; produced-water tank/drain header/facility drain beyond package nozzles/tie-ins; flare header | source Scope Notes / Open Items |
| Construction sequence / workface plan | TBD — to be developed from final vendor general arrangement and site plot plan | ASSUMPTION (not in source) |
| Lifting / handling study reference | MEC-018 vendor deliverable | source Vendor Engineering Deliverables |
| Hydrotest / pressure-test package reference | PIP-024 vendor deliverable | source Vendor Engineering Deliverables |
| Flushing / cleaning / drying procedure reference | PIP-025 vendor deliverable | source Vendor Engineering Deliverables |
| Equipment installation / setting drawings reference | MEC-017 vendor deliverable | source Vendor Engineering Deliverables |
| FAT / SAT references | MEC-021/MEC-022 (mechanical), ELE-029/ELE-030 (electrical) | source Vendor Engineering Deliverables |
| Site preparation / civil scope (foundations, anchor bolts, embedments) | STR-005, STR-006, STR-013, CIV-014 | source Vendor Engineering Deliverables |
| Construction interface coordination notes | TBD (source records "Interface Coordination Notes: TBD.") | source Interface Coordination Notes |

## References

- `_Sources/26020-Package_Requirements.docx`, package heading `26020-01-PT-22-003 - Mole Sieve Drier Unit (NGL)` (Basic Scope; Major Included Equipment; Scope Notes / Open Items; Physical Interface Summary; Vendor Engineering Deliverables; Interface Coordination Notes)
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` (interface source referenced by package heading; row 74 cited for Area / Exterior Lighting note) — location TBD inside workbook
- DELIVERABLE_REGISTER.csv row 410 (DEL-070-03), `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (this deliverable folder)
