# Review 01 of PR #1008, transcribed

- **Reviewer:** a fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high) dispatched by HELP_HUMAN. It authored nothing in the PR. Its final report is transcribed from the host subagent transcript (verbatim apart from any disclosed whitespace normalization).
- **Reviewed head:** `0e9c4c83d200cb4ab4216b94e5216b8a86fd7109`. The repairs listed under Disposition, this file and a merge of `origin/main` follow that head.
- **SHA-256 of the report text below (UTF-8; the report text between the blank line after "## Report (verbatim)" and the blank line before the final "## Disposition", with no trailing newline):** `025b5ae9f6c3df285f8fb19757cf00da59bd9d58f9e11b8f305687d5ee2cb061`.

## Report (verbatim)

## Review of PR #1008 (D-PEC-106 act), head 0e9c4c83d200cb4ab4216b94e5216b8a86fd7109

**Verdict: PASS WITH NOTES.** Nothing blocks. I found three non-blocking findings (all about record accuracy or staleness) and a few notes. No product byte, ordering, containment or check result is wrong.

I made no edits and no git writes, and I did not check out anything. All work ran on `git archive` exports in `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/rev1008.l4c4ko`, each with a scratch-local `.git` that borrows the repository's objects through alternates. `TMPDIR` and `PYTHONDONTWRITEBYTECODE=1` were set in every shell.

