# Validation Record — G2-DELIVERABLE-OWNERSHIP-20260726

Basis: `2db2c712825af13d6b5425c34d31ff9daf470c89`

## Results

| Check | Result |
|---|---|
| Focused G2 + G4 tests | `60 passed in 0.60s` |
| Live basis G2 | `PASS`; 6 entries, 6 materialized package children |
| Pending Project Setup candidate G2 | `PASS`; 7 entries, 6 materialized package children |
| G4 CI-mode manifest validation | `PASS`; 8 manifests schema-valid |
| New-manifest direct schema validation | `PASS`; zero failures, zero notes |
| Worktree instruction-path coverage using G4 path predicates | `PASS`; 3 touched instruction paths, zero uncovered |
| `git diff --check` | `PASS` |
| Read-only adversarial review | `PASS` |

## Commands

```text
PYTHONDONTWRITEBYTECODE=1 python -m pytest -q -p no:cacheprovider \
  tools/validation/test_validate_root_surface_ownership.py \
  tools/validation/test_validate_instruction_tranche_manifest.py

PYTHONDONTWRITEBYTECODE=1 \
  python tools/validation/validate_root_surface_ownership.py

PYTHONDONTWRITEBYTECODE=1 \
  python tools/validation/validate_instruction_tranche_manifest.py

PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=tools/validation python -c \
  '<validate only G2-DELIVERABLE-OWNERSHIP-20260726.yaml with
  validate_manifest()>'

PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=tools/validation python -c \
  '<compare git-status instruction paths against the new manifest with G4
  intersects_instruction_surface() and covered_by()>'

PYTHONDONTWRITEBYTECODE=1 \
  PYTHONPATH=/Users/ryan/dev/chirality-g2-deliverable-validator/tools/validation \
  python -c '<run g2.check() against
  /Users/ryan/dev/chirality-root-project-setup-del0206>'

git diff --check
```

The Apple system `python3` lacks `pytest`; the repository-default `python`
resolved to the installed Python 3.13 environment and ran the suite. Pytest
cache creation was disabled, and bytecode writes were suppressed.

## Candidate hashes

```text
5d755ff5b2ee357694517c3ba8b4d0d7bba0acc671dfc5b784516257b8669b4a  tools/validation/validate_root_surface_ownership.py
e74bdf75f241cc5a781393a5479af336e4724a5385d34e08732010547d2e6c4a  tools/validation/test_validate_root_surface_ownership.py
478431b966f41105f924b6ac2a1a3f3aaf02b97fb219cfe55b69f3bdcbacb157  docs/governance_harness/tranche_manifests/G2-DELIVERABLE-OWNERSHIP-20260726.yaml
```

The manifest hash changed during Agent 0 closeout because the public-export
derivative was explicitly identified and deferred. No export byte changed.

## Observation boundary

The checks establish deterministic behavior over register entries, declared
write targets, companion-register IDs/package ownership, filesystem
existence/containment, manifest schema, and the named candidate checkout.
They do not establish semantic acceptance, inspect deliverable contents,
discover unregistered nested deliverables recursively, amend Project Setup,
or authorize Git integration.
