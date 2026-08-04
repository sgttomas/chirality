# S4 launch brief — COV-POST-001 exact candidate preparation

Role: `SCOPE_CHANGE` (Agent 1)
Node: `S4`
Plan: `ORCHESTRATION_PLAN_V7.md`
Owner ruling SHA-256:
`0349897a313f1a41973d3134be3dd1addffc4e9d20ed73bb60b337143de6022b`

## Objective

Prepare, validate, and present one exact metadata-only candidate correcting
only the three current-facing passages identified by COV-POST-001 in
`execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md` at current
SHA-256
`69bdb9ca682a80adab6c23e0a615bd4f9c5ed64f281f11a4e558a1f0e991278c`.

The corrected passages state that exact SCA-003 candidate acceptance and
application are completed acts, cite the exact owner-ruling and applied-hash
evidence identities, and refer confirmation status to the SCA-003
`Decision_Log.md`. They must remain true before and after later human Gate 1
confirmation and must not encode `pending` or `confirmed` as current-facing
decomposition prose.

## Allowed writes

- a new candidate/evidence subdirectory under
  `execution/_ScopeChange/SCA-003_2026-08-02_2212/`;
- S4 terminal return/status under this instance directory;
- append-only candidate-preparation entries in SCA-003 `Decision_Log.md` and
  `Handoff_State.md` only if needed to identify the exact gate; these entries
  must not claim application, confirmation, or closure.

## Required outputs

1. exact candidate copy of the live decomposition;
2. exact unified diff against the live source;
3. deterministic structured validation proving only the three authorized
   passages changed and all protected hashes/semantic inventories remain
   unchanged;
4. candidate presentation with candidate SHA-256, diff SHA-256, source/evidence
   hashes, exact owner application-token grammar, and no-effect boundary;
5. terminal `RETURN.md` and `STATUS.json`.

## Hard stops

Do not write the live decomposition, PRD, `_ScopeChange/_LATEST.md`, companion
registers, DEL packet surfaces, runtime/client/project surfaces, lifecycle,
release, reliance, Task Management, or Git. Do not regenerate the DEL packet,
dispatch N0, route App work, confirm Gate 1, or close SCA-003. Stop and return
if any frozen input differs or if exact containment cannot be proved.
