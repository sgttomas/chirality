# Validation Record — ROOT-HARNESS-46-PIN-20260726

Accepted instruction basis:
`ff04694afa709856a58f9f54a79ca2056b8e0b4e`  
Project Setup predecessor candidate:
`dd28d201b8bc7c7fb534cf6ff75817da25023120`

## Results

| Check | Result |
|---|---|
| PR #369 authoritative failed-job inspection | exactly 3 stale live-root failures; full CI test run was 3 failed / 346 passed |
| Focused `test_root_adoption.py` candidate | `38 passed in 1.28s` |
| Complete practitioner-harness suite after brief amendment | `349 passed in 33.39s` |
| G0–G4 complete registered test set | `124 passed in 1.58s` |
| Live G0 validator | `PASS`; G1–G4 registered/passing |
| Live G1 validator | `PASS`; 46 observed and pinned files, pin `2db2c712...` |
| Live G2 validator | `PASS`; 7 entries, 6 materialized package children |
| Live G3 validator | `PASS`; 6 nodes, none active |
| Live G4 CI validator | `PASS`; 9 manifests schema-valid |
| New-manifest direct validation | `PASS`; zero failures, zero notes |
| Actual instruction-path coverage predicates | `PASS`; 2 touched, zero uncovered |
| Authorized-write coverage | `PASS`; zero unauthorized paths |
| Pin-only overlay on accepted 45-file base | expected `FAIL`; exactly 3 failures / 35 passes |
| Read-only Agent 2 adversarial review | `PASS`; non-blocking adapter-comment residual only |
| `git diff --check` | `PASS` |

## Static live facts proved

- Adapter baseline: 46 files, zero mismatch.
- Measured drift: 46 files, 46 matches, zero mismatch, zero unparseable
  documents, zero documents without a state assertion.
- Lifecycle distribution: 45 `INITIALIZED`, one `OPEN`; total 46.
- DAG posture: not declared by `root-harness-adapter/v1`, unchanged.
- Expected values are literal constants and are not derived from the live
  tree.

## SCC negative proof

A scratch archive of accepted basis `ff04694` was created under `/tmp`. The
candidate `test_root_adoption.py` was overlaid without any Project Setup state.
The focused run returned exactly:

```text
3 failed, 35 passed in 0.90s
```

The three failures were the adapter 46-vs-45 pin, drift 46-vs-45 pin, and the
missing one-`OPEN` status row. This proves the 46-file pin cannot pass on the
45-file base. Conversely, PR #369 job `89892137423` proves `dd28d201b` without
the refreshed pin fails exactly those three assertions. The recorded
cycle-resolution move is `MERGE`: separate commits within one human-gated PR.

## Commands

```text
PYTHONDONTWRITEBYTECODE=1 python -m pytest -q -p no:cacheprovider \
  tools/practitioner_harness

PYTHONDONTWRITEBYTECODE=1 python -m pytest -q -p no:cacheprovider \
  tools/validation/test_validate_root_materialization_fence.py \
  tools/validation/test_validate_root_harness_adapter.py \
  tools/validation/test_validate_root_surface_ownership.py \
  tools/validation/test_validate_root_work_graph_dispatch.py \
  tools/validation/test_validate_instruction_tranche_manifest.py

PYTHONDONTWRITEBYTECODE=1 \
  python tools/validation/validate_root_materialization_fence.py
PYTHONDONTWRITEBYTECODE=1 \
  python tools/validation/validate_root_harness_adapter.py
PYTHONDONTWRITEBYTECODE=1 \
  python tools/validation/validate_root_surface_ownership.py
PYTHONDONTWRITEBYTECODE=1 \
  python tools/validation/validate_root_work_graph_dispatch.py
PYTHONDONTWRITEBYTECODE=1 \
  python tools/validation/validate_instruction_tranche_manifest.py

PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=tools/validation python -c \
  '<directly validate only ROOT-HARNESS-46-PIN-20260726.yaml>'

PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=tools/validation python -c \
  '<compare tracked plus untracked candidate paths with G4
  intersects_instruction_surface() and covered_by() predicates>'

git diff --check
```

The Apple system Python lacks `pytest`; the installed Python 3.13 interpreter
at `/Users/ryan/.local/share/mise/installs/python/3.13/bin/python3` ran the
suites. Bytecode and pytest-cache writes were disabled.

## Candidate hashes before this validation record

```text
28165baf063ad6e9a1c83991bb95f51d527a64893489d8ff64b4770e032aa9ad  tools/practitioner_harness/test_root_adoption.py
f1311e5ddcdd0b93eb9d25ac8a5ba96c27836b1127c7459e61d727a7e22aa106  docs/governance_harness/tranche_manifests/ROOT-HARNESS-46-PIN-20260726.yaml
67cc3ccbe0d2b99e0e0d42a94729dcb0c90f0f5d2a945b0c8b1ce1d8b0671410  execution/_Coordination/AgentRuns/ROOT-HARNESS-46-PIN-20260726/ADVERSARIAL_BRIEF.md
49395f089995cc4d5b0b5fb5b5224d1a05d17c574cf03a44f212b67af3a1746e  execution/_Coordination/AgentRuns/ROOT-HARNESS-46-PIN-20260726/ADVERSARIAL_RETURN.md
527e0a93f96d05ba14624a102943d4a760a2f3778842be1d48a36c9edbca8e09  execution/_Coordination/AgentRuns/ROOT-HARNESS-46-PIN-20260726/BRIEF_AMENDMENT_01.md
d8266adbf0d616fd7ab0470dd0332db4173db9ba8112d02c310dd2a1ba9d5a01  execution/_Coordination/AgentRuns/ROOT-HARNESS-46-PIN-20260726/HANDOFF_STATE.md
6fc47c1a797135f9d7550c9d7f75763cd003ccc98ff515c8921b8055acfc19ba  execution/_Coordination/AgentRuns/ROOT-HARNESS-46-PIN-20260726/IMPLEMENTATION_RETURN.md
5e7cff53f0edbff9987fd5ee7d9bcfedcbc49fba66e1cb6c690082359e83950c  execution/_Coordination/AgentRuns/ROOT-HARNESS-46-PIN-20260726/RUN_MANIFEST.md
```

## Observation boundary

The checks establish the literal static pins, live adapter/status/drift
measurements, registered guard behavior, manifest schema/coverage, authorized
path containment, and the named Git states. They do not semantically accept
PR #369, regenerate the public export, correct the excluded adapter preamble,
or grant Git integration.
