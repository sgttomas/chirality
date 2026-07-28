---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-03-06
package_id: PKG-03
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-001, SOW-002, SOW-061, SOW-103]
package_objective_refs: [OBJ-002, OBJ-004]
---

# Scope of Work — DEL-03-06

## Purpose and Objective Traceability

This deliverable holds materialization readiness behind the D-GOV-21 §5.3 gate
— root `execution/` carries control-plane records only until it closes — and
carries one complete deliverable stream end to end once it does.

It covers four project scope items and supports one package objective:

- `SOW-001` (SourceRef: PRD §3 v1 boundary (a) [PROPOSED]) — v1 is reached only
  when the D-GOV-21 §6 sequence has closed through step 9: root packages
  materialized from an accepted root decomposition with G0–G4 registered and
  passing. The scope ledger records that materialization itself remains behind
  the D-GOV-21 §5.3 gate.
- `SOW-002` (SourceRef: PRD §3 v1 boundary (b) [PROPOSED]) — v1 requires the
  root product's own governed loop to have carried at least one complete
  deliverable stream end to end.
- `SOW-061` (SourceRef: PRD §6.1 [TRANSCRIBED]) — until the materialization gate
  closes, root `execution/` holds control-plane records only.
- `SOW-103` (SourceRef: PRD §10.3 [TRANSCRIBED]) — recorded in the scope ledger
  with `InOutStatus` of OUT: adoption does not materialize anything under root
  `execution/`, does not create a root decomposition, and does not change the
  public-export boundary. It is a boundary item this deliverable observes, not
  work it performs.
- `OBJ-002` — governed production of professional knowledge work: at least one
  complete deliverable stream runs decomposition → package/deliverable →
  checking → issuance decision, with every consequential acceptance, reliance,
  and issuance judgment performed by an accountable human.

The deliverable is a `REQ_SLICE` under context envelope M, whose envelope note
records readiness and evidence collection that **authorizes nothing on its own**.

**Authority boundary.** The D-GOV-21 §5.3 gate holds materialization. This
Scope of Work grants no materialization authority: it does not open the gate,
does not shorten it, and does not convert a readiness observation into
permission to materialize. The gate closes only through a separate,
human-gated act.

## Deliverable Definition — Ontology

The anticipated artifacts transcribed from the deliverable register are three
control-plane records.

- **OUT-001** — Readiness checklist. An enumeration of the preconditions that
  the covered scope places on step-9 materialization, each carrying a
  determinate state and an evidence anchor.
- **OUT-002** — Gate-state record. A record of whether the D-GOV-21 §5.3 gate is
  open or closed as observed at a named commit, together with the class of act
  that would change it.
- **OUT-003** — First deliverable-stream evidence. The collected evidence that
  the root product's own governed loop carried one complete deliverable stream
  end to end, once the gate has closed.

- **CLM-001** — Under `SOW-001`, materialization is conditional, not scheduled:
  the condition is an accepted root decomposition plus G0–G4 registered and
  passing, and the ledger records that materialization stays behind the §5.3
  gate regardless of how ready the checklist reads.
- **CLM-002** — Under `SOW-002`, the demonstration is scoped to the root
  product's own governed loop carrying one complete stream. That is the scope
  item this deliverable covers; nothing here claims a demonstration in any other
  working root.
- **CLM-003** — Under `SOW-061`, the hold has positive content: while the gate is
  open, root `execution/` holds control-plane records only. `OUT-001` and
  `OUT-002` are themselves control-plane records and conform to that limit.
- **CLM-004** — Under `SOW-103`, adoption is not materialization. The item is
  carried in the ledger as an OUT boundary statement with no mapped objective;
  this deliverable observes the exclusion so that a later reader cannot mistake
  an adoption act for the gate closing.
- **CLM-005** — Under `OBJ-002`, deterministic guards, fan-in gates, and
  structural validation gates remain lawful non-human gates: they gate on
  objective preconditions and hygiene and never make the acceptance or issuance
  judgment. The stream evidence must therefore show human judgment at each
  consequential point, not merely a sequence of passing checks.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — The readiness checklist shall enumerate each precondition that
  the covered scope items place on step-9 materialization, and each entry shall
  carry a determinate state and a resolvable evidence anchor. An unstated or
  implicit precondition is a defect of the checklist.
- **REQ-002** — The gate-state record shall state the observed gate state, the
  commit at which it was observed, and the class of act that would change it. It
  shall record a state and never effect one.
- **REQ-003** — While the gate holds, no output of this deliverable shall place
  anything other than control-plane records under root `execution/`, per
  `SOW-061`.
- **REQ-004** — The deliverable-stream evidence shall carry one stream through
  decomposition, package/deliverable production, checking, and the issuance
  decision, with every consequential acceptance, reliance, and issuance judgment
  attributed to an accountable human and with provenance sufficient for a
  reviewer to determine reliance.
