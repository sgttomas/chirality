---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-08-02
package_id: PKG-08
decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@3623b958b
project_scope_refs: [SOW-042]
package_objective_refs: [OBJ-001]
---

# Scope of Work — DEL-08-02 Versioned additive API schema

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-08-02` (Versioned
additive API schema) in package `PKG-08` (API & Access). It covers project
scope item SOW-042 and supports package objective OBJ-001.

The accepted basis is `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md`
revision 1.2 (SCA-002 successor, accepted under `D-PEC-64`), pinned at commit
`3623b958b`. `_REFERENCES.md` still names revision 1.1; that phrase is
superseded provenance, as recorded in the `_CONTEXT.md` supersession line, and
is not the accepted basis for this contract.

**Objective warrant.** The attribution `DEL-08-02 → OBJ-001` was made by
SCA-002 at accepted revision 1.2 by way of SOW-042's anchor in the product
requirements document, requirement `PEC-API-003` (versioned additive API
schema). SOW-042 is not independently reinterpreted here.

Source chain, in order of authority for this contract:

1. `execution/_Decomposition/ScopeLedger.csv`, row SOW-042 — scope statement
   and its `SourceRef`:

   > SOW-042,IN,Version the API schema; evolve additively,PEC-API-003,PKG-08,DEL-08-02,OBJ-001

2. `docs/PRD.md` §9.6 (PEC-API), the ledger's cited source:

   > | PEC-API-003 | The API schema is versioned; evolution is additive. |

3. `execution/_Decomposition/SOFTWARE_DECOMP.md` §5, PKG-08 row for this
   deliverable:

   > | DEL-08-02 | Versioned additive API schema | API_CONTRACT | S | P1 | SOW-042 |

   Its `ContextEnvelopeNotes` field in `Deliverables.csv` is empty; there are no
   envelope notes to carry.

4. `execution/_Decomposition/SOFTWARE_DECOMP.md` §3, objective row:

   > | OBJ-001 | Orientation for any loop is a sub-second query with per-claim citations, not a session-length prose derivation | §3.1 | ... | DEL-00-03, DEL-01-01, DEL-02-01..07, DEL-04-01..05, DEL-08-01..04, DEL-10-01, DEL-10-04 |

5. Deliverable-local control files (`_CONTEXT.md`, `_REFERENCES.md`,
   `_DEPENDENCIES.md`, `Dependencies.csv`, `_STATUS.md`).

`DEL-08-02` is a tier-0 root node in the accepted dependency graph: it has no
upstream predecessors, so no upstream Scope of Work contributes to this
contract.

## Deliverable Definition — Ontology

- **OUT-001** — The versioned PEC API schema: the schema artifact that defines the machine-consumer request and response shapes for the PKG-08 API surface and declares the schema version those shapes belong to.
- **OUT-002** — The API schema compatibility tests: the executable checks that compare a candidate schema version against its recorded predecessor and determine whether the change is additive.

Both outputs are named by the accepted register: `Deliverables.csv` records
`AnticipatedArtifacts` for `DEL-08-02` as "Schema + compatibility tests". No
third artifact is created by this contract.

- **CLM-001** — `DEL-08-02` is typed `API_CONTRACT` in the accepted decomposition; its outputs are contract artifacts (a schema definition and the compatibility checks that police its evolution), not a running service, transport, or endpoint implementation.
- **CLM-002** — `DEL-08-02` is a root node with no upstream predecessors, and three accepted downstream relations: `DEL-08-03` (Compact citation-bearing response format) CONSUMES it, `DEL-07-05` (Shared-runtime client seam (v2)) CONSUMES it, and `DEL-10-03` (No-ruling-write verification) TESTS it. Those consumers' own scope is not defined here.
- **CLM-003** — At the time of this contract, `_STATUS.md` records lifecycle state `OPEN` and no schema artifact, version identifier, or compatibility test exists. Every statement below describes what a future implementation must satisfy; nothing here asserts that anything has been built.
- **CLM-004** — Transport binding, token-scoped access classes, latency budget, response compactness and citation-bearing form, and SSE subscription belong to sibling PKG-08 deliverables (`DEL-08-01`, `DEL-08-03`, `DEL-08-04`, `DEL-08-05`) per the accepted §5 package table; they are out of scope for `DEL-08-02`.

Unresolved information carried forward, not invented:

- **TBD-001** — `ResponsibleParty` is `TBD` in both `Deliverables.csv` and `_CONTEXT.md`; assignment occurs at WORKING_ITEMS activation.
- **TBD-002** — The concrete schema language, serialization, and repository location of OUT-001 are not fixed by the accepted basis or by `PEC-API-003`.
- **TBD-003** — The version identifier scheme (for example an integer major version versus a semantic version string) is not fixed by the accepted basis or by `PEC-API-003`.
- **TBD-004** — The concrete taxonomy of permitted additive changes, and the posture for elements that a later version supersedes but cannot remove, are not fixed by the accepted basis or by `PEC-API-003`.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — The API schema shall be versioned: OUT-001 shall carry an explicit, machine-readable version identifier that a consumer can bind to.
- **REQ-002** — Schema evolution shall be additive: each successor version of OUT-001 shall add to its predecessor without removing any published element, and without changing the meaning of any element the predecessor published.
- **REQ-003** — OUT-001 shall define the machine-consumer surface of PKG-08 so that the orientation reads OBJ-001 describes can be issued and interpreted against a named schema version rather than against an undeclared shape.
- **REQ-004** — OUT-002 shall implement an executable additive-compatibility check between a candidate schema version and its recorded predecessor, and shall fail when the candidate is not additive.

Acceptance criteria for `DEL-08-02`. Each states a property the future
implementation must exhibit; none asserts a present state.

- **AC-001** — The delivered schema declares an explicit version identifier, and any consumer can determine from the artifact alone which schema version a given request or response shape belongs to.
- **AC-002** — Every successor schema version is additive with respect to its recorded predecessor: no element published by the predecessor is removed, and no element published by the predecessor changes meaning; the concrete taxonomy of permitted additive changes remains TBD-004 and is not narrowed by this contract.
- **AC-003** — The delivered compatibility tests execute the additive check of REQ-002 against a recorded predecessor schema version, pass on an additive change, and fail on a non-additive change.
- **AC-004** — The delivered schema and compatibility tests trace to SOW-042 and OBJ-001 and introduce no scope beyond SOW-042; in particular they do not absorb the transport, access-class, latency, response-format, or subscription scope held by the sibling deliverables named in CLM-004.

## Production and Verification Method — Praxeology

- **VER-001** — Inspect the delivered schema artifact and confirm it declares an explicit version identifier that resolves the version of every request and response shape it defines.
- **VER-002** — Execute the delivered compatibility tests against the recorded predecessor schema version and confirm they pass on an additive candidate and fail on a seeded non-additive candidate (a removed element and a meaning-changing element).

Production sequence for a future implementer, bounded by the accepted basis:

1. Resolve TBD-002 and TBD-003 (schema language, location, version identifier
   scheme) as an explicit recorded decision before authoring OUT-001.
2. Author OUT-001 against REQ-001 and REQ-003, recording the initial version as
   the first predecessor baseline.
3. Resolve TBD-004 into a recorded taxonomy, then author OUT-002 against
   REQ-004 so that REQ-002 becomes machine-checkable rather than asserted.
4. Run VER-001 and VER-002 and retain their output as evidence.

Tests implement verification methods and produce evidence. They do not create
scope or acceptance criteria: OUT-002 exists because the accepted register names
it, and VER-002 is the method by which AC-003 and AC-002 are checked, not a
source of new obligations.

## Governing Values and Decisions — Axiology

- **AX-001** — The versioned-and-additive posture originates in `PEC-API-003` and enters project scope as SOW-042. This contract carries that posture without reinterpretation, extension, or softening.
- **AX-002** — The deliverable is at `OPEN` with no implementation. This contract states obligations on a future artifact; it does not certify, imply, or record that a schema exists, and it performs no lifecycle transition. `_STATUS.md` remains the sole lifecycle authority and is untouched by this run.
- **AX-003** — Unknowns are preserved as TBD-001 through TBD-004 rather than resolved by authoring judgment. Resolving them is production work or a human ruling, not contract drafting.
- **AX-004** — The accepted basis is decomposition revision 1.2 (SCA-002 under `D-PEC-64`) at commit `3623b958b`. The revision 1.1 phrase still present in `_REFERENCES.md` is a deferred pointer sweep and superseded provenance; it is recorded here so the divergence is visible rather than silently normalized.
- **AX-005** — Additive-only evolution is a constraint on this deliverable's own artifacts. It does not authorize `DEL-08-02` to constrain, define, or pre-empt the scope of the consuming deliverables named in CLM-002.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-042 OBJ-001 | REQ-001, REQ-002, REQ-003, CLM-001 | AC-001, AC-002 | VER-001, VER-002 | Delivered schema artifact with its declared version identifier, plus the recorded predecessor baseline it was compared against |
| OUT-002 | SOW-042 OBJ-001 | REQ-004, CLM-001 | AC-003 | VER-002 | Compatibility test sources and a retained run log showing a pass on an additive candidate and a failure on a seeded non-additive candidate |
| OUT-001 | SOW-042 OBJ-001 | CLM-002, CLM-003, CLM-004 | AC-004 | HUMAN_REVIEW: REVIEW gate confirms traceability to SOW-042 and OBJ-001 and confirms no absorption of sibling PKG-08 scope | Review record citing the scope-ledger row, the objective row, and the sibling deliverable boundary |
