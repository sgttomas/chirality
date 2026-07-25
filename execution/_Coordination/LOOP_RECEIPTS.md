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

### Receipt 18 — 2026-07-14 — DEL-01-01 H1 evidence prepared

- P1 acceptance: all 22 ordinary PKG-01–04 members are single-format
  `SOW_V1`; status/lifecycle are preserved; excluded `DEL-01-01` remains exact
  legacy-only `ISSUED`; PKG-00 remains upstream-only context.
- I0 preparation: fresh author, fresh verifier, manager fan-in, and direct
  RECONCILIATION all pass for the exact clean production candidate
  `23d92ddeb0cc4e3fe37694b1c8b79284017799cd08caaaad9767c8a4f0121f21`.
- Evidence: 335/335 upstream bindings; 27/27 preserved mappings; 272/272
  physical source lines; exact five-row replacement/inverse; apply/rollback;
  six negative probes; fresh 19, 20, and 264-test suites; zero semantic
  additions, project writes, blockers, conflicts, waivers, or unknowns.
- Acceptance: normalized, rebound RECON snapshot manifest
  `802656d604adcaed53bdfd6789a79d852da77dc252382387954f369fe603bc74`;
  HELP_HUMAN evidence acceptance and decision slate are under
  `snapshots/I0/H1_EVIDENCE/`.
- State: `H1_EVIDENCE_PREPARED — AWAITING_ISSUED_ADMINISTRATIVE_APPROVAL`.
  H1 is unapproved; integration, reissue, reauthentication, lifecycle action,
  release, reliance, retirement, and H2 remain prohibited.

### Receipt 19 — 2026-07-14 — DEL-01-01 H1 approved

- Owner ruling: “I APPROVE H1 for the exact DEL-01-01 representation
  replacement bound at commit
  `054ef5dd2de62f0803569573e162d613258b1b40`.” The owner also agreed with the
  governed pause because the deliverable was `ISSUED` and directed the goal to
  resume.
- Effect: authorize only the exact five-row replacement using clean production
  SHA-256 `23d92ddeb0cc4e3fe37694b1c8b79284017799cd08caaaad9767c8a4f0121f21`,
  with `_STATUS.md` byte-identical and lifecycle preserved as `ISSUED`.
- Sequence: bind the ruling on synchronized main before releasing I1 CHANGE.
- Fences: no candidate regeneration, semantic modification, reissue,
  reauthentication, lifecycle change, release, reliance, rollback, retirement,
  or H2 authorization is implied.

### Receipt 20 — 2026-07-14 — DEL-01-01 integrated; closure released

- Binding: ready PR #230 passed `governance-harness / harness` on exact source
  head `41c65bd1f862701314b9c98df216cd8dbdcfe0a5` and merged cleanly as
  `6d56a1b6f391d21618f3328179d5a48654aec422`.
- Result: the H1-authorized project delta is exactly one clean
  `ScopeOfWork.md` addition plus four legacy deletions; `_STATUS.md` remains
  byte-identical and lifecycle remains `ISSUED`.
- Evidence: exact five-row replacement/inverse, live clean-format validation,
  rollback simulation without execution, 20 root tests, 264 practitioner
  tests, root validators, and whole-diff hygiene pass. One terminal-LF evidence
  defect was mechanically normalized before source freeze with exact hashes
  retained.
- Handoff: `snapshots/I0/integration/postmerge/`. Cross-wave 146-member
  conversion/rollback closure is released. Legacy compatibility remains live;
  retirement is prohibited until a separate fresh H2 human ruling.

### Receipt 21 — 2026-07-14 — W-P2 integrated; P3 released

- Binding: ready PR #231 passed `governance-harness / harness` on source head
  `3ea904a6e6228a93f8b0dd9c5ff84c235fa194b3` and merged as
  `7b5f27c17f425c1e1f8e47f4e81200b070227f69`.
- Result: 29 PKG-05–09 members are clean `SOW_V1`; the project delta is
  exactly 29 additions plus 116 legacy deletions, with all status/control/
  dependency/lifecycle bytes preserved.
- Evidence: 919 mappings, 8,203/8,203 source lines, 29/29 simulations, exact
  145-row replacement/inverse manifests, 264 practitioner tests, 20 export/
  Scope-of-Work tests, root validators, and postmerge checks pass.
- Handoff: `snapshots/W_P2/integration/postmerge/`.
- State: W-P2 integration is closed and W-P3 is released. W-P4, conversion
  closure, rollback execution, retirement, and H2 remain parked.

### Receipt 22 — 2026-07-14 — W-P3 integrated; P4 released

- Binding: ready PR #233 passed `governance-harness / harness` on source head
  `2628c4ec68d65c7fa422c202d12f95d11b9e456b` and merged as
  `b999fbd24852aa6acee36a61c2f049c7a2e6fa36`.
- Result: 15 PKG-10–12 members are clean `SOW_V1`; the project delta is
  exactly 15 additions plus 60 legacy deletions, with all status/control/
  dependency/lifecycle bytes preserved.
- Evidence: 493 mappings, 4,919/4,919 source lines, 15/15 simulations, exact
  75-row replacement/inverse manifests, 264 practitioner tests, 20 export/
  Scope-of-Work tests, root validators, and isolated postmerge checks pass.
- Handoff: `snapshots/W_P3/integration/postmerge/`, manifest SHA-256
  `15affcebf7c766a27879e90f39891b0d9035268475a0ae35452f2a1d2ca5918f`.
- Portability closeout: three ignored compiled-residue rows were removed from
  the current PKG-10 author and PKG-12 verifier manifests; both package
  manifests were rebuilt and all ten current package/child manifests pass
  8,796 existence/byte/hash bindings with zero candidate or project change.
