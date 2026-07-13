# WORKING-P-P Scheduling Amendment — v3

Authority: explicit parent scheduling direction after terminal PASS of App
WORKING-P-A and release of all child slots.

This amendment changes scheduling only. The four v2 verifier briefs,
objectives, accepted basis, read/write scopes, acceptance criteria, failure
isolation, and fan-in gates remain unchanged.

- At most two disjoint Piping verifier children may run concurrently.
- Dispatch `TASK-PIP-13-01` and `TASK-PIP-13-02` first.
- Replenish the numeric next child only after the manager accepts a terminal
  PASS from an active child.
- A failed or invalid child blocks only its declared dependent fan-in and is
  not repaired; independent active work may finish, but no replacement child
  is launched into the failed lane without parent direction.
- Package fan-in still requires four manager-accepted terminal PASS returns.

Resume preflight passed on `main@0d260eb024d8b8dada0df477b70ac880a6906ffa`:
main/origin/remote divergence `0/0`; four P3 rows, 20 live source/status
hashes, four `IN_PROGRESS` states, frozen legacy inputs, and four candidate
hashes remain exact.
