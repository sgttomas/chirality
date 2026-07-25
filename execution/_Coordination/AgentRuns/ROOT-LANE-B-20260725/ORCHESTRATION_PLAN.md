# Orchestration Plan — ROOT-LANE-B-20260725 (Lane B: guard capability G1–G4)

Agent 0: `HELP_HUMAN` posture (this session). Owner direction of record
(2026-07-25, in-session): "Merge PR #345 and proceed with Lane B."
Basis: `main@ba2b80bf2` (merge of PR #345). Authorization: D-GOV-21 §6
step 6; workplan `WORKPLAN_2026-07-25_root_product_development.md` §Lane B.

## Structure

- **N0 — §7 preflight (Agent 0, parent-executed).** Scratch materialization
  of a root `PKG-*` skeleton in a throwaway git worktree (never committed);
  run the production CI suites and key standalone validators against it;
  record per-suite outcomes as the §5.1 evidence (expected: only G0
  detects, reporting BLOCK — the fence working as designed); destroy the
  worktree. Evidence: `evidence/PREFLIGHT_REPORT.md`.
- **N1 — Guard capability implementation (ephemeral Agent 2, `opus-5`,
  sealed brief).** Validator code + tests + CI wiring for G1–G4 per packet
  §5.3, PASS-idle before their state surfaces are instantiated (G0
  bootstrap-semantics precedent). Write scope: `tools/validation/`,
  `.github/workflows/governance-harness.yml`, run-record return only.
- **V1 — Fan-in (Agent 0).** Diff scope check; full test battery; G0–G4
  idle-PASS on the clean tree; tranche manifest (G4 discipline applied to
  itself); pin survey for M6 notices; receipt; human-gated PR (M2; no
  self-merge).

## Executor-form rationale

No Agent 1 charter covers root guard-tool authoring; TASK has no matching
skill. Ephemeral bounded generalist per AGENTS.md Agent 2 construction
form 2, `opus-5` per standing owner posture direction.
