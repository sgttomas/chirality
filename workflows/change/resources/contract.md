# change — contract

## Non-negotiable invariants

- **Human owns decisions.** WORKING_ITEMS proposes; the human decides.
- **No invention.** Do not claim a file change exists unless supported by evidence (git output and/or explicit file contents).
- **Disjoint write scopes are the default concurrency control.** When agents hold non-overlapping write scopes inside the monorepo and commit frequently, preserve the shared checkout. Do not introduce worktrees merely because work is concurrent.
- **Worktrees are explicit isolation lanes.** Use branch + worktree lanes when the human asks, or when isolation materially reduces risk (overlapping write scopes, concurrent root governance edits, risky refactors, long-lived/speculative work, generated-output churn, tool/process interference).
- **`main` is the default integration branch.** Unless the human names another, treat `main` as accepted integrated state and branch task work from it.
- **Branches are candidate work, not accepted truth.** A task branch/worktree does not make governed state closed. Governed acceptance still requires the owning workflow's snapshots, handoff state, closure verdict, derivative-package status, and audit/validation records.
- **No silent integration.** Do not merge a task branch into the integration branch until WORKING_ITEMS has reported readiness risks and merge execution is authorized: per-merge human approval of the exact merge action is the standing default, and beyond that default the owner may direct merge execution — typed by the owner directly or executed by an agent as the owner's proxy, identical authority either way — with the direction recorded in the loop's ordinary closeout evidence per `docs/PRD_ROOT.md` annex §5.3.1. Merges are never routine closeout. Each loop's stricter local merge discipline remains controlling until that loop adopts or acknowledges the policy under its own instruments.
- **Undertaking scope.** Selecting the change workflow supplies Git/file-state methods within the accepted undertaking. It does not itself authorize unrelated workflow or tool changes. HELPS_HUMANS helps design those components; WORKING_ITEMS implements authorized designs through bounded TASK work and integrates their evidence.
- **Minimize noise.** Default output is decision-ready, not verbose.
- **Workflow and undertaking ownership.** WORKING_ITEMS applies project-setup, dependency review, reconciliation, and change methods as selected by the undertaking. It retains that undertaking’s ownership across workflow changes and routes separately owned work to the responsible instance or loop. Substantive acceptance remains with the applicable workflow and human decision.

---

## Inputs (optional)

All inputs are optional; defaults are safe. If an input is omitted, proceed with the safe default and state the assumption in the State Report. Common controls include session label and scope, the comparison ref and path focus, whether execution is permitted, the integration branch and base ref for new lanes, requested worktree lanes, merge strategy, and an optional session-log path under `{EXECUTION_ROOT}/_Change/`. Sensible defaults: session label `WORKING_ITEMS`, whole-repo scope, `main` as integration branch, `codex/` branch prefix, no-fast-forward merge, low verbosity, execution disabled until approved (routine closeout excepted). Details of assembling these are ordinary competence and left to agent judgment.

---

## Approval and closeout gates

### Routine closeout (commit and push by default)
WORKING_ITEMS commits and pushes as a matter of course when **all** of the following hold:

- WORKING_ITEMS is invoked by an owning-workflow handoff, a project-local closeout rule, or a direct human request for final Git closeout.
- The tranche has a named objective, bounded scope, and recorded validation (or an explicit skipped-check rationale).
- Changed files can be separated from unrelated dirty files, and the commit can stage only tranche-scoped paths.
- The current branch has an upstream, or a project-local rule names the push target.
- The action is an ordinary scoped `git add`, `git commit`, and `git push` of the current branch — no merge, rebase, reset, force push, cleanup, or history rewrite.

When these hold, WORKING_ITEMS does not ask for an `APPROVE:` token; it performs the closeout, then reports commit SHA, push target, remaining dirty files, and validation evidence. **If any condition fails, WORKING_ITEMS stops with a State Report naming the blocker and the smallest approval or ruling needed.**

Clean-basis branch and worktree-lane creation is also routine WORKING_ITEMS
execution. Creating a task branch, and when warranted its worktree lane, from
a verified clean exact basis on the integration branch requires no `APPROVE:`
token when status is clean, no Git operation is in progress, and the base SHA
is recorded. WORKING_ITEMS reports the branch or lane name and base SHA and proceeds.
Basing a lane on a dirty worktree, or any switch that would discard or carry
uncommitted work, remains non-routine and requires the applicable approval
gate. This exception grants no routine authority for merge, rebase, reset,
force push, cleanup, history rewrite, or any other state-changing action.

### Approval token (required for non-routine execution)
WORKING_ITEMS executes non-routine state-changing actions only after a human message containing `APPROVE:` followed by an explicit action list (e.g. `APPROVE: apply patch to Docs/Spec.md; git add -A; git commit -m "..."`, or `APPROVE: merge codex/domain-kty into main with --no-ff`). A bare "yes" without an explicit `APPROVE:` list is insufficient for a non-routine action; request the token. For merge execution alone, an owner direction to merge — given by the owner directly or executed by an agent as the owner's proxy — is sufficient for the exact merge it names; record the direction in the loop's ordinary closeout evidence per PRD annex §5.3.1. This token is not required for routine validated closeout.

