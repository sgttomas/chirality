# Review 01 of HELP_HUMAN's commits on PR #943 (SCA-006 checkpoint-3 application), transcribed

- **Reviewer:** fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high), dispatched by HELP_HUMAN. Its final report is transcribed verbatim from the host subagent transcript.
- **Reviewed head:** `a11a6cb057fc78aaeac4f5aa1a8be3a7eabded76`.
- **SHA-256 of the report text below (UTF-8):** `4452da811e6e5ec3be271c832f719132f7520786f45375dfc1dc1bdb0979ef34`.

## Report (verbatim)

**Verdict: CHANGES REQUIRED. There is 1 blocking finding, in HELP_HUMAN's STATUS commit `c75631e6a`.** Everything else checked is correct: the Lane A bytes, the owner-approved hunk, the manifest, the three notices, merge containment and hygiene.

I confirmed the head with `gh pr view 943`: `a11a6cb057fc78aaeac4f5aa1a8be3a7eabded76`. I read it through `git archive` into a fresh mktemp directory. I ran the validators in a separate `git clone --shared` checked out at the head, with `origin/main` pinned to `53145aaeb`. I did not modify or switch anything in the review worktree. Its `git status` is clean. Its branch now reads `claude/pec-d98-first-sows-proposal`, not the session-start branch; that was not caused by me.

## Blocking

**B1. `projects/pec/docs/STATUS.md:137-141` names a retirement undertaking that does not exist at the head or on `origin/main`, and it contradicts the same file.**
- Text: "The existing sections stay as records until the retirement undertaking `HELP-HUMAN-PEC-20260926-REMAINING-RETIREMENT` concludes".
- `git grep` at `a11a6cb05` and at `origin/main` finds that ID only in this line. It exists only on the unmerged branch `origin/claude/pec-remaining-retirement-account` (commit `be8459f49`, "RS1 COMPLETE", D-PEC-98). No PR is open for that branch.
- At the head, STATUS L257-259 still says "Owner decision pending: whether to open a separate undertaking to retire the 57 `## Remaining` sections … (work-graph node RS1)". The work graph agrees: `WORK_GRAPH.md` L74 and L84 say "Blocked on the owner: RS1".
- It also narrows the approved `AGENTS.md` L266 ("Until any retirement ruling, the existing sections stay in place") into an undertaking's conclusion.
- `projects/pec/AGENTS.md` L300-302 forbids relying on an owner act that is visible only on an unmerged branch.
- **Fix:** change L139-141 to follow `AGENTS.md`. For example: "The existing sections stay in place as records until any retirement ruling; whether to open that undertaking is the owner's pending RS1 decision (What's next)". Alternatively, land the RS1 record on main first, then update L140 and L257-259 together.

Apart from this, amendment 1's required STATUS correction is done: the stale "the sections remain as records" wording is gone.

## Non-blocking

