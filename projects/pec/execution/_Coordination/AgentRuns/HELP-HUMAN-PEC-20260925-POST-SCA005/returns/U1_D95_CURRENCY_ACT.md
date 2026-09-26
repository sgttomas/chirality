# U1 return — D-PEC-95 P + R currency act with T1 (WORKING_ITEMS)

Undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node U1 (N1–N3 and T1). Returned by WORKING_ITEMS (Type 1) to HELP_HUMAN. The host reports the serving model as Opus 5.5 (`claude-opus-5-5`); the role and the `high` reasoning effort are instruction-asserted.

## PR

- **PR:** #924, https://github.com/sgttomas/chirality/pull/924, `claude/pec-d95-currency-act` → `main`. OPEN and **not merged**, as the brief requires.
- **Head at hand-back:** the commit that adds this return. Its SHA is given in the hand-back report to HELP_HUMAN, because a file cannot contain the SHA of its own commit.
- **Commits:**
  - `fdc7a2071`: the act, T1 and the checks;
  - `fb030850b`: MANIFEST, VALIDATION and HANDOFF_STATE;
  - `0ed78d797`: verdict 01 and the N-1..N-3 repairs;
  - `5caaf4b94`: the saved containment rerun;
  - the commit that adds this return.
- **CI:** at `5caaf4b94`, every completed required check was SUCCESS or SKIPPED and `harness` was still IN_PROGRESS. `mergeStateStatus` was BLOCKED while checks ran. There was no "Update the PR base" notice.

## `{D}`

2026-09-25. This was the local date at the generator run, 20:36:19 MDT. `TZ` was unset and `/etc/localtime` is America/Edmonton. There was no clock or time-zone manipulation. The act date equals the table date, so the slot rule was not applied.

## Generator report aggregate

One run of `gen_d95.py` (`0e9ede5044b34cc4594836aab73a0a8df02cd4d1de8ae5e1e5625ebb232ebe78`) from the repository root:

```text
PYTHONDONTWRITEBYTECODE=1 python3 projects/pec/execution/_Coordination/CURRENCY_REV15_D95_2026-09-25/gen_d95.py --repo . --act-date 2026-09-25 --option P --retired-covers
```

It exited 0 with empty stderr. The report lines:

```text
CHECK	active_execution_quotes_verbatim	111	111
AGGREGATE	option=P+R files=119	b8ce26799bb6e1a3acd4204f8cfa632f429b730751449553030b43794c54e7ed	aab21097590a73e84328a262d7058f717ff216a44a68a95106578b9f17ef8361
PATHLIST	option=P+R	ebac38d0f8acb0556a88d83669d37e64e9965beba0ffc4adafdc9da6867edd03
```

- The pre-aggregate and the path list equal the proposal's option-P row.
- The post-aggregate is P + R's own. No table gives the combination; per-file byte identity carries it.

## Written paths with hashes

The manifest is `projects/pec/execution/_Coordination/CURRENCY_REV15_D95_2026-09-25/MANIFEST.md`. It has all 119 paths with their preimage and postimage SHA-256, plus the T1 register hashes. In summary:

- **119 product paths, all modified:**
  - N1: 3 records;
  - N3: 10 `Dependencies.csv`;
  - N2: 42 `_CONTEXT.md` and 64 `_REFERENCES.md`, including R's 4 retired-deliverable "covers" bullets.
- **SCA-005 files.** `Handoff_State.md` (`a86ae910…328a`) and `RUN_SUMMARY.md` (`e9a0224e…e518`) are byte-unchanged.
- **T1:**
  - `REGISTER.csv`: `d350d007…799d` → `634641f0b7bf2d1f53d74283cc5e5253fee49ee6292e58a74b751f477345376a`;
  - `REGISTER_CLOSED.csv`: `ea730ae0…afd94` → `3c1349ba79ffb6eb0abc3502b0325da93ff28e7ecafd5498739a28ea0af11fd2`;
  - both equal the proposal's prototype values.
- **Run root:** `projects/pec/execution/_Coordination/CURRENCY_REV15_D95_2026-09-25/`. It holds:
  - the bound `gen_d95.py`, `verify_d95.py` and `t1_tm_pec_023.py`, byte-identical to the preparation copies;
  - the generator report;
  - `checks/`, indexed by `checks/COMMANDS.txt` with exit codes;
  - the read-only check helpers;
  - MANIFEST, VALIDATION and HANDOFF_STATE;
  - `VERIFIER_VERDICT_01.md`.
