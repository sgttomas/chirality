# Guidance: DEL-032-03_construction-work-package

## Purpose

This Construction Work Package exists so that the cathodic protection (CP) system for `PKG-032` is physically installed, inspected, tied into the larger 03-25 Comp and Liquids facility, and turned over to operations in a controlled and auditable way. The DBM identifies cathodic protection as in-scope electrical work for the facility (line 718, 770), but does not by itself specify *how* CP is constructed; this deliverable carries the construction-execution intent for that scope.

Source: `_CONTEXT.md`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Electrical Design Scope.

## Principles

- **Construction follows decomposition truth.** The package responsibility model (`PACKAGE_REGISTER.csv` row `PKG-032`) places package engineering/design and the physical equipment package with the Package Vendor; construction execution and facility integration sit with the EPC Integrator. The construction work package treats vendor design as the input, not as something to be re-derived during construction.
- **Source-grounded, not invention-driven.** Where the accessible source slices do not state a value (CP type, anode count, rectifier rating, acceptance potentials), this deliverable carries the gap as `TBD` rather than inventing engineering basis.
- **Interface discipline.** The four declared interfaces for `PKG-032` (Electrical Power; Grounding/Bonding; I&C/Control Cabling; Communications/Network) are construction-execution drivers, not paperwork artifacts.
- **CP-to-grounding coordination is the critical electrical-interface concern.** Bonding a CP-protected asset directly to a low-resistance ground grid without isolation typically degrades CP effectiveness; construction shall preserve the isolation strategy from the vendor design.

## Considerations

- **Construction Responsibility model (DBM).** Facility construction scope includes grading, piling, foundations, home-run cabling, terminations, and area lighting (`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, line 75). CP installation fits within this construction scope as an electrical sub-scope.
- **Winterization.** Site basis -40 deg C to +35 deg C drives trenching schedule, anode bed installation method, and rectifier shelter design (line 145).
- **Geotechnical caveat.** Foundation values are design placeholders pending the final geotechnical report (line 141). Anode bed civil execution and rectifier shelter foundations carry the same caveat.
- **Tie-in sequencing.** Several CP elements (test-station leads at vessel/tank nozzles, anode connections to buried piping, isolation flange kits) must be installed before the protected asset is buried, insulated, or otherwise inaccessible. Construction sequencing shall recognize this even though the source DBM does not state it.
- **Interface protocol selection.** Communications protocol for CP remote monitoring may use plant Modbus TCP/IP integration via Kepware KepserverEX, or a Redlion DA30D protocol converter where appropriate (`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, line 812). Selection should follow vendor capability.
- **Decomposition narrative is directional, not authoritative.** Package-grouped objective associations (OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010) are recorded as context per `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC`; treat them as best-effort context, not requirements (ASSUMPTION).

## Trade-offs

- **Impressed-current vs. galvanic CP.** Not specified in accessible sources for `PKG-032`. Trade-offs include initial cost, ongoing maintenance, ground-grid interaction, and applicability to soil resistivity and protected-asset size. Detail `TBD` pending vendor design.
- **Deep-well anode bed vs. surface horizontal bed.** Civil/construction impact differs significantly (drilling rig mobilization vs. trench-and-backfill). Selection is a vendor design output; construction shall plan for either possibility until vendor design is accepted.
- **Schedule risk on test-station installation.** Installing test stations early increases coordination burden with civil/piping crews but is required to avoid rework on buried assets.

## Examples

`TBD`. No examples extracted from accessible source slices for this deliverable.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONFLICT-032-03-01 | None identified at Pass 2: source-slice content for `PKG-032` is limited; conflicts may emerge once vendor CP design is accepted. | n/a | n/a | n/a | Surface during P3 / vendor handoff | TBD |

## Notes on unresolved items

- HRR-032-03-001 — CP system type (impressed-current vs. galvanic), anode-bed geometry, rectifier rating/count, and protected-asset list are not specified by accessible source slices for `PKG-032`. Proposed handling: keep these values `TBD` and resolve from the vendor engineered equipment package (`DEL-032-04`) when accepted.
- HRR-032-03-002 — CP-to-ground-grid isolation strategy is a critical construction concern but is not explicitly directed by the DBM for cathodic protection. Proposed handling: carry as ASSUMPTION pending vendor design ruling.
- HRR-032-03-003 — Project electrical specifications, project painting/coating/corrosion specifications, and CP-specific NACE/AMPP standards are referenced indirectly; document paths and clause-level applicability remain `location TBD` pending source extraction.
