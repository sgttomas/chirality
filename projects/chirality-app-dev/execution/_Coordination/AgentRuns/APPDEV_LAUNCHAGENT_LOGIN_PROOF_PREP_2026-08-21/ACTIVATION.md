# PKG-09 / DEL-09-04 activation

- RunID: `APPDEV_LAUNCHAGENT_LOGIN_PROOF_PREP_2026-08-21`
- Parent: `HELP_HUMAN`
- ManagerInstanceID: `WI-PKG09-LOGIN-PROOF-PREP-01`
- PackageID: `PKG-09`
- Selected deliverable: `DEL-09-04`
- Objective: prepare a fail-closed harness and minimal owner procedure for a
  later owner-scheduled logout/login proof of actual LaunchAgent login-session
  discovery and auto-start.
- Authority: owner ruling relayed in-session 2026-08-21: `PREPARE-THEN-OWNER`.
  Preparation is authorized; logout/login remains an owner act and is not part
  of this run.
- Accepted basis: D-APP-97 C1; DEL-09-04 live `ScopeOfWork.md`, `_STATUS.md`,
  `MEMORY.md`, `Dependencies.csv`, and `_DEPENDENCIES.md`; R10/R11 D-APP-97
  RunAtLoad records; existing packaged RunAtLoad proof script/tests; committed
  App workplan `WORKPLAN_2026-07-18b_app_dev_loop.md` read from `HEAD`.
- APP-HOLD-1: `ALLOW` for dispatch at
  `b1876a5e0f0083e10c0c18255cd92ed0079b63a2`.
- Software profile: `projects/chirality-app-dev/software-workflow.json` under
  `docs/SOFTWARE_WORKFLOW_PROFILE.md`.
- Write boundary: App-local frontend scripts/tests/config only when essential;
  DEL-09-04 `_run_records/**`, `_STATUS.md`, `MEMORY.md`; this run root.
- Exclusions: no logout/login; no owner LaunchAgent action; no launcher
  mutation; no root or piping writes; no provider/network expansion; no
  signing, notarization, distribution, release, reliance, lifecycle, or
  professional-approval claim.
- Return contract: validated product/test preparation, exact owner procedure,
  independent review over the frozen product diff, checks, residuals, and an
  explicit owner-gated/unexecuted-proof handoff.
