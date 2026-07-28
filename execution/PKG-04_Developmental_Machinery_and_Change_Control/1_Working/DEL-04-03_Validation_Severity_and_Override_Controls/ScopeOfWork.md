---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-04-03
package_id: PKG-04
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-039]
package_objective_refs: [OBJ-003]
---

# Scope of Work — DEL-04-03

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-04-03`, "Validation
Severity and Override Controls", a `CI_CD_CHANGE`-type deliverable of
`PKG-04 Developmental Machinery and Change Control`. It serves project scope
item SOW-039 and package objective OBJ-003.

Per its `_CONTEXT.md` Description, the deliverable exists to keep validation
deterministic and severity-typed with exit-code semantics and human-only
recorded BLOCK override, to keep BLOCK bounded to its declared observation
boundary, and to keep validator findings from mechanically rejecting owner-ruled
content.

The accepted decomposition states no per-deliverable acceptance criteria;
`_CONTEXT.md` records that as unresolved rather than inferring criteria
(K-INVENT-1). The `AC-*` and `VER-*` records below are therefore **candidates**
proposed from the four authorized grounding sources — the deliverable register
row, `_CONTEXT.md`, the scope-ledger statement of SOW-039, and the adopted
`docs/PRD_ROOT.md`. They assert no acceptance, no approval, and no lifecycle
state; the owner disposes of them at the review gate.

### Grounding sources

- Deliverable register row `DEL-04-03_Validation_Severity_and_Override_Controls`
  in `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`.
- `_CONTEXT.md` of this deliverable.
- Scope-ledger row SOW-039 in
  `execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv`.
- `docs/PRD_ROOT.md` §5.3 commitment D-5, §5.1 commitment N-3, and §4.2.

## Deliverable Definition — Ontology

The anticipated artifacts named in the register row and in `_CONTEXT.md`
Anticipated Artifacts define three outputs.

- **OUT-001** — Severity conformance report: a report over the examined
  validator set recording whether findings are severity-typed from the declared
  vocabulary and whether the severity-to-exit-code mapping holds.
- **OUT-002** — Override-record format: a record format for a human-only
  override of a BLOCK, fixing what an override must capture to be a recorded
  act rather than a silent bypass.
- **OUT-003** — Defective-validator escalation path: a written path for the case
  where a validator finding trips on owner-ruled content, routing the defect to
  the validator rather than to the ruled content.

Descriptive claims that fix what this deliverable is about:

- **CLM-001** — SOW-039 states that validation is deterministic and
  severity-typed with exit-code semantics and human-only recorded BLOCK
  override, that BLOCK never means globally proven safe or unsafe, and that a
  validator finding may never mechanically reject content the owner has ruled —
  where ruled text trips a validator, the validator is defective. Source:
  scope-ledger SOW-039, `SourceRef` PRD §5.3 D-5 [TRANSCRIBED].
- **CLM-002** — PRD §5.3 D-5 names the severity vocabulary as BLOCK, REVIEW,
  WARN, INFO, and NOT_APPLICABLE, with exit-code semantics and a human-only
  recorded BLOCK override. That vocabulary and its exit-code mapping are
  implemented at this basis in `tools/practitioner_harness/harness_common.py`.
- **CLM-003** — BLOCK carries a declared observation boundary. Per CLM-001 a
  BLOCK reports what a specific check observed within its own scope; it is not
  a claim that the subject is globally proven safe or unsafe, and a report that
  reads a BLOCK as such a claim misstates it.
- **CLM-004** — Defectiveness runs toward the validator. Per CLM-001, ruled
  content that trips a check is evidence about the check. The corresponding
  repair is to the validator, never an amendment to what the owner ruled.
- **CLM-005** — Machinery gates preconditions; it does not judge. PRD §4.2 states
  that deterministic tools, guards, and validators supply findings to the three
  human judgments and gate objective preconditions but never perform any of
  them, and PRD §5.1 N-3 holds that no machine BLOCK on the issuance judgment
  may be non-overridable.
- **CLM-006** — The register row types this deliverable `CI_CD_CHANGE` with
  `ContextEnvelope: M` and the note "One severity model across the validator
  set", bounding the work to one severity model applied across the examined
  validators.
- **CLM-007** — A human-only recorded BLOCK override already exists at this
  basis. `tools/scaffolding/write_status.sh` accepts
  `--force-human-override <reason>`; the flag is refused when the actor does not
  normalize to HUMAN, converts a BLOCK into a recorded override when it does,
  never converts a usage error into an override, and appends the reason to the
  deliverable's `_STATUS.md` history line as `[override: <reason>]`. The
  facility is registered in `tools/REGISTRY.md` as "human-recorded override via
  `--force-human-override`". OUT-002 therefore reconciles with running prior art
  rather than inventing an override discipline from nothing.

## Completion and Reliance Basis — Epistemology

Requirements restate the covered scope obligation as checkable production
requirements. They are candidates for owner disposition, not accepted criteria.

- **REQ-001** — The report of OUT-001 shall record, per validator in the examined
  set, whether every emitted finding carries a severity drawn from the declared
  vocabulary of CLM-002, treating an untyped or off-vocabulary severity as a
  finding rather than normalizing it.
- **REQ-002** — The report shall record the severity-to-exit-code mapping each
  examined validator exhibits and shall report a deviation from the declared
  mapping as a finding.
- **REQ-003** — The report shall record, for each BLOCK it examines, the
  declared observation boundary of the check that raised it, so that no BLOCK in
  the report reads as a global safety or unsafety claim, per CLM-003.
- **REQ-004** — Determinism shall be treated as a checkable property: the report
  shall record that a repeated run over unchanged inputs produced the same
  findings and the same exit code, and shall report a divergence as a finding.
- **REQ-005** — The format of OUT-002 shall be defined against the existing
  facility of CLM-007, not independently of it: it shall cite
  `tools/scaffolding/write_status.sh --force-human-override` and its
  registration in `tools/REGISTRY.md`, and shall carry forward what that
  facility already establishes — a human-only gate on the override, a stated
  reason, and visible persistence of that reason in the subject's own history
  rather than a silent bypass.
- **REQ-009** — Beyond what CLM-007 already persists, the format of OUT-002
  shall additionally require the specific BLOCK finding overridden and the scope
  and commit the override binds to. Both are outside what the existing facility
  writes: the overridden code is emitted only to stderr as
  `OVERRIDE recorded (HUMAN): <code>`, and no commit binding is recorded at all.
  The format shall admit no machine-issuable override and no blanket or standing
  override, and shall record any field it requires that the existing facility
  does not yet capture as an extension of that facility rather than a defect
  claim against it.
- **REQ-006** — The path of OUT-003 shall specify, for a validator that trips on
  owner-ruled content, the steps that record the defect and route repair to the
  validator, and shall state explicitly that amending the ruled content is not
  an available remedy, per CLM-004.
- **REQ-007** — No output of this deliverable shall itself override a BLOCK, rule
  on content, or assert acceptance, approval, or lifecycle transition. Findings
  are observations routed to the owner.
- **REQ-008** — Production shall write only under the execution tree.
  `_CONTEXT.md` records `AnticipatedWriteLocus: tools/ (M2); execution-tree for
  evidence`. That locus is a planning note and not authorization: any change to
  a validator under `tools/` requires an independently authorized M2 tranche,
  which this Scope of Work does not grant and cannot grant. Within this
  deliverable the validator set is observed and reported on, not modified.

Candidate acceptance criteria:

- **AC-001** — For every validator in the examined set, the OUT-001 report
  records each emitted finding's severity as a member of the declared
  vocabulary, records the observed exit code against the declared mapping, and
  records the repeated-run result; every deviation appears as an explicit
  finding.
- **AC-002** — The OUT-002 format cites the existing `--force-human-override`
  facility of CLM-007 as its prior art, carries forward the human-only gate, the
  stated reason, and the visible persistence that facility already provides,
  additionally requires the specific BLOCK overridden and the bound scope and
  commit, and contains no machine-issuable, blanket, or standing override path.
- **AC-003** — The OUT-003 path routes a validator tripping on owner-ruled
  content to validator repair, states that amending the ruled content is not an
  available remedy, and names where the defect is recorded.

## Production and Verification Method — Praxeology

Production reads the four grounding sources and observes the live severity
model, then writes the report, the format, and the escalation path under the
execution tree. At this basis the severity vocabulary of CLM-002, the exit-code
constants, and the severity-to-exit-code computation are implemented in
`tools/practitioner_harness/harness_common.py`, which also carries the rule that
findings on unratified invariants are advisory rather than BLOCK. That module is
observed, not modified.

- **VER-001** — Deterministic severity and exit-code observation: run each
  validator in the examined set, capture its emitted finding severities and its
  process exit code, and compare both against the declared vocabulary and the
  declared exit-code mapping. Re-run each over unchanged inputs and compare the
  two captures byte-for-byte to evidence the determinism REQ-004 requires. A
  mismatch in either comparison is recorded as a finding.
- **VER-002** — Deterministic ruled-content regression check: run the examined
  validator set over a fixture whose content reproduces owner-ruled text, and
  confirm that no BLOCK is raised against that content. A BLOCK raised on ruled
  content is recorded as a defect against the validator and routed through
  OUT-003, per CLM-004; it is never routed as a defect in the ruled content.
- **VER-003** — Deterministic write-locus check: confirm by path inspection that
  every artifact produced by this deliverable resolves under the execution tree
  and that no file under `tools/` or the wider instruction surface — `AGENTS.md`,
  `agents/`, `skills/`, root `docs/`, `init/`, `.github/workflows/` — was written
  by this deliverable's production, consistent with REQ-008.
- **VER-004** — Deterministic override-facility exercise: against a disposable
  fixture deliverable folder created for the check, run
  `tools/scaffolding/write_status.sh` with `--force-human-override <reason>` and
  a HUMAN actor over a transition that raises a BLOCK, and confirm exit 0,
  `OVERRIDE recorded (HUMAN)` naming the overridden code on stderr, and the
  reason present in the fixture `_STATUS.md` history line as
  `[override: <reason>]`. Run the same invocation with a non-HUMAN actor and
  confirm the refusal path — exit 1, the `does not normalize to HUMAN` note, and
  the fixture `_STATUS.md` unchanged. Run the three checks that already cover
  this facility in `tools/practitioner_harness/test_write_status_guard.py`:
  `test_force_human_override_records_reason`,
  `test_force_human_override_requires_human_actor`, and
  `test_force_human_override_never_overrides_usage_errors`. Any departure from
  these observed behaviours is recorded as a finding.
- **VER-005** — Deterministic override-field differential: enumerate the fields
  the facility of CLM-007 actually persists in the history line it writes —
  date, target state, actor string, and reason — and compare that set
  field-by-field against the set REQ-005 and REQ-009 fix, recording each
  required field as either already persisted by the existing facility or
  supplied by this deliverable's format. The resulting delta is the evidence
  that OUT-002 extends the facility rather than duplicating or contradicting it.

The override mechanism of CLM-007 is running and exercisable at this basis, so
OUT-002 is verified against it rather than deferred to a reading. Two honest
bounds hold. First, that facility guards lifecycle transitions in
`write_status.sh`; whether an equivalent recorded override belongs on the wider
examined validator set is a question OUT-002 raises for the owner, not one this
Scope of Work settles. Second, the facility is observed and exercised against
disposable fixtures only — it is never invoked against a governed member's
`_STATUS.md`, and `write_status.sh` itself is read, never modified, per REQ-008.

## Governing Values and Decisions — Axiology

- **AX-001** — Machinery supplies findings; humans judge. Per CLM-005, a
  validator gates objective preconditions and never performs the evaluation,
  iteration, or release judgment, and no machine BLOCK on the issuance judgment
  is non-overridable.
- **AX-002** — Override is human-only and recorded. An override that leaves no
  attributable record is indistinguishable from a bypass, which is why the
  format fixes identity, subject, reason, and binding scope. The facility of
  CLM-007 already holds the human-only and recorded-reason half of that value in
  running code; this deliverable extends it rather than restating it.
- **AX-003** — A BLOCK is bounded. Per CLM-003 it reports one check's
  observation within its declared boundary and claims nothing globally; reading
  it as a proof of safety would overstate what any check can establish.
- **AX-004** — The validator yields to the ruling. Per CLM-004, where ruled text
  trips a check, the check is defective; the remedy is repair of the check, and
  mechanically rejecting ruled content is prohibited rather than merely
  discouraged.
- **AX-005** — The instruction surface is governed separately. `_CONTEXT.md`
  places `tools/` under M2 for this deliverable. This Scope of Work grants no
  such authorization, and its acceptance would grant none — so a defect this
  deliverable finds is reported, and its repair is a separate authorized act.
- **AX-006** — Nothing is inferred beyond the authorized sources (K-INVENT-1).
  Where the accepted decomposition is silent — on per-deliverable acceptance
  criteria, and on `ResponsibleParty`, which is `Ryan Tufts` under D-GOV-27 and the current deliverable register — the accepted assignment is preserved, while the acceptance-criteria silence is surfaced.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-039 OBJ-003 | CLM-001 CLM-002 CLM-003 CLM-006 REQ-001 REQ-002 REQ-003 REQ-004 REQ-007 | AC-001 | VER-001 VER-003 | Per-validator capture of emitted severities and exit codes, the repeated-run comparison, the declared observation boundary per examined BLOCK, and every deviation as a listed finding |
| OUT-002 | SOW-039 OBJ-003 | CLM-001 CLM-005 CLM-007 REQ-005 REQ-007 REQ-008 REQ-009 | AC-002 | VER-003 VER-004 VER-005 | Format definition citing the existing `--force-human-override` facility, the fixture-run capture of a recorded override and of the non-HUMAN refusal, the results of the three named guard tests, and the persisted-versus-required field differential |
| OUT-003 | SOW-039 OBJ-003 | CLM-001 CLM-004 REQ-006 REQ-007 REQ-008 | AC-003 | VER-002 VER-003 | Escalation-path document plus the ruled-content regression result, with any BLOCK raised on ruled content recorded as a validator defect and routed for separately authorized repair |
