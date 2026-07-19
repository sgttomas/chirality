# Sealed Launch Brief — N1 GOV-WRITES (D-APP-52 live-demonstration closures)

- **Parent:** HELP_HUMAN (Agent 0), RunID `DAPP52_LIVE_DEMONSTRATION_2026-07-18`
- **Child role:** Agent 1, WORKING_ITEMS posture (PKG-04 / PKG-10 deliverable
  state), mechanical conformance to this brief; closure decisions were made by
  the orchestrator under the D-APP-64 overlay and the owner's in-session act.
- **Repo root:** current working tree, branch `claude/dapp52-live-demonstration`.
- **Source summaries (session-temp, read-only inputs; copy verbatim):**
  - PACK1 `…/scratchpad/dapp52-live-sdk-probe/summary.json`
  - PACK2 `…/scratchpad/dapp52-live-llm-demo/summary.json`
  - PACK3 `…/scratchpad/dapp52-packaged-live-proof/summary.json`
  where `…` = `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-help-human-agent-setup-b9bff5/fb6fcf91-eadf-42ba-bf6b-7921bf796aa0`.
  Before copying, independently confirm each contains no `sk-ant-` secret
  material (they were secret-scanned at capture; re-grep to be sure).
- **Write scope (nothing else):** DEL-04-01, DEL-04-03, DEL-04-05 kit files
  named below under `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/`;
  DEL-10-03 kit files under `…/PKG-10_Domain_Engine_Future_Boundary/1_Working/`;
  one run record in DEL-04-01 `_run_records/`.
- **Prohibitions:** no `_DomainEngines/**`, no piping/pec writes, no
  `_STATUS.md` state/lifecycle transitions (`IN_PROGRESS` and every
  `Checking Approval SHA` stay untouched), no receipts, no register writes, no
  frontend writes, no commit/stage/push. Record no claim beyond the facts
  below.

## Established live facts (2026-07-18; owner at screen; code SHA at capture `a91f72b19aeb6dbca7e565fe336c91ce7e841421`; model `claude-sonnet-5`)

**PACK1 — dev SDK probe** (`frontend/scripts/run-dapp52-live-sdk-probe.mjs`, new; status pass; redaction scan pass):
- Pinned `@anthropic-ai/claude-agent-sdk@0.3.150`; **claudeCodeVersion 2.1.150**; node v24.5.0; darwin:arm64.
- Live `query()` message sequence (phase 1): `system/init` → `assistant` (thinking block) → `assistant` (tool_use `Read`) → `user` (tool_result) → `assistant` (text) → `result/success` with `is_error:false`; every message carries `session_id`.
- `result` message top-level keys observed: `api_error_status, duration_api_ms, duration_ms, fast_mode_state, is_error, modelUsage, num_turns, permission_denials, result, session_id, stop_reason, subtype, terminal_reason, total_cost_usd, ttft_ms, type, usage, uuid`.
- Session/transcript placement: transcript JSONL at `CLAUDE_CONFIG_DIR/projects/<escaped-cwd>/<session-uuid>.jsonl`; config dir also gains `.claude.json`, `backups/`, `policy-limits.json`; controlled `HOME` stays empty; project cwd untouched beyond the read target.
- Live error shapes: invalid key → repeated `system/api_retry` events `{attempt, max_retries:10, retry_delay_ms, error_status:401, error:"authentication_failed"}` then a synthetic assistant message and `result{subtype:"success", is_error:true, api_error_status:401, result:"Failed to authenticate. API Error: 401 API key is invalid."}`; unreachable base URL → `api_retry` with `error_status:null, error:"unknown"`; abort → thrown `Error("Claude Code process aborted by user")`. RATE_LIMITED was NOT triggered live (bounded, recorded as such — no fabricated shape).
- Interrupt behavior (REQ-010): abort after init ends the stream after three messages with the same abort error; no partial result message.

**PACK2 — live-LLM pec demonstration** (`frontend/scripts/run-dapp52-live-llm-demo.ts`, new; status pass; redaction pass):
- A live model session (claude-sonnet-5) itself called `mcp__chirality__domain_propose_operation` (propose, then mode "refresh") and `mcp__chirality__domain_proposal_validate` (twice) through the in-process Chirality MCP server against a D-PEC-06-guarded scratch pec server on `127.0.0.1:4909` (projectId 2, synthetic CSV only).
- Envelopes: proposalId 1 (ref IPR-0001); engine.version 2 before refresh → 4 after; envelope keys `{engine, inputs, mode, ok, profileId, resultSemantics, toolId, transportStatus}`; `resultSemantics` verbatim: "transport/evidence envelope only; no domain verdict; a green dry-run is NOT acceptance — acceptance and application are human acts in pec behind admin-only RBAC (K-DOMAIN-3/K-DOMAIN-4)".
- NO accept, screen act, or apply occurred; `force` was never used in any form; scratch server stopped and DB (+wal/shm) deleted after capture; agent credentials runtime-generated, local-env only, secret-scanned absent from artifacts. Terminal `result/success`, `is_error:false`.
- This discharges exactly the act the D-APP-52 packet deferred ("live-LLM demonstration through a harness model session").

**PACK3 — packaged live proof** (`frontend/scripts/run-live-packaged-agent-sdk-read-tool-proof.mjs`, existing, vs a fresh `desktop:pack` bundle; status pass; redaction pass): packaged SDK 0.3.150 / claudeCodeVersion 2.1.150, platform binary `@anthropic-ai/claude-agent-sdk-darwin-arm64` under `app.asar.unpacked/node_modules`; live sequence `init → assistant → user → assistant → result/success`; Read tool use and proof token observed; no error result.

