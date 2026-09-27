# Closeout checks — before (base 5d0680951) and after (candidate working tree)

Run from the repository root of the closeout worktree, CPython 3.13.7, PYTHONDONTWRITEBYTECODE=1, TMPDIR under the session scratchpad. Outputs compared byte for byte (cmp); SHA-256 of each output:

| Check | Command | Before | After | Result |
|---|---|---|---|---|
| strict | `python3 tools/validation/validate_decomposition_registers.py --strict projects/pec/execution` | `64b0e91ce3e598f5…` | `64b0e91ce3e598f5…` | identical;   WARNING findings: 26 strict exit 1  |
| harness | `python3 tools/practitioner_harness/harness.py self-check` | `f0231f9354341ed7…` | `f0231f9354341ed7…` | identical; - checks_run: DE-1..8 (domain-engine surfaces incl. stale open issues vs later rulings), GEN-1 (abs-path), GEN-2 (ruling |
| receipts | `python3 tools/validation/validate_pec_loop_receipts.py --repo-root .` | `a9a1ef0f0fe0a048…` | `a9a1ef0f0fe0a048…` | identical; VALID projects/pec/loop/LOOP_RECEIPTS.m |
| tm_open | `python3 tools/taskmgmt/taskmgmt.py validate --register …/_TaskManagement/REGISTER.csv` | `5dba917a5cc0f672…` | `5dba917a5cc0f672…` | identical; taskmgmt validate PASS: projects/pec/execution/_Coordination/_TaskManagement/REGISTER.csv — 9 row(s), schema columns a |
| tm_closed | `python3 tools/taskmgmt/taskmgmt.py validate --register …/_TaskManagement/REGISTER_CLOSED.csv` | `ec97db8613aebb3d…` | `ec97db8613aebb3d…` | identical; taskmgmt validate PASS: projects/pec/execution/_Coordination/_TaskManagement/REGISTER_CLOSED.csv — 16 row(s), schema c |

Strict registers: 0 ERROR / 26 WARNING (the D-GOV-48 XRG-013 set), exit 1, identical before and after. Harness self-check exit 0; receipts validator exit 0 (ledger frozen); Task Management registers PASS (9 live, 16 archived), unchanged. `git diff --check 5d0680951` clean.
