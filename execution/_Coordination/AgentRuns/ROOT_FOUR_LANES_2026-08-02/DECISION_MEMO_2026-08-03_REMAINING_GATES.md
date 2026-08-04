# HELP_HUMAN decision memo — remaining Root four-lane gates

Date: `2026-08-03`
Role: `HELP_HUMAN`
Effect: `DECISION SUPPORT ONLY`

## Currentness check

Remote references were refreshed on 2026-08-03. `origin/main` is
`7249281e1f84ba5abee3c31c2fea3736b22000d3`, three commits after the frozen
evaluation basis. The only path added after that basis is
`execution/_Coordination/ASSESSMENT_2026-08-02_LOOP_PATTERN_CONVERGENCE.md`.

No remote change touches the S2 or Pi candidate dependencies:

- `origin/main:docs/PRD_ROOT.md` remains SHA-256
  `278f31ae99607f970e39c6535f809c93a7c5bf09b139ffa2cbbdbe3f08c3746c`;
- `origin/main:execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md`
  remains SHA-256
  `6f43f3fbc25e0663697464a7a20f3b1bac4b731b01efbe473642e238b93a4d49`;
- the frozen-basis-to-current-main diff over `runtime/` and
  `projects/chirality-app-dev/frontend/` is empty.

The existing S2 17/17 validation and H2 identity proposal therefore remain
current. This check does not integrate `origin/main` into the dirty proposal
worktree and creates no Git effect.

## Recommendation 1 — SCA-003

Recommend issuing both exact S1 rulings in sequence:

1. `ACCEPT SCA-003 BASIS RECONCILIATION c3ce8db0`; then
2. `APPLY SCA-003 BASIS RECONCILIATION c3ce8db0`.

Reason: the paired candidate corrects independently verified current-facing
status contradictions; preserves all stable commitments, §5.3.1, 89
decomposition identifiers, companion registers, SCA-002 evidence, and prior
candidate history; and passes 17/17 deterministic checks. No current upstream
drift changes either target. Application remains bounded by the exact M2
tranche-manifest, registered-loop notice, export-disposition, SCOPE_CHANGE
ordering, and post-application AUDIT_DECOMP obligations stated in the S1
return.

This recommendation is not acceptance or application.

## Recommendation 2 — Pi PIA-U10 G1

Recommend `SELECT_G1_B_FOR_VALIDATION_ONLY`.

Reason: G1-B names the implementation family that is actually executable in
the frozen/current App composition (`PiAgentEngineAdapter`) while making its
App ownership explicit under Root's generic collision-proof identity schema.
It is the cleanest validation target because it separates the Pi `0.82.0`
evidence question from an unperformed architecture migration:

- G1-A would first require App composition migration to make the Root wrapper
  the executed family;
- G1-C has no materialized implementation bytes and would first require the
  broadest SCOPE_CHANGE and implementation tranche; and
- G1-D preserves the hold but cannot advance identity-dependent package/live
  proof.

Selecting G1-B for validation does not accept it as the final architecture.
It does not approve Pi `0.82.0`, supersede D-APP-72/SCA-APP-002 Pi `0.80.10`,
authorize App work, or preclude a later G1-A/G1-C architecture decision after
evidence fan-in. It merely ensures that the next evidence campaign identifies
the implementation family that produced the evidence instead of attributing
App-host behavior to an unexecuted Root wrapper.

## Consequences of the recommended rulings

After SCA acceptance/application, HELP_HUMAN routes the exact M2/SCOPE_CHANGE
application, validates the paired REF-001 pin, reruns AUDIT_DECOMP, and returns
the original SCA-003 zero-action Gate-1 confirmation. W2 then instantiates the
post-S2 six-file packet candidate and presents its manifest for a separate
exact owner acceptance before copying live inputs or dispatching N0-R2.

After G1-B selection, the next Root act is to bind an exact App-host
implementation identity proposal and prepare, but not foreign-write or
dispatch, the App work-acceptance handoff. App remains the owner of its proof
and successor instruments. Pi version approval remains at later G4 after
immutable evidence and independent EVALUATION fan-in.
