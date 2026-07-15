# RECON-CLOSURE Attempts

## Attempt 1 — mechanics path binding

- Command: `python3 instances/RECON-CLOSURE/reconcile_closure.py` from the
  repository root using the full run-relative path.
- Result: failed before reading the corpus because the runner bound `ROOT` to
  the `execution/` directory and could not import `tools/scope_of_work/common.py`.
- Project writes: none.
- Evidence writes: none.
- Disposition: retained mechanics failure; corrected `ROOT` from `parents[5]`
  to `parents[6]` without changing audit scope or acceptance criteria.

## Attempt 2 — accepted-package and action-schema binding

- Result: corpus and caller checks reproduced, but the manifest aggregate was
  incomplete because it omitted the later accepted package-batch adoption
  snapshot for Piping PKG-01/02. The W-P4 rollback also uses `RESTORE` where
  earlier ledgers use `ADD`, which the first normalizer did not bind.
- Project writes: none.
- Evidence writes: provisional `evidence/*` only; retained and superseded by
  the rebound run.
- Disposition: added the accepted eight-member package-batch reconciliation
  pair and normalized `RESTORE` to the same add transition. The candidate
  residue check was tightened to the finalizer's exact forbidden marker
  families; acceptance criteria remain unchanged.

## Attempt 3 — frontend dependency binding

- Direct `npm run typecheck` in this fresh worktree returned 127 because this
  worktree has no `node_modules` and `tsc` was unavailable.
- Project writes: none; the failed output is retained as overwritten command
  evidence in the rebound suite.
- Disposition: run the exact checked-out frontend copy in a disposable `/tmp`
  root against the existing dependency cache from the primary worktree. This
  follows the ignored-state containment rule: no dependency tree or build
  output is created in the closure worktree.

## Attempt 4 — frontend repository-root fixture binding

- The first disposable frontend-only copy passed typecheck and build but four
  tests failed because their intentional repository-root fixtures resolved to
  `/private` rather than the copied frontend's source repository.
- Project writes: none; disposable root removed automatically.
- Disposition: preserve the external-copy posture while reconstructing the
  repository-relative layout in `/tmp` with read-only symlinks to the exact
  checked-out root and project siblings. Frontend sources and build output
  remain isolated copies.

## Attempt 5 — deliverable-count command binding

- The first count invocation omitted the required project execution-root
  argument and exited 1 with usage text before scanning.
- Project writes: none.
- Disposition: retained the failed invocation and reran once for each accepted
  project execution root.
