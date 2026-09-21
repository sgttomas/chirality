# Review return 1 — D-APP-128 activation candidate

- Reviewer: fresh-context read-only TASK (Type 2, no write scope, no delegation), Claude Opus 5, dispatched by HELP_HUMAN via harness-native Agent spawn, 2026-09-21. Same-model independent context, not model diversity.
- Candidate reviewed: `00115c719..2f040ed23` (PR #836).
- Verdict: PASS with four non-blocking findings. Checks it ran: every one of the 54 status files by script; all nine quote hashes and the plan hash; the six pinned method hashes; git claims; `harness.py self-check` exit 0; `app_hold.py scan --require-register-match` PASS.

| Finding | Disposition | Repair |
|---|---|---|
| 1a DEL-00-02 kept a sole `- None.` beside the new item; packet §8 said 51 appended | Accepted | `- None.` removed; packet §8 now 50 appended + 2 replaced |
| 3a Ruling said no `docs/` file differed, but the tranche manifest is under `docs/` | Accepted | Reworded to "no governing `docs/` file" |
| 3b "Not a divergence" sentence read as broader than the owner's words | Accepted | Relabelled as agent application; post-v3.0.1 row marking retained |
| 7a Work graph carried pre-ruling text | Accepted | Scope, packet node and R1a blocker updated |

Backcheck after repair: script over all 54 files, 0 problems (no `None.` beside an item, exactly one pinned item each, no residual gate); registered checks rerun PASS (`STAGE_P_RULING_CHECKS.json`).
