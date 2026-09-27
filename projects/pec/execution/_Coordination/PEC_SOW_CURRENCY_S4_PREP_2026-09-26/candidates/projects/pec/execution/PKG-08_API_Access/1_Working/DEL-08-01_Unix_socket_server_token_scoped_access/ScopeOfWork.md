---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-08-01
package_id: PKG-08
decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@189f205ff02df4111b33c20be441ce06e65ada7a
project_scope_refs: [SOW-003, SOW-040]
package_objective_refs: [OBJ-001]
---

# Scope of Work — DEL-08-01 Unix-socket server + token-scoped access

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-08-01` — "Unix-socket
server + token-scoped access" — in `PKG-08` (API & Access) of the PEC v2 build.
It covers project scope items `SOW-003` and `SOW-040` in service of package
objective `OBJ-001`. It replaces as a whole the contract with SHA-256
`8ac1dc050efb…3d76` (AX-010).

The accepted basis is `execution/_Decomposition/SOFTWARE_DECOMP.md`
**revision 1.6** (`current_basis`, SCA-006 successor), accepted by the owner at
SCA-006 checkpoint group 3 on 2026-09-26. The frontmatter pin
`189f205ff02df4111b33c20be441ce06e65ada7a` is the checkpoint-3 acceptance
commit, an ancestor of `origin/main`. At that commit `SOFTWARE_DECOMP.md` has
SHA-256 `9374c21fb87b…8eb1`, `Deliverables.csv` `94ee5d182ae9…9805`,
`ScopeLedger.csv` `1d24a4b86f05…916e` and `ContextBudgetQA.csv`
`93b0bb075a0e…4c7c`, and `docs/PRD.md` v2.4 has SHA-256 `ae49b8065698…3fbe`.

**Observation commit.** The pin binds the accepted decomposition bytes only.
Unless a claim names another commit, every statement below about the state of
a file, record, lifecycle or decision is an observation at `origin/main`
`125cfacc1`. There the four decomposition files and the PRD
named above are byte-identical to the pin. At `125cfacc1` the deliverable-local
`_CONTEXT.md` carries the revision-1.6 register `Description` and a provenance
tail ending at revision 1.6, and `_REFERENCES.md` names revision 1.6 and PRD
v2.4.

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

   > SOW-003,IN,"Implement token-scoped access with four access classes: owner, harness, agent (read-only query for tool calls), admin",§8,PKG-08,DEL-08-01,OBJ-001,DL-11; SCA-006,FALSE,v1.0/prototype role ontologies retired

   > SOW-040,IN,"Bind the service local-only on a Unix socket by default, token-scoped",PEC-API-001,PKG-08,DEL-08-01,OBJ-001,,FALSE,Loopback TCP is TBD (SOW-083)

2. `docs/PRD.md` §9.6 (PEC-API), the anchor cited by `SOW-040`:

   > | PEC-API-001 | The service binds local-only, Unix socket by default, with token-scoped access; any loopback TCP listener is a §16 open decision in light of D-GOV-43 A2 (no network-exposed listener), superseding D-GOV-20 item 4. |

3. `docs/PRD.md` §8 (Users and access), the anchor cited by `SOW-003`:

   > Access is local-only (Unix socket; any loopback listener is a §16 open
   > decision), token-scoped. The v1.0 role ontology (12 roles, v1.0 §8) and
   > the prototype's implemented 14-role RBAC set (`core/src/types.ts`) are
   > retired; access classes are owner, harness, agent, and admin. The `agent`
   > class is read-only query access for tool calls: orientation, deltas, gate
   > verdicts, decision-slate and presence reads, with no event ingest, no
   > presence reports and no admin act. Every class is local-only and
   > token-scoped; the token mechanism, including credentials for the `agent`
   > class, is the open §16.6 decision.

4. `execution/_Decomposition/SOFTWARE_DECOMP.md` §5, PKG-08 row for this
   deliverable:

   > | DEL-08-01 | Unix-socket server + token-scoped access | SECURITY_CONTROL | M | P1 | SOW-003, 040 |

   with the `ContextEnvelopeNotes` field of `Deliverables.csv`:

   > OI-006 determines the PEC-local token mechanism (Runtime token registries
   > are private to each application's Runtime instance, so no shared registry
   > exists to reuse); the socket+access-class core is stable either way, but
   > the auth half may be reworked on ruling

5. `execution/_Decomposition/SOFTWARE_DECOMP.md` §3, objective row:

   > | OBJ-001 | Orientation for any loop is a sub-second query with per-claim citations, not a session-length prose derivation | §3.1 | SOW-001, SOW-003..009, SOW-011..017, SOW-038, SOW-040..044, SOW-089, SOW-095..099; instruments: SOW-058, SOW-059, SOW-063, SOW-100 | DEL-00-03, DEL-01-01, DEL-02-01..09, DEL-03-05, DEL-04-01..05, DEL-08-01..06, DEL-10-01, DEL-10-04, DEL-10-08, DEL-10-13 |

6. Deliverable-local control files (`_CONTEXT.md`, `_REFERENCES.md`,
   `_DEPENDENCIES.md`, `Dependencies.csv`, `_STATUS.md`).

`DEL-08-01` is a tier-0 root node in the accepted dependency graph: it has no
upstream predecessors, so no upstream Scope of Work contributes to this
contract.

## Deliverable Definition — Ontology

- **OUT-001** — The PEC Unix-socket server: the listener and its binding configuration, which expose the PKG-08 API surface on a local Unix domain socket as the default transport.
- **OUT-002** — The token-scoped access control: the token acceptance path and the access-class decision logic that resolves each request to exactly one of the access classes owner, harness, agent, and admin before any operation is served.
- **OUT-003** — The automated test suite covering the socket binding and the access-class decision, implementing the verification methods declared in this contract.

The three outputs are the register's own naming: `Deliverables.csv` records
`AnticipatedArtifacts` for `DEL-08-01` as "Socket server + auth + tests". No
fourth artifact is created by this contract.

### Identity of record

- **CLM-001** — `DEL-08-01` is typed `SECURITY_CONTROL` at Context Envelope `M` with `PhaseHint` `P1` in the accepted decomposition. Its outputs are a transport binding and an access-control decision surface; the operations served over that surface are defined by sibling deliverables, not here.
- **CLM-007** — `DEL-08-01` is named "Unix-socket server + token-scoped access", `ResponsibleParty` `TBD`, `CoversScopeItems` `SOW-003;SOW-040`, `SupportsObjectives` `OBJ-001` (`Deliverables.csv` row `DEL-08-01`). Its register `Description` reads "Local-only Unix-socket binding with token-scoped access classes (owner, harness, agent, admin; agent is read-only query for tool calls); auth-reuse choice tracked by OI-006." SCA-006 amendment A-31 gave it that text. The deliverable-local `_CONTEXT.md` carries the same text, and the consumer rows `DEP-09-06-003` and `DEP-10-03-003` quote it as their `EvidenceQuote`, refreshed under `D-PEC-101`. The folder was scaffolded under `D-PEC-62` and holds no `MEMORY.md`.
- **CLM-004** — The access classes are exactly owner, harness, agent, and admin, per PRD §8 and `SOW-003`. PRD §8 characterizes them: the human owner has full read over dashboards, decision slate, and presence board; explicitly PEC-enabled harnesses may act as machine consumers of the API on behalf of agent sessions, and the hooks CLI is also a producer of presence and status events; the `agent` class is "read-only query access for tool calls: orientation, deltas, gate verdicts, decision-slate and presence reads, with no event ingest, no presence reports and no admin act". Under `PEC-K-03`, whether and when a consumer requests orientation and whether it injects labeled PEC data are consumer-owned decisions; no polling, cadence, contact, or injection duty follows from the access class. PRD §8 names no equivalent characterization for admin.
- **CLM-008** — PRD §8 states how agents use PEC data on either path:

> - **Agents** — may act on PEC data received through an explicitly enabled
>   consumer, and may query PEC directly through tool calls under the
>   read-only `agent` access class (PEC-API-007) where that surface is
>   enabled. Either way they act on labeled, non-authoritative data under
>   operational reliance within the declared envelope (PEC-K-03,
>   PEC-ORI-007), never as authority (PEC-K-02), and only from a release that
>   has passed the §12 reliance-advertisement gate. Enabling any path is
>   consumer-owned; injection is not required, and no agent, harness or loop
>   is required to query PEC (PEC-K-01, PEC-K-11).

  `PEC-API-007` offers the tool-call query interface "under the `agent` access class" as a "P3 capability". An access class decides which operations a token may reach. It grants no operational reliance, which is available only from a PEC release that has passed the PRD §12 reliance-advertisement gate, and it never makes PEC output citable as authority (AX-008).
- **CLM-006** — `SOFTWARE_DECOMP.md` §8 (Context Budget QA) records `DEL-08-01` as one of two OI-coupled MEDIUM risks at `M` envelope: "DEL-08-01 (socket + tokens — OI-006 decides the PEC-local token mechanism; no shared Runtime token registry exists to reuse). Held at current envelope; re-assessed on the linked ruling." `ContextBudgetQA.csv` rates it `Risk` `MEDIUM` with the recommended action "Hold envelope; re-assess on the linked OI's ruling". SCA-006 Impact Assessment §9.2 keeps it at `M` and MEDIUM: "the agent class is one more enumeration, and OI-006 still governs the token half." The envelope is not re-assessed by this contract.
- **CLM-003** — At `125cfacc1` `_STATUS.md` records lifecycle state `INITIALIZED` and carries no `## Remaining` section; its history records that section's retirement under `D-PEC-99`. No socket server, token mechanism, access-class logic, or test exists: no file under `projects/pec/v2` contains `access_class`, `admin` or `.listen(`, and the one file there that contains `AF_UNIX` is the locality-assertion test fixture `v2/tests/enforcement/fixtures/locality/local_unix/core/app.py`. Every statement below describes what a future implementation must satisfy; nothing here asserts that anything has been built.

