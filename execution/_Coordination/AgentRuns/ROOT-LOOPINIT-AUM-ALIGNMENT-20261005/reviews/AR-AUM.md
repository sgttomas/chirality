# AR review: PR #1094 (App v4 reading sentence; Agent User Manual alignment; Piping entry pointers)

**Reviewer.** AR, a Type 2 TASK dispatched by HELP_HUMAN (ROOT) for run `ROOT-LOOPINIT-AUM-ALIGNMENT-20261005`, under `RUN2/BRIEF_AR.md`. Claude Code subagent, Claude Opus 5.5 (`claude-opus-5-5`). I wrote none of the reviewed text. I made no Git writes and did not delegate.

**Candidate.** PR #1094, branch `codex/root-loopinit-aum-alignment-20261005`, head `4c286de23f5ef1bb683c58a0577b098e6e01f588`. It has 17 changed paths against main `87661be164`. At review time the PR was open, a draft and MERGEABLE, and main was still `87661be164`. Every hosted check on the head had passed or been skipped by coverage selection, including `harness`.

**Placeholders.** `WT` is the T3 worktree root. `RUN2` is `WT/aum-pr/execution/_Coordination/AgentRuns/ROOT-LOOPINIT-AUM-ALIGNMENT-20261005`. `NUM` is `WT/numerics`. `P` is `projects/chirality-piping`. `V4` is `projects/chirality-app-v4`. `AUM` is `docs/alignment-manual/CHIRALITY_AGENT_USER_MANUAL_v3.md`. Logs are in `WT/scratch/ar_aum_01/`.

## Verdict: REPAIR

| Severity | Count |
|---|---|
| BLOCKING | 0 |
| MAJOR | 1 |
| MINOR | 0 |
| NOTE | 5 |

The Markdown edits, the re-render, the pointer edits, the carried piping records and the gates are all correct. The one MAJOR finding is narrow: the App v4 notice, ruling 8 and the manifest rationale name App v4's pins of LOOP_INIT. They leave out that the same product resources also pin the AUM Markdown and `docs/alignment-manual/README.md`, which this tranche also changes. The repair is a few sentences across three records. No AUM or instruction bytes need to change.

## Findings

### MAJOR-1: the App v4 notice omits four of the seven App v4 pins that this tranche moves

**Evidence.** I compared each hash pinned in V4's product resources with main and with the head:

| Resource (`V4/app/src-tauri/resources/…`) | Pinned source | Previous sha256 | In the notice? |
|---|---|---|---|
| `instructions/SOURCE_MAP.json` l.103 (`loop`) | `V4/loop/LOOP_INIT.md` | `45c23cf4…` | yes |
| `policy_standing/basis.json` l.20 | `V4/loop/LOOP_INIT.md` | `45c23cf4…` | yes |
| `policy_standing/a16/basis.json` l.14 | `V4/loop/LOOP_INIT.md` | `45c23cf4…` | yes |
| `instructions/SOURCE_MAP.json` l.110 (`manual_index`) | `docs/alignment-manual/README.md` | `31217d30…` | **no** |
| `policy_standing/basis.json` l.32 | `docs/alignment-manual/README.md` | `31217d30…` | **no** |
| `instructions/SOURCE_MAP.json` l.124 (`user_manual`) | AUM | `08ca0e40…` | **no** |
| `policy_standing/basis.json` l.40 | AUM | `08ca0e40…` | **no** |

