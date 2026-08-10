# Work graph v1 — D-APP-93 attempt-3 packet preparation

Selection authority: HELP_HUMAN sealed activation for
`APPDEV_DAPP93_ATTEMPT3_PACKET_PREPARATION_2026-08-09`.

Posture: `MIXED`, fully serialized because the verifier consumes an immutable
manager freeze of the author's write set.

| Node | Role | Dependency | Reads | Write ownership | Required return | Gate |
|---|---|---|---|---|---|---|
| A3-AUTHOR-01 | ephemeral Agent 2 author | activation and accepted live basis | ruled D-APP-93/D-APP-94 sources, R8 evidence, R4.4.6 lineage, static repo bytes | `prepared/**`, `returns/A2_DAPP93_ATTEMPT3_PACKET_AUTHOR_RETURN.md` only | complete new exact candidate packet plus evidence-rich author return | manager content/schema/containment review |
| A3-FREEZE-01 | WORKING_ITEMS manager | accepted author return | entire run root and accepted sources | manager records outside child-owned paths | versioned freeze, validation, frozen hashes, verifier brief | all candidate objects exist, hash, parse, preserve exclusions and predecessor bytes |
| A3-VERIFY-01 | genuinely fresh ephemeral Agent 2 verifier | accepted immutable manager freeze | read-only repo and frozen run root | `reviews/A2_DAPP93_ATTEMPT3_FRESH_VERIFIER_RETURN.md` only | `PASS_DAPP93_ATTEMPT3_PACKET` or bounded `BLOCK_DAPP93_ATTEMPT3_PACKET` | PASS permits manager closeout; BLOCK permits only fresh bounded remediation under this activation |
| A3-CLOSE-01 | WORKING_ITEMS manager | verifier PASS | run root and validation evidence | manager return/handoff under run root | validated package-preparation return and owner-gated handoff | stop before execution-token approval or any packet command |

Edges: `A3-AUTHOR-01 -> A3-FREEZE-01 -> A3-VERIFY-01 -> A3-CLOSE-01`.
No nodes are concurrency-eligible. Agent 2 nodes may not delegate.

Escalate immediately if a required packet repair would alter predecessor bytes,
require a decision/ruling/deliverable/product/Task-Management/foreign-loop
write, execute a packet command, perform C1118, approve a token, or cross any
activation exclusion.
