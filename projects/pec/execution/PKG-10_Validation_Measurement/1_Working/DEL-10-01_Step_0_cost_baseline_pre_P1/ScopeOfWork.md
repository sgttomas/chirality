---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-10-01
package_id: PKG-10
decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@11a494e9a
project_scope_refs: [SOW-058]
package_objective_refs: [OBJ-001, OBJ-006]
---

# Scope of Work — DEL-10-01 Step-0 cost baseline (pre-P1)

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-10-01` in package `PKG-10`
(Validation & Measurement). It covers project scope item `SOW-058` and supports
package objectives `OBJ-001` and `OBJ-006`.

`SOW-058` states: "Measure the Step-0 cost baseline (LLM tokens per
loop-iteration orientation) before P1 begins; this re-tests the harness
query-pain precondition recorded unmet 2026-07-02"
(`execution/_Decomposition/ScopeLedger.csv`, row `SOW-058`, `SourceRef` =
"§11.1, §2", `OpenIssue` = FALSE, Notes = "Sequencing obligation, pre-P1;
baselines SOW-004/041"; mirrored at
`execution/_Decomposition/SOFTWARE_DECOMP.md` §Scope Ledger).

`OBJ-001` states: "Orientation for any loop is a sub-second query with per-claim
citations, not a session-length prose derivation" (`SOFTWARE_DECOMP.md`
§Objectives, `SourceRef` = §3.1; `projects/pec/docs/PRD.md` §3 outcome 1).

`OBJ-006` states: "The product thesis remains measurable and falsifiable:
adoption, parity, defect, and collision metrics are gathered in system behavior
and the §11 falsification clause stays armed" (`SOFTWARE_DECOMP.md` §Objectives,
`SourceRef` = §11).

**Objective warrant (register-direct, both objectives).** The
`DEL-10-01` → {`OBJ-001`, `OBJ-006`} attribution is carried directly in the
accepted registers and predates `SCA-002`; this contract records it rather than
deriving it. `ScopeLedger.csv` row `SOW-058` carries `ObjectiveIDs` =
`OBJ-001;OBJ-006`. `Deliverables.csv` row `DEL-10-01` carries
`SupportsObjectives` = `OBJ-001;OBJ-006`. `SOFTWARE_DECOMP.md` §Objectives lists
`SOW-058` under `OBJ-001` explicitly as an instrument ("instruments: SOW-058,
SOW-059") and among `OBJ-006`'s mapped scope items, and lists `DEL-10-01` in the
`MappedDeliverables` cell of both rows. The dual mapping is the register's own:
this deliverable measures the thing `OBJ-001` promises (orientation cost) using
the measurement posture `OBJ-006` requires (gathered in observable system and
use behavior, keeping the §11 falsification clause armed). No new derivation is
asserted here.

**Basis-revision note.** `_REFERENCES.md` now names
`execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.3 as the accepted
`current_basis` under the reference-parity integration at `af62343d3`.
`_CONTEXT.md` retains the revision-1.1 to revision-1.2 supersession trace;
SCA-003 establishes revision 1.3 as the current successor. The accepted basis
bound in this contract's frontmatter is revision 1.3 at merge `11a494e9a`,
and this contract cites revision 1.3.

- **OUT-001** — The Step-0 cost measurement method: a documented, repeatable protocol for measuring LLM tokens per loop-iteration orientation, defined so that the same protocol yields the post-P1 "after" measurement of the same metric.
- **OUT-002** — The pre-P1 baseline report: the "before" values captured under `OUT-001`'s method before P1 begins, together with the re-test of the practitioner-harness query-pain precondition recorded unmet on 2026-07-02.

## Deliverable Definition — Ontology

### Identity

