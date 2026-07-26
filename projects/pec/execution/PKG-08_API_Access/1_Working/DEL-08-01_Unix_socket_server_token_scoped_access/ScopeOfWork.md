---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-08-01
package_id: PKG-08
decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@3623b958b
project_scope_refs: [SOW-003, SOW-040]
package_objective_refs: [OBJ-001]
---

# Scope of Work — DEL-08-01 Unix-socket server + token-scoped access

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-08-01` — "Unix-socket
server + token-scoped access" — in `PKG-08` (API & Access) of the PEC v2 build.
It covers project scope items `SOW-003` and `SOW-040` in service of package
objective `OBJ-001`.

The accepted basis is `execution/_Decomposition/SOFTWARE_DECOMP.md`
**revision 1.2** (`current_basis`, SCA-002 successor, accepted at `D-PEC-64`
closure), pinned at commit `3623b958b`. The deliverable-local `_REFERENCES.md`
still names revision 1.1; that phrase is superseded provenance from a deferred
pointer sweep and is not the basis of this contract, as `_CONTEXT.md`'s own
supersession line records.

**Objective warrant.** The `DEL-08-01` → `OBJ-001` attribution was made by
SCA-002 and accepted at revision 1.2. It runs through the PRD anchors of this
deliverable's two scope items: `SOW-040`'s anchor `PEC-API-001` and `SOW-003`'s
anchor PRD §8 together define the API surface through which the sub-second,
per-claim-cited orientation reads named by `OBJ-001` are served. The widening to
`OBJ-001;OBJ-004` was explicitly considered and declined at the Gate 3 /
SCA-002 ruling: the `SOW-003` access-class set includes **owner**, which admits
an `OBJ-004` reading, but the dashboards serving `OBJ-004` are PKG-09
deliverables that already carry it, and this row gates the API rather than
providing the view. Single `OBJ-001` is the ruled attribution and is not
reinterpreted here.

Source chain, in order of authority for this contract:

1. `execution/_Decomposition/ScopeLedger.csv`, rows `SOW-003` and `SOW-040` —
   the scope statements and their `SourceRef` values:

   > SOW-003,IN,"Implement token-scoped access with three access classes: owner, harness, admin",§8,PKG-08,DEL-08-01,OBJ-001,DL-11,FALSE,v1.0/prototype role ontologies retired

   > SOW-040,IN,"Bind the service local-only on a Unix socket by default, token-scoped",PEC-API-001,PKG-08,DEL-08-01,OBJ-001,,FALSE,Loopback TCP is TBD (SOW-083)

2. `docs/PRD.md` §9.6 (PEC-API), the anchor cited by `SOW-040`:

   > | PEC-API-001 | The service binds local-only, Unix socket by default, with token-scoped access; any loopback TCP listener is a §16 open decision in light of D-GOV-20's no-TCP-control-listener posture. |

3. `docs/PRD.md` §8 (Users and access), the anchor cited by `SOW-003`:

   > Access is local-only (Unix socket; any loopback listener is a §16 open
   > decision), token-scoped. The v1.0 role ontology (12 roles, v1.0 §8) and
   > the prototype's implemented 14-role RBAC set (`core/src/types.ts`) are
   > retired; access classes are owner, harness, and admin.

4. `execution/_Decomposition/SOFTWARE_DECOMP.md` §5, PKG-08 row for this
   deliverable:

   > | DEL-08-01 | Unix-socket server + token-scoped access | SECURITY_CONTROL | M | P1 | SOW-003, 040 |

   with the `ContextEnvelopeNotes` field of `Deliverables.csv`:

   > OI-006 determines the token mechanism (PEC-local vs daemon registry); the
   > socket+access-class core is stable either way, but the auth half may be
   > reworked on ruling

5. `execution/_Decomposition/SOFTWARE_DECOMP.md` §3, objective row:

   > | OBJ-001 | Orientation for any loop is a sub-second query with per-claim citations, not a session-length prose derivation | §3.1 | ... | DEL-00-03, DEL-01-01, DEL-02-01..07, DEL-04-01..05, DEL-08-01..04, DEL-10-01, DEL-10-04 |

6. Deliverable-local control files (`_CONTEXT.md`, `_REFERENCES.md`,
   `_DEPENDENCIES.md`, `Dependencies.csv`, `_STATUS.md`).

`DEL-08-01` is a tier-0 root node in the accepted dependency graph: it has no
upstream predecessors, so no upstream Scope of Work contributes to this
contract.

## Deliverable Definition — Ontology

- **OUT-001** — The PEC Unix-socket server: the listener and its binding configuration, which expose the PKG-08 API surface on a local Unix domain socket as the default transport.
- **OUT-002** — The token-scoped access control: the token acceptance path and the access-class decision logic that resolves each request to exactly one of the access classes owner, harness, and admin before any operation is served.
- **OUT-003** — The automated test suite covering the socket binding and the access-class decision, implementing the verification methods declared in this contract.

The three outputs are the register's own naming: `Deliverables.csv` records
`AnticipatedArtifacts` for `DEL-08-01` as "Socket server + auth + tests". No
fourth artifact is created by this contract.

- **CLM-001** — `DEL-08-01` is typed `SECURITY_CONTROL` at Context Envelope `M` with `PhaseHint` `P1` in the accepted decomposition. Its outputs are a transport binding and an access-control decision surface; the operations served over that surface are defined by sibling deliverables, not here.
- **CLM-002** — `DEL-08-01` is a root node with no upstream predecessors (`_DEPENDENCIES.md`; `Dependencies.csv` holds only the three ANCHOR rows `DEP-08-01-001` package anchor, `DEP-08-01-002` `SOW-003` trace, `DEP-08-01-003` `SOW-040` trace). Five accepted downstream relations are recorded, all five at `PROPOSAL` stratum: `DEL-09-06` (Universal drill-down to cited source) CONSUMES `[E-N06]`, `PROPOSAL`; `DEL-10-12` (Poll-adoption measurement) MEASURES `[E-N08]`, `PROPOSAL`; `DEL-08-04` (Orientation latency budget, p95 ≤ 100 ms) TESTS `[E-P52]`, `PROPOSAL`; `DEL-10-03` (No-ruling-write verification) TESTS `[E-P54]`, `PROPOSAL`; and `DEL-08-05` (SSE delta/presence subscription) CONSUMES `[E-P58]`, `PROPOSAL`. Those consumers' own scope is not defined here.
- **CLM-003** — At the time of this contract `_STATUS.md` records lifecycle state `OPEN`, and no socket server, token mechanism, access-class logic, or test exists. Every statement below describes what a future implementation must satisfy; nothing here asserts that anything has been built.
- **CLM-004** — The access classes are exactly owner, harness, and admin, per PRD §8 and `SOW-003`. PRD §8 characterizes them: the human owner has full read over dashboards, decision slate, and presence board; harnesses (the runtime daemon and the terminal-session hooks CLI) are "machine consumers of the API on behalf of agent sessions"; agents never call PEC directly by instruction and receive harness-injected orientation as labeled data (`PEC-K-03`). PRD §8 names no equivalent characterization for admin.
- **CLM-005** — Schema versioning, response format, latency budget, and SSE subscription belong to the sibling PKG-08 deliverables `DEL-08-02` (Versioned additive API schema), `DEL-08-03` (Compact citation-bearing response format), `DEL-08-04` (Orientation latency budget), and `DEL-08-05` (SSE delta/presence subscription) per the accepted §5 package table. They are out of scope for `DEL-08-01`.
- **CLM-006** — `SOFTWARE_DECOMP.md` §8 (Context Budget QA) records `DEL-08-01` as one of two OI-coupled MEDIUM risks at `M` envelope: "DEL-08-01 (socket + tokens — OI-006 decides the auth mechanism). Held at current envelope; re-assessed on the linked ruling." The envelope is not re-assessed by this contract.

Unresolved information carried forward, not invented:

- **TBD-001** — `ResponsibleParty` is `TBD` in both `Deliverables.csv` and `_CONTEXT.md`; assignment occurs at WORKING_ITEMS activation.
- **TBD-002** — The token mechanism itself — token format, issuance, storage, presentation, expiry, and rotation — is not fixed by any accepted source, because the PEC-local-versus-daemon-registry choice is CON-001.
- **TBD-003** — The socket path, filesystem permissions, and wire framing of OUT-001 are not fixed by the accepted basis, by `PEC-API-001`, or by PRD §8.
- **TBD-004** — The mapping from individual API operations to the three access classes is not fixed by any accepted source; PRD §8 characterizes owner and harness in general terms and characterizes admin not at all.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — The service shall bind local-only, on a Unix domain socket as the default transport, per `SOW-040` and `PEC-API-001`.
- **REQ-002** — Access shall be token-scoped: every request shall present a token that resolves to exactly one access class before any operation is served, and a request whose token is absent, unresolvable, or not valid shall be refused rather than served at a reduced scope.
- **REQ-003** — The delivered access-class set shall be exactly owner, harness, and admin, per `SOW-003` and PRD §8.
- **REQ-004** — No role or permission ontology beyond those three access classes shall be delivered. The v1.0 12-role ontology and the prototype's implemented 14-role RBAC set are retired, per the `SOW-003` ledger note and PRD §8; neither may be carried forward as code, configuration, or identifier.
- **REQ-005** — No loopback TCP listener shall be delivered under this contract. The loopback question is carried as `SOW-083` (`OI-009`) and stated in `PEC-API-001` itself as a §16 open decision "in light of D-GOV-20's no-TCP-control-listener posture"; see CON-002.
- **REQ-006** — The token mechanism shall be separable from the socket server and from the access-class decision logic, sitting behind a declared internal seam, so that a later `OI-006` ruling reworks the auth half without reworking the socket-and-access-class core. This requirement carries the accepted `ContextEnvelopeNotes` position; it does not choose a mechanism.
- **REQ-007** — Tests shall implement the verification methods declared in this contract. They shall not define scope, requirements, or acceptance criteria.

Acceptance criteria for `DEL-08-01`. Each states a property the future
implementation must exhibit; none asserts a present state.

- **AC-001** — The delivered service binds a Unix domain socket as its default listener, is reachable only through that local socket, and binds no network-reachable listener; the socket path and permissions chosen during production are recorded, and remain TBD-003 in this contract.
- **AC-002** — Every operation served over the socket is preceded by a token resolution that yields exactly one access class; a request with an absent, unresolvable, or invalid token is refused, with no operation served and no partial or default-scoped result returned.
- **AC-003** — The delivered access-class set is exactly owner, harness, and admin; no identifier from the retired v1.0 12-role ontology or the retired prototype 14-role RBAC set appears in the delivered code, configuration, or fixtures.
- **AC-004** — The token mechanism is reachable only through a declared internal seam, such that replacing it with the alternative named in CON-001 changes no socket-server and no access-class decision code; CON-001 remains open and no delivered artifact may be read as settling it.
- **AC-005** — No loopback or other TCP listener is delivered, and no delivered artifact presumes the outcome of `SOW-083` / `OI-009`; CON-002 remains open.
- **AC-006** — The automated test suite implements VER-001 through VER-004, executes in the service test run, passes, and introduces no acceptance criterion absent from this contract.
- **AC-007** — The delivered artifacts trace to `SOW-003`, `SOW-040`, and `OBJ-001` and introduce no scope beyond those two ledger rows; in particular they do not absorb the schema, response-format, latency, or subscription scope held by the sibling deliverables named in CLM-005, and the operation-to-access-class mapping applied during production is recorded against TBD-004 rather than asserted as accepted scope.

Unresolved constraints carried into this contract, neither resolved nor
narrowed by authoring:

- **CON-001** — The token mechanism is undecided. `SOFTWARE_DECOMP.md` §10 (Open Issues) carries the disposition of record verbatim: "| OI-006 | SOW-080 | §16.6 auth reuse undecided | §16 ruling |". `SOW-080` states the question as "Auth reuse: PEC tokens vs the daemon's project-scoped token registry" with `InOutStatus` `TBD`, `OpenIssue` `TRUE`, and the ledger note "OI-006. Affects SOW-003 implementation choice"; PRD §16.6 states the same. `SOFTWARE_DECOMP.md` §8 records the consequence for this deliverable: the socket-and-access-class core is stable either way, but the auth half may be reworked on the ruling, and the deliverable is held at `M` envelope at MEDIUM risk pending it. Nothing in this contract resolves `OI-006`, and no output may be read as settling it.
- **CON-002** — The transport question beyond the Unix socket is undecided. `SOW-040`'s ledger note records "Loopback TCP is TBD (SOW-083)"; `SOW-083` is `InOutStatus` `TBD`, `OpenIssue` `TRUE`, and states "Event-contract home ... and API transport (Unix socket only vs additional loopback listener)" against PRD §16.9 with the note "OI-009. Fenced: PEC builds local-first either way (SOW-034/040)". `PEC-API-001` itself defers the loopback listener to §16. This contract delivers the Unix-socket default only and does not resolve `OI-009`.

## Production and Verification Method — Praxeology

Production proceeds in the order socket binding → access-class decision →
token seam → tests, because the access-class decision is the acceptance surface
of the transport, and the seam of REQ-006 is what keeps CON-001 cheap. All work
is bounded to the deliverable's own service source; this contract authorizes no
register, decomposition, or PRD edit.

- **VER-001** — Start the delivered service and enumerate its bound listeners; confirm a Unix domain socket listener exists and is the default, confirm no TCP or otherwise network-reachable listener is bound, and record the socket path and its filesystem permissions.
- **VER-002** — Exercise the access path with a token for each of owner, harness, and admin and confirm each resolves to exactly one class; then exercise it with absent, malformed, unresolvable, and invalid tokens and confirm each is refused with no operation served and no partial or default-scoped result.
- **VER-003** — Inspect the delivered source, configuration, and fixtures for identifiers belonging to the retired v1.0 12-role ontology or the retired prototype 14-role RBAC set, and confirm the delivered access-class set is exactly owner, harness, and admin.
- **VER-004** — Inspect the module boundary between the token mechanism and the socket-and-access-class core: confirm the mechanism is reached only through the declared seam interface, and confirm by substituting a stub mechanism through that seam that no socket-server or access-class decision code changes.
- **VER-005** — Run the service test suite and confirm that each of VER-001 through VER-004 has a corresponding executing automated test, that the suite passes, and that no test asserts a criterion absent from this contract.

Tests implement verification methods and produce evidence. They do not create
scope or acceptance criteria: OUT-003 exists because the accepted register names
it, and VER-005 is the method by which AC-006 is checked, not a source of new
obligations.

## Governing Values and Decisions — Axiology

- **AX-001** — Local-only, token-scoped access originates in `PEC-API-001` and PRD §8 and enters project scope as `SOW-040` and `SOW-003`. This contract carries that posture without reinterpretation, extension, or softening; in particular, "Unix socket by default" is not read as licensing a second default transport.
- **AX-002** — `DL-11` is the decision that assigned `SOW-003` (access classes) to `PKG-08` "with the token-scoped transport" rather than to a separate access-control package. The access classes and the socket binding are therefore one deliverable by ruling, not by authoring convenience.
- **AX-003** — Retirement is a governing constraint, not a stylistic preference. PRD §8 retires the v1.0 12-role ontology and the prototype's implemented 14-role RBAC set explicitly; REQ-004 and AC-003 exist so that the retired sets cannot re-enter through carried prototype code, which PRD §7.3 permits only as pattern and never as code.
- **AX-004** — The deliverable is at `OPEN` with no implementation. This contract states obligations on future artifacts; it does not certify, imply, or record that anything exists, and it performs no lifecycle transition. `_STATUS.md` remains the sole lifecycle authority and is untouched by this run.
- **AX-005** — Unknowns are preserved as TBD-001 through TBD-004 and as CON-001 and CON-002 rather than resolved by authoring judgment. `OI-006` and `OI-009` close by owner §16 ruling; resolving TBD items is production work. Neither is contract drafting.
- **AX-006** — The accepted basis is decomposition revision 1.2 (SCA-002, accepted at `D-PEC-64`) at commit `3623b958b`. The revision 1.1 phrase still present in `_REFERENCES.md` is a deferred pointer sweep and superseded provenance; it is recorded here so the divergence is visible rather than silently normalized.
- **AX-007** — `C-04` PHASE_PRECEDENCE and `C-10` STRATUM_RULE are register-wide non-gating constraints recorded in `_DEPENDENCIES.md`. The `P1` phase hint is release-strategy ordering, and all five downstream edges in CLM-002 (E-N06, E-N08, E-P52, E-P54, E-P58) are `PROPOSAL` stratum, accepted as presented under `D-PEC-62` §1(4) and carrying no exhibit flag. Stratum is provenance, not authority — it records how an edge was derived, not whether it has been accepted — and blocker output is advisory visibility only, never work assignment.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-040 OBJ-001 | REQ-001, REQ-005, CLM-001, CLM-005 | AC-001, AC-005 | VER-001 | Listener enumeration from the started service showing the Unix socket default and the absence of any network-reachable listener, plus the recorded socket path and permissions |
| OUT-002 | SOW-003 OBJ-001 | REQ-002, REQ-003, REQ-004, REQ-006, CLM-004, CLM-006 | AC-002, AC-003, AC-004 | VER-002, VER-003, VER-004 | Token-resolution transcripts for each access class and for each rejection case, an identifier scan of source/config/fixtures against the retired role sets, and the seam interface signature plus the stub-substitution diff |
| OUT-003 | SOW-003 OBJ-001 | REQ-007, CLM-003 | AC-006 | VER-005 | Service test-run output mapping each executed test to its declared verification method |
| OUT-001 | SOW-003 SOW-040 OBJ-001 | CLM-002, CLM-005 | AC-007 | HUMAN_REVIEW: REVIEW gate confirms traceability to SOW-003, SOW-040, and OBJ-001, confirms no absorption of sibling PKG-08 scope, and confirms CON-001 and CON-002 are left open | Review record citing the two scope-ledger rows, the objective row, the sibling deliverable boundary, and the recorded operation-to-access-class mapping against TBD-004 |
