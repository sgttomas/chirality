# VERIFIER_VERDICT_01 — D-PEC-106 X1 act (P1 parser fixture suites, add-on L)

- **Verifier role:** TASK (Type 2). Fresh, read-only, independent. I authored nothing in this change and repaired nothing.
- **Model, as the host reports it:** Opus 5.5 (`claude-opus-5-5`).
- **Date:** 2026-09-27. Last check at 17:57 UTC.
- **Repository and worktree:** `sgttomas/chirality`, at `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d106-act`, branch `claude/pec-d106-x1-fixtures-act`.
- **Head reviewed:** `f4ab6c307e812f872498a7cbfbccc8448443610b`. Base `origin/main` is `c5d852c4a95a478f34d9e4e4375d603e08245e25`; it is the merge-base, and `git ls-remote` shows the remote `main` still at that commit. PR #1008.
- **Skill applied:** `.agents/skills/software-code-review/SKILL.md`, SHA-256 `ee085d589c44f912d11a59eead8edac214f0343761d26b0d33e886a979888bca`, recomputed at head and at base.
- **Scratch directory (TMPDIR):** `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/x1verify.RQNTEW`. It has been removed.
- **Instructions read:** `agents/AGENT_TASK.md`, root `AGENTS.md`, `projects/pec/AGENTS.md`, the ruling and the proposal (all of it).

## Verdict: **PASS WITH NOTES**

Nothing blocks. The 35 written files match their tabled postimages byte for byte. Containment is exact. Add-on L's bytes are exact, and L was committed before the act. The ruled FX-PEC-0 holds, and nothing scans for the retired sections. The registered checks pass when I rerun them, and they write nothing. The three notes below are about how the evidence is recorded. None concerns a product byte.

## Findings (most severe first)

**1. NON-BLOCKING — the row-9 evidence file is mislabelled, and no clean row-9 run is recorded.**
- **Where:** `projects/pec/execution/_Coordination/X1_FIXTURES_2026-09-27/evidence/row9_diff_check_first_attempt.out`, added in `f4ab6c307`.
- **What the file actually holds:** the *second* `git diff --check` run, at `17:46:34 UTC` with `HEAD f657822b2`. That run flagged the trailing whitespace inside the then-committed `row9_diff_check.out`.
- **Where the real first attempt is:** it ran at `17:46:19 UTC` with HEAD at `7ff6eb7bb` and exited 2. It flagged `row1_basis.out:30` and `row1a_addon_L.out:24,29,41,46,57,62`. It was committed as `row9_diff_check.out` in `f657822b2` and deleted at `f4ab6c307`. It now exists only at `f657822b2:.../evidence/row9_diff_check.out`.
- **Consequences:**
  - The brief's description ("the first row-9 output is kept as …first_attempt.out") does not match the bytes.
  - No passing row-9 output exists in the tree at head. My own run at head is clean (below), so row 9 passes today, but the run root does not show it.
- **Remediation:**
  - Rename the retained file or describe it accurately, for example as the second attempt.
  - Cite the first attempt by `f657822b2:<path>`, or restore it with its whitespace marked.
  - Capture a final clean `git diff --check origin/main...HEAD` at the final candidate head, and record both failed attempts in `VALIDATION.md`.

**2. NON-BLOCKING — captured outputs were normalized after commit. The change is whitespace-only, but it alters the captured diff text.**
- **Where:** `evidence/row1_basis.out` (raw bytes at `2886540c0`) and `evidence/row1a_addon_L.out` (raw bytes at `3f1e1a4d7`), both rewritten in `f657822b2`.
- **Whitespace-only:** confirmed. `git diff -w --exit-code 2886540c0 f4ab6c307 -- …/row1_basis.out` exits 0, and `git diff -w --exit-code 3f1e1a4d7 f4ab6c307 -- …/row1a_addon_L.out` exits 0.
- **Why it matters anyway:** in `row1a_addon_L.out` the edit turns the captured unified-diff context lines `" "` (a blank context line) into `""`. The retained text is therefore no longer a byte-faithful capture of `git diff` output, and it no longer applies as a patch.
- **Remediation:** have `MANIFEST.md` and `VALIDATION.md` name `2886540c0` and `3f1e1a4d7` as the raw captures and state the edit.

**3. NON-BLOCKING — in `row1_basis.out`, the last recorded command does not match its output.**
- **Where:** `evidence/row1_basis.out`, final line. The raw capture at `2886540c0` has the same mismatch.
- **What is wrong:** the recorded command is `git log --oneline -1 --format='%H %s' c5d852c4a`. Its output line has the merge's two parent SHAs (`16010b4ca9ab…`, `0a7a4bdd162f…`) appended. I reran that exact command and it does not print them.
- **Impact on the basis:** none. The parents are correct: `git log -1 --format=%P c5d852c4a` gives the same two SHAs. But the evidence does not record the command that produced the output.
- **Remediation:** record the exact composite command in `VALIDATION.md`.

