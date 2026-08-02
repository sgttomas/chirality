# Baseline — Task Management Federation Survey

Basis: `main@3e03b257748822dba2ad7697453f3495fb7578db`
Branch: `codex/task-management-federation-survey`
Date: 2026-08-02

## Register SHA-256 values before implementation

| Register | SHA-256 |
|---|---|
| `execution/_Coordination/_TaskManagement/REGISTER.csv` | `584ee4f9eaa4006c37c248077b26d1aadd5e8678833c46991a2d1101b4fac0ac` |
| `projects/chirality-app-dev/execution/_Coordination/_TaskManagement/REGISTER.csv` | `e6a3de4c96e4471c1bf4157e1e65f8e9b607534c3a61e395abf87a61ae9bfd64` |
| `projects/chirality-piping/execution/_Coordination/_TaskManagement/REGISTER.csv` | `bdfef05ec04d8a64fd8c86bdddc679a48e5317c4557613dd5c8762c9de5b68ce` |
| `_DomainEngines/pec/_TaskManagement/REGISTER.csv` | `85b8e0a66975ffa44fec6db8597940ff2d87f61e8bd09316d1ea0e1d874a9c91` |

## Baseline checks

- `python3 -m pytest tools/taskmgmt/test_taskmgmt.py -q` — PASS, 16 tests.
- `python3 tools/validation/validate_agent_instructions.py` — PASS, 34 files,
  0 errors, 0 warnings.

These values are evidence for the required zero-register-write comparison at
fan-in. They are not authority or semantic acceptance.