### Placement in the work graph

- **CLM-002** — `DEL-08-01` is a root node with no upstream predecessors (`_DEPENDENCIES.md`; `Dependencies.csv` holds only the three ANCHOR rows `DEP-08-01-001` package anchor, `DEP-08-01-002` `SOW-003` trace, `DEP-08-01-003` `SOW-040` trace). Six accepted downstream relations are recorded, each an `ACTIVE` `PREREQUISITE` row in the consumer's own register at `RequiredMaturity` `INITIALIZED` and `SatisfactionStatus` `PENDING`: `DEL-09-06` (Universal drill-down to cited source) CONSUMES `[E-N06]`, `PROPOSAL`; `DEL-10-12` (Poll-adoption measurement) MEASURES `[E-N08]`, `PROPOSAL`; `DEL-08-04` (Orientation latency budget, p95 ≤ 100 ms) TESTS `[E-P52]`, `PROPOSAL`; `DEL-10-03` (No-ruling-write verification) TESTS `[E-P54]`, `PROPOSAL`; `DEL-08-05` (SSE delta/presence subscription) CONSUMES `[E-P58]`, `PROPOSAL`; and `DEL-08-06` (Agent tool-call query surface) CONSUMES `[E-P84]`, `DERIVED`, whose row `DEP-08-06-003` states "Tool-call queries run under the read-only agent access class of the socket server". Those consumers' own scope is not defined here.
- **CLM-009** — `DEL-08-06` and `DEL-10-13` (Reliance-advertisement gate) were set up under `D-PEC-101` Part K1, whose act merged in PR #976 as `ce934ac33`, an ancestor of `125cfacc1`. Each folder holds a `_STATUS.md` at `OPEN` and a `Dependencies.csv`, and neither holds a `ScopeOfWork.md`. This contract cites them by deliverable ID and register row only.
- **CLM-011** — Phase staging, checked against the `PhaseHint` column of `Deliverables.csv` for every deliverable this contract names in its own voice: `DEL-08-01`, `DEL-08-02`, `DEL-08-03`, `DEL-08-04`, `DEL-04-03`, `DEL-10-03` and `DEL-10-13` carry `P1`; `DEL-09-06` carries `P2`; `DEL-08-06` and `DEL-10-12` carry `P3`; and `DEL-08-05` carries `P4`. The `agent` class is therefore P1 scope of this deliverable, while the tool-call surface that runs under it is P3 scope of `DEL-08-06`. No claim here stages any of them differently.

