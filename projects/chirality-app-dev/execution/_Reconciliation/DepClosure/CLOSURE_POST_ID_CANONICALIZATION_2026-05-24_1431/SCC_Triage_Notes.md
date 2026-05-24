# SCC Triage Notes

## Recommended Order

1. Resolve or rule on SCC-002 first because it has only two nodes and two concrete rows.
2. Then triage SCC-001 using the current bidirectional-pair evidence.

## SCC-002 Initial Reading

Rows:

- `DEP-10-02-004`: `DEL-10-02` upstream `DEL-10-03`, `INTERFACE`, `TBD`, `MEDIUM`.
- `DEP-10-03-006`: `DEL-10-03` upstream `DEL-10-02`, `PREREQUISITE`, `PENDING`, `HIGH`.

Default recommendation:

- Treat `DEP-10-03-006` as the likely true sequencing edge unless source evidence proves it is already satisfied or not applicable.
- Treat `DEP-10-02-004` as opposite-direction interface evidence that needs source-grounded reconciliation for strict FULL_GRAPH DAG closure.

## SCC-001 Initial Reading

The large runtime/SDK/session/tooling SCC remains strict-cyclic. CODEV-001 cleared the blocker-subset SCC, but strict FULL_GRAPH still includes interface and prerequisite cycles.

Next pass should classify current cyclic edges by existing schema fields only. Do not invent new dependency types.

