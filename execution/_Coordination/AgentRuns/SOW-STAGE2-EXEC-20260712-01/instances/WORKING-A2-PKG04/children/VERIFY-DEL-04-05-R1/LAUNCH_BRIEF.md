# VERIFY-DEL-04-05-R1 Evidence Terminalization Remediation Brief — v1

Role: fresh ephemeral Agent 2 generalist; no delegation.

Objective: terminalize already-complete VERIFY-DEL-04-05 evidence only. Read
the original brief/workspace/evidence. Accepted candidate SHA-256 is
`1095591a196fb61fbfbe30aaa779e3eaeba99c27c79864da428a74ac70c25157`.
All deterministic, duplicate, negative-fixture and four-verdict evidence is
already present. Do not rerun substantive checks.

AllowedWriteTargets (exact only):

- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG04/children/VERIFY-DEL-04-05/MANIFEST.tsv`
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG04/children/VERIFY-DEL-04-05/RETURN.md`
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG04/children/VERIFY-DEL-04-05/STATUS.json`
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG04/children/VERIFY-DEL-04-05/workspace/evidence/REPLACEMENT_MANIFEST.tsv`
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG04/children/VERIFY-DEL-04-05/workspace/_run_records/TASK_RUN_2026-07-13_1219.md`

Tasks:

1. Existing evidence only; no converter/validator/map/parity/checklist/render/negative rerun.
2. Create exact 5-row replacement (ADD candidate, DELETE four legacy production files; exclude status/control).
3. Create terminal PASS RETURN/STATUS with terminal:true, manifest COMPLETE, exact candidate/four verdict/mapping/coverage/checklist/render bindings, no repair/blocker.
4. Set run record SUCCESS and completed headings.
5. Mechanically generate portable self-excluding child MANIFEST path/sha256/bytes and reproduce all rows.
6. Return PASS_REPAIRED/PASS_UNCHANGED with hashes/counts/files changed/JSON/containment/blockers; exit immediately.

EXCLUSIONS: candidate/project/source/control writes; substantive reruns; Git;
integration/lifecycle/H1/H2/ISSUED/release/retirement; other child/package
paths; `.claude-worktrees/**`.
