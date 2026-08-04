# E4 refutation backcheck — TM-ROOT-112

Status: `COMPLETE / PASS WITH NON-BLOCKING WARN`

## Binding

All eight SHA-256 values in `DISPATCH_INPUT.md` matched exactly: the six revised
manager drafts and the two E3 artifacts. No drift was found.

## E3 finding closure

### E3 BLOCK-01 — `CLOSED`

The prior unconditional 2,500 ms consequence is gone.
`SEMANTIC_OPTIONS.json:38-40` now derives connection termination as selected
grace plus 500 ms. `OWNER_SEMANTIC_DECISION_PACKET.md:135-137` and
`CANDIDATE_NORMATIVE_CLAUSES.md:73-78` enumerate the resulting 1,500/2,500/4,500
ms bounds. The alternate return requires selection-specific clause regeneration
and accepts the 500 ms policy value without fixing the G2 total
(`OWNER_RETURN_TEMPLATES.md:45-52`). G1 and G3 can no longer authorize a
contradictory 2,500 ms total.

### E3 BLOCK-02 — `CLOSED`

N-STOP-6 now separates failure classes and supplies deterministic recovery
semantics (`CANDIDATE_NORMATIVE_CLAUSES.md:99-120`):

- clean transport/metadata plus interruption failure becomes
  `STOPPED_DEGRADED`, rejects stop, blocks instance reuse, and requires
  process/runtime-service replacement;
- incomplete transport/metadata cleanup becomes `STOP_FAILED_CLEANUP`; repeated
  `stop()` is the named cleanup-only retry and transitions to `STOPPED` or
  `STOPPED_DEGRADED` according to remaining interruption state.

The scope map now requires observations for both degraded interruption failure
and injected cleanup failure/retry (`IMPLEMENTATION_TEST_SCOPE_MAP.md:16-18`).
This removes the prior ambiguity about whether cleanup success could silently
clear an interruption failure.

### E3 REVIEW-03 — `CLOSED`

The 500 ms cap is expressly labeled a proposed human product-policy value, not
an empirical Node guarantee, with its tradeoff and rejection consequence in the
packet, clauses, and risks (`OWNER_SEMANTIC_DECISION_PACKET.md:28-30,135-137`;
`CANDIDATE_NORMATIVE_CLAUSES.md:73-78`; `RISKS_AND_CAVEATS.md:31-36`). Both owner
return paths expressly accept that calibration
(`OWNER_RETURN_TEMPLATES.md:19-22,45-52`).

### E3 REVIEW-04 — `CLOSED`

The Restart row now requires a second start during the first start to reject and
leave one listener/owner (`IMPLEMENTATION_TEST_SCOPE_MAP.md:18`). This maps the
N-STOP-6 concurrent-start obligation within the already-approved daemon source
and bounded daemon-test surfaces.

### E3 REVIEW-05 — `CLOSED`

N-STOP-3 now makes the pre-identity latch closing-generation-owned, expires it
at force with `INTERRUPTION_IDENTITY_UNAVAILABLE`, forbids late interrupt, and
observes later iterator settlement without mutating a restart
(`CANDIDATE_NORMATIVE_CLAUSES.md:30-42`). The scope map requires never-yields and
yields-after-force coverage, including no duplicate interrupt or unhandled
rejection (`IMPLEMENTATION_TEST_SCOPE_MAP.md:16`). Risks and both recommended
authorization language and structured options preserve the same terminal rule.

## Final attempted refutations

### Cross-document semantics — `PASS WITH WARN`

The recommended G2+C1+F1 packet is internally coherent, and alternate grace
totals are now derived. One non-blocking structured-document omission remains:
`SEMANTIC_OPTIONS.json.fixedConsequences` contains `startDuringStop: REJECT` but
does not contain the packet's fixed concurrent-start rejection, even though the
packet, N-STOP-6, recommended return, and test map all require it. This does not
make the recommended signed return ambiguous because that return spells out
concurrent-start rejection and accepts N-STOP-1 through N-STOP-7. For complete
machine-readable parity—especially before using the alternate return—add
`"startDuringStart":"REJECT"` to `fixedConsequences` and refresh affected
hashes.

### Implementability — `PASS`

The selected semantics can be represented inside `runtime-daemon.ts` with a
lifecycle state/shared promises, per-generation socket/SSE registries and
cancellation latches, force timers, and generation-guarded cleanup. The bounded
daemon tests can inject service/transport outcomes for the required states. The
packet correctly requires a scope-change return if canonical interruption
cannot be achieved inside that boundary.

### Scope and holds — `PASS`

The recommended signed return authorizes only the previously approved contract
surface, `runtime-daemon.ts`, and bounded `daemon.test.ts` cases. Implementation
remains held until a signed, hash-bound semantic return. No App, core,
process/SIGTERM, CLI, register, lifecycle, or Git expansion is authorized. The
Root-to-App notice remains held until semantic acceptance and an accepted repair
landing; the parity rerun remains App-owned.

### Evidence calibration — `PASS`

The packet continues to distinguish bound Node v24 executable behavior from the
Node >=22.19 support-floor gap, policy timing from empirical guarantees, Root's
reproduced mechanism from App R2 causality, and transport settlement from
canonical terminal persistence. No new empirical claim is introduced by the
repairs.

## Verdict

The two E3 blockers and all three E3 review findings are closed. No blocking
contradiction, scope expansion, hold release, or evidence overclaim remains.
The packet is suitable for accountable-human decision. The JSON parity warning
should be corrected before an alternate-option return is used, but it does not
block the fully explicit recommended return.
