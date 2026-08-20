# Handoff amendment 01 — return to CHANGE

- Basis: `d8c47d9fbc459b32c053c844be0fa789fd1ffab2`, D-APP-97 C1.
- Correction: ten AgentRuns files each lost one extraneous final empty line; no other predecessor byte changed; `AMENDMENT_01_EOF_WHITESPACE.md` records the cause and supersession.
- Current review authority: `FROZEN_DIFF_MANIFEST_V2.md` plus `REVIEWER_RETURN_02.md`; the v1 identity/review remain historical and are not current correction-closeout proof.
- Fresh review: `PASS`, 23/23 corrected subject hashes and aggregate identity matched, zero findings.
- Manager status: `CORRECTION_REVIEWED / READY_FOR_CHANGE_RESTAGE / EXTERNAL_PROOF_REQUIRED`.

CHANGE must discard no work and make no semantic edit. Restage the exact final candidate paths from the worktree, then run `git diff --cached --check`. A zero exit is required before commit. If it fails, return the exact finding without commit. If it passes, proceed with the previously issued initial proof-loop commit handoff, then run committed candidate-range G4 and open/push the PR proof loop.

Shared `LOOP_RECEIPTS.md` and `PLAN_COMPLETION_LOG.md` remain untouched. DEL-09-04 remains `IN_PROGRESS`; R4-P49 Remaining remains open; actual macOS staged/mounted proof and committed-range G4 remain required. No signing, notarization, publication/distribution, release-readiness, lifecycle, merge, owner-machine, provider/network, credential, dependency/lockfile, or foreign-loop authority is created.
