# Work graph — lifecycle reversal and dependency schema adoption

## Intent and selected route

- Stable run identity: `APP-LIFECYCLE-DEPS-2026-09-26`.
- Steering: owner direction "Fix it appropriately." (2026-09-26, Claude Code
  conversation) about three App-owned items that Root D-GOV-46 and
  `ROOT-REVIEW-SPEC34-REVERSAL-20260926` left behind. Transcription and notice
  adoption are in the [receipt](../../AgentRuns/APP-LIFECYCLE-DEPS-2026-09-26/RECEIPT.md).
  The owner's follow-up decision "A, B, C and E all as recommended" (2026-09-26)
  settles the authorizing record for `ISSUED -> IN_PROGRESS`, the known-limit
  record, the receipt placement and the App follow-ups; the receipt transcribes
  it.
- Basis: `origin/main` at `8f9bd314c5f2499e6faf5bf4bdce917927e8185e`, rebased
  without conflicts onto `6281273fa7bd96b66703009e6325db2fa74815b3`; local branch
  `wave3-app-lifecycle-deps` in an isolated worktree. The parent session
  integrates it on `claude/brave-goodall-wj3hok` (PR #960), reviews and merges;
  the review revision (R2) is Examined-Through origin/main
  `6128f8b85251ccb0a5e13ad48d0e4d5e971d11d6`.
- Route: `NOTICE_2026-09-26_DEPENDENCY_SCHEMA_D-GOV-46.md` → App SPEC §5.2 and the
  scaffold `_DEPENDENCIES.md` template (DEL-07-02);
  `NOTICE_2026-09-26_DEPENDENCY_FOLLOWUPS.md` and
  `NOTICE_2026-09-26_PROJECT_DAG_D-GOV-49.md` → App SPEC §5.2 (union recorded
  register, accepted-DAG blocker split) and the scaffold Register line (R2);
  `NOTICE_2026-09-26_REVIEW_SPEC34_REVERSAL.md` and DEL-07-04 REQ-004/REQ-005
  (concordance residual `DEL-07-04#CLM-011.4`) → `transition.ts`, the transition
  API/MCP surfaces and App SPEC §4.3. Only the `CHECKING -> IN_PROGRESS` reversal
  is implemented; `ISSUED -> IN_PROGRESS` stays refused until the tools check the
  authorizing amendment record (see departures).
- APP-HOLD-1: `dispatch` preflight ALLOW for DEL-07-04 and DEL-07-02 at
  `8f9bd314c`.
- Authority limits: no lifecycle transition, dependency acceptance, approval-SHA
  refresh, authority-corpus repin, UI change, Runtime change or release.

## Work

| ID / outcome | Scope | Completion check | State / result |
|---|---|---|---|
| W1 — App SPEC §5.2 on the D-GOV-46 schema and modes | App `docs/SPEC.md` §5.2 (schema, legacy headings, modes, and the Root §13 coordination-representation wording, which the App SPEC had no section for); §4.3 records the reversal evidence the tools require, the owner-decided authorizing record for `ISSUED -> IN_PROGRESS` (an ACCEPTED amendment whose accepted action register names the deliverable with `MODIFY`, or `RECLASSIFY` where the reclassification changes the deliverable's scope, citing Root SPEC §3.3, D-GOV-50 and `scope-change`), and that the tools reject that move until they check the record. §4.2–4.4 already carried both human reversals. | Headings, placeholder form, legacy-heading reading, `NOT_TRACKED`/`DECLARED`/`FULL_GRAPH` meanings, the union recorded register and accepted-DAG blocker split (R2) and the §13 statements match Root SPEC §5.2–5.4 and §13; App-specific scaffold and read behavior stated. | COMPLETE |
| W2 — scaffold writes the §5.2 skeleton | DEL-07-02 `frontend/src/lib/harness/scaffold.ts` and `harness-scaffold.test.ts`. | Exact heading order, mode shared with the `_COORDINATION.md` it writes, resolvable coordination pointer, `NOT_RUN_YET`/`(placeholder)` bodies, no inferred edges, no handoff section. | COMPLETE |
| W3 — human-ruled CHECKING reversal | DEL-07-04 `transition.ts`, `status-writer.ts`, `deliverable-contracts.ts`, transition route, MCP `status_transition` schema, client type, and their tests. | Full 30-pair transition table; reversal evidence, denial (including HUMAN with a missing SHA or ruling, through the validator, API and MCP tool) and path-containment cases; `ISSUED -> IN_PROGRESS` and other backward moves stay rejected; the new tests fail against the prior `transition.ts`. | COMPLETE (CHECKING reversal); ISSUED check is follow-up FU1 |
| V1 — checks | Candidate checks listed in the receipt. | Typecheck, focused and full Vitest, harness self-check and pytest, APP-HOLD scan, tranche-manifest, conflict-marker, run-record-leak and receipt validators. | COMPLETE for this worktree candidate; CI and independent review belong to the parent's PR. |
| R1 — records | Receipt, MEMORY rows, App tranche manifest, `loop/LOOP_RECEIPTS.md` notice-adoption pointer; revised for the owner's 2026-09-26 decision. | Receipt validator VALID after append; tranche-manifest validator exit 0. | COMPLETE |
| R2 — PR #960 review revision | App SPEC §4.3/§5.2, scaffold Register line, `status-writer.ts`, `transition.ts`, `deliverable-contracts.ts`, their tests, and these records. | Union Register line matches `materialize_local_dependencies.py`; D-GOV-49 split and D-GOV-50 `RECLASSIFY` restated; reserved or multi-line status fields, `;` in a ruling, empty rulings and the deliverable's own `_STATUS.md` as ruling are rejected; the reversal removes the Checking Approval SHA field; forward gates accept an optional ruling; `..`-prefixed names are not over-rejected; the new behavior tests fail against the prior source (negative control). | COMPLETE for this candidate; checks in the receipt |
| F1 — integration | Parent session. | Fresh independent review of the frozen diff (product source needs the `software-code-review` path), required CI, merge. | PENDING (parent) |

## Implementation departures and limits

- Resumed after a container restart. The first pass had also admitted
  `ISSUED -> IN_PROGRESS` on any record under a `_ScopeChange/` directory. That
  evidence rule was not accepted anywhere: the `scope-change` workflow defines no
  record or checkpoint state that authorizes reopening an issued deliverable, and
  Root `write_status.sh` hard-blocks the move. The resumed pass removed it, per the
  dispatch brief's fallback. The validator, API and MCP tool reject
  `ISSUED -> IN_PROGRESS` as `BACKWARD_TRANSITION`, naming the scope-change
  process. The owner has since decided the authorizing record (E1): an ACCEPTED
  amendment (checkpoint group 3 accepted) whose accepted action register names
  the deliverable with action `MODIFY`, or `RECLASSIFY` where the
  reclassification changes the deliverable's scope (D-GOV-50). App SPEC §4.3
  states it. The tools keep
  refusing the move until an amendment-record check is implemented (FU1).
- The reversal requires a HUMAN/USER/OPERATOR actor, a format-valid
  `approvalSha` and a `ruling`: the same human-gate evidence as entry to
  `CHECKING`/`ISSUED`, plus the ruling `write_status.sh` requires. The API checks
  that the ruling resolves to a non-empty regular file inside `projectRoot`,
  including after symlinks are resolved, that is not the deliverable's own
  `_STATUS.md`; the reference may not contain brackets, semicolons or control
  characters. The history line records the project-relative ruling and SHA, and
  the reversal removes the `**Checking Approval SHA:**` field (`write_status.sh`
  leaves it as history). `IN_PROGRESS -> CHECKING` and `CHECKING -> ISSUED`
  accept an optional ruling under the same checks, as `write_status.sh` does, and
  record it in history; a ruling supplied to any other transition is denied. To
  reverse this, remove the rule and the ruling checks.
- Status-field writes reject reserved labels (Current State, Last Updated,
  History, in any normalized form), keys containing `*`, `#`, `:` or control
  characters, and values containing newlines or control characters, so metadata
  cannot forge the lifecycle state or history.
- Known limit (owner decision E2): unlike `write_status.sh`, this layer has no
  Git access, so it does not check that the ruling is committed or that the SHA
  is a reachable commit; the existing CHECKING/ISSUED gates have the same limit.
  The actor is caller-asserted, and any caller able to write files in the
  project can satisfy the checks; App SPEC §4.3 states this.
  `APP_HOLD_REGISTER.csv` cannot carry it: `app_hold.py` admits only
  `HOLD`/`STRUCTURAL_BOOTSTRAP`/`SOW_INITIALIZATION` rows, and a `HOLD` row must
  mirror a scanned held contract and would hold DEL-07-04. The register is
  unchanged; the limit is recorded in the receipt, here and in DEL-07-04 MEMORY.
- REQ-005's live limit (P-07/P-14) is unchanged. A caller-supplied
  HUMAN/USER/OPERATOR string, a format-valid SHA and a ruling path do not prove
  a human act. This applies to the reversal as it already did to `CHECKING` and
  `ISSUED`; an agent that can supply all three through the MCP tool can reach
  the reversal exactly as it can reach those gates.
- The workbench and pipeline transition forms still offer forward targets only
  (`nextLifecycleTargets`) and have no ruling input. Adding one is UI work that
  needs D-APP-36 render evidence.
- The Runtime-owned descriptor for `status_transition`
  (`projects/chirality-runtime/packages/contracts/src/harness/tool-descriptor.ts`)
  does not list `ruling`, and its human-gate text still names only
  CHECKING/ISSUED. Its schema does not forbid the extra property. This run did
  not edit it.
- Authority-corpus: the App SPEC was already drifting from corpus v25, and so
  were DIRECTIVE and the D-GOV-47 `software-decomp` files. After this change
  `status` still reports the same five drifting refs. As in Receipt 262, the
  drift is retained for owner-directed reconciliation. It is not repinned here.
- DEL-07-04 ScopeOfWork CLM-003/CLM-008 still list "reversal" among open
  candidate-bound checks. The requirement text is unchanged. Updating those
  verification-state sentences is left to the undertaking's bounded closeout.
- `loop/LOOP_RECEIPTS.md` gains one notice-adoption pointer at the dispatch
  brief's direction. Since `NOTICE_2026-09-23_CENTRAL_LOOP_RECEIPTS.md`, LOOP_INIT
  §5 places the undertaking receipt in `AgentRuns/<RunID>/RECEIPT.md`; the ledger
  entry only points there.

## App-loop follow-ups (FU1–FU4 owner decision E4, FU5–FU6 from the R2 review; not implemented here)

| ID | Follow-up | Home |
|---|---|---|
| FU1 | Status tools check the amendment record (ACCEPTED, checkpoint group 3, action register names the deliverable with `MODIFY` or scope-changing `RECLASSIFY`) before admitting `ISSUED -> IN_PROGRESS`. | DEL-07-04 REQ-004 |
| FU2 | The Runtime `status_transition` descriptor lists `ruling` and names the reversal gate. | DEL-07-04 MCP surface; Runtime-owned descriptor |
| FU3 | Workbench and pipeline transition forms gain a reversal input, with D-APP-36 render evidence. | DEL-07-04 UI consumers |
| FU4 | DEL-07-04 SOW verification sentences (CLM-003/CLM-008) updated at the bounded closeout. | Undertaking closeout |
| FU5 | App dependency reads compute blockers from the recorded register (the union of the declared sections and `Dependencies.csv`); today they are CSV-only register evidence. | App dependency read surfaces |
| FU6 | Decide when the App's bundled `dependency-extract`, `project-setup` and `review` workflows pick up the dependency follow-up revision. | App loop |
