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
