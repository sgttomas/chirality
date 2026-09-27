# Brief RV1A — RV1: REVIEW of the D-PEC-105 bytes for DEL-00-01 and DEL-00-03 (WORKING_ITEMS dispatching REVIEW)

- **Parent:** HELP_HUMAN.
- **Undertaking:** `HELP-HUMAN-PEC-20260927-RV1-INTAKE`, node RV1.
- **Role:** WORKING_ITEMS (Type 1). You dispatch the REVIEW work to fresh Type 2 instances and integrate it. Record the SHA-256 of each method file you load.
- **Model:** `claude-opus-5-5`, high reasoning, for you and every child.
- **Branch:** `claude/pec-rv1-d1-review`, in your own isolated worktree, cut from fresh `origin/main`, which contains PR #1018.

## Authority

The authority is `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-107_OWNER_DIRECTION_2026-09-27.md` §"RV1 authorization", together with the owner's confirmation, verbatim: "Yes I still want you to complete the task management work and the RV1."

It implements `D-PEC-105` RR1: `_DECISIONS/D-PEC-105_d1_premise_amendment_proposal_2026-09-26.md` ("Acceptance-lapse account" and question 3), and `D-PEC-105_RULING_2026-09-27.md`.

## Scope

**What is reviewed.** The current bytes of each deliverable. Verify their hashes first, and stop if any differs:
- DEL-00-03 `artifacts/v2/SPEC.md`, `f84c067bf8388cbd348541dd821af040cee4e84fb34fe4e3e3ab473acdd5f617`;
- DEL-00-03 `ScopeOfWork.md`, `0fed4ecb771ccef8f8575dd08420e13792629cd7ac9d14f720423eba6c2ae843`;
- DEL-00-01 `artifacts/v2/ADRs.md`, `ad6bab7ee00779e0cff5900d74d986e5e05c66b7dc469f5ddd9b224ecc65c49e`;
- DEL-00-01 `ScopeOfWork.md`, `3757632b507d1f5a5668ccefb99d87b9e2a30a9e6bd38d7349e9f4721c5da647`.

**Review type** (as each prior acceptance):
- DEL-00-01: `SELF_CHECK`, the owner's replacement ruling recorded in its `_REVIEW.md`.
- DEL-00-03: `PEER_REVIEW`. The peer reviewer must be a fresh Type 2 instance that authored none of the `D-PEC-105` bytes.

**Method basis.** The bundled `review` workflow as of commit `2f825f180`. Read it with `git show 2f825f180:workflows/review/...`, and record its hashes.
- Do **not** apply the revised edition's CHECKING-entry, frozen-SHA, Gate 5 or reversal rules (`77dbfcb72` onward). PEC has not adopted them.
- If the old edition's process relies on something no longer present, such as a role or path, use the nearest current equivalent and record the substitution.
- Follow the 2026-08-09 precedent: no transition is attempted and Gate 5 is not entered. Snapshot finalization, which the old method ties to Gate 5, follows that precedent's form.
- Record no CRITICAL or MAJOR finding as DEFERRED, because SPEC §3.4 allows no deferral carve-outs even though the old edition would. Any later CHECKING → ISSUED step still faces SPEC §3.4.
- Name the reviewer's identity and independence in the record. The DEL-00-03 PEER_REVIEW is agent-performed, as the prior one was, with findings labelled as agent checks.
- State whether the DEL-00-03 owner custom item CU-001 carries forward. It asserts revision-1.4 totals, now stale after the rebind to revision 1.6.
- Record the `D-PEC-107` §Freeze point limit: any correction a finding calls for is recorded only and not prepared.
- Derive the checklists with `tools/scope_of_work/derive_review_checklist.py`. The `D-PEC-105` proposal expects DEL-00-03 `a3bc80a0…21b1` and DEL-00-01 `6e99f93c…8cf9`. If a checklist differs, record why.

