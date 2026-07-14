# Root Governance Loop Receipts

> **Epistemic status: derivative handoff ledger — not authority.** Append-only.
> Current state is always re-derived from live decisions, accepted snapshots,
> Git, project loops, and deterministic checks. On disagreement, those sources
> govern.

## Rules

1. **Pointer, not narrative.** Prefer artifact paths, decision IDs, commit
   SHAs, PR numbers, run IDs, and project receipt IDs.
2. **Owner directions verbatim.** Quote chat-only owner direction exactly when
   it is not captured in another governed artifact.
3. **Checks as summaries.** Record pass/fail and an evidence pointer; detailed
   counts belong in the evidence package.
4. **Map deltas, never rewrites.** Record a one-line pointer when a plan or old
   receipt disagrees with live state.
5. **Gate outcomes with reasons.** State executed, parked, failed, or awaiting
   owner and identify the releasing act.
6. **No simulated execution.** A brief, plan, or placeholder directory is not
   a child run. Cite only real `AgentRuns/<RunID>` records.
7. **Capped.** Keep each receipt to roughly 6–12 lines; put detail elsewhere.

## Receipts

### Receipt 0 — 2026-07-12 — Stage-1 candidate machinery prepared

- Basis: `origin/main@67ba77e5107f941e6fcc7382ef467b6b018e972d`.
- Worktree/branch: `chirality-sow-stage1` / `codex/deliverable-sow-stage1`;
  candidate snapshot `c4c5dd2df0d7b5424d48672c38d1eef37262e2f6`.
- Authority: owner instruction to implement the Stage-1 plan; pilot variance
  remains inactive pending D-GOV-15 ruling.
- Evidence: sizing report, four-document consumer inventory, proposed D-GOV-15,
  candidate standard, registered skill/tools, and App Dev feature-gated reader.
- Checks: root Python suites `347 passed`; App Dev `703 passed, 4 skipped`;
  typecheck, agent/skill/entrypoint/path validators, export regeneration, and
  `git diff --check` passed.
- State: `AWAITING_OWNER`; no pilot deliverable, `_STATUS.md`, historical
  receipt, TYPES, or SPEC content was changed.
- Release gate: explicit APPROVED/AMENDED ruling on the nine-item D-GOV-15
  slate and SHA-bound publication before any pilot worktree conversion.

### Receipt 1 — 2026-07-12 — D-GOV-15 approved; execution deferred

- Owner ruling: "I rule APPROVED for all nine. Incorporate this, but do not
  proceed with implementation."
- Decision: `D-GOV-15`, proposed snapshot
  `c4c5dd2df0d7b5424d48672c38d1eef37262e2f6`, published ruling
  `58aa81d62f4a32e3c2d687e4356a1e4be8141674`; all nine items approved.
- Effect: the exact pilot variance and Stage-1 execution contract are
  authorized, but no pilot worktree or conversion was started in this session.
- State: `HANDOFF_READY`; next session must inspect live Git/project-loop state,
  publish a versioned orchestration plan, and execute the calibration gate
  before any frozen-schema wave.
- Stop gate remains: no candidate pilot deliverable merges to `main`; stop for
  D-GOV-16 after preservation audit and Stage-2 evidence assembly.

### Receipt 2 — 2026-07-12 — Stage-1 PASS; D-GOV-16 proposed

- Basis: frozen `main@2770fda4c63c98ee9f18cffbafd14c9aa59f497f`; ruled
  D-GOV-15 `58aa81d62f4a32e3c2d687e4356a1e4be8141674`; proposal snapshot
  `a43b7431b7ec3be8b250042bf83fcf02f2fe78c8`.
- Pilot evidence: App `fb83ffca8a7f674db13c6cda775ca7b7d7c8ef26`; Piping
  `31c35ea9798c29cd0af16b7089186f3942dcfcb1`; neither branch is merged.
- Result: 10 candidates, 325/325 PRESERVED mappings and 3,466/3,466 source
  lines; statuses/sources preserved; no fresh conversion or verifier rerun.
- Governance correction: deterministic AC checklist compiler is authoritative;
  REVIEW consumes it and reserves judgment for human-gated review.
- Checks: root tools 785 passed; full preservation, consumer, HTML, agent,
  skill, path, export, App, and Piping evidence PASS; substrate fallback is
  separately recorded from schema/content PASS.
- Handoff: RECONCILIATION PASS and D-GOV-16 proposal/evidence package are
  decision-ready. Stage 2, canon application, corpus conversion, and pilot
  integration remain unauthorized pending the owner ruling.

### Receipt 3 — 2026-07-12 — D-GOV-16 patch-artifact revision

