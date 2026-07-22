# Sealed Brief — App Dev tranche: deflake managed-delegation concurrent-reservation race

Issued by: HELP_HUMAN, run `AGENT-INDEX-REDISPOSITION-20260721` (post-closeout addendum)
Recorded at: LOOP_RECEIPTS.md Receipts 29–31; companion notice
`APPDEV-ORCHESTRATOR-RENAME-HANDOFF.md`
Owner: the App Dev project loop (WORKING_ITEMS tranche on the deliverable owning
the managed-delegation runtime). This brief is a ready-to-execute package; the
App Dev loop adopts, amends, or declines it under its own authority.

## Objective

Make the concurrent write-target reservation path deterministic so
`frontend/src/__tests__/lib/managed-delegation.test.ts > managed delegation >
atomically reserves concurrent sibling write targets` never flakes, and so
legitimately disjoint concurrent siblings are never spuriously rejected.

## Diagnosis summary (verified against source, 2026-07-22)

- Observed CI failure (twice recorded, e.g. root PR #304 run 29893947930):
  expected rejection `Concurrent write overlap` arrived instead as
  `Cannot prove write disjointness because sibling <id> has an invalid status
  record`. 5/5 local reruns pass; the window only opens under CI-load timing.
- Root cause, `frontend/src/lib/harness/managed-delegation.ts`:
  - L624 creates `instances/<id>/STATUS.json` with `writeNew` (`flag: 'wx'`,
    status `LAUNCHED`), then L625 immediately **overwrites the same path** with
    a plain `writeFile` (status `RUNNING`). Plain `writeFile` truncates before
    writing, so the file is observably empty/partial mid-transition. Later
    status transitions (L662, L667) use the same in-place overwrite pattern.
  - `assertNoActiveWriteOverlap` (L382–420) scans every sibling's STATUS.json;
    any read/parse failure falls into a catch-all that fails closed with the
    "invalid status record" message (L411–418).
- Consequence beyond test noise: two siblings with genuinely DISJOINT write
  targets can hit the same window, and the second is spuriously rejected —
  an availability defect (valid concurrent work refused), not just a flaky
  assertion. The harness fails closed in all interleavings, so there is no
  safety hole.

## Suspected fix pattern (for the tranche to confirm)

1. **Atomic status replacement:** route every STATUS.json write through a
   single helper that writes to a temp file in the same directory and
   `rename(2)`s over the target (rename is atomic on POSIX). Applies to the
   L625/L662/L667 in-place overwrites; the initial `writeNew` may remain
   creation-exclusive or adopt the same helper with an existence guard.
2. **Scan-side tolerance decision (secondary, judgment):** decide whether a
   sibling directory with a still-absent STATUS.json (created-but-not-yet-
   populated) should be treated as fail-closed (current behavior, acceptable)
   or bounded-retried inside the existing `withRunLaunchLock` window. Atomic
   writes alone close the observed failure mode; document whichever posture
   is chosen.
3. **Test hardening:** keep the strict `Concurrent write overlap` assertion
   (deterministic after fix 1). Add the missing complementary case: two
   siblings with disjoint write targets launched concurrently must BOTH
   succeed. Do not paper over the race by widening the assertion to accept
   the "invalid status record" message.

## Stress-verification acceptance criteria

- `managed-delegation.test.ts` passes ≥300 consecutive iterations locally
  (e.g. loop `npx vitest run` or a vitest `repeats` harness), including runs
  under artificial CPU constraint (`taskset`/`cpulimit` or CI-class runner)
  to widen scheduler jitter.
- The new disjoint-siblings-both-succeed case passes the same stress regime.
- Full frontend suite green; no new fs-layer behavior change observable
  outside the atomic-write helper (diff bounded to the harness lib + tests).
- Evidence recorded in the App Dev tranche's run record and receipt: iteration
  counts, environment, and the before/after failure reproduction (a pre-fix
  stress run demonstrating at least one reproduction is desirable but not
  mandatory if CI history is cited).

## Sequencing note

This deflake is the prerequisite that makes the recorded hardening follow-on
(strict branch protection requiring `Harness pre-merge` plus an always-run
no-op reporting job) livable: a flaky required check is a merge blocker. Land
the deflake first; then the root loop can revisit strict protection.

## Constraints

- Write scope: `frontend/src/lib/harness/managed-delegation.ts`, its tests,
  and any small shared fs-helper module the App Dev loop deems proper — under
  the App Dev loop's own receipts and checks. No root-surface writes.
- No behavior change to reservation SEMANTICS (what overlaps, what is
  refused) without a separate App Dev decision; this brief covers only
  determinism of the existing semantics.