- **REQ-005** — No output of this deliverable, and no state it records, shall be
  relied on as authorization to materialize. Readiness is a finding; closing the
  gate is a separate human act (`CLM-001`; `CLM-004`).

- **AC-001** — Every precondition in the readiness checklist carries a
  determinate state and an evidence anchor that resolves in the checkout, and a
  reviewer can tell from the checklist alone which preconditions are unmet.
- **AC-002** — The gate-state record names the commit of observation and the act
  class that would change the gate, and contains no statement that purports to
  change the gate state itself.
- **AC-003** — The stream evidence exhibits all four stages in order, and each
  consequential acceptance, reliance, and issuance judgment in it is attributed
  to an accountable human rather than to an agent or a passing check.

- **CON-001** — The accepted decomposition states no per-deliverable acceptance
  criteria for DEL-03-06, and `_CONTEXT.md` records them as TBD. `AC-001`
  through `AC-003` are candidate criteria authored under this initialization run,
  grounded only in the register row, `_CONTEXT.md`, the scope-ledger statements
  of `SOW-001`, `SOW-002`, `SOW-061`, and `SOW-103`, and the adopted PRD
  (K-INVENT-1). They claim no acceptance. `ResponsibleParty` is `Ryan Tufts` under D-GOV-27 and the current deliverable register.
- **CON-002** — `OUT-003` is producible only after the §5.3 gate closes, which
  this deliverable cannot cause. Its readiness half and its evidence half
  therefore complete at different times, and the second half is blocked on an act
  outside this scope. Surfaced for owner disposition; not resolved here.

## Production and Verification Method — Praxeology

Production of `OUT-001` and `OUT-002` proceeds now, under the hold: both are
control-plane records and are lawful while the gate is open (`CLM-003`).
Production of `OUT-003` is collection after the fact — the stream is carried by
the governed loop and this deliverable gathers what the loop leaves behind; it
does not stage a stream to satisfy its own criterion.

- **VER-001** — Materialization fence execution. Run
  `python3 tools/validation/validate_root_materialization_fence.py`, the
  validator registered in `tools/REGISTRY.md` for G0, and require exit 0. The
  fence blocks when `PKG-*`/`DEL-*` direct children exist under root
  `execution/` while G1–G4 are not registered and passing, and passes idle
  otherwise. This is the deterministic check on the containment condition that
  `SOW-061` and the §5.3 gate ordering state, and it binds the gate-state record
  to an observable fact rather than to a self-report.

The readiness checklist and the stream evidence turn on whether an enumeration
is complete and whether a judgment was genuinely human — neither of which a
command can decide. Their verification is explicit human review at the gate, and
no command is invented for them.

All verification here is read-only. Neither the fence run nor any review named
in this contract authorizes a materialization act.

## Governing Values and Decisions — Axiology

- **AX-001** — Readiness is not authorization. This is the governing value of the
  deliverable and the reason the context envelope records that it authorizes
  nothing on its own: a complete checklist increases what is known, never what is
  permitted (`REQ-005`; K-AUTH-1).
- **AX-002** — The hold is substantive, not ceremonial. `SOW-061` restricts what
  may exist under root `execution/` while the gate is open, so conformance is
  checkable during the wait rather than only after it (`VER-001`).
- **AX-003** — Human judgment at every consequential point. Under `OBJ-002`,
  deterministic guards are lawful gates on objective preconditions and never make
  the acceptance or issuance judgment; evidence that shows only passing checks
  does not satisfy the objective (`CLM-005`).
- **AX-004** — One stream carried honestly beats several claimed. The scope asks
  for a complete stream end to end, so partial coverage is reported as partial
  rather than aggregated into an appearance of completeness.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-001 SOW-061 OBJ-002 | CLM-001 CLM-003 REQ-001 REQ-003 REQ-005 | AC-001 | HUMAN_REVIEW: owner review of the checklist against the covered scope-ledger statements and PRD §3 v1 boundary (a) at the human-gated PR review | The checklist as a control-plane record, each precondition carrying its state and a resolvable evidence anchor, plus the reviewer's recorded disposition |
| OUT-002 | SOW-061 SOW-103 OBJ-002 | CLM-001 CLM-004 REQ-002 REQ-005 | AC-002 | VER-001 | The gate-state record naming its commit of observation, plus the captured exit status of the registered materialization-fence validator at that commit |
| OUT-003 | SOW-002 OBJ-002 | CLM-002 CLM-005 REQ-004 | AC-003 | HUMAN_REVIEW: owner review of the stream evidence against PRD §3 OBJ-2 at the human-gated PR review, confirming each consequential judgment is attributed to an accountable human | The end-to-end record of one deliverable stream across decomposition, package/deliverable production, checking, and the issuance decision, with provenance sufficient to determine reliance |

The matrix is the stable target. It records no lifecycle state and no
acceptance; the deliverable remains `OPEN`, and `_STATUS.md` is the sole
lifecycle authority. No row in it opens the D-GOV-21 §5.3 gate or authorizes
materialization.
