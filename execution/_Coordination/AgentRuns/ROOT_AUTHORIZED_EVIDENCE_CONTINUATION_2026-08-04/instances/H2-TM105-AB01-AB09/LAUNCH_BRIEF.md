# H2 launch brief — TM105 AB-01 and AB-09 evidence acquisition

InstanceID: `H2-TM105-AB01-AB09`

Role: `HELPS_HUMANS` (Agent 1), managed by `HELP_HUMAN`

## Objective

Execute TM105 acquisition brief AB-01 (authorization/execution threat model)
and AB-09 (DEL-02-06 compatibility/lifecycle alignment) under the standing
preparation-only posture. Use actual governed Agent-2 children with sealed,
disjoint, read-only evidence briefs where specialist reasoning is required;
persist their briefs and returns below this instance directory and validate
their fan-in before returning.

## Required reads

- root `AGENTS.md`, `agents/AGENT_HELPS_HUMANS.md`, and applicable canonical
  Root contracts;
- signed TM105 owner return and the Phase-1 TM105 evidence census;
- exact AB-01 and AB-09 briefs in `ACQUISITION_BRIEFS.md`;
- accepted DEL-02-06 V2 semantic-byte snapshot in its exact scope;
- current client auth, tool descriptor/bridge, session/event/runtime, and
  affected-client evidence cited by the Phase-1 manifest.

## Write ownership

This instance directory only, including any governed Agent-2 subdirectories.
All evidence sources are read-only. Do not edit candidates, contracts,
registers, receipts, App/Piping/DEL surfaces, runtime/product source or tests,
current workplans, or other run directories.

## Required outputs and acceptance checks

AB-01 must return an asset/principal/trust-boundary inventory and a threat
matrix covering confused deputy, replay, stale grants, policy mismatch,
credential leakage, child widening, native-tool bypass, and evidence tamper.
It must distinguish required mechanical controls, unmitigated risks, and
falsification evidence, leaving unsupported assumptions `UNKNOWN`.

AB-09 must return a field-by-field identity/lifetime/rollover crosswalk,
compatibility and migration delta, old/new client behavior, interrupted and
partial-work treatment, digest/profile migration, affected-client census, and
conflict/non-coverage register with exact evidence hashes. It must not widen
DEL semantics into TM105.

The manager must hash-bind inputs/outputs, identify source drift, validate the
Agent-2 fan-in, run candidate whitespace and `git diff --check`, prove write
containment, and emit `RETURN.md`, `STATUS.json`, and `HANDOFF_STATE.md`.

No owner/vendor/platform fact may be inferred. Do not draft a no-TBD
successor, present a byte gate, select contract semantics, authorize a backend,
or make any implementation/lifecycle/release/reliance/Git act. Escalate every
consequential choice to HELP_HUMAN.
