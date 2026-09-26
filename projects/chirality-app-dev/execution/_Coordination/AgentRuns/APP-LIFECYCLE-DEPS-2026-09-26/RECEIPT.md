# Receipt — APP-LIFECYCLE-DEPS-2026-09-26

Derivative account; the [work graph](../../WorkGraphs/app-lifecycle-deps-2026-09-26/WORK_GRAPH.md)
carries execution, and the sources below keep their authority.

## Owner direction

CHAT_TRANSCRIPTION — EVIDENCE, NOT RULING. Ryan Tufts, 2026-09-26, Claude Code
conversation, about three App-owned items that Root changes left behind (the App
SPEC dependency vocabulary, the scaffold `_DEPENDENCIES.md` template, and
`transition.ts` rejecting `CHECKING -> IN_PROGRESS`):

> Fix it appropriately.

CHAT_TRANSCRIPTION — EVIDENCE, NOT RULING. Ryan Tufts, 2026-09-26, Claude Code
conversation, deciding the open points the first candidate reported:

> A, B, C and E all as recommended

E, as the parent session relayed it to this run:

1. Reopening an ISSUED deliverable is authorized only by an ACCEPTED amendment
   (checkpoint group 3 accepted) whose accepted action register names that
   deliverable with action `MODIFY`, or `RECLASSIFY` where the reclassification
   changes the deliverable's scope. The relay named only `MODIFY`; D-GOV-50,
   which records the same owner decision, and Root SPEC §3.3 also admit a
   scope-changing `RECLASSIFY`, and this restatement follows them. A separate
   Root branch writes the rule into Root SPEC §3.3 and the `scope-change`
   workflow. The App SPEC §4.3 states it;
   the tools keep refusing `ISSUED -> IN_PROGRESS` until an amendment-record check
   is implemented, which is an App follow-up.
2. The App layer's inability to verify that the ruling is committed or the SHA is
   a real commit is recorded as a known limit.
3. Both this run-folder receipt and the `LOOP_RECEIPTS.md` pointer are kept.
4. The Runtime descriptor, the UI reversal input and the DEL-07-04 SOW
   verification sentences are App-loop follow-ups, not implemented here.

The parent session relayed only E's content to this run; A, B and C are
recorded here only as part of the quoted decision.

## Root notice adoption

