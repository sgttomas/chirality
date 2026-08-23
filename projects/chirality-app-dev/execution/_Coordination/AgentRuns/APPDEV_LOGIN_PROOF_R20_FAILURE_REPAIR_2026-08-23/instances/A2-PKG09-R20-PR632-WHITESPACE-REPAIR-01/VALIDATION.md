# Validation — PR #632 record-only whitespace repair

## Verdict

`REPAIR PASS — POST-COMMIT VALIDATION REQUIRED`

The exact 12-path mutation and its lossless postimage verification passed. The first attempted post-repair validator invocation exited `1` because its committed-range subcheck evaluates `origin/main...HEAD`, not the repaired worktree candidate. HEAD remains the required Git-fenced basis commit and therefore still contains all 12 preimages. HELP_HUMAN, through the parent manager, classified this as a documented sequencing diagnostic rather than a substantive repair failure and directed terminal candidate freeze for an intermediate CHANGE commit. No later substantive gate was run.

## Commands and exits

| Order | Command or bounded operation | Exit / result |
| ---: | --- | --- |
| 1 | `git rev-parse --show-toplevel` | `0`; `/Users/ryan/.codex/worktrees/ef5e/chirality` |
| 2 | APP-HOLD-1 dispatch preflight from the App root: `python3 execution/_Scripts/app_hold.py check --operation dispatch --entry-path execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/briefs/A2-PKG09-R20-PR632-WHITESPACE-REPAIR-01.md --target DEL-09-04` | `0`; `ALLOW`, `DEL-09-04` not held |
| 3 | Read-only HEAD/frontend/preimage byte-count, SHA-256, and RETURN line-hex freeze | `0`; all 12 diagnostic preimages reproduced exactly |
| 4 | One targeted `apply_patch` removing exactly one terminal U+0020 from each of RETURN lines 23–25 | success; 16,439 → 16,436 bytes; SHA-256 `7d3b2ad4f49c2316dce7e1878ca4426ab5cb367e64a385ea2ee3137b37a5d399` → `253819ca75533f6c0f46f9844ea1641f16e694a51ed3e4fffd9bb80b9f0afb55` |
| 5 | One `gzip -n -9` invocation over the exact 11 diagnostic raw-log paths | `0`; every raw source deleted and same-name `.gz` created |
| 6 | Per-member raw-absence, gzip-presence, `gzip -t`, `gzip -cd` byte-count/SHA-256, RETURN hash/hex, and Git-diff verification | `0`; all 11 recovered preimages exact and RETURN diff limited to the three authorized bytes |
| 7 | `python3 tools/validation/validate_candidate_whitespace.py --base-ref origin/main` | `1`; `FAIL: candidate whitespace findings (untracked binary/symlink paths safely skipped: 11).` |

## Controlling failure

The validator first invokes Git's committed-range check for `origin/main...HEAD`. Because the sealed brief forbids staging or committing, HEAD is still `85caafd4882a2ffff204ed87334171608ce462be`, whose committed diff contains the 12 frozen defects. The validator therefore reports those committed preimages even though the worktree replacements are exact. Its later unstaged and untracked checks do not cancel committed-range findings. This invocation is retained as a sequencing diagnostic; it is not a post-commit verdict on the repaired candidate.

The same run also found one terminal blank line in the newly created instance-local `ACTIVATION.md`. That record-only artifact was cleaned while freezing this terminal report. The validator was not rerun because exact committed-range evaluation must follow the intermediate repair commit.

## Terminal candidate freeze authorized after the diagnostic

- All 11 raw source paths are absent; all 11 same-name `.gz` files are regular files; every `gzip -t` exits `0`; and every `gzip -cd` byte count and SHA-256 matches its frozen raw preimage.
- Repaired executor RETURN remains 16,436 bytes / SHA-256 `253819ca75533f6c0f46f9844ea1641f16e694a51ed3e4fffd9bb80b9f0afb55`.
- HEAD remains `85caafd4882a2ffff204ed87334171608ce462be`; frontend tree remains exactly `b4c73edda1fe3346815ce75449b2327c80c79bf8`; frontend worktree status and `cb008dc5d6aa9b249639c91f3453a18609530d0f..HEAD` frontend diff stat are empty.
- Full candidate status contains only `projects/chirality-app-dev/` paths; outside-App status is empty.
- `git diff --cached --name-only` is empty.

## Exact child-owned inventory

- Modified: `instances/A2-PKG09-R20-PHASEB-EXECUTE-01/RETURN.md`.
- Deleted raw paths: `desktop-pack.full.log`, `app_hold.log`, `corpus.log`, `focused.log`, `npm-test.local-socket-cure.log`, `npm-test.sandboxed.log`, `package_verify.log`, `pytest.log`, `receipt.log`, `self_check.log`, and `typecheck.log` in the executor instance.
- Added gzip paths: the same 11 raw names with `.gz` appended in the executor instance.
- Added unique-instance evidence: `ACTIVATION.md`, `REPAIR_LINEAGE.md`, `VALIDATION.md`, and `RETURN.md` in `instances/A2-PKG09-R20-PR632-WHITESPACE-REPAIR-01/`.
- Total child-owned filesystem paths: 27. Manager-owned preparation paths already present before dispatch remain outside this child's ownership.

## Unreached gates

Receipt validation, aggregate `git diff --check`, App containment/index/frontend identity, instruction-root identity, authority-corpus status, routed tools/practitioner validation, repository self-check, G0–G4 live gates, and any remaining non-product pre-push checks were not run after the controlling failure.

## Rerun requirement

CHANGE must make the authorized intermediate record-repair commit, after which the exact validator can evaluate the repaired bytes as part of HEAD. This Agent-2 instance has no authority to stage or commit. Candidate bytes are ready for that bounded CHANGE handoff.