- State: W-P3 integration is closed and W-P4 is released. Conversion closure,
  rollback execution, retirement, and H2 remain parked.

### Receipt 23 — 2026-07-14 — W-P4 integrated; conversion closure released

- Binding: ready PR #235 passed `governance-harness / harness` on source head
  `0abe2c611e8a74f7cbacae1e7b7fe4381930413f` and merged as
  `e87c2ef9453ba2deafb30fa996937bffd4466e23`.
- Result: 22 PKG-14–17 members are clean `SOW_V1`; the project delta is
  exactly 22 additions plus 88 legacy deletions, with all status/control/
  dependency/lifecycle bytes preserved.
- Evidence: 729 mappings, 6,759/6,759 source lines, 22/22 simulations, exact
  110-row replacement/inverse manifests, 264 practitioner tests, 20 root
  tests, four validators, and isolated postmerge checks pass.
- Handoff: `snapshots/W_P4/integration/postmerge/`, manifest SHA-256
  `157c0b673eb447506916c70eaf1aac37a05ab08618e9dcb6f0ed73c915304570`.
- State: W-P4 integration is closed and conversion closure is released to
  consume the accepted wave handoffs. Rollback execution, retirement, and H2
  remain parked.

### Receipt 24 — 2026-07-14 — Clean-production residue repaired

- Finding: fresh pre-repair closure managers identified 57 live production
  contracts retaining migration-only candidate metadata: all 53 App members
  and four Piping PKG-13 pilots. All other closure gates passed.
- Repair: direct WORKING_ITEMS applied only the registered deterministic
  finalizer; fresh RECONCILIATION reproduced all 57 outputs and reports from
  basis blobs, preserving 1,753 source blocks with zero semantic rewrite.
- Integration: ready PR #237 passed both `governance-harness / harness` and
  `Harness pre-merge`, then merged as
  `74b9804cf62c014118ad222699a3591fdf5bda42`. Closeout PR #238 passed its
  required harness and merged as
  `79de30d83b91a2ab468a3f17536a5233c2f85fe7`.
- Binding: immutable repair-integration manifest SHA-256
  `6bca228f08e34094e538c81d905f3efe4b50de990ccca16f69daed8394cc9dd8`.
  H2 and legacy retirement were untouched.

### Receipt 25 — 2026-07-14 — Conversion and rollback closure accepted

- Basis: exact
  `origin/main@79de30d83b91a2ab468a3f17536a5233c2f85fe7`.
- RECONCILIATION: fresh independent PASS; 154-member census, 146 clean
  `SOW_V1`, eight exact PKG-00 exemptions, lifecycle 153 `IN_PROGRESS` plus
  sole issued `DEL-01-01`, zero residue, 730 unique inverse rows, 146 rollback
  round trips, callers, compatibility, and all root/App/Piping checks pass.
  Snapshot manifest SHA-256
  `7975141369025a50087c6f8d94b51d59740d0adabb49576518c9c4d7926add27`.
- EVALUATION: fresh independent PASS with no blockers, waivers, or material
  unknowns. Snapshot manifest SHA-256
  `3a17c5b5637216b74018206a931a4a01fb6c90769094ac77d4a3c57da47b133f`.
- State: `CONVERSION_CLOSED — LEGACY_RETIREMENT_RULING_REQUIRED`. H2 is a
  fresh human decision; silence performs no retirement.

### Receipt 26 — 2026-07-14 — H2-R approved; compatibility retained

- Owner ruling: “I APPROVE H2-R at commit
  `92725eace3ef50306bf0c09032bc59492e636c01`.”
- Effect: retain the eight ruled Piping PKG-00 legacy contracts, the
  compatibility-only `four-documents` skill, legacy validator, active
  format-aware callers, and full 730-row human-gated rollback support.
- Writes authorized: ruling record, closure pointer, work graph, receipt, and
  handoff only. No project, skill, tool, caller, lifecycle, rollback,
  historical-evidence, or retirement implementation write is authorized.
- State: `STAGE2_CLOSED — H2-R COMPATIBILITY RETAINED`; legacy retirement is
  `RETAINED_NOT_AUTHORIZED`.

### Receipt 27 — 2026-07-15 — PKG-00 reversal aligned

- Owner direction: reverse the PKG-00 file-disposition portion of H2-R,
  retain the D-43 consolidation merged as
  `291301291bdaa8ec6b64dbbf3cff98ecfeadeca7`, assess the resulting state,
  and proceed with the narrow current-reading alignment. No root compatibility
  machinery retirement or lifecycle act was directed.
- Result: all eight Piping PKG-00 members remain reference-only
  `ArchitectureBasis.md` members; sealed revision-0.7 `_CONTEXT.md` surfaces
  are marked superseded for current consumption, current dependency/reference
  navigation is aligned to DAG-007 and decomposition revision 0.9, and a
  separate fail-closed ArchitectureBasis validator is live.
- Historical boundary: Receipt 26, the accepted Stage-2 workplan, frozen H2-R
  evidence, `MEMORY.md`, semantic derivatives, run records, and immutable
  DAG-007 were not rewritten. Root four-document compatibility and rollback
  machinery remains retained pending a separate human ruling.
- Checks: eight-member validator PASS; Piping 498/498 tests PASS; strict
  canonical DAG-007 PASS (1,480 edges, 101 nodes, zero endpoint/canonical/SCC/
  duplicate/bidirectional findings); practitioner harness 264/264 PASS;
  self-check exit 0 with the pinned non-blocking baseline.
- State: `CLOSED_CURRENT_STATE_ALIGNED`; future compatibility retirement, DAG
  successor publication, PDU-007, and TP-SEAM-WASM-001 remain parked at their
  named authority gates.

