# PEC Remaining retirement — run basis (RR1)

Status: **candidate account and draft packet for HELP_HUMAN and the owner.**
Nothing was applied. No `_STATUS.md`, Scope of Work, decision, register,
instruction, graph, `docs/**`, `loop/**`, `v2/**` or foreign file was written.

## Authority and brief

- Brief: `RR1_REMAINING_RETIREMENT_ACCOUNT.md` (HELP_HUMAN scratch),
  SHA-256 `e0bda78f24357181457409b5f035e7b2717d32f9e3c20ab6584a5ceca6486227`,
  verified before work. Undertaking `HELP-HUMAN-PEC-20260926-REMAINING-RETIREMENT`, node RR1.
- Owner words (quoted in the brief, recorded by HELP_HUMAN in its own PR, not
  yet observable on `origin/main` at preparation): "Why am I seeing
  `remaining-items` appearing?  There must not be any of those going forward,
  so no need to scan for them." and "open RS1". This record is evidence of
  them, not a ruling.
- HELP_HUMAN's course correction (2026-09-26 message): prepare against the
  approved SCA-006 amendment-1 hunk; the SOW sequencing rule; notices to Root
  and Runtime only; record the 73 held residuals; provisional number D-PEC-99.
  These are coordination decisions within the undertaking, not owner rulings.
- Write boundary: this folder and the RR1 return path only.

## Instruction and method sources (SHA-256)

