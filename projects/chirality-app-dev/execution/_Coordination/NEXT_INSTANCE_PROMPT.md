# NEXT INSTANCE PROMPT - Chirality App Dev

## Entry Protocol

1. Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`.
2. Set `WORKING_ROOT` to `{REPO_ROOT}/projects/chirality-app-dev`.
3. Read `{REPO_ROOT}/agents/AGENT_WORKING_ITEMS.md`.
4. Read `{WORKING_ROOT}/AGENTS.md`.
5. Act in the `WORKING_ITEMS` persona for `{WORKING_ROOT}`.
6. Read `{WORKING_ROOT}/execution/_Coordination/_COORDINATION.md`.
7. Read `{WORKING_ROOT}/execution/_Coordination/_LATEST.md` for discovery pointers only.
8. Read `{WORKING_ROOT}/plans/PLAN_2026-06-20_deliverable_inspection_and_development_evidence.md` as the active queue (D-APP-19 Option D inspection phase); read `{WORKING_ROOT}/plans/PLAN_2026-06-18_deliverable_issuance_and_evidence_consolidation.md` for the transposed materials and the eventual issuance follow-on; read `{WORKING_ROOT}/plans/DESIGN_2026-06-18_agent_orchestration_ui.md` and `PLAN_2026-06-19_loop_first_pivot.md` as the completed preceding arc, and `PLAN_2026-06-17_live_packaged_agentsdk_read_tool_proof.md`, `PLAN_2026-06-17_r6_extensibility_mcp_boundary.md`, and `PLAN_2026-06-16_runtime_stabilization.md` as completed history/evidence context.
9. Read `{WORKING_ROOT}/execution/_Coordination/_DECISIONS/_REGISTER.md`.
10. Discover current state from the authoritative surfaces named by `_COORDINATION.md`: governed docs, decomposition and deliverable artifacts, dependency/SCC snapshots, decision records, source, tests, validation evidence, and git history.
11. Read `{WORKING_ROOT}/execution/_Reconciliation/DepClosure/_LATEST.md` and the latest dependency closure report when dependency or SCC posture can affect blocker claims or selected-tranche scope.
12. Read the relevant authority and implementation-reference files named by `_COORDINATION.md`.
13. For validation, release-quality, build, packaging, network, or governance-control-plane work, read `docs/VALIDATION_STRATEGY.md`, `docs/RELEASE_QUALITY_GATES.md`, and `docs/BUILD_AND_RELEASE.md`.
14. For workflow or docs-index work, read `docs/AGENTIC_DEVELOPMENT_WORKFLOW.md`, `docs/README.md`, and `docs/MANIFEST.json`.
15. Record `git status --short` before coordination-sensitive planning or edits.

## Active Direction

The active development queue is the **deliverable INSPECTION & development-evidence program** — `plans/PLAN_2026-06-20_deliverable_inspection_and_development_evidence.md` (D-APP-19 Option D custom). It moves all 53 deliverables `IN_PROGRESS -> CHECKING` and inspects each at issuance-gate rigor to **form new evidence on how to proceed developing the application**, while evaluating whether the issuance-gate process is the one to keep. Issuance (`CHECKING -> ISSUED`) is **deferred** — the owner does not expect to close out deliverables yet. The preceding Agent-Orchestration UI & Information Architecture redesign (`plans/DESIGN_2026-06-18_agent_orchestration_ui.md`) is COMPLETE: Phases 1-5 plus the D-APP-28 loop-first pivot (live loop primary app-wide, right sidebar, Portal/Workbench/Pipeline as sidebar-reachable tertiary forms). The D-APP-18 default-provider cutover landed (key-aware default). Typecheck clean, 503 vitest pass, `next build` green, `desktop:pack` green after 28d.

The inspection tranche spine: INSP-00 -> INSP-00b (both LANDED 2026-06-20: D-APP-19 ruled Option D, this plan authored, prior plans superseded, coordination repointed) -> INSP-01a (normalize preflight) -> INSP-01 (move all 53 `IN_PROGRESS -> CHECKING` with the owner-blessed approvalSha) -> INSP-02 control-plane truth-fix -> INSP-03 per-deliverable inspection sweep, multi-agent -> INSP-04 gate-process evaluation -> INSP-05 development roadmap -> INSP-FINAL. **INSP-01a executed 2026-06-20, found a status-history preservation blocker, and reran clean under D-APP-33:** 52 `_STATUS.md` files contain one semantic/provisional noncanonical history bullet each that would be dropped by the writer; evidence is `plans/artifacts/insp01a_status_preflight_2026-06-20.md`; D-APP-33 ruled that those semantic/provisional history bullets do not need preservation (`execution/_Coordination/_DECISIONS/D-APP-33_RULING_2026-06-20.md`); rerun evidence is `plans/artifacts/insp01a_rerun_after_dapp33_2026-06-20.md` with zero unaccepted drops. **INSP-01 landed 2026-06-20** with owner-approved SHA `8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec`; evidence is `plans/artifacts/insp01_owner_approval_sha_2026-06-20.md`, `plans/artifacts/insp01_status_transition_evidence_2026-06-20.md`, and `plans/artifacts/insp01_status_transition_log_2026-06-20.json`; all 53 deliverables are `CHECKING`, 0 `IN_PROGRESS`, 0 `ISSUED`. **INSP-02 landed 2026-06-20** and aligned PKG-00 control-plane documents with accepted acyclic DepClosure snapshot `CLOSURE_SCC_SAFE_MOVES_001_2026-06-16_0325Z`; evidence is `plans/artifacts/insp02_control_plane_truth_fix_2026-06-20.md`. **INSP-03 waves 001-006 are recorded:** PKG-00 control-plane assessments DEL-00-01 and DEL-00-02, PKG-01 governance/reliance assessments DEL-01-01 through DEL-01-04, PKG-02 desktop shell/navigation/operator-state assessments DEL-02-01 through DEL-02-05, PKG-03 runtime engine assessments DEL-03-01 through DEL-03-04, PKG-04 SDK adapter / prompt / provider / settings assessments DEL-04-01 through DEL-04-05, and PKG-05 session audit / replay / tool-result assessments DEL-05-01 through DEL-05-05 are complete (25/53), 28 assessments remain pending, 0 deliverables are issued, reviewed SHA `18511e933233b90ff2a84dd41f5b40041719c300` is recorded for wave 006 as inspected source-state evidence, and the coverage index is `plans/artifacts/insp03_assessment_index_2026-06-20.md`. `CHECKING` means "admitted to inspection," not approved-for-issue, so 53xCHECKING is not 53 issuance approvals; `CHECKING` is one-way in code (reverting needs a manual `_STATUS.md` amend). No code development in this plan (the G1-G6 gaps are roadmap outputs); no `CHECKING -> ISSUED`; REF-006 / AMD-01 / PKG-10 doc-only basis remain separate later rulings. Next selected work: continue `INSP-03` with the PKG-06 wave.

D-APP-20 through D-APP-33 are ALL RULED (`execution/_Coordination/_DECISIONS/_REGISTER.md`). Key rulings: D-APP-28 -> Option B (full loop-first pivot); D-APP-30 -> B (guard-mid-turn in-place launch); D-APP-31 -> B (in-place `/pipeline` tertiary form, staged with 28d); D-APP-32 -> A (new sidebar tabs); D-APP-33 -> custom semantic/provisional-history normalization accepted for `INSP-01a`. Chat history stays on the RIGHT as the existing Sessions tab — no left rail (owner directive 2026-06-19). The Phase rulings D-APP-20..25 are ruled AND implemented.

D-APP-18 (default-provider cutover) is RULED Option A (2026-06-20) and the bounded cutover has LANDED. The harness now uses a **key-aware default** (`resolveHarnessProviderMode`, `lib/harness/runtime.ts`): with no explicit `CHIRALITY_HARNESS_PROVIDER`, it selects the real `agentSdk` path when an Anthropic API key is configured (env `ANTHROPIC_API_KEY`/`CHIRALITY_ANTHROPIC_API_KEY` or the UI Settings store) and falls back to `stub` when none is. `stub` remains an explicit opt-in via `CHIRALITY_HARNESS_PROVIDER=stub`; explicit `anthropic`/`agentSdk` still win. The provider manager is selected once at runtime construction, so adding a key after a keyless start needs an app restart to leave the stub. D-APP-18 does NOT approve provider expansion beyond the Anthropic path or any release/distribution posture (signing/notarization/publication) — those remain separately gated.

Completed closed history (retain as evidence, do not revive as a queue): the live packaged `agentSdk` read-tool proof (`plans/PLAN_2026-06-17_live_packaged_agentsdk_read_tool_proof.md`, where D-APP-17 passed with `sonnet`) and its `plans/artifacts/*` evidence; the R6 Extensibility & MCP Boundary Maturity program (`plans/PLAN_2026-06-17_r6_extensibility_mcp_boundary.md`, R6-04 deferred); the Runtime Stabilization program (`plans/PLAN_2026-06-16_runtime_stabilization.md`, STAB-00..06); `plans/PLAN_2026-06-16_six_node_scc_resolution.md`; and `plans/PLAN_2026-06-13_runtime_completion.md`.

Current stabilized runtime posture:

- a **governance / UI / audit / lifecycle / adapter layer over provider harness mechanics** — NOT a standalone general agent harness, and NOT a Claude Code / Pi / Codex feature-parity effort; generic harness primitives the adapter provides well are governed, not reimplemented (CONTRACT **K-ENGINE-6**);
- a Chirality-owned runtime contract and audit/event model;
- provider-adapter-general runtime architecture;
- Claude Agent SDK / Anthropic as the first concrete adapter, now the **key-aware default provider** per D-APP-18 (real `agentSdk` when an Anthropic key is configured, else `stub`); the earlier D-APP-12 Option B hold on the default is superseded for the default selection only;
- Pi retained as a pattern corpus / reference only, not an adapter, fork, package import, sidecar, or spike target; any other provider/harness path requires a fresh governed tranche.

## Selection Rules

The active queue is the deliverable-inspection program (`plans/PLAN_2026-06-20_deliverable_inspection_and_development_evidence.md`). **Next action is continuing `INSP-03` with the PKG-06 wave**: D-APP-33 ruled the INSP-01a semantic-history blocker, `INSP-01a` reran clean under that acceptance basis, `INSP-01` moved all 53 deliverables to `CHECKING` with owner-approved SHA `8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec`, `INSP-02` aligned PKG-00 to the accepted acyclic DepClosure snapshot, and `INSP-03` waves 001-006 completed PKG-00, PKG-01, PKG-02, PKG-03, PKG-04, and PKG-05 assessments (25/53) with reviewed SHA `18511e933233b90ff2a84dd41f5b40041719c300` recorded for wave 006 as inspected source-state evidence. The Agent-Orchestration redesign / loop-first pivot is complete history; do not select from it, from the completed live-proof / R6 / Runtime Stabilization / SCC / retired runtime-completion plans, or from the superseded issuance proposal (`plans/PLAN_2026-06-18_...`, its materials already transposed).

Default priority:

1. Repair failing validation for already-landed runtime/control-plane/UI work first if such a regression is found.
2. Advance the inspection tranche spine in order — INSP-03 -> INSP-04 -> INSP-05 -> INSP-FINAL — keeping each governance-gate / typecheck+vitest green as applicable, and stopping the dev server before any build/pack/premerge.
3. Issuance is DEFERRED: do NOT transition any deliverable `CHECKING -> ISSUED`, and do NOT pre-decide REF-006 (PRD-hash) / AMD-01 (UI render-test bar) / the PKG-10 doc-only basis — each is a separate later ruling informed by the inspection.
4. The owner confirms ONE blessed `approvalSha` (commit HEAD) before INSP-01; apply transitions mechanically (actor=HUMAN, the owner-blessed SHA), never mint a SHA or claim approval. `CHECKING` = admitted-to-inspection, not approved-for-issue.
5. No code development in this plan (G1-G6 are roadmap outputs; only the INSP-02 control-doc truth-fix is applied). Keep the public UIEvent contract, permission plane, and provider posture untouched; cross no `docs/PLAN.md` §11 fence. Apply the CONTRACT **K-ENGINE-6** strategic lens to every assessment and roadmap item — Chirality is a governance/UI/audit/lifecycle/adapter layer over provider harness mechanics; flag standalone-harness or Claude Code / Pi / Codex parity-chasing recommendations as OFF-STRATEGY.
6. D-APP-18 is RULED (Option A); its key-aware default cutover has landed. Provider/network EXPANSION beyond the Anthropic path and release/distribution posture remain separately gated — do not broaden providers or declare release readiness without a fresh ruling.
7. If any work requires remote MCP, plugins, broad tool search, domain tools, provider/network expansion, release posture changes, or a new runtime roadmap, stop and require a fresh human ruling.
8. Do not revive a completed/closed/retired/superseded plan or invent a replacement queue.

## Execution Rules

- The active queue is the deliverable-inspection program (`plans/PLAN_2026-06-20_deliverable_inspection_and_development_evidence.md`, D-APP-19 Option D); D-APP-33 ruled the `INSP-01a` semantic-history blocker, `INSP-01a` reran clean under that acceptance basis, INSP-01 moved all 53 deliverables to `CHECKING` with owner-approved SHA `8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec`, INSP-02 aligned PKG-00 to the accepted acyclic DepClosure snapshot, and INSP-03 waves 001-006 completed PKG-00, PKG-01, PKG-02, PKG-03, PKG-04, and PKG-05 assessments (25/53; reviewed SHA `18511e933233b90ff2a84dd41f5b40041719c300` recorded for wave 006 as inspected source-state evidence) with coverage index `plans/artifacts/insp03_assessment_index_2026-06-20.md`. Continue INSP-03 at the PKG-06 wave. The completed loop-first pivot, live-proof, R6, and Runtime Stabilization plans and the superseded issuance proposal no longer grant pre-approval for new work. `D-APP-13`..`D-APP-17` and D-APP-18 + D-APP-19 + D-APP-20..D-APP-33 are ruled; D-APP-18 (Option A) landed the key-aware default-provider cutover; D-APP-19 (Option D) opened the inspection phase with issuance deferred. Provider expansion beyond the Anthropic path and release posture remain separately gated.
- Do not read, update, or recreate `NEXT_INSTANCE_STATE.md`; current state is discovered from the dependency and authority surfaces named above.
- Spawn `TASK` agents only for separable subscopes with explicit briefs and disjoint write scopes.
- At validated closeout, autonomously hand off to a `CHANGE` agent/subagent for Git/file-state review under `{WORKING_ROOT}/AGENTS.md` closeout discipline. This closeout handoff is required and is not a substitute implementation tranche.
- Keep writes scoped to the selected tranche.
- For browser-verified tranches, stop the local Next dev server before running `npm run build`, `npm run desktop:pack`, or `npm run harness:validate:premerge` unless the command explicitly owns the server lifecycle; see `plans/PLAN_2026-06-19_validation_server_build_isolation.md`.
- Use `{REPO_ROOT}/../pi` and `plans/pi-agent-harness-assessment.md` only as read-only pattern-corpus references where they refine the active plan item.
- Do not perform provider-network, concrete non-Anthropic provider, Pi migrations, or new runtime roadmap work unless the active plan item and human rulings explicitly allow them. (The default-provider cutover is ruled and landed under D-APP-18; provider expansion beyond the Anthropic path is still gated.)
- D-APP-01 and D-APP-02 rule out Pi adapter, fork, import, Node 22 sidecar, runtime-floor migration, and immediate spike work. D-APP-03 approves provider-adapter generality only; concrete new providers require bounded future implementation tranches.
- Stop when any further progress requires a human ruling.

## Closeout

At completion of a validated tranche:

1. Run appropriate verification.
2. Route checks through `docs/VALIDATION_STRATEGY.md`, `docs/RELEASE_QUALITY_GATES.md`, and `docs/BUILD_AND_RELEASE.md` for build, packaging, or release-significant work.
3. Update the active plan and `plans/PLAN_COMPLETION_LOG.md` only when a selected tranche lands; completed plans are edited only for closeout corrections or explicit human-directed governance work.
4. Update `execution/_Coordination/_DECISIONS/_REGISTER.md` only when decision-packet state changes.
5. Update `execution/_Coordination/_LATEST.md` only when discovery pointers change.
6. Report skipped checks explicitly.
7. Hand off to a `CHANGE` agent/subagent for final Git/file-state review under `{WORKING_ROOT}/AGENTS.md` closeout discipline.

End the session summary with:

- completed tranche;
- validation performed;
- files changed;
- human rulings pending or blocking from `_DECISIONS/_REGISTER.md`;
- next selected work from the active inspection queue (`plans/PLAN_2026-06-20_deliverable_inspection_and_development_evidence.md`; continue `INSP-03` with the PKG-06 wave), and the state of open rulings (D-APP-19 ruled Option D, issuance deferred; D-APP-33 ruled; REF-006 / AMD-01 / PKG-10 doc-only basis still open).
