# Work graph v1 — D-APP-93 attempt-3 packet v2

Status: `FROZEN FOR DISPATCH`

Selection authority: HELP_HUMAN activation brief. Posture: `MIXED`.

## Nodes and ownership

| Node | Agent 2 | Depends on | Write ownership | Return/gate |
|---|---|---|---|---|
| A | ephemeral generalist ledger author | activation | `candidate/COMMAND_AUTHORITY_LEDGER.md`, `returns/A2_LEDGER_AUTHOR_RETURN.md` only | Exact ledger plus self-check; no index/token |
| B | ephemeral generalist supporting-packet author | activation | runbook, reconstruction manifest, evidence-return, ingestion/causal contract, LLDB copy/revalidation, overlay/config objects, and `returns/A2_SUPPORTING_AUTHOR_RETURN.md` only | Complete disjoint supporting packet; no ledger/index/token |
| C | ephemeral generalist integration author | accepted A+B | `candidate/PACKET_INDEX.md`, `candidate/FUTURE_OWNER_COMMAND_APPROVAL_REQUEST.md`, `returns/A2_INTEGRATION_AUTHOR_RETURN.md` only | Cross-object integration; may identify but not silently repair A/B defects |
| D | WORKING_ITEMS manager | accepted C | freeze/static-validation/telemetry/handoff records outside candidate | Exact freeze and static validation |
| E | genuinely fresh ephemeral generalist verifier | accepted D | `reviews/A2_FRESH_VERIFIER_RETURN.md` only | Read-only complete packet PASS or concrete BLOCK |
| F | bounded remediation/fresh verifier | concrete within-authority verifier BLOCK only | explicitly amended targets | At most bounded repair/refreeze/new fresh verifier |

## Edges and concurrency

- A and B are dependency-ready and write-disjoint; dispatch concurrently.
- C is held until A and B returns are accepted.
- D follows C. E follows the complete D freeze.
- F exists only for concrete, bounded, within-authority BLOCK findings.
- Any author that cannot return an exact blocker or complete output after one checkpoint is interrupted. No endless author chain.

## Fan-in gates

1. A+B: exact allowed writes only; new v2 identity; no claim of lost-ledger continuity.
2. C: complete index and prospective token bind all v2 objects and the full new command range.
3. D: returned destination remains absent; fixed-root consistency; no old command IDs or old/lost authority; hashes and static parses reproduce.
4. E: genuinely fresh, read-only, independent review of 100% of the frozen packet.
5. Owner gate: verifier PASS does not approve execution. Fresh contact evidence and an exact later owner return remain future gates.

## Escalation

Escalate any authority conflict, occupied namespace, operational-action need, irreparable cross-object contradiction, or verifier BLOCK not repairable within the candidate-only write boundary. Do not broaden scope.
