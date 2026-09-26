# Return C5 — D-PEC-93 option A PROJECT_SETUP act (WORKING_ITEMS, `pec-manager`/opus; one TASK `audit-decomp` child and one fresh read-only verifier, both opus)

Written and committed by the C5 manager on its PR branch before hand-back.
The full evidence is in the run root
`projects/pec/execution/_Coordination/PROJECT_SETUP_SCA005_A4_B3_2026-09-25/`
(`MANIFEST.md`, `VALIDATION.md`, `HANDOFF_STATE.md`, `gen_d93_report.tsv`,
`checks/`, `closure/`, `probes/`, `VERIFIER_VERDICT_NN.md`).

## Result

The option-A act ran once, exactly as the proposal states, and every
check gave the proposal's numbers. The re-audit reported 0 BLOCKERs, so the
audit pointer moved. The independent verifier reproduced the act byte for
byte on the same date: verdict 01 PASS WITH NOTES, no blocking finding;
after run-root wording repairs, verdict 02 PASS with no finding.

- **PR:** https://github.com/sgttomas/chirality/pull/914 (branch
  `claude/pec-d93-project-setup-act`, base `main`); not merged. Head SHA:
  see the PR (this file is committed in the head commit).
- **Act date:** 2026-09-25 (local, MDT). The generator ran at
  2026-09-25 16:01 MDT. The tabled hashes applied directly; no slot rule.

## Basis and instruction sources

| Source | Origin | SHA-256 |
|---|---|---|
| C5 brief `C5_D93_PROJECT_SETUP_ACT.md` | HELP_HUMAN session scratchpad `closeout/` (not in the repository) | `89b6d2ad04bb0db060795f041d624b7fbd5850aa475f25c4abab463942b08666` |
| Root `AGENTS.md` | repository at `04e04da00` | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `projects/pec/AGENTS.md` | same | `46689c36d5379029a34a5c5d26f109445e338fca82b86e590826bcbc39ad3846` |
| `agents/AGENT_WORKING_ITEMS.md` (role) | same | `9ae4bea25bd95750a6878a9d53fbbbd7cd058d72c652a36baf4aa90601799665` |
| `workflows/project-setup/WORKFLOW.md` (`chirality-root:bundled:workflow:project-setup`; entrypoint only — the proposal is the specification) | same; `workflows/index.json` `213a0738…fca3c` | `51c1cb9f7492aa28aaaa3f042ba3404e344f5870ff85f318112e05c4fdbea5a2` |
| `workflows/audit-decomp/WORKFLOW.md` (read to brief the child) | same | `4aaa7e10990ddd1b769ba09da78a03f9f491a6b6f3be6df08a1a8de93c26e3e6` |
| D-PEC-93 ruling | `_DECISIONS/`, on `origin/main` `04e04da00` | `ffb0b58293d868e1d7ddf61d2958a6b18ca73fa0c36da077f5309a8782153709` |
| D-PEC-93 proposal | same | `46470575625522398fa47d0a39aa09d2b4d252dd89c083ba317f9e577f489422` |
| Register row D-PEC-93 `RULED A / EFFECTIVE ON MERGE` | `_DECISIONS/_REGISTER.md` line 110 | — |
| `gen_d93.py` | PREP folder and the run-root copy | `cfae005258659c55915d0e9e2a8566399c3c84a95ede8e567205fecaea08d6c2` |
| `pec_reliance_hold.py` / `ACTIVE_RELIANCE_HOLDS.csv` (header only) | `execution/_Scripts/`, `_Coordination/` | `b1712e4b…cd0e` / `f877d931…41cbc` |
| `update_latest_pointer.sh` | `tools/scaffolding/` | `21899520ab84e0d88056b19a4318810cc3a730bc4b6d22e7ec66291549f015bc` |

No other role's instructions were consulted.

## Preconditions

