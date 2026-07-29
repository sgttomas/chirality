# Run Manifest — GOV-STEP4-APPLICATION-20260729

Status: `APPLICATION AUTHORED — HUMAN-GATED PR REQUIRED`
Parent: HELP_HUMAN (Agent 0, loop-readiness transition program session)
Lanes: SCOPE_CHANGE (SCA-002 application) + HELPS_HUMANS (receipt, run
records, manifest)
Executor: bounded Agent 2 AUTHOR (this run; no delegation)
Accepted Git basis:
`204321467b567ede862636a36dd67bcac1ff326a` (merge of PR #418; PRD Rev 7
§5.3.1 live; SCA-002 candidate package on main; operative surfaces
reconciled)
Branch: `gov/step4-sca-application`

## Objective

Transcribe the 2026-07-29 owner acts of record and perform what they
authorize, in one tranche: (1) apply the accepted SCA-002 amendment to the
three live decomposition surfaces from the exact Gate 3 candidate bytes,
plus the owner-ruled SOW-042 `SourceRef` bracket delta; (2) record
acceptance and application in the SCA-002 package (append-only/new files);
(3) append the Step-4 closeout Receipt 63, recording the acceptance, the
bracket ruling, the application, and the PR #417/#418 merges per the
owner's direction; (4) this run record and the tranche manifest.

## Owner acts of record (each verified byte-exact before transcription)

| Act | Bytes | SHA-256 |
|---|---|---|
| `ACCEPT SCA-002 271d456a — Ryan Tufts 2026-07-29` | 49 | `cfd81bc53f29c051b8d59b89b3566c36a459011c52d8deaa2eb39ddbe592208b` |
| `BRACKET AS RECOMMENDED: at application, update SOW-042 SourceRef to cite D-GOV-31 adoption — Ryan Tufts 2026-07-29` | 116 | `a34878f59dcd4365a5f95fd68b7da70a452c875cc398724148c4a189d8db035a` |
| `APPROVE HEADS dfc8d4af5 (PR #417) AND e5e8f760 (PR #418); MERGE #417 THEN #418 ON MY BEHALF — Ryan Tufts 2026-07-29` | 117 | `f7b0136d3b8daf11d312d4d6e0714f6e45c59d35e618ff03c3fd6d67e190834b` |

## Merge record (verified in git before transcription)

- PR #417 (`gov/step4-sca-decomposition`): approved HEAD
  `dfc8d4af532b07f8e562ace2f910ca777e63173f`, merged as
  `6e21530f7182ca2a7e7831b9528f85889a4a4467`.
- PR #418 (`gov/step4-operative-surfaces`): approved HEAD
  `e5e8f760548e739078a1735b176cd56604d5d4c9`, merged as
  `204321467b567ede862636a36dd67bcac1ff326a`.
- Each HEAD was the merge commit's second parent (verified unchanged);
  both merges were executed on the owner's behalf per the direction
  above, via the owner-authenticated `gh` CLI (GitHub merge actor
  `sgttomas`).

## Exact write scope

Modified:

- `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md`
  (exact accepted candidate bytes; applied SHA-256
  `6f43f3fbc25e0663697464a7a20f3b1bac4b731b01efbe473642e238b93a4d49`)
- `execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv`
  (accepted candidate bytes + the one owner-ruled bracket delta; applied
  SHA-256
  `fea77787c2e20217bf168f7f773c4c86d1dbb5e2984d1712723afea95173c1dc`;
  CRLF preserved)
- `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`
  (exact accepted candidate bytes; applied SHA-256
  `b18ebe6b9bc3cdac6bd0bd78f6470be328a81783c7c6ab5b55478b506c61e8da`)
- `execution/_ScopeChange/SCA-002_2026-07-29_0800/Decision_Log.md`
  (application append only; drafting record above the append unedited)
- `execution/_ScopeChange/SCA-002_2026-07-29_0800/Handoff_State.md`
  (application append only)
- `execution/_Coordination/LOOP_RECEIPTS.md` (Receipt 63 appended)

Added:

- `execution/_ScopeChange/SCA-002_2026-07-29_0800/validate_gate5_applied.py`
- `execution/_ScopeChange/SCA-002_2026-07-29_0800/Gate_5_Validation.json`
  (33/33 PASS over the LIVE files)
- `execution/_ScopeChange/SCA-002_2026-07-29_0800/Applied_File_Hashes.json`
- `docs/governance_harness/tranche_manifests/ROOT-SCA002-APPLICATION-20260729.yaml`
- `execution/_Coordination/AgentRuns/GOV-STEP4-APPLICATION-20260729/RUN_MANIFEST.md`
- `execution/_Coordination/AgentRuns/GOV-STEP4-APPLICATION-20260729/VALIDATION.md`
- `execution/_Coordination/AgentRuns/GOV-STEP4-APPLICATION-20260729/HANDOFF_STATE.md`

## Owner course correction honored (2026-07-29, in-session)

The owner directed, mid-run, that no grant record or exercise log be
created or maintained, that the existing
`docs/governance_harness/_PROPOSALS/GRANT-2026-07-29_transition_merge_execution/GRANT_CANDIDATE.md`
remain untouched as an inert draft, and that agent-executed merges under
explicit owner direction be recorded plainly — the owner is reworking the
PR-approvals basis separately. This run therefore transcribes owner acts
1–3 only and records the #417/#418 merges as ordinary owner-directed
closeouts.

## Prohibitions honored

- No push, no merge, no PR creation; one commit on
  `gov/step4-sca-application` only.
- Frozen surfaces untouched: `Gate_3_Candidate/` bytes unedited (the
  Gate 3 validator re-run regenerated `Gate_3_Validation.json`
  byte-identically); SCA-002 package changes are appends and new files
  only; the grant candidate in `_PROPOSALS/` untouched as an inert draft;
  receipts 0–62 untouched.
- No new policy; no retroactive characterization of any historical act;
  transcription and application only.
- `execution/_ScopeChange/_LATEST.md` NOT touched (outside the sealed
  write scope); its refresh is recorded as a follow-on in the SCA-002
  Handoff_State application append.

## Engine identity

Provider: Anthropic
Engine: Claude Code (Agent SDK)
Model: claude-fable-5