### Boundaries

- **CLM-005** — Schema versioning, response format, latency budget, and SSE subscription belong to the sibling PKG-08 deliverables `DEL-08-02` (Versioned additive API schema), `DEL-08-03` (Compact citation-bearing response format), `DEL-08-04` (Orientation latency budget), and `DEL-08-05` (SSE delta/presence subscription) per the accepted §5 package table. They are out of scope for `DEL-08-01`.
- **CLM-010** — The acts that SCA-006 placed next to the access classes are owned elsewhere and are cited here, never discharged. The read-only query interface packaged for agent tool calls is `DEL-08-06` (`SOW-099`, `PEC-API-007`); it runs under the `agent` class this deliverable implements. Before any such tool is declared or invoked, the PEC Domain Engine Profile (`_DomainEngines/profiles/pec.yaml`) is amended under its own tier-0 act, which SCA-006 `Propagation_Plan.md` §B6 names; it is not this deliverable's act. Declared response-size budgets are `DEL-08-03`'s (`SOW-098`, `PEC-API-006`); the reliance envelope on every orientation response is `DEL-04-03`'s (`SOW-097`, `PEC-ORI-007`); the standing reliance-advertisement gate is `DEL-10-13`'s (`SOW-100`, PRD §12); the verification that no write path records adoption, ruling, or direction is `DEL-10-03`'s (`SOW-025`); and measuring consumer uptake, including enabled agent tool-call surfaces, is `DEL-10-12`'s (`SOW-060`). Schema versioning, the response format, the latency budget and the SSE subscription stay with `DEL-08-02`, `DEL-08-03`, `DEL-08-04` and `DEL-08-05` (CLM-005).

