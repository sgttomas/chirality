# RUN — P1_STORE_GUARD_02 (D-PEC-87 C-A correction slice)

Role: WORKING_ITEMS (Type 1), instruction-asserted, owning PKG-01 / DEL-01-03
only. Parent: HELP_HUMAN run `HELP-HUMAN-PEC-20260923-SCA005`, node C2.
Brief: `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/briefs/C2_D87_CORRECTION_SLICE.md`
(supplied verbatim in the dispatch message; the canonical copy was being
committed separately and was not read from disk by this run).
Date: 2026-09-24 (session date). Host: Claude Code Agent tool, isolated
worktree. Model steer: `claude-opus-5-5`, high reasoning (D-PEC-86 I-8;
D-PEC-87 ruling). The host reports the manager as `claude-opus-5-5`.

## Basis (actual origins and SHA-256 at `origin/main` `6b4a0f59d292ed9f5f0ca222986ca95bc01bb0b6`)

| Source | SHA-256 |
|---|---|
| `AGENTS.md` (Root) | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `projects/pec/AGENTS.md` | `46689c36d5379029a34a5c5d26f109445e338fca82b86e590826bcbc39ad3846` |
| `agents/AGENT_WORKING_ITEMS.md` | `9ae4bea25bd95750a6878a9d53fbbbd7cd058d72c652a36baf4aa90601799665` |
| `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-87_RULING_2026-09-24.md` | `7da38e54508b913efba445e1968d5c86383ea6235719fb1dc908fd91717f66fe` |
| `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-87_del_01_03_store_guard_correction_proposal_2026-09-24.md` | `ba3d3e64eab7c0488b7973a10e360479d9f34bb075113f821266aea4a4684569` (matches ruling) |
| `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/returns/OBLIGATION_TRIAGE_DEL-01-03.md` | `db335614da29883212ce653cc12b672c68c5d6639200c33280c78c7b466ae6ea` |
| `_run_records/REMAINING_EVIDENCE_DEL-01-03-REM-001/REPORT.md` | `8fcb3ff3c317a2819f0043fdd548f34b5558cb89136fdeaaa33544a19de3c312` |
| `_run_records/REMAINING_EVIDENCE_DEL-01-03-REM-002/REPORT.md` | `b5d6632df94cd3cb7d3ba57b5ff8b0331e732cf9a0182040c8eefa6850364c60` |
| `_run_records/REMAINING_EVIDENCE_DEL-01-03-REM-003/REPORT.md` | `ca1b7b3e03ad96e3eaa8aef32751be0945331bfe34f10c32ae54d0bdc69ca930` |
| `workflows/software-bounded-implementation/WORKFLOW.md` (bundled; author method) | `2ea0ddf4f53241fa94274e709b8042ad9de4d8beb9c82cd1ed1dcd0c6f8f0f7b` |
| `.agents/skills/software-code-review/SKILL.md` (project skill; verifier method) | `06c27b1be5cfbd9e638570918a8f837d8439c8073c40d3ef708e53874f95570a` |
| `workflows/software-code-review/WORKFLOW.md` (bundled; verifier method detail) | `9054dfd47318a680e54fe390b00c67e2baf9595156487d4d1897a83458414810` |

Method-path discrepancy (routed, not behaviour-changing): the brief names
`.agents/skills/software-bounded-implementation/SKILL.md`, which does not
exist at `6b4a0f59d`. The method exists only as the bundled workflow
`workflows/software-bounded-implementation/WORKFLOW.md` (no project or user
workflow collides). The author was given that bundled source. The D-PEC-87
proposal governs the product specification either way. HELP_HUMAN then sent
a brief C2 correction confirming it: the author's method is the bundled
workflow `chirality-root:bundled:workflow:software-bounded-implementation` at
`workflows/software-bounded-implementation/WORKFLOW.md`; the verifier's
method stays `.agents/skills/software-code-review/SKILL.md`; scope unchanged.
The author had already been dispatched with that corrected path.

D-PEC-85 closeout (`projects/pec/execution/_Coordination/D85_PRODUCTION_CLOSEOUT_2026-09-08/`)
was consulted for context only and is not written.