### Receipt 28 — 2026-07-15 — Pilot source references retired

- Owner direction, verbatim: “I'm not really bothered about retaining pilot
  evidence, so long as the actual work isn't missing without them. Just change
  the record to explain the evidence wasn't preserved but the human approved
  its removal or something like that.”
- Verification: all six App PKG-07 and four Piping PKG-13 production members
  match the accepted conversion-closure status/contract hashes, validate as
  `SOW_V1`, and contain no legacy four-document files on
  `main@c7e88216baf32acd27e34f3e64851b0918c33a75`.
- Disposition: local-only pilot refs `fb83ffca8...` and `31c35ea97...` were
  owner-approved for removal; their branch-resident evidence is not durably
  retained. The evidence-package index records the resulting rerun boundary.
- Boundary: no production, lifecycle, semantic, closure-snapshot, or
  historical run-record content changed.

### Receipt 29 — 2026-07-22 — D-GOV-18 agent-index re-disposition executed

- Owner ruling, verbatim: "I APPROVE D-GOV-18 items 1–8 at commit
  `9a900b3b76dda415cc4d41185350eb2e5a436302`" (2026-07-21). Owner directions
  recorded in-run: PR #302 merge; session-scoped self-merge grant for
  subsequent PRs on green checks; path-bounded variance, verbatim: "I grant
  the variance: PR-3 may edit persona-resolution.ts and its test to map
  ORCHESTRATE to PROJECT_SETUP."
- Execution: five sequential PRs under run
  `execution/_Coordination/AgentRuns/AGENT-INDEX-REDISPOSITION-20260721/`.
  PR #302 (D-GOV-18 ruling, register, matrix, run scaffold); PR #303
  (AGENT_CHANGE.md slim 477→151, authority semantics retained); PR #304
  (EVALUATION shell 155→112 + new `evaluation-protocol` skill, frontmatter
  byte-identical); PR #305 (atomic ORCHESTRATOR→PROJECT_SETUP rename: 43+3
  files, validator delegation-edge key, OWNER_WORKFLOWS legacy shim, plus the
  two-file App Dev variance edit); PR-4 (this closeout: Function 5 moved
  PROJECT_SETUP→HELPS_HUMANS remove+add atomically, App Dev handoff notice).
- Deviations recorded: PR #304 was merged while `Harness pre-merge` was red
  (chained merge command; the failure was a `managed-delegation.test.ts`
  concurrency flake, 5/5 local passes, CI re-run green); corrective
  explicit-verdict-gate rule adopted and held for PR #305 and PR-4. D-GOV-18
  Item 6's no-CI-breakage premise was falsified by the App Dev matrix guard
  and resolved by the owner variance above.
- Checks at each merge: validate_agent_instructions 33/0/0;
  validate_skill_metadata 45/0; practitioner harness 311/311 (incl. GEN-9);
  harness self-check exit 0; App Dev `Harness pre-merge` green at final states.
- Open follow-ons (recorded, unscheduled): App Dev doc-alias updates
  (TYPES.md:132, PRD.md:519/134) per
  `AgentRuns/AGENT-INDEX-REDISPOSITION-20260721/notices/APPDEV-ORCHESTRATOR-RENAME-HANDOFF.md`;
  AUDIT_DECOMP undeclared-caller hygiene (REVIEW/SCOPE_CHANGE frontmatter);
  tools/decomp gate-seed old-name refresh; optional AGENT_REVIEW.md legacy
  Reviews note; AGENT_WORKING_ITEMS.md does not name NEXT_INSTANCE_STATE.md
  though two files assert it updates that file (pre-existing gap).
- State: `AGENT-INDEX-REDISPOSITION_CLOSED` — index now: PROJECT_SETUP
  (renamed/narrowed), EVALUATION (thin shell + skill), CHANGE (slimmed),
  REVIEW/SCOPE_CHANGE (ruled SAFE), Function 5 owned by HELPS_HUMANS. No
  lifecycle act, specialist removal, or historical rewrite occurred.

### Receipt 30 — 2026-07-22 — Deviation corrections directed; follow-ons extended

- Owner direction, verbatim: "Apply the branch protection and fold in #2 plus
  the flaky-test note into the existing follow-on list."
- Branch protection: a required-status-checks rule on `main` (contexts
  `harness` and `Harness pre-merge`, enforce_admins true) was directed;
  application from the executing session was blocked by local tool
  permissions, so the exact `gh api` command was returned to the owner for
  direct application. Until it is applied, red-check merges remain
  mechanically possible and are barred only by the recorded
  explicit-verdict-gate discipline.
- Follow-on list (Receipt 29) extended with two items: (a) a one-line
  standing rule in `agents/AGENT_CHANGE.md` merge semantics — inspect check
  verdicts explicitly before executing any merge; never chain a merge behind
  a watch — a governed agent-instruction edit for a future small tranche;
  (b) App Dev `frontend/src/__tests__/lib/managed-delegation.test.ts`
  ("atomically reserves concurrent sibling write targets") is
  concurrency-flaky under CI load and should be deflaked by the App Dev loop,
  especially once required status checks make every flake a merge blocker.
- Discoverability note: root LOOP_INIT step 2 mandates reading the newest
  LOOP_RECEIPTS.md entry each session, so this list is guaranteed surfaced to
  the next root loop. The App Dev items reach the App Dev loop by root relay
  (Agent 0 notice routing), not by App Dev's own bootstrap; the root loop's
  first return should carry them forward until the App Dev loop records them.

### Receipt 31 — 2026-07-22 — Deflake brief issued; protection application interrupted

