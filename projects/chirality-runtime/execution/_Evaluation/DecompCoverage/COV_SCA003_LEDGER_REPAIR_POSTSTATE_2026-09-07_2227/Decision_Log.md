# Decision log

| Decision | Disposition | Basis |
| --- | --- | --- |
| Variant binding | SOFTWARE | Sealed brief and authoritative companion-register layout. |
| Scope | `PKG-02_Runtime_Product` | Exact brief scope; repository topology equals scoped topology. |
| Canonical repair | PASS | Live ledger equals the approved v6 postimage; the one-row patch changes only `DecisionRef` and `Notes`. |
| First audit blocker | RESOLVED | Current ledger treats the 2026-09-07 blocker as history and explicitly records resolution of its metadata inconsistency. |
| `CandidateState` meaning | HISTORICAL | Current `Notes` explicitly identifies `GATE3_REVIEW_NOT_ACCEPTED` as preserved migration/decomposition candidate-stratum metadata, not current SCA-002/SCA-003 approval state. |
| Contract basis | CONSERVED | `HOST-P1`, `POLICY-R1`, and `ACCOUNT-WIRE-V1` are accepted contract choices; later implementation and evidence gates remain unmet. |
| Gate 5 | PENDING | This audit is evidence only. Separate owner confirmation is required by `AGENT_SCOPE_CHANGE.md` lines 590–597. |
| Human override | None | The sealed brief limited writes to this snapshot and its audit pointer. |
