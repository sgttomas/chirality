# Agent 0 session handoff — Runtime implementation

Status: implementation checkpoint prepared for PR publication, not product closure or release acceptance. The owner subsequently requested: “let's do a full PR to merge your work and incorporate that into the handoff information.” Current validation/publication status is in `PR_PUBLICATION.md`; it supersedes the original uncommitted checkpoint and pending-closeout statements below. The manager SESSION_HANDOFF and checkpoint archive preserve the earlier frozen state; follow later PR repair evidence for changed code. This is the operational handoff for a fresh HELP_HUMAN instance. The owner requested a handoff before the session limit: stop new work, resolve current operations, then transfer enough implementation context to continue. After interrupting running work, the owner clarified: “I didn't mean to crash your work. Resume what I interrupted.” Existing operations were resumed toward a clean checkpoint; this does not cancel the handoff request.

Prepared by OpenAI GPT-6; exact serving model ID unavailable. Agent 0 role is not mechanically enforced. Native role hierarchy and specialist non-delegation are instruction-asserted.

## Start here, in this checkout

Use `/Users/ryan/.codex/worktrees/341e/chirality`, branch `codex/runtime-execution`. Before publication this implementation was uncommitted; use `PR_PUBLICATION.md` and actual Git state to determine whether to resume this branch or the merged main commit. A checkout of main contains the implementation only after the PR is actually merged. Do not discard any subsequent local changes. Resolve the repository root and read root `AGENTS.md`, `agents/AGENT_HELP_HUMAN.md`, project `AGENTS.md`, and `loop/LOOP_INIT.md`. Follow currentness discovery, then read this handoff and `IMPLEMENTATION/SESSION_HANDOFF.md` beside it. Old in-memory subagent IDs are historical evidence, not resources a fresh session can assume it can reuse.

At handoff preparation, HEAD is `92ca3f1a639cda4dcb7544f1f59dfc78d7acf377`, the owner-authorized merge of PR #734. Last fetched main is `5738637472b616665fb4fe5003c4dec077a12380`, two commits ahead, App PR #735 only with no Runtime overlap. Refresh before relying on that statement. The checkpoint inventory records the actual final local files. That was the pre-publication checkpoint. The later PR record and Receipt 2 report actual validation and publication; do not infer merge acceptance from an open PR.

All candidate writes belong under `projects/chirality-runtime/**`. Root/shared instructions, tools, sibling projects, frontend, operational accounts, launch jobs, and release state are outside this run. The owner deliberately moved Root governance out of this session. Do not restart the migration or reopen its completed gates.

Checkpoint protection: `PARENT_CHECKS/SESSION_CHECKPOINT/FILES.json` inventories the final candidate and Git basis. A recovery copy of these modified/untracked files is `/private/tmp/runtime-execution-20260906/session-checkpoint/runtime-candidate.tar.gz`; its digest and member verification are in sibling `ARCHIVE.json`. This is a local backup, not a commit or remote publication. It excludes installed dependencies and the large supplier scratch; those remain at the separate paths below. If recovery is needed, inspect/extract into a separate directory first, never blindly over current work. The inventory excludes itself to avoid a circular hash.

## Authority and requirements: follow the sources

