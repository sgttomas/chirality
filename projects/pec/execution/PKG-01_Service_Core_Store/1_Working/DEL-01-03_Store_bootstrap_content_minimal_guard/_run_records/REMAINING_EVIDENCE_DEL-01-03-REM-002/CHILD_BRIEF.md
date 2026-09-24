# CHILD BRIEF — DEL-01-03-REM-002 read-only evidence inquiry (TASK author)

- Parent: WORKING_ITEMS manager for the PEC loop. HELP_HUMAN (Agent 0)
  dispatched that manager under D-PEC-86 §3 I-4. Roles are asserted by
  instruction, not enforced.
- Reasoning effort: high. **Do not use the Agent tool and do not delegate.**
  Do this work yourself.
- REPO_ROOT: `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5`.
  WORKING_ROOT: `REPO_ROOT/projects/pec`. Use absolute paths in every command.
  The basis is HEAD `d61981ee2b9e36c82c6cdd28d4f3c12d3d32a69b`.
- DELIVERABLE: `WORKING_ROOT/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/`

## Objective

Carry out `DEL-01-03-REM-002` exactly as `_STATUS.md` words it: "Inspect and
map existing source-state-bound evidence for single-boundary content-minimal guard behavior, admitted field classes, located rejection, no silent loss and uniform ingest. Cover the exact
linked claims; distinguish observed implementation, bounded local absence,
missing/unmapped evidence, finite method execution and historical acceptance.
Retain UNKNOWN where evidence is unavailable and return exact unresolved
obligations for owner disposition." This is a read-only inquiry that produces
a derivative evidence report. It is not a contract, an implementation, a test,
a measurement run, an acceptance, or a lifecycle or production act.

Exact linked claims, from the D83 `PROPOSED_ITEMS.csv` and
`CLAIM_TO_PROPOSAL_MAP.json`: DEL-01-03::OUT-002; REQ-003; REQ-004; REQ-005; REQ-006; AC-003; AC-004; AC-005; AC-006; VER-003; VER-004; VER-005; VER-006 (13 claims).

Points to cover:
- Whether there is one ingest boundary, and whether any write path bypasses the guard (REQ-003, AC-003, VER-003). Inspect every persistence call and every write the adapter makes, including schema creation, delete and reset. Say exactly which writes are record writes and which are lifecycle writes, and what evidence shows the guard cannot be bypassed.
- The admitted field classes and the rejection of file content, diff content and register-row prose, with no residue left in the store (REQ-004, AC-004, VER-004). Note which fixtures exist. Note whether a full dump of persisted fields is made. Note what "no residue" is tested against.
- Located rejection, and the accounting that proves no record is silently lost (REQ-005, AC-005, VER-005). REQ-005 also refers to PEC-ORI-006 feed-limitation statements; record whether any feed-level evidence exists or whether that part stays UNKNOWN.
- Uniform ingest across the reconciler, presence and event ingest paths (REQ-006, AC-006, VER-006). The fixtures are test-local stand-ins and no real P1 or P3 ingest paths exist. Record that as a bounded local absence, and keep "by construction" reasoning apart from executing evidence.
- CON-001, REQ-009, AC-009 and VER-008 belong to HELD item REM-004 and are **out of scope**. Mention them only where an in-scope claim depends on them.

## Write boundary (exact)

You may write **only** inside
`WORKING_ROOT/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_run_records/REMAINING_EVIDENCE_DEL-01-03-REM-002/`, and
only these new files:

- `REPORT.md`, the derivative evidence report.
- `EVIDENCE_MANIFEST.json`, the evidence manifest.
- `STORAGE_SUITE_OBSERVATION.json`, optional. Include it only if you run the
  suite.

Do not modify `CHILD_BRIEF.md`, `PREFLIGHT_RELIANCE_HOLD.json` or
`MANAGER_LOG.md`. Do not write anywhere else: not `_STATUS.md`,
`ScopeOfWork.md`, `MEMORY.md`, sources, tests, `software-workflow.json`, git
state, or any other item's folder. Do not stage or commit anything.

## Read set

Read-only. Follow citations inside `projects/pec` as needed, and list every
file you relied on in the manifest.

- The deliverable's `ScopeOfWork.md`, `_STATUS.md`, `MEMORY.md`, `_CONTEXT.md`,
  `Dependencies.csv` and `_DEPENDENCIES.md`, and `_run_records/P1_STORE_GUARD_01/**`.
- `execution/_Coordination/D85_EXECUTION_2026-09-08/**` and
  `execution/_Coordination/D85_PRODUCTION_CLOSEOUT_2026-09-08/**`.
- `v2/src/pec_v2/core/ports/store.py`, `v2/src/pec_v2/core/content_minimal_guard.py`,
  `v2/src/pec_v2/adapters/storage/**`, `v2/tests/storage/**` and
  `v2/docs/STORE_LIFECYCLE_AND_GUARD.md`.
- `software-workflow.json`.
- The DEL-10-02 folder:
  `execution/PKG-10*/1_Working/DEL-10-02_Kill_test_standing_release_gate/`.
- The D83 baseline for your claim IDs:
  `execution/_Reconciliation/DeliverableConcordance/PEC_REMAINING_CONCORDANCE_2026-09-05/R1_R4_2026-09-05/SYNTHESIS/APPLICATION_PREPARATION/FULL_01/{PROPOSED_ITEMS.csv,CLAIM_TO_PROPOSAL_MAP.json,build_full_preparation.py}`
  and `.../SYNTHESIS/FULL_02/CONSOLIDATED_CLAIMS.csv`. This is historical
  baseline only.
