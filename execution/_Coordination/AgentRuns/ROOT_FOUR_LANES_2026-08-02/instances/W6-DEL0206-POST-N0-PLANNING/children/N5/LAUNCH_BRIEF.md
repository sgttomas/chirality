# W6 sealed child launch — N5 fresh adversarial verification

- RequestedBy: `WORKING_ITEMS/W6-DEL0206-POST-N0-PLANNING`
- RunID: `DEL-02-06-RUNTIME-SPEC-001`
- Parent runtime identity: `/root/w1_del0206`
- Expected child runtime identity: `/root/w1_del0206/n5_w6`
- Form: fresh ephemeral Agent 2 generalist; delegation forbidden; read-only refuter; repair forbidden.
- Governing brief: `briefs/N5.md`, SHA-256 `632d2cbefac9003f36d9d722374b22fdeca5d0da45e637acf7335c8a7d872121`.
- Accepted N0-N3 identities: those exact pairs recorded in N4 self-check SHA-256 `924ae2ebc528925818513bcdaaa34132c664e2f2f64ebf4a61653ab254e9462a`.
- Accepted N4 outputs: `RECOVERY_SPEC_CANDIDATE.md` `5f16ca9e1a11f0035110655d400153ad5d57aeee3e25ba6032b0c91f66467bc7`; `COMPATIBILITY_DISPOSITION_CANDIDATE.md` `689b41e3fc9416a5fcc637c4ebe543f4b6272b96fe32f65f47766855c222dda1`; `DEGRADED_MODE_DELTA_CANDIDATE.md` `cfec76035e3a527e561922308a67134f879cfd9b58122c7687593945ea88c593`; `OPEN_ITEM_MAP.md` `38149d3292234a071064300c826c2707a8f6b445e878558f31c3c6c7ece66eaf`; `IMPLEMENTATION_PLAN_CANDIDATE.md` `e2f4fda9fa44eff9caf3c6894b6112c4eec39fc9bbac43b8e840382fc3b17bd9`; `N4_SELF_CHECK.md` `924ae2ebc528925818513bcdaaa34132c664e2f2f64ebf4a61653ab254e9462a`; `N4_RETURN.md` `a8a34949160fec63bf6dd6c33a373cd0dfd1609df0c3bd268e69a8555f2dab72`.
- Accepted Scope of Work: `ScopeOfWork.md` `dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146`.
- Declared reads: accepted N0-N4 outputs, accepted Scope of Work, governing brief, and this launch only.
- Allowed tools: non-shell bounded Node file reads/hashes/parsing only. No write tool, Bash, network, executable test/check, runtime execution, implementation command, repair, or delegation.
- Allowed writes: none. Return the terminal finding ledger and verdict only through the runtime response; WORKING_ITEMS will capture it.
- Required review: 100% of all seven N4 outputs; attempt to refute semantic completeness, source grounding, client boundaries, write/authority containment, restart/replay sufficiency, drain accounting, exactly-one-terminal proof, rollback honesty, D1-D9 preservation, and absence of false evidence/closure claims.
- Verdict: `ADMIT` only if no material finding; otherwise `RETURN` with severity, exact evidence, affected output, and required manager/N4 disposition. Uncertainty fails closed.
- Hard stop: no repair; no semantic adoption, implementation, runtime/client/project write, profile/check adoption, lifecycle/release/reliance, SCA/decomposition/PRD, Task Management, Git, or foreign write.
