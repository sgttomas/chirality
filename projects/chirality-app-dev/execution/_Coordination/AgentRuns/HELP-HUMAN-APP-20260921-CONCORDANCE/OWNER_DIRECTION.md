# Owner direction — App whole-corpus concordance (pre-activation)

Recorded 2026-09-21 from this HELP_HUMAN (Agent 0) session. Quotations below are
owner words transcribed from the session; SHA-256 is over each quoted text in
UTF-8 without a trailing newline. Individual message timestamps are not invented.
This record transcribes direction; it is not a ruling and activates nothing.
Activation is the separate D-APP-128 register decision.

## request

> This project has a particular perspective on agents, and has many custom workflows pre-defined in the repo.  I'm interested in the ones for auditing the differences between the codebase and the deliverables, and then reconciling the deliverables to what's in the codebase.  See what you can find in that regard.

SHA-256: `df7307a923f004f07d597f998bbac355206ffbe96a776be3dfcd6b8d29e899c5`

## role

> You will be in the role of `HELP_HUMAN` for this run, in Agent 0 mode, so from that perspective how do you see this workflow being deployed within this actual repo?  This is pre-R0.

SHA-256: `32cf387c4a4d8460fe990bed4fefb33617274a2ed5c4328530f36088c4608a8f`

## frictions

> Let's focus on one project at a time, starting with `chirality-app-dev`.  The frictions:
>
> 1. You are right and I claimed too much.  You should run the workflow as it is written and I will provide rulings on discrepancies and which way to resolve them, at R4.
> 2. If you cannot have subagents spawn their own subagents in this harness, then you must directly manage the work yourself.  But preference is the Agent 0/1/2 mode with a `WORKING_ITEMS` manager in between you and the work.
>
>
> Don't start on the reconciliation yet.  Just assess the matter now that I've provided my answers.

SHA-256: `ca9cf2f00ac4eac9ed49700be28acdea02bf9bdd19ca5dac5bf6e008ef0a320b`

## topology_scope_source

> use exclusively `opus-5` models on `high` reasoning level for all Type 1 and Type 2 agent instances.  Break the workers up by package, with one manager for each package, and also running in phases to limit max concurrency to 16 total agents (including yourself).  Depending on how the session usage limits are being consumed I may adjust the max concurrency later in the run.
>
> Yes, reconcile the entirety of the deliverables, not just a subset.  Use the state as the current `main` which I just pulled and should actually have a minor version bump for some fixes I pushed `v3.0.1` .  Crucially I don't recall what the method revisions were from back in July, so let's discuss those further now.

SHA-256: `010934b35a29227fc54f790c3f6c72ccaf4363d8b6078ca30eb9c8a2f0d40895`

## conventions

> * all eleven enter R0 as candidate conventions.
> * I accept the MR-6 split.  And can we revise the instructions to allow that kind of activity so that it isn't exceptional?
> * What's the agent definition file?
>
>
> Explain to me more about how you see the MR-2 convention playing out.

SHA-256: `37829c8e3e973db6daffd57440d96f26bdf5f95a7d51d54be440bcc71147907b`

## concept

> Okay don't worry about adding instructions.  We got it worked out this time and that's sufficient.  Making such changes is not warranted.  I will preset your agent setting to `opus-5` on `high` before we initiate this work.  It's sufficient for your role and it will mean you can just spawn like-agents and this issue of not being able to select the reasoning level is a non-issue.
>
> Regarding MR-2, it isn't just about Remaining Items, but did the implementation match the scope of work?  I didn't pay the scope of work any regard once I set out to publish the app.  It was a hard push through reading the code and making judgments about what fit and what was appropriate without reference to the deliverables folders.  A dependency graph of the work alone was what guided, along with my declaration of what "done" looked like.  Now I want to reconcile what transpired with the deliverables as-is and determine what needs to change in the deliverables, and if anything needs to change in the codebase.  Let's unpack this, because it's a different concept from what you're describing (though not a different type of activity).

SHA-256: `00675d9c3f70cd48dc1047dcec646488ff3a04d1e568410946e5da5fb8c3c9a3`

## done_and_four_way

> * I don't know if it's recorded in any one spot.  It took shape across sessions.
> * Yes, that four-way picture is what I had in mind.  Yes, it's a lot more than previous.  And harder.  And worth doing.
>
>
> Plan out the execution of this work accordingly.

SHA-256: `8804d47a64a3753ec13b5796037344d5357bbbde848b1f2216a5a3f4fa2b94fd`