- PRD passages that the linked claims cite (`docs/PRD.md`: PEC-K-10, PEC-SVC-005, PEC-ORI-006, PEC-RCN-002, PEC-PRS-002, PEC-STR-001, §7.1, §7.2). Read them by locator only.
- This folder's `PREFLIGHT_RELIANCE_HOLD.json`. The manager's reliance
  preflight returned ALLOW. Copy its JSON into your manifest.

### Optional suite observation

You may run the registered storage suite once, read-only, to observe executing
tests. From WORKING_ROOT:

`PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s v2/tests/storage -p 'test_*.py' -v`

Record in `STORAGE_SUITE_OBSERVATION.json`: the exact command, cwd, `python3
--version`, UTC time, HEAD, each test ID with its result, the totals and the
exit code. Record no other output. This observation is not a new measurement,
acceptance or VER-discharge claim, and must be labelled that way. Run no other
command that writes files. After the run, confirm that `git status --short`
shows nothing new outside your folder.

## Evidence classes (use exactly these labels)

| Label | Meaning |
|---|---|
| `OBSERVED_IMPLEMENTATION` | Source code at HEAD that you inspected implements the behavior, cited by path:line. |
| `BOUNDED_LOCAL_ABSENCE` | You searched a stated finite scope with a stated method, and the thing is absent there. State the scope and the method. A search miss shows absence only within that scope. |
| `MISSING_OR_UNMAPPED` | The claim requires evidence that you cannot locate or cannot map to the claim. |
| `FINITE_METHOD_EXECUTION` | A recorded or observed finite run, such as a D85 check record or your observation run, with its identity, date and result. The execution itself is not acceptance. |
| `HISTORICAL_ACCEPTANCE` | A recorded ruling or acceptance act, such as the D-PEC-85 ruling, a D85 fan-in, or a decomposition or SOW acceptance, with its exact scope. Say what that act did **not** accept. For example, D85 records no artifact acceptance, CHECKING, ISSUED or full DEL-01-03 acceptance. |
| `UNKNOWN` | Evidence is unavailable, and you draw no inference either way. |

## Discipline

- **Content-minimal.** Cite by repository-relative path, line range and file
  SHA-256 (`shasum -a 256`). Do not paste code, diffs, test bodies or long
  prose. Quote only identifiers (function, test, class, requirement IDs) and,
  where a claim needs it, a normative phrase of 20 words or fewer.
- **UNKNOWN.** Keep UNKNOWN wherever the evidence is not there. Never close a
  claim by inference. Never turn a search miss into "not implemented" beyond
  the bounded scope you searched. Never turn "a test exists" into "the
  criterion is accepted". Never present store-local delete/recreate as
  DEL-10-02 kill-test evidence.
- **No dispositions.** Do not say a Remaining item is satisfied, closed or
  complete. Your output is the obligations list, and the owner decides.
- Every line locator must reproduce at HEAD. Every hash must be the SHA-256 of
  the whole file as it is now in the worktree.

## REPORT.md structure

1. **Header.** Item ID, date 2026-09-23, HEAD, author role (TASK,
   instruction-asserted), your serving model if the host exposes it (otherwise
   "not exposed"), and parent (WORKING_ITEMS manager).
2. **Scope and linked claims.** Every claim ID, each with its SOW locator
   (`ScopeOfWork.md` line).
3. **Method (read-only).** What you read, searched and ran.
4. **Evidence table.** Columns: `Row | Claim | Evidence class | Observation
   (one line) | Source path:lines | SHA-256`. Give each claim at least one row.
   A claim may carry several classes.
5. **Per-claim summary.** One row per claim: the classes present, what is
   still missing, and the residual status (`EVIDENCED_PARTIAL`, `UNKNOWN`,
   `NO_LOCAL_EVIDENCE` and so on). Never use `SATISFIED`, `ACCEPTED` or
   `CLOSED`.
6. **UNKNOWN entries.** List each one explicitly, with what evidence would
   resolve it.
7. **Exact unresolved obligations for owner disposition.** Number them
   `O-2-1`, `O-2-2`, and so on. For each, give the claim(s), what is
   unresolved, and the kind of authority it would need, for example a
   production ruling, a separate measurement run, DEL-10-02, DEL-01-05, or
   owner acceptance.
8. **Limits.** What this inquiry did not do.

## EVIDENCE_MANIFEST.json

The manifest must contain:

- `item`, `date`, `head`, and `author_role`;
- `preflight`, a copy of `PREFLIGHT_RELIANCE_HOLD.json`;
- `linked_claims`;
- `sources`, a list of every file relied on, each as `{path, sha256}`;
- `evidence_rows`, one per table row, each as `{row, claim, class, path,
  lines, sha256}`;
- `class_counts`, which has two parts:
  - `rows_by_class`;
  - `claims_with_class`, the number of distinct claims carrying at least one
    row of that class;
- `unknowns`;
- `obligations`, each as `{id, claims, summary, authority_needed}`;
- `suite_observation`, a pointer to the observation file, or null;
- `report_sha256`. Compute it after `REPORT.md` is final.

## Return

Reply with a short note of no more than 250 words. Give the report and
manifest paths and their SHA-256 values, the class counts, the obligation
IDs, any deviation from this brief, and a confirmation that you wrote only
inside your folder.
