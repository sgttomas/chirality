# App runtime and basis evaluation

## Verdict

`DECISION_READY_WITH_ACTIVE_RELIANCE_HOLDS`

The evidence supports the already-selected Root-owner/App-and-PEC-client
boundary. It does not support immediate contract repinning or hold clearance.
OD-6 should proceed only after the App boundary SCOPE_CHANGE establishes the
corrected accepted basis.

The evaluation records 17 findings: two BLOCK findings attached to named
reliance claims, ten REVIEW findings, two WARN findings, and three INFO
findings. Neither BLOCK classifies the App or Piping product as a whole.

## Decision spine

1. **Keep APP-HOLD-1 active.** The exact six held contracts still declare an
   unresolvable basis. The tool, register, instructions, and 12/12 tests agree.
2. **Do not repin yet.** Forty-five other decomposition-derived contracts pin
   valid historical bytes, not current bytes. The two PKG-00 controls are a
   different source class and should not join a decomposition repin.
3. **Choose a current-byte acceptance method after App SCOPE_CHANGE.** Either
   prospectively bind the corrected current population or adopt a
   non-rewriting provenance register. Neither route may invent the six
   contracts' missing historical provenance.
4. **Create or explicitly defer the invariant register before REVIEW.** The
   requirement is open but no present deliverable has entered REVIEW.
5. **Repair SOW-064 traceability.** The relevant PRD behavior is substantially
   present, but both mapped contracts omit the accepted scope identity.
6. **Disposition D-APP-48/49 as a separate evidence tranche.** D-APP-48 has an
   internal source-commit conflict and stale downstream Piping metadata.
   D-APP-49 migrated byte-identically to Root but lacks a current-location
   executable audit.
7. **Route version/degraded behavior to Root/Tier-0.** Same-build App coherence
   is strong; cross-release PEC compatibility has no handshake. Bounded
   fail-closed behavior exists, but the general contract remains incomplete.

## Runtime topology found

App packages the Root daemon and, in its normal GUI/API/CLI postures, acts as
its client. The daemon-host posture owns credentials, sessions, engines,
delegation, auth, and runtime state. Ten App workflow routes use the daemon
client and have no in-process runtime fallback.

PEC is the only other production-code client found. Its current use is limited
to scratch/demo agent routes and lacks a governed live daemon run. Piping is
not a runtime client.

## Evidence limits

- No App/PEC runtime was started by this evaluation.
- Historical governed runtime drills were inspected but not rerun.
- Current D-APP-49 tests could not run because dependencies were absent.
- No client-side cross-version negotiation evidence exists.
- No repin target, new version value, or hold exception is proposed.

The complete decision alternatives are in `OWNER_ALTERNATIVES.md`; individual
claim status and rerun triggers are in `FINDINGS.csv`.
