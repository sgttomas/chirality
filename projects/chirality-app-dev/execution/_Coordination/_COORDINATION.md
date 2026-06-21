# Coordination Record - Chirality App Dev

**Recorded:** 2026-06-13
**Active persona:** `WORKING_ITEMS`
**Default work mode:** bounded app-integration tranches
**Current strategic focus:** Deliverable INSPECTION & development evidence (`plans/PLAN_2026-06-20_deliverable_inspection_and_development_evidence.md`, D-APP-19 Option D) — move all 53 deliverables `IN_PROGRESS -> CHECKING` and inspect each at issuance-gate rigor to form new evidence on how to proceed developing the application, while evaluating whether the issuance-gate process is the one to keep. Issuance (`CHECKING -> ISSUED`) is deferred. The preceding Agent-Orchestration UI redesign (`plans/DESIGN_2026-06-18_agent_orchestration_ui.md`; Phases 1-5 + the D-APP-28 loop-first pivot) is complete. The underlying runtime posture is unchanged: Chirality-owned provider-adapter runtime, with Claude Agent SDK / Anthropic as the first concrete adapter, now the key-aware default provider per D-APP-18 (real `agentSdk` when an Anthropic key is configured, else `stub`). Pi is a pattern corpus / reference only, not an adapter, fork, package import, sidecar, or spike target.
**Current active queue:** `plans/PLAN_2026-06-20_deliverable_inspection_and_development_evidence.md` (D-APP-19 Option D custom: deliverable-inspection phase, issuance deferred). Tranche spine INSP-00 -> INSP-00b (both landed 2026-06-20: D-APP-19 ruled, plan authored, prior plans superseded, coordination repointed) -> INSP-01a (normalize preflight) -> INSP-01 (move all 53 `IN_PROGRESS -> CHECKING` with the owner-blessed approvalSha) -> INSP-02 control-plane truth-fix -> INSP-03 per-deliverable inspection sweep -> INSP-04 gate-process evaluation -> INSP-05 development roadmap -> INSP-FINAL. **INSP-01a executed 2026-06-20, found a status-history preservation blocker, and reran clean under D-APP-33**: 52 `_STATUS.md` files contain one semantic/provisional noncanonical history bullet each that would be dropped by the writer, and D-APP-33 ruled that preservation is not required for this project. Evidence: `plans/artifacts/insp01a_status_preflight_2026-06-20.md`, `execution/_Coordination/_DECISIONS/D-APP-33_RULING_2026-06-20.md`, and `plans/artifacts/insp01a_rerun_after_dapp33_2026-06-20.md`. **INSP-01 landed 2026-06-20** with owner-approved SHA `8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec`; all 53 deliverables are now `CHECKING`, 0 `IN_PROGRESS`, 0 `ISSUED`. Evidence: `plans/artifacts/insp01_owner_approval_sha_2026-06-20.md`, `plans/artifacts/insp01_status_transition_evidence_2026-06-20.md`, and `plans/artifacts/insp01_status_transition_log_2026-06-20.json`. **INSP-02 landed 2026-06-20** and aligned PKG-00 control-plane documents with accepted acyclic DepClosure snapshot `CLOSURE_SCC_SAFE_MOVES_001_2026-06-16_0325Z`; evidence: `plans/artifacts/insp02_control_plane_truth_fix_2026-06-20.md`. **INSP-03 waves 001-003 are recorded 2026-06-20**: PKG-00 control-plane assessments DEL-00-01 and DEL-00-02, PKG-01 governance/reliance assessments DEL-01-01 through DEL-01-04, and PKG-02 baseline UI assessments DEL-02-01 through DEL-02-05 are complete (11/53), the index is `plans/artifacts/insp03_assessment_index_2026-06-20.md`, reviewed SHA `50b063f3ec4d9df900b4f2c465cf2f9ac79e91a0` is recorded for wave 003 per owner instruction, 42 assessments remain pending, and 0 deliverables are issued. Next selected work: continue `INSP-03` with the PKG-03 wave. `CHECKING` here means "admitted to inspection," not approved-for-issue; `CHECKING -> ISSUED` is a separate, deferred, per-deliverable gate. Completed/superseded history (non-governing): the D-APP-28 loop-first pivot `plans/PLAN_2026-06-19_loop_first_pivot.md` (28a-28e landed; typecheck clean, 503 vitest, `next build` + `desktop:pack` green); the issuance program `plans/PLAN_2026-06-18_deliverable_issuance_and_evidence_consolidation.md` (materials transposed; issuance spine retained as eventual follow-on); the live packaged `agentSdk` read-tool proof (D-APP-17 `sonnet`); the R6 program (R6-04 deferred); the Runtime Stabilization program (STAB-00..06); and the six-node SCC plan. D-APP-18 + D-APP-19 + D-APP-20..D-APP-33 are all ruled (see `_DECISIONS/_REGISTER.md`); D-APP-18 landed the key-aware default-provider cutover; provider expansion beyond the Anthropic path and release/distribution posture remain separately gated.

