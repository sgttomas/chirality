# R0 Calibration Notes — DEL-10-01 DomainEngineProfile Contract Draft

- **Run:** `RUN_D55_CONCORDANCE_2026-07-11_1904Z` (D-APP-55, Option A)
- **Deliverable:** DEL-10-01 (PKG-10 Domain Engine Future Boundary)
- **Source state:** `main` = `4c8ed8907` — every evidence citation in the paired
  claims CSV binds to this SHA
- **Agent role:** TASK (bounded R0 method-calibration executor); date 2026-07-11
- **Method:** pinned plan `plans/PLAN_2026-07-10_deliverable_implementation_reconciliation.md`
  @ `551f84ef6` §§6–8; shared kernel `docs/DELIVERABLE_CONCORDANCE_METHOD.md` (RATIFIED)

> **Epistemic status: immutable, source-state-bound evidence artifact.** This
> file records claim-level findings and method-calibration observations. It is
> not authority, not a queue, and no disposition here is a human ruling.

## 1. Claim census

Paired ledger: `R0_CALIBRATION/DEL-10-01_claims.csv` — 28 rows.

| ClaimType | Count |
|---|---:|
| REQUIREMENT | 12 (REQ-001..011 + DOC-001) |
| ACCEPTANCE | 7 (six Datasheet Conditions + one Validation Notes row) |
| EXCLUSION | 4 |
| IMPLEMENTED_UNMAPPED | 2 |
| REMAINING_WORK | 3 |

| Disposition | Count | Rows |
|---|---:|---|
| ALIGNED | 22 | REQ-001..011, ACC-003..007, EXC-002..004, REM-001..003 |
| STALE_SPECIFICATION | 3 | DOC-001, ACC-001, EXC-001 |
| ACCEPTED_DIVERGENCE | 1 | ACC-002 |
| IMPLEMENTED_UNDOCUMENTED | 2 | UNMAPPED-1, UNMAPPED-2 |

Derived summary (per plan §7, a derivation and not a verdict): the contract
draft's substance is in strong concordance with the framework canon pin
(`agents/AGENT_DOMAIN_ENGINE.md@77a327727`, unchanged to `4c8ed8907`; REF table
8/8 sha256 re-verified MATCH) and with `docs/TYPES.md` §11.1. The stale rows are
all wording, not substance: the kit's future-boundary/CHECKING-era wording froze
in June while the corpus moved by ruling (D-APP-49..52 F3 steps, D-APP-54
rebaseline). The INSP-03 assessment is stale in all four of its gap conclusions
and in its source-state caveat (details in §3b).

Dependency provenance re-verified live per the AUTHORITY_MAP baseline rule: all
3 anchor rows (DEP-10-01-001..003) confirmed against the live decomposition at
`4c8ed8907` (PKG-10 package row §7 ~line 270; DEL-10-01 deliverable row §8 ~line
371; SOW-066/067 at §5 ~lines 224–225 and §9 ~lines 448–449). The D53A snapshot
bases hold; nothing relied on the snapshot without live confirmation.

## 2. Top findings

1. **The Release-scope exclusion wording is overtaken by ruled F3 steps**
   (ACC-001/EXC-001, STALE_SPECIFICATION). The Datasheet condition and the
   Specification out-of-scope list still assert that source types and domain
   MCP tools "must not be implemented as current-release scope," while
   D-APP-49..52 landed exactly those bounded surfaces (`domain-profile.ts` /
   `operation-proposal.ts` mirrors; the `mcp__chirality__domain_*` tool set).
   Endpoints and path hooks remain absent as stated. Repair is an R5 wording
   refresh, R4-gated.
2. **Frozen CHECKING-posture wording across three kit documents** (DOC-001,
   STALE_SPECIFICATION): Procedure Prerequisites/Verification, Specification
   Status-policy row, and Guidance all still say `_STATUS.md` "remains
   CHECKING"; the D-APP-54 rebaseline put the deliverable at IN_PROGRESS.
3. **INSP-03 is comprehensively stale as an evidence record** — every gap
   conclusion is overtaken (doc-only basis → D-APP-37; status-history mismatch
   → 2026-07-02 forward correction; validator/instance absence → validator +
   ADOPTED instance now exist; dependency closure → D-APP-53 DRQ-06 3/3
   SATISFIED), its REF-006 HASH_MISMATCH caveat no longer holds (8/8 MATCH
   recomputed), and its requirement numbering targets the pre-D-APP-45 spec.
   Claim substance mostly still passes, so staleness rides the
   AssessmentEvidence column rather than flipping dispositions (see §4 item 2).

## 3. R0 calibration self-report (plan §8/R0 criteria)

