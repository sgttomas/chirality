# VERIFY-DEL-04-04-R1 Evidence Terminalization Remediation Brief — v1

Role: fresh ephemeral Agent 2 generalist; no delegation.

Objective: terminalize already-complete VERIFY-DEL-04-04 evidence only. Read
the original sealed brief and existing verifier workspace/evidence. Candidate
`9d7a5de67db2b656f86246b1f2f466862ae60e53102d011be6910555afab15b6`,
all deterministic checks, both negative fixtures, and four verdict classes are
already complete PASS. Do not rerun substantive checks.

AllowedWriteTargets (exact only):

- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG04/children/VERIFY-DEL-04-04/MANIFEST.tsv`
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG04/children/VERIFY-DEL-04-04/RETURN.md`
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG04/children/VERIFY-DEL-04-04/STATUS.json`
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG04/children/VERIFY-DEL-04-04/workspace/evidence/REPLACEMENT_MANIFEST.tsv`
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG04/children/VERIFY-DEL-04-04/workspace/_run_records/TASK_RUN_2026-07-13_1158.md`

Tasks:

1. Use existing recorded evidence only; no converter/validator/map/parity/checklist/render/negative rerun.
2. Create/validate exact five-row replacement (ADD candidate, DELETE four legacy production files; no status/control path).
3. Create terminal PASS RETURN and STATUS with `terminal:true`, no blockers/repair, exact candidate hash, four PASS verdicts, mapping/coverage/checklist/render bindings from evidence, `manifest: COMPLETE`.
4. Set the existing run record to SUCCESS with completed output headings.
5. Mechanically generate a portable self-excluding child MANIFEST with path/sha256/bytes and reproduce every row.
6. Return PASS_REPAIRED (or PASS_UNCHANGED if already valid), row/hash counts, exact files changed, JSON/hash/containment verdict, blockers; exit immediately.

EXCLUSIONS: candidate/project/source/control writes; substantive reruns; Git;
integration/lifecycle/H1/H2/ISSUED/release/retirement; other child/package
paths; `.claude-worktrees/**`.