## plan_amendment_step0

> Your plan is good, but add one step right at the start which is before you set off write a prompt that I can send to another agent in a different session to get them oriented to this task as we've refined it.  They will be undertaking the reconciliation of `chirality/projects/chirality-piping/` so some things are different in that repo.  Let that agent discover the particulars, I just need you to give orientation guidance to get that session started.  Make that your first action, for you Agent 0 to carry out, before initiating the rest of your plan as-is.

SHA-256: `1655aed0a99f348fba2b6b2fcc2e35e4623c187f38f36f31350e9d719ce7aba4`

## ruling_d_app_128

> First pull origin/main into this worktree and use that as your baseline.  I accept the changes you identified since the v3.0.1 release.  Then D-APP-128: Option A; §6 as recommended.

SHA-256: `ee3c2f6c5af71780e2ae8cbdbcef2c683b3ee06bf32dd315a4716b6c0f6815fc`

## r0_gate_scope_question

> Before I rule, are any other surfaces good candidates for inclusion at this R0 gate?

SHA-256: `7fae0c784badbddaa7881b0025e69a25d84297082e762d4854e63c729813d217`

## r0_gate_governance_workflow

> Items 1-2 can be addressed through a governance audit workflow, I believe?

SHA-256: `783db874fc7c8209be8b32c311ff64749887a61b934e6b83c44828b55df886d1`

## ruling_r0_gate

> Add items 3-7 in the manner you indicated.  R0 gate: A as recommended; B option 2; C as recommended

SHA-256: `0f41325e1a73a617efab38aa9d017350cda5913b6947826d4aff00db3ae9fea0`

## ruling_r0_gate_governance_items

> Neither

SHA-256: `9957d09c21ebc6cad181d56bc43cbd9bde18999c98bd708a416c29fcd3705b7f`

Context for `ruling_r0_gate_governance_items`: the owner's selection in a structured question from HELP_HUMAN, "Which governance items join the scope extension alongside items 3-7?", with the options "1a and 1b+2 (Recommended)", "1a only" and "Neither".

## r2_rerun_rule

> Yes, apply that from wave 2 and give the instructions to the current workers too.

SHA-256: `1d76a2731c7288920e91e984b1ad1e3b6dc08cfbc50d7baa33660bb77480225f`

Context for `r2_rerun_rule`: the owner's answer to HELP_HUMAN's wave 1 status proposal (2026-09-21 ~19:50Z) to keep the >10% fresh-worker rerun threshold for verdict errors only, and to record verifier refutations of other fields as corrections, not reruns, with every refuted row still reported for R3. Applied as RUN_BASIS Addendum 3.

## r2_tiebreak_q4

> Yes, write the tie-break wording and add R4-Q4

SHA-256: `264bea63de073570aa8b9c51b836016dbc6d28be0c0a086260e271aafe46a3bd`

Context for `r2_tiebreak_q4`: the owner's answer to HELP_HUMAN's report on PKG-06 and PKG-08 (2026-09-21 ~20:05Z). It asks for (1) draft wording of a STALE_SPECIFICATION / REMAINING_STATE_MISMATCH tie-break rule, to be approved by the owner before adoption, and (2) adds the PKG-08 candidate question as named question R4-Q4 (applied as RUN_BASIS Addendum 4).

## r2_tiebreak_adopt

> Approved, adopt it and launch PKG-05.  Allow both claims to stand for those 2 instances outside the rule and I'll make a determination later when I can pay closer attention to the surrounding context.

SHA-256: `97b37a0e13a635793a63bb551d330177796eff7261ce73fce9a18f435d56a370`

Context for `r2_tiebreak_adopt`: approves the tie-break wording HELP_HUMAN drafted under `r2_tiebreak_q4` (applied as RUN_BASIS Addendum 5 and CONVENTIONS §2.6). "Those 2 instances" are the DEL-06-02 double-blind keys where the workers split between IMPLEMENTED_DIFFERENTLY and STALE_SPECIFICATION (CLM-005, CLM-032).

## r2_r4q1_subject_test

> Approved, adopt it and send it to the running managers

SHA-256: `75a027b0140020bb7a6a8c8339b1e9c63c5bb33c625dcb6ec833ff6e959978a0`

Context for `r2_r4q1_subject_test`: approves, as drafted, the legacy-versus-live subject test for R4-Q1 that HELP_HUMAN wrote at the owner's request ("Yes, draft the R4-Q1 subject test."), after PKG-04's DEL-04-03 attempts disagreed on R4-Q1 rows (20, 4, 1). Applied as RUN_BASIS Addendum 6 and CONVENTIONS §2.4.