### (a) Correct authority precedence

The AUTHORITY_MAP sufficed everywhere; zero AUTHORITY_CONFLICT rows. The one
genuinely conflict-shaped tension — `docs/SPEC.md` §18's blanket
"must not be implemented as current-release scope" versus the live ruled tool
surfaces — resolved cleanly through AUTHORITY_MAP precedence note 1 ("a ruled
decision may amend/interpret" the corpus; each D-APP-49/50 register row names
the F3 fence as its subject). Without that note this deliverable would have
produced spurious AUTHORITY_CONFLICT rows; the note is the load-bearing line of
the map for PKG-10 and should be kept verbatim for R2.

Where precedence was still hard: choosing *which* stale-family disposition wins
once precedence is settled (see §4 item 3) — a disposition-vocabulary question,
not a precedence question.

### (b) Evidence granularity

Line-level and hash-level granularity was achievable and cheap: sha256
recompute of all 8 `_REFERENCES.md` rows, `git diff` emptiness of the REF-008
pin to `4c8ed8907`, enum-const line ranges in `domain-profile.ts`,
catalog/descriptor line ranges for tool posture, decomposition line numbers for
dependency rows. Adequate for a doc-heavy deliverable. One granularity gap: for
doc-only claims the ImplementationEvidence column is semantically awkward
(the documents *are* the implementation) — I wrote "documentary claim" plus the
exact doc sections, which worked but is a convention the method should name.

### (c) False-positive risk

Least confident rows, in order:

1. **ACC-001 / EXC-001 (STALE_SPECIFICATION, MEDIUM)** — the alternative
   reading (the exclusion speaks only to DEL-10-01's own scope, and DEL-10-01
   itself implemented nothing) would make both rows ALIGNED. I chose stale
   because a reader of the kit today would conclude no source types or domain
   MCP tools exist in the current release, which is false. If the R0 reviewer
   prefers the deliverable-scope reading, these two rows are the false
   positives.
2. **ACC-002 (ACCEPTED_DIVERGENCE, MEDIUM)** — turns on whether register
   rulings under the tier-0 stepwise lane count as the "future governed
   amendment" the Datasheet names. I read them as governed-but-not-R7, hence
   accepted divergence rather than ALIGNED or STALE.
3. **UNMAPPED-2 (MEDIUM)** — the domain MCP tool surface may already be mapped
   by DEL-10-04/DEL-10-05 requirements; their kits are outside this subscope,
   so the "unmapped" claim is provisional pending their R2 rows (named as the
   smallest next check in the row).

### (d) Scope vs current behavior distinction

Hardest exactly where the calibration sample predicted: the future-boundary
exclusions, where *behavior* moved by ruling while the deliverable *scope text*
froze. The discipline that worked: treat the kit text as declared state, the
rulings as accepted decisions, the tree as evidence, and let the disposition
carry the mismatch — never silently reading the rulings back into the kit. The
IMPLEMENTED_UNMAPPED rows kept ruled-but-unmapped behavior out of the
requirement rows, which preserved the distinction.

### (e) Usefulness of RemainingWork statements

