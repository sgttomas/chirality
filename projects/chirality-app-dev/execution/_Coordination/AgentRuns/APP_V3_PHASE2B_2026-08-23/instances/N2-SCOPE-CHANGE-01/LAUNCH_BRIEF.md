# N2-SCOPE-CHANGE-01 — Sealed Launch Brief

**Parent:** HELP_HUMAN / APP v3 Phase 2b
**Role:** SCOPE_CHANGE (Agent 1)
**Basis:** exact `HEAD` and `origin/main` at
`ef92fab10f40aa95da484701982d83fa1abca874`
**Consumed N1 candidate:**
`cf889103744df7fe4f20b85e9c8d4610a85af287cbfe60f0f6471a7bd642e3b8`
**Objective:** Re-pin the Phase-2 K-EVENT-4 transaction candidate to the
ratified Root contract under A6-B without changing the resolved row bytes.

## Declared context

- `agents/AGENT_SCOPE_CHANGE.md`
- Phase-2b steer and ruling records A6, A4, and A5
- frozen Phase-2 K-EVENT-4 transaction artifact and Phase-2 handoff
- ratified and immediately prior Root `docs/CONTRACT.md` blobs
- the four unchanged A4-A Root source blobs
- N1 regenerated K-CONTROL-1 candidate at the consumed identity above

## Write scope

- `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/Phase2b/K_EVENT_4_REPINNED_CONTRACT_ROW_CANDIDATE.md`
- this instance's `LAUNCH_BRIEF.md`, `RETURN.md`, and `STATUS.json`

No N1/shared run file, existing SCA snapshot file, N3/N4 artifact, live target,
receipt, pointer, register, SOW, status, dependency, decomposition, docs,
frontend, Root-loop, or other-project surface may be written.

## Output contract

Produce one full K-EVENT-4 transaction artifact that changes only the Root
grounding from the pre-ratification Root contract identity to the ratified
identity. Preserve the exact live App pre-image, the exact LF-terminated
resolved row, its Phase-2 resolved full-contract relationship, and all four
other Root source pins. Prove the Root contract differs only at line 162 and
that the cited K-RUNTIME-1 line 161 and K-STORE-2 line 164 bytes are unchanged.

## Acceptance checks

1. N1 is consumed only at the declared `cf889103…` artifact identity.
2. Prior and ratified Root contracts differ only at line 162.
3. Root K-RUNTIME-1 line 161 and K-STORE-2 line 164 are byte-identical.
4. The other four A4-A Root blobs remain at their exact pins.
5. The resolved K-EVENT-4 LF-terminated row remains exactly
   `92c9d359f70a934fad07b399e18b93df07dc9573f0bf04ab4dd4d40d18eebf93`.
6. Candidate whitespace runs against
   `ef92fab10f40aa95da484701982d83fa1abca874` before `RETURN.md` or
   `STATUS.json` pins the new artifact identity.

Stop without output if preserving the resolved row requires a byte change.
No N3 full-contract recomputation, commit, push, merge, application,
acceptance, or authority claim.
