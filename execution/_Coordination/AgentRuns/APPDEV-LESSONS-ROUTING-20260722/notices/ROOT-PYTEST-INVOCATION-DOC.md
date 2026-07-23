# Coordination Notice — document the practitioner-harness / validation pytest invocation

Issued by: HELP_HUMAN, app-dev loop iteration of 2026-07-22 (Receipts 86–88)
Basis: owner in-session adoption 2026-07-22 (Ryan Tufts) routing this item to the root loop
Status: OPEN — owned by the root loop
Priority: low

## What already happened

- The app-dev standing plan requires a full practitioner-harness pytest run at
  closeout. The app-dev loop ran that gate during its 2026-07-22 iteration
  (Receipts 86–88).
- The repository documents no canonical way to run that suite. The gate
  therefore depends on whichever invocation the operator happens to discover,
  making a required closeout check operator-environment-dependent.

## Evidence from the 2026-07-22 iteration

- The default `mise` Python on the operator's machine ships no `pytest`, so a
  bare `pytest` invocation fails before collecting anything.
- The working invocation, run from the repo root, was:

  > `PYTHONPATH=. PYTHONDONTWRITEBYTECODE=1 uvx --with pyyaml pytest tools/practitioner_harness tools/validation`

  Result: 434 passed.
- Two environment facts made it work and are worth recording alongside it:
  - `PYTHONPATH=.` is required because the tests import `tools.validation.*`
    as a package rooted at the repo root.
  - `--with pyyaml` is required because `tools/validation` includes
    `test_validate_domain_engine_profile.py`, which imports `yaml`.

## This notice's ask

Record the canonical invocation in root tooling documentation so the closeout
gate is reproducible independent of operator environment. The placement is the
root loop's choice — for example a `practitioner_harness` row in
`tools/REGISTRY.md`, or a short `README` under `tools/practitioner_harness/`.
The app-dev loop does not write root tooling docs; it routes the evidence here.

## Authority

This is a coordination notice, not an instruction. The root loop adopts,
amends, or declines it under its own decision and review instruments.