## Items 1–9: what I checked and how

**Item 1 — Basis. PASS.**
- **Ruling, proposal and register row at `c5d852c4a`:**
  - Ruling `5161630b…96fe` and proposal `677b59f6…d279`, recomputed from `git show c5d852c4a:<path> | shasum -a 256` and from the worktree.
  - The `_REGISTER.md` row for `D-PEC-106` is at line 123: `RULED A / FX-PEC-0 AND THRESHOLDS CONFIRMED / L / M / EFFECTIVE ON MERGE`.
- **Act script:** the run-root `apply_x1p.py` hashes to `452ff66a…2428`, the same as the prep-folder copy.
- **Run root equals the prep folder:**
  - `cmp` of all 45 non-evidence run-root files (the bound script, template, builder, aids and 35 candidates) against `PEC_X1_FIXTURES_PREP_2026-09-26/` found 0 differences.
  - The prep folder's `shasum -a 256 -c SHA256SUMS` exits 0.
  - The prep folder is unchanged in this diff.
- **Act pins:** all 12 `PINNED` hashes in `apply_x1p.py` match at both `c5d852c4a` and `f4ab6c307` (12/12 each, by Python over `git show`).
- **Manifest pins:** `report_x1p_pins.py <worktree> f4ab6c307 …/pinned/MANIFEST.json` gives `RESULT PASS 19/19` (exit 0). `FX-PEC-0.graph` shows path drift (`changed d35e1a31c`). That is informational only, because the pin is by blob.

**Item 2 — Byte identity. PASS.**
- **Postimages:** I parsed the proposal's grant table (lines 208–242, 35 rows). Every path's SHA-256 at `git show f4ab6c307:` and in the worktree equals its tabled postimage (0 mismatches).
- **The one modify:** `software-workflow.json` preimage at base is `8ec9ba6d…8a8b`; postimage is `d55fff77…0bbd`.
- **Nothing extra:** `git ls-tree -r` of `v2/tests/parsers` holds exactly the 34 tabled creates, and nothing else is on disk, ignored files included.
- **Registry change:** the `software-workflow.json` diff adds only the `v2-parsers` check and its path rule.

**Item 3 — Test and fixture review (software-code-review). PASS.**
- **Sample checked:** I dumped all 65 golden expectations and all 24 synthetic cases.
- **Fixed tier:** I spot-checked these `fixed` expectations against the three `ScopeOfWork.md` files, whose hashes match the act pins:
  - DEL-02-08 AC-005: `F1` is `ACTIVE`, and FC-1/2/3 have no completion claim. Lines 35/31/27 of the three graph blobs.
  - DEL-02-08 AC-006 and REQ-006: identity against folder. FC-1 is equal; FC-2 and FC-3 differ.
  - DEL-02-08 REQ-010: FC-3 `F1 — final PR` has an em-dash suffix.
  - DEL-02-03 AC-017 with VER-016: the FC-1 Receipt-ID comes from the cursor field. VER-016 requires the cursor-field identity to be asserted, which justifies `fixed`.
  - DEL-02-03 REQ-014 and AC-015: `EVIDENCE.md` is not a receipt.
  - DEL-02-03 REQ-015, AC-016 and CLM-018: registry surfaces and labels `receipt-ledger`/`central-receipts`, `historical`/`live`.
  - DEL-02-09 AC-004 with CON-004: headings `h3`, `h16`, `h82` and `h109` of the DEL-01-03 `MEMORY.md` blob (`497bb0042`) carry only decision IDs, prose and parenthesized tokens. The anchor lines are correct.
  - DEL-02-09 REQ-001 and AC-001: FC-2 dated-heading anchors 157/211/123/431 are correct.
