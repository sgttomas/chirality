# Validation — GOV-STEP4-OPERATIVE-20260729

Status: `PRE-COMMIT PASS`

## Basis and preimages

- Worktree branch `gov/step4-operative-surfaces` resolves to
  `ea3db3607fbcbb7ce5f65bab31268a7eca431adb` (frozen basis; clean before
  authoring). PRD Rev 7 annex §5.3.1 verified live at this basis.
- `agents/AGENT_CHANGE.md` preimage SHA-256 verified equal to the
  POLICY_DELTA row-8 pin
  `1269db1275aa55bd0940ae2bd29a2299cc3e881ef571d8a5d4fb4713d0987243`
  before editing; postimage
  `f59e5455e1eeac687f69f091a74974fbfb2fb0a520fcb3bc7db8ab24529a4c77`
  recomputed after the final edit and quoted identically in all three
  routed M6 notices.
- Backfill SHAs resolved from git, short to full:
  PR 410 merge `7eda81c0c990471ba1b27d7cee7249cc01d74e04` (2026-07-28);
  PR 411 merge `1d4d3187ba120e328cd2f6bf2a515a8f17635cb5` (2026-07-28);
  PR 412 merge `9f5af48c259eb5a7f93f448431eb32d2e409d565` (2026-07-28);
  PR 416 merge `ea3db3607fbcbb7ce5f65bab31268a7eca431adb` (2026-07-29).
- Owner merge-direction quote transcribed byte-exact for the D-GOV-31
  merge-execution note: `Merge PR #416 and then proceed accordingly.`
  — 43 bytes UTF-8, SHA-256
  `2e98e19bb48e9c1d02c607a83373e12c7a70adf1847962fae9c7cc34d5e3b565`,
  verified with `printf | shasum -a 256`.

## Deterministic checks

- `python3 -m pytest tools/validation/test_validate_instruction_tranche_manifest.py -q`
  — 36 passed, exit 0. The suite keeps `test_block_on_self_merge` (the
  preserved failing mode for undeclared self-merge) and adds passing and
  failing `m2_gate.merge_execution_grant` cases (complete grant PASS
  with INFO; incomplete, expired, malformed-SHA, and non-repo-relative
  grant-record cases BLOCK).
- `python3 tools/validation/validate_instruction_tranche_manifest.py`
  (G4 CI mode) — `G4 PASS (CI mode)`: all 15 manifests schema-valid,
  including `ROOT-GOV31-PROPAGATION-20260729`, exit 0.
- `python3 tools/validation/validate_candidate_whitespace.py --base-ref
  ea3db3607fbcbb7ce5f65bab31268a7eca431adb` — run against the committed
  HEAD after the tranche commit; result recorded below.
- `git diff --check` clean on the working tree; trailing-whitespace grep
  over every touched file clean.
- `grep -rn "never self-merge" execution/_Coordination/LOOP_INIT.md
  agents/` — no matches (exit 1). Live operative surfaces carry no
  superseded literal.

## Row-7 harness-mapping verification (no change)

`docs/CONTRACT.md` §1.8 K-MERGE-1 is byte-unamended by Rev 7; annex
§5.3.1 strengthens evidencing only. The
`tools/practitioner_harness/harness_common.py` line-78 mapping
`"K-MERGE-1": "RATIFIED"` remains accurate. No edit made; verification
recorded here per POLICY_DELTA §4 row 7.

## Grant candidate identity

`docs/governance_harness/_PROPOSALS/GRANT-2026-07-29_transition_merge_execution/GRANT_CANDIDATE.md`
SHA-256
`cdd8844b42ca772aab96b5c942873eb4e7c957f0b262fba6daabc61834f2f38e`
(token SHA8 = `cdd8844b`). DRAFT — no effect until owner issuance by
token per annex §5.3.1.

## Post-commit check (appended at closeout)

- Committed-HEAD whitespace validator
  (`--base-ref ea3db3607fbcbb7ce5f65bab31268a7eca431adb`): recorded in
  HANDOFF_STATE with the commit SHA.
