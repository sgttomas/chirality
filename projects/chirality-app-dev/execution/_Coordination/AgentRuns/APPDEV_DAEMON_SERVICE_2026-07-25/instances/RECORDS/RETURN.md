# RECORDS — RETURN (records stage)

**Run:** TRB-APPDEV-DAEMON-SERVICE-2026-07-25 · **Agent 2 (opus)** · branch
`feat/daemon-service`, records written on top of `45aeaa465`
**Authority:** `../../ADOPTED_BRIEF.md` (incl. `## Corrections`) ·
**Launch brief:** `LAUNCH_BRIEF.md` (verbatim, copied before any other act)
**Status:** COMPLETE. Three commits, not pushed. No frontend, electron, runtime,
`package.json`, or `README.md` file touched; no stage RETURN or ROUND review file
modified; lockfile untouched.

---

## 1. Commits

| # | SHA | Subject |
|---|---|---|
| 1 | `d9c8971f9cdd1aeba237132e7a37dd71b3647ca5` | `docs(app-dev): daemon-service tranche closeout records` |
| 2 | `dd01d7b9d6d9a4a0411ef55b88a572178add721c` | `docs(app-dev): append Receipt-91 — daemon-service tranche executed` |
| 3 | (this file) | `docs(app-dev): RECORDS stage return` |

Commit 1 carries the four DEL run records and `_STATUS.md` updates, the
completion-log entry, the run `HANDOFF_STATE.md`, and this instance's
`LAUNCH_BRIEF.md`. Commit 2 is the receipt alone, as directed. Commit 3 exists
only because this return has to cite the two SHAs above.

## 2. Deliverables touched

| DEL | Run record | Remaining effect |
|---|---|---|
| DEL-02-01 | `_run_records/R7_DAEMON_SERVICE_2026-07-25.md` | 3 closed, 1 retained, 3 added |
| DEL-02-05 | `_run_records/R6_DAEMON_SERVICE_2026-07-25.md` | unchanged (gated item untouched) |
| DEL-05-04 | `_run_records/R2_DAEMON_SERVICE_2026-07-25.md` | amended only; both items stay open |
| DEL-09-04 | `_run_records/R6_DAEMON_SERVICE_2026-07-25.md` | 1 narrowed, 1 preserved, 6 added |

All four keep their lifecycle state, `Authorization Basis`, `Directive`, and
`Checking Approval SHA`; each got a `## History` line and `Last Updated`
2026-07-25 (history insertion follows each file's own ordering — newest-first for
DEL-02-01, DEL-02-05, DEL-09-04; oldest-first for DEL-05-04).

**Brief-assumption correction:** the runtime-connectivity-dot residual is
**DEL-02-01**, not DEL-05-04 — DEL-02-01 carried all three of the residuals this
tranche was raised against (packaged smoke evidence, connectivity indicator,
`.icns` cross-referenced to DEL-09-04). DEL-05-04's residual is the replay
transcript-item rendering item, which is adjacent but different.

### DEL-02-01 — closed

1. Packaged Desktop smoke evidence for the redesigned shell — closed on
   window-scoped frames of the packed app (`v3-window-connected.png`,
   `v0-window-disconnected.png`, `v5-window-*`): logo tile, wordmark, `RUNTIME
   connected` chip, navigator groups, coordination projection, activity shelf,
   legacy affordance, plus observed connectivity transitions and an end-to-end
   stub-adapter turn.
2. True runtime-connectivity indicator — closed (supervisor + IPC + chip,
   transitions observed on the packed app).
3. `.icns` packaged application icon — closed (`CFBundleIconFile` = `icon.icns`,
   packaged icns byte-identical to committed, quincunx verified in extracted
   reps, Dock and Finder captures).

Retained: the `metadata.icons` record-only note.

### DEL-02-01 — added

1. No operator reconnect affordance on the connectivity chip.
2. Cross-reference to the DEL-09-04-owned Finder/Dock daemon-resolution bounce.
3. Cross-reference to the DEL-02-02 / DEL-08-02 packaged-evidence items still
   owed (deliberately **not** closed: the packaged frames show the Dialogue
   surface only, and no recorded sessions existed in the isolated user data, so
   neither the Workbench/Pipeline surfaces nor the navigator selection path was
   exercised). Those two `_STATUS.md` files were not edited.

### DEL-09-04 — narrowed + added

- Item 1 narrowed, not deleted: the headless daemon, LaunchAgent, and bundled CLI
  are evidenced on the packed app, so what survives is the login-time `RunAtLoad`
  path (never exercised — the drill plist lived outside `~/Library/LaunchAgents`)
  and the still-gated DMG/dist scope. The `(gated: G5 packaging; no release
  authority)` suffix is preserved on the surviving part; F-APP-2 restated.
- R4-P49 release-preparation item preserved verbatim.
- Added: (a) daemon helper-bundle identity, owner-escalated; (b) SIGKILL stale
  control socket; (c) unsatisfied premerge row for this branch; (d) post-merge
  owner-machine deployment (decision gate 3); (e) packaged-daemon instruction-root
  divergence, pre-existing.

