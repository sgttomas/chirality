# Review 01 of PR #1018, transcribed

- **Reviewer:** a fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high) dispatched by HELP_HUMAN. It authored nothing in the PR. Its final report is transcribed from the host subagent transcript (verbatim apart from any disclosed whitespace normalization).
- **Reviewed head:** `6036e8aa329aa85fb08cb0005873f5e730370927` (it also covered `392c582cb`). The repairs listed under Disposition and this file follow that head.
- **SHA-256 of the report text below (UTF-8; the report text between the blank line after "## Report (verbatim)" and the blank line before the final "## Disposition", with no trailing newline):** `fb2f0c33992bbcf452c5ad15bb6e2bfa6c907e92f41028c3a802f43a04c92281`.

## Report (verbatim)

## Review of PR #1018 (sgttomas/chirality). Covers the final head 6036e8aa329aa85fb08cb0005873f5e730370927 and the first head 392c582cb

**Verdict: FAIL.** There is one BLOCKING finding. It is a disclosure repair of one or two sentences. Once it is fixed, I expect PASS WITH NOTES.

### What I checked
- **Remote head.** `git ls-remote` shows head 6036e8aa3. The base is `origin/main` 974bf7da4, which is also the merge-base. There are two commits: 392c582cb and then 6036e8aa3.
- **Containment.** The PR touches exactly the four paths named. `git diff --check 974bf7da4...6036e8aa3` is clean (exit 0).
- **Checks run at 6036e8aa3.** Each ran in a scratch bare clone plus an archive; nothing touched the worktree.
  - `harness.py self-check --repo-root` exited 0, with INFO=14, NOT_APPLICABLE=1, REVIEW=4, WARN=130. These counts are identical to main 974bf7da4, so the PR adds no findings.
  - `validate_pec_loop_receipts.py` returned VALID (exit 0).
- **CI at 6036e8aa3.** harness, pec, Harness pre-merge, Desktop E2E, and Select App/PEC/source coverage all pass. The other jobs were skipped by path selection. None failed or is pending.
- **Postimage hashes.** I recomputed them with `shasum -a 256` on main, and all four match the D-PEC-105 grant table:
  - SPEC f84c067b…d5f617
  - DEL-00-03 SOW 0fed4ecb…2ae843
  - ADRs ad6bab7e…65c49e
  - DEL-00-01 SOW 3757632b…5da647
- **Checklist hashes.** The a3bc80a0…21b1 and 6e99f93c…8cf9 abbreviations match D-PEC-105 proposal L263 and L154.
- **Review types.** They match each `_REVIEW.md`: DEL-00-01 is `SELF_CHECK` by the owner's replacement ruling (L5, L98), and DEL-00-03 is `PEER_REVIEW` (L6, L72). Both deliverables' `_STATUS.md` read CHECKING.
- **Method basis.**
  - 2f825f180 is the last commit to touch `workflows/review/` before 77dbfcb72; it only added frontmatter metadata.
  - `git diff 2f825f180 77dbfcb72^ -- workflows/review` is empty, so the claim of "last edition before the tranche" is correct.
  - The files hash to: WORKFLOW.md f8a8f240…06bc, execution.json d1c668ae…74df, contract.md d3d7eb27…b328, method.md 63c8a395…0daa.
  - The PEC notice hashes to 30aab470…4168, which equals the D-PEC-105 pin.
- **PR #1007.** Confirmed as the D-PEC-105 act (merge e1af32fc4).

### BLOCKING

