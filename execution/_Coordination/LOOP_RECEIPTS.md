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
