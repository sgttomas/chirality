# PEC Execution Scripts

Standalone deterministic validation and preflight tooling for the PEC
execution workspace.

## `pec_reliance_hold.py` (D-PEC-67 / L-A1)

Evaluates one target, clause set, and operation against the authoritative
`execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv` register. Active held
clauses block production reliance, production dispatch, promotion, and
consumption regardless of entry path. Historical read-only inspection, exact
correction preparation, and candidate validation remain allowed.

The tool is read-only and emits one JSON result. Exit 0 permits, 3 rejects an
unreadable or malformed register, and 4 blocks a held operation. It has no
runtime-exception input.
