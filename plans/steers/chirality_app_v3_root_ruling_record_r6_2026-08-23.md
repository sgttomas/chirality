# ROOT RULING RECORD R6 — SCA-004 Gate-5 confirmation, pointer approval with named fills, Git-effect backfill — owner ruling of 2026-08-23

> **Plans-folder status:** ACTIVE owner-ruling record — non-governing transcription source. Owner: Ryan Tufts. Scope: SCA-004 closure (Gate-5 confirmation, `_LATEST.md` pointer, Git-effect backfill). Target workspace: Root governance loop (transcribed into Receipt 120). Supersedes nothing; the loop's instruments govern. Companion to `plans/steers/chirality_app_v3_root_ruling_record_r5_2026-08-23.md`.


Ruled by Ryan Tufts (K-AUTH-1) in the HELP_HUMAN session minder chat, after
PR #633 merged as `6d4438d8d3a580b65d6d50ad497dadfe07f177f2` (Root Phase 0f,
Gate-5 second attempt; content commit `4ad3fea7ef9e397852913c08e533e1846e264134`, PR head `17d3bc2af666005676a517c0a37e5ebd7b3a6614`;
Receipt 119). HELP_HUMAN had byte-verified the applied state on `main` before
the slate: all seven live files under `execution/_Decomposition/` equal the
R4-A applied identities exactly; its own rerun of `validate_gate5_applied.py`
returned PASS 65/65 with the validation JSON identical except the recorded
absolute worktree path; the post-Gate-5 `AUDIT_DECOMP` backcheck reports
`overall_status OK`, zero blocker/warning/info issues, and
`closure_readiness PASS_FOR_GATE5_APPLIED_PACKAGE_ONLY` against the preserved
Gate-1 baseline `2210e77f…`; `_LATEST.md` unchanged at `b2849c6e…`. "[click]"
marks the option the owner selected.

R6-A — SCA-004 Gate-5 confirmation: [click] "Confirm".
  Subject state: the seven live files at the R4-A identities
  (`546b6e4c…`, `2cdf1e68…`, `63e6fa6b…`, `b65da0f8…`, `9fcfa2a5…`,
  `750aed6c…`, `bdd6bc08…`; full values in the R4 record), read against
  `Gate_5_Application_Record.md` SHA-256
  `31207f122e9d64b4734a701cae364b2456df65d0605b2b1d0c6880ce5595760a`,
  `Gate_5_Rehearsal_Record.md` SHA-256
  `ea5d90e88ebc7528f758664bf354f815deb8c50b638276ead19a5f49f9f92532`,
  `Gate_5_Applied_Validation.json` SHA-256
  `f811bf1c08742833ef13ca0a503ecb8d5ac965a093b21f04767c4e8df6daa1b1`,
  and the backcheck `coverage_summary.json` SHA-256
  `70ed91a848c762d9afb778423220c53408e1e4d2273a4a8aa7d5d81fd25359e9`.
  Recorded form: the owner confirms the SCA-004 Gate-5 application. Revision
  1.3 is the accepted current basis. SCA-004 Gates 1–5 are complete.
  Propagation remains later, separately gated work per the approved
  `Propagation_Plan.md`: PREPARATION INIT ×7, the DEL-02-06 `_CONTEXT.md`
  edit list, dependency extraction, estimates, schedule, `WORK_GRAPH.json`/
  `DAG.md` re-derivation, and `AUDIT_DEP_CLOSURE`. No hold is lifted; all ten
  DEL-02-06 bindings remain `HELD_UNAVAILABLE`.

R6-B — `_LATEST.md` pointer: [click] "Approve with named fills".
  Subject bytes: `Gate_5_Pointer_Candidate.md` SHA-256
  `5918e7bff305bfc0a22c4a4fd172a2ad7bf013a217a778d6ca3797ce773dfabf`.
  Recorded form: the owner approves replacing
  `execution/_ScopeChange/_LATEST.md` (currently SHA-256
  `b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1`) with
  the candidate's fenced replacement bytes, with exactly three slot fills
  from recorded acts and no other change:
    application-append approval reference → `R4-A` (owner ruling record
      `plans/steers/chirality_app_v3_root_ruling_record_r4_2026-08-23.md`,
      SHA-256 `5916aa599bf5953324636b8c5e0b0a5e2b9e6a793fd6dd9b1cac1c7e19e0755a`);
    Gate-5 confirmation reference → `R6-A` (this record);
    Git effect → PR #633 merge
      `6d4438d8d3a580b65d6d50ad497dadfe07f177f2` (content
      `4ad3fea7ef9e397852913c08e533e1846e264134`, PR head `17d3bc2af666005676a517c0a37e5ebd7b3a6614`).
  The applying tranche drafts the final pointer bytes; HELP_HUMAN
  byte-verifies before endorsement that they differ from the candidate's
  fenced block only at those three slots. The pointer identifies revision 1.3
  as the accepted decomposition basis and SCA-004 as the latest snapshot.

R6-C — SCA-004 Git-effect backfill: [click] "Authorize".
  Recorded form: the owner authorizes filling the `TBD` Git-effect and
  reference slots in `Gate_5_Application_Record.md` and the SCA-004
  `Decision_Log.md` (and only those slots) from the recorded chain, in the
  D-GOV-34 backfill convention — nothing inferred: content commit
  `4ad3fea7ef9e397852913c08e533e1846e264134` (full value from the PR #633 chain), PR head `17d3bc2af666005676a517c0a37e5ebd7b3a6614`,
  merge `6d4438d8d3a580b65d6d50ad497dadfe07f177f2`; append-approval
  reference R4-A; execution authorization R4-B; re-authorization R5-A;
  confirmation R6-A. Each fill is shown as a one-line diff in the receipt.

Not ruled here: any PREPARATION INIT dispatch, SOW, `_CONTEXT.md` edit,
dependency, estimate, schedule, graph, or audit act (all remain later
propagation work); the pending App-loop PR #632 (its whitespace repair
proceeds under its own direction); C1 (App Server 0.149.0 artifact download)
remains not authorized; no pin change (G0 B4; TM-ROOT-106/122 stay G1
blockers).
