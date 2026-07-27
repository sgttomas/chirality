# Sealed Brief — D-APP-49 Admission Recheck 02

- **Dispatch ID:** `A2-DAPP49-ADMISSION-RECHECK-02-20260727`
- **Parent:** `/root/od6_dapp48_49_apply`
- **Role:** read-only Agent 2 admission validator
- **Current accepted commit:** `4214915d9fcfecdc2952626421bf50b0e5f7845b`
- **Current accepted tree:** `078262ed304d1e11acc882b7c76210e599a74258`
- **Audit commit:** `fb16e32ed60bb4f384cf1e07a83c4a14ff63bbae`
- **Audit tree:** `65f1ca55329a091ca9759a483ec40c41e27fdd23`
- **Selected Revision 3 packet SHA-256:** `c6d7b3bd8041eb19e38e7b09f8c9cdb2325bbc02368afbadd73de28195b31f54`
- **Frozen audit return SHA-256:** `18e0ca3f98b05f793e5b21e65ba28eb6ae90ecadd1865a7212d2fd21707cc47a`

## Objective

Independently validate the pre-terminal D-APP-49 current-location audit
admission package and companion D-APP-76 candidate for identity, basis,
schema, evidence boundary, F1/E1 authority containment, and readiness for
manager fan-in.

## Read scope

Read only:

- this complete evaluation package as it exists at dispatch;
- the companion D-APP-76 candidate and App decision register;
- the Piping factual notice;
- repository objects and files at the current and audit bases;
- the session-staged Revision 3 packet at
  `/private/tmp/OD6_DAPP48_49_GATE_CANDIDATE_REV3_2026-07-27_684979863/`;
- governing App, Root, Tier-0, and SCA-APP-005 anchors cited by the package.

## Tools and permissions

Use read-only Git, hashing, CSV, text, and deterministic validation commands.
Do not modify repository or package files. Do not use network access. Do not
delegate.

## Required checks

1. Reproduce the current and audit commit/tree identities and ancestry.
2. Reproduce the frozen audit return and Revision 3 packet hashes and verify
   the packet's internal hash list.
3. Verify the companion D-APP-76 candidate identity and confirm it remains
   outside the accepted Git basis.
4. Verify the ten-column `FINDINGS.csv` schema and all report sections.
5. Confirm that static identities are separated from return-attested
   behavioral outcomes.
6. Confirm that F1 closes only OD6-011's basis-scoped evidence gap after
   durable integration.
7. Confirm that E1 creates only a preparation route and no activation,
   identity, version, commit, implementation, repin, retirement, release, or
   lifecycle authority.
8. Reproduce the D-APP-48/D-30 pin mismatch facts and the scope of the Piping
   notice.
9. Check candidate whitespace for the pre-terminal package, D-APP-76,
   register, and notice.
10. Report any missing or stale identity without editing it.

## Fan-in convention

This recheck validates a pre-terminal population. Its own terminal return and
run record do not yet exist, and the manager will regenerate
`ARTIFACT_HASHES.sha256` after preserving them. Do not block solely because
those future artifacts are absent or because the pre-terminal hash list must
be regenerated after fan-in. Do block on any substantive identity, schema,
authority, evidence-boundary, path, or whitespace failure in the population
that exists at dispatch.

## Required return

Return:

- dispatch ID and brief SHA-256;
- engine/provider/model if exposed, otherwise explicit `UNKNOWN`;
- PASS or BLOCK verdict;
- reproduced identities;
- static-versus-behavioral evidence disposition;
- F1/E1 authority verdict;
- whitespace verdict;
- exact blockers and corrections, if any;
- repository-write and delegation attestations.

The return must not propose or perform product repair, repinning, facade
retirement, successor activation, implementation, release, or lifecycle
transition.