Unresolved information carried forward, not invented:

- **TBD-001** — `ResponsibleParty` is `TBD` in both `Deliverables.csv` and `_CONTEXT.md`; assignment occurs at WORKING_ITEMS activation.
- **TBD-002** — The token mechanism itself — token format, issuance, storage, presentation, expiry, and rotation, including the credentials of the `agent` class — is not fixed by any accepted source, because the choice of PEC-local token mechanism is CON-001.
- **TBD-003** — The socket path, filesystem permissions, and wire framing of OUT-001 are not fixed by the accepted basis, by `PEC-API-001`, or by PRD §8.
- **TBD-004** — The mapping from individual API operations to the four access classes is not fixed by any accepted source. PRD §8 characterizes owner and harness in general terms and characterizes admin not at all; for the `agent` class it fixes the read-only bound and three exclusions (REQ-008), and whether its read list is exhaustive is CON-003.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — The service shall bind local-only, on a Unix domain socket as the default transport, per `SOW-040` and `PEC-API-001`.
- **REQ-002** — Access shall be token-scoped: every request shall present a token that resolves to exactly one access class before any operation is served, and a request whose token is absent, unresolvable, or not valid shall be refused rather than served at a reduced scope.
- **REQ-003** — The delivered access-class set shall be exactly owner, harness, agent, and admin, per `SOW-003` and PRD §8.
- **REQ-004** — No role or permission ontology beyond those four access classes shall be delivered. The v1.0 12-role ontology and the prototype's implemented 14-role RBAC set are retired, per the `SOW-003` ledger note and PRD §8; neither may be carried forward as code, configuration, or identifier.
- **REQ-005** — No loopback TCP listener shall be delivered under this contract. The loopback question is carried as `SOW-083` (`OI-009`) and stated in `PEC-API-001` itself as a §16 open decision "in light of D-GOV-43 A2 (no network-exposed listener), superseding D-GOV-20 item 4"; see CON-002.
- **REQ-006** — The token mechanism shall be separable from the socket server and from the access-class decision logic, sitting behind a declared internal seam, so that a later `OI-006` ruling reworks the auth half without reworking the socket-and-access-class core. This requirement carries the accepted `ContextEnvelopeNotes` position; it does not choose a mechanism.
- **REQ-007** — Tests shall implement the verification methods declared in this contract. They shall not define scope, requirements, or acceptance criteria.
- **REQ-008** — A request whose token resolves to the `agent` class shall be served read-only query operations only. Event ingest, presence reports, every admin act, and any operation that writes shall be refused for that class, with no operation served, no state changed, and no partial or default-scoped result returned, per PRD §8 and `PEC-API-007`. The class is local-only and token-scoped like every class (REQ-001, REQ-002), and its credentials follow the open token mechanism (CON-001). This requirement fixes no read list beyond what PRD §8 states (CON-003).
- **REQ-009** — `DEL-08-01` shall perform no act owned by another deliverable and shall perform no act owned by another package: versioning the API schema (`DEL-08-02`); defining the response format or its declared size budgets (`DEL-08-03`); setting or measuring the orientation latency budget (`DEL-08-04`); serving the SSE subscription (`DEL-08-05`); packaging the read-only query interface as agent tools or declaring those tools (`DEL-08-06`); declaring or invoking any PEC tool before the tier-0 profile act that SCA-006 `Propagation_Plan.md` §B6 names; declaring the reliance envelope (`DEL-04-03`); running or recording the reliance-advertisement gate (`DEL-10-13`); verifying that no write path records adoption, ruling, or direction (`DEL-10-03`); and measuring consumer uptake (`DEL-10-12`). Each is cited to its owner in CLM-005 and CLM-010.