Each of these previous hashes equals main's bytes, and this PR changes all three sources. Their new hashes are `c2e88f81…`, `e5d23a6e…` and `1ba63acd…`. `a16/basis.json` pins neither the AUM nor the README.
- **The notice.** `V4/execution/_Coordination/NOTICE_2026-10-05_ROOT_LOOP_INIT_READING_SENTENCE.md`, "What it affects in App v4", lists only the LOOP_INIT pins and says "The recorded basis is now one revision behind". It mentions the AUM update but not that App v4 pins it.
- **RULINGS ruling 8** names only "the previous LOOP_INIT's sha256".
- **The manifest's `m6_notice.rationale`** gives "The Agent User Manual is shared guidance; it amends no loop's instructions, so no other loop needs a notice". That reasoning does not test pins. Root `AGENTS.md` requires notice to "each affected project loop whose authority corpus or contract mirrors pin changed instructions", and App v4's resources pin the AUM and its README.
- **AM's survey** (`AUM_EDITS.md` §2) searched only for the LOOP_INIT hash, so the gap began there.

What is true:
- The disposition (routed to App v4) is right.
- No other loop pins the changed bytes. I searched for every changed file's main hash. Outside App v4, only historical AgentRuns and reconciliation records and the public export manifest contain one (see NOTE-4).
- The notice's claim that no test or source compares these hashes also holds for the AUM and README pins. Only `SOURCE_MAP.json`'s directory is compiled in (`runtime_session.rs`, via `include_bytes!` of the instruction files, not the map), and `tests/policy_standing.rs` reads other fixtures.

**Why MAJOR.** The notice is the governed instrument that the receiving loop relies on to decide re-pinning. As written, App v4 could re-pin `loop` and leave `user_manual` and `manual_index`, and the two README/AUM rows in `basis.json`, one revision behind without knowing it.

**Fix.**
1. **The notice.** Add to "What it affects in App v4": the same tranche changes two other sources that these resources pin. The first is the AUM Markdown (previous sha256 `08ca0e40cd5157574a011bac57d539e77e9007a0d46494785da8b92745391b1a`; `SOURCE_MAP.json` entry `user_manual`; `policy_standing/basis.json`). The second is `docs/alignment-manual/README.md` (previous sha256 `31217d30b0d2743bef0d7c1a54bb9a81814d56b24ff0961cf01d9532952e305f`; `SOURCE_MAP.json` entry `manual_index`; `policy_standing/basis.json`). `a16/basis.json` pins neither, and no test or source compares them. Optionally, adjust the title or opening so that the notice covers the manual change as well as the sentence.
2. **Ruling 8.** Name the AUM and README pins alongside LOOP_INIT's.
3. **The manifest rationale.** Say that App v4's resources also pin the manual and its README, and that the routed notice covers them. Keep "no other loop needs a notice", which is true.

### NOTE-1: ruling 4's premise for E17 is inaccurate; the edit itself is right

`AUM_EDITS.md` E17 says "The App build guide now records Node `>=22.19.0`". Ruling 4 says "The guide now records `>=22.19.0`, so the note would be false at the new basis." But `projects/chirality-app-dev/docs/BUILD_AND_RELEASE.md` line 33 already read "Node engine: `>=22.19.0`;" at the previous render basis `1cb9fd536e` and at the AUM's original basis `b3e2ce4`. Commit `a89b5ddecf` (2026-09-22) removed `>=20`. So the "stale at this basis" note had been false since it was written (`233b0abcd2`, the same day).

E17 is correct and minimal, and the E1 clause about it is true. Only the recorded rationale is off. A corrected premise also narrows the distinction from ruling 5 (PEC): both correct statements that were already inaccurate. The remaining difference is that E17's sentence explicitly asserts "at this basis", and PEC needs a broader PEC-scoped pass. That distinction is defensible.

**Fix (optional, records only).** Reword ruling 4's premise ("The guide has recorded `>=22.19.0` since 2026-09-22, so the note was already false and would be re-asserted at the new basis"). ROOT should confirm that the ruling stands on that premise.

### NOTE-2: B1/B2 and E8 assign the "standing constraints" to different files