| Notice | This loop's adoption |
|---|---|
| `NOTICE_2026-09-26_DEPENDENCY_SCHEMA_D-GOV-46.md` | Adopted for the two App surfaces it affects. App SPEC §5.2 now carries the §5.2 heading schema, placeholder form, legacy-heading reading, the `NOT_TRACKED`/`DECLARED`/`FULL_GRAPH` meanings with `TRACKED` read as `FULL_GRAPH`, and the Root §13 coordination-representation wording. `scaffold.ts` writes the §5.2 skeleton. Existing `_DEPENDENCIES.md` files are not rewritten. |
| `NOTICE_2026-09-26_DEPENDENCY_FOLLOWUPS.md` | Adopted for App SPEC §5.2 and the scaffold (item 1 and item 5). App SPEC §5.2 states that the recorded register is the union of the declared sections and `Dependencies.csv`, that a reader never relies on the CSV alone, the one-edge and disagreement rules, and the default maturity threshold for a declaration without one. The scaffold template, its test and the App SPEC template write the Register line exactly as `tools/coordination/materialize_local_dependencies.py` writes it. App SPEC §5.2 also says the App's own dependency reads are CSV-only register evidence, not a blocker judgment. Not adopted here: App blocker computation from the union (App follow-up) and the App's bundled `dependency-extract`, `project-setup` and `review` workflows, whose timing the notice leaves to this loop. |
| `NOTICE_2026-09-26_PROJECT_DAG_D-GOV-49.md` | Adopted for App SPEC §5.2 only: it restates Root §5.3/§5.4's split of blocker computation between a project without an accepted DAG (recorded registers) and one with (the accepted current version; `DAG pending` on an undecided departure), and that neither the local files nor a DAG is self-authorizing. The App has no `execution/_DAG/`, so the no-accepted-DAG rule applies. The App's legacy PKG-00 SCC case home, `project-dag` adoption and `LOOP_INIT.md` are not addressed. |
| `NOTICE_2026-09-26_REVIEW_SPEC34_REVERSAL.md` | Adopted for `transition.ts`, the transition API and the MCP `status_transition` tool, which now admit the human-ruled `CHECKING -> IN_PROGRESS` reversal: HUMAN/USER/OPERATOR actor, format-valid `approvalSha`, and a `ruling` naming a non-empty file inside the project root other than the deliverable's own `_STATUS.md`. As `write_status.sh` does, they also accept an optional `ruling` on `IN_PROGRESS -> CHECKING` and `CHECKING -> ISSUED` (the review method passes `--ruling` there) and record it in history. `ISSUED -> IN_PROGRESS` and every other backward move stay rejected, as in `write_status.sh`. Differences from `write_status.sh`: the App does not check that the ruling is git-tracked or that the SHA is a reachable commit (a known limit, below); it always requires the SHA on the human gates; it records a forward-gate ruling in the history note rather than an `**Authorization Basis:**` field; and the reversal removes the `**Checking Approval SHA:**` field, which `write_status.sh` leaves as history. The workflow's review-gate changes are not addressed here. |
| `NOTICE_2026-09-26_DECOMP_RULINGS_D-GOV-47.md`, `NOTICE_2026-09-26_WORKFLOW_WAVE2A_FORMATION.md` | Not addressed. The resulting `software-decomp` authority-corpus drift is retained without repinning. |
| `NOTICE_2026-09-26_PACKAGE_HOME_D-GOV-48.md` | Not addressed; it arrived with the rebase onto `6281273fa`. Its `software-decomp` drift is retained without repinning. |
| Other 2026-09-26 notices (research contract, duplicate retirement, wave 2a setup-deps, change-concerns, closure, execution) | Not addressed by this run; no App surface here depends on them. |

## Result

- Deliverables: DEL-07-04 (CHECKING reversal rule, ruling checks,
  route/MCP/client field and tests) and DEL-07-02 (scaffold template and test).
  The App SPEC change also belongs to this run.
- Branch `wave3-app-lifecycle-deps`, first cut from
  `8f9bd314c5f2499e6faf5bf4bdce917927e8185e` and rebased without conflicts onto
  `6281273fa7bd96b66703009e6325db2fa74815b3`; integrated by the parent session
  on `claude/brave-goodall-wj3hok` (PR #960). The review revision is
  Examined-Through origin/main `6128f8b85251ccb0a5e13ad48d0e4d5e971d11d6`. The
  parent session integrates, reviews and merges.
- Second PR #960 review hardening: caller metadata can no longer set the
  approval SHA fields (`INVALID_METADATA`); metadata keys are printable ASCII;
  C1 controls and Unicode line and paragraph separators are rejected in values,
  history notes and rulings; the actor is recorded on one line.
- Tranche manifest:
  `docs/governance_harness/tranche_manifests/APP-LIFECYCLE-DEPS-ADOPTION-20260926.yaml`.
- Loop ledger pointer: `loop/LOOP_RECEIPTS.md` Receipt-265.

## Checks (worktree candidate)

- APP-HOLD-1 `dispatch` ALLOW for DEL-07-04 and DEL-07-02 (first pass);
  `app_hold.py scan --require-register-match` PASS on the resumed candidate.
- `npm run typecheck` pass. Focused Vitest pass for lifecycle-status,
  deliverable-contracts, chirality-mutating-mcp, harness-scaffold,
  workspace-deliverable-api and tool-descriptor. The new transition tests fail
  against the prior `transition.ts` (negative control).
- Full Vitest: one failure, `harness-attachment-resolver` "rejects unreadable
  regular files", because the host runs as uid 0 (a `chmod 000` file stays
  readable). It is unrelated to the changed files.