- Proposal revision: `31e5efd986b7c59fc709f4fe967575c59659aae0` re-encodes
  only the inactive TYPES/SPEC unified-diff artifacts as whitespace-clean
  zero-context patches; their target bytes are unchanged.
- Validation: both patches reproduce their prior targets and pass
  `git apply --unidiff-zero --check` against a tree read directly from frozen
  `main@2770fda4c63c98ee9f18cffbafd14c9aa59f497f`.
- Handoff: D-GOV-16 binds this revised proposal snapshot. No RECON evidence,
  project/pilot path, ratified canon, lifecycle, integration, or Stage-2 act
  changed; the owner ruling remains the sole release gate.

### Receipt 4 — 2026-07-12 — D-GOV-16 binding identity correction

- Correction: the full SHA for the Receipt 3 proposal revision is
  `31e5efd985db4cc7b25543e11a65933979e07e4f`; its earlier expansion was
  recorded incorrectly while sharing the same abbreviated prefix.
- Effect: D-GOV-16 and current handoff state now bind the verified commit.
  No proposal artifact, target byte, validation result, RECON evidence,
  project/pilot path, ratified canon, lifecycle, integration, or Stage-2 act
  changed; the owner ruling remains the sole release gate.

### Receipt 5 — 2026-07-12 — D-GOV-16 items 1–10 approved

- Owner ruling: "I rule APPROVED for D-GOV-16 items 1–10 exactly as proposed.
  Publish the ruling, then stop before Stage-2 implementation until a fresh
  governed orchestration plan is presented from synchronized main."
- Basis: proposal snapshot
  `31e5efd985db4cc7b25543e11a65933979e07e4f`; ruling publication SHA is
  `PENDING_PUBLICATION` until CHANGE binds it.
- Effect: exact successor-standard bytes ratified; exact TYPES/SPEC patch bytes
  approved but unapplied; items 3–10 approved exactly as recorded.
- Stop: no Stage-2 implementation, conversion, consumer migration, pilot
  integration, lifecycle act, or legacy retirement in the publication run.
- Release gate: present a fresh governed orchestration plan derived from a
  synchronized `main` that contains the published ruling.

### Receipt 6 — 2026-07-12 — D-GOV-16 ruling SHA binding

- Binding: Receipt 5's owner ruling is published at
  `7584718aa32b112e415331736d1a8e68c12ac176`; the D-GOV-16 decision and
  register now cite that full SHA.
- State: `D-GOV-16_RULED_STAGE2_PLAN_REQUIRED`; the exact standard is ratified
  and exact TYPES/SPEC patches remain approved but unapplied.
- Stop: publication is not Stage-2 implementation. A fresh governed plan from
  synchronized `main` remains the only release gate.

### Receipt 7 — 2026-07-12 — D-GOV-16 Stage-2 plan presented

- Basis: synchronized `main@c9af689118e4e87f329e1ab4c6e71fea331b2674`;
  plan snapshot `27f03730c956447b9a9696422cc9c63b8f061939` on
  `codex/sow-stage2-plan`.
- Evidence: `AgentRuns/SOW-STAGE2-PLAN-20260712/`, with sealed plan, graph,
  census, caller, traceability, and handoff outputs.
- Checks: 10/10 D-GOV-16 traceability; 10 pilots + 143 ordinary + 1 ISSUED =
  154; sealed output hashes match the ORCHESTRATOR return.
- State: `STAGE2_PLAN_PRESENTED_AWAITING_ACCEPTANCE`; no Stage-2 node was
  dispatched and no canon, project, lifecycle, pilot, or remote state changed.
- Release gate: human accepts or amends this plan, then a fresh governed
  execution run reruns synchronized-main basis checks before dispatch.

### Receipt 8 — 2026-07-12 — D-GOV-16 Stage-2 root loop activated

- Authority: owner direction “proceed accordingly,” recorded in
  `SOW-STAGE2-PLAN-20260712/PLAN_ACCEPTANCE.md`; plan acceptance is not H1/H2.
- Binding: loop activation snapshot
  `1eebc67ca0ce82bb2ae320fec49b1568fa037ba1` establishes the deterministic
  `LOOP_INIT.md` → `CURRENT_WORKPLAN.md` → Stage-2 workplan chain.
- Checks: target containment, launcher immutability, and all four sealed
  ORCHESTRATOR loop-output hashes PASS.
- State: `STAGE2_LOOP_ACTIVE — READY_FOR_FRESH_EXECUTION_SESSION`; no Stage-2
  node ran, and H1/H2 remain unapproved.
- Release gate: a fresh governed execution run repeats Step 0 synchronized-main
  and census/caller preflight before it may dispatch a dependency-released node.

### Receipt 9 — 2026-07-13 — Piping PKG-00 excluded from Stage-2 conversion

