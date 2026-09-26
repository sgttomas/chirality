# change — contract

## Non-negotiable invariants

- **Human owns reserved decisions.** Agents act within existing authorization and bring reserved decisions to the human with a concrete proposal.
- **No invention.** Do not claim a file change, commit, push, check result, review, or merge exists unless supported by evidence (Git output, check output, or explicit file contents).
- **Preserve unrelated work.** Stage only the intended change. Never discard, overwrite, or reformat another contributor's pending work to make the change fit.
- **Disjoint write scopes are the default concurrency control.** When agents hold non-overlapping write scopes in a shared checkout and commit frequently, preserve the shared checkout. Do not introduce worktrees merely because work is concurrent.
- **Worktrees are explicit isolation lanes.** Use branch + worktree lanes when the human asks, or when isolation materially reduces risk (overlapping write scopes, concurrent edits to instruction or governance files, risky refactors, long-lived or speculative work, generated-output churn, tool or process interference).
- **Branches are candidate work, not accepted truth.** A branch, commit, push, pull request, or merge concerns Git state. None of them accepts governed content or releases a product; that remains with the owning workflow and the applicable human decision.
- **Authorization is actual, not assumed.** Git authority comes from the user or the repository's instructions, bounded by host permissions. Selecting this workflow adds none (see Authorization and closeout).
- **Undertaking scope.** Selecting the change workflow supplies Git and file-state methods within the accepted undertaking. It does not itself authorize unrelated workflow or tool changes. HELPS_HUMANS helps design those components; WORKING_ITEMS implements authorized designs through bounded TASK work and integrates their evidence.
- **Minimize noise.** Default output is decision-ready, not verbose.
- **Workflow and undertaking ownership.** WORKING_ITEMS applies project-setup, dependency review, reconciliation, and change methods as selected by the undertaking. It retains that undertaking's ownership across workflow changes and routes separately owned work to the responsible instance or loop. Substantive acceptance remains with the applicable workflow and human decision.

---

## Repository conventions

This method is repository-agnostic. Before acting, look for the repository's
own change conventions: a project `AGENTS.md` or equivalent instruction file,
a project-scoped change skill, contributor documentation, branch protection,
and required CI. Where they exist they specialize this method's defaults for:

- the integration branch and branch naming;
- when to use a worktree lane and which paths are high-risk for overlap;
- the checks, review, and review independence required before merge;
- the merge strategy and the pull-request record;
- any standing Git authorization and its conditions;
- downstream notices when the change affects other consumers.

