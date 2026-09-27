# D-PEC-102 act — manifest

Run root `projects/pec/execution/_Coordination/SOW_CURRENCY_S4_2026-09-26/`,
undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node S4 (the act).
Act date 2026-09-26 (session and local date, MDT); the UTC timestamps in `evidence/`
read 2026-09-27T04:51Z onward.

## Actors and delegation

| Actor | Role | Mechanism | Model (host-reported) | Scope |
|---|---|---|---|---|
| Manager | WORKING_ITEMS (Type 1) under HELP_HUMAN, `Workflow: chirality-root:bundled:workflow:scope-of-work` (authoring discipline already applied at preparation: `MODE=INIT`, `STATUS_POLICY=NO_STATUS_TOUCH`, `DECOMP_VARIANT=SOFTWARE`; independent `MODE=VERIFY` at the act) | Claude Code subagent launched by HELP_HUMAN; own git worktree `.claude/worktrees/pec-d102-act` on branch `claude/pec-d102-s4-sow-act` from fresh `origin/main` `4c2a7768f` | `claude-opus-5-5` (high effort per the owner's "defaults"; instruction-asserted) | run root, act, verification, records, PR, return |
| Verifier | TASK (Type 2), fresh read-only `pec-reviewer`, `MODE=VERIFY` plus basis, byte identity, Part B, readings 3a/3b, seven-component consistency, containment | harness-native descendant (Agent tool, `subagent_type=pec-reviewer`, `model=opus`, `run_in_background=false`), agent id `aba354cc9ba64fbab` | `claude-opus-5-5` (host-reported by the verifier) | read-only; own `mktemp -d` under the session scratchpad with `TMPDIR` set to it; returned the `VERIFIER_VERDICT_01.md` text, saved verbatim by the manager |

Enforcement limits: role identity and write boundaries are instruction-asserted; the
host enforces only its own permissions. The verifier read the manager's worktree in
place and reported no writes there; containment was checked with `git status` and
`git diff`. The manager wrote run-root files with shell commands inside its own
worktree.

## Instruction and authority sources relied on (origin, SHA-256)

| Source | SHA-256 |
|---|---|
| Brief `S4A.md` (HELP_HUMAN session scratchpad `acts2/`; copied unchanged to `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/S4A_D102_SOW_ACT.md`) | `98f744886651e3d4ce9e54ef22dbbbbfaca486de421b45b9e80e46ceada6932e` |
| Root `AGENTS.md` (`CLAUDE.md` imports it; `CLAUDE.md` `336cc4fb…ab49`) | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `projects/pec/AGENTS.md` | `df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8` |
| `agents/AGENT_WORKING_ITEMS.md` | `9ae4bea25bd95750a6878a9d53fbbbd7cd058d72c652a36baf4aa90601799665` |
| `_DECISIONS/D-PEC-102_RULING_2026-09-26.md` | `782ee02fc5fc6375bc001568061796562ee2b82a603b601bee7f6e02a1bdd288` |
| `_DECISIONS/D-PEC-102_s4_sow_currency_proposal_2026-09-26.md` (the specification) | `baf178125e37ea8d82735f0bd4c0913531188ca9daffd95309339eb82fffcfdd` |
| `_DECISIONS/_REGISTER.md` at `4c2a7768f` (row `D-PEC-102` `RULED A / PART B AND 3a, 3b CONFIRMED / M / EFFECTIVE ON MERGE`) | `e167f532a1749b11e2c5850b9b636e533569bbe50a99b0b68d95c26339efe4bf` |
| Bound act script `PEC_SOW_CURRENCY_S4_PREP_2026-09-26/apply_s4p.py` (and the run-root copy) | `2b6792fee7b69266ad28f517734f89f9c01b60c6e6d4489118fd14375f364869` |
| Prep `SHA256SUMS` (107 entries, all OK; source of the 36 copied files' hashes) | `bf127a693eb27019ba76792159e7342db43c1bab2f6b22a6868a96952617f611` |
| `D-PEC-99_REMAINING_RETIREMENT_2026-09-26/EXHIBIT_MOVED_ITEMS.md` (pinned) | `69b646f8481fe39a12b811d8078ed14a4c49622d9a8ab566d87f83683044f45e` |
| `ACTIVE_RELIANCE_HOLDS.csv` / `execution/_Scripts/pec_reliance_hold.py` | `f877d9316c7da76218399838aa6b69f1bb51bbd3e59b5b1d19b31f69ad741cbc` / `b1712e4b6e9f1476c577afd9170a4dd078beaa95878fa5f3b6c46a17b548cd0e` |
| Precedent read (not relied on as authority): `SOW_REBUILD_S2_2026-09-26/` records, `briefs/S2A_D100_SOW_ACT.md`, `returns/REVIEW_PR979_0{1,2}.md` | at `4c2a7768f` |

## Method files

Workflow `chirality-root:bundled:workflow:scope-of-work`, resolved from
`workflows/index.json` (`2bfa2c5faae1081c55ce95fd3d81c00b1d87ba1f51d0bc13e03c8fcb6ccdafb3`);
no project (`.chirality/workflows`) or user (`~/.chirality/workflows`) workflow of
that name exists. At `4c2a7768f`:

| File | SHA-256 | Use |
|---|---|---|
| `workflows/scope-of-work/WORKFLOW.md` | `84dadde4c573b1d3d9ecd65e1e1be12efee1a95299b4115806c02e9c9cdebc2b` | loaded by the manager and the verifier |
| `workflows/scope-of-work/resources/checks.md` | `44ab41ace2fb14549ef0268c357ced42e798d97b01a325d62a60226767adf188` | loaded by the verifier (`MODE=VERIFY` subset) |
| `workflows/scope-of-work/execution.json` | `4ad8b7eb42dba41f1609e6b3c61f14baa15ad82a1342f4ad12a095c4a570a26d` | hashed only |
| `workflows/scope-of-work/resources/brief.md` | `1696cd9a0c13aeda4151ebdd666fff7d0450450c88ea1aa00f7435fdcbf492bc` | hashed only |
| `workflows/scope-of-work/resources/tools.md` | `fbd07771140f6350e964445014ba4f8f79f5d1f5c86df3379607b0489e6e5cc7` | hashed only |
| `workflows/scope-of-work/resources/representation-migration.md` | `698957a5005bc0078322c2bd6f12d73ab20f130999b060fe149aa7d4cb33e3c3` | hashed only (conversion) |
| `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` | `26c8254aaf2e2894e7d32096ec1e0d71b3ad881c1445094945031be19741433c` | hashed only |

The manager did not re-author content. Tools (equal to the proposal's pins):
`validate_scope_of_work.py` `f0f10590…fecfe`, `derive_review_checklist.py`
`bfb64dc9…0109`, `check_boundary_owner_resolution.py` `22ef57e0…ae16a`, `common.py`
`61a34722…0389`, `id_catalog.json` `7a1f8a12…757`;
`tools/validation/validate_decomposition_registers.py` `300a321f…ee20`.
Interpreter: Python 3.13.7 (CPython), `PYTHONDONTWRITEBYTECODE=1` throughout.

## Write-set decision (brief Act step 1)

`apply_s4p.py` inventories every file under `projects/pec` before and after the write
and leaves out its own directory (`SELF_DIR = Path(__file__).resolve().parent`, pruned
from `os.walk`); its placement guard accepts a directory beginning
`projects/pec/execution/_Coordination/SOW_CURRENCY_S4_`. The run-root copy was run,
so the run root is excluded, and **output was written beside the script in the run
root** (`evidence/apply_run.out`, created by the shell redirect before the script
started). Nothing else under `projects/pec` was written during the run. The verifier
confirmed the decision is consistent with the script and the proposal (verdict 01,
"Manager decision").

## Commits (branch `claude/pec-d102-s4-sow-act`, base `4c2a7768f`)

| Commit | Content |
|---|---|
| `70a3cebf9` | run root, bound script copy and aids, preconditions, dispatch preflight, pre-act baselines, `--check-only`, brief copy |
| `5d13cfdb8` | the act (eight replacements), rely preflight |
| `a26ca1613` | verification rows 2–12, rerun on `4c2a7768f` exports, negative controls (the verified candidate) |
| `b4e5a44e9` | `VERIFIER_VERDICT_01.md`, rely preflight before fan-in |
| `c8b3a8f9c` | no-rebase merge of `origin/main` `78e74f590` (PR #995; no `projects/pec` path) |
| `abe995b87` | post-merge rechecks at `78e74f590` |

Then the run-root records and the return. PR #998.

## Product writes (the act)

| Path (under `projects/pec/execution/`) | Preimage | Postimage |
|---|---|---|
| `PKG-04_Orientation_Services/1_Working/DEL-04-01_Loop_orientation_return/ScopeOfWork.md` | `6f4e8c66…30ae` | `98a3a3ec227380db2dd030c9c1ca31535d67071a44a3b79508ab4566b32771a0` |
| `PKG-04_Orientation_Services/1_Working/DEL-04-02_Delta_service_since_SHA/ScopeOfWork.md` | `a2b50f87…e65a` | `bcd69f503acf308e2ef7e73cc722efd61b59710877a5561624260aad71736b11` |
| `PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access/ScopeOfWork.md` | `8ac1dc05…3d76` | `b8c021f581448d1ff5413938563d40b015672aefede15ed97da9dd9b92865e01` |
| `PKG-08_API_Access/1_Working/DEL-08-03_Compact_citation_bearing_response_format/ScopeOfWork.md` | `013c615a…3138` | `d4bb8ffa475a7165a00f4d383a210f3d232dd16af3a971b87d9c1bad77cf81bf` |
| `PKG-08_API_Access/1_Working/DEL-08-04_Orientation_latency_budget_p95_100_ms/ScopeOfWork.md` | `6d1ec1ad…222b` | `16d731a51556cb644220c2c532696d8d0144972e20576db29495e200a775404c` |
| `PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping/ScopeOfWork.md` | `6ec7432b…ec6d` | `10819cb2ea90c7663a51bfc400d44e50a0d688325935d30472c8f29e3f087e18` |
| `PKG-03_Reconciliation_Parity/1_Working/DEL-03-04_Practitioner_harness_parity_diff/ScopeOfWork.md` | `e007f530…4e02` | `5f7bd434694c8a87bba512ba74a8b8f2dee4f5e2a0ab10e5a50c234e432b196f` |
| `PKG-10_Validation_Measurement/1_Working/DEL-10-03_No_ruling_write_verification/ScopeOfWork.md` | `cbcabbde…6ff8` | `e0df75bdcbdeaa2ecd0c320a3c36082c7c47551f2f514392856c761a96b99865` |

No `_STATUS.md`, `_REVIEW.md`, `Review_Findings.csv`, `MEMORY.md`, register,
dependency, context, reference, decomposition, `v2/**`, PRD or `docs/**` file is
written. Add-on M waits for closeout node M1.

## Run-root contents

- Copied from the prep folder, byte-identical (36 files; `evidence/runroot_copy.sha256`,
  `evidence/runroot_copy_check.out`): `apply_s4p.py`, `apply_s4p.template.py`,
  `build_apply_s4p.py`, `check_quote_currency.py`, `check_sibling_ids.py`,
  `negative_controls.sh`, `run_s4p_checks.sh`, `scan_external_quotes.py`,
  `scan_s2_quotes.py`, `test_apply_s4p.py`, `verify_s4p_quotes.py`,
  `verify_s4p_state_claims.py`, `candidates/…` ×8, `quotes/DEL-*.json` ×8,
  `claims/DEL-*.json` ×8.
- Outputs: `checklist_<DEL>.json` ×8 and `boundary_<DEL>.json` ×8 (proposal rows 3–4);
  `evidence/` (preconditions, reliance preflights, baselines, act, `post/` for rows
  2–12, `rerun_4c2a7768f/` and `rerun_78e74f590/` for the rerun method,
  `post_merge_78e74f590/`, `negative_controls.out`).
- Records: `MANIFEST.md`, `VALIDATION.md`, `HANDOFF_STATE.md`, `VERIFIER_VERDICT_01.md`
  (`9e3bd56010ef486a7ddc4b69c1bfa1c2b5d25c0017ee36dcc5b5f06af57a318f`; the verifier's
  handback text, SHA-256 `64b1635dd43c88c558177aee7f8d499291d48beadb0c1d52cd27444a254fca32`,
  plus one final newline, compared against the host subagent transcript).
- `SHA256SUMS`: every run-root file except itself.

## Scratch and footprint

Scratch lived under the session scratchpad (`s4a/`: the verification script, the rerun
consoles and `TMPDIR` for the check aids, which delete their own `mktemp` directories).
One exception: while recording `evidence/preconditions.out` the manager wrote one
temporary file `/tmp/_s4a_unused_<pid>` (the prep `shasum -c` output, to count OK
lines) and removed it in the same command. No repository file outside the brief's write
boundary was written.