- `origin/main` fetched at `04e04da00f620a1a5786ee744b167490cc90531c`
  (contains PR #913, the ruling and the register row).
- Local date = act date = 2026-09-25; no clock or time-zone manipulation.
- Branch `claude/pec-d93-project-setup-act` cut from fresh `origin/main` in an
  isolated worktree (the host allowed the new branch).
- Reliance-hold preflight `dispatch-for-production`: 34/34 `ALLOW` (31 product
  paths, pointer, audit stem, run-root stem), before the generator and the
  audit dispatch; `rely-for-production` 34/34 `ALLOW` before fan-in.
- Preimages 31/31 as tabled (generator guard and READ lines;
  `checks/00b_preimages_at_04e04da00.out`).

## Generator report

One run from the repository root:
`PYTHONDONTWRITEBYTECODE=1 python3 projects/pec/execution/_Coordination/PROJECT_SETUP_SCA005_A4_B3_2026-09-25/gen_d93.py --repo /Users/ryan/ai-env/projects/chirality/.claude/worktrees/agent-adb8a84864c6fa862 --act-date 2026-09-25`
— exit 0, empty stderr; report `gen_d93_report.tsv`
(`a0292ff96ec8f6b6698240ccf8ffed28f5c2976654db1a2be8628b96930f4466`): 27 READ,
31 WRITE, 2 CHECK (`check_min_viable_fileset` PASS for DEL-02-08 and
DEL-02-09). The verifier's independent run produced a byte-identical report.

## Written paths with hashes

All 31 equal the proposal table; the full table is in the run root's
`MANIFEST.md`. Aggregate over the 31 (bytewise-sorted path order)
`c4525add6b621d16523ad7567410b96f1864683cf93fd0d03c3f43954a79727a`; path-list
hash `1133e1ab0867f71f01346ed566cd8ede7fa2cff73ef79e4dbf87bc3bc8dcb9f1` —
both equal the proposal.

- **Created (12):** DEL-02-08 `_STATUS.md` `d80800a4…0eef`, `_CONTEXT.md`
  `721a9807…4d20`, `_REFERENCES.md` `87f95d42…840b`, `_DEPENDENCIES.md`
  `0ee572b9…9a3d`, `_SEMANTIC.md` `e3b0c442…b855`, `Dependencies.csv`
  `c23cd711…701e`; DEL-02-09 `_STATUS.md` `3e14313c…d768`, `_CONTEXT.md`
  `2413b5c0…0502`, `_REFERENCES.md` `211cb59c…073f`, `_DEPENDENCIES.md`
  `41c841a4…df3a`, `_SEMANTIC.md` `e3b0c442…b855`, `Dependencies.csv`
  `41afd6dc…8e4b`.
- **Modified registers (6):** DEL-03-01 `833fbfe0…436b`, DEL-06-04
  `ac55576e…b8fc`, DEL-07-02 `77230bbb…d8dd`, DEL-07-04 `cbb2175b…2b12`,
  DEL-07-05 `aa1dbe67…d41c`, DEL-09-05 `9811343c…32d5`.
- **Modified mirrors (13):** DEL-00-02 `818a06a3…2c3c`, DEL-01-01
  `1c39420c…72f0`, DEL-01-02 `625bb400…052e`, DEL-03-01 `e039ded3…61ec`,
  DEL-06-01 `9fd90c72…afad`, DEL-07-01 `2ea6519d…5360`, DEL-07-03
  `a9536c7a…7b8b`, DEL-09-05 `faa212e0…5251`, DEL-02-07 `2e53136f…8cdb`,
  DEL-06-04 `d6a1ad59…034d`, DEL-07-02 `f315d8a8…da89`, DEL-07-04
  `b1dc2ed3…3ac6`, DEL-07-05 `fc43eb3d…3617`.
- **Pointer:** `_Evaluation/DecompCoverage/_LATEST.md` `0084d218…7432` →
  `2b43dc3bb34163ae51067f6176ebf235430b59aa668890c1e65d7cc9d3cf1450`
  (`Latest: COV_SCA005_POSTSETUP_2026-09-25_1606`, `Updated: 2026-09-25`).

## Check results

| Check | Result |
|---|---|
| Written paths ⊆ 31-path list | holds |
| Postimage hashes | 31/31 equal the table |
| Strict registers validator | exit 0; 66 registers, 263 rows (ANCHOR 140 / EXECUTION 123); 0 errors / 0 warnings |
| `analyze_dep_closure.py` | exit 0; PASS; 111 edges, 66 nodes, 0 SCCs, 0 bidirectional pairs, 0 orphans; isolated exactly DEL-00-03, DEL-01-05, DEL-06-04, DEL-07-02, DEL-07-04, DEL-07-05; hub DEL-03-01 (25) |
| Schema validator, 8 registers | VALID ×8 |
| `check_min_viable_fileset`, 2 folders | PASS ×2 |
| Row conservation | holds; ACTIVE gained exactly the 8 added; 20 RETIRED; 0 deleted |
| Quote currency (new/refreshed) | 5/5 EXECUTION quotes verbatim; the 4 new ANCHOR rows use the D-PEC-62 locus-descriptor form, as every existing anchor does |
| `git diff --check` | product paths 0 notices; whole diff 109 notices, all in byte-exact raw tool outputs in the run root (disclosed deviation from "clean") |

## Re-audit

`projects/pec/execution/_Evaluation/DecompCoverage/COV_SCA005_POSTSETUP_2026-09-25_1606/`
(9 files: the method's eight plus `PrePost_Comparison.md`; hashes in
`HANDOFF_STATE.md`). SOFTWARE, ALL, revision 1.5 (`dc2b8479…9660`), compared
with `COV_SCA005_POSTCHANGE_2026-09-25_1344` (`912610ff…4deb`).
**0 BLOCKER, 3 WARNING (PRE-EXISTING: DEL-01-03, DEL-01-05, DEL-08-02
artifact location), 70 INFO; `overall_status` `WARNINGS`,
`closure_readiness` `WARN`.** Prior COV-001/002 (BLOCKER), 070/071, 068/069,
079/080/081 and 072 resolved (073–076 also resolved, by checkpoint 3 and A6);
006/008/042 and 077 carried; 078 carried as "64 of 66". New INFO: COV-015/016
(new folders have no artifacts yet), COV-071 (six isolated units, expected),
COV-072 (19 stale evidence quotes, PRE-EXISTING, not caused by this act),
COV-073 (SCA-005 handoff records and the two pointers still describe the
pre-act state).

## Pointer

Moved, because the re-audit reported 0 BLOCKERs: `tools/scaffolding/update_latest_pointer.sh projects/pec/execution/_Evaluation/DecompCoverage COV_SCA005_POSTSETUP_2026-09-25_1606`, exit 0.

## Verifier verdicts

- **Verdict 01** (`returns/C5_VERIFIER_VERDICT_01.md`; reviewed `f64a9a7c0`):
  **PASS WITH NOTES**, no blocking finding. Same-day N2 reproduction on a
  fresh `git archive` export of `04e04da00` at 16:27:44 MDT — 31/31 paths and
  the full `PKG-*` tree byte-identical. Notes: N-1 executor deviation
  (disclosed; see below); N-2 whitespace wording; N-3 pre-run preimage
  evidence; N-4 an abbreviated hash in the ruled proposal text (line 270
  gives `21899520…10cb25`; the tool is `21899520…49f015bc`); N-5 brief hash not
  recorded. N-2, N-3 and N-5 were repaired in the run-root records
  (`3984cb475`); no product byte changed.
- **Verdict 02** (`returns/C5_VERIFIER_VERDICT_02.md`; reviewed `3984cb475`):
  **PASS**, no blocking or non-blocking finding. The repairs resolve N-2,
  N-3 and N-5 without overstatement; no product path, audit file or pointer
  changed; verdict 01 was transcribed faithfully; `checks/00b` reproduces.
  Informational only: I-1 (the verifier cannot itself confirm the harness
  details in the manager's transcription header), I-2 (a count phrasing,
  correct as written).
- Both verdicts are also in the run root as `VERIFIER_VERDICT_01.md` and
  `VERIFIER_VERDICT_02.md`.

## Containment

`git diff --name-status origin/main...HEAD` contains only: the 31 proposal
paths; `_Evaluation/DecompCoverage/COV_SCA005_POSTSETUP_2026-09-25_1606/**`;
`_Evaluation/DecompCoverage/_LATEST.md`; the run root; and
`returns/C5_D93_PROJECT_SETUP_ACT.md` and `returns/C5_VERIFIER_VERDICT_NN.md`.
No `_Decomposition/**`, `_ScopeChange/**`, SOW, other `_STATUS.md` /
`_CONTEXT.md` / `_REFERENCES.md`, `v2/**`, `docs/**`, `loop/**`, `README.md`,
`_DECISIONS/**`, HELP_HUMAN `RUN.md` or foreign path changed. Scratch work
lived outside the repository (the manager's `scratchpad/c5_work/`; the
verifier's `mktemp -d` export, deleted). The only scratchpad file the manager
read that it did not create was the C5 brief.

## What the caller must resolve

1. **Merge.** The PR is open and not merged. `origin/main` moved to
   `23aad15d6` (PR #905, `projects/chirality-piping/**` only; no overlap).
   The first CI run on `77bc78b48` failed "Select source coverage" with
   "Update the PR base: event target base is missing, unavailable or not
   integrated into head", and "Desktop E2E (source mode)" failed as its
   dependent gate. The manager merged `origin/main` into the branch
   (`ecbaaa2ba`, no conflicts; the merge brings only
   `projects/chirality-piping/**`). The verifier reviewed `f64a9a7c0` and
   `3984cb475`; the merge changes no PEC path. CI must pass on the final
   head before merge.
2. **Executor disclosure (N-1).** The proposal's administrative grant names a
   TASK author for the generator; the C5 brief (and `RUN.md`'s C5 work graph)
   gave the run to the manager. The two `_STATUS.md` history lines read
   `TASK+preparation`, the ruled bytes. The verifier classes this as an
   acceptable, disclosed deviation. Carry it into the receipt.
3. **N-4.** The ruled proposal's abbreviated `update_latest_pointer.sh` hash
   at line 270 is wrong; a clarification in a later record if wanted (the
   proposal bytes are not edited).
4. **Loop records (D-PEC-88).** The register-row status after merge, the
   receipt, and `docs/STATUS.md` / `README.md` lines.
5. **Stale pre-act descriptions (re-audit COV-073; proposal finding 5).**
   SCA-005 `Handoff_State.md` / `RUN_SUMMARY.md`, the revision and
   scope-change `_LATEST.md` pointers and `_COORDINATION.md` still describe
   the pre-act state; none is opened by D-PEC-93.
6. **Residuals.** 19 stale evidence quotes (owner ruled: carry); B1 open
   (42 contexts, 64 references); B4 (first SOWs for DEL-02-08/09).

Nothing here claims CHECKING, ISSUED, acceptance, readiness or reliance, and
nothing prompts about CHECKING.

## Delegation record

| Child | Mechanism | Type / role | Model (host-reported) | Scope | Return |
|---|---|---|---|---|---|
| `a7bd6f9190b204e9f` | Claude Code Agent tool, `subagent_type: pec-task`, `model: opus`, foreground | TASK, `chirality-root:bundled:workflow:audit-decomp` | Opus 5.5 (`claude-opus-5-5`) | write only the new `COV_SCA005_POSTSETUP_*` folder; no git writes | hand-back to the manager; 0 BLOCKER, `WARNINGS`; wrote only its folder |
| `aafd0dde534417a2d` | Claude Code Agent tool, `subagent_type: pec-reviewer` (no Edit/Write tools), `model: opus`, foreground; resumed once by SendMessage for verdict 02 | TASK verifier, `chirality-root:bundled:skill:software-code-review` adapted to governed metadata | Opus 5.5 (`claude-opus-5-5`) | read-only; scratch outside the repository | verdicts transcribed verbatim by the manager |

The high reasoning effort is instruction-asserted. The manager ran the
generator, the checks, the reliance preflights and the pointer step itself,
and made all commits. The manager is `pec-manager` (Opus 5.5).
