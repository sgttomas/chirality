# Fresh review brief — N3 D-GOV-34 and TM-ROOT-124 instruction tranche

RunID: `ROOT_DEL0206_ACCEPTANCE_DGOV34_2026-08-21`

ReviewID: `N3-R1-DGOV34-CHANGE`

Role: fresh independent read-only reviewer

AcceptedBasis: `33e871fc38d8ef4bb51f7c25cdc6ca2e8dcb69e0`

## Objective

Adversarially review the complete uncommitted N3 candidate for exact compliance
with the owner D4 ruling, live TM-ROOT-124 proposed disposition, D-GOV-33 record
convention, G4 manifest contract, and the root agent-index change-notice rule.

## Required reads

- root `AGENTS.md`;
- `agents/AGENT_HELPS_HUMANS.md` and pre/post diff of
  `agents/AGENT_CHANGE.md`;
- N3 `LAUNCH_BRIEF.md` and amendment
  `../../amendments/N3-HELPS-HUMANS-DGOV34/V2.md` resolved from the run root;
- the run owner direction transcript;
- live TM-ROOT-124 row;
- App `projects/chirality-app-dev/loop/LOOP_RECEIPTS.md` Receipt-74;
- D-GOV-33 and the live D-GOV register convention;
- `tools/validation/validate_instruction_tranche_manifest.py` and the candidate
  manifest;
- all three candidate routed notices.

## Candidate paths

- `docs/governance_harness/_DECISIONS/D-GOV-34_change_clean_basis_lane_routine.md`
- `docs/governance_harness/_DECISIONS/_REGISTER.md`
- `agents/AGENT_CHANGE.md`
- `docs/governance_harness/tranche_manifests/ROOT-TM124-CHANGE-ROUTINE-BRANCH-20260821.yaml`
- `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-08-21_ROOT_DGOV34_CHANGE_ROUTINE_BRANCH.md`
- `projects/chirality-piping/execution/_Coordination/NOTICE_2026-08-21_ROOT_DGOV34_CHANGE_ROUTINE_BRANCH.md`
- `_DomainEngines/_Coordination/NOTICE_2026-08-21_ROOT_DGOV34_CHANGE_ROUTINE_BRANCH.md`

## Review gates

Return `PASS` only if all gates pass:

1. D4 is transcribed verbatim, D-GOV-34 is framed by this run, AcceptedBasis is
   exact, Supersedes is none, and the record makes no self-publication claim.
2. The register has exactly one D-GOV-34 row and does not expand the ruling.
3. The CHANGE diff says clean-basis branch/worktree-lane creation is routine,
   dirty-basis lanes remain non-routine, and grants no broader authority.
4. The candidate `AGENT_CHANGE.md` pre-hash is exactly
   `950e96f4cfff13af48b9edd93a4b47356e8b388a430d70977fd528ffbd4120fa`;
   its notices consistently name the observed post-hash.
5. Manifest `basis:` is the real full 40-character branch base and resolves as
   a commit; all changed protected paths are declared; routed notice paths and
   dispositions are honest.
6. App, Piping, and domain-engine notices each identify pre/post SHA-256 and a
   loop-owned follow-on, including corpus/SHA repin where applicable, without
   adopting on behalf of the receiving loop.
7. No Task Management register, receipt, product implementation, lifecycle,
   release, publication, reliance, Git commit/push/PR/merge, or out-of-scope
   instruction change is present in N3's diff.
8. G4 schema, agent instruction, entrypoint, focused tests, and diff hygiene
   evidence are credible and reproducible.

## Output

Write only
`execution/_Coordination/AgentRuns/ROOT_DEL0206_ACCEPTANCE_DGOV34_2026-08-21/instances/N3-HELPS-HUMANS-DGOV34/REVIEW_RETURN_R1.md`.
Return `PASS` or `FAIL`, list each gate, enumerate every finding with exact
path/line evidence, and name commands rerun. Do not edit candidate files or any
other path.
