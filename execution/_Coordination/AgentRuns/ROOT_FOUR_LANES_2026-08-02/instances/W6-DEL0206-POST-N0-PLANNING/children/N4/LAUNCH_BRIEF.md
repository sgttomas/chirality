# W6 sealed child launch — N4 recovery specification integration

- RequestedBy: `WORKING_ITEMS/W6-DEL0206-POST-N0-PLANNING`
- RunID: `DEL-02-06-RUNTIME-SPEC-001`
- Parent runtime identity: `/root/w1_del0206`
- Expected child runtime identity: `/root/w1_del0206/n4_w6`
- Form: fresh ephemeral Agent 2 generalist; delegation forbidden; sole integration writer.
- Governing brief: `briefs/N4.md`, SHA-256 `d8e47eda5594692379d408fd8a7713383589dd38a23f511c3fba37d04392db22`.
- Accepted N0: `basis/N0_R2_RETURN.md` `ca8c1b18f6bd3d32ab7f1bad5d0cdc15d3bd31c811d3a2484ed38f61c64ac522`; report `e11d4c2888d9d449e463c85ef5b06dad138b8eca7b9da00b123e51a346c97cd8`.
- Accepted N1: `inventory/N1_INVENTORY.md` `f4b6039095fa0b7f98d83969fdab29c351d59ee31e43cdb5eb23cd5fa242dcc0`; return `42ea23f2191f1057c09c3bb7d0c2c660a3628117498dc4eb88d169f0778d9866`.
- Accepted N2: `clients/N2_CLIENT_CENSUS.md` `14abde6b3b5eb188555c55749c4b6105d8b4fad08d21e9cf3998a76ea9f4ee52`; return `7f4d2aefccf289bb9b26fbde1cc84aaa66a0436dbd1543cb12b8d5718ca49d64`.
- Accepted N3: `evidence/N3_EVIDENCE_DESIGN.md` `e05b56d3b3a1bd349cd0b9da8e2df761126f2c46c44baf1c9282c6cf55180dd0`; return `1c1746a05f1afee4886f6057544bf7093fc89d182420da718ead9a9c0a4f2fd2`.
- Accepted Scope of Work: `ScopeOfWork.md` `dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146`.
- Fan-in ruling: WORKING_ITEMS accepted N1/N2/N3 as complete and non-contradictory. Preserve N1 F01-F08, N2 F-001, N3 F01-F07, PEC `UNRESOLVED`, and N3 D1-D9.
- Declared reads: only the accepted N0-N3 outputs, accepted Scope of Work, governing brief, and this launch.
- Allowed tools: non-shell bounded Node file reads/hashes/parsing and `apply_patch` for exact outputs only. No Bash, network, executable test/check, implementation command, or delegation.
- Allowed writes, exactly: `integration/RECOVERY_SPEC_CANDIDATE.md`, `integration/COMPATIBILITY_DISPOSITION_CANDIDATE.md`, `integration/DEGRADED_MODE_DELTA_CANDIDATE.md`, `integration/OPEN_ITEM_MAP.md`, `integration/IMPLEMENTATION_PLAN_CANDIDATE.md`, `integration/N4_SELF_CHECK.md`, `integration/N4_RETURN.md`.
- Expected verdict: `ADMIT_FOR_N5` or `RETURN_TO_MANAGER`.
- Acceptance checks: exact requirements and change sequence; fact/candidate separation; no unresolved value inferred; D1-D9 explicit; Root CLI/App affected and PEC unresolved per accepted N2 only; preserve REQ-027/035/052; no present-byte, test, lifecycle, release, or closure claim.
- Hard stop: no semantic adoption, implementation, runtime/client/project write, profile/check adoption, lifecycle/release/reliance, SCA/decomposition/PRD, Task Management, Git, or foreign write.
