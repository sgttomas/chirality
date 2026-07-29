# Run Manifest — GOV-STEP2-ROOT-20260728

Status: `CANDIDATE AUTHORED — OWNER RULING GATE REQUIRED`
Parent: HELP_HUMAN (Agent 0, loop-readiness transition program session)
Lane: HELPS_HUMANS (Agent 1)
Executor: bounded Agent 2 AUTHOR (this run; no delegation)
Accepted Git basis:
`85ea0628fa4e57dd6aae53b06139b2b8734a9612`
Branch: `gov/step2-root-disclosure`

## Objective

Author the D-GOV-30 program disclosure-and-ratification instrument as a
complete, immutable-before-ruling candidate: packet, decision record
(AWAITING_RULING), register row, G4 tranche manifest, and this bounded
run record. No ruling is contained; every ruling slot holds the fenced
placeholder `<<RULING PLACEHOLDER — OWNER RETURN VERBATIM: D-GOV-30>>`.

## Exact write scope

This run writes exactly, and only:

- add
  `docs/governance_harness/_PROPOSALS/D-GOV-30_2026-07-28_program_disclosure_ratification/PACKET.md`
  (CandidateSubjectSHA256
  `32b4afbfb402d65fecc14558bca79f5b83fc5690bd0b4f56cc9a656ced6c35e3`);
- add
  `docs/governance_harness/_DECISIONS/D-GOV-30_program_disclosure_and_ratification.md`;
- append one `D-GOV-30` row to
  `docs/governance_harness/_DECISIONS/_REGISTER.md` (append-only;
  preimage SHA-256
  `4bc26afed30dfb665df4d137722640f1e16d551c60be809863af8e74b08ec147`);
- add
  `docs/governance_harness/tranche_manifests/ROOT-GOV30-DISCLOSURE-20260728.yaml`;
- add
  `execution/_Coordination/AgentRuns/GOV-STEP2-ROOT-20260728/RUN_MANIFEST.md`;
- add
  `execution/_Coordination/AgentRuns/GOV-STEP2-ROOT-20260728/VALIDATION.md`;
  and
- add
  `execution/_Coordination/AgentRuns/GOV-STEP2-ROOT-20260728/HANDOFF_STATE.md`.

## Pinned surfaces this run must not touch

Verified byte-identical at the accepted basis before and after authoring:

- `docs/PRD_ROOT.md` — SHA-256
  `0e36a03abc16b86f99024aa2a17c467ae7f4303f9740be3a6ba2e9dd1dfb2f2d`
  (D-8 remains as written; no amendment).
- `execution/_Coordination/CHIRALITY_PROGRAM_ARCH_REMEDIATION_CLOSEOUT_2026-07-28.md`
  — SHA-256
  `27c3e36cf11c94521a87eabb0f0dfd9563e42915aa8af9c87681f7f8776caaac`
  (the owner-direction transcription cited by reference).
- `execution/_Coordination/LOOP_RECEIPTS.md` — preimage SHA-256
  `f10a022732262ba9e98d252e0f13fb110142630a42c7f8607dffc640779fd518`
  (Receipt 59 is the cursor; Receipt 60 is drafted in the packet and is
  appended only in the post-session completion commit, not by this run).
- `docs/CONTRACT.md` — SHA-256
  `1a448a822084d8dad1daf53884d6835caadabfe5cb5c89a9cfbaf896656cedec`
  (K-MERGE-1 cited, not amended).
- `execution/_Coordination/ROOT_TRACE_MAINTENANCE_EFFECTIVE_STATE_CLOSEOUT_2026-07-28.md`
  — SHA-256
  `05d68b1f66c80fcc42f1a36eb3f71a0e5a6a45dfb37cf81c79fa1eab2450e645`
  (R-1 subject).
- `execution/_Coordination/PROGRAM_ARCH_REMEDIATION_RECORD_CURRENCY_2026-07-28.md`
  — SHA-256
  `6a3504ca944772befb96c71cecead629943f46e1fd918d8c7ae46dcbc5ae9fe9`
  (R-2 subject).
- `docs/governance_harness/_PROPOSALS/OD7-G1_program_record_closeouts_2026-07-27/ARTIFACT_HASHES.sha256`
  — SHA-256
  `d6421ce6076238fd49dc0469d1160f8dc7698b2e730d8833e57136baaa957aa0`
  (R-4 manifest 1; frozen).
- `docs/governance_harness/_PROPOSALS/OD7-G1_ROOT_MANIFEST_G4_CORRECTION_2026-07-27/ARTIFACT_HASHES.sha256`
  — SHA-256
  `574f82592171dad9d4597fdf1591a2b7adf1f857af23cd246f087ef32dc6a35b`
  (R-4 manifest 2; frozen).

## Prohibitions

- No owner ruling authored, summarized, or anticipated; placeholders only.
- No retroactive-cure claim anywhere in the candidate.
- No edit to any pre-existing file except the single append-only
  `_REGISTER.md` row.
- No LOOP_RECEIPTS.md append, no notice routing, no self-merge, no Git
  closeout beyond the single candidate commit on
  `gov/step2-root-disclosure`.
- No claim that the frozen evidence packages exist at this basis; they
  land via the separate evidence PR (branch `gov/step1-evidence-landing`,
  commit `02b1f091a`) and are cited content-addressed.

## Engine identity

Provider: Anthropic
Engine: Claude Code (Agent SDK)
Model: claude-fable-5
