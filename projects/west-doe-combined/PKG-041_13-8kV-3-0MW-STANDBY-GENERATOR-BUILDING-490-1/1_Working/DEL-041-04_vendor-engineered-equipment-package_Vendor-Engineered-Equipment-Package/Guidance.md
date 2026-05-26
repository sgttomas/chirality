# Guidance: DEL-041-04 — Vendor Engineered Equipment Package

## Purpose

`DEL-041-04` exists as the Package Vendor production unit for PKG-041 — the 13.8 kV, 3.0 MW standby generator building (490-1). It captures the vendor-side engineering, design, fabrication/supply, and physical package that is developed downstream of the EPC anchor deliverables (`DEL-041-01` Scope of Work and `DEL-041-02` Package Datasheet) and is fed forward into EPC review and acceptance (`DEL-041-06`).

Source: `DELIVERABLE_REGISTER.csv` (GATE-07) row `DEL-041-04`; `_CONTEXT.md`.

## Principles

- **Vendor-owned, EPC-integrated.** The Package Vendor owns engineering, design, vendor documentation, and the physical equipment package. The EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. (Source: `PACKAGE_REGISTER.csv` GATE-07 ResponsibleParty narrative.)
- **Drive from the EPC handoff.** The vendor design basis is anchored by `DEL-041-01` and `DEL-041-02`; the vendor must not re-scope the package from first principles.
- **Single coordinated physical package.** The deliverable is the engineered, fabricated, supplied physical package — not a collection of disaggregated components.
- **Interface obligations are bilateral.** Each of the twelve declared interfaces in `INTERFACE_REGISTER.csv` (GATE-07) is a vendor design input *and* an EPC integration obligation.

## Considerations

- The deliverable supports objectives `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` per the package-grouping heuristic (ASSUMPTION — see `_CONTEXT.md`).
- No deliverable-specific source slices have been copied locally (`_REFERENCES.md` Missing/Deferred). Vendor performance details (fuel, cooling, exhaust, controls, acoustic, emissions) are `TBD` and should be sourced from the EPC Package Datasheet during vendor engineering kickoff.
- Standby duty (vs. prime/continuous) is an ASSUMPTION from the package name "STANDBY GENERATOR"; confirm with the EPC Package Datasheet.
- Building 490-1 is referenced in the package name; whether the building is vendor-supplied (pre-engineered enclosure) or EPC-supplied (cast-in-place / structural building housing vendor equipment) is `TBD`.

## Trade-offs

| Trade-off | Considerations | Source/basis |
|---|---|---|
| Pre-engineered vendor enclosure vs. EPC-built structure | Vendor enclosure tightens interface scope and shortens schedule; EPC-built structure may offer better facility integration. | ASSUMPTION — building delineation not in accessible sources |
| Skidded vs. field-erected configuration | Skidded reduces field labor; field-erected may better accommodate site constraints. | ASSUMPTION |
| Vendor-standard controls vs. owner-standard SCADA/DCS interface | Vendor-standard accelerates package design; owner-standard simplifies facility integration. | ASSUMPTION — controls standard not stated in accessible sources |

## Examples

No source-grounded examples are available locally. `TBD` until deliverable-specific source slices are copied.

## Conflict Table (for human ruling)

No source conflicts identified within the accessible decomposition registers at this pass.
