# T1 — Classify plain `R4` rows into named questions (Addenda 4, 7, 9)

Read `_COMMON.md` first. Also read CONVENTIONS §1 (authority handling) and §2.4 (named questions).

**Input.** `<RUN>/R3/_work/CAND_R4PLAIN.csv`: every row (deliverable and EXT) whose current
HumanDecisionNeeded contains the plain token `R4`. Ledgers sealed before Addenda 4, 7 and 9 kept
plain `R4` on rows that turn on a named question; R3 maps them.

**Question texts** (CONVENTIONS §2.4):
- `R4-Q1`: legacy in-process harness versus the live Codex path — whether retained harness code
  is history, compatibility or obligation (K-PATH, K-ROOT, K-HOOK, SPEC §15.2 unamended for
  D-GOV-43).
- `R4-Q2`: the Codex engine never run through the K-ENGINE-2 conformance suite.
- `R4-Q3`: the actor check on the legacy `status_transition` tool, which the agent supplies itself.
- `R4-Q4`: whether the 2026-09-09 v3 four-role adoption (`9b005c23a`; alias map, default role,
  retired agent matrix and Pipeline surface, new agent-file header format) is a governing
  amendment of SPEC §7 and §13 and the persona and matrix contracts, which were not amended.
- `R4-Q5`: Codex event payloads stored as received (amended CONTRACT K-EVENT-1/K-EVENT-6,
  SPEC §11) or translated (unamended K-ENGINE-4, SPEC §10.3)?
- `R4-Q6`: do the unamended App DIRECTIVE clauses (§2.8, §2.10, §4.1, §4.2) and CONTRACT
  K-PERM-1/K-PERM-6 still bind the Codex-hosted App, or did D-GOV-43 supersede them? Covers the
  Anthropic API-key UI, the live "Full access" option and the unfiltered `~/.codex` link, and
  the DIRECTIVE-versus-D-GOV-43 cluster generally (policy rows on shared config, approval policy,
  event pass-through).

**Method.** The evidence is the row itself (NormativeSource, DeclaredState, evidence cells,
Disposition, Notes). Open the frozen tree only when the row text is ambiguous about which clause
is in conflict. For each row decide which named question(s) the row *turns on*: the owner's answer
to that question would settle the row's R4 need. A row may turn on more than one question
(`R4-Q5; R4-Q6`). If it turns on none of them (a different, unframed owner question), keep `R4`
and state that question in one line. Keep any other tokens the cell already has (for example a
`D-APP-11x` or `R4-Q1` token) — you only replace the plain `R4`.

**Output.** `<RUN>/R3/_work/T1_R4QN_VERDICTS.csv`, one row per input row:
`ClaimKey,OldHumanDecisionNeeded,NewHumanDecisionNeeded,Question,Basis`
- `NewHumanDecisionNeeded`: the full new cell (`;`-separated, e.g. `R4-Q1; R4-Q6`), or the old
  value unchanged when it stays plain `R4`.
- `Question`: `R4-Q4|R4-Q5|R4-Q6|R4-Q1|R4-Q2|R4-Q3|MULTI|STAYS_R4`.
- `Basis`: one sentence citing the row text (clause names) that ties it to the question; for
  STAYS_R4, the unframed question in one line.

Also write `<RUN>/R3/_work/T1_NOTES.md` (≤ 60 lines): counts, the STAYS_R4 questions grouped by
theme (these become candidate R4 clusters), and any row you found hard.
