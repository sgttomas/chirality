# Work graph amendment v3 — successor repair, freeze, and verification

Selection authority: `HELP_HUMAN replan v2` under unchanged D-APP-94 Option A
preparation-only authority.

Posture: `MIXED`, fully serialized. All predecessor nodes remain preserved and
terminal/interrupted. This amendment appends the following nodes:

| Node | Role | Dependency | Write ownership | Required return | Gate |
|---|---|---|---|---|---|
| `A3-SUCCESSOR-REPAIR-02` | fresh bounded ephemeral Agent 2 author/remediator | pinned blocked handoff and draft snapshot | exact repairs under `prepared/**`; `returns/A2_DAPP93_ATTEMPT3_SUCCESSOR_REPAIR_RETURN.md` | complete candidate plus evidence-rich `SUCCESSOR_REPAIR_COMPLETE` return | manager recomputes all hashes/counts/coverage and accepts or rejects fan-in |
| `A3-SUCCESSOR-FREEZE-02` | successor WORKING_ITEMS manager | accepted repair return | successor manager records under run root only | immutable candidate-byte freeze and static validation | all candidate objects indexed; complete token/ledger/runbook/evidence fan-in; no placeholder, scope, or containment defect |
| `A3-SUCCESSOR-VERIFY-02` | genuinely fresh bounded ephemeral Agent 2 verifier | accepted immutable successor freeze | `reviews/A2_DAPP93_ATTEMPT3_SUCCESSOR_FRESH_VERIFIER_RETURN.md` only | `PASS_DAPP93_ATTEMPT3_PACKET` or concrete bounded `BLOCK_DAPP93_ATTEMPT3_PACKET` | PASS permits owner-gated manager closeout; BLOCK may permit only bounded repair/re-freeze/reverify within preparation authority |
| `A3-SUCCESSOR-CLOSE-02` | successor WORKING_ITEMS manager | verifier PASS | distinct successor manager return and handoff under run root | exact hashes, verdict, reruns, derivative posture, next-owner action | stop before execution or token approval |

Edges:
`A3-REMEDIATE-01 (INTERRUPTED) -> A3-SUCCESSOR-REPAIR-02 -> A3-SUCCESSOR-FREEZE-02 -> A3-SUCCESSOR-VERIFY-02 -> A3-SUCCESSOR-CLOSE-02`.

No nodes are concurrency-eligible. Each Agent 2 has one sealed objective and
may not delegate. The verifier is read-only except for its distinct return and
must not repair candidate bytes. Any verifier BLOCK must cite concrete packet
defects. A bounded remediation/reverification cycle is lawful only for defects
repairable inside this run root without crossing the exclusions in
`SUCCESSOR_ACTIVATION.md`; otherwise the manager stops blocked and escalates.
