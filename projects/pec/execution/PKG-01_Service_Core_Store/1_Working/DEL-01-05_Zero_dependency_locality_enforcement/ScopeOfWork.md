---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-01-05
package_id: PKG-01
decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@3623b958b
project_scope_refs: [SOW-052, SOW-053]
package_objective_refs: [OBJ-005]
---

# Scope of Work — DEL-01-05 Zero-dependency & locality enforcement

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-01-05` — "Zero-dependency
& locality enforcement" — in `PKG-01` Service Core & Store of the PEC v2 build.
It covers project scope items `SOW-052` and `SOW-053` in service of package
objective `OBJ-005`.

The accepted basis is `execution/_Decomposition/SOFTWARE_DECOMP.md`
**revision 1.2** (`status: current_basis`, `SCA-002` successor accepted
2026-07-25 under `D-PEC-64`, commit `3623b958b`). The deliverable-local
`_REFERENCES.md` still names "revision 1.1, accepted working surface". That
phrase is superseded provenance awaiting a deferred pointer sweep — `_CONTEXT.md`
records revision 1.1 as "superseded by revision 1.2 (`current_basis`, SCA-002
successor)" — and it is not the basis of this contract.

**Standing character (load-bearing), and what authorizes it.** Everything below
is written as a contract on a *continuing* enforcement behaviour: there is no
state in which this deliverable's assertion is finished, and a passing run is
evidence for the state it evaluated and for no later state. That framing is
directed by the wave brief — `execution/_Coordination/PLAN_2026-07-25_pec_phase_2_2_sow_wave.md`
instructs that "DEL-01-05 is a standing assertion (C-08) — author it as such,
not as a one-shot artifact" — and it is informed by, not derived from, the `C-08`
`STANDING_NODES` annotation described in CLM-006. It is therefore a property of
how this contract is written. It is not an owner-ruled gating force, and the
question of whether the enforcement carries release-gating authority is routed
to the owner under CON-002 rather than assumed here.

**Objective warrant.** The `DEL-01-05` → `OBJ-005` attribution is `SCA-002`-
qualified and accepted at revision 1.2. It runs through the PRD §10 anchors of
the two covered scope items: a service core with no third-party runtime
dependency and no external network egress is a core that nothing outside PEC has
to be present for, and nothing outside PEC has to reach out to. That is the
deletability posture `OBJ-005` states.

- **CLM-001** — `SOW-052` states: "Keep the service core free of third-party runtime dependencies; workspace-internal contracts packages permitted", `SourceRef` `PEC-SVC-001`, ledger note "Carries ADR-002" (`execution/_Decomposition/ScopeLedger.csv`, row `SOW-052`).
- **CLM-002** — `SOW-053` states: "Operate local, single-owner, with no external network egress", `SourceRef` `PEC-SVC-002` (`ScopeLedger.csv`, row `SOW-053`).
- **CLM-003** — The PRD anchors read: `PEC-SVC-001` — "The service core has zero third-party runtime dependencies (carries ADR-002); workspace-internal runtime contracts packages are permitted"; `PEC-SVC-002` — "Local, single-owner posture; no external network egress" (`projects/pec/docs/PRD.md` §10).
- **CLM-004** — `OBJ-005` states: "Everything PEC holds can be deleted at any moment without blocking any governed act", `SourceRef` §3.5, mapped scope items "SOW-010, SOW-021, SOW-025, SOW-052..056, SOW-088; bound by C1/C2 across all items", mapped deliverables including `DEL-01-05` (`SOFTWARE_DECOMP.md` §Objectives; `PRD.md` §3 outcome 5).
- **CLM-005** — The same two rules appear as hard constraints of the decomposition: `C7` — "Zero third-party runtime dependencies in the service core (workspace-internal contracts packages permitted)" — and `C8` — "Local-only, Unix socket default, token-scoped, no external egress; any loopback TCP listener is an open owner decision" (`SOFTWARE_DECOMP.md` §1.3). These decomposition constraint labels are distinct from the dependency-register constraint rows cited below.

## Deliverable Definition — Ontology

`DEL-01-05` is typed `CI_CD_CHANGE` at Context Envelope `S` with `PhaseHint`
`P1` and no `ContextEnvelopeNotes`. Its description of record is "Automated
assertion that the service core carries no third-party runtime dependencies
(workspace-internal contracts permitted) and no external egress", and its
anticipated artifacts are "CI/lint check + posture note"
(`execution/_Decomposition/Deliverables.csv`, row `DEL-01-05`;
`SOFTWARE_DECOMP.md` §5 table for `PKG-01`; restated in `_CONTEXT.md`).

- **OUT-001** — The automated dependency assertion, delivered registered: an executable check that evaluates the service core's runtime dependency surface and fails on any third-party runtime dependency, admitting only workspace-internal runtime contracts packages — together with the wiring that binds it into the service-core change path and the release gate, so that it is re-evaluated on every subsequent state without further action. The registration is part of this output's delivery, not a separate artifact; `Deliverables.csv` names the artifact class as "CI/lint check + posture note" and admits no third artifact.
- **OUT-002** — The automated locality assertion, delivered registered: an executable check that evaluates the service core for external network egress and fails on any egress path, leaving local transport unflagged — together with the same wiring into the service-core change path and the release gate, on the same terms as OUT-001.
- **OUT-003** — The posture note: the documented statement of the enforced posture, the permitted exception, the standing character of the gate, how a failure is read and acted on, and the record of the still-open transport decision.

- **CLM-006** — `DEL-01-05` is named in constraint row `C-08` `STANDING_NODES` of the accepted gate exhibit: "excluded from one-shot COMPLETE/UNBLOCKED arithmetic; they gate releases not successors" (member set "DEL-01-05, DEL-03-04, DEL-10-02, DEL-10-03, DEL-10-10", evidence "Own text: 'Automated assertion' ..."). The row's own `Notes` field reads "R3-F9; owner confirmation requested". At `D-PEC-62` §1.4 the owner accepted the DAG candidate "all strata as presented", and that packet reads the acceptance as taking the exhibit's **flags as flags**: the `C-08` standing-node set is one of the enumerated annotations that "remain recorded-but-unresolved, non-gating annotations". What is settled is therefore the arithmetic exclusion — `C-08` is a non-gating constraint row and this deliverable is excluded from one-shot `COMPLETE`/`UNBLOCKED` counting. What is not settled is the classification's force as a release gate. The deliverable-local `_DEPENDENCIES.md` compresses this to "(owner-confirmed at D-PEC-62 ruling)"; that phrase is accurate as to the arithmetic exclusion and overstates the rest, and this contract cites the `D-PEC-62` text over the local paraphrase.
- **CLM-007** — It is a deliberate zero-edge node: `_DEPENDENCIES.md` declares "no upstream predecessors (root node)", `Dependencies.csv` (v3.1) holds only the three ANCHOR rows (`DEP-01-05-001` package anchor, `DEP-01-05-002` `SOW-052` trace, `DEP-01-05-003` `SOW-053` trace), and the gate exhibit records "DEL-01-05 (C-08 standing CI gate — deliberate)" among its zero-edge nodes. No accepted register edge names a consumer of this deliverable, because it gates releases rather than successors.
- **CLM-008** — The enforced surface is `PKG-01`'s subject: "The zero-dependency service foundation: record- and presence-tier entity schemas, the gitignored store with ingest-boundary content-minimal enforcement, locality/no-egress posture, self-observability logging, loop-registration config" (`SOFTWARE_DECOMP.md` §Packages, row `PKG-01`).
- **CLM-009** — The access posture the locality assertion must not contradict is `PEC-API-001`: "The service binds local-only, Unix socket by default, with token-scoped access; any loopback TCP listener is a §16 open decision in light of D-GOV-20's no-TCP-control-listener posture" (`PRD.md` §9.6; restated in the §8 "Users and access" description).
- **CLM-010** — The deliverable is at lifecycle state `OPEN` (`_STATUS.md`) with no implementation present. Every requirement, acceptance criterion, and verification method below states a contract on future production; none asserts that any check, registration, or note has been built.
- **TBD-001** — `ResponsibleParty` is unassigned; the register records `TBD`, with assignment at WORKING_ITEMS activation.
- **TBD-002** — The concrete enforcement mechanism (which CI or lint system, its configuration file locations, and the on-disk home of the posture note) is not fixed by any accepted source. `Deliverables.csv` names the artifact class "CI/lint check + posture note" and nothing further; no accepted source names a CI system for the PEC v2 build.
- **TBD-003** — The service core's toolchain and dependency-manifest format are not fixed by an accepted v2 source. The archived `ADR-002` text names one language across core/server/web, but the live carried form of that posture is `PEC-SVC-001` alone (`PRD.md` §13; re-citation of the carried posture is `DEL-00-01`'s scope under `SOW-088`, not this deliverable's).
- **TBD-004** — The boundary between a *runtime* dependency and a build-, test-, or development-time dependency of the service core is not fixed by an accepted source; `PEC-SVC-001` constrains runtime dependencies only.
- **TBD-005** — The precise module boundary of "the service core" follows the v2 core-isolation style, which is undecided: `OI-012` is dispositioned "Decided in DEL-00-01's ADR; owner review at that ADR" (`SOFTWARE_DECOMP.md` §Open Issues). The accepted register declares no edge from `DEL-00-01` to `DEL-01-05`; this contract records the information dependency without asserting a graph edge.
- **CON-001** — API transport is an undecided owner question: `OI-009` / `SOW-083` (`InOutStatus` `TBD`, "Event-contract home ... and API transport (Unix socket only vs additional loopback listener)", `SourceRef` §16.9, ledger note "Fenced: PEC builds local-first either way"). A loopback listener is not external egress, and this contract neither authorizes nor forbids one. Constraint `C12` governs: the §16 open decisions "are not resolved by this decomposition; where one materially affects architecture the affected work is fenced or flagged, never guessed."
- **CON-002** — Whether this deliverable's enforcement carries *release-gating authority* is unconfirmed. The `C-08` `STANDING_NODES` row that classifies it records "owner confirmation requested" in its own `Notes`, and `D-PEC-62` §1.4 accepted the standing-node set as a recorded-but-unresolved, non-gating annotation rather than ruling it (CLM-006). The mechanism this contract requires is designed to block and its verdicts are unambiguous; what is open is whether a blocking verdict binds a release candidate or is advisory. AC-011 routes that question to an accountable owner. This contract neither asserts the authority nor waives it, and no production choice may settle it.

## Completion and Reliance Basis — Epistemology

The requirements below state the contract the future enforcement must satisfy.
Under the standing framing established above — brief-directed and informed by
the `C-08` annotation (CLM-006, CON-002) — they bind the enforcement mechanism's
*continuing* behaviour: each is a property that must hold on every evaluated
service-core state, not a one-time production event.

- **REQ-001** — The dependency assertion shall evaluate the service core's runtime dependency surface and shall fail whenever that surface contains a package that is not workspace-internal.
- **REQ-002** — The admitted exception shall be exactly `PEC-SVC-001`'s: workspace-internal runtime contracts packages. The admitted set shall be enumerated explicitly in the check's own configuration, and the check shall not widen the permission by inference, wildcard, or unreviewed default.
- **REQ-003** — The locality assertion shall fail whenever the service core initiates or is configured to initiate external network egress. Local transport consistent with `PEC-API-001` shall not be reported as a violation, and no outcome of the check shall depend on the resolution of CON-001.
- **REQ-004** — Both assertions shall report failure explicitly and locatably — the offending dependency and its importer, the offending call site or configuration entry — and shall never report a pass over a surface they did not actually evaluate.
- **REQ-005** — Both assertions shall be fail-closed: an unresolvable manifest, an unreadable surface, an absent target, or a tooling error is a failure, never a pass and never a silent skip.
- **REQ-006** — The enforcement shall be registered as a standing gate: re-evaluated on every change to the service core and on every release candidate, against that exact candidate state. It shall have no completion state, and no passing run shall be carried forward as evidence for a later state.
- **REQ-007** — The enforcement mechanism shall be designed to block: for a release candidate on which either assertion fails, or against which either assertion has not been executed, the mechanism shall return an explicit blocking verdict rather than a pass, a skip, or an absent result. This requirement binds the mechanism's design intent and the verdict it produces. It does not, by itself, establish that a blocking verdict binds a release: whether the enforcement carries release-gating authority follows the pending `C-08` confirmation recorded at CON-002 and is routed to the owner at AC-011.
- **REQ-008** — The enforcement shall assert only. It shall not edit dependency manifests or service-core source, shall not add a third-party runtime dependency to the service core, and shall make no network call of its own.
- **REQ-009** — Production shall record the operative definitions it uses for "the service core" and for a "runtime" dependency (TBD-003, TBD-004, TBD-005) alongside the check, rather than leaving either implicit in the mechanism's behaviour.
- **REQ-010** — The posture note shall state the enforced posture, its two source rules (`PEC-SVC-001`, `PEC-SVC-002`), the permitted workspace-internal exception, the standing character of the gate, how a failure is read and acted on, and shall record the transport question of CON-001 as open without resolving it.
- **REQ-011** — Nothing produced under this contract shall make a governed act depend on PEC-held state or on the gate's availability; the gate constrains PEC's own build and confers no authority over any loop.
- **REQ-012** — Tests and deterministic checks shall implement the verification methods declared below; they shall not define scope, requirements, or acceptance criteria.

- **AC-001** — On a service-core state whose runtime dependency surface is entirely workspace-internal the dependency assertion passes, and on any state that introduces a third-party runtime dependency it fails and names both the offending dependency and the importing module.
- **AC-002** — The check's admitted set is enumerated in its own configuration, contains only workspace-internal runtime contracts packages, and admits no entry that `PEC-SVC-001` does not permit; adding an entry is a visible configuration change, not an inferred default.
- **AC-003** — On a service-core state that initiates or configures external network egress the locality assertion fails and names the call site or configuration entry, and on a state using only local transport consistent with `PEC-API-001` it passes; no fixture outcome changes according to whether a loopback listener is later permitted.
- **AC-004** — Both assertions execute on every change to the service core and on every release candidate, each execution bound to the exact state it evaluated, and no earlier passing run is presented as evidence for a later state.
- **AC-005** — On a release candidate whose assertions fail, and on one against which either assertion was not executed, the mechanism returns an explicit blocking verdict, demonstrated on a candidate deliberately constructed to violate each rule and on a candidate for which the check was withheld. Whether that verdict binds the release is CON-002 and AC-011, not this criterion.
- **AC-006** — Each assertion, when given an unresolvable manifest, an unreadable surface, or a failing tool invocation, reports failure; no such condition yields a pass, a skip, or an empty successful result.
- **AC-007** — The registration remains armed without further action: disabling, removing, or bypassing either assertion is a visible change to the gate configuration and produces a reported gate failure rather than a silent no-op.
- **AC-008** — The enforcement mechanism adds no third-party runtime dependency to the service core, makes no network call, and leaves service-core source and dependency manifests unmodified across a full run.
- **AC-009** — The posture note contains every element required by REQ-010, states the operative definitions recorded under REQ-009, and asserts no completion of the enforcement obligation.
- **AC-010** — An accountable owner confirms that neither the posture note nor either assertion resolves, pre-empts, or forecloses `OI-009` / `SOW-083`, and that the enforcement makes no governed act depend on PEC-held state.
- **AC-011** — An accountable owner confirms, or declines to confirm, that the enforcement delivered under this contract carries release-gating authority — that its blocking verdict blocks a release candidate — given that `C-08`'s standing-node classification carries "owner confirmation requested" and was accepted at `D-PEC-62` §1.4 as a recorded-but-unresolved, non-gating annotation (CLM-006, CON-002). A decline leaves the mechanism's verdicts advisory and invalidates no other criterion in this contract; the standing framing of the contract stands either way, because it is how the contract is written rather than a claim about the gate's force.

## Production and Verification Method — Praxeology

Expected production sequence: record the operative service-core and runtime
definitions (REQ-009); build the dependency assertion; build the locality
assertion; register both as a standing gate; write the posture note last so it
describes what is actually enforced. All work is bounded to this deliverable's
artifacts and the service-core surfaces they read; this contract authorizes no
register, decomposition, or PRD edit, and constraint `C14` keeps every
implementation tranche dependent on its own owner-ruled packet. The verification
methods below are themselves standing: each is re-run on every evaluated state,
not once at hand-over.

- **VER-001** — Execute the dependency assertion against a conforming service-core fixture and against fixtures that introduce a third-party runtime dependency at direct and transitive positions; assert pass on the former and, on each violating fixture, a failure naming the dependency and its importer.
- **VER-002** — Inspect the check's admitted-set configuration against the `PEC-SVC-001` wording; assert every entry is a workspace-internal runtime contracts package and that no wildcard or implicit default widens the permission.
- **VER-003** — Execute the locality assertion against fixtures that (a) make an external network call, (b) declare an external endpoint in configuration, and (c) use only local transport; assert located failure for (a) and (b), pass for (c), and re-run the whole set under both readings of CON-001 to confirm identical outcomes.
- **VER-004** — Inspect the gate record across a sequence of service-core changes and at least one release candidate; assert an execution exists for each state, that each execution is bound to the state it evaluated, and that no result is reused across states.
- **VER-005** — Blocking-verdict demonstration: submit a release candidate violating each rule in turn, and one candidate with the assertion withheld; assert that the mechanism returns an explicit blocking verdict in every case. The method demonstrates the mechanism's verdict, not the release process's obligation to honour it (CON-002).
- **VER-006** — Fault injection: run each assertion with an unresolvable manifest, an unreadable surface, and an induced tooling error; assert a reported failure in every case with no pass, skip, or empty success.
- **VER-007** — Mutation check: in a scratch state, disable and then remove the registration; assert the gate reports the missing enforcement and that the change is visible in the gate configuration diff.
- **VER-008** — Self-inspection of the mechanism: compare the service-core dependency manifest and working tree before and after a full run, and inspect the mechanism for network calls; assert no added runtime dependency, no network call, and no modified service-core file.
- **VER-009** — Document inspection of the posture note against REQ-009 and REQ-010, confirming each required element is present and that no element asserts completion of the enforcement obligation.

## Governing Values and Decisions — Axiology

- **AX-001** — `OBJ-005` governs: everything PEC holds can be deleted at any moment without blocking any governed act. Zero third-party runtime dependencies and no external egress are what make that true from the outside — nothing external is entangled with PEC's presence.
- **AX-002** — `PEC-K-01` graceful absence and hard constraint `C1` govern the gate itself: it constrains PEC's own build. Its failure blocks a PEC release, never a governed act in any loop.
- **AX-003** — The standing shape of this contract is brief-directed contract design, informed by the `C-08` annotation rather than derived from an owner ruling on it (CLM-006, CON-002). It governs how the obligations below are written: treating a passing run as completion would convert a continuing assertion into a one-shot artifact, which the wave brief's direction and the deliverable's own description ("Automated assertion") both refuse. It is not a claim that the gate has been ruled release-blocking; that question is CON-002, routed at AC-011.
- **AX-004** — Constraint `C12` governs the fence: the §16 open owner decisions are not resolved here. CON-001 is recorded and fenced, not guessed, and `SOW-083` remains `TBD` in the ledger.
- **AX-005** — `ADR-002` is a carried live posture whose re-citation belongs to `DEL-00-01` under `SOW-088`. This deliverable enforces the live service rule `PEC-SVC-001` and claims no ADR authority; decision-log entry `DL-12` keeps package mechanics one-way — packages publish, dependants consume, and no deliverable writes into another package.
- **AX-006** — The accepted basis is `SOFTWARE_DECOMP.md` revision 1.2 at commit `3623b958b`, accepted through `SCA-002` under `D-PEC-64`. The revision 1.1 phrase in `_REFERENCES.md` is superseded provenance, not a competing authority.
- **AX-007** — Unknowns remain marked. TBD-002 through TBD-005 and CON-001 are recorded rather than resolved by inference; in particular the service-core boundary follows the `OI-012` decision that is the owner's to make at `DEL-00-01`'s ADR.
- **AX-008** — This contract is lifecycle-neutral. `_STATUS.md` remains the sole lifecycle authority, is untouched by the run that authored this document, and records `OPEN`; nothing here asserts that any enforcement exists.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-052 OBJ-005 | REQ-001, REQ-004, REQ-009, CLM-003, CLM-008, TBD-003, TBD-004, TBD-005 | AC-001 | VER-001 | Fixture set with expected verdicts, check output naming each offending dependency and importer |
| OUT-001 | SOW-052 OBJ-005 | REQ-002, CLM-003 | AC-002 | VER-002 | The admitted-set configuration read against the PEC-SVC-001 wording |
| OUT-001 | SOW-052 OBJ-005 | REQ-005, REQ-012 | AC-006 | VER-006 | Fault-injection transcripts showing failure on every degraded input |
| OUT-001 | SOW-052 OBJ-005 | REQ-008, REQ-012 | AC-008 | VER-008 | Before/after manifest and working-tree comparison for a full run |
| OUT-002 | SOW-053 OBJ-005 | REQ-003, REQ-004, REQ-009, CLM-003, CLM-009, CON-001 | AC-003 | VER-003 | Egress and local-transport fixture results with located failures, and a re-run under both readings of the open transport question showing identical verdicts |
| OUT-002 | SOW-053 OBJ-005 | REQ-005, REQ-012 | AC-006 | VER-006 | Fault-injection transcripts for the locality assertion |
| OUT-002 | SOW-053 OBJ-005 | REQ-008, REQ-012 | AC-008 | VER-008 | The same self-inspection record showing no added runtime dependency, no network call, and no modified service-core file |
| OUT-003 | SOW-052 SOW-053 OBJ-005 | REQ-009, REQ-010, CLM-006, TBD-002 | AC-009 | VER-009 | The posture note itself, checked element by element against REQ-010 and against the recorded operative definitions |
| OUT-003 | SOW-052 SOW-053 OBJ-005 | REQ-011, CON-001, AX-002, AX-004 | AC-010 | HUMAN_REVIEW: accountable owner confirmation, recorded against this deliverable, that the posture note and both assertions leave OI-009 / SOW-083 open and make no governed act depend on PEC-held state | Dated owner ruling naming the fenced open decision and confirming the graceful-absence posture |
| OUT-001 | SOW-052 OBJ-005 | REQ-006, CLM-006, CLM-007, AX-003 | AC-004 | VER-004 | Registration records for the dependency assertion binding each execution to the state it evaluated |
| OUT-001 | SOW-052 OBJ-005 | REQ-007, CLM-006, CON-002 | AC-005 | VER-005 | Blocking-verdict demonstrations for the dependency rule and for a withheld check |
| OUT-001 | SOW-052 OBJ-005 | REQ-006, CLM-007 | AC-007 | VER-007 | A mutation run showing the disabled registration reported rather than silently skipped |
| OUT-002 | SOW-053 OBJ-005 | REQ-006, CLM-006, CLM-007, AX-003 | AC-004 | VER-004 | Registration records for the locality assertion on the same terms |
| OUT-002 | SOW-053 OBJ-005 | REQ-007, CLM-006, CON-002 | AC-005 | VER-005 | Blocking-verdict demonstrations for the egress rule and for a withheld check |
| OUT-002 | SOW-053 OBJ-005 | REQ-006, CLM-007 | AC-007 | VER-007 | A mutation run showing the disabled registration reported rather than silently skipped |
| OUT-003 | SOW-052 SOW-053 OBJ-005 | REQ-007, CLM-006, CON-002, AX-003 | AC-011 | HUMAN_REVIEW: accountable owner confirmation or declination that the enforcement carries release-gating authority, given C-08's "owner confirmation requested" note and D-PEC-62 §1.4's acceptance of the standing-node set as a recorded-but-unresolved non-gating annotation | Dated owner ruling recorded against this deliverable, stating whether a blocking verdict blocks a release candidate or is advisory, and leaving the contract's standing framing intact either way |
