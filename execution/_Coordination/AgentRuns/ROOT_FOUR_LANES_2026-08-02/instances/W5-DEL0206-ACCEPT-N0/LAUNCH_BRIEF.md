# W5 launch brief — accept, copy, and run fresh N0

Role: `WORKING_ITEMS` (Agent 1)
Node: `W5`
Plan: `ORCHESTRATION_PLAN_V11.md`
Owner acceptance ruling SHA-256:
`7ddbef0480700483cb07efe771b64e3f413b489288a02bde987a6a85b9ba70f7`

## Objective

Verify exact current candidate manifest
`360f8f12c4719d79a506394bcd98a4b630c2610f9c80d90a08b0519e8a1d508f`
and the exact owner token. Create an external RunID-local acceptance record,
validate it with the existing acceptance validator, copy the six candidate
files byte-identically to the accepted Scope-of-Work path
`accepted_inputs/`, validate exact live-copy parity, and dispatch fresh N0
through a real bounded child session using the existing N0 rerun brief and
checklist. Validate the child return and stop at the N0 gate.

## Exact inputs

- acceptance ruling SHA-256:
  `7ddbef0480700483cb07efe771b64e3f413b489288a02bde987a6a85b9ba70f7`;
- candidate presentation SHA-256:
  `2ecd01dcfe95ca9417592875624dff1990cc4ddf6622a2d1126e24e97a2d4a42`;
- W4 return SHA-256:
  `25cd4cd934d0141612c15719db1aa562ba4615657ca5eb2a4787fcfe61aeeac0`;
- N0 rerun brief SHA-256:
  `d9519594a6fe1a9eb115725bef4d16ac73e1d459853b7c98577da4061e99be36`;
- N0 rerun checklist SHA-256:
  `fb326c03008c3bbfc58efa9a98d4cf22e58c60b80d36bcdc8462624ebff14af7`;
- accepted Scope of Work SHA-256:
  `dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146`;
- PRD `d4f97d75…5cc4`, decomposition `23f6ae0f…64f3d`, fresh audit
  `ee10313f…420e1`, and SCA Gate 1 record `05395c30…f40f` as frozen in W4.

## Required outputs

1. `packet_acceptance/` record with the one exact owner token and evidence
   identities, validated against the current candidate;
2. `accepted_inputs/` containing exactly the same six regular files and bytes
   as `packet_candidate/`;
3. a fresh N0 child launch/return/status with explicit basis, source,
   lifecycle, profile, dependency, path-containment, packet, and currentness
   findings required by the N0 brief/checklist;
4. WORKING_ITEMS validation and W5 `RETURN.md`/`STATUS.json` stating the exact
   N0 verdict, blockers, released/held edges, and protected-surface checks.

## Hard stops

Stop after N0 regardless of its verdict. Do not dispatch or release N1–N6.
Do not write runtime/client/project implementation, SCA/decomposition/PRD,
lifecycle/release/reliance, Task Management, Git, or foreign-loop surfaces.
If any exact precondition differs, stop before acceptance/copy/N0 and report
the mismatch.
