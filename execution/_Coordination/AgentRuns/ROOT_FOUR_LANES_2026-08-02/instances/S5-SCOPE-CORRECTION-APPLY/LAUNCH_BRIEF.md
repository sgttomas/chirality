# S5 launch brief — apply and backcheck COV-POST-001 correction

Role: `SCOPE_CHANGE` (Agent 1)
Node: `S5`
Plan: `ORCHESTRATION_PLAN_V8.md`
Owner ruling SHA-256:
`8a9c005aa219d6e19f58e164721368ad72418019960182379edf52d5327a9851`

## Objective

Verify the frozen source/candidate/diff/ruling identities, apply exact accepted
candidate SHA-256
`23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d`
to `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md` only,
validate exact containment and protected hashes, then dispatch a fresh
read-only `AUDIT_DECOMP` backcheck of COV-POST-001 under SCOPE_CHANGE's allowed
manager workflow. Return the applied/backchecked state for human confirmation.

## Required evidence

1. pre/post live hash and byte parity with the exact accepted candidate;
2. exact accepted diff reproduction;
3. deterministic validation proving the same three authorized passages and
   preservation of PRD, `_LATEST.md`, companion registers, DEC-023,
   identifiers, row counts, scope/topology/mappings/counts, and substantive
   requirements;
4. fresh audit evidence under
   `execution/_ScopeChange/SCA-003_2026-08-02_2212/Evidence/AUDIT_DECOMP_COV_POST_001_BACKCHECK/`
   explicitly dispositioning COV-POST-001 and distinguishing audit evidence
   from human confirmation;
5. SCA-003 application summary, Decision Log/Handoff append, and S5
   `RETURN.md`/`STATUS.json`.

## Hard stops

Do not change `_ScopeChange/_LATEST.md`, any companion register, PRD, candidate
evidence, DEL packet/N0, runtime/client/project state, lifecycle,
release/reliance, Task Management, or Git. Do not confirm Gate 1 or close
SCA-003. If any frozen precondition differs, stop without applying.