Executable as `## Remaining` items with minor dressing: the three
STALE_SPECIFICATION rows share one natural R5 item ("refresh the release-scope
and lifecycle-posture wording to cite D-APP-49..52 / D-APP-54"), and the two
UNMAPPED rows produce one R3/R4 mapping question. All are phrased with a
target, a source citation, and an implied gate (R4), so they would drop into
`## Remaining` format cleanly. REM-row RemainingWork statements name the
smallest next check (e.g., re-verify the stage gate on app-dev surfaces before
flipping the descriptor), which is the right altitude.

## 4. Method friction and proposed run-local revisions

Concrete revisions for the run-local method before R2 (plan §8/R0 "revise the
run-local method before scaling"); none touches agent instruction files or
workflow contracts.

1. **Define the residual columns for non-REMAINING rows (plan §6 table).**
   `RecordedRemaining`/`RemainingSource`/`RemainingGate` are naturally
   NONE_RECORDED for requirement/acceptance/exclusion rows, but
   `SelectableUnderCurrentLoop` has no defined value when there is nothing to
   select. Convention used here: `NO` (nothing recorded = nothing selectable).
   Propose adopting that convention run-wide, or admitting a fourth value
   (`N/A`) by run-local extension — projects may extend, never weaken (kernel §3).
2. **ALIGNED vs STALE_ASSESSMENT collision (plan §6/§7).** When a claim aligns
   today but the inspection conclusion about it is overtaken, one Disposition
   cell cannot carry both facts. Convention used here: Disposition = current
   concordance state; the AssessmentEvidence cell ends with an explicit
   CURRENT / STALE / N/A verdict (plan §6 already requires "whether still
   current"). Reserve the STALE_ASSESSMENT disposition for rows where the stale
   conclusion is itself the operative finding. Propose run-wide adoption —
   otherwise R2 waves will tally stale assessments inconsistently.
3. **STALE_SPECIFICATION vs ACCEPTED_DIVERGENCE precedence (plan §7).** Both
   fit wording overtaken by a deliberate ruling. Rule used here: if the text
   flatly asserts a now-false state, STALE_SPECIFICATION (repair-shaped); if
   the text acknowledges the gate and the ruling permits a bounded/transitional
   difference, ACCEPTED_DIVERGENCE (no repair implied). Propose recording this
   tie-break in the run-local method.
4. **Assessment requirement-ID drift.** INSP-03 numbers its matrix against the
   pre-D-APP-45 requirement set; current REQ IDs do not correspond 1:1.
   Convention used here: AssessmentEvidence cites `old-REQnnn` explicitly and
   states the mapping (or "no direct conclusion"). Propose requiring this
   old-ID→claim mapping notation in R2 for any deliverable whose spec was
   rewritten after its assessment.
5. **Verification-basis vocabulary for doc-only claims.** Naming the D-APP-37
   basis per row worked (plan §6: name the appropriate verification basis
   rather than inventing a code test). Propose a short enumerated vocabulary
   for R2 CSV cells — e.g. `DOC-BASIS(D-APP-37)`, `RUN-INSPECTION@<sha>`,
   `RULING-RECORD(D-APP-nn)`, `SNAPSHOT+LIVE-REVERIFY(<snapshot>)` — to make
   the verification column machine-tallyable at R3.

**DEFERRED_AGENT_WORKFLOW observations:** none required a row. The one
agent-file surface touched — REF-008 `agents/AGENT_DOMAIN_ENGINE.md` — was
consumed strictly as a FROZEN_PROCESS_INPUT normative pin (hash + commit
verified, content never judged), which the plan §5 classification handled
without friction. No agent-instruction or skill-contract change is implied by
any row.

## 5. Gate-derivation verdict (the question this deliverable was sampled for)

**Verdict: the §6 columns are sufficient for layered gates, with one verbatim
convention and one derivation rule that should be written down.**

- **Layered suffixes fit in one column.** REM-001 carries both an owner-ruling
  gate `(gated: new owner ruling required — D-APP-53 2026-07-10 ruled Option A
  only)` and a stage gate `(stage-gated: F-APP-3 / tier-0 D-T0-08 stepwise
  lane)`. Preserving both suffixes verbatim in `RemainingGate` (rather than
  normalizing to one) lost nothing and kept the plan §3 boundary-9 discipline
  (suffixes preserved unless their owning authority changes them). Proposed
  rule for R2: `RemainingGate` = concatenated verbatim suffixes;
  `SelectableUnderCurrentLoop` = NO if **any** gate is unsatisfied; the
  binding (first-failing) gate is named in the verification cell.
- **Gate vs stage-gate distinction held up.** The gated item (REM-001) needs a
  human act to unlock (hence HumanDecisionNeeded = NEW-PACKET, no action
  proposed); the stage-gated item (REM-002) is already inside the D-APP-50
  grant and needs only an external state change (hence HumanDecisionNeeded =
  NO). The two columns plus HumanDecisionNeeded expressed that difference
  without extension.
- **Cross-project stage gate under F-APP-3: no real tension, one rule worth
  recording.** REM-002's gate lives in piping (DEC-064 / TP-RUNNER-014), which
  this run must not audit. Derivation succeeded entirely from app-dev surfaces:
  the descriptor's own `gateReason` and the catalog text at `4c8ed8907` state
  the entrypoint is provisional/TBD, so `NO` was derivable without crossing the
  fence. Proposed rule for R2: **derive cross-project gate status only from the
  consuming project's own pinned surfaces; if no such surface states it, the
  answer is UNKNOWN — never a cross-project read of the other project's
  execution tree.** The F-APP-3 boundary never blocked evidence gathering; the
  nearest approach was the Guidance cross-reference note naming the ADOPTED
  tier-0 instance, which was treated as declared kit context and not audited.
- **Doc-only acceptance path (D-APP-37) worked as the verification basis.**
  Every non-behavioral ALIGNED row names the D-APP-37 basis plus this run's
  source-state-bound inspection (and, where available, the D-APP-45
  conformance record) instead of a code test; the two rows with live
  corroboration (tool posture) cite it as corroboration, not as the basis.
  This is the pattern PKG-10's remaining four deliverables should reuse in R2.