- Owner direction, verbatim: "draft the sealed brief for the App Dev tranche
  now (diagnosis summary, suspected fix pattern, stress-verification
  acceptance criteria) and drop it alongside the existing handoff notice.
  Then run the 'require only harness' command now for immediate protection
  with zero risk of stuck PRs, and treat the both-checks-plus-no-op-job setup
  as the recorded hardening follow-on to do alongside the deflake."
- Sealed brief issued:
  `AgentRuns/AGENT-INDEX-REDISPOSITION-20260721/notices/APPDEV-MANAGED-DELEGATION-DEFLAKE-BRIEF.md`
  — root cause verified in `managed-delegation.ts` (non-atomic in-place
  STATUS.json overwrites, L624-625/L662/L667, racing the sibling
  disjointness scan); fix pattern: atomic temp+rename status writes plus a
  disjoint-siblings-both-succeed test; acceptance: ≥300-iteration stress
  passes under CPU constraint. Adoption remains the App Dev loop's act.
- Branch protection: the require-only-`harness` application first failed on
  an expired GitHub CLI token (HTTP 401); after owner re-authentication the
  API returned HTTP 403 "Upgrade to GitHub Pro or make this repository
  public to enable this feature" — branch protection and rulesets are
  unavailable on this private free-plan repository. Mechanical enforcement
  therefore requires an owner decision: upgrade the account to GitHub Pro or
  make the repository public. Until one is taken, red-check merges stay
  barred only by the recorded explicit-verdict-gate discipline and the
  pending CHANGE standing-rule follow-on.
- Hardening follow-on (recorded): strict protection requiring `Harness
  pre-merge` as well, paired with an always-run no-op reporting job in
  `harness-premerge.yml` so path-filtered PRs cannot hang; sequenced AFTER
  the deflake lands (a flaky required check is a merge blocker).

### Receipt 32 — 2026-07-22 — Branch protection applied

- Owner act: upgraded the account to GitHub Pro, unblocking branch
  protection on this private repository (closes the Receipt 31 plan-gate
  finding).
- Applied and verified on `main`: required status check `harness`
  (runs on every PR), `strict: false`, `enforce_admins: true` — red-check
  merges are now mechanically refused for all tokens, including admin.
  The PR carrying this receipt is the first merge governed by the rule.
- Remaining in sequence (unchanged from Receipt 31): App Dev
  managed-delegation deflake per the sealed brief, then optionally the
  strict hardening (`Harness pre-merge` added as a required context plus an
  always-run no-op reporting job in `harness-premerge.yml`); the CHANGE
  merge-verdict standing rule remains a recorded governed-edit follow-on.

### Receipt 33 — 2026-07-25 — D-GOV-21 ruled and effective; loop reoriented to root product development

- Owner acts of record (in-session, 2026-07-25), verbatim where quoted:
  ruling "I rule APPROVED for O-A against candidate SHA
  c038c493e871c95871823281b45890ba9404624b" (published:
  `docs/governance_harness/_DECISIONS/D-GOV-21_root_working_root_exception.md`);
  "Merge the branch and report the EffectiveSHA" (merge of PR #338 executed
  at that direction → EffectiveSHA
  `ee42157290618e3f84be0e0b651c041387ad6ee0`); "Proceed with the
  reorientation tranche. Remain in the Agent 0 posture, Use `opus-5` models
  for Agent 1 and Agent 2 instances."
- This tranche (run `ROOT-LOOP-REORIENT-20260725`, single-node terminal
  fan-out/fan-in): Agent 1 PROJECT_SETUP (`opus-5`) authored
  `WORKPLAN_2026-07-25_root_product_development.md` and moved the
  `CURRENT_WORKPLAN.md` pointer to it (Status `ACTIVE — ROOT PRODUCT
  DEVELOPMENT`); Agent 0 validated fan-in (V1 gates: exact two-file diff,
  pointer resolution, G0 PASS idle, path anchors PASS 992) and executed the
  disjoint N2 record-keeping: EffectiveSHA backfill into the D-GOV-21
  decision record and implementation handoff (`f1549afb1` precedent).
- D-GOV-21 sequence state: steps 1–3 complete at the EffectiveSHA; step 4
  complete when this tranche merges; steps 5 (candidate root PRD) and 6
  (guard capability G1–G4) open as parallel lanes under the new workplan;
  steps 7–9 gated downstream, not released.
- Noted agent reading for owner awareness (recorded in the workplan Lane B
  and `AgentRuns/ROOT-LOOP-REORIENT-20260725/returns/N1_RETURN.md`): the §7
  guard-design preflight's scratch `PKG-*` skeleton will trigger a G0 BLOCK
  in its throwaway worktree by design; recorded as intended fence behavior,
  not a defect and not the §5.1 finding.
- Unresolved blockers: none for the live lanes. Standing follow-ons and
  parked lanes carried into the new workplan (App Dev deflake; optional
  strict branch-protection hardening; CHANGE merge-verdict rule; class b/c
  reconciliation; predecessor parked lanes). Export-staging regeneration
  remains DEFERRED per the implementation handoff.
- Gate: this tranche merges only through a human-gated PR; never
  self-merged.

### Receipt 34 — 2026-07-25 — Lane A executed: candidate root PRD authored

- Owner acts of record (in-session, 2026-07-25): "Merge PR #339 and proceed
  with Lane A" — PR #339 merged at that direction (step 4 closed at
  `7ac718c7e`); Lane A executed under the standing posture direction
  (Agent 0; `opus-5` children).
- Step 0 preflight: EffectiveSHA contained in `main`; harness 311 passed;
  self-check exit 0; G0 PASS idle + 9/9 suite. Recorded green before
  dispatch.