**D-APP-63 rider check (performed):** no DEL-04-04 (PersonaComposer / instruction-root)-relevant output was produced by any pack — no new row is minted.

## Task A — evidence files

1. Copy PACK1 → `DEL-04-01_SDK_Probe_and_Version_Pinned_Adoption_Decision/Evidence_DAPP52_LIVE_PROBE_2026-07-18_summary.json`; PACK3 → `…/Evidence_DAPP52_PACKAGED_LIVE_PROOF_2026-07-18_summary.json` (byte-verbatim copies; record each file's SHA-256).
2. Write `…/Evidence_DAPP52_LIVE_PROBE_2026-07-18.md`: authority line (D-APP-52 ruling O-A riders 1–11; the deferred live-LLM demonstration executed as the owner's in-session act 2026-07-18, owner at screen, short-lived owner-supplied key never persisted); the PACK1 + PACK3 facts above (sequence, result keys, placement, error shapes, interrupt, packaged proof), each traceable to the JSON artifacts by SHA-256; a "not evidenced" paragraph (RATE_LIMITED shape not live-triggered; no adoption-verdict, release, or professional claim; rider check outcome recorded).
3. Copy PACK2 → `DEL-10-03_OperationProposal_Record_and_Human_Gate_Workflow/Evidence_DAPP52_LIVE_LLM_DEMO_2026-07-18_summary.json`; write `…/Evidence_DAPP52_LIVE_LLM_DEMO_2026-07-18.md` with the PACK2 facts (basis, actors, model-driven acts table in stream order with message indexes, demo-cast section stating NONE occurred and force never used, teardown, deferred-statement discharge, boundaries respected: riders 2/3/5/8/9 and F-APP-3 — evidence home is this deliverable folder per the D-APP-64 selection recorded in the run record; `_DomainEngines/**` untouched).

## Task B — dependency closures

In DEL-04-01 `Dependencies.csv` (follow the DEP-04-01-010 closure precedent for cell formats; keep column count intact):
- **DEP-04-01-007** → SatisfactionStatus `SATISFIED` (and the row's closure convention as used for 010): all four recorded needs now stand — pins, deterministic harness, packaging posture (ADQ-15), and the last residual, live Claude Code subprocess version **2.1.150**, live-confirmed in Evidence_DAPP52_LIVE_PROBE_2026-07-18.md. Resolve `TBD` TargetLocation to that evidence file.
- **DEP-04-01-011** → `SATISFIED`: the exact observed live `query()` message sequence is now recorded (same evidence file); consumption basis Evidence_HANDOVER_CONSUMPTION_2026-07-18.md section B stands.
- **DEP-04-01-013** → `SATISFIED`: live-confirmed SDK error object shapes AND packaged live behavior both recorded (Evidence_DAPP52_LIVE_PROBE + Evidence_DAPP52_PACKAGED_LIVE_PROOF). Note plainly: RATE_LIMITED not live-triggered; DEL-04-05 RQ-011 four-class assertion gap remains that deliverable's own gated item.
- Consumer mirrors: DEL-04-03 `Dependencies.csv` **DEP-04-03-007** and DEL-04-05 `Dependencies.csv` **DEP-04-05-007** → `SATISFIED` with matching notes citing the DEL-04-01 evidence file.
- Sync all three kits' `_DEPENDENCIES.md` tables (ACTIVE/SATISFIED/TBD counts) and append one dated note each describing this pass.

## Task C — `_STATUS.md` Remaining updates (content only; state untouched)

- DEL-04-01: remove the two D-APP-52-gated Remaining items (rows 011/013 closure item; CODEV-001 live-environment residuals item) — both discharged; leave every other Remaining item untouched; append one dated History line (owner act; packs; rows closed; rider check: no DEL-04-04-relevant output, no new row).
- DEL-10-03: remove the "Run the D-APP-52 live-LLM demonstration…" Remaining item (discharged); other items (DEP-10-03-004 ruling; open_pipe_stress transport) stay verbatim; append one dated History line.

## Task D — run record

`DEL-04-01/_run_records/TASK_RUN_2026-07-18_DAPP52_live_demonstration_closures.md`:
basis (owner act + D-APP-52 ruling + D-APP-64 overlay), the three packs with
status and artifact SHAs, the closures performed, the rider check, and TWO
D-APP-64 attribution blocks (schema from the D-APP-64 packet §5.3,
`OwnerStandingApproval: D-APP-64 §3`, `AgentJudgment: SELECT_AND_ADVANCE`,
`OwnerCaseSelection: NONE`, `EffectStatus: EFFECTIVE`, `RationaleArtifact:`
this run record):
1. Evidence-home selection — deliverable-folder homes; rejected: pec-loop
   `_DomainEngines/pec/` surface (F-APP-3 fence for this loop; pec loop may
   mirror under its own authority).
2. Full closure of DEP-04-01-013 after running the packaged proof against a
   fresh bundle — rejected: narrowing the row to a packaged-live residual
   (unnecessary once the proof passed) and closing without packaged evidence
   (would overstate). Also record the model-id substitution
   (claude-sonnet-4-20250514 → claude-sonnet-5 after a live 404) as an
   ordinary in-run fact, not a separate exercise.

## Return contract

Final message (data): files written with paths; per-copied-JSON SHA-256; the
Dependencies.csv cell-level changes (old → new per row); confirmation that no
`_STATUS.md` state line or `Checking Approval SHA` changed
(`git diff` derived); confirmation nothing outside the write scope was
touched; any deviation reported, not improvised.