**Inputs.**
- The prior review records: each deliverable's `_REVIEW.md`, `Review_Findings.csv`, and the `_Evaluation/Reviews/REV_DEL-00-0x_*` snapshots, notably `REV_DEL-00-03_2026-08-09_2156` and DEL-00-01's 2026-08-01 SELF_CHECK.
- The `D-PEC-105` act run root `execution/_Coordination/D1_PREMISE_AMEND_2026-09-27/`, including `HANDOFF_STATE.md` items 6–7.
- The `D-PEC-105` proposal's "Other findings" 1–11.
- The DEL-00-01 and DEL-00-03 items of intake `CAND-PEC-2026-09-27-01`, which go with RV1 under `D-PEC-107` CAND-01 (b).

## Do

1. **Run each REVIEW.** For each deliverable:
   - derive its checklist;
   - assess every acceptance criterion against the current bytes;
   - record findings by severity (CRITICAL, MAJOR, MINOR, OBSERVATION) with evidence;
   - write the review records as the method requires: update the deliverable's `_REVIEW.md` so it describes the new bytes, keeping the prior acceptance history as history; update `Review_Findings.csv`; create one new `projects/pec/execution/_Evaluation/Reviews/REV_DEL-00-0x_<YYYY-MM-DD>_<HHMM>/` snapshot; and update `_Evaluation/Reviews/_LATEST.md` if the method and precedent require it.
2. **Record the acceptance status honestly.**
   - The owner's `ACCEPT_EXACT_BYTES` of the new hashes is **not** given yet.
   - DEL-00-01 AC-007 and DEL-00-03 AC-011 stay unsatisfied until the owner's act.
   - The review records must say that the owner act is the next step.
   - Prepare, in your return, the exact text of the owner decision it would need: the hashes, AC-007's two confirmations and AC-011's two, as the prior acts carried them.
3. **Handle findings.**
   - If a finding would require changing a `ScopeOfWork.md` or an artifact, do **not** change it. Record it, and state that an owner-ruled correction packet is needed before re-acceptance.
   - If there are no CRITICAL or MAJOR findings, say so plainly.
4. **Verify.** Have one fresh read-only `pec-reviewer` (opus) verify:
   - that the REVIEW records are faithful to the bytes and the method;
   - that the review types and method basis were applied as authorized;
   - that no lifecycle, CHECKING, ISSUED, SOW or artifact change was made;
   - that nothing prompts about CHECKING.

   Wait for it inside your turn.
5. **Checks.** Strict registers, the harness self-check (`tools/practitioner_harness/harness.py self-check`) and `validate_pec_loop_receipts.py` must give output identical to `origin/main`, and `git diff --check` must be clean.

## Write boundary

You may write only:
- DEL-00-01 and DEL-00-03 `_REVIEW.md` and `Review_Findings.csv`;
- the two new `REV_*` snapshot folders, and `_Evaluation/Reviews/_LATEST.md` if required;
- a run folder `projects/pec/execution/_Coordination/RV1_D1_REVIEW_<date>/` for your manifests, checklists and evidence;
- this brief, copied to `…/AgentRuns/HELP-HUMAN-PEC-20260927-RV1-INTAKE/briefs/RV1A_D1_REVIEW.md`;
- your return, at `…/returns/RV1A_D1_REVIEW.md`.

**No** `_STATUS.md`, `ScopeOfWork.md`, artifact, `MEMORY.md`, register, dependency, context, reference, graph, STATUS, `_DECISIONS/**` or foreign write.

## Publication and rules

- Export `TMPDIR` to your own directory under the session scratchpad `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/`, and set `PYTHONDONTWRITEBYTECODE=1`. Never write to `/tmp` or `/var/folders`. Children follow the same rules and never run `git fetch`.
- Commit and push early.
- Open a PR against `main`, and do not merge it.
- Commit messages end with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. The PR body ends with `🤖 Generated with [Claude Code](https://claude.com/claude-code)`.
- **Return:**
  - the PR URL and head;
  - findings per deliverable, with severities;
  - the checklists and their hashes;
  - the method-basis hashes and any substitutions;
  - the written paths and their hashes;
  - the verdict;
  - the exact owner-acceptance decision text.
- Never prompt about CHECKING. Both deliverables stay `CHECKING`.
