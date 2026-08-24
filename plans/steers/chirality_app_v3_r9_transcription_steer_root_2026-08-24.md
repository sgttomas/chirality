# ROOT LOOP STEER — v3 R9 transcription: seat the schedule-basis acceptance — 2026-08-24

> **Plans-folder status:** ACTIVE owner-carried steer — non-governing
> coordination instrument. Owner: Ryan Tufts. Target workspace: Root loop
> (repository root `execution/`). The loop's instruments govern; this steer
> directs one bounded tranche under them. Authorizing ruling: R10
> (`chirality_app_v3_root_ruling_record_r10_2026-08-24.md`; SHA-256 recorded
> in the PR that published this steer — the files merged together). This
> steer is the contract for one bounded act. Read it in full before any
> write.

## Basis gate (check before any write; stop and report if any line fails)

1. `origin/main` contains merge commit `84fe4c6ce` (PR #663). Work on a fresh
   branch `codex/root-r9-transcription-2026-08-<DD>` from current
   `origin/main`. Record the exact basis commit.
2. Verify ruling record R9 at
   `plans/steers/chirality_app_v3_root_ruling_record_r9_2026-08-23.md`,
   SHA-256
   `bc3a3bf414cfd64a5a650d633e942c2bb741a4562622857a79f5101c837e577b`.
3. Verify all seven accepted identities in
   `execution/_ScopeChange/SCA-004_2026-08-22_1749/Evidence/SCHEDULE_BASIS_POST_PHASE4/`
   (SHA-256):
   - `SCHEDULE_BASIS.md`
     `cbcb84e91f6eaf1d00a31a17bc4938fab0a48afcb955366d79e68e9b52244e20`
   - `WORK_STREAMS.csv`
     `c5c2df4c8e7d42ffe64804e371ecea125d08cee723b5249460f99e831aea03ef`
   - `BLOCKER_REGISTER.md`
     `9eccd494d7a93680ce644370150683c63e357c3c8bf202ed8291b429c29ce137`
   - `INPUT_HASHES.csv`
     `39e1d46cdeee605825b62254ea53c74287a05461818c3687c1388635b3b3ee25`
   - `RETURN.md`
     `535918255cf89f77419b7c466f471e7645f83322ada33b97f235c6d16947aed4`
   - `REVIEW.md`
     `fcb3d46415a2b5d851dac73653037c66ddb44cb7070dfbf5a091bd1a21616e1d`
   - self-excluding manifest `ARTIFACT_HASHES.csv`
     `7c4eb1478edb6aeea99886f87282806bd2634dd38b9aa811deae3a64746ecfaf`
4. Verify that `OWNER_ACCEPTANCE.md` does not yet exist in that directory.
5. Incorporate by reference (immutable path + SHA-256; do not transcribe):
   this steer and ruling record R10 at their `plans/steers/` paths, with the
   SHA-256 values recorded in the PR that published them.
6. If any check fails, stop and report. Do not repair, regenerate, or
   substitute.

## Authority context

R9-A accepted the exact sealed schedule-basis package and expressly withheld
transcription into governed state. R10-A authorizes exactly this tranche. The
form mirrors Phase-5 N1 (the R8 estimate-acceptance transcription at
`Evidence/ESTIMATE_SNAPSHOT_POST_PHASE3/OWNER_ACCEPTANCE.md`). This steer
grants the single addition below and nothing else: no schedule, calendar,
staffing, velocity, commitment, lifecycle, implementation, activation, pin,
hold-release, cutover, release, publication, reliance, or App authority, and
no blocker lift.

## N1 — the transcription

Write one new file
`execution/_ScopeChange/SCA-004_2026-08-22_1749/Evidence/SCHEDULE_BASIS_POST_PHASE4/OWNER_ACCEPTANCE.md`
recording:

- the acceptance date `2026-08-23`;
- the owner ruling record path
  `plans/steers/chirality_app_v3_root_ruling_record_r9_2026-08-23.md` and its
  SHA-256 `bc3a3bf414cfd64a5a650d633e942c2bb741a4562622857a79f5101c837e577b`;
- the accepted aggregate: 1,012 base effort-hours with a 560–1,464
  effort-hour deterministic uncertainty range across eight work streams;
  ordering derived solely from the eight accepted Root gating edges; the
  nineteen recorded blockers and exclusions remain open, held, or excluded
  grounding gaps outside the accepted envelope, priced at no effort;
- the seven exact accepted artifact identities, restated from the basis gate
  above;
- the sentence that acceptance creates schedule-basis truth only, followed by
  the negative grant restated from R9-A (no calendar, staffing, velocity,
  commitment, lifecycle, implementation, activation, pin, hold-release,
  cutover, release, publication, reliance, or App authority);
- the rerun condition: the package must be rebuilt and independently
  re-reviewed per its recorded rerun triggers after any change to a pinned
  input, and no act may rely on superseded bytes.

Modify no existing snapshot file — the accepted bytes are immutable; this is
an addition beside them. Add no claim that R9 did not rule.

## Post-write validation

- Run the loop's standard tranche validator suite as applicable to this
  change set, including candidate whitespace against the recorded basis
  commit and CI-form G4 (this tranche touches no instruction surface, so no
  covering manifest is expected — if G4 demands one, stop and report).
- Confirm with `git status`/diff that exactly the write set below changed and
  nothing else.

## Receipt and return

- Append Receipt 127 to `execution/_Coordination/LOOP_RECEIPTS.md` following
  the ledger's receipt contract, incorporating this steer and R10 by
  immutable path and SHA-256 and recording the added file's SHA-256.
- Record run evidence under
  `execution/_Coordination/AgentRuns/ROOT_R9_TRANSCRIPTION_2026-08-<DD>/`.
- Commit, push the branch, and open one unlabeled PR against `main`. Do not
  merge. The owner decides the merge separately.

## Write set, exactly

- The one new `OWNER_ACCEPTANCE.md` named in N1.
- One append to `execution/_Coordination/LOOP_RECEIPTS.md` (Receipt 127).
- New files strictly inside
  `execution/_Coordination/AgentRuns/ROOT_R9_TRANSCRIPTION_2026-08-<DD>/`.

Not selectable: every existing `execution/_ScopeChange/` snapshot file
(including all seven accepted schedule-basis artifacts and every other
SCA-004 artifact); `docs/CONTRACT.md` and every other root `docs/**` file;
the Root Task Management register; any SOW, `_CONTEXT.md`, `_STATUS.md`, or
lifecycle file; `agents/**`, `tools/**`, `AGENTS.md`, `exports/**`,
`plans/**`, `skills/**`, `runtime/**`; anything under `projects/**` or
`_DomainEngines/**`; any App-loop path.

## Sync rule

If `origin/main` advances mid-run, the standing routine-sync authorization
recorded in Receipt 125 permits one non-rewriting sync; record it, and stop
fail-closed if the sync changes any identity named in the basis gate.

## Rollback and abort

This tranche adds files only. Any validation failure, identity disagreement,
or unexpected write deletes the additions on the branch (or abandons the
branch), verifies that every pre-existing surface remains byte-identical to
the basis, and stops with a report. A stop-and-report is a compliant outcome
of this steer, not a failure.

## Discipline

Fail closed on every disagreement. Produce durable evidence for every claim.
Do not expand the write set for any reason; if the act appears to require a
write outside the set, stop and report — the owner decides. No authority is
inferred from this steer beyond the single transcription it names.
