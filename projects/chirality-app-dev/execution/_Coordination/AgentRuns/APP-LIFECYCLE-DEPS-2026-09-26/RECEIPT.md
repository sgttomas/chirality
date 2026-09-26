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
   deliverable with action `MODIFY`. A separate Root branch writes the rule into
   Root SPEC §3.3 and the `scope-change` workflow. The App SPEC §4.3 states it;
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
| `NOTICE_2026-09-26_REVIEW_SPEC34_REVERSAL.md` | Adopted for `transition.ts`, the transition API and the MCP `status_transition` tool, which now admit the human-ruled `CHECKING -> IN_PROGRESS` reversal: HUMAN/USER/OPERATOR actor, format-valid `approvalSha` and a `ruling` file inside the project root, matching `write_status.sh` under the App adapter's guards. `ISSUED -> IN_PROGRESS` and every other backward move stay rejected, as in `write_status.sh`. The workflow's review-gate changes are not addressed here. |
| `NOTICE_2026-09-26_DECOMP_RULINGS_D-GOV-47.md`, `NOTICE_2026-09-26_WORKFLOW_WAVE2A_FORMATION.md` | Not addressed. The resulting `software-decomp` authority-corpus drift is retained without repinning. |
| `NOTICE_2026-09-26_PACKAGE_HOME_D-GOV-48.md` | Not addressed; it arrived with the rebase onto `6281273fa`. Its `software-decomp` drift is retained without repinning. |
| Other 2026-09-26 notices (research contract, duplicate retirement, wave 2a setup-deps, change-concerns, closure, execution) | Not addressed by this run; no App surface here depends on them. |

## Result

- Deliverables: DEL-07-04 (CHECKING reversal rule, ruling checks,
  route/MCP/client field and tests) and DEL-07-02 (scaffold template and test).
  The App SPEC change also belongs to this run.
- Branch `wave3-app-lifecycle-deps`, first cut from
  `8f9bd314c5f2499e6faf5bf4bdce917927e8185e` and rebased without conflicts onto
  `6281273fa7bd96b66703009e6325db2fa74815b3`; no PR yet. The parent session
  integrates, reviews and merges.
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

## Limits

- `ISSUED -> IN_PROGRESS` is still refused. The owner's decision (E1) answers
  REQ-004's question of which record authorizes it; App SPEC §4.3 states the
  rule. Enforcement waits for an amendment-record check in the status tools.
- Known limit (E2): the App layer cannot verify that the ruling is committed or
  that the SHA is a real commit. An agent that supplies HUMAN, a well-formed SHA
  and a real ruling path can perform the `CHECKING -> IN_PROGRESS` reversal. The
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
- The Runtime `status_transition` descriptor does not list `ruling`.
- The workbench and pipeline UI forms have no reversal input.
- The DEL-07-04 SOW verification sentences (CLM-003/CLM-008) are left for the
  bounded closeout.

Details are in the work graph.

Execution: Claude Code subagents (TASK-type executors, no delegation) in an
isolated worktree for the parent session; a second subagent resumed the run
after a container restart. Model identifiers are withheld at the dispatching
session's instruction; the commit's session trailer identifies the run.
