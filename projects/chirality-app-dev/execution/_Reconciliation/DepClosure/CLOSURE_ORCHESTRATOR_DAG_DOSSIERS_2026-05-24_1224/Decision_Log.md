# Decision Log

- Replaced mechanical retirement proposals with cycle dossiers and a human ruling workbook.
- Did not invent new dependency edge types.
- Used existing schema fields to separate hard blocker candidates from interface/co-development couplings.
- Defined blocker subset from existing app logic: active upstream `PREREQUISITE` / `CONSTRAINT` deliverable rows whose satisfaction is not `SATISFIED`, `WAIVED`, or `NOT_APPLICABLE`.
- Preserved strict FULL_GRAPH verdict separately: all active execution deliverable rows remain cyclic.
- Did not edit deliverable-local `Dependencies.csv` files.
