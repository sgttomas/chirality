# Handoff State — WI-PKG09-RUNATLOAD-01

- Upstream snapshots: D-APP-97 C1; live DEL-09-04 SOW/status/dependencies;
  `origin/main@7584de0a8`; exact final product hashes in `MANAGER_RETURN.md`.
- Closure verdict: `PRODUCT_VALIDATED / EXTERNAL_PROOF_PENDING`.
- Current derivative package: manager/child briefs, returns, statuses, check
  JSON, reviews, and DEL-09-04 pre-CI run record are current.
- Remaining blocker: PR-CI `macos-15` launchd execution only.
- Rerun requirement: `artifact-proof` label must trigger the unsigned Desktop
  job; inspect the dedicated proof summary and verify PASS/identity/cleanup/
  default-protection fields before status closeout.
- Next owner: Agent 0 for integration decision; CHANGE for Git/PR; Agent 0 for
  single shared fan-in closeout after CI evidence.

## Exact CHANGE handoff

1. Integrate this branch with `origin/main@7584de0a8` (PR #590) before commit;
   preserve the exact event types, `artifact-proof` job gate, and associated
   test bytes already present in the working tree. Do not lose or duplicate
   upstream intent.
2. Verify final four product/test hashes match `MANAGER_RETURN.md` after
   integration, or rerun the full focused/registered/fresh-review gate if
   semantic bytes change.
3. Stage only the four product/test paths, this run root, the DEL-09-04 pre-CI
   run record, and Agent-0-owned minimal shared closeout changes. Exclude
   generated build outputs and unrelated dirty files.
4. Commit the validated node, push branch
   `codex/app-launchagent-runatload-proof-20260820`, and open one PR against
   `main` with PR #590/base dependency stated as already integrated.
5. Apply PR label `artifact-proof`. Wait for `Desktop Unsigned Artifact
   Verification` job `verify-unsigned-macos`; require step `Prove packaged
   LaunchAgent RunAtLoad` and job success.
6. Inspect artifact `chirality-packaged-launchagent-runatload-proof` summary:
   `status=PASS`; `runAtLoad`, `bootstrapOnly`, `automaticLaunchObserved`,
   loaded program/process identity true; cleanup process/job/plist/runtime true;
   default plist/job state unchanged and mutation targets excluded.
7. Only after that proof, Agent 0 performs the single shared receipt/completion/
   DEL-09-04 Remaining closeout and records the CI run/job/artifact identity.
