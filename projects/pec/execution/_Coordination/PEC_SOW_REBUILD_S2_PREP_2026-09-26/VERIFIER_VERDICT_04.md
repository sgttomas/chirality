# VERIFIER_VERDICT_04: S2 Scope of Work rebuild packet (provisional D-PEC-100), PR #964, review target dafce6d7ee8c4bb98af341286658b80e44b439ea

Transcribed verbatim by WORKING_ITEMS from the final report of a fresh read-only `pec-reviewer` TASK (Opus 5.5, `claude-opus-5-5`, high reasoning; host-reported model; role instruction-asserted), 2026-09-26. This reviewer took no part in rounds 1–3. Dispositions follow the transcription and are the manager's.

---

**Verdict: PASS WITH NOTES.** Nothing blocks.

- **Diff since round 3:** no byte of `candidates/`, `quotes/` or `claims/` changed between `3be700545` and `dafce6d7e`.
- **Guard:** the new run-root guard is correct. I found no way to bypass it that could hide a write.
- **Test case 9:** it catches the failure it was written for. The new test file fails the old script (8/9) and passes the new one.
- **Pins:** TARGETS and PINNED match recomputed hashes at `2b5389a97` and at `aca930622`, and also at the newer remote `main` `121900105`.
- **Manifest:** `SHA256SUMS` verifies on an archive of the head.
- **Fault injection:** `RESULT PASS 9/9`.
- **Round-3 dispositions:** they hold in substance.
- **Notes:** four NON-BLOCKING findings on draft wording and one INFO.

**Reviewer.** Fresh read-only TASK (pec-reviewer). The host reports the model as Opus 5.5 (`claude-opus-5-5`); the role is instruction-asserted. I authored nothing and took no part in rounds 1–3.
- The worktree is untouched: `git status --short --ignored` on PREP is empty and no `__pycache__` exists.
- All Python ran with `PYTHONDONTWRITEBYTECODE=1`.
- Every write went under the session scratchpad. I deleted my exports (`base/`, `head/`, `mut/`). The scratchpad is shared, and my scratch scripts (`pins.py`, `probe.py`, `probe2.py`, `idshow.py`, `acver.py`, `scan.py`, `qa21.py`) may have overwritten same-named scratch files from earlier reviewers.

**Instructions read:**
- Root `AGENTS.md` `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd`
- `projects/pec/AGENTS.md` `df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8`
- `agents/AGENT_TASK.md` `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7`