B1 and B2 (`P/README.md`, `P/docs/README.md`) say "`AGENTS.md` holds the standing constraints". E8 (AUM line 601) says Piping's `loop/LOOP_INIT.md` "holds its entry reading, record pointers, conventions and standing constraints". Piping's LOOP_INIT does have a "Standing constraints" section, the stage gate. Project `AGENTS.md` says "This file holds Piping-specific constraints", and the Root launcher says it "holds its fences".

Both statements are defensible in Piping's vocabulary ("Standing constraints — fences"), and a reader is sent to LOOP_INIT in any case, so there is no behavioural risk. B1–B3 were drafted and reviewed in run `PIPING-LOOP-INIT-20261005`.

**Fix (optional).** In B1 and B2, say "`AGENTS.md` holds the project constraints and fences".

### NOTE-3: contributor guide row 8 keeps "the pointer" without a referent

Row 8 now reads "`loop/LOOP_INIT.md`, the work graph the human's steering selects, and `_COORDINATION.md` … the pointer does not expand scope or lift holds." "The pointer" meant LOOP_INIT's selected-graph pointer, which no longer exists. The clause is still true on any reading.

**Fix (optional).** Write "these sources do not expand scope or lift holds", or leave it.

Also observed, no action needed: the banner of `P/execution/_Coordination/NEXT_INSTANCE_PROMPT.md` still says "The current session entry is … → the newest `loop/WORKPLAN_*.md`". It is a historical record marked on 2026-07-10, and the Root launcher calls it "a historical map". `P/docs/AGENTIC_DEVELOPMENT_WORKFLOW.md` line 51 is disclaimed by its own banner, as LR noted.

### NOTE-4: the public export manifest is now behind on three more rows

`exports/chirality-app/export-manifest.csv` records hashes for the AUM Markdown, the AUM HTML and `docs/alignment-manual/README.md`, and this PR changes all three. Main was already behind on `workflows/construct-local-work-graph/WORKFLOW.md` and `workflows/index.json`, from #1093. No test compares the committed manifest with the tree; `tools/validation/test_public_export_profile.py` builds a fresh stage. Earlier manual tranches regenerated the export in the same PR (`9111fcf933`, `aa37eaa006`); #1093 did not. I did not run the exporter, which my brief does not permit.

**Fix (optional).** Regenerate the export in this PR, or leave it for the next export. ROOT's choice.

### NOTE-5: the AUM's PEC statements remain untrue at the new render basis (ruling 5, recorded)

This confirms ruling 5 and adds nothing new. PEC's loop adopted `construct-local-work-graph` and the single `RECEIPT.md` in `11be801130` (2026-09-25). That predates the previous render basis `1cb9fd536e`, so these changes did not cause the inaccuracy. The manifest records the deferral. The HTML now re-asserts lines 62, 74, 106, 667, 684 and 690 at `87661be164`, as it did at `1cb9fd536e`. Ruling 5 is sound because the owner named Piping's and App v4's changes. A PEC-scoped revision should follow.

## Checks by priority

### 1. App v4's LOOP_INIT
- **Exactly one sentence changed.** The diff against main is one line. Lines 32–33 now read "…Record what you read in the run evidence. If you are unsure whether a section matters, read it." This matches the owner's direction and Piping's sentence in #1092, and nothing else changed. Main's file hash is `45c23cf4…` and the head's is `c2e88f81…`.
- **The notice.** Every statement it makes is true:
  - the three pinned hashes and their locations;
  - "No test or source compares these hashes", checked over `V4/app` sources and tests, `tools/`, `.github/` and the repository (`git grep`);
  - the owner-record path;
  - "the owner's guidance on LOOP_INIT intends", supported by `V4/…/APP-V4-GRAPH-CLOSURE-20261004/OWNER_DECISIONS.md` ("the agent decides when to visit it");
  - "Piping's LOOP_INIT took the same binding form, with this sentence, in PR #1092".

  It is incomplete; see MAJOR-1.
