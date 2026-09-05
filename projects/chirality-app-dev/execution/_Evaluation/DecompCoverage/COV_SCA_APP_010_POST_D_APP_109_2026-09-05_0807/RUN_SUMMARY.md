# Run Summary — SCA-APP-010 Post-D-APP-109 Fresh Full Audit

**RUN_STATUS:** WARNINGS
**OVERALL_STATUS:** WARNINGS
**CLOSURE_READINESS:** FAIL
**Basis:** `f38f1448675b8e9f40f33932a11b7ffa4126fe69` plus the working tree (N8 context alignment and N9 emission, uncommitted)
**Timestamp:** `2026-09-05T08:33:00-06:00`
**RUN_LABEL:** `SCA_APP_010_POST_D_APP_109`

Executed by Claude Fable 5.1 (Anthropic, `claude-fable-5-1`) as a Claude Code
subagent acting as AUDIT_DECOMP, dispatched by HELP_HUMAN; role not
mechanically enforced; no descendant launched. Read-only on every
deliverable, the live decomposition and companion register, and all SCA
snapshots; wrote only the nine named files plus `MANIFEST.sha256` into
`projects/chirality-app-dev/execution/_Evaluation/DecompCoverage/COV_SCA_APP_010_POST_D_APP_109_2026-09-05_0807/` and the instance
`RETURN.md` and `STATUS.json`; no `_LATEST.md` on any surface moved (brief
override, Decision PD-010-001).

The live pair is byte-identical to the 0518 run's inputs (`c7c05169...`,
`63383f04...`); `_LATEST.md` (`b297f43e...`) names SCA-APP-010. Topology is
10 packages / 52 deliverables / 84 scope rows (79 IN / 4 OUT / 1 TBD), 10
objectives, 8 open issues, envelopes S9/M41/L2/XL0. Forward coverage is
52/52 and 10/10; reverse coverage carries the undeclared PKG-00 and
DEL-00-01/02 (52/54). Reverse-view parity holds on all 52 deliverables; no
duplicate or dangling ID; every objective mapping is valid; OI-008 has four
affected scope items equal to the telemetry. The companion is exactly 83
rows / 50 families / 18 columns with 83/83 pins to the live decomposition.
All 52 contexts and statuses exist; 54/54 `ScopeOfWork.md` validate as
SOW_V1; 51 paired MEMORY files were read. The thirteen registers hash
exactly to the sealed brief, validate against v3.1, carry the applied row
names, anchor every applied scope item and objective with resolvable
pointers, and carry the nineteen emitted D-APP-109 rows once each, ACTIVE
and marked cycle-participating and non-gating. Authority corpus v20: no
drift.

Occurrence-weighted result: 0 blockers, 59 warnings, 25 informational.
Versus the 0518 run (0 / 72 / 10): no new blocker and no new major; zero
new warning occurrences. PA-010-COV-004 is RESOLVED: the D-APP-109 context
alignment brought all thirteen carriers' `_CONTEXT.md` Traceability rows,
Anticipated Artifacts paragraphs, the three PKG-02 Source Authority
paragraphs, and the DEL-08-03 ownership section to the applied rows, with
pre- and post-images verified 39/39, so context fidelity moves from 35 MATCH
/ 17 PARTIAL to 48 MATCH / 4 PARTIAL and no residual remains on those
carriers. The thirteen occurrences leave the warning class and are recorded
as an INFO resolution record. One INFO row is added for a pre-existing
condition the 0518 run misstated: the full register validator rejects
DEL-05-01 and DEL-05-05 on legacy `TargetType` values (byte-identical to the
basis, outside the thirteen carriers, already DC-007 / DC-008 in the closure
audit), so declared-register validity is 50/52, not 52/52. Everything else
is carried unchanged.

Closure readiness is FAIL because four carried contexts still lag
authority, the active snapshot's own `Handoff_State.md` records
`ReadyForNextPhase = NO` and `DerivativePackageState = INCOMPLETE`, the N8
and N9 writes are uncommitted pending owner byte review of the PR #714 second
commit, the post-emission twenty-node and two-node SCCs are recorded and
unresolved, and SCA-APP-009 derivative closure and the SCA-APP-008 residue
remain open. This audit authorizes no application, amendment, pointer
movement, commit, SCC resolution, or downstream act.
