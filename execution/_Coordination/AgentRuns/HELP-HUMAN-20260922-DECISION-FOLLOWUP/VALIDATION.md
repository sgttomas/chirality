# Proposal-candidate validation

Source base: `e74feb34b7ca99ebeb903ffb52f7fdd2b3efd169`.
Scope: two proposal packages, this coordination record and two graph continuation
updates. No product, accepted scope, dependency basis, instruction or workflow
change. Native/product checks are not claimed by these document checks.

| Check | Result | Evidence / consequence |
|---|---|---|
| `PYTHONDONTWRITEBYTECODE=1 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 -m pytest -q tools/practitioner_harness` from repository root | PASS, 379 tests, exit 0 | `validation/practitioner-pytest.log`; Python 3.13, inherited host environment, no product configuration overrides |
| `python3 -B tools/practitioner_harness/harness.py self-check` from repository root | PASS, exit 0; no BLOCK | `validation/self-check.log`; INFO=14, NOT_APPLICABLE=1, REVIEW=4, WARN=113 retained; no warning cleanup or waiver |
| `python3 execution/_Scripts/app_hold.py scan --require-register-match` from App root | PASS, 54 contracts, 0 active holds, register matches | `validation/app-hold.json`; this structural guard does not release substantive decision holds |
| App author reliance preflight | ALLOW, eight actual targets | App proposal `SOURCES.json` retains exact invocation and result |
| `python3 tools/validation/validate_app_dev_loop_receipts.py --repo-root .` | PASS, exit 0 | Frozen through Receipt-52, versioned contract satisfied; receipt unchanged |
| `python3 tools/validation/validate_piping_loop_receipts.py --repo-root .` | PASS, exit 0 | Frozen through Receipt-44, versioned contract satisfied; receipt unchanged |
| Source hashes, candidate bindings, graph preservation and guide links | PASS | `validation/structure-check.json`; source SHA-256 values recomputed, both historical graph objects and bytes before current_continuation match base, linked files exist |

The last check is direct artifact verification, not a new maintained test suite.
Recompute source SHA-256 values from each proposal's SOURCES.json; compare each
graph to the base after excluding current_continuation, and compare prefix bytes
before that key. Resolve guide links relative to this directory. The independent
reviews additionally inspect meaning and ownership, which hashes cannot prove.

Review findings and final checked path identities belong in PIPING_REVIEW.md
and APP_INTEGRATION_REVIEW.md. Corrections require affected backchecks.
Commit-range conflict-marker/G4 checks and required hosted CI must cover the
actual submitted commit; their final outcomes are recorded in the PR. A
successful proposal merge is not acceptance of its proposed decisions.
