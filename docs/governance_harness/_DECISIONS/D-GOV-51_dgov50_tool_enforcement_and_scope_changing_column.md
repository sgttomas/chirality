# D-GOV-51 — D-GOV-50 tool enforcement and the ScopeChanging register column

Status: OWNER-DIRECTED 2026-09-26 — application carried in the same pull
request as this record, for merge under the standing Git authorization of
2026-09-12

Date: 2026-09-26 (America/Edmonton)

FramedBy: Claude Code session, workflow-library review wave 2 (D-GOV-50 tool
enforcement), prepared in a worktree branch for integration by the Claude Code
parent session

AcceptedBasis: main@dfb089b8abae48ee699117c5bc167301963b2ab5 (merge of PR #960)

PriorRevisions (git blob SHAs at AcceptedBasis, preserved by history):
`docs/SPEC.md` `e5dbdc04…`;
`workflows/scope-change/WORKFLOW.md` `2bb9243e…`;
`workflows/scope-change/resources/contract.md` `cb99a576…`;
`workflows/scope-change/resources/method.md` `774baa39…`;
`workflows/project-setup/resources/method.md` `21b543f2…`;
`tools/scaffolding/write_status.sh` `bbb9b234…`;
`tools/practitioner_harness/test_write_status_guard.py` `da653a07…`;
`tools/practitioner_harness/README.md` `8afe9ec5…`;
`tools/REGISTRY.md` `d864c79e…`;
`tools/validation/test_workflow_catalog.py` `5d555cc1…`;
`docs/governance_harness/_DECISIONS/_REGISTER.md` `728e35d5…`

PublicationSHA: the merge commit of the pull request that introduces this
file; recorded in `_REGISTER.md` by the next Root change that touches the
register (K-AUTH-2)

EffectiveSHA: same as PublicationSHA; project loops adopt by their own ruling
(see Adoption)

## Owner direction (verbatim)

Owner Ryan Tufts (repository owner sgttomas), 2026-09-26, in the Claude Code
conversation, answering the open questions of the wave-2 plan, which included
enforcing D-GOV-50 in the Root tool:

> D1 and D2 as recommended, D3 (a), and D4 yes proceed that way. Your work plan is approved.

The recommendation for D1 was: add a `ScopeChanging` column (`YES`/`NO`) to
the scope-change accepted action register, recorded at checkpoint-group-2
acceptance. The tools admit `ISSUED → IN_PROGRESS` when the register names the
deliverable with `MODIFY`, or with `RECLASSIFY` and `ScopeChanging` `YES`. For
a register without the column (legacy), the tool refuses `RECLASSIFY` and the
human records that reopening directly, as before; `MODIFY` is still admitted.
The approved plan enforces D-GOV-50 in the Root tool; the App's validator
follows in its own change.

## The gap

D-GOV-50 item 4 left tool enforcement as a follow-up:
`tools/scaffolding/write_status.sh` refused `ISSUED → IN_PROGRESS` outright,
so every lawful reopening was recorded by hand. D-GOV-50 also admitted
`RECLASSIFY` only "where the reclassification changes the deliverable's
scope", which no register field recorded, so a tool could not tell a
scope-changing reclassification from a move.

## Decision

1. **`ScopeChanging` column.** The accepted action register
   (`Amendment_Actions.csv`, or the name its group-2 `ACCEPTED_MANIFEST.csv`
   binds) gains a `ScopeChanging` column, `YES` or `NO`, filled on every row
   in checkpoint-group-2 preparation and accepted with the register.
   `Intake_Actions.csv` may leave it blank. For a `DELIVERABLE` `RECLASSIFY`,
   `YES` records that the reclassification changes the deliverable's scope.
2. **The deterministic check.** `tools/validation/check_amendment_reopen.py`
   (CLI and importable `check_reopen()`) admits reopening a deliverable under an
   amendment only when:
   - a `checkpoint_snapshots/{AMENDMENT_ID}_GROUP-3_*/` folder holds
     `ACCEPTED_MANIFEST.csv` and a `DECISION.md` whose first heading reads
     `# {AMENDMENT_ID} checkpoint group 3 — accepted …`;
   - a group-2 `ACCEPTED_MANIFEST.csv` of the amendment binds the action
     register, and the register's current SHA-256 matches. The register is the
     row whose file name begins `Amendment_Actions` and ends `.csv`; where
     several such rows exist, it is the one whose `Role` names the
     `action register`;
   - a register row has `EntityType` `DELIVERABLE`, `EntityID` equal to the
     deliverable ID (or the ID followed by `_` and a label), `AmendmentID`
     equal to the amendment when filled, and `ActionType` `MODIFY`, or
     `RECLASSIFY` with `ScopeChanging` `YES`.

   It reads only inside the scope-change root, refuses paths and symlinks that
   leave it, and, when given a deliverable folder, refuses a scope-change root
   of another execution root. Group-1 and group-2 decisions, candidate
   snapshots and other actions are refused.
3. **Legacy registers.** A register accepted without the `ScopeChanging`
   column is legacy: the check admits its `MODIFY` rows and refuses its
   `RECLASSIFY` rows. A run that records group 3 only by moving `_LATEST.md`,
   or has no hash-bound group-2 decision snapshot, is refused. In those cases
   the human records a lawful reopening directly, citing the accepted
   snapshot, as under D-GOV-50.
4. **`write_status.sh`.** `ISSUED → IN_PROGRESS` is admitted only with all of
   these: a `HUMAN` actor; a git repository; `--approval-sha` on every root, well
   formed, reachable, and a commit whose tree holds the group-3
   `DECISION.md`; and a new `--amendment <id-or-path>` that passes the checker.
   Every reopening refusal is hard: `--force-human-override` cannot waive
   it. Without `--amendment`, the transition stays refused as
   `BACKWARD_TRANSITION`. The history line records the amendment ID, the
   group-3 snapshot, the register row and the approval SHA. `--amendment` on
   any other transition is a usage error. Every other refusal is unchanged.
5. **Group-3 record.** An amendment that authorizes reopening an `ISSUED`
   deliverable records its group-3 acceptance as a decision folder with that
   heading; PEC's SCA-005 and SCA-006 records already do.
6. **Surfaces.** `docs/SPEC.md` §3.3 (transition row and reopening rule);
   `scope-change` contract (reopening invariant, deterministic tool contract,
   snapshot-layout note, register schema), method (group-2 preparation of
   `ScopeChanging`, register header, group-3 record) and `WORKFLOW.md`;
   `project-setup` method Phase 5.5; the tool registry and the practitioner
   harness guard-reconciliation notes.

## Limits

The check reads recorded structure and hashes. It does not establish that the
human's act was genuine, or interpret a decision beyond its heading, and it
grants nothing (K-AUTH-1). Hand edits of `_STATUS.md` bypass any guard.

## Adoption

Project loops adopt this by their own ruling. The App's lifecycle
`transition.ts` still refuses `ISSUED → IN_PROGRESS`; a following App pull
request mirrors this checker's interface and refusal codes there. Runtime,
Piping and PEC receive notices; nothing is retrofitted, accepted registers
keep their columns, and historical `_STATUS.md` records are not rewritten.

## Unchanged

- The D-GOV-50 rule itself: which record authorizes reopening, the human as
  the actor, and the `project-setup` `INCREMENTAL` routing.
- The rest of the lifecycle table, §3.4, and every other `write_status.sh`
  refusal, including the human-ruled `CHECKING → IN_PROGRESS` reversal.
- `projects/chirality-app-dev`, including its transition validator.

## Application and assurance

- Application paths are listed in the tranche manifest
  `docs/governance_harness/tranche_manifests/ROOT-DGOV50-ENFORCEMENT-20260926.yaml`.
- `tools/validation/test_check_amendment_reopen.py` covers fixture and real
  amendment folders, hash mismatch, group-1 and group-2-only records,
  candidate snapshots, other actions, `RECLASSIFY` with `YES`, `NO`, blank
  and a missing column, and path and symlink escapes.
  `tools/practitioner_harness/test_write_status_guard.py` covers the
  `write_status.sh` admit and refuse paths. `tools/validation/test_workflow_catalog.py`
  checks the rule text.
- Notices are routed to the App, Runtime, Piping and PEC loops. PEC is being
  redeveloped; its notice asks for no action. No release is made.