- `OWNER_DIRECTION.md`: exact post-PR734 instruction to get Runtime working through actual managers before the next PR; ordinary implementation and repairs are authorized. Do not manufacture intermediate permission gates for engineering work.
- `ORCHESTRATION_PLAN.md`, `IMPLEMENTATION_RELEASE.json`, `INTEGRATION_RELEASE.json`, and `IMPLEMENTATION_AMENDMENT_1.json` through `IMPLEMENTATION_AMENDMENT_14.json`: successive scoped dispatch grants and their limits. The early plan alone is not the final scope.
- Project `execution/_Coordination/MIGRATION_ACCEPTANCE_2026-09-06.md`, `docs/PRD_AUTHORITY.md`, accepted decomposition register, seven deliverable contracts, and `HOLD_SUCCESSOR_MAP.csv`: authoritative ownership, requirements, and outstanding owner acts.
- `SPEC_FAN_IN.json` and DEL-02-06 `_run_records/DEL-02-06-RUNTIME-SPEC-001/`: actual N0–N6 specification execution, independent review and integration basis. The accepted specification cycle ran; do not repeat it merely because the older project handoff described readiness only.
- `IMPLEMENTATION/PLAN_V2.md`, current `IMPLEMENTATION/CAPABILITY_MATRIX.md`, and manager `IMPLEMENTATION/SESSION_HANDOFF.md`: architecture, empirical coverage, unfinished implementation and latest checkpoint. Earlier sealed child returns describe their historical source versions.
- Repository-relative `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html`, sections 6.1–6.2: accepted native containment/conformance expectations. SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`. Read this before deciding which untested limb can be called complete.

Seven carriers remain INITIALIZED and nine holds remain. Successful engineering tests do not release those holds, accept a new supplier, activate operational state, promote lifecycle, or accept App adoption. R16-B's separately disposed Tier-0 relationship is not a tenth open hold. TM-ROOT-106's historical Pi source identity versus candidate Pi 0.82.0 remains a separate source-acceptance question.

## The Agent 0 plan and why the work took this shape

The objective is an executable Runtime, not another design packet. I kept one run/branch and used a real WORKING_ITEMS manager with bounded native specialists. The manager owns production code/tests and fan-in; Agent 0 owns authority interpretation, cross-stream coordination, parent-run endpoint tests, evidence calibration, and eventual Git closeout. Independent specialists reproduced defects and backchecked repairs. Briefs and reports alone were never counted as execution.

The implementation order was: accepted specification fan-in; additive v2 contracts and private supervisor/continuity foundations; reachable daemon/client/CLI integration; actual exact-supplier actor; actual Pi SDK/oMLX child; manager-to-child composition; containment/approval and production-admission checks; independent defect repairs; actual native canaries. The new v2 path coexists with v1; it does not declare the old API conformant or silently replace the accepted compatibility identity.

The broker is separate from the private worker. Public clients cannot select executable paths, policy, private credentials or arbitrary RPC. The supervisor authenticates its Unix channel and fences generation/root/account/epoch/policy. Codex provides the native worker and its descendants; Pi provides the bounded local model child. The manager composition actually creates a child, records a read receipt, and requires review. Production acquisition fails closed without a complete current conformance record and separate acceptance; controlled test factories are explicitly different evidence.

The major practical discovery was that the pinned vendor executable could perform text/resume but its sandboxed shell aborted before executing commands. A narrow source-built candidate fixed a literal-root directory read. Actual positive/negative controls then exposed a second supplier issue: named ask-network policy had no approval callback. We prepared a second narrowly reviewed source candidate rather than disabling sandboxing, broadening platform reads, globally preallowing a destination, or pretending configuration readback proved enforcement. Both candidates remain unaccepted. This is ordinary candidate preparation under the user's grant; changed-supply acceptance remains the owner's later decision.

The next Agent 0 should continue the remaining technical checks and repairs with the same distinction: an unimplemented or untested limb is work, not automatically an owner gate. Stop for the genuine account/source/acceptance boundary only after the ordinary candidate is concrete and reviewable.

## Evidence lessons that matter when resuming

- Exact supplier protocol/schema is read from the exact source and actual responses. The dedicated `codex-app-server` binary is invoked directly with `-c` arguments; do not append an `app-server` subcommand.
- Strict policy readback uses whole inline TOML table overrides. Trusted approval policy/reviewer fields are pinned on start, resume and turn, with start/resume response equality; CLI config alone did not prevent stored-thread overrides.
- A denial result is meaningless if the command never started. Pair network-off with a working positive control. Loopback is independently forbidden by the supplier and cannot be the network-on positive control.
- An echoed rejected command containing marker text is not execution evidence. Match standalone output markers or host-observed marker files. Exact errors may start `exec_command failed for`, not `failed:`. Missing captured stdout alone does not prove no shell startup.
- `applied:true` for an approval means its bounded transport write callback succeeded, not a provider acknowledgement or successful command.
- Observed process census/cleanup is not exhaustive orphan proof. Preserve limitations concerning between-poll detach and coarse process identity. Never signal arbitrary discovered processes by stale PID.
- Test-only no-account deterministic manager plus real Pi/oMLX is useful actual integration evidence, not hosted account or owner-live native delegation proof.
- Historical passing slices are not a final test total. Source pins and old failures remain historical; do not rewrite seals to claim an earlier result covers later changes.

## Parent endpoint tests and supplier artifacts

Parent scratch is `/private/tmp/runtime-execution-20260906/`. Keep it for the successor; source/toolchain/cache and test scripts are outside Git. Compact candidate binaries are needed for owner review. Do not delete them as routine cleanup. The manager handoff records whether any resumed build is still active; do not start a duplicate build.

| Artifact | Absolute path under scratch | SHA-256 |
|---|---|---|
| Original pinned executable, 179721344 bytes, version 0.149.0 | `supply/app-server` | `b1d1a8c3146b16a01c057e9ecc2213b969a775ba76c424d812714a2911708de2` |
| Source baseline, 241191088 bytes | `supplier-candidate/builds/baseline-artifacts/codex-app-server` | `a3ac0445f8fab23c62a97f3c9c8e420f094b67927948c1cfa69390b6e0742f93` |
| First literal-root candidate, 241191088 bytes | `supplier-candidate/builds/patched-artifacts/codex-app-server` | `b1ba73f40c3a40ebc161ea75dd68c24e90589e6e74e651065167636ad56876b2` |

Exact upstream source commit `758ef40f50c1a458425c7cfbf1eb12cbc07af0b0`, rust-v0.149.0 annotated tag object `a4e15bf371341b067c8278d3b70b1a8c7b3d793e`. Read supplier build provenance for the identical baseline/candidate path-version-only lock normalization. Candidate 2 compilation was interrupted and is safely stopped; no new artifact exists. Its exact cached resume command and source pins are in the manager checkpoint. Do not relabel the old target/release bytes as Candidate 2.

Parent comparison evidence is `PARENT_CHECKS/SUPPLIER_COMPARISON/`. Selected first-candidate shell and file-change primary/native canaries passed; public network-on and matched off passed. Public ask attempts failed and exposed the missing callback. Earlier failed controls and their explicit reassessment remain there.

The last three parent tests before handoff all exited and were preserved:

- `BOUNDARY_1`: primary/native read/environment summaries passed, but aggregate P1 failed with a masked exception. A startup-file assertion was a hypothesis, not an established diagnosis. At final checkpoint the diagnosis remains unresolved and no repair had begun; add bounded stage-specific diagnostics before any policy change.
- `PROCESS_NORMAL_1`: actual command markers were interleaved with denied `/private/var/select/sh` diagnostics, breaking a concatenated-string assertion. Observed cleanup had zero owned-group or detached survivors; the owned sibling signal count remained unchanged after its positive control. This is not a passing aggregate process profile. Parser and cleanup repairs were in progress.
- `ROLE_1`: failed before any vendor process/model call, `Daemon compatibility basis is unavailable`. The public fixture needed the real daemon compatibility basis; do not bypass the production check. Its correction was not started; the manager handoff identifies the exact fixture defect.

The existing parent wrapper `run_runtime_check.py` in scratch captures complete before/after source inventories, bounded output and timing. Use fresh result directories. Exact test opt-ins and candidate identity arguments are documented in their fixture headers and manager handoff. Do not rerun the whole historical sequence. Use the final candidate and relevant current-source limbs once repairs are frozen.

User's oMLX server: `http://127.0.0.1:8000/v1`, model `Qwen3.6-35B-A3B-8bit`. Actual SDK child read and full deterministic Codex-manager → supervisor → coordinator → live Pi child → review passed; see `PARENT_CHECKS/LIVE_PI/`, especially `EXACT_MANAGED_1`. The credential was supplied directly in conversation and used only by Agent 0 in memory; it is deliberately absent from this handoff and repository. If the fresh session lacks it, obtain a local credential from the owner only when a relevant live rerun is needed. Do not stop the user-owned server. No hosted login, account import or external inference was authorized by that local credential.