## Preconditions

1. Fetched `origin/main` = `6b4a0f59d292ed9f5f0ca222986ca95bc01bb0b6`, the
   PR #890 merge; the ruling file and the `D-PEC-87` register row
   (`RULED C-A / L-1a / L-2a (AMENDED) / EFFECTIVE ON MERGE`) are present. PASS.
2. Fresh preimage verification: all seven granted paths and the unopened
   `adapters/storage/__init__.py` match the proposal (see `PREIMAGE.md`). PASS.
3. Reliance-hold `dispatch-for-production` preflight: ALLOW for all seven
   paths and the DEL-01-03 folder (see `PREIMAGE.md`). PASS.

Branching note: the host refused a local branch checkout in this isolated
worktree. The worktree's own branch was already at `6b4a0f59d` with a clean
tree, so the slice was built on that exact basis; the commit is published to
the remote branch `claude/pec-d87-correction-slice` named in the brief.

Interpreter: `/Library/Frameworks/Python.framework/Versions/3.13/bin/python3`,
Python 3.13.7.

## Work graph

| Node | Owner | Act | Depends |
|---|---|---|---|
| N1 | WORKING_ITEMS | Preconditions, run root, `PREIMAGE.md`, X-1 selector BEFORE | — |
| N2 | TASK author (`pec-task`, opus) | R1–R8 and X-1 on the seven granted paths under software-bounded-implementation; record at `AUTHOR_RETURN*.md` | N1 |
| N3 | WORKING_ITEMS | Five registered checks plus X-1 selector AFTER, under `checks/` | N2 |
| N4 | TASK verifier (`pec-reviewer`, opus, read-only) | software-code-review, substantive admissibility, PATH row vs PRD §7.1/§7.2; verdict at `VERIFIER_VERDICT*.md` | N3 |
| N2'/N4' | author / verifier | Correction cycles while a blocking finding remains | N4 |
| N5 | WORKING_ITEMS | `rely-for-production` preflight, containment, whitespace | N4 PASS |
| N6 | WORKING_ITEMS | L-1a `_STATUS.md` edit; `MEMORY.md` entry | N5 |
| N7 | WORKING_ITEMS | Commit, push, PR (no merge) | N6 |

## Progress log

- N1 complete. X-1 BEFORE: `checks/X-1_select_affected_checks_BEFORE.out`
  (selects `harness-self-check`, `v2-api-contract`, `v2-core-posture`,
  `v2-loop-registry`; not `v2-store-guard`), exit 0.
- N2 cycle 1 complete: author record `AUTHOR_RETURN_01.md` (agent id
  `ab75628e92cb1419f`, host-reported model `claude-opus-5-5`). The seven
  granted paths changed; no new test ID.
- N3 cycle 1: manager ran `tools/software_workflow/run_registered_checks.py`
  from the repository root for each check. All exited 0 with status PASS:
  `checks/v2-store-guard.json`, `checks/v2-core-posture.json`,
  `checks/v2-loop-registry.json`, `checks/v2-api-contract.json` and
  `checks/harness-self-check.json`. Verbose storage run:
  `checks/v2-store-guard_verbose.out` (13 tests OK, exit 0). X-1 AFTER:
  `checks/X-1_select_affected_checks_AFTER.out` now also selects
  `v2-store-guard`, exit 0. The wrapper's stdout, which only echoed absolute
  machine paths, was not retained.
- N4 cycle 1: verifier (agent id `a8e5f6d3e21db42cd`, `pec-reviewer`,
  host-reported `claude-opus-5-5`) returned **FAIL**; see
  `VERIFIER_VERDICT_01.md`. Code R1–R8 and X-1 all done exactly and all checks
  pass. The one blocking finding, B-1, is a documentation overclaim: a `str`
  subclass whose `__conform__` substitutes text at sqlite binding carries
  multi-line content through PATH, record_id, field names and SHA fields. This
  is pre-existing at HEAD, since D-PEC-85. Manager disposition: documentation
  correction inside the grant goes back to the author. The code closure (an
  exact-`str` rule on guard output) is outside R1's exact rule and is **routed
  to HELP_HUMAN for an owner-ruled packet**, not worked around. N-1, N-2 and
  N-5 (documentation/test, in place) are also sent to the author. N-3 and N-4
  are recorded as notes only.
