# W6 sealed child launch — N3 recovery evidence design

- RequestedBy: `WORKING_ITEMS/W6-DEL0206-POST-N0-PLANNING`
- RunID: `DEL-02-06-RUNTIME-SPEC-001`
- Parent runtime identity: `/root/w1_del0206`
- Expected child runtime identity: `/root/w1_del0206/n3_w6`
- Form: fresh ephemeral Agent 2 generalist; delegation forbidden.
- Governing brief: `briefs/N3.md`, SHA-256 `c4d97e2ad8998c67efd407aad2e2a470997159dc538ee0f46f48cf1055a21b7e`.
- Accepted dependency: `basis/N0_R2_RETURN.md`, SHA-256 `ca8c1b18f6bd3d32ab7f1bad5d0cdc15d3bd31c811d3a2484ed38f61c64ac522`, manager-accepted by W5 return SHA-256 `938899201de1941108cc6a817fbf75043a8a0c308d384db783e9719902237c3e`.
- Current Git basis: `ba576264793deba0708397874414b7482c243f89`; contains `origin/main@379b8b19b12b29eda4fa307e497499d6fe414f8a`.
- Declared reads: accepted `ScopeOfWork.md`; `execution/_Coordination/_TaskManagement/DEL-02-06_HANDOFF_TM-ROOT-108_2026-08-02.md`; `execution/_Coordination/NOTICE_D-APP-85_C06_DAEMON_RECOVERY_ROOT_ROUTE_2026-08-02.md`; `READ_SCOPE_AMENDMENT_1.md`; accepted N0 return/report; and this launch.
- Allowed tools: non-shell bounded Node file reads/hashes/parsing and `apply_patch` for the exact outputs only. No Bash, network, executable software check, implementation command, or delegation.
- Allowed writes: `evidence/N3_EVIDENCE_DESIGN.md` and `evidence/N3_RETURN.md` only.
- Expected result: complete requirement/evidence matrix, restart/replay scenarios, cutover/rollback evidence plan, all unresolved policies named and human-gated; verdict `ACCEPT_FOR_N4` or `RETURN_TO_MANAGER`.
- Hard stop: no runtime execution or semantic selection; no implementation, runtime/client/project write, profile/check adoption, lifecycle/release/reliance, SCA/decomposition/PRD, Task Management, Git, or foreign write.