- **Observed tier:** every `observed` value is an as-cited token. None fixes a representation. `none`, the full SHAs as cited and the dates as cited leave DEL-02-03 TBD-007 and DEL-02-08 TBD-007 open.
- **Grounding, content-minimality, bindings:** the rerun suite's grounding, content-minimality and binding tests pass.
- **No TBD or CON pre-empted:** no synthetic `expect` pre-empts one. For example, SYN-MEM-06 `dated_heading_run_token_emitted: false` sits on headings that carry only prose, `D-SYN-9601` and `(ZEBRA_PAREN_0603)`, which is AC-004's case.
- **Copied text:** I ran my own 8-word scan (net of the two templates) of the 27 synthetic `.md` files against all 16,735 tracked `.md` files. Outside PEC's own X1 prep and run-root copies it found 0 overlapping files.
- **Git helper:** read-only.
  - It has one `subprocess.run`, allowlisted to `version`, `cat-file`, `ls-tree`, `rev-parse`, `merge-base` and `config --get`.
  - It sets `GIT_NO_LAZY_FETCH`, `GIT_NO_REPLACE_OBJECTS`, `GIT_TERMINAL_PROMPT=0` and `GIT_OPTIONAL_LOCKS=0`.
  - It fails closed on Git older than 2.44, on a shallow clone and on `extensions.partialclone`. The class flag is set only after the check passes, so a failed check fails every later test.
- **Negative controls:** I reran them independently in my TMPDIR against `f4ab6c307`: `zsh …/negative_controls_x1p.sh <worktree> f4ab6c307 <run root>` gives `RESULT PASS 20/20` (exit 0). This includes the old-Git shim, partial-clone and shallow cases.

**Item 4 — FX-PEC-0 as ruled; no parser code; no scanning. PASS.**
- **What FX-PEC-0 pins:** the manifest pins the registry, the ledger, the undertaking graph and two `MEMORY.md` files at `6c6cc1b00`. It pins no `_STATUS.md` and nothing from the retirement undertaking.
- **No retired sections:** `grep -rni remaining projects/pec/v2/tests/parsers/` exits 1 (no match). The same grep over the run-root aids and evidence scripts (`*.py`, `*.sh`, `pre_act_checks.cmd`) and over the brief copy also finds nothing.
- **No parser code:** the diff has no `v2/src/**` path.

**Item 5 — Containment and lifecycle. PASS.**
- **Paths:** `git diff --name-status c5d852c4a...f4ab6c307` shows 143 entries:
  - the 34 `A` under `v2/tests/parsers/`;
  - `M software-workflow.json`;
  - three `M _STATUS.md` (DEL-02-03, DEL-02-08, DEL-02-09);
  - `A` of the brief copy;
  - 104 `A` under `X1_FIXTURES_2026-09-27/`.
- **No forbidden paths:** a grep for `v2/src/`, `MEMORY.md`, `ScopeOfWork.md`, `_REGISTER.md`, `Dependencies.csv`, `_DEPENDENCIES.md` and `docs/` exits 1 (no match).
- **Scope validator:** `tools/software_workflow/validate_change_scope.py <worktree> --base c5d852c4a --head f4ab6c307 --allowed <those roots>` exits 0.
- **Whitespace:** `git diff --check c5d852c4a...f4ab6c307` exits 0.

**Item 6 — Add-on L bytes. PASS.**
- **Preimages at base:** `6f94c04f…cf06f`, `4341d6b2…04fe`, `e67be587…1056`.
- **Postimages:** `84b238d2…9b5e`, `bfc99586…1ff6`, `50bc10f4…372a`.
- **Exact change:** I built each expected postimage from its base preimage: state line to `IN_PROGRESS`, `**Last Updated:** 2026-09-27`, and the exact tabled history line appended at the end. All three equal the head bytes exactly. The unified diffs show no other changed byte.

**Item 7 — Ordering. PASS.**
- **Commit order:** `2886540c0` (row 1 evidence) → `3f1e1a4d7` (L: only the three `_STATUS.md` and three L evidence files) → `26b27b2b0` (act: 34 A, 1 M, and the two row-2 outputs).
- **L commit is clean:** `3f1e1a4d7` contains no `v2/tests/parsers` file and no `software-workflow.json`.
- **Act evidence:** `row2_apply.out` records `HEAD 3f1e1a4d7… (add-on L committed)`, the bound hash, `CHECK targets 35/35 byte-exact; write set = grant (34 created, 1 modified, 0 removed …); pinned 12/12 unchanged` and `exit=0`.
- **Row 1 predates the L commit:**
  - `row1_basis.out`: 17:36:07 UTC.
  - Preimages and dependencies: 17:36:53 UTC. The 10/10 named dependency rows are ACTIVE and PENDING. `write_status.sh` is `0bf835f5…ece3`.
  - Hold preflight: 17:37:07 UTC, with `SUMMARY dispatch-for-production: ALLOW exit 0 on 41 of 41 targets`.
  - Check-only: 17:37:17 UTC, `CHECK preflight passed`.
  - All were committed in `2886540c0`.
  - L then ran at 17:42:19 UTC and was committed at 17:42:45 UTC. The act's check-only ran at 17:43:07 UTC and the act itself at 17:43:15 UTC.

