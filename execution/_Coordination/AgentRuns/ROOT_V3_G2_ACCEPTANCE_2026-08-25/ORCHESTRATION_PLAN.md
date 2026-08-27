# Orchestration Plan — Root v3 G2 Acceptance — 2026-08-25

- **Version:** 1 (frozen before transcription)
- **Selection authority:** HUMAN — R15-A and its owner-carried steer
- **Basis:** `origin/main@baa29d22fa034784cda221b2929061213e83ec91`
- **Posture:** one bounded, sequential mechanical transcription node
- **Supervisor:** HELP_HUMAN (Agent 0)
- **Delegation:** none; the owner directed a single transcription act

## Work graph

| Node | Objective | Dependencies | Write ownership | Expected return | Fan-in gate |
| --- | --- | --- | --- | --- | --- |
| N1 | Materialize R15 and its steer, preserve the accepted packet, record acceptance evidence, and append Receipt 130 | All basis and subject-pin gates PASS | Two `plans/steers/` files; this run folder; Receipt 130 append | Actual identities, packet-preservation proof, negative-grant preservation, validator results, PR handoff | No candidate mutation; pure receipt append; exact R15 owner-act transcription; zero validation failures |

No semantic decision remains inside the tranche. The merge of the resulting PR
is a separate owner act. Any basis drift, packet mutation, negative-grant loss,
or validator failure stops the run without widening the write set.
