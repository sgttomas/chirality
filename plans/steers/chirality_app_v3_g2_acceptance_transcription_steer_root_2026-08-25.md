# ROOT v3 STEER — R15 App Server 0.149.0 G2 acceptance transcription — 2026-08-25

## OWNER ACT — TRANSCRIBE VERBATIM

R15-A — [click] “Accept at G2 with documented gaps and G5 finding.”

I accept as the G2 supply unit the exact App Server 0.149.0 candidate published
by PR #673 at main merge commit
`baa29d22fa034784cda221b2929061213e83ec91`, tree
`bd5fdf75a4c03df9f920a396489a0348cb03431c`, with the following expressly
in view:

1. generated JSON schema is `UNAVAILABLE_UNDER_BOUNDS`;
2. generated TypeScript types are `UNAVAILABLE_UNDER_BOUNDS`;
3. the exhaustive schema-derived stable/experimental method inventory is
   `UNAVAILABLE_UNDER_BOUNDS`;
4. the `version` invocation’s committed per-run gate-hash record is absent and
   its preflight records are empty, so that evidence is
   `VERSION_RUN_GATE_EVIDENCE_UNAVAILABLE_UNDER_BOUNDS`;
5. the invalid published vendor signature remains the named R13-B G5 finding.

This acceptance applies only to the three exact recorded release assets and
their recorded equivalent App Server payload identities.

This acceptance does not amend a pin; dispose the G5 finding; approve the
invalid signature for preparation or release; authorize implementation,
cutover, activation, release, publication, redistribution, reliance, or App
adoption; complete OUT-002 policy; lift TM-ROOT-106 or TM-ROOT-122; or lift
any of the ten existing DEL-02-06 held bindings. Every later act remains
separately governed.

## END OWNER ACT

## BASIS GATE

1. Fetch current remote state without rebasing or rewriting history.
2. Require `origin/main` to equal
   `baa29d22fa034784cda221b2929061213e83ec91`.
3. Require that merge commit to have parents:
   - `5cb493a09bf336593d2ed7412cfdabdcbc4e09a1`
   - `b46f41a858938f41e99f3e2abb487238b78ed875`
4. Require its tree to equal
   `bd5fdf75a4c03df9f920a396489a0348cb03431c`.
5. Confirm PR #673 is merged, its remote head branch is absent, and the
   post-merge main governance harness passed.
6. If any basis check fails, stop and report without writing.

## SUBJECT PINS — RECOMPUTE FROM ACTUAL BYTES

Candidate packet:
`execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-08_Exact_Supply_and_Protocol_Pinning/_run_records/APP-SERVER-0.149.0-G2-CANDIDATE-2026-08-24/`

Require:

- `G2_ACCEPTANCE_SHEET.md`
  SHA-256 `cec83abc2fc39358037600c883dd7b55ad09b154140d68a4d86346c309cda5ae`
- `README.md`
  SHA-256 `ff4ed9502b2b4ac843107cf14a9f5ff35983f6e9f70469f80610b960582bd897`
- `EVIDENCE_HASH_MANIFEST.csv`
  SHA-256 `acbc96a61b35f6f5812ece08895586967ac571c5367753035d7def7d46a1ddfb`
- `04_REVIEW/REVIEW.md`
  SHA-256 `b3bb1f1d2e496c6ed484943033c87fdc9737379cc6c37aac1c571d286e897de9`
- `execution/_Coordination/AgentRuns/ROOT_SUPPLY_PINNING_2026-08-24/HANDOFF_STATE.md`
  SHA-256 `f470116910ae7432d0f0b634d206bca4edeb08699dbc9ec0b622bb413e6f6fd4`
- pre-transcription `execution/_Coordination/LOOP_RECEIPTS.md`
  SHA-256 `47a0c384578bff69629ca6cbbd94eabcd5625bc645d0f7c44e67706150e2c4b2`

Read and verify the cumulative supply instruments:

- `plans/steers/chirality_app_v3_supply_pinning_steer_root_2026-08-24.md`
  SHA-256 `1384b216889d4357b332fa3507f573d887b11aa009f49ba9b29797b23d312391`
- `plans/steers/chirality_app_v3_root_ruling_record_r12_2026-08-24.md`
  SHA-256 `2ee282fc1330c466e17ce2791cb7cb8c66f2a7e13f455c2ab1750c42719321fd`
- `plans/steers/chirality_app_v3_supply_resume_steer_root_2026-08-24.md`
  SHA-256 `248317951603551eafd54754e79fc04b1d8082906653136ff7042dfd5132c701`
- `plans/steers/chirality_app_v3_root_ruling_record_r13_2026-08-24.md`
  SHA-256 `0ba74959dac38f49f81f6ba8aff4020df520fd418bed2a3aa6617b19f3aa4960`
- `plans/steers/chirality_app_v3_supply_resume2_steer_root_2026-08-24.md`
  SHA-256 `38b76ca27defd39507f6d9cfe9501d392b1e9ade7c5f107cd67cb4ce420ef164`
- `plans/steers/chirality_app_v3_root_ruling_record_r14_2026-08-24.md`
  SHA-256 `2633637bd68c7f4cb54457a3547b2bcab8933f19e021abf558b1ef2463d1b5e9`

Never copy a digest from memory in the resulting records; recompute every
identity from actual bytes.

## EXECUTION

1. Create a fresh branch
   `codex/root-g2-acceptance-2026-08-25` from the exact required main.
2. Materialize the owner act as:
   `plans/steers/chirality_app_v3_root_ruling_record_r15_2026-08-25.md`.
3. Materialize this full owner-carried steer as:
   `plans/steers/chirality_app_v3_g2_acceptance_transcription_steer_root_2026-08-25.md`.
4. Create bounded run evidence under:
   `execution/_Coordination/AgentRuns/ROOT_V3_G2_ACCEPTANCE_2026-08-25/`.
   Record the basis, subject pins, negative grants, validation, and final state
   `G2_ACCEPTED_WITH_DOCUMENTED_GAPS_AND_G5_FINDING`.
5. Append Receipt 130 to
   `execution/_Coordination/LOOP_RECEIPTS.md`.
   Transcribe the OWNER ACT block verbatim, record the actual R15 and steer
   SHA-256 values, the accepted packet identities, every documented gap, the
   G5 finding, and every retained negative grant.
6. Do not alter any byte in the accepted candidate packet. Acceptance is a new
   immutable record referring to that exact packet; it does not rewrite its
   pre-acceptance state.
7. Do not alter deliverable contracts, pins, Task Management registers, held
   bindings, App-loop surfaces, implementation files, workplans, or any other
   lifecycle state.

## VALIDATION

- Prove the candidate packet is byte-identical before and after transcription.
- Recompute and verify every cited SHA-256.
- Verify Receipt 130 is a pure append to the pinned receipt pre-image.
- Run `git diff --check` and the applicable Root G0–G4/governance validators.
- Push an ordinary commit, open an unlabeled PR targeting `main`, and confirm
  hosted governance CI.
- Do not merge the PR.

## STOP CONDITIONS

Stop and report without expanding scope if main moved, a pinned identity
differs, the packet would need mutation, a negative grant cannot be preserved,
a validator fails, or any action beyond mechanical G2 acceptance transcription
appears necessary.

## RETURN

Return the branch, commit, PR, exact changed-path list, recomputed identities,
validation results, hosted-CI state, and confirmation that the candidate packet,
G5 finding, blockers, holds, and all negative grants remain unchanged. The PR
merge is a separate owner act.
