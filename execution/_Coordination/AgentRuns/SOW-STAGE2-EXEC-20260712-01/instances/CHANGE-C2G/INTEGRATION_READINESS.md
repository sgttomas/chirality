# C2G Integration Readiness

Verdict: `READY`
Recorded: `2026-07-13`
Branch: `codex/sow-stage2-consumers`
Integration base: `main@e150c972889d05a8fc270239451a35c7512dc9a9`

## State and approval

- Local `main`, `origin/main`, and remote `refs/heads/main` were equal to the
  required integration base before branch creation.
- The source branch was created at that exact commit. No local or remote branch
  collision existed.
- GitHub authentication passed. No merge, rebase, cherry-pick, revert, or bisect
  operation was in progress.
- Human merge approval is `amendments/HUMAN-STEER-001.md`. It authorizes the
  run-scoped PR merge only after the sealed checks and containment gates pass.
- `.claude-worktrees/` is a pre-existing untracked container and is excluded
  from every stage, commit, and cleanup action.

## Accepted source and closure

- P2 derivative snapshot: `IMMUTABLE DERIVATIVE — C2F-R2 PASS`.
- `snapshots/P2_CONSUMERS/MANIFEST.tsv`: every listed SHA-256 passed.
- C2R-R3: terminal `PASS`; root current caller inventory `64/64`, with 48
  current changed source paths and no extra source path.
- C2A-R1: terminal `PASS`; App current caller inventory `9/9`, with four
  changed source paths and no extra source path.
- C2F-R2: RECONCILIATION, EVALUATION, and REVIEW terminal `PASS`; blockers,
  waivers, and material unknowns are none. `EVAL-C2F-004` remains low and
  non-blocking.
- Root/App source intersection: zero. No governed deliverable, lifecycle,
  release, conversion, H1, H2, or legacy-retirement path is in a source tranche.
- Current-hash-bound full producer evidence remains 792 root tests and 713 App
  tests plus four skips. C2G reruns only the sealed bounded integration checks.

## Commit 1 — root consumers

Commit subject: `feat: activate Scope-of-Work root consumers`

Exactly these 48 source paths:

- `agents/AGENT_AUDIT_DECOMP.md`
- `agents/AGENT_AUDIT_EPISTEMIC.md`
- `agents/AGENT_EVALUATION_STRUCTURE_AUDIT.md`
- `agents/AGENT_ORCHESTRATOR.md`
- `agents/AGENT_PREPARATION.md`
- `agents/AGENT_PROJECT_DECOMP.md`
- `agents/AGENT_RECONCILIATION.md`
- `agents/AGENT_REVIEW.md`
- `agents/AGENT_WORKING_ITEMS.md`
- `docs/DIRECTIVE.md`
- `docs/SE_Design_Analysis.md`
- `exports/chirality-app/export-manifest.csv`
- `skills/README.md`
- `skills/content-digest/SKILL.md`
- `skills/deliverable-consistency/BRIEF_SCHEMA.md`
- `skills/deliverable-consistency/SKILL.md`
- `skills/four-documents/BRIEF_SCHEMA.md`
- `skills/four-documents/QA_CHECKS.md`
- `skills/four-documents/SKILL.md`
- `skills/four-documents/TOOL_POLICY.md`
- `skills/lens-register/BRIEF_SCHEMA.md`
- `skills/lens-register/SKILL.md`
- `skills/lens-register/TOOL_POLICY.md`
- `skills/proposal-format/BRIEF_SCHEMA.md`
- `skills/proposal-format/SKILL.md`
- `skills/scope-of-work/BRIEF_SCHEMA.md`
- `skills/scope-of-work/SKILL.md`
- `skills/scope-of-work/TOOL_POLICY.md`
- `skills/semantic-lensing/SKILL.md`
- `skills/semantic-matrix-build/BRIEF_SCHEMA.md`
- `skills/semantic-matrix-build/SKILL.md`
- `tools/EXTERNAL_TOOLS.md`
- `tools/REGISTRY.md`
- `tools/evaluation/count_deliverable_files.sh`
- `tools/reporting/generate_coverage_csv.py`
- `tools/reporting/test_generate_coverage_csv.py`
- `tools/scope_of_work/common.py`
- `tools/scope_of_work/convert_four_documents_to_scope_of_work.py`
- `tools/scope_of_work/derive_review_checklist.py`
- `tools/scope_of_work/render_scope_of_work.py`
- `tools/scope_of_work/report_scope_of_work_parity.py`
- `tools/scope_of_work/test_scope_of_work_tools.py`
- `tools/scope_of_work/validate_scope_of_work.py`
- `tools/validation/scan_deliverable_consistency.py`
- `tools/validation/test_semantic_artifact_validators.py`
- `tools/validation/validate_p3_disposition.py`
- `tools/validation/validate_semantic_matrix.py`
- `tools/validation/validate_semantic_pipeline_scope.py`

No `execution/**` or `projects/**` path belongs to commit 1.

## Commit 2 — App runtime

Commit subject: `feat: activate Scope-of-Work App runtime`

Exactly these four source paths:

- `projects/chirality-app-dev/frontend/src/lib/workspace/filesystem.ts`
- `projects/chirality-app-dev/frontend/src/components/shell/document-view.tsx`
- `projects/chirality-app-dev/frontend/src/__tests__/lib/workspace-deliverable-contract-scanner.test.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/api/project/deliverables-route.test.ts`

No project execution, control, or deliverable path belongs to commit 2.

## Commit 3 — evidence binding

Commit subject: `chore: bind Scope-of-Work consumer activation`

The path set is limited to:

- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/**`;
- `execution/_Evaluation/SOW-STAGE2-EXEC-20260712-01/C2F/**`;
- `execution/_Evaluation/SOW-STAGE2-EXEC-20260712-01/C2F-R1/**`;
- `execution/_Evaluation/SOW-STAGE2-EXEC-20260712-01/C2F-R2/**`;
- the C2F, C2F-R1, and C2F-R2 packages under
  `execution/_Evaluation/Reviews/**`;
- the C2F, C2F-R1, and C2F-R2 packages under
  `execution/_Reconciliation/DeliverableConcordance/**`;
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01-C2A/**`;
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01-C2A-R1/**`.

No other path belongs to commit 3.

## Preintegration checks

- Root focused tests: `34 passed`.
- Agent contracts: `33 files, 0 errors, 0 warnings`.
- Skill contracts: `44 valid, 0 invalid`.
- Public export profile: `1 passed`.
- Instruction entrypoints: `PASS`.
- Path anchors: `447` live surfaces, no literal home path.
- Root shell syntax and `git diff --check`: `PASS`.
- App focused seam: `7 files / 76 tests passed`.
- App typecheck: `PASS`.
- Repository self-check: exit `0`; its recorded pre-existing findings remain
  non-blocking.
- Exact ruled authority at resolver, converter, checklist, and App scanner
  seams: `PASS`.
- Exact manifest/hash/containment: root `64/64`, root changed `48`; App `9/9`,
  App changed `4`; C2F-R2 manager pointers `3/3 PASS`; no extra modified source
  path: `PASS`.

Readiness risk: only the recorded low non-blocking `EVAL-C2F-004`. The lane is
ready for the three sealed serial commits, one non-draft PR to `main`, and
repository-default merge under `HUMAN-STEER-001`.
