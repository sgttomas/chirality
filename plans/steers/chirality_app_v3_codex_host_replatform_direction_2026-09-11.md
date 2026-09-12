# Owner direction transcription — Codex host re-platform (2026-09-11)

Status: non-governing transcription (see `plans/steers/README.md`). This
record authorizes nothing by itself. It preserves the owner's verbatim words
from the Chirality v3 Codex-only MVP trial session so the D-GOV-43 proposal
packet can cite them exactly.

Owner: Ryan Tufts. Date: 2026-09-11 (America/Edmonton). Session: HELP_HUMAN
trial session continuing the Stage26/R17 native pass.

## Context supplied before the direction

HELP_HUMAN reported, after the plan/execute/save-as-workflow demonstration
(findings R17-F1 and R17-F2), that the Runtime fences Codex rather than
hosting it, and offered two routes: an in-place seam repair of the daemon, or
a re-platform in which the Electron main process owns a stock
`codex app-server` child over one channel to the renderer, dropping the Next
turn route and most of the daemon and relying on Codex's own persistence for
restart. Four decisions were requested: trust posture, Codex home, binary, and
doctrine amendment.

## Verbatim owner statements

Prompt establishing intent:

> I need your judgment now. I like how this App is taking shape. To use a
> metaphor, there are good ingredients here but the dish isn't quite ready to
> serve, it needs something removed, or maybe something added, or maybe a
> change in how the ingredients are prepared. So to speak. Do you see the
> meta-workflow I'm trying to build into the functionality of this App? This
> is a tool to give the Codex agents to the user for planning work, and using
> and creating workflows that can be used again and iterated over. I'd like
> to get that core functionality working. I need to have the Codex agents in
> their full glory, so to speak. There should not be any limits on tool use
> or the useful features that come baked in to the Codex agents. This
> Chirality App was built with a lot of governance oversight resulting in
> some overly restrictive or naively limited views of how to implement this
> concept. But there are probably better known solutions to the problems we
> face, or clear instructions from OpenAI on how to do it. If you can't find
> a good solution through direct instructions or a clear idea from yourself,
> then you can see the Pi Agent harness or T3 Code for open source examples
> with permissive licenses. Let's talk about this before you set out so we
> can get aligned.

Direction:

> I approve the second re-platform route. You are right to start with the
> governance, and any impacted deliverable's and their scopes of work may
> need to be revised accordingly too. Was the Pi or T3 Code examples
> instructive for you in any way or not necessary because the path is clear?

Addendum:

> Also, the things built to-date are also, hopefully, useful when we get to
> the local LLM server expansion for Chirality App.

Revision-2 direction, relaying an independent reviewing agent's feedback
(reproduced in the packet's `REVIEW_FEEDBACK_R1.md`):

> I had another agent review your proposal and they offer this feedback.
> Let's iterate to get the best proposal. How do you see this matter now? You
> don't have to adopt everything, it's offered as feedback for your
> consideration.

Revision-3 direction, relaying the same reviewer's round-2 feedback
(reproduced in the packet's `REVIEW_FEEDBACK_R2.md`):

> Once more consider the other agent's feedback. Seek any further answers
> from me if needed. Otherwise update your proposal for my direction.

Handoff direction, relaying the reviewer's round-3 refinements (reproduced in
the packet's `REVIEW_FEEDBACK_R3.md`):

> I have some final refinements, then we need to make this guidance durable
> so a third agent can begin implementation in their own session.

Ruling and merge authorization (transcribed into
`docs/governance_harness/_DECISIONS/D-GOV-43_codex_host_replatform.md`):

> I rule D-GOV-43 accepted as revision 3 at commit 3ef2ef524, with the
> post-build minimum-not-ceiling clarification. The three folded choices
> stand.
>
> You may push changes and open a PR and merge once the CI goes green.

Reopening and topology decision (2026-09-12), after the owner relayed the
reviewer's counter-proposal ("Let's not merge this PR just yet. I might
revise it further. We can take advantage of the failed CI to reconsider."),
directed the comparison ("Start the comparison."), added the embedding
context ("the same agents and agent server is intended to be imbedded in
subsequent applications from Chirality, like the SWBPIPE ... and I want to
be able to integrate local models with Codex"), and concluded:

> We are all in agreement this is the path forward. You will be handing
> this off so a third agent can begin implementation.

Recorded in `docs/governance_harness/_DECISIONS/D-GOV-43_supplement_topology_A2.md`.

## Referent

The "second re-platform route" is the re-platform described in the context
above. The D-GOV-43 proposal packet at
`docs/governance_harness/_PROPOSALS/D-GOV-43_2026-09-11_codex_host_replatform/`
framed it as a ruling candidate; the owner ruled on 2026-09-11 as quoted above.