- N2' cycle 2 complete: `AUTHOR_RETURN_02.md`. B-1 is fixed in documentation
  only: the `str`-subclass channel is stated as a guard-wide residual,
  pre-existing since D-PEC-85 and not closed by R1. N-1, N-2 and N-5 are
  applied. No code changed this cycle.
- N3 cycle 2: manager reran all five registered checks on the cycle-2 bytes;
  each exited 0 with PASS. The `checks/*.json`, `checks/v2-store-guard_verbose.out`
  (13 OK) and `checks/X-1_select_affected_checks_AFTER.out` files were
  overwritten with the final-bytes runs; the cycle-1 results are recorded
  above.
- N4' cycle 2: verifier **PASS** (`VERIFIER_VERDICT_02.md`, relayed verbatim
  by HELP_HUMAN because in this host the child's completion notices go to
  HELP_HUMAN). B-1 is resolved; documenting the residual is judged within the
  grant and truthful. Non-blocking C2-1 and C2-2 and notes C2-3 and C2-4
  remain.
- N2'' cycle 3 (doc only, directed by HELP_HUMAN): the author was asked to add
  C2-1 pointer sentences after `:79-80` and `:100-101`, correct C2-2 at `:95`,
  and rewrap C2-3. No code or test edits. Result: `AUTHOR_RETURN_03.md`. The
  doc is now `e9d65fc77ae3009a3d362eb34c8de527350456fcd7bc7670ef9e95ff9641ed35`;
  the other six paths are unchanged from cycle 2.
- N3 cycle 3: manager reran all five registered checks on the final bytes.
  Each exited 0 with PASS; the `checks/*.json`, the verbose run (13 OK) and
  the X-1 AFTER output (selects `v2-store-guard`) hold the final-bytes runs.
- N4'' cycle 3: verifier **PASS**, no blocking finding
  (`VERIFIER_VERDICT_03.md`, relayed verbatim by HELP_HUMAN).
- N5: manager `rely-for-production` preflight before fan-in: ALLOW with exit 0
  for all seven granted paths (register `f877d931…1cbc`). Containment and
  whitespace are below.
- N6: L-1a `_STATUS.md` edit: REM-001..003 ticked plus one history line citing
  the three reports, the triage and the ruling by name and hash. No lifecycle
  change. One `MEMORY.md` entry appended.

## Containment and whitespace (N5)

Changed paths against `origin/main` `6b4a0f59d`, excluding this run root
(`P1_STORE_GUARD_02/**`, which holds `RUN.md`, `PREIMAGE.md`,
`AUTHOR_RETURN_0{1,2,3}.md`, `VERIFIER_VERDICT_0{1,2,3}.md` and `checks/`):

```
projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/MEMORY.md
projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_STATUS.md
projects/pec/software-workflow.json
projects/pec/v2/docs/STORE_LIFECYCLE_AND_GUARD.md
projects/pec/v2/src/pec_v2/adapters/storage/sqlite_store.py
projects/pec/v2/src/pec_v2/core/content_minimal_guard.py
projects/pec/v2/src/pec_v2/core/ports/store.py
projects/pec/v2/tests/storage/test_content_minimal_guard.py
projects/pec/v2/tests/storage/test_store_lifecycle.py
```

That is exactly the seven granted paths, plus `MEMORY.md` and `_STATUS.md`.
The whitespace check against `origin/main` exits 0. The interpreter created
gitignored `__pycache__/` directories, which are not staged.
`harness-self-check` was rerun after the `_STATUS.md` and `MEMORY.md` edits:
exit 0 (`checks/harness-self-check.json`).

## Final postimages (relative to `projects/pec/`)