- Run `ROOT-PRD-LANE-A-20260725` (terminal fan-out/fan-in, single node;
  executor form: ephemeral Agent 2 generalist under sealed brief — recorded
  rationale in the run's ORCHESTRATION_PLAN: no live Agent 1 charter covers
  candidate-PRD authoring): authored
  `execution/_Coordination/PRD_CANDIDATE_2026-07-25_root_product.md`
  (CANDIDATE — NOT ADOPTED; 78 labeled requirements: 67 TRANSCRIBED /
  4 OWNER_DECLARED / 4 CLARIFIED / 3 PROPOSED; falsifiers F1–F3 transcribed,
  F4–F6 proposed; four reserved decisions RD-1..RD-4 surfaced with options,
  none resolved).
- Fan-in V1 accepted; dispositions in the run's `returns/N1_RETURN.md`,
  including: the issuing brief's in-repo-history date (2026-02-18) was
  wrong — first commit is `7bee9ae41` 2026-05-18; the child refused the
  error and the record now carries the verified fact. New conflicts C-2
  (CONTRACT invariant-index drift 27 vs 34) and C-3 (README omits
  `runtime/` from its export-boundary description) surfaced in-document and
  routed to the owner; both need M2/propagation tranches, neither amended
  here.
- Lane A terminal gate reached: the candidate stops at owner review.
  Adoption is a separate instrument (RD-3), expressly not exercised.
- Gate: this tranche merges only through a human-gated PR; never
  self-merged.

### Receipt 35 — 2026-07-25 — PRD candidate Rev 2 after adversarial review

- Owner act of record (in-session, 2026-07-25): routed an independent
  adversarial review of PRD candidate Rev 1 and directed its consideration.
  Review preserved verbatim in
  `AgentRuns/ROOT-PRD-LANE-A-20260725/reviews/ADVERSARIAL-REVIEW-1.md`;
  verdict: not adoption-ready — a governed-basis concordance that must
  become a directional product definition.
- Agent 0 accepted all review items (dispositions in
  `AgentRuns/ROOT-PRD-LANE-A-20260725/briefs/PRD-AUTHOR-BRIEF-AMENDMENT-1.md`,
  a versioned brief amendment expanding the write scope to two files) and
  resumed the same authoring instance (`opus-5`) with context intact.
- Rev 2: main PRD restructured to the reviewer's ten-section shape (~20%
  shorter; objectives OBJ-1..OBJ-7 with v1 success conditions; generative
  loop; upward variant promotion; corrected user strata; RD-5 added;
  release authority; OWNER_DECLARED key relabeled honestly as Agent 0
  synthesis) plus a companion concordance annex (derivative package,
  regenerable, never adopted; adoption binds the main PRD bytes only;
  D-14 six-class source-currency specification).