**Base moved during the review.** `origin/main` went from `0adfbc747` to `8bbd022b9` (PR #1011). That PR changes 10 files, all under `projects/chirality-app-v4/`, and nothing under `projects/pec`.

### Findings

**NON-BLOCKING 1: a second fixture-pin path drift came in with the merge and no record discloses it.**
- The merge `0040299f6` brought in PR #1009. That PR changed the current bytes at the path of pin `FC-3.memory.DEL-05-04`: `projects/chirality-app-dev/.../DEL-05-04_Runtime_Replay_and_Transcript_View/MEMORY.md` now holds blob `1176cb5c2`, while the pin is `4d1e8a96b` at `d61981ee2`.
- The run root's own evidence shows it: `X1_FIXTURES_2026-09-27/evidence/rerun_after_merge_0adfbc747/pins.out` prints `changed 1176cb5c2`. My runs of `report_x1p_pins.py` at the head and at `origin/main` show it too.
- It does no harm. The pin is by blob, so pins stay 19/19 and the suite passes; the proposal (line 152) treats path drift as informational.
- The records never mention it:
  - `VALIDATION.md:22` names only the FX-PEC-0.graph drift.
  - The rerun section `VALIDATION.md:39-45` omits it.
  - HANDOFF_STATE, the return and verdict 02 omit it (verdict 02 reran pins at the merged head).
- The brief asks for a report "if a pinned file changed". **Fix:** add one line to `VALIDATION.md` (rerun section) and to the graph X1 row.

**NON-BLOCKING 2: STATUS and the graph have lines this act made stale.**
- `projects/pec/docs/STATUS.md:298` still lists "P1 fixtures;" as an open item. The same list marks finished items "done:", and line 283 now says the X1 act is "Done".
- `WORK_GRAPH.md:168` still reads "Local or unmerged work: this ruling PR; …". In this PR that phrase no longer describes a ruling PR (#1006 has merged), and it omits PR #1008 itself.
- `WORK_GRAPH.md:169`: the "Handed back" list omits the X1A manager and its return `returns/X1A_D106_FIXTURES_ACT.md`.
- `WORK_GRAPH.md:159`: the checked basis `16010b4ca` is older than the act's base. This one was already stale before the PR; noted only.

**NON-BLOCKING 3: verdict 02 calls itself "Fresh", but it comes from the same reviewer as verdict 01.**
- `VERIFIER_VERDICT_02.md:3` says "Fresh, read-only, independent".
- Line 60 says "`VERIFIER_VERDICT_01.md` reproduces my hand-back", and line 11 says the text was also sent by SendMessage. It is therefore a backcheck by the verdict-01 reviewer, not a fresh instance.
- It is still independent of the author and applies `software-code-review` (`ee085d58…8bca`). The brief's one required fresh verifier is verdict 01, which meets that requirement.
- `VALIDATION.md:49` describes 02 correctly as a "Backcheck". Only the self-description is off.

**NOTES**
- `WORK_GRAPH.md:246` (the D-PEC-88 trace) lists only the "README.md census". It does not record the README `IN_PROGRESS` sentence that `0e9c4c83d` added.
- `README.md:25` still says "present-current as of 2026-09-26", while its census now reads 2026-09-27.
- `STATUS.md:287-290` says the D-PEC-98 act left "both deliverables `INITIALIZED`". That is historically true, but it now sits beside their `IN_PROGRESS` state and could be misread. Optional wording change.
- `VALIDATION.md:21` says check-only ran "from the run root". The evidence shows cwd was the repository root, with the script in the run root. Wording only.
- I could not independently confirm that the `/var/folders` scratch file was removed. I did not look outside my scratch directory. The disclosure is consistent and nothing entered the repository.

### Verification by item

**1. Product writes: PASS.**
- All 35 postimages match the proposal's grant table (lines 208-242) exactly.
- `v2/tests/parsers` holds exactly 34 files and nothing extra.
- `software-workflow.json` goes from `8ec9ba6d…8a8b` to `d55fff77…0bbd`. The diff adds only the `v2-parsers` check and its path rule.
- The three `_STATUS.md` files:
  - Preimages at `origin/main` match the table.
  - I rebuilt each postimage from its preimage using the slot rule with {D}=2026-09-27 (state line, `Last Updated` line, one history line). All three equal the head bytes: `84b238d2…9b5e`, `bfc99586…1ff6`, `50bc10f4…372a`.
- No `v2/src/**` path and no `MEMORY.md` in the diff.

**2. Order: PASS.**
- Commit chain: `2886540c0` (row 1, parent `c5d852c4a`, which contains the ruling; `b23d0276b` is an ancestor) → `3f1e1a4d7` (only L and its evidence) → `26b27b2b0` (the act).
- Evidence times (UTC, 2026-09-27):

| Step | Time | Result |
|---|---|---|
| Basis | 17:36:07 | as recorded |
| Preimages, dependencies (10/10 ACTIVE PENDING) | 17:36:53 | `write_status.sh` `0bf835f5…ece3` |
| `dispatch-for-production` | 17:37:07 | ALLOW 41/41 |
| Check-only; pins | 17:37:17 | pins 19/19 |
| Add-on L run | 17:42:19 | at HEAD `2886540c0`; commit at 11:42:45 local |
| Act | 17:43:15 | exit 0 at HEAD `3f1e1a4d7`, 35/35, write set = grant, 12/12 pinned |
| `rely-for-production` | 18:01:07 | ALLOW 41/41, after verdict 01 finished (17:57) and before its fan-in commit `c9d0aa40c` |

**3. Reproduced at the head: PASS.**
- `v2-parsers`: 10 tests OK.
- `run_registered_checks.py` on the six affected checks: all exit 0.
- `select_affected_checks.py` selects the same six.
- Posture: PASS, `core_tree_sha256` `dd7e1dda…6e5a`.
- Bindings `RESULT PASS 442/442`; pins `RESULT PASS 19/19`.
- Strict registers (exit 1, 0 errors, 26 `XRG-013`), harness (exit 0) and receipts (exit 0) are byte-identical to `origin/main` `8bbd022b9` after normalizing the root path.
- `run_x1p_checks.sh` against current `origin/main` `8bbd022b9`: OVERALL PASS (act, containment, six checks, 10 tests, 442/442, 19/19, 67/67, identical before and after, hygiene, fault injection 11/11, negative controls 20/20).
- `grep -rni remaining` over `v2/tests/parsers` and the run-root `*.py`, `*.sh` and `*.cmd` files finds nothing, so there is no retired-section scanning.

**4. Verifiers: PASS, with NON-BLOCKING 3.**
- Every disposition checks out:
  - the row-9 attempt files are relabelled, attempt 1 is restored with markers, and a final clean `row9_diff_check.out` exists at `38757b1e0`;
  - the composite `%P` command is recorded;
  - the final row 7 and 8 captures exist;
  - the "HEAD inferred" wording is in place.

**5. Run root: PASS.**
- `SHA256SUMS`: 150/150 OK, and it covers every file exactly (no file missing, none extra).
- `apply_x1p.py` is `452ff66a…2428`. The candidates and the nine aids are byte-identical to the prep folder, and the prep folder's `SHA256SUMS` passes (112/112).
- Whitespace-stripped captures:
  - `row1_basis.out`: raw `86476cb8…5b3a` at `2886540c0`, now `4bc0e8ce…8a89`;
  - `row1a_addon_L.out`: raw `eebeb32c…5925` at `3f1e1a4d7`, now `7597dafa…0906`;
  - the diffs show only trailing whitespace removed;
  - `row1a_addon_L_slots.out` is unchanged (`8e49e75e…632d`).
- The brief copy is `8cde96bf…b81a`, byte-identical.
- MANIFEST, VALIDATION and HANDOFF_STATE are otherwise truthful.

**6. Merge from main: PASS, with NON-BLOCKING 1.**
- `0040299f6` has parents `c9d0aa40c` and `0adfbc747`. It leaves `projects/pec` unchanged, and outside PEC its tree equals `0adfbc747`.
- No pin or act pin moved.
- Current `origin/main` `8bbd022b9` merges cleanly and touches no X1 input.

**7. HELP_HUMAN records: PASS, with NON-BLOCKING 2 and the notes.**
- I recounted all 68 deliverable `_STATUS.md` files: 28 OPEN / 27 INITIALIZED / 4 CHECKING / 5 IN_PROGRESS (DEL-01-03, DEL-01-05, DEL-02-03, DEL-02-08, DEL-02-09) / 4 RETIRED. This matches STATUS:127-136 and README:52-57.
- STATUS X1 done text (lines 280-287) gives test module + pinned manifest + four goldens + synthetic set = 34. This matches the register row (synthetic manifest plus 27 files).
- Graph X1 row (line 68): ACTIVE in PR #1008, and its claims are accurate.
- The Order line (90) and Next-work line (162) are updated.

**8. Containment, whitespace and CI: PASS.**
- The diff against `origin/main` has 194 paths, all within the allowed set: the 34 fixtures, `software-workflow.json`, the three `_STATUS.md`, the run root, the brief, the return, the graph, STATUS and README.
- `git diff --check origin/main...HEAD` is clean (exit 0). The two-dot form flags only App-v4 lines from PR #1011, which are not PR content.
- CI at `0e9c4c83d`: every check passed or was skipped (`harness`, `pec`, `PEC workspace tests`, `Harness pre-merge`, `Desktop E2E (source mode)` and the three selectors passed). PR state OPEN, MERGEABLE, `mergeStateStatus` CLEAN.
- Hosted CI does not run `v2-parsers`; this is a disclosed residual.

Nothing here prompts about CHECKING.

## Disposition (HELP_HUMAN)

Verdict PASS WITH NOTES; nothing blocking. Dispositions:

- **NB-1 (a second pin path drift was not recorded): repaired.** A dated line added to `VALIDATION.md`'s rerun section records the drift. At `0adfbc747`, the path of pin `FC-3.memory.DEL-05-04` holds blob `1176cb5c2`, while the pin is `4d1e8a96b`. The pin is by blob, so 19/19 still holds. The run-root `SHA256SUMS` entry is regenerated, and all entries pass. The graph's X1 row names both path drifts. A note appended to the X1A return gives the new `VALIDATION.md` and `SHA256SUMS` hashes.
- **NB-2 (stale STATUS and graph lines): repaired.**
  - STATUS marks P1 fixtures done.
  - The graph now has the checked basis `8bbd022b9` with PR #1006, the unmerged-work line lists PRs #1008, #1010 and #1007, and the active-operations line names the handed-back X1A, S1A and D1A managers.
- **NB-3 (verdict 02 calls itself "Fresh"): recorded.** Verdict 02 is the verdict-01 reviewer's backcheck. `VALIDATION.md` already calls it one, and the graph row says so. The verdict's bytes stay bound.
- **Notes:**
  - **D-PEC-88 trace:** repaired. It now names the README `IN_PROGRESS` sentence.
  - **README date:** repaired. The present-current date now reads 2026-09-27.
  - **STATUS D-PEC-98 sentence:** repaired. It now reads "then `INITIALIZED` (now `IN_PROGRESS` under `D-PEC-106`)".
  - **`VALIDATION.md` check-only wording:** repaired to "script in the run root, cwd the repository root".
  - **The `/var/folders` removal:** it stays as the manager disclosed it.
- **Reviewer footprint:** HELP_HUMAN removed the reviewer's scratch directory.

The repair head needs a fresh review before merge.