**B1. The K3 resolution mixes two HELP_HUMAN messages without saying so (K-AUTH-1).**
Locator: D-PEC-107 L22–24 against L35; also the register row at L124, graph L12, L14 and L24, and STATUS L380.
- The Context section quotes only the *last* recommendation. That recommendation has two parts: K3 stays the single tier-0 publication record, prepared when a DEL-08-06 production packet fixes the shape; and a consumer contract becomes a design item for the next scope change.
- The Resolution adds "A PEC Task Management row tracks it, replacing the carried graph node". That element comes from the *earlier* message, which the record never mentions. The record also silently drops that message's other element, the consumer-enablement notices to each project.
- Substance is taken from the last message and the tracking vehicle from the earlier one. That is a plausible reading of "the approach you recommend", but the record does not say where each part came from.
- It matters here because promoting a Task Management row is an owner act. The intake header says so, and so does LOOP_INIT §4 ("Promotion, disposition and external assignment remain actual human acts").
- The C1 intake had also judged K3 already homed: "waiting for a later planned act is not an intake ground", with a recommendation to carry it in the receipt (INTAKE.md L150). The record overrides that judgment without acknowledging it.
- **Repair:** in D-PEC-107, name the earlier message's two elements, say the row comes from it and the notices were dropped (superseded by the consumer-contract design item), and label the combination as HELP_HUMAN's interpretation, noting that it departs from the intake's "already homed" recommendation. Alternatively, confirm the row with the owner.

### NON-BLOCKING

**N1. The freeze section does not say how RV1's consequences behave under the freeze.**
Locator: D-PEC-107 L67 against L50–51; graph L13, L26 and L34.
- L67 says TM1 and RV1 "record" and that "neither changes the frozen product or opens new design".
- But RV1 writes new records in both deliverables. Its findings can call for owner-ruled correction packets (L50). It also ends in an owner re-acceptance that HELP_HUMAN "presents … once the REVIEW has merged" (L51). That is a new owner decision after the freeze.
- Suggested wording: during the freeze, any correction a finding calls for is recorded only and not prepared, and presenting the re-acceptance (ACC) is subject to the owner's freeze hold.
- The graph's "Next work" (L34) still reads "merge this direction PR, then dispatch TM1 and RV1". It should put the offered hold into effect: surface the RV1 hold option when the merge is reported, and dispatch RV1 unless the owner holds it. RV1's Needs column (L25) could carry the same condition.

