# Sealed Brief — N1-TASK-DEL-02-02 — TASK + dependency-extract (REPORT-ONLY PREVIEW)

- **RunID:** `APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05` · **Node:** N1 · **InstanceID:** `N1-TASK-DEL-02-02`
- **Parent:** HELP_HUMAN (Agent 0) in an untyped Claude Code session; RequestedBy: HELP_HUMAN for the `TASK_dependency-extract` owner named in SCA-APP-010 `OWNER_ACTION_MATRIX.csv` step 19 and `DOWNSTREAM_HANDOFFS.csv` row 3.
- **Role:** `TASK` (Agent 2) with `TaskSkill: dependency-extract`; a fresh bounded Claude Code subagent; **no delegation**; role not mechanically enforced.
- **Repository root:** `/Users/ryan/dev/chirality/.claude/worktrees/task-management-gen-pass-518da2` (git worktree, branch `claude/sca-app-010-dependency-closure`). Run every command from this root. Do not `cd` into subfolders in a way that persists.
- **Basis:** `origin/main` `d66395d101143df68d956984f7ab93f5027418ec` (PR #713 merge). Stop if `git rev-parse HEAD` is not this commit or a fast-forward descendant that leaves the paths below unchanged.
- **Accepted upstream truth:** applied decomposition `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` at content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291` (the carrier's `ScopeOfWork.md` front matter pins `@dbd812a52d5ed0cb3ed173f3aaaa68703a914291`); companion register `projects/chirality-app-dev/execution/_Decomposition/contract_invariant_coverage_register.csv` SHA-256 `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca`; pointer `_ScopeChange/_LATEST.md` SHA-256 `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0` naming SCA-APP-010; authority corpus v20, no drift. Recompute the decomposition hash before extracting and stop on a mismatch.
- **Authorization:** SCA-APP-010 `FUTURE_WRITE_SET.csv` rows `DEP-003` and `DEP-004` (permitted effect: "Write only reviewed report-only-preview rows for the SOW-081..084 and revised SOW-001/002/004/006/007/008/010 relations; retire rather than delete stale rows"; forbidden effect: "Any edge inside the live nine-node SCC; any Root path; any unreviewed write"), triggered by the owner's acceptance of the WORKING_ITEMS alignment (Ryan Tufts, 2026-09-05, verbatim: "Merge PR #713.  Then proceed with the next steps.  Continue as the Agent 0 in your role of `HELP_HUMAN` and orchestrate the work according to your instructions on agents and delegation."). This instance is the **report-only preview**. It authorizes no write under the carrier folder.

## Scope

- **Carrier:** `DEL-02-02` — Right-Panel Coordination, Workflows, and Proposal UX (UX_UI_SLICE, PKG-02); folder `projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-02_Workbench_and_Pipeline_Selection_UX`.
- **Applied decomposition row:** `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` line 308. Scope refs on the row: SOW-006, SOW-081, SOW-082. Objectives: OBJ-001, OBJ-007. Amended Scope Ledger rows for this carrier: SOW-006 line 176; SOW-081 line 251; SOW-082 line 252. Also read the Scope Ledger to Deliverables reverse view (lines 404 to 487 (Scope Ledger to Deliverables reverse view)), open issue OI-008 (line 602), and DEC-025 (line 634).
- **Pre-images (must match before you start):** `Dependencies.csv` SHA-256 `ccc6f4018a0c61eb3ff59105080bf3f6cd807c2a326a67d2a5f4d5998cafeb92` (9 data rows); `_DEPENDENCIES.md` SHA-256 `77360b1b8f8ba69f594ba7ab10c013d21a01836d0d78fa0ae105e3867931a925`.

## Runtime overrides

```yaml
TaskSkill: dependency-extract
SCOPE: DEL-02-02_Workbench_and_Pipeline_Selection_UX
RUN_ROOT: projects/chirality-app-dev/execution
DECOMPOSITION_PATH: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md
MODE: UPDATE
STRICTNESS: CONSERVATIVE
CONSUMER_CONTEXT: RECONCILIATION
SOURCE_DOCS: [ScopeOfWork.md, _CONTEXT.md, _STATUS.md]
ANCHOR_DOC: ScopeOfWork.md
EXECUTION_DOC_ORDER: [ScopeOfWork.md, _CONTEXT.md, _STATUS.md]
ApplyEdits: false
ScopePath: projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/instances/N1-TASK-DEL-02-02
AllowedWriteTargets:
  - projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/instances/N1-TASK-DEL-02-02/
```

`_STATUS.md` is an execution source only for its `## Remaining` section (the seated items' `Depends`, `Write locus`, and gate lines are owner-adopted information-flow signals); its lifecycle, history, and approval fields are not dependency evidence. `_REFERENCES.md` is read to resolve document pointers. Exclude `_SEMANTIC.md`, `_SEMANTIC_LENSING.md`, `MEMORY.md`, `Assessment_*`, `Evidence*`, and `_run_records/**` as sources.

## Read

`AGENTS.md`; `agents/AGENT_TASK.md`; `skills/dependency-extract/SKILL.md`, `BRIEF_SCHEMA.md`, `QA_CHECKS.md`, `TOOL_POLICY.md`; the carrier folder; the decomposition at the lines above; the precedent run record `projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-04_Type_2_Subagent_Governance_Bridge/_run_records/TASK_RUN_2026-08-24_0053.md` and the precedent child return `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_GATE5_2026-08-24/instances/N4-SCOPE-CHANGE-01/children/TASK-DEL-08-04/RETURN.md` and `STATUS.json` (form only). Read other deliverable folders only to confirm that a target deliverable exists and to quote its applied row; never as a source for this carrier's rows. No network.

## Write (only these; nothing else anywhere)

- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/instances/N1-TASK-DEL-02-02/POSTIMAGE_Dependencies.csv` — the complete proposed post-image of the carrier's `Dependencies.csv` (all rows, v3.1, 29 columns, same column order and quoting convention as the pre-image).
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/instances/N1-TASK-DEL-02-02/POSTIMAGE__DEPENDENCIES.md` — the complete proposed post-image of `_DEPENDENCIES.md`.
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/instances/N1-TASK-DEL-02-02/PREVIEW.md` — see contract below.
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/instances/N1-TASK-DEL-02-02/RETURN.md` and `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/instances/N1-TASK-DEL-02-02/STATUS.json` — the child return in the precedent shapes (`schema: chirality-managed-child-status/v1`, `parentRunId: N1`, `status: PASS | WARNINGS | BLOCKED`, `humanRulingRequired`).
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/instances/N1-TASK-DEL-02-02/_run_records/TASK_RUN_2026-09-05_<HHmm>.md` — the TASK run record required by `agents/AGENT_TASK.md` (ScopePath is this instance folder, so the record lives here, not under the carrier).

Do not create or modify any byte under `projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-02_Workbench_and_Pipeline_Selection_UX` or under any other deliverable, decomposition, snapshot, register, `docs/**`, `frontend/**`, `agents/**`, `skills/**`, or Root surface. No state-changing git command. LF line endings, no trailing whitespace, final newline.

## Method

1. Verify the basis and the three upstream identities; verify both pre-image hashes.
2. **Pass 1 (ANCHOR).** From `ScopeOfWork.md` (front matter `decomposition_basis`, `project_scope_refs`, objective refs, and the traceability matrix) and `_CONTEXT.md`: exactly one `IMPLEMENTS_NODE` row (preserve the existing one and its `DependencyID`); one `TRACES_TO_REQUIREMENT` row per scope ref on the applied row and per objective (preserve existing IDs; add rows for refs that are new on the applied row, for example SOW-081 to SOW-084 where this carrier carries them; keep the existing `TargetType=UNKNOWN` convention for objectives with the existing note). An anchor to a scope ref that is no longer on the applied row becomes `Status=RETIRED` with a `Notes` entry citing the applied row line and DEC-025; never delete it.
3. **Pass 2 (EXECUTION).** Extract the information-flow and constraint relations that the applied row's Scope, Artifacts, and Notes columns, the amended Scope Ledger rows, `ScopeOfWork.md` requirements and verification claims, `_CONTEXT.md`, and the seated `## Remaining` items state for this carrier. Ownership statements on the row ("X owns the file contract; Y owns the view") are interface or constraint edges only when this carrier consumes or supplies a named artifact, contract, tool, event, or policy; pure coordination is not an edge. Root-owned semantics (Root DEL-02-09 login home, Root DEL-02-10 `proposal.*` event acceptance, Root DEL-02-11 delegation-policy field, daemon session store, closed `HarnessEvent` schema) are `TargetType=EXTERNAL` with `TargetLocation=TBD` and `SatisfactionStatus=PENDING`; never a Root path (Gate-5 and A12 convention).
4. **Existing rows.** Preserve every `DependencyID` and every `Origin=DECLARED` row. The legacy four-document kit (`Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`) no longer exists in this carrier; a row whose `EvidenceFile` names one of them must be re-evidenced to live bytes (`ScopeOfWork.md#<heading or REQ/CLM id>`, `_CONTEXT.md#<heading>`, or the decomposition `#L<n>`) when the relation is still stated, with `LastSeen=2026-09-05`; when the relation is not stated anywhere in the live sources, set `Status=RETIRED`, keep every other field, and explain in `Notes` (`RETIRED 2026-09-05: legacy kit retired; relation not restated in SOW_V1 sources`). Never delete a row. `Status=CANDIDATE` is never emitted.
5. **Fences (report, never suppress silently).**
- **F1: DEL-02-02 is not a member of SCC-001.** No new `EXECUTION` row may target an SCC-001 member in a way that would make this carrier a member (that is, do not add a row to an SCC-001 member if an SCC-001 member already has an active row back to this carrier); report any such candidate under `FENCE_F1_CANDIDATES` in `PREVIEW.md` instead of emitting it.
- **F2 (Root path).** `TargetLocation` may name only paths under `projects/chirality-app-dev/**` or repo-root files this carrier's `_REFERENCES.md` already pins; every Root-owned target is `EXTERNAL` with `TargetLocation=TBD`. List any candidate that would need a Root path under `FENCE_F2_CANDIDATES` and do not emit it.
- **F3 (permitted effect).** New rows are limited to relations introduced or revised by the amended rows named above and by this carrier's applied row prose; do not invent edges from SCC ordering, schedule, or "keep aligned" statements.
6. **Function 5 checks** against the post-image files in this instance folder: `PYTHONDONTWRITEBYTECODE=1 python3 tools/validation/validate_dependencies_schema.py projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/instances/N1-TASK-DEL-02-02/POSTIMAGE_Dependencies.csv`; `python3 tools/validation/validate_enum.py <ENUM> <value>` for every enum value you emit or change; `tools/validation/validate_id_format.sh` (the generic three-digit profile rejects the accepted App two-digit IDs; record that as the known `PROJECT_ID_FORMAT_PROFILE` warning and change no ID); exactly one ACTIVE `IMPLEMENTS_NODE`; every ACTIVE row has `EvidenceFile` and `SourceRef` that resolve to live bytes; `_DEPENDENCIES.md` tables reconciled to the post-image CSV following that file's existing count conventions; `FromDeliverableID=DEL-02-02` on every row; unique `DependencyID`s.
7. In `POSTIMAGE__DEPENDENCIES.md`: keep the declared sections and their headings; refresh `## Extracted Dependency Register`, add Run Notes for this run (defaults, paths, warnings, fence results, every `NEEDS_HUMAN_GRAPH_DECISION`), append one `## Run History` row (`2026-09-05`, `UPDATE`, `CONSERVATIVE`, decomposition found at the pinned identity, warnings, ACTIVE count), refresh `## Lifecycle Summary`, and refresh `## Downstream Handoff Notes` for `RECONCILIATION`. Place the new history row under `## Run History` (a prior pass once mis-placed it under `## Lifecycle Summary`).

## PREVIEW.md contract

1. Header: instance, carrier, basis, decomposition identity, pre-image hashes, post-image hashes (of the two `POSTIMAGE_*` files), row census pre and post (total / ACTIVE / RETIRED / ANCHOR / EXECUTION).
2. Row-level diff table over every row of the post-image: `DependencyID | Change (ADDED, RE-EVIDENCED, REFRESHED, RETIRED, UNCHANGED) | Class/AnchorType | Direction/Type | Target | EvidenceFile#SourceRef | Note`. `UNCHANGED` means byte-identical.
3. Fence results: `F1`, `F2`, `F3` each `NONE` or the list; `NEEDS_HUMAN_GRAPH_DECISION` (`none` or the rows); `FENCE_F1_CANDIDATES` / `FENCE_F2_CANDIDATES` (`none` or the list with the evidence you would have cited).
4. Validator outputs verbatim (schema, enum summary, ID-format warning, anchor check).
5. Epistemic notes: FACT / ASSUMPTION / PROPOSAL per new or re-evidenced row where not obvious.
6. Attribution: "Claude Fable 5.1 (Anthropic, `claude-fable-5-1`) as a Claude Code subagent acting as TASK + dependency-extract (report-only preview), dispatched by HELP_HUMAN; role not mechanically enforced; no descendant launched."

## Acceptance

`STATUS.json.status` is `PASS` when every check above passes and every fence result is `NONE`; `WARNINGS` when checks pass but a fence candidate or `NEEDS_HUMAN_GRAPH_DECISION` row exists (set `humanRulingRequired: true` in that case); `BLOCKED` when a pre-image, basis, or identity check fails (then write nothing but `RETURN.md`, `STATUS.json`, and the run record). Return the post-image hashes, the row census, the fence results, and the run-record path in `RETURN.md`.