**The branch moved during the review.**
- It was `dafce6d7e` when I started. The local and remote branch are now `2ed9806dfce61f9bcc42cc0850d612d8c57bdb8c` ("pec: S2P manager return").
- That commit adds only `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/S2P_SOW_REBUILD_PROPOSAL.md`. PREP is byte-identical: `git diff --quiet dafce6d7e 2ed9806df -- PREP` gives rc=0.
- I did not review that return file, apart from noting that its L126 says the drafter returns are not tracked.
- Remote `main` is now `121900105` (PR #966); see Finding 5.

## Findings

### 1. NON-BLOCKING: the changed-ID convention "unless noted" has unnoted exceptions

**Where:** draft L28 ("Where a requirement is listed, its matrix-linked `AC-*` and `VER-*` change with it unless noted").

Checked by matrix-row linkage in the postimages against `aca930622`. These linked criteria are byte-identical before and after:
- DEL-01-06 `REQ-001` → `AC-001` and `VER-001`;
- DEL-01-06 `REQ-005` → `AC-004` and `VER-004`;
- DEL-01-01 `REQ-009` → `VER-008` (`AC-008` did change).

None of these is noted. The list therefore claims changes that did not happen. That is the safer direction of error, but it is still inaccurate.

**Repair (draft only):** note these as exceptions, or soften the convention.

### 2. NON-BLOCKING: some kept IDs whose rule changed are still missing from the list

**Where:** draft L28–35, and L62 ("the kept IDs whose rule changed are listed under Method").

- **DEL-02-06.** The list names `VER-009` for adding "a normalized entrypoint and a full-length procedure SHA … guard-evasion encoding". The same new obligations appear in `REQ-009` (the entrypoint "shall be emitted as a normalized repository-relative path and the procedure SHA as a full-length digest"; no value "encoded, truncated, padded or relabelled to pass it") and in `AC-009`. Neither is listed.
- **Other candidates from a sampled reading** (I did not read every kept ID in full):
  - DEL-02-06 `REQ-007`, `AC-007` and `VER-007` add two limitation cases: a field that cannot be obtained, and no workplan declaration.
  - DEL-02-03 `REQ-010` and `VER-010` add a third change exercise: a declared profile's live or historical state flips.
  - DEL-02-03 `REQ-005` adds per-grammar availability and the live/historical label, which parallels the listed DEL-01-01 `REQ-008`.

L28 no longer says "complete", which is an improvement. L62 still implies completeness. Candidate validity is unaffected; this concerns only the accuracy of an owner-facing disclosure.

### 3. NON-BLOCKING: the QA 21 note overstates which verdicts checked the hand-resolution table

**Where:** draft L235 ("checked against the requirement text by verdicts 01–03").
- Verdict 01 (item 21) and verdict 02 (item 21) did check the table.
- Verdict 03 ran only the boundary tool ("validate, checklist and boundary: PASS ×7"). It did not check the hand-resolution table against the requirement text.
- **The substance holds.** I checked all 13 rows of the table myself (`qa21.py`). Each requirement names its owner. Each cited claim names that owner. Each requirement cites the claim, except DEL-02-06 `REQ-004`, which cites `CLM-012` as the table's parenthesis says.

**Repair:** "verdicts 01, 02 and 04", or "01 and 02".

### 4. NON-BLOCKING: the draft's binding failure semantics omit the new location precondition

**Where:** draft L186 (Preflight) and L188 (Write set).
- The bound script (`2e195590…190c`) now refuses at preflight when its directory lies inside `projects/pec` outside `projects/pec/execution/_Coordination/SOW_REBUILD_S2_*`.
- The draft's Preflight bullet does not list this refusal. The script docstring (L28–31) states it.
- It does not affect the drafted invocation (L181), which I confirmed is accepted (see the guard review below).

**Repair:** add one clause to L186.

### 5. INFO: remote `main` has moved past the draft's "checked at" commit

**Where:** draft L19.
- Remote `main` is now `121900105d93d9458a4680d7d4cfc37c93e6ca0c` (PR #966, first-parent child of `2b5389a97`).
- Its only change under `projects/pec` is `execution/_Coordination/NOTICE_2026-09-26_DEPENDENCY_FOLLOWUPS.md`. The notice is routed for the record; it says no PEC file changes and that the owner defers adoption.
- No TARGET, PIN or runner tool changed. I recomputed the pins at `121900105`: 7 targets and 23 pins, 0 mismatches.
- Claims and quotes are commit-anchored, so nothing is affected.
- Carry-forward: refresh L19 at the next re-render. The act's own preflight re-verifies the pins anyway.

## Guard review (brief item 2)

`apply_s2p.py` L116–117 and L163–170.
- `SELF_DIR = Path(__file__).resolve().parent` and `repo = Path(a.repo).resolve()`: both are resolved, so symlinks and a relative `--repo` are normalized.
- The refusal applies when the script's path relative to `repo` starts with `projects/pec/` but not with `RUN_ROOT_PREFIX`.
- The exclusion (L124–125) prunes only the directory whose resolved path equals `SELF_DIR`.

**Can a run root contain a target or pin?** No. Every TARGET is under `execution/PKG-0*`. The PINs are under `_Decomposition/`, `docs/`, `v2/config/`, `AGENTS.md` and `_Coordination/_DECISIONS/…`. None can lie under `_Coordination/SOW_REBUILD_S2_*`.

**Probes.** Run as subprocesses on fresh copies of a `git archive 2b5389a97 projects/pec` export, using the head's `apply_s2p.py` and candidates.

| Case | Layout | Result |
|---|---|---|
| L1 | Drafted invocation, `--check-only` (cwd repo, `…/SOW_REBUILD_S2_D-PEC-100/apply_s2p.py`, absolute `--repo`) | rc 0, pristine |
| L2 | Drafted invocation, apply | rc 0, applied |
| L3 | Relative `--repo .` | rc 0, applied |
| L4 | cwd = run root, `--repo ../../../../..` | rc 0, applied |
| L5 | Script outside the repository, relative `--repo` | rc 0, applied |
| B1 | Script in the PREP folder inside the repository | rc 1, pristine, refused by the guard |
| B3 | `SOW_REBUILD_S2_L` is a symlink to `projects/pec/tools/x` | rc 1, refused (resolves to `tools/x`) |
| B4 | Real run root invoked through a symlink elsewhere | rc 0 (resolves to the run root; correct) |
| B9 | Nested under a run-root-named directory | rc 0 (the exclusion covers only that nested directory) |
| B2 | Script in `projects/pec` itself | Guard not triggered, because `rel_self == "projects/pec"` has no trailing slash |
| B5–B7 | Miscased paths on case-insensitive APFS | Guard not triggered |

**Fail-closed check for the gaps (`probe2.py`).** For B2, B5–B7 and a miscased legitimate run root, I wrote files into the script's own directory during the act. Every case gave rc 1 with `write set differs from grant: added=[…]` and rolled back.
- `Path.resolve()` does not canonicalize case, and the base directory is never pruned.
- So in each gap the exclusion also fails to match, and nothing is hidden. The invariant "the exclusion can only ever cover a run root" holds.
- The docstring's "anywhere other than a run root … preflight refuses" is literally untrue for B2 and B5–B7. It is harmless, because those layouts exclude nothing.

**Case 9.**
- It copies the script to `projects/pec/tools/x` and requires rc 1 with the targets pristine. Its output shows exactly one FAIL line, the guard line.
- It does not assert the message text, but the other preflight inputs are the same as in cases 7 and 8, which pass.
- **Mutation check:** the head `test_apply_s2p.py` run against the round-3 script (`f820e581…74e4e5`, no guard) gives `FAIL bound copy inside projects/pec but outside a run root` and `RESULT FAIL 8/9`, rc 1. Case 9 therefore detects the missing guard.

`run_s2p_checks.sh` L33–35 runs the PREP copy against an export outside the repository (`rel_self` is None), so the runner is unaffected.

## Disposition backcheck (brief item 3)

**Changed-ID list: verified true.** I compared every item below at `aca930622` with the postimage, 12 items and more:
- DEL-01-01 `AC-005`
- DEL-01-06 `REQ-001` and `REQ-005` ("version-1" becomes schema version 2)
- DEL-02-03 `AC-011`, `CON-002` and `TBD-003`
- DEL-02-04 `REQ-001`
- DEL-02-05 `CON-004`
- DEL-02-06 `OUT-001`, `REQ-003`, `TBD-003` and `VER-009`
- DEL-02-07 `REQ-004`, `AC-001`, `VER-001`, `AC-006` and `VER-006`

Each changed as the draft describes. Exceptions and omissions are in Findings 1 and 2.

**Partiality note (L28): verified.** I read the rebuild-provenance AX entries in the candidates.
- DEL-02-03 `AX-015`, DEL-01-06 `AX-012` and DEL-02-04 `AX-012` name none of the listed changes. DEL-02-04's entry lists categories only.
- DEL-01-01 `AX-011` names some; it omits `AC-005`.
- DEL-02-06 `AX-014` names some; it omits `OUT-001`, `REQ-001`, `REQ-003`, `TBD-003` and `VER-009`.
- DEL-02-05 `AX-013` names its only listed item, `CON-004`.
- DEL-02-07 `AX-014` names all of its listed items.

**Consequence bullet (L97): verified** against `evidence/run_main/scan_external_quotes.out` (`SUMMARY stale=31 kept=32`).
- The set of contracts with STALE lines is exactly the fifteen named.
- Its examples match the scan: DEL-03-01 quotes DEL-01-06 "version-1" and the prior DEL-02-03/02-04 text; DEL-04-05 `CLM-011` (L137 at `2b5389a97`) quotes DEL-02-03 `REQ-001`; DEL-10-10 quotes DEL-02-05.
- DEL-02-08 `CLM-008` and DEL-02-09 `CLM-007` cite `43f1f57a13bb…0170`.
- DEL-02-01 `REQ-002` still names DEL-02-07 as the feed-manifest supplier.
- All fifteen `_STATUS.md` read `INITIALIZED` at `2b5389a97`.

**QA 21 note (L235):** see Finding 3.

**Drafter returns: no remaining evidentiary reliance.**
- The draft's remaining "drafter" mentions are L38 (the rules, citing the tracked brief `ab7fdc29…43fd`), L39 (actors) and L352 (attribution).
- "Confirmed by the drafters" and "drafter returns; the verifier re-checks" are gone.

## Commands (exit codes and result lines)

1. **Diff since round 3.**
   - `git diff --quiet 3be700545 dafce6d7e -- PREP/candidates PREP/quotes PREP/claims`: rc 0.
   - `git diff --name-status 3be700545 dafce6d7e -- PREP` lists what changed:
     - M: `DRAFT_D-PEC-100_s2_sow_rebuild_proposal.md`, `SHA256SUMS`, `apply_s2p.py`, `test_apply_s2p.py`, and `evidence/run_main/{SUMMARY,apply,containment,receipts_post,receipts_pre,test_apply_s2p}.out`
     - A: `VERIFIER_VERDICT_03.md`
   - The evidence changes are the new closing-line wording, case 9 and new export paths only.
   - `git diff --check 3be700545 dafce6d7e`: rc 0.
2. **Pin recomputation.** `pins.py` at `2b5389a97` and `aca930622`: "targets 7 pins 23 mismatches 0" for each, and "candidates vs postimage mismatches 0", rc 0. At `121900105`: 0 mismatches.
3. **Manifest.** `git archive dafce6d7e PREP | tar -x`, then `shasum -a 256 -c SHA256SUMS`: rc 0, 86 lines, 0 not OK. `diff` of the `SHA256SUMS` paths against `git ls-files PREP` minus `SHA256SUMS`: rc 0 (identical).
4. **Fault injection.** `git archive 2b5389a97 projects/pec | tar -x` (178 MB), then `test_apply_s2p.py <export> <head PREP>/candidates`: `RESULT PASS 9/9`, rc 0.
5. **Mutation check.** Head test against the round-3 script: `RESULT FAIL 8/9`, rc 1 (case 9 fails as intended).
6. **Guard probes.** `probe.py` (L1–L5, B1–B9) and `probe2.py`: results as tabled above.
7. **ID comparisons.** `idshow.py`, `acver.py` (matrix-linked AC/VER), `scan.py` (difflib screen) and `qa21.py`.
8. **Remote heads.** `git ls-remote`: branch `2ed9806df…`, main `121900105…`. `origin/main` (local ref `2b5389a97`) is an ancestor of HEAD.
9. **Not run:** the full `run_s2p_checks.sh` (optional; disk is tight at 22 GB free). Round 3 ran it at the same basis, and since then only the `apply` and `test` outputs changed. I reran both paths (items 4 and 6).

## Hashes relied on

**Draft and scripts (at `dafce6d7e`):**
- Draft `730f043224b2448a7816bcd26c5cc21c021707f8ac9a828bfd0f727477bf9384`
- `apply_s2p.py` `2e1955902bed16884f4628683594f475863c804d0585766e6ba1a75ea1bf190c` (equals draft L178)
- `test_apply_s2p.py` `d8f2b4220fea24a4252d708f7be16482d285fbcc65cdf8f83dfa9861943ec61c` (equals draft L195)
- `SHA256SUMS` `a30d61ad50403d0f029d9da0f9ef0b6155c6a5094d71dff87ab28c167ed0c6d2`
- `VERIFIER_VERDICT_03.md` `31ea00eb4e0d5bc8317452c2f0ebf1d90765641af8c46ef854af35177c19354f`
- `run_s2p_checks.sh` `6b2845d91b53de8089c1986b3e72cffbac064ff418c908fb4d24939289a5b8e7`
- Round-3 script (mutation baseline) `f820e5818b94a95fafe72829a3fc22e4f318a0e3c8c4a87290df5ec61074e4e5`

**Postimages:** unchanged, and equal to TARGETS and SHA256SUMS: `14be02f5…8b88`, `2053fb65…177e`, `c8bb9f1b…294b`, `18183769…37b1`, `0b2d5714…fd92`, `53d99682…2928`, `3d122087…18fb`.

**Commits:**
- Review target `dafce6d7ee8c4bb98af341286658b80e44b439ea`
- Current branch head `2ed9806dfce61f9bcc42cc0850d612d8c57bdb8c`
- `origin/main` (local) `2b5389a970847850ea05762ca9ca35ac9fbaacb4`
- Remote main `121900105d93d9458a4680d7d4cfc37c93e6ca0c`
- Drafting base `aca930622ba167689881416044ba0feaee3ef003`

---

## Manager dispositions (WORKING_ITEMS, 2026-09-26)

Draft wording only, plus the routine re-render; no candidate, claim, quote or act-script byte changes except the act script's pin comment naming the new `origin/main` (script rebound).

1. **Repaired.** The convention now says the linked `AC-*`/`VER-*` usually change, and names the exceptions found (DEL-01-06 `AC-001`/`VER-001`, `AC-004`/`VER-004`; DEL-01-01 `VER-008`).
2. **Repaired.** Added DEL-02-06 `REQ-007`/`AC-007`/`VER-007` and `REQ-009`/`AC-009`/`VER-009`, and DEL-02-03 `REQ-005` and `REQ-010`/`VER-010`. The list now calls itself the principal list from verdicts 02–04 (verdict 04 sampled), not a guarantee of exhaustiveness, and the lead-in to "What each rebuild changes" says "principal".
3. **Repaired.** The QA 21 note now cites verdicts 01, 02 and 04.
4. **Repaired.** The Preflight bullet now includes the run-root location precondition.
5. **Repaired.** `origin/main` `121900105` (PR #966, one routed notice, no PEC file change) is merged into the branch; the draft's source state names it; the full runner was rerun there.

These repairs were not re-reviewed by a fifth verifier; they change owner-facing wording and the pin comment only, as listed.
