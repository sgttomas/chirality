# PEC v2 — first architecture decision records

**Authority status:** architecture selection is owner-ruled by D-PEC-72 O-B.
Artifact-fitness and lifecycle dispositions are recorded separately on the
governed REVIEW, owner-ruling, and `_STATUS.md` surfaces; this file does not
enact those acts.

**Accepted basis:** `projects/pec/docs/PRD.md` v2.2 and
`projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.3 at
`11a494e9a`, accepted through SCA-003.

## ADR-PEC-V2-001 — Hexagonal application isolation

- Status: DECIDED by D-PEC-72 O-B
- Date: 2026-08-01
- Resolves: OI-012
- Scope item: SOW-088
- Objective: OBJ-005

### Context

PEC v2 is a deterministic coordination-plane service whose record tier is a
rebuildable projection of governed file truth and whose presence tier is
operational and disposable. The PRD requires graceful absence, file-native
authority, best-effort ingest with guaranteed reconciliation, explainable
derivations, content-minimal data, and a zero-third-party-dependency service
core (`PEC-K-01`, `PEC-K-02`, `PEC-K-07`, `PEC-K-08`, `PEC-K-10`,
`PEC-SVC-001`; `SOW-052`, `SOW-055`, `SOW-056`).

The accepted Gate-4 basis records two conforming isolation styles. It also
records a package grain congruent with hexagonal isolation: core behavior in
PKG-03/04/05 with PKG-01 entities; driven edges in PKG-02/06 and the store;
driving edges in PKG-07/08/09. The entity-schema/core versus
store-persistence/adapter seam inside PKG-01 is the boundary that must remain
explicit (`SOFTWARE_DECOMP.md` OI-012; `DEL-00-01` CLM-006 and REQ-006).

D-PEC-72's owner ruling selected O-B after recording the intended architectural
reason: independently replaceable applications should communicate through
typed contracts. That broader intent is rationale here; this PEC decision has
normative effect only inside the PEC v2 boundary.

### Decision

PEC v2 uses **ports and adapters (hexagonal isolation)** at its application
boundary.

1. PEC domain and application behavior depend inward on PEC-owned capability
   contracts. Transport, filesystem, Git, persistence, runtime-client, event,
   and presentation implementations remain adapters and do not become domain
   dependencies. This applies the accepted PKG-03/04/05 + PKG-01-entity core
   grain and PKG-02/06/store + PKG-07/08/09 edge grain (OI-012).
2. Ports are named for capabilities or use cases, not for the current external
   actor. An adapter may bind App, Root, Task Management, a domain application,
   CLI, daemon, socket, filesystem, store, or dashboard to such a port, but
   those actor names do not enter the PEC core merely because they are the
   first consumers or providers. This is an architectural interpretation of
   the selected O-B style, not a new consumer duty (`PEC-K-03`, `PEC-K-11`).
3. Where the accepted product already requires a cross-boundary schema, the
   port contract is typed and versioned. Commands, queries, events, results,
   errors, and compatibility behavior belong to that contract to the extent
   required by `PEC-STR-002`, `PEC-API-003`, `SOW-034`, and `SOW-042`.
   This ADR does not decide the open contract-home or transport choices in
   OI-009.
4. Runtime interaction may be bidirectional, but source dependencies point
   inward: an adapter implements a core-owned port; the core never imports an
   adapter. Composition is an outer-shell concern.
5. Functional-core / imperative-shell remains the preferred internal
   implementation technique where it fits deterministic derivation. It is
   compatible with this decision: pure transformations can form the interior
   of a use case, while the hexagonal boundary governs interaction between PEC
   and replaceable external implementations.
6. Inside PKG-01, record- and presence-tier entity schemas are core-facing.
   Store connection, schema migration, query dialect, transaction handling,
   and physical persistence are adapter concerns behind a core-owned
   persistence port. A candidate change that alters an entity's domain meaning
   is core; one that changes only how the same meaning is stored or retrieved
   is adapter work (`SOW-001`, `SOW-002`, `SOW-056`).
7. The core remains free of third-party runtime dependencies. Workspace-local
   typed contract packages are permitted only as allowed by `PEC-SVC-001` and
   `SOW-052`; this decision does not select their repository home.

### Consequences

- Filesystem grammars, the projection store, Git observation, daemon/hook/cmux
  bridges, Unix-socket/API transport, and dashboards can be replaced without
  changing PEC's domain/application behavior, provided their adapters continue
  to satisfy the applicable typed port contracts.
- Tests can exercise the core through in-memory port implementations and run
  contract suites against real adapters. The exact test artifacts remain with
  their accepted deliverables; this ADR creates no new deliverable.
- More interfaces and composition wiring are expected than under a single
  imperative shell. Ports are created only for accepted capabilities, not for
  speculative actors or transports.
- No universal shared-types package is selected. Contract ownership and home
  remain governed by accepted scope and the unresolved placement decisions.

### Alternatives considered

- **Functional core / imperative shell as the complete isolation posture:**
  conforming to the forced invariants and lighter for one deterministic
  service, but not selected because the owner requires explicit typed
  boundaries supporting interchangeable applications.
- **Direct application-to-application implementation dependencies:** rejected
  because they defeat the selected isolation style and make replacement depend
  on another application's internals.

### Non-decisions

This ADR decides none of OI-001 through OI-009 or OI-013. It creates no
architecture mandate for App, Root, Task Management, Piping, or another loop;
those owners require their own instruments. It creates no source tree,
software-workflow profile, runtime dependency, API transport, contract home,
or P1 implementation authority.

## ADR-PEC-V2-002 — Carried runtime and dependency postures

- Status: CARRIED POSTURES RECORDED
- Date: 2026-08-01
- Scope item: SOW-088
- Sources: archived ADR-002 and ADR-014 (historical corpus), D-PEC-56,
  D-PEC-58, PRD v2.2 §§4, 10, 13, and 15

### Context

The frozen v0.4 ADR catalogue is historical evidence, not present authority.
The accepted v2 basis requires the first ADR set to re-cite ADR-002 in its v2
carried form, cite ADR-014 only as lineage, and state the surviving
Root-runtime / optional-client / human-only-act boundary (`SOW-088`;
`DEL-00-01` REQ-003..005).

### Carried posture

1. **ADR-002 is the sole live carried posture from the archived ADR set.** Its
   relevant v2 form is `PEC-SVC-001`: the service core has zero third-party
   runtime dependencies, while workspace-internal runtime-contract packages
   are permitted (`SOW-052`). Re-citation carries that dependency posture; it
   does not restore the archived ADR's complete TypeScript, Node-version,
   router, database, or web-toolchain allocation.
2. **ADR-014 is historical lineage only.** It records the v0.4 migration toward
   Root-owned generic runtime semantics. D-PEC-58 explicitly retired its
   allocation of deterministic acts, RBAC, reporting, visibility, and data
   boundaries to an old PEC project-adapter service. That allocation is not a
   PEC v2 requirement and is not re-adopted here.
3. **The surviving live boundary is independent of ADR-014:** Root owns generic
   runtime semantics including sessions, delegation, turn locks, credentials,
   interruption, and model residency; PEC is an optional client and starts no
   second execution loop; adoption, ruling, acceptance, rejection, force, and
   other human-only acts remain unavailable to agents (`D-PEC-56` behaviors
   2, 4, and 7 as limited by `D-PEC-58` behavior 8; PRD v2.2 §4.2 and §15).
4. PEC's runtime-client seam is an adapter under ADR-PEC-V2-001. It does not
   transfer Root runtime ownership into PEC and does not restore the retired
   v0.4 project-adapter allocation (`SOW-087`).

### Consequences and boundary

ADR-002 alone is cited as a live carried posture. ADR-014 and every other
archived ADR remain historical. No archived v0.4 source, dependency, database,
RBAC design, reporting surface, or runtime ownership becomes live through this
record.

## Deliverable authority boundary

D-PEC-72 selected the architecture before these bytes existed. Whether these
ADR bytes satisfy the mapped `AC-*`/`VER-*` criteria and are fit as the
deliverable artifact is established only through REVIEW and a separate owner
act recorded on their governed surfaces. This file neither records nor implies
that disposition, advances `_STATUS.md`, or closes C-05.
