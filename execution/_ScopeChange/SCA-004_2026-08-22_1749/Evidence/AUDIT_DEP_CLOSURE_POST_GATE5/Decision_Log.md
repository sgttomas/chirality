# Decision log — post-Gate-5 dependency closure

## DC-DL-001 — Output-location override

The Phase-1 steer and sealed brief require this SCA evidence folder and forbid
the default `execution/_Evaluation/DepClosure/` root and pointer. That human
override controls this run.

## DC-DL-002 — Root-local source model

The generic repository analyzer only discovers `Dependencies.csv` registers.
Root currently has zero such files. This preserved script therefore binds the
53 applied register rows to their live `_DEPENDENCIES.md` containers, while
retaining the generic core-check semantics and never inferring edges from prose,
shared objectives, or package membership.

The generic tool was also invoked exactly as prescribed, with its output
captured under `Generic_Tool_Raw/`. It deterministically reported zero CSV
files, zero nodes, and zero edges. `normalize_generic_raw()` deterministically
normalizes those preimages to LF with a terminal newline before hashing. Those
bytes are preserved as method evidence, not misread as the live 53-node
coverage result.

## DC-DL-003 — Expected post-INIT state

The seven N1 containers are classified `EXPECTED_POST_INIT_EMPTY`, not defects.
The 46 pre-existing containers remain `PRE_EXISTING_NOT_RUN_YET`. Missing
extracted schema and anchor coverage are warnings; absence of a dependency edge
is not itself a closure violation.

## DC-DL-004 — Cycle disposition

No non-trivial SCC exists, so no move is required and no human-gated cut/merge
was made. The rerun after extraction must apply the cycle-resolution doctrine.

## DC-DL-005 — Immutable derivative boundary

The accepted SCA-004 snapshot, live decomposition, pointer, deliverable
metadata, Task Management state, and prior audit were read-only. This package
must be regenerated after accepted SOWs and dependency extraction.
