# Federation preflight for applying the 2026-09-27 dispositions

Scope: this is the `task-management` row-maintenance step that applies the owner's
`D-PEC-107` dispositions of this folder's intake. Only those dispositions and the
K3 row are applied, with no harvest and no `scan`. Actor: the WORKING_ITEMS manager of node TM1 of
`HELP-HUMAN-PEC-20260927-RV1-INTAKE`. Basis: `origin/main` `acc7d3cc7` (the
PR #1018 merge), fetched 2026-09-27. Run from the repository root of its own
worktree, CPython 3.13.7, with `PYTHONDONTWRITEBYTECODE=1`. Tool
`tools/taskmgmt/taskmgmt.py` SHA-256
`9c5cdc562053b2cc2eeb6674b750d95cb7fa47971eb07acee010a404c221d101`.

Command, run before and after the register write (`--out` names differ):

```text
python3 tools/taskmgmt/taskmgmt.py federation \
  --register projects/pec/execution/_Coordination/_TaskManagement/REGISTER.csv \
  --out projects/pec/execution/_Coordination/_TaskManagement/.candidates/TM1_RV1_INTAKE_2026-09-27/federation.json
```

Both runs exited 0. The output directory was verified Git-ignored first
(`.gitignore:95`). The projections are derived, not authority, and are not
committed. Their SHA-256 values are `1cf6a25c…a6f5` (before) and `8d89637f…edb1` (after).

| Run | Coverage | Findings | Classes | PEC position |
|---|---|---:|---|---|
| Before | COMPLETE, 4 registers, 0 operational errors | 28 | `LOCAL_CLOSED_REMOTE_OPEN` 22, `MISSING_NOTICE` 5, `REMOTE_CLOSED_LOCAL_OPEN` 1 | OPEN 8, DEFERRED 1; archived 16 |
| After | COMPLETE, 4 registers, 0 operational errors | 28 | the same | OPEN 9, DEFERRED 2, ELEVATED 1; archived 16 |

No finding in either run involves a PEC row. The counts equal the closeout
intake's preflight (`FEDERATION_PREFLIGHT.md`). `TM-PEC-027`'s `NoticeRef`
resolves to the Root notice, so it raises no `MISSING_NOTICE`. `ElevatedTo`
`Root` names a register without inventing a row ID, so it raises no link finding.
Deduplication: the closeout preflight compared the live rows. A re-search of the Root
register at `acc7d3cc7` found no row about hosted PEC v2 checks.
