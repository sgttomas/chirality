# Run Record R6 — Managed-Delegation Concurrent-Reservation Deflake

- **Deliverable:** DEL-08-04 Type-2 Subagent Governance Bridge
- **Date:** 2026-07-22
- **Agent:** Agent 2 bounded specialist (chirality-app-dev loop), sealed brief
- **Adopted-brief basis:** APPDEV-MANAGED-DELEGATION-DEFLAKE
  (`execution/_Coordination/AgentRuns/AGENT-INDEX-REDISPOSITION-20260721/notices/APPDEV-MANAGED-DELEGATION-DEFLAKE-BRIEF.md`),
  itself the sealed brief issued by HELP_HUMAN run `AGENT-INDEX-REDISPOSITION-20260721`
  (LOOP_RECEIPTS Receipts 29–31).
- **Lifecycle:** no change. `_STATUS.md` state remains IN_PROGRESS; the single
  `## Remaining` item (D-APP-53 Option-C-gated per-attempt decision-replay
  artifact) is unrelated to this work and is left untouched.

## Objective

Make the concurrent write-target reservation path in
`frontend/src/lib/harness/managed-delegation.ts` deterministic so the test
`atomically reserves concurrent sibling write targets` never flakes, and so
genuinely disjoint concurrent siblings are never spuriously rejected. No change
to reservation semantics (what overlaps, what is refused).

## Diagnosis confirmation (re-verified against live source 2026-07-22)

Confirmed the brief's diagnosis against the current file:

- `STATUS.json` was created creation-exclusively with `writeNew` (`flag: 'wx'`,
  status `LAUNCHED`) and then **overwritten in place** with a plain `writeFile`
  (status `RUNNING`) at the two adjacent lines inside `withRunLaunchLock`.
  Plain `writeFile` truncates before writing, so mid-transition the file is
  observably empty/partial.
- Two further in-place `writeFile` overwrites of the same `STATUS.json` occur
  in the post-launch block — the terminal-status write and the failure-path
  write — and **both run outside `withRunLaunchLock`**. This is the decisive
  window: a concurrent sibling `delegate` holding the launch lock runs
  `assertNoActiveWriteOverlap`, which reads every sibling `STATUS.json`; if it
  reads one mid-truncate, `JSON.parse` throws and the fail-closed catch raises
  `Cannot prove write disjointness because sibling <id> has an invalid status
  record` instead of the intended `Concurrent write overlap` (or instead of a
  legitimate success for a disjoint sibling).
- The harness fails closed in all interleavings, so this is an availability /
  determinism defect (valid concurrent work refused, flaky assertion), not a
  safety hole. Diagnosis matches the brief exactly.

## Fix applied

1. **Atomic status replacement.** Added a single `writeAtomic(filePath, content)`
   helper (kept inline in `managed-delegation.ts`, no new module, to bound the
   diff): it writes content to a uniquely-named temp file
   (`.STATUS.json.<uuid>.tmp`) in the **same directory** with `flag: 'wx'`, then
   `rename(2)`s it over the target. `rename` is atomic on POSIX, so any
   concurrent reader observes either the complete prior contents or the complete
   new contents — never a torn/empty record. On any failure the temp file is
   removed and the error re-thrown. `rename` was added to the `node:fs/promises`
   import.
2. **Routed all three in-place `STATUS.json` overwrites through the helper:**
   the `RUNNING` transition (previously the plain-`writeFile` immediately after
   the exclusive `LAUNCHED` create), the terminal-status write, and the
   failure-path write.
3. **Initial creation left creation-exclusive.** The first write
   (`LAUNCHED` via `writeNew` with `flag: 'wx'`) is unchanged. Rationale: the
   exclusive create is the cheap uniqueness guard on the per-instance directory
   and never races a sibling scan (it executes while this `delegate` holds the
   launch lock, and sibling scans are serialized behind that same lock). Making
   it atomic would add no safety and would remove the create-exclusive guard, so
   it stays as-is; only the overwrites — which can run concurrently with sibling
   scans — were converted to atomic replacement.

### Scan-side posture decision: keep fail-closed (no bounded retry)

`assertNoActiveWriteOverlap` retains its current fail-closed posture for a
sibling whose `STATUS.json` cannot be read/parsed. Rationale:

- Atomic replacement alone fully closes the observed failure mode. `STATUS.json`
  is created (`LAUNCHED`) and transitioned to `RUNNING` entirely inside
  `withRunLaunchLock`; sibling scans acquire the same lock, so no scanner ever
  runs during an instance's creation window. The only writes that overlap a
  sibling scan are the post-launch overwrites, and those are now atomic renames
  over an already-existing file — the file is never absent and never partial
  from a scanner's viewpoint.
- With the torn-read eliminated there is no legitimate transient
  absent/partial state left to tolerate, so a bounded retry would only mask
  genuine corruption. Fail-closed remains the correct, safest posture and
  requires no semantic change. (The brief explicitly rates fail-closed
  acceptable and notes atomic writes alone close the race.)

## Test hardening

- Kept the strict `Concurrent write overlap` assertion in
  `atomically reserves concurrent sibling write targets` unchanged (overlapping
  `execution/PKG-02` vs `execution/PKG-02/nested`: exactly one fulfilled, one
  rejected, rejection reason contains `Concurrent write overlap`).
- Added the complementary case `lets concurrent siblings with genuinely
  disjoint write targets both succeed`: two siblings on `execution/PKG-02` and
  `execution/PKG-03` launched concurrently must **both** be fulfilled and there
  must be **zero** rejections. No assertion was widened to accept the "invalid
  status record" message.

## Verification evidence

Environment: macOS (Darwin 25.5.0), Node/vitest v2.1.9, project
`projects/chirality-app-dev/frontend`. `npm install` was run once to link the
`@chirality/harness-contract` workspace package before testing.

- **Single run** of `managed-delegation.test.ts`: 15 passed (14 prior + new
  disjoint-siblings case).
- **Stress — full file ×300 consecutive:**
  `for i in $(seq 1 300); do npx vitest run src/__tests__/lib/managed-delegation.test.ts --reporter=dot || break; done`
  → 300 / 300 green, 0 failures. (The new disjoint-siblings case and the strict
  overlap case are both in the file, so both are exercised on every iteration.)
- **Full frontend suite:** `npx vitest run` → 780 passed, 4 skipped
  (98 files passed, 1 skipped). Exit 0.
- **Typecheck:** `npm run typecheck`
  (`tsc --noEmit` + `tsc -p tsconfig.electron.json --noEmit`) → exit 0.
- **`git diff --check`:** clean.

## Changed files

- `projects/chirality-app-dev/frontend/src/lib/harness/managed-delegation.ts`
  (atomic `writeAtomic` helper; `rename` import; three `STATUS.json` overwrites
  routed through it)
- `projects/chirality-app-dev/frontend/src/__tests__/lib/managed-delegation.test.ts`
  (added disjoint-siblings-both-succeed case)

No shared fs-helper module was added; the helper is inline to keep the diff
bounded to the harness lib and its test, per the brief's write scope.

## Deviations from the brief

None. Reservation semantics unchanged; write scope respected; no git/receipt/
completion-log/_STATUS.md lifecycle changes (handled by the parent loop).
