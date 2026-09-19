# Sealed correction 1 to brief DESIGN-SYSTEM-05: the independent review's two findings

Sealed by ROOT (HELP_HUMAN, Agent 0) on 2026-09-19T02:04Z and sent to the owning child by the host's message-to-agent mechanism. It is part of the child's brief and binds as the brief does: you work alone, you do not delegate, you run no state-changing git command, and your write scope is the brief's. Path placeholders as in the brief.

## What the reviewer returned

Read the retained return first: `{RUN}/lanes/DESIGN-SYSTEM-05/reviews/DS5-REVIEW_RETURN.md` (SHA-256 `f1744ee7c784232aa80f4ec2143832f41e9e88b3997189c616743c456ce8fc70`). The reviewer was Claude Opus 5, read-only, in a fresh context, on candidate `9b0e12b0db45653d1430fe21a1da2b6230649ae8`. Verdict: FINDINGS, one minor that is actionable before merge and one trivial. Every figure it recomputed agrees with the document, the token diff is the three changes and no more, and both tools run clean. Both findings are about what the document says, not about what it measures.

## Finding 1 (minor): what a disabled cell sits on

§5.1's cell-state table gives the Disabled state as "`text.disabled`; never used in the layout table" and names no fill, where its sibling states name theirs. §1.3 gives `disabled.fill` to a control that has a fill and the bare ink to a control with no fill of its own, and its list of those names neither a cell nor a row. The specimen draws the state two ways: `.rowdemo .dis` (near line 796) on `disabled.fill`, and row A-05 of the Candidate sizes table (near line 1282) in `text.disabled` inline with no fill. The disabled sampler in `tools/render.mjs` selects neither, so the render check's "0 under the stated ratio" does not cover the cell state. On a selected row the bare ink would read 2.60:1 and 2.55:1, and on a proposed row 2.67:1 and 2.87:1: under the stated dark ratio.

Correct it so that the document, the specimen and the render check say one thing.

1. Decide by the design's own logic what a disabled cell, and a disabled row, sits on, and state it in §5.1's Disabled row in one clause, as the sibling states do. The reviewer names two candidates: on `disabled.fill`, which is what §1.3 and `.rowdemo .dis` already say; or the ink on the row surface, with a stated rule that such a row takes neither band. If a third form is better, say why. Whichever you choose, the stated ratio (2.5:1 or better in light, 3:1 or better in dark, on everything the ink is drawn on) must hold on every background your statement allows, by the tool's own measurement. If you choose the second, state whether such a row can be selected or can carry a proposal, because those are the two backgrounds on which the bare ink falls short. If the design needs a disabled row to stay selectable, for example so that a user can read why it is disabled, the second form cannot hold and the choice is made.
2. Make §1.3 agree. Either its list of controls with no fill of their own is stated as closed, or it gains the cell. The reviewer's answer to ROOT's question (that neither `selection.band` nor `canvas.bg` belongs in §2.9's disabled pairs) rests on reading that list as closed; the document should say so itself.
3. Make the specimen agree in both places, and extend the disabled sampler in `tools/render.mjs` so that the render check's count covers the cell state. Re-run the render check. Retain `report.json` and, at 1440 px in light and dark, the screenshot of each specimen section whose pixels change, in place of those retained now. Write every other rendering to a temporary directory outside the repository, so that nothing uncommitted is left in the worktree.
4. If §2.9's pair list changes as a consequence, it changes through `tools/contrast.mjs` and `tools/splice.mjs`, never by hand.

## Finding 2 (trivial): the scope of the wash pairs

§2.9's findings prose and the §5 control rule say "against everything it sits on … at rest and under the hover and pressed washes", and the pair list carries the washes over `surface.panel`, `surface.sunken` and `surface.raised` only. `border.control` under a pressed wash over `surface.base` measures 2.99:1 in light. The reviewer found no control that reaches it. Add the one clause that says so: the wash pairs are those of a control's own fill, and which fills those are. Decide from what §1.3 and §5 already require whether the clause is a statement of scope or a rule (a control that carries the boundary has a fill of its own and never washes `surface.base` directly). If it is a rule and `tools/agree.mjs` or the render check can fail on its breach cheaply, make it so; if that is not cheap, say so and leave it as prose.

## Limits

- `tokens.json` does not change (SHA-256 `0e01828c4e7739313a47b5f71ac3c9fa3cf21aae3d07648eadc805fd82d18c00`). If you find that it must, stop and return the reason before changing it: the product slice that adopts 1.3 is drafted against that hash.
- Change-log rows 1 to 120 stay byte-identical. Your corrections are new rows from 121. The revision stays V1.4, because it has not merged.
- §7 and every ruling of the owner stay untouched, as before. §8 item 6 keeps its statement of what is settled and what is open.
- Both tools run clean: `node tools/contrast.mjs tokens.json <a new file in a temporary directory outside the repository>` and `node tools/agree.mjs DESIGN_SYSTEM_V1.md tokens.json specimen.html`.
- ROOT commits. The branch has moved since your return: it now carries a merge of `origin/main` and ROOT's records. Nothing under the design system's folder changed in that merge.

## Return

Your final message: what you decided for finding 1 and why, in the design's terms; what you decided for finding 2; each file you changed with its SHA-256; the two tools' output; the render check's counts (control readings, disabled samples with the new cell samples counted apart, readings under each stated ratio, blocked requests, console issues); what you did not check; and the model you are. ROOT retains it at `{RUN}/lanes/DESIGN-SYSTEM-05/returns/DESIGN-SYSTEM-05_CORRECTION_1_RETURN.md`, and the same reviewer backchecks the corrected candidate.

Standard claim fence applies (F-PIP-2; claims taxonomy per DEC-081).
