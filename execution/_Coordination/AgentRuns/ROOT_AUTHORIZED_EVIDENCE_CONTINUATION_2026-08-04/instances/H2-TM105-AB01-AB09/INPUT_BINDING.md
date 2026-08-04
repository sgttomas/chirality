# H2 input binding and source-drift report

InstanceID: `H2-TM105-AB01-AB09`

Posture: `DERIVATIVE EVIDENCE ONLY — NO AUTHORITY EFFECT`

## Checkout identity

- Resolved `REPO_ROOT` and `WORKING_ROOT`:
  `/Users/ryan/.codex/worktrees/1342/chirality`
- Local branch/HEAD at acquisition start:
  `codex/root-owner-rulings-2026-08-03@26f505e4d5a90ec10a87e6fbe982231de19b80c7`
- Accepted current main named by the orchestration plan:
  `origin/main@cdc76a1d398231267f1379e7143b4de27abaa01b`
- `git diff --stat HEAD origin/main` returned no output. The evidence-bearing
  working tree content is therefore byte-equal between those two tree states;
  this statement is tree equality, not merge or publication authority.

## Governing and acquisition inputs

| SHA-256 | Repo-relative path | Use and limit |
|---|---|---|
| `268becd0bac9da8421b30089e4e4167a5e5f79bf3892d0f72ad41a63180a3aeb` | `AGENTS.md` | Runtime hierarchy and governed-child/write/handoff rules. |
| `47a30075b4286a7352d78aae9d033d8eead8ef125e4063d0cc7c1235b3e9101a` | `agents/AGENT_HELPS_HUMANS.md` | Agent-1 evidence/fan-in contract. |
| `6271cac33a7cd97d9d13143e17951ac63544763a0f1fd832cebdd2ca1d64d4e6` | `docs/CONTRACT.md` | K-GHOST/K-PROV/K-INVENT/K-CONFLICT/K-CLAIM/K-WRITE constraints. |
| `5de31f552bea356629ad29af9bc664f33d49392d1c63fc2fb4dc70614abd7df9` | `docs/WORKFLOW_COMPONENT_STANDARD.md` | Artifact classes, delegation, human authority, and handoff rules. |
| `6396dd26c3fb8b6ed922c1cb7da584f67a08188d5b27525d650bf3ca1560c566` | `execution/_Coordination/AgentRuns/ROOT_SEMANTIC_RETURNS_2026-08-03/OWNER_RETURN_TRANSCRIPT_2026-08-03.txt` | Standing TM105-A preparation-only evidence lane; no new authority and no byte gate while an implementation-critical TBD survives. |
| `03245133a99b8844950e9cc33c6c2b08ce20ae525ba7dbcad2223630b5c2e3a7` | `execution/_Coordination/AgentRuns/ROOT_TM105_EVIDENCE_COLLECTION_2026-08-03/HANDOFF_STATE.md` | Accepted Phase-1 derivative handoff. |
| `2364215ced4e1ad0227d67f7233778160294efe6837872a4e1a701083afc7bc4` | `execution/_Coordination/AgentRuns/ROOT_TM105_EVIDENCE_COLLECTION_2026-08-03/ACQUISITION_BRIEFS.md` | Exact AB-01 and AB-09 output contracts. |
| `2c6e59d2edce6ac6699cf8ae1faa6ac3e7cce8b64664772c299480c55c45ec6a` | `execution/_Coordination/AgentRuns/ROOT_TM105_EVIDENCE_COLLECTION_2026-08-03/EVIDENCE_MANIFEST.tsv` | Phase-1 38-entry primary evidence binding. |
| `b2d4add54787e174fa5fa0b1d11d32be60c6d2123587bcb80f0f3cd5c8a8183c` | `execution/_Coordination/AgentRuns/ROOT_TM105_EVIDENCE_COLLECTION_2026-08-03/TBD_EVIDENCE_MATRIX.tsv` | Phase-1 TBD status and acquisition dependency map. |
| `fc0dc536f01c39345e6ee195e789fb07ce28f7fd593f9e83dccdcae3ec7c78aa` | `execution/_Coordination/AgentRuns/ROOT_TM105_EVIDENCE_COLLECTION_2026-08-03/OWNER_VENDOR_PLATFORM_FACTS.md` | Non-inferable fact inventory; not a decision form. |
| `3fc56807c4cd83fd2b5f967848b770adfd226541880629493ddfe8ad3df989aa` | `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_run_records/DEL-02-06-SEMANTIC-BYTE-ACCEPTANCE-003/ACCEPTED_SEMANTIC_SNAPSHOT.md` | Exact scope and authority boundary of accepted DEL-02-06 V2 bytes. |
| `e1f841d808e73642e28a6dec0b19adfdcf0e0c4800b6541701a9d8e7ee6a2874` | `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_run_records/DEL-02-06-SEMANTIC-BYTE-ACCEPTANCE-003/ACCEPTED_SEMANTIC_MEMBERS.sha256` | Six-member accepted-byte verification manifest. |

## Drift and accepted-member verification

The manager recomputed every current file in the 38-entry Phase-1
`EVIDENCE_MANIFEST.tsv`: `38/38 MATCH`, `0 DRIFT`, `0 MISSING`.

The accepted DEL member verifier returned `OK` for all six members. The exact
sorted V2 package-manifest file remains
`6005a00695a96eb46e59896f01653d3504ef85b35a7d28509bba8d33171425e2`.
No accepted member was regenerated or edited.

## Disjoint Agent-2 evidence sets

- AB-01 reads only the ten source paths and hashes enumerated in
  `children/AB-01/LAUNCH_BRIEF.md`; these cover current authorization, tool
  bridge, event/conformance, interruption, tests, and Piping-local needs.
- AB-09 reads only the eighteen source paths and hashes enumerated in
  `children/AB-09/LAUNCH_BRIEF.md`; these cover the exact accepted DEL bytes,
  current session/event/client/runtime identity and persistence surfaces,
  tests, and App-local direction.
- The two child evidence sets have no overlapping path. Both children are
  non-delegating and write only their own `RETURN.md` and `STATUS.json`.

The parent manager, not either child, owns authority interpretation and final
fan-in. Hash match is evidence of byte identity only; it is not semantic,
implementation, lifecycle, release, reliance, publication, or Git approval.
