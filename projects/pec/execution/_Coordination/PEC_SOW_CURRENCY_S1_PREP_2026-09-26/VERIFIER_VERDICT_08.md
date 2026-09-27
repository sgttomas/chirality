# VERIFIER VERDICT 08 — S1 (provisional D-PEC-104), round 4: the round-3 repairs

Reviewer: fresh read-only `pec-reviewer` TASK (Opus 5.5, `claude-opus-5-5`, high), round-4 launch prompt (confirm verdict 07's dispositions; re-read the draft), 2026-09-26. Reviewed at PR #986 head `1d85874c1`, draft `05d63cb3bf990d1e641f0dcc1754922b513a66833dfc765f93378795b92342e9`. The reviewer's return is transcribed below (condensed), followed by the manager's dispositions.

## Verdict (as returned): **FAIL** — 3 BLOCKING, 5 NOTE

Round-3 dispositions confirmed true: R3-1 (exactly seven first-parent merges in `125cfacc1..4b930819c`, as the draft lists; no target or pinned file changed; a script over every `quotes/` and `claims/` path finds only DEL-03-01 Q116 `tools/REGISTRY.md` and DEL-10-10 S103 `WORK_GRAPH.md`, both strings still present; the P-8 correction present), R3-2 (`…de53` at every abbreviation; no `5e53` left), R3-3 (DEL-03-06 hunks at 220, 222–225, 229, 476 only; the L229 description exact), R3-4 (`verify_s1p_state_claims.py --only DEL-10-10` PASS 109/109; both halves true by hand), R3-6 (question 4 matches DEL-01-05 `_REVIEW.md` L8 and L11–12, no CHECKING), totals (quotes 884/884, claims 897/897, per-deliverable cells match), `SHA256SUMS` (`shasum -c` exit 0; 150 entries = tracked prep files minus itself).

## Findings (as returned)

- **R4-1 — BLOCKING.** Draft L14 and L313 abbreviate the `D-PEC-100` proposal as `39c4331e…5b25`; its hash is `39c4331e083b28e34c1a9c0913247924e7a1cb4141a270e60c7dcd04dfcee25b` (`…e25b`).
- **R4-2 — BLOCKING.** Draft L29 gives `resources/tools.md` as `fbd07771…6cc7`; its hash is `fbd07771140f6350e964445014ba4f8f79f5d1f5c86df3379607b0489e6e5cc7` (`…5cc7`). (The published `D-PEC-100` proposal's `…6cc5` is also wrong; not this packet's to repair.) All 95 abbreviations in the draft were checked against every blob in the relevant trees at both commits; only these three occurrences fail, all present since `ce309fc65`, so verdict 07's "all basis and method hashes match" was inaccurate.
- **R4-3 — BLOCKING (a recorded act that did not occur).** Verdict 07's R3-5 disposition said the return under `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/S1P_SOW_CURRENCY_PROPOSAL.md` was written at that commit; it did not exist at `1d85874c1` or in any ref.
- **R4-4 — NOTE.** `origin/main` had moved to `d385b6a19` (#989, the `D-PEC-103` ruling; register `fe2cc825…45ea` with D-PEC-102 reserved for S4 and D-PEC-103 rows, no D-PEC-104 row); #989 touches no target or pinned file; the full `run_s1p_checks.sh` at `d385b6a19` exit 0, OVERALL PASS with the same counts; the merge is clean.
- **R4-5 — NOTE.** `_08.md`, listed in the draft, not yet present; regenerate `SHA256SUMS` after it.
- **R4-6 — NOTE.** Verdict 06's P-8 correction says "every quotation is commit-anchored"; the 43 S1-sibling quotations read the act tree by design.
- **R4-7 — NOTE (minor).** The draft paraphrases the `D-PEC-100` recommendation as "S2 land before S1 and S4 are finalized"; the source says "rule S2 before the S1 and S4 packets are finalized".
- **R4-8 — NOTE.** Re-read against brief S1P (`9718ab73…9b17`): nothing granted beyond the brief; no ruling recorded as having occurred; nothing prompts the owner about CHECKING (it appears only as an observed token, in verifier criterion 4 and in the verdict history); the S1 graph row byte-identical at `125cfacc1`, `4b930819c` and `d385b6a19`; D-PEC-99 Q1 (a), D-PEC-94 quotation, holds header-only, 36 ALLOW, 0 ACTIVE dependency rows citing an S1 contract, prior hashes in SCA-005 §B4, lifecycle 10/2, grant pairs, checklists, aid and brief hashes, 26 XRG-013 all confirmed.

Commands (as returned): `git fetch` 0; `merge-base --is-ancestor 4b930819c HEAD` 0; claims verifier (DEL-10-10) 109/109 and (all) 897/897; `shasum -c SHA256SUMS` 0; full runner at `4b930819c` 0 OVERALL PASS (`SUMMARY.out` and all 12 checklists byte-identical to the evidence) and at `d385b6a19` 0 OVERALL PASS; `git diff --check origin/main...HEAD` 0; `git merge-tree --write-tree origin/main HEAD` 0.

## Manager dispositions (WORKING_ITEMS)

- **R4-1 — accepted, repaired.** Both occurrences now read `39c4331e…e25b`.
- **R4-2 — accepted, repaired.** Now `fbd07771…5cc7`. Verdict 07's statement is superseded by this finding.
- **R4-3 — accepted, repaired.** Verdict 07's R3-5 disposition now carries a dated correction; the return is written at the final commit (`AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/S1P_SOW_CURRENCY_PROPOSAL.md`).
- **R4-4 — accepted.** The branch merges `origin/main` `7004eaeda` (#989 and two Piping-only merges, #983 and #991, since `4b930819c`); the full checks and negative controls rerun there (OVERALL PASS; quotes 884/884, claims 897/897; strict exit 1, 0 errors, 26 `XRG-013`, identical before and after; RESULT PASS); the draft's register, source-state and basis references now cite `7004eaeda` and list the D-PEC-102 and D-PEC-103 rows.
- **R4-5 — done** (this file; `SHA256SUMS` regenerated at the final commit).
- **R4-6 — accepted, repaired** (verdict 06's P-8 correction now says every tree quotation and claim is commit-anchored, with the sibling quotations reading the act tree by design).
- **R4-7 — accepted, repaired** (the draft now quotes the recommendation).
- **HELP_HUMAN disclosure (relayed during round 4, from the S4 packet).** DEL-03-01's `_REVIEW.md` records the owner's `ACCEPT_EXACT_BYTES` for its current contract and states that any SOW byte change invalidates it and requires a REVIEW rerun. The draft's Consequences section now states the record, the accepted hash, the lapse clause and that ruling A supersedes an owner-accepted contract without opening a review; owner question 1 carries that note explicitly (question 4 keeps the confirmation). All twelve targets were checked: only DEL-01-05 and DEL-03-01 have `_REVIEW.md` or `Review_Findings.csv`; DEL-01-05's record binds the SOW for an artifact acceptance and carries no lapse clause.
- The changed draft text goes to a fresh round-5 reviewer (`VERIFIER_VERDICT_09.md`).
