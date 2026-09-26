# Brief B6 — SCA-006 checkpoint-3 preparation (WORKING_ITEMS, scope-change workflow, pinned edition)

Parent: HELP_HUMAN, undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node R3. Role: WORKING_ITEMS (Type 1). Model steer: `claude-opus-5-5`, high reasoning, for you and your children.

## Authority

The owner accepted SCA-006 checkpoint group 2 on 2026-09-25 with "SCA-006 CP2: accept; Q1 a; Q2 a". The record is `projects/pec/execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-2_2026-09-25/`, which holds `DECISION.md`, `ACCEPTED_MANIFEST.csv` and `Handoff_State.md`. Register row `D-PEC-97` makes that snapshot the D-PEC packet that opens PEC's write fence for Lane A.

On 2026-09-26 the owner added:
> Why am I seeing `remaining-items` appearing?  There must not be any of those going forward, so no need to scan for them.

> revision 4: drop remaining-items and remaining-loop; yes, ride checkpoint 3.  SCA-006 pinned.

These are recorded as group-2 amendment 1 in `checkpoint_snapshots/SCA-006_GROUP-2_AMENDMENT-1_2026-09-26/DECISION.md`. It sets two things:
- checkpoint 3 runs on the **pinned** scope-change edition;
- the `projects/pec/AGENTS.md` Remaining-sections correction rides the A4 instruction tranche.

**Stage: checkpoint-3 preparation.** Execute the accepted writes, validate and audit them, complete the SCA snapshot, and produce the audited poststate package for the owner's checkpoint-3 acceptance. Then stop.

## Method (pinned edition)

Use `Workflow: chirality-root:bundled:workflow:scope-change` **at the pinned edition**. Read these files from Git history (for example `git show 4d5f7b911:<path>`), not from the working tree, and record their SHA-256:
- `workflows/scope-change/WORKFLOW.md` `58f5d1d53c655fdc5668d928f6087003590f40e321e25e3d9447805ee64a7a90`;
- `resources/contract.md` `4453a719f1588c4eba08bdb4a979140ff3541ed5a29f04477ea58a844f344d02`;
- `resources/method.md` `34187e83856853f655389625e3465e3c2cb9ff8ad38be1f4d138ee7470d167f5`.

Follow the method's checkpoint-3 preparation.

Your specification is the accepted `SCA-006_2026-09-25_1912/Propagation_Plan.md` together with `Amendment_Preview.md`, `PRD_V2_4_SUCCESSOR_DIFF.md` and `AGENTS_MD_CANDIDATE_DIFF.md`, at the group-2 manifest hashes. The group-2 `DECISION.md` and amendment 1 bound them, and govern wherever they differ. Do not enlarge them.

The post-change audit uses the **current** `audit-decomp` workflow. It is a separate workflow, and its Root wave-2A revision adds `EXPECTED_CONSEQUENCE`. Use that classification for:
- the COV-068/069/072/073 findings that `D-PEC-95` resolved;
- the expected Lane B consequences: B1's absent folders, B3's two quotes, and B7's revision-1.5 pins.

The mixed editions were disclosed to the owner before the pinned choice.

## Preconditions

Stop before any write if any of these fails. A mismatch returns the work to checkpoint 2 with drift evidence.