For example, a repository may carry a project-scoped skill (the Chirality
repository's `chirality-change` is one) that names its branch prefix, its
standing merge authorization, and its notice rules. Apply the specialization
and name it in the State Report. A convention may narrow or extend the defaults
below; it cannot weaken the invariants above. A convention or grant belonging to
one repository never applies to another.

---

## Inputs (optional)

All inputs are optional; defaults are safe. If an input is omitted, proceed
with the safe default and state the assumption in the State Report. Common
controls include session label and scope, the comparison ref and path focus,
how far closeout may proceed (inspect only, prepare, commit, push, pull
request, merge), the integration branch and base ref for new lanes, a branch
prefix, requested worktree lanes, merge strategy, and an optional session-log
path under `{EXECUTION_ROOT}/_Change/` (the project's execution root, when it
has one).

Defaults, each overridden by the repository's conventions or the user:

- session label `WORKING_ITEMS`; whole-repository scope;
- the repository's default branch as integration branch;
- no branch prefix; a short descriptive branch name;
- merge strategy per the repository's settings, otherwise a no-fast-forward
  merge that preserves the lane's history;
- low verbosity;
- closeout limited to what is authorized: local commits when closeout is
  requested; no push, pull request, or merge without actual authorization.

Details of assembling these are ordinary competence and left to agent judgment.

---

## Authorization and closeout

Default posture: when neither the user nor the repository's instructions grant
it, do not push, open or update a pull request, or merge. Commit locally when
the user requests closeout or the repository makes committing the normal
terminal action; otherwise leave the change uncommitted and say so. State the
authorization basis you relied on, or its absence, in the State Report.

Authorization may come from the user's request in the session or from a
standing grant in the repository's instructions. Apply a standing grant only
within its stated scope and conditions (for example, required CI passing and
independent review of the actual candidate). Explicit holds and later
directions from the user or repository owner prevail. Use the user's
configured Git identity and credentials, keep authorship and agent attribution
truthful, and do not describe agent review as the owner's personal review.
Host permissions, approval policy, and sandbox bound every operation; a stated
authorization never grants access the host did not provide.

Actions that discard work, overwrite remote state (such as a force push), change
repository protections or permissions, or rewrite published history need
separate explicit authorization even under a standing grant. No special
approval-token syntax is required. Git integration never substitutes for a
required human decision about governed content or product release.

---

## Coordination rules (handoffs)

- **WORKING_ITEMS (workflow: project-setup) (project setup).** Treat setup requirements (baseline structure, renames, approved bulk edits) as inputs. Routine validated closeout follows the authorization in this contract; new setup edits still require an explicit request or authorization.
- **WORKING_ITEMS (audit / dependency governance).** Implement human-approved remediation from structural, dependency, epistemic, governance, or coherence findings. Do not reinterpret findings; report what changed.
- **WORKING_ITEMS (workflow: reconciliation) (deliverable-corpus concordance).** Implement authorized concordance repairs (references, headings, IDs, alignment to approved rulings). Do not reinterpret governance; report what changed.
- **Parallel agents / worktree lanes.** First check whether existing scope discipline (bounded tasks, frequent commits, disjoint writable paths) suffices to stay in the shared checkout; propose isolated `{worktree path} + {branch}` lanes only when isolation is requested or warranted. Warn when two lanes overlap on high-risk paths (instruction and role files, workflow or skill libraries, governance documents, accepted snapshots, generated derivative outputs, shared coordination roots, and any paths the repository's conventions name). Overlap is a risk requiring human awareness and later integration review, not an automatic prohibition.
- **Integration coordinator.** Inspect the source lane and integration branch, required check verdicts, review, and applicable governed handoff state. Merge only under actual authorization and its conditions, verifying the source HEAD at merge and recording the pull-request, source, and merge identities in the ordinary closeout record. Reassess affected checks when the candidate changes; a passing rerun does not show that a known defect was repaired. Do not infer semantic acceptance from integration, and do not chain a merge behind a watch command without inspecting its final verdicts.

---

## Validity

A WORKING_ITEMS session is valid when:
- It produces a decision-ready State Report separating observations, interpretations, and options, and states the authorization basis and conventions applied.
- It carries closeout to the furthest authorized step when invoked by an owning-workflow handoff or direct human request, and names any remaining step and the authority it needs.
- It executes state-changing actions only within existing authorization and host permissions, and reports the actions and results truthfully.
- Any concurrent-work setup either confirms disjoint shared-checkout write scopes or proposes isolated branch/worktree lanes when isolation is warranted.
- Any merge satisfies the applicable authorization and its candidate conditions, and the existing pull request or closeout record identifies the checks, review, and source and merge revisions.
- Workflow or tool changes have an explicit design basis and implementation scope. Git closeout records their validation and owning undertaking without treating workflow selection as additional authorization.

---

## STRUCTURE — State Report (chat output)

The State Report is a chat deliverable, not a fixed template; include only the sections the situation needs. It must, at minimum, separate:

- **Identity** — repository, branch, HEAD, upstream; the conventions and authorization basis applied.
- **Change inventory** — staged / unstaged / untracked; renames/deletions; and, when relevant, concurrency/worktree-lane status and any path-overlap risks.
- **Observations** — facts drawn from Git output, check output, and file contents.
- **Interpretations** — what the state likely signifies.
- **Risks** — scope drift, accidental artifacts, divergence, stale derivative outputs.
- **Next actions** — the concrete actions or decisions needed for this state.

When merging, summarize candidate readiness, review, checks, remaining limits, and source/merge revisions in the existing pull request or closeout record. Do not create a separate readiness report or approval receipt merely to repeat this information.

When an action falls outside existing authorization, identify that action and the missing authority. Covered Git operations require no additional confirmation or approval token.

---
