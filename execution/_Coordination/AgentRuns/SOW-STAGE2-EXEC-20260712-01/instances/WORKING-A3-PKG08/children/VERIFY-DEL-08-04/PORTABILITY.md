# VERIFY-DEL-08-04 Portability Record

All verifier-generated method evidence uses repository-relative paths. Three machine-specific literals are retained only because they are immutable accepted source/control content or marker-bound derivatives; every occurrence is inventoried in `PRESERVED_LITERALS.tsv` and remains byte-exact.

The TASK run record necessarily contains normalized absolute execution paths required by `AGENT_TASK.md`. Those fields are execution metadata, not candidate authority. No generated metadata introduces a temporary-root path or `file://` URI. The deterministic render is script-free and contains no external resource reference.