- **No other conflict in App v4's live instructions.** I searched for "unsure", "in doubt", "ask the human", "something matters" and "section matters" in `V4/loop`, `V4/init`, `V4/README.md`, `V4/docs` and `V4/app/src-tauri/resources/instructions`. Outside run records, the only hits are the sentence itself and a product design aim in `conceptual/EXEMPLARS_AND_LESSONS.md` line 217. App v4 has no project `AGENTS.md`.

### 2. The AUM Markdown
- **Exact application.** I parsed all 17 Before/After pairs from `RUN2/AUM_EDITS.md` (sha256 `12897483…`, as ruled). Each Before occurs exactly once in main's AUM (sha256 `08ca0e40…`), on the stated line. Applying all 17 gives sha256 `1ba63acdf4b4…`, 896 lines, which is byte-identical to the head's AUM. Nothing else changed (`apply_edits.log`).
- **Citations, verbatim.** All 32 "Now carried by" quotes are present verbatim in their sources at the head, with whitespace collapsed (`quotecheck.log`). The sources are construct §§1, 3 and 4, BR's "normally the penultimate merge", Field Book §5 ("1. Orient and recover"), SPEC §9.8, Piping `AGENTS.md` ("Software checks" and the loop-end sentence), both loops, and the App build guide. I read every edited line at the head against its cited text. Each one lands on text that carries the rule.
- **Truth at `87661be164`.** Every edited statement holds:
  - Neither the App loop nor the Piping loop names an undertaking.
  - Both name the WorkGraphs location: App by full path, Piping by folder.
  - Piping's entry step 3 and App §0 take the graph from the steering.
  - App's loop is evergreen.
  - Both manifests and the build guide give `>=22.19.0`.
  - E1's section lists match the edited lines: §§1, 2, 9, 14, 15, and §§2, 9, 13, 15, 18, 20.
- **No `[Piping loop §…]` citation remains.** The 8 `[Piping loop]` citations (lines 62, 104, 347, 524, 601, 603, 605 and 613) cite content the file now holds.
- **Links.** All 102 reference definitions resolve, and no label is undefined. `[field-book]` resolves and is used twice. The 8 unused definitions are the same at main and at the head, so the edits created no orphan (`links.log`).
- **App v3, Runtime and PEC statements the edits touched.** These are still true: App §§0, 1, 5 and 6, and the Runtime and PEC loop citations kept on line 102.
- **Nothing the edits should have caught remains.** I searched the AUM for LOOP_INIT, "none selected", "at this basis", "live loop", pointer, WORKPLAN, LOOP_RECEIPTS, receipt-chain and App v4 statements. The remaining "at this basis" (line 607, no Piping root `Cargo.toml`) is true. Lines 207, 565, 595, 603 (F-PIP-1 to F-PIP-4, retained by Piping `AGENTS.md`), 675 (both validators exist), 684 and 700 are true. Only the PEC statements remain untrue (NOTE-5).
- **Rulings 3–6.**
  - Ruling 3 is sound: E2 and E4 had to rewrite joint App/Piping sentences, and E16 follows the re-render's truth rule.
  - Ruling 4 is sound in outcome, with an inaccurate premise (NOTE-1).
  - Ruling 5 is sound and recorded (NOTE-5).
  - Ruling 6 is sound. The owner named the AUM. "In doubt, ask." comes from accepted rulings GC-7 and GC-8 for a named class of found relationships. That is a reserved decision under Root `AGENTS.md`, not uncertainty alone.

### 3. The AUM HTML
- **In place.** `python3 docs/alignment-manual/render_manual.py --source AUM --output docs/alignment-manual/CHIRALITY_AGENT_USER_MANUAL_v3.html --basis-date 2026-10-05 --basis-revision 87661be164179046710f0fd60002c9ce752f029d --check` gives "Verified". So the committed HTML is byte-exact to the renderer's output for the head Markdown, at that date and revision: HTML sha256 `0b583d84…`, source `1ba63acd…`. The renderer used markdown-it-py 4.2.0 and mdurl 0.1.2.
- **Scratch render.** The same arguments with output in `WT/scratch/ar_aum_01/` differ only in the two source-link lines (lines 254 and 261), which are relative to the output path (`render.log`).
- **README.** The AUM command now records `2026-10-05` and `87661be164…`. The Field Book command is unchanged, and the Field Book's own `--check` with that command also gives "Verified".

