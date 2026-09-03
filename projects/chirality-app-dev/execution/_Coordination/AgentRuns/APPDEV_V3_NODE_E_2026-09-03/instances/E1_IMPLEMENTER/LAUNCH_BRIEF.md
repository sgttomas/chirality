# LAUNCH BRIEF — E1_IMPLEMENTER (verbatim sealed brief as received)

RunID: `APPDEV_V3_NODE_E_2026-09-03` · Instance: `E1_IMPLEMENTER` · Received 2026-09-03 from HELP_HUMAN (Claude Fable 5.1). The text below is the dispatch prompt reproduced verbatim; nothing is added or removed.

---

You are the sealed implementer for development node E of the Chirality App v3.0.0-rc.1 pathway: one seated, SELECTABLE, docs-only item, DEL-01-01-V3-01 — the AT-053 App governed-basis evidence record. This is the single-manager path (no product source), so no independent review child is required; HELP_HUMAN reviews the PR.

Repository: the git repo whose worktree is /Users/ryan/dev/chirality/.claude/worktrees/task-management-gen-pass-518da2. DO NOT change that worktree's branch or work inside it. Create your own worktree:
```
cd /Users/ryan/dev/chirality/.claude/worktrees/task-management-gen-pass-518da2
git fetch origin
git worktree add /private/tmp/claude-501/-Users-ryan-dev-chirality--claude-worktrees-task-management-gen-pass-518da2/88f4d942-8887-44e9-b9df-8a72e2ed6f30/scratchpad/wt-nodeE -b codex/app-v3-nodeE-at053-evidence-2026-09-03 origin/main
```
Work only there (REPO_ROOT). Never use bare `git stash`. `WORKING_ROOT` = `{REPO_ROOT}/projects/chirality-app-dev`. Basis must be `0c683fb16` or a descendant; record it.

## Read first
`{REPO_ROOT}/AGENTS.md`; `{WORKING_ROOT}/AGENTS.md`; `loop/LOOP_INIT.md`; the standing plan via `git show HEAD:projects/chirality-app-dev/loop/WORKPLAN_2026-09-03_app_dev_loop.md`; Rules + Receipt 205 of `loop/LOOP_RECEIPTS.md`; the item contract in `execution/PKG-01_.../DEL-01-01_.../_STATUS.md` `## Remaining` (DEL-01-01-V3-01), its `ScopeOfWork.md` and existing evidence artifacts in that folder (follow their format); the plan HTML `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` — extract AT-053's row and gate rows G0/G0.5/G1 and section 8 (governance and contract work) with python html parsing; `execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/{Carrier_Map.md,Impact_Assessment.md,Phase5/CLOSURE_ADDENDUM_2026-09-03.md}`; `execution/_ScopeChange/_LATEST.md`; the seating packet `execution/_Coordination/AgentRuns/APP_V3_PATHWAY_SEATING_2026-09-03/{MAPPING.md,COVERAGE_MATRIX.md}`; the routed Root notices `execution/_Coordination/NOTICE_2026-08-21_ROOT_DEL0206_COMPATIBILITY_ACCEPTANCE.md`, `NOTICE_D-GOV-35_DELEGATED_HARNESS_NATIVE_CLASS.md`, and the App-authored `NOTICE_2026-09-03_APP_TM-ROOT-122_ELECTRON_AUTHORITY_DISPOSITION.md`; the Root accepted compatibility snapshot `{REPO_ROOT}/execution/PKG-02_.../DEL-02-06_.../_run_records/DEL-02-06-COMPATIBILITY-ACCEPTANCE-005/ACCEPTED_COMPATIBILITY_SNAPSHOT.md` (ten bindings) and DEL-02-06's `ScopeOfWork.md` for REQ-027 and its exclusion; `docs/RELEASE_QUALITY_GATES.md` §13 (each condition); `docs/CONTRACT.md` at corpus v20 (K-CONTROL-1, K-ROLE-2, K-NET-1, K-KEY-1, K-EVENT-3/4/6, K-CONSENT-1, K-UNTYPED-1 and K-ENGINE-6); `execution/_Coordination/_DECISIONS/D-APP-103_*.md` (or the register row) for the D-APP-103 interaction; the live App Task Management register `execution/_Coordination/_TaskManagement/REGISTER.csv` (11 rows) and the Root register `{REPO_ROOT}/execution/_Coordination/_TaskManagement/REGISTER.csv` (open rows incl. TM-ROOT-106; TM-ROOT-122 is now closed); root ruling records R16, R17, R18 and App A11, A12 under `plans/steers/`.

