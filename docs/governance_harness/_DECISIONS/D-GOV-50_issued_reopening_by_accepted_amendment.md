# D-GOV-50 — Reopening an ISSUED deliverable under an accepted amendment

Status: OWNER-DIRECTED 2026-09-26 — application carried in the same pull
request as this record, for merge under the standing Git authorization of
2026-09-12

Date: 2026-09-26 (America/Edmonton)

FramedBy: Claude Code session, workflow-library review wave 3 (incremental
project-setup after a scope change), prepared on local branch
`wave3-incremental-setup` for integration by the Claude Code parent session on
`claude/brave-goodall-wj3hok`

AcceptedBasis: main@5bbc9de22378f8f7056a010e1a05d2c13518f0e7 (merge of PR #945)

PriorRevisions (git blob SHAs at AcceptedBasis, preserved by history):
`docs/SPEC.md` `73223c0b…`;
`workflows/scope-change/WORKFLOW.md` `414957e4…`;
`workflows/scope-change/resources/contract.md` `b0fb2fbc…`;
`workflows/scope-change/resources/method.md` `def62110…`;
`workflows/project-setup/resources/method.md` `3ba16fd8…`;
`tools/validation/test_workflow_catalog.py` `9579a643…`;
`docs/governance_harness/_DECISIONS/_REGISTER.md` `be4e4cb5…`

PublicationSHA: the merge commit of the pull request that introduces this
file; recorded in `_REGISTER.md` by the next Root change that touches the
register (K-AUTH-2)

EffectiveSHA: same as PublicationSHA; project loops adopt by their own ruling
(see Adoption)

## Owner direction (verbatim)

Owner Ryan Tufts (repository owner sgttomas), 2026-09-26, in the Claude Code
conversation, answering the open questions of the incremental project-setup
tranche (`ROOT-PROJECT-SETUP-INCREMENTAL-20260926`), one of which (E1) asked
which record authorizes reopening an `ISSUED` deliverable:

> A, B, C and E all as recommended

The recommendation for E1 was: `ISSUED → IN_PROGRESS` is authorized only by
an accepted scope-change amendment whose accepted action register names the
deliverable with `MODIFY`; the human records the transition, citing the
accepted amendment snapshot; the incremental setup mode's `MODIFY` routing is
where it happens; tool enforcement is a later follow-up.

## The gap

`docs/SPEC.md` §3.3 listed `ISSUED → IN_PROGRESS` as "Human, via the governed
scope-change process only" without saying which scope-change record
authorizes it or when. `scope-change` did not state it either, and the new
incremental setup mode held `ISSUED` deliverables with no defined way
forward. The App's DEL-07-04 REQ-004 asks the same question for its
transition validator.

## Decision

1. **Authorizing record.** `ISSUED → IN_PROGRESS` is authorized only by an
   accepted amendment of the governed scope-change process: its checkpoint
   group 3 is accepted, and its accepted action register names that
   deliverable with action `MODIFY`, or `RECLASSIFY` where the
   reclassification changes the deliverable's scope (`scope-change` treats a
   PROJECT/SOFTWARE `RECLASSIFY` as `MODIFY` plus relocation). A proposal, a
   group-1 or group-2 decision, a candidate snapshot, or any other action does
   not authorize it.
2. **Actor and record.** The human records the transition in `_STATUS.md`,
   citing the accepted amendment snapshot. No agent records it.
3. **Where it happens.** After acceptance, at the `MODIFY` routing of
   `project-setup` in `INCREMENTAL` mode (method Phase 5.5), which presents the
   reopening to the human. After it is recorded, the contract revision runs
   through `scope-of-work` `MODE=REVISE`. `scope-change` records in its
   propagation plan and `Handoff_State.md` which `ISSUED` deliverables the
   amendment will authorize the human to reopen; it does not change their
   lifecycle state in the candidate.
4. **Tool enforcement is not part of this decision.**
   `tools/scaffolding/write_status.sh` and the App's
   `projects/chirality-app-dev/frontend/src/lib/lifecycle/transition.ts` still refuse
   `ISSUED → IN_PROGRESS` until they implement a check of the amendment
   record. Until then the human records the transition directly. That tool
   work is a follow-up; neither tool is changed here.
5. **Surfaces.** `docs/SPEC.md` §3.3 (transition table row and a new
   "Reopening an `ISSUED` deliverable" rule; §3.4 points to it);
   `scope-change` contract (invariant), method (`MODIFY` planning, apply step,
   `Handoff_State.md`) and `WORKFLOW.md`; `project-setup` method Phase 5.5.

## Adoption

Project loops adopt this by their own ruling. It answers the App's DEL-07-04
REQ-004 question ("which scope-change record authorizes reopening an issued
deliverable"): the accepted amendment snapshot whose accepted action register
names the deliverable with `MODIFY` (or scope-changing `RECLASSIFY`). The App
decides whether and when its validator checks that record. Nothing is
retrofitted; historical `_STATUS.md` records are not rewritten.

## Unchanged

- The rest of the lifecycle table and §3.4 entry conditions, including the
  human-ruled `CHECKING → IN_PROGRESS` reversal.
- `docs/TYPES.md`, whose statement that post-issuance changes flow only
  through the governed scope-change process is consistent with this rule.
- `tools/scaffolding/write_status.sh`, the App's transition validator, and
  every other tool.

## Application and assurance

- Application paths are listed in the tranche manifest
  `docs/governance_harness/tranche_manifests/ROOT-PROJECT-SETUP-INCREMENTAL-20260926.yaml`,
  which also carries the owner's other decisions of the same direction.
- `tools/validation/test_workflow_catalog.py` checks the rule text in SPEC
  §3.3 and the `scope-change` contract, and the related `scope-of-work`
  `REVISE` mode and `project-setup` routing.
- Notices are routed to the App, Runtime, Piping and PEC loops. PEC is being
  redeveloped and the owner is deferring action there. No release is made.
