# Work graph amendment v2 — author remediation

Reason: `A3-AUTHOR-01` was interrupted after missing its manager completion
checkpoint with partial unindexed bytes and no terminal return.

Replace the unaccepted author result with this serialized node:

| Node | Role | Dependency | Write ownership | Return | Gate |
|---|---|---|---|---|---|
| A3-REMEDIATE-01 | fresh ephemeral Agent 2 integration/remediation author | interrupted draft plus v2 brief | `prepared/**` and `returns/A2_DAPP93_ATTEMPT3_PACKET_REMEDIATION_AUTHOR_RETURN.md` only | coherent finished candidate and evidence-rich terminal return | manager freeze/hash/static validation |

Revised edges:
`A3-AUTHOR-01 (INTERRUPTED) -> A3-REMEDIATE-01 -> A3-FREEZE-01 -> A3-VERIFY-01 -> A3-CLOSE-01`.

No authority, scope, exclusion, or later-verifier write surface changes.