- **CLM-001** — `DEL-10-01` is named "Step-0 cost baseline (pre-P1)", Type `MEASUREMENT`, Context Envelope `S` with no envelope notes, `PhaseHint` `pre-P1`, `ResponsibleParty` `TBD`, covering `SOW-058` and supporting `OBJ-001;OBJ-006`; source `execution/_Decomposition/Deliverables.csv` row `DEL-10-01` and `SOFTWARE_DECOMP.md` §5 table for `PKG-10`.
- **CLM-002** — The deliverable description of record is: "LLM tokens per loop-iteration orientation, measured before P1; re-tests the harness query-pain precondition (unmet 2026-07-02)"; source `Deliverables.csv` row `DEL-10-01`, restated in `_CONTEXT.md`.
- **CLM-003** — The anticipated artifact class of record is "Measurement method + baseline report"; source `Deliverables.csv` `AnticipatedArtifacts` for `DEL-10-01`. The outputs of this deliverable are a measurement instrument and its captured evidence, not product code.
- **TBD-001** — `ResponsibleParty` is unassigned; assignment happens at WORKING_ITEMS activation, not in this contract (`SOFTWARE_DECOMP.md` §5 preamble; `_CONTEXT.md`).
- **TBD-002** — The sampling design of the baseline — which loops and scopes are sampled, how many loop-iteration orientations constitute the baseline, and over what window — is not fixed by the accepted decomposition or by PRD §11.1, which state the metric but not its sampling. It is set by this deliverable's own method and remains unresolved in this contract.
- **TBD-003** — The concrete repository path at which the method document and the baseline report are published is not fixed by the accepted decomposition; it is set by this deliverable's packet and remains unresolved in this contract.

### Subject matter carried into the outputs

- **CLM-004** — The metric of record is PRD §11 success metric 1: "Step-0 cost: LLM tokens per loop-iteration orientation, before vs after; the 'before' baseline is measured before P1 begins (this also re-tests the query-pain precondition the practitioner harness recorded unmet on 2026-07-02)" (`projects/pec/docs/PRD.md` §11.1). PRD §11's current heading scopes all six metrics as "measured in observable system and use behavior"; observing consumer use creates no receiving-loop duty or conformance criterion.
- **CLM-005** — The measured condition of record is PRD §2: "Step 0 is the most expensive, most repeated computation in the OS. Every iteration of every loop re-derives the live lawful work surface from prose: >1,200 `_STATUS.md` files, ~230 decision records, receipts ledgers, workplans. Each derivation burns an LLM session, and the loop archives document the recurring failure mode: 'a fluent draft grounded on stale facts.'" PRD §2 closes with the same obligation this deliverable carries: "Step-0 cost is re-measured before P1 (§11)".
- **CLM-006** — The precondition being re-tested is the practitioner harness's own record: its cache half "remains closed by its own record (`tools/practitioner_harness/README.md` §Cache contract): its query-pain precondition was measured **unmet** on 2026-07-02 (slowest command ~4 s)", and a `D-PEC-57`/`D-PEC-58` ruling "neither directs the harness nor remeasures that precondition. §11 metric 1 re-measures Step-0 cost before P1" (`PRD.md` §15).
- **CON-001** — The unit of the re-test is not settled by the accepted sources. `SOW-058` and PRD §11.1 state the metric as **LLM tokens per loop-iteration orientation**, while the harness precondition being re-tested was originally recorded in **command latency** ("slowest command ~4 s", PRD §15). No accepted source states whether the re-test applies the harness's original latency criterion, the token metric, both, or a stated successor criterion. This contract records the ambiguity and requires the method to declare which criterion it applies; it does not resolve the question by inference, and no resolution may be read into this document.
- **CLM-007** — `OBJ-006`'s armed clause is PRD §11's falsification clause: if, after Phase 3, explicit consumer enablement or enabled-consumer orientation use remains negligible and the owner does not consult the dashboards, the product thesis is falsified; PEC is deleted and, by PEC-K-01, nothing breaks. Non-adoption is evidence about PEC, never external consumer nonconformance. This deliverable supplies the "before" leg of metric 1 that keeps that clause evaluable; it does not evaluate the clause, which is a post-Phase-3 act.
- **CLM-008** — The relationship to the harness is bounded by constraint C10: "Permanent parity-diff against the practitioner harness; PEC neither directs the harness nor opens its cache half" (`SOFTWARE_DECOMP.md` §1.3 "Hard constraints (identified at intake)", row `C10`; `PRD.md` §15) — a decomposition constraint label distinct from the deliverable-local dependency-register constraint row `C-10` (STRATUM_RULE) recorded in `_DEPENDENCIES.md`. Re-measuring Step-0 cost is a measurement, not a ruling about the harness.
- **CLM-009** — Measurement work is scope distinct from the behavior it measures. Decision-log entry DL-6 records: "§11 measurements and §12 exit tests enter as IN scope items (SOW-058..063, SOW-084, SOW-085) distinct from the behaviors they test; each Notes cell cross-links its behavior item"; and `PKG-10`'s declared exclusion is "The behaviors under test (their home packages)" (`SOFTWARE_DECOMP.md` §4 package table, §Decision Log DL-6).