- Fan-in V1 accepted; two child-side validator gaps closed by Agent 0
  re-run (path anchors PASS 992; G0 PASS idle). Top items flagged for
  owner attention: the PROPOSED v1 boundary (child construction —
  re-scope if the owner's v1 differs), OBJ-1..OBJ-7, and D-14.
- Lane A remains at its terminal gate: owner review of the candidate.
  Adoption instrument and the four+one reserved decisions (RD-1..RD-5)
  remain owner acts.

### Receipt 36 — 2026-07-25 — PRD candidate Rev 3 after second review pass

- Owner act of record (in-session, 2026-07-25): routed the second
  adversarial-review pass on Rev 2 ("recognizably a product PRD"; one more
  revision recommended; issues are precise contradictions). Review
  verbatim in `AgentRuns/ROOT-PRD-LANE-A-20260725/reviews/ADVERSARIAL-REVIEW-2.md`;
  Agent 0 accepted all eleven items + two refinements (Brief Amendment 2).
- Rev 3 (same authoring instance, `opus-5`): genus-neutral ID-1;
  K-DOMAIN-1 exception stated in N-1 itself; O-10 human-authority
  correction; OBJ-2 narrowed to consequential acceptance/reliance/issuance
  judgments; §2.3 separable human capacities; RD-5-B de-narrowed; §4.2 two
  distinct human judgments (evaluation vs iteration); OBJ-6 population +
  lifecycle-checkable condition; D-2 narrowed with generalization carried
  as new D-16 PROPOSED; annex regenerability claims made honest
  (specified/proposed, MECHANICAL vs SEMANTIC classes); §10.3 final
  adoption transformation (two-step; prior revisions immutable); OBJ-3
  pre-fixed thresholds; OBJ-5 promotion-disposition success.
- Provenance: 43 stable commitments (34/5/4); 17 PROPOSED items total.
  Flagged closest for owner: D-16, D-14, the PROPOSED v1 boundary.
- Fan-in V1 accepted; validators green child-side and re-run green by
  Agent 0 (path anchors PASS 992; G0 PASS idle).
- Lane A remains at its terminal gate: owner review; then RD-1..RD-5
  rulings; then the final adoption-ready revision per §10.3.

### Receipt 37 — 2026-07-25 — RD-1 RULED (genus); PRD candidate Rev 4

- Owner acts of record (in-session, 2026-07-25): (1) stated intent to
  resolve the genus before approving the PRD; (2) routed the third
  adversarial-review pass (verbatim in
  `AgentRuns/ROOT-PRD-LANE-A-20260725/reviews/ADVERSARIAL-REVIEW-3.md`);
  (3) **RULED RD-1** — presented the slate (A retain DIRECTIVE genus /
  B adopt README genus / C two-level formulation), the owner selected,
  recorded verbatim from the selection interface: "C — Two-level
  formulation". The ruled genus text is the option-C formulation
  reproduced exactly in the PRD §9.1 and in Brief Amendment 3.
  SHA-binding of the ruling occurs at the adoption instrument (RD-3).
- Ruling consequences recorded, none performed in this tranche: (a)
  exact-prose human-gated M2 supersession of the ratified
  `docs/DIRECTIVE.md` §1 genus clause; (b) `README.md` reword; (c)
  propagation survey of SPEC/TYPES/AGENTS.md "operating system" prose.
  DIRECTIVE §1 remains in force until (a) lands; PRD C-1 status is
  `RESOLVED-IN-PRINCIPLE — concordance pending`.
- Rev 4 (same authoring instance, `opus-5`, Brief Amendment 3): RD-1
  incorporated (ID-0; §1.2 ruled-pending-concordance; §9.1 ruling
  record); all eight review items + two wording corrections applied
  (D-16 narrowed; D-1/D-3 evidenced scope; OBSERVED provenance category;
  split annex bases; D-14 nine-class accounting; release as third human
  judgment; OBJ-3/OBJ-5 quantifiers; commentary normalization).
- Fan-in V1 accepted (two-file diff; path anchors PASS 992; G0 PASS
  idle; DIRECTIVE-not-amended claims verified by direct inspection).
- Open: RD-2..RD-5 rulings; C-2/C-3/C-4; then the final adoption-ready
  revision per PRD §10.3 and the adoption instrument per RD-3.

### Receipt 38 — 2026-07-25 — RD-2..RD-5 RULED; final review cycle closed; PRD candidate Rev 5 (adoption-ready)

- Owner acts of record (in-session, 2026-07-25):
  1. Routed the fourth adversarial-review pass (single subject: D-3's
     authority status; verbatim in
     `AgentRuns/ROOT-PRD-LANE-A-20260725/reviews/ADVERSARIAL-REVIEW-4.md`)
     with the direction: "Consider this as the final review cycle.
     Incorporate what has merit from your perspective and proceed from
     there." Agent 0 accepted the reviewer's Option 1: D-3 leaves the §5
     requirements table and is preserved as OBSERVED practice —
     "practice supplies evidence; evidence informs judgment; judgment
     alone makes the rule."
  2. **RULED RD-2** (jurisdiction/accountability) — recorded verbatim
     from the selection interface: "A1+B2 could seemingly be scaled up
     to multi-practitioner using the PEC interface and a database, and
     attribution can be done more securely that way. If you agree I
     would go that way. And that database and PEC interface are not
     current scope. That can be something that may be incorporated as
     Chirality morphs and responds to usage with ongoing development and
     refinement." The ruling was conditioned on Agent 0 agreement; Agent
     0 agreed, with the D-GOV-01 caveat recorded as CLARIFIED (a future
     PEC/database layer supplies the attribution mechanism; the
     authoritative record stays file-native unless D-GOV-01 is
     consciously amended).
  3. **RULED RD-3** (adoption instrument) — selection verbatim: "A+y
     (Recommended)". Instrument: a D-GOV-* exact-candidate decision
     record over the adoption-ready bytes, plus a bidirectional
     concordance map (PRD ↔ DIRECTIVE §1) drawn against DIRECTIVE §1
     as it stands, the RD-1 divergence recorded; obligation (a) lands in
     the adoption/implementation tranche.
  4. **RULED RD-4** (placement) — selection verbatim: "D — Split with
     pointer". Adopted PRD in root `docs/` through the existing export
     allowlist; candidates and revision evidence immutable in
     `execution/`; a pointer identifies the adopted exact bytes.
  5. **RULED RD-5** (v1 user scope) — recorded verbatim: "It's for all
     of those, but I see it progressing over time as we start with A and
     learn from my use to make a better version for B which I can test
     out locally with multiple computers with multiple Agent 0 instances
     on each and learn from that and make a better C which is the target
     level of maturity for the platform." Incorporated as v1 = A with an
     OWNER_DECLARED A→B→C maturation trajectory, C the target maturity.
- SHA-binding of all four rulings occurs at the adoption instrument
  (RD-3), as with RD-1 (Receipt 37).
- Rev 5 (fresh ephemeral Agent 2 instance, `opus-5`, Brief Amendment 4;
  the prior instance's transcript had expired and the successor worked
  from the durable run record): the final adoption-ready revision per
  PRD §10.3 — banner `ADOPTION-READY — adopted only by the instrument
  named below`; D-3 removed (identifier retired, not reassigned; §6.2
  OBSERVED practice statement added; commitments 43 → 42, TRANSCRIBED
  34 → 33); §9 reduced to records of the five rulings with verbatim
  fences; drafting commentary stripped; annex §5.6 correction + rulings
  tables; C-3 expressly flagged for owner confirmation at the
  instrument.
- Fan-in V1 accepted (two-file diff; path anchors PASS 992; G0 PASS
  idle; independent script count 42 = 33/5/4 with D-3 absent and no
  renumbering; all five verbatim fences verified by direct grep; no
  adoption claims; DIRECTIVE §1 nowhere claimed amended). Return:
  `AgentRuns/ROOT-PRD-LANE-A-20260725/returns/N1_RETURN-REV5.md`.
- Open: the adoption instrument (RD-3-A record + RD-3-y map) and the
  owner's adoption ruling against the exact candidate SHA; C-2/C-3/C-4;
  §9.1 obligations (a)/(b)/(c) and RD-4-D placement in the
  adoption/implementation tranche. Merging PR #340 records candidates;
  it does not adopt.

### Receipt 39 — 2026-07-25 — D-GOV-22 RULED: the root PRD is ADOPTED; Lane A closed

- Owner acts of record (in-session, 2026-07-25), in order:
  1. Directed the merge of PR #340 (candidates + instrument packet onto
     `main`; merge SHA `d0f128647`). Merging recorded candidates; it did
     not adopt.
  2. **Confirmed C-3** — verbatim: "the 'roughly three years' lingo is
     true but it was such a throwaway comment I find it hilarious and
     depressing that it's still getting mentioned all this time later.
     Chirality has been in development for some time preceding the first
     commit evidence available.  Move on." C-3 CLOSED: ID-3 testimony
     confirmed true, expressly not load-bearing; no further recitation
     warranted.
  3. **RULED D-GOV-22** — verbatim: "I rule APPROVED for O-A against
     candidate SHA 90fae458bf485412e9c3a6295df193eb323c9774." The Rev 5
     adoption-ready PRD (exact bytes at `d9ea86f88`, sha256-pinned in
     the packet) is ADOPTED. Per packet §6.2, the uncorrected O-A ruling
     also confirms the ID-1/ID-2/ID-3 syntheses.