Acceptance criteria for `DEL-08-01`. Each states a property the future
implementation must exhibit; none asserts a present state.

- **AC-001** — The delivered service binds a Unix domain socket as its default listener, is reachable only through that local socket, and binds no network-reachable listener; the socket path and permissions chosen during production are recorded, and remain TBD-003 in this contract.
- **AC-002** — Every operation served over the socket is preceded by a token resolution that yields exactly one access class; a request with an absent, unresolvable, or invalid token is refused, with no operation served and no partial or default-scoped result returned.
- **AC-003** — The delivered access-class set is exactly owner, harness, agent, and admin; no identifier from the retired v1.0 12-role ontology or the retired prototype 14-role RBAC set appears in the delivered code, configuration, or fixtures.
- **AC-004** — The token mechanism is reachable only through a declared internal seam, such that replacing it with another PEC-local token mechanism changes no socket-server and no access-class decision code; CON-001 remains open and no delivered artifact may be read as settling it.
- **AC-005** — No loopback or other TCP listener is delivered, and no delivered artifact presumes the outcome of `SOW-083` / `OI-009`; CON-002 remains open.
- **AC-006** — The automated test suite implements VER-001 through VER-004 and VER-006, executes in the service test run, passes, and introduces no acceptance criterion absent from this contract.
- **AC-007** — The delivered artifacts trace to `SOW-003`, `SOW-040`, and `OBJ-001` and introduce no scope beyond those two ledger rows; in particular they do not absorb the schema, response-format, latency, or subscription scope held by the sibling deliverables named in CLM-005, or the scope CLM-010 assigns elsewhere; no delivered artifact presents an access-class grant as operational reliance or as authority; and the operation-to-access-class mapping applied during production is recorded against TBD-004 rather than asserted as accepted scope.
- **AC-008** — For an `agent`-class token, every event-ingest, presence-report or admin operation the delivered service serves, and every operation it serves that writes, is refused with no operation served, no state changed, and no partial or default-scoped result; every operation served to that class is a read; and the exercised operation list and its classification are recorded against TBD-004, with CON-003 left open.
- **AC-009** — The delivered artifacts perform none of the acts REQ-009 excludes, and where they meet an adjacent act they reach it only through the interface its owner in CLM-005 or CLM-010 provides.

Unresolved constraints carried into this contract, neither resolved nor
narrowed by authoring:

