# RUN_BASIS — RUN_D128_CONCORDANCE_2026-09-21_1614Z

> **Epistemic status:** immutable, append-only, source-state-bound evidence artifact. It
> is not a queue, a selection surface or authority. Additions are appended as dated
> sections; frozen text is never rewritten.

- **RunID:** `RUN_D128_CONCORDANCE_2026-09-21_1614Z`.
- **Activation authority:** D-APP-128.
  - Ruled 2026-09-21: Option A (whole corpus, 54 deliverables); packet §6 as recommended;
    post-v3.0.1 App/Runtime commits accepted as baseline.
  - Ruling record: `execution/_Coordination/_DECISIONS/D-APP-128_RULING_2026-09-21.md`.
  - Merged to `main` at `0bdb43d94bbb071ffda23b4244ac33dbbbc06e66` (PR #836) **before any
    dispatch**, as the kernel §6 hard rule requires.
- **Pinned method:** the six files and SHA-256 values in ruling §4, at `00115c719`.
  - The adoption record is amended by packet Δ1–Δ11.
  - Run-local candidate conventions are in `CONVENTIONS_CANDIDATE.md`, which is
    **not in force** until the R0 gate.
- **Source state under review:** `main` `00115c71931bcae79909602d653740d3bb72dfa1`.
  - Every citation binds to this SHA unless a row says otherwise.
  - The activation merge `0bdb43d94` changes only D-APP-128 surfaces: the packet, the
    ruling, the register row, the 54 bootstrap items and the AgentRuns folder. Those are
    run artifacts, excluded from audit.
  - A mid-run change to audited paths marks affected claims `STALE_INPUT`.
- **Frozen reading tree:**
  - A detached worktree of this repository at `00115c719`, placed outside the repository
    in the HELP_HUMAN session scratchpad.
  - All workers read deliverables and code there.
  - A second detached worktree at the same SHA holds installs, builds and test runs, so the
    reading tree carries no `node_modules/` or build output.
  - Neither path is committed.
- **Gate transcripts:**
  - `GATE_TRANSCRIPTS/GATE_TRANSCRIPT_RUNTIME_00115c719.md`: Vitest 407/407 passed;
    typecheck and build exit 0.
  - `GATE_TRANSCRIPTS/GATE_TRANSCRIPT_APP_00115c719.md`: typecheck exit 0; Vitest 2,285
    passed and 4 skipped.
  - These replace MR-3's per-wave transcript. That replacement is a candidate for the R0
    gate, and is sound only because the source state is frozen.

## 1. Corpus census at dispatch (re-enumerated from the frozen tree)

- **Deliverables:**
  - 11 packages, `PKG-00`..`PKG-10`.
  - 54 `1_Working/DEL-*` deliverables: 53 `IN_PROGRESS`; `DEL-09-07` `OPEN`.
  - No `CHECKING` or `ISSUED` deliverables.
- **Audit units:** `R1_INVENTORY/CLAIM_INDEX.csv` (`_scripts/claim_index.py`) holds 1,746.
  - 1,635 `CLM` headings.
  - 52 claim-less contract sections (`SEC`).
  - 55 Remaining items (`REM`).
  - 4 Remaining prose notes (`REMTXT`).
  - The D-APP-128 bootstrap item is excluded; it is the run's own carrier.
- **APP-HOLD-1:**
  - The register is header-only; there are no holds.
  - Dispatch preflights are recorded under `PREFLIGHT/`. The R0 sample returned `ALLOW` for all 8.
- **Open register rows:** D-APP-116..119 are `AWAITING_RULING`. Per ruling §5.5.4, rows
  touching them carry `HumanDecisionNeeded = D-APP-11x` and are held from R5.

## 2. Concurrent-work check (2026-09-21 ~16:15Z)

- **Other worktrees on this machine:** one — a Codex worktree, detached at `fd195cf42`
  (PR #828 merge, an ancestor of `main`), with a clean status. It is stale, and no App
  work is in flight.
- **Recent `main` activity** since the packet: piping and public-export only.
- **App development** is paused by owner direction (2026-09-19).
- **Deferrals for contention:** none.

## 3. Evidence roots (packet Δ3; MR-6 split accepted by owner)

- **Implementation and verification evidence**, both read-only:
  - `projects/chirality-app-dev/frontend/**`;
  - `projects/chirality-runtime/packages/**` and `projects/chirality-runtime/tests/**`.
- **Not read:**
  - `projects/chirality-runtime/execution/**`;
  - any other project's execution tree.
- **Gate and lifecycle status** for Runtime-owned work comes only from App surfaces.
- **Packaged instruction bundle sources** are Root-owned: root `AGENTS.md`, `agents/**`,
  bundled `workflows/`, `.agents/skills`, `tools/`, `docs/`.
  - They are read only where an App deliverable packages, loads or presents them.
  - Findings are routed per Δ10 and are not repaired.

## 4. Fences and write boundaries

- **Discovery is read-only.** R0–R3 write only to:
  - this run folder;
  - `execution/_Coordination/AgentRuns/HELP-HUMAN-APP-20260921-CONCORDANCE/`.
- **Carried fences:**
  - no deliverable edit;
  - no lifecycle transition;
  - no `CHECKING -> ISSUED` (F-APP-4);
  - no hold change;
  - no agent-instruction or workflow change (Δ10);
  - no new standing surface (F-APP-5);
  - no F-APP-1..3 crossing;
  - no product, Runtime or cross-project edit.
- **Commits.** HELP_HUMAN is the only committer. Children never run git, tests, or
  installs.
- **Absolute paths.** No machine-specific absolute path is written to any run artifact.
  The validator checks this.

## 5. Authority and reliability map (ruling §5.5.2; finalized here)

| Class | Sources | Use |
|---|---|---|
| **GOVERNING** | `projects/chirality-app-dev/docs/{PRD,DIRECTIVE,CONTRACT,SPEC,TYPES}.md`; Root `docs/{DIRECTIVE,CONTRACT,SPEC,TYPES}.md` where App docs defer to them; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` and accepted SCAs (`execution/_ScopeChange/_LATEST.md` → SCA-APP-010, **status `OPEN_PENDING_DERIVATIVE_CLOSURE`**; earlier accepted SCAs by their records); `RULED` rows of `execution/_Coordination/_DECISIONS/_REGISTER.md` with their ruling records; D-GOV-43 (Codex host re-platform, topology A2) and its App application D-APP-127 | Normative scope and accepted decisions. A ruled decision stands over untranscribed corpus wording (MR-11 generalized). |
| **GOVERNING, flagged** | `RULED` rows whose effect is recorded as pending, held or unapplied: D-APP-104, 107, 121, 122, 123, 125, 126 (some superseded in part by D-APP-127) | Cite with the flag. Unapplied effect is not treated as landed. |
| **CONTEXT** | `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` §3, §10; `plans/steers/chirality_app_v3_g0_record_2026-08-22.md`; `plans/steers/chirality_app_v3_app_ruling_record_a*.md`, `…_root_ruling_record_r*.md` and other `chirality_app_v3_*` steers (self-labelled non-governing transcription sources); `execution/_ScopeChange/SCA-APP-008_*` (unaccepted; partly superseded); `execution/_Coordination/AgentRuns/APP_V3_*`, `APPDEV_V3_NODE_*`, `CHIRALITY_V3_APP_ADOPTION_20260909`; `R0_DONE_DECLARATION/V3_DONE_DECLARATION_CANDIDATE.md` (until the owner confirms it) | Explains divergences (`DirectionEvidence`) and drives `CauseTag`. **Never changes a Disposition.** |
| **Declared state** | Deliverable `ScopeOfWork.md`, `_STATUS.md`, `_CONTEXT.md`, `MEMORY.md`, `_DEPENDENCIES.md`/`Dependencies.csv`, `_REFERENCES.md`, `_SEMANTIC*.md` | The audited surface. |
| **Implementation / verification evidence** | §3 roots; gate transcripts | Behavior at `00115c719`. |
| **Assessment evidence** | `Assessment_INSP-03_*`, `Evidence_*`, `_run_records/**` | Recency judged per MR-1. Not current truth. |
| **Execution protocol** | `loop/LOOP_INIT.md`, `AGENTS.md`, `loop/LOOP_RECEIPTS.md` | Constrains execution; creates no scope. |
| **Historical** | `plans/**` other than the pinned adoption record; retired workplans; closed concordance runs (D-APP-55, 68/69, 85) | Provenance only. Closed runs are upstream evidence. |
| **Frozen process input** | Agent instructions, role files, workflow and skill bodies | Read only as packaged product content (Δ10). |

**Known basis defects,** carried as findings and not fixed:

- `decomposition_basis` pins differ across SoW frontmatter; there are at least three
  distinct commits.
- The DepClosure snapshot named by `_LATEST.md`
  (`CLOSURE_SCC-DECOMPOSE-SCA-APP-010_2026-09-05_1034`) says in its own text that the
  pointer was not moved. The pointer was later moved under D-APP-111.
- The 2026-09-19 work graph defers "authority corpus drift in CONTRACT, SPEC and PRD".

## 6. R0 plan and roster

- **Calibration sample** (ruling §5.5.5):
  - DEL-01-01, DEL-02-05, DEL-03-01 (double-blind: two independent workers), DEL-04-05,
    DEL-06-04, DEL-08-04, DEL-09-07 and DEL-10-01.
  - Reverse-pass area `frontend/src/lib/harness/**` (`AREA = HARNESS`).
  - One fresh verifier.
- **Roster:**
  - HELP_HUMAN (Agent 0): this session.
  - One WORKING_ITEMS calibration manager, owning `R0_CALIBRATION/**`, which dispatches the
    calibration TASK workers and the verifier.
  - One TASK assembles the v3 done-declaration candidate (`R0_DONE_DECLARATION/**`).
  - One TASK runs the R1 deterministic inventories (`R1_INVENTORY/**`, except
    `CLAIM_INDEX.csv`, which HELP_HUMAN owns). This overlap is authorized by ruling §5.5.6.
- **Model and mechanism.** All agents run Opus 5 at effort `high`, the owner-preset
  session inheritance. Mechanism: Claude Code harness-native descendants (D-GOV-35).
  Parentage and actual model are recorded per dispatch in `RUN_STATE.jsonl` and in
  manager returns.
- **Concurrency:** at most 16 agents including HELP_HUMAN.
- **Briefs** are stored under `BRIEFS/` with their SHA-256 in `RUN_STATE.jsonl`.
- **Exit.** R0 ends with `R0_CALIBRATION/R0_CALIBRATION_REPORT.md` and the owner gate. No
  deliverable is edited.

## Addendum 1 — R0 gate (appended 2026-09-21)

- **R0 gate ruled.** D-APP-129
  (`execution/_Coordination/_DECISIONS/D-APP-129_RULING_R0_GATE_RUN_D128_2026-09-21.md`).
  - A: all calibration §7 verdicts adopted. `CONVENTIONS.md` is now the rulebook, and
    `CONVENTIONS_CANDIDATE.md` is the historical R0 edition.
  - B: the done declaration stays CONTEXT; Q-01..Q-13 go to R4. This amends D-APP-128
    §5.5.3.
  - C: R2 scale-out as proposed, with the named questions R4-Q1..Q3.
  - D: scope extension to items 3–7. The governing documents and the invariant coverage
    register are excluded.
- **§4 fence amended by the adopted PostReleaseBasis rule.** Children may run
  **read-only** `git log`, `git show` and `git blame -L` against the frozen reading tree.
  No other git use is permitted, and none against the working repository.
- **Claim index regenerated.** It gained an additive `SubItems` column to implement the
  adopted splitting rule ("R1 should emit REQ, AC and VER bullets as index units").
  - The 1,746 keys are unchanged.
  - 120 units list 208 sub-items.
  - The validator's `V-SUBITEMS` check requires at least one row per listed sub-item.
  - R0 ledgers predate this and are not re-graded.
- **HELP_HUMAN accepts four integration interpretations** from
  `R0_GATE_INTEGRATION_NOTES.md` §3:
  1. A missing forward row cannot be added by errata; it goes to `reverse_notes`.
  2. `CONTEXT_CLAIM` dispositions follow the adopted text literally.
  3. `NOT_AUDITABLE` rows are exempt from the `CTX:`/`GOV:` prefix.
  4. Code reached from nothing takes `REACH=LEGACY_ONLY`, with `UNREACHED` in Notes. The
     tag vocabulary is not widened.
- **Not implemented.** MR-9's optional old-ID mapping column; the rule itself is adopted
  unchanged.
- **Extension index.** `R1_INVENTORY/EXTENSION_INDEX.csv` holds 221 units: DEC 38, DOC
  (item 4) 58, SOW 84, PRODAGENTS 9, harness developer docs 32. D-APP-116..119 are
  `AWAITING_RULING`, so they are not DEC units.

## Addendum 2: attribution correction (appended 2026-09-21)

- Addendum 1 attributed the whole §4 git amendment to the adopted PostReleaseBasis rule. That
  attribution is only partly right:
  - the PostReleaseBasis rule covers read-only `git blame -L`;
  - allowing read-only `git log` and `git show` against the frozen tree is HELP_HUMAN's own
    run-protocol choice, made so the evidence pack can be built.
- Neither D-APP-128 nor D-APP-129 limits child git, and the allowance stays read-only and
  confined to the frozen tree.
- Recorded after the PR #838 backcheck.

## Addendum 3: R2 rerun threshold counts verdict errors only (appended 2026-09-21)

Owner direction `r2_rerun_rule` (OWNER_DIRECTION.md, SHA-256 `1d76a273…0225f`). It replaces
the rerun criterion in `BRIEFS/R2_PACKAGE_MANAGER.md` step 7 from this point on, for wave 1
managers still running and for every later wave.

- **Verdict fields.** A ledger row's `Disposition` (including an errata row that changes
  one), and a reverse-file `Response` (`CLAIMED_BY` / `PARTIAL` / `NOT_MINE`, including the
  claim it names).
- **Rerun trigger.** A structural failure, or more than 10% of checked distinct rows REFUTED
  on a verdict field. Rows refuted only on other fields do not count toward the threshold.
- **Corrections instead of reruns.** Each refutation on any other field (evidence citations
  and line anchors, REACH, AuthorityTier, CauseTag, DirectionEvidence, LatestDecision,
  PostReleaseBasis, HumanDecisionNeeded, Notes, and so on) is recorded, by script from the
  verifier shard, in `<RUN>/R2/<PKG>/CORRECTIONS.csv` with the columns
  `ClaimKey,Field,SealedValue,CorrectedValue,VerifierShard,Evidence`. Nobody edits the sealed
  ledger. R3 applies CORRECTIONS.csv after errata, and the package summary shows the
  corrected figures next to the sealed ones.
- **Reporting is unchanged.** Every REFUTED and CONTESTED item, whatever the field, stays in
  VERIFICATION.md with its evidence.
- **Wave 1 transition.**
  - A rerun that is already running finishes and is verified under this rule.
  - No new rerun starts on field-only refutations.
  - Where a deliverable has more than one completed attempt, the ledger of record is the
    most recent attempt that passes under this rule. Earlier attempts stay where they are,
    marked superseded in STATE.jsonl.
  - Any verdict-field refutations in an earlier attempt are listed in VERIFICATION.md, so R3
    can compare the attempts.

## Addendum 4: named question R4-Q4 (appended 2026-09-21)

Owner direction `r2_tiebreak_q4` (OWNER_DIRECTION.md, SHA-256 `264bea63…6a3bd`) adds a
fourth named R4 question, proposed by the PKG-08 manager:

- **R4-Q4:** is the 2026-09-09 v3 four-role adoption (`9b005c23a`) a governing amendment of
  SPEC §7 and §13 and the persona and matrix contracts? App PRD, SPEC and CONTRACT were not
  amended.
- CONVENTIONS §2.4 and §10 now list it. The validator (`HDN_TOKEN`, MR-11 check) accepts
  `R4-Q4`, and a test covers it (76 tests pass).
- Ledgers sealed before this addendum keep plain `R4` on such rows; R3 maps them to R4-Q4 when
  it clusters. Nobody edits a sealed ledger for this.

## Addendum 5: STALE_SPECIFICATION / REMAINING_STATE_MISMATCH tie-break (appended 2026-09-21)

Owner direction `r2_tiebreak_adopt` (OWNER_DIRECTION.md, SHA-256 `97b37a0e…6a370`) adopts the
tie-break rule now in CONVENTIONS §2.6. It answers the DEL-06-02 double-blind result (Disposition
agreement 19/35), where most splits fell between these two verdicts.

- **Scope.** Forward passes not yet sealed at adoption, and every later wave. Sealed ledgers are
  not edited; R3 applies the rule when it clusters and records each re-mapping it makes.
- **Owner-deferred items.** DEL-06-02#CLM-005 and DEL-06-02#CLM-032, where the double-blind
  workers split between `IMPLEMENTED_DIFFERENTLY` and `STALE_SPECIFICATION`, are outside the
  rule. Both workers' verdicts stand side by side (worker A's ledger of record and worker B's
  ledger in `R2/PKG-06/DEL-06-02_B/`). R3 must not resolve them and carries both to R4 as
  owner-deferred items; the owner will decide after reviewing the surrounding context.

## Addendum 6: legacy-versus-live subject test for R4-Q1 (appended 2026-09-21)

Owner direction `r2_r4q1_subject_test` (OWNER_DIRECTION.md, SHA-256 `75a027b0…978a0`) adopts
the subject test now in CONVENTIONS §2.4. It answers PKG-04's finding that three independent
DEL-04-03 attempts cited R4-Q1 on 20, 4 and 1 rows, depending on whether the worker read a
requirement as product behaviour or as about the retained module.

- **Scope.** Forward passes not yet sealed at adoption, and every later wave. Sealed ledgers are
  not edited. R3 re-derives R4-Q1 on sealed rows by rule 3, by script from the REACH tags, and
  records each change it makes.
- **Expected effect.** Legacy-heavy packages show more R4-Q1 rows and fewer ALIGNED rows than a
  module-level reading gives. Every such row waits on the owner's R4-Q1 ruling.
- **Verifiers** grade new ledgers against the test. Where rule 1 still leaves the subject
  genuinely open, rule 2 decides it, so CONTESTED on subject grounds should become rare.

## Addendum 7: named question R4-Q5 (appended 2026-09-21)

Owner direction `r2_r4q5` (OWNER_DIRECTION.md, SHA-256 `fb0fbf2f…1a83b`) adds a fifth named
R4 question, proposed after PKG-03:

- **R4-Q5:** are Codex event payloads stored as received (amended CONTRACT K-EVENT-1/K-EVENT-6,
  SPEC §11) or translated (unamended K-ENGINE-4, SPEC §10.3)?
- CONVENTIONS §2.4 and §10 now list it. The validator accepts `R4-Q5`, including for
  AUTHORITY_CONFLICT (MR-11), and a test covers it.
- Ledgers sealed before this addendum keep plain `R4` on such rows (PKG-03 has 15; R0 and PKG-06
  also have some); R3 maps them to R4-Q5 when it clusters. Nobody edits a sealed ledger for this.

## Addendum 8: HELP_HUMAN reading of Addendum 6 rule 3 (appended 2026-09-21)

This is a HELP_HUMAN (A0) clarification, not an owner direction; the owner may reverse it at any time.
PKG-07's DEL-07-02 double-blind split on R4-Q1 (worker A 0 rows, worker B 22) because rule 3 did not
say how to treat a claim met partly by `LEGACY_ONLY` code and partly by `TEST_ONLY` code
(`scaffold.ts`).

- **Reading.** Cite R4-Q1 only when `LEGACY_ONLY` code is the only code meeting the claim on the
  product path. `TEST_ONLY` code does not meet a product claim, so a claim met by legacy code and
  otherwise only by test code cites R4-Q1.
- **Distribution.** Sent to the PKG-09, PKG-01 and EXT managers for workers not yet sealed. R3 applies
  it to every sealed ledger by script from the REACH tags, together with rule 3.

## Addendum 9: named question R4-Q6 and the owner's recorded answer (appended 2026-09-21)

Owner direction `r2_r4q6_answer` (OWNER_DIRECTION.md, SHA-256 `9ebeaaa1…27430`).

- **R4-Q6.** Do the unamended App DIRECTIVE clauses (§2.8, §2.10, §4.1, §4.2) and CONTRACT
  K-PERM-1/K-PERM-6 still bind the Codex-hosted App, or did D-GOV-43 supersede them? It covers the
  Anthropic API-key UI, the live "Full access" option and the unfiltered `~/.codex` link. Proposed
  by the PKG-01 manager and broadened by HELP_HUMAN to the DIRECTIVE-versus-D-GOV-43 cluster (also
  PKG-02 DEL-02-05 and PKG-04 DEL-04-01/04-05).
- **The owner's answer, recorded ahead of R4.** D-GOV-43 superseded those governance texts, so that
  the Codex-hosted App publishes first. Local-model hosting comes later, and an API-hosted path no
  sooner than after that.
- **Status.** This is an owner direction in session, not yet a register ruling. Per the authority
  map (§5) and CONVENTIONS §1, R2 dispositions are unchanged: AUTHORITY_CONFLICT rows stay as sealed
  and cite R4-Q6. The R4 ruling record transcribes this answer as its R4-Q6 clause, with the affected
  row population. R3 builds that packet as **pre-answered**: its purpose is to confirm the row
  population and the repair direction (deliverable and DIRECTIVE text change, code stands), not to
  re-ask the question.
- **Scope of the answer as HELP_HUMAN reads it.** It resolves authority and sequence only. It does not
  itself rule on the separate live-path findings (event redaction, protected paths, human gate),
  which stay with their own clusters and R4-Q1/Q3/Q5.
- CONVENTIONS §2.4 and §10 list R4-Q6. The validator accepts it, including for AUTHORITY_CONFLICT,
  and a test covers it. Sealed ledgers keep plain `R4`; R3 maps them.

## Addendum 10: absence is not evidence of absence; owner check before conclusions (appended 2026-09-21)

Owner direction `r2_absence_not_evidence` (OWNER_DIRECTION.md, SHA-256 `344ed714…8fc50`).

- **Owner statement of fact, recorded as CONTEXT.** v3.0.1 was notarized, as v3.0.0 was. It is not
  applied to any row now; the owner will address it when it comes up (R3/R4).
- **Rule (CONVENTIONS §2.6).** A claim about whether an action or event happened outside the code,
  where the only evidence is the absence of a record within the evidence roots, takes `UNKNOWN`
  with `OWNER_CHECK: <question>` in Notes. Positive evidence either way still counts. Code-presence
  findings are unaffected.
- **HELP_HUMAN correction.** HELP_HUMAN's EXT report relayed "15 rows record processes that never
  ran" (including v3.0.1 notarization) as if established. They rest on missing records, and are
  treated as owner-check candidates, not findings.
- **Sealed ledgers** are not edited. R3 identifies every sealed row whose conclusion rests only on
  an absent record of an off-code event. It does so by script (for example `NONE_FOUND` evidence
  on process or event claims, and "never ran / not performed / no record" phrasing), plus the
  managers' OWNER_CHECK candidate lists and the EXT release-doc rows. It re-maps those rows to
  `UNKNOWN` + `OWNER_CHECK`, and records each re-mapping.
- **Owner check before R4 packets.** R3 compiles all OWNER_CHECK questions into one
  `R3/OWNER_CHECK.md` questionnaire, grouped by event. HELP_HUMAN puts it to the owner **before**
  building the R4 packets. The owner's answers are recorded verbatim as owner direction, and the
  affected rows are dispositioned from them. An answer the owner cannot give stays `UNKNOWN`.
- **Distribution.** Relayed to the PKG-09 manager (the only manager running) for workers not yet
  sealed and for its verifiers.

## Addendum 11: PR #840 review repairs (appended 2026-09-21)

HELP_HUMAN (A0) repairs after the fresh-context review of PR #840. None is an owner direction.

- **Re-seal of DEL-04-05 (scanner hygiene).** Row `DEL-04-05#CLM-009.8` quoted a placeholder
  credential URL (`https` + `://user:pw@api.anthropic.com`). The repository secret scanner
  (`frontend/scripts/scan-secret-evidence.mjs`, URL-credential pattern) flags it, so it would turn
  "Harness pre-merge" red on main. HELP_HUMAN rewrote only the scheme separator, to
  `https[:]//user:pw@api.anthropic.com`. No other byte changed, and the row's meaning is unchanged.
  - Sealed SHA-256 `06247159ecc67149aa1295cb42d2263a68486ee1569d498dd06d2979abace20d` →
    re-sealed `277a6777a1867def62fae5c1fbe6e2f3f8692566f7794fa06fa11e441ced39d4`.
  - The ledger, all 7 reverse-area checks and the errata re-validate PASS 0/0.
  - PKG-04's `PACKAGE_SUMMARY.md`, `VERIFICATION.md`, `STATE.jsonl` and reverse notes keep the
    original SHA as historical record. R3 treats this addendum as the mapping.
- **Labels.** Two addenda contain HELP_HUMAN design alongside owner direction:
  - Addendum 9: "pre-answered", and the proposed repair direction ("deliverable and DIRECTIVE
    text change, code stands"). The owner's recorded words establish only that D-GOV-43
    superseded those texts, and the sequence Codex-hosted first, local models later, API no
    sooner. The R4-Q6 packet will put the owner's recorded answer to the owner for confirmation,
    together with HELP_HUMAN's proposed row population and repair direction, which the owner may
    change.
  - Addendum 10: the `UNKNOWN` + `OWNER_CHECK` mechanism and the R3 questionnaire. The owner's
    words establish the principle, and the requirement to check with the owner first.
- **Cross-reference and test.** CONVENTIONS §2.4 rule 3 now points to the Addendum 8 reading. The
  validator test for MR-11 (AUTHORITY_CONFLICT needs R4 or R4-Qn) now covers R4-Q4, R4-Q5 and R4-Q6.
- **Merge inputs.** `R2/EXT/SOW_A` and `SOW_B` (and the split halves in PKG-01, 02 and 09) are
  merge inputs, not ledgers of record. They fail coverage when validated alone, by design; each
  merged ledger passes.
- **WORK_GRAPH.json** is restored to its original formatting, with "5 double-blinds".

## Addendum 12: authority-map flags corrected by R3 (appended 2026-09-21)

The EXT audit (item 3) found, and R3 (`R3/RUNWIDE_CALLS.md`, call g) recorded, that RULED rows
D-APP-104, D-APP-107, D-APP-122 and D-APP-123 did land at the frozen basis. §5 above flagged them
as pending, held or unapplied. §5 is not rewritten (append-only). For R4 and later stages, read those
four rows as GOVERNING and landed. D-APP-121, D-APP-125 and D-APP-126 stay as flagged unless R3
evidence says otherwise.

## Addendum 13: owner-check answers (appended 2026-09-22)

Owner direction `r3_owner_check_answers` (OWNER_DIRECTION.md, SHA-256 `d1578523…50f2a`) answers
`R3/OWNER_CHECK.md`. The answers are owner testimony about events the owner saw. Under Addendum 10
they are evidence for the rows they decide. They are not rulings on direction of change.

| Question | Answer | Reading |
|---|---|---|
| OC-01 authorization of 3.0.0 and 3.0.1 candidates | yes | |
| OC-02 v3.0.1 DMG built with `desktop:dist` and Developer ID signed | yes | The owner did not say where a build record is kept; its location stays open |
| OC-03 v3.0.1 notarized and stapled | yes | Confirms the Addendum 10 statement |
| OC-04 v3.0.1 published | yes | Location of a record stays open |
| OC-05 K-VALIDATE-1 local set incl. `desktop:dist` passed before release | yes | |
| OC-06 Section 8 premerge run against the Codex-hosted Runtime | yes | |
| OC-07 premerge with full 16-ID Section 9 manifest, summary kept | yes | |
| OC-08 attestation / SBOM | don't know | The owner does not recognise the terms. Rows stay UNKNOWN; R4 may explain the terms |
| OC-09 build for any target other than macOS arm64 | no | Owner testimony that no other target was built |
| OC-10 arm64 architecture inspected | yes | |
| OC-11 `LSMinimumSystemVersion` inspected | yes | |
| OC-12 packaged App run with bundled `codex app-server`, secret and network checks taken | yes | |
| OC-13..OC-20 | don't know | Rows stay UNKNOWN. The owner's belief that steps the instructions called for were likely done (the process was lengthy) is noted on each row as `OWNER_BELIEF`. It does not change a Disposition |

Application: a TASK applies these answers to `R3/CLAIM_CONCORDANCE.csv` and
`R3/EXTENSION_CONCORDANCE.csv` through `R3/REMAP_LOG.csv` (Source `OWNER_CHECK`), row by row.
- **"Rows decided":** the Disposition is set from the answer and the claim text.
- **"Rows noted":** notes that asserted absence are corrected.
- **Output:** every change is listed in `R3/OWNER_CHECK_APPLIED.md`.

A "yes" confirms that an event happened. It does not by itself establish that the deliverable text
is accurate. That judgement is still made against the claim.

## Addendum 14: R4 complete; R5 opens with packet rulings (appended 2026-09-22)

Owner direction `r4_gate_acceptance` (OWNER_DIRECTION.md, SHA-256 `e53bd5b3…5fe25`), recorded as
D-APP-130. The owner accepts the R4 decision book (SHA-256 `3daab45c…`) and packets at main
`1b63e075c` as the R5 basis. R4 is complete. R5 step 1 is the owner's packet rulings, which are
transcribed into their own ruling record and merged before any repair. Nothing is repaired under
D-APP-130.

## Addendum 15: claim granularity captured as D-GOV-44; the run keeps its pinned method (appended 2026-09-22)

Owner directions `r5_granularity_question`, `r5_granularity_posture` and `r5_granularity_capture`
(OWNER_DIRECTION.md, SHA-256 `c41a2126…ccd8`, `d894d01d…f70c`, `3df6e687…b6de`). At the opening of
R5 the owner adopted HELP_HUMAN's claim-granularity reading (a statement is a claim when its
invalidation by implementation change would need a decision; interface and verification as companion
tests; reconciliation continues through the lifecycle at claim level) and "(b) as the default repair
posture" (lift the claim and move the mechanism to evidence, rather than rewrite the mechanism to
match the code), and directed that it be captured and merged for other agents before R5 proceeds.

Captured as D-GOV-44: kernel `docs/DELIVERABLE_CONCORDANCE_METHOD.md` Revision 2 (§3.1) and the
`reconciliation` workflow's R3, R4, R5 and contract text (PR A, owner-reviewed and owner-merged).

**This run's method does not change.** The pinned method in §1 (the six files and SHA-256 values in
the D-APP-128 ruling §4, at `00115c719`) stands; kernel §6 keeps later edits from changing the method
of an in-flight run absent a new ruling. The run adopts the posture as an owner rider at the head of
its R5 ruling record (D-APP-131), in PR B, which the owner will call for. Until then: no packet is
ruled, no repair manifest is built, no deliverable is edited. The owner's standing constraint against
instruction changes is superseded by `r5_granularity_capture` for the D-GOV-44 scope only.
