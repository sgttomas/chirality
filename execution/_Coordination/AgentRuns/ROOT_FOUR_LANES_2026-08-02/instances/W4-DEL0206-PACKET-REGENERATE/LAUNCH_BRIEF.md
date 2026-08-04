# W4 launch brief — regenerate and present DEL-02-06 packet

Role: `WORKING_ITEMS` (Agent 1)
Node: `W4`
Plan: `ORCHESTRATION_PLAN_V10.md`

## Objective

Under owner continuation ruling SHA-256
`9b98fe3dc6f8d9abb53c5b087e666cd17d53569ea0f39f1dea489534c9ebf6b6`,
regenerate the exact six-file candidate in the existing
`DEL-02-06-RUNTIME-SPEC-001` packet instrument against the current corrected
and Gate-1-confirmed basis. Revalidate the full candidate and isolated
negative cases, update the packet presentation and DEL run handoff/manager
return truthfully, and return the new manifest identity plus one exact owner
acceptance token.

## Required current basis

- accepted Scope of Work SHA-256:
  `dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146`;
- PRD SHA-256:
  `d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4`;
- live decomposition SHA-256:
  `23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d`;
- fresh audit return SHA-256:
  `ee10313f42c99bc9432d3999b148d81ef0d959c58fa8e58d6df3dc40470420e1`;
- Gate 1 owner-confirmation SHA-256:
  `05395c308e81d31362dbc87d6d61b7073a3dbffc0b2b3172aba596e7e551f40f`;
- SCA Decision Log SHA-256:
  `d64272d9c25b3ee21d622a7dc16a5cc20dea0979252e0b899f189ff95a51f508`;
- SCA Handoff State SHA-256:
  `625f5e93c8e657785910e31bfc9e179d4aa83896e5e5f9fe1dca98119a9f23f6`.

The old candidate manifest `dd007522…53cf` is a stale derivative bound to
the prior decomposition hash. Preserve its history in the presentation/run
records; do not describe it as accepted or as current.

## Required outputs

1. regenerated six-file `packet_candidate/` with a new exact manifest;
2. deterministic content/full validation and all required isolated negative
   cases;
3. updated `packet_presentation/PRESENTATION_RECORD.md`, DEL activation/work
   graph/handoff records as needed for current truth, and W1/W4 terminal
   returns/status;
4. exact owner token grammar binding the new manifest and the owner/date;
5. proof that no acceptance record, `accepted_inputs/`, N0 dispatch, runtime,
   client/project, lifecycle/release/reliance, Task Management, Git, or
   foreign-loop write occurred.

## Hard stops

Do not accept the packet, embed an acceptance token in candidate bytes,
reconstruct missing historical bytes, create/write `accepted_inputs/`, or
dispatch N0. Do not modify SCA/decomposition/PRD, runtime/client/project,
lifecycle/release/reliance, Task Management, Git, or foreign-loop surfaces.
If any required basis identity differs, stop without regenerating.