- **CON-001** — The token mechanism is undecided. `SOFTWARE_DECOMP.md` §10 (Open Issues) carries the disposition of record verbatim: "| OI-006 | SOW-080 | §16.6 auth reuse undecided; premise re-expressed under SCA-005: Runtime token registries are private to each application's Runtime instance and reuse of an App registry is foreclosed, so the open choice is the PEC-local token mechanism; the open choice also covers credentials for the agent access class (tool-call query, SOW-099; SCA-006) | §16 ruling |". `SOW-080` states the question as "Auth reuse: which PEC-local token mechanism PEC uses, including credentials for the agent access class (premise: Runtime token registries are private to each application's Runtime instance, and reuse of an App registry is foreclosed by the Runtime consumer guide)" with `InOutStatus` `TBD`, `OpenIssue` `TRUE`, and the ledger note "OI-006. Affects SOW-003 implementation choice". PRD §16.6 states that "The decision on PEC's own token mechanism stays open; it includes the credentials of the `agent` access class for tool-call query (PEC-API-007)." `SOFTWARE_DECOMP.md` §8 records the consequence for this deliverable (CLM-006): the socket-and-access-class core is stable either way, but the auth half may be reworked on the ruling, and the deliverable is held at `M` envelope at MEDIUM risk pending it. Nothing in this contract resolves `OI-006`, and no output may be read as settling it.
- **CON-002** — The transport question beyond the Unix socket is undecided. `SOW-040`'s ledger note records "Loopback TCP is TBD (SOW-083)"; `SOW-083` is `InOutStatus` `TBD`, `OpenIssue` `TRUE`, and states "Event-contract home (shared Runtime contracts at `projects/chirality-runtime/packages/contracts` vs PEC-local schema + pinned mirror) and API transport (Unix socket only vs additional loopback listener; transport posture per D-GOV-43 A2)" against PRD §16.9 with the note "OI-009. Fenced: PEC builds local-first either way (SOW-034/040)". `PEC-API-001` itself defers the loopback listener to §16. This contract delivers the Unix-socket default only and does not resolve `OI-009`.
- **CON-003** — **The `agent` class's read list.** PRD §8 lists the class's reads as "orientation, deltas, gate verdicts, decision-slate and presence reads" and excludes event ingest, presence reports and admin acts; `PEC-API-007` and `SOW-099` describe the surface as a "read-only query interface". No accepted source states whether that list is exhaustive, so that any other read the API serves (a drill-down read, for example) is refused to the class, or illustrates "read-only query access". REQ-008 binds only the read-only bound and the stated exclusions. Which further reads the class admits is decided by the owner, through the first Scope of Work of `DEL-08-06` (work-graph node K2) or a later PEC scope change; this contract neither narrows nor widens the list.

## Production and Verification Method — Praxeology

Production proceeds in the order socket binding → access-class decision →
token seam → tests, because the access-class decision is the acceptance surface
of the transport, and the seam of REQ-006 is what keeps CON-001 cheap. All work
is bounded to the deliverable's own service source; this contract authorizes no
register, decomposition, or PRD edit. It opens no source path either: each
production write needs an owner-ruled D-PEC packet naming the exact paths,
acts, verification and rollback, because the PEC source fence opens no path by
itself.

- **VER-001** — Start the delivered service and enumerate its bound listeners; confirm a Unix domain socket listener exists and is the default, confirm no TCP or otherwise network-reachable listener is bound, and record the socket path and its filesystem permissions.
- **VER-002** — Exercise the access path with a token for each of owner, harness, agent, and admin and confirm each resolves to exactly one class; then exercise it with absent, malformed, unresolvable, and invalid tokens and confirm each is refused with no operation served and no partial or default-scoped result.
- **VER-003** — Inspect the delivered source, configuration, and fixtures for identifiers belonging to the retired v1.0 12-role ontology or the retired prototype 14-role RBAC set, and confirm the delivered access-class set is exactly owner, harness, agent, and admin.
- **VER-004** — Inspect the module boundary between the token mechanism and the socket-and-access-class core: confirm the mechanism is reached only through the declared seam interface, and confirm by substituting a stub mechanism through that seam that no socket-server or access-class decision code changes.
- **VER-005** — Run the service test suite and confirm that each of VER-001 through VER-004 and VER-006 has a corresponding executing automated test, that the suite passes, and that no test asserts a criterion absent from this contract.
- **VER-006** — Enumerate every operation the delivered service serves and exercise each with an `agent`-class token; confirm that each event-ingest, presence-report or admin operation, and each operation that writes, is refused with no operation served, no state changed, and no partial or default-scoped result, and that each operation served is a read; record the enumerated list and its classification against TBD-004.
- **VER-007** — Inspect the delivered source, configuration, and tests for any act REQ-009 excludes, confirm none is present, and confirm that each adjacent act the artifacts meet is reached only through its owner's interface.

