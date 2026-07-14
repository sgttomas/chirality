# VERIFY-DEL-08-05 Portability Record

Verifier-generated method evidence uses repository-relative paths. Four machine-specific or placeholder literals already present in immutable accepted source/control bytes are inventoried in `PRESERVED_LITERALS.tsv`; source-derived occurrences remain byte-exact and are not normalized or endorsed.

The TASK run record contains normalized absolute execution paths required by `AGENT_TASK.md`. Those fields are execution metadata, not candidate authority. No generated method metadata introduces a temporary-root path or `file://` URI. The deterministic render is script-free and contains no external resource reference.
