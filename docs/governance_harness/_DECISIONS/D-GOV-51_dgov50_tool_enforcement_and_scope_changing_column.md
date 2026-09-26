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
   - a decision folder
     `checkpoint_snapshots/{AMENDMENT_ID}_GROUP-3_[AMENDMENT-{K}_]{YYYY-MM-DD}[_{N}]/`
     holds `ACCEPTED_MANIFEST.csv` and a `DECISION.md` whose first non-blank
     line is the heading `# {AMENDMENT_ID} checkpoint group 3 — accepted …`,
     with `accepted` directly after the dash. Folders with other names, such
     as candidates, do not count. Scope-change group 3 accepts or returns, so
     a qualified acceptance (`accepted with a limited basis`) is the accepted
     outcome; its qualifications are not interpreted;
   - the governing group-2 `ACCEPTED_MANIFEST.csv` binds the action register,
     and the register's SHA-256 matches. The governing manifest is that of the
     latest group-2 decision folder that binds a register (highest
     `AMENDMENT-{K}`, then date, then `_{N}`), so a revised group-2 acceptance
     replaces an earlier binding. The register is the row whose file name
     begins `Amendment_Actions` and ends `.csv`; where one manifest binds
     several such rows, it is the single row whose whole `Role` value is
     `action register` or `exact final action register` (case-insensitive,
     optionally with a parenthesized note);
   - the register rows naming the deliverable (`EntityType` `DELIVERABLE`,
     `EntityID` equal to the deliverable ID or the ID followed by `_` and a
     label, `AmendmentID` equal to the amendment or blank) include no
     `REMOVE`, and one is `MODIFY`, or `RECLASSIFY` with `ScopeChanging`
     `YES`. Values are read as recorded; a relevant value or column name with
     stray leading or trailing whitespace is a schema refusal (no accepted
     register in the repository carried any on 2026-09-26);
   - given the deliverable's `_STATUS.md`, its history does not already record
     `reopened from ISSUED; amendment: {AMENDMENT_ID}`: one tool-recorded
     reopening per accepted amendment. A human may still record a further
     reopening directly.

   With `--at-commit <sha>` (importable `at_commit=`), every record above is
   read from that commit through git, never from the working tree:
   `checkpoint_snapshots/` is listed from the commit's tree, tree entries are
   resolved as such, a symlink entry whose target leaves the scope-change root
   is refused, and the commit must be an ancestor of `HEAD`. Git reads
   ignore local replace refs and grafts. Without it the
   working tree is read and the result is reported as unanchored; that mode
   serves inspection only. The scope-change root is the `_ScopeChange/` folder
   of the deliverable's execution root (its outermost `execution/` ancestor,
   which an adapter manifest found above the deliverable must agree with); a
   `_ScopeChange/` inside a package or deliverable folder is never used. It
   reads only inside that root and refuses paths and symlinks that leave it.
   Group-1 and group-2 decisions, candidate snapshots and other actions are
   refused. Refusal codes: `AMENDMENT_UNRESOLVED`,
   `SCOPE_CHANGE_ROOT_NOT_FOUND`, `PATH_ESCAPE`,
   `AMENDMENT_OUTSIDE_DELIVERABLE_ROOT`, `APPROVAL_SHA_UNREACHABLE`,
   `APPROVAL_SHA_NOT_ANCESTOR`, `AMENDMENT_ALREADY_USED`,
   `GROUP3_NOT_ACCEPTED`, `GROUP2_MANIFEST_MISSING`, `MANIFEST_SCHEMA`,
   `REGISTER_NOT_BOUND`, `REGISTER_AMBIGUOUS`, `REGISTER_MISSING`,
   `REGISTER_HASH_MISMATCH`, `REGISTER_SCHEMA`, `NO_DELIVERABLE_ACTION`,
   `DELIVERABLE_REMOVED`, `RECLASSIFY_LEGACY_REGISTER`,
   `RECLASSIFY_NOT_SCOPE_CHANGING`, `ACTION_NOT_AUTHORIZING`.
3. **Legacy registers.** A register accepted without the `ScopeChanging`
   column is legacy: the check admits its `MODIFY` rows and refuses its
   `RECLASSIFY` rows. A run that records group 3 only by moving `_LATEST.md`,
   or has no hash-bound group-2 decision snapshot, is refused. In those cases
   the human records a lawful reopening directly, citing the accepted
   snapshot, as under D-GOV-50.
4. **`write_status.sh`.** `ISSUED → IN_PROGRESS` is admitted only with all of
   these: a `HUMAN` actor; a git repository; `--approval-sha` on every root,
   well formed, reachable and an ancestor of `HEAD`; and a new
   `--amendment <id-or-path>` that passes the checker run as
   `--at-commit <approval SHA> --status-file <_STATUS.md>`. The guard never
   uses the checker's working-tree mode. Every reopening refusal is hard:
   `--force-human-override` cannot waive it. Without `--amendment`, the
   transition stays refused as `BACKWARD_TRANSITION`. The history line records
   the amendment ID, the group-3 snapshot, the register row and the approval
   SHA. `--amendment` on any other transition is a usage error. Every other
   refusal is unchanged.
5. **Group-3 record.** An amendment that authorizes reopening an `ISSUED`
   deliverable records its group-3 acceptance as a committed decision folder
   with that heading; PEC's SCA-005 and SCA-006 records already do.
6. **Surfaces.** `docs/SPEC.md` §3.3 (transition row and reopening rule);
   `scope-change` contract (reopening invariant, deterministic tool contract,
   snapshot-layout note, register schema), method (group-2 preparation of
   `ScopeChanging`, register header, group-3 record) and `WORKFLOW.md`;
   `project-setup` method Phase 5.5; the tool registry and the practitioner
   harness guard-reconciliation notes.

## Limits

The check reads recorded structure and hashes. The approval SHA fixes which
committed records are read; it does not establish that the human's act was
genuine or took place at that commit, and a record committed on the branch's
history is read as recorded. The check does not interpret a decision beyond
its heading, and it grants nothing (K-AUTH-1). Hand edits of `_STATUS.md`
bypass any guard, including the once-per-amendment check, which reads the
tool's own history line.

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
  amendment folders (PEC SCA-005 and SCA-006, Piping SCA-011 and Runtime
  SCA-001, read at `HEAD`), hash mismatch, group-1 and group-2-only records,
  candidate snapshots and folders, heading forms, `REMOVE` beside `MODIFY`,
  other actions, `RECLASSIFY` with `YES`, `NO`, blank and a missing column,
  revised group-2 bindings, role matching, stray whitespace, replay, nested
  `_ScopeChange/` folders, path and symlink escapes in the working tree and in
  a commit's tree, and the at-commit regressions: uncommitted register and
  manifest edits, an uncommitted heading flip, an untracked forged group-3
  folder, and a side-branch commit.
  `tools/practitioner_harness/test_write_status_guard.py` covers the
  `write_status.sh` admit and refuse paths, including those regressions and a
  second reopening under the same amendment. `tools/validation/test_workflow_catalog.py`
  checks the rule text.
- Independent review of the first candidate of the introducing pull request
  (#968) found that the approval SHA bound no content: the checker read the
  working tree. The at-commit mode, the ancestry check, the anchored heading
  pattern, candidate-folder exclusion, the `REMOVE`, replay, execution-root,
  revised-group-2, `AmendmentID`, role and whitespace rules above were added
  in the same pull request before merge, so this record states the merged
  behaviour.
- Notices are routed to the App, Runtime, Piping and PEC loops. PEC is being
  redeveloped; its notice asks for no action. No release is made.
