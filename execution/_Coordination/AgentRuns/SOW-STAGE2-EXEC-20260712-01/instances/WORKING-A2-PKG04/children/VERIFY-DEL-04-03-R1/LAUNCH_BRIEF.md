# VERIFY-DEL-04-03-R1 Evidence Terminalization Remediation Brief — v1

Role: fresh ephemeral Agent 2 generalist. Do not delegate.

Objective: validate and, only if necessary, finish the already-complete
VERIFY-DEL-04-03 terminal evidence. This is evidence terminalization only; it
does not repeat or alter substantive verification.

Accepted predecessor:

- Original sealed brief: `instances/WORKING-A2-PKG04/children/VERIFY-DEL-04-03/LAUNCH_BRIEF.md`
- Existing verifier workspace/evidence under the same child root
- Accepted candidate SHA-256: `72c083f28a597583abf1b6e950f0ce0965221f9cd2fee0233408954336aaa100`
- Original verifier reported all substantive and negative checks PASS

Declared reads:

- Original verifier brief, workspace, evidence, and candidate (read-only)
- Exact DEL-04-03 A2 manifest row and activation references named by the original brief

AllowedWriteTargets (only these exact existing terminal surfaces):

- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG04/children/VERIFY-DEL-04-03/MANIFEST.tsv`
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG04/children/VERIFY-DEL-04-03/RETURN.md`
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG04/children/VERIFY-DEL-04-03/STATUS.json`
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG04/children/VERIFY-DEL-04-03/workspace/evidence/REPLACEMENT_MANIFEST.tsv`
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A2-PKG04/children/VERIFY-DEL-04-03/workspace/_run_records/TASK_RUN_2026-07-13_1133.md`

Tasks:

1. Do not rerun converter, validator, mapper, parity, checklist, renderer, or negative fixtures.
2. Validate the existing candidate/source/status/control hashes only from recorded evidence.
3. Require exact five-row replacement: ADD candidate plus DELETE four legacy production files; exclude every status/control path.
4. Require terminal PASS STATUS, terminal RETURN, SUCCESS run record, and portable self-excluding MANIFEST with path/hash/bytes bindings that mechanically reproduce.
5. If all existing files already pass, leave their bytes unchanged. If a terminal evidence defect exists, change only the exact defective allowed terminal surface.
6. Return `PASS_UNCHANGED` or `PASS_REPAIRED` with manifest row count/hash, replacement row count, files changed, JSON/hash/containment verdict, and blockers. Exit immediately.

EXCLUSIONS: candidate/source/control/project writes; substantive reruns; Git;
integration; lifecycle; H1/H2; ISSUED; release; retirement; other child/package
paths; `.claude-worktrees/**`.