- Everything in `Propagation_Plan.md` §"Checkpoint-3 preconditions". That includes the live preimages: `projects/pec/AGENTS.md` `c9d3b44d…197a`, `docs/PRD.md` `fff27a66…dfc32`, `SOFTWARE_DECOMP.md` `dc2b8479…9660`, the four registers, both `_LATEST.md` files and the three A2 context preimages.
- Fetched `origin/main` contains the group-2 record, `D-PEC-97`, and group-2 amendment 1 (PR #940), including its §"Verification rule".
- Every artifact in the group-2 `ACCEPTED_MANIFEST.csv` has its listed hash.
- `pec_reliance_hold.py` returns `ALLOW` for every write target, with operation `dispatch-for-production`.

## Execute (Lane A as bounded by D-PEC-97 and amendment 1)

- **A1.** Apply the decomposition candidate with its two pre-acceptance front-matter lines, the four register postimages, and `docs/PRD.md` from `CP2_CANDIDATE/docs/PRD.md`.
  - The PRD's acceptance-date slots S1–S4 and the group-2 folder token keep their 2026-09-25 values. Those are the act-date values.
  - The decomposition's application-date slots take the actual application date.
  - Record every slot value, and prove each hash under the slot rule.
- **A2.** Apply the three `_CONTEXT.md` mirrors for Seq 30, 31 and 32 exactly as planned.
- **A3.** None. No `_STATUS.md` is written and no lifecycle changes.
- **A4.** Carry out the instruction tranche `PEC-SCA006-OPERATIONAL-RELIANCE-<YYYYMMDD>`, where the date is the application date.
  1. Start from `CP2_CANDIDATE/AGENTS.candidate.md`, which is Q-CP2-1 (a) with I1. Fill its application-date slots per `AGENTS_MD_CANDIDATE_DIFF.md` §9.
  2. **Amendment 1.** Replace exactly the paragraph at candidate L261–270, which begins "PEC's deliverable `_STATUS.md` `## Remaining` sections stay in place as". Change no other line.
     - The replacement states the owner's direction: PEC adds no new `## Remaining` sections or entries, PEC does not read them, and new open scope goes to the work graph and its governing records.
     - It keeps the status quo for the existing sections until any retirement ruling: they stay in place, each item's gate markers still bind that item, and they are updated only under a packet that opens that `_STATUS.md`.
     - It keeps the statement that retiring them, as App and Piping did, is a separate owner-directed undertaking.
     - Keep the change minimal and factual, and do not decide the retirement.
     - Record the hunk, with its before and after text, in a new `SCA-006_2026-09-25_1912/AGENTS_MD_AMENDMENT1_DIFF.md`, together with the resulting `AGENTS.md` postimage hash.
     - The verification rule is amendment 1's §"Verification rule": the applied file equals `49ce993a…` with its application-date slots filled, except this one hunk. **The owner must explicitly approve the exact hunk before your PR merges.**
  3. Write that result over `projects/pec/AGENTS.md`.
  4. Write the tranche manifest `docs/governance_harness/tranche_manifests/PEC-SCA006-OPERATIONAL-RELIANCE-<YYYYMMDD>.yaml` from the draft in `AGENTS_MD_CANDIDATE_DIFF.md` §6.1.
     - Fill its slots, including the verbatim checkpoint-2 act and the group-2 `DECISION.md` path.
     - Add amendment 1 as the only addition: the owner's 2026-09-26 words, verbatim, its snapshot path, and the Remaining-sections correction among the changes.
     - Set `m6_notice.disposition: routed`.
  5. Write the three notices. **HELP_HUMAN delegates the file write to you:** the plan assigns them to HELP_HUMAN, and HELP_HUMAN reviews them before merge. Use the texts drafted in `AGENTS_MD_CANDIDATE_DIFF.md` §6.3, with application-date names, and add one line noting the Remaining-sections correction. The three files are:
     - `execution/_Coordination/NOTICE_<date>_PEC_SCA-006_OPERATIONAL_RELIANCE.md` (Root);
     - `projects/chirality-app-dev/execution/_Coordination/NOTICE_<date>_PEC_SCA-006_OPERATIONAL_RELIANCE.md` (App);
     - `projects/chirality-runtime/execution/_Coordination/NOTICE_<date>_PEC_SCA-006_OPERATIONAL_RELIANCE.md` (Runtime).

     They grant nothing.
  6. Run the plan's checks:
     - `validate_instruction_entrypoints.py`;
     - G4 `validate_instruction_tranche_manifest.py`, in CI mode and in `--added-manifests-only` mode over the PR range;
     - `validate_pec_loop_receipts.py`;
     - `git diff --check`.
- **A5.** Complete the SCA snapshot.
  - Generate `Supersession_Map.csv` with the accumulator command in the plan. Never write it by hand.
  - Copy `Post_Change_Coverage.json` from the audit.
  - Write `RUN_SUMMARY.md`.
  - Update `Decision_Log.md`: set SCA006-CP3 to `PREPARED / AWAITING_OWNER`, with hashes. Update `Handoff_State.md` additively.
  - Keep every checkpoint-1 and checkpoint-2 artifact byte-unchanged.
- **A6.** Do NOT move either `_LATEST.md` pointer. HELP_HUMAN does that after the owner's checkpoint-3 acceptance.

## Validate (Lane C)

- **C1.** Check containment against the Lane A allowlist:
  - the decomposition and its four registers;
  - `docs/PRD.md`;
  - the three `_CONTEXT.md` files;
  - `projects/pec/AGENTS.md`, the manifest and the three notices;
  - the SCA-006 snapshot folder;
  - the `COV_SCA006_POSTCHANGE_*` folder;
  - your returns.

  Every hash must match under the slot rule. For `AGENTS.md`, the expected postimage is the accepted candidate plus the amendment-1 hunk, with slots filled.
- **C2.** Run the strict registers validator. Expect 0 errors and exactly two DRB-008 warnings, for DEL-08-06 and DEL-10-13. Run `analyze_dep_closure.py`. Expect 111 edges and 0 SCCs, unchanged.
- **C3.** Run the plan's exact successor assertions. They include:
  - 100 scope items (74/18/8);
  - 68 deliverables (64/4);
  - 49 PRD requirements, with PEC-K-01, K-02, K-11 and the P1 row byte-identical;
  - envelopes 28/34/2/0;
  - the union rule on 64 rows.
- **C4.** Dispatch a TASK child (`pec-task`, opus) to run `audit-decomp` at its current edition.
  - Settings: SOFTWARE, full scope, expected revision 1.6, candidate SCA-006.
  - Output: a new `projects/pec/execution/_Evaluation/DecompCoverage/COV_SCA006_POSTCHANGE_<YYYY-MM-DD>_<HHMM>/`.
  - Compare against `COV_SCA005_POSTSETUP_2026-09-25_1606`, and classify as described under Method.
  - Then a separate review instance, one that authored nothing, audits the poststate as plan C4.3 states.
- **C5.** Check the snapshot for completeness.

If validation fails, keep the failed state as evidence and report it. Do not repair beyond the accepted plan and amendment.

## Independent verification

Dispatch one fresh read-only verifier (`pec-reviewer`, opus). It confirms:
- the live poststate equals the accepted candidates plus the amendment-1 hunk;
- the amendment-1 hunk is bounded and states the owner's direction faithfully, without deciding the retirement;
- nothing lies outside the plan;
- the C1–C5 results;
- the audit reading is honest, including the `D-PEC-95` attribution;
- the manifest and notices are correct.

Loop until nothing is blocking, and save each verdict.

Guard against forced handbacks: commit your work in progress at each major step, and push the branch early.

## Write boundary

Work in your isolated worktree on branch `claude/pec-sca006-cp3-execution`, cut from fresh `origin/main`.

You may write only:
- the Lane A targets above, except A3 and A6;
- the SCA-006 snapshot folder, including `AGENTS_MD_AMENDMENT1_DIFF.md`;
- the `COV_SCA006_POSTCHANGE_*` folder;
- `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/B6_SCA006_CHECKPOINT3.md` (your return) and `returns/B6_VERIFIER_VERDICT_NN.md`.

Do NOT write:
- either `_LATEST.md`, `checkpoint_snapshots/**`, or the `*_AUTHORIZED.md` pointers;
- any SOW, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` or `Dependencies.csv`;
- `v2/**`, `software-workflow.json` or `_DomainEngines/**` (including `pec.yaml`);
- `loop/**`, `docs/STATUS.md`, `README.md`, `_DECISIONS/**` or the work graph;
- any other Root, sister or foreign path.

## Checkpoint-3 owner question

At the end of `RUN_SUMMARY.md`, put this question: accept the audited poststate. Cite:
- the live decomposition, registers, PRD and `AGENTS.md` hashes;
- **the exact amendment-1 hunk text** (the owner must explicitly approve it before the application PR merges);
- the audit snapshot and its verdict;
- the closure state fields;
- the known Lane B consequences.

On acceptance, HELP_HUMAN moves the pointers (A6). List only the genuinely open choices, each with a recommendation. Do not ask about CHECKING.

## Publication

Commit, ending each message with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. Push and open a PR against `main`, ending the body with `🤖 Generated with [Claude Code](https://claude.com/claude-code)`. **Do not merge.** The owner must explicitly approve the amendment-1 hunk before this PR merges, and HELP_HUMAN obtains that approval. If CI shows "Update the PR base", report it; do not repair it.

## Return

- PR URL and head SHA.
- Written files, with preimage and postimage hashes.
- Slot values.
- The amendment-1 hunk, verbatim.
- C1–C5 results.
- The audit path and verdict.
- The closure state fields.
- The checkpoint-3 question set.
- Verifier verdicts.
- Containment.
- Anything unresolved.
- The delegation record.

## Limits

- No Lane B item, pointer move or lifecycle change.
- No retirement of any Remaining section.
- No `v2/**` or tier-0 write.
- No CHECKING, ISSUED or acceptance. Do not ask the owner about CHECKING.