### 4. Piping's pointer edits
- B1, B2 and B3 equal `P/execution/_Coordination/AgentRuns/PIPING-LOOP-INIT-20261005/CONSISTENCY_EDITS.md` §B's After text byte for byte.
- Row 8 changes only its graph phrase, to "the work graph the human's steering selects".
- All four are minimal and true, apart from the optional wording in NOTE-2 and NOTE-3.

### 5. The manifest
- **G4.** Run with the Piping venv:
  - CI mode: PASS, 155 manifests.
  - Diff mode against `origin/main` (= `87661be164`) with `--tranche ROOT-LOOPINIT-AUM-ALIGNMENT-20261005`: PASS, 17 changed paths, 4 on the instruction surface, no BLOCK.
  - With `--added-manifests-only`: PASS.
  - The INFO lines are non-blocking over-declarations, the same pattern as `PIPING-LOOP-INIT-20261005`.
- **The authorization quote** matches `RUN2/OWNER_DECISIONS.md` exactly. The elided span is only the nested quotation, and the double spaces are kept.
- **The disposition** ("routed") is right. The rationale is true except for the omission in MAJOR-1. The piping notice it cites exists and is routed by `PIPING-LOOP-INIT-20261005.yaml`.

### 6. The piping run records carried here
`RULINGS.md`, `reviews/LR-LOOPINIT.md` and `reviews/SHA256SUMS` are byte-identical to NUM's at `db606c4efa`, and the run folder's tree hash is the same (`0ceef155…`).
- `LR-LOOPINIT.md` is `2de7d5d4…`, the new third line of `SHA256SUMS`. Its first 36,845 bytes hash to `787b8443…`, as Addendum B says.
- Addendum C's merge facts are correct: `87661be164` has the single parent `a2addb20d2` and a commit time of 16:38:21Z, and `gh` shows head `1ca59756f7` merged into it. Its tree `96ed3e12…` equals H4's.

### 7. Portability and publication
- **GEN-8.** `CHIRALITY_REQUIRE_LIVE_TESTS=1 … -m pytest -q -p no:cacheprovider tools/practitioner_harness/test_live_baseline.py -k gen8` at `4c286de23f`: 1 passed (`gen8.log`).
- **Entrypoint validator.** "PASS: root instruction entrypoints are canonical."
- **Added lines.** None of the 635 added lines contains a machine-absolute path, home path or credential pattern. Neither does `RUN2/BRIEF_AR.md`, which is untracked.
- **Public export.** See NOTE-4.

## Host and method disclosures
- **Commands I ran.** The renderer, the two validators, the GEN-8 pytest, and read-only analysis scripts of my own (edit application, link, quote, pin and export-drift checks), with output in the log folder.
- **Outside the brief's list.** I also ran `tools/validation/validate_piping_loop_receipts.py --repo-root .` once, read-only, to confirm that the validator AUM line 678 names exists and runs. It printed VALID, wrote nothing, and supports no finding.
- **Network.** `gh pr view` reads and one `git ls-remote origin refs/heads/main`.
- **Writes.** Only this report and `SHA256SUMS` in the worktree; `git status` shows only these and the untracked `BRIEF_AR.md`. No Git writes, cargo, installs or system-temp use.

---

## Addendum A: confirmation at H2 (2026-10-05)

