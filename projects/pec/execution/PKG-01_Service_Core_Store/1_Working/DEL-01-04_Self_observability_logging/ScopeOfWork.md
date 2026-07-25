---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-01-04
package_id: PKG-01
decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@3623b958b
project_scope_refs: [SOW-057]
package_objective_refs: [OBJ-006]
---

# Scope of Work — DEL-01-04 Self-observability logging

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-01-04` —
"Self-observability logging" — in `PKG-01` Service Core & Store of the PEC v2
build. It covers project scope item `SOW-057` in service of package objective
`OBJ-006`.

The accepted basis is `execution/_Decomposition/SOFTWARE_DECOMP.md`
**revision 1.2** (`current_basis`, SCA-002 successor; accepted 2026-07-25 at
D-PEC-64 closure, commit `3623b958b`). The deliverable-local `_REFERENCES.md`
still names revision 1.1; that phrase is superseded provenance from a deferred
pointer sweep and is not the basis of this contract, as `_CONTEXT.md`'s own
supersession line records.

**Objective warrant.** The `DEL-01-04` → `OBJ-006` attribution is
**register-direct**, not SCA-002-qualified. The `ScopeLedger.csv` row for
`SOW-057` already carried `OBJ-006` before SCA-002, and the `Deliverables.csv`
row for `DEL-01-04` already carried `SupportsObjectives` `OBJ-006`; revision
1.2 added no mapping here. The warrant is read directly from the accepted
register: `OBJ-006` is anchored at PRD §11, whose measurability outcome is that
the thesis metrics are "measured in system behavior, not human behavior" and
that the falsification clause stays armed. Metrics gathered in system behavior
require PEC's own runs to be observable, which is exactly what `SOW-057`
requires and this deliverable produces.

- **CLM-001** — `SOW-057` states: "Log PEC's own reconcile runs and ingest activity, inspectable (self-observability)", with SourceRef `PEC-SVC-006`, `InOutStatus` `IN`, `OpenIssue` `FALSE`, and an empty ledger note.
- **CLM-002** — `PEC-SVC-006` (PRD §10) states: "PEC's own reconcile runs and ingest activity are logged and inspectable (it is observable about itself)."
- **CLM-003** — `OBJ-006` states: "The product thesis remains measurable and falsifiable: adoption, parity, defect, and collision metrics are gathered in system behavior and the §11 falsification clause stays armed", anchored at PRD §11.
- **CLM-004** — `SOW-085` (`DEL-10-05`, Owner-consultation logging, P2) is recorded in the ledger as "grounded in SOW-057 self-observability", and PRD §11's preamble states the metrics are measured in system behavior; this deliverable is the observation substrate other `OBJ-006` instruments build on, and is not itself a metric.

## Deliverable Definition — Ontology

`DEL-01-04` is typed `OBSERVABILITY` at Context Envelope `S` with `PhaseHint`
`P1`. The decomposition register describes it as "Reconcile-run and
ingest-activity logging with an inspection command", records its anticipated
artifacts as "Logging module + inspection CLI verb + tests", and carries no
`ContextEnvelopeNotes`. It is a root node of the accepted dependency DAG:
`_DEPENDENCIES.md` declares no upstream predecessors, and `Dependencies.csv`
holds only the two ANCHOR rows (`DEP-01-04-001` package anchor,
`DEP-01-04-002` `SOW-057` requirement trace).

- **OUT-001** — A self-observability logging module in the PEC service core that records PEC's own reconcile runs and its own ingest activity as durable, append-only, content-minimal events on one common surface.
- **OUT-002** — An inspection command (CLI verb) that reads the recorded events and presents them, making the logged activity inspectable without reading the raw store.
- **OUT-003** — An automated test suite covering the module and the inspection command, implementing the verification methods declared in this contract.

- **CLM-005** — The two logged subject classes are PEC's own activity, not governed-loop content: a "reconcile run" is an execution of the reconciler (`DEL-03-01`, `SOW-010`/`SOW-021`, P1) and "ingest activity" is PEC's own event ingest (`DEL-07-01`, `SOW-033`/`SOW-039`, P3).
- **CLM-006** — Three consumer edges depend on this deliverable in the frozen gate exhibit, all downstream and informational in the deliverable-local register: `DEL-10-05` `[E-A26]` DECLARED ("SOW-085 note: 'grounded in SOW-057 self-observability'"), `DEL-03-01` `[E-N14]` PROPOSAL ("facility-first — logging facility precedes its emitting subjects"), and `DEL-07-01` `[E-N15]` PROPOSAL ("ingest-logging half is phase-staged to P3").
- **CLM-007** — PRD §6 records that "the append-only discipline of v1.0 PEC-I-11 applies to PEC's own event log", and `PEC-K-10` content-minimal restricts recorded values to "Paths, counts, SHAs, states, hashes — never file or diff content"; `PEC-SVC-005` places the store at a gitignored path with the content-minimal rule enforced at ingest.
- **CLM-008** — The deliverable is at lifecycle state `OPEN` with no implementation present. Every requirement, acceptance criterion, and verification method below states a contract on future production; none asserts that anything has been built.
- **CLM-009** — The system-level kill test is owned elsewhere and is not reachable from this deliverable. `SOW-055` — "delete the store, run representative governed workflows, nothing blocks" — and its PRD anchor `PEC-SVC-004` are covered by `DEL-10-02` (Kill test, standing release gate). `SOW-057`, which this deliverable covers, does not reach that gate, and the accepted edge register records no edge in either direction between `DEL-01-04` and `DEL-10-02`: this deliverable's only recorded relations are the three downstream consumer edges of CLM-006. `DEL-10-02` will observe graceful absence at the system level under its own contract; nothing here executes, gates on, or discharges it.
- **TBD-001** — `ResponsibleParty` is unassigned; the register records `TBD`, with assignment at WORKING_ITEMS activation.
- **TBD-002** — The concrete event schema, field set, serialization, on-disk file layout, and any rotation or retention policy of the log are not fixed by any accepted source; they are chosen during production within the bounds of REQ-003, REQ-004, and REQ-007.
- **TBD-003** — The inspection command's verb name, its host CLI surface, and its output shape are not fixed by any accepted source beyond the register phrase "inspection CLI verb"; they are chosen during production within the bounds of REQ-005.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — The module shall record every execution of PEC's own reconciler as a durable log event bearing a run identity and a timestamp, per the "Log PEC's own reconcile runs" limb of `SOW-057`.
- **REQ-002** — The module shall record PEC's own ingest activity as log events on the same surface and under the same event schema as reconcile-run events, so that the P3 ingest subject named in CLM-005 can emit without a schema change; the completion question raised by that phase gap is CON-001.
- **REQ-003** — Log records shall be content-minimal per `PEC-K-10`: paths, counts, SHAs, states, hashes and comparable identifiers only, never file or diff content, and never a restatement of authored text from any governed loop.
- **REQ-004** — The log shall be append-only, per the `PEC-I-11` discipline PRD §6 carries onto PEC's own event log; the module shall expose no in-place mutation or deletion of a recorded event.
- **REQ-005** — The inspection command shall present the recorded reconcile-run and ingest-activity events in recorded order with each event's identity and timestamp, and shall report an empty or absent log explicitly rather than presenting it as an observed clean run, per `PEC-SVC-006` "inspectable" and the honesty posture of `PEC-K-08`.
- **REQ-006** — Neither logging nor its absence shall block any governed act or any reconcile run: a deleted, unwritable, or absent log store shall degrade to an explicit absence report and shall never cause a reconcile or a governed workflow to fail, per `PEC-K-01` and the standing kill test `PEC-SVC-004`.
- **REQ-007** — The log shall reside under the gitignored store path per `PEC-SVC-005`, and the module and command shall introduce no third-party runtime dependency and no external network egress per `PEC-SVC-001` and `PEC-SVC-002`, whose standing enforcement is `DEL-01-05` covering `SOW-052` and `SOW-053`.
- **REQ-008** — Tests shall implement the verification methods declared in this contract; they shall not define scope, requirements, or acceptance criteria.

- **AC-001** — Every reconcile run produces exactly one durable log event carrying a run identity and a timestamp, and a fixture run whose event is suppressed is detected as a failure rather than passing silently.
- **AC-002** — Ingest-activity events validate against the same event schema as reconcile-run events, demonstrated by a fixture emitter, and the schema carries no reconcile-only assumption that would require a change when the P3 ingest subject arrives.
- **AC-003** — No recorded event carries file or diff content or restated authored text, only the `PEC-K-10` field classes, and the module refuses in-place mutation and deletion of any recorded event through every interface it exposes.
- **AC-004** — The inspection command presents recorded events in recorded order with each event's identity and timestamp, and reports an empty or absent log with an explicit statement that is distinguishable from a report of observed clean runs.
- **AC-005** — With the log store deleted, unwritable, or absent, a reconcile run completes unblocked and produces its normal result, and the inspection command reports the absence explicitly rather than as an observed clean run. The system-level kill test — deleting the store, running representative governed workflows, and asserting that nothing blocks — belongs to `DEL-10-02` under `SOW-055` and `PEC-SVC-004` (CLM-009); no accepted edge connects this deliverable to it, and this criterion neither exercises nor discharges it.
- **AC-006** — The module and the inspection command add no third-party runtime dependency, make no network call, and write only under the gitignored store path, leaving the `DEL-01-05` zero-dependency and locality assertion intact.
- **AC-007** — The automated test suite implements VER-001 through VER-006, executes in the service-core test run, passes, and introduces no acceptance criterion absent from this contract.

- **CON-001** — `SOW-057` names both the reconcile-run and the ingest-activity limb, and the register gives `DEL-01-04` a single `PhaseHint` of `P1`, but the only accepted emitting subject for the ingest limb (`DEL-07-01`) is `P3`, and the frozen DAG exhibit records "ingest-logging half is phase-staged to P3" as the rationale for edge `[E-N15]`. No accepted source states whether `DEL-01-04` completes at `P1` with the ingest limb implemented against no live emitter, or whether that limb is a `P3` completion obligation against a `P1` deliverable. This contract requires the facility and the common schema at `P1` (REQ-002, AC-002) and does not decide the completion question; it is an owner or WORKING_ITEMS ruling and nothing here may be read as settling it.

## Production and Verification Method — Praxeology

Production proceeds in the order event schema → logging module →
inspection command → tests, because each stage is the acceptance surface of the
next. The reconcile-run limb is exercised against a fixture reconciler stand-in
until `DEL-03-01` exists, per the facility-first ordering recorded for
`[E-N14]`. All work is bounded to the deliverable folder and the service-core
source it names; this contract authorizes no register, decomposition, or PRD
edit.

- **VER-001** — Execute a reconcile run against a fixture corpus and assert exactly one recorded event bearing run identity and timestamp, then run the same assertion against a fixture whose emission is suppressed and confirm the check fails.
- **VER-002** — Drive a fixture ingest-activity emitter through the module, assert its events validate against the same schema as reconcile-run events, and inspect the schema and module interface for reconcile-only fields or assumptions.
- **VER-003** — Apply a content-minimality check across generated events asserting only `PEC-K-10` field classes and no file, diff, or authored-text payload, then attempt in-place mutation and deletion through every module interface and assert both are refused.
- **VER-004** — Run the inspection command over populated, single-event, and empty log fixtures and assert recorded order, per-event identity and timestamp, and an explicit empty-or-absent report textually distinguishable from an observed-clean-run report.
- **VER-005** — Delete, make unwritable, and omit the log store in turn, then run a reconcile against a fixture corpus and assert unblocked completion with its normal result, plus an explicit inspection-command absence report in each case. Scope boundary: representative governed workflows and the kill test are not executed here; that is `DEL-10-02`'s standing gate under `SOW-055` (CLM-009), and no output of this method may be presented as satisfying it.
- **VER-006** — Inspect the service-core dependency manifest and the module and command import graph for third-party runtime dependencies and network calls, assert every write path resolves under the gitignored store path, and re-run the `DEL-01-05` locality and zero-dependency enforcement once that deliverable is available.
- **VER-007** — Run the service-core test suite and confirm that each of VER-001 through VER-006 has a corresponding executing automated test and that no test asserts a criterion absent from this contract.

## Governing Values and Decisions — Axiology

- **AX-001** — `PEC-K-01` graceful absence governs, with `PEC-SVC-004` as its standing release gate: PEC observing itself must never become something a governed act depends on. Logging is the first place that temptation appears, so REQ-006 and AC-005 are non-negotiable rather than best-effort.
- **AX-002** — `PEC-K-10` content-minimal governs the recorded events. Self-observability is not an exemption from the ingest-boundary rule; `PEC-SVC-005` states that rule is enforced at ingest, and PEC's own log is ingested state like any other.
- **AX-003** — PRD §6 carries the v1.0 `PEC-I-11` append-only discipline onto PEC's own event log. An observability record that can be rewritten cannot support §11's system-behavior measurement, which is why REQ-004 forbids mutation rather than merely discouraging it.
- **AX-004** — `PEC-K-02` files govern: the log records what PEC did, never what a governed loop decided. Log contents are not citable as authority over any loop's file truth, and no consumer may treat this deliverable's output as a source of governed state.
- **AX-005** — `C-04` PHASE_PRECEDENCE and `C-10` STRATUM_RULE are register-wide non-gating constraints. The `P1`/`P3` gap behind CON-001 is release-strategy ordering. Two of the three consumer edges in CLM-006 are `PROPOSAL` stratum (`[E-N14]`, `[E-N15]`) and the third is `DECLARED` (`[E-A26]`), and all three are *accepted* at those strata: `D-PEC-62` §1.4 records the owner accepting the DAG candidate "all strata as presented", so no stratum here is pending. What that ruling left recorded-but-unresolved is the enumerated set of flag annotations — `E-A11`, `E-P69`/`E-N02`, `E-N13`/`E-N18`, the `C-02` direction, and the `C-08` standing-node set — none of which attaches to any edge cited in this contract. Stratum is provenance, not authority.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-057 OBJ-006 | REQ-001, REQ-002, REQ-003, REQ-004, REQ-006, REQ-007, CLM-005, CLM-007, CON-001 | AC-001, AC-002, AC-003, AC-005, AC-006 | VER-001, VER-002, VER-003, VER-005, VER-006 | Event-schema documentation, recorded fixture events for both subject classes, suppressed-emission and mutation/deletion refusal transcripts, content-minimality check output, and dependency-manifest plus import-graph inspection records |
| OUT-002 | SOW-057 OBJ-006 | REQ-005, REQ-006, REQ-007, CLM-006, CLM-009, TBD-003 | AC-004, AC-005, AC-006 | VER-004, VER-005, VER-006 | Inspection-command output over populated, single-event, empty, and absent log fixtures, showing recorded order, per-event identity and timestamp, and the explicit absence report; reconcile-run transcripts under deleted, unwritable, and absent log stores showing unblocked completion (the kill-test transcript is DEL-10-02's evidence under SOW-055, not this deliverable's) |
| OUT-003 | SOW-057 OBJ-006 | REQ-008, CLM-008 | AC-007 | VER-007 | Service-core test-run output mapping each executed test to its declared verification method |
