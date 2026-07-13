# WORKING-A2-PKG06 Checks

Verdict: `PASS`.

## Fan-in and preservation

- Exact package membership: 6/6 (`DEL-06-01` through `DEL-06-06`).
- Author/verifier pairs: 6/6 terminal `PASS` / `PASS_UNCHANGED`.
- Candidate hashes: 6/6 match author, verifier, member-result, and replacement bindings.
- Preservation: 195 mappings cover 2,116 source lines with zero parity issue.
- Child manifests: 12/12 self-excluding; 362/362 file/hash/byte bindings reproduce.
- Live preflight bindings: 54/54 source, status, and control hashes reproduce.
- Live format: 6/6 remain exact `LEGACY_FOUR_DOC`, `IN_PROGRESS`, with zero live `ScopeOfWork.md`.
- Replacement: 30 exact rows (six SOW adds, 24 legacy deletes); no status/control path.
- Rollback: 30 exact rows and pairwise inverse of replacement.
- Candidate scope: exactly six `ScopeOfWork.md` files under `candidates/W_A2/APP-PKG06/**`.

## Registered App checks

The initial combined record is preserved in `PROJECT_CHECKS.json`:

| Check | Result | Evidence |
|---|---|---|
| `harness-self-check` | PASS | registered App profile |
| `harness-pytest` | PASS | 264 tests passed |
| `frontend-typecheck` | PASS | registered typecheck |
| `frontend-test` | PASS | 713 passed, 4 skipped |
| `frontend-build` | PASS | production and Electron build |
| `frontend-premerge` | FAIL (substrate only) | no API server; zero tests |

The initial failure was retained. A temporary `CHIRALITY_HARNESS_PROVIDER=stub`
Next server was started on the registered local port, and only
`frontend-premerge` was rerun through the registered profile. The separate
`PROJECT_CHECKS_PREMERGE.json` is `PASS`: Section 8 is 8/8 and Section 9 is
16/16 report-only. The server was stopped immediately afterward.

## Portability and containment

- Eleven generated evidence files were normalized with 46 repo-root and six
  temporary-directory substitutions; every row has an exact reverse proof.
- Twelve child manifests were mechanically rebound; all 362 bindings reproduce.
- Generated candidates, checks, returns, run records, manifests, and package
  records contain zero machine repo-root or temporary-directory literals.
- Fifty-one repo-root literals remain only in 18 byte-identical copied
  source/control files and are inventoried, not rewritten.
- `git status` for `projects/chirality-app-dev` is empty after check residue.
- `git diff --check` passes for the PKG-06 candidate/evidence scope.
- No live project, lifecycle, Git, H1/H2, or other-package write occurred.

Blockers: none. Waivers: none. Rerun requirements: none.

