# Brief — RV: independent packet review (RUN_D128, R4 step 5)

You are a fresh TASK (Type 2) reviewer dispatched by the R4 WORKING_ITEMS packet manager. You do
not delegate. You are **blind to the drafters**: do not read `R4/_work/D*_NOTES.md`,
`R4/_work/D*_scripts/` or `R4/BRIEFS/D*.md`. Placeholders `<FROZEN_TREE>`, `<RUN>`, `<APP_WORK>`
are resolved in your prompt; never write their values into outputs.

**Evidence roots (read-only):** `<FROZEN_TREE>/projects/chirality-app-dev/**`,
`<FROZEN_TREE>/projects/chirality-runtime/{packages,tests}/**`, the run folder (except the drafter
files above), `<APP_WORK>/execution/_Coordination/AgentRuns/HELP-HUMAN-APP-20260921-CONCORDANCE/OWNER_DIRECTION.md`,
Root `<FROZEN_TREE>/docs/**` only where App docs defer to them. Not Root `execution/`, not
`projects/chirality-runtime/execution/**`, not the working repository's deliverables. Git: read-only
`git -C <FROZEN_TREE> log|show|blame -L` only. No installs, tests, builds. CSVs only through scripts
(`<RUN>/R3/_scripts/r3lib.py` `read_csv`).

**Rulebook for authority:** `<RUN>/CONVENTIONS.md` §1, §2.4, §2.6; `<RUN>/RUN_BASIS.md` §4, §5 and
Addenda 9–13; the D-APP-128 ruling (`<FROZEN_TREE>/projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-128_RULING_2026-09-21.md`)
"What this authorizes"; `workflows/reconciliation/resources/method.md` §R4–R5 (at `<FROZEN_TREE>`).

## For each of the 25 packets in `<RUN>/R4/PACKETS/`

1. **Three evidence statements.** Pick three substantive statements from "What we found" (prefer
   ones the recommendation relies on), and check each against the frozen tree or run files:
   `CONFIRMED`, `REFUTED` (with the correct fact and its source) or `UNVERIFIABLE`. Also check its
   tag (`[GOVERNING]`, `[CONTEXT]`, `[code]`, `[owner testimony]`, `[run finding]`) against RUN_BASIS
   §5; a CONTEXT source tagged GOVERNING is a finding.
2. **Authority of options and mechanism.** Check that every option and the "On ruling" mechanism
   stay within the run's authority: R5 edits deliverable text only; code changes go to a separate
   implementation brief (Runtime code to the Runtime loop); no lifecycle transition; no agent
   instruction, workflow or Root governance change from this run (routes to Root / HELPS_HUMANS);
   App governing-doc amendments go by their own governed path; rows on D-APP-116..119 stay held.
   Flag anything that overreaches, or a decision type misnamed.
3. **Consistency.** The header `recommended` agrees with the body's recommendation; the question is
   one rulable sentence; sub-question counts agree with `R4/PACKET_SUBQUESTIONS.csv`; the owner's
   R4-Q6 answer is quoted verbatim in P-04 (compare `OWNER_DIRECTION.md` `r2_r4q6_answer`); the
   packet is plain language (flag undefined jargon codes the owner would have to decode).

Also check `R4/R4_DECISION_BOOK.md`: census figures against `R3/CLAIM_CONCORDANCE.csv` +
`EXTENSION_CONCORDANCE.csv`; the ruling order is consistent with packets' `depends_on`.

## Output

`<RUN>/R4/PACKET_REVIEW.md`: a summary table (packet, 3 statement verdicts, authority OK/finding,
consistency OK/finding), then findings, each numbered `RV-nn`, with severity `BLOCKING` (a wrong
fact the recommendation relies on, CONTEXT presented as GOVERNING, an option outside authority) or
`MINOR`, the packet and line, what is wrong, the evidence, and the proposed fix. Helpers in
`<RUN>/R4/_work/RV_scripts/`. Write nothing else.

## Return (≤ 10 lines)

Counts of CONFIRMED/REFUTED/UNVERIFIABLE, findings by severity with IDs, and SHA-256 of
`PACKET_REVIEW.md`.