## Step 0 (record before editing)
Clean status; basis SHA; receipts validator VALID; corpus status no drift (v20); APP-HOLD-1 `python3 execution/_Scripts/app_hold.py check --operation dispatch --entry-path loop/LOOP_INIT.md --target DEL-01-01` ALLOW. No `frontend/` is touched, so the A1 re-stage rule does not fire; say so. Create `execution/_Coordination/AgentRuns/APPDEV_V3_NODE_E_2026-09-03/` with ORCHESTRATION_PLAN.md, WORK_GRAPH.json, `instances/E1_IMPLEMENTER/LAUNCH_BRIEF.md` (this prompt verbatim), STEP0_DISCOVERY.md, later RETURN.md, CHECKS.json, HANDOFF_STATE.md, MANIFEST.sha256.

## Objective
Write one evidence record in the DEL-01-01 folder, e.g. `Evidence_AT-053_Governed_Basis_2026-09-03.md`, headed as App evidence for the G0.5/G1 REVIEW (not a verdict, not acceptance), that maps, with exact path + SHA-256 for every cited artifact recomputed from the tree:
1. every Root and App amendment in the v3 pathway (D-GOV-35, Root SCA-004, SCA-APP-008 Gate-5, the A-series A1..A12 and R-series R1..R18 rulings by title) to its accepted carrier or explicit unseated state;
2. each of the ten held DEL-02-06 bindings (verbatim binding names) with its current state `HELD_UNAVAILABLE` and the R16-A routing, without inferring any lift;
3. each RQG §13 Shared Runtime Gate condition to the App deliverable(s) that carry its evidence and the current evidence status (present / absent / gated), citing files;
4. DEL-02-06 REQ-027 and its exclusion, as stated in the accepted Root SOW, and how App consumes it;
5. the D-APP-103 interaction (packet authorized, awaiting ruling) and where it sits in DEL-08-04's Remaining;
6. every open App Task Management row (8 OPEN, 3 DEFERRED) and every open Root row relevant to the App pathway (at minimum TM-ROOT-106; state TM-ROOT-122 closed by R18 with PR #682 merge `fd55023e2`) mapped to its carrier/gate or explicit "not a carrier obligation";
7. the SCOPE_AMENDMENT_REQUIRED list S-1..S-7 from the seating packet, unchanged;
8. an explicit "not claimed" section: G0.5 and G1 remain unruled; no authority, closure, lifecycle, implementation, or release inference.
Use only facts present in the tree at your basis; where a fact is unavailable, write `TBD` with what would resolve it. Provide a machine-readable companion `Evidence_AT-053_Governed_Basis_2026-09-03.json` with the same mapping (arrays of {subject, class, carrier_or_state, citations:[{path, sha256}]}) and a sorted manifest.

## Write locus (nothing else may change)
The DEL-01-01 folder (`_STATUS.md`, `MEMORY.md` if present, the new evidence files), the AgentRuns run record, `loop/LOOP_RECEIPTS.md` append. No `docs/**`, corpus, register, Root, product, or other deliverable write.

## Checks
`git diff --check`; from REPO_ROOT `python3 tools/practitioner_harness/harness.py self-check` and `python3 -m pytest -q tools/practitioner_harness`; from WORKING_ROOT `python3 execution/_Scripts/app_hold.py scan --require-register-match` and corpus `status`; `python3 tools/validation/validate_app_dev_loop_receipts.py --repo-root .` after the receipt; a script-verified recomputation of every SHA-256 cited in the JSON (write the tiny verifier into the run record and run it). Frontend gates skipped (no product source); say so.

## Closeout
Update DEL-01-01 `_STATUS.md`: remove V3-01 from Remaining; History line naming the evidence files, commit, checks, and "revised if the G1 REVIEW returns a gap"; lifecycle lines untouched. HANDOFF_STATE.md and MANIFEST.sha256. Append **Receipt 209** (Parent `Receipt-205`; Examined-Through = basis; Owner-Direction pointer to the owner's 2026-09-03 dev-slate selection recorded in the run record; Pointers; Checks pass/fail only; Model-Attribution "Claude Fable 5.1 (claude-fable-5-1) as ephemeral Agent 2 implementer under HELP_HUMAN (Claude Fable 5.1)"; Gate-Outcome `EXECUTED — App AT-053 evidence prepared; G0.5/G1 unruled; awaiting owner merge`). Concurrent nodes append 206–208 with the same parent (ledger rule 7). `git fetch origin && git rebase origin/main` if needed (receipts append only), rerun receipts validator and diff --check, commit (message ends with `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`), push, `gh pr create` against `main` (body: basis, what the record maps, the not-claimed section verbatim, check table; end with `🤖 Generated with [Claude Code](https://claude.com/claude-code)`). Do not merge. Return PR number, head SHA, a two-paragraph summary of what the record establishes and what it leaves TBD; remove the scratch worktree (keep the branch).