Tests implement verification methods and produce evidence. They do not create
scope or acceptance criteria: OUT-003 exists because the accepted register names
it, and VER-005 is the method by which AC-006 is checked, not a source of new
obligations.

## Governing Values and Decisions — Axiology

- **AX-001** — Local-only, token-scoped access originates in `PEC-API-001` and PRD §8 and enters project scope as `SOW-040` and `SOW-003`. This contract carries that posture without reinterpretation, extension, or softening; in particular, "Unix socket by default" is not read as licensing a second default transport.
- **AX-002** — `DL-11` is the decision that assigned `SOW-003` (access classes) to `PKG-08` "with the token-scoped transport" rather than to a separate access-control package. The access classes and the socket binding are therefore one deliverable by ruling, not by authoring convenience.
- **AX-003** — Retirement is a governing constraint, not a stylistic preference. PRD §8 retires the v1.0 12-role ontology and the prototype's implemented 14-role RBAC set explicitly; REQ-004 and AC-003 exist so that the retired sets cannot re-enter through carried prototype code, which PRD §7.3 permits only as pattern and never as code.
- **AX-004** — The deliverable is at `INITIALIZED` with no implementation (CLM-003). This contract states obligations on future artifacts; it does not certify, imply, or record that anything exists, and it performs no lifecycle transition. `_STATUS.md` remains the sole lifecycle authority and is untouched by this rebuild.
- **AX-005** — Unknowns are preserved as TBD-001 through TBD-004 and as CON-001 through CON-003 rather than resolved by authoring judgment. `OI-006` and `OI-009` close by owner §16 ruling, and CON-003 by the owner decision it names; resolving TBD items is production work. None of these is contract drafting.
- **AX-006** — The accepted basis is decomposition revision 1.6 (SCA-006) at the checkpoint-3 acceptance commit `189f205ff`. The deliverable-local metadata names the same revision: `_CONTEXT.md` keeps its supersession trace from revision 1.1 through revision 1.6 as provenance, and `_REFERENCES.md` names revision 1.6 and PRD v2.4, so no divergence between basis and local metadata remains to record.
- **AX-007** — `C-04` PHASE_PRECEDENCE and `C-10` STRATUM_RULE are register-wide non-gating constraints recorded in `_DEPENDENCIES.md`. The `P1` phase hint is release-strategy ordering. Five of the six downstream edges in CLM-002 (E-N06, E-N08, E-P52, E-P54, E-P58) are `PROPOSAL` stratum, accepted as presented under `D-PEC-62` §1(4) and carrying no exhibit flag; the sixth, E-P84, is `DERIVED` stratum, and its packet states that all strata require owner acceptance and that the `D-PEC-101` ruling is that acceptance. Stratum is provenance, not authority — it records how an edge was derived, not whether it has been accepted — and blocker output is advisory visibility only, never work assignment.
- **AX-008** — Operational reliance is not access and not authority. Under `PEC-K-03` a consumer, or an agent acting through one or through the tool-call surface, may act on a record-tier claim within the pin, coverage and trust tier a response declares, with file fallback, only from a PEC release that has passed the PRD §12 reliance-advertisement gate; PEC output stays never citable as authority (`PEC-K-02`, `D-PEC-90`). An access class grants no reliance, advertises none and waives no file fallback, so this contract is not written around verify-before-rely (the SCA-006 `Propagation_Plan.md` §B4 pass rule, after `D-PEC-90` grant item 1). Operational reliance is also distinct from the reliance-hold control of `projects/pec/AGENTS.md` and from professional reliance.
- **AX-009** — SCA-006 (`DL-21`, accepted at checkpoint 1 with option DQ-a) added the read-only `agent` class to `SOW-003` and to this deliverable and extended `OI-006` to the class's credentials. The unselected DQ-b option would have had tool hosts query as harnesses, with no fourth class. A distinct class lets an agent query PEC directly where a tool-call surface is enabled, and keeping it read-only keeps PEC an observer (`PEC-K-06`): no event ingest, presence report or admin act is reachable through it (REQ-008). Enabling any path stays consumer-owned, and no agent, harness or loop is required to query PEC (`PEC-K-01`, `PEC-K-11`).
- **AX-010** — Rebuild provenance. This contract replaces, as a whole, the prior contract with SHA-256 `8ac1dc050efbd22530700d140a57944d0f82f48bcb2f9994bee4cddd588a3d76` (basis pin `SOFTWARE_DECOMP.md@11a494e9a`, revision 1.3). It is that contract's currency rebuild under the S4 Scope of Work currency packet (provisional `D-PEC-102`), which is not yet ruled. It carries the SCA-005 cause (`OI-006` re-expressed for application-private Runtime token registries, and the `D-GOV-20` citation of `PEC-API-001` replaced by `D-GOV-43` A2; SCA-005 `Propagation_Plan.md` §B4 class `STALE_REVIEW_REQUIRED`) and the SCA-006 causes (the read-only `agent` class of PRD v2.4 §8 and `SOW-003`, and operational reliance under `PEC-K-03` in place of verify-before-rely; combined class `STALE_REBUILD_REQUIRED` in SCA-006 `Propagation_Plan.md` §B4). No ID is retired. Kept IDs whose rule changed: OUT-002, CLM-002, CLM-003, CLM-004, CLM-006, TBD-002, TBD-004, REQ-003, REQ-004, REQ-005, AC-003, AC-004, AC-006, AC-007, VER-002, VER-003, VER-005, CON-001, CON-002, AX-004, AX-005, AX-006 and AX-007. Kept IDs keep their meaning; new IDs take the next unused number for their prefix: CLM-007 through CLM-011, REQ-008, REQ-009, AC-008, AC-009, VER-006, VER-007, CON-003, and AX-008 through AX-010.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-040 OBJ-001 | REQ-001, REQ-005, CLM-001, CLM-005, CON-002, TBD-003 | AC-001, AC-005 | VER-001 | Listener enumeration from the started service showing the Unix socket default and the absence of any network-reachable listener, plus the recorded socket path and permissions |
| OUT-002 | SOW-003 OBJ-001 | REQ-002 | AC-002 | VER-002 | Token-resolution transcripts for each access class and for each rejection case |
| OUT-002 | SOW-003 OBJ-001 | REQ-003, REQ-004, CLM-004, CLM-007 | AC-003 | VER-003 | An identifier scan of source/config/fixtures against the retired role sets |
| OUT-002 | SOW-003 OBJ-001 | REQ-006, CLM-006, CON-001, TBD-002 | AC-004 | VER-004 | The seam interface signature plus the stub-substitution diff |
| OUT-002 | SOW-003 OBJ-001 | REQ-008, CLM-004, CLM-008, CON-003, TBD-004 | AC-008 | VER-006 | The enumerated operation list with its read/write classification and the agent-class refusal transcripts |
| OUT-002 | SOW-003 SOW-040 OBJ-001 | REQ-009, CLM-005, CLM-009, CLM-010, CLM-011 | AC-009 | VER-007 | Source, configuration and test inspection records against each act REQ-009 excludes |
| OUT-003 | SOW-003 OBJ-001 | REQ-007, CLM-003 | AC-006 | VER-005 | Service test-run output mapping each executed test to its declared verification method |
| OUT-001 | SOW-003 SOW-040 OBJ-001 | CLM-002, CLM-005, CLM-008, CLM-010, TBD-001, AX-008 | AC-007 | HUMAN_REVIEW: REVIEW gate confirms traceability to SOW-003, SOW-040, and OBJ-001, confirms no absorption of sibling PKG-08 scope or of the scope CLM-010 assigns elsewhere, confirms no access-class grant is presented as operational reliance or authority, and confirms CON-001, CON-002 and CON-003 are left open | Review record citing the two scope-ledger rows, the objective row, the sibling deliverable boundary, and the recorded operation-to-access-class mapping against TBD-004 |