- Practitioner-harness self-check and pytest pass; receipt validator VALID
  after the append. Tranche-manifest, conflict-marker and run-record-leak
  validators are recorded in the commit's hand-off to the parent.
- Revision for the owner's decision, rebased on `6281273fa`: `app_hold.py scan
  --require-register-match` PASS (exit 0); `check` `dispatch` and `reliance`
  ALLOW for DEL-07-04 and DEL-07-02; typecheck exit 0; focused Vitest
  (lifecycle-status, deliverable-contracts, chirality-mutating-mcp,
  harness-scaffold) 4 files, 122 tests pass; harness self-check exit 0 (WARN
  rows only, none on changed files) and pytest 398 pass; receipt validator
  VALID; tranche-manifest validator `--added-manifests-only` exit 0. No product
  source changed in this revision.
- Review revision for PR #960, on `claude/brave-goodall-wj3hok` at origin/main
  `6128f8b85`: `npx tsc --noEmit -p .` exit 0; focused Vitest
  (lifecycle-status, deliverable-contracts, chirality-mutating-mcp,
  harness-scaffold) 4 files, 150 tests pass, exit 0. The new behavior tests fail
  against the prior source (negative control: 24 failures). Full Vitest: 2369
  pass and 2 fail, both host-environment failures outside the changed files: the
  uid-0 `harness-attachment-resolver` case above, and
  `controlled-ci-runtime.integration` because the borrowed `node_modules` cannot
  resolve the Runtime package's `yaml` dependency. The Root validators and the
  export regeneration are recorded in the commit's hand-off to the parent.

## Limits

- `ISSUED -> IN_PROGRESS` is still refused. The owner's decision (E1) answers
  REQ-004's question of which record authorizes it; App SPEC §4.3 states the
  rule. Enforcement waits for an amendment-record check in the status tools.
- Known limit (E2): the actor is asserted by the caller, and the App layer does
  not verify that the ruling is committed or that the SHA names a real commit.
  Its checks are format, location and non-empty-content checks only, so any
  caller able to write files in the project can satisfy them: an agent that
  supplies HUMAN, a well-formed SHA and a non-empty ruling file it wrote can
  perform the `CHECKING -> IN_PROGRESS` reversal. App SPEC §4.3 states this. The
  existing CHECKING and ISSUED gates share this limit, as does REQ-005's live
  human-identity limit (P-07/P-14): these values are evidence, not proof of a
  human act. The brief asked for this limit in
  `execution/_Coordination/APP_HOLD_REGISTER.csv`. That register does not fit
  it: `app_hold.py` admits only `HOLD`, `STRUCTURAL_BOOTSTRAP` and
  `SOW_INITIALIZATION` rows. A `HOLD` row must mirror a held contract that the
  scan finds, carry D-APP-75/D-APP-79 authority and prohibit every operation on
  its deliverable. A limit row would fail `load_register` or the scan match, or
  would wrongly hold DEL-07-04. The limit is therefore recorded here, in the
  work graph and in DEL-07-04 MEMORY, and the register is unchanged.
- No lifecycle transition, approval-SHA refresh, dependency acceptance,
  authority-corpus repin, release or issuance.

## App-loop follow-ups (E4; not implemented here)

- Implement the amendment-record check that admits `ISSUED -> IN_PROGRESS`
  (DEL-07-04 REQ-004).
- Compute App dependency blockers from the recorded register (the union of the
  declared sections and `Dependencies.csv`); the App's reads are CSV-only.
- Decide when the App's bundled `dependency-extract`, `project-setup` and
  `review` workflows pick up the dependency follow-up revision.
- The Runtime `status_transition` descriptor does not list `ruling`.
- The workbench and pipeline UI forms have no reversal input.
- The DEL-07-04 SOW verification sentences (CLM-003/CLM-008) are left for the
  bounded closeout.

Details are in the work graph.

Execution: Claude Code subagents (TASK-type executors, no delegation) in an
isolated worktree for the parent session; a second subagent resumed the run
after a container restart. Model identifiers are withheld at the dispatching
session's instruction; the commit's session trailer identifies the run.