**Reviewer.** The same AR instance. I made no Git writes. The original review is bytes 1–17,712 of this file (sha256 `2437c0bf…`, the first line of `SHA256SUMS`). H2's commit of it is byte-identical. ROOT's request permitted these runs: GEN-8, the two validators, `test_public_export_profile.py`, the renderer's `--check`, and the exporter with `--stage-dir` under `WT/scratch/ar_aum_01/`.

**Candidate.** H2 = `6049100caa427dc8ba9a03f1f16240c912b540f7`. Its parent is `09fd599bbc`, whose parent is H (`4c286de23f`). Main is still `87661be164`. The PR is open, a draft and MERGEABLE. When I looked, hosted `harness` and "App Runtime integration" were still in progress on H2. Every finished check had passed or been skipped by coverage selection.

### Verdict at H2: REPAIR

| Severity | Count (this addendum) |
|---|---|
| BLOCKING | 0 |
| MAJOR | 1 |
| MINOR | 1 |
| NOTE | 1 |

MAJOR-1 is repaired correctly. NOTE-1, NOTE-2 and NOTE-3 are applied correctly. The export manifest is exactly the exporter's output for H2's tree. One new MAJOR remains, introduced by the regeneration: the export report records a machine-absolute path.

### The original findings
- **MAJOR-1: repaired.** I checked all seven pins against the resources and against main's file bytes (`A_pins.log`). Each resource entry exists exactly once and records exactly the hash the notice states. Each stated hash equals main's bytes and differs from H2's.

  | Resource | Pinned file | Notice hash = resource = main | H2 hash |
  |---|---|---|---|
  | `SOURCE_MAP.json`, `loop` | `V4/loop/LOOP_INIT.md` | `45c23cf4…` | `c2e88f81…` |
  | `policy_standing/basis.json` | `V4/loop/LOOP_INIT.md` | `45c23cf4…` | `c2e88f81…` |
  | `policy_standing/a16/basis.json` | `V4/loop/LOOP_INIT.md` | `45c23cf4…` | `c2e88f81…` |
  | `SOURCE_MAP.json`, `manual_index` | `docs/alignment-manual/README.md` | `31217d30…` | `e5d23a6e…` |
  | `policy_standing/basis.json` | `docs/alignment-manual/README.md` | `31217d30…` | `e5d23a6e…` |
  | `SOURCE_MAP.json`, `user_manual` | AUM | `08ca0e40…` | `1ba63acd…` |
  | `policy_standing/basis.json` | AUM | `08ca0e40…` | `1ba63acd…` |

  The three resources pin no other file that the PR changes. The manifest rationale ("seven hashes … three pins of that LOOP_INIT, and four pins of the alignment-manual README and the Agent User Manual Markdown") is true. RULINGS Addendum A's erratum to ruling 8 is true. Nothing new is false.
- **NOTE-1: applied.** RULINGS Addendum A says "the 'stale at this basis' Node note was false at every basis it was rendered with". That is true: none of the build guide versions at the AUM HTML's seven render bases, `b3e2ce4` to `1cb9fd536e`, contains `>=20`, and `a89b5ddecf` precedes the first of them.
- **NOTE-2: applied.** B1 and B2 now read "`AGENTS.md` holds the project constraints and fences", which is true. The change from the piping run's §B text is recorded in RULINGS Addendum A.
- **NOTE-3: applied.** Row 8 now reads "these sources do not expand scope or lift holds", which is true.
- **NOTE-4: applied,** but see A-MAJOR-1 and A-NOTE-1.
- **NOTE-5:** no change, as ruled.

### New findings

#### A-MAJOR-1: the regenerated export report records a machine-absolute path