Amendment 13 permits only a bounded public network canary GET of `http://example.com/`, without auth, cookies, payload, query, redirect or external inference; body discarded after status/known marker. Amendment 14 governs the second candidate. Read the exact limits rather than widening them from this summary.

## Resume sequence after the session checkpoint

1. Verify local inventory, branch/base/current main and manager checkpoint. Preserve all uncommitted files. Establish fresh real manager/specialist instances with bounded scopes; do not rely on old task IDs. Start only unfinished authorized work.
2. Resolve the specific current P1/P2/P4 fixture or implementation findings from the manager checkpoint. Complete unexecuted P3 protected-pattern coverage and the remaining process lifecycle scenarios; these are not claimed passed.
3. Verify Candidate 2 build/review/source tests, then parent-run actual ask allow/deny/cancel and public Runtime primary/native approval attribution. Include missing-client/ambiguous/disconnected behavior according to accepted requirements. Do not combine different supplier identities into one accepted conformance result.
4. Consume later PR closeout repair evidence as well as the completed dependency-integrity repair/backcheck (stable 63 tests, independent 67) and reviewer-operation repair/backcheck (68); repeat only when later changed inputs justify it. Finish the eighteen-limb matrix. The declared dependency inventory has material latency (latest initial 8.50s, unchanged 3.82s); report it honestly and distinguish file integrity from arbitrary dynamic-import or already-loaded-module proof.
5. Obtain a manager semantic freeze and current independent review. Then package evidence, run final integrated checks, inspect source scope and currentness, and produce the actual implementation closeout. No final freeze or aggregate pass is implied by this session checkpoint.
6. Only at that point add the next Runtime receipt, commit, push and open one PR with concrete residual owner decisions. Do not merge it. Source acceptance, hosted account action, remaining holds, lifecycle/release and App adoption remain distinct decisions; do not treat the PR as automatic acceptance of all of them.

