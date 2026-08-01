# D-PEC-72 — PKG-00 activation record

- RunID: `D-PEC-72-PRE-P1-FOUNDATION`
- InstanceID: `D-PEC-72-PKG-00-WI-01`
- PackageID: `PKG-00`
- Package path: `projects/pec/execution/PKG-00_Architecture_Runway_Contracts`
- Selected deliverables: `DEL-00-01`, `DEL-00-03`
- Accepted basis: `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md`, revision 1.3, accepted through SCA-003
- Approval reference: D-PEC-72, owner-ruled O-B on 2026-08-01
- ResponsibleParty: `TBD` (the owner named no accountable human)
- Execution posture: serialized single-operator integration; no child session or concurrent write

## Objective

Produce the PEC v2 first ADR set and v2 SPEC seed as candidate deliverable
outputs. For OI-012, select ports-and-adapters / hexagonal isolation at PEC's
application boundary. Typed ports are capability-shaped; adapters contain
transport, store, filesystem, runtime-client, and presentation details.
Functional-core / imperative-shell remains permitted inside the bounded PEC
application and is not the selected cross-application boundary style.

## Reads

- D-PEC-72 and the selected deliverables' `ScopeOfWork.md`, `_CONTEXT.md`,
  `_REFERENCES.md`, `_STATUS.md`, and dependency records
- PRD v2.2 and accepted decomposition revision 1.3
- archived ADR source as historical evidence only
- D-PEC-58 and the surviving Root-runtime / optional-client / human-only-act
  boundary sources

## Allowed writes

- `DEL-00-01.../artifacts/v2/ADRs.md`
- `DEL-00-03.../artifacts/v2/SPEC.md`
- each selected deliverable's `_run_records/D-PEC-72_*.md`
- D-PEC-72 shared coordination targets named by the ruling packet

No source tree, software-workflow profile, lifecycle file, dependency
register, decomposition surface, PRD, frozen corpus, or other package is open.

## Work graph v1

Posture: serialized direct production and package fan-in. Nodes:

1. `A-ADR`: author ADR candidate; no predecessor; owns `ADRs.md`.
2. `A-SPEC`: author SPEC candidate; no predecessor; owns `SPEC.md`.
3. `V-PKG00`: validate both outputs against their contract mappings, path
   containment, citations, accepted basis, and open-issue preservation; depends
   on `A-ADR` and `A-SPEC`; writes only D-PEC-72 run evidence.

The two authoring nodes have disjoint files but are executed serially in this
session. Missing evidence or an acceptance-criterion mismatch holds only the
affected deliverable. Neither artifact is accepted by being written.

## Entry gate

`pec_reliance_hold.py --operation dispatch-for-production` returned `ALLOW`
for both selected contracts on 2026-08-01. Fan-in requires the same preflight.