### Heightened approval (destructive / irreversible actions)
For any action that can discard work, rewrite history, or overwrite remote state, WORKING_ITEMS MUST (1) restate the risk in one sentence and (2) require `APPROVE_DESTRUCTIVE:` followed by the explicit action list. Destructive actions include (non-exhaustive): `git reset --hard`, `git push --force` / `--force-with-lease`, `git clean -fd`, rebases/amends on shared branches, deleting branches or removing dirty/unmerged worktrees, and aborting an in-progress merge/rebase when it would discard manual conflict-resolution work.

---

## Coordination rules (handoffs)

- **WORKING_ITEMS (workflow: project-setup) (project setup).** Treat setup requirements (baseline structure, renames, approved bulk edits) as inputs. Routine validated closeout follows the closeout gate; new setup edits still require explicit request or approval.
- **WORKING_ITEMS (audit / dependency governance).** Implement human-approved remediation from structural, dependency, epistemic, governance, or coherence findings. Do not reinterpret findings; report what changed.
- **WORKING_ITEMS (workflow: reconciliation) (deliverable-corpus concordance).** Implement authorized concordance repairs (references, headings, IDs, alignment to approved rulings). Do not reinterpret governance; report what changed.
- **Parallel agents / worktree lanes.** First check whether existing scope discipline (bounded tasks, frequent commits, disjoint writable paths) suffices to stay in the shared checkout; propose isolated `{worktree path} + {branch}` lanes only when isolation is requested or warranted. Warn when two lanes overlap on high-risk paths (`agents/`, `workflows/`, governance docs, accepted snapshots, generated derivative packages, shared control roots); overlap is a risk requiring human awareness and later integration review, not an automatic prohibition.
- **Integration coordinator.** Inspect the source lane and integration branch before merge. Verify the source lane identifies its accepted upstream snapshot(s), derivative-package status, closure verdict, rerun requirements, and remaining blockers when it changes governed state. Never decide substantive governance acceptance; if closure evidence is missing or contradictory, report the blocker and ask which owning workflow must close it. Execute a merge only under the non-routine Approval Gate (the standing default) or an owner direction to merge recorded in the loop's ordinary closeout evidence per PRD annex §5.3.1; in either case verify the approved source SHA and record the approved source HEAD, the owner's direction (or per-merge approval), and the effective merge SHA in the closeout evidence. Before executing any merge, inspect the source branch's check verdicts explicitly (a completed checks listing showing pass/fail per check); never chain a merge behind a watch command whose final verdicts were not read.

---

## Validity

A WORKING_ITEMS session is valid when:
- It produces a decision-ready State Report separating observations, interpretations, and options.
- It treats routine validated commit/push closeout as the normal terminal action when invoked by an owning-workflow handoff or direct human request.
- It does not execute non-routine state-changing actions unless the Approval Gate is satisfied, and it lists any executed actions exactly with reported results.
- Any concurrent-work setup either confirms disjoint shared-monorepo write scopes or proposes isolated branch/worktree lanes when isolation is warranted.
- Any integration merge is preceded by an Integration Readiness Report naming the source branch, approved source SHA, integration branch, closure/handoff status, derivative-package status when relevant, and remaining risks — and executes only the approved SHA and strategy, under per-merge human approval by default or an owner direction to merge recorded per PRD annex §5.3.1, leaving the approved source HEAD, the authorizing act, and the effective merge SHA observable in the closeout evidence.
- Workflow or tool changes have an explicit design basis and implementation scope. Git closeout records their validation and owning undertaking without treating workflow selection as additional authorization.

---

## STRUCTURE — State Report (chat output)

The State Report is a chat deliverable, not a fixed template; include only the sections the situation needs. It must, at minimum, separate:

- **Identity** — repo, branch, HEAD, upstream.
- **Change inventory** — staged / unstaged / untracked; renames/deletions; and, when relevant, concurrency/worktree-lane status and any path-overlap risks.
- **Observations** — facts drawn from git output and file contents.
- **Interpretations** — what the state likely signifies.
- **Risks** — scope drift, accidental artifacts, divergence, stale derivative packages.
- **Next actions** — the concrete actions or decisions needed for this state.

When merging, add an **Integration Readiness** section: source branch/worktree, source HEAD approved for merge, integration branch, changed paths, closure/handoff evidence, derivative-package status, validation/audit status, the authorizing act (per-merge human approval, or the owner's direction to merge recorded in the loop's ordinary closeout evidence per PRD annex §5.3.1), and a `READY` / `CONDITIONAL` / `BLOCKED` verdict.

When execution is requested, state the exact actions/commands, their risks, and which approval token is required.

---
