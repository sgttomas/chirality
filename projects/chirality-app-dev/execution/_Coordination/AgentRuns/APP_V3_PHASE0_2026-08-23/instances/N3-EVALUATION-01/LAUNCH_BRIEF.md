# Sealed N3 EVALUATION brief

- RequestedBy: `HELP_HUMAN`
- RunID: `APP_V3_PHASE0_2026-08-23`
- ParentRole: `HELP_HUMAN` (Agent 0)
- InstanceID: `N3-EVALUATION-01`
- Role: `EVALUATION` (Agent 1)
- Objective: produce the evidence-only v3 preparation-lane baseline required by
  N3 of the re-issued App Phase-0 steer, with every fact bound to exact
  `origin/main` bytes at the accepted basis.
- AcceptedBasis: commit `3af765222bbd4f43a52dcbe17bd151c13942e5ac`;
  frozen `origin/main` at the same commit; frontend tree
  `74e3dbe858b5a4e31d7bf4d3d5e9a7e7f13e76eb`.
- SourceScope: repository files named by N3, the Revision 3.1 plan section
  10.1, and repository evidence needed to identify governed Electron `43.1.1`
  and the R18/Tranche-A frozen Electron supply posture.
- FixedContentWriteTarget:
  `projects/chirality-app-dev/execution/_Evaluation/V3_PREP_BASELINE_2026-08-23/`
  only.
- FixedControlPlaneWriteTarget:
  `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_PHASE0_2026-08-23/instances/N3-EVALUATION-01/`
  only.
- PrimaryOutput: `REPORT.md` only in the fixed content write target.
- ControlOutputs: this brief, `STATUS.json`, review evidence, and `RETURN.md`
  only in the fixed control-plane target.
- Toolbelt: read-only Git and filesystem inspection, `rg`, `sed`, `awk`,
  `shasum`, deterministic local scripts for citation verification, and one
  fresh bounded read-only reviewer. No network.
- RequiredCoverage: Electron 43.2.0 package/lock versus governed 43.1.1;
  frozen electronDist source/version/size/SHA; safeStorage null-collapse; CLI
  launcher bundled path and `ELECTRON_RUN_AS_NODE`; hard-coded
  `--runtime-daemon`; secret-scanner extension list; desktop-release credential
  hard-fail; SDK bypass; tool-path argument-only inspection; PEC suffix globs;
  managed sibling overlap; Release Quality Gates section 13; BUILD_AND_RELEASE
  release steps; and the R20 login-proof harness as the seed for a later
  G-HELPER two-label fixture.
- CitationContract: every stated fact cites a repo-relative `path:line` and the
  SHA-256 of that path's exact Git blob bytes at basis, and quotes the cited
  line verbatim. Every citation must reproduce with
  `git show origin/main:<path> | sed -n '<n>p'`.
- ClosingMapping: conclude with the plan section 10.1 AT identifiers fed by
  each fact; observations remain evidence, never authority or an owner ruling.
- Checks: all quotations and line numbers verified programmatically against
  `origin/main`; all cited blob hashes recomputed from `git show`; fixed write
  scopes respected; frontend tree remains untouched and equal to the accepted
  basis; fresh review PASS after unlimited in-scope repair/re-review.
- Escalations: stop and return a genuine blocker if basis bytes move, a required
  fact cannot be evidenced at the frozen basis, a requested write would exceed
  either fixed write target, or a finding cannot be repaired without changing
  evaluated project state.
- Prohibitions: no code, contract, register, lifecycle, pointer, frontend,
  docs, plans, Root, Git index, commit, push, PR, merge, network, artifact,
  login/logout, or provider action; no delegation by the bounded reviewer.