**N2. The freeze baseline is ambiguous.** Locator: D-PEC-107 L61.
- The freeze point is pinned at 974bf7da4 (PR #1014). The owner's "important decision have been made" plausibly also covers D-PEC-107's own decisions, which come after 974bf7da4.
- Suggested fix: state the baseline as 974bf7da4 plus D-PEC-107, with the TM1 and RV1 records as the only additions after the freeze.

**N3. Recorded-only proposals: the introduction does not match the list.** Locator: D-PEC-107 L56 against L64–66.
- L56 describes HELP_HUMAN's list as three things: a consumer-contract options note, preparing SCA-007, and "what it would not start".
- The bullets add a third proposal: re-review of DEL-04-01 and DEL-03-01. It is accurate that their acceptances lapsed and no re-review is scheduled (POST-SCA005 RECEIPT L82).
- Suggested fix: make the introduction name every proposal listed, and say whether the DEL-02-07/DEL-01-06 pair, whose re-review waits for their production, was part of the list.

**N4. The consumer-contract design item is presented as part of the CAND-02 disposition.** Locator: register L124 ("CAND-02 promoted (… now also carrying the per-project consumer-contract design item)"), STATUS L377 and graph L24.
- "CAND-02 promote" promoted a housekeeping wording candidate (INTAKE L85–118).
- Attaching a design item to that row comes from the K3 recommendation and HELP_HUMAN's choice of where to track it. That is disclosed only in the K3 row of the record (L35).
- Suggested fix: say the attachment is HELP_HUMAN's, or use a separate row. The freeze reduces the impact, since both are now considerations only.

**N5. The `_LATEST.md` write scope is inconsistent.**
- D-PEC-107 L45 authorizes "the reviews `_LATEST.md` pointer where the method requires it". The register row (L124) and graph RV1 row (L25) leave it out.
- The old edition's method requires it: 2f825f180 `method.md` Gate 4 step 6 calls `update_latest_pointer.sh`.
- `execution/_Evaluation/Reviews/_LATEST.md` is one pointer shared by the whole project.
- Suggested fix: align the three records.

**N6. The MEMORY.md grant is missing.** Locator: graph L27.
- M1 plans rows in the DEL-00-01 and DEL-00-03 `MEMORY.md` files. D-PEC-107 grants no MEMORY path.
- `projects/pec/AGENTS.md` ("Deliverable records and loop ownership") requires the governing D-PEC packet to name those paths. Otherwise the graph must record the missing grant and bring it to the owner.
- Suggested fix: add the grant, or record the gap in the graph.

**N7. The method basis is pinned by commit only.** Locator: D-PEC-107 L47.
- Add the four file hashes listed under "Method basis" above. D-PEC-105 proposal L35 is the precedent for pinning file hashes.

### Risks of using the older review edition

The choice of method basis is defensible. D-PEC-105 excludes adopting the revised edition and says the later authorization names the method basis (ruling L46 and L78). The notice itself says "This loop decides its own adoption". The PEC record also documents that the owner has deferred adopting Root notices. Three risks remain:

- **(a) It is out of step with Root SPEC §3.4.**
  - The tranche manifest says it "implements the existing SPEC §3.3/§3.4 … no SPEC or TYPES change". So the old edition departs from Root SPEC text that already existed, not from a new rule.
  - The departure is its deferral rules. Gate 4 of the old `method.md` (L190–191) lets CRITICAL findings be "deferred with rationale" and MAJOR findings be "DEFERRED". SPEC §3.4 allows "no disclosed-deferral carve-outs".
  - RV1 makes no transition, so the conflict is latent for now. The RV1 brief should still say that no CRITICAL or MAJOR finding is recorded as DEFERRED. Any later CHECKING→ISSUED step still faces SPEC §3.4.
- **(b) The old edition is organized around a transition.**
  - Gate 1 asks for a target transition. Snapshots are finalized "after the Gate 5 decision" (method L195).
  - The 2026-08-09 precedent works around this: "no transition attempted; GATE 5 NOT ENTERED" (DEL-00-03 `_REVIEW.md` L1–2 and L71).
  - The brief should say that RV1 follows that pattern.
- **(c) The old edition expects a practitioner for PEER_REVIEW.**
  - It describes PEER_REVIEW as "another practitioner" reviewing, and says "substantive engineering findings originate from human reviewers" (contract L22 and L59).
  - Precedent covers this: the prior DEL-00-03 review was agent-performed, with findings labeled `AGENT_CHECK`.
  - The brief should name the reviewer's identity and independence.

Otherwise the old edition still fits the repository. Its roles are WORKING_ITEMS and TASK, which is the current four-role model. The tools it names all exist on main: `derive_review_checklist.py`, `create_snapshot_folder.sh`, `update_latest_pointer.sh` and `write_status.sh`.

Nothing in the PR prompts about CHECKING and nothing changes lifecycle. D-PEC-107 L47–49, register L124 and graph L38 all confirm this.

### NOTES

- **CAND-01 (b) is transcribed faithfully.** It matches the option text (INTAKE L81–83). Reading the DEL-00-01/00-03 items as "review inputs; correction only by an owner-ruled packet" (L30) is narrower than the intake's "their correction travels with RV1's authorization" (L67). That is the conservative reading and is consistent with D-PEC-105's limits. CAND-02, CAND-03 (a PEC row plus a Root notice at `execution/_Coordination/`, as in earlier PEC notices) and "keep D-PEC-96 row" match the owner's words and the proposed treatments.
- **Freeze reading.** Continuing TM1 is plainly within "put in the record". Continuing RV1, which the owner directed earlier the same day, while offering a hold is a fair reading. "Later owner directions take precedence" applies only to an explicit hold, and the freeze message's "work you're proposing now" refers to the parallel proposals. N1 is the gap in how the hold is put into effect.
- **Custom checklist item CU-001.** The DEL-00-03 prior review used an owner custom item, CU-001 (`_REVIEW.md` L53 and L127). Its text asserts revision-1.4 totals, which are now stale after the rebind to revision 1.6. RV1 should state whether CU-001 carries forward.
- **K3 row wording notes.** The row should carry the PR #994 review 02 wording notes. The prior graph (L167) and INTAKE L150 point them to "the next K3 row touch", but D-PEC-107 and the TM1 node do not mention them.
- **Register row style (L124).**
  - The state "DIRECTED / EFFECTIVE ON MERGE" differs from the precedent for a direction, D-PEC-94's "DIRECTION OF RECORD / EFFECTIVE ON MERGE".
  - The D-PEC-94 row also quotes the owner inline, while D-PEC-107's row only points to the record.
  - Otherwise the row is accurate.
- **Graph (L1–44).** It is well formed and adequate, with a sound CARRIED rule (PEC's disclosed extension of the template's states; POST-SCA005 RECEIPT L65) and no production node. Four points:
  - It leaves out template sections: Deliverable scope, Open deferrals and follow-ups (where N1, N6, CU-001 and the K3 wording notes belong), Completed work, Route through DAG, and Open questions.
  - "READY after DIR" is really PLANNED until DIR merges.
  - The order and the claim that TM1 and RV1 share no file are correct.
  - The D-PEC-88 trace is present.
- **STATUS (L376–388).**
  - "K3 moved to a PEC Task Management row" (L380) is in the present tense, but the row does not exist until TM1.
  - Items resolved by D-PEC-107 still sit under "Current owner gates" (L224).
  - L377 frames the consumer-contract item as CAND-02 scope (see N4). The freeze paragraph added in 6036e8aa3 correctly limits the undertaking to TM1 and RV1.
- **SCA-007.** It is the correct next PEC ID; the only other SCA-007 is Piping's.

### Files
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-107_OWNER_DIRECTION_2026-09-27.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260927-RV1-INTAKE/WORK_GRAPH.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/docs/STATUS.md

All four were read at 6036e8aa3 through `git show`; the worktree is on another branch. The scratch directories `rev1018.*` were deleted. I made no edits and no git writes to the worktree.

## Disposition (HELP_HUMAN)

Verdict **FAIL**, with one blocking finding. Dispositions:

- **B1 (the K3 resolution mixes two HELP_HUMAN messages without saying so): repaired.**
  - The record's Context now names both messages' elements: (i) the Task Management row and (ii) the per-project enablement notices from the earlier message; (iii) the single publication record and (iv) the consumer-contract design item from the last one.
  - The K3 resolution is labelled HELP_HUMAN's interpretation. It takes (iii) as the substance and (i) as the vehicle, and records that (ii) was dropped because (iv) replaced it. It discloses the departure from the intake's "already homed" judgment and carries the PR #994 review 02 wording notes.
- **N1: repaired.** The freeze section now says three things:
  - any correction a RV1 finding calls for is recorded only and not prepared;
  - ACC is presented as an owner option under the freeze;
  - the owner's verbatim confirmation ("Yes I still want you to complete the task management work and the RV1.") settles the hold question.

  The graph's RV1 and ACC rows carry the same.
- **N2: repaired.** The freeze baseline is `974bf7da4` together with `D-PEC-107`'s decisions, and the TM1 and RV1 records are the only additions after it.
- **N3: repaired.** The introduction now lists every proposal and says the DEL-02-07/DEL-01-06 pair was not on the list.
- **N4: repaired.** Attaching the consumer-contract item to the CAND-02 row is stated as HELP_HUMAN's choice in the record, the register row and STATUS.
- **N5: repaired.** The `_LATEST.md` pointer is aligned in the register row and the graph.
- **N6: repaired.** `D-PEC-107` grants no `MEMORY.md` path. The graph and the record say RV1 is recorded in the graph and receipt only, unless the owner grants rows at closeout.
- **N7: repaired.** The method basis now pins its four file hashes.
- **Risks (a)–(c): repaired in the record, and carried into the RV1 brief when it is dispatched.**
  - No CRITICAL or MAJOR finding is recorded as DEFERRED.
  - There is no transition, and Gate 5 is not entered, as on 2026-08-09.
  - The agent reviewer's identity and independence are named.
- **Notes:**
  - CU-001's carry-forward is now stated in the record, and carried into the RV1 brief.
  - The K3 wording notes go on the K3 row.
  - The register state now reads "DIRECTION OF RECORD".
  - The STATUS K3 tense is repaired. The owner-gates header note is left as it is.
  - The missing template sections are left as they are, since the graph is deliberately compact.

The repair head needs a fresh review before merge.