## Active Surface

Use this coordination surface as the active entrypoint for app-integration work. Keep it lean: project truth remains in governed docs, decomposition and deliverable artifacts, source, tests, evidence records, and git history.

Path anchors for executable prompts:

- Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`.
- Set `WORKING_ROOT` to `{REPO_ROOT}/projects/chirality-app-dev`.

Primary authority and guidance:

- `{REPO_ROOT}/AGENTS.md`
- `{REPO_ROOT}/agents/AGENT_WORKING_ITEMS.md`
- `{WORKING_ROOT}/AGENTS.md` - project-local agent posture and closeout discipline
- `docs/PRD.md` - product requirements and current runtime scope
- `docs/PLAN.md` - strategic roadmap, not the active queue
- `docs/DIRECTIVE.md`
- `docs/CONTRACT.md`
- `docs/SPEC.md`
- `docs/TYPES.md`
- `docs/VALIDATION_STRATEGY.md`
- `docs/RELEASE_QUALITY_GATES.md`
- `docs/BUILD_AND_RELEASE.md`
- `docs/AGENTIC_DEVELOPMENT_WORKFLOW.md`
- `docs/README.md`
- `docs/MANIFEST.json`
- `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
- `execution/_ScopeChange/_LATEST.md`
- `frontend/docs/harness/runtime_engine_contract.md`
- `plans/DESIGN_2026-06-18_agent_orchestration_ui.md` - active Agent-Orchestration UI & Information Architecture redesign design; Phases 1-5 complete
- `plans/PLAN_2026-06-19_loop_first_pivot.md` - completed D-APP-28 full loop-first pivot (28a, 28b, 28c, 28d, and 28e landed; no remaining unstarted tranche)
- `plans/PLAN_2026-06-19_validation_server_build_isolation.md` - CLOSED validation-loop follow-up; its sequencing rule (stop dev server before build/package/premerge unless the command owns server lifecycle) is codified in `docs/BUILD_AND_RELEASE.md` §4 and `docs/VALIDATION_STRATEGY.md` §3
- `plans/PLAN_2026-06-17_live_packaged_agentsdk_read_tool_proof.md` - completed Live Packaged `agentSdk` Read-Tool Proof plan; live `sonnet` proof passed (D-APP-17); D-APP-18 since ruled Option A and its key-aware default-provider cutover landed
- `plans/artifacts/lp02_live_packaged_agentsdk_read_tool_procedure.md` - exact LP-03 command, package path, key supply, artifact directory, stop conditions, and redaction checks
- `plans/artifacts/lp03_live_packaged_agentsdk_read_tool_evidence_2026-06-18.md` - LP-03 failed-proof evidence and redaction disposition
- `plans/artifacts/dapp17_live_packaged_agentsdk_read_tool_success_2026-06-18.md` - successful app-directory packaged live read-tool proof evidence
- `plans/PLAN_2026-06-17_r6_extensibility_mcp_boundary.md` - completed R6 Extensibility & MCP Boundary Maturity program (R6-01..R6-05; R6-04 deferred), accepted by D-APP-14 and closed by R6-05
- `plans/PLAN_2026-06-16_runtime_stabilization.md` - completed Runtime Stabilization program (STAB-00..STAB-06), accepted by D-APP-11 and closed by STAB-06
- `plans/PLAN_2026-06-16_six_node_scc_resolution.md` - completed non-governing SCC-resolution tranche-selection plan (closed history)
- `plans/PLAN_2026-06-13_runtime_completion.md` - retired runtime completion history
- `plans/PLAN_COMPLETION_LOG.md` - landed-tranche narrative history
- `plans/chirality-app-future-development-plan.md` - seed runtime roadmap/reference
- `plans/claude-agent-sdk-implementation-followups.md` - first-adapter implementation reference
- `plans/pi-agent-harness-assessment.md` - Pi pattern-corpus reference
- `plans/pi-assessment/*.md` - Pi pattern-corpus reference assessments
- `execution/_Coordination/_LATEST.md`
- `execution/_Coordination/NEXT_INSTANCE_PROMPT.md`
- `execution/_Coordination/_DECISIONS/_REGISTER.md`
- `execution/_Reconciliation/DepClosure/_LATEST.md`
- `execution/_Reconciliation/DepClosure/CLOSURE_SCC_SAFE_MOVES_001_2026-06-16_0325Z/Dependency_Closure_Report.md`
- `execution/_Reconciliation/DepClosure/CLOSURE_SCC_SAFE_MOVES_001_2026-06-16_0325Z/Closure_Acceptance_Audit.md`