### Placement in the work graph

- **CLM-010** — `DEL-10-01` has no upstream predecessors and is a valid root node; its declared downstream consumers are `DEL-04-01` (Loop orientation return, `SEQUENCING [E-A27]`) and `DEL-08-04` (Orientation latency budget p95 ≤ 100 ms, `SEQUENCING [E-A28]`); source `_DEPENDENCIES.md` and `Dependencies.csv` (v3.1, anchors `DEP-10-01-001` and `DEP-10-01-002`).
- **CLM-011** — The ledger records this deliverable as baselining the behaviors those consumers implement: `SOW-058` Notes read "Sequencing obligation, pre-P1; baselines SOW-004/041", where `SOW-004` is the per-loop orientation serve (`PKG-04`, `DEL-04-01`) and `SOW-041` is "Complete orientation reads in ≤100 ms at p95 against the current corpus" (`PKG-08`, `DEL-08-04`); source `ScopeLedger.csv` rows `SOW-004`, `SOW-041`, `SOW-058`.
- **CLM-012** — Two register-wide sequencing constraints bind this node: `C-04` (`PHASE_PRECEDENCE`, release-strategy ordering, with hard-versus-soft classification a Phase 1.3 owner ruling) and `C-05` (`PRE_P1_OBLIGATION`, "All three complete before any P1 node starts"); source `_DEPENDENCIES.md`. PRD §12 fixes P1 as "One-loop reconciler", so "before P1 begins" means before the P1 phase's first node starts.

## Completion and Reliance Basis — Epistemology

The requirements below state what the future measurement work must satisfy. No
measurement method and no baseline report exist for this deliverable at the time
of writing; `_STATUS.md` records state `INITIALIZED`. Nothing in this section asserts
that any baseline has been captured or that any value has been observed.

- **REQ-001** — The method shall define the measured unit — one loop-iteration orientation — in terms the accepted sources support (`CLM-004`, `CLM-005`), and shall state the sampling population, the sample count, and the observation window (`TBD-002`).
- **REQ-002** — The method shall define LLM tokens as the measure and shall state the counting boundary explicitly: which sessions, calls, and token classes (input, output, cached) are counted and which are excluded.
- **REQ-003** — The method shall be repeatable by a second party from its own text, and shall be stated so that the identical protocol produces the post-P1 "after" measurement of the same metric, making the "before vs after" comparison of PRD §11.1 well-defined.
- **REQ-004** — The method shall record its own measurement limits: what the metric does not capture, and what variation (corpus size, loop, model, session shape) it does not control for.
- **REQ-005** — The baseline report shall record the captured "before" values with, for each sampled orientation, the token count, the capture date, the corpus state (commit or SHA), and the loop and scope sampled; and shall record that capture occurred before any P1 node started (`CLM-012`).
- **REQ-006** — The baseline report shall record the re-test of the harness query-pain precondition: the criterion applied, the 2026-07-02 unmet record it re-tests (`CLM-006`), and the observed result stated as a measurement.
- **REQ-007** — Neither output shall direct the practitioner harness, open or recommend opening its cache half, or assert a ruling about it; the re-test reports a measurement against the harness's recorded precondition and nothing more (`CLM-008`).
- **REQ-008** — Neither output shall create scope, requirements, or acceptance criteria for the behaviors it measures; those remain with their home packages (`CLM-009`). The measurement instrument records what is observed, and its own method, only.
- **REQ-009** — The method shall state which criterion it applies for the precondition re-test — the harness's original latency criterion, the token metric, both, or a declared successor — and shall not silently substitute one unit for the other; if the choice is not settled at production time, the method shall carry `CON-001` forward as an open question rather than close it by assumption.
- **REQ-010** — Both outputs shall be complete and consumable before any P1 node starts, satisfying the `PRE_P1_OBLIGATION` constraint, and shall be consumable by `DEL-04-01` and `DEL-08-04` as their declared sequencing predecessor (`CLM-010`, `CLM-011`, `CLM-012`).
- **REQ-011** — Both artifacts shall be published at the path set by this deliverable's packet (`TBD-003`), and that path shall be recorded before the artifacts are treated as consumable; production shall write only within `PKG-10`.
- **REQ-012** — The baseline report shall not assert that any post-P1 "after" measurement has occurred, shall not compare against an unmeasured "after" value, and shall not itself evaluate the §11 falsification clause (`CLM-007`).