- **This return:** `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/U1_D95_CURRENCY_ACT.md`.

## Check results

Run from the repository root with `PYTHONDONTWRITEBYTECODE=1` and Python 3.13.7. Details are in `VALIDATION.md`.

- **Preconditions:**
  - fetched `origin/main` is `590ec52c15f86d812ce3c5d4919b475fe9cf3985` and contains the ruling (`51dceb71…4beb`) and the register row `RULED P + R / EFFECTIVE ON MERGE`;
  - PR #919 is merged;
  - the branch was cut from fresh `origin/main` in an isolated worktree;
  - the preimages match, 126/126 against a `git archive` export of `590ec52c1`, which was kept outside the repository.
- **Reliance holds.** `pec_reliance_hold.py` returned ALLOW for 121/121 targets under `dispatch-for-production` before the generator, and under `rely-for-production` before fan-in. The targets are the 119 paths and both registers.
- **`verify_d95.py <pre> . --option P --retired-covers`:** 11/11 PASS.
- **Byte identity.** 115 files equal their P postimage in `genP.tsv`. The 4 retired `_REFERENCES.md` equal their A + R postimage in `genAR.tsv`. The SCA-005 files are unchanged.
- **Strict registers:** exit 0; 66 registers; 263 rows; 0 errors / 0 warnings. The output is byte-identical to the pre-act run.
- **Closure.** `closure_summary.json` is `bd73806c…187a` before and after, equal to D-PEC-93's: 111 edges, 66 nodes, 0 SCCs.
- **Schema:** VALID for each of the 10 registers.
- **Receipts validator and `harness.py self-check`:** exit 0, with output byte-identical before and after.
- **Containment.** 119 product modifications and 2 Task Management modifications. Everything else is an addition under the run root or this return. Nothing is outside the boundary.
- **`git diff --check`:** clean outside the run root. The whole diff has 291 trailing-whitespace notices, all in raw run-root tool outputs kept byte-exact. This deviation is disclosed as in D-PEC-93.
- **T1, under `workflows/task-management/`:**
  - federation preflight: COMPLETE, with no register writes;
  - `taskmgmt validate`: PASS on both registers before the close, after it, and after archiving;
  - `t1_tm_pec_023.py` closed TM-PEC-023 as `RESOLVED_BY_DECISION` on the ruling's "confirm TM-PEC-023";
  - `taskmgmt archive` moved the row, leaving 9 live rows (8 `OPEN`, 1 `DEFERRED`) and 16 archived.

## Verifier verdicts

The verifier was a fresh read-only `pec-reviewer` (TASK), which the host reports as Opus 5.5.

- **Verdict 01 (`fb030850b`): PASS WITH NOTES**, with no blocking finding.
  - It reproduced the act the same day on a fresh `13df8b795` export, without `--reproduction`. All 119 files and the report were byte-identical.
  - Every fixed check matched.
  - DEP-10-05-004's weaker warrant is recorded and not failed, per the ruling.
  - Its three non-blocking notes, N-1..N-3, were repaired in run-root records only.
- **Verdict 02 (backcheck of `5caaf4b94`): PENDING at hand-back.** The same verifier (agent `a0042f7d556e45196`) was resumed with the repairs and had not returned when hand-back was required. HELP_HUMAN should collect its result, save it as `VERIFIER_VERDICT_02.md` in the run root, and re-run review on the final head before merging.
- Verdict 01 is saved verbatim in the run root.

## Containment

Everything written is inside the brief's boundary: the 119 P + R paths, the run root, `REGISTER.csv` and `REGISTER_CLOSED.csv` (T1), and this return. Nothing was written to:
- any other `_Decomposition/**`, `_ScopeChange/**` or `_Evaluation/**` path;
- `checkpoint_snapshots/**`;
- any SOW or `_STATUS.md`;
- `docs/**`, `README.md` or `v2/**`;
- `_DECISIONS/**`, the work graph or `MEMORY.md`;
- any foreign path.