## Closeout mechanics left unfinished

The scratch `package_evidence.py` was applied during PR packaging. Do not apply it again. See `PARENT_CHECKS/PACKAGING/ORIGINAL_BYTES.json` and `SPEC_ORIGINAL_BYTES.json` for the lossless original-byte maps. It preserves original bytes in base64 with old/new hashes, removes trailing whitespace/extra terminal blank lines, and renames a historical test preimage to `.source` so Vitest will not discover it. It does not rewrite historical seals. Check for other reviewer `.test.ts` preimages before aggregate discovery. Do not use `.gitattributes` to hide whitespace defects. Create a separate final manifest over current presentation.

Final PR check verdicts and any repaired regressions are recorded in `PR_PUBLICATION.md` and `PARENT_CHECKS/PR_FINAL/`; the earlier failed aggregate remains as `registered-attempt-1.json`. Actual opt-in supplier/conformance gaps remain pending regardless of default-suite results. The registered runner requires its output path **inside Runtime**:

```sh
python3 tools/software_workflow/run_registered_checks.py projects/chirality-runtime/software-workflow.json --output /Users/ryan/.codex/worktrees/341e/chirality/projects/chirality-runtime/execution/_Coordination/AgentRuns/RUNTIME_EXECUTION_2026-09-06/PARENT_CHECKS/registered-final.json --timeout-seconds 600
```

Also run the required entrypoint validator, candidate whitespace against fetched origin/main, G0–G4, harness self-check and affected tests; discover exact commands in prior parent check records/live validators. Initial affected testing passed 825 tests plus nine subtests, but later source changes require final appropriate verification. Preserve the accepted basis hashes, inspect `git diff --check`, and scan candidate files for credentials without printing matching secrets.

The run uses one branch and one PR, not one per specialist. A publication-metadata follow-up may record the PR URL after its creation; it is not another implementation iteration. Commit attribution ends `Co-Authored-By: GPT-6 <noreply@openai.com>`. PR ends `🤖 Generated with [Codex](https://openai.com/codex/)`. No closeout was performed solely to manufacture a clean-looking handoff.
