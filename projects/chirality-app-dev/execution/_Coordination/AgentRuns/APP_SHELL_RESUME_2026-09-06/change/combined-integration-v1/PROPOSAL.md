# Isolated App D124 + Runtime PR738 validation lane

Owner authorized local isolated preparation/integration validation. Original App checkout synchronized by fresh fetch: HEAD equals origin/main `ec491aee1870a2a6a8eb2faf2919d4d5db5124b4`. Runtime PR738 is OPEN at `49951af6237bbb8701c0a2cebcd8c30fbde75b8e`, based on `ec491aee1870a2a6a8eb2faf2919d4d5db5124b4`. No published change outside Runtime is included. The original dirty App run remains intact (715 path identities).

Executed clean isolated checkout recipe:
```
git worktree add --no-track -b codex/app-runtime-integration-20260906 /private/tmp/chirality-app-runtime-integration-20260906-738-49951af 49951af6237bbb8701c0a2cebcd8c30fbde75b8e
```

The isolated checkout is clean. Branch is a candidate integration-validation lane, not accepted main. Its source basis is the published PR738 commit, not the external Runtime agent's mutable worktree.

Only pending App overlay: `projects/chirality-app-dev/frontend/tsconfig.electron.json` from immutable run candidate `pkg02/final-validation-v1/typecheck-repair-candidate/tsconfig.electron.candidate.json`, exact raw-byte SHA256 `522b114f541f6b4882404069f6b4ca5553f887635948df972c07bbbed849f5b0`. Isolated file preimage is `8b8bfb49b7e9361cdbbcd94dbc4df31ccb16f3dda24c37b0859ef48639de23ec`. The original App file also equals the frozen postimage. Do not copy seven shell redesign files or any other dirty App source. No overlay applied yet: await frozen parent brief and release; then verify both hashes, copy this one candidate, assert exactly one tracked changed path and preserve every other tracked input.

Validation commands/dependency preparation require the parent's exact frozen brief. No provider, fixture, environment-source or tracked Runtime edits; no operational external Runtime agent state; no push, PR, merge publication, source acceptance or release claim. Isolated ignored dependency/build outputs may be selected under the subsequent validation brief. Stop on drift or a requested wider repair.

The existing successful dependency preparation in the original App checkout does not validate the new PR738 source/dependency basis: isolated installation/build/checks remain required. `PR_CHANGED_PATHS.tsv` records the candidate's full Runtime path delta.
