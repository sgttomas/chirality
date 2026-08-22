# Orchestration plan — DEL-02-06 exact-byte acceptance, TM promotions, and D-GOV-34

RunID: `ROOT_DEL0206_ACCEPTANCE_DGOV34_2026-08-21`

Version: `1`

SelectionAuthority: `HUMAN`

Posture: `MIXED`

## Accepted basis and pre-dispatch gate

- Repository/working root: `/Users/ryan/.codex/worktrees/0b6e/chirality`.
- Branch: `codex/root-del0206-acceptance-governance-20260821`.
- Branch base: `origin/main@33e871fc38d8ef4bb51f7c25cdc6ca2e8dcb69e0`.
- Required PR #605 merge is the branch base and Receipt 112 is present.
- Candidate byte gate: `14191` bytes and SHA-256 `e5ae4e874bdace43720db082a9bd1ae3ff81b9e731264c65039b02d7f720467c`: PASS.
- Root Step-0 G0–G4: PASS. Branch was clean and `0/0` from `origin/main` before run-record creation.
- Governing transcript: `OWNER_DIRECTION_TRANSCRIPT_2026-08-21.md` (`CHAT_TRANSCRIPTION`).

## Work graph

| Node | Manager | Objective | Dependencies | Write ownership | Expected return | Fan-in gate |
|---|---|---|---|---|---|---|
| N1 | WORKING_ITEMS | Record exact-byte acceptance in `DEL-02-06-COMPATIBILITY-ACCEPTANCE-005`, preserve `INITIALIZED` absent an explicit accepted-SOW transition, and route the App carrier notice | none | DEL-02-06 package path; one App coordination notice; N1 instance records | immutable acceptance snapshot, member and snapshot manifests, fresh rehash validation, status/handoff, notice, acceptance-record SHA | fresh independent review PASS; exact candidate gate and held bindings preserved |
| N2 | TASK_MANAGEMENT | Apply D2/D3 promotions with ruling file and mandatory federation; leave TM-ROOT-126/127 untouched | none | Root Task Management register home; N2 instance records | two exact row promotions, firing evidence, ruling file, complete federation, no foreign writes | register validators/federation PASS; no disposition or unruled row changes |
| N3 | HELPS_HUMANS | Mint D-GOV-34, register it, amend CHANGE routine closeout, add G4 manifest and routed notices | none; commit after N1/N2 | D-GOV-34 decision/register; `agents/AGENT_CHANGE.md`; one G4 manifest; App/Piping/domain-engine notices; N3 instance records | exact D4 authority record, narrow instruction amendment, real-base manifest, three notices, fresh review | fresh independent review PASS; pre/post hashes and containment validated |
| N4 | TASK_MANAGEMENT follow-up | After N3 lands, close TM-ROOT-124 `RESOLVED_WITH_CHANGE` citing D-GOV-34 and landed bytes | N3 committed | Root Task Management register/archive and N2 follow-up records | exact closure/archive with evidence SHA and final federation | register validators/federation PASS; no unrelated row changes |

N1, N2, and N3 are execution-independent and write-disjoint. Their commits are
serialized in the owner-prescribed order N1, N2, N3. N4 is a dependent
follow-up to N2 and runs only after the N3 commit exists. HELP_HUMAN owns
cross-node fan-in, final validation, Git publication, PR creation, Receipt 113,
and the terminal run handoff.

## Human gates and exclusions

- D1 accepts only the named 14,191 candidate bytes. All ten `HELD_UNAVAILABLE` bindings remain held.
- No implementation, cutover, inferred lifecycle promotion, release, publication, reliance, foreign-loop work/register write, artifact-proof label, or merge.
- TM-ROOT-126/127 remain OPEN and unassigned. No other OPEN row or unfired DEFERRED row is selectable.
- If `origin/main` advances mid-PR, no sync occurs without a new owner authorization.
- A failed review is repaired against enumerated findings and re-reviewed by a fresh reviewer until PASS; independent nodes continue.
