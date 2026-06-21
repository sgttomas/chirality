# NEXT INSTANCE PROMPT - Chirality App Dev

## Entry Protocol

1. Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`.
2. Set `WORKING_ROOT` to `{REPO_ROOT}/projects/chirality-app-dev`.
3. Read `{REPO_ROOT}/agents/AGENT_WORKING_ITEMS.md`.
4. Read `{WORKING_ROOT}/AGENTS.md`.
5. Act in the `WORKING_ITEMS` persona for `{WORKING_ROOT}`.
6. Read `{WORKING_ROOT}/execution/_Coordination/_COORDINATION.md`.
7. Read `{WORKING_ROOT}/execution/_Coordination/_LATEST.md` for discovery pointers only.
8. Read `{WORKING_ROOT}/plans/PLAN_2026-06-20_autonomous_development_queue.md` as the **active queue** (D-APP-39: autonomous pull-and-execute on everything except the hard fences, with autonomous commit+push); read `{WORKING_ROOT}/plans/artifacts/insp05_development_roadmap_2026-06-21.md` as its backlog source and `{WORKING_ROOT}/plans/PLAN_2026-06-20_deliverable_inspection_and_development_evidence.md` as the completed D-APP-19 inspection program; read `{WORKING_ROOT}/plans/PLAN_2026-06-18_deliverable_issuance_and_evidence_consolidation.md` for the transposed materials and the eventual issuance follow-on; read `{WORKING_ROOT}/plans/DESIGN_2026-06-18_agent_orchestration_ui.md` and `PLAN_2026-06-19_loop_first_pivot.md` as the completed preceding arc, and `PLAN_2026-06-17_live_packaged_agentsdk_read_tool_proof.md`, `PLAN_2026-06-17_r6_extensibility_mcp_boundary.md`, and `PLAN_2026-06-16_runtime_stabilization.md` as completed history/evidence context.
9. Read `{WORKING_ROOT}/execution/_Coordination/_DECISIONS/_REGISTER.md`.
10. Discover current state from the authoritative surfaces named by `_COORDINATION.md`: governed docs, decomposition and deliverable artifacts, dependency/SCC snapshots, decision records, source, tests, validation evidence, and git history.
11. Read `{WORKING_ROOT}/execution/_Reconciliation/DepClosure/_LATEST.md` and the latest dependency closure report when dependency or SCC posture can affect blocker claims or selected-tranche scope.
12. Read the relevant authority and implementation-reference files named by `_COORDINATION.md`.
13. For validation, release-quality, build, packaging, network, or governance-control-plane work, read `docs/VALIDATION_STRATEGY.md`, `docs/RELEASE_QUALITY_GATES.md`, and `docs/BUILD_AND_RELEASE.md`.
14. For workflow or docs-index work, read `docs/AGENTIC_DEVELOPMENT_WORKFLOW.md`, `docs/README.md`, and `docs/MANIFEST.json`.
15. Record `git status --short` before coordination-sensitive planning or edits.

## Active Direction

The deliverable INSPECTION & development-evidence program — `plans/PLAN_2026-06-20_deliverable_inspection_and_development_evidence.md` (D-APP-19 Option D custom) — is COMPLETE. It moved all 53 deliverables `IN_PROGRESS -> CHECKING`, inspected each at issuance-gate rigor, evaluated the gate process, produced a development roadmap, and deferred issuance (`CHECKING -> ISSUED`). D-APP-34 through D-APP-43 are now ruled. The **P0 governance cluster** from the roadmap has been APPLIED (commit `a5ccfc591`, 2026-06-20): D-APP-37 PKG-10 status-truth repair; D-APP-34/36 issue-readiness evidence profiles + AMD-01 UI render-test bar (`docs/ISSUE_READINESS_PROFILES.md`); and the D-APP-38 reference-integrity model (Option D hybrid) — a post-inspection audit found 6 of 7 authority-doc references stale (only REF-006 flagged), so a reconciliation tool (`execution/_Reconciliation/References/reconcile_authority_corpus.py`) + versioned corpus snapshots (`AUTHORITY_CORPUS.json`) were built, corpus `v1` established, and all deliverable references reconciled (0 `HASH_MISMATCH`). ADQ-05 later bumped the authority corpus to `v2` after D-APP-40 PRD/SPEC/TYPES edits and reconciled 153 deliverable reference rows.

**Operating mode: AUTONOMOUS (D-APP-39), currently exhausted.** The active queue is the autonomous development queue (`plans/PLAN_2026-06-20_autonomous_development_queue.md`). The `WORKING_ITEMS` persona ran in autonomous, multi-tranche mode until queue exhaustion. ADQ-12 is complete, all rows in the autonomous queue are `DONE`, and no eligible `READY` item remains. A future instance should stop after discovery unless a new roadmap item, ruling, or human directive adds work. The preceding Agent-Orchestration UI & Information Architecture redesign (`plans/DESIGN_2026-06-18_agent_orchestration_ui.md`) is COMPLETE: Phases 1-5 plus the D-APP-28 loop-first pivot (live loop primary app-wide, right sidebar, Portal/Workbench/Pipeline as sidebar-reachable tertiary forms). The D-APP-18 default-provider cutover landed (key-aware default). Typecheck clean, 503 vitest pass, `next build` green, `desktop:pack` green after 28d; ADQ-12 validation later passed 551 vitest tests, typecheck, Section 9, local package refresh, and premerge.

The inspection tranche spine: INSP-00 -> INSP-00b -> INSP-01a -> INSP-01 -> INSP-02 -> INSP-03
per-deliverable inspection sweep -> INSP-04 gate-process evaluation -> INSP-05
development roadmap -> INSP-FINAL. INSP-01a reran clean under D-APP-33; INSP-01 landed
2026-06-20 with owner-approved SHA `8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec`, leaving all 53
deliverables in `CHECKING`, 0 `IN_PROGRESS`, 0 `ISSUED`; INSP-02 aligned PKG-00 control-plane
documents with accepted acyclic DepClosure snapshot `CLOSURE_SCC_SAFE_MOVES_001_2026-06-16_0325Z`.

INSP-03 waves 001-011 are recorded: PKG-00 through PKG-10 assessments are complete (53/53), 0
assessments remain pending, 0 deliverables are issued, reviewed SHA
`0aea715f573cfd7759d7fe3f13ca03285b53ef98` is recorded for wave 011 as inspected source-state
evidence, and the coverage index is `plans/artifacts/insp03_assessment_index_2026-06-20.md`.
`CHECKING` means "admitted to inspection," not approved-for-issue, so 53xCHECKING is not 53 issuance
approvals; `CHECKING` is one-way in code (reverting needs a manual `_STATUS.md` amend). No code
development in this plan (the G1-G6 gaps are roadmap outputs); no `CHECKING -> ISSUED`; REF-006 /
AMD-01 / PKG-10 doc-only basis remain separate later rulings now mapped to D-APP-35 through D-APP-37.
`INSP-FINAL` closeout is recorded at `plans/artifacts/insp_final_closeout_2026-06-21.md`. `INSP-04`
gate-process evaluation prepared D-APP-34; it is now ruled Option B. `INSP-05` development roadmap
synthesis prepared D-APP-35 through D-APP-37; they are now ruled Option A, Option B, and Option A
respectively.

D-APP-20 through D-APP-43 are ALL RULED (`execution/_Coordination/_DECISIONS/_REGISTER.md`). Key rulings: D-APP-28 -> Option B (full loop-first pivot); D-APP-30 -> B (guard-mid-turn in-place launch); D-APP-31 -> B (in-place `/pipeline` tertiary form, staged with 28d); D-APP-32 -> A (new sidebar tabs); D-APP-33 -> custom semantic/provisional-history normalization accepted for `INSP-01a`; D-APP-34 -> B evidence profiles; D-APP-35 -> A refresh accepted PRD hash (subsumed by D-APP-38); D-APP-36 -> B component/render tests; D-APP-37 -> A PKG-10 doc-only acceptance profile; D-APP-38 -> D hybrid reference-integrity model (reconciliation tool feeding versioned corpus snapshots; authority-doc edits trigger a corpus version bump); D-APP-40 -> B dedicated `turn.interrupted`; D-APP-41 -> D eager legacy session conversion; D-APP-42 -> A SHA-256 tool-artifact metadata with session-lifetime retention; D-APP-43 -> 1B/2B/3B permission/tool closure semantics for interrupted tool results, PreCompact/Stop adapter lifecycle mapping, and strict workspace/tool behavior. D-APP-34/36/37 were APPLIED and D-APP-38 corpus `v1` reconciled in commit `a5ccfc591` (the P0 governance cluster); ADQ-05 later reconciled D-APP-38 corpus `v2`. Chat history stays on the RIGHT as the existing Sessions tab — no left rail (owner directive 2026-06-19). The Phase rulings D-APP-20..25 are ruled AND implemented. ADQ-05, ADQ-08, ADQ-09, ADQ-10, ADQ-11, and ADQ-12 are complete; the autonomous queue has no eligible `READY` item.

D-APP-18 (default-provider cutover) is RULED Option A (2026-06-20) and the bounded cutover has LANDED. The harness now uses a **key-aware default** (`resolveHarnessProviderMode`, `lib/harness/runtime.ts`): with no explicit `CHIRALITY_HARNESS_PROVIDER`, it selects the real `agentSdk` path when an Anthropic API key is configured (env `ANTHROPIC_API_KEY`/`CHIRALITY_ANTHROPIC_API_KEY` or the UI Settings store) and falls back to `stub` when none is. `stub` remains an explicit opt-in via `CHIRALITY_HARNESS_PROVIDER=stub`; explicit `anthropic`/`agentSdk` still win. The provider manager is selected once at runtime construction, so adding a key after a keyless start needs an app restart to leave the stub. D-APP-18 does NOT approve provider expansion beyond the Anthropic path or any release/distribution posture (signing/notarization/publication) — those remain separately gated.

Completed closed history (retain as evidence, do not revive as a queue): the live packaged `agentSdk` read-tool proof (`plans/PLAN_2026-06-17_live_packaged_agentsdk_read_tool_proof.md`, where D-APP-17 passed with `sonnet`) and its `plans/artifacts/*` evidence; the R6 Extensibility & MCP Boundary Maturity program (`plans/PLAN_2026-06-17_r6_extensibility_mcp_boundary.md`, R6-04 deferred); the Runtime Stabilization program (`plans/PLAN_2026-06-16_runtime_stabilization.md`, STAB-00..06); `plans/PLAN_2026-06-16_six_node_scc_resolution.md`; and `plans/PLAN_2026-06-13_runtime_completion.md`.

Current stabilized runtime posture:

- a **governance / UI / audit / lifecycle / adapter layer over provider harness mechanics** — NOT a standalone general agent harness, and NOT a Claude Code / Pi / Codex feature-parity effort; generic harness primitives the adapter provides well are governed, not reimplemented (CONTRACT **K-ENGINE-6**);
- a Chirality-owned runtime contract and audit/event model;
- provider-adapter-general runtime architecture;
- Claude Agent SDK / Anthropic as the first concrete adapter, now the **key-aware default provider** per D-APP-18 (real `agentSdk` when an Anthropic key is configured, else `stub`); the earlier D-APP-12 Option B hold on the default is superseded for the default selection only;
- Pi retained as a pattern corpus / reference only, not an adapter, fork, package import, sidecar, or spike target; any other provider/harness path requires a fresh governed tranche.

## Selection Rules

The deliverable-inspection program (`plans/PLAN_2026-06-20_deliverable_inspection_and_development_evidence.md`) is complete: D-APP-33 ruled the INSP-01a semantic-history blocker, `INSP-01a` reran clean under that acceptance basis, `INSP-01` moved all 53 deliverables to `CHECKING` with owner-approved SHA `8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec`, `INSP-02` aligned PKG-00 to the accepted acyclic DepClosure snapshot, `INSP-03` waves 001-011 completed PKG-00 through PKG-10 assessments (53/53) with reviewed SHA `0aea715f573cfd7759d7fe3f13ca03285b53ef98` recorded for wave 011 as inspected source-state evidence, `INSP-04` produced `plans/artifacts/insp04_gate_process_evaluation_2026-06-21.md`, `INSP-05` produced `plans/artifacts/insp05_development_roadmap_2026-06-21.md`, `INSP-FINAL` recorded closeout, and D-APP-34 through D-APP-37 are now ruled. The Agent-Orchestration redesign / loop-first pivot is complete history; do not select from it, from the completed live-proof / R6 / Runtime Stabilization / SCC / retired runtime-completion plans, or from the superseded issuance proposal (`plans/PLAN_2026-06-18_...`, its materials already transposed).

The active queue is the **autonomous development queue** (`plans/PLAN_2026-06-20_autonomous_development_queue.md`, released by D-APP-39 on 2026-06-20): pull-and-execute on everything except the hard fences, with autonomous commit+push.

Default priority:

1. Repair failing validation for already-landed runtime/control-plane/UI work first if such a regression is found.
2. **Pull-and-execute (D-APP-39):** select the highest-priority `READY`, `AUTONOMOUS` item from the autonomous queue whose prerequisites are met (recompute readiness; do not trust recorded status if the filesystem disagrees); execute it, pass the Section 4 validation gates, then commit and push the validated tranche (stage only `projects/chirality-app-dev/`; abort if any path outside it is staged). Repeat until only blocked/fenced items remain, then stop and surface the decision/blocker queue.
3. **Hard fences (always stop and require a human ruling):** provider/network expansion beyond the Anthropic path; release/distribution posture (signing/notarization/publication/external distribution/release-readiness/professional/certification claims); R7 domain-engine implementation (PKG-10 stays doc-only); any `CHECKING -> ISSUED` issuance. Split a fenced sub-part off an otherwise-eligible item and defer it.
4. **Governance-decision gate (do not self-rule):** a genuinely new decision (a design fork with material trade-offs not covered by an existing ruling) is raised as a `PROPOSAL` packet under `_DECISIONS/`; mark that item `BLOCKED` and continue with other eligible items. **Never author a `*_RULING_*.md`, set a register row to `RULED`, or record an owner-attributed `Ruling basis` — only the owner rules.** Any option preference goes inside the `PROPOSAL` packet, explicitly marked `PROVISIONAL — AWAITING RULING`. A *general* owner steer (e.g. "favor long-term consistency") is not a ruling on any specific fork and never licenses selecting Option A/B/C/D on the owner's behalf; the dependent item stays `BLOCKED` until the owner records an explicit per-decision selection. (Precedent: the 2026-06-21 self-recording of D-APP-40/41/42/43 as `RULED` was a gate breach; the picks were later owner-ratified on their merits, but the queue should have left those items `BLOCKED`.)
5. Code development IS in scope under the autonomous queue, gated by Section 4 validation (typecheck + tests + build/premerge + the D-APP-36 render bar for UI). Keep the public UIEvent contract and permission plane intact unless an item eligibly changes them within fence limits. Apply the CONTRACT **K-ENGINE-6** strategic lens to every item — Chirality is a governance/UI/audit/lifecycle/adapter layer over provider harness mechanics; treat standalone-harness or Claude Code / Pi / Codex parity work as OFF-STRATEGY and do not build it.
6. D-APP-18 is RULED (Option A); its key-aware default cutover has landed. Provider/network EXPANSION beyond the Anthropic path and release/distribution posture remain hard fences (rule 3) — do not broaden providers or declare release readiness without a fresh ruling.
7. If any work requires remote MCP, plugins, broad tool search, domain tools, provider/network expansion, release posture changes, or a new runtime roadmap, stop and require a fresh human ruling.
8. Do not revive a completed/closed/retired/superseded plan or invent work outside the queue's backlog and the INSP-05 roadmap.

## Execution Rules

- The active queue is the autonomous development queue (`plans/PLAN_2026-06-20_autonomous_development_queue.md`, D-APP-39), but it is exhausted: all ADQ rows are `DONE`, and no eligible `READY` item remains. Stop after discovery unless new work is added by a roadmap update or human directive. The deliverable-inspection program (D-APP-19 Option D) and its P0 governance cluster are complete. The completed loop-first pivot, live-proof, R6, and Runtime Stabilization plans and the superseded issuance proposal no longer grant pre-approval for new work. `D-APP-13`..`D-APP-17` and D-APP-18 + D-APP-19 + D-APP-20..D-APP-43 are ruled; D-APP-18 (Option A) landed the key-aware default-provider cutover; D-APP-19 (Option D) ran the inspection phase with issuance deferred; D-APP-39 released the autonomous queue. Provider expansion beyond the Anthropic path and release posture remain hard fences.
- Do not read, update, or recreate `NEXT_INSTANCE_STATE.md`; current state is discovered from the dependency and authority surfaces named above.
- Spawn `TASK` agents only for separable subscopes with explicit briefs and disjoint write scopes.
- At validated closeout, autonomously hand off to a `CHANGE` agent/subagent for Git/file-state review under `{WORKING_ROOT}/AGENTS.md` closeout discipline, then **commit and push the validated tranche (D-APP-39)**: stage only `projects/chirality-app-dev/<scoped paths>`, run `git diff --cached --name-only` and abort if any path is outside `projects/chirality-app-dev/` (never commit `projects/chirality-piping/**` or repo-root `tools/**`), commit with a message ending in the `Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>` trailer, `git push origin main`, and confirm sync. One commit per validated tranche.
- Keep writes scoped to the selected tranche.
- For browser-verified tranches, stop the local Next dev server before running `npm run build`, `npm run desktop:pack`, or `npm run harness:validate:premerge` unless the command explicitly owns the server lifecycle; see `plans/PLAN_2026-06-19_validation_server_build_isolation.md`.
- Use `{REPO_ROOT}/../pi` and `plans/pi-agent-harness-assessment.md` only as read-only pattern-corpus references where they refine the active plan item.
- Do not perform provider-network, concrete non-Anthropic provider, Pi migrations, or new runtime roadmap work unless the active plan item and human rulings explicitly allow them. (The default-provider cutover is ruled and landed under D-APP-18; provider expansion beyond the Anthropic path is still gated.)
- D-APP-01 and D-APP-02 rule out Pi adapter, fork, import, Node 22 sidecar, runtime-floor migration, and immediate spike work. D-APP-03 approves provider-adapter generality only; concrete new providers require bounded future implementation tranches.
- When editing an authority document (`docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, `docs/PLAN.md`, `docs/PRD.md`), run the D-APP-38 reference reconciliation as part of closeout: `python3 execution/_Reconciliation/References/reconcile_authority_corpus.py status`, then `bump` and `apply` to mint a new corpus version and re-reconcile deliverable `_REFERENCES.md` (the model is hybrid: edits are allowed and trigger a version change). See `docs/ISSUE_READINESS_PROFILES.md` §6.
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
- the ruling state (D-APP-19 ruled Option D, issuance deferred; D-APP-33..D-APP-43 ruled; D-APP-39 released the autonomous queue) and which autonomous-queue items advanced this session;
- the queue-exhausted state or any newly blocked/fenced items, so the next session does not revive completed work.