## r2_r4q5

> Yes, add R4-Q5 and send it to the running managers

SHA-256: `fb0fbf2fe681c9820cf76a594289121acde36ea501a42afac5d4ae215461a83b`

Context for `r2_r4q5`: approves HELP_HUMAN's recommendation, after PKG-03 returned, to add named question R4-Q5 on the Codex event-payload conflict (15 AUTHORITY_CONFLICT rows in PKG-03; also seen in R0 and PKG-06). Applied as RUN_BASIS Addendum 7.

## r2_r4q6_answer

> D-GOV-43 superseded the governance files for the very purpose of publishing this Codex-hosted App first, and in the future local-model hosting, and API after that or no sooner at least.

SHA-256: `9ebeaaa187e2a15851b454fb217838d09cf1e97d2f5a54a6bcc8923897127430`

Context for `r2_r4q6_answer`: the owner's reply to HELP_HUMAN's proposed R4-Q6 (whether the unamended App DIRECTIVE §2.8, §2.10, §4.1, §4.2 and K-PERM-1/6 still bind the Codex-hosted App, or D-GOV-43 superseded them). HELP_HUMAN reads it as (1) adding R4-Q6 and (2) the owner's answer to it: superseded. The owner also gave a sequence: the Codex-hosted App first, local-model hosting later, and an API-hosted path no sooner than after that. This transcribes direction; it is not a register ruling. Applied as RUN_BASIS Addendum 9.

## r2_absence_not_evidence

> yeah notarization was done for `v3.0.1` as it was for `v3.0.0` , we can address that when it comes up.  But a lack of evidence is not evidence of lack.  Check with me first about what I did and didn't see happen.

SHA-256: `344ed714809e8c59291634bac0196b5a770df60ea52ed265ef2d68d66c38fc50`

Context for `r2_absence_not_evidence`: the owner's reply to HELP_HUMAN's report of the EXT audit. That report relayed EXT findings that release steps including "v3.0.1 notarization" never ran, based on the absence of records within the evidence roots. The owner states that v3.0.1 was notarized, as v3.0.0 was, and directs that absence of a record not be taken as absence of the event: HELP_HUMAN is to check with the owner about what the owner did and did not see happen. Applied as RUN_BASIS Addendum 10.

## r3_owner_check_answers

> 1-7 yes, 8 I don't know what that is, 9 no. 10-12 yes, 13 onwards I'm not sure but if it's in the instructive there's a good chance it was. The process was lengthy.

SHA-256: `d1578523f46ac15c6f31a3147745f137b4290d4518adaf45c1d2d16308c50f2a`

Context for `r3_owner_check_answers`: the owner's answers to the 20 questions of `RUN_D128.../R3/OWNER_CHECK.md` (OC-01..OC-20), as HELP_HUMAN put them in chat on 2026-09-22. HELP_HUMAN's reading, recorded in RUN_BASIS Addendum 13:
- OC-01..OC-07 yes; OC-08 don't know (the owner does not recognise attestation or SBOM); OC-09 no; OC-10..OC-12 yes;
- OC-13..OC-20 don't know. For these the owner adds that "if it's in the instructive there's a good chance it was", which HELP_HUMAN reads as "if the instructions called for it". This is recorded as the owner's belief, not as a yes.

## r4_gate_acceptance

> I accept this as the basis for R5 once rulings are made, but I want that to be the starting task in R5.  So I want to consider that R4 is complete with my acceptance of this decision book, and to merge via PR what you've done.

SHA-256: `e53bd5b32d3d02817ff3096e446bb058900478b7382338692c4c542af635fe25`

Context for `r4_gate_acceptance`: given after PR #841 merged (main `1b63e075c`), which carries the R4 decision book and its 25 packets. HELP_HUMAN's reading, recorded as D-APP-130:
- the owner accepts the decision book as the basis for R5;
- R4 is complete on that acceptance;
- ruling the packets is the first task of R5;
- what has been done is to be merged by PR.

## r5_granularity_question

> I want to start R5 with an assessment of the findings from R4 and the decisions put before me.  It hinges on a question, of to what degree do the deliverables need to describe what's in code?  A 1:1 mapping is too much, clearly.  And 0:1 not enough.  The goldilocks principle here is hard to come by.  But I think it has to do with once the deliverable has been defined sufficiently that it is considered stable, even if all the details haven't been worked out, or even all the dependencies fully resolved, but it's clear how to resolve them and no more are expected to arise, then around that point we would stop reconciling the deliverables to the code?  Or it is appropriate right through to publishing, just being conscious of how to account for the continuing developments (what level of detail).  What's your perspective?

