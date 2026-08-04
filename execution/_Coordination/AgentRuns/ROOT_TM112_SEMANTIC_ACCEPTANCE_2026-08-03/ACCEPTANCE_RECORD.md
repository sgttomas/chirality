# TM-ROOT-112 semantic acceptance record

Status: `ACCEPTED BY ACCOUNTABLE HUMAN / IMPLEMENTATION AUTHORIZED BUT NOT STARTED`
DecisionID: `ROOT-TM112-SEMANTICS-01`
Selection: `G2 + C1 + F1`
Accountable human: Ryan Tufts
Decision date: 2026-08-03

## Authority identity

The ruling of record is the exact signed block at transcript lines 11–35 and
bytes `[593,2436)` in:

`execution/_Coordination/AgentRuns/ROOT_SEMANTIC_RETURNS_2026-08-03/OWNER_RETURN_TRANSCRIPT_2026-08-03.txt`

- Transcript SHA-256:
  `6396dd26c3fb8b6ed922c1cb7da584f67a08188d5b27525d650bf3ca1560c566`.
- Exact signed-block SHA-256 (1843 bytes, excluding the following blank-line
  separator):
  `a18f963d4666af73dd44674ea2d43f5052dc7eb96ddfe977f7a84070927f3a53`.

The signed return accepts N-STOP-1 through N-STOP-7 as the authoritative
semantic basis and authorizes the previously bounded contract/source/test
implementation tranche. The other transcript returns and additions are outside
this carrier's application scope.

## Clause-byte binding across whitespace repair

Accepted clause path:

`execution/_Coordination/AgentRuns/ROOT_TM112_STOP_CONTRACT_2026-08-03/CANDIDATE_NORMATIVE_CLAUSES.md`

| State | Commit | SHA-256 | Bytes |
|---|---|---|---:|
| Pre-whitespace candidate presented to owner | `ba4678ca00c0cf9fb862ba36d1410d11ce1ff6ac` | `2428824746c5a6928c2894619d67bbc817717bed536f5ee64b11cdafda0db62e` | 7796 |
| Post-whitespace branch candidate | `2b6d53027ea10374dd515a4a5a203f8ed4cf2f04` | `fd3ba31a8c53719e165b131d872868a53760adab4dc7ae92015fbd6641a11ead` | 7792 |

The clause-file byte delta is exactly four bytes: two trailing two-space
Markdown hard-break markers were removed from the `Status` and `Candidate set`
lines. The file's words, tokens, punctuation, ordering, and terminal newline are
unchanged. Normalizing Markdown hard breaks makes the two clause blobs byte-
identical. The broader repair commit also removes redundant EOF whitespace in
other candidate/run files; this is the same Markdown-hard-break/EOF whitespace
normalization class and introduces no semantic packet regeneration.

Therefore the signed semantic acceptance binds the post-whitespace clause blob
without changing the selected N-STOP semantics. `AUTHORITY_BINDING.json`
records the machine-checkable identity and equivalence proof.

## Accepted semantic identity

1. `G2`: exactly 2,000 ms graceful interval from first `STOPPING` transition.
2. `C1`: stop admission, then immediately request canonical, idempotent,
   generation-owned SSE interruption. A pre-identity Agent 1 latch exists only
   until force; at force it expires with identity-unavailable failure and may
   not cause a late interrupt.
3. `F1`: at grace expiry, call `server.closeAllConnections()` after
   `server.close()`, then destroy all tracked residual server sockets.
4. Allow at most 500 additional ms for Node close/tracked-socket settlement.
   This is an accepted product-policy cap, not an empirical Node guarantee; the
   selected connection-governed bound is 2,500 ms before filesystem cleanup.
5. Response or interruption acknowledgement does not extend waiting after
   force. Owned socket and owner cleanup are attempted before settlement.
6. Concurrent stop coalesces; stopped stop is a no-op; concurrent start and
   start during stop reject; successful stop supports same-instance restart;
   prior-generation events cannot mutate the new listener/owner generation.
7. Clean-metadata interruption failure is `STOPPED_DEGRADED` and blocks
   instance reuse. Incomplete cleanup is `STOP_FAILED_CLEANUP`; repeated stop
   retries only incomplete cleanup.

## Authority boundary

This acceptance authorizes the sealed implementation/test brief in this
carrier. It does not itself edit the canonical contract, source, or tests; prove
implementation; change lifecycle; update registers/receipts; authorize Git; or
route the App notice. The App notice remains conditional on an accepted repair
landing. Root still has not proved that this mechanism caused App R2 or proved
any process/SIGTERM behavior.
