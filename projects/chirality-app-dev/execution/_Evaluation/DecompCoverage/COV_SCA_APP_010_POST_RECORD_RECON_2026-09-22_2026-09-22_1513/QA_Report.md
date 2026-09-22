# QA Report

- Input freeze verified at publication: decomposition SHA-256 `9261ce30f933a0b72364a5af09c8aeed9208372774959864ff24a805126ea8a6`; companion register SHA-256 `918e475a48899d18755139027e61db200d23a531e48ed9f969c526dd842fa944`; active ScopeChange pointer SHA-256 `f3a25a9baadefb69b3b30494774e4e9d0971b3f756ae4d7a55ff7b254fe8fffb`.
- Parser: 10 package rows, 52 deliverable rows, 84 ledger rows, 10 objective rows.
- Inventory: 11 physical package folders and 54 physical deliverable folders, including one control package and two control deliverables.
- Forward package/deliverable coverage: 10/10 and 52/52. Reverse-only rows are explicit in matrix and issue log.
- Context screen: 51 MATCH, 1 PARTIAL, 0 MISSING for declared units. Retired DEL-09-07 is deliberately kept as PARTIAL because its scaffold context conflicts with the current retirement record.
- ScopeOfWork validator: 54/54 pass, 0 fail.
- Scope Ledger deliverable reverse view: 0 mismatches/dangling references. Objective support: 10/10 objectives have ledger support.
- Active SCA-APP-010 root artifact set: 11/11; manifest entries verified: 59/59. Historical SCA-APP-008 incompleteness is called out separately.
- Snapshot outputs are deterministic tables plus narrative; `MANIFEST.sha256` covers snapshot output files and `INPUT_MANIFEST.sha256` records evaluated inputs.

## Limits

This is not semantic product verification. Artifact presence is a filename-token screen, and absence of a matching filename is not proof the behavior does not exist. No code, SoW, dependency, lifecycle or source truth was edited. Owner acceptance and release readiness remain outside this audit.