| Path | SHA-256 |
|---|---|
| `v2/src/pec_v2/core/content_minimal_guard.py` | `d63932c28dd346581deb0b04bb14841f00eff9481432a379ce67dd8e9d626b33` |
| `v2/src/pec_v2/core/ports/store.py` | `d7544f7191c38a40df49e55c8aaadbb54ea122003be5eb6ab7a2a1d6400a05eb` |
| `v2/src/pec_v2/adapters/storage/sqlite_store.py` | `05b9846a2baa9a5fe2691196d83d35770b8227f8b653f39c3831dcd4b89eae0a` |
| `v2/tests/storage/test_store_lifecycle.py` | `edbd41df5e05573d9992ee9778aba053570b4de6d4a0bf392ff7a888ff42cadf` |
| `v2/tests/storage/test_content_minimal_guard.py` | `c8e23563c226585c9f557d0c7d14eb880232452ab30541fa034a643afd561c29` |
| `v2/docs/STORE_LIFECYCLE_AND_GUARD.md` | `e9d65fc77ae3009a3d362eb34c8de527350456fcd7bc7670ef9e95ff9641ed35` |
| `software-workflow.json` | `8ec9ba6dcba7ea6b935923f5b4d846b2a9ac3f3d5cc43f5e160abe0971058a8b` |
| `v2/src/pec_v2/adapters/storage/__init__.py` (unopened) | `c9d8b3e5a1338ecf9dbc5a7405c47c69956e3c68e3219f60e3c988c1f1880540` |

## Delegation record

| Child | Mechanism | Parent | Type / model requested | Model reported by host | Cycles | Limits (instruction-asserted) |
|---|---|---|---|---|---|---|
| Author | Claude Code Agent tool, `subagent_type: pec-task`, `model: opus`; resumed with SendMessage for cycles 2 and 3 | this WORKING_ITEMS manager | TASK (Type 2), `claude-opus-5-5`, high | `claude-opus-5-5` | 3 | Seven granted paths plus its own `AUTHOR_RETURN_0N.md`; no state-changing git; no delegation |
| Verifier | Claude Code Agent tool, `subagent_type: pec-reviewer` (host type without Edit/Write tools), `model: opus`; resumed with SendMessage for cycles 2 and 3 | this WORKING_ITEMS manager | TASK (Type 2), `claude-opus-5-5`, high | `claude-opus-5-5` | 3 (FAIL, PASS, PASS) | Read-only, host-enforced by the absence of write tools; scratch outside the checkout; no repair; no delegation |

The reasoning level is instruction-asserted; neither child could confirm it.
The completion notices for later cycles were delivered to HELP_HUMAN and
relayed verbatim.

## Open scope questions (routed to HELP_HUMAN; not worked around)

1. **`str`-subclass content channel (code closure).** Pre-existing since
   D-PEC-85 and guard-wide. It reaches record IDs, field names, source paths,
   PATH values, and SHA and hash digests, through `__conform__` at sqlite
   binding and `__format__` in rendering. Closing it needs an exact-`str` rule
   on every string the guard outputs. That is outside the D-PEC-87 R1 exact
   rule, so it needs a separate owner ruling. HELP_HUMAN has said it will
   prepare that packet. This slice documents the residual only. Per
   `VERIFIER_VERDICT_02.md`, the packet's scope should also cover C2-2: the
   pre-existing normalization, absolute-path and `..` checks call methods a
   subclass can override. It should also state C2-4's threat boundary: an
   exact-`str` rule does not defend against in-process code that registers a
   global `sqlite3` adapter or writes the database directly.
2. **`close()` not wrapped under R8, and the `reopen()` `mkdir` `OSError`.**
   R8's explicit method list is `admit_batch`, `read_all`, `reopen`, `delete`
   and `reset`. A direct `close()` can still raise a raw `sqlite3.Error`, and
   `mkdir` in `reopen()` can raise `OSError`. R8 is not extended here.
   HELP_HUMAN routes this together with item 1.
3. **Invalid identifiers echoed in returned `AdmissionFailure` results.** The
   store never persists them. Consumers (DEL-03-01, DEL-06-02, API) must not
   log or persist that caller text. Routed to HELP_HUMAN.
4. Notes that need no action under the specification: N-3 (the accounting
   `RuntimeError` is unreachable by construction, so no test can observe it)
   and N-4 (only the `read_all` wrapping is test-proven for R8).
