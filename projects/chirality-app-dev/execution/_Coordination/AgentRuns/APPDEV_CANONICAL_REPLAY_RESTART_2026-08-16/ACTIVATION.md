# WORKING_ITEMS activation — PKG-05 canonical replay restart

- RunID: `APPDEV_CANONICAL_REPLAY_RESTART_2026-08-16`
- InstanceID: `WI-PKG05-CANONICAL-REPLAY`
- PackageID: `PKG-05`
- Selected deliverable: `DEL-05-04`
- Objective: prove Desktop and CLI replay the same daemon-owned canonical session across daemon restart and lazy legacy migration while preserving recorded manager/child attribution.
- Accepted basis: branch `codex/app-dev-parallel-product-nodes` at `44903bc69cf56d4ca794fe9629f26793a82bf1b3`; D-APP-73 ruled daemon/client/CLI and non-destructive lazy central-session migration; the live Root `SessionStore`, daemon, client, App compatibility port, and Woven Dialogue projection seams are present and read-only.
- Gate/selectability finding: the named `daemon/client vertical slice` is satisfied by ruled D-APP-73 plus live daemon/client/replay implementation and existing vertical-slice tests. The residual is still real because no App test combines Desktop/CLI same-session replay, daemon restart, lazy migration, and manager/child attribution.
- APP-HOLD-1: supervising dispatch preflight reported `ALLOW`; this instance independently received `ALLOW` for DEL-05-04 reliance and accepted-dependency consumption of DEL-05-01, DEL-05-02, and DEL-08-05.
- Profile: `projects/chirality-app-dev/software-workflow.json` under `docs/SOFTWARE_WORKFLOW_PROFILE.md`.
- Write boundary: dedicated PKG-05 test(s); only demonstrably necessary App product fixes under `frontend/src/lib/runtime-client/**` or `frontend/src/lib/woven-dialogue/**`; DEL-05-04 `_STATUS.md`, `MEMORY.md`, one `_run_records/**` record; this run root.
- Exclusions: Root `runtime/**`, `frontend/electron/**`, manifests/lockfiles, receipts, completion log, decisions/registers, authority docs, loop plans, other packages/deliverables, PKG-08 node files, and Git mutation.

## D-APP-64 reasoned selection

Selected: add a dedicated PKG-05 integration proof against the existing public runtime seams, with App source repair only if the proof exposes a defect. This best preserves Root runtime ownership, package attribution, and disjoint parallel-node writes. Rejected: extend the PKG-03 model-drain test (wrong package ownership and parallel collision risk); change Root runtime (outside authority and no demonstrated defect); add projection-only unit evidence (cannot prove cross-client restart/migration canonicality).
