# Independent-refutation disposition

## Session history

- The first E3 session was interrupted before producing artifacts after the
  manager noticed two input hashes had changed. Its dispatch binding was
  corrected; the session was later bounded and interrupted again when it did
  not return within the manager's closeout window. No finding was attributed to
  that incomplete attempt.
- A fresh no-history Agent 2 recovery session verified all rebound hashes and
  produced E3 `REFUTATION.md`/`RETURN.md`. It returned `BLOCK` with two blockers
  and three review findings.
- After bounded repair, the same independent refuter received a new E4 sealed
  brief and exact hashes. E4 returned `PASS WITH NON-BLOCKING WARN`, closing all
  five E3 findings.

## Finding disposition

| E3 finding | Disposition | Repair |
|---|---|---|
| BLOCK-01 alternate grace vs fixed 2,500 ms | CLOSED by E4 | Machine and prose consequences now derive total as selected grace + 500 ms; G1/G2/G3 totals are 1,500/2,500/4,500 ms. |
| BLOCK-02 undefined failure recovery | CLOSED by E4 | `STOPPED_DEGRADED` and `STOP_FAILED_CLEANUP` now have distinct reuse/retry semantics and mapped tests. |
| REVIEW-03 uncalibrated 500 ms | CLOSED by E4 | Packet, clauses, risks, and both templates expressly make 500 ms a human product-policy cap, not empirical Node evidence. |
| REVIEW-04 start-during-start unmapped | CLOSED by E4 | Restart/lifecycle test row now covers concurrent start. |
| REVIEW-05 pre-identity terminal rule | CLOSED by E4 | Latch is generation-owned, expires at force with identity-unavailable failure, forbids late interrupt, and has never/yields-after-force cases. |
| E4 WARN structured concurrent-start parity | FIXED AFTER E4 | Added exact `"startDuringStart":"REJECT"` field to `SEMANTIC_OPTIONS.json`; this is the sole post-backcheck semantic-file change and exactly implements E4's non-blocking repair instruction. Deterministic validation confirms parity. |

## Final verdict

`PASS FOR ACCOUNTABLE-HUMAN DECISION / IMPLEMENTATION HELD`.

E4 found no remaining blocking contradiction, implementability failure, scope
expansion, premature hold release, or evidence overclaim. The final structured
parity repair does not alter the backchecked prose obligation or recommendation.