## Authority And State Rules

Do not maintain a separate next-instance state file. Current state must be discovered from authoritative artifacts, dependency evidence, current implementation surfaces, selected plans, decision records, validation evidence, and git history. Do not let handoff prose, completion plans, dependency snapshots, or runtime logs become substitute authority.

Authoritative state:

1. `docs/PRD.md`, `docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, and `docs/TYPES.md` define requirements, invariants, mechanics, and vocabulary.
2. `docs/PLAN.md` records strategic runtime direction and roadmap rationale. It is not the ordinary active work queue.
3. `docs/VALIDATION_STRATEGY.md`, `docs/RELEASE_QUALITY_GATES.md`, and `docs/BUILD_AND_RELEASE.md` route evidence, release-quality checks, and local build/package evidence. They do not create release readiness, lifecycle issuance, publication authorization, or professional acceptance.
4. `docs/AGENTIC_DEVELOPMENT_WORKFLOW.md`, `docs/README.md`, and `docs/MANIFEST.json` are workflow/index surfaces. They help discovery and orientation, but they do not replace canonical agent instructions, coordination policy, project truth, or human rulings.
5. `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` records the package/deliverable decomposition and source-governed scope basis.
6. Accepted SCOPE_CHANGE snapshots under `execution/_ScopeChange/**` record governed decomposition/guidance amendments. `SCA-APP-001` approves provider-adapter generality, Pi pattern-corpus-only posture, and capability-forward permission governance with explicit hard-deny precedence.
7. Deliverable-local `_STATUS.md`, `MEMORY.md`, `_run_records/**`, four-document kits, dependency files, and review/evidence files carry lifecycle, working memory, and execution evidence inside their ownership boundary.
8. Current dependency and SCC evidence lives in immutable reconciliation snapshots under `execution/_Reconciliation/DepClosure/**`, with `execution/_Reconciliation/DepClosure/_LATEST.md` as a discovery pointer. The accepted latest snapshot `CLOSURE_SCC_SAFE_MOVES_001_2026-06-16_0325Z` reports strict `scc_count = 0`; the residual six-node SCC no longer blocks project-wide strict dependency-closure claims. This is dependency-closure evidence only and does not create product, runtime, release, lifecycle, professional, certification, sealing, authentication, or code-compliance approval. Future SCC work follows the shared cycle-driven resolution doctrine (the shared repo-root `docs/CYCLE_DRIVEN_RESOLUTION.md`): each strongly-connected component is resolved by a recorded move — decompose / invert / merge / cut (cut/merge human-gated) — and cycle-participating edges stay non-gating until resolved.
9. Current implementation truth lives in source, tests, build scripts, validation artifacts, and git history.

Guidance and history surfaces:

0. `plans/PLAN_2026-06-19_loop_first_pivot.md` is the completed D-APP-28 full loop-first pivot (tranches 28a..28e). It builds on `plans/DESIGN_2026-06-18_agent_orchestration_ui.md`, whose Phases 1-5 are complete. It was a routing/layout change only: the public UIEvent contract and permission plane stayed untouched, in-flight turns survive every relayout, and nothing was deleted. The plan did not itself approve default-provider cutover; that was separately ruled and landed under D-APP-18 (Option A, key-aware default).
0aa. `plans/PLAN_2026-06-17_live_packaged_agentsdk_read_tool_proof.md` is completed closed history. LP-00 landed D-APP-15 preparation, LP-01 landed the D-APP-15 Option A ruling, LP-02 landed the exact proof command/procedure, LP-03 consumed the approved live run but failed on selected-model availability/access before `Read` tool use, D-APP-16 approved one retry that also failed on model availability, and D-APP-17 approved bounded CLI alias troubleshooting that passed with `sonnet`. D-APP-18 has since been ruled Option A and its key-aware default-provider cutover has landed. The plan does not itself approve default-provider cutover (D-APP-18 does).
0a. `plans/PLAN_2026-06-17_r6_extensibility_mcp_boundary.md` is completed closed history after R6-05. It matured the local/in-process tool extension boundary (catalog, naming, collision prevention, contributor docs) and exposed no new capability; remote MCP, plugins, broad tool search, and domain tools remain out of scope (§7). R6-04 was deferred as optional organization work.
0b. `plans/PLAN_2026-06-16_runtime_stabilization.md` is completed closed history (tranches STAB-00..STAB-06), accepted by `D-APP-11` and closed by STAB-06. It records the current runtime stabilization evidence, D-APP-12 Option B hold ruling, and D-APP-13 mutating MCP ruling, but it is no longer an active tranche-selection queue.
1. `plans/PLAN_2026-06-16_six_node_scc_resolution.md` is the completed non-governing SCC-resolution plan. It records closure of the residual six-node strict dependency SCC; it is closed history and is no longer the active queue.
2. `plans/PLAN_2026-06-13_runtime_completion.md` is retired as the active queue and retained only as historical completion evidence for landed runtime work.
3. `plans/PLAN_COMPLETION_LOG.md` preserves landed-tranche narrative after plan rows are compressed.
4. `execution/_Coordination/_DECISIONS/_REGISTER.md` tracks human-gated decision-packet status. Agents prepare `PROPOSAL` packets; humans rule.
5. `execution/_Coordination/_LATEST.md` is a discovery pointer for coordination surfaces only. It is not authority and must not accumulate state history.
6. There is no active `NEXT_INSTANCE_STATE.md`; do not recreate it or use any hand-maintained coordination file as the app state.

When guidance surfaces disagree with authoritative surfaces, surface the discrepancy and correct the guidance surface. Do not silently rewrite authority.

## Baseline Intake

At the start of a new loop:

1. Read `{REPO_ROOT}/agents/AGENT_WORKING_ITEMS.md`.
2. Read `{WORKING_ROOT}/AGENTS.md`.
3. Act in the `WORKING_ITEMS` persona for `{WORKING_ROOT}`.
4. Read this file and `NEXT_INSTANCE_PROMPT.md`.
5. Read `execution/_Coordination/_LATEST.md` for discovery pointers only.
6. Read `plans/PLAN_2026-06-20_deliverable_inspection_and_development_evidence.md` as the active queue; read `plans/DESIGN_2026-06-18_agent_orchestration_ui.md`, `plans/PLAN_2026-06-19_loop_first_pivot.md`, `plans/PLAN_2026-06-17_live_packaged_agentsdk_read_tool_proof.md`, `plans/PLAN_2026-06-17_r6_extensibility_mcp_boundary.md`, and `plans/PLAN_2026-06-16_runtime_stabilization.md` as completed history and evidence context.
7. Read `_DECISIONS/_REGISTER.md` for ruled and pending human decisions. `D-APP-20` through `D-APP-33` are all ruled (key: D-APP-28 -> Option B full loop-first pivot; D-APP-30 -> B guard-mid-turn in-place launch; D-APP-31 -> B in-place `/pipeline` tertiary form staged with 28d; D-APP-32 -> A new sidebar tabs; D-APP-33 -> custom semantic/provisional-history normalization accepted for `INSP-01a`; chat history stays on the right as the existing Sessions tab, no left rail). `D-APP-14` accepted the now-completed R6 program; `D-APP-12` is ruled Option B (its hold on the default is now superseded by D-APP-18); `D-APP-13`, `D-APP-15`, `D-APP-16`, and `D-APP-17` are ruled and consumed; `D-APP-18` (default-provider cutover) is ruled Option A and its key-aware default cutover has landed.
8. Read `execution/_Reconciliation/DepClosure/_LATEST.md` and the latest dependency closure report when dependency/SCC state can affect tranche selection or blocker claims.
9. Read `execution/_ScopeChange/_LATEST.md` when provider, Pi, permission posture, decomposition amendment, or deliverable-local context alignment can affect the selected tranche.
10. Read `docs/PRD.md`, `docs/PLAN.md`, and `frontend/docs/harness/runtime_engine_contract.md` enough to confirm the selected tranche's runtime target.
11. Read selected deliverable-local `_DEPENDENCIES.md`, `Dependencies.csv`, `_STATUS.md`, `MEMORY.md`, `_run_records/**`, and review/evidence files only when the plan item or dependency evidence points to those surfaces.
12. Read `docs/VALIDATION_STRATEGY.md`, `docs/RELEASE_QUALITY_GATES.md`, and `docs/BUILD_AND_RELEASE.md` when selecting validation for governance, runtime, SDK/tool, network, packaging, build, or release-significant work.
13. Read `docs/AGENTIC_DEVELOPMENT_WORKFLOW.md` and `docs/README.md` when changing the coordination loop or docs index.
14. Read the implementation reference surfaces needed for the selected tranche.
15. Run `git status --short` before coordination-sensitive planning or edits.

## Active Development Loop

Use bounded app-integration tranches. The loop-first pivot plan `plans/PLAN_2026-06-19_loop_first_pivot.md` is complete and has no remaining unstarted tranche. Do not invent a replacement queue; select new work only from an explicit human direction or a newly accepted plan/ruling. Do not select from the completed live packaged proof plan, completed R6 program, completed Runtime Stabilization spine, closed SCC-resolution plan, or retired runtime completion plan.

A tranche is acceptable when it has:

- one clear objective tied to the human-selected active plan;
- a narrow write scope;
- a validation command or concrete manual verification target;
- all required human rulings recorded in `_DECISIONS/_REGISTER.md`;
- work contained within accepted professional-boundary, network, dependency, runtime, and release policy.

Default ordering:

1. Repair failing validation or incomplete evidence for already-landed runtime/control-plane work first if such a regression is found.
2. Do not rerun the live proof; D-APP-17 passed with `sonnet`.
3. D-APP-18 (default-provider cutover) is ruled Option A and its key-aware default has landed: with no explicit `CHIRALITY_HARNESS_PROVIDER`, the harness uses the real `agentSdk` path when an Anthropic key is configured (env or UI Settings) and `stub` otherwise; `stub` stays an explicit opt-in. What remains gated is provider expansion beyond the Anthropic path and release/distribution posture (signing/notarization/publication) — do not declare those without a fresh ruling.
4. Advance the active inspection queue (`plans/PLAN_2026-06-20_deliverable_inspection_and_development_evidence.md`, D-APP-19 Option D): D-APP-33 has ruled the `INSP-01a` semantic-history blocker, `INSP-01a` reran clean under that acceptance basis, `INSP-01` moved all 53 deliverables to `CHECKING` with owner-approved SHA `8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec`, `INSP-02` aligned PKG-00 to the accepted acyclic DepClosure snapshot, and `INSP-03` waves 001-003 completed PKG-00, PKG-01, and PKG-02 assessments (11/53) with index `plans/artifacts/insp03_assessment_index_2026-06-20.md`. Next selected work is continuing `INSP-03` with PKG-03. Issuance (`CHECKING -> ISSUED`) is deferred; do not issue any deliverable. The completed loop-first pivot is closed history.
5. For browser-verified tranches, stop the local Next dev server before running `npm run build`, `npm run desktop:pack`, or `npm run harness:validate:premerge` unless the command explicitly owns the server lifecycle; see `plans/PLAN_2026-06-19_validation_server_build_isolation.md`.
6. If any work requires remote MCP, plugins, broad tool search, domain tools, provider/network expansion beyond the bounded Anthropic path, release posture changes, or a new runtime roadmap, stop and require a fresh human ruling. (The default-provider cutover itself is ruled and landed under D-APP-18.)
7. Do not revive a completed/closed/retired plan or invent a replacement queue.

If dependency evidence is needed, use the latest DepClosure snapshot and selected deliverable-local dependency files to discover blockers. Do not infer project-wide blocked/unblocked state from a stale summary or from a hand-maintained coordination state file.

## Subagent Use

Spawn `TASK` agents only for separable implementation subscopes with explicit briefs and disjoint write scopes. Use fan-out/fan-in when the work naturally separates by subsystem, for example:

- runtime contract and event schema;
- SDK options and message mapping;
- session storage and replay;
- permission overlay and tool descriptor design;
- documentation / evidence update.

Every subagent brief must state:

- source files to read;
- files it may write;
- validation expected;
- whether it may modify production code or only produce assessment/docs.

Keep parallel write scopes disjoint.

This TASK restriction does not apply to final Git closeout. After a validated tranche, `WORKING_ITEMS` must autonomously hand off to a `CHANGE` agent/subagent for final Git/file-state review under `{WORKING_ROOT}/AGENTS.md` closeout discipline.

## Git And Validation Closeout

At the end of a validated tranche:

1. Run the tranche-specific verification.
2. Run broader checks when the tranche touches shared runtime behavior:
   - from `frontend/`: `npm run test`;
   - from `frontend/`: `npm run typecheck`;
   - from `frontend/`: `npm run harness:validate:premerge`;
   - from `frontend/`: `npm run instruction-root:integrity`.
3. For governance/control-plane-only tranches, run static governance checks and explicitly record that frontend tests were skipped because no runtime/source files changed.
4. Route build, packaging, and release-significant changes through `docs/VALIDATION_STRATEGY.md`, `docs/RELEASE_QUALITY_GATES.md`, and `docs/BUILD_AND_RELEASE.md`.
5. Completed plans are edited only for closeout corrections or explicit human-directed governance work. There is no active R6 plan after R6-05 closeout, no active live packaged proof plan after D-APP-17, and no remaining unstarted tranche in the completed loop-first pivot plan `plans/PLAN_2026-06-19_loop_first_pivot.md`.
6. Move landed narrative detail to `plans/PLAN_COMPLETION_LOG.md` when closing a tranche.
7. Update `_DECISIONS/_REGISTER.md` only when a decision packet or ruling state changes.
8. Update `execution/_Coordination/_LATEST.md` only when coordination or planning discovery surfaces change.
9. Do not update or recreate `NEXT_INSTANCE_STATE.md`.
10. Record any skipped checks and why.
11. Autonomously hand off to a `CHANGE` agent/subagent for final Git/file-state review under `{WORKING_ROOT}/AGENTS.md` closeout discipline.

Git closeout is source-control hygiene. Lifecycle issuance, release readiness, professional approval, certification, sealing, authentication, and code-compliance acceptance remain human-governed states.

## Human-Ruling Stops

Stop and surface a human-ruling request when further progress requires a change to:

- product runtime policy in `docs/PRD.md` or strategic roadmap policy in `docs/PLAN.md`;
- outbound network policy or shipped provider scope;
- package/runtime requirements for Pi-backed execution, which remains unapproved after D-APP-01 and D-APP-02;
- concrete non-Anthropic provider implementation, provider-network expansion, or provider routing beyond the current shipped Anthropic path;
- write/edit/bash/tool-execution exposure beyond the current approved plan item;
- the project-truth model for sessions, transcripts, chats, runtime logs, or completion logs;
- professional-boundary claims or release-readiness posture.

Record human-gated questions in `_DECISIONS/_REGISTER.md`.