- **AC-001** — The published method defines the measured unit, the sampling population, the sample count, the observation window, and the token counting boundary, in text sufficient for a second party to repeat the measurement without further instruction.
- **AC-002** — The published method states its repeatability conditions and declared limits, and states in its own text that the identical protocol applies unchanged to the post-P1 "after" measurement of the same metric.
- **AC-003** — The baseline report records, for every sampled orientation, a token count, a capture date, a corpus commit or SHA, and the loop and scope sampled; every capture date precedes the start of the first P1 node.
- **AC-004** — The baseline report records the query-pain re-test with an explicitly named criterion, cites the 2026-07-02 unmet record, states the observed result, and contains no statement that directs the harness or opens its cache half.
- **AC-005** — Every statement in both artifacts is classifiable by a reviewer as measurement method, measured value, or declared limit; neither artifact contains a requirement or acceptance criterion for a behavior owned by another package.
- **AC-006** — The packet-recorded path exists and holds both the method document and the baseline report, and the production change set touches no path outside `PKG-10`.
- **AC-007** — The published method states which criterion the precondition re-test applies, or records `CON-001` as still unresolved and names what would settle it; neither artifact silently substitutes the token metric for the latency criterion or the reverse.
- **AC-008** — An accountable owner confirms that the captured baseline is fit to serve as the "before" leg of PRD §11 metric 1 and that the `PRE_P1_OBLIGATION` constraint is satisfied before any P1 node starts.

## Production and Verification Method — Praxeology

Production sequence expected of the future measurement run: read the accepted
basis row for `DEL-10-01`, the `SOW-058` ledger row, PRD §11.1 and §2, and the
harness record cited at PRD §15; draft the measurement method including its
sampling design (`TBD-002`), token counting boundary, and precondition-re-test
criterion (`CON-001`); record the packet path (`TBD-003`); execute the method
against the then-current corpus and capture the baseline values; author the
baseline report; publish under `PKG-10` only. Tests and deterministic checks
implement the verification methods below; they do not create scope or acceptance
criteria, and none of them may add a requirement that is not already stated in
this contract.

- **VER-001** — Document inspection of the published method against `SOW-058`'s ledger statement, the `SOFTWARE_DECOMP.md` §5 row for `DEL-10-01`, PRD §11.1 and §2, and `REQ-001`, `REQ-002`, `REQ-003`, `REQ-004`, `REQ-009`.
- **VER-002** — Data-completeness check of the baseline report: every sampled orientation carries a token count, capture date, corpus commit or SHA, and loop/scope identifier; the sample matches the method's declared sampling design; every capture date precedes the recorded start of the first P1 node.
- **VER-003** — Citation resolution and boundary check on the precondition re-test: the cited 2026-07-02 record and PRD §15 resolve to locatable text, the applied criterion is named, and no statement in either artifact directs the harness or opens its cache half.
- **VER-004** — Classification check against `REQ-008` and `REQ-012`: each statement in both artifacts is labelled method, value, or limit; no statement is a requirement or acceptance criterion for another package's behavior; no "after" value or falsification verdict is asserted.
- **VER-005** — Path and dependency check: the packet-recorded path exists and holds both artifacts, `DEL-04-01` and `DEL-08-04` can consume them as declared sequencing predecessors, and the change set touches no path outside `PKG-10`.

## Governing Values and Decisions — Axiology