**Evidence.** In H2's `exports/chirality-app/export-report.md`, line 5 reads "- Staging path: `` `<absolute path under the owner's home directory, ending …/.claude/t3/scratch/aum_pr/export_stage>` ``". At H and at every earlier report it read "- Staging path: `exports/chirality-app/staging`".
- **The cause.** `write_report` prints the stage path relative to `REPO_ROOT` when it can, and otherwise prints the absolute path. This happened because the stage was outside the repository.
- **The scope.** It is the only machine-absolute path among H→H2's added lines, and no credential pattern appears in them.
- **The checks.** GEN-8 passes on H2, so it does not catch this file.
- **The precedent.** The same defect appeared once before, in `7bd2283dbc`, and was repaired under a review HOLD in `d2929fd62b`: "the report records the default staging path".

**Fix.** Re-run `python3 exports/chirality-app/export_public.py` with the default stage. `exports/chirality-app/staging` is gitignored (`.gitignore`, `exports/*/staging/`). Commit the report, then remove the staging folder. The manifest will not change: the stage location does not affect it, since my stage path differs from ROOT's and the manifests are byte-identical. The report should then differ from H2's only in line 5. Adjust RULINGS Addendum A's "It is staged outside the repository" accordingly.

#### A-MINOR-1: the manifest's scope limit excludes the export files that H2 now changes

The manifest's `scope_limits` says "the paths above, this run's records and the App v4 notice only". H2 also changes `exports/chirality-app/export-manifest.csv` and `exports/chirality-app/export-report.md`, which are not listed. Earlier manual tranches that regenerated the export listed both paths (`ROOT-MANUAL-60PCT-20261004.yaml` lines 19–20 and its scope limit; `ROOT-DGOV52-APPLICATION-20261004.yaml` lines 52–53). G4 passes either way, because it does not check `scope_limits`.

**Fix.** Add both paths to `instruction_surface_paths`, or name them in `scope_limits`.

#### A-NOTE-1: erratum to my NOTE-4

I wrote that main was behind on `workflows/index.json`. It was not. The exporter rewrites `workflows/index.json` into the stage (it filters out the project-only skill), so the export row legitimately differs from the repository file. Only construct's `WORKFLOW.md` row was behind on main. H2's manifest is consistent with this: it changes construct's row and not the index row.

### Checks at H2
- **The export.** I ran `exports/chirality-app/export_public.py` from H2's clean tree, with the stage at `WT/scratch/ar_aum_01/export_stage`. I ran the exporter's `main()` steps (`build_stage`, `write_manifest`, `boundary_findings`, `write_report`) unchanged, with only the two metadata output paths redirected to `WT/scratch/ar_aum_01/export_out/` and their location check disabled, so that no tracked file was written. The script is `run_export_redirected.py`.
  - The result was 1,878 rows, 0 sanitized and 0 boundary findings.
  - **`export-manifest.csv`** is byte-identical to H2's.
  - **`export-report.md`** differs from H2's only at line 5, the staging path (A-MAJOR-1).
  - **H→H2 manifest rows.** The changes are exactly the three AUM files, construct's `WORKFLOW.md` and the three new tranche manifests (`PIPING-LOOP-INIT-20261005`, `ROOT-CONSTRUCT-LOOPINIT-WORDING-20261005`, `ROOT-LOOPINIT-AUM-ALIGNMENT-20261005`).
- **The AUM.** The Markdown, the HTML and `docs/alignment-manual/README.md` are unchanged from H to H2. The renderer's `--check` with the README's arguments gives "Verified".
- **G4.**
  - CI mode: PASS, 155 manifests.
  - Diff mode against `origin/main` with `--tranche ROOT-LOOPINIT-AUM-ALIGNMENT-20261005`: PASS, 22 changed paths, 4 on the instruction surface, no BLOCK or WARN.
  - With `--added-manifests-only`: PASS.
- **The entrypoint validator.** "PASS: root instruction entrypoints are canonical."
- **GEN-8.** `CHIRALITY_REQUIRE_LIVE_TESTS=1 … test_live_baseline.py -k gen8` at H2: 1 passed.
- **`tools/validation/test_public_export_profile.py`.** 5 passed, with pytest's base temp under `WT/scratch/ar_aum_01/pytest_tmp/`.
- **Committed records.** `reviews/AR-AUM.md` and `reviews/SHA256SUMS` at H2 match what I wrote. `BRIEF_AR.md` is committed.

Logs are `A_*.log`, `export_run.log` and `export_out/` in `WT/scratch/ar_aum_01/`. After every run, `git status` in `WT/aum-pr` was clean apart from this append.

### Remaining condition
Repair A-MAJOR-1, and A-MINOR-1 or a ruling on it. Then `harness` and the other hosted checks must pass on the final head, and main must not have moved. A re-run with the default stage changes only `export-report.md` line 5 and records, so a confirmation by me can be limited to that delta.

---

## Addendum B: confirmation at H3 (2026-10-05)

**Reviewer.** The same AR instance. I made no Git writes. The file through Addendum A is bytes 1–25,753 (sha256 `17ef5b9a…`, the second line of `SHA256SUMS`). H3's commit of it is byte-identical. As ROOT asked, I confirmed the delta only.

**Candidate.** H3 = `6245dc6f9b9b93a84760ea93dbf082b67e75f372`, whose parent is H2 `6049100caa`. Main is still `87661be164`. The PR is open, a draft and MERGEABLE.

### Verdict at H3: READY

No BLOCKING, MAJOR or MINOR finding remains open. There is one new NOTE (B-NOTE-1).

### The delta
- **A-MAJOR-1: repaired.** Line 5 of `exports/chirality-app/export-report.md` again reads "- Staging path: `exports/chirality-app/staging`". H3's report is byte-identical to the exporter output from my Addendum A run, with only line 5 normalized to the default stage. `export-manifest.csv` is unchanged from H2 and still byte-identical to that output. No `exports/chirality-app/staging` folder remains in `WT/aum-pr`. The H2→H3 added lines contain no machine-absolute path.
- **A-MINOR-1: repaired.** The manifest now declares `exports/chirality-app/export-manifest.csv` and `exports/chirality-app/export-report.md`. Its `scope_limits` names the regenerated export (with the default staging path), this run's records, the Piping LOOP_INIT run's final records and the App v4 notice. All 22 paths changed against main are now covered: 11 declared paths, plus this run's records, the piping run's records and the notice. This also covers the piping run records, which the earlier scope limit had omitted. G4 diff mode with `--tranche` passes: 22 paths, 4 on the instruction surface, no BLOCK or WARN, and the two export paths reported as non-blocking over-declarations. The entrypoint validator passes.
- **RULINGS Addendum B.** Its wording accurately reports Addendum A's counts and confirmations, the A-MAJOR-1 repair, the erratum to Addendum A's NOTE-4 and the A-MINOR-1 repair. B-NOTE-1 below concerns its last bullet.

### B-NOTE-1: correction to my A-NOTE-1, and so to RULINGS Addendum B's last bullet

A-NOTE-1 said that only construct's `WORKFLOW.md` row was behind on main. That is incomplete. Main's export manifest also lacked rows for two tranche manifests already on main: `PIPING-LOOP-INIT-20261005.yaml` (#1092) and `ROOT-CONSTRUCT-LOOPINIT-WORDING-20261005.yaml` (#1093). My earlier drift check compared existing rows only.

No exported bytes are affected: H3's manifest contains both rows, and the docs count went from 338 to 341. RULINGS Addendum B's "Before this PR, main was behind only on construct's `WORKFLOW.md` row" repeats my wording. ROOT may correct it in a later addendum or rely on this one; no repair is required.

### Remaining conditions
When I looked, `harness`, "PEC workspace tests" and "App Runtime integration" were still in progress on H3. Every finished check had passed or been skipped by coverage selection. Merge needs every required check to pass on H3, or on whatever final head is merged, and main must still be `87661be164`. If main moves, the gates need refreshing or carrying over by ruling.

Logs are `B_*.log` and `B_*.txt` in `WT/scratch/ar_aum_01/`.