Scratch material (the pre-act export and the verifier's exports and helpers) lives only in the session scratchpad.

## Unresolved, for HELP_HUMAN

1. **Verdict 02 and merge.** Collect the pending verdict 02 from agent `a0042f7d556e45196` and transcribe it into the run root. PR #924 is open and unmerged. Under the standing authorization it can be merged once required CI passes on the final head and review has no unresolved blocking finding.
2. **Loop records.** These remain yours:
   - the work graph (U1/T1 outcome);
   - the central receipt;
   - the `docs/STATUS.md` and `README.md` lines under D-PEC-88;
   - any register-row status wording after merge.

   D-PEC-95 opens no MEMORY row.
3. **SCA-006 baseline (verifier N-2).** The SCA-006 checkpoint-1 package reused `COV_SCA005_POSTSETUP_2026-09-25_1606` as its pre-change baseline. That baseline carries COV-068/069/072/073 against the pre-D-PEC-95 state, so the proposal's re-audit rationale no longer holds.
   - The first audit to observe this state will be SCA-006's post-change audit (R3).
   - The ruling ("no re-audit") stands. The SCA-006 manager should know the baseline predates this act.
4. **Carry-forwards:**
   - DEP-10-05-004 evidence re-location to SOW-085, in a later dependency packet;
   - the 11 ACTIVE EXECUTION rows that cite `ScopeOfWork.md` files. The proposal recommends that each SOW packet run the corpus-wide quote check or `verify_d95.py`.
5. **Preparation folder.** Its `SHA256SUMS` lists a `D-PEC-95_DRAFT.md` that is not present, so `shasum -c` exits 1. The verifier noted this. It predates this PR and was not touched.
6. **Not claimed.** This return claims no CHECKING, ISSUED, acceptance, readiness or reliance. Nothing here prompts about CHECKING.

## Sources relied on

| Source | SHA-256 |
|---|---|
| U1 brief `U1_D95_CURRENCY_ACT.md` (HELP_HUMAN scratchpad; verified before work) | `6cdf4c63cdc8c993319dd069db6938c701b4d619da5985a8918811a03986553e` |
| Root `AGENTS.md` / `CLAUDE.md` | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` / `336cc4fbf19beaada7ccf9986414fa91851a8d7a07dfb3ccbe800a69eed0ab49` |
| `projects/pec/AGENTS.md` | `c9d3b44dfb5b07cff9790d58a67ff02825e297fcf0d2e290ab1599bf59ee197a` |
| `agents/AGENT_WORKING_ITEMS.md` | `9ae4bea25bd95750a6878a9d53fbbbd7cd058d72c652a36baf4aa90601799665` |
| D-PEC-95 ruling / proposal | `51dceb7136c24c1dea2f68c2338f66781de17fb2b63a8caf8bc719dd5a4e2beb` / `9137d3872329cea5093f61fb6c4150121e4ffcc2abe900ca88e7339049064b22` |
| `gen_d95.py` / `verify_d95.py` / `t1_tm_pec_023.py` | `0e9ede5044b34cc4594836aab73a0a8df02cd4d1de8ae5e1e5625ebb232ebe78` / `fcf172b5aa2ec6179a5af541f1a01d68a0148590d3b3f6eafbf913e64bfb185f` / `0e0cd6f94448005ecf17f564f35ef72a42f2c2862e97bc33256a3c701b957bec` |
| `workflows/task-management/WORKFLOW.md` / `resources/contract.md` / `resources/method.md` | `db06263d41f2a17e12b965a337dd6ba0baf3bd21c71ed6e5dc0de7997e101e9b` / `e1c97a76b8a411873ca86a6ef4351a7f76303e74331a52307a3705a83827c837` / `7f9e0d5ea7c2b74e7148faf3d2a35efc6ddd0552efd4b577a1c56895f75fe2f8` |
| Root `docs/CONTRACT.md` (K-TM-3) / `tools/taskmgmt/taskmgmt.py` | `64747d2a3c58ae93194bd5c7118d89a591b7b4ebe8cec7e88cb6a95dc55895bd` / `9c5cdc562053b2cc2eeb6674b750d95cb7fa47971eb07acee010a404c221d101` |
| `ACTIVE_RELIANCE_HOLDS.csv` / `pec_reliance_hold.py` | `f877d9316c7da76218399838aa6b69f1bb51bbd3e59b5b1d19b31f69ad741cbc` / `b1712e4b6e9f1476c577afd9170a4dd078beaa95878fa5f3b6c46a17b548cd0e` |
| Precedent run root `PROJECT_SETUP_SCA005_A4_B3_2026-09-25/` (format; `closure_summary.json`) | `bd73806c98e82455f6abfe66aeeee38623cd24f2e48ed102bb2689934bbc187a` |

Delegation: one fresh `pec-reviewer` child (Claude Code native subagent, agent id `a0042f7d556e45196`, model steer `opus`), read-only. It was resumed once for the backcheck. No TASK author was dispatched; the manager ran the generator, as the proposal's administrative grant assigns.