- **AX-001** — `OBJ-006` governs the instrument: the thesis stays measurable and falsifiable only if metric 1 has a real "before" leg captured under a repeatable method. A baseline that cannot be reproduced, or whose method cannot be applied unchanged after P1, silently disarms the §11 falsification clause even though the clause's text remains.
- **AX-002** — `OBJ-001` governs the subject: the metric exists to test whether orientation becomes a sub-second cited query rather than a session-length prose derivation. What is measured before P1 is therefore the cost of the derivation PRD §2 describes, not the cost of any PEC capability, which does not yet exist at `pre-P1`.
- **AX-003** — Measurement is not participation. Constraint C10 and PRD §15 hold that PEC neither directs the practitioner harness nor opens its cache half; re-testing the query-pain precondition reports a value against the harness's own record and confers no authority over it.
- **AX-004** — The instrument never becomes the behavior. DL-6 and `PKG-10`'s declared exclusion keep the behaviors under test in their home packages; a measurement artifact that starts specifying `DEL-04-01` or `DEL-08-04` has left this deliverable's scope.
- **AX-005** — The accepted basis is `SOFTWARE_DECOMP.md` revision 1.3 at merge `11a494e9a`, accepted through `SCA-003`. Revision 1.1 and revision 1.2 references are superseded provenance, not competing authority.
- **AX-006** — Unknowns remain marked. `TBD-001`, `TBD-002`, `TBD-003`, and `CON-001` are recorded rather than resolved by inference. `CON-001` in particular is a unit-of-measure question the accepted sources do not answer; this contract fixes the obligation to declare a criterion, not the criterion itself.
- **AX-007** — This contract is lifecycle-neutral. `_STATUS.md` remains the sole lifecycle authority and is untouched by this reconciliation; the deliverable is at `INITIALIZED`, and no measurement method, no sampled orientation, and no baseline value exists.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-058 OBJ-001 OBJ-006 | REQ-001 REQ-002 REQ-003 REQ-004 CLM-004 CLM-005 TBD-002 | AC-001 AC-002 | VER-001 | Published measurement-method document stating unit, sampling design, sample count, window, token counting boundary, repeatability conditions, and declared limits |
| OUT-001 | SOW-058 OBJ-001 OBJ-006 | REQ-009 CON-001 CLM-006 | AC-007 | VER-001 VER-003 | Method text naming the criterion applied to the query-pain re-test, or carrying CON-001 forward with what would settle it, plus resolvable citations to the 2026-07-02 record and PRD §15 |
| OUT-001 | SOW-058 OBJ-001 OBJ-006 | REQ-008 CLM-009 AX-004 | AC-005 | VER-004 | Statement-level classification pass over the method showing method/value/limit labelling and no requirement or acceptance criterion belonging to another package |
| OUT-002 | SOW-058 OBJ-001 OBJ-006 | REQ-005 REQ-012 CLM-004 CLM-007 | AC-003 | VER-002 | Baseline report table with token count, capture date, corpus commit or SHA, and loop/scope per sampled orientation, all captured before the first P1 node started |
| OUT-002 | SOW-058 OBJ-001 OBJ-006 | REQ-006 REQ-007 CLM-006 CLM-008 AX-003 | AC-004 | VER-003 | Re-test section citing the harness's 2026-07-02 unmet record with a named criterion and an observed result, containing no direction to the harness and no cache-half recommendation |
| OUT-002 | SOW-058 OBJ-001 OBJ-006 | REQ-010 REQ-011 CLM-003 CLM-010 CLM-011 CLM-012 TBD-003 | AC-006 | VER-005 | Packet-recorded path holding both artifacts, availability to DEL-04-01 and DEL-08-04 as declared sequencing predecessor, and a change set confined to PKG-10 |
| OUT-002 | SOW-058 OBJ-001 OBJ-006 | REQ-010 AX-001 AX-002 CLM-012 TBD-001 | AC-008 | HUMAN_REVIEW: accountable owner confirmation that the captured baseline serves as the PRD §11 metric-1 "before" leg and that the PRE_P1_OBLIGATION constraint is satisfied before any P1 node starts | Dated owner ruling recorded against this deliverable, naming the accepted baseline artifacts and confirming the pre-P1 obligation |
