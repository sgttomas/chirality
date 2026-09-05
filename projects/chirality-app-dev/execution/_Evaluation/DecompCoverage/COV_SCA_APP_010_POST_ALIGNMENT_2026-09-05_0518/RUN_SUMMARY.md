# Run Summary — SCA-APP-010 Post-alignment Fresh Full Audit

**RUN_STATUS:** WARNINGS
**OVERALL_STATUS:** WARNINGS
**CLOSURE_READINESS:** FAIL
**Basis:** `d66395d101143df68d956984f7ab93f5027418ec` plus the working tree (thirteen refreshed registers, uncommitted)
**Timestamp:** `2026-09-05T05:35:53-06:00`
**RUN_LABEL:** `SCA_APP_010_POST_ALIGNMENT`

Executed by Claude Fable 5.1 (Anthropic, `claude-fable-5-1`) as a Claude Code
subagent acting as AUDIT_DECOMP, dispatched by HELP_HUMAN; role not
mechanically enforced; no descendant launched. Read-only on every
deliverable, the live decomposition and companion register, and all SCA
snapshots; wrote only the nine named files plus `MANIFEST.sha256` into
`projects/chirality-app-dev/execution/_Evaluation/DecompCoverage/COV_SCA_APP_010_POST_ALIGNMENT_2026-09-05_0518/` and the instance
`RETURN.md` and `STATUS.json`; `_Evaluation/DecompCoverage/_LATEST.md` not
moved (brief override, Decision PA-010-001).

The live pair equals the approved SCA-APP-010 post-images (`c7c05169...`,
`63383f04...`); `_LATEST.md` (`b297f43e...`) names SCA-APP-010 under the
G5-POINTER ruling. Topology is 10 packages / 52 deliverables / 84 scope rows
(79 IN / 4 OUT / 1 TBD), 10 objectives, 8 open issues, envelopes S9/M41/L2/XL0.
Forward coverage is 52/52 and 10/10; reverse coverage carries the undeclared
PKG-00 and DEL-00-01/02 (52/54). Reverse-view parity holds on all 52
deliverables; no duplicate or dangling ID; every objective mapping is valid;
OI-008 has four affected scope items equal to the telemetry. The companion is
exactly 83 rows / 50 families / 18 columns with 83/83 pins to the live
decomposition. All 52 contexts and statuses exist; 54/54 `ScopeOfWork.md`
validate as SOW_V1 (DEL-09-07 added since Gate 5); 51 paired MEMORY files were
read. The thirteen refreshed dependency registers hash exactly to the sealed
brief, validate against v3.1, carry the applied row names, and anchor every
applied scope item and objective, with Root-owned targets EXTERNAL/TBD.
Authority corpus v20: no drift.

Occurrence-weighted result: 0 blockers, 72 warnings, 10 informational.
Versus the Gate-5 post-change audit (0 / 74 / 8): no new blocker and no new
major; zero new warning occurrences. G5-010-COV-005 (DEL-02-02 name lag) is
resolved at the context by PR #713 (the folder label is retained by design,
INFO). G5-010-COV-004 is only partially resolved: PR #713 aligned the
thirteen carriers' identity, DeliverableName, Package Scope, and Deliverable
Scope exactly as the WI permitted effect names, but the Traceability
`CoversScopeItems` table on nine carriers and the Anticipated Artifacts
paragraph on ten still lag the applied rows, and DEL-08-03's
ownership-boundary section still names the retired DEL-02-02 consumer, so all
thirteen remain PARTIAL (13 occurrences) and need a further WORKING_ITEMS
authorization. The SCA-APP-009 state-field vocabulary warning is reclassified
to INFO because SCA-APP-009 is no longer the active snapshot; SCA-APP-010's
handoff state exposes all seven fields by name and does not overclaim.
Everything else is carried unchanged.

Closure readiness is FAIL because seventeen contexts still lag authority,
the active snapshot's own `Handoff_State.md` records `ReadyForNextPhase = NO`
and `DerivativePackageState = INCOMPLETE`, the refreshed registers are
uncommitted pending owner byte review, and SCA-APP-009 derivative closure and
the nine-node SCC remain open. This audit authorizes no application,
amendment, pointer movement, commit, or downstream act.
