# D-PEC-95 P + R — Revision-1.5 Currency Act Validation

All commands ran from the repository root (worktree
`agent-a471961b37f906dd4`, branch `claude/pec-d95-currency-act`) with
`PYTHONDONTWRITEBYTECODE=1`, Python 3.13.7
(`/Library/Frameworks/Python.framework/Versions/3.13/bin/python3`), local date
2026-09-25 (MDT), unless a row says otherwise. `checks/COMMANDS.txt` lists every
command in order with its exit code; each output is the file named in the
table. `<pre>` is a `git archive` export of `origin/main` `590ec52c1`
(tar SHA-256 `152aba22aee83d9b0a76c7265d533f523a0373f43b6e6cda9ac7033ef75a4024`),
extracted in the session scratchpad outside the repository. The verifier's
own fresh `git archive` of `590ec52c1` has the same tar SHA-256
(`VERIFIER_VERDICT_01.md`).

## Preconditions

| Check | Result |
|---|---|
| Fetched `origin/main` is `590ec52c15f86d812ce3c5d4919b475fe9cf3985` (PR #923) and contains the ruling `D-PEC-95_RULING_2026-09-25.md` (`51dceb71…4beb`) and the register row `D-PEC-95 … RULED P + R / EFFECTIVE ON MERGE` | holds |
| PR #919 (the work graph the N1 texts cite) merged on `origin/main` | holds: merge `7562c4434`; `WORK_GRAPH.md` at `590ec52c1` `f32ab9d2…3802` |
| Local date equals the act date | 2026-09-25 = 2026-09-25; `TZ` unset, `/etc/localtime` America/Edmonton; the generator's own date guard also passed |
| Branch cut from fresh `origin/main` in an isolated worktree | `claude/pec-d95-currency-act` at `590ec52c1` |
| Bound scripts copied byte for byte | `gen_d95.py` `0e9ede50…be78`, `verify_d95.py` `fcf172b5…185f`, `t1_tm_pec_023.py` `0e0cd6f9…7bec`; `cmp` against the preparation copies identical |
| Reliance-hold preflight, `dispatch-for-production`, 121 targets (119 product paths and both Task Management registers), before the generator | 121/121 `{"status": "ALLOW"}`, exit 0 (`checks/hold_dispatch-for-production.tsv`); `ACTIVE_RELIANCE_HOLDS.csv` `f877d931…41cbc` has a header and no rows; script `b1712e4b…cd0e` |
| Reliance-hold preflight, `rely-for-production`, the same 121 targets, before fan-in | 121/121 `ALLOW`, exit 0 (`checks/hold_rely-for-production.tsv`) |
| Preimages | 126/126 against `<pre>` (`checks/preimages_at_590ec52c1.out`): the generator's 124 READ pins (119 targets, 3 basis files, 2 SCA-005 files) and the two Task Management registers. The manager's pre-run working-tree check (243 pins in `genP.tsv`, 0 mismatches) printed to the terminal only; the saved record is the `<pre>` check and the generator's fail-closed guard |

## Finite verification (proposal table, option P with add-on R)

| Check | Required | Observed | Output |
|---|---|---|---|
| Generator | exit 0; `AGGREGATE option=P+R files=119`; `CHECK active_execution_quotes_verbatim 111 111` | exit 0; both lines as required; 119 WRITE; empty stderr | `gen_d95_report.tsv`, `gen_d95_stderr.txt` |
| `verify_d95.py <pre> . --option P --retired-covers` | every check PASS | exit 0; 11/11 PASS: population 66/66; contexts 66/66 at revision 1.5; references 66/66 at revision 1.5 and PRD v2.3; edits confined to the anchors (42 contexts, 64 references, R's bullets in the 4 retired); one shared provenance block; exactly 19 rows changed, in `EvidenceQuote`, `LastSeen` and `Notes` only; ACTIVE EXECUTION quotes 111/111; ACTIVE ANCHOR rows 132/132; `Handoff_State.md` and `RUN_SUMMARY.md` unchanged | `checks/verify_d95.out` |
| Byte identity | 115 files equal their P postimage in `genP.tsv`; the 4 retired `_REFERENCES.md` equal their A + R postimage in `genAR.tsv`; slot rule only if `{D}` ≠ 2026-09-25 | 115/115 and 4/4; the report's preimage and postimage columns agree; `{D}` = 2026-09-25, so no slot substitution | `checks/byte_identity.out` |
| SCA-005 snapshot files | `Handoff_State.md` and `RUN_SUMMARY.md` byte-unchanged | `a86ae910…328a` and `e9a0224e…e518`, unchanged | `checks/byte_identity.out`, `checks/verify_d95.out` |
| Strict registers | exit 0; 66 registers; 263 rows; 0 errors / 0 warnings; output byte-identical to the pre-act run | exit 0; 66; 263 (ANCHOR 140 / EXECUTION 123); 0 / 0; `cmp` identical | `checks/pre_strict.out`, `checks/post_strict.out` |
| Closure | exit 0; `closure_summary.json` byte-identical to D-PEC-93's (`bd73806c…187a`): 111 edges, 66 nodes, 0 SCCs, 0 bidirectional pairs, 0 orphans, the same six isolated | exit 0 before and after; `closure_summary.json` `bd73806c98e82455f6abfe66aeeee38623cd24f2e48ed102bb2689934bbc187a` both times, equal to `PROJECT_SETUP_SCA005_A4_B3_2026-09-25/closure/closure_summary.json`; 111 / 66 / 0 / 0 / 0; isolated 6; `subject_status` PASS | `checks/closure_pre*`, `checks/closure_post*` |
| Quote currency | 111/111 | 111/111 in the generator report and in `verify_d95.py` | as above |
| Schema per register | VALID × 10 | VALID × 10, exit 0 each | `checks/schema_10.out` |
| Receipts validator unaffected | exit 0; output identical before and after | exit 0 both; `cmp` identical ("frozen through Receipt-166; versioned receipt contract satisfied") | `checks/pre_receipts.out`, `checks/post_receipts.out` |
| Every-PR check | `harness.py self-check` exit 0; no finding cites a target path that the pre-act run did not | exit 0 both; output byte-identical before and after (`diff` empty) | `checks/pre_harness.out`, `checks/post_harness.out` |
| Containment | exactly the grant's paths plus the run root; with T1, also the two Task Management registers; nothing else | at the act commit `fdc7a2071` (printed to the terminal, indexed in `checks/COMMANDS.txt`): 119 product MODIFY, 2 Task Management MODIFY, 57 run-root ADD; 0 granted paths unchanged; 0 paths outside the boundary. Saved rerun: `checks/containment.out`, at the commit its header names (after the verdict-01 repairs). Later commits add only run-root files and the brief-authorized return file under `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/`, which `containment.py` accepts; the return records the final rerun | `containment.py origin/main`; `checks/containment.out` |
| Whitespace | `git diff --check origin/main...HEAD` clean | **Disclosed deviation, as in the D-PEC-93 act.** Outside the run root (the 119 product paths and both registers): exit 0, 0 notices. Whole diff: exit 2, 291 `trailing whitespace` notices, all in raw tool outputs kept byte-exact in this run root: 164 in the CR-at-EOL rows of the analyzer's `checks/closure_pre/*.csv` and `checks/closure_post/*.csv`, 125 in the empty trailing field of the generator report's READ and PATHLIST lines, and 2 in the tab-terminated PASS lines of `checks/verify_d95.out`. They stay unnormalized because they are hashed or rerun-comparable evidence. `.gitattributes` states that cosmetic whitespace does not gate CI | `checks/diff_check.out` |
| T1 | `taskmgmt validate` PASS on both registers after closing and after `archive` | PASS / PASS before, after closing and after archiving (details below) | `checks/t1_*` |

## T1 — TM-PEC-023 under `task-management`

Workflow `workflows/task-management/` (`WORKFLOW.md` `db06263d…e9b`,
`resources/contract.md` `e1c97a76…c837`, `resources/method.md`
`7f9e0d5e…e2f8`); invocation mode: register review, resolution of a specified
ruled item. Disposition source: the D-PEC-95 ruling, "confirm TM-PEC-023"
(Root `docs/CONTRACT.md` K-TM-3, `64747d2a…95bd`). Tool
`tools/taskmgmt/taskmgmt.py` `9c5cdc56…d101`.

| Step | Command | Result |
|---|---|---|
| Federation preflight | `taskmgmt.py federation --register …/REGISTER.csv --out <RR>/checks/t1_federation_projection.json` | exit 0; coverage COMPLETE; 4 registers; `register_writes: 0`; no finding names TM-PEC-023 |
| Validate before | `taskmgmt.py validate` on `REGISTER.csv` / `REGISTER_CLOSED.csv` | PASS (10 rows) / PASS (15 rows) |
| Close | `t1_tm_pec_023.py --repo . --act-date 2026-09-25` | exit 0; `REGISTER.csv` `d350d007…799d` → `62f897ab…4e24`; empty stderr |
| Validate after closing | both registers | PASS (10) / PASS (15) |
| Archive | `taskmgmt.py archive --register …/REGISTER.csv` (a `--dry-run` first) | exit 0; 1 CLOSED row moved; live 9 rows (8 `OPEN`, 1 `DEFERRED`); archive 16 |
| Validate after archiving | both registers | PASS (9) / PASS (16) |

Final hashes: `REGISTER.csv` `634641f0b7bf2d1f53d74283cc5e5253fee49ee6292e58a74b751f477345376a`,
`REGISTER_CLOSED.csv` `3c1349ba79ffb6eb0abc3502b0325da93ff28e7ecafd5498739a28ea0af11fd2`,
both equal to the proposal's prototype values.

## Checks not run, with reason

- `validate_instruction_entrypoints.py` and its pytest: no launcher, init or
  posture surface changed.
- Source-only, kill-test and parity checks: not applicable; no PEC capability
  or source changed (governance/control-only work).
- Re-audit and audit-pointer move: excluded by the ruling ("no re-audit").

## Not claimed

No CHECKING, ISSUED, acceptance, readiness or reliance claim. Git closeout is
source-control hygiene, not lifecycle issuance. Independent verification is
recorded in `VERIFIER_VERDICT_NN.md`.