SHA-256: `c41a212612408385c8a45842404828fb3af63deddc959a9a8815d7732f72ccd8`

Context for `r5_granularity_question`: given after PR #843 merged (main `a9da9f971`, D-APP-130), as the owner's opening of R5. HELP_HUMAN answered with a perspective (not a ruling): the kernel already makes the claim the unit; a statement belongs in a deliverable as a claim when changing the implementation so it no longer holds would need a decision (with interface and verification tests alongside); reconciliation continues through publication at that level; the "stable" point the owner describes is the CHECKING entry, where the candidate is frozen, not where reconciliation stops; every "change the text" option has two executions, (a) rewrite the mechanism detail to match the code or (b) lift the claim to requirement level and move the mechanism to evidence; (b) recommended as the default R5 posture.

## r5_granularity_posture

> I agree with what your saying and would also take your recommendation for (b) as the default repair posture.  But instead of proceeding here yet, let's capture this and merge via PR so other agents doing this task can benefit from it too.  I'm not sure where this understanding and insight belongs, but the specific instructions should have a clear home.  What's your perspective on the best way to preserve this and make it available for others?

SHA-256: `d894d01d42d3ee1bd5100b20a205f8a828ad76e926316a22c605a328571df70c`

Context for `r5_granularity_posture`: the owner adopts the claim-granularity reading and (b) as the default repair posture, and asks that it be captured and merged for other agents before R5 proceeds. HELP_HUMAN proposed: the principle in the kernel (`docs/DELIVERABLE_CONCORDANCE_METHOD.md`, Revision 2); the specific instructions in the reconciliation workflow (`workflows/reconciliation/resources/method.md` R4 and R5, through `create-workflow`); this run's adoption as a rider at the head of the R5 ruling record (PR B); notices to the piping and App loops.

## r5_granularity_capture

> Yes PR A now for "The principle" and "The specific instructions".  I'll review, then merge and pause work.  I will instruct when to proceed with PR B.

SHA-256: `3df6e687837def37123e7081e9cd1457b1a51911698f989cc55873f7c762b6de`

Context for `r5_granularity_capture`: authorizes PR A (kernel Revision 2, workflow R4/R5 revision, decision record D-GOV-44, loop notices, run-record capture). This is the owner act that amends the kernel (§7: "amended only by owner act"). It is the first instruction change in this run; the earlier `concept` direction ("Making such changes is not warranted") declined agent-setting instructions for reasoning-level selection and did not address the kernel or the workflow. The owner reviews and merges PR A personally, then pauses; PR B (D-APP-131: the rider and the packet rulings) waits for the owner's instruction. HELP_HUMAN does not merge PR A.

## Plan approval

The owner approved the session execution plan (plan-mode approval act, after the
`plan_amendment_step0` amendment). The approved bytes are preserved beside this
record as `PLAN_OF_RECORD.md` (SHA-256
`c1136b456f82b8fff997902e987e400a3f86af131fbb54c8d99326c669d36f7c`). The plan is
an execution plan for this undertaking, not a governing method; the method is
whatever the D-APP-128 ruling pins.

## Agent application (not owner words)

- Scope indicated: whole corpus, all live App deliverables; source state = current
  `main` (App `frontend/package.json` reads 3.0.1; no `v3.0.1` tag exists, so the
  run pins a commit SHA).
- Topology indicated: HELP_HUMAN → one WORKING_ITEMS manager per package → TASK
  workers; nested harness-native delegation verified on this host 2026-09-21.
  Max 16 concurrent agents including Agent 0; the owner may change the cap.
- Model/effort: the owner preset this session to Opus 5 / high; spawned Type 1 and
  Type 2 agents inherit it. Earlier turns of this session ran as Claude Fable 5.1
  (orientation and planning only; no run work).
- MR-1..MR-11 enter R0 as candidate conventions only. MR-6 split accepted for this
  run: `projects/chirality-runtime/{packages,tests}` may be read as implementation
  and verification evidence; its execution tree is not read; gate status for
  runtime-owned work comes only from App surfaces. No instruction change follows
  from this (owner: "Making such changes is not warranted.").
- Step 0 of the approved plan (piping orientation prompt) was completed in-session
  and delivered to the owner as a chat file; it is not committed here and grants
  nothing to any piping session.