1. **D-PEC-88 trace is not recorded yet.** `WORK_GRAPH.md` L163-177 lists STATUS/README changes only through the "Eighth PR". This PR's changes are not named there, which `AGENTS.md` L306-309 requires. Add them in this PR or the next graph update.
2. **STATUS L240-243 is stale.** It lists `D-PEC-96` under "Open" as "proposed". At the head the register row is `RULED A / EFFECTIVE ON MERGE` (PR #946, brought in by the update-branch merge). This was already stale on main, but it sits in the same list as the changed item.
3. **STATUS L245** still lists "residual `projects/pec/AGENTS.md` corrections" as open. They are applied in this PR (I1 rides R3). It could say "applied; completes with checkpoint-3 acceptance".
4. **Minor staleness in nearby text:**
   - STATUS L212 still says "Current owner gates (2026-09-25; …)".
   - STATUS L232-233 says "The next audit to observe this state is SCA-006's post-change audit". That audit has now run (`COV_SCA006_POSTCHANGE_2026-09-26_0051`).
   - STATUS L227 and README L33-34 say "all 66 contexts … name revision 1.5". Three contexts now also carry the revision 1.6 successor clause.
5. **Notice wording nit.** In all three notices' amendment-1 paragraph (Root L32-33, App L32-33, Runtime L27-28), "until any retirement ruling, which is a separate owner-directed undertaking" makes the ruling the undertaking. `AGENTS.md` says retiring the sections is the undertaking. The meaning is not materially wrong.
6. **Already disclosed:** the three A2 `_CONTEXT.md` lines say "revision 1.6 (`current_basis`…)" before acceptance (COV-079, `RUN_SUMMARY.md` L270). COV-083 and Q-CP3-1 are carried as known.

## What I verified

**1. STATUS and README.** Every changed sentence other than B1 is true at the head:
- PRD v2.4 is applied, byte-equal to `CP2_CANDIDATE/docs/PRD.md`, and its Status row says adopted 2026-09-25 by group 2.
- `D-PEC-97` is recorded; PEC-ORI-007, API-006, API-007 and the §12 gate are present.
- The tranche ID `PEC-SCA006-OPERATIONAL-RELIANCE-20260926` matches the manifest.
- The audit reads `WARNINGS` with 0 BLOCKER / 3 WARNING / 71 INFO / 12 EXPECTED_CONSEQUENCE.
- The run used the pinned edition (`4453a719…`, `34187e83…`).
- "approve hunk" is recorded.
- Acceptance is pending: neither `_LATEST.md` is in the diff, there is no GROUP-3 snapshot, and `SOFTWARE_DECOMP.md` is `candidate_pending_checkpoint_3`.
- The Remaining wording matches `AGENTS.md` L261-272, apart from B1.
- No acceptance, CHECKING or ISSUED claim appears anywhere.

**2. The owner-approved hunk.**
- The return's quoted block (`B6_SCA006_CHECKPOINT3.md` L103-114) equals applied `AGENTS.md` L261-272 byte for byte. So does `AGENTS_MD_AMENDMENT1_DIFF.md` §3 (L90-101).
- `shasum -a 256 projects/pec/AGENTS.md` gives `4400c4e97d5c9dfeda7a9a764b204ed14784c687e55e81bb04875323b6c7139c`.
- Diffing against candidate `49ce993a…` (hash recomputed) shows only the L6 `amended:` slot and the one hunk (candidate L261, L263-270 → applied L261-266, L268-272; L262 kept as L267).
- The approval is recorded in `Decision_Log.md` row SCA006-G2-A1 (L29) with the verbatim section at L137-153, and in the manifest at `group2_amendment_1.owner_hunk_approval` (L133-145).

**3. The three notices.**
- I extracted the §6.3 drafts; all four draft hashes match (manifest `852b1d5b…`, root `43cfa318…`, app `eb927e1f…`, runtime `385e5e2f…`).
- Each notice differs from its draft only by the named amendment-1 block and the manifest-path date slot (`20260925` → `20260926`).
- The manifest differs from its draft only by the §9 slots (ID, date, basis `94e9255b6`, which is on main; CP2-ACT verbatim; CP2-VARIANT; notice dates) and the `group2_amendment_1` block.
- Owner quotes are verbatim, with double spaces, against the amendment-1 `DECISION.md`.
- Each notice grants nothing, and each says reliance is not usable until the §12 gate passes.
- The Runtime basis is true: `SOURCE_PINS.json` S4, S5 and S6 are `projects/pec/AGENTS.md`, `Deliverables.csv` and `ScopeLedger.csv`, and DEL-02-06 `ScopeOfWork.md` read item 5 (L459-461) names them. SOW-097..100, DEL-08-06 and DEL-10-13 are present, and PRD §16.6 / OI-006 are cited correctly. The Root notice's reference to Root `AGENTS.md` L54-55 is accurate.

**4. Merge and containment.**
- `a11a6cb05` brings in 14 main-side paths; none intersects the PR's 50 paths.
- The PR path set equals the D-PEC-97 A1/A2/A4/A5/C4 grants, plus `_Coordination` returns, plus STATUS/README.
- The registers, `Companion_Inventory.csv` and `ContextBudgetQA.csv` are byte-equal to the candidates. `SOFTWARE_DECOMP.md` differs only in the pre-acceptance slots.

**5. Hygiene, all run at the head.**
- `git diff --check origin/main...HEAD`: exit 2, all 46 reports are in `Supersession_Map.csv` (the known CRLF), nothing else.
- `validate_pec_loop_receipts.py`: VALID.
- `validate_instruction_entrypoints.py`: PASS.
- G4 in CI mode: PASS (127 manifests). G4 with `--added-manifests-only`: PASS (50 paths, 1 on the instruction surface, 1 manifest). PEC-SCA006 shows only INFO lines.
- `validate_decomposition_registers.py --strict`: 0 errors, 2 DRB-008 (DEL-08-06, DEL-10-13), 26 XRG-013, exit 1 as designed. Nothing prompts about CHECKING.
- Harness self-check: exit 0, with 147 findings identical to main.
- pytest: 33 passed.
- Reliance-hold preflight on `AGENTS.md` for `exact-correction-preparation`: ALLOW.
- GitHub checks: all pass or skipping.

Key paths:
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/docs/STATUS.md (at `a11a6cb05`)
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md (at `a11a6cb05`)

## HELP_HUMAN disposition

The verdict was CHANGES REQUIRED on B1. B1 is resolved by merging `origin/main`, which now carries the RS1 record and the retirement undertaking's graph (PR #944, `2b2c19b9e`). The STATUS sentence now follows `AGENTS.md`: the sections stay in place until any retirement ruling, and the undertaking was opened on 2026-09-26. The merge also resolved a STATUS conflict in favour of both sides.

The non-blocking findings are handled as follows:
- **1:** the D-PEC-88 trace is added to the graph.
- **2 and 4:** the stale STATUS lines are updated. The `D-PEC-96` act merged as PR #950, the owner-gates date is corrected, the SCA-006 audit is named, and the three contexts' revision-1.6 clause is noted in STATUS and README.
- **3:** the AGENTS corrections are marked as applied.
- **5:** notice wording, left as is. The meaning is not materially wrong, and the notices' bytes were reviewed against their drafts.
- **6:** already disclosed.
