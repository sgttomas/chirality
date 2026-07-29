# Handoff — GOV-STEP4-APPLICATION-20260729

Status: `READY_FOR_HUMAN_GATED_PR`

## State

- `ClosureVerdict`: `APPLICATION_AUTHORED_AWAITING_PR_GATE`
- `DecompositionTruthState`: revision 1.2 applied on this branch per the
  owner acceptance and bracket ruling; becomes published truth at the
  human-gated merge
- `AuthoritativeEffect`: transcribes and applies already-returned owner
  acts (acceptance, bracket ruling, merge direction); rules nothing new
  (K-AUTH-1)
- `GlobalBlocker`: none for the PR gate itself

## Dependencies and gates

1. **Publication merge authorization.** This tranche's PR is human-gated;
   merge authorization is a separate owner act on the exact final branch
   HEAD (`self_merge: false` in the tranche manifest). The owner has
   directed that merges may be executed on the owner's behalf when the
   owner says so; the owner is reworking the PR-approvals basis
   separately, and this run pre-claims nothing about it.
2. **Step-4 state at this handoff.** POLICY_DELTA §4 row 1 (SOW-042
   restatement) is applied here; rows 2–9 were merged as PR #418. The
   audit-pair obligation is dispositioned (deterministic application
   validation + register baseline stand in; full AUDIT_DECOMP deferred to
   the next regular audit cycle).
3. **Follow-on (small, recorded):** `execution/_ScopeChange/_LATEST.md`
   still shows the pre-acceptance pointer state; refresh is outside this
   run's sealed write scope and is recorded in the SCA-002 Handoff_State
   application append for the next SCOPE_CHANGE-owned act.

## What later phases consume

- Receipt 63 in `execution/_Coordination/LOOP_RECEIPTS.md` covers this
  tranche: SCA-002 acceptance and application, and the PR #417/#418
  merges per the owner's direction.
- Applied decomposition identities (SHA-256):
  working surface
  `6f43f3fbc25e0663697464a7a20f3b1bac4b731b01efbe473642e238b93a4d49`;
  scope ledger
  `fea77787c2e20217bf168f7f773c4c86d1dbb5e2984d1712723afea95173c1dc`;
  deliverable register
  `b18ebe6b9bc3cdac6bd0bd78f6470be328a81783c7c6ab5b55478b506c61e8da`.
- SCA-002 applied-state evidence: `Applied_File_Hashes.json`,
  `validate_gate5_applied.py`, `Gate_5_Validation.json` (33/33 PASS),
  Decision_Log/Handoff_State application appends.

## Post-commit record

- Tranche commit: recorded by the supervising session at fan-in (single
  commit on `gov/step4-sca-application`; committed-HEAD whitespace
  validation run with
  `--base-ref 204321467b567ede862636a36dd67bcac1ff326a`; G4 diff mode run
  `--base 204321467b567ede862636a36dd67bcac1ff326a --head HEAD`).