- Owner ruling: Piping PKG-00 is retained upstream governance/architecture
  context, not a conversion package; actual packages must incorporate it and
  PKG-00 must depend on no other package or deliverable.
- Plan effect: tracked census remains 154; conversion population is 146;
  ordinary waves are 135; P1 begins at PKG-01 with 22 members split 3/5/8/6.
- Evidence: revised P1 preflight PASS, 198/198 bindings, all PKG-01–17 with
  active upstream PKG-00 basis, zero PKG-00 outbound contradictions; snapshot
  manifest `3fad35f47088b1f1968bd2f8cef8b2fed3659891a4e96abffac88521fbb8ed77`.
- Handoff: `WORKING-P1-PKG01` is next eligible but undispatched at the owner's
  requested conversation boundary. PKG-02–04 remain serially parked; H1/H2
  remain unapproved; no project, lifecycle, or dependency-truth edit occurred.
- Git binding: the exact 58-path control-plane closeout was committed and
  pushed on synchronized `main` at
  `25bbb8b65f157ea522fe3e70bbca47cd0160cc33`.

### Receipt 10 — 2026-07-13 — Agentic runtime hardening complete

- Authority: owner direction captured at
  `AgentRuns/SOW-RUNTIME-HARDENING-20260713-01/HUMAN_DIRECTION.md`.
- Implementation: managed-service project checks, run-contained runtime
  telemetry, and narrowed rare-escape RECON contract at
  `aa41b254233dcfcf5ca90c4ede1b40a865784a3c`.
- Checks: 19 focused tests; agent/path/entrypoint validation PASS; cold-substrate
  App premerge PASS at 8 Section-8 + 16 report-only Section-9 tests; manifest
  8/8.
- State: `CLOSED — HOLD_FOR_HUMAN`; Piping execution, deliverables, lifecycle,
  H1/H2, PKG-00, candidates, release, and retirement were unchanged.
- Next gate: fresh human instruction; Piping does not resume automatically.

### Receipt 11 — 2026-07-14 — Clean Scope-of-Work production boundary complete

- Authority: owner direction recorded in
  `AgentRuns/SOW-CLEAN-PRODUCTION-20260714-01/HUMAN_DIRECTION.md`.
- Implementation: evidence-rich migration candidates are now deterministically
  finalized into separate clean production contracts; migration metadata is
  externalized and downstream evidence binds the production hash, at
  `8a8a3ee79aa8daa0a9909d7d624ad691530bfbc9`.
- Checks: 19 focused tests; skill, agent, path, entrypoint, compilation, and
  whitespace validation PASS; all 60 prepared candidates finalize with 1,841
  source blocks and zero compatibility findings.
- State: `CLOSED — HOLD_FOR_HUMAN`; prepared candidates require fresh
  finalization and rebinding before later integration. Piping execution,
  project content, lifecycle, H1/H2, integration, and retirement remain
  unchanged and parked.

### Receipt 12 — 2026-07-14 — Package-batch method adopted; PKG-01/02 integrated

- Authority: owner accepted both bounded package experiments, their documented
  whitespace warnings, and the PKG-01/02 integration; PKG-00 remains excluded.
- Binding: PR #227 merged as `4296d3f4069b838ae2e0d1c4845ebe0b944aece9`;
  both required checks passed on its final head.
- Result: eight ordinary Piping members are clean `SOW_V1`; 32 legacy files
  were removed and 40 control/dependency files remained byte-identical.
- Method: one package manager, bounded package author, fresh 100% verifier, and
  narrowed exception/final-member RECON are now the standing ordinary workflow.
- Next: P1 PKG-03 is dependency-released as two consecutive batches,
  `DEL-03-01..05` (1,267 lines) and `DEL-03-06..08` (699 lines).
- Gates: `DEL-01-01` H1, lifecycle, release, retirement, and H2 remain parked.

### Receipt 13 — 2026-07-14 — PKG-03 prepared; RECON child gate blocked

- Basis: synchronized `main@5f124ad80fe84357f6dc33072dc4fbdbeb05d545`; graph v38 and session handoff at `snapshots/W_P1/PKG03-session-blocked/HANDOFF_STATE.md`.
- WORKING_ITEMS PASS: 8/8 members, 234 mappings, 1,966/1,966 lines, exact 40-row replacement/inverse manifests, 8/8 simulations, and 264/264 tests; no project write.
- RECON Agent-1 full-package reproduction PASS: five manifests / 3,610 rows, all members, simulations, 16/16 negatives, checks, and before/after project-tree containment reproduced.
- Gate: three mandatory evidence-only Agent-2 launches failed `agent thread limit reached`; the frozen brief is not treated as execution or acceptance.
- State: `BLOCKED_WITH_HANDOFF`; PKG-03 integration and PKG-04 remain held. No commit, push, PR, merge, lifecycle, H1/H2, release, or retirement act occurred.
- Rerun: free one governed child slot, execute the unchanged RECON verifier brief, validate fan-in, and mint a new immutable acceptance snapshot before CHANGE.

