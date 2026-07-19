# Sealed Verifier Brief — V1 Carry-Forward (refutation-only)

- **Parent:** HELP_HUMAN (Agent 0), RunID `D-APP-64_REASONED_SELECTION_OVERLAY_2026-07-18`
- **Verifier posture:** fresh context; no shared authorship with the work it
  checks; read-only except the single return file; sole deliverable is
  `COMMIT-SAFE` or `BLOCK`.
- **Write scope:** exactly
  `projects/chirality-app-dev/execution/_Coordination/AgentRuns/D-APP-64_REASONED_SELECTION_OVERLAY_2026-07-18/RETURN_CARRY_FORWARD_1.md`.

## Claims to refute (carry-forward contract)

Baseline: `projects/chirality-app-dev/loop/WORKPLAN_2026-07-18_app_dev_loop.md`
(committed, unmodified). Candidate:
`projects/chirality-app-dev/execution/_Coordination/AgentRuns/D-APP-64_REASONED_SELECTION_OVERLAY_2026-07-18/WORKPLAN_CANDIDATE_2026-07-18b_app_dev_loop.md`.

1. The candidate differs from the baseline ONLY within six bounded regions:
   (E1) the epistemic-status header's first three lines (re-mint lineage:
   "Re-minted at owner standing direction … through the D-APP-64 overlay;
   supersedes `WORKPLAN_2026-07-18_app_dev_loop.md` …, carried forward
   verbatim except the clauses marked *(D-APP-64)*, with the carry-forward
   gated by an independent verifier");
   (E2) one new Owner-intent bullet beginning `- **2026-07-18** (D-APP-64):`
   inserted immediately after the D-APP-61 M2-A bullet;
   (E3) in protocol Step 1, the delegation-triage sentence "Decide what
   clearly passes … naming the failed gate in near-miss form." replaced by the
   fast-reject-boundary / select-and-advance sentence marked `*(D-APP-64)*`,
   with the following asymmetry sentence intact;
   (E4) in Step 2, "under the D-APP-60 instrument" extended with "as refined
   by the D-APP-64 overlay *(D-APP-64)*", parenthetical duties unchanged;
   (E5) in Step 3, the sentence extension "as refined by D-APP-64: ambiguity
   about whether a fast-reject boundary is touched is owner-class; plurality
   of surviving defensible outcomes is not itself owner-class *(D-APP-64)*";
   (E6) in the pointer index's Delegation-instrument bullet, the insertion
   "as refined by the D-APP-64 reasoned-selection overlay (fast-reject
   boundary, selection method, attribution schema) *(D-APP-64)*".
   Every byte outside those six regions is identical, including all fences
   (F-APP-1..5), fresh-ruling stops, Step 0/4/5 text, and the rest of the
   pointer index.
2. No delta weakens, deletes, or reorders any hard fence, fresh-ruling stop,
   non-negotiable, or check obligation.
3. The candidate's Appendix-W twin — the span between
   `<!-- BEGIN APPENDIX W D-APP-64 -->` and `<!-- END APPENDIX W D-APP-64 -->`
   in `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-64_PACKET_REASONED_SELECTION_OVERLAY_2026-07-18.md`
   — is byte-identical to the candidate file minus its single trailing LF.

Method: derive your own diff (e.g. `git diff --no-index`) and your own span
extraction; do not rely on any run record, return, or brief narrative as
proof. Any unexplained byte delta, any seventh region, or any claim-3
mismatch is `BLOCK`. Default to `BLOCK` if uncertain.

## Return format

Write `RETURN_CARRY_FORWARD_1.md`: verdict line first
(`Verdict: COMMIT-SAFE` or `Verdict: BLOCK`), then per-claim findings with
the evidence commands you ran and their observed results.