**Item 8 — Registered checks, rerun independently. PASS.**
- **Setup:** `export TMPDIR=<mine>; export PYTHONDONTWRITEBYTECODE=1`, cwd `projects/pec`, Python 3.13.7 at `/Library/Frameworks/Python.framework/Versions/3.13/bin/python3`, git 2.54.0. The clone is not shallow and has no `extensions.partialclone`.
- **Fixture suite:** `python3 -m unittest discover -s v2/tests/parsers -p 'test_*.py' -v` ran 10 tests, all OK, exit 0.
- **Posture:** `python3 v2/tools/check_service_core_posture.py --config v2/config/service_core_posture.json --workflow software-workflow.json` returns verdict PASS, exit 0. `core_tree_sha256` is `dd7e1dda…6e5a` (unchanged) and `workflow_sha256` is `d55fff77…0bbd`.
- **No writes:** `git -C <worktree> status --short --ignored` shows 0 lines both before and after every command I ran.
- **Hold preflight for my own review:** `pec_reliance_hold.py --operation candidate-validation` returns ALLOW with exit 0 on 38/38 targets (the 35 act paths and the three `_STATUS.md`). The register is `f877d931…1cbc` and the script `b1712e4b…cd0e`.

**Item 9 — Evidence handling. ACCEPTABLE, with notes 1–3.**
- **Why acceptable:** the normalization is whitespace-only (verified with `-w`), and the raw bytes are recoverable at `2886540c0`, `3f1e1a4d7` and `f657822b2`.
- **Conditions:** the run-root records must cite those commits and state the edit, correct the "first attempt" label (finding 1), and add a final clean row-9 capture.

## Residual risk (carried, not findings)

- **FX-PEC-0 expectations and the run-index declaration.** The `fixed` expectations on DEL-01-06 and DEL-01-03 presuppose that PEC's registry declares the run-index surface. DEL-02-09 TBD-003 and CON-002 do not yet rely on that declaration. This was disclosed in the proposal and confirmed by the owner under question 2. Carry it to the parser packets.
- **Hosted CI.** It does not run the v2 Python checks, so a future hosted job needs full history (F-5/X-2).
- **AST guard.** The guard is a guard, not a proof; its known gaps were disclosed in preparation.
- **Open fan-in preflight.** Row 1's `rely-for-production` preflight before fan-in is not yet in the evidence. It is due at WORKING_ITEMS fan-in.
- **Suitability.** The act is suitable for manager fan-in once findings 1–3 are dispositioned. No acceptance, readiness, release or reliance claim is made, and nothing here prompts about CHECKING.

## Write confirmation

- I wrote nothing outside my TMPDIR.
- The worktree's `git status --short --ignored` was empty before and after my work, and its HEAD is unchanged at `f4ab6c307`.
- My TMPDIR was removed with `rm -rf`, and `ls` confirmed it no longer exists.
- The negative-control scratch repositories were created and removed inside that TMPDIR.
- My only network access was a read-only `git ls-remote`.

---

## WORKING_ITEMS dispositions (appended; the verdict above is transcribed verbatim from the verifier's hand-back)

| Finding | Disposition |
|---|---|
| 1 (row-9 label; no clean row-9 capture) | Repaired. The misnamed file is renamed `evidence/row9_diff_check_attempt2.out` (it is the second attempt, at `f657822b2`). The true first attempt is restored from `f657822b2:…/evidence/row9_diff_check.out` as `evidence/row9_diff_check_attempt1.out`, with each trailing-whitespace run replaced by a visible marker. A final clean `evidence/row9_diff_check.out` is captured at the final candidate head. `VALIDATION.md` records both failed attempts and their cause. |
| 2 (whitespace normalization after commit) | Accepted and recorded. `MANIFEST.md` and `VALIDATION.md` name `2886540c0` (`row1_basis.out`) and `3f1e1a4d7` (`row1a_addon_L.out`) as the raw captures, give both before and after hashes, and state that only trailing whitespace was removed, so the captured diff text in `row1a_addon_L.out` is no longer patch-applicable. The postimage hashes and the slot check (`row1a_addon_L_slots.out`) are the binding L evidence. |
| 3 (composite command in `row1_basis.out`) | Recorded. `VALIDATION.md` states that the last line of `row1_basis.out` was produced by `git log -1 --format='%H %s %P' c5d852c4a` (the echoed label omitted `%P`). The evidence file is not rewritten. |
| Residual: fan-in preflight | Done before fan-in: `evidence/fanin_hold_rely_for_production.out`. |