### Receipt 14 — 2026-07-14 — PKG-03 RECON blocked continuation

- Fresh drift audit on synchronized `main@5f124ad80fe84357f6dc33072dc4fbdbeb05d545` passed: snapshot 102/102, upstream manifests 3,610/3,610, all live and candidate bindings unchanged.
- Evidence: `snapshots/W_P1/PKG03-session-blocked/CONTINUATION_20260714_01.md`; ten-file standard/tool digest `a13c842bef5a563a64a644e2046ece18d892fec1828e006f9c6e6c91488e20a2`.
- Gate: the unchanged mandatory RECON Agent-2 launch was again rejected before execution with `agent thread limit reached`; completed upstream sessions remain counted.
- State remains `BLOCKED_WITH_HANDOFF`; no acceptance snapshot, CHANGE action, project write, lifecycle act, commit, push, PR, merge, H1/H2, release, or retirement act occurred.
- Rerun remains: one genuinely available governed child slot, actual verifier execution, validated fan-in, then a new immutable acceptance snapshot.

### Receipt 15 — 2026-07-14 — PKG-03 runtime blocker formally terminal

- Basis and unchanged RECON child brief reconfirmed at `main@5f124ad80fe84357f6dc33072dc4fbdbeb05d545` and SHA-256 `71608e216b47498cbb3bcae1ca9a2f297d2c9cb2348005f9967b9d191567c51f`.
- Third consecutive goal-turn launch was rejected before execution: `collab spawn failed: agent thread limit reached`.
- Evidence: `snapshots/W_P1/PKG03-session-blocked/CONTINUATION_20260714_02.md`; no prior evidence was rewritten and no substitute child execution was claimed.
- State: formally `BLOCKED_WITH_HANDOFF`; PKG-03 acceptance/integration and all declared dependants remain held.
- Resume condition: external runtime capacity change providing one genuine child slot, followed by unchanged verifier execution, validated fan-in, and a new immutable acceptance snapshot.

### Receipt 16 — 2026-07-14 — Piping PKG-03 integrated

- Authority: the human clarified the manager topology, directed deterministic
  evidence normalization instead of stopping, and granted blanket approval to
  merge this run's PR after required checks passed.
- Binding: ready PR #228 passed `governance-harness / harness` on source head
  `413c7765c7df85a8a9ad6ef4e424f896f801e065` and merged as
  `2826a12ba3f53720312737bd6e1480dc62d57a37`.
- Result: eight PKG-03 members are clean `SOW_V1`; the project delta is exactly
  eight additions plus 32 legacy deletions, with all 40 status/control/
  dependency files byte-identical.
- Evidence: 234 mappings, 1,966/1,966 source lines, 8/8 simulations, exact
  40-row replacement/inverse manifests, 3,734 rebound manifest rows, 264
  practitioner tests, and 20 export/Scope-of-Work tests pass. The exact
  pre-normalization state remains at `ce4ea40f2`.
- State: PKG-03 integration is closed and PKG-04 is released. `DEL-01-01`, H1,
  lifecycle, release, retirement, and H2 remain parked.

### Receipt 17 — 2026-07-14 — Piping PKG-04 integrated; P1 handoff ready

- Binding: ready PR #229 passed `governance-harness / harness` on source head
  `f2b1d22bd4c84298ba5b9eb4f133a82904086f79` and merged as
  `4c945be4c049b3ea04205f5de047d2c14d055754`.
- Result: six PKG-04 members are clean `SOW_V1`; the project delta is exactly
  six additions plus 24 legacy deletions, with all 30 status/control/
  dependency files byte-identical.
- Evidence: 178 mappings, 1,368/1,368 source lines, 6/6 simulations, exact
  30-row replacement/inverse manifests, 1,766 scoped binding rows, 264
  practitioner tests, and 20 export/Scope-of-Work tests pass. Two terminal-LF
  findings were mechanically fixed before freeze with exact byte deltas bound.
- Handoff: `snapshots/W_P1/PKG04-integration-postmerge/`, manifest SHA-256
  `e590866ae070c5284d6a19c9c61f34b6d9e0304667563086dbd2d41c341b4387`.
- State: PKG-04 integration is closed and the P1 postmerge handoff is ready for
  HELP_HUMAN fan-in. `DEL-01-01`, H1, lifecycle, release, retirement, and H2
  remain parked.
