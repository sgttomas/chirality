# APP-DEV LOOP STEER — v3 pointer act: `_LATEST.md` to SCA-APP-008 — 2026-08-24

> **Plans-folder status:** ACTIVE owner-carried steer — non-governing
> coordination instrument. Owner: Ryan Tufts. Target workspace: App-dev loop.
> Authorizing ruling: A9 (`chirality_app_v3_app_ruling_record_a9_2026-08-24.md`;
> SHA-256 recorded in the PR that published this steer — the files merged
> together). This steer is the contract for one bounded act. Read it in full
> before any write.

## Basis gate (check before any write; stop and report if any line fails)

1. `origin/main` contains merge commit
   `d5e40b3c25fe527919f1d2d2a31ea97ce2835795` (PR #662, SCA-APP-008 Gate 5).
   Work on a fresh branch `codex/app-v3-pointer-act-2026-08-<DD>` from current
   `origin/main`. Record the exact basis commit.
2. All paths below are relative to `projects/chirality-app-dev/`. Verify these
   exact identities at the basis:
   - `execution/_ScopeChange/_LATEST.md` — SHA-256
     `a0298fdc5709181119d4c645b72b72f07b0c3b14904da67043d9de1f7ee01794`,
     1347 bytes, Git blob OID `c6ce8b2a92c67506887d95c88790a445dbc5668d`.
   - `execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/Phase5/_LATEST.proposed.md`
     — SHA-256
     `12c7758b4ec15c50379fcae1bf26670e26e281518687db4dc9200ff9dd23cc9b`,
     1572 bytes, 21 lines.
   - `execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/Phase5/LATEST_POINTER_CANDIDATE.md`
     — SHA-256
     `44c39e11b4de7621fe25d643d049443223ffbbcd8160855c3fb85d4a4186609a`.
   - `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` —
     SHA-256
     `932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f`.
   - `docs/CONTRACT.md` — SHA-256
     `842bf170e6737adf8eaa7a4a1acfd74e22390bc6e14c64eed9502195c68dbed9`.
   - `execution/_Decomposition/contract_invariant_coverage_register.csv` —
     SHA-256
     `62c9a318cf673b9b72bf31754aaf7dadb0f2db4b439eb79232c9e8d456d70bb3`.
3. Incorporate by reference (immutable path + SHA-256; do not transcribe):
   this steer and ruling record A9 at their `plans/steers/` paths, with the
   SHA-256 values recorded in the PR that published them.
4. If any identity, byte count, or line count above fails to verify, stop and
   report. Do not repair, regenerate, or substitute.

## Authority context

A8-B withheld `_LATEST.md` movement from the Gate-5 act and directed an exact
pointer candidate instead, per Gate-4 section 8's fallback. Gate 5 executed
that way and merged. A9-A now authorizes applying exactly the candidate's
proposed post-image. This steer grants that one application and nothing else:
no notice routing, no carrier activation, no SOW/lifecycle/status change, no
implementation, release, publication, readiness, or reliance authority, and
no blocker lift.

## The act

1. Re-hash the live target immediately before writing. It must still be the
   exact pre-image (`a0298fdc…`, blob `c6ce8b2a…`). Any divergence stops the
   act fail-closed.
2. Replace the full contents of `execution/_ScopeChange/_LATEST.md` with the
   exact bytes of the immutable snapshot file `Phase5/_LATEST.proposed.md` in
   one atomic write. Copy the bytes from the snapshot file; do not re-type,
   regenerate, template, or reflow them.
3. Verify the applied file: SHA-256
   `12c7758b4ec15c50379fcae1bf26670e26e281518687db4dc9200ff9dd23cc9b`,
   1572 bytes, 21 lines, and `git hash-object` agreement with the snapshot
   file's blob. If any check fails, restore the pre-image (blob
   `c6ce8b2a92c67506887d95c88790a445dbc5668d`), verify the restoration, and
   stop with a report.

## Post-write validation

- Run candidate whitespace against the recorded basis commit; it must pass.
- Run authority-corpus `status`; it must report no drift (the pointer file is
  not a governed corpus member, so no `bump`/`apply` is expected — if `status`
  demands one, stop and report rather than running it).
- Run the loop's receipt validator after the receipt append.
- Confirm with `git status`/diff that exactly the write set below changed and
  nothing else.

## Review, receipt, and return

- One fresh independent reviewer instance verifies the transaction: basis
  identities, pre-image re-verification evidence, applied post-image identity,
  snapshot-byte provenance, and the absence of any other write. Its review and
  return are recorded in the run evidence.
- Append Receipt 200 (parent `Receipt-199`) to `loop/LOOP_RECEIPTS.md`,
  incorporating this steer and A9 by immutable path and SHA-256 and recording
  the applied pre→post identities and the review verdict.
- Record run evidence under
  `execution/_Coordination/AgentRuns/APP_V3_POINTER_ACT_2026-08-<DD>/`.
- Commit, push the branch, and open one unlabeled PR against `main`. Do not
  merge. The owner decides the merge separately.

## Write set, exactly

- `projects/chirality-app-dev/execution/_ScopeChange/_LATEST.md` (the exact
  proposed post-image only).
- One append to `projects/chirality-app-dev/loop/LOOP_RECEIPTS.md`
  (Receipt 200; parent Receipt-199).
- New files strictly inside
  `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_POINTER_ACT_2026-08-<DD>/`.

Not selectable: every `_ScopeChange` snapshot file (all existing snapshot
contents are immutable, including every SCA-APP-008 artifact); the
decomposition, contract, and companion register; any `_REFERENCES.md`,
`Dependencies.csv`, `_DEPENDENCIES.md`, or `AUTHORITY_CORPUS.json`; the App
Task Management register; any carrier SOW, `_CONTEXT.md`, `_STATUS.md`, or
lifecycle file; any `_Evaluation` file; anything under
`projects/chirality-app-dev/frontend/` or any other
`projects/chirality-app-dev/docs/` file; any Root-loop path; `agents/**`,
`tools/**`, `AGENTS.md`, root `docs/**`, `exports/**`, `plans/**`; any other
project. Routing `Phase5/NOTICE_TO_ROOT_READY_TO_ROUTE.md` is forbidden in
this act.

## Sync rule

If `origin/main` advances mid-run, the Receipt-197 standing authorization
permits one non-rewriting sync; record it, and stop fail-closed if the sync
changes any identity named in the basis gate.

## Rollback and abort

Until owner merge, rollback truth for the target is Git blob
`c6ce8b2a92c67506887d95c88790a445dbc5668d` (the exact pre-image). Any
validation failure, identity disagreement, or unexpected write restores the
pre-image, verifies the restoration byte-for-byte, and stops with a report.
A stop-and-report is a compliant outcome of this steer, not a failure.

## Discipline

Fail closed on every disagreement. Produce durable evidence for every claim.
Do not expand the write set for any reason; if the act appears to require a
write outside the set, stop and report — the owner decides. No authority is
inferred from this steer beyond the single pointer application it names.