- Publication tranche (this commit): decision record
  `docs/governance_harness/_DECISIONS/D-GOV-22_root_prd_adoption.md`
  (ruling + C-3 statement verbatim-fenced); `_REGISTER.md` row; RD-4-D
  placement `docs/PRD_ROOT.md` (pointer block + adopted bytes,
  byte-identity verified by sha256 at placement). PublicationSHA and
  EffectiveSHA backfilled per the `f1549afb1` precedent after the human
  merge gate.
- Effects: the 17 PROPOSED items take effect; all five RD rulings
  SHA-bound at publication; the Annex A concordance map is the recorded
  divergence state (one DIVERGENT pair — RD-1 genus; C-1 pending
  obligation (a)). **D-GOV-21 §6 step 5 (Lane A) is CLOSED.**
- Open after this receipt: obligations (a) DIRECTIVE §1 exact-prose
  supersession (closes C-1), (b) README reword, (c) SPEC/TYPES/AGENTS.md
  propagation survey; C-2 and C-4 correction proposals; Lane B (guard
  capability G1–G4 + §7 preflight) — the next open root-loop lane;
  export-staging regeneration remains DEFERRED.

### Receipt 40 — 2026-07-25 — D-GOV-22 effective; obligation (a) candidate staged (D-GOV-23)

- Owner act of record (in-session, 2026-07-25): "Merge PR #341 and proceed
  with obligation (a)." PR #341 merged; **D-GOV-22 EffectiveSHA
  `08f526277`**. PublicationSHA `c800631d5` and the EffectiveSHA backfilled
  into the decision record per the `f1549afb1` precedent. The root PRD
  adoption is now effective on `main`: adopted copy live at
  `docs/PRD_ROOT.md`; the 17 PROPOSED items in force; all five RD rulings
  SHA-bound.
- Obligation (a) staged as **D-GOV-23** (CANDIDATE — NOT RULED):
  `docs/governance_harness/_PROPOSALS/D-GOV-23_directive_genus_supersession/PACKET.md`
  — exact-prose supersession of the DIRECTIVE §1 genus clause with the
  RD-1 ruled two-level formulation (Annex A current text verified
  byte-exact against `main@08f526277`; replacement = ruled text verbatim +
  a provenance parenthetical, remainder of the paragraph unchanged
  byte-for-byte). An O-A ruling closes C-1. Scope expressly excludes
  obligations (b)/(c) surfaces.
- Open after this receipt: the D-GOV-23 owner ruling; obligations (b)
  README reword and (c) propagation survey; C-2/C-4 correction proposals;
  Lane B (G1–G4); export-staging regeneration DEFERRED.

### Receipt 41 — 2026-07-25 — D-GOV-23 RULED: DIRECTIVE §1 genus superseded; C-1 CLOSED

- Owner act of record (in-session, 2026-07-25) — verbatim: "I rule
  APPROVED for O-A against candidate SHA
  65bb96378428a86ed8ab8581149ead056d756789". Obligation (a) is performed.
- Application (this commit): the Annex A.2 replacement prose was extracted
  programmatically from the ruled packet (not retyped), the A.1 current
  text verified to occur exactly once in live `docs/DIRECTIVE.md`, and the
  paragraph replaced byte-faithfully. DIRECTIVE §1 now opens with the RD-1
  ruled two-level genus verbatim (plus the candidate's provenance
  parenthetical); the rest of the paragraph is byte-identical. No
  deviation occurred, so no re-approval round was required.
- **C-1 CLOSED.** The D-GOV-22 Annex A concordance map's single DIVERGENT
  pair is concordant. The adopted PRD bytes are not edited (RD-4); its
  §1.2 "concordance pending" state is satisfied by events, stated in the
  D-GOV-23 decision record.
- Publication tranche (this commit): decision record
  `docs/governance_harness/_DECISIONS/D-GOV-23_directive_genus_supersession.md`;
  `_REGISTER.md` row; routed change notices (M6, D-GOV-21 precedent) to
  `projects/chirality-app-dev/execution/_Coordination/` and
  `domains/chirality/_Coordination/` — the app-dev
  `AUTHORITY_CORPUS.json` sha256 pin for DIRECTIVE was already stale
  before this change and re-pins on that loop's own cadence.
  PublicationSHA/EffectiveSHA backfilled after the human merge gate.
- Open after this receipt: obligations (b) README genus reword and (c)
  SPEC/TYPES/AGENTS.md propagation survey; C-2/C-4 correction proposals;
  Lane B (G1–G4); export-staging regeneration DEFERRED.

### Receipt 42 — 2026-07-25 — D-GOV-23 effective; obligations (b) applied and (c) surveyed

- Owner act of record (in-session, 2026-07-25): "Merge PR #342 and proceed
  with obligations (b) and (c)." PR #342 merged; **D-GOV-23 EffectiveSHA
  `b6ae1d5d8`** — the DIRECTIVE §1 genus supersession is live on `main`;
  PublicationSHA `9a28c8d37` and the EffectiveSHA backfilled into the
  decision record per the `f1549afb1` precedent.
