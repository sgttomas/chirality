---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-01-06
package_id: PKG-01
decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@11a494e9a
project_scope_refs: [SOW-094]
package_objective_refs: [OBJ-004]
---

# Scope of Work — DEL-01-06 Loop registry (local config default)

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-01-06` — "Loop registry
(local config default)" — in `PKG-01` Service Core & Store of the PEC v2 build.
It covers project scope item `SOW-094` in service of package objective
`OBJ-004`.

The accepted basis is `execution/_Decomposition/SOFTWARE_DECOMP.md`
**revision 1.3** (`current_basis`, SCA-003 successor), pinned at merge
`11a494e9a`.

**Objective warrant.** The `DEL-01-06` → `OBJ-004` attribution is
SCA-002-qualified, not register-direct. At revision 1.1 the ledger row for
`SOW-094` carried no objective. Scope change SCA-002 attributed it to
`OBJ-004` and the attribution was accepted at revision 1.2. The warrant runs
through `SOW-094`'s own PRD anchor: `PEC-DSH-002` requires a "Lifecycle census
across all registered loops' packages/deliverables", and "all registered loops"
is only resolvable once something names them — which is exactly what this
deliverable produces. PRD §12 P2 confirms the same reading ("All five loops;
Overview, census, registers, decision slate").

- **CLM-001** — `SOW-094` states: "Maintain the loop-registration configuration naming the loops PEC serves (local config default)", with SourceRef "§12 P2, PEC-DSH-002".
- **CLM-002** — `OBJ-004` states: "The human owner has one live view: loops, gates, lifecycle census, decisions waiting on them, and who is working where" (PRD §3.4).
- **CLM-003** — The `SOW-094` ledger note records that the long-term registry home and shape stay open as `SOW-077` (`OI-003`), and that the local-config default follows that item's resolved note under decision-log entry `DL-14`.

## Deliverable Definition — Ontology

`DEL-01-06` is typed `BACKEND_FEATURE_SLICE` at Context Envelope `S` with
`PhaseHint` `P1`. The decomposition register records its anticipated artifacts
as "Config format + loader + tests" and carries no `ContextEnvelopeNotes`. It
is a root node of the accepted dependency DAG: `_DEPENDENCIES.md` declares no
upstream predecessors, and `Dependencies.csv` holds only the two ANCHOR rows
(`DEP-01-06-001` package anchor, `DEP-01-06-002` `SOW-094` requirement trace).

- **OUT-001** — A loop-registry configuration format: documented field semantics for a local configuration file that names the loops PEC serves, together with the checked-in local default instance of that file.
- **OUT-002** — A loader in the PEC service core that reads the registry configuration, validates it against OUT-001, and exposes the resulting registered-loop set to record-tier consumers.
- **OUT-003** — An automated test suite covering the format and the loader, implementing the verification methods declared in this contract.

- **CLM-004** — "Loop" is the PRD §7.1 record-tier entity: the tenancy unit above Project, a LOOP_INIT/workplan-governed work loop, with `root, app-dev, piping, pec, bridge` named as the current instances and "today five" recorded at PRD §16.3.
- **CLM-005** — Registry coverage is phase-staged: at P1 exactly one loop is registered — PEC v2's own build, per `OI-010` as resolved at Gate 2 (2026-07-24, `DL-10`) — and at P2 coverage extends to all five registered loops, per the `_CONTEXT.md` description and PRD §12.
- **CLM-006** — Three accepted consumer edges depend on this deliverable, all at `RequiredMaturity` `INITIALIZED` and all currently `PROPOSAL` stratum: DEL-02-07 `[E-N16]` ("DEL-01-06 names 'the loops PEC serves'; DEL-02-07 reads per-project manifests per loop"), DEL-03-01 `[E-P18]` ("Reconciler needs the loop registry"), and DEL-09-02 `[E-P62]` ("Census spans the registered loops").
- **CLM-007** — The deliverable is at lifecycle state `INITIALIZED` with no implementation present. Every requirement, acceptance criterion, and verification method below states a contract on future production; none asserts that anything has been built.
- **TBD-001** — `ResponsibleParty` is unassigned; the register records `TBD`, with assignment at WORKING_ITEMS activation.
- **TBD-002** — The concrete on-disk path, filename, serialization, and per-loop field set of the local default are not fixed by any accepted source; they are chosen during production within the bounds of CON-001 and REQ-005.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — The configuration shall name each loop PEC serves with a stable loop identifier, and shall carry per loop the minimum locator the reconciler needs to reach that loop's file truth; the concrete field set remains TBD-002.
- **REQ-002** — The registry shall be delivered as a local configuration file with a checked-in default instance, per the "local config default" wording of `SOW-094` and its `DL-14` resolved note.
- **REQ-003** — The loader shall reject a configuration that does not validate and shall state the failure explicitly, naming the offending entry or field; silent omission and silent substitution of a partial or empty loop set are prohibited, consistent with `PEC-ORI-006`.
- **REQ-004** — The loader shall expose the registered-loop set to the record-tier consumers declared in CLM-006 through a stable in-process interface.
- **REQ-005** — Consumers shall not depend on the registry's on-disk location or serialization, so that a later `SOW-077` ruling can change the registry's home and shape without amending DEL-02-07, DEL-03-01, or DEL-09-02.
- **REQ-006** — The registry format, default instance, and loader shall introduce no third-party runtime dependency and no external network egress, per `PEC-SVC-001` and `PEC-SVC-002`, whose standing enforcement is `DEL-01-05` covering `SOW-052` and `SOW-053`.
- **REQ-007** — Tests shall implement the verification methods declared in this contract; they shall not define scope, requirements, or acceptance criteria.

- **AC-001** — The configuration format documents every field it defines, names each served loop with a stable identifier, and is validatable deterministically, with a valid instance accepted and every malformed fixture rejected.
- **AC-002** — The checked-in default instance registers exactly one loop at P1, identified as PEC v2's own build per OI-010, and admits the remaining registered loops at P2 by adding entries only, with no format change and no entry for a loop not named in an accepted source.
- **AC-003** — The loader rejects an invalid or unreadable configuration with an explicit failure that names the offending entry or field, and never returns a silently defaulted, partial, or empty loop set in its place.
- **AC-004** — The loader exposes the registered-loop set through an interface whose signature carries no configuration path or serialization detail, so that relocating or reshaping the registry changes no consumer deliverable.
- **AC-005** — The format, the default instance, and the loader add no third-party runtime dependency and make no network call, leaving the DEL-01-05 zero-dependency and locality assertion intact.
- **AC-006** — The automated test suite implements VER-001 through VER-005, executes in the service-core test run, passes, and introduces no acceptance criterion absent from this contract.

- **CON-001** — The long-term home and shape of the loop registry is an undecided owner question, carried as `SOW-077` (`InOutStatus` `TBD`, PRD §16.3) and open issue `OI-003` awaiting a §16 ruling. This deliverable produces the local config default only. Nothing in this contract resolves `OI-003`, and no output may be read as settling it.

## Production and Verification Method — Praxeology

Production proceeds in the order format → default instance → loader → tests,
because each stage is the acceptance surface of the next. All work is bounded
to the deliverable folder and the service-core source it names; this contract
authorizes no register, decomposition, or PRD edit.

- **VER-001** — Validate the documented format against the checked-in default instance and against a fixture set of deliberately malformed configurations; the valid instance validates and every malformed fixture is rejected with a located failure.
- **VER-002** — Inspect the default instance and assert exactly one registered loop at P1 whose identity is PEC v2's own build, then confirm by construction that adding the remaining registered loops requires new entries only and no schema change.
- **VER-003** — Execute the loader against invalid, unreadable, and absent configuration fixtures and assert an explicit located failure in each case, with no fallback, partial, or empty loop set returned.
- **VER-004** — Exercise the loader's consumer-facing interface, assert the returned loop set matches the configuration, and inspect the interface signature for configuration-path or serialization leakage.
- **VER-005** — Inspect the service-core dependency manifest and the registry module import graph for third-party runtime dependencies and network calls, and re-run the DEL-01-05 locality and zero-dependency enforcement once that deliverable is available.
- **VER-006** — Run the service-core test suite and confirm that each of VER-001 through VER-005 has a corresponding executing automated test and that no test asserts a criterion absent from this contract.

## Governing Values and Decisions — Axiology

- **AX-001** — `PEC-K-01` graceful absence governs: no governed act may require a PEC read or write. The registry is PEC-internal configuration; naming a loop confers no authority over it, and its absence blocks nothing outside PEC.
- **AX-002** — `PEC-K-02` files govern: the registry records where each loop's file truth is read from and never becomes an alternative source of truth about a loop. Registry contents are not citable as authority.
- **AX-003** — `DL-14` (Phase 6 adversarial verification, applied at revision 0.9) is the decision that created `SOW-094` and `DEL-01-06`. The "local config default" is that entry's resolved-note position, adopted so P1 can proceed; it is explicitly not a settled long-term architecture.
- **AX-004** — Gate 2 (2026-07-24, `DL-10`) resolved `OI-010`: the first loop the P1 reconciler ingests is PEC v2's own build, the §12 closing paragraph governing over the P1 table's "(piping or root)" parenthetical. The P1 registry default follows that ruling.
- **AX-005** — `C-04` PHASE_PRECEDENCE and `C-10` STRATUM_RULE are register-wide non-gating constraints. The P1→P2 coverage step is release-strategy ordering. The consumer edges in CLM-006 are `PROPOSAL` stratum and are accepted: `D-PEC-62` §1(4) accepted the candidate v0.2 exhibit "all strata as presented", reading acceptance as carrying the exhibit's flags as flags, so what remains recorded-but-unresolved is the specific annotated set (E-A11, E-P69/E-N02, E-N13/E-N18, C-02 direction, C-08 standing-node set) — none of which touches E-N16, E-P18, or E-P62. Stratum is provenance, not authority; it records how an edge was derived, not whether it has been accepted.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-094 OBJ-004 | REQ-001, CLM-004 | AC-001 | VER-001 | Format documentation, the checked-in default instance, the malformed-fixture set, and validation output showing accept/reject per fixture |
| OUT-001 | SOW-094 OBJ-004 | REQ-002, CLM-005 | AC-002 | VER-002 | The checked-in default instance |
| OUT-001 | SOW-094 OBJ-004 | REQ-006 | AC-005 | VER-005 | Dependency-manifest plus import-graph inspection records |
| OUT-002 | SOW-094 OBJ-004 | REQ-003 | AC-003 | VER-003 | Loader failure-path transcripts |
| OUT-002 | SOW-094 OBJ-004 | REQ-004, REQ-005, CLM-006 | AC-004 | VER-004 | The consumer-facing interface signature |
| OUT-002 | SOW-094 OBJ-004 | REQ-006 | AC-005 | VER-005 | Dependency-manifest plus import-graph inspection records |
| OUT-003 | SOW-094 OBJ-004 | REQ-007, CLM-007 | AC-006 | VER-006 | Service-core test-run output mapping each executed test to its declared verification method |
