# WORKING-A1-PKG00 Package Checks

Overall verdict: `PASS`.

## Basis and live rows

- Dispatch basis local `HEAD`, `main`, `origin/main`, and remote main was
  `34b87ec77010035eeaa76f0fa65981ec57e78933` at activation.
- The accepted row basis is
  `0724f26f6ef79d733c8f1c513b29d837fd43c8eb`; the intervening commit is
  evidence-only activation state with zero `projects/**` path.
- Both exact manifest members remain `IN_PROGRESS`, non-pilot, non-ISSUED,
  exact live `LEGACY_FOUR_DOC`, no live `ScopeOfWork.md`, and intentionally no
  `Dependencies.csv`.
- All sixteen frozen source/status/control hashes match the accepted manifest
  and live project at package close. Status hashes remain
  `7d8e0d99d5371986257bc9165cd50733d1fb9d72691066c84e5765ac08c8c46f`
  and `2d86b9a502936d285436d70a83145ede6721e85c1ff07806e5129a7f50291d3d`.

## Author/verifier fan-in

Both authors and both fresh, separate verifiers have terminal `PASS` durable
returns. No child delegated or contacted a sibling. The manager accepted each
author before releasing its verifier.

| Member | Candidate SHA-256 | Mappings | Source lines | Author | Verifier |
|---|---|---:|---:|---|---|
| DEL-00-01 | `2e51af467ef3ccfd8c79e7b2fe04bcbfed5d56af2e66fbf3792e74ae2600c838` | 26 | 250 | PASS | PASS |
| DEL-00-02 | `acd4fc457339b6aa9c1d29c6b598f2dc0e7ba51bada2fb719fab0d297e466045` | 30 | 276 | PASS | PASS |

Aggregate coverage is 56 mappings over all 526 source lines. All dispositions
are preserved and parity has zero drop or mismatch. Every candidate directory
contains exactly `ScopeOfWork.md`; both candidate-only directories validate as
exact `SOW_V1`. Each author workspace and fresh verifier workspace validates
as authorized isolated `MIGRATION_DUAL` under exact
`D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176`.

Independent verifier gates passed for exact source/status/control/candidate
identity, map and target resolution, parity and line coverage, conservative
OUT/AC/VER semantic authority, duplicate checklist byte stability and exact
linkage, duplicate render byte stability and script/external-resource safety,
partial and unauthorized-dual fail-closed fixtures, replacement paths, and
write containment. Schema, content authority, preservation, and execution
substrate are separately `PASS` for both members.

## Execution-substrate records

- AUTHOR-DEL-00-02 first supplied the orchestration manager label
  `APP-PKG-00` to the converter. The schema guard rejected it before output;
  direct existence checking proved no partial candidate survived. The accepted
  invocation/candidate binds only canonical manifest package `PKG-00`.
- The first combined project-check run invoked `frontend-premerge` before a
  harness API was running. It failed immediately with zero tests. This is
  preserved in `PROJECT_CHECKS.json` as non-accepted substrate evidence.
- The exact registered `frontend-premerge` check was rerun as R1 with a
  temporary local Next harness API pinned to the keyless stub provider. It
  passed 8/8 Section 8 tests and the report-only Section 9 validation (16 test
  IDs); the server was then stopped. `PROJECT_CHECKS_PREMERGE_R1.json` is the
  accepted premerge result.

Neither substrate event altered candidate meaning, accepted inputs, authority,
project truth, or the acceptance criteria.

## Required App package checks

| Registered check | Result |
|---|---|
| `harness-self-check` | PASS |
| `harness-pytest` | PASS — 264 tests |
| `frontend-typecheck` | PASS |
| `frontend-test` | PASS — 97 files / 713 tests; 1 file / 4 tests skipped |
| `frontend-build` | PASS |
| `frontend-premerge` R1 | PASS — Section 8: 8; Section 9 report-only: 16 |

## Replacement, rollback, portability, and containment

- `REPLACEMENT_MANIFEST.tsv` has exactly ten non-header rows: one ADD
  `ScopeOfWork.md` and four DELETE legacy-production rows per member.
- `ROLLBACK_MANIFEST.tsv` has the exact ten inverse actions with the same paths
  and hashes. Neither manifest contains `_STATUS.md` or another control path.
- Both verifier five-row manifests are semantically byte-identical to their
  manager-manifest slices after normalizing the verifier's optional
  `deliverable_id` column.
- Checkout-specific prefix hits: 0. Machine-specific temporary-prefix hits: 0.
  Registered check evidence uses `~/` and `${TMPDIR}/` anchors.
- Live `projects/chirality-app-dev/**` tracked/untracked dirty paths: 0.
- Candidate directories contain only their two authorized SOW files.
- `git diff --check` over this package and candidate scope: PASS.
- Writes remain inside `candidates/W_A1/APP-PKG00/**` and
  `instances/WORKING-A1-PKG00/**`.

## Closure disposition

Blockers, conflicts, unknowns, waivers, and human rulings needed: none. This is
a derivative candidate recommendation only. RECONCILIATION remains mandatory
before CHANGE may perform any later atomic project-tree replacement.