- **Obligation (b) applied (this commit):** `README.md` genus paragraph
  reworded to the RD-1 ruled two-level formulation (ruled sentences
  carried with a provenance pointer to `docs/PRD_ROOT.md`; README's
  concrete enumeration retained as a third sentence). README is a
  non-binding surface (D-GOV-21 packet §3b classification); the change is
  gated by this PR's human merge, per the D-GOV-21 tranche precedent.
- **Obligation (c) executed (this commit) — proposals only, nothing
  applied:**
  `execution/_Coordination/SURVEY_2026-07-25_OBLIGATION_C_operating_system_prose.md`.
  Universe: all instruction surfaces; ten governed instances, all in the
  four `docs/` authority files; `AGENTS.md`, `agents/`, `init/`,
  `skills/`, and both standards have zero. Six instances are consistent
  contained-level usages (KEEP). Four lean on the pre-RD-1 top-level
  identity and carry exact candidate replacement prose as PROPOSALS
  P-1..P-4 (DIRECTIVE:5 preamble, CONTRACT:7, SPEC:5, TYPES:5), awaiting
  owner direction on both content and vehicle (small exact-prose packet
  recommended; PR-review approval lawful under K-AUTH-2 per adopted PRD
  §6.2).
- Open after this receipt: owner direction on P-1..P-4; C-2/C-4
  correction proposals; Lane B (G1–G4); export-staging regeneration
  DEFERRED. With (b) applied and (c) surveyed, all three §9.1 follow-on
  obligations of the RD-1 ruling are performed or (for P-1..P-4
  application) staged for direction.

### Receipt 43 — 2026-07-25 — D-GOV-24 RULED: genus propagation complete (P-1..P-4 applied)

- Owner act of record (in-session, 2026-07-25) — verbatim: "I rule
  APPROVED for O-A against candidate SHA
  444e29359883e50506ac0ea0ee5f6cc3f5f7d7de".
- Application (this commit): the four Annex A replacements extracted
  programmatically from the ruled packet, each current sentence
  re-verified unique in its live file, all four applied byte-faithfully —
  DIRECTIVE preamble (P-1), CONTRACT :7 (P-2), SPEC :5 (P-3), TYPES :5
  (P-4). No deviation; no re-approval round required.
- **The RD-1 genus propagation is complete.** Across D-GOV-23 (DIRECTIVE
  §1), obligation (b) (README), and D-GOV-24 (four self-descriptions), no
  governed surface presents the pre-RD-1 top-level identity as current
  self-description; the six contained-level "agent operating system"
  usages remain by design under the ruled two-level formulation.
- Publication tranche (this commit): decision record
  `docs/governance_harness/_DECISIONS/D-GOV-24_operating_system_prose_propagation.md`;
  `_REGISTER.md` row; routed M6 change notices to
  `projects/chirality-app-dev/execution/_Coordination/` and
  `domains/chirality/_Coordination/` (the app-dev `AUTHORITY_CORPUS.json`
  pins all four touched files; re-pins on that loop's cadence).
  PublicationSHA/EffectiveSHA backfilled after the human merge gate.
- Open after this receipt: C-2 (CONTRACT §1 invariant-index arithmetic)
  and C-4 (README export description) correction proposals; Lane B
  (G1–G4); export-staging regeneration DEFERRED.

### Receipt 44 — 2026-07-25 — D-GOV-24 effective; C-2 and C-4 corrected

- Owner act of record (in-session, 2026-07-25): "Merge PR #344 and proceed
  with C-2 and C-4." PR #344 merged; **D-GOV-24 EffectiveSHA
  `b3bd99863`** — the genus propagation (P-1..P-4) is live on `main`;
  PublicationSHA `ed99d8e3e` and the EffectiveSHA backfilled into the
  decision record per the `f1549afb1` precedent.
- **C-2 CORRECTED (this commit):** `docs/CONTRACT.md` §1 K-* Invariant
  Index — count line updated from "27 stable invariants across 12
  subsections" to "**34 across 13**", and seven index rows added for the
  D-GOV-20 §1.13 Shared Runtime family (K-RUNTIME-1, K-CONTROL-1,
  K-PROJECT-1, K-STORE-2, K-RESIDENCY-1, K-ROLE-2, K-EXPORT-1).
  Mechanically verified post-edit: index membership == catalog membership
  (34 == 34), subsection count 13. No invariant definition changed —
  index arithmetic only, exactly the M2 correction the adopted PRD §10.2
  recommended. Routed M6 notice shipped to
  `projects/chirality-app-dev/execution/_Coordination/` (its
  `AUTHORITY_CORPUS.json` pins CONTRACT).
- **C-4 CORRECTED (this commit):** `README.md` now describes root
  `runtime/` — a row in the root-surface table (root-owned generic
  executable agent-runtime substrate per D-GOV-20; included in the public
  export with the standing exclusions) and a mention in the summary
  sentence — matching the export profile's `ROOT_DIRS`, which has
  exported `runtime` all along. README is non-binding; the PR merge is
  the gate, per the obligation (b) precedent.
- **With C-2 and C-4 closed, every conflict the adopted PRD surfaced
  (C-1..C-4) is resolved.** C-1 closed by D-GOV-23; C-3 confirmed at the
  D-GOV-22 ruling; C-2/C-4 corrected here.
- Open after this receipt: Lane B (guard capability G1–G4 + §7
  preflight) — the sole remaining open root-loop lane before the
  D-GOV-21 §6 sequence can advance; export-staging regeneration
  DEFERRED.