Residual (b) was verified in source before wording, per instruction:
`RuntimeDaemon.start()` calls `recoverStaleSocket()`
(`runtime/packages/daemon/src/runtime-daemon.ts`), which unlinks the socket and
owner record **only** when the path is a socket owned by this uid and the recorded
owner pid is demonstrably absent, and otherwise refuses (`FORBIDDEN` /
`RESIDENCY_TRANSITION_IN_PROGRESS`) rather than replacing a live or ambiguous
owner. Recorded as mechanism, not as observation-only.

Residual (c) was homed on DEL-09-04 with cross-references to DEL-09-01 (Section 8
contract) and DEL-09-05 (CI workflow) rather than editing those two files.

## 3. Receipt-91

Appended to `loop/LOOP_RECEIPTS.md`: 9 records, body 3,676 of 4,096 bytes,
`Parent-Receipt` `Receipt-90`, `Gate-Outcome` `EXECUTED`, all five owner
directions transcribed verbatim under the required
`CHAT_TRANSCRIPTION — EVIDENCE, NOT RULING` label.

Validator, run before and after the append:

```
$ python3 tools/validation/validate_app_dev_loop_receipts.py --repo-root .
VALID …/projects/chirality-app-dev/loop/LOOP_RECEIPTS.md: frozen through
Receipt-52; versioned receipt contract satisfied            (exit 0)
```

**Two grammar decisions Agent 0 must know about.**

1. **`Examined-Through` deviates from the launch brief.** The brief directed the
   post-records-commit HEAD; the ledger's fixed rule 7 defines
   `Examined-Through` as *"the full commit SHA examined at the end of Step 0
   before mutation"*, and Receipt-90 followed that reading exactly (it recorded
   `403f228f4`, the parent tranche's merge commit and its branch base, not a
   branch head). The brief's own wording was also self-contradictory ("the HEAD
   your records commit will sit on top of" = `45aeaa465`, versus "rev-parse HEAD
   after your content commits" = `d9c8971f9`). I followed the grammar and
   recorded `e9068c87d76c75b133f3686db8bf453565ce8fa2` (this session's Step-0
   tree, `main` at the PR #330 merge), and put the branch range
   `8c20f214d`…`d9c8971f9` in `Pointers` so the records commit is still
   reachable from the receipt. Both candidates satisfy the validator (it only
   requires ancestry of the validation commit), so if Agent 0 prefers the other
   reading the fix is a one-line amend of commit `dd01d7b9d` before pushing.
2. **There is no PR field in the grammar.** Receipt-90 carried `PR #330` inside
   `Pointers`, which is free-form, so no separate convention exists for pre-PR
   receipts. Receipt-91's `Pointers` therefore ends with "PR pending, opened by
   Agent 0 immediately after this receipt". **Action for Agent 0:** the ledger is
   append-only, so once the PR number exists either amend commit `dd01d7b9d`
   in place (nothing is pushed yet — cheapest, keeps one receipt) or leave the
   pending pointer as the durable record. Do **not** append a second receipt just
   to carry the number.

## 4. Corpus reconciliation

`reconcile_authority_corpus.py status` → **no drift**, at corpus `v17`, before
and after the record edits. No governed authority document was edited by this
stage, so no bump/apply flow was owed or run.

**One follow-on flagged, not performed:** `docs/PRD.md` KG-033 still lists the
runtime-connectivity indicator and the packaged application icon among its
narrowed residuals; both are now closed. Editing the PRD triggers D-APP-38
reconciliation (bump + apply across deliverable reference rows), which was
outside this stage's scope and outside its instruction. It is recorded in the
receipt's `Stale-Map-Delta`, in `HANDOFF_STATE.md`, and here. Agent 0's call
whether to fold it into this PR or take it separately.

## 5. Other checks

- `python3 tools/practitioner_harness/harness.py self-check` → **exit 0**
  (unchanged baseline: the standing review/warning findings lie outside this
  tranche's paths).
- `git diff --cached --check` → clean on both content commits.
- `git status --short` → clean after commit 2; no `package-lock.json` change at
  any point.
- Write containment: every path written is under
  `projects/chirality-app-dev/{execution,plans,loop}/`.
- Frontend gates were not re-run: this stage changed only records. The
  authoritative gate figures are Agent 1's round-2 table
  (`../AGENT1-VALIDATOR/ROUND2_REVIEW.md` §3).

## 6. Notes of record

- The records deliberately carry the **corrections**, not the originally accepted
  claims: brief root cause #2 → C-1 (a wrong restart contract blind to a clean
  exit, not a missing plist key), and `ROUND1_REVIEW.md` §3 → its appended
  retraction (the JS SIGTERM handler never runs in a packaged Electron main
  process). Both are cited in the DEL records, the completion-log entry, the
  handoff state, and the receipt's `Stale-Map-Delta`.
- `HANDOFF_STATE.md` names the accepted upstream basis as the **round-2 tree**
  and marks round-1 measurements as superseded where round 2 re-measured them.
- The self-introduced round-2 defect (a fork that broke the daemon's own stop
  path) is recorded in the DEL-09-04 run record as a note of record rather than
  omitted.
