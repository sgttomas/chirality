# D-APP-103 — Per-attempt subagent decision-replay packet authorization

Status: `RULED — B4`

DecisionID: `D-APP-103`

Date: `2026-08-17`

Owner: `Ryan Tufts`

Owning loop: `Chirality App Dev`

## Exact owner ruling

```
**B4 — Per-attempt subagent decision-replay packet authorized, DEL-08-04 (D-APP-53 §3 Option C).**

Prepare the decision packet for the per-attempt subagent decision-replay artifact as one bounded planning node: what a per-attempt record captures (brief hash, scope, decision points, outcome, attribution) beyond the accepted canonical hierarchy replay; where it lives relative to `AgentRuns` and the daemon-owned canonical session; how Desktop and CLI would render it; the checks that would prove it; and the exact deliverable-local scope of implementation. Present at most three options with a recommendation. This authorizes the packet only; implementation follows a later ruling on it. DEL-08-04's Remaining item is updated to "packet authorized; awaiting ruling."
```

## Recording-tranche sequencing direction

```
**Sequencing:** the recording tranche is one iteration on its own — one branch, one commit, one receipt, one PR under the usual token, no merge. Do not begin B1–B4 or C1 engineering in the recording tranche. From the next iteration, B1, B2, B3, B4, and the C1 items are all selectable; the standing direction governs selection.
```

## Effect

DEL-08-04 is packet-authorized and awaits a later ruling after packet
preparation. No B4 packet or implementation work occurs in this recording
tranche.
