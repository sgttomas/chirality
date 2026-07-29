# Run Manifest — GOV-STEP3-D8-CANDIDATES-20260729

Status: `DUAL CANDIDATES AUTHORED — OWNER SELECTION GATE REQUIRED`
Parent: HELP_HUMAN (Agent 0, loop-readiness transition program session)
Lane: HELPS_HUMANS (Agent 1)
Executor: bounded Agent 2 AUTHOR (this run; no delegation)
Accepted Git basis:
`4f7808acb2802443370d045efa198152934c1674`
Branch: `gov/step3-d8-candidates`

## Objective

Author the two D-8 successor-policy candidates (Step 3 of the approved
program plan) as complete, separately hashed, candidate-only packages
under
`docs/governance_harness/_PROPOSALS/D-GOV-31_2026-07-29_merge_gate_policy_succession/`:
Candidate A (ROOT-ONLY scope) and Candidate B (SHARED-CHANGE-POLICY
scope), each a full `PRD_ROOT_REV7_CANDIDATE.md` derived byte-exactly
from the live `docs/PRD_ROOT.md` at the basis plus a `POLICY_DELTA.md`
and a hash manifest; plus the framing `PACKET.md`, a package-level hash
manifest, the G4 tranche manifest, and this bounded run record. No
selection, no adoption, no PRD edit, no register row, no decision
record: candidates only.

## Exact write scope

This run writes exactly, and only (all adds; no existing file modified):

- `docs/governance_harness/_PROPOSALS/D-GOV-31_2026-07-29_merge_gate_policy_succession/PACKET.md`
- `docs/governance_harness/_PROPOSALS/D-GOV-31_2026-07-29_merge_gate_policy_succession/ARTIFACT_HASHES.sha256`
  (package-level; written last)
- `docs/governance_harness/_PROPOSALS/D-GOV-31_2026-07-29_merge_gate_policy_succession/CANDIDATE_A_ROOT_ONLY/PRD_ROOT_REV7_CANDIDATE.md`
- `docs/governance_harness/_PROPOSALS/D-GOV-31_2026-07-29_merge_gate_policy_succession/CANDIDATE_A_ROOT_ONLY/POLICY_DELTA.md`
- `docs/governance_harness/_PROPOSALS/D-GOV-31_2026-07-29_merge_gate_policy_succession/CANDIDATE_A_ROOT_ONLY/ARTIFACT_HASHES.sha256`
- `docs/governance_harness/_PROPOSALS/D-GOV-31_2026-07-29_merge_gate_policy_succession/CANDIDATE_B_SHARED_CHANGE/PRD_ROOT_REV7_CANDIDATE.md`
- `docs/governance_harness/_PROPOSALS/D-GOV-31_2026-07-29_merge_gate_policy_succession/CANDIDATE_B_SHARED_CHANGE/POLICY_DELTA.md`
- `docs/governance_harness/_PROPOSALS/D-GOV-31_2026-07-29_merge_gate_policy_succession/CANDIDATE_B_SHARED_CHANGE/ARTIFACT_HASHES.sha256`
- `docs/governance_harness/tranche_manifests/ROOT-GOV31-CANDIDATES-20260729.yaml`
- `execution/_Coordination/AgentRuns/GOV-STEP3-D8-CANDIDATES-20260729/RUN_MANIFEST.md`
- `execution/_Coordination/AgentRuns/GOV-STEP3-D8-CANDIDATES-20260729/VALIDATION.md`
- `execution/_Coordination/AgentRuns/GOV-STEP3-D8-CANDIDATES-20260729/HANDOFF_STATE.md`

## Pinned surfaces this run must not touch

Verified byte-identical at the accepted basis before and after authoring:

- `docs/PRD_ROOT.md` — SHA-256
  `0e36a03abc16b86f99024aa2a17c467ae7f4303f9740be3a6ba2e9dd1dfb2f2d`
  (the candidates' preimage; D-8 remains as written; no amendment).
- `docs/CONTRACT.md` — SHA-256
  `1a448a822084d8dad1daf53884d6835caadabfe5cb5c89a9cfbaf896656cedec`
  (K-MERGE-1 cited, not amended).
- `execution/_Coordination/LOOP_INIT.md` — SHA-256
  `a2c1e6f3077793ffa6ad78340ea74d9c655f703f68a33a787dbb9f923aa4f5ad`
  (§7 line 126 cited, not amended).
- `docs/governance_harness/_DECISIONS/_REGISTER.md` — SHA-256
  `d595d9979578b2d3e34e789fc93d1da15fd2a1cc68ada8264ab116e0ddaf6109`
  (no D-GOV-31 row; the row arrives with the record at adoption).
- `execution/_Coordination/LOOP_RECEIPTS.md` — SHA-256
  `694f3845d6d82cdb52b01f865978530be1355abee61200278ce95a8e7a307941`
  (no receipt appended by this run).
- `execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv` —
  SHA-256
  `0d48abe08aa336ac5e495650451f286b4b717606f047adff931c45dacc8531a4`
  (SOW-042 row cited as a propagation target only).
- `execution/PKG-04_Developmental_Machinery_and_Change_Control/1_Working/DEL-04-06_Change_Management_and_Human_Gated_Closeout/ScopeOfWork.md`
  — SHA-256
  `2f14f8c56d9a40e6024c212de9cf468e45930469f04198762b6df2c58b1385ce`
  (REQ-001 and no-self-merge occurrences cited as propagation targets
  only).
- `agents/AGENT_CHANGE.md` — SHA-256
  `1269db1275aa55bd0940ae2bd29a2299cc3e881ef571d8a5d4fb4713d0987243`
  (Candidate B propagation target only; untouched).

## Prohibitions

- No owner selection, ruling, or adoption authored, summarized, or
  anticipated anywhere in the package.
- No edit to any pre-existing file; this tranche is adds-only.
- No D-GOV-31 decision record and no `_REGISTER.md` row.
- No retroactive-cure or compliance claim about the 2026-07-28 window.
- No grant issued or exercised; no merge authorized; no self-merge; no
  Git closeout beyond the single candidate commit on
  `gov/step3-d8-candidates`.
- No LOOP_RECEIPTS.md append, no notice routing (M6 disposition is
  `pending` at Agent 0 fan-in).
- The two candidates must be independently complete and must differ only
  where scope requires; verified by diff in `VALIDATION.md`.

## Engine identity

Provider: Anthropic
Engine: Claude Code (Agent SDK)
Model: claude-fable-5