| Source | SHA-256 |
|---|---|
| Root `AGENTS.md` | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `projects/pec/AGENTS.md` (`origin/main`) | `c9d3b44dfb5b07cff9790d58a67ff02825e297fcf0d2e290ab1599bf59ee197a` |
| `projects/pec/AGENTS.md` (PR #943 head `7f3102ed`, approved hunk) | `4400c4e97d5c9dfeda7a9a764b204ed14784c687e55e81bb04875323b6c7139c` |
| `agents/AGENT_WORKING_ITEMS.md` | `9ae4bea25bd95750a6878a9d53fbbbd7cd058d72c652a36baf4aa90601799665` |
| `agents/AGENT_TASK.md` (children) | `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7` |
| `workflows/task-management/WORKFLOW.md`, `contract.md`, `method.md` | `d5e8eff5…e654`, `3162f7ed…c61e`, `d52403c9…c61e` |
| `workflows/bounded-reconciliation/WORKFLOW.md` | `b96f91549e5b0c74d5403303a5de505abf50f24eb2aec95d20694af367d88098` |
| `workflows/scope-of-work/WORKFLOW.md` | `d616865a5cbfa84b47fd509d2910826106db57473543a86d067ddc3edf6fbd8b` |
| `workflows/construct-local-work-graph/WORKFLOW.md` | `3e197c9ddc75d40daa02929dc3df653a66f7d76ab6996239e823bba647dd9dc3` |
| SCA-006 amendment 1 `DECISION.md` | `15720eb1d25ade4e7cb5d62765824634318e0e956129a6e6c3ad30cdaf74777e` |
| `D-PEC-80_RULING`, `…_D_RULING_OWNER_INTENT_OF_RECORD`, `…_loop_home_and_instruction_surface` | `b821157e…fe33`, `585d764b…124f`, `d73b5f22…ff61` |
| `D-PEC-81_RULING`, `D-PEC-81` proposal, `D-PEC-82` proposal | `2947d99e…6c43`, `97b8bc73…7626`, `6cee5768…876d` |
| `D-PEC-83_RULING`, `D-PEC-83` proposal | `b0029459…2492`, `9892db3e…492b` |
| `D-PEC-84_RULING`, `D-PEC-84_L_RULING` | `6d9812b4…7a7e`, `2f52907f…9d10` |
| `D-PEC-94` record, `D-PEC-95_RULING`, `D-PEC-96_AMEND_DIRECTION` | `b6814e90…e33b`, `51dceb71…beb`, `c506732e…b3d2` |
| `D-PEC-95` proposal, `D-PEC-96` proposal (format) | `9137d387…4b22`, `4506597b…180e` |
| Post-SCA-005 `WORK_GRAPH.md` | `a203523d57b2f4337bd83cb3ad49d2e254a52797f911cdb014b01ef438296720` |
| SCA-005 `Propagation_Plan.md` (§B4 classes) | `50cd0b1d91ea25cc8ecba28ce649278b376fb952feec09e007a26ca5bbf91350` |
| Concordance `APPLICATION_MANIFEST.json`, `PROPOSED_ITEMS.csv`, `CARRIER_DISPOSITIONS.csv`, `RESIDUAL_RECOMMENDATIONS.csv`, R5 `APPLICATION_RESULTS.json` | `47db5a13…283d`, `91be3621…9b75`, `0c9b6116…14c0`, `193bbcc8…f5a5`, `74de0cb0…02ba` |
| Piping precedent at `2b531a7a3`: `CANDIDATE_ROW_ACCOUNT.csv`, `CENSUS_COMPARISON.md`, `FEDERATION_PREFLIGHT.md`, `REVIEW_RETURN.md`, `SEMANTIC_DECISION_PACKET.md`, `SEMANTIC_RUN_BASIS.md` | `b07e43eb…a7dc`, `fd882ae8…437b`, `257ad443…2c73`, `49554753…1913`, `5fae3235…70bd`, `385ea6cf…ac52` |
| Manifests: Piping, App, PEC D-PEC-94 | `009307b5…a100`, `1d20d6ad…f746`, `0ccddebe…b783` |
| App `EXCEPTION_DECISION_PACKET.md` | `06eea316f0aa1ca43703526ee938510fd1fb7dc915c362797f5855291af62403` |
| Reliance-hold register / script | `f877d931…41cbc` / `b1712e4b…cd0e` |

Wider consultation: `agents/AGENT_TASK.md` was read to brief the children;
no other role file was loaded.

## Execution

- Checkout: worktree branch `claude/pec-remaining-retirement-account`, cut
  from `origin/main` `6281273fa`, rebased onto `f90320c1d` (PR #946) during
  the run with no change to any census source.
- Manager: WORKING_ITEMS (`pec-manager`, Opus 5.5, high reasoning;
  instruction-asserted role). It built the census and comparison, ran the
  federation and reliance preflights, integrated the account, and wrote the
  draft packet, generator, closure check and this basis.
- Children: four `pec-task` TASKs (Opus 5.5, high reasoning), harness-native
  subagents of the manager, read-only on the checkout, each writing two files
  to the manager's scratch. Brief `RR1_SEM_TASK_BRIEF.md` SHA-256
  `f39f78213cdcc78adf740d02915b612bffa32e4ce557f966e4468f1dfad490c9`, plus one
  course-correction message each (the sequencing rule). Returns:

| Group | Keys | CSV SHA-256 | Notes SHA-256 | Result |
|---|---:|---|---|---|
| G1 PKG-00..02 | 23 | `cfaf8dc91476e8d99714954575770bb180d303e6259050f0e31d2a9b41e4c150` | `43153dcc2abdd70f4fe032d70206e5c25ac11cd138c4233d7bc77a32769f5c67` | c 5, d 18 |
| G2 PKG-03 | 24 | `0c4848e6dfb041844b846dccff28762880d5dc52b8f6612910af689afaa20f38` | `1f9c10b4f992acd20dc767911c4d515071a495830d616ce3f7e96fcfdc872fe6` | d 23, e 1 |
| G3 PKG-04..07 | 21 | `8876b0d9f66f37125f7f292039ea152b100910e1dcba253da06ab3b1cdc3d546` | `b81ab5757386242f5dbad4f264a3bc63a01f231b46946795195a396c12b91543` | c 4, d 17 |
| G4 PKG-08..10 | 24 | `a68733f2c387289d08c2308fb446823d94d9fb9a1af6ec09ebda86fb667cfc7b` | `dc2c5b8a78cae0072304c560b8b9624054979474dd4e23355873a4dbe9928dc8` | d 24 |

- Preparation aids (manager scratch; not bound): `build_census.py`
  `061e10bc…2f3f`, `build_account.py` `4b7e4a78…4db2`, `build_gen.py`
  `6c993c1b…45e4`, `gen_d99.template.py` `c00f4cff…9fbb`.

## Preparation evidence

All ran under CPython 3.13.7 with `PYTHONDONTWRITEBYTECODE=1`.

| Run | Where | Result |
|---|---|---|
| Census rebuild after the rebase | worktree (read) | byte-identical CSV `b0e25361…45eb4` |
| Reliance preflight, 102 targets × 2 operations | `projects/pec` | all `ALLOW`, exit 0 |
| Federation | worktree, ignored `.candidates/` output | COMPLETE; 4 registers; 28 findings, none PEC; 0 writes |
| `gen_d99.py --check-only` | scratch `git archive` export of the branch with `projects/pec/AGENTS.md` replaced by the PR #943 bytes | `CHECK write_set 62`, `status_sections_removed 57`, exit 0 |
| `gen_d99.py` act | scratch clone of that export | wrote 62 files; a second run fails `FAIL preimage …` (exit 1) |
| `gen_d99.py --check-only` against the live worktree | worktree (read) | `FAIL AGENTS.md preimage: SCA-006 checkpoint 3 (PR #943) must be merged first`, exit 1 (the dependency is enforced) |
| `--q1 decline`; `--decision D-PEC-100` | scratch | exit 0; classes as expected |
| `verify_d99.py --account-only` | worktree | `RESULT PASS` (8 checks) |
| `verify_d99.py --repo <post> --pre <pre>` | scratch | `RESULT PASS` (16 checks) |
| `verify_d99.py` on a mutated post-tree (Remaining heading re-added; one SOW byte added) | scratch | `RESULT FAIL` on the four expected checks |
| Tranche manifest, CI mode (module `repo_root` pointed at the scratch post-tree; no git) | scratch | `G4 PASS`, 126 manifests |
| `validate_instruction_entrypoints.py .` | scratch pre and post | PASS / PASS |
| `validate_decomposition_registers.py --strict` | scratch pre and post | identical output: 0 errors, 26 `XRG-013` warnings (baseline) |
| `validate_scope_of_work.py`, 32 SOWs | worktree and scratch post | 32/32 PASS (no SOW written) |
| `harness.py self-check` | worktree (pre) | exit 0 (post-act run is an act-time check: needs Git metadata) |
| `validate_pec_loop_receipts.py --repo-root .` | worktree | VALID (ledger unchanged by the act) |
| `taskmgmt.py validate`, both registers | worktree | PASS / PASS |
| `pytest` entrypoints + receipts tests | worktree | 33 passed |

Git-dependent post-act checks (manifest diff mode, harness self-check) could
not run on the scratch tree: this manager's Git access is confined to its own
worktree. They are act-time checks in the packet's verification table.
